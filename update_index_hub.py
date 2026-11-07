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
newest_cards = """      <!-- 高保湿PDRNクリーム -->
      <a href="/winter-pdrn-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #ffe4e6; color: #be123c;">🧬 サーモンDNA・細胞修復・しぼみ肌救済 NEW</span>
        <h2 class="hub-card-title">🧬 保湿力の強さで肌乾燥とさようなら！サーモンDNAの細胞修復力で真冬のしぼみ肌を底上げする保湿力高めPDRNクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の暖房乾燥・角層脱水・冬のしぼみ肌を救う高保湿PDRNクリーム10選を徹底検証！VT、メディキューブ、Anua、リジュラン、センテリアン24までサーモンDNAの生化学的根拠とエモリエント密閉技術と共に紹介。</p>
      </a>

      <!-- 高保湿グルタチオンクリーム -->
      <a href="/winter-glutathione-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #f3e8ff; color: #7e22ce;">✨ 白玉抗酸化・発光水分シールド NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥とさようなら！白玉のような発光透明感と濃密水分シールドで真冬の枯れ肌を救う保湿力高めグルタチオンクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥・血行不良による冬の土気色くすみ・乾燥しぼみ肌を救う高保湿グルタチオンクリーム10選を徹底検証！ナンバーズイン、メディキューブ、バイオヒールボ、Dr.Gまで白玉抗酸化ペプチドの生化学的根拠とエモリエント密閉技術と共に紹介。</p>
      </a>

      <!-- 高保湿セラミドリップ -->
      <a href="/winter-ceramide-lip" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #be185d;">💄 唇ラメラ液晶修復・皮むけ根本撃退 NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで肌乾燥とさようなら！めくれる皮むけ・ひび割れを角層ラメラで密閉修復する保湿力高めセラミドリップランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥・エアコン暖房による唇のめくれる皮むけ・ひび割れ・縦ジワを救う高保湿セラミドリップ10選を徹底検証！ケアセラ、キュレル、タカミ、エトヴォス、トリデンまで角層ラメラ液晶修復の生化学的根拠と共に紹介。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-pdrn-cream' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
