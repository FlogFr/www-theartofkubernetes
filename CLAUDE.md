# CLAUDE.md

Project memory for Claude Code. **Keep this file, `claude/rules/` and `claude/docs/`
up to date** whenever you change how the project works (see `claude/rules/workflow.md`).

## What this project is

`theartofkubernetes.com` is the marketing site of the book **The Art of Kubernetes –
French Edition** by Florian Grignon, sold as a Kindle ebook on Amazon.fr
(ASIN `B0DMHYT348`, 9,99 €). An English edition is being written.

The site has one business goal: **turn search traffic into Amazon sales**.
- Primary call to action: "Acheter sur Amazon" (amber button), everywhere.
- Secondary call to action: the newsletter (EmailOctopus), whose lead magnet is a free
  chapter sent by email.
- Acquisition: SEO on French Kubernetes searches (book page + articles).

## Stack

- [Pelican](https://getpelican.com) 4.9 static site generator, content in reStructuredText.
- Custom Jinja theme: `themes/theartofkubernetes/`.
- Tailwind CSS v4 (`npm run build:css`), compiled CSS **committed** so Pelican builds
  without Node.
- Hosting: GitHub Pages, `gh-pages` branch, custom domain via `content/extra/CNAME`.

## Commands

```bash
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
npm ci                      # only needed to rebuild the CSS
make devserver              # http://localhost:8000, rebuilds on change
make css                    # rebuild themes/theartofkubernetes/static/assets/css/site.css
make publish                # production build into output/
make check                  # SEO/integrity checks on output/ (must report 0 errors)
make images                 # regenerate optimized image derivatives
make github                 # publish + check + push to gh-pages (only when the user asks)
```

## Map

```
pelicanconf.py                 settings: URLs, BOOKS (price/ASIN), HOME_PAGES, Jinja filters
publishconf.py                 production overrides (SITEURL, feeds)
content/fr/*.rst               French articles   -> /fr/<slug>
content/pages/fr/*.rst         French pages      (home.rst -> /, articles.rst, bienvenue.rst)
content/drafts/                article ideas, never published
content/images/                content images (originals + optimized derivatives)
content/assets/                PDFs (article PDF versions, free chapter)
content/extra/                 CNAME, robots.txt, site.webmanifest, favicon.ico
themes/theartofkubernetes/
  templates/base.html          layout + SEO <head> (title, description, canonical, OG, hreflang)
  templates/home.html          landing layout + JSON-LD (Book/Product, FAQPage, Person)
  templates/home_fr.html       French landing page copy and data (FAQ, testimonials…)
  templates/article.html       article page + BlogPosting/Breadcrumb JSON-LD
  templates/partials/i18n.html UI strings per language
  templates/sitemap.html       /sitemap.xml
  src/site.css                 Tailwind source  -> static/assets/css/site.css
scripts/check_seo.py           SEO checker used by `make check`
scripts/make_images.py         image derivatives (never touches originals)
```

## Rules (always apply)

@claude/rules/workflow.md
@claude/rules/seo.md
@claude/rules/content.md
@claude/rules/design.md
@claude/rules/assets.md

## Documentation (read when relevant)

- `claude/docs/architecture.md`: how the build, templates, settings and URLs fit together.
- `claude/docs/development.md`: setup, commands, deployment, troubleshooting.
- `claude/docs/content-guide.md`: writing articles and pages (metadata, rst cheatsheet).
- `claude/docs/seo.md`: SEO strategy, keywords, what is implemented, Search Console.
- `claude/docs/i18n.md`: how to launch the English edition.
- `claude/docs/content-roadmap.md`: planned articles and target keywords.
- `claude/docs/decisions.md`: log of design decisions (update it when you make one).
