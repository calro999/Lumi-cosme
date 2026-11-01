import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 濡れた肌用高保湿インバスボディミルク -->
      <a href="/winter-inbath-body" class="hub-card">
        <span class="hub-card-tag" style="background: #ecfeff; color: #0891b2;">🛁 脱衣所の極寒過乾燥ゼロ NEW</span>
        <h2 class="hub-card-title">🛁 保湿力の強さで冬の脱衣所極寒・粉吹き乾燥とさようなら！浴室で濡れたまま塗って即潤い閉じ込める高保湿インバスボディミルクランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の凍える脱衣所での寒冷ストレスと、お風呂上がりの急激な水分蒸発（過乾燥）を徹底解決！キュレル、ビオレu、BARTH、ヴェレダ、ニュートロジーナ、ニベア、ミノン、セタフィルなど、浴室の中で濡れたまま塗って即座に潤いを閉じ込める最強高保湿インバスボディミルク10選。</p>
      </a>

      <!-- 高保湿ホットアイマスク -->
      <a href="/winter-hot-eyemask" class="hub-card">
        <span class="hub-card-tag" style="background: #f5f3ff; color: #7c3aed;">👀 目元冷え・乾燥クマ小ジワ改善 NEW</span>
        <h2 class="hub-card-title">👀 保湿力の強さで冬の目元ショボショボ冷え・乾燥クマ小ジワとさようなら！蒸気と温熱で巡りを促しふっくらハリ感を取り戻す高保湿ホットアイマスクランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の寒冷凝固による目元血流滞留と、エアコン暖房・年末PC作業による深刻な乾燥小ジワ・青クマを徹底解決！めぐりズム、あずきのチカラ、SALUA、パナソニック、La Luna、ドクターエアなど、温熱スチームと心地よい温もりで目元を満たす最強高保湿ホットアイマスク10選。</p>
      </a>

      <!-- 高保湿ハンドマスク -->
      <a href="/winter-hand-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #fff1f2; color: #be123c;">🧤 水仕事手荒れ・指先ひび割れ集中再生 NEW</span>
        <h2 class="hub-card-title">🧤 保湿力の強さで冬の水仕事手荒れ・指先ガサガサひび割れとさようなら！手袋型で美容液が角層深部まで超密着浸透する高保湿ハンドマスクランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の大掃除・水仕事・アルコール消毒による深刻な手荒れ・指先ひび割れ・手の甲の乾燥小ジワを徹底解決！DearIrean、KOCOSTAR、ビューティーワールド、ラッキーウィンク、ウルオイート、Dr.Jart+、絹屋など、ODT密閉発想で角層深部まで美容液を届ける最強高保湿ハンドマスク10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-inbath-body' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
