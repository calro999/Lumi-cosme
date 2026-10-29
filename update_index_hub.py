import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# メタ情報の更新
html = html.replace(
    "全21大特集",
    "全24大特集"
)
html = html.replace(
    '<meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿スリーピングマスク・ネイルオイル・フットクリーム・乳液・フェイスオイル・リペアバーム・入浴剤・洗顔料・ミスト化粧水・化粧水・クレンジング・デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">',
    '<meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿スティック美容液・スカルプローション・トーンアップ下地・スリーピングマスク・ネイルオイル・フットクリーム・乳液・フェイスオイル・リペアバーム・入浴剤・洗顔料・ミスト化粧水・化粧水・クレンジング・デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">'
)
html = html.replace(
    '<meta property="og:description" content="11月・12月の本格乾燥シーズン到来！高保湿乳液、フェイスオイル、リペアバームなど全21大特集公開中。">',
    '<meta property="og:description" content="11月・12月の本格乾燥シーズン到来！スティック美容液、スカルプローション、トーンアップ下地など全24大特集公開中。">'
)
html = html.replace(
    '<meta name="twitter:description" content="11月・12月の本格乾燥シーズン到来！高保湿乳液、フェイスオイル、リペアバームなど全21大特集公開中。">',
    '<meta name="twitter:description" content="11月・12月の本格乾燥シーズン到来！スティック美容液、スカルプローション、トーンアップ下地など全24大特集公開中。">'
)

new_cards = """      <!-- 高保湿スティック美容液 -->
      <a href="/winter-stick-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #db2777;">💄 メイクの上から直塗りレスキュー NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで肌乾燥とさようなら！日中いつでもメイクの上から乾燥小じわ・粉吹きをレスキューする高保湿スティック美容液ランク10</h2>
        <p class="hub-card-desc">オフィス暖房のファンデ割れ・ちりめんジワをひと塗りで解決！イプサ、KAHI、ダルバ、アスタリフトなど高保湿バームスティック10選。</p>
      </a>

      <!-- 高保湿スカルプローション -->
      <a href="/winter-scalp-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #ecfdf5; color: #059669;">💆 冬の乾性フケ・かゆみ撃退 NEW</span>
        <h2 class="hub-card-title">💆 保湿力の強さで頭皮乾燥とさようなら！冬のフケ・かゆみ・つっぱりを防ぎうるおい頭皮を育てる高保湿スカルプローションランク10</h2>
        <p class="hub-card-desc">冬のパラパラ乾性フケ・強い地肌かゆみに終止符！キュレル、ミルボン、ヴェレダ、無印良品など頭皮のセラミド保水ローション10選。</p>
      </a>

      <!-- 高保湿コントロールカラー＆トーンアップ下地 -->
      <a href="/winter-toneup-base" class="hub-card">
        <span class="hub-card-tag" style="background: #f5f3ff; color: #7c3aed;">🌸 冬の血色レス・くすみ払拭 NEW</span>
        <h2 class="hub-card-title">🌸 保湿力の強さで肌乾燥とさようなら！冬の血色レス・乾燥くすみを払拭し夕方まで透き通る高保湿コントロールカラー＆トーンアップ下地ランク10</h2>
        <p class="hub-card-desc">寒さによる青白さ・黄ぐすみ・ファンデの粉浮きを一掃！ポール＆ジョー、コスメデコルテ、ジルスチュアートなど美容液トーンアップ下地10選。</p>
      </a>
"""

if '<div class="hub-grid">' in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully!")
