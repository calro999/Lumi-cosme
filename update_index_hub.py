import re
import os
from update_all_internal_links import footer_links_html

# 1. index.html の更新
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# フッターリンクの更新
if '<div class="footer-links">' in html:
    html = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, html, flags=re.DOTALL)
elif '<div class="footer-links-grid" id="footer-links-box">' in html:
    html = re.sub(r'<div class="footer-links-grid" id="footer-links-box">.*?</div>', '<div class="footer-links-grid" id="footer-links-box">\n' + footer_links_html + '\n          </div>', html, flags=re.DOTALL)

# 新規3記事のカード定義
brand_new_cards = """      <!-- 高保湿ヒアルロン酸シートマスク -->
      <a href="/winter-hyaluronic-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">💧 多段ヒアルロン酸・暖房脱水救済 NEW</span>
        <h2 class="hub-card-title">💧 保湿力の強さで肌乾燥とさようなら！多段分子ヒアルロン酸の圧倒的保水ヴェールと高密着セルロース膜で真冬の暖房脱水肌を満たす保湿力高めヒアルロン酸シートマスクランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥・暖房直撃によるインナードライ・カサつき・メイク崩れを一撃救済！トリデン、メディヒール、ドクタージャルト、ルルルン、クオリティファーストまで高保湿ヒアルロン酸シートマスクの科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿セラミド導入美容液 -->
      <a href="/winter-ceramide-booster" class="hub-card">
        <span class="hub-card-tag" style="background: #d1fae5; color: #047857;">🛡️ ヒト型ナノセラミド・硬直角質柔軟ブースト NEW</span>
        <h2 class="hub-card-title">🛡️ 保湿力の強さで肌乾燥とさようなら！ヒト型ナノセラミドの角層柔軟力と先行浸透ブースト処方で真冬の硬直ゴワつき肌を解きほぐす保湿力高めセラミド導入美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥で化粧水が入らないゴワつき肌を一撃で解きほぐす！アスタリフト、エトヴォス、コーセー、トワニー、キュレルまで高保湿セラミド導入美容液（先行美容液・ブースター）の科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿コラーゲン美容液 -->
      <a href="/winter-collagen-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #ffe4e6; color: #9f1239;">🧬 超低分子生コラーゲン・寒冷肌痩せリフト NEW</span>
        <h2 class="hub-card-title">🧬 保湿力の強さで肌乾燥とさようなら！超低分子生コラーゲンの高密度ホールド膜と弾力ペプチド処方で真冬の寒冷肌痩せ・たるみ毛穴を押し上げる保湿力高めコラーゲン美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷刺激による肌痩せ・たるみ毛穴・乾燥小ジワを徹底撃退！メディキューブ、魔女工場、アスタリフト、ドクターシーラボ、ファンケルまで高保湿コラーゲン美容液の科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-hyaluronic-mask' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + brand_new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")

# 2. 関連ハブページへの誘導追加
# A. winter-face-mask.html への誘導追加
if os.path.exists("winter-face-mask.html"):
    with open("winter-face-mask.html", "r", encoding="utf-8") as f:
        mask_html = f.read()
    if "/winter-hyaluronic-mask" not in mask_html:
        guide_banner = """
    <div style="background:linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);border:2px solid #0284c7;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#0369a1;margin-bottom:8px;font-size:1.2rem;">💧 暖房砂漠肌を即リセット！高保湿ヒアルロン酸シートマスク特集</h3>
      <p style="color:#334155;margin-bottom:16px;font-size:0.95rem;">自重の約6,000倍の保水力を誇る多段分子ヒアルロン酸と極薄密着シートが、真冬の暖房脱水・インナードライを秒速充填！トリデン、メディヒール、ドクタージャルト、ルルルンなど厳選10選を詳しく解説！</p>
      <a href="/winter-hyaluronic-mask" style="display:inline-block;background:#0284c7;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿ヒアルロン酸シートマスクランキング10選を見る →</a>
    </div>
"""
        if "</main>" in mask_html:
            mask_html = mask_html.replace("</main>", guide_banner + "\n  </main>")
        with open("winter-face-mask.html", "w", encoding="utf-8") as f:
            f.write(mask_html)
        print("Updated winter-face-mask.html with hyaluronic mask guide banner!")

# B. winter-serum-booster.html への誘導追加
if os.path.exists("winter-serum-booster.html"):
    with open("winter-serum-booster.html", "r", encoding="utf-8") as f:
        booster_html = f.read()
    if "/winter-ceramide-booster" not in booster_html:
        guide_banner = """
    <div style="background:linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);border:2px solid #059669;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#065f46;margin-bottom:8px;font-size:1.2rem;">🛡️ 真冬の寒冷角質硬化を解きほぐす！高保湿セラミド導入美容液特集</h3>
      <p style="color:#064e3b;margin-bottom:16px;font-size:0.95rem;">寒さで化粧水が入らない冬のゴワつき肌に、ヒト型ナノセラミドの生体適合ブースト処方が浸透水路を開拓！アスタリフト、エトヴォス、ONE BY KOSE、トワニーなど厳選10選を徹底検証！</p>
      <a href="/winter-ceramide-booster" style="display:inline-block;background:#059669;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿セラミド導入美容液ランキング10選を見る →</a>
    </div>
"""
        if "</main>" in booster_html:
            booster_html = booster_html.replace("</main>", guide_banner + "\n  </main>")
        with open("winter-serum-booster.html", "w", encoding="utf-8") as f:
            f.write(booster_html)
        print("Updated winter-serum-booster.html with ceramide booster guide banner!")

# C. winter-collagen.html への誘導追加
if os.path.exists("winter-collagen.html"):
    with open("winter-collagen.html", "r", encoding="utf-8") as f:
        col_html = f.read()
    if "/winter-collagen-serum" not in col_html:
        guide_banner = """
    <div style="background:linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);border:2px solid #be123c;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#881337;margin-bottom:8px;font-size:1.2rem;">🧬 真冬の寒冷肌痩せ・たるみ毛穴を押し上げる！高保湿コラーゲン美容液特集</h3>
      <p style="color:#4c0519;margin-bottom:16px;font-size:0.95rem;">真冬の冷気による血行不良と真皮しぼみを、超低分子生コラーゲンと弾力ペプチドの高密度ホールド膜で上向きリフト！メディキューブ、魔女工場、アスタリフト、シーラボなど厳選10選を公開中！</p>
      <a href="/winter-collagen-serum" style="display:inline-block;background:#be123c;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿コラーゲン美容液ランキング10選を見る →</a>
    </div>
"""
        if "</main>" in col_html:
            col_html = col_html.replace("</main>", guide_banner + "\n  </main>")
        with open("winter-collagen.html", "w", encoding="utf-8") as f:
            f.write(col_html)
        print("Updated winter-collagen.html with collagen serum guide banner!")
