import os
import re

ALL_ARTICLES = [
    {
        "url": "/winter-serum-booster",
        "file": "winter-serum-booster.html",
        "title": "💧 浸透力を底上げする高保湿・導入先行美容液おすすめ10選",
        "desc": "硬くなった冬肌をほぐし、化粧水をグングン引き込む土台美容液。ランコム、コスメデコルテなど。",
        "footer_name": "導入美容液"
    },
    {
        "url": "/winter-face-mask",
        "file": "winter-face-mask.html",
        "title": "💧 水分爆弾で砂漠肌を即リセット！高保湿シートマスク＆夜用パック10選",
        "desc": "暖房乾燥でしぼんだ肌に潤い集中チャージ！トリデン、ルルルン、バイオダンスなど話題の密着パック。",
        "footer_name": "シートマスク"
    },
    {
        "url": "/winter-moisture-cream",
        "file": "winter-moisture-cream.html",
        "title": "🧴 保湿力の強さで肌乾燥とさようなら！高保湿フェイスクリーム＆濃密バーム10選",
        "desc": "暖房下でも粉吹きゼロへ！キールズ、キュレル、コスメデコルテなど水分を閉じ込める最強クリーム。",
        "footer_name": "保湿クリーム"
    },
    {
        "url": "/winter-eye-cream",
        "file": "winter-eye-cream.html",
        "title": "👁️ 暖房直撃の目元・ほうれい線をふっくら密着！高保湿アイクリーム＆薬用リンクルケア10選",
        "desc": "夕方のちりめんジワ・ファンデ割れを撃退！純粋レチノール、ニールワン、リポソーム配合アイケア。",
        "footer_name": "アイクリーム"
    },
    {
        "url": "/winter-base-makeup",
        "file": "winter-base-makeup.html",
        "title": "✨ 夕方まで潤いツヤが続く高保湿ファンデーション＆美容液下地10選",
        "desc": "エアコン直撃でもひび割れない！クレ・ド・ポー ボーテ、SHISEIDOなど生ツヤ肌ベースメイク。",
        "footer_name": "ベースメイク"
    },
    {
        "url": "/winter-lip-care",
        "file": "winter-lip-care.html",
        "title": "🎁 冬のガサガサ皮剥けに終止符！高保湿リップトリートメント＆濃密ティント10選",
        "desc": "皮脂腺のない唇を乾燥冷風から守る！ラネージュスリーピングマスク、ディオールマキシマイザーなど。",
        "footer_name": "リップケア"
    },
    {
        "url": "/winter-body-care",
        "file": "winter-body-care.html",
        "title": "🛁 すねの粉吹き・全身の乾燥かゆみにサヨナラ！高保湿ボディミルク＆濃厚ボディバター10選",
        "desc": "お風呂上がりの全身をうるおいで包み込む！ニュートロジーナ、ニベア、キュレル、サボンなど厳選。",
        "footer_name": "ボディケア"
    },
    {
        "url": "/winter-hair-care",
        "file": "winter-hair-care.html",
        "title": "🌿 冬の静電気・毛先パサつきと完全決別！高保湿ヘアオイル＆濃厚ヘアマスク10選",
        "desc": "マフラー摩擦や暖房で傷んだキューティクルを補修。モロッカンオイル、ケラスターゼ、オルビスなど。",
        "footer_name": "ヘアケア"
    },
    {
        "url": "/winter-hand-care",
        "file": "winter-hand-care.html",
        "title": "🤲 手荒れ・あかぎれ・ささくれ知らずへ！神ハンドクリーム＆ネイルケア10選",
        "desc": "水仕事や冷風で荒れた手先を即効リペア。ベタつかないデスク用から夜の集中補修バームまで。",
        "footer_name": "ハンドケア"
    },
    {
        "url": "/summer-cosme",
        "file": "summer-cosme.html",
        "title": "☀️ 夏の汗・皮脂でも崩れない！最新トレンドコスメ厳選10選",
        "desc": "皮脂崩れ防止下地やウォータープルーフコスメなど夏特有の肌悩みを解決する特集。",
        "footer_name": "夏コスメ"
    }
]

footer_links_html = '<div class="footer-links">\n      <a href="/">トップページ</a>\n' + "\n".join([f'      <a href="{a["url"]}">{a["footer_name"]}</a>' for a in ALL_ARTICLES]) + '\n    </div>'

for target_article in ALL_ARTICLES:
    file_path = target_article["file"]
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 関連記事リスト構築（自分自身を除く）
    related_cards = []
    for a in ALL_ARTICLES:
        if a["file"] == file_path:
            continue
        related_cards.append(f"""        <a href="{a['url']}" class="related-link-card">
          <div class="related-link-title">{a['title']}</div>
          <div class="related-link-desc">{a['desc']}</div>
        </a>""")

    new_related_section = f"""<section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list">
{chr(10).join(related_cards)}
      </div>
    </section>"""

    # 置換
    if '<section id="related"' in content:
        content = re.sub(r'<section id="related".*?</section>', new_related_section, content, flags=re.DOTALL)
    else:
        content = content.replace('</main>', f'{new_related_section}\n  </main>')

    # フッターリンク置換
    if '<div class="footer-links">' in content:
        content = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated internal links for {file_path}")

print("All article files successfully updated with comprehensive internal cross-links!")
