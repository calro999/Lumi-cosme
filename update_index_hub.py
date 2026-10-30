import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 最新3記事のカード定義
latest_cards = """      <!-- 高保湿ナイトクリーム -->
      <a href="/winter-night-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #9d174d;">🌙 睡眠中集中リペア・翌朝もっちり肌 NEW</span>
        <h2 class="hub-card-title">🌙 保湿力の強さで睡眠中の砂漠肌・乾燥小ジワとさようなら！翌朝もっちり吸い付く高保湿ナイトクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の冬乾燥を睡眠中に集中リペア！コスメデコルテ、KANEBO、エリクシール、キュレル、オルビス、SK-IIなど、翌朝ふっくらハリ肌へ導く高保湿ナイトクリーム10選。</p>
      </a>

      <!-- 高保湿クレンジングミルク -->
      <a href="/winter-cleansing-milk" class="hub-card">
        <span class="hub-card-tag" style="background: #f0fdf4; color: #166534;">🥛 洗い上がりツッパリ摩擦ゼロ・美容液洗顔 NEW</span>
        <h2 class="hub-card-title">🥛 保湿力の強さで冬の洗い上がりツッパリ・摩擦乾燥とさようなら！うるおい残して優しく落とす高保湿クレンジングミルクランク10</h2>
        <p class="hub-card-desc">11月・12月の洗顔後ツッパリ・摩擦ダメージ・乾燥小ジワを徹底解決！カバーマーク、カウブランド、チャントアチャーム、シスレー、ヴェレダなどうるおい守る高保湿ミルク10選。</p>
      </a>

      <!-- 高保湿ヘアミスト -->
      <a href="/winter-hair-mist" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #1e40af;">✨ 冬の静電気・毛先パサつき防止ヘアミスト NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで冬の静電気・毛先パサつきとさようなら！髪にうるおいヴェールをまとう高保湿ヘアミストランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の静電気・マフラー摩擦・暖房乾燥による髪のパサパサ・ボサボサを瞬時に解消！ジルスチュアート、スティーブンノル、オルビス、ナプラ、ReFaなど高保湿ミスト10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-night-cream' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + latest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
