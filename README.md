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

Feature copy was checked against the app's current help, subscription feature gates, existing legal documents and App Store listing. The site describes matching PinShot logs or timestamped GPX recordings, version 1.3 GPX import, supported media, and different iOS/Mac original-media handling. Regional prices are deferred to the App Store.

## Assets and provenance

- The app icon and six localized app screenshots come from the existing GPSImage project. Screenshots are reduced and JPEG-encoded for delivery without changing their depicted interfaces. Original screenshot files remain in the app repository.
- `assets/images/travel-lake.jpg` is an illustrative travel image created using the built-in image-generation tool on 2026-11-11. It is labeled as AI-generated on the product pages and is not presented as a customer photo or a geotagging result.
- The small route motif and interface icons are original inline SVG artwork, not an actual map or an app screenshot.

Image-generation prompt:

> Use case: photorealistic-natural. Asset type: landscape photograph for the hero of PinShot, a photography/travel GPS geotagging product website. Create a premium editorial travel photograph of a quiet alpine lake at dawn, pale jagged limestone mountain peaks in the distance, a winding lakeshore footpath with a few dark evergreen trees in the foreground, clear muted turquoise water, subtle warm sunlight on the rock faces. No people, no buildings, no device, no UI, no text, no logos, no watermark. Natural believable photographic detail, soft atmospheric depth, muted sage/teal and warm stone palette. Wide landscape framing about 3:2, visually strong mountain silhouette in upper center and open calm water in lower half. Refined travel magazine photography, not oversaturated HDR. This is an illustrative travel image, not a real user photo or an actual geotagging result. Save the generated image for inclusion in the local website project.

## Release status

The owner approved publication on 2026-11-11. GitHub Pages is verified to publish main / (root). This release branch is based on origin/main at 6059a24 and preserves that live branch’s newer legal pages, rather than replacing them with the older local preview copies. App-version-dependent guide content is explicitly labeled 1.3 or later. Deployment verification is recorded after publication.

Local verification on 2026-11-11: all four product/guide pages, internal anchors and 18 linked local page/asset URLs passed checks. English and Chinese language navigation, mobile menu, screenshot tabs (including keyboard navigation), FAQ expansion and the existing Chinese privacy URL were checked in a browser. Responsive layouts were inspected at 390 px and 1280 px CSS viewport widths, with an additional narrow-screen check. Both existing legal-file hashes remain identical to the starting versions.

SHA-256 hashes of the preserved live legal files from origin/main (6059a24):

```text
8f7153f224db6abac9a00104e5383e57e2044ac4b3c0bfb7bb8cfe30ed62f65d  privacy/index.html
177c904d215b3d68925c66658f91541250113c9c121d513eec1eae839a45cf22  privacy/terms.html
```

The samples/ package is synthetic demonstration data. It contains a generated labeled JPEG with an explicit original EXIF capture time and a fictional GPX track. It is provided for a controlled first-use/review example, not as a real customer trip.

Download buttons use the website campaign URL generated by App Store Connect. The site adds no analytics SDK or visitor identifier. App Store campaign reporting is subject to Apple’s minimum attribution thresholds. Campaign links are in scripts/campaign_links.json.

Publication verified 2026-11-11: all four public product/guide pages, the sample ZIP and the two preserved legal documents returned HTTP 200 with expected content.

Post-release check 2026-11-12: iOS and macOS 1.3 (50) are Ready for Distribution. Updated English/Chinese hero text, workflow and FAQ to consistently include timestamped GPX import; existing legal paths and campaign links remain unchanged.

## GPX migration guides

`/gpx-migration/` and `/zh/gpx-migration/` explain migration from existing timestamped GPX recordings, including Geotag Photos Pro. Its service status is attributed to the developer's announcement and dated 2026-11-12. The guides distinguish supported tracks/media from planned routes, proprietary RAW files and account/subscription transfers.

The hero is a cropped capture of the real PinShot GPX import screen on an isolated test simulator. The phone screen, prerequisites, Apple Maps attribution and import control are preserved. It shows only the clearly labeled synthetic sample track. `assets/images/gpx-sample-photo.jpg` is the existing owned synthetic example, with its original EXIF capture time and no GPS.

The pages work as standalone illustrated guides. Verified demonstration video is embedded only when the matching MP4, poster and WebVTT assets all exist under `assets/videos/`. Otherwise they present the sample image and downloadable GPX/photo package, without a broken or placeholder video player. Video post-production sources are maintained in the PinShot app repository under `marketing/migration/`.

Downloaded third-party Panasonic camera samples are used only for local compatibility diagnosis. They are not included in this website or promotional videos.

### Completed walkthrough videos

Both migration pages include a 56-second, 1080×1920 H.264 walkthrough with real captured interface steps, a persistent synthetic-data label, downloadable MP4/VTT/SRT assets and an expandable text transcript. There is no audio. The two editions use Chinese and English captions over the same real Simplified Chinese interface; the English edition states this explicitly.

The sequence includes the actual successful geotagging result and the tagged copy's location in Apple Photos. The sample photo's original capture time and both its Photos/embedded GPS coordinates were verified separately. The UTC+8 example time is explicitly explained as 10:01 local = 02:01 UTC.

Validation: both files were fully decoded and all six keyframes reviewed; H.264, yuv420p, 30 fps, 56-second duration and faststart atom order were checked. Browser playback completed to the end, captions/transcripts loaded, and both locales were inspected at a 390-pixel mobile width. The mobile navigation and Escape behavior were checked. The watch link targets the player directly, and the Chinese mobile headline avoids an orphaned final word. Desktop layout and horizontal overflow were also checked.
