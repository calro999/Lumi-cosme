import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 最新3記事のカード定義
latest_cards = """      <!-- 高保湿クレンジングオイル -->
      <a href="/winter-cleansing-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #fff7ed; color: #c2410c;">🫧 毛穴詰まり・摩擦レス高保湿オイル NEW</span>
        <h2 class="hub-card-title">🫧 保湿力の強さで冬の頑固な毛穴詰まり・洗い上がりの砂漠化とさようなら！摩擦レスでうるおい守る高保湿クレンジングオイルランク10</h2>
        <p class="hub-card-desc">11月・12月の寒さで固まった毛穴の角栓・皮脂詰まりや濃密メイクを摩擦レスに浮かせながら、リッチな植物美容オイルで洗い上がりのつっぱり・乾燥を防ぐ神高保湿クレンジングオイル10選。</p>
      </a>

      <!-- 高保湿ボディミルク -->
      <a href="/winter-body-milk" class="hub-card">
        <span class="hub-card-tag" style="background: #f0fdfa; color: #0f766e;">🧴 全身の粉吹き・衣類摩擦防止エマルジョン NEW</span>
        <h2 class="hub-card-title">🧴 保湿力の強さで全身のカサカサ粉吹き・インナー摩擦乾燥とさようなら！スーッと浸透して服もすぐ着られる高保湿ボディミルクランク10</h2>
        <p class="hub-card-desc">11月・12月のタイツやヒートテックによる摩擦乾燥・すねの粉吹き・かゆみを撃退！水分と油分を黄金バランスで補給し、ベタつかず就寝前も快適に使える神高保湿ボディミルク10選。</p>
      </a>

      <!-- 高保湿トナーパッド -->
      <a href="/winter-toner-pad" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #1d4ed8;">💧 朝の3分水分爆弾チャージ・部分パック NEW</span>
        <h2 class="hub-card-title">💧 保湿力の強さで朝の乾燥ゴワつき・メイクの粉浮きとさようなら！貼るだけで水分爆弾チャージする高保湿トナーパッドランク10</h2>
        <p class="hub-card-desc">11月・12月の朝の暖房乾燥やインナードライによるメイクの粉浮き・毛穴目立ちを解決！美容液を贅沢に含んだパッドで部分パック＆角質ケアができる神高保湿トナーパッド10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-cleansing-oil' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + latest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
