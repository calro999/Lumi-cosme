import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新3記事のカード定義
new_cards = """      <!-- 高保湿日焼け止め・UV美容液 -->
      <a href="/winter-uv-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #fef08a; color: #854d0e;">☀️ 冬の紫外線防御・夕方までツッパリ知らず NEW</span>
        <h2 class="hub-card-title">☀️ 保湿力の強さで冬の紫外線＆乾燥ツッパリとさようなら！まるで美容クリームな極上高保湿日焼け止め・UV美容液ランク10</h2>
        <p class="hub-card-desc">冬の乾燥と冷風に負けない！カネボウ ヴェイル オブ デイ、コスメデコルテ サンシェルター、オルビス、クレ・ド・ポー ボーテ、POLAなど高保湿UV10選。</p>
      </a>

      <!-- 高保湿シワ改善リンクルクリーム -->
      <a href="/winter-wrinkle-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #ede9fe; color: #5b21b6;">👁️ 乾燥小ジワ・ほうれい線撃退・真皮ハリ NEW</span>
        <h2 class="hub-card-title">👁️ 保湿力の強さで冬の乾燥小ジワ・ほうれい線とさようなら！角層深く密着する高保湿シワ改善リンクルクリームランク10</h2>
        <p class="hub-card-desc">冬の乾燥小ジワ・ほうれい線・ちりめんジワを撃退！エリクシール レチノパワー、POLA リンクルショット、コスデコ iP.Shot、KANEBOなど薬用リンクル10選。</p>
      </a>

      <!-- 高保湿ボディウォッシュ -->
      <a href="/winter-body-wash" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">🛁 お風呂上がりのかゆみ・すねの粉吹き防止 NEW</span>
        <h2 class="hub-card-title">🛁 保湿力の強さで冬のお風呂上がり乾燥・かゆみとさようなら！うるおいを守ってしっとり洗い上げる高保湿ボディウォッシュランク10</h2>
        <p class="hub-card-desc">脱衣所でのかゆみ・すねの粉吹きを元から防ぐ！ケアセラ、ミノン、キュレル、SABON、ロクシタンなどセラミド保持泡ソープ＆シャワーオイル10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-uv-cream' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with new article cards and footer links!")
