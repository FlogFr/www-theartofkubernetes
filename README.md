# theartofkubernetes.com

Website of the book **The Art of Kubernetes – French Edition** by Florian Grignon,
available on [Amazon.fr](https://www.amazon.fr/dp/B0DMHYT348).

Static site built with [Pelican](https://getpelican.com) and Tailwind CSS, hosted on
GitHub Pages.

## Quick start

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
make devserver          # http://localhost:8000
```

Rebuild the CSS after changing templates (needs Node.js): `npm ci && make css`.

Before deploying: `make publish && make check` (0 errors). Deploy: `make github`.

## Documentation

- [CLAUDE.md](CLAUDE.md): project overview and map (also read by Claude Code).
- [claude/docs/](claude/docs/): architecture, development, content guide, SEO, i18n,
  content roadmap, decision log.
- [claude/rules/](claude/rules/): rules followed when changing the site.

The book's illustrations are the property of the author: see
[claude/rules/assets.md](claude/rules/assets.md).
