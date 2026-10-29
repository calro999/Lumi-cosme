import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新3記事のカード定義
new_cards = """      <!-- 高保湿メイクキープミスト -->
      <a href="/winter-make-keep-mist" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">✨ 暖房崩れ・粉吹き・マフラー摩擦防止 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥・粉吹きとさようなら！暖房直撃でもうるツヤ肌を一日中ロックする高保湿メイクキープミストランク10</h2>
        <p class="hub-card-desc">冬の暖房乾燥による粉吹き・ひび割れ・マフラー摩擦を完全防御！コーセー、コスメデコルテ、ディオール、クラランス、ダルバなど高保湿ミスト10選。</p>
      </a>

      <!-- 高保湿リップオイル -->
      <a href="/winter-lip-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #fce7f3; color: #be185d;">💄 唇の皮剥け・縦ジワ消滅・ガラス玉ツヤ NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで唇のガサガサ皮剥けとさようなら！濃密植物オイルでガラス玉のようなぷるツヤ唇を叶える高保湿リップオイルランク10</h2>
        <p class="hub-card-desc">冬の皮剥け・縦ジワを濃密植物オイルで集中トリートメント！クラランス、ディオール、ジバンシイ、シャネル、エクセルなど極上リップオイル10選。</p>
      </a>

      <!-- 高保湿ボディオイル -->
      <a href="/winter-body-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #fef3c7; color: #b45309;">🛁 すねの粉吹き・乾燥かゆみ・冷えむくみ解消 NEW</span>
        <h2 class="hub-card-title">🛁 保湿力の強さで全身の乾燥かゆみ・粉吹きとさようなら！お風呂上がりの肌をとろけるシルクへ導く高保湿ボディオイルランク10</h2>
        <p class="hub-card-desc">すねの粉吹き・乾燥かゆみ・冷えむくみを完全解消！ヴェレダ、クラランス、ニュクス、バイオイル、メルヴィータなど高保湿ボディオイル10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-make-keep-mist' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with new article cards and footer links!")
