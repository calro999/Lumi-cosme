import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 最新3記事のカード定義
latest_cards = """      <!-- 高保湿ハンドクリーム -->
      <a href="/winter-hand-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #ecfdf5; color: #047857;">🧤 水仕事でも落ちない・手荒れ救済 NEW</span>
        <h2 class="hub-card-title">🧤 保湿力の強さで冬の手荒れ・あかぎれひび割れ砂漠手肌とさようなら！水仕事でも落ちない高保湿ハンドクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の手荒れ・あかぎれ・水仕事乾燥・スマホのベタつきを徹底解決！ロクシタン、アトリックス、イソップ、ユースキン、ニュートロジーナ、ヘパソフト、シャネル、オサジなど、高純度シアバターやヘパリン類似物質配合の神高保湿ハンドクリーム10選。</p>
      </a>

      <!-- 高保湿レチノールクリーム -->
      <a href="/winter-retinol-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #fefce8; color: #a16207;">✨ 冬こそ始める・ふっくらハリ弾力覚醒 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで冬の小ジワ・乾燥毛穴たるみとさようなら！ふっくらハリ弾力を呼び覚ます高保湿レチノールクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の小ジワ・たるみ毛穴・A反応乾燥を徹底解決！エリクシール、キールズ、イニスフリー、COSRX、トゥヴェール、なめらか本舗、ドクターシーラボなど、高保湿バリア成分とピュアレチノール配合の神高保湿レチノールクリーム10選。</p>
      </a>

      <!-- 高保湿セラミド美容液 -->
      <a href="/winter-ceramide-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #1d4ed8;">💧 インナードライ撃退・角層バリア再構築 NEW</span>
        <h2 class="hub-card-title">💧 保湿力の強さで冬のインナードライ・バリア破壊赤み肌とさようなら！角層細胞を満たす高濃度ヒト型セラミド美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬のインナードライ・乾燥粉吹き・暖房赤み肌を徹底解決！コスメデコルテ、エトヴォス、キュレル、松山油脂、トゥヴェール、カネボウ、アスタリフトなど、高純度ヒト型セラミド配合の神高保湿セラミド美容液10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-hand-cream' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + latest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
