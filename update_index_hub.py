import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新3記事のカード定義
new_cards = """      <!-- 高保湿クリスマスコフレ＆ホリデーコレクション -->
      <a href="/winter-holiday-coffret" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #be185d;">🎁 11月・12月限定ホリデーコレクション＆高保湿コフレ NEW</span>
        <h2 class="hub-card-title">🎁 贅沢なうるおいと輝きで真冬の乾燥肌・メイクを特別格上げ！11月12月限定ホリデーコレクション＆高保湿クリスマスコフレランク10</h2>
        <p class="hub-card-desc">11月・12月限定の争奪戦コフレを厳選！コスメデコルテ、ディオール、ルナソル、SABON、キールズ、SK-IIなど、冬の乾燥肌を高保湿ケアしながら特別な輝きを添える名品10選。</p>
      </a>

      <!-- 高保湿酵素洗顔パウダー -->
      <a href="/winter-enzyme-wash" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #1d4ed8;">🫧 角質肥厚リセット・つっぱらず透明感を呼び覚ます酵素洗顔 NEW</span>
        <h2 class="hub-card-title">🫧 保湿力の強さで冬の角質ゴワつき・くすみ毛穴とさようなら！つっぱらず透明感を呼び覚ます高保湿酵素洗顔パウダーランク10</h2>
        <p class="hub-card-desc">冬の寒さと乾燥で硬くなった角質ゴワつき・くすみ毛穴を救う！オバジC、suisaiゴールド、ファンケル、カネボウ、estなど、つっぱらず透明感を呼び覚ます高保湿酵素洗顔10選。</p>
      </a>

      <!-- 高保湿カラーリップバーム -->
      <a href="/winter-tinted-lip-balm" class="hub-card">
        <span class="hub-card-tag" style="background: #fff1f2; color: #e11d48;">💄 唇の皮剥け＆血色レス撃退・ひと塗りでぷるんと潤う高保湿バーム NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで冬のカサカサ唇＆血色レスとさようなら！ひと塗りでぷるんと潤う高保湿カラーリップバームランク10</h2>
        <p class="hub-card-desc">冬の寒風・エアコン乾燥による唇の皮剥け・縦ジワ・血色不良を救う！ディオール、シャネル、KANEBO、NARS、ボビイ ブラウンなど、高保湿と透け感美発色を両立した神カラーリップバーム10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-holiday-coffret' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 new cards and latest footer links!")
