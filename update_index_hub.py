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
brand_new_cards = """      <!-- 高保湿PDRNシートマスク -->
      <a href="/winter-pdrn-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">🧬 サーモンDNA・細胞間再生浸透 NEW</span>
        <h2 class="hub-card-title">🧬 保湿力の強さで肌乾燥とさようなら！高純度サーモンDNA・PDRNの細胞間再生力とバイオセルロース密着膜で真冬のしぼみ肌を跳ね返す保湿力高めPDRNシートマスクランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥・暖房脱水・肌痩せ・毛穴の開きを一撃再生！リジュラン、VT、メディヒール、アヌア、IOPE、KISOまで最先端高保湿PDRNシートマスクの科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿レチノールアイクリーム -->
      <a href="/winter-retinol-eye-cream" class="hub-card">
        <span class="hub-card-tag" style="background: #f3e8ff; color: #7e22ce;">👁️ 純粋レチノール・目元ちりめんジワ撃退 NEW</span>
        <h2 class="hub-card-title">👁️ 保湿力の強さで肌乾燥とさようなら！純粋レチノールの角層深部ターンオーバー促進と密着リペアバーム処方で真冬の目元ちりめんジワをふっくら伸ばす保湿力高めレチノールアイクリームランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥・エアコン暖房・まばたき摩擦による目元の小ジワ・ちりめんジワ・たるみを徹底撃退！エリクシール、ポーラ、なめらか本舗、KISO、AHC、アスタリフトまで最新実勢価格・口コミ・科学的シワ改善メカニズムを網羅。</p>
      </a>

      <!-- 高保湿パンテノールバーム -->
      <a href="/winter-panthenol-balm" class="hub-card">
        <span class="hub-card-tag" style="background: #dcfce7; color: #047857;">🛡️ 高濃度パンテノール・寒冷粉吹き緊急鎮静 NEW</span>
        <h2 class="hub-card-title">🛡️ 保湿力の強さで肌乾燥とさようなら！高濃度パンテノールの生体組織修復力と濃密密閉バリア膜で真冬のヒリヒリ粉吹き肌を緊急鎮静する保湿力高めパンテノールバームランク10</h2>
        <p class="hub-card-desc">11月・12月の寒冷乾燥・木枯らし・急激な暖房寒暖差による肌のヒリつき・粉吹き・赤みを緊急鎮静！ラロッシュポゼ、アベンヌ、エストラ、イハダ、キュレル、キールズまで最新実勢価格・口コミ・科学的生体修復メカニズムを網羅。</p>
      </a>\n"""

# まだ追加されていなければ hub-grid の直後に挿入
if '/winter-pdrn-mask' not in html:
    html = html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + brand_new_cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with 3 newest cards and latest footer links!")

# 2. 関連ハブページへの誘導追加
# A. winter-face-mask.html への誘導追加
if os.path.exists("winter-face-mask.html"):
    with open("winter-face-mask.html", "r", encoding="utf-8") as f:
        mask_html = f.read()
    if "/winter-pdrn-mask" not in mask_html:
        guide_banner = """
    <div style="background:linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);border:2px solid #0284c7;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#0369a1;margin-bottom:8px;font-size:1.2rem;">🧬 最先端美容医療発想！高保湿PDRNシートマスク特集</h3>
      <p style="color:#334155;margin-bottom:16px;font-size:0.95rem;">寒冷による肌痩せ・しぼみ肌・たるみ毛穴を根本から立て直すサーモンDNA由来PDRN配合マスクを徹底検証！リジュラン、VT、メディヒール、アヌアなど話題の10選を詳しく解説！</p>
      <a href="/winter-pdrn-mask" style="display:inline-block;background:#0284c7;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿PDRNシートマスクランキング10選を見る →</a>
    </div>
"""
        if "</main>" in mask_html:
            mask_html = mask_html.replace("</main>", guide_banner + "\n  </main>")
        with open("winter-face-mask.html", "w", encoding="utf-8") as f:
            f.write(mask_html)
        print("Updated winter-face-mask.html with PDRN mask guide banner!")

# B. winter-eye-cream.html への誘導追加
if os.path.exists("winter-eye-cream.html"):
    with open("winter-eye-cream.html", "r", encoding="utf-8") as f:
        eye_html = f.read()
    if "/winter-retinol-eye-cream" not in eye_html:
        guide_banner = """
    <div style="background:linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 100%);border:2px solid #9333ea;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#581c87;margin-bottom:8px;font-size:1.2rem;">👁️ 真冬の目元ちりめんジワを集中修復！高保湿レチノールアイクリーム特集</h3>
      <p style="color:#3b0764;margin-bottom:16px;font-size:0.95rem;">皮膚の薄い目元の乾燥小ジワ・まぶたのたるみには、純粋レチノールと密着リペアバーム処方が効果的！エリクシールやPOLA、なめらか本舗、KISOなど厳選10選を徹底検証！</p>
      <a href="/winter-retinol-eye-cream" style="display:inline-block;background:#9333ea;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿レチノールアイクリームランキング10選を見る →</a>
    </div>
"""
        if "</main>" in eye_html:
            eye_html = eye_html.replace("</main>", guide_banner + "\n  </main>")
        with open("winter-eye-cream.html", "w", encoding="utf-8") as f:
            f.write(eye_html)
        print("Updated winter-eye-cream.html with retinol eye cream guide banner!")

# C. winter-repair-balm.html への誘導追加
if os.path.exists("winter-repair-balm.html"):
    with open("winter-repair-balm.html", "r", encoding="utf-8") as f:
        balm_html = f.read()
    if "/winter-panthenol-balm" not in balm_html:
        guide_banner = """
    <div style="background:linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);border:2px solid #059669;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#064e3b;margin-bottom:8px;font-size:1.2rem;">🛡️ 真冬の粉吹き・赤み・ヒリつきを緊急鎮静！高保湿パンテノールバーム特集</h3>
      <p style="color:#065f46;margin-bottom:16px;font-size:0.95rem;">木枯らしや急激な暖房寒暖差で角層バリアが崩壊した肌に、プロビタミンB5（高純度パンテノール）と濃密シールド膜が素早く浸透！ラロッシュポゼやアベンヌ、イハダなど厳選10選を公開中！</p>
      <a href="/winter-panthenol-balm" style="display:inline-block;background:#059669;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿パンテノールバームランキング10選を見る →</a>
    </div>
"""
        if "</main>" in balm_html:
            balm_html = balm_html.replace("</main>", guide_banner + "\n  </main>")
        with open("winter-repair-balm.html", "w", encoding="utf-8") as f:
            f.write(balm_html)
        print("Updated winter-repair-balm.html with panthenol balm guide banner!")
