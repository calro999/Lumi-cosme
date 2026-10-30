import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 最新3記事のカード定義
latest_cards = """      <!-- 高保湿クレンジングバーム -->
      <a href="/winter-cleansing-balm" class="hub-card">
        <span class="hub-card-tag" style="background: #f0fdf4; color: #15803d;">🫧 体温でとろける高保湿クレンジングバーム NEW</span>
        <h2 class="hub-card-title">🫧 保湿力の強さで冬の突っ張り・乾燥小じわとさようなら！体温でとろけて毛穴汚れもつるんと落とす高保湿クレンジングバームランク10</h2>
        <p class="hub-card-desc">11月・12月の冬乾燥を救う！DUO、パーフェクトワンフォーカス、ルルルン、クリニーク、KANEBOなど、体温でとろけて毛穴の角栓・濃密メイクを摩擦レスに落とす神バーム10選。</p>
      </a>

      <!-- 高保湿スカルプシャンプー -->
      <a href="/winter-scalp-shampoo" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #1d4ed8;">🌿 頭皮砂漠化・フケかゆみ予防アミノ酸スカルプ NEW</span>
        <h2 class="hub-card-title">🌿 保湿力の強さで頭皮乾燥・フケかゆみとさようなら！うるおい守る高保湿スカルプシャンプーランク10</h2>
        <p class="hub-card-desc">11月・12月の厳しい寒さとエアコン暖房による頭皮の砂漠化、乾性フケ、かゆみをブロック！haru、オージュア、キュレル、エトヴォス、カダソンなどアミノ酸高保湿シャンプー10選。</p>
      </a>

      <!-- 高保湿シカクリーム -->
      <a href="/winter-cica-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #be185d;">🌱 寒風赤み・肌荒れ急速リペア高保湿CICA NEW</span>
        <h2 class="hub-card-title">🌱 保湿力の強さで冬の肌荒れ・寒風赤みとさようなら！肌バリアを集中強化する高保湿シカクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の冷たい北風と暖房乾燥による赤ら顔、ヒリつき、粉吹き肌荒れを急速リペア！ラロッシュポゼ、VT、Dr.Jart+、アベンヌ、Dr.Gなど肌バリア集中強化シカクリーム10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-cleansing-balm' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + latest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
