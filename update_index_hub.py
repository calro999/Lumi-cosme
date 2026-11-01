import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 最新3記事のカード定義
newest_cards = """      <!-- 高保湿ヘアトリートメント -->
      <a href="/winter-hair-treatment" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #be185d;">💆 毛先集中補修・静電気防止 NEW</span>
        <h2 class="hub-card-title">💆 保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！サロン帰りの濃密ツヤまとまりが続く高保湿ヘアトリートメントランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の乾燥でパサつく毛先・静電気広がり・枝毛ダメージを徹底解決！オージュア、ケラスターゼ、フィーノ、ミルボン、モロッカンオイル、アンドハニーなど、高純度補修成分とCMC脂質配合の最強高保湿ヘアトリートメント10選。</p>
      </a>

      <!-- 薬用高保湿リップクリーム -->
      <a href="/winter-lip-balm" class="hub-card">
        <span class="hub-card-tag" style="background: #fff1f2; color: #e11d48;">💄 唇ひび割れ修復・セラミド密封 NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで冬の唇ひび割れ・血がにじむガサガサ皮剥けとさようなら！ひと塗りで潤い密封する薬用高保湿リップクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の乾燥で血がにじむ唇のひび割れ・皮剥け・口角炎を徹底解決！キュレル、モアリップ、ニベア、オバジ、メンソレータム、DHC、ラロッシュポゼなど、セラミドやアラントイン配合の最強薬用高保湿リップクリーム10選。</p>
      </a>

      <!-- 高保湿炭酸泡美容液 -->
      <a href="/winter-carbonic-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #f0fdfa; color: #0d9488;">🫧 血行促進・土台浸透ブースト NEW</span>
        <h2 class="hub-card-title">🫧 保湿力の強さで冬の血行不良くすみ・ゴワつき砂漠肌とさようなら！炭酸泡で巡りを呼び覚ます高保湿炭酸美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の寒冷血管収縮・血行不良くすみ・ゴワつきインナードライを徹底解決！ソフィーナiP、エスト、エリクシール、アスタリフト、ドクターシーラボ、KANEBO、Yunth、タカミなど、マイクロ炭酸泡やボーア効果で巡りをブーストする最強高保湿炭酸泡美容液10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-hair-treatment' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
