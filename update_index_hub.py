import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 最新3記事のカード定義
newest_cards = """      <!-- 高保湿ボディクリーム -->
      <a href="/winter-body-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #f0fdf4; color: #15803d;">🧴 全身粉吹き防止・高濃度セラミド NEW</span>
        <h2 class="hub-card-title">🧴 保湿力の強さで冬の粉吹き・全身カサつき乾燥とさようなら！しっとり潤い肌が続く高保湿ボディクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の乾燥で粉を吹くすね・腕・お腹まわりのカサつきを徹底解決！キュレル、セタフィル、ニュートロジーナ、ロクシタン、ローラメルシエなど、高純度シアバターやセラミド配合の最強高保湿ボディクリーム10選。</p>
      </a>

      <!-- 高保湿ブースターオイル -->
      <a href="/winter-booster-oil" class="hub-card">
        <span class="hub-card-tag" style="background: #fefce8; color: #a16207;">✨ 角層柔軟・吸水力爆上げプレオイル NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで冬のゴワつき・カサカサ砂漠肌とさようなら！化粧水をぐんぐん引き込む高保湿ブースターオイルランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の寒さで硬くこわばった肌・化粧水が入らないインナードライを徹底解決！RMK、メルヴィータ、トリロジー、HABA、FEMMUE、アルビオンなど、洗顔後すぐの肌をふっくらほぐし吸水力を劇的アップする最強高保湿ブースターオイル10選。</p>
      </a>

      <!-- 高保湿シャンプー -->
      <a href="/winter-moisture-shampoo" class="hub-card">
        <span class="hub-card-tag" style="background: #eff6ff; color: #1d4ed8;">🫧 静電気防止・濃密アミノ酸補修 NEW</span>
        <h2 class="hub-card-title">🫧 保湿力の強さで冬のパサつき・静電気・頭皮乾燥とさようなら！うるおい満ちる濃密高保湿シャンプーランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の暖房風や乾燥による毛先のパサパサ・静電気広がり・頭皮のカサつきを徹底解決！オージュア、ケラスターゼ、ボタニストプレミアム、ミルボン、エッセンシャルプレミアムなど、アミノ酸系洗浄＆濃密保湿で髪と頭皮をうるおす最強高保湿シャンプー10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-body-cream' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
