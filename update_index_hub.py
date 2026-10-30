import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新3記事のカード定義
new_cards = """      <!-- 高保湿ヘアバーム -->
      <a href="/winter-hair-balm" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #9d174d;">💆‍♀️ 毛先パサつき・静電気ブロック・濡れツヤ全身保湿 NEW</span>
        <h2 class="hub-card-title">💆‍♀️ 保湿力の強さで毛先のパサつき・静電気・広がりとさようなら！冬の冷風から一日中うるおいキープ＆全身保湿できるマルチ高保湿ヘアバームランク10</h2>
        <p class="hub-card-desc">冬の寒風・乾燥・マフラー静電気でパサつく髪を救う！ザ・プロダクト、N.（エヌドット）、track（トラック）、ミルボンなど、毛先のうるおい束感キープから手肌・リップの保湿まで叶える神ヘアバーム厳選10選。</p>
      </a>

      <!-- 高保湿温感クレンジング -->
      <a href="/winter-hot-cleansing" class="hub-card">
        <span class="hub-card-tag" style="background: #ffedd5; color: #9a3412;">🫧 冷え固まった毛穴溶解・スチーム温活・美容液90% NEW</span>
        <h2 class="hub-card-title">🫧 保湿＆温感スチーム効果で冬の冷え固まった毛穴・乾燥ゴワつきとさようなら！じんわり温めてうるおいを守り抜く高保湿温感クレンジングランク10</h2>
        <p class="hub-card-desc">冬の寒さで冷え固まった毛穴の角栓・乾燥ゴワつきを撃退！マナラ、DUO（デュオ）、スキンビル、ベネフィーク、ラフラなど、じんわり温感スチーム＆美容液成分90%超で洗い上げる高保湿温感クレンジング厳選10選。</p>
      </a>

      <!-- 高保湿ネック＆デコルテクリーム -->
      <a href="/winter-neck-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #ede9fe; color: #5b21b6;">✨ 首の横ジワ・マフラーチクチク摩擦防止・首元リフト NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで首元の乾燥小ジワ・マフラー摩擦とさようなら！冬のタートルネック映えするハリツヤ肌へ導く高保湿ネック＆デコルテクリームランク10</h2>
        <p class="hub-card-desc">冬のタートルネックやマフラーのチクチク摩擦、乾燥で深まる首の横ジワを救う！クラランス、資生堂リバイタル、ポーラ、シスレー、肌美精など、首元専用の高保湿ネック＆デコルテクリーム厳選10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-hair-balm' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 new cards and latest footer links!")
