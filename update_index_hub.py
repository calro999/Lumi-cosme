import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿エクソソーム美容液 -->
      <a href="/winter-exosome-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f4; color: #c94b6e;">🧬 次世代細胞サイエンス・ハリ密度再生 NEW</span>
        <h2 class="hub-card-title">🧬 保湿力の強さで冬の肌荒れ・しぼみ肌とさようなら！次世代細胞サイエンスで角層深部から押し返す高保湿エクソソーム美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の寒気と暖房直撃による大人のしぼみ肌・たるみ毛穴・乾燥小ジワを徹底解決！2026年最新の次世代エイジングケア成分「高純度エクソソーム」を配合した高保湿美容液10選を徹底比較！メディキューブ、KISO、フラコラ、GD11、ディレイアなど厳選。</p>
      </a>

      <!-- 高保湿バスミルク -->
      <a href="/winter-bath-milk" class="hub-card">
        <span class="hub-card-tag" style="background: #e6fffa; color: #319795;">🛁 お湯が極上美容液に・全身粉吹き撃退 NEW</span>
        <h2 class="hub-card-title">🛁 保湿力の強さで冬の全身粉吹き乾燥・かゆみとさようなら！お湯が極上美容液に変わる高保湿バスミルク・薬用ミルク入浴液ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化する全身の粉吹き乾燥・すねのかゆみ・入浴後の急速乾燥を徹底解決！お湯を乳白色の極上モイストベールに変える高保湿バスミルク・薬用ミルク入浴液10選！アユーラ、キュレル、カウブランド、ミノン、ヴェレダなど厳選。</p>
      </a>

      <!-- 高保湿白玉グルタチオン美容液 -->
      <a href="/winter-glutathione-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #faf5ff; color: #805ad5;">✨ 白玉点滴発想・冬のどんよりくすみ一掃 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで冬のどんより乾燥くすみ・透明感不足とさようなら！濃密保湿×白玉グルタチオンで発光ツヤ肌へ導く高保湿グルタチオン美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の寒冷と暖房乾燥によるどんより血行不良くすみ・色ムラ・透明感低下を徹底解決！美容医療の白玉点滴発想で話題の「高純度グルタチオン」を配合した高保湿美容液10選！ナンバーズイン、アヌア、メディキューブ、BIOHEAL BOH、KISOなど厳選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-exosome-serum' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
