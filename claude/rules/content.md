# Content rules

Full how-to with examples: `claude/docs/content-guide.md`.

## Voice

- French, *vouvoiement*, the author's first person ("je") where he gives an opinion.
- Pedagogical and pragmatic, with a strong point of view (e.g. "use Operators sparingly").
  No hype, no marketing superlatives, no emoji.
- Use the author's existing wording as the source of truth. Do not invent facts about the
  book (chapters, page count, formats, interviews, prices): they come from `BOOKS` in
  `pelicanconf.py` and the existing copy. Ask the user when unsure.

## Never edit

- **Testimonials** (`testimonials` in `home_fr.html`): quoted verbatim, typos included.
  Never write or invent new ones.
- The back-cover text ("Quatrième de couverture") beyond typo fixes.

## Files

- Articles: `content/<lang>/<name>.rst`. Pages: `content/pages/<lang>/<name>.rst`.
- Ideas and unfinished posts: `content/drafts/` (excluded from the build). Move a file out
  of `drafts/` only when it is complete and has all the metadata.
- Required article metadata: `lang`, `date`, `modified`, `slug`, `category`, `tags`,
  `authors`, `seo_title`, `description`, `summary`, `logo`. Optional: `pdf`, `robots`,
  `logo_alt`.
- Update `:modified:` when the content changes substantially (not for typo fixes).

## reStructuredText conventions

- The document title (`####` underline) is the `<h1>`. Sections: `====` → `h2`,
  `----` → `h3`. Start with an introduction paragraph before the first `h2`.
- External links: anonymous form `` `texte <https://…>`__ `` (double underscore).
- Internal links: `` `texte <{filename}autre-article.rst>`__ ``; home page: `` `texte </>`__ ``.
- Key ideas: `.. pull-quote::` (1 to 3 per article). Images: `.. figure::` or `.. image::`
  with `:alt:`, `:width:`, `:height:` (see the content guide).
- No raw HTML (`.. raw:: html`) unless rst cannot express it; the theme styles plain rst.
- Typography: write normal spaces before `: ; ! ?` and inside `« »`; the
  `french_typography` filter turns them into no-break spaces.

## Landing page

- Copy and data live in `themes/theartofkubernetes/templates/home_fr.html`; SEO metadata
  in `content/pages/fr/home.rst`.
- Keep the conversion structure: hero (buy + free chapter) → key facts → back cover →
  audience → contents → reviews → author → buy box → FAQ → articles → newsletter.
