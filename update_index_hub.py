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
newest_cards = """      <!-- 高保湿セラミド乳液 -->
      <a href="/winter-ceramide-milk" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">🧴 ラメラ液晶乳化・水分油分バリア NEW</span>
        <h2 class="hub-card-title">🧴 保湿力の強さで肌乾燥とさようなら！角層ラメラ液晶を満たして水分蒸散をブロックする保湿力高めセラミド乳液ランク10</h2>
        <p class="hub-card-desc">11月・12月の暖房乾燥・インナードライ・角層硬化を救う高保湿セラミド乳液10選を徹底検証！ケアセラ、キュレル、ミノン、エトヴォス、松山油脂までヒト型セラミドとラメラ液晶乳化の科学的根拠と共に紹介。</p>
      </a>

      <!-- 高保湿夜用美容液 -->
      <a href="/winter-night-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #eef2ff; color: #3730a3;">🌙 時計遺伝子同調・夜間集中修復 NEW</span>
        <h2 class="hub-card-title">🌙 保湿力の強さで肌乾燥とさようなら！睡眠中の細胞修復と濃密水分チャージを極める保湿力高め夜用美容液・ナイトセラムランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥や暖房ダメージを寝ている間に集中リセット！エスティローダー、コスメデコルテ、YSL、クラランス、キールズまでサーカディアンリズムと持続放出リポソームの科学的根拠と共に紹介。</p>
      </a>

      <!-- 高保湿アイセラム -->
      <a href="/winter-eye-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #ecfdf5; color: #047857;">👁️ 極薄目元防護・冷却アプリケーター NEW</span>
        <h2 class="hub-card-title">👁️ 保湿力の強さで肌乾燥とさようなら！薄膜目元の乾燥小ジワ・くぼみを潤いで押し戻す保湿力高めアイセラム（目元美容液）ランク10</h2>
        <p class="hub-card-desc">11月・12月の暖房直撃と寒冷乾燥から極薄目元を守る高保湿アイセラム10選を徹底検証！ランコム、エスティローダー、クラランス、ディオール、コスメデコルテまで解剖学的根拠とアプリケーター工学と共に紹介。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-ceramide-milk' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
