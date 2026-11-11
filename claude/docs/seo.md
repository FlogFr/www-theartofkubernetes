# SEO

## Goal and funnel

1. A French-speaking developer, SRE, architect or CTO searches Google for a Kubernetes
   topic or for a Kubernetes book.
2. They land on the home page (book queries) or on an article (topic queries).
3. They click **"Acheter sur Amazon"** (primary) or subscribe to the newsletter to get a
   **free chapter** (secondary, nurtured by email until they buy).

Every page therefore needs: a search intent it answers, internal links toward the book,
and a visible buy button (the header always has one).

## Keyword map

| Intent / cluster | Example queries (fr) | Target page |
| ---------------- | -------------------- | ----------- |
| Book, brand | livre kubernetes, livre kubernetes français, meilleur livre kubernetes, the art of kubernetes, kubernetes ebook kindle | `/` |
| Learning | apprendre kubernetes, comprendre kubernetes, kubernetes pour débutant | `/`, `/fr/qu-est-ce-que-kubernetes` |
| Definition | qu'est-ce que kubernetes, kubernetes définition, à quoi sert kubernetes | `/fr/qu-est-ce-que-kubernetes` |
| Platform | kubernetes paas, plateforme kubernetes, platform engineering kubernetes | `/`, `/fr/qu-est-ce-que-kubernetes` |
| Operators | kubernetes operator, operator kubernetes avantages, cloudnativepg | `/fr/operator-or-not-operator` |
| Multi-cluster | kubernetes multi cluster, kubestellar, liqo, submariner, hub and spoke kubernetes | `/fr/multi-cluster-kubernetes` |
| Edge | edge computing kubernetes, kubeedge, kubernetes iot | `/fr/edge-computing-avec-kubernetes` |
| Upcoming articles | see `content-roadmap.md` | |

One main keyword per page; never create two pages for the same intent (cannibalisation).

## What is implemented

**Technical**
- Clean, stable, extensionless URLs; canonical link on every indexable page.
- `<html lang>`, unique `<title>` and meta description per page (`seo_title`,
  `description` metadata), `robots` meta (`max-image-preview:large`).
- Open Graph + Twitter card (1200×630 image of the book), `article:*` tags on articles.
- hreflang alternates generated from translations (ready for the English edition).
- `sitemap.xml` (theme template): indexable pages only, `lastmod`, hreflang, image entries.
- `robots.txt`: allows everything except `/assets/` (PDF duplicates), points to the sitemap.
- No thin pages: tag/category/author/archive pages disabled, drafts excluded, the
  newsletter thank-you page is `noindex`.
- Custom `404.html` with links to the home page, articles and Amazon.
- Atom feed `feeds/all.atom.xml` (production build).

**Structured data (JSON-LD)**
- Home: `WebSite`, `WebPage`, `Person` (author, CKA credential), `Book`+`Product`
  (Kindle offer with price and free instant `shippingDetails`, ASIN as `sku`,
  testimonials as `Review` plus an `aggregateRating` computed from them), `FAQPage`.
- Articles: `BlogPosting` (dates, author, image, word count, keywords) + `BreadcrumbList`.
- Article list: `CollectionPage` with `ItemList` + `BreadcrumbList`.

**On-page**
- One `<h1>` per page with the main keyword, logical `h2`/`h3` outline.
- Landing page sections written around search intents: what the book is, what you learn,
  who it is for, contents, reviews, author (E-E-A-T), price, FAQ.
- Articles rewritten with descriptive headings, internal links between articles and
  to the book, links to authoritative sources, corrected alt texts.

**Performance (Core Web Vitals)**
- About 975 KB of template CSS, JS and icon font loaded on every page (plus a Google
  Fonts request) replaced by one minified CSS file (~56 KB, ~10 KB gzipped) and < 1 KB
  of JS. The theme's static folder went from 15.7 MB to 1.2 MB.
- Self-hosted fonts (no Google Fonts request), preloaded.
- WebP images sized for display, `width`/`height` everywhere, lazy loading below the fold,
  `fetchpriority="high"` on the hero cover.

## Automated checks

`make check` (`scripts/check_seo.py`) fails on: missing/duplicate title or description,
title > 70 chars, ≠ 1 `<h1>`, skipped heading levels, missing/foreign canonical, missing
OG image, invalid JSON-LD, a `Product` without `offers`, `review` or `aggregateRating`
(or whose `aggregateRating` does not match its reviews), `<img>` without
alt/width/height, broken internal links or anchors, sitemap/indexable pages mismatch,
robots.txt without sitemap.

## After each deployment (manual)

- Google Search Console (domain property `theartofkubernetes.com`): submit
  `https://theartofkubernetes.com/sitemap.xml`, inspect new URLs, watch "Pages" and
  "Core Web Vitals" reports.
- Rich Results Test (https://search.google.com/test/rich-results) on `/` and one article.
- Search Console "Product snippets" report (history below): after a deployment that
  fixes an issue, click "Validate fix" on it.
- Bing Webmaster Tools: import from Search Console.
- Removed URLs from the old site (tag/category/archive pages, `/fr/kubernetes-autoscaler`)
  now return 404: let them drop from the index, or request removal in Search Console.

## Search Console history

- **"Multiple reviews without aggregateRating object"** (Product snippets): the
  2026-11-07 version had three `Review` and no `aggregateRating`. A deployment of
  2026-11-10, made from sources that were never committed, removed the reviews (and
  added `shippingDetails`); Google validated the fix.
- **"Missing field review" / "Missing field aggregateRating"** (non-critical): caused
  by that removal. Fixed on 2026-11-11 by restoring the reviews and adding an
  `aggregateRating` computed from them (5/5, 3 reviews: the stars shown on the page).
  `make check` now reports both issues as errors.

## Recommendations (not implemented, need the author)

- **Measure conversions**: set up Amazon Attribution (available to KDP authors through
  Amazon Ads) or an Amazon Associates tag (`AMAZON_ASSOCIATE_TAG`) to know which pages
  sell. A privacy-friendly analytics tool (Plausible, GoatCounter) would show traffic;
  the buy links already carry `data-track` attributes for click tracking.
- **Author entity (E-E-A-T)**: fill `AUTHOR_PROFILES` (LinkedIn, GitHub…) and claim the
  Amazon Author Central page; link back to the site from those profiles.
- **Backlinks**: guest articles and talks in the French Kubernetes community (Cloud Native
  Days France, Kubernetes/CNCF meetups, podcasts), the interviewees of the book sharing
  it, a short presentation on LinkedIn linking to articles rather than only to Amazon.
- **Content**: publish the articles of `content-roadmap.md` (one every 2–4 weeks),
  each answering one search intent and linking to the book.
- **Amazon page**: reuse the site's keywords in the Kindle description and the 7 KDP
  keywords; encourage readers to leave Amazon reviews (they are the social proof that
  converts on Amazon).
- **Paper edition**: a paperback (KDP print) would add an ISBN, a second offer in the
  structured data, and buyers who prefer print.
