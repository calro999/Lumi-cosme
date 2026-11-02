import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿PDRN美容液 -->
      <a href="/winter-pdrn-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f4; color: #c94b6e;">🧬 サーモン注射発想・ハリ密度爆誕 NEW</span>
        <h2 class="hub-card-title">🧬 保湿力の強さで冬枯れ肌・弾力低下とさようなら！サーモン注射発想の再生成分で内側から押し返すハリツヤ肌へ導く高保湿PDRN美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の暖房直撃と寒波による深刻な冬枯れ肌・たるみ毛穴・乾燥小ジワを徹底解決！VT、リジュラン、アヌア、Yunth、センテリアン24、IOPEなど、角層深部を満たして押し返すようなハリ肌を叶える名品PDRN美容液10選。</p>
      </a>

      <!-- 高密着バイオコラーゲンマスク -->
      <a href="/winter-collagen-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #fffbeb; color: #d97706;">🌙 一晩貼って朝ぷるん肌 NEW</span>
        <h2 class="hub-card-title">🌙 保湿力の強さで朝の乾燥砂漠肌・毛穴開きとさようなら！寝ている間に角層深部へ溶け込み朝ぷるん肌が蘇る高密着バイオコラーゲンマスクランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の夜間暖房による砂漠肌・朝の粉吹き・たるみ毛穴を徹底解決！一晩貼って寝るだけで白から透明に変わるバイオコラーゲンリアルディープマスク10選！BIODANCE、メディキューブ、PESTLO、Abib、VTなど厳選。</p>
      </a>

      <!-- 高濃度炭酸シャンプー -->
      <a href="/winter-carbonic-shampoo" class="hub-card">
        <span class="hub-card-tag" style="background: #f0f9ff; color: #0284c7;">🫧 頭皮冷え凝固・乾燥フケ撃退 NEW</span>
        <h2 class="hub-card-title">🫧 保湿力の強さで冬の頭皮乾燥フケ・寒冷凝固とさようなら！高濃度マイクロ炭酸泡で毛穴汚れを浮かし血行を巡らせる高保湿炭酸シャンプーランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷による頭皮の血行不良・固まった皮脂・暖房による乾燥フケ・ペタンコ髪を徹底解決！5,000ppm超の微細マイクロ炭酸泡で優しく毛穴をクレンジングし巡りを高める高保湿炭酸シャンプー10選！b.ris、ルメント、ミルボンなど厳選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-pdrn-serum' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
