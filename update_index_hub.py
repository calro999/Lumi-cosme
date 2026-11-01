import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿かかとパック＆保湿ソックス -->
      <a href="/winter-foot-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #f3e8ff; color: #7b2cbf;">🦶 かかとガサガサ・タイツ電線ゼロ NEW</span>
        <h2 class="hub-card-title">🦶 保湿力の強さで冬のかかとひび割れ・タイツ電線ガサガサとさようなら！履くだけで角質深部まで濃密柔軟ケアする高保湿かかとパック＆保湿ソックスランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の寒冷乾燥による頑固なかかとガサガサ・ひび割れ・タイツの引っかかり電線を徹底解決！ベビーフット、かかとちゃん、KOCOSTAR、太陽ニット、ビューティーワールド、休足時間、ドクターショール、足うら美人など、削らず履くだけで生まれたてのツルツル素肌へ導く最強高保湿かかとパック＆ソックス10選。</p>
      </a>

      <!-- 高密着ハイドロゲルアイパッチ -->
      <a href="/winter-eye-patch" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0284c7;">👀 目元ちりめんジワ・乾燥クマ改善 NEW</span>
        <h2 class="hub-card-title">👀 保湿力の強さで冬の目元ちりめんジワ・乾燥クマとさようなら！ぷるぷる高密着ハイドロゲルが角層深部を潤す高保湿アイパッチランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の寒冷と暖房直撃による目元のちりめんジワ・乾燥クマ・夕方のファンデ割れを徹底解決！プチフェ、Abib、ヘイミッシュ、クリアターン、JMsolution、goodal、メディヒール、ドクタージャルト、イニスフリーなど、体温でとろけて角層深部を潤す最強高保湿ハイドロゲルアイパッチ10選。</p>
      </a>

      <!-- 浸透ケラチン・高保湿ネイル補修美容液 -->
      <a href="/winter-nail-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f8; color: #be185d;">💅 爪割れ・二枚爪・ガサガサ縦ジワ集中補修 NEW</span>
        <h2 class="hub-card-title">💅 保湿力の強さで冬の爪割れ・二枚爪・ガサガサ縦ジワとさようなら！浸透ケラチンと高保湿成分で強くしなやかな美爪を育てる高保湿ネイル補修美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の乾燥・水仕事による爪割れ・二枚爪・爪の縦ジワを徹底解決！ドクターネイル、メンソレータム、エテュセ、OPI、スパルーチェ、LCN、カントリー＆ストリーム、デュカート、無印良品など、浸透ケラチンと高保湿成分で折れない美爪を育てる最強ネイル補修美容液10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-foot-mask' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
