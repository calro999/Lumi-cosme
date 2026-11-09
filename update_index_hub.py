import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)
elif '<div class="footer-links-grid" id="footer-links-box">' in html:
    html = re.sub(r'<div class="footer-links-grid" id="footer-links-box">.*?</div>', '<div class="footer-links-grid" id="footer-links-box">\n' + footer_links_html + '\n          </div>', html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿コラーゲンクリーム -->
      <a href="/winter-collagen-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf4ff; color: #a21caf;">🐟 超低分子ナノコラーゲン・弾力ホールド NEW</span>
        <h2 class="hub-card-title">🐟 保湿力の強さで肌乾燥とさようなら！超低分子コラーゲンの弾力ホールド膜で真冬のしぼみ肌を跳ね返す保湿力高めコラーゲンクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥で萎縮した肌クッションを急速再構築！メディキューブ、バイオヒールボ、エチュード、アスタリフト、カナデルまで超低分子マリンコラーゲンの弾力ホールド膜と最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿スクワランクリーム -->
      <a href="/winter-squalane-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #f0f9ff; color: #0369a1;">💧 天然皮脂膜バリア・粉吹き完全密閉 NEW</span>
        <h2 class="hub-card-title">💧 保湿力の強さで肌乾燥とさようなら！天然皮脂膜バリアの生体親和性で真冬の粉吹き・脱水肌を完全密閉する保湿力高めスクワランクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の皮脂膜消失による粉吹き・角層脱水を救う生体親和性シールド！アンブリオリス、キールズUFC、松山油脂、キュレル、Dr.Gまで高純度フィトスクワランのエモリエント密閉技術と最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿ペプチドクリーム -->
      <a href="/winter-peptide-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #f5f3ff; color: #6d28d9;">🧬 多機能ペプチド・寒冷たるみ溝密度再建 NEW</span>
        <h2 class="hub-card-title">🧬 保湿力の強さで肌乾燥とさようなら！多機能ペプチド複合体の密度再建力で真冬の寒冷たるみと乾燥溝を押し上げる保湿力高めペプチドクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷たるみ・表情ジワ・肌密度低下を救う細胞シグナルケア！メディピール、ドクターペプチ、COSRX、ドクターシーラボ、ジオーディナリーまでマルチペプチドとボルフィリンの密度再建力と最新実勢価格・口コミを網羅してご紹介。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-collagen-cream' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
