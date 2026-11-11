# Development guide

## Requirements

- Python 3.11+ (Pelican 4.9, docutils, Pillow; see `requirements.txt`).
- Node.js 20+ and npm, only to rebuild the CSS or update the fonts.

## Setup

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
npm ci            # optional: Tailwind CLI + fonts
```

## Everyday commands

| Command            | What it does |
| ------------------ | ------------ |
| `make devserver`   | Build with `pelicanconf.py` and serve on http://localhost:8000, rebuilding on change. |
| `make html`        | One-off development build into `output/`. |
| `make css`         | Compile `themes/theartofkubernetes/src/site.css` → `static/assets/css/site.css` (minified). Run after changing templates or classes. |
| `npm run watch:css`| Same, in watch mode (run it next to `make devserver`). |
| `make publish`     | Production build (`publishconf.py`: production `SITEURL`, Atom feed). |
| `make check`       | `scripts/check_seo.py output`: SEO and integrity checks. Must report 0 errors. |
| `make images`      | `scripts/make_images.py`: regenerate optimized image derivatives. |
| `npm run fonts`    | Copy the woff2 fonts from `node_modules` into the theme. |
| `make github`      | `publish` + `check`, then push `output/` to the `gh-pages` branch (deployment). |

Typical change: edit content/templates → `make css` (if needed) → `make publish && make check`
→ look at the pages (`make devserver`) → commit (including `site.css`).

## Deployment

The site is hosted on **GitHub Pages** from the `gh-pages` branch of
`FlogFr/www-theartofkubernetes`, with the custom domain `theartofkubernetes.com`
(`content/extra/CNAME` is copied to the site root).

```bash
make github   # publish, check, ghp-import output/ to gh-pages, git push origin gh-pages
```

Deploy from what is on `main` (or about to be fast-forwarded to it, see
`claude/rules/workflow.md`): `main` must always hold the sources of the live site.

`make github` stops if `make check` fails. GitHub Pages:
- serves `/fr/slug` from `fr/slug.html` (extensionless canonical URLs);
- serves `404.html` for unknown URLs;
- caches files for about 10 minutes: CSS changes can take a few minutes to appear.

## Checking a page visually

Playwright and Chromium are available in Claude Code cloud sessions. Example:

```bash
make publish && pelican -l content -o output -s publishconf.py -p 8000 &
node -e "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:390,height:844}});await p.goto('http://localhost:8000/');
await p.screenshot({path:'home-mobile.png',fullPage:true});await b.close();})()"
```

Lazy-loaded images only appear in full-page screenshots after scrolling the page with
`page.mouse.wheel`. The EmailOctopus form needs network access to `eocampaign1.com`.

## Troubleshooting

- **A Tailwind class has no effect**: run `make css`; check that the class is written
  literally in a template or `.rst` file (no concatenation).
- **`sitemap.xml` is wrong or doubled**: make sure the `pelican-sitemap` plugin is not
  installed (`pip uninstall pelican-sitemap`); `PLUGINS = []` also disables it.
- **"Skipping … could not find information about 'date'"**: an `.rst` file outside
  `content/drafts/` lacks metadata. Move it to `drafts/` or complete it.
- **Links point to localhost**: you deployed a development build; use `make publish`.
- `tasks.py` (invoke) is the Pelican quickstart file and is not maintained; use the Makefile.
