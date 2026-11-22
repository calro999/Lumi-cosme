import os
import re
from update_all_internal_links import footer_links_html

# 1. index.html の更新
with open("index.html", "r", encoding="utf-8") as f:
    idx_html = f.read()

if '<div class="footer-links">' in idx_html:
    idx_html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, idx_html, flags=re.DOTALL)

idx_html = re.sub(r'（全\d+特集公開中）', '（全244特集公開中）', idx_html)
idx_html = re.sub(r'（全\d+大特集）', '（全244特集公開中）', idx_html)

new_cards = """      <!-- 高保湿クレンジングウォーター -->
      <a href="/winter-cleansing-water" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0c4a6e;">❄️ W洗顔不要・冬の摩擦レス水クレンジング NEW</span>
        <h2 class="hub-card-title">保湿力の強さで冬洗顔のつっぱりとさようなら！W洗顔不要の高保湿クレンジングウォーター（ミセラー水）ランク10【11月・12月】</h2>
        <p class="hub-card-desc">寒い洗面所の冷水洗顔がつらい夜や乾燥する朝に！ビオデルマ、江原道、チャコット、ビフェスタ、資生堂dプログラム、クレ・ド・ポー ボーテ、ユリアージュ、エチュード、魔女工場、ラロッシュポゼまで10選を徹底比較。</p>
      </a>

      <!-- お湯落ち高保湿・美容液マスカラ -->
      <a href="/winter-moisture-mascara" class="hub-card">
        <span class="hub-card-tag" style="background: #fce7f3; color: #831843;">👁️ 目元乾燥小ジワを防ぐ・お湯落ち美容液マスカラ NEW</span>
        <h2 class="hub-card-title">冬の目元乾燥とパンダ目を同時に防ぐ！まつ毛を労わるお湯落ち高保湿・美容液マスカラ厳選10選【11月・12月】</h2>
        <p class="hub-card-desc">11月・12月の目元乾燥＆クレンジング摩擦を回避！デジャヴュ、ヒロインメイク アドバンストフィルム、オペラ、D-UP、クリニーク、ウォンジョンヨ、スカルプD、UZU、エトヴォス、メイベリンなど10本を比較検証。</p>
      </a>

      <!-- 11月・12月向け人気ブランド高保湿ギフトセット -->
      <a href="/winter-gift-set" class="hub-card">
        <span class="hub-card-tag" style="background: #dcfce7; color: #14532d;">🎁 クリスマス＆年末お礼に・定番高保湿ギフト NEW</span>
        <h2 class="hub-card-title">11月・12月の贈り物に外さない！冬の乾燥肌を潤す人気ブランド高保湿ハンド＆ボディ・リップギフトセット厳選10選</h2>
        <p class="hub-card-desc">限定コフレが完売でも贈れる実力派！ロクシタン、イソップ、ジルスチュアート、サボン、ディオール、SHIRO、ジョンマスター、ニールズヤード、ポール＆ジョー、アユーラまで予算別・相手別に徹底比較。</p>
      </a>
"""

if '/winter-cleansing-water' not in idx_html:
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

# 2. winter-cleansing.html, winter-wipe-lotion.html, winter-point-makeup-remover.html -> /winter-cleansing-water
cw_banner = """
    <!-- 新規追加：高保湿クレンジングウォーター誘導バナー -->
    <div style="background:linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);border:2px solid #0284c7;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#0c4a6e;margin-bottom:8px;font-size:1.18rem;">❄️ 寒い夜や朝の冷水洗顔を卒業！W洗顔不要の高保湿クレンジングウォーター特集</h3>
      <p style="color:#0f172a;margin-bottom:16px;font-size:0.94rem;">熱いお湯すすぎによる冬の皮脂膜流出を防ぎながらメイクや汚れをオフできる「ミセラー水クレンジング」を厳選。ビオデルマ、江原道、チャコット、dプログラム、クレ・ド・ポー ボーテ、魔女工場など10本を比較しています。</p>
      <a href="/winter-cleansing-water" style="display:inline-block;background:#0284c7;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿クレンジングウォーター10選を見る →</a>
    </div>"""
insert_banner("winter-cleansing.html", "/winter-cleansing-water", cw_banner)
insert_banner("winter-wipe-lotion.html", "/winter-cleansing-water", cw_banner)
insert_banner("winter-point-makeup-remover.html", "/winter-cleansing-water", cw_banner)

# 3. winter-base-makeup.html, winter-eyelash-serum.html, winter-cream-eyeshadow.html -> /winter-moisture-mascara
ms_banner = """
    <!-- 新規追加：お湯落ち高保湿・美容液マスカラ誘導バナー -->
    <div style="background:linear-gradient(135deg, #fdf2f8 0%, #fce7f3 100%);border:2px solid #9d174d;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#831843;margin-bottom:8px;font-size:1.18rem;">👁️ クレンジング摩擦で目元を乾かさない！お湯落ち高保湿・美容液マスカラ特集</h3>
      <p style="color:#1f2937;margin-bottom:16px;font-size:0.94rem;">11月・12月の目元ちりめんジワを防ぎながらパンダ目にもなりにくいフィルムマスカラ10選を公開中。デジャヴュ、ヒロインメイク アドバンストフィルム、クリニーク、ウォンジョンヨ、スカルプD、エトヴォスなどを徹底比較しています。</p>
      <a href="/winter-moisture-mascara" style="display:inline-block;background:#9d174d;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">お湯落ち高保湿・美容液マスカラ10選を見る →</a>
    </div>"""
insert_banner("winter-base-makeup.html", "/winter-moisture-mascara", ms_banner)
insert_banner("winter-eyelash-serum.html", "/winter-moisture-mascara", ms_banner)
insert_banner("winter-cream-eyeshadow.html", "/winter-moisture-mascara", ms_banner)

# 4. winter-holiday-coffret.html, winter-hand-care.html, winter-body-care.html, winter-lip-care.html -> /winter-gift-set
gf_banner = """
    <!-- 新規追加：人気ブランド高保湿ギフトセット誘導バナー -->
    <div style="background:linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);border:2px solid #15803d;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#14532d;margin-bottom:8px;font-size:1.18rem;">🎁 クリスマス＆年末お礼に外さない！人気ブランド高保湿ハンド＆ボディギフト特集</h3>
      <p style="color:#1c1917;margin-bottom:16px;font-size:0.94rem;">限定コフレが売り切れでもすぐ贈れて色選びの失敗がない、定番ラグジュアリー＆人気ブランドの高保湿ギフトセット10選！ロクシタン、イソップ、ジルスチュアート、サボン、ディオール、SHIRO、アユーラ等を予算別にご紹介しています。</p>
      <a href="/winter-gift-set" style="display:inline-block;background:#15803d;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">冬の高保湿ギフトセット10選を見る →</a>
    </div>"""
insert_banner("winter-holiday-coffret.html", "/winter-gift-set", gf_banner)
insert_banner("winter-hand-care.html", "/winter-gift-set", gf_banner)
insert_banner("winter-body-care.html", "/winter-gift-set", gf_banner)
insert_banner("winter-lip-care.html", "/winter-gift-set", gf_banner)
