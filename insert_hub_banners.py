import os

# A. winter-face-mask.html へのバナー追加
if os.path.exists("winter-face-mask.html"):
    with open("winter-face-mask.html", "r", encoding="utf-8") as f:
        html = f.read()
    if "寒暖差の赤み・暖房荒れを秒速鎮静" not in html:
        banners = """
    <!-- 新規追加：高保湿CICA＆グルタチオンシートマスク誘導バナー -->
    <div style="background:linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);border:2px solid #16a34a;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#15803d;margin-bottom:8px;font-size:1.2rem;">🌿 寒暖差の赤み・暖房荒れを秒速鎮静！高保湿CICAシートマスク特集</h3>
      <p style="color:#14532d;margin-bottom:16px;font-size:0.95rem;">11月・12月の外気と暖房の激しい温度差で赤らんだゆらぎ肌を、高純度ツボクサエキス（マデカッソシド）と密着シートが心地よくクールダウン！VT、メディヒール、アピュー、ドクタージャルトなど厳選10選を詳しく解説！</p>
      <a href="/winter-cica-mask" style="display:inline-block;background:#16a34a;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿CICAシートマスクランキング10選を見る →</a>
    </div>

    <div style="background:linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);border:2px solid #9333ea;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#7e22ce;margin-bottom:8px;font-size:1.2rem;">✨ 真冬の寒冷血行不良くすみを晴らす！高保湿グルタチオンシートマスク特集</h3>
      <p style="color:#581c87;margin-bottom:16px;font-size:0.95rem;">冬の冷えによるどんより青白いチアノーゼ型くすみを、美容医療の白玉点滴発想「高純度グルタチオン」とビタミンC多重浸透膜で一掃！ナンバーズイン、ルルルン、VT、クオリティファーストなど厳選10選を徹底検証！</p>
      <a href="/winter-glutathione-mask" style="display:inline-block;background:#9333ea;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿グルタチオンシートマスクランキング10選を見る →</a>
    </div>
"""
        if "</main>" in html:
            html = html.replace("</main>", banners + "\n  </main>")
            with open("winter-face-mask.html", "w", encoding="utf-8") as f:
                f.write(html)
            print("Successfully added banners to winter-face-mask.html!")

# B. winter-lotion.html へのバナー追加
if os.path.exists("winter-lotion.html"):
    with open("winter-lotion.html", "r", encoding="utf-8") as f:
        html = f.read()
    if "真冬の深層インナードライを潤し尽くす" not in html:
        banner = """
    <!-- 新規追加：高保湿ヒアルロン酸化粧水誘導バナー -->
    <div style="background:linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);border:2px solid #0284c7;border-radius:12px;padding:24px;margin:32px 0;">
      <h3 style="color:#0369a1;margin-bottom:8px;font-size:1.2rem;">💧 真冬の深層インナードライを潤し尽くす！高保湿ヒアルロン酸化粧水特集</h3>
      <p style="color:#0c4a6e;margin-bottom:16px;font-size:0.95rem;">自重の約6,000倍の保水力を誇る多段分子ヒアルロン酸が、暖房直撃で萎縮した角質層深部まで満水充填！肌ラボ極潤プレミアム、トリデン、アクセーヌ、カルテHDなど厳選10選を徹底解説！</p>
      <a href="/winter-hyaluronic-lotion" style="display:inline-block;background:#0284c7;color:#fff;font-weight:700;padding:10px 20px;border-radius:6px;text-decoration:none;">高保湿ヒアルロン酸化粧水ランキング10選を見る →</a>
    </div>
"""
        if "</main>" in html:
            html = html.replace("</main>", banner + "\n  </main>")
            with open("winter-lotion.html", "w", encoding="utf-8") as f:
                f.write(html)
            print("Successfully added banner to winter-lotion.html!")

# C. index.html のグリッド先頭カード確認
with open("index.html", "r", encoding="utf-8") as f:
    idx_html = f.read()

if '<a href="/winter-cica-mask"' not in idx_html:
    brand_new_cards = """      <!-- 高保湿CICAシートマスク -->
      <a href="/winter-cica-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #dcfce7; color: #15803d;">🌿 高純度ツボクサ・寒暖差赤み鎮静 NEW</span>
        <h2 class="hub-card-title">🌿 保湿力の強さで肌乾燥とさようなら！高純度ツボクサエキス・CICAの濃厚鎮静ヴェールと密着シートで真冬の寒暖差赤み・暖房荒れを速攻鎮静する保湿力高めCICAシートマスクランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の寒冷と暖房の激しい寒暖差による赤ら顔・ヒリつき・乾燥ゆらぎ肌を秒速鎮静！VT、メディヒール、アピュー、ドクタージャルト、Anua、ネイチャーリパブリック、クオリティファースト、KISOまで高純度ツボクサエキス配合の神高保湿CICAシートマスクの科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿グルタチオンシートマスク -->
      <a href="/winter-glutathione-mask" class="hub-card">
        <span class="hub-card-tag" style="background: #f3e8ff; color: #7e22ce;">✨ 白玉グルタチオン・寒冷血行不良くすみ晴らし NEW</span>
        <h2 class="hub-card-title">✨ 保湿力の強さで肌乾燥とさようなら！高純度白玉グルタチオンの抗酸化発光力とビタミンC多重浸透膜で真冬の寒冷血行不良くすみを晴らす保湿力高めグルタチオンシートマスクランク10</h2>
        <p class="hub-card-desc">11月・12月の冬の寒冷血行不良によるどんよりくすみ・青白い疲労顔・暖房乾燥小ジワを徹底解決！ナンバーズイン、ルルルン、VT、クオリティファースト、魔女工場、バイオヒールボ、Anuaまで高純度グルタチオン配合の神高保湿シートマスクの科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>

      <!-- 高保湿ヒアルロン酸化粧水 -->
      <a href="/winter-hyaluronic-lotion" class="hub-card">
        <span class="hub-card-tag" style="background: #e0f2fe; color: #0369a1;">💧 多段ヒアルロン酸・深層インナードライ救済 NEW</span>
        <h2 class="hub-card-title">💧 保湿力の強さで肌乾燥とさようなら！多段分子ヒアルロン酸の超濃密保水クッションと浸透ブースト処方で真冬のカサつきインナードライを潤し尽くす保湿力高めヒアルロン酸化粧水ランク10</h2>
        <p class="hub-card-desc">11月・12月の冬乾燥・暖房直撃によるインナードライ・ファンデ粉吹き・カサつきを徹底解決！肌ラボ極潤プレミアム、トリデン、アクセーヌ、ナンバーズイン、カルテHD、オルビス、キュレル、イハダ、ちふれ、KISOまで多段分子ヒアルロン酸配合の神高保湿化粧水の科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。</p>
      </a>\n"""
    idx_html = idx_html.replace('<div class="hub-grid">\n', '<div class="hub-grid">\n' + brand_new_cards)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(idx_html)
    print("Successfully added cards to index.html!")
