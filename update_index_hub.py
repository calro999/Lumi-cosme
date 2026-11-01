import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿マイクロニードルパッチ -->
      <a href="/winter-needle-patch" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf4ff; color: #a21caf;">🔬 目元・ほうれい線角層注入 NEW</span>
        <h2 class="hub-card-title">🔬 保湿力の強さで冬の目元・ほうれい線乾燥小ジワとさようなら！寝ている間にヒアルロン酸針が角層深部へ直接届く高保湿マイクロニードルパッチランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の凍える冷気とエアコン暖房で深く刻まれる目元・口元の乾燥小ジワ・ほうれい線を徹底解決！北の快適工房、資生堂ナビジョン、クオニス、VT CICA、コーセークリアターン、ドクターフィルなど、寝ている間にヒアルロン酸針が角層深部へダイレクト注入する最強高保湿マイクロニードルパッチ10選。</p>
      </a>

      <!-- 高保湿バスソルト -->
      <a href="/winter-bath-salt" class="hub-card">
        <span class="hub-card-tag" style="background: #f0f9ff; color: #0369a1;">🛁 冷え性改善・湯上がり全身過乾燥防止 NEW</span>
        <h2 class="hub-card-title">🛁 保湿力の強さで冬の冷え性・全身カサつき乾燥とさようなら！マグネシウム＆ミネラル温浴で湯上がりしっとり極上肌へ導く高保湿バスソルトランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の寒冷による末端冷え性・入浴後の全身粉吹き乾燥・かゆみを徹底解決！シークリスタルス、クナイプ、NEHAN TOKYO、MARKS&WEB、SABON、BARAKA、SHIRO、アユーラなど、高純度エプソムソルトや死海ミネラルで芯まで温め肌をうるおす最強高保湿バスソルト10選。</p>
      </a>

      <!-- 高保湿プランプリップグロス -->
      <a href="/winter-lip-gloss" class="hub-card">
        <span class="hub-card-tag" style="background: #fff1f2; color: #be123c;">💄 唇の縦ジワしぼみ・ホリデー水光ツヤ NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで冬の唇乾燥・縦ジワしぼみとさようなら！ホリデーの煌めきとぷるんとした濃密ツヤが続く高保湿プランプリップグロスランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の唇乾燥・縦ジワ・皮剥け・血色レスを徹底解決！ディオール、クラランス、ジルスチュアート、シャネル、ロムアンド、キャンメイク、RMK、SUQQUなど、カプサイシンや濃密植物オイルで唇をふっくら満たしホリデーの濡れツヤをキープする最強高保湿プランプリップグロス10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-needle-patch' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
