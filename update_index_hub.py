import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿オイルインミスト -->
      <a href="/winter-oil-mist" class="hub-card">
        <span class="hub-card-tag" style="background: #fdf2f4; color: #c94b6e;">✨ 暖房砂漠肌・午後粉吹きゼロ NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで暖房乾燥・午後カサカサ肌とさようなら！水分と美容オイルの黄金比で日中も瞬時に艶肌復活する高保湿オイルインミストランク10</h2>
        <p class="hub-card-desc">11月・12月の暖房直撃による砂漠肌・粉吹き・メイク崩れ・夕方のちりめんジワを徹底解決！ダルバ、エリクシール、dプログラム、アルビオン、RMK、カネボウなど、振ってスプレーするだけで一日中ツヤと潤いが続く最強高保湿オイルインミスト10選。</p>
      </a>

      <!-- 薬用重炭酸入浴剤 -->
      <a href="/winter-carbonic-bath" class="hub-card">
        <span class="hub-card-tag" style="background: #f0f9ff; color: #0284c7;">🛁 冷え性改善・全身粉吹き撃退 NEW</span>
        <h2 class="hub-card-title">🛁 保湿力の強さで冬の冷え性・カサカサ全身乾燥とさようなら！重炭酸イオン温浴で芯から温まり角層深部まで潤す薬用重炭酸入浴剤ランク10</h2>
        <p class="hub-card-desc">11月・12月の寒波による冷え性・血行不良・全身のカサカサ粉吹き乾燥を徹底解消！BARTH、薬用ホットタブ、きき湯ファインヒート、バブメディキュア、クナイプ、AYURAなど、中性重炭酸イオンが温浴効果を高めて血流を促進する至高の入浴剤10選。</p>
      </a>

      <!-- 温感ヘッドスパトリートメント -->
      <a href="/winter-hot-treatment" class="hub-card">
        <span class="hub-card-tag" style="background: #f5f3ff; color: #8b5cf6;">💆‍♀️ パサつき静電気・頭皮コリ解消 NEW</span>
        <h2 class="hub-card-title">💆‍♀️ 保湿力の強さで冬のパサつき剛毛・冷えたガチガチ頭皮とさようなら！塗った瞬間じんわり温感で美髪成分が急速浸透する温感ヘッドスパトリートメントランク10</h2>
        <p class="hub-card-desc">11月・12月の寒さで凝り固まったガチガチ頭皮と、静電気・暖房乾燥でパサつく毛先をダブルで救済！moremo、ヘッドスパセブン、トリコレ、サロニア、アミノレスキューなど、水と反応して温感クリームへ変化する最新温感トリートメント10選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-oil-mist' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
