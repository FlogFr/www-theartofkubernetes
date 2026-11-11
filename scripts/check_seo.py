#!/usr/bin/env python3
"""SEO and integrity checks for the generated site.

Run after a production build:

    make publish && make check        # or: python3 scripts/check_seo.py output

Checks every HTML page of the output directory (theme assets excluded):
  - <html lang>, <title> (length), meta description (length), exactly one <h1>,
    no skipped heading level, canonical URL, Open Graph image, robots meta;
  - JSON-LD blocks are valid JSON; Product nodes have offers, review and an
    aggregateRating that matches the reviews (Search Console "Product snippets");
  - every <img> has an alt attribute plus width and height;
  - internal links and #anchors point to existing pages/ids;
  - titles and descriptions are unique;
  - sitemap.xml lists exactly the indexable pages, robots.txt references it.

Errors make the script exit with status 1; warnings are informative.
Only the Python standard library is used.
"""

import json
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

SITE_URL = "https://theartofkubernetes.com"
TITLE_MAX = 65          # Google truncates around 60 characters / 600px
TITLE_MIN = 15
DESC_MIN = 70
DESC_MAX = 160


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.title = None
        self.meta = {}
        self.links = []          # (rel, href, hreflang)
        self.headings = []       # (level, text)
        self.images = []         # attrs dict
        self.anchors = []        # href values of <a>
        self.ids = set()
        self.jsonld = []
        self._in_title = False
        self._in_heading = None
        self._heading_text = []
        self._in_jsonld = False
        self._jsonld_text = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
            self.title = ""
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link":
            self.links.append((a.get("rel", ""), a.get("href", ""), a.get("hreflang")))
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._in_heading = int(tag[1])
            self._heading_text = []
        elif tag == "img":
            self.images.append(a)
        elif tag == "a" and "href" in a:
            self.anchors.append(a["href"])
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_jsonld = True
            self._jsonld_text = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif self._in_heading and tag == f"h{self._in_heading}":
            self.headings.append((self._in_heading, " ".join("".join(self._heading_text).split())))
            self._in_heading = None
        elif tag == "script" and self._in_jsonld:
            self.jsonld.append("".join(self._jsonld_text))
            self._in_jsonld = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_heading:
            self._heading_text.append(data)
        if self._in_jsonld:
            self._jsonld_text.append(data)


def jsonld_nodes(data):
    """Yield every JSON-LD object (top level, @graph items, nested values)."""
    if isinstance(data, list):
        for item in data:
            yield from jsonld_nodes(item)
    elif isinstance(data, dict):
        yield data
        for value in data.values():
            yield from jsonld_nodes(value)


def check_product(node, err):
    """Mirror the Search Console "Product snippets" report.

    Google needs one of offers/review/aggregateRating and flags as missing the ones
    that are absent, and flags several reviews without an aggregateRating. The
    aggregateRating must be computed from the reviews on the page, never invented.
    """
    name = node.get("name", "?")
    for field in ("offers", "review", "aggregateRating"):
        if field not in node:
            err(f'Product {name!r}: missing field "{field}"')
    reviews = node.get("review", [])
    reviews = reviews if isinstance(reviews, list) else [reviews]
    aggregate = node.get("aggregateRating")
    if not isinstance(aggregate, dict):
        return
    ratings = [float(r.get("reviewRating", {}).get("ratingValue", 0)) for r in reviews]
    count = aggregate.get("reviewCount", aggregate.get("ratingCount"))
    if count != len(reviews):
        err(f"Product {name!r}: aggregateRating count {count} != {len(reviews)} reviews")
    if ratings and abs(float(aggregate.get("ratingValue", 0)) - sum(ratings) / len(ratings)) > 0.05:
        err(f"Product {name!r}: aggregateRating ratingValue is not the mean of the reviews")


def url_to_file(output, path):
    """Map a URL path to the generated file, mimicking GitHub Pages."""
    path = unquote(path)
    if path.endswith("/"):
        candidates = [path + "index.html"]
    else:
        candidates = [path, path + ".html", path + "/index.html"]
    for c in candidates:
        f = output / c.lstrip("/")
        if f.is_file():
            return f
    return None


def file_to_url(output, f):
    rel = f.relative_to(output).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel[: -len(".html")]


def main():
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "output").resolve()
    if not (output / "index.html").is_file():
        sys.exit(f"No built site in {output}: run `make publish` first.")

    errors, warnings = [], []
    pages = {}
    for f in sorted(output.rglob("*.html")):
        if f.relative_to(output).parts[0] == "theme":
            continue
        p = PageParser()
        p.feed(f.read_text(encoding="utf-8"))
        pages[f] = p

    titles, descriptions = defaultdict(list), defaultdict(list)
    indexable = set()

    for f, p in pages.items():
        name = f.relative_to(output).as_posix()
        err = lambda msg: errors.append(f"{name}: {msg}")  # noqa: E731
        warn = lambda msg: warnings.append(f"{name}: {msg}")  # noqa: E731
        robots = p.meta.get("robots", "")
        is_indexable = "noindex" not in robots
        if is_indexable:
            indexable.add(file_to_url(output, f))

        if not p.lang:
            err("missing <html lang>")
        title = (p.title or "").strip()
        if not title:
            err("missing <title>")
        elif not TITLE_MIN <= len(title) <= TITLE_MAX:
            (err if len(title) > 70 else warn)(f"title is {len(title)} chars: {title!r}")
        desc = p.meta.get("description", "").strip()
        if not desc:
            err("missing meta description")
        elif not DESC_MIN <= len(desc) <= DESC_MAX:
            warn(f"meta description is {len(desc)} chars (aim for {DESC_MIN}-{DESC_MAX})")
        if is_indexable:
            titles[title].append(name)
            descriptions[desc].append(name)

        h1 = [h for h in p.headings if h[0] == 1]
        if len(h1) != 1:
            err(f"{len(h1)} <h1> (expected exactly 1)")
        previous = 0
        for level, text in p.headings:
            if level > previous + 1:
                err(f"heading level skipped: h{previous} -> h{level} ({text!r})")
            previous = level

        canonical = [href for rel, href, _ in p.links if rel == "canonical"]
        if is_indexable:
            if len(canonical) != 1:
                err("missing canonical link")
            elif not canonical[0].startswith(SITE_URL):
                err(f"canonical is not absolute on {SITE_URL}: {canonical[0]}")
            elif url_to_file(output, urlparse(canonical[0]).path) != f:
                err(f"canonical {canonical[0]} does not point to this page")
        og_image = p.meta.get("og:image", "")
        if not og_image.startswith(SITE_URL):
            err(f"og:image missing or not absolute: {og_image!r}")
        elif not url_to_file(output, urlparse(og_image).path):
            err(f"og:image file not found: {og_image}")

        for block in p.jsonld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as exc:
                err(f"invalid JSON-LD: {exc}")
                continue
            for node in jsonld_nodes(data):
                types = node.get("@type", [])
                if "Product" in (types if isinstance(types, list) else [types]):
                    check_product(node, err)

        for img in p.images:
            src = img.get("src", "?")
            if "alt" not in img:
                err(f"<img> without alt: {src}")
            if not (img.get("width") and img.get("height")):
                err(f"<img> without width/height (layout shift): {src}")
            if src.startswith("/") and not url_to_file(output, urlparse(src).path):
                err(f"image not found: {src}")

        for href in p.anchors:
            if href.startswith(SITE_URL):
                href = href[len(SITE_URL):] or "/"
            parsed = urlparse(href)
            if parsed.scheme or href.startswith("//"):
                continue  # external link or mailto:
            if href.startswith("#"):
                target, fragment = f, parsed.fragment
            else:
                target = url_to_file(output, parsed.path) if parsed.path else f
                fragment = parsed.fragment
                if target is None:
                    err(f"broken internal link: {href}")
                    continue
            if fragment and target in pages and fragment not in pages[target].ids:
                err(f"missing anchor #{fragment} in {target.relative_to(output)} (link {href})")

    for title, names in titles.items():
        if len(names) > 1:
            errors.append(f"duplicate title {title!r}: {', '.join(names)}")
    for desc, names in descriptions.items():
        if len(names) > 1:
            errors.append(f"duplicate description on: {', '.join(names)}")

    # Sitemap and robots.txt
    sitemap = output / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("sitemap.xml is missing")
    else:
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [e.text.strip() for e in ET.parse(sitemap).getroot().findall("s:url/s:loc", ns)]
        in_sitemap = set()
        for loc in locs:
            if not loc.startswith(SITE_URL):
                errors.append(f"sitemap: URL not on {SITE_URL}: {loc}")
                continue
            path = urlparse(loc).path or "/"
            if not url_to_file(output, path):
                errors.append(f"sitemap: URL without page: {loc}")
            in_sitemap.add(path)
        for url in sorted(indexable - in_sitemap - {"/404"}):
            errors.append(f"sitemap: indexable page missing: {url}")
        for url in sorted(in_sitemap - indexable):
            errors.append(f"sitemap: non-indexable page listed: {url}")
    robots_txt = output / "robots.txt"
    if not robots_txt.is_file() or "Sitemap:" not in robots_txt.read_text():
        errors.append("robots.txt is missing or does not reference the sitemap")

    for w in warnings:
        print(f"WARNING  {w}")
    for e in errors:
        print(f"ERROR    {e}")
    print(f"\n{len(pages)} pages checked: {len(errors)} error(s), {len(warnings)} warning(s).")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
