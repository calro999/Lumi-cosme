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
newest_cards = """      <!-- 高保湿セラミドミスト -->
      <a href="/winter-ceramide-mist" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">🛡️ 暖房砂漠レスキュー・ヒト型セラミド NEW</span>
        <h2 class="hub-card-title">🛡️ 保湿力の強さで肌乾燥とさようなら！日中の暖房砂漠から角層バリアを守り抜く保湿力高めセラミドミストランク10</h2>
        <p class="hub-card-desc">11月・12月の暖房乾燥・オフィス砂漠から角層バリアを守る高保湿セラミドミスト10選を徹底検証！キュレル、エトヴォス、CNP、ミノン、ダルバまでヒト型セラミドと微細化技術の科学的根拠と共に紹介。</p>
      </a>

      <!-- 高保湿パンテノール美容液 -->
      <a href="/winter-panthenol-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #d1fae5; color: #047857;">🧬 プロビタミンB5・細胞間脂質合成修復 NEW</span>
        <h2 class="hub-card-title">🧬 保湿力の強さで肌乾燥とさようなら！損傷した角層バリアを深部から修復する保湿力高めパンテノール美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷刺激や暖房乾燥で傷んだ角層バリアを深部から修復する高保湿パンテノール（プロビタミンB5）美容液10選を徹底検証！バイオヒールボ、ラロッシュポゼ、ジオーディナリー、魔女工場まで細胞修復の生化学的根拠と共に紹介。</p>
      </a>

      <!-- 高保湿オイルイン化粧水 -->
      <a href="/winter-oil-in-lotion" class="hub-card">
        <span class="hub-card-tag" style="background: #fef3c7; color: #b45309;">✨ 水分×油分黄金比・冬の硬化角質柔軟 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥とさようなら！水分と上質オイルの黄金比で満たす保湿力高めオイルイン化粧水ランク10</h2>
        <p class="hub-card-desc">11月・12月の冷え固まった冬の硬化角質をほぐし、水分と良質オイルを同時にチャージする高保湿オイルイン化粧水10選を徹底検証！RMK、SHIRO、アルビオン、カネボウ、コスメデコルテまで二層式乳化処方の科学的根拠と共に紹介。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-ceramide-mist' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
