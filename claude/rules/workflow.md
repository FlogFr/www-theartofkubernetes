# Workflow rules

## Languages

- Everything written for maintainers is in **English**: `CLAUDE.md`, `claude/rules/`,
  `claude/docs/`, code comments, commit messages, README.
- Site content is in **French** (`lang: fr`). English content will come with the English
  edition (see `claude/docs/i18n.md`). Talk to the user in the language they use.

## Definition of done for any change

1. If a template or a CSS class changed: `make css` and commit the regenerated
   `themes/theartofkubernetes/static/assets/css/site.css` in the same commit.
2. `make publish && make check` reports **0 errors**. Fix warnings when reasonable.
3. For visual changes: look at the affected pages at 1280px and 390px wide (Playwright
   screenshots, `make devserver` on port 8000). No horizontal scroll, buy button visible.
4. Documentation updated (see below).

## Keep the documentation in sync

Update the files in the same change when you:

| You changed…                                    | Update                                                |
| ----------------------------------------------- | ----------------------------------------------------- |
| a command, a script, a dependency               | `CLAUDE.md` (Commands), `claude/docs/development.md`  |
| a setting in `pelicanconf.py`                   | `claude/docs/architecture.md` (Settings)              |
| a template, a template variable, a page type    | `claude/docs/architecture.md`                         |
| a metadata field or an rst convention           | `claude/docs/content-guide.md`, `claude/rules/content.md` |
| SEO behaviour (meta, JSON-LD, sitemap, robots)  | `claude/docs/seo.md`, `claude/rules/seo.md`           |
| published or planned an article                 | `claude/docs/content-roadmap.md`                      |
| made a structural decision                      | `claude/docs/decisions.md` (dated entry)              |

## Git

- Work on the branch you were given, then update `main` with it once the change meets
  the definition of done: `git fetch origin main`, rebase the branch on `origin/main` if
  `main` has moved, then fast-forward `main` (`git push origin HEAD:main`).
  Never force-push `main`, never rewrite its history.
- `main` holds the sources of the live site: deploy only commits that are on `main`
  (or put them on `main` right after deploying), never uncommitted work.
- Never run `make github` (deployment) unless the user explicitly asks. Never push to
  `gh-pages` other than through `make github`.
- Never commit `output/`, `node_modules/` or virtualenvs.
- Small, focused commits with descriptive English messages.

## Ask the user before

- Changing anything commercial: price, format, edition, ASIN, store, page count.
- Writing claims about the book's content that are not already in the site copy.
- Deleting or replacing any image (see `claude/rules/assets.md`).
- Changing a published URL/slug (it loses rankings; a redirect would be needed).
- Adding a third-party script, tracker, font or paid service.
