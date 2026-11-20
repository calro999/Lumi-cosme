import os
import re
from update_all_internal_links import footer_links_html

# 1. index.html の更新
with open("index.html", "r", encoding="utf-8") as f:
    idx_html = f.read()

# フッターリンク更新
if '<div class="footer-links">' in idx_html:
    idx_html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, idx_html, flags=re.DOTALL)

# タイトル横のサブタイトルの件数更新
idx_html = re.sub(r'（全\d+大特集）', '（全238特集公開中）', idx_html)

new_cards = """      <!-- 高保湿オールインワンジェル＆クリーム -->
      <a href="/winter-all-in-one" class="hub-card">
        <span class="hub-card-tag" style="background: #ffedd5; color: #9a3412;">🧴 時短5秒で乾燥対策・朝夜対応 NEW</span>
        <h2 class="hub-card-title">真冬の朝5秒で角層までうるおう！乾燥知らずの高保湿オールインワンジェル＆クリーム厳選ランキング10【11月・12月】</h2>
        <p class="hub-card-desc">寒い朝の時短ケアや年末の帰省・旅行でも乾燥しない！カルテHD、アクアレーベル、ドクターシーラボ、カナデル、メディプラスゲルなど、モロモロが出にくく朝まで潤う高保湿オールインワン10選を徹底比較。</p>
      </a>

      <!-- 高保湿ビタミンC化粧水 -->
      <a href="/winter-vitamin-c-lotion" class="hub-card">
        <span class="hub-card-tag" style="background: #fef3c7; color: #b45309;">🍋 くすみ＆乾燥毛穴・しっとりVC化粧水 NEW</span>
        <h2 class="hub-card-title">冬のくすみも乾燥毛穴もまとめて潤す！しっとり高保湿ビタミンC化粧水おすすめランキング10選【11月・12月版】</h2>
        <p class="hub-card-desc">「ビタミンC化粧水＝夏向けで乾く」を覆す！VC100、ナンバーズイン5番、メラノCCしっとり、オバジC、ドクターケイなど、潤いと透明感を両立できる高保湿ビタミンC誘導体化粧水10選を徹底検証。</p>
      </a>

      <!-- メンズ高保湿スキンケア -->
      <a href="/winter-mens-skincare" class="hub-card">
        <span class="hub-card-tag" style="background: #dbeafe; color: #1e3a8a;">👔 髭剃り負け対策＆12月ギフトにも NEW</span>
        <h2 class="hub-card-title">髭剃り負けと冬の粉吹きを一掃！メンズ高保湿スキンケア人気ランキング10選【11月・12月の乾燥対策＆ギフトにも】</h2>
        <p class="hub-card-desc">ベタつきは苦手でも冬の乾燥は防ぎたい男性へ。オルビスミスター、SHISEIDO MEN、バルクオム、NULL、クワトロボタニコ、アスタリフトメンまで、日常ケアから12月のクリスマスギフトに喜ばれる名品を厳選。</p>
      </a>
"""

if '/winter-all-in-one' not in idx_html:
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
    # Avoid duplicate banner
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

# 2. winter-moisture-cream.html & winter-emulsion.html -> /winter-all-in-one
aio_banner = """
    <!-- 新規追加：高保湿オールインワン誘導バナー -->
    <div style="background:linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);border:2px solid #c2410c;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#9a3412;margin-bottom:8px;font-size:1.18rem;">🧴 寒い朝や忙しい夜は1本で完結！冬向け高保湿オールインワン特集</h3>
      <p style="color:#431407;margin-bottom:16px;font-size:0.94rem;">化粧水・乳液・クリームを重ねる余裕がない朝や、年末の旅行・帰省には「油分乳化型」の高保湿オールインワンが便利。モロモロが出にくく朝まで乾きにくいカルテHD、アクアレーベル、ドクターシーラボなど10製品を比較しています。</p>
      <a href="/winter-all-in-one" style="display:inline-block;background:#c2410c;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿オールインワンランキング10選を見る →</a>
    </div>"""
insert_banner("winter-moisture-cream.html", "/winter-all-in-one", aio_banner)
insert_banner("winter-emulsion.html", "/winter-all-in-one", aio_banner)

# 3. winter-lotion.html & winter-vitamin-c-serum.html -> /winter-vitamin-c-lotion
vc_banner = """
    <!-- 新規追加：高保湿ビタミンC化粧水誘導バナー -->
    <div style="background:linear-gradient(135deg, #fefce8 0%, #fef3c7 100%);border:2px solid #d97706;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#b45309;margin-bottom:8px;font-size:1.18rem;">🍋 冬のくすみ・乾燥毛穴に！しっとり高保湿ビタミンC化粧水特集</h3>
      <p style="color:#451a03;margin-bottom:16px;font-size:0.94rem;">冷えによる顔色の冴えなさや暖房による毛穴の目立ちが気になる11月・12月におすすめの「とろみ系・高保湿ビタミンC誘導体化粧水」を厳選。VC100、ナンバーズイン5番、メラノCCしっとり、オバジC、ドクターケイなど10選をまとめました。</p>
      <a href="/winter-vitamin-c-lotion" style="display:inline-block;background:#d97706;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿ビタミンC化粧水ランキング10選を見る →</a>
    </div>"""
insert_banner("winter-lotion.html", "/winter-vitamin-c-lotion", vc_banner)
insert_banner("winter-vitamin-c-serum.html", "/winter-vitamin-c-lotion", vc_banner)

# 4. winter-holiday-coffret.html, winter-lotion.html, winter-face-wash.html -> /winter-mens-skincare
mens_banner = """
    <!-- 新規追加：メンズ高保湿スキンケア誘導バナー -->
    <div style="background:linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);border:2px solid #1d4ed8;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#1e3a8a;margin-bottom:8px;font-size:1.18rem;">👔 冬の髭剃り負け対策＆12月ギフトに！メンズ高保湿スキンケア特集</h3>
      <p style="color:#172554;margin-bottom:16px;font-size:0.94rem;">カサつきやカミソリ負けに悩む男性の毎日ケアはもちろん、12月のクリスマスプレゼントにも人気のメンズコスメを特集。オルビスミスター、SHISEIDO MEN、バルクオム、アスタリフトメンなどベタつかない高保湿10選を公開中です。</p>
      <a href="/winter-mens-skincare" style="display:inline-block;background:#1d4ed8;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">メンズ高保湿スキンケアランキング10選を見る →</a>
    </div>"""
insert_banner("winter-holiday-coffret.html", "/winter-mens-skincare", mens_banner)
insert_banner("winter-lotion.html", "/winter-mens-skincare", mens_banner)
insert_banner("winter-face-wash.html", "/winter-mens-skincare", mens_banner)
