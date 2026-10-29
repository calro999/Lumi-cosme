import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# メタ情報の更新
html = html.replace(
    "全18大特集",
    "全21大特集"
)
html = html.replace(
    '<meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿乳液・フェイスオイル・リペアバーム・高保湿入浴剤・洗顔料・ミスト化粧水・化粧水・クレンジング・朝用デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・高保湿ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">',
    '<meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿スリーピングマスク・ネイルオイル・フットクリーム・乳液・フェイスオイル・リペアバーム・入浴剤・洗顔料・ミスト化粧水・化粧水・クレンジング・デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">'
)

new_cards = """      <!-- 高保湿スリーピングマスク -->
      <a href="/winter-sleeping-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">🌙 睡眠中濃厚ラッピング NEW</span>
        <h2 class="hub-card-title">🌙 保湿力の強さで肌乾燥とさようなら！寝ている間に集中密着ケアする高保湿スリーピングマスク＆ナイトパックランク10</h2>
        <p class="hub-card-desc">睡眠中の暖房乾燥脱水を完全遮断！ラネージュ、エリクシール、ファミュ、コスメデコルテなど翌朝ぷるんと吸い付く神パック10選。</p>
      </a>

      <!-- 高保湿ネイルオイル -->
      <a href="/winter-nail-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf4ff; color: #a21caf;">💅 爪割れ・ささくれ集中リペア NEW</span>
        <h2 class="hub-card-title">💅 保湿力の強さで肌乾燥とさようなら！指先のささくれ・パサつきを防ぎ美爪を育てる高保湿ネイルオイルランク10</h2>
        <p class="hub-card-desc">爪割れ・二枚爪・痛いささくれを徹底リペア！uka、OPI、ロクシタン、アンドネイル、無印良品などケラチン浸透植物オイル10選。</p>
      </a>

      <!-- 高保湿かかと＆フットクリーム -->
      <a href="/winter-foot-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #fef3c7; color: #92400e;">👣 ガサガサ・ひび割れレスキュー NEW</span>
        <h2 class="hub-card-title">👣 保湿力の強さで肌乾燥とさようなら！頑固なガサガサ・ひび割れをふっくら柔らかくする高保湿かかと＆フットクリームランク10</h2>
        <p class="hub-card-desc">タイツの電線やパックリ割れと決別！ニュートロジーナ、ロコベース、ドクターショール、ユースキン、ヒビケアFTなど最強フットケア10選。</p>
      </a>
"""

if '<div class="hub-grid">' in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

# フッターリンクの更新
from update_all_internal_links import footer_links_html
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully!")
