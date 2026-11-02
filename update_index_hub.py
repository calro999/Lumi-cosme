import re
from update_all_internal_links import footer_links_html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)

# 新規3記事のカード定義
newest_cards = """      <!-- 高保湿セラミドクリーム -->
      <a href="/winter-ceramide-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #ebf8ff; color: #2b6cb0;">🧴 角層バリア再建・粉吹き乾燥撃退 NEW</span>
        <h2 class="hub-card-title">🧴 保湿力の強さで冬の肌荒れ・粉吹き乾燥とさようなら！角層バリアを高密度修復する高保湿セラミドクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の冬本番に深刻化する冷気と暖房による角層バリア破壊・粉吹き乾燥・ヒリつき肌を徹底解決！ヒト型セラミドや高濃度セラミドを贅沢配合した高保湿フェイスクリーム10選を徹底比較！キュレル、AESTURA、松山油脂、リアルバリア、エトヴォス、ケアセラなど厳選。</p>
      </a>

      <!-- 高保湿ペプチド美容液 -->
      <a href="/winter-peptide-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #faf5ff; color: #6b46c1;">🧬 塗るボトックス発想・ふっくら弾力 NEW</span>
        <h2 class="hub-card-title">🧬 保湿力の強さで冬の乾燥小ジワ・刻まれジワとさようなら！塗るボトックス発想でふっくら押し返す高保湿ペプチド美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷と暖房乾燥による表情ジワの定着・大人の乾燥小ジワ・ハリ低下を徹底解決！ボトックス注射発想のシンエイクやアセチルヘキサペプチド、複合ペプチドを高濃度配合した高保湿ペプチド美容液10選を徹底比較！The Ordinary、BIOHEAL BOH、メディキューブ、VT、魔女工場など厳選。</p>
      </a>

      <!-- 高保湿ヘアセラム -->
      <a href="/winter-hair-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #fff5f7; color: #b83280;">💇‍♀️ 毛先パサつき・静電気爆発撃退 NEW</span>
        <h2 class="hub-card-title">💇‍♀️ 保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！芯まで潤い満たす洗い流さない高保湿ヘアセラム・ヘアエッセンスランク10</h2>
        <p class="hub-card-desc">11月・12月の暖房直撃・マフラー摩擦・静電気による頑固な毛先のパサつき・枝毛・広がりを徹底解決！髪の内部コルテックスまで浸透して水分とケラチンを補給する洗い流さない高保湿ヘアセラム・ヘアエッセンス10選！ラサーナ、オルビス、ケラスターゼ、ミルボン、ロレアルなど厳選。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-ceramide-cream' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")
