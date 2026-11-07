# Architecture

## Overview

```
content/ (rst) ──► Pelican + theme templates (Jinja) ──► output/ (static HTML) ──► gh-pages ──► GitHub Pages
                                  ▲
themes/theartofkubernetes/src/site.css ──► Tailwind CLI ──► static/assets/css/site.css (committed)
```

- Pelican 4.9 renders reStructuredText content with the Jinja theme
  `themes/theartofkubernetes/`. Configuration: `pelicanconf.py` (development) and
  `publishconf.py` (production, imports the former).
- Tailwind CSS v4 compiles `src/site.css` into `static/assets/css/site.css`. The output is
  committed, so building the site only needs Python.
- No Pelican plugin is used (`PLUGINS = []`): the sitemap is a theme template.

## Directory layout

```
content/
  fr/                      French articles (one .rst per article) -> /fr/<slug>
  pages/fr/                French pages: home.rst (/), articles.rst (/fr/articles),
                           bienvenue.rst (/fr/bienvenue, noindex)
  drafts/                  article ideas, excluded from the build (ARTICLE_EXCLUDES)
  images/                  content images: protected originals + optimized derivatives
  assets/                  PDFs (article PDF versions, free chapter)
  extra/                   files copied to the site root: CNAME, robots.txt,
                           site.webmanifest, favicon.ico
themes/theartofkubernetes/
  src/site.css             Tailwind source (fonts, tokens, components, prose styles)
  static/assets/css/       compiled CSS (site.css)
  static/assets/fonts/     self-hosted woff2 fonts (Crimson Pro, Libre Franklin)
  static/assets/images/    brand images (logos, mountains, author portrait, favicons)
  static/assets/js/site.js mobile menu toggle
  templates/               Jinja templates (see below)
  templates/icons/         Feather icons (inner SVG markup)
scripts/
  check_seo.py             SEO/integrity checker (`make check`)
  make_images.py           image derivatives (`make images`)
claude/rules/              instructions for Claude (imported by CLAUDE.md)
claude/docs/               project documentation (this folder)
```

## URL scheme

| Content                    | Source                         | Saved as                     | Canonical URL              |
| -------------------------- | ------------------------------ | ---------------------------- | -------------------------- |
| Home page (fr)             | `content/pages/fr/home.rst`    | `index.html`                 | `/`                        |
| Article                    | `content/<lang>/<file>.rst`    | `<lang>/<slug>.html`         | `/<lang>/<slug>`           |
| Page                       | `content/pages/<lang>/<f>.rst` | `<lang>/<slug>.html`         | `/<lang>/<slug>`           |
| 404                        | `templates/404.html`           | `404.html`                   | (noindex)                  |
| Sitemap                    | `templates/sitemap.html`       | `sitemap.xml`                |                            |
| Atom feed (publish only)   | Pelican                        | `feeds/all.atom.xml`         |                            |

GitHub Pages serves `fr/slug.html` for `/fr/slug`; the extensionless form is used
everywhere (links, canonical, sitemap). Tag, category, author and archive pages are
disabled (`*_SAVE_AS = ""`), as are drafts.

## Templates

| Template                     | Used for                                   | Notes |
| ---------------------------- | ------------------------------------------ | ----- |
| `base.html`                  | every HTML page                            | `<head>` SEO tags, header, footer, `french_typography` filter on `<main>` |
| `home.html`                  | landing layout (all languages)             | JSON-LD: WebSite, WebPage, Person, Book+Product, FAQPage |
| `home_fr.html`               | French landing page (`:template: home_fr`) | copy + data: `learn`, `audiences`, `chapters`, `testimonials`, `faq`, `book_description` |
| `article.html`               | articles                                   | JSON-LD: BlogPosting, BreadcrumbList; book CTA, author box, related articles, newsletter |
| `articles.html`              | article list page (`:template: articles`)  | JSON-LD: CollectionPage + ItemList |
| `page.html`                  | other pages (e.g. bienvenue)               | |
| `404.html`, `sitemap.html`   | direct templates                           | `DIRECT_TEMPLATES = ["404", "sitemap"]` |
| `partials/i18n.html`         | UI strings per language (`t.<key>`)        | add every key to all languages |
| `partials/macros.html`       | `icon`, `buy_button`, `stars`, `article_card` | |
| `partials/header.html`, `footer.html`, `newsletter.html`, `book-cta.html`, `jsonld-person.html` | shared blocks | |

### Variables contract of `base.html`

Child templates set these **before** `{% extends "base.html" %}`:

| Variable          | Meaning                                         | Default |
| ----------------- | ----------------------------------------------- | ------- |
| `obj`             | the Pelican article/page                        | none |
| `lang`            | language code                                   | `DEFAULT_LANG` |
| `seo_title`       | `<title>` and `og:title`                        | required |
| `seo_description` | meta description and `og:description`           | required |
| `canonical`       | absolute canonical URL                          | `SITEURL/obj.url` |
| `robots`          | robots meta                                     | `index, follow, max-image-preview:large` |
| `og_type`, `og_image`, `og_image_width/height/alt` | Open Graph    | website, `BOOKS[lang].og_image` (1200×630) |
| `has_newsletter`  | the page includes `partials/newsletter.html` (enables the "free chapter" link of the book CTA) | false |

`base.html` then defines for every template: `t` (UI strings), `book` (`BOOKS[lang]`),
`home_url` (`HOME_PAGES[lang]`), and imports the macros. hreflang links are generated
from `obj.translations` (plus `x-default` = default-language version).

## Settings (`pelicanconf.py`)

| Setting                 | Purpose |
| ----------------------- | ------- |
| `SITEURL`               | `http://localhost:8000` in development, production URL in `publishconf.py`. Used for absolute URLs only. |
| `BOOKS`                 | one entry per language edition: title, format, pages, price (`price` for schema.org, `price_display` for humans), currency, ASIN, store, Amazon `url`, `link_rel`, `cover`, `og_image`. |
| `AMAZON_ASSOCIATE_TAG`  | optional affiliate tag appended to Amazon URLs; switches links to `rel="noopener sponsored"`. |
| `HOME_PAGES`            | languages with a home page (`{"fr": "/"}`), drives the language switcher. |
| `AUTHOR_PROFILES`       | author's public profile URLs → schema.org `sameAs`. Empty for now. |
| `CONTACT_EMAIL`         | contact address shown on the site. |
| `NEWSLETTER_FORM_ID`    | EmailOctopus form id embedded by `partials/newsletter.html`. |
| `BUILD_YEAR`            | copyright year in the footer. |
| `JINJA_FILTERS`         | `long_date(lang)`, `reading_time`, `responsive_images`, `french_typography(lang)`. |

## Jinja filters

- `long_date(date, lang)`: "9 septembre 2024" / "September 9, 2024" (no locale needed).
- `reading_time(html)`: minutes at 220 words/minute.
- `responsive_images(html)`: docutils writes image sizes as inline styles; the filter turns
  them into `width`/`height` attributes and adds `loading="lazy" decoding="async"`.
- `french_typography(html, lang)`: narrow no-break space before `: ; ! ?` and inside
  `« »` in French text (tags, `pre`, `code`, `script`, `style` untouched).

## Front-end

- CSS: Tailwind v4 with `@tailwindcss/typography`; `@source` limits scanning to
  `templates/` and `content/**/*.rst`. Custom components are `@utility` blocks.
- Fonts: Crimson Pro (headings) and Libre Franklin (body), variable woff2, latin subset,
  preloaded, copied from `@fontsource-variable/*` by `npm run fonts`.
- JS: `site.js` (mobile menu). The only third-party script is the EmailOctopus form.
