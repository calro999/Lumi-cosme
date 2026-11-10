import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)
elif '<div class="footer-links-grid" id="footer-links-box">' in html:
    html = re.sub(r'<div class="footer-links-grid" id="footer-links-box">.*?</div>', '<div class="footer-links-grid" id="footer-links-box">\n' + footer_links_html + '\n          </div>', html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿バリアクリーム -->
      <a href="/winter-barrier-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0284c7;">🛡️ セラミドカプセル・ラメラ液晶再建 NEW</span>
        <h2 class="hub-card-title">🛡️ 保湿力の強さで肌乾燥とさようなら！高密度セラミドカプセルとバリア再建ヴェールで真冬の寒冷粉吹き肌を完全シールドする保湿力高めバリアクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥・粉吹き・皮剥け・暖房インナードライを徹底救済！エストラ、リアルバリア、イリユン、ラロッシュポゼ、エトヴォス、ドクタージャルトまで高密度セラミドカプセルとバリア再建ヴェールの科学的根拠・最新価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿ナイアシンアミドクリーム -->
      <a href="/winter-niacinamide-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #f3e8ff; color: #9333ea;">✨ 医薬部外品・シワ改善×セラミド自生 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥とさようなら！医薬部外品ナイアシンアミドのシワ改善×セラミド自生力で真冬の寒冷くすみ・小ジワをふっくら押し上げる保湿力高めナイアシンアミドクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷くすみ・乾燥小ジワ・暖房脱水を徹底救済！ONE BY KOSÉ、ルシェリ、なめらか本舗、カナデル、極潤ハリクリームまで医薬部外品ナイアシンアミドのシワ改善＆美白メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿エクソソームクリーム -->
      <a href="/winter-exosome-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #d1fae5; color: #059669;">🔬 最先端ナノカプセル・細胞間浸透再建 NEW</span>
        <h2 class="hub-card-title">🔬 保湿力の強さで肌乾燥とさようなら！最先端ナノカプセル・エクソソームの細胞間浸透力で真冬のしぼみ・ゴワつき肌を根本再建する保湿力高めエクソソームクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷しぼみ肌・たるみ毛穴・浸透ブロックを徹底救済！VTリードルショット、メディキューブ、リジュラン、魔女工場、センテリアン24まで最先端エクソソーム＆ナノカプセルの科学的メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-barrier-cream' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
