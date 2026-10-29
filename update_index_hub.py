import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# メタ情報の更新
html = html.replace("全30大特集", "全33大特集")
html = html.replace(
    '<meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿美容液・高保湿コンシーラー・高保湿リップティント・フェイスパウダー・リッププランパー・集中ヘアマスク・スティック美容液・スカルプローション・トーンアップ下地・スリーピングマスク・ネイルオイル・フットクリーム・乳液・フェイスオイル・リペアバーム・入浴剤・洗顔料・ミスト化粧水・化粧水・クレンジング・デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">',
    '<meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿ヘアミルク・高保湿クッションファンデ・高保湿ボディスクラブ・高保湿美容液・高保湿コンシーラー・高保湿リップティント・フェイスパウダー・リッププランパー・集中ヘアマスク・スティック美容液・スカルプローション・トーンアップ下地・スリーピングマスク・ネイルオイル・フットクリーム・乳液・フェイスオイル・リペアバーム・入浴剤・洗顔料・ミスト化粧水・化粧水・クレンジング・デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">'
)
html = html.replace(
    '<meta property="og:description" content="11月・12月の本格乾燥シーズン到来！高保湿美容液、高保湿コンシーラー、高保湿リップティントなど全30大特集公開中。">',
    '<meta property="og:description" content="11月・12月の本格乾燥シーズン到来！高保湿ヘアミルク、高保湿クッションファンデ、高保湿ボディスクラブなど全33大特集公開中。">'
)
html = html.replace(
    '<meta name="twitter:description" content="11月・12月の本格乾燥シーズン到来！高保湿美容液、高保湿コンシーラー、高保湿リップティントなど全30大特集公開中。">',
    '<meta name="twitter:description" content="11月・12月の本格乾燥シーズン到来！高保湿ヘアミルク、高保湿クッションファンデ、高保湿ボディスクラブなど全33大特集公開中。">'
)

new_cards = """      <!-- 高保湿ヘアミルク＆アウトバストリートメント -->
      <a href="/winter-hair-milk" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf4ff; color: #c026d3;">💆‍♀️ 髪パサつき・静電気防止 NEW</span>
        <h2 class="hub-card-title">💆‍♀️ 保湿力の強さで髪のパサつき・静電気とさようなら！冬の乾燥・マフラー摩擦を芯から防ぐ高保湿ヘアミルク＆アウトバストリートメントランク10</h2>
        <p class="hub-card-desc">オイルだけでは届かない毛髪内部へ水分＆CMCを集中補給！オルビス、ミルボンエルジューダ、N.シアミルク、ケラスターゼなど神ヘアミルク10選。</p>
      </a>

      <!-- 高保湿クッションファンデーション＆美容液ファンデ -->
      <a href="/winter-cushion-foundation" class="hub-card">
        <span class="hub-card-tag" style="background: #fefce8; color: #ca8a04;">✨ 暖房直撃でも夕方までひび割れない NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥とさようなら！冬の暖房直撃でも夕方までひび割れない高保湿クッションファンデーション＆美容液ファンデランク10</h2>
        <p class="hub-card-desc">暖房の効いた部屋でも夕方まで乾燥割れ・粉吹き知らず！TIRTIRクリスタル、CLIOハイグロウ、ジョンセンムル、YSLなど美容液クッション10選。</p>
      </a>

      <!-- 高保湿ボディスクラブ＆角質ケア -->
      <a href="/winter-body-scrub" class="hub-card">
        <span class="hub-card-tag" style="background: #f0fdf4; color: #16a34a;">🛁 全身ゴワつき粉吹きオフ＆オイル膜 NEW</span>
        <h2 class="hub-card-title">🛁 保湿力の強さで全身のゴワつき・粉吹きとさようなら！入浴時に潤いオイルを仕込む高保湿ボディスクラブ＆角質ケアランク10</h2>
        <p class="hub-card-desc">頑固なひじ・ひざ・かかとの角質をオフし濃厚オイル膜で全身シールド！SABON、ハウスオブローゼ、LUSH、クナイプなど神スクラブ10選。</p>
      </a>
"""

if '<div class="hub-grid">' in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully with 3 new articles!")
