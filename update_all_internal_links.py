import os
import re

ALL_ARTICLES = [
    {
        "url": "/winter-sleeping-mask",
        "file": "winter-sleeping-mask.html",
        "title": "🌙 保湿力の強さで肌乾燥とさようなら！寝ている間に集中密着ケアする高保湿スリーピングマスク＆ナイトパックランク10",
        "desc": "睡眠中の暖房乾燥脱水を完全遮断！ラネージュ、エリクシール、ファミュ、コスメデコルテなど翌朝ぷるんと吸い付く神パック10選。",
        "footer_name": "スリーピングマスク"
    },
    {
        "url": "/winter-nail-oil",
        "file": "winter-nail-oil.html",
        "title": "💅 保湿力の強さで肌乾燥とさようなら！指先のささくれ・パサつきを防ぎ美爪を育てる高保湿ネイルオイルランク10",
        "desc": "爪割れ・二枚爪・痛いささくれを徹底リペア！uka、OPI、ロクシタン、アンドネイル、無印良品などケラチン浸透植物オイル10選。",
        "footer_name": "ネイルオイル"
    },
    {
        "url": "/winter-foot-cream",
        "file": "winter-foot-cream.html",
        "title": "👣 保湿力の強さで肌乾燥とさようなら！頑固なガサガサ・ひび割れをふっくら柔らかくする高保湿かかと＆フットクリームランク10",
        "desc": "タイツの電線やパックリ割れと決別！ニュートロジーナ、ロコベース、ドクターショール、ユースキン、ヒビケアFTなど最強フットケア10選。",
        "footer_name": "かかとフットケア"
    },
    {
        "url": "/winter-emulsion",
        "file": "winter-emulsion.html",
        "title": "🌸 保湿力の強さで肌乾燥とさようなら！うるおい密封と柔らかツヤ肌を叶える高保湿乳液＆エマルジョンランク10",
        "desc": "寒さでゴワつく角層をほぐし水分油分バランスを再構築！コスメデコルテAQ、アルビオン、ミノン、キュレルなど至高の乳液10選。",
        "footer_name": "高保湿乳液"
    },
    {
        "url": "/winter-face-oil",
        "file": "winter-face-oil.html",
        "title": "🌿 保湿力の強さで肌乾燥とさようなら！皮脂枯れ砂漠肌を救う極上高保湿フェイスオイル＆美容オイルランク10",
        "desc": "11月・12月の急落する皮脂膜をたった1滴で代行！ハーバースクワラン、メルヴィータアルガン、RMK、トリロジーなど極上オイル10選。",
        "footer_name": "高保湿フェイスオイル"
    },
    {
        "url": "/winter-repair-balm",
        "file": "winter-repair-balm.html",
        "title": "🛡️ 保湿力の強さで肌乾燥とさようなら！粉吹き・ひび割れ皮剥けを緊急レスキューする高保湿リペアバームランク10",
        "desc": "暖房や木枯らしで粉を吹いた頬・口元を鉄壁シールド！イハダ高精製ワセリン、ラロッシュポゼCICA、カルテHDなど神バーム10選。",
        "footer_name": "高保湿リペアバーム"
    },
    {
        "url": "/winter-bath-care",
        "file": "winter-bath-care.html",
        "title": "🛁 保湿力の強さで肌乾燥とさようなら！温活と全身うるおいバリアを叶える高保湿入浴剤＆バスミルクランク10",
        "desc": "出浴後の粉吹き・乾燥かゆみ・冷え性と完全決別！アユーラ、BARTH、キュレルなど湯上がりもしっとり吸い付く神入浴剤10選。",
        "footer_name": "入浴剤・バスケア"
    },
    {
        "url": "/winter-face-wash",
        "file": "winter-face-wash.html",
        "title": "🫧 保湿力の強さで肌乾燥とさようなら！冬のつっぱり・粉吹きを防ぐうるおい吸着・高保湿洗顔料ランク10",
        "desc": "洗顔直後のパリパリ乾燥・毛穴詰まりに終止符！カネボウ、オバジX炭酸泡、エスト温感ジェルなど洗うだけでうるおう至高の洗顔料10選。",
        "footer_name": "高保湿洗顔料"
    },
    {
        "url": "/winter-face-mist",
        "file": "winter-face-mist.html",
        "title": "💧 保湿力の強さで肌乾燥とさようなら！暖房の砂漠化からメイクを守る高保湿ミスト化粧水＆オイルミストランク10",
        "desc": "オフィスの暖房直風によるファンデ割れ・粉吹きを撃退！エリクシールつや玉ミスト、ダルバ白トリュフ、コスメデコルテなど神ミスト10選。",
        "footer_name": "高保湿ミスト"
    },
    {
        "url": "/winter-lotion",
        "file": "winter-lotion.html",
        "title": "💧 保湿力の強さで肌乾燥とさようなら！冬の乾きを満たす高保湿化粧水＆とろみ浸透ローションランク10",
        "desc": "暖房でカラカラに干からびた角層をごくごく潤す！イプサ、アクセーヌ、エスト、カルテHDなど超微細ナノカプセル配合ローション徹底比較。",
        "footer_name": "高保湿化粧水"
    },
    {
        "url": "/winter-cleansing",
        "file": "winter-cleansing.html",
        "title": "洗うほど肌がモチモチ潤う！冬の粉吹き・つっぱりを防ぐ高保湿クレンジング＆濃密バームランク10",
        "desc": "乾燥悪化の主犯「過剰脱脂」をストップ！DUO、カバーマーク、シュウウエムラ、カネボウなど洗顔後も化粧水いらずの至高クレンジング10選。",
        "footer_name": "クレンジング"
    },
    {
        "url": "/winter-day-cream",
        "file": "winter-day-cream.html",
        "title": "☀️ 暖房乾燥と冬紫外線をダブル遮断！一日中しっとり続く高保湿UV美容液＆朝用デイクリームランク10",
        "desc": "エアコン温風の砂漠化と真皮まで届く冬のUV-A波を完全ブロック！カネボウ クリームインデイ、ランコム、オルビスなど夕方までツヤ肌キープ。",
        "footer_name": "朝用UVクリーム"
    },
    {
        "url": "/winter-serum-booster",
        "file": "winter-serum-booster.html",
        "title": "💧 ゴワつく冬の砂漠肌を即ほぐす！浸透力を底上げする高保湿・導入先行美容液おすすめ10選",
        "desc": "硬くなった冬肌をほぐし、化粧水をグングン引き込む土台美容液。ランコム、コスメデコルテなど。",
        "footer_name": "導入美容液"
    },
    {
        "url": "/winter-face-mask",
        "file": "winter-face-mask.html",
        "title": "💧 水分爆弾で砂漠肌を即リセット！高保湿シートマスク＆夜用パック10選",
        "desc": "暖房乾燥でしぼんだ肌に潤い集中チャージ！トリデン、ルルルン、バイオダンスなど話題の密着パック。",
        "footer_name": "シートマスク"
    },
    {
        "url": "/winter-moisture-cream",
        "file": "winter-moisture-cream.html",
        "title": "🧴 保湿力の強さで肌乾燥とさようなら！高保湿フェイスクリーム＆濃密バーム10選",
        "desc": "暖房下でも粉吹きゼロへ！キールズ、キュレル、コスメデコルテなど水分を閉じ込める最強クリーム。",
        "footer_name": "保湿クリーム"
    },
    {
        "url": "/winter-eye-cream",
        "file": "winter-eye-cream.html",
        "title": "👁️ 暖房直撃の目元・ほうれい線をふっくら密着！高保湿アイクリーム＆薬用リンクルケア10選",
        "desc": "夕方のちりめんジワ・ファンデ割れを撃退！純粋レチノール、ニールワン、リポソーム配合アイケア。",
        "footer_name": "アイクリーム"
    },
    {
        "url": "/winter-base-makeup",
        "file": "winter-base-makeup.html",
        "title": "✨ 夕方まで潤いツヤが続く高保湿ファンデーション＆美容液下地10選",
        "desc": "エアコン直撃でもひび割れない！クレ・ド・ポー ボーテ、SHISEIDOなど生ツヤ肌ベースメイク。",
        "footer_name": "ベースメイク"
    },
    {
        "url": "/winter-lip-care",
        "file": "winter-lip-care.html",
        "title": "🎁 冬のガサガサ皮剥けに終止符！高保湿リップトリートメント＆濃密ティント10選",
        "desc": "皮脂腺のない唇を乾燥冷風から守る！ラネージュスリーピングマスク、ディオールマキシマイザーなど。",
        "footer_name": "リップケア"
    },
    {
        "url": "/winter-body-care",
        "file": "winter-body-care.html",
        "title": "🛁 すねの粉吹き・全身の乾燥かゆみにサヨナラ！高保湿ボディミルク＆濃厚ボディバター10選",
        "desc": "お風呂上がりの全身をうるおいで包み込む！ニュートロジーナ、ニベア、キュレル、サボンなど厳選。",
        "footer_name": "ボディケア"
    },
    {
        "url": "/winter-hair-care",
        "file": "winter-hair-care.html",
        "title": "🌿 冬の静電気・毛先パサつきと完全決別！高保湿ヘアオイル＆濃厚ヘアマスク10選",
        "desc": "マフラー摩擦や暖房で傷んだキューティクルを補修。モロッカンオイル、ケラスターゼ、オルビスなど。",
        "footer_name": "ヘアケア"
    },
    {
        "url": "/winter-hand-care",
        "file": "winter-hand-care.html",
        "title": "🤲 手荒れ・あかぎれ・ささくれ知らずへ！神ハンドクリーム＆ネイルケア10選",
        "desc": "水仕事や冷風で荒れた手先を即効リペア。ベタつかないデスク用から夜の集中補修バームまで。",
        "footer_name": "ハンドケア"
    },
    {
        "url": "/summer-cosme",
        "file": "summer-cosme.html",
        "title": "☀️ 夏の汗・皮脂でも崩れない！最新トレンドコスメ厳選10選",
        "desc": "皮脂崩れ防止下地やウォータープルーフコスメなど夏特有の肌悩みを解決する特集。",
        "footer_name": "夏コスメ"
    }
]

footer_links_html = '<div class="footer-links">\n      <a href="/">トップページ</a>\n' + "\n".join([f'      <a href="{a["url"]}">{a["footer_name"]}</a>' for a in ALL_ARTICLES]) + '\n    </div>'

for target_article in ALL_ARTICLES:
    file_path = target_article["file"]
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 関連記事リスト構築（自分自身を除く）
    related_cards = []
    for a in ALL_ARTICLES:
        if a["file"] == target_article["file"]:
            continue
        related_cards.append(f"""        <a href="{a['url']}" class="related-link-card">
          <div class="related-link-title">{a['title']}</div>
          <div class="related-link-desc">{a['desc']}</div>
        </a>""")

    new_related_section = f"""<section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list">
{chr(10).join(related_cards)}
      </div>
    </section>"""

    # 既存の関連記事セクションの置換
    if '<section id="related"' in content:
        content = re.sub(r'<section id="related".*?</section>', new_related_section, content, flags=re.DOTALL)
    
    # フッターリンクの置換
    if '<div class="footer-links">' in content:
        content = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated internal links and footer in: {file_path}")

print("\nAll articles internal links updated successfully!")
