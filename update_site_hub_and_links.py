import json
import os
import re

ALL_ARTICLES = [
    {
        "url": "/winter-bath-care",
        "file": "winter-bath-care.html",
        "tag": "🛁 温活＆うるおいバリア NEW",
        "tag_style": "background: #e0e7ff; color: #3730a3;",
        "title": "🛁 保湿力の強さで肌乾燥とさようなら！温活と全身うるおいバリアを叶える高保湿入浴剤＆バスミルクランク10",
        "desc": "出浴後の粉吹き・乾燥かゆみ・冷え性と完全決別！アユーラ、BARTH、キュレル、クナイプなど湯上がりもしっとり吸い付く神入浴剤10選。",
        "footer_name": "入浴剤・バスケア"
    },
    {
        "url": "/winter-face-wash",
        "file": "winter-face-wash.html",
        "tag": "🫧 つっぱり・粉吹き防止 NEW",
        "tag_style": "background: #ccfbf1; color: #0f766e;",
        "title": "🫧 保湿力の強さで肌乾燥とさようなら！冬のつっぱり・粉吹きを防ぐうるおい吸着・高保湿洗顔料ランク10",
        "desc": "洗顔直後のパリパリ乾燥・毛穴詰まりに終止符！カネボウ、オバジX炭酸泡、エスト温感ジェルなど洗うだけでうるおう至高の洗顔料10選。",
        "footer_name": "高保湿洗顔料"
    },
    {
        "url": "/winter-face-mist",
        "file": "winter-face-mist.html",
        "tag": "💧 暖房砂漠化レスキュー NEW",
        "tag_style": "background: #fce7f3; color: #9d174d;",
        "title": "💧 保湿力の強さで肌乾燥とさようなら！暖房の砂漠化からメイクを守る高保湿ミスト化粧水＆オイルミストランク10",
        "desc": "オフィスの暖房直風によるファンデ割れ・粉吹きを撃退！エリクシールつや玉ミスト、ダルバ白トリュフ、コスメデコルテなど神ミスト10選。",
        "footer_name": "高保湿ミスト"
    },
    {
        "url": "/winter-lotion",
        "file": "winter-lotion.html",
        "tag": "💧 水分満タン保水",
        "tag_style": "background: #e0f2fe; color: #0369a1;",
        "title": "💧 保湿力の強さで肌乾燥とさようなら！冬の乾きを満たす高保湿化粧水＆とろみ浸透ローションランク10",
        "desc": "暖房でカラカラに干からびた角層をごくごく潤す！イプサ、アクセーヌ、エスト、カルテHDなど超微細ナノカプセル配合ローション徹底比較。",
        "footer_name": "高保湿化粧水"
    },
    {
        "url": "/winter-cleansing",
        "file": "winter-cleansing.html",
        "tag": "🍯 うるおい落とし",
        "tag_style": "background: #fef3c7; color: #b45309;",
        "title": "洗うほど肌がモチモチ潤う！冬の粉吹き・つっぱりを防ぐ高保湿クレンジング＆濃密バームランク10",
        "desc": "乾燥悪化の主犯「過剰脱脂」をストップ！DUO、カバーマーク、シュウウエムラ、カネボウなど洗顔後も化粧水いらずの至高クレンジング10選。",
        "footer_name": "クレンジング"
    },
    {
        "url": "/winter-day-cream",
        "file": "winter-day-cream.html",
        "tag": "☀️ 暖房＆UVシールド",
        "tag_style": "background: #ffe4e6; color: #be123c;",
        "title": "☀️ 暖房乾燥と冬紫外線をダブル遮断！一日中しっとり続く高保湿UV美容液＆朝用デイクリームランク10",
        "desc": "エアコン温風の砂漠化と真皮まで届く冬のUV-A波を完全ブロック！カネボウ クリームインデイ、ランコム、オルビスなど夕方までツヤ肌キープ。",
        "footer_name": "朝用UVクリーム"
    },
    {
        "url": "/winter-serum-booster",
        "file": "winter-serum-booster.html",
        "tag": "💧 スキンケアの土台作り",
        "tag_style": "background: #e0e7ff; color: #3730a3;",
        "title": "💧 ゴワつく冬の砂漠肌を即ほぐす！浸透力を底上げする高保湿・導入先行美容液おすすめ10選",
        "desc": "化粧水が入っていかない冬の角質肥厚をリセット！ランコム、コスメデコルテ、ソフィーナiPなどマイクロ炭酸泡やリポソームカプセルで水分吸収力を劇的向上。",
        "footer_name": "導入美容液"
    },
    {
        "url": "/winter-face-mask",
        "file": "winter-face-mask.html",
        "tag": "💧 集中水分チャージ",
        "tag_style": "background: #ccfbf1; color: #0f766e;",
        "title": "💧 水分爆弾で砂漠肌を即リセット！翌朝の化粧ノリ激変・高保湿シートマスク＆夜用パック10選",
        "desc": "暖房でしぼんだ肌に潤い集中補給！トリデン、ルルルンハイドラEX、バイオダンス生コラーゲンゲルなど話題の最新密着マスクを徹底比較。",
        "footer_name": "シートマスク"
    },
    {
        "url": "/winter-moisture-cream",
        "file": "winter-moisture-cream.html",
        "tag": "🧴 11-12月 注目度No.1",
        "tag_style": "background: #fef3c7; color: #b45309;",
        "title": "🧴 保湿力の強さで肌乾燥とさようなら！高保湿フェイスクリーム＆濃密バーム10選",
        "desc": "湿度が急激に下がる真冬の暖房下でも粉吹き・つっぱりゼロへ。キールズ、コスメデコルテ、キュレルなどセラミド＆ヘパリン類似物質配合の最強クリーム！",
        "footer_name": "保湿クリーム"
    },
    {
        "url": "/winter-eye-cream",
        "file": "winter-eye-cream.html",
        "tag": "👁️ 目元・ほうれい線",
        "tag_style": "background: #fae8ff; color: #86198f;",
        "title": "👁️ 暖房直撃の目元・ほうれい線をふっくら密着！乾燥小じわ撃退・高保湿アイクリーム＆薬用リンクルケア10選",
        "desc": "夕方のちりめんジワ・ファンデ割れを解消！エリクシール純粋レチノール、ポーラニールワン、コスメデコルテ目元リポソームなど実力派アイケア厳選。",
        "footer_name": "アイクリーム"
    },
    {
        "url": "/winter-base-makeup",
        "file": "winter-base-makeup.html",
        "tag": "💄 冬のベースメイク特集",
        "tag_style": "background: #ffe4e6; color: #be123c;",
        "title": "✨ 冬の暖房でもひび割れない！夕方まで潤いツヤが続く高保湿ファンデ＆下地10選",
        "desc": "エアコン直撃でもほうれい線のめり込み・毛穴落ちを防ぐ！クレ・ド・ポー ボーテ、SHISEIDOエッセンススキングロウなど生ツヤ肌アイテム厳選。",
        "footer_name": "ベースメイク"
    },
    {
        "url": "/winter-lip-care",
        "file": "winter-lip-care.html",
        "tag": "💋 リップ＆ホリデーギフト",
        "tag_style": "background: #fee2e2; color: #991b1b;",
        "title": "🎁 冬のガサガサ皮剥けに終止符！ひと塗りでぷるんと潤う高保湿リップ＆濃密ティント10選",
        "desc": "皮脂腺のないデリケートな唇を物理シールド！ラネージュの夜用スリーピングマスク、ディオールマキシマイザーなど縦ジワを消し去る極上トリートメント。",
        "footer_name": "リップケア"
    },
    {
        "url": "/winter-body-care",
        "file": "winter-body-care.html",
        "tag": "🛁 全身・粉吹き対策",
        "tag_style": "background: #f3e8ff; color: #6b21a8;",
        "title": "🛁 すねの粉吹き・全身の乾燥かゆみにサヨナラ！高保湿ボディミルク＆濃厚ボディバター10選",
        "desc": "お風呂上がりの全身をうるおいヴェールで包み込む！ニュートロジーナ純度99%CICA、ニベア、キュレル、サボン、ロクシタンシアなど極上ボディケア。",
        "footer_name": "ボディケア"
    },
    {
        "url": "/winter-hair-care",
        "file": "winter-hair-care.html",
        "tag": "🌿 冬の美髪・静電気防止",
        "tag_style": "background: #dcfce7; color: #166534;",
        "title": "🌿 冬の静電気・毛先パサつきと完全決別！うる艶髪を叶える高保湿ヘアオイル＆濃厚ヘアマスク10選",
        "desc": "マフラー摩擦や暖房乾燥で傷んだキューティクルを集中補修。モロッカンオイル、ケラスターゼ、オルビス、finoなどサロン級のツヤ髪を叶える冬の必須アイテム。",
        "footer_name": "ヘアケア"
    },
    {
        "url": "/winter-hand-care",
        "file": "winter-hand-care.html",
        "tag": "🤲 手荒れ・あかぎれレスキュー",
        "tag_style": "background: #ffedd5; color: #9a3412;",
        "title": "🤲 手荒れ・あかぎれ・ささくれ知らずへ！高保湿なのにベタつかない神ハンドクリーム＆ネイル10選",
        "desc": "水仕事や冷風で荒れた手元を即効修復！PC・スマホ作業でもベタつかない速乾バームから、あかぎれを治す指定医薬部外品、指先ネイルオイルまで徹底網羅。",
        "footer_name": "ハンドケア"
    },
    {
        "url": "/summer-cosme",
        "file": "summer-cosme.html",
        "tag": "☀️ 特集アーカイブ",
        "tag_style": "background: #e0f2fe; color: #0369a1;",
        "title": "☀️ 夏コスメおすすめ3選",
        "desc": "紫外線予報UVスプレー、靴消臭スプレー、リフレアクリーム！夏の汗・UV・ニオイ対策神アイテム厳選。",
        "footer_name": "夏コスメ"
    }
]

# 1. index.html の更新
hub_cards_html = []
for art in ALL_ARTICLES:
    card = f"""      <!-- {art['footer_name']} -->
      <a href="{art['url']}" class="hub-card">
        <span class="hub-card-tag" style="{art['tag_style']}">{art['tag']}</span>
        <h2 class="hub-card-title">{art['title']}</h2>
        <p class="hub-card-desc">{art['desc']}</p>
      </a>"""
    hub_cards_html.append(card)

cards_block = "\n\n".join(hub_cards_html)

footer_links_list = ['      <a href="/">トップページ</a>']
for art in ALL_ARTICLES:
    footer_links_list.append(f'      <a href="{art["url"]}">{art["footer_name"]}</a>')
footer_links_html = '<div class="footer-links">\n' + "\n".join(footer_links_list) + '\n    </div>'

index_html = f"""<!DOCTYPE html>
<html lang="ja" prefix="og: http://ogp.me/ns#">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lumi Cosme (ルミコスメ) | 2026年最新トレンドコスメ＆真冬の高保湿ケア厳選メディア</title>
  <meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿入浴剤・高保湿洗顔料・ミスト化粧水・高保湿化粧水・クレンジング・朝用デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・高保湿ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">
  <meta name="keywords" content="コスメ, 美容, 高保湿入浴剤, 高保湿洗顔料, ミスト化粧水, 高保湿化粧水, クレンジングバーム, 朝用デイクリーム, 高保湿クリーム, 導入美容液, シートマスク, アイクリーム, ボディミルク, ヘアオイル, ハンドクリーム, 冬ファンデーション, リップケア, トレンドコスメ, ルミコスメ, 2026コスメ">

  <!-- SEO & Canonical -->
  <link rel="canonical" href="https://lumi-cosme.vercel.app/">
  <meta name="robots" content="index, follow">

  <!-- OGP (SNSシェア最適化 / 日本人向け) -->
  <meta property="og:site_name" content="Lumi Cosme (ルミコスメ)">
  <meta property="og:title" content="Lumi Cosme | 2026最新トレンドコスメ＆真冬の高保湿ケア厳選メディア">
  <meta property="og:description" content="11月・12月の本格乾燥シーズン到来！高保湿入浴剤、洗顔料、ミスト化粧水、化粧水、クレンジングなど全15大特集公開中。">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/">
  <meta property="og:image" content="https://lumi-cosme.vercel.app/2.jpg">
  <meta property="og:locale" content="ja_JP">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Lumi Cosme | 2026最新トレンドコスメ＆真冬の高保湿ケア厳選メディア">
  <meta name="twitter:description" content="11月・12月の本格乾燥シーズン到来！高保湿入浴剤、洗顔料、ミスト化粧水、化粧水、クレンジングなど全15大特集公開中。">
  <meta name="twitter:image" content="https://lumi-cosme.vercel.app/2.jpg">

  <link rel="stylesheet" href="style.css">

  <!-- 構造化データ (JSON-LD) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Lumi Cosme (ルミコスメ)",
    "url": "https://lumi-cosme.vercel.app/",
    "description": "SNSで話題のトレンドコスメや真冬の過酷な肌悩みを解決する高保湿スキンケアを厳選紹介するビューティーメディア。",
    "publisher": {{
      "@type": "Organization",
      "name": "Lumi Cosme"
    }}
  }}
  </script>
</head>
<body>

  <!-- ヘッダー -->
  <header class="site-header">
    <div class="header-badge">✨ 2026 BEAUTY SELECTION</div>
    <h1 class="site-title">Lumi Cosme 特集一覧</h1>
    <p class="site-subtitle">11月・12月の過酷な乾燥を撃退する真冬の厳選ビューティー特集（全15大特集）</p>
  </header>

  <!-- メインコンテンツ -->
  <main class="container">
    <div class="hub-grid">

{cards_block}

    </div>
  </main>

  <!-- フッター -->
  <footer class="site-footer">
    {footer_links_html}
    <p class="copyright">© 2026 Lumi Cosme (ルミコスメ) All Rights Reserved.</p>
  </footer>

</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
print("Updated index.html successfully!")

# 2. 全HTMLファイルのフッターリンクを一括更新
for art in ALL_ARTICLES:
    fn = art["file"]
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8") as f:
            content = f.read()
        
        # footer-links を置換
        new_content = re.sub(
            r'<div class="footer-links">.*?</div>',
            footer_links_html,
            content,
            flags=re.DOTALL
        )
        if new_content != content:
            with open(fn, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated footer in {fn}")

# 3. sitemap.xml の更新
sitemap_urls = ['  <url>\n    <loc>https://lumi-cosme.vercel.app/</loc>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>\n  </url>']
for art in ALL_ARTICLES:
    sitemap_urls.append(f"""  <url>
    <loc>https://lumi-cosme.vercel.app{art['url']}</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>""")

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>"""

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print("Updated sitemap.xml successfully!")

# 4. submit_indexnow.py の URL_LIST 更新
with open("submit_indexnow.py", "r", encoding="utf-8") as f:
    idx_script = f.read()

target_urls_code = "URL_LIST = [\n" + ",\n".join([f'    f"https://{{HOST}}/"'] + [f'    f"https://{{HOST}}{art["url"]}"' for art in ALL_ARTICLES]) + "\n]"
new_idx_script = re.sub(r'URL_LIST = \[.*?\]', target_urls_code, idx_script, flags=re.DOTALL)
with open("submit_indexnow.py", "w", encoding="utf-8") as f:
    f.write(new_idx_script)
print("Updated submit_indexnow.py successfully!")
