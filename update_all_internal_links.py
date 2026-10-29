import os
import re

ALL_ARTICLES = [
    {
        "url": "/winter-highlighter",
        "file": "winter-highlighter.html",
        "title": "✨ 保湿力の強さで冬の乾燥くすみ・粉浮きとさようなら！暖房下でも内側から発光する生ツヤを宿す高保湿ハイライトランク10",
        "desc": "暖房の乾燥でパウダーが粉浮き・小じわ崩れする冬の肌に！シャネルのボームエサンシエル、hince、ディオール、クレドポーなど、うるおい生ツヤを宿す高保湿ハイライト厳選10選。",
        "footer_name": "高保湿ハイライト"
    },
    {
        "url": "/winter-hair-oil",
        "file": "winter-hair-oil.html",
        "title": "💆‍♀️ 保湿力の強さで毛先のパサつき・静電気・マフラー摩擦とさようなら！真冬の髪を芯から守り抜く濃厚高保湿ヘアオイルランク10",
        "desc": "冬の北風・暖房・静電気・マフラー摩擦に負けない！モロッカンオイル、ミルボンエルジューダMO、ケラスターゼ、N.ポリッシュオイルなど濃厚高保湿ヘアオイル10選。",
        "footer_name": "高保湿ヘアオイル"
    },
    {
        "url": "/winter-lip-mask",
        "file": "winter-lip-mask.html",
        "title": "💄 保湿力の強さで唇のガサガサ皮剥け・縦ジワとさようなら！寝ている間に濃厚ラップで集中リペアする高保湿リップマスクランク10",
        "desc": "暖房の乾燥でカサカサ・皮剥け・縦ジワが目立つ唇を寝ている間に集中リペア！ラネージュ、キュレル、トリデン、CNP、タカミなど高保湿リップマスク10選。",
        "footer_name": "高保湿リップマスク"
    },
    {
        "url": "/winter-hair-milk",
        "file": "winter-hair-milk.html",
        "title": "💆‍♀️ 保湿力の強さで髪のパサつき・静電気とさようなら！冬の乾燥・マフラー摩擦を芯から防ぐ高保湿ヘアミルク＆アウトバストリートメントランク10",
        "desc": "オイルだけでは届かない毛髪内部へ水分＆CMCを集中補給！オルビス、ミルボンエルジューダ、N.シアミルク、ケラスターゼなど神ヘアミルク10選。",
        "footer_name": "高保湿ヘアミルク"
    },
    {
        "url": "/winter-cushion-foundation",
        "file": "winter-cushion-foundation.html",
        "title": "✨ 保湿力の強さで肌乾燥とさようなら！冬の暖房直撃でも夕方までひび割れない高保湿クッションファンデーション＆美容液ファンデランク10",
        "desc": "暖房の効いた部屋でも夕方まで乾燥割れ・粉吹き知らず！TIRTIRクリスタル、CLIOハイグロウ、ジョンセンムル、YSLなど美容液クッション10選。",
        "footer_name": "クッションファンデ"
    },
    {
        "url": "/winter-body-scrub",
        "file": "winter-body-scrub.html",
        "title": "🛁 保湿力の強さで全身のゴワつき・粉吹きとさようなら！入浴時に潤いオイルを仕込む高保湿ボディスクラブ＆角質ケアランク10",
        "desc": "頑固なひじ・ひざ・かかとの角質をオフし濃厚オイル膜で全身シールド！SABON、ハウスオブローゼ、LUSH、クナイプなど神スクラブ10選。",
        "footer_name": "ボディスクラブ"
    },
    {
        "url": "/winter-hydrating-serum",
        "file": "winter-hydrating-serum.html",
        "title": "💧 保湿力の強さで肌乾燥・砂漠化とさようなら！冬のバリア崩壊を集中救済する高保湿美容液＆高濃度アンプルランク10",
        "desc": "暖房直撃でカラカラの角層を集中救済！コスメデコルテリポソーム、トリデン、キュレル、エトヴォスなどセラミド＆ヒアルロン酸セラム10選。",
        "footer_name": "高保湿美容液"
    },
    {
        "url": "/winter-concealer",
        "file": "winter-concealer.html",
        "title": "👁️ 保湿力の強さで目元・口元の乾燥ひび割れとさようなら！冬の青クマ・くすみを潤いヴェールで消し去る高保湿コンシーラーランク10",
        "desc": "夕方の目元のちりめんジワ・地割れ割れに終止符！ディオールスキン、コスメデコルテ、NARS、アンドビーなど美容液コンシーラー10選。",
        "footer_name": "高保湿コンシーラー"
    },
    {
        "url": "/winter-lip-tint",
        "file": "winter-lip-tint.html",
        "title": "💄 保湿力の強さで唇の乾燥・皮剥け・血色レスとさようなら！真冬のイベントも一日中うるおい発色が続く高保湿リップティント＆美容液ルージュランク10",
        "desc": "皮剥け知らずで一日中落ちない！KATEリップモンスター、ロムアンドメルティングバーム、オペラ、ディオールなど高保湿ルージュ10選。",
        "footer_name": "高保湿リップティント"
    },
    {
        "url": "/winter-powder",
        "file": "winter-powder.html",
        "title": "✨ 保湿力の強さで肌乾燥とさようなら！冬の粉吹き・乾燥小じわを防ぎ一日中うるおいツヤ肌が続く高保湿フェイスパウダーランク10",
        "desc": "暖房直撃でも夕方まで粉吹き・地割れシワ知らず！コスメデコルテ、NARSリフ粉、エクセル、ミラコレなど美容液パウダー10選。",
        "footer_name": "冬用パウダー"
    },
    {
        "url": "/winter-lip-plumper",
        "file": "winter-lip-plumper.html",
        "title": "💄 保湿力の強さで唇乾燥とさようなら！冬のガサガサ・縦ジワ・皮剥けを濃密オイルと温感ボリュームで満たす高保湿リッププランパーランク10",
        "desc": "真冬の過酷な唇トラブルを即効解消！ディオールマキシマイザー、クラランス、ヴィセなど温感刺激＆濃密オイルプランパー10選。",
        "footer_name": "リッププランパー"
    },
    {
        "url": "/winter-hair-mask",
        "file": "winter-hair-mask.html",
        "title": "💆‍♀️ 保湿力の強さで髪の乾燥・静電気とさようなら！真冬の毛先パサつき・広がりを芯から集中補修する濃密高保湿ヘアマスクランク10",
        "desc": "マフラー摩擦や暖房の静電気・毛先パサつきを芯からリペア！フィーノ、オージュア、ケラスターゼ、TSUBAKIなどサロン級マスク10選。",
        "footer_name": "高保湿ヘアマスク"
    },
    {
        "url": "/winter-stick-serum",
        "file": "winter-stick-serum.html",
        "title": "💄 保湿力の強さで肌乾燥とさようなら！日中いつでもメイクの上から乾燥小じわ・粉吹きをレスキューする高保湿スティック美容液ランク10",
        "desc": "オフィス暖房のファンデ割れ・ちりめんジワをひと塗りで解決！イプサ、KAHI、ダルバ、アスタリフトなど高保湿バームスティック10選。",
        "footer_name": "スティック美容液"
    },
    {
        "url": "/winter-scalp-serum",
        "file": "winter-scalp-serum.html",
        "title": "💆 保湿力の強さで頭皮乾燥とさようなら！冬のフケ・かゆみ・つっぱりを防ぎうるおい頭皮を育てる高保湿スカルプローションランク10",
        "desc": "冬のパラパラ乾性フケ・強い地肌かゆみに終止符！キュレル、ミルボン、ヴェレダ、無印良品など頭皮のセラミド保水ローション10選。",
        "footer_name": "スカルプローション"
    },
    {
        "url": "/winter-toneup-base",
        "file": "winter-toneup-base.html",
        "title": "🌸 保湿力の強さで肌乾燥とさようなら！冬の血色レス・乾燥くすみを払拭し夕方まで透き通る高保湿コントロールカラー＆トーンアップ下地ランク10",
        "desc": "寒さによる青白さ・黄ぐすみ・ファンデの粉浮きを一掃！ポール＆ジョー、コスメデコルテ、ジルスチュアートなど美容液トーンアップ下地10選。",
        "footer_name": "トーンアップ下地"
    },
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
        "title": "👣 保湿力の強さで肌乾燥とさようなら！頑固なガサガサ・ひび割れかかとをつるんとなめらかに再生する高保湿フットクリームランク10",
        "desc": "タイツに引っかかる粉吹きかかとを救済！尿素高配合、ワセリン、シアバターなど角質柔軟フットバーム10選。",
        "footer_name": "フットクリーム"
    },
    {
        "url": "/winter-emulsion",
        "file": "winter-emulsion.html",
        "title": "💧 保湿力の強さで肌乾燥とさようなら！化粧水を閉じ込めふっくら柔肌へ導く高保湿乳液ランク10",
        "desc": "乳液先行型からセラミド高配合まで！コスメデコルテ、アルビオン、ミノノン、イプサなど冬のうるおい乳液10選。",
        "footer_name": "高保湿乳液"
    },
    {
        "url": "/winter-face-oil",
        "file": "winter-face-oil.html",
        "title": "✨ 保湿力の強さで肌乾燥とさようなら！真冬のゴワつきをほぐしツヤ肌へ導く高保湿美容オイルランク10",
        "desc": "アルガン、ホホバ、スクワラン！ハーバー、メルヴィータ、キールズなどブースター＆保護フェイスオイル10選。",
        "footer_name": "美容オイル"
    },
    {
        "url": "/winter-repair-balm",
        "file": "winter-repair-balm.html",
        "title": "🛡️ 保湿力の強さで肌乾燥とさようなら！粉吹き・皮剥け・肌荒れを濃密密封する高保湿リペアバームランク10",
        "desc": "暖房の過酷な乾燥から肌を守るシールド！イハダ、シカバーム、カルテHD、アベンヌなどレスキューバーム10選。",
        "footer_name": "リペアバーム"
    },
    {
        "url": "/winter-bath-care",
        "file": "winter-bath-care.html",
        "title": "🛁 お風呂上がりの全身乾燥を防ぐ！極上のうるおいを仕込む高保湿入浴剤＆バスミルク10選",
        "desc": "入浴中の水分蒸散をブロック。BARTH、アユーラ、キュレル、クナイプなど極上バスコスメ厳選。",
        "footer_name": "高保湿入浴剤"
    },
    {
        "url": "/winter-face-wash",
        "file": "winter-face-wash.html",
        "title": "🧴 洗い上がりのつっぱり感ゼロ！冬の朝も夜も潤いを守る高保湿洗顔料＆泡洗顔10選",
        "desc": "冬の朝の皮脂膜を守るマイルド洗顔。カネボウ、オルビス、カウブランド、Obagiなど高保湿洗顔料厳選。",
        "footer_name": "高保湿洗顔料"
    },
    {
        "url": "/winter-face-mist",
        "file": "winter-face-mist.html",
        "title": "💦 日中のオフィス暖房・メイクの上から瞬間水分チャージ！携帯必須の高保湿ミスト化粧水10選",
        "desc": "午後3時のパリパリ乾燥肌をレスキュー。コスメデコルテ、キュレル、ダルバ、エリクシールなどオイルインミスト厳選。",
        "footer_name": "ミスト化粧水"
    },
    {
        "url": "/winter-lotion",
        "file": "winter-lotion.html",
        "title": "💧 冬の乾いた角層をごくごく潤す！とろみ・浸透力に優れた高保湿化粧水10選",
        "desc": "乾燥でゴワつく真冬の肌を柔軟にほぐす。IPSA、アクセーヌ、オルビス、POLAなど殿堂入り化粧水厳選。",
        "footer_name": "高保湿化粧水"
    },
    {
        "url": "/winter-cleansing",
        "file": "winter-cleansing.html",
        "title": "🧖‍♀️ メイクは落として潤いは残す！冬のつっぱりを防ぐ高保湿クレンジング10選",
        "desc": "美容液成分90%超やとろけるバーム。ファンケル、DUO、カバーマーク、シュウウエムラなど高保湿クレンジング厳選。",
        "footer_name": "高保湿クレンジング"
    },
    {
        "url": "/winter-day-cream",
        "file": "winter-day-cream.html",
        "title": "☀️ 朝の仕込みで一日中うるおいキープ！メイク前の高保湿デイクリーム＆朝用UV乳液10選",
        "desc": "化粧下地効果も兼ね備えた朝用クリーム。カネボウ、エリクシール、アンブリオリスなどファンデが綺麗に密着する名品。",
        "footer_name": "朝用デイクリーム"
    },
    {
        "url": "/winter-moisture-cream",
        "file": "winter-moisture-cream.html",
        "title": "❄️ 冬の超乾燥肌を救う！濃厚高保湿フェイスクリームおすすめ10選",
        "desc": "暖房の効いた室内でも朝までしっとり。キールズ、キュレル、コスメデコルテなど冬の厳選フェイスクリーム。",
        "footer_name": "高保湿クリーム"
    },
    {
        "url": "/winter-serum-booster",
        "file": "winter-serum-booster.html",
        "title": "✨ 冬のゴワつき肌をほぐす！高保湿ブースター＆導入美容液10選",
        "desc": "化粧水の浸透を劇的に高める導入美容液。コスメデコルテリポソーム、ランコムジェニフィックなど厳選。",
        "footer_name": "導入美容液"
    },
    {
        "url": "/winter-face-mask",
        "file": "winter-face-mask.html",
        "title": "🧖‍♀️ 週末の集中保湿！乾燥・くすみを一瞬でリセットする高密着シートマスク10選",
        "desc": "乾ききった角層に美容液を集中補給。ルルルンプレシャス、メディヒール、VTシカなど冬の救済マスク。",
        "footer_name": "シートマスク"
    },
    {
        "url": "/winter-eye-cream",
        "file": "winter-eye-cream.html",
        "title": "👁️ 冬の乾燥小じわ・クマを徹底ケア！高保湿アイクリーム10選",
        "desc": "皮膚の薄い目元を乾燥から守る。エリクシールリンクルクリーム、ポーラB.Aなど話題のアイケア。",
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

def update_links():
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
        elif '<div class="footer-nav">' in content:
            content = re.sub(r'<div class="footer-nav">.*?</div>', footer_links_html, content, flags=re.DOTALL)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Updated internal links and footer in: {file_path}")

    print("\nAll articles internal links updated successfully!")

if __name__ == "__main__":
    update_links()
