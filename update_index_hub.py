import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 最新3記事のカード定義
latest_cards = """      <!-- 高保湿ビタミンC美容液 -->
      <a href="/winter-vitamin-c-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #fffbeb; color: #b45309;">🍊 毛穴引き締め・乾燥くすみ解消 NEW</span>
        <h2 class="hub-card-title">🍊 保湿力の強さで冬の毛穴開き・乾燥くすみとさようなら！うるおい満ちる濃密高保湿ビタミンC美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の乾燥でしぼんだ毛穴・血行不良によるどんよりくすみを徹底解決！オバジC25、メラノCCプレミアム、キールズ、タカミ、Yunth生ビタミンCなど、冬でも乾燥・ピリつき知らずの高保湿ビタミンC美容液10選。</p>
      </a>

      <!-- 高保湿化粧下地プライマー -->
      <a href="/winter-makeup-primer" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #1d4ed8;">💧 美容液成分90%・粉吹き防止 NEW</span>
        <h2 class="hub-card-title">💧 保湿力の強さで冬のカサつき粉吹き・乾燥崩れとさようなら！うるおい満ちる高保湿化粧下地プライマーランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の暖房によるファンデ粉吹き・小ジワ割れ・乾燥崩れを徹底解決！ポール＆ジョー、クレ・ド・ポー ボーテ、コスメデコルテ、カネボウ、ボビイブラウンなど、一日中うるおいを閉じ込め極上ツヤ肌をキープする高保湿化粧下地10選。</p>
      </a>

      <!-- 高保湿クリームファンデーション -->
      <a href="/winter-cream-foundation" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #be185d;">✨ 最高峰の艶肌・擬似皮脂シールド NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで冬のカサつき・粉吹きファンデ割れとさようなら！極上ツヤ肌が続く高保湿クリームファンデーションランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の乾燥による粉吹き・小ジワ割れ・ファンデ浮きを徹底解決！SUQQU、KANEBO、クレ・ド・ポー ボーテ、コスメデコルテ、RMKなど、美容オイルとスキンケアエキスで肌を一日中密封ガードする高保湿クリームファンデーション10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-vitamin-c-serum' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + latest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
