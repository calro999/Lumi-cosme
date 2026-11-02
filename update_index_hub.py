import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 米発酵・ライスパワー高保湿 -->
      <a href="/winter-rice-power" class="hub-card">
        <span class="hub-card-tag" style="background: #fef3c7; color: #92400e;">🌾 水分保持能改善・セラミド自給力 NEW</span>
        <h2 class="hub-card-title">🌾 保湿力の強さで肌乾燥とさようなら！自らうるおう力を育む米発酵・ライスパワー高保湿ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化するインナードライ・粉吹き乾燥を根本解決！日本で唯一『水分保持能を改善する』医薬部外品認可のライスパワーNo.11や純米コメ発酵液を配合した高保湿スキンケア10選を徹底比較！ONE BY KOSE、米肌、ライスフォース、菊正宗、松山油脂など厳選。</p>
      </a>

      <!-- 高純度椿油 -->
      <a href="/winter-camellia-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #ffe4e6; color: #be123c;">🌺 オレイン酸85%・日本伝統ツヤ膜 NEW</span>
        <h2 class="hub-card-title">🌺 保湿力の強さで肌乾燥とさようなら！日本の冬を潤すオレイン酸85%の極上ツヤ膜・高純度椿油ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化する皮脂枯れ・粉吹き乾燥を徹底解決！人の皮脂成分オレイン酸が約85%と極めて酸化しにくい日本古来の最高峰高保湿植物油・純椿油10選を徹底比較！大島椿、黒バラ本舗、かづら清老舗、五島特産、よーじやなど厳選。</p>
      </a>

      <!-- 高浸透アミノ酸 -->
      <a href="/winter-amino-acid" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0284c7;">💧 NMF集中補給・角層内部保水 NEW</span>
        <h2 class="hub-card-title">💧 保湿力の強さで肌乾燥とさようなら！天然保湿因子NMFを速攻チャージして乾きを断つ高浸透アミノ酸コスメランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化する角層バリア破壊・インナードライを徹底解決！肌の天然保湿因子NMFの主成分である高浸透アミノ酸を配合した高保湿スキンケア10選を徹底比較！ミノン アミノモイスト、松山油脂、味の素Jino、キュレル、ドクターシーラボなど厳選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-rice-power' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
