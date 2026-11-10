"""Pelican settings for theartofkubernetes.com.

These are the base (development) settings. Production overrides live in
publishconf.py. The architecture is documented in claude/docs/architecture.md.
"""

import re
from datetime import datetime

AUTHOR = "Florian Grignon"
SITENAME = "The Art of Kubernetes"
# Base URL used to build absolute URLs (canonical, Open Graph, JSON-LD,
# sitemap, {filename} links). Development value: the local preview server
# (`make devserver`). publishconf.py sets the production URL.
SITEURL = "http://localhost:8000"

PATH = "content"
TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "fr"
THEME = "themes/theartofkubernetes"

# Plugins are disabled on purpose: the sitemap is rendered by the theme
# (templates/sitemap.html) so that its URLs match the canonical URLs.
PLUGINS = []

# --- URLs -------------------------------------------------------------------
# Every piece of content lives under its language prefix: /fr/<slug>, /en/<slug>.
# Files are saved as <slug>.html; GitHub Pages serves them without the
# extension, which is the canonical form used everywhere.
ARTICLE_URL = "{lang}/{slug}"
ARTICLE_SAVE_AS = "{lang}/{slug}.html"
ARTICLE_LANG_URL = ARTICLE_URL
ARTICLE_LANG_SAVE_AS = ARTICLE_SAVE_AS
PAGE_URL = "{lang}/{slug}"
PAGE_SAVE_AS = "{lang}/{slug}.html"
PAGE_LANG_URL = PAGE_URL
PAGE_LANG_SAVE_AS = PAGE_SAVE_AS

# Articles live in content/<lang>/, pages in content/pages/<lang>/.
# content/drafts/ holds article ideas and unfinished posts: never published.
ARTICLE_EXCLUDES = ["drafts"]
DRAFT_SAVE_AS = ""
DRAFT_LANG_SAVE_AS = ""
DRAFT_PAGE_SAVE_AS = ""
DRAFT_PAGE_LANG_SAVE_AS = ""

# Thin listing pages (tags, categories, authors, archives) hurt SEO more than
# they help on a small site: do not generate them.
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
YEAR_ARCHIVE_SAVE_AS = ""
MONTH_ARCHIVE_SAVE_AS = ""
DAY_ARCHIVE_SAVE_AS = ""

# The home page is a regular page (content/pages/fr/home.rst, saved as
# index.html) so that each language version can be linked with hreflang.
DIRECT_TEMPLATES = ["404", "sitemap"]
PAGINATED_TEMPLATES = {}
SITEMAP_SAVE_AS = "sitemap.xml"

# --- Static files -----------------------------------------------------------
STATIC_PATHS = ["images", "assets", "extra"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/site.webmanifest": {"path": "site.webmanifest"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

# --- Feeds (enabled in publishconf.py only) ---------------------------------
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Raw HTML in reStructuredText is allowed, but prefer plain rst (see
# claude/rules/content.md).
FORMATTED_FIELDS = []
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

# --- The book ---------------------------------------------------------------
# Optional Amazon Associates tag (e.g. "theartofk8s-21"). When set, it is
# appended to every Amazon link of the site.
AMAZON_ASSOCIATE_TAG = ""


def _amazon_url(domain, asin):
    url = f"https://www.{domain}/dp/{asin}"
    if AMAZON_ASSOCIATE_TAG:
        url += f"?tag={AMAZON_ASSOCIATE_TAG}"
    return url


# One entry per language edition of the book. Templates read BOOKS[lang].
# To announce the English edition, add an "en" entry (see claude/docs/i18n.md).
BOOKS = {
    "fr": {
        "title": "The Art of Kubernetes",
        "edition": "French Edition",
        "full_title": "The Art of Kubernetes - French Edition",
        "language": "fr",
        "format": "Kindle",
        "schema_format": "https://schema.org/EBook",
        "pages": 350,
        "price": "9.99",
        "price_display": "9,99 €",
        "currency": "EUR",
        "asin": "B0DMHYT348",
        "store": "Amazon.fr",
        # Country of the store: schema.org shipping destination / return policy.
        "country": "FR",
        # Return window of the store for this ebook, in days. None = not
        # declared in the structured data (hasMerchantReturnPolicy omitted).
        # Only set it to a value checked on the store's help pages.
        "return_days": None,
        "url": _amazon_url("amazon.fr", "B0DMHYT348"),
        # Affiliate links must be marked rel="sponsored" (Google guidelines).
        "link_rel": "noopener sponsored" if AMAZON_ASSOCIATE_TAG else "noopener",
        # Cover derivatives: -400.webp and -800.webp (scripts/make_images.py).
        "cover": "/images/the-art-of-kubernetes-couverture-800.webp",
        "og_image": "/images/og-the-art-of-kubernetes.jpg",
    },
}

CONTACT_EMAIL = "bonjour@theartofkubernetes.com"
# EmailOctopus form of the newsletter (the lead magnet: a free chapter).
# /fr/bienvenue is the "welcome" page for new subscribers (most likely the
# form's redirect URL): keep that URL stable.
NEWSLETTER_FORM_ID = "7f014dd2-69c3-11ef-b4cf-7d716c80cc13"
BUILD_YEAR = datetime.now().year

# Public profiles of the author (LinkedIn, GitHub, ...). They feed the
# schema.org "sameAs" property, which helps search engines identify the author.
AUTHOR_PROFILES = []

# Languages that have a home page, mapped to its path. Drives the language
# switcher of the header (shown when there are 2+ languages) and the links
# to the home page. Add "en": "/en/" when the English home page exists.
HOME_PAGES = {"fr": "/"}

# --- Jinja filters ----------------------------------------------------------
_MONTHS = {
    "fr": [
        "janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre",
    ],
    "en": [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December",
    ],
}


def long_date(value, lang="fr"):
    """Format a date as '9 septembre 2024' (fr) or 'September 9, 2024' (en)."""
    month = _MONTHS.get(lang, _MONTHS["en"])[value.month - 1]
    if lang == "fr":
        day = "1er" if value.day == 1 else str(value.day)
        return f"{day} {month} {value.year}"
    return f"{month} {value.day}, {value.year}"


def reading_time(html, words_per_minute=220):
    """Estimated reading time in minutes of an HTML fragment."""
    text = re.sub(r"<[^>]+>", " ", html or "")
    return max(1, round(len(text.split()) / words_per_minute))


def _fix_img(match):
    tag = match.group(0)
    size = re.search(r'\sstyle="width:\s*(\d+)px;\s*height:\s*(\d+)px;?"', tag)
    if size:
        tag = tag.replace(size.group(0), f' width="{size.group(1)}" height="{size.group(2)}"')
    if "loading=" not in tag:
        tag = tag.replace("<img ", '<img loading="lazy" decoding="async" ', 1)
    return tag


def responsive_images(html):
    """Post-process images rendered by docutils.

    docutils writes `:width:`/`:height:` as an inline style, which breaks
    responsive images. Turn them into width/height attributes (no layout
    shift, CSS keeps images fluid) and lazy-load every content image.
    """
    return re.sub(r"<img\b[^>]*>", _fix_img, html or "")


_TYPO_SKIP = re.compile(r"<(pre|code|script|style|textarea)\b.*?</\1>|<[^>]+>", re.S | re.I)
_NNBSP = "\u202f"  # narrow no-break space


def _typo_text(text):
    text = re.sub(r" ([:;!?»])", _NNBSP + r"\1", text)
    return re.sub(r"« ", "«" + _NNBSP, text)


def french_typography(html, lang="fr"):
    """French typography: no-break space before : ; ! ? » and after «.

    Prevents a line from starting with punctuation. Tags, attributes and
    pre/code/script/style blocks are left untouched.
    """
    if lang != "fr" or not html:
        return html
    out, pos = [], 0
    for match in _TYPO_SKIP.finditer(html):
        out.append(_typo_text(html[pos:match.start()]))
        out.append(match.group(0))
        pos = match.end()
    out.append(_typo_text(html[pos:]))
    return "".join(out)


JINJA_FILTERS = {
    "long_date": long_date,
    "reading_time": reading_time,
    "responsive_images": responsive_images,
    "french_typography": french_typography,
}
