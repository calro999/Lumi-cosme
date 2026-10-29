import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# メタ情報の更新
html = html.replace(
    "全27大特集",
    "全30大特集"
)
html = html.replace(
    '<meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿フェイスパウダー・リッププランパー・集中ヘアマスク・スティック美容液・スカルプローション・トーンアップ下地・スリーピングマスク・ネイルオイル・フットクリーム・乳液・フェイスオイル・リペアバーム・入浴剤・洗顔料・ミスト化粧水・化粧水・クレンジング・デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">',
    '<meta name="description" content="真冬（11月・12月）の深刻な乾燥・暖房ダメージを乗り切る高保湿美容液・高保湿コンシーラー・高保湿リップティント・フェイスパウダー・リッププランパー・集中ヘアマスク・スティック美容液・スカルプローション・トーンアップ下地・スリーピングマスク・ネイルオイル・フットクリーム・乳液・フェイスオイル・リペアバーム・入浴剤・洗顔料・ミスト化粧水・化粧水・クレンジング・デイクリーム・高保湿クリーム・導入美容液・シートマスク・アイクリーム・ファンデーション・リップ・ボディケア・ヘアケア・ハンドクリームを徹底解説するビューティー厳選メディア。">'
)
html = html.replace(
    '<meta property="og:description" content="11月・12月の本格乾燥シーズン到来！高保湿乳液、フェイスオイル、リペアバームなど全27大特集公開中。">',
    '<meta property="og:description" content="11月・12月の本格乾燥シーズン到来！高保湿美容液、高保湿コンシーラー、高保湿リップティントなど全30大特集公開中。">'
)
html = html.replace(
    '<meta name="twitter:description" content="11月・12月の本格乾燥シーズン到来！高保湿乳液、フェイスオイル、リペアバームなど全27大特集公開中。">',
    '<meta name="twitter:description" content="11月・12月の本格乾燥シーズン到来！高保湿美容液、高保湿コンシーラー、高保湿リップティントなど全30大特集公開中。">'
)

new_cards = """      <!-- 高保湿美容液＆高濃度アンプル -->
      <a href="/winter-hydrating-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #2563eb;">💧 冬の砂漠肌・バリア救済 NEW</span>
        <h2 class="hub-card-title">💧 保湿力の強さで肌乾燥・砂漠化とさようなら！冬のバリア崩壊を集中救済する高保湿美容液＆高濃度アンプルランク10</h2>
        <p class="hub-card-desc">暖房直撃でカラカラの角層を集中救済！コスメデコルテリポソーム、トリデン、キュレル、エトヴォスなどセラミド＆ヒアルロン酸セラム10選。</p>
      </a>

      <!-- 高保湿コンシーラー＆美容液リキッドコンシーラー -->
      <a href="/winter-concealer" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #db2777;">👁️ 目元の乾燥小じわ・ひび割れ防止 NEW</span>
        <h2 class="hub-card-title">👁️ 保湿力の強さで目元・口元の乾燥ひび割れとさようなら！冬の青クマ・くすみを潤いヴェールで消し去る高保湿コンシーラーランク10</h2>
        <p class="hub-card-desc">夕方の目元のちりめんジワ・地割れ割れに終止符！ディオールスキン、コスメデコルテ、NARS、アンドビーなど美容液コンシーラー10選。</p>
      </a>

      <!-- 高保湿リップティント＆とろける美容液ルージュ -->
      <a href="/winter-lip-tint" class="hub-card">
        <span class="hub-card-tag" style="background: #fff1f2; color: #e11d48;">💄 冬の皮剥け防止＆落ちない血色 NEW</span>
        <h2 class="hub-card-title">💄 保湿力の強さで唇の乾燥・皮剥け・血色レスとさようなら！真冬のイベントも一日中うるおい発色が続く高保湿リップティント＆美容液ルージュランク10</h2>
        <p class="hub-card-desc">皮剥け知らずで一日中落ちない！KATEリップモンスター、ロムアンドメルティングバーム、オペラ、ディオールなど高保湿ルージュ10選。</p>
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
