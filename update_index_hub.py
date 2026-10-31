import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 最新3記事のカード定義
latest_cards = """      <!-- 高保湿クレンジングクリーム -->
      <a href="/winter-cleansing-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #1d4ed8;">🫧 まるで美容パック・摩擦ゼロオフ NEW</span>
        <h2 class="hub-card-title">🫧 保湿力の強さで冬の突っ張り・乾燥砂漠肌とさようなら！まるで美容パックな高保湿クレンジングクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の冷え固まった毛穴・洗い上がりのつっぱり乾燥を徹底解決！コスメデコルテAQ、オルビス、カネボウ、アルビオン、POLA、アルージェ、ポンズ、ちふれなど、摩擦レスにメイクを浮かせ角層のうるおいを守り抜く高保湿クレンジングクリーム10選。</p>
      </a>

      <!-- 高保湿ナイアシンアミド美容液 -->
      <a href="/winter-niacinamide-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #f0fdf4; color: #15803d;">✨ シワ改善・美白・バリア強化 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで冬の乾燥小ジワ・くすみたるみとさようなら！ハリ艶と透明感を呼び覚ます高保湿ナイアシンアミド美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の乾燥小ジワ・暖房くすみ・肌バリア崩壊を徹底解決！ワンバイコーセー、ラロッシュポゼ、魔女工場、オルビス、ジオーディナリー、肌ラボ、ディセンシア、ドクターケイ、大正製薬など、シワ改善・美白・セラミド合成を同時に促す高保湿ナイアシンアミド美容液10選。</p>
      </a>

      <!-- 高保湿リップスティック口紅 -->
      <a href="/winter-lipstick" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #be185d;">💄 24時間乾かない・皮剥け知らず NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで冬の唇乾燥・ガサガサ皮剥けとさようなら！うる艶と美発色が一日中続く高保湿リップスティック口紅ランク10</h2>
        <p class="hub-card-desc">11月・12月の忘年会やホリデーイベントで唇が乾かない！皮剥け・縦ジワ知らずの高保湿ルージュ10選。KATEリップモンスター、ディオール、シャネル、KANEBO、SUQQU、デコルテ、オペラ、YSL、ロムアンド、クレドポーなど、濃密オイル＆保湿成分で一日中ツヤと発色が続く名品を徹底比較！</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-cleansing-cream' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + latest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
