import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新3記事のカード定義
new_cards = """      <!-- 高保湿まつ毛美容液・アイラッシュセラム -->
      <a href="/winter-eyelash-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #be185d;">👁️ まつ毛抜け＆乾燥切断ストップ・ナノペプチド高保湿 NEW</span>
        <h2 class="hub-card-title">👁️ 保湿力の強さで冬のまつ毛抜け・パサつき乾燥とさようなら！ハリ・コシ・密度感を呼び覚ます高保湿まつ毛美容液・アイラッシュセラムランク10</h2>
        <p class="hub-card-desc">冬の暖房乾燥・冷風・マスカラ摩擦で細く傷んだまつ毛を救う！ラッシュアディクト、エマーキット、ディオール、ランコム、コスメデコルテなど、キューティクルを高保湿補修して圧倒的なハリ・コシ・密度感を呼び覚ます神まつ毛美容液厳選10選。</p>
      </a>

      <!-- 高保湿ポイントメイクリムーバー -->
      <a href="/winter-point-makeup-remover" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #1d4ed8;">✨ こすらずスルン・目元口元の摩擦乾燥小ジワ防止 NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで目元・口元の摩擦ダメージ＆乾燥小ジワとさようなら！デリケートな皮膚をうるおいで守り抜く高保湿ポイントメイクリムーバーランク10</h2>
        <p class="hub-card-desc">冬の乾燥小ジワ・色素沈着・唇の皮剥けの主因となるクレンジング摩擦を撃退！RMK、シャネル、クレ・ド・ポー ボーテ、ビフェスタ、ランコムなど、濃密アイメイクやティントをこすらずスルンと落として高保湿キープする神ポイントメイクリムーバー厳選10選。</p>
      </a>

      <!-- 高保湿フェイスマッサージクリーム -->
      <a href="/winter-massage-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #faf5ff; color: #7e22ce;">💆‍♀️ 冬の冷えむくみ＆コリ解消・血行促進上向きハリ肌 NEW</span>
        <h2 class="hub-card-title">💆‍♀️ 保湿力の強さで冬の冷えむくみ・乾燥くすみ・フェイスラインたるみとさようなら！巡りを高めてふっくら上向き肌へ導く高保湿フェイスマッサージクリームランク10</h2>
        <p class="hub-card-desc">冬の寒波による血行不良・冷え固まった筋肉のコリ・重たいむくみ・乾燥くすみを撃退！POLA B.A、SUQQU、資生堂エリクシール、コスメデコルテAQ、アルビオンエクシアなど、摩擦ゼロで巡りを高め上向き立体ハリ肌へ導く神マッサージクリーム厳選10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-eyelash-serum' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 new cards and latest footer links!")
