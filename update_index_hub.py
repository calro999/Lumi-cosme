import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿シアバター -->
      <a href="/winter-shea-butter" class="hub-card">
        <span class="hub-card-tag" style="background: #fef3c7; color: #92400e;">🧈 天然濃厚ベール・全身密封保護 NEW</span>
        <h2 class="hub-card-title">🧈 保湿力の強さで肌乾燥とさようなら！天然の濃厚ベールで極上保護する高保湿シアバターランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化する皮脂枯れ・粉吹き乾燥・冷風刺激を徹底解決！西アフリカの大自然が育んだ天然植物油脂・シアバター100%バームから高濃度ブレンドクリームまで、高保湿シアバター10選を徹底比較！ロクシタン、ママバター、生活の木、spa hinokiなど厳選。</p>
      </a>

      <!-- 高保湿ホホバオイル -->
      <a href="/winter-jojoba-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #fef9c3; color: #854d0e;">🌿 皮脂膜成分補給・ブースター導入 NEW</span>
        <h2 class="hub-card-title">🌿 保湿力の強さで肌乾燥とさようなら！皮脂膜を補い真冬の肌を柔らかく包む高保湿ホホバオイルランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に急減する皮脂膜を補修！人間の皮脂と同じ『ワックスエステル』を豊富に含む高保湿ホホバオイル10選を徹底比較！無印良品、インカオイル、spa hinoki、生活の木、KISOなど、未精製ゴールデンから高純度精製クリアまで厳選。</p>
      </a>

      <!-- 高保湿尿素クリーム -->
      <a href="/winter-urea-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #dcfce7; color: #166534;">🦶 ガサガサかかと・角質柔軟治療 NEW</span>
        <h2 class="hub-card-title">🦶 保湿力の強さでガサガサ角質とさようなら！硬くなったかかと・ひじをしっとり柔らかく整える高保湿尿素クリームランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥でカチコチに硬化するガサガサかかと・ひび割れ・粉吹き肌を徹底解決！天然保湿因子NMFを補い角質を柔軟化する高保湿尿素クリーム10選を徹底比較！ケラチナミンコーワ、フェルゼア、資生堂尿素10%、メンソレータム、アトリックス、ユースキンなど厳選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-shea-butter' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
