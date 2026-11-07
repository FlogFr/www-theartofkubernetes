# Content guide

How to write and publish content. Rules to follow: `claude/rules/content.md` and
`claude/rules/seo.md`.

## New article

1. Create `content/fr/<short-name>.rst` (or start from an idea in `content/drafts/`).
2. Fill in the metadata (template below) and write the body in plain reStructuredText.
3. Add an illustration (`:logo:`, 800×500 WebP) — ask the author for one from the
   illustrator; until then reuse an existing article illustration.
4. Link it from at least one existing article, and link to an existing article from it.
5. `make publish && make check`, look at it with `make devserver`.
6. Update `claude/docs/content-roadmap.md`.

```rst
Titre de l'article avec le mot-clé principal
############################################

:lang: fr
:date: 2026-11-07
:modified: 2026-11-07
:slug: mot-cle-principal
:category: Kubernetes
:tags: kubernetes, mot-clé 1, mot-clé 2
:authors: Florian Grignon
:seo_title: Titre court pour Google (60 caractères max)
:description: Description de 120 à 160 caractères qui donne envie de cliquer.
:summary: Chapeau de 1 à 3 phrases, affiché sous le titre et sur les cartes d'articles.
:logo: logo-mon-article.webp
:pdf: /assets/Article-Mon-Article.pdf

Paragraphe d'introduction : le problème et ce que l'article apporte.

Premier intertitre (h2)
=======================

Texte avec un `lien externe <https://kubernetes.io/>`__, un
`lien vers un autre article <{filename}multi-cluster.rst>`__ et un
`lien vers le livre </>`__.

Sous-partie (h3)
----------------

.. pull-quote::

   Une idée clé mise en avant.

.. figure:: /images/mon-schema.webp
   :alt: Description précise du schéma pour les moteurs de recherche et l'accessibilité.
   :width: 800
   :height: 500

   Légende affichée sous l'image.
```

## Metadata reference

| Field          | Required | Used for |
| -------------- | -------- | -------- |
| title (first line) | yes  | `<h1>`, cards, breadcrumb, JSON-LD headline |
| `lang`         | yes      | URL prefix, `<html lang>`, hreflang |
| `date`         | yes      | publication date (`datePublished`, `article:published_time`) |
| `modified`     | yes      | update date (`dateModified`, sitemap `lastmod`); shown when different from `date` |
| `slug`         | yes      | URL `/<lang>/<slug>`, **never change it once published**; translations share the slug |
| `category`     | yes      | Atom feed only (`Kubernetes`) |
| `tags`         | yes      | `article:tag`, JSON-LD keywords |
| `authors`      | yes      | `Florian Grignon` |
| `seo_title`    | yes      | `<title>` (≤ 60 chars). Default: the title followed by the site name |
| `description`  | yes      | meta description (120–160 chars). Default: truncated summary |
| `summary`      | yes      | lead under the `<h1>`, article cards |
| `logo`         | yes      | illustration file in `content/images/` (800×500), Open Graph image |
| `logo_alt`     | no       | alt text of the illustration (empty = decorative) |
| `pdf`          | no       | path of a PDF version, adds a "Version PDF" button |
| `robots`       | no       | e.g. `noindex, follow` (also removes the page from the sitemap) |
| `status`       | no       | `hidden` for pages that must not be listed (e.g. bienvenue) |
| `template`     | pages    | `home_fr`, `articles`, or default `page` |

The reading time is computed automatically.

## Pages

Pages live in `content/pages/<lang>/`. The home page `home.rst` only holds metadata
(`:template: home_fr`, `:save_as: index.html`, `:url:` empty); its copy is in
`themes/theartofkubernetes/templates/home_fr.html`.

## Images

- Put the original file in `content/images/` (never modify it afterwards), add a
  derivative step in `scripts/make_images.py` and run `make images`.
- Reference the WebP derivative with its real `:width:` and `:height:`; the
  `responsive_images` filter makes it fluid and lazy-loaded.
- `:align: right` on `.. image::` floats a small image (e.g. a project logo).

## Before publishing — checklist

- [ ] Title with the main keyword, `seo_title` ≤ 60 chars, `description` 120–160 chars.
- [ ] Introduction before the first `h2`; `h2`/`h3` structure readable on its own.
- [ ] At least one link to another article and one to the book; descriptive anchors.
- [ ] Images with alt text, width and height.
- [ ] `make publish && make check` → 0 errors.
