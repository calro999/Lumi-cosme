import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 薬用ヘパリン類似物質コスメ -->
      <a href="/winter-heparinoid" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">🧪 医薬部外品・保水構造再建 NEW</span>
        <h2 class="hub-card-title">🧪 保湿力の強さで肌乾燥とさようなら！角層深部の保水構造を立て直す薬用ヘパリン類似物質コスメランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化するインナードライ・粉吹き乾燥を根本解決！角層深部の水分保持能を立て直す薬用ヘパリン類似物質コスメ10選を徹底比較！カルテHD、アドライズ、ヒルメナイド、ヘパソフト、ピアソンHPなど厳選。</p>
      </a>

      <!-- 高純度ワセリン -->
      <a href="/winter-vaseline" class="hub-card">
        <span class="hub-card-tag" style="background: #d1fae5; color: #047857;">🛡️ 水分蒸発ゼロ・鉄壁保護シールド NEW</span>
        <h2 class="hub-card-title">🛡️ 保湿力の強さで肌乾燥とさようなら！水分蒸発をゼロに抑えて冬の冷風から守り抜く高純度ワセリンランク10</h2>
        <p class="hub-card-desc">11月・12月の真冬乾燥に！水分蒸発をゼロに抑えて外気刺激を完全遮断する高純度ワセリン10選を徹底比較！サンホワイト、プロペト、ベビーワセリン、IHADA薬用バームなど厳選。</p>
      </a>

      <!-- 高濃度プラセンタ原液 -->
      <a href="/winter-placenta" class="hub-card">
        <span class="hub-card-tag" style="background: #f3e8ff; color: #7e22ce;">✨ アミノ酸＆成長因子・エイジング保湿 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥とさようなら！冬の代謝低下とハリ不足を跳ね返す高濃度プラセンタ原液ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬枯れ肌に！アミノ酸と成長因子が代謝低下とハリ不足を跳ね返す高濃度プラセンタ原液10選を徹底比較！フラコラ、Bbラボラトリーズ、チューンメーカーズ、KISOなど厳選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-heparinoid' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
