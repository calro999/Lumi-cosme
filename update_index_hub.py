import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿アルガンオイル -->
      <a href="/winter-argan-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #fef3c7; color: #92400e;">🥑 モロッコの黄金・角質柔軟ブースター NEW</span>
        <h2 class="hub-card-title">🥑 保湿力の強さで肌乾燥とさようなら！モロッコの黄金オイルでふっくら極上やわらか肌へ導く高保湿アルガンオイルランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化するゴワつき・砂漠乾燥・角質硬化を徹底解決！モロッコ南西部のみに自生するアルガンの樹から抽出された高純度オーガニックアルガンオイル10選を徹底比較！メルヴィータ、コディナ、spa hinoki、生活の木、ナイアード、マカダミ屋など厳選。</p>
      </a>

      <!-- 高保湿馬油クリーム -->
      <a href="/winter-horse-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #fed7aa; color: #9a3412;">🐴 人肌皮脂類似・粉吹きひび割れ救済 NEW</span>
        <h2 class="hub-card-title">🐴 保湿力の強さで頑固な肌乾燥・粉吹きとさようなら！人の皮脂に極めて近い天然脂質で包み込む高保湿馬油クリームランク10</h2>
        <p class="hub-card-desc">11月・12月の真冬の冷風と暖房直撃による深刻な粉吹き乾燥・ひび・あかぎれ・肌荒れを徹底解決！人の皮脂バランスに極めて酷似した天然不飽和脂肪酸が角層深部へ驚異のスピードで浸透する高保湿馬油10選を徹底比較！ソンバーユ、北海道純馬油本舗、リマーユ、ロッシモイストエイドなど厳選。</p>
      </a>

      <!-- 高保湿パンテノールクリーム -->
      <a href="/winter-panthenol-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #dbeafe; color: #1e40af;">🧪 プロビタミンB5・肌バリア鉄壁補修 NEW</span>
        <h2 class="hub-card-title">🧪 保湿力の強さで冬のヒリつき・敏感乾燥とさようなら！高濃度プロビタミンB5で角層バリアを鉄壁補修する高保湿パンテノールクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷刺激やエアコン乾燥によって引き起こされるバリア破壊・ヒリヒリ敏感肌・乾燥赤みを徹底修復！抗炎症＆組織再生を促進する高濃度プロビタミンB5（パンテノール）を配合した高保湿シカ＆バリアクリーム10選を徹底比較！ラロッシュポゼ シカプラストB5+、BIOHEAL BOH、アヌア、Dr.G、リアルバリアなど厳選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-argan-oil' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
