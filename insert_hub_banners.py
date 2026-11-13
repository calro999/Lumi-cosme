import os

# 1. winter-face-mask.html
with open("winter-face-mask.html", "r", encoding="utf-8") as f:
    h = f.read()

banner_mask = """
    <!-- 新着特集バナー: 高保湿ヒアルロン酸シートマスク -->
    <div style="background:linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);border:2px solid #0284c7;border-radius:12px;padding:24px;margin:28px 0;box-shadow:0 4px 6px -1px rgba(2,132,199,0.15);">
      <span style="display:inline-block;background:#0284c7;color:#fff;font-size:0.75rem;font-weight:800;padding:3px 10px;border-radius:9999px;margin-bottom:8px;">2026年11月・12月 冬季最新特集</span>
      <h3 style="color:#0369a1;margin-bottom:8px;font-size:1.25rem;font-weight:800;">💧 暖房砂漠肌を即リセット！高保湿ヒアルロン酸シートマスク厳選10選</h3>
      <p style="color:#334155;margin-bottom:14px;font-size:0.95rem;line-height:1.6;">自重の約6,000倍の水分を抱え込む多段分子ヒアルロン酸（5D・8重複合体）と極薄密着シートが、真冬の暖房脱水・インナードライを秒速充填！トリデン、メディヒール、ドクタージャルト、ルルルンなど最新ランキングを詳しく解説！</p>
      <a href="/winter-hyaluronic-mask" style="display:inline-block;background:#0284c7;color:#fff;font-weight:700;padding:10px 22px;border-radius:6px;text-decoration:none;box-shadow:0 2px 4px rgba(2,132,199,0.2);">高保湿ヒアルロン酸シートマスクランキング10選を見る →</a>
    </div>
"""

if '<!-- 新着特集バナー: 高保湿ヒアルロン酸シートマスク -->' not in h:
    if '<div class="toc-box">' in h:
        h = h.replace('<div class="toc-box">', banner_mask + '\n    <div class="toc-box">')
    elif '</main>' in h:
        h = h.replace('</main>', banner_mask + '\n  </main>')
    with open("winter-face-mask.html", "w", encoding="utf-8") as f:
        f.write(h)
    print("Added dedicated top banner to winter-face-mask.html!")

# 2. winter-serum-booster.html
with open("winter-serum-booster.html", "r", encoding="utf-8") as f:
    h = f.read()

banner_booster = """
    <!-- 新着特集バナー: 高保湿セラミド導入美容液 -->
    <div style="background:linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);border:2px solid #059669;border-radius:12px;padding:24px;margin:28px 0;box-shadow:0 4px 6px -1px rgba(5,150,105,0.15);">
      <span style="display:inline-block;background:#059669;color:#fff;font-size:0.75rem;font-weight:800;padding:3px 10px;border-radius:9999px;margin-bottom:8px;">2026年11月・12月 冬季最新特集</span>
      <h3 style="color:#065f46;margin-bottom:8px;font-size:1.25rem;font-weight:800;">🛡️ 寒冷角質硬化を一撃でほぐす！高保湿セラミド導入美容液厳選10選</h3>
      <p style="color:#064e3b;margin-bottom:14px;font-size:0.95rem;line-height:1.6;">寒さで化粧水が入らない冬のゴワつき肌に、ヒト型ナノセラミドの生体適合ブースト処方が浸透水路を開拓！アスタリフト、エトヴォス、ONE BY KOSE、トワニーなど厳選10選を徹底検証！</p>
      <a href="/winter-ceramide-booster" style="display:inline-block;background:#059669;color:#fff;font-weight:700;padding:10px 22px;border-radius:6px;text-decoration:none;box-shadow:0 2px 4px rgba(5,150,105,0.2);">高保湿セラミド導入美容液ランキング10選を見る →</a>
    </div>
"""

if '<!-- 新着特集バナー: 高保湿セラミド導入美容液 -->' not in h:
    if '<div class="toc-box">' in h:
        h = h.replace('<div class="toc-box">', banner_booster + '\n    <div class="toc-box">')
    elif '</main>' in h:
        h = h.replace('</main>', banner_booster + '\n  </main>')
    with open("winter-serum-booster.html", "w", encoding="utf-8") as f:
        f.write(h)
    print("Added dedicated top banner to winter-serum-booster.html!")

# 3. winter-collagen.html
with open("winter-collagen.html", "r", encoding="utf-8") as f:
    h = f.read()

banner_collagen = """
    <!-- 新着特集バナー: 高保湿コラーゲン美容液 -->
    <div style="background:linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);border:2px solid #be123c;border-radius:12px;padding:24px;margin:28px 0;box-shadow:0 4px 6px -1px rgba(190,18,60,0.15);">
      <span style="display:inline-block;background:#be123c;color:#fff;font-size:0.75rem;font-weight:800;padding:3px 10px;border-radius:9999px;margin-bottom:8px;">2026年11月・12月 冬季最新特集</span>
      <h3 style="color:#881337;margin-bottom:8px;font-size:1.25rem;font-weight:800;">🧬 真冬の寒冷肌痩せ・たるみ毛穴を押し上げる！高保湿コラーゲン美容液厳選10選</h3>
      <p style="color:#4c0519;margin-bottom:14px;font-size:0.95rem;line-height:1.6;">真冬の冷気による血行不良と真皮しぼみを、超低分子生コラーゲンと弾力ペプチドの高密度ホールド膜で上向きリフト！メディキューブ、魔女工場、アスタリフト、シーラボなど厳選10選を公開中！</p>
      <a href="/winter-collagen-serum" style="display:inline-block;background:#be123c;color:#fff;font-weight:700;padding:10px 22px;border-radius:6px;text-decoration:none;box-shadow:0 2px 4px rgba(190,18,60,0.2);">高保湿コラーゲン美容液ランキング10選を見る →</a>
    </div>
"""

if '<!-- 新着特集バナー: 高保湿コラーゲン美容液 -->' not in h:
    if '<div class="toc-box">' in h:
        h = h.replace('<div class="toc-box">', banner_collagen + '\n    <div class="toc-box">')
    elif '</main>' in h:
        h = h.replace('</main>', banner_collagen + '\n  </main>')
    with open("winter-collagen.html", "w", encoding="utf-8") as f:
        f.write(h)
    print("Added dedicated top banner to winter-collagen.html!")
