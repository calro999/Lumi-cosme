import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 最新3記事のカード定義
newest_cards = """      <!-- 高保湿スカルプスクラブ -->
      <a href="/winter-scalp-scrub" class="hub-card">
        <span class="hub-card-tag" style="background: #f0fdf4; color: #15803d;">💆 頭皮クレンジング・乾燥フケ防止 NEW</span>
        <h2 class="hub-card-title">💆 保湿力の強さで冬の頭皮乾燥フケ・毛穴詰まり・かゆみとさようなら！うるおい頭皮へ導く高保湿スカルプスクラブランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の湿気低下による頭皮の乾燥フケ・ニット帽や暖房による蒸れ毛穴詰まり・血行不良を徹底解決！SABON、ロクシタン、uka、ラ・カスタ、ヴェレダ、アヴェダ、OSAJI、モロッカンオイル、ミルボンなど、天然塩・シュガースクラブとボタニカルオイル配合の高保湿スカルプスクラブ10選。</p>
      </a>

      <!-- 薬用高保湿重炭酸入浴剤 -->
      <a href="/winter-medicinal-bath" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #1d4ed8;">🛁 冷え性疲労回復・湯上がり過乾燥防止 NEW</span>
        <h2 class="hub-card-title">🛁 保湿力の強さで冬の冷え性・湯冷めカサつき砂漠肌とさようなら！芯までポカポカ潤う薬用高保湿重炭酸入浴剤ランク10</h2>
        <p class="hub-card-desc">11月・12月の厳しい寒さによる末端冷え・肩こり・お風呂上がりの急激な肌乾燥（過乾燥）を徹底解決！BARTH、薬用ホットタブ重炭酸湯、きき湯ファインヒート、アユーラメディテーションバス、クナイプ、ツムラ日本の名湯、ヴェレダなど、中性重炭酸イオンと生薬・高保湿オイル配合の薬用高保湿重炭酸入浴剤10選。</p>
      </a>

      <!-- 朝用ふき取り高保湿化粧水 -->
      <a href="/winter-wipe-lotion" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf4ff; color: #a21caf;">💧 朝の時短角質オフ・冷水洗顔防止 NEW</span>
        <h2 class="hub-card-title">💧 保湿力の強さで冬の朝の冷水洗顔・乾燥つっぱりとさようなら！拭くだけで角質オフ＆濃密保水する朝用ふき取り高保湿化粧水ランク10</h2>
        <p class="hub-card-desc">11月・12月の朝の寒さで冷水洗顔がつらい・洗顔後の急激なつっぱり・メイク崩れ・ゴワつき角質を徹底解決！カネボウ ラディアントスキンリファイナー、ビオデルマ サンシビオ、ネイチャーコンク、イプサ、クリニーク、チャコットなど、拭くだけで角質オフ＆濃密保水する朝用ふき取り高保湿化粧水10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-scalp-scrub' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
