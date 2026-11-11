#!/usr/bin/env python3
"""Render the checked-in static pages. Python standard library only.

GitHub Pages serves the resulting HTML directly; no build service is required.
Never writes to privacy/ or edits the existing legal documents.
"""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = "https://robincoderzhao.github.io/pinshot-legal/"
STORE = "https://apps.apple.com/app/id6784540498"

PATHS = {
    "arrow": '<path d="M5 12h14m-6-6 6 6-6 6"/>',
    "external": '<path d="M7 17 17 7M7 7h10v10"/>',
    "pin": '<path d="M20 10c0 6-8 11-8 11S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    "camera": '<path d="m8 5 1.5-2h5L16 5h4a2 2 0 0 1 2 2v12H2V7a2 2 0 0 1 2-2Z"/><circle cx="12" cy="12" r="4"/>',
    "route": '<circle cx="5" cy="5" r="2"/><circle cx="19" cy="19" r="2"/><path d="M7 5h9a4 4 0 0 1 0 8H8a3 3 0 0 0 0 6h9"/>',
    "check": '<path d="m5 12 4 4L19 6"/>',
    "lock": '<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/><path d="M12 14v3"/>',
    "devices": '<rect x="2" y="3" width="14" height="11" rx="1.5"/><path d="M5 19h7m-4-5v5"/><rect x="16" y="9" width="6" height="12" rx="1.5"/>',
    "image": '<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8" cy="8" r="1.5"/><path d="m3 17 6-6 5 5 3-3 4 4"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7v.01"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "spark": '<path d="m12 2 2.7 7.3L22 12l-7.3 2.7L12 22l-2.7-7.3L2 12l7.3-2.7Z"/>',
}

def icon(name, size=20):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{PATHS[name]}</svg>'

COPY = {
 "en": {
  "html_lang":"en", "title":"PinShot — Put your photos back on the map", "description":"Record GPS tracks on iPhone and add missing locations to photos, Live Photos, and videos by capture time. Available for iPhone, iPad, and Mac. Free to start, with a lifetime Pro option.",
  "skip":"Skip to content", "brand_small":"PHOTO · PLACE · MEMORY", "nav":["How it works","The app","Free & Pro","FAQ"], "download":"Get PinShot", "store":"Download on the App Store", "language":"简体中文", "menu":"Open navigation", "nav_label":"Main navigation", "language_label":"Switch to Simplified Chinese",
  "hero_eyebrow":"FOR THE PLACES YOU WANT TO REMEMBER", "hero_title":"Put your photos<br>back on <em>the map.</em>", "hero_description":"Your camera captures the moment. PinShot remembers the place. Record your route, then add missing locations to your photos and videos by capture time.", "see_how":"See how it works", "devices":"For iPhone, iPad & Mac · Free with in-app purchases", "prerequisite":"Start recording before you shoot. Matching GPS logs and accurate capture times are required.",
  "photo_alt":"Illustrative alpine lake with a lakeside trail and mountains in warm morning light", "photo_overline":"THE MOMENT. AND THE PLACE.", "photo_title":"Keep them together.", "photo_note":"AI-generated travel illustration", "tag_title":"A memory with a place", "tag_sub":"GPS track + capture time", "strips":[["image","Photos, Live Photos & videos"],["devices","iPhone, iPad & Mac"],["lock","On-device by default"],["spark","Free to get started"]],
  "workflow_eyebrow":"A LITTLE PREPARATION. A LASTING MEMORY.", "workflow_title":"Go out. Take photos.<br>Bring the places home.", "workflow_lead":"A simple companion for camera days, weekend walks, and the trips you want to keep.", "steps":[["route","Record your route","Start GPS recording in PinShot on your iPhone before taking photos. Keep it with you while your camera captures the day."],["camera","Choose your photos","Import supported media into your photo library, or use files and folders on Mac with Pro. Make sure your camera’s clock is correct."],["pin","Match the moment","PinShot matches capture times with your recorded route and writes location metadata. Review the results and find your photos by place."]], "workflow_note":"Already home from a trip? You’ll need PinShot logs that cover when the photos were taken. Locations cannot be recovered automatically without matching logs.", "guide_link":"Read the getting-started guide",
  "app_eyebrow":"A CLOSER LOOK", "app_title":"Your route. Your photos.<br>One connected story.", "tab_label":"Explore PinShot features", "tab_names":{"record":"01 Record","tag":"02 Geotag","track":"03 Revisit"},
  "panels":{
   "record":{"eyebrow":"BEFORE YOU TAKE THE FIRST PHOTO","title":"Let your phone<br>remember the route.","body":"Start a recording session before you shoot. PinShot records in the background, with adaptive power saving when you’re stationary.","features":["Background GPS recording on iPhone","Review recording status and permissions","Export your route as GPX or BIN with Pro"],"alt":"Actual PinShot iPhone screenshot showing GPS recording controls"},
   "tag":{"eyebrow":"AFTER THE ADVENTURE","title":"Give your photos<br>their missing places.","body":"Find media without GPS information, select what you want to tag, and match its capture time to your PinShot logs.","features":["Photos, Live Photos and supported videos","Manual selection and photo library scanning","Camera clock offset settings for time matching"],"alt":"Actual PinShot iPhone screenshot showing GPS tagging, media selection and matching requirements"},
   "track":{"eyebrow":"REMEMBER THE WAY YOU WENT","title":"Follow the day<br>back, one turn at a time.","body":"Review your recorded route on a map, with speed segments, distance, duration and recorded points.","features":["Daily routes on a map","A clear view of the journey you recorded","Personal iCloud log sync across devices with Pro"],"alt":"Actual PinShot iPhone screenshot showing a recorded route on a map"}},
  "screen_note":"Actual app screenshot. Appearance may vary by device and version.", "app_pair":"Record on iPhone. Organize on your Apple devices.",
  "privacy_eyebrow":"YOUR MEMORIES STAY YOURS", "privacy_title":"A personal photo tool.<br>A personal approach.", "privacy_body":"Your GPS logs are stored on your device by default. PinShot has no tracking server, no ad SDKs, and no PinShot account to create.", "privacy_body2":"With Pro, you can choose to sync GPS logs through your own iCloud. The app does not sell or share your location data with third parties.", "privacy_link":"Read the app’s privacy policy", "privacy_art":"LOCAL BY DEFAULT · PERSONAL BY DESIGN",
  "plans_eyebrow":"START WITH YOUR NEXT OUTING", "plans_title":"Try it. Make it part of your kit.", "plans_lead":"Start free. Unlock Pro when you’re ready for bigger photo batches and a workflow across devices.", "free_name":"PinShot Free", "free_title":"Your first places.", "free_body":"Try the core workflow with your own photos.", "free_features":["GPS track recording and route viewing","Geotag up to 20 media items per month","Manual selection and basic library scanning"], "free_cta":"Start for free", "pro_name":"PinShot Pro", "pro_badge":"LIFETIME AVAILABLE", "pro_title":"More memories. All the tools.", "pro_body":"Choose a one-time lifetime purchase, or a monthly or yearly subscription.", "pro_features":["Unlimited media geotagging","Full-library and custom-date scans","GPX / BIN export and optional iCloud log sync","Batch file and folder tagging on Mac"], "pro_cta":"Explore Pro in the App Store", "plan_legal":"Prices and available offers are shown in the App Store for your region. Monthly and yearly subscriptions renew automatically unless canceled. Lifetime is a separate one-time purchase, with no subscription renewal.",
  "faq_eyebrow":"BEFORE YOUR FIRST TRIP", "faq_title":"A few good<br>questions.", "faq_intro":"The right expectations make the first outing better. Here’s what to know before you start.", "contact":"Ask a question", "faqs":[
   ["Can I add locations to old photos?","Only when matching PinShot GPS logs exist for the time those photos were taken, and their capture times are accurate. PinShot cannot automatically recover an unrecorded journey or infer the original location from the image."],
   ["Which photos and videos are supported?","JPEG, HEIC/HEIF, PNG, TIFF and DNG photos; Live Photos in the system photo library; and MP4, MOV and M4V video containers, including common H.264 and HEVC video. Proprietary RAW files such as CR2, CR3, NEF, ARW, RAF and RW2 are not modified directly. Unsupported media is skipped."],
   ["What happens to my original photos?","On iOS, geotagging creates GPS-tagged copies and keeps the originals for your review and manual cleanup in Photos. For edited items, the current visible result is preserved, but the earlier edit and Revert history does not transfer. Mac Photos uses a validated replacement workflow; Mac folder tagging may modify selected files in place. Keep a backup of important originals."],
   ["Can I use PinShot on Mac?","Yes. Use GPS logs recorded on iPhone, transferred in PinShot’s own log format or synced through your personal iCloud with Pro. Mac can tag supported media, and Pro adds batch file and folder tagging. Mac does not replace the iPhone’s GPS recording workflow."],
   ["Can I import a GPX track from another app?","PinShot can export recordings as GPX with Pro. General GPX import is not currently available; importing logs uses PinShot’s own record format."],
   ["Do I need a subscription?","No. You can start with the free version, which includes up to 20 media geotags per month. Pro offers a separate lifetime purchase as well as monthly and yearly subscriptions. Check current prices and any trial eligibility in the App Store."]],
  "closing_eyebrow":"MAKE ROOM FOR THE NEXT MEMORY", "closing_title":"Take the photo.<br>Keep the place.", "closing_body":"Start your first recording before your next outing.", "footer_privacy":"Privacy policy", "footer_terms":"Terms of service", "footer_guide":"Getting started", "footer_contact":"Contact", "footer_note":"Illustrative travel imagery; app screenshots show actual interfaces. iPhone, iPad, Mac and App Store are trademarks of Apple Inc.", "copyright":"© 2026 PinShot. All rights reserved.",
  "guide_title":"Your first trip with PinShot", "guide_description":"A practical guide to recording a route, matching photos and videos by capture time, and reviewing geotagged results in PinShot.", "home":"Home", "guide_name":"Getting started", "guide_eyebrow":"THE PINSHOT FIELD GUIDE", "guide_intro":"A little setup before you leave makes it easier to give your photos the right places when you return.", "toc":"IN THIS GUIDE", "guide_sections":[["before","Before you leave"],["record","While you’re out"],["match","When you get home"],["review","Review your results"],["formats","Supported formats"],["troubleshoot","If something doesn’t match"]], "back_home":"Back to PinShot",
 },
 "zh": {
  "html_lang":"zh-Hans", "title":"PinShot 影像轨迹 — 让旅行影像回到地图上", "description":"用 iPhone 记录 GPS 轨迹，按拍摄时间为照片、实况照片和视频补写位置。支持 iPhone、iPad 和 Mac，免费开始使用，Pro 提供永久买断。",
  "skip":"跳转到正文", "brand_small":"影像 · 地点 · 回忆", "nav":["使用方式","功能一览","免费与 Pro","常见问题"], "download":"下载 PinShot", "store":"在 App Store 下载", "language":"EN", "menu":"打开导航菜单", "nav_label":"主导航", "language_label":"Switch to English",
  "hero_eyebrow":"为每一个值得记住的地方", "hero_title":"让旅行影像，<br>回到<em>地图上。</em>", "hero_description":"相机记下瞬间，PinShot 记下地点。用 iPhone 记录旅途轨迹，再按拍摄时间，为照片和视频补上缺失的位置信息。", "see_how":"了解使用方式", "devices":"适用于 iPhone、iPad 和 Mac · 免费下载，含 App 内购买", "prerequisite":"请在拍摄前开始记录。补写位置需要对应时段的 GPS 轨迹，以及准确的拍摄时间。",
  "photo_alt":"旅行示意图：晨光中的山峰、湖泊与湖边小径", "photo_overline":"记住瞬间，也记住地点", "photo_title":"让回忆，有迹可循。", "photo_note":"AI 生成的旅行示意图", "tag_title":"一段回忆，一个地点", "tag_sub":"GPS 轨迹 + 拍摄时间", "strips":[["image","照片、实况照片与视频"],["devices","iPhone · iPad · Mac"],["lock","默认保存在本地"],["spark","免费开始使用"]],
  "workflow_eyebrow":"出发前的一小步，回忆里的一张地图", "workflow_title":"出发，拍摄，<br>把沿途的地点带回来。", "workflow_lead":"无论是带着相机远行，还是周末随意走走，让照片和拍摄地点一起留下来。", "steps":[["route","出发时，记录轨迹","拍摄前，在 iPhone 上打开 PinShot 并开始记录。带着手机出发，用相机记录眼前的风景。"],["camera","回来后，选择影像","将支持的影像导入照片图库，或用 Mac 的 Pro 功能处理文件与文件夹。先确认相机的拍摄时间准确。"],["pin","按时间，补上地点","PinShot 将拍摄时间与记录的轨迹匹配，写入位置信息。检查处理结果，让影像可以按地点查找。"]], "workflow_note":"已经结束的旅行，也需要当时对应的 PinShot 轨迹。没有匹配的记录，就无法自动找回过去的拍摄地点。", "guide_link":"查看完整上手指南",
  "app_eyebrow":"看看 PINSHOT 如何工作", "app_title":"让走过的路，<br>连起拍过的照片。", "tab_label":"查看 PinShot 功能", "tab_names":{"record":"01 记录","tag":"02 标记","track":"03 回顾"},
  "panels":{
   "record":{"eyebrow":"在按下第一张快门之前","title":"让手机，<br>记住你走过的路。","body":"拍摄前开始一次记录。PinShot 支持后台记录，并在静止时自适应省电，让你可以专注眼前的风景。","features":["在 iPhone 上后台记录 GPS 轨迹","查看记录状态与所需权限","Pro 支持导出 GPX 或 BIN 轨迹"],"alt":"PinShot iPhone 实际界面截图：GPS 记录与控制"},
   "tag":{"eyebrow":"旅途结束，回忆开始整理","title":"为照片和视频，<br>补上缺失的地点。","body":"找到缺少 GPS 信息的影像，选择需要处理的项目，再将拍摄时间与 PinShot 轨迹进行匹配。","features":["支持照片、实况照片和常见视频","手动选择与照片图库扫描","可设置相机时间偏移，辅助准确匹配"],"alt":"PinShot iPhone 实际界面截图：GPS 标记、影像选择和匹配前提"},
   "track":{"eyebrow":"重新走一遍记忆里的路线","title":"从一个转角，<br>想起一整天的旅程。","body":"在地图上回顾记录的路线，查看速度分段、距离、耗时与记录点，让走过的路更清晰。","features":["按日期查看轨迹地图","回顾记录下来的行程","Pro 可通过个人 iCloud 跨设备同步轨迹"],"alt":"PinShot iPhone 实际界面截图：轨迹地图与行程信息"}},
  "screen_note":"App 实际界面截图；显示效果可能因设备和版本而异。", "app_pair":"用 iPhone 记录，在你的 Apple 设备上整理。",
  "privacy_eyebrow":"你的回忆，由你保管", "privacy_title":"个人影像工具，<br>也尊重个人空间。", "privacy_body":"GPS 轨迹默认保存在设备本地。PinShot 不运营轨迹追踪服务器，不集成广告 SDK，也不需要注册 PinShot 账号。", "privacy_body2":"Pro 用户可以自行选择，通过个人 iCloud 同步 GPS 轨迹。应用不会向第三方出售或分享你的定位数据。", "privacy_link":"阅读 App 隐私政策", "privacy_art":"默认保存在本地 · 由你掌握",
  "plans_eyebrow":"从下一次出发开始", "plans_title":"先体验，再成为你的摄影装备。", "plans_lead":"免费完成第一次标记。需要处理更多影像、跨设备整理时，再选择适合你的 Pro 方案。", "free_name":"PinShot 免费版", "free_title":"从最初的几个地点开始。", "free_body":"用自己的照片，体验完整的核心流程。", "free_features":["GPS 轨迹记录与路线回顾","每月最多标记 20 个影像项目","手动选择与基础图库扫描"], "free_cta":"免费下载体验", "pro_name":"PinShot Pro", "pro_badge":"支持永久买断", "pro_title":"更多影像，完整工具。", "pro_body":"可选择一次购买的永久版，也提供月度和年度订阅。", "pro_features":["不限数量的影像 GPS 标记","完整图库与自定义日期扫描","GPX / BIN 导出与可选 iCloud 轨迹同步","Mac 文件与文件夹批量标记"], "pro_cta":"在 App Store 查看 Pro", "plan_legal":"具体价格与可用优惠，以你所在地区的 App Store 显示为准。月度和年度订阅会自动续订，除非提前取消。永久版是独立的一次性购买，无订阅续费。",
  "faq_eyebrow":"第一次出发前，你可能想知道", "faq_title":"先了解，<br>再放心出发。", "faq_intro":"了解适用范围和必要准备，让第一次使用更顺利。", "contact":"联系开发者", "faqs":[
   ["以前拍的照片，也能补上位置吗？","需要有覆盖拍摄时段的 PinShot GPS 轨迹，并且照片的拍摄时间准确。没有匹配的记录，PinShot 无法自动还原过去的行程，也不会仅凭画面推测原始拍摄地点。"],
   ["支持哪些照片和视频格式？","支持 JPEG、HEIC/HEIF、PNG、TIFF、DNG 照片，系统照片图库中的实况照片，以及 MP4、MOV、M4V 视频容器，包括常见的 H.264 和 HEVC 视频。CR2、CR3、NEF、ARW、RAF、RW2 等相机专有 RAW 格式不会被直接修改；不支持的影像会跳过处理。"],
   ["标记后，原来的照片会怎样？","在 iOS 上，标记会生成带 GPS 的副本，并保留原片，由你检查后在“照片”中手动清理。已编辑影像会保留当前可见效果，但之前的编辑指令和“复原”历史不会转移。Mac 照片图库采用验证后的替换流程，Mac 文件夹标记可能原地修改所选文件。重要原片建议保留备份。"],
   ["可以在 Mac 上使用吗？","可以。使用 iPhone 记录的 GPS 轨迹，通过 PinShot 自身的日志格式传入，或使用 Pro 通过个人 iCloud 同步。Mac 可以处理支持的影像，Pro 还提供文件与文件夹批量标记。Mac 不能代替 iPhone 完成随身 GPS 记录。"],
   ["能导入其他 App 的 GPX 轨迹吗？","目前 Pro 可以将 PinShot 的轨迹导出为 GPX，但尚不支持通用 GPX 轨迹导入。日志导入使用 PinShot 自身的记录格式。"],
   ["一定要订阅才能使用吗？","不需要。免费版每月可标记最多 20 个影像项目。Pro 同时提供独立的永久买断、月度订阅与年度订阅；当前价格和是否符合试用资格，以 App Store 显示为准。"]],
  "closing_eyebrow":"下一段值得记住的旅程", "closing_title":"拍下瞬间，<br>也留下它的地点。", "closing_body":"下次出发前，开始你的第一次轨迹记录。", "footer_privacy":"隐私政策", "footer_terms":"服务条款", "footer_guide":"上手指南", "footer_contact":"联系我们", "footer_note":"旅行图片用于示意，App 截图展示实际界面。iPhone、iPad、Mac 和 App Store 是 Apple Inc. 的商标。", "copyright":"© 2026 PinShot。保留所有权利。",
  "guide_title":"和 PinShot 一起，开始第一次记录", "guide_description":"了解如何记录轨迹、按拍摄时间匹配照片与视频，以及检查 PinShot 的 GPS 标记结果。", "home":"首页", "guide_name":"上手指南", "guide_eyebrow":"PINSHOT 出发手册", "guide_intro":"出发前做一点准备，回来后就能更顺利地为照片补上正确的拍摄地点。", "toc":"这份指南包含", "guide_sections":[["before","出发前准备"],["record","旅途中记录"],["match","回来后匹配"],["review","检查处理结果"],["formats","支持的格式"],["troubleshoot","匹配不成功时"]], "back_home":"返回 PinShot 首页",
 }
}

def button(label, cls="", href=STORE):
    external = ' target="_blank" rel="noopener noreferrer"' if href.startswith("https://apps.apple.com") else ""
    return f'<a class="button {cls}" href="{href}"{external}>{label}{icon("external" if external else "arrow",17)}</a>'

def text_link(label, href):
    return f'<a class="text-link" href="{href}">{label}<span class="arrow" aria-hidden="true">↗</span></a>'

def document_head(c, locale, guide, root):
    path = ("zh/" if locale=="zh" else "") + ("guide/" if guide else "")
    en_path = "guide/" if guide else ""
    title = c["guide_title"] + " — PinShot" if guide else c["title"]
    desc = c["guide_description"] if guide else c["description"]
    schema = {"@context":"https://schema.org","@type":"SoftwareApplication","name":"PinShot","applicationCategory":"PhotographyApplication","operatingSystem":"iOS 17.0 or later; iPadOS 17.0 or later; macOS 14.0 or later","url":PUBLIC+path,"downloadUrl":STORE,"description":desc}
    return f'''<!doctype html>
<html lang="{c['html_lang']}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(desc,quote=True)}">
<meta name="theme-color" content="#f8f7f3"><meta name="color-scheme" content="light">
<link rel="canonical" href="{PUBLIC+path}">
<link rel="alternate" hreflang="en" href="{PUBLIC+en_path}"><link rel="alternate" hreflang="zh-Hans" href="{PUBLIC+'zh/'+en_path}"><link rel="alternate" hreflang="x-default" href="{PUBLIC+en_path}">
<meta property="og:type" content="website"><meta property="og:site_name" content="PinShot"><meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(desc,quote=True)}"><meta property="og:url" content="{PUBLIC+path}"><meta property="og:image" content="{PUBLIC}assets/images/travel-lake.jpg"><meta property="og:image:alt" content="{escape(c['photo_alt'],quote=True)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{root}assets/images/app-icon.png"><link rel="apple-touch-icon" href="{root}assets/images/app-icon.png">
<link rel="stylesheet" href="{root}assets/site.css"><script src="{root}assets/site.js" defer></script>
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
</head><body>
<a class="skip-link" href="#main">{c['skip']}</a>'''

def header(c, locale, guide, root):
    home = root + ("zh/" if locale=="zh" else "")
    other = root + ("" if locale=="zh" else "zh/") + ("guide/" if guide else "")
    nav = "".join(f'<a href="{home if guide else ""}#{section}">{label}</a>' for section,label in zip(["how-it-works","the-app","pro","faq"],c["nav"]))
    return f'''<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="{home}" aria-label="PinShot {c['home']}"><img src="{root}assets/images/app-icon.png" width="37" height="37" alt=""><span>PinShot<small>{c['brand_small']}</small></span></a>
<nav class="desktop-nav" aria-label="{c['nav_label']}">{nav}</nav>
<div class="header-actions"><a class="language-link" data-language-link href="{other}" lang="{'en' if locale=='zh' else 'zh-Hans'}" hreflang="{'en' if locale=='zh' else 'zh-Hans'}" aria-label="{c['language_label']}">{c['language']}</a>{button(c['download'],'small dark')}<button class="mobile-toggle" data-menu-toggle aria-controls="mobile-navigation" aria-expanded="false" aria-label="{c['menu']}">{icon('menu',23)}</button></div>
</div><nav id="mobile-navigation" class="mobile-nav" aria-label="{c['nav_label']}" hidden>{nav}</nav></header>'''

def footer(c, locale, root):
    legal_lang = "zh-Hans" if locale=="zh" else "en"
    guide_link = root + ("zh/" if locale=="zh" else "") + "guide/"
    home = root + ("zh/" if locale=="zh" else "")
    return f'''<footer class="site-footer"><div class="wrap"><div class="footer-top"><a class="brand" href="{home}"><img src="{root}assets/images/app-icon.png" width="29" height="29" alt="">PinShot</a><nav class="footer-links" aria-label="{'页脚导航' if locale=='zh' else 'Footer navigation'}"><a href="{guide_link}">{c['footer_guide']}</a><a href="{root}privacy/?lang={legal_lang}">{c['footer_privacy']}</a><a href="{root}privacy/terms.html?lang={legal_lang}">{c['footer_terms']}</a><a href="mailto:414108176@qq.com">{c['footer_contact']}</a></nav></div><div class="footer-bottom"><p>{c['footer_note']}</p><span>{c['copyright']}</span></div></div></footer></body></html>'''

def check_list(items):
    return '<ul class="feature-list">'+''.join(f'<li>{icon("check",16)}<span>{item}</span></li>' for item in items)+'</ul>'

def home_page(locale):
    c=COPY[locale]; root="../" if locale=="zh" else "./"
    steps=''.join(f'<article class="step"><div class="step-number">0{i+1}</div><div class="step-icon">{icon(name,23)}</div><h3>{title}</h3><p>{body}</p></article>' for i,(name,title,body) in enumerate(c['steps']))
    strip=''.join(f'<div>{icon(name,18)}<span>{label}</span></div>' for name,label in c['strips'])
    tabs=''.join(f'<button role="tab" id="tab-{key}" aria-controls="panel-{key}" aria-selected="{str(key=="tag").lower()}" tabindex="{0 if key=="tag" else -1}">{c["tab_names"][key]}</button>' for key in ['record','tag','track'])
    panels=''
    for key,p in c['panels'].items():
        hidden=' hidden' if key!='tag' else ''
        panels+=f'''<div class="app-panel" id="panel-{key}" role="tabpanel" aria-labelledby="tab-{key}" tabindex="0"{hidden}><div class="app-panel-copy"><p class="eyebrow">{p['eyebrow']}</p><h3>{p['title']}</h3><p>{p['body']}</p>{check_list(p['features'])}<div class="pair-note">{icon('devices',16)}<span>{c['app_pair']}</span></div></div><figure class="phone-figure"><div class="phone-shell"><img src="{root}assets/images/app-{key}-{locale}.jpg" width="1284" height="2778" loading="lazy" decoding="async" alt="{p['alt']}"></div><figcaption>{c['screen_note']}</figcaption></figure></div>'''
    faq=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in c['faqs'])
    return document_head(c,locale,False,root)+header(c,locale,False,root)+f'''
<main id="main">
<section class="hero wrap" aria-labelledby="hero-title"><div class="hero-grid"><div class="hero-copy"><p class="eyebrow"><span class="tiny-dot" aria-hidden="true"></span>{c['hero_eyebrow']}</p><h1 id="hero-title">{c['hero_title']}</h1><p class="hero-description">{c['hero_description']}</p><div class="hero-actions">{button(c['store'])}<a class="text-link" href="#how-it-works">{c['see_how']}<span aria-hidden="true">↓</span></a></div><p class="device-note">{c['devices']}</p><p class="prerequisite">{icon('info',14)}<span>{c['prerequisite']}</span></p></div>
<div class="hero-art"><div class="travel-photo"><img src="{root}assets/images/travel-lake.jpg" width="1536" height="1024" fetchpriority="high" alt="{c['photo_alt']}"><div class="photo-caption"><span>{c['photo_overline']}</span><strong>{c['photo_title']}</strong></div></div><div class="map-token" aria-hidden="true"><svg viewBox="0 0 160 145"><rect width="160" height="145" fill="#e9ede1"/><path d="M-5 90Q40 120 62 83T112 56T169 75" fill="none" stroke="#cedfdc" stroke-width="25"/><path d="M10-10 46 155M92-10 125 150M-5 32 164 20M-5 123 164 109" stroke="#fff" stroke-width="7"/><path d="M-5 32 164 20M10-10 46 155M92-10 125 150M-5 123 164 109" stroke="#dadccf" fill="none"/><path d="M28 115 53 109 50 81Q46 60 79 58L104 58 101 34" stroke="#e2663b" fill="none" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 5"/><circle cx="28" cy="115" r="5" fill="#e2663b" stroke="#fff" stroke-width="3"/><path d="M112 30c0 10-11 18-11 18S90 40 90 30a11 11 0 1 1 22 0Z" fill="#e2663b"/><circle cx="101" cy="30" r="4" fill="#fff"/></svg></div><div class="memory-tag"><div class="memory-pin">{icon('pin',24)}</div><div><strong>{c['tag_title']}</strong><small>{c['tag_sub']}</small></div></div><span class="photo-note">{c['photo_note']}</span></div></div><div class="intro-strip">{strip}</div></section>
<section class="section workflow wrap" id="how-it-works"><div class="section-heading"><div><p class="eyebrow">{c['workflow_eyebrow']}</p><h2>{c['workflow_title']}</h2></div><p>{c['workflow_lead']}</p></div><div class="steps">{steps}</div><div class="workflow-bottom"><p>{c['workflow_note']}</p>{text_link(c['guide_link'],'guide/')}</div></section>
<section class="app-section" id="the-app"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">{c['app_eyebrow']}</p><h2>{c['app_title']}</h2></div><div class="tab-list" role="tablist" aria-label="{c['tab_label']}" data-tabs>{tabs}</div></div>{panels}</div></section>
<section class="section privacy-section wrap"><div class="privacy-art" aria-hidden="true"><div class="lock-tile">{icon('lock',66)}</div><span class="privacy-caption">{c['privacy_art']}</span></div><div class="privacy-copy"><p class="eyebrow">{c['privacy_eyebrow']}</p><h2>{c['privacy_title']}</h2><p>{c['privacy_body']}</p><p>{c['privacy_body2']}</p>{text_link(c['privacy_link'],root+'privacy/?lang='+('zh-Hans' if locale=='zh' else 'en'))}</div></section>
<section class="plans-section wrap" id="pro"><div class="plans-heading"><p class="eyebrow">{c['plans_eyebrow']}</p><h2>{c['plans_title']}</h2><p class="section-lead">{c['plans_lead']}</p></div><div class="plans-grid"><article class="plan-card"><span class="plan-name">{c['free_name']}</span><h3>{c['free_title']}</h3><p>{c['free_body']}</p>{check_list(c['free_features'])}{button(c['free_cta'],'light')}</article><article class="plan-card pro"><span class="plan-name">{c['pro_name']}<span class="plan-badge">{c['pro_badge']}</span></span><h3>{c['pro_title']}</h3><p>{c['pro_body']}</p>{check_list(c['pro_features'])}{button(c['pro_cta'],'white')}</article></div><p class="plan-legal">{c['plan_legal']}</p></section>
<section class="section faq-section wrap" id="faq"><div class="faq-intro"><p class="eyebrow">{c['faq_eyebrow']}</p><h2>{c['faq_title']}</h2><p>{c['faq_intro']}</p>{text_link(c['contact'],'mailto:414108176@qq.com')}</div><div class="faq-list">{faq}</div></section>
<section class="closing wrap"><div><p class="eyebrow">{c['closing_eyebrow']}</p><h2>{c['closing_title']}</h2><p>{c['closing_body']}</p></div>{button(c['store'],'white')}</section>
</main>'''+footer(c,locale,root)

GUIDE_BODY={
"en":'''<section id="before"><h2>01 · Before you leave</h2><p><strong>Install PinShot on your iPhone and check your camera’s clock.</strong> Photo locations are matched by capture time. An incorrect date, time zone or clock setting can prevent a correct match.</p><ul><li>Allow the location permissions needed for your chosen recording mode. Check the app’s permission guidance before relying on background recording.</li><li>Set your camera’s date and time accurately, including when traveling across time zones.</li><li>Try a short recording and a few supported photos before an important trip.</li></ul><div class="guide-note">A matching recording is essential. Installing PinShot after a trip does not recreate its GPS history.</div></section>
<section id="record"><h2>02 · While you’re out</h2><p>Open the recording screen and start GPS recording <strong>before you take photos</strong>. Keep your iPhone with you, and check that recording has actually started.</p><p>PinShot supports background recording and adapts sampling while stationary. GPS quality and continuity still depend on location permissions, signal conditions and system behavior. Tunnels, buildings or interrupted recording may leave gaps.</p><p>When you finish, review your route and stop recording when you no longer need it.</p></section>
<section id="match"><h2>03 · When you get home</h2><p>Choose the photos or videos you want to geotag in the tagging screen. You can scan your photo library or select items manually. Pro adds full and custom-date scans, as well as Mac batch file and folder tagging.</p><ol><li>Make sure the GPS logs cover the media’s actual capture period.</li><li>Choose the appropriate log source, especially when working with logs transferred from another device.</li><li>If the camera clock was offset, review the camera time offset in Settings before matching.</li><li>Start with a small selection, run tagging, and inspect the results.</li></ol><h3>Working on Mac</h3><p>Bring your iPhone logs to Mac using PinShot’s own log format, or enable personal iCloud log sync with Pro. For folder workflows, keep a backup of important files before processing them.</p><div class="guide-note">GPX export is a Pro feature. Importing general GPX files from other apps is not currently supported.</div></section>
<section id="review"><h2>04 · Review your results</h2><p>Check the result summary and inspect several locations in your photo library. Review failed, skipped or unmatched items separately.</p><p><strong>On iOS, keep the originals until you have checked the GPS-tagged copies.</strong> New copies are organized in the PinShot album; eligible originals may appear in the cleanup album for your manual review. Copies do not automatically inherit the originals’ albums. If album organization is pending, retain the originals and check again.</p><p>For edited media, the visible edited result is preserved, but earlier adjustment instructions and Revert history do not transfer. Mac Photos uses validated replacement, while Mac folder tagging may modify files in place.</p></section>
<section id="formats"><h2>05 · Supported formats</h2><table class="compatibility-table"><thead><tr><th scope="col">Media</th><th scope="col">Supported workflow</th></tr></thead><tbody><tr><td>Photos</td><td>JPEG/JPG, HEIC/HEIF, PNG, TIFF/TIF and DNG</td></tr><tr><td>Live Photos</td><td>Supported Live Photos in the system photo library</td></tr><tr><td>Videos</td><td>MP4, MOV and M4V containers, including common H.264 and HEVC/H.265 video</td></tr><tr><td>Camera RAW</td><td>CR2, CR3, NEF, ARW, RAF and RW2 are not modified directly. Consider a supported DNG workflow while keeping the original files.</td></tr></tbody></table><p>File extensions alone do not guarantee compatibility. Unsupported or unrecognized media is skipped, and an accurate capture time is needed for matching.</p></section>
<section id="troubleshoot"><h2>06 · If something doesn’t match</h2><h3>No matching GPS record</h3><p>Check whether recording was active at the actual capture time, whether the correct device’s logs are selected, and whether there was a recording or signal gap. No matching track means the location cannot be recovered automatically.</p><h3>The time looks wrong</h3><p>Check the original capture time, camera clock, time zone and configured offset. The date a file was imported into your library is not necessarily the time it was taken. Review the media details before trying another small batch.</p><h3>A file is skipped</h3><p>Check the supported formats above and the result shown in the app. Do not treat a skipped file as a successful geotag. For help, send the developer the file format, device, app version and error message; avoid sending private photos or exact routes unless necessary.</p><h3>Using free and Pro</h3><p>The free version includes up to 20 media geotags per month. Pro unlocks unlimited tagging, full/custom-date scans, export, personal iCloud log sync and Mac folder tagging. A separate lifetime purchase is available alongside monthly and yearly subscriptions. Prices and eligible offers are shown in the App Store.</p></section>''',
"zh":'''<section id="before"><h2>01 · 出发前准备</h2><p><strong>在 iPhone 上安装 PinShot，并检查相机的时钟。</strong>影像的位置通过拍摄时间匹配；日期、时区或时钟设置不正确，都可能影响匹配结果。</p><ul><li>按应用内说明，允许所选记录方式需要的定位权限。依赖后台记录前，先检查权限提示。</li><li>确认相机日期和时间准确，跨时区旅行时尤其需要留意。</li><li>重要旅行前，先做一次短时间记录，用几张支持的照片体验完整流程。</li></ul><div class="guide-note">对应时段的轨迹是必要条件。旅行结束后才安装 PinShot，无法补录过去的 GPS 历史。</div></section>
<section id="record"><h2>02 · 旅途中记录</h2><p>在<strong>拍照之前</strong>进入记录页面，开始 GPS 记录。随身携带 iPhone，并确认记录已实际开始。</p><p>PinShot 支持后台记录，并在静止时自适应调整采样。GPS 质量和连续性仍受定位权限、信号环境及系统行为影响；隧道、建筑物或记录中断都可能造成空缺。</p><p>行程结束后，检查记录下来的路线，在不再需要时停止记录。</p></section>
<section id="match"><h2>03 · 回来后匹配</h2><p>在标记页面选择要补写位置的照片或视频。可以扫描照片图库，也可以手动选择。Pro 支持完整扫描、自定义日期扫描，以及 Mac 文件与文件夹批量标记。</p><ol><li>确认 GPS 轨迹覆盖影像的真实拍摄时段。</li><li>选择正确的轨迹来源，尤其是在使用其他设备传入的日志时。</li><li>如果相机时钟有偏差，先在设置中核对相机时间偏移。</li><li>先选少量影像完成一次标记，再检查处理结果。</li></ol><h3>在 Mac 上整理</h3><p>可以使用 PinShot 自身的日志格式，将 iPhone 轨迹传到 Mac；也可以通过 Pro 开启个人 iCloud 轨迹同步。处理文件夹前，请备份重要文件。</p><div class="guide-note">GPX 导出属于 Pro 功能。目前尚不支持从其他应用导入通用 GPX 文件。</div></section>
<section id="review"><h2>04 · 检查处理结果</h2><p>查看完成后的结果汇总，并在照片图库中抽查几个拍摄地点。失败、跳过和未匹配项目，需要分别检查原因。</p><p><strong>在 iOS 上，请检查带 GPS 的副本后，再决定是否清理原片。</strong>新副本会整理到 PinShot 相册，符合条件的原片可能进入待清理相册，供你手动检查。副本不会自动继承原片所属的相册；如果相册整理尚未完成，请先保留原片，稍后再检查。</p><p>对于已编辑影像，会保留当前可见的编辑效果，但之前的调整指令和“复原”历史不会转移。Mac 照片图库采用验证后的替换流程；Mac 文件夹标记可能原地修改文件。</p></section>
<section id="formats"><h2>05 · 支持的格式</h2><table class="compatibility-table"><thead><tr><th scope="col">影像类型</th><th scope="col">支持范围</th></tr></thead><tbody><tr><td>照片</td><td>JPEG/JPG、HEIC/HEIF、PNG、TIFF/TIF、DNG</td></tr><tr><td>实况照片</td><td>系统照片图库中受支持的 Live Photos</td></tr><tr><td>视频</td><td>MP4、MOV、M4V 容器，包括常见 H.264 与 HEVC/H.265 视频</td></tr><tr><td>相机 RAW</td><td>CR2、CR3、NEF、ARW、RAF、RW2 不会被直接修改。可考虑受支持的 DNG 流程，同时保留原始文件。</td></tr></tbody></table><p>文件扩展名本身不代表一定兼容。不支持或无法识别的影像会跳过处理；进行匹配还需要准确的原始拍摄时间。</p></section>
<section id="troubleshoot"><h2>06 · 匹配不成功时</h2><h3>没有找到对应轨迹</h3><p>检查实际拍摄时是否正在记录、是否选中了正确设备的日志，以及对应时段是否存在记录或信号空缺。没有匹配轨迹，就无法自动恢复拍摄位置。</p><h3>时间看起来不对</h3><p>检查原始拍摄时间、相机时钟、时区和已设置的偏移。照片导入图库的日期，不一定就是实际拍摄时间。先查看媒体详情，再用少量影像尝试。</p><h3>文件被跳过</h3><p>核对上方支持格式和应用内显示的结果。被跳过的文件不代表已经成功标记。需要帮助时，可以向开发者提供文件格式、设备、App 版本和错误提示；没有必要时，无需发送私人照片或精确行程。</p><h3>免费版和 Pro 怎么选</h3><p>免费版每月最多标记 20 个影像项目。Pro 解锁不限量标记、完整与自定义日期扫描、轨迹导出、个人 iCloud 轨迹同步和 Mac 文件夹标记。可选择独立的永久买断，也有月度与年度订阅。价格和可用优惠以 App Store 显示为准。</p></section>'''
}

def guide_page(locale):
    c=COPY[locale]; root="../../" if locale=="zh" else "../"
    home=root+("zh/" if locale=="zh" else "")
    toc=''.join(f'<a href="#{id}">{title}</a>' for id,title in c['guide_sections'])
    return document_head(c,locale,True,root)+header(c,locale,True,root)+f'''<main id="main"><div class="wrap"><section class="guide-hero"><nav class="breadcrumb" aria-label="{'当前位置' if locale=='zh' else 'Breadcrumb'}"><a href="{home}">{c['home']}</a><span aria-hidden="true">/</span><span aria-current="page">{c['guide_name']}</span></nav><p class="eyebrow">{c['guide_eyebrow']}</p><h1>{c['guide_title']}</h1><p class="section-lead">{c['guide_intro']}</p></section><div class="guide-layout"><nav class="guide-toc" aria-label="{c['toc']}"><strong>{c['toc']}</strong>{toc}</nav><article class="guide-body">{GUIDE_BODY[locale]}<div class="guide-closing">{button(c['store'])}{text_link(c['back_home'],home)}</div></article></div></div></main>'''+footer(c,locale,root)

for locale in ['en','zh']:
    dest=ROOT/('zh' if locale=='zh' else '')
    dest.mkdir(parents=True,exist_ok=True)
    (dest/'index.html').write_text(home_page(locale),encoding='utf-8')
    (dest/'guide').mkdir(exist_ok=True)
    (dest/'guide'/'index.html').write_text(guide_page(locale),encoding='utf-8')
    print(f'Rendered {locale} home and guide')

urls=['','zh/','guide/','zh/guide/','privacy/','privacy/terms.html']
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{PUBLIC}{path}</loc></url>\n' for path in urls)+'</urlset>\n',encoding='utf-8')
