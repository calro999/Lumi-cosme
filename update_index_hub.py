import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 最新3記事のカード定義
latest_cards = """      <!-- 高保湿クレンジングジェル -->
      <a href="/winter-cleansing-gel" class="hub-card">
        <span class="hub-card-tag" style="background: #fff7ed; color: #c2410c;">🫧 摩擦ゼロ・毛穴ほぐし高保湿ジェル NEW</span>
        <h2 class="hub-card-title">🫧 保湿力の強さで冬の摩擦ダメージ・洗い上がり突っ張りとさようなら！毛穴汚れも優しく包み落とす高保湿クレンジングジェルランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の乾燥・毛穴冷え・摩擦ダメージを徹底解決！マナラ、キュレル、サンタマルシェ、オルビス、エストなど、厚みのあるクッションジェルで洗い上がりのつっぱりを防ぎ、毛穴汚れも摩擦レスに落とす神高保湿クレンジングジェル10選。</p>
      </a>

      <!-- 高保湿角質柔軟美容液・ピールセラム -->
      <a href="/winter-peel-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #f0fdfa; color: #0f766e;">💧 角質ゴワつき解消・化粧水浸透ブースター NEW</span>
        <h2 class="hub-card-title">💧 保湿力の強さで冬の角質ゴワつき・化粧水はじき砂漠肌とさようなら！うるおい浸透を呼び覚ます高保湿角質柔軟美容液・ピールセラムランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の角質肥厚・化粧水が浸透しないインナードライを根本解決！タカミスキンピール、ラロッシュポゼ、CNP、ソフィーナiPなど、剥がさず肌代謝を整えて化粧水の吸い込みを爆上げする神高保湿ピールセラム10選。</p>
      </a>

      <!-- 高保湿リップセラム・唇用美容液 -->
      <a href="/winter-lip-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #be185d;">💄 唇の皮剥け・縦ジワ集中リペア美容液 NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで冬の唇皮剥け・砂漠縦ジワとさようなら！24時間ぷるんと満たす高保湿リップセラム・唇用美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の深刻な唇の皮剥け・出血・縦ジワ・しぼみを徹底リペア！コスメデコルテ、オバジ、タカミ、トリデン、ディオールなど、固形バームでは届かない深層まで潤いを届けふっくら満たす神高保湿リップセラム10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-cleansing-gel' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + latest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
