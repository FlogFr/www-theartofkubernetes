# Design and front-end rules

## Visual identity

- Colors: `night` (`#0f2a2e`, the blue-green of the cover's mountains) for dark sections,
  Tailwind `teal` for brand accents and links, `amber` **only** for the buy-on-Amazon
  button, `slate` for text.
- Fonts (self-hosted woff2, latin subset): Crimson Pro for headings (`font-serif`),
  Libre Franklin for body text (`font-sans`).
- Imagery: the book cover, the mock-up, the mountains photo, the author's portrait and the
  article illustrations. Never replace them with stock or generated images.

## Conversion

- The buy button (`buy_button` macro, `btn-buy`) stays visible in the header on every
  page and appears in the hero, after the contents, in the buy box and in article CTAs.
- The newsletter (free chapter) is the secondary action (`btn-secondary`,
  `btn-ghost-light`).

## Tailwind CSS v4

- Source: `themes/theartofkubernetes/src/site.css`; output:
  `static/assets/css/site.css` (minified, committed). Run `make css` after any change to
  templates, `site.css` or classes in rst files.
- Only `templates/` and `content/**/*.rst` are scanned for classes (`@source`). Build
  class names literally: no string concatenation of class fragments.
- Utility classes in templates; repeated patterns become an `@utility` in `site.css`
  (`btn`, `btn-buy`, `wrap`, `eyebrow`, `section-title`…). Article typography uses the
  `prose` classes from `@tailwindcss/typography`, customised in `site.css`.

## Templates

- Shared UI strings come from `partials/i18n.html` (`t.<key>`); never hard-code French in
  shared templates. Language-specific copy lives in `home_<lang>.html`.
- Reuse the macros of `partials/macros.html` (`icon`, `buy_button`, `stars`,
  `article_card`). Icons are Feather SVGs in `templates/icons/` (see its README).
- Pelican does not autoescape: escape dynamic text in attributes with `|e`, and output
  JSON-LD values with `|tojson`.

## Quality bar

- Mobile first: check 390px and 1280px; no horizontal scroll.
- Accessibility: WCAG AA contrast, visible focus, one `<h1>`, landmarks, `aria-label` on
  icon-only buttons, decorative SVGs `aria-hidden`.
- The site must work without JavaScript (`site.js` only toggles the mobile menu).
- No jQuery, carousels, animation libraries or icon fonts.
