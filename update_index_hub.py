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
newest_cards = """      <!-- 高保湿レチノール美容液 -->
      <a href="/winter-retinol-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #faf5ff; color: #7e22ce;">✨ 濃密ビタミンA・毛穴小ジワ・A反応ゼロ NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥とさようなら！濃密ビタミンA×セラミド処方で真冬の乾燥小ジワと毛穴の開きをふっくら押し戻す保湿力高めレチノール美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の紫外線低下期こそ始めるベストシーズン！イニスフリー、VT、COSRX、キールズ、ラロッシュポゼまで、真冬でも皮むけしないエモリエントバッファリング技術と最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿ヒアルロン酸クリーム -->
      <a href="/winter-hyaluronic-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #f0f9ff; color: #0369a1;">💦 暖房インナードライ・5D多層水分爆弾 NEW</span>
        <h2 class="hub-card-title">💦 保湿力の強さで肌乾燥とさようなら！多層ヒアルロン酸の水分シールドで真冬の暖房インナードライを根本解決する保湿力高めヒアルロン酸クリームランク10</h2>
        <p class="hub-card-desc">11月・12月の暖房湿度20%下の乾燥砂漠を救う水分爆弾シールド！トリデン、ラネージュ、肌ラボ極潤プレミアム、Anua、Dr.Gまで多層複合ヒアルロン酸の保水メカニズムと最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿シカ美容液 -->
      <a href="/winter-cica-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #ecfdf5; color: #047857;">🌱 寒暖差赤み鎮静・高純度ツボクサ100% NEW</span>
        <h2 class="hub-card-title">🌱 保湿力の強さで肌乾燥とさようなら！高純度ツボクサエキスの急速鎮静力で寒暖差のピリピリ赤み肌をしっとり救う保湿力高めシカ美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の木枯らしと過熱暖房の寒暖差（温度差15℃）による急性皮膚炎を急速鎮静！SKIN1004、VT、ドクタージャルト、Anua、魔女工場まで高純度ツボクサの生化学的根拠と最新実勢価格・口コミを網羅してご紹介。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-retinol-serum' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
