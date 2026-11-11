# PinShot product website and legal pages

Static English and Simplified Chinese product pages for GitHub Pages. No npm packages, database, external fonts, analytics SDK, or hosted backend are required.

## Pages

| Location | Content |
| --- | --- |
| `/` | English product homepage |
| `/zh/` | Simplified Chinese product homepage |
| `/guide/` | English getting-started guide |
| `/zh/guide/` | Simplified Chinese getting-started guide |
| `/privacy/` | Existing multilingual app privacy policy, unchanged |
| `/privacy/terms.html` | Existing multilingual terms, unchanged |

Public URLs use the existing `https://robincoderzhao.github.io/pinshot-legal/` prefix. All navigation and asset paths work under that prefix. Legal URLs keep their existing `?lang=en` / `?lang=zh-Hans` parameters.

## Local preview

From this repository:

```sh
python3 scripts/preview.py
```

- English: <http://127.0.0.1:4173/pinshot-legal/>
- 中文: <http://127.0.0.1:4173/pinshot-legal/zh/>

The preview binds only to `127.0.0.1`, reproduces the GitHub Pages path prefix, and disables caching. Use `--port 4174` if the default port is occupied. Stop it with Control-C.

## Editing

- Product copy and HTML templates: `scripts/build_site.py`.
- Shared presentation: `assets/site.css`.
- Mobile navigation, accessible screenshot tabs and language switching: `assets/site.js`.
- Assets: `assets/images/`.

Regenerate the four product/guide pages and sitemap after changing copy:

```sh
python3 scripts/build_site.py
```

The generated HTML is checked in and served directly. GitHub does not need to run Python or a build step. `.nojekyll` keeps the site as ordinary static files. The renderer never writes into `privacy/`; legal content continues to use the established product legal-document workflow.

Feature copy was checked against the app's current help, subscription feature gates, existing legal documents and App Store listing. The site explicitly describes the need for existing matching PinShot logs, the lack of general GPX import, supported media, and different iOS/Mac original-media handling. Regional prices are deferred to the App Store.

## Assets and provenance

- The app icon and six localized app screenshots come from the existing GPSImage project. Screenshots are reduced and JPEG-encoded for delivery without changing their depicted interfaces. Original screenshot files remain in the app repository.
- `assets/images/travel-lake.jpg` is an illustrative travel image created using the built-in image-generation tool on 2026-11-11. It is labeled as AI-generated on the product pages and is not presented as a customer photo or a geotagging result.
- The small route motif and interface icons are original inline SVG artwork, not an actual map or an app screenshot.

Image-generation prompt:

> Use case: photorealistic-natural. Asset type: landscape photograph for the hero of PinShot, a photography/travel GPS geotagging product website. Create a premium editorial travel photograph of a quiet alpine lake at dawn, pale jagged limestone mountain peaks in the distance, a winding lakeshore footpath with a few dark evergreen trees in the foreground, clear muted turquoise water, subtle warm sunlight on the rock faces. No people, no buildings, no device, no UI, no text, no logos, no watermark. Natural believable photographic detail, soft atmospheric depth, muted sage/teal and warm stone palette. Wide landscape framing about 3:2, visually strong mountain silhouette in upper center and open calm water in lower half. Refined travel magazine photography, not oversaturated HDR. This is an illustrative travel image, not a real user photo or an actual geotagging result. Save the generated image for inclusion in the local website project.

## Release status

Prepared for local review only. No remote push, GitHub Pages deployment, or App Store metadata change has been performed. Confirm the actual GitHub Pages source branch/folder before any approved publication; the local checkout branch is not proof of the live publishing source.

Local verification on 2026-11-11: all four product/guide pages, internal anchors and 18 linked local page/asset URLs passed checks. English and Chinese language navigation, mobile menu, screenshot tabs (including keyboard navigation), FAQ expansion and the existing Chinese privacy URL were checked in a browser. Responsive layouts were inspected at 390 px and 1280 px CSS viewport widths, with an additional narrow-screen check. Both existing legal-file hashes remain identical to the starting versions.

Baseline SHA-256 hashes of the preserved legal files:

```text
0632ae3b32794874128a0fb2fc4049d29699d1d0b15a2f5ddc4f047be8424b58  privacy/index.html
1ee3f902d67d4fc2bdf1769f605ecef3844fb8a669b0ab27e6d908f6c75d22f3  privacy/terms.html
```
