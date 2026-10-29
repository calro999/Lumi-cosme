import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新3記事のカード定義
new_cards = """      <!-- 高保湿美容液リキッドファンデーション -->
      <a href="/winter-liquid-foundation" class="hub-card">
        <span class="hub-card-tag" style="background: #fef08a; color: #854d0e;">✨ 夕方の粉吹き・ひび割れ完全防止 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥・粉吹きとさようなら！美容液級のうるおいで一日中ひび割れ・毛穴落ちを防ぐ高保湿リキッドファンデーションランク10</h2>
        <p class="hub-card-desc">暖房直撃でも夕方の粉吹き・ひび割れ・毛穴落ちゼロ！資生堂エッセンススキングロウ、コスデコゼンウェアグロウ、ディオール、SUQQUなど美容液ファンデ10選。</p>
      </a>

      <!-- 高保湿クリーム＆リキッドチーク -->
      <a href="/winter-cream-cheek" class="hub-card">
        <span class="hub-card-tag" style="background: #fce7f3; color: #be185d;">🌸 冬の冷えくすみ一掃・生ツヤ血色 NEW</span>
        <h2 class="hub-card-title">🌸 保湿力の強さで肌乾燥・寒暖差くすみとさようなら！冬の冷え切った頬にじゅわっと上気ツヤを仕込む高保湿チークランク10</h2>
        <p class="hub-card-desc">冬の寒暖差による青白いくすみやパウダーチークの粉浮きを一掃！シャネル、アディクション、コスデコ、ローラメルシエなど高保湿クリーム＆リキッドチーク10選。</p>
      </a>

      <!-- 高保湿クリーム＆リキッドアイシャドウ -->
      <a href="/winter-cream-eyeshadow" class="hub-card">
        <span class="hub-card-tag" style="background: #e0e7ff; color: #3730a3;">👁️ まぶた乾燥・二重幅の粉落ち防止 NEW</span>
        <h2 class="hub-card-title">👁️ 保湿力の強さでまぶたの乾燥・二重幅の粉落ちとさようなら！濡れツヤと透明感を一日中キープする高保湿アイシャドウランク10</h2>
        <p class="hub-card-desc">冬の乾燥まぶたや二重幅のシワ溜まりを完全解決！コスメデコルテアイグロウジェム、ローラメルシエキャビアスティックなど高保湿クリーム＆リキッドアイシャドウ10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-liquid-foundation' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with new article cards and footer links!")
