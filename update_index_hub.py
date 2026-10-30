import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新3記事のカード定義
new_cards = """      <!-- 高保湿リップスクラブ -->
      <a href="/winter-lip-scrub" class="hub-card">
        <span class="hub-card-tag" style="background: #fce7f3; color: #9d174d;">💄 唇の皮剥け・縦ジワ撃退・ぷるツヤ唇 NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで唇のガサガサ皮剥け・縦ジワとさようなら！古い角質を優しくオフしてぷるんと潤う高保湿リップスクラブランク10</h2>
        <p class="hub-card-desc">冬の北風と暖房乾燥でガサガサに皮剥けした唇を救う！レブロン、キャンメイク、ディオール、LUSH、ハウスオブローゼなど高保湿リップスクラブ厳選10選。</p>
      </a>

      <!-- 高保湿BB・CCクリーム -->
      <a href="/winter-bb-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #fef3c7; color: #92400e;">✨ 朝の粉ふき・乾燥崩れ防止・うるツヤ美肌 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで冬の粉ふき・乾燥崩れとさようなら！1本で一日中うるツヤ肌が続く高保湿BB・CCクリームランク10</h2>
        <p class="hub-card-desc">冬の朝の冷え込みと乾燥によるファンデの粉吹き・ひび割れを撃退！コスメデコルテ、dプログラム、マキアージュ、ラロッシュポゼなど高保湿BB・CCクリーム厳選10選。</p>
      </a>

      <!-- 高保湿炭酸パック -->
      <a href="/winter-carbonic-pack" class="hub-card">
        <span class="hub-card-tag" style="background: #ccfbf1; color: #115e59;">🫧 冬の冷えくすみ・血行不良撃退・サロン級発光 NEW</span>
        <h2 class="hub-card-title">🫧 保湿＆血行促進で冬の冷えくすみ・ゴワつきとさようなら！サロン級の透明感と弾力を呼び覚ます高保湿炭酸パック・炭酸マスクランク10</h2>
        <p class="hub-card-desc">冬の寒波による血行不良・くすみ・ゴワつく角質を撃退！エニシーグローパック、EKATO、ドクターメディオンなど高保湿炭酸パック厳選10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-lip-scrub' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 new cards and latest footer links!")
