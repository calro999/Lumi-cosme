import os
import re
from update_all_internal_links import footer_links_html

# 1. index.html の更新
with open("index.html", "r", encoding="utf-8") as f:
    idx_html = f.read()

# フッターリンク更新
if '<div class="footer-links">' in idx_html:
    idx_html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, idx_html, flags=re.DOTALL)

# 特集件数表記の更新
idx_html = re.sub(r'（全\d+特集公開中）', '（全241特集公開中）', idx_html)
idx_html = re.sub(r'（全\d+大特集）', '（全241特集公開中）', idx_html)

new_cards = """      <!-- 高保湿クレイマスク＆泥パック -->
      <a href="/winter-clay-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #ccfbf1; color: #134e4a;">🫧 お風呂で潤う・つっぱらない泥パック NEW</span>
        <h2 class="hub-card-title">お風呂で温まりながらくすみ・ゴワつきを潤いオフ！つっぱらない高保湿クレイマスク＆洗い流す泥パック厳選ランク10【11月・12月】</h2>
        <p class="hub-card-desc">シートマスクが冷たい冬の夜に！イプサ、キールズ、ビープレーン、イニスフリー、THREE、SKIN1004、VT、CLAYD、ナイアードガスール、クレージュまで乾燥しにくい保湿型クレイ10選を徹底比較。</p>
      </a>

      <!-- 冬の乾燥大人ニキビ高保湿ケア -->
      <a href="/winter-acne-moisture" class="hub-card">
        <span class="hub-card-tag" style="background: #cffafe; color: #164e63;">💧 乾燥大人ニキビ・ノンコメド保湿 NEW</span>
        <h2 class="hub-card-title">冬の乾燥大人ニキビを乾かさず鎮静！高保湿×ノンコメドジェニック薬用スキンケアおすすめランク10【11月・12月】</h2>
        <p class="hub-card-desc">頬は乾くのにアゴや口周りにニキビができる冬悩みへ。dプログラム、オルビス クリアフル、ミノン、ノブ ACアクティブ、キュレル、ファンケル、イハダ、カルテHDバランスケアなど10選を検証。</p>
      </a>

      <!-- 高保湿パウダーファンデーション -->
      <a href="/winter-powder-foundation" class="hub-card">
        <span class="hub-card-tag" style="background: #ffe4e6; color: #881337;">✨ 粉吹きゼロ・真冬のしっとり密着パウダリー NEW</span>
        <h2 class="hub-card-title">保湿力の強さで粉吹き肌とさようなら！真冬もしっとり密着する保湿力高めパウダーファンデーションランク10【11月・12月】</h2>
        <p class="hub-card-desc">冬でも手軽にしっとり仕上がる！マキアージュ、アルビオン パウダレスト、クレ・ド・ポー ボーテ タンプードルエクラII、カバーマーク、エスプリーク、プリマヴィスタ、エトヴォス、ヴァントルテなど10選。</p>
      </a>
"""

if '/winter-clay-mask' not in idx_html:
    idx_html = idx_html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_html)
print("Updated index.html!")

def insert_banner(fname, marker_url, banner_html):
    if not os.path.exists(fname):
        print(f"Skip missing: {fname}")
        return
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    if f'href="{marker_url}" style=' in content:
        print(f"Already has banner in {fname} for {marker_url}")
        return
    if '<section id="related"' in content:
        content = content.replace('<section id="related"', banner_html + '\n    <section id="related"', 1)
    elif '</main>' in content:
        content = content.replace('</main>', banner_html + '\n  </main>', 1)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Added banner for {marker_url} in {fname}")

# 2. winter-face-mask.html, winter-peel-serum.html, winter-bath-care.html -> /winter-clay-mask
clay_banner = """
    <!-- 新規追加：高保湿クレイマスク＆泥パック誘導バナー -->
    <div style="background:linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%);border:2px solid #0f766e;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#134e4a;margin-bottom:8px;font-size:1.18rem;">🫧 シートマスクが冷たい冬の夜に！お風呂で使える高保湿クレイマスク特集</h3>
      <p style="color:#1e293b;margin-bottom:16px;font-size:0.94rem;">寒さで硬くなった冬の角質や毛穴くすみを、湯船に浸かりながら穏やかにオフできる「つっぱらない保湿型クレイ＆泥パック」を特集。イプサ、キールズ、ビープレーン、THREE、ナイアードガスールなど10選を比較しています。</p>
      <a href="/winter-clay-mask" style="display:inline-block;background:#0f766e;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿クレイマスク＆泥パック10選を見る →</a>
    </div>"""
insert_banner("winter-face-mask.html", "/winter-clay-mask", clay_banner)
insert_banner("winter-peel-serum.html", "/winter-clay-mask", clay_banner)
insert_banner("winter-bath-care.html", "/winter-clay-mask", clay_banner)

# 3. winter-lotion.html, winter-moisture-cream.html, winter-cica-cream.html, winter-azelaic-acid.html -> /winter-acne-moisture
acne_banner = """
    <!-- 新規追加：冬の乾燥大人ニキビ高保湿ケア誘導バナー -->
    <div style="background:linear-gradient(135deg, #ecfeff 0%, #cffafe 100%);border:2px solid #0e7490;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#164e63;margin-bottom:8px;font-size:1.18rem;">💧 頬は乾くのにアゴにニキビ…11月・12月の乾燥大人ニキビ向け高保湿ケア特集</h3>
      <p style="color:#0f172a;margin-bottom:16px;font-size:0.94rem;">暖房によるインナードライやマフラー摩擦で悪化しやすい冬の大人ニキビを、乾かさず穏やかにケアする薬用・ノンコメドジェニック保湿10選。dプログラム、オルビス クリアフル、ミノン、カルテHDバランスケア等を徹底比較しています。</p>
      <a href="/winter-acne-moisture" style="display:inline-block;background:#0e7490;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">冬の乾燥大人ニキビ高保湿ケア10選を見る →</a>
    </div>"""
insert_banner("winter-lotion.html", "/winter-acne-moisture", acne_banner)
insert_banner("winter-moisture-cream.html", "/winter-acne-moisture", acne_banner)
insert_banner("winter-cica-cream.html", "/winter-acne-moisture", acne_banner)
insert_banner("winter-azelaic-acid.html", "/winter-acne-moisture", acne_banner)

# 4. winter-base-makeup.html, winter-powder.html, winter-makeup-primer.html -> /winter-powder-foundation
pf_banner = """
    <!-- 新規追加：高保湿パウダーファンデーション誘導バナー -->
    <div style="background:linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);border:2px solid #9f1239;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#881337;margin-bottom:8px;font-size:1.18rem;">✨ 朝1分で粉吹きゼロ！真冬もしっとり密着する高保湿パウダーファンデーション特集</h3>
      <p style="color:#1f2937;margin-bottom:16px;font-size:0.94rem;">ムース製法や保湿オイル・セラミド配合で冬の乾いた頬にも溶け込む最新パウダーファンデ10選を公開中。マキアージュ、アルビオン パウダレスト、タンプードルエクラII、カバーマーク、エトヴォスなどを厳選比較しています。</p>
      <a href="/winter-powder-foundation" style="display:inline-block;background:#9f1239;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿パウダーファンデーション10選を見る →</a>
    </div>"""
insert_banner("winter-base-makeup.html", "/winter-powder-foundation", pf_banner)
insert_banner("winter-powder.html", "/winter-powder-foundation", pf_banner)
insert_banner("winter-makeup-primer.html", "/winter-powder-foundation", pf_banner)
