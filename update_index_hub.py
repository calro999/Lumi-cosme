import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新3記事のカード定義
new_cards = """      <!-- 高保湿ハンド美容液・ハンドセラム -->
      <a href="/winter-hand-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #ecfdf5; color: #047857;">🤲 スマホ操作サラリ・老け手＆乾燥シワ撃退・高浸透 NEW</span>
        <h2 class="hub-card-title">🤲 保湿力の強さで手荒れ・老け手・乾燥シワとさようなら！スマホ操作もサラリと快適＆手肌のキメをふっくら満たす高保湿ハンド美容液・ハンドセラムランク10</h2>
        <p class="hub-card-desc">冬の寒風・手洗い・消毒による手荒れや乾燥小ジワを救う！SHIRO、アルビオンエクシア、アユーラ、オサジ、コスメデコルテなど、ベタつかずスマホも快適操作できる神高保湿ハンド美容液厳選10選。</p>
      </a>

      <!-- 極上高保湿バスオイル -->
      <a href="/winter-bath-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">🛁 湯上がり乾燥ゼロ・お風呂で全身シルク膜・極上温活 NEW</span>
        <h2 class="hub-card-title">🛁 保湿力の強さで冬の湯上がり乾燥・粉吹きとさようなら！お風呂に浸かるだけで全身シルク肌へ導く極上高保湿バスオイルランク10</h2>
        <p class="hub-card-desc">真冬の脱衣所での急激な乾燥・粉吹き・かゆみを救う！ジョーマローン、アユーラ、アロマセラピーアソシエイツ、ポールシェリー、ヴェレダなど、お風呂上がりボディクリーム不要の極上高保湿バスオイル厳選10選。</p>
      </a>

      <!-- 超濃密高保湿ボディバター -->
      <a href="/winter-body-butter" class="hub-card">
        <span class="hub-card-tag" style="background: #fef3c7; color: #b45309;">🧴 粉吹きすね救済・シアバター濃厚密着・96時間保湿 NEW</span>
        <h2 class="hub-card-title">🧴 保湿力の強さで冬の粉吹き肌・乾燥かゆみとさようなら！こっくり濃厚ヴェールで全身を包み込む神高保湿ボディバターランク10</h2>
        <p class="hub-card-desc">真冬のすねの粉吹き・乾燥かゆみ・ひじひざのガサガサを救う！ザボディショップ、ローラメルシエ、キールズ、ロクシタン、サボンなど、こっくり濃厚エモリエント膜で一晩中うるおいを守り抜く神高保湿ボディバター厳選10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-hand-serum' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 new cards and latest footer links!")
