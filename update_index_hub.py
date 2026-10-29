import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# メタ情報の更新
html = html.replace(
    "全24大特集",
    "全27大特集"
)
html = html.replace(
    '<meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿スティック美容液・スカルプローション・トーンアップ下地・スリーピングマスク・ネイルオイル・フットクリーム・乳液・フェイスオイル・リペアバーム・入浴剤・洗顔料・ミスト化粧水・化粧水・クレンジング・デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">',
    '<meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿フェイスパウダー・リッププランパー・集中ヘアマスク・スティック美容液・スカルプローション・トーンアップ下地・スリーピングマスク・ネイルオイル・フットクリーム・乳液・フェイスオイル・リペアバーム・入浴剤・洗顔料・ミスト化粧水・化粧水・クレンジング・デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">'
)
html = html.replace(
    '<meta property="og:description" content="11月・12月の本格乾燥シーズン到来！スティック美容液、スカルプローション、トーンアップ下地など全24大特集公開中。">',
    '<meta property="og:description" content="11月・12月の本格乾燥シーズン到来！高保湿フェイスパウダー、リッププランパー、集中補修ヘアマスクなど全27大特集公開中。">'
)
html = html.replace(
    '<meta name="twitter:description" content="11月・12月の本格乾燥シーズン到来！スティック美容液、スカルプローション、トーンアップ下地など全24大特集公開中。">',
    '<meta name="twitter:description" content="11月・12月の本格乾燥シーズン到来！高保湿フェイスパウダー、リッププランパー、集中補修ヘアマスクなど全27大特集公開中。">'
)

new_cards = """      <!-- 高保湿フェイスパウダー -->
      <a href="/winter-powder" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #2563eb;">✨ 冬の粉吹き・乾燥小じわ防止 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥とさようなら！冬の粉吹き・乾燥小じわを防ぎ一日中うるおいツヤ肌が続く高保湿フェイスパウダーランク10</h2>
        <p class="hub-card-desc">暖房直撃でも夕方まで粉吹き・地割れシワ知らず！コスメデコルテ、NARSリフ粉、エクセル、ミラコレなど美容液パウダー10選。</p>
      </a>

      <!-- 高保湿リッププランパー＆濃密リップオイル -->
      <a href="/winter-lip-plumper" class="hub-card">
        <span class="hub-card-tag" style="background: #fff1f2; color: #e11d48;">💄 冬の縦ジワ・皮剥け即効リペア NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで唇乾燥とさようなら！冬のガサガサ・縦ジワ・皮剥けを濃密オイルと温感ボリュームで満たす高保湿リッププランパーランク10</h2>
        <p class="hub-card-desc">真冬の過酷な唇トラブルを即効解消！ディオールマキシマイザー、クラランス、ヴィセなど温感刺激＆濃密オイルプランパー10選。</p>
      </a>

      <!-- 濃密高保湿ヘアマスク＆インバストリートメント -->
      <a href="/winter-hair-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #f0fdf4; color: #16a34a;">💆‍♀️ 静電気・毛先パサつき集中補修 NEW</span>
        <h2 class="hub-card-title">💆‍♀️ 保湿力の強さで髪の乾燥・静電気とさようなら！真冬の毛先パサつき・広がりを芯から集中補修する濃密高保湿ヘアマスクランク10</h2>
        <p class="hub-card-desc">マフラー摩擦や暖房の静電気・毛先パサつきを芯からリペア！フィーノ、オージュア、ケラスターゼ、TSUBAKIなどサロン級マスク10選。</p>
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
