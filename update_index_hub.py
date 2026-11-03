import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高純度プロテオグリカン原液 -->
      <a href="/winter-proteoglycan" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">🧬 ヒアルロン酸超え保水・EGF様作用 NEW</span>
        <h2 class="hub-card-title">🧬 保湿力の強さで肌乾燥とさようなら！ヒアルロン酸超えの保水力で乾燥小ジワを撃退する高純度プロテオグリカン原液ランク10</h2>
        <p class="hub-card-desc">11月・12月の真冬乾燥に！ヒアルロン酸の約1.3倍の保水力とEGF様作用で乾燥小ジワを撃退する高純度プロテオグリカン原液10選を徹底比較！フラコラ、KISO、自然化粧品研究所、あおもりPG認証原液など厳選。</p>
      </a>

      <!-- 高保湿プロポリスアンプル -->
      <a href="/winter-propolis" class="hub-card">
        <span class="hub-card-tag" style="background: #fef3c7; color: #b45309;">🐝 濃密蜜膜ヴェール・極上水光ツヤ NEW</span>
        <h2 class="hub-card-title">🐝 保湿力の強さで肌乾燥とさようなら！濃密な栄養と蜜膜ヴェールで肌荒れ・粉吹きを防ぐ高保湿プロポリスアンプルランク10</h2>
        <p class="hub-card-desc">11月・12月の真冬乾燥に！濃密な栄養と蜜膜ヴェールで肌荒れ・粉吹きを防ぎ極上の水光ツヤ肌を叶える高保湿プロポリスアンプル10選を徹底比較！CNP、COSRX、スキンフード、バイオヒールボなど厳選。</p>
      </a>

      <!-- 高浸透ガラクトミセス美容液 -->
      <a href="/winter-galactomyces" class="hub-card">
        <span class="hub-card-tag" style="background: #ccfbf1; color: #0f766e;">🍶 酵母発酵NMF産生・透明感ブースト NEW</span>
        <h2 class="hub-card-title">🍶 保湿力の強さで肌乾燥とさようなら！角層の水分密度を極限まで高めて冬のくすみを晴らす高浸透ガラクトミセス美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の真冬乾燥に！角層の水分密度を極限まで高めて冬のくすみを晴らす高浸透ガラクトミセス美容液10選を徹底比較！魔女工場、SK-II、COSRX、KISOなど厳選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-proteoglycan' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
