"""Generate the optimized image derivatives used by the site.

The original files (book cover, illustrations, logos, portraits) are paid
artwork and must never be modified or deleted: this script only READS them
and writes new, web-optimized files next to them. Re-run it after replacing
an original:

    python3 scripts/make_images.py

Requires Pillow (pip install Pillow).
"""

from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "images"
THEME = ROOT / "themes" / "theartofkubernetes" / "static" / "assets" / "images"


def save(img, dest, quality=82, **kwargs):
    dest.parent.mkdir(parents=True, exist_ok=True)
    fmt = "WEBP" if dest.suffix == ".webp" else "JPEG"
    if fmt == "JPEG" and img.mode != "RGB":
        img = img.convert("RGB")
    if fmt == "WEBP":
        kwargs.setdefault("method", 6)
    else:
        kwargs.setdefault("optimize", True)
        kwargs.setdefault("progressive", True)
    img.save(dest, fmt, quality=quality, **kwargs)
    print(f"{dest.relative_to(ROOT)}  {img.width}x{img.height}  {dest.stat().st_size // 1024} KB")


def resize_width(img, width):
    if img.width <= width:
        return img.copy()
    height = round(img.height * width / img.width)
    return img.resize((width, height), Image.LANCZOS)


def main():
    # Book cover (French edition): hero image + structured data.
    cover = Image.open(CONTENT / "CouvertureFirstPage.jpg")
    for width in (400, 800):
        save(resize_width(cover, width), CONTENT / f"the-art-of-kubernetes-couverture-{width}.webp")

    # Book mock-up on a table: "back cover" section.
    mockup = Image.open(CONTENT / "BackgroundBook.jpg")
    save(resize_width(mockup, 1200), CONTENT / "the-art-of-kubernetes-livre-1200.webp", quality=78)

    # Open Graph / Twitter card image (1200x630), centred on the book.
    og = ImageOps.fit(resize_width(mockup, 1300), (1200, 630), centering=(0.52, 0.38))
    save(og, CONTENT / "og-the-art-of-kubernetes.jpg", quality=85)

    # Article diagrams: SEO-friendly names, no spaces.
    save(Image.open(CONTENT / "Diag MultiCluster Hub and Spoke.png"),
         CONTENT / "kubernetes-multi-cluster-hub-and-spoke.webp", quality=90)
    save(Image.open(CONTENT / "Diag Kubernetes Features.png"),
         CONTENT / "kubernetes-fonctionnalites.webp", quality=90)
    save(resize_width(Image.open(CONTENT / "logo-kubeedge.png"), 240),
         CONTENT / "logo-kubeedge-240.webp", quality=90)

    # Hero background (mountains of the cover).
    mountains = Image.open(THEME / "Mountains.jpg")
    for width in (960, 1920):
        save(resize_width(mountains, width), THEME / f"mountains-{width}.webp", quality=70)

    # Header/footer logos, trimmed and resized for a ~48px display height.
    for variant in ("dark", "light"):
        logo = Image.open(THEME / f"TheArtOfKubernetes-logo-{variant}.png")
        logo = logo.crop(logo.getbbox())
        save(resize_width(logo, 480), THEME / f"logo-the-art-of-kubernetes-{variant}.webp",
             quality=90)

    # Author portrait (drawing).
    portrait = Image.open(THEME / "auteur-florian-grignon.jpg")
    save(resize_width(portrait, 480), THEME / "auteur-florian-grignon-480.webp")

if __name__ == "__main__":
    main()
