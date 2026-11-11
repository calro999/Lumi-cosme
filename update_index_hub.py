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
newest_cards = """      <!-- 高保湿セラミドシートマスク -->
      <a href="/winter-ceramide-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0284c7;">❄️ ナノセラミド・密閉オクルージョン浸透 NEW</span>
        <h2 class="hub-card-title">❄️ 保湿力の強さで肌乾燥とさようなら！高密度ナノセラミドと濃密マイクロファイバーシートで真冬の寒冷脱水肌を一撃で蘇らせる保湿力高めセラミドシートマスクランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥・粉吹き・暖房インナードライを徹底救済！ミノン、キュレル、トリデン、ドクタージャルト、ルルルンまで高密度ナノセラミドシートマスクの科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿リップスリーピングマスク -->
      <a href="/winter-lip-sleeping-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #ffe4e6; color: #e11d48;">🌙 就寝中集中密閉・角質自然軟化剥離 NEW</span>
        <h2 class="hub-card-title">🌙 保湿力の強さで肌乾燥とさようなら！就寝中の濃厚密閉ラッピング処方で真冬のガサガサ皮剥け唇をぷるんと再生する保湿力高めリップスリーピングマスクランク10</h2>
        <p class="hub-card-desc">11月・12月の夜間暖房と寒冷乾燥による唇の皮剥け・縦ジワ・ひび割れを徹底救済！ラネージュ、トリデン、ニベア、CNP、キュレルまで夜用高密着リップスリーピングマスクの科学的修復メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿バリア美容液 -->
      <a href="/winter-barrier-serum" class="hub-card">
        <span class="hub-card-tag" style="background: #d1fae5; color: #059669;">🧪 微細リポソーム・暖房インナードライ鎮静 NEW</span>
        <h2 class="hub-card-title">🧪 保湿力の強さで肌乾燥とさようなら！微細リポソーム化バリア成分とパンテノールの生体浸透力で真冬の暖房インナードライを芯から鎮静する保湿力高めバリア美容液ランク10</h2>
        <p class="hub-card-desc">11月・12月の暖房直撃によるインナードライ・赤み・ピリつきを徹底救済！エストラ、トリデン、dプログラム、キュレル、魔女工場、コーセーまで高保湿バリア美容液の科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-ceramide-mask' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + newest_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")

# 2. 関連ハブページへの誘導追加
# A. winter-face-mask.html への誘導追加
if os.path.exists("winter-face-mask.html"):
    with open("winter-face-mask.html", "r", encoding="utf-8") as f:
        mask_html = f.read()
    if "/winter-ceramide-mask" not in mask_html:
        guide_banner = """
    <div style="background:linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);border:2px solid #0284c7;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#0369a1;margin-bottom:8px;font-size:1.2rem;">❄️ 11月・12月の寒冷砂漠肌に！高保湿セラミドシートマスク特集</h3>
      <p style="color:#334155;margin-bottom:16px;font-size:0.95rem;">通常のフェイスマスクでは追いつかない冬の粉吹き・寒冷脱水には、高密度ナノセラミドをたっぷり浸透させた高密着シートが効果的です。ミノンやキュレル、トリデンなど厳選10選を詳しく解説！</p>
      <a href="/winter-ceramide-mask" style="display:inline-block;background:#0284c7;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿セラミドシートマスクランキング10選を見る →</a>
    </div>
"""
        if "</main>" in mask_html:
            mask_html = mask_html.replace("</main>", guide_banner + "\n  </main>")
        with open("winter-face-mask.html", "w", encoding="utf-8") as f:
            f.write(mask_html)
        print("Updated winter-face-mask.html with guide banner!")

# B. winter-lip-care.html への誘導追加
if os.path.exists("winter-lip-care.html"):
    with open("winter-lip-care.html", "r", encoding="utf-8") as f:
        lip_html = f.read()
    if "/winter-lip-sleeping-mask" not in lip_html:
        guide_banner = """
    <div style="background:linear-gradient(135deg, #ffe4e6 0%, #fecdd3 100%);border:2px solid #e11d48;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#881337;margin-bottom:8px;font-size:1.2rem;">🌙 寝ている間に集中密閉再生！高保湿リップスリーピングマスク特集</h3>
      <p style="color:#4c0519;margin-bottom:16px;font-size:0.95rem;">日中のリップ塗り直しだけでは治らない真冬のガサガサ皮剥け・縦ジワには、就寝中の8時間密閉ラッピングが必須！ラネージュやトリデン、ニベアなど人気10選を徹底検証！</p>
      <a href="/winter-lip-sleeping-mask" style="display:inline-block;background:#e11d48;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿リップスリーピングマスクランキング10選を見る →</a>
    </div>
"""
        if "</main>" in lip_html:
            lip_html = lip_html.replace("</main>", guide_banner + "\n  </main>")
        with open("winter-lip-care.html", "w", encoding="utf-8") as f:
            f.write(lip_html)
        print("Updated winter-lip-care.html with guide banner!")

# C. winter-barrier-cream.html への誘導追加
if os.path.exists("winter-barrier-cream.html"):
    with open("winter-barrier-cream.html", "r", encoding="utf-8") as f:
        barrier_html = f.read()
    if "/winter-barrier-serum" not in barrier_html:
        guide_banner = """
    <div style="background:linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);border:2px solid #059669;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#064e3b;margin-bottom:8px;font-size:1.2rem;">🧪 クリームの前に仕込む！高保湿バリア美容液特集</h3>
      <p style="color:#065f46;margin-bottom:16px;font-size:0.95rem;">バリアクリームでフタをする前に、角層深部に微細リポソーム化セラミドやパンテノールを満たすことで、暖房インナードライを根本解決！エストラやdプログラムなど厳選10選を公開中！</p>
      <a href="/winter-barrier-serum" style="display:inline-block;background:#059669;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿バリア美容液ランキング10選を見る →</a>
    </div>
"""
        if "</main>" in barrier_html:
            barrier_html = barrier_html.replace("</main>", guide_banner + "\n  </main>")
        with open("winter-barrier-cream.html", "w", encoding="utf-8") as f:
            f.write(barrier_html)
        print("Updated winter-barrier-cream.html with guide banner!")
