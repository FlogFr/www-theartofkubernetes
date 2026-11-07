# Image and asset rules

The book's illustrations and visuals were made by an illustrator the author paid. They
are protected assets.

## Never

- Delete, overwrite, re-encode in place, crop, recolor or rename an original.
- Replace an original with a stock photo, an AI-generated image or a template placeholder.
- Re-introduce template demo assets (the old Upcover placeholders were removed on purpose).

## Protected originals

`content/images/`: `CouvertureFirstPage.jpg` (cover), `BackgroundBook.jpg`/`.webp`
(mock-up), `Diag Kubernetes Features.png`, `Diag MultiCluster Hub and Spoke.png`,
`logo-edge.webp`, `logo-kubernetes.webp`, `logo-multicluster.webp`, `logo-operator.webp`,
testimonial portraits (`*-Portrait.webp`), `logo-kubeedge.png`.

`themes/theartofkubernetes/static/assets/images/`: `TheArtOfKubernetes-*.png/.webp`
(logos), `Mountains.jpg`, `TouchingTheClouds.jpg`, `auteur-florian-grignon.jpg/.webp`,
`Favicon.jpg`, favicons and `android-chrome-*`/`apple-touch-icon` icons.

## Derivatives

- Web-optimized versions are **new files** written by `scripts/make_images.py`
  (`make images`), e.g. `the-art-of-kubernetes-couverture-800.webp`,
  `mountains-1920.webp`, `og-the-art-of-kubernetes.jpg`. Templates use the derivatives.
- To add an image: put the original in place, add a step to `scripts/make_images.py`
  (WebP, kebab-case name, sized for its display), run `make images`, commit both.
- Testimonial portraits are personal data of real people: use them only next to their
  own testimonial.

## PDFs

- `content/assets/Chapitre-Introduction.pdf` is not linked from the site; it is most
  likely the free chapter sent to newsletter subscribers. Keep its URL stable and do not
  link it publicly without the author's approval (it is the lead magnet).
- Article PDFs are linked with the article's `:pdf:` metadata.
- `/assets/` is disallowed in `robots.txt`: PDFs duplicate the HTML articles and must
  not compete with them in search results.
