"""Bilingual, factual GPX migration landing-page content."""
from html import escape
from pathlib import Path

COPY = {
    "en": {
        "title": "Geotag Photos Pro alternative: bring your GPX to PinShot",
        "description": "Bring an existing timestamped GPX into PinShot on iPhone, iPad or Mac. Preview the route, match camera photos by capture time and check the results. Free GPX import.",
        "eyebrow": "YOUR ROUTES CAN COME WITH YOU",
        "heading": "Keep the route.<br>Give your photos<br><em>their place.</em>",
        "intro": "Already have a recorded GPX? Bring it into PinShot, check its coverage, and add locations to the photos you took along the way.",
        "download": "Try PinShot for free", "watch": "Watch the example", "guide": "Read the full guide",
        "requirement": "Requires PinShot 1.3+ · iPhone, iPad & Mac · A matching timestamped track is essential.",
        "image_alt": "Actual PinShot GPX import screen using a clearly labeled synthetic demonstration track",
        "image_caption": "Actual PinShot interface · Synthetic example data",
        "notice_title": "Moving from Geotag Photos Pro?",
        "notice": "Its developer says the mobile apps have been removed from the stores. Existing accounts, trip uploads and GPX exports continue until at least 31 December 2027. Export your own recorded trips while you have access, keep the originals, and test a small trip first.",
        "source": "Read the developer’s announcement", "checked": "Checked 12 November 2026",
        "steps_title": "One small trip. Four clear steps.",
        "steps_intro": "Start with a few supported photos and their corresponding track. You can check the match before changing any media.",
        "steps": [
            ("Bring your GPX", "Export the recorded trip from your existing logger. Keep a copy. PinShot reads GPX 1.0/1.1 track points with valid timestamps; a planned route without times will not work."),
            ("Check before importing", "Open Settings or Geotag → Import GPX track. Review the map, time range, points and skipped items, then confirm. The imported source stays separate from your other recordings."),
            ("Match the camera clock", "Preview a capture time inside the track. Check the camera clock and time zone. The calibration assistant changes the matching offset; it does not rewrite photo dates."),
            ("Tag a few, then inspect", "Select a few matching photos and run geotagging. Inspect the resulting locations and media before processing a larger batch. On iOS, review tagged copies before manually cleaning up originals.")],
        "demo_title": "See the workflow before trying your own trip.",
        "demo_body": "An edited step-by-step demonstration using real PinShot screens. The track and sample photo are fictional test data, not a customer trip.",
        "video_label": "PinShot GPX import and photo matching demonstration",
        "video_download": "Download the video", "captions_download": "Download captions",
        "transcript": "Read the video steps",
        "sample_title": "Try the same small example",
        "sample_body": "The ZIP includes a labeled sample JPEG, a three-point GPX and bilingual instructions. GPX import and time-match preview are free. The free plan includes 20 media geotags per month.",
        "sample_button": "Download GPX + sample photo",
        "sample_note": "Use the sample only with its included photo. Set the camera offset to zero for this example and restore your previous setting afterward. The photo’s EXIF capture time is 1 November 2026, 02:01 UTC; your device may display it in local time.",
        "scope_title": "Bring the recording. Check the differences.",
        "table_head": ["What you have", "What PinShot can do"],
        "scope": [
            ("A recorded, timestamped GPX", "Import it as a separate source and preview capture-time matches. Reimporting the identical file reuses that source."),
            ("Photos taken during that recording", "Add GPS to supported JPEG, HEIC/HEIF, PNG, TIFF and DNG files. Live Photos and supported videos can also be matched."),
            ("A planned route without recording times", "It cannot identify where a particular photo was taken. PinShot does not infer missing locations from the image."),
            ("CR2, CR3, NEF, ARW, RAF or RW2 files", "These proprietary RAW files are not modified directly. Keep the originals and use a supported photo workflow."),
            ("An account or subscription in another app", "It does not transfer. PinShot imports GPX files, not accounts, purchases or your entire cloud library.")],
        "coverage_note": "Imported tracks are matched only within valid recorded segments. Gaps longer than five minutes and gaps between segments are not matched. Overlapping/conflicting tracks are rejected. Import limit: 20 MB, 200,000 points and 10,000 segments.",
        "faq_title": "Before you move a whole photo trip",
        "faqs": [
            ("Do I need Pro to import GPX?", "No. GPX import and the read-only time-match preview are available without Pro. The free monthly allowance is 20 media geotags. Pro adds unlimited tagging, full/custom-date scans, Mac folder tagging, exports and optional personal iCloud log sync."),
            ("Will every exported GPX work?", "No universal compatibility is promised. The file needs recorded track points with valid timestamps. Start with one short trip, review skipped points and gaps, and verify a few photo locations."),
            ("Can Mac record the route for me?", "Mac imports or syncs recordings; it does not act as a mobile GPS recorder. Use PinShot on iPhone or another recorder before shooting."),
            ("What if the location or file result is wrong?", "Check the selected source, original capture time, time zone and camera offset. Keep original-file backups. A skipped or failed item is not a successful geotag. Contact support with the app version, file format and error text; private trips or photos are not needed for a first report.")],
        "closing_title": "Start with one track.<br>See one photo find its place.",
        "closing_body": "Free to start. Pro offers lifetime, monthly and yearly options; current prices and eligibility appear in the App Store.",
        "independent": "PinShot is independently developed and is not affiliated with Geotag Photos Pro or TappyTaps. Product names belong to their respective owners."
    },
    "zh": {
        "title": "Geotag Photos Pro 替代方案：把 GPX 轨迹带到 PinShot",
        "description": "将已有的带时间戳 GPX 导入 PinShot，在 iPhone、iPad 和 Mac 上预览轨迹，按拍摄时间为相机照片补定位。GPX 导入免费，先用小示例体验。",
        "eyebrow": "已有轨迹，也能继续派上用场",
        "heading": "把走过的路，<br>带回你的<em>照片里。</em>",
        "intro": "已经有一份记录行程的 GPX？把它导入 PinShot，检查覆盖时段，再为当时拍下的照片补上地点。",
        "download": "免费下载 PinShot", "watch": "观看操作示例", "guide": "查看完整上手指南",
        "requirement": "需要 PinShot 1.3+ · 支持 iPhone、iPad 和 Mac · 必须有对应时段的带时间戳轨迹。",
        "image_alt": "PinShot GPX 导入实际界面，使用明确标记的人工构造示例轨迹",
        "image_caption": "App 实际界面 · 示例数据并非真实行程",
        "notice_title": "正在寻找 Geotag Photos Pro 的替代方案？",
        "notice": "其开发者已公告移动应用从商店下架；已有账号、行程上传和 GPX 导出服务至少维持到 2027 年 12 月 31 日。仍可访问时，先导出自己的行程并保留原文件，再用一段小行程验证新的整理流程。",
        "source": "查看开发者原始公告", "checked": "核实于 2026 年 11 月 12 日",
        "steps_title": "先拿一小段行程，走完这四步。",
        "steps_intro": "准备少量支持格式的照片，以及拍摄时对应的轨迹。正式标记前，可以先预览时间匹配。",
        "steps": [
            ("带上已有 GPX", "从原记录工具导出实际行程，并保留副本。PinShot 支持 GPX 1.0/1.1 中带有效时间戳的轨迹点；没有记录时间的规划路线不能用于照片定位。"),
            ("看清楚，再导入", "打开“设置或标记 → 导入 GPX 轨迹”。检查地图、时间范围、记录点和跳过项目，再确认导入。它会成为独立来源，保留已有记录。"),
            ("对准相机时间", "先预览轨迹覆盖内的一个拍摄时间，核对相机时钟与时区。时间校准助手只改变匹配偏移，不会改写照片的拍摄日期。"),
            ("先标几张，检查结果", "选择对应时段的几张照片完成标记，检查位置和影像是否正常，再扩大处理范围。iOS 会保留原片；先确认带 GPS 的副本，再手动清理原片。")],
        "demo_title": "用自己的照片前，先看一次完整步骤。",
        "demo_body": "使用 PinShot 真实界面剪辑的分步演示。轨迹与图片是人工构造的测试数据，不代表用户的真实照片或行程。",
        "video_label": "PinShot GPX 导入与照片时间匹配演示",
        "video_download": "下载演示视频", "captions_download": "下载字幕",
        "transcript": "查看视频文字步骤",
        "sample_title": "跟着同一个小示例试一遍",
        "sample_body": "示例包里有带标记的 JPEG、含三个记录点的 GPX，以及中英文说明。GPX 导入和时间匹配预览免费；免费版每月可标记 20 个影像项目。",
        "sample_button": "下载 GPX 与示例图片",
        "sample_note": "示例轨迹只用于包内图片。测试时将相机时间偏移设为 0，完成后恢复原设置。图片的原始 EXIF 时间为 2026 年 11 月 1 日 02:01 UTC，设备可能按本地时区显示。",
        "scope_title": "能带来什么，也先了解边界。",
        "table_head": ["你现有的内容", "在 PinShot 中怎么用"],
        "scope": [
            ("带时间戳的已记录 GPX", "作为独立来源导入，预览拍摄时间的匹配位置；重复导入完全相同的文件会复用原来源。"),
            ("记录期间拍摄的照片", "为支持的 JPEG、HEIC/HEIF、PNG、TIFF 和 DNG 补写 GPS；也支持系统图库中的实况照片和受支持的视频。"),
            ("没有记录时间的规划路线", "无法确定某张照片拍摄时的地点。PinShot 不会仅凭画面推测缺失的原始位置。"),
            ("CR2、CR3、NEF、ARW、RAF、RW2", "这些相机专有 RAW 不会被直接修改。请保留原始文件，使用支持的影像流程。"),
            ("其他应用的账号与订阅", "不会转移。这里导入的是 GPX 文件，不是账号、购买记录或整套云端照片。")],
        "coverage_note": "导入轨迹只在有效记录分段内匹配；分段间和超过五分钟的记录空缺不会匹配。时间重叠或冲突的轨迹会被拒绝。单次上限：20 MB、20 万个点、1 万个分段。",
        "faq_title": "迁移整段旅行前，你可能想确认",
        "faqs": [
            ("导入 GPX 必须购买 Pro 吗？", "不需要。GPX 导入与只读时间匹配预览免费，免费版每月可标记 20 个影像项目。Pro 提供不限量标记、完整与自定义日期扫描、Mac 文件夹标记、轨迹导出及可选的个人 iCloud 日志同步。"),
            ("所有工具导出的 GPX 都能用吗？", "不承诺普遍兼容。文件必须包含有有效时间戳的记录轨迹点。请先导入一小段行程，查看跳过点与记录空缺，再核验几张照片的位置。"),
            ("Mac 能替我随身记录轨迹吗？", "Mac 负责导入、同步与整理，不充当移动 GPS 记录器。拍摄前请使用 iPhone 上的 PinShot 或其他记录工具。"),
            ("位置不对，或文件写入失败怎么办？", "先核对轨迹来源、原始拍摄时间、时区与相机偏移，并保留原片备份。跳过或失败不代表已经标记成功。初次反馈可以先提供 App 版本、文件格式和错误提示，无需直接发送私人照片或精确行程。")],
        "closing_title": "从一条轨迹开始，<br>让一张照片找到地点。",
        "closing_body": "免费体验。Pro 提供永久买断、月度和年度订阅；价格与优惠资格以 App Store 显示为准。",
        "independent": "PinShot 为独立开发的产品，与 Geotag Photos Pro 或 TappyTaps 无从属关系。相关产品名称归各自所有者所有。"
    }
}

def content(locale, root, store):
    c = dict(COPY[locale])
    language = "zh" if locale == "zh" else "en"
    video = f"{root}assets/videos/pinshot-gpx-demo-{language}"
    asset_root = Path(__file__).resolve().parents[1] / 'assets' / 'videos'
    has_video = all((asset_root / f'pinshot-gpx-demo-{language}{suffix}').is_file()
                    for suffix in ('.mp4', '.poster.jpg', '.vtt'))
    watch_target = "demo-video" if has_video else "demo"
    if not has_video:
        c.update({
            'watch': '试用示例包' if locale == 'zh' else 'Try the sample pack',
            'demo_title': '先用小示例，完成你的第一次匹配。' if locale == 'zh' else 'Try one small example before your own trip.',
            'demo_body': '示例图片的拍摄时间位于示例轨迹覆盖内，可用于体验一次真实的时间匹配。它们都是人工构造的数据，不代表用户的照片或行程。' if locale == 'zh' else 'The sample photo’s capture time falls within the sample track. Use the pair to try a real time match. These are fictional test data, not a customer photo or trip.'
        })
    guide = root + ("zh/" if locale == "zh" else "") + "guide/"
    cta = f'<a class="button" href="{escape(store, quote=True)}" target="_blank" rel="noopener noreferrer">{c["download"]} ↗</a>'
    steps = ''.join(f'<li><span class="migration-number">0{i+1}</span><h3>{title}</h3><p>{body}</p></li>' for i, (title, body) in enumerate(c['steps']))
    rows = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a,b in c['scope'])
    faqs = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in c['faqs'])
    transcript = ""
    captions = Path(__file__).resolve().parents[1] / 'assets' / 'videos' / f'pinshot-gpx-demo-{language}.vtt'
    if captions.exists():
        cues = []
        for block in captions.read_text(encoding='utf-8').strip().split('\n\n'):
            lines = block.splitlines()
            timing = next((i for i, line in enumerate(lines) if '-->' in line), None)
            if timing is not None:
                cues.append('<li>' + '<br>'.join(escape(line) for line in lines[timing + 1:]) + '</li>')
        transcript = f'<details class="migration-transcript"><summary>{c["transcript"]}</summary><ol>{"".join(cues)}</ol></details>'
    if has_video:
        media = f'''<div class="migration-video" id="demo-video"><video controls playsinline preload="metadata" poster="{video}.poster.jpg" aria-label="{c['video_label']}"><source src="{video}.mp4" type="video/mp4"><track kind="captions" src="{video}.vtt" srclang="{'zh-Hans' if locale=='zh' else 'en'}" label="{'简体中文' if locale=='zh' else 'English'}">{c['video_label']}</video><div class="migration-video-links"><a href="{video}.mp4" download>{c['video_download']} ↓</a><a href="{video}.vtt" download>{c['captions_download']} ↓</a></div>{transcript}</div>'''
    else:
        sample_label = '测试图片 · 原始拍摄时间 02:01 UTC · 初始无 GPS' if locale == 'zh' else 'Test image · Capture time 02:01 UTC · No GPS initially'
        media = f'''<figure class="migration-sample-figure"><img src="{root}assets/images/gpx-sample-photo.jpg" width="2400" height="1800" alt="{sample_label}"><figcaption>{sample_label}</figcaption><div class="migration-time-example"><span>GPX 02:00–02:04 UTC</span><strong>02:01 UTC</strong><span>{'拍摄时间在覆盖内' if locale=='zh' else 'Capture time inside coverage'}</span></div></figure>'''
    return f'''<main id="main" class="migration-page">
<section class="migration-hero wrap"><div><p class="eyebrow">{c['eyebrow']}</p><h1>{c['heading']}</h1><p class="section-lead">{c['intro']}</p><div class="migration-actions">{cta}<a class="text-link" href="#{watch_target}">{c['watch']} ↓</a></div><p class="migration-requirement">{c['requirement']}</p></div><figure class="migration-screen"><img src="{root}assets/images/gpx-import-demo.jpg" alt="{c['image_alt']}" width="640" height="1302"><figcaption>{c['image_caption']}</figcaption></figure></section>
<aside class="migration-notice wrap"><div><p class="eyebrow">GEOTAG PHOTOS PRO</p><h2>{c['notice_title']}</h2></div><div><p>{c['notice']}</p><a class="text-link" href="https://www.geotagphotos.net/" target="_blank" rel="noopener noreferrer">{c['source']} ↗</a><small>{c['checked']}</small></div></aside>
<section class="section wrap"><div class="migration-heading"><h2>{c['steps_title']}</h2><p>{c['steps_intro']}</p></div><ol class="migration-steps">{steps}</ol></section>
<section class="migration-demo" id="demo"><div class="wrap migration-demo-grid">{media}<div><p class="eyebrow">PINSHOT · GPX</p><h2>{c['demo_title']}</h2><p class="section-lead">{c['demo_body']}</p><div class="migration-sample"><h3>{c['sample_title']}</h3><p>{c['sample_body']}</p><a class="button light" href="{root}samples/pinshot-demo.zip" download>{c['sample_button']} ↓</a><p class="migration-small">{c['sample_note']}</p></div></div></div></section>
<section class="section wrap"><div class="migration-heading"><h2>{c['scope_title']}</h2></div><div class="migration-table-wrap"><table class="compatibility-table migration-table"><thead><tr><th scope="col">{c['table_head'][0]}</th><th scope="col">{c['table_head'][1]}</th></tr></thead><tbody>{rows}</tbody></table></div><p class="migration-small">{c['coverage_note']}</p></section>
<section class="section faq-section wrap"><div class="faq-intro"><p class="eyebrow">FAQ</p><h2>{c['faq_title']}</h2><a class="text-link" href="{guide}">{c['guide']} ↗</a></div><div class="faq-list">{faqs}</div></section>
<section class="closing wrap"><div><h2>{c['closing_title']}</h2><p>{c['closing_body']}</p></div>{cta}</section><p class="wrap migration-independent">{c['independent']}</p></main>'''
