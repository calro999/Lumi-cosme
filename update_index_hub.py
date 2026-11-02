import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿セラミド化粧水 -->
      <a href="/winter-ceramide-lotion" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">🧴 角層深透保水・インナードライ撃退 NEW</span>
        <h2 class="hub-card-title">🧴 保湿力の強さで肌乾燥とさようなら！角層深く浸透してバリアを守る高保湿セラミド化粧水ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化する冷気と暖房による角層バリア崩壊・深層インナードライ・粉吹き乾燥を徹底解決！ヒト型セラミドや疑似セラミドを贅沢配合した高保湿セラミド化粧水10選を徹底比較！セザンヌ、松山油脂、カルテHD、エトヴォス、ケアセラ、キュレル、菊正宗など厳選。</p>
      </a>

      <!-- 高保湿薬用リップクリーム -->
      <a href="/winter-medicinal-lip" class="hub-card">
        <span class="hub-card-tag" style="background: #fee2e2; color: #991b1b;">💄 唇ひび割れ・皮むけ集中治療 NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで唇の皮むけ・ひび割れとさようなら！荒れた唇を集中修復する高保湿薬用リップクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化する唇の皮むけ・血がにじむひび割れ・口角炎を徹底解決！医薬品有効成分やセラミドを贅沢配合した高保湿薬用リップクリーム10選を徹底比較！モアリップ、ユースキン、ヒビプロ、キュレル、アルージェ、オバジ、ニベア、DHCなど厳選。</p>
      </a>

      <!-- 高純度スクワランオイル -->
      <a href="/winter-squalane-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #d1fae5; color: #065f46;">✨ たった1滴・皮脂膜完全再現 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥とさようなら！たった1滴で極上ツヤ膜を張る高純度スクワランオイルランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化する皮脂分泌急落・粉吹き乾燥・小ジワを徹底解決！純度99.9%のスクワランや植物性シュガースクワランを贅沢配合した高純度スクワランオイル10選を徹底比較！HABA、無印良品、KISO、チューンメーカーズ、The Ordinaryなど厳選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-ceramide-lotion' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
