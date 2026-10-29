import os
import re

ALL_ARTICLES = [
    {
        "url": "/winter-liquid-foundation",
        "file": "winter-liquid-foundation.html",
        "title": "✨ 保湿力の強さで肌乾燥・粉吹きとさようなら！美容液級のうるおいで一日中ひび割れ・毛穴落ちを防ぐ高保湿リキッドファンデーションランク10",
        "desc": "暖房直撃でも夕方の粉吹き・ひび割れ・毛穴落ちゼロ！資生堂エッセンススキングロウ、コスデコゼンウェアグロウ、ディオール、SUQQUなど美容液ファンデ10選。",
        "footer_name": "リキッドファンデ"
    },
    {
        "url": "/winter-cream-cheek",
        "file": "winter-cream-cheek.html",
        "title": "🌸 保湿力の強さで肌乾燥・寒暖差くすみとさようなら！冬の冷え切った頬にじゅわっと上気ツヤを仕込む高保湿チークランク10",
        "desc": "冬の寒暖差による青白いくすみやパウダーチークの粉浮きを一掃！シャネル、アディクション、コスデコ、ローラメルシエなど高保湿クリーム＆リキッドチーク10選。",
        "footer_name": "高保湿チーク"
    },
    {
        "url": "/winter-cream-eyeshadow",
        "file": "winter-cream-eyeshadow.html",
        "title": "👁️ 保湿力の強さでまぶたの乾燥・二重幅の粉落ちとさようなら！濡れツヤと透明感を一日中キープする高保湿アイシャドウランク10",
        "desc": "冬の乾燥まぶたや二重幅のシワ溜まりを完全解決！コスメデコルテアイグロウジェム、ローラメルシエキャビアスティックなど高保湿クリーム＆リキッドアイシャドウ10選。",
        "footer_name": "アイシャドウ"
    },
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
        "title": "✨ 保湿力の強さで肌乾燥・粉吹きとさようなら！暖房の乾燥に負けないしっとり高保湿フェイスパウダーランク10",
        "desc": "エアコン乾燥で粉吹き・小じわ割れする冬の肌に！コスメデコルテ、エレガンス、NARSなど美容液成分高配合の冬用高保湿パウダー10選。",
        "footer_name": "冬用パウダー"
    },
    {
        "url": "/winter-lip-plumper",
        "file": "winter-lip-plumper.html",
        "title": "💄 保湿力の強さで唇乾燥・縦ジワとさようなら！ぷるんとボリューミーに潤す高保湿リッププランパーランク10",
        "desc": "カサカサ・縦ジワ唇を瞬時にふっくらボリュームアップ！ディオール、クラランス、ヴィセ、ジルスチュアートなど神プランパー10選。",
        "footer_name": "リッププランパー"
    },
    {
        "url": "/winter-hair-mask",
        "file": "winter-hair-mask.html",
        "title": "💆‍♀️ 保湿力の強さで髪乾燥・静電気とさようなら！冬のパサつき・枝毛を芯から集中補修する高保湿ヘアマスク＆ヘアトリートメントランク10",
        "desc": "暖房の乾燥やマフラー摩擦で傷んだハイダメージ毛を集中リペア！フィーノ、資生堂ツバキ、ケラスターゼ、オージュアなど濃厚ヘアマスク10選。",
        "footer_name": "高保湿ヘアマスク"
    },
    {
        "url": "/winter-stick-serum",
        "file": "winter-stick-serum.html",
        "title": "💄 保湿力の強さで肌乾燥とさようなら！メイクの上から直塗り潤いレスキュー高保湿スティック美容液ランク10",
        "desc": "日中の暖房乾燥・目元口元のカサつきを瞬時にリセット！イプサ、KANEBO、ミノンなど携帯必須のスティック美容液10選。",
        "footer_name": "スティック美容液"
    },
    {
        "url": "/winter-scalp-serum",
        "file": "winter-scalp-serum.html",
        "title": "💆 保湿力の強さで頭皮乾燥・フケ・かゆみとさようなら！冬の地肌に潤いをチャージする高保湿スカルプローションランク10",
        "desc": "暖房と乾いた空気で悲鳴をあげる頭皮を集中救済！キュレル、アヴェダ、資生堂など冬の頭皮保湿ローション10選。",
        "footer_name": "スカルプローション"
    },
    {
        "url": "/winter-toneup-base",
        "file": "winter-toneup-base.html",
        "title": "🌸 保湿力の強さで肌乾燥とさようなら！夕方までカサつかず透明感を底上げする高保湿トーンアップ下地ランク10",
        "desc": "冬の乾燥くすみ・血色不良を一掃！ラロッシュポゼ、コスメデコルテ、ポール＆ジョーなど美容液成分高配合の神下地10選。",
        "footer_name": "トーンアップ下地"
    },
    {
        "url": "/winter-sleeping-mask",
        "file": "winter-sleeping-mask.html",
        "title": "🌙 保湿力の強さで肌乾燥とさようなら！寝ている間に集中補修する高保湿スリーピングマスクランク10",
        "desc": "睡眠中の暖房乾燥から肌を守り抜く！ラネージュ、エリクシール、VTなど翌朝ぷるん肌を叶えるナイトパック10選。",
        "footer_name": "スリーピングマスク"
    },
    {
        "url": "/winter-nail-oil",
        "file": "winter-nail-oil.html",
        "title": "💅 保湿力の強さで爪乾燥・二枚爪とさようなら！指先をしっとり保護する高保湿ネイルオイルランク10",
        "desc": "冬のガサガサささくれ・爪割れを撃退！uka、OPI、アンドネイルなど高浸透キューティクルオイル10選。",
        "footer_name": "ネイルオイル"
    },
    {
        "url": "/winter-foot-cream",
        "file": "winter-foot-cream.html",
        "title": "👣 保湿力の強さで足裏ガサガサ・かかとひび割れとさようなら！高保湿フットクリームランク10",
        "desc": "靴下を脱いでもツルツル！ユースキン、ロコベース、ニュートロジーナなど冬のかかと集中保湿クリーム10選。",
        "footer_name": "フットクリーム"
    },
    {
        "url": "/winter-emulsion",
        "file": "winter-emulsion.html",
        "title": "🌸 保湿力の強さで肌乾燥とさようなら！うるおい密封＆柔らかツヤ肌を叶える高保湿乳液ランク10",
        "desc": "化粧水のうるおいを逃さずふっくら閉じ込める！コスメデコルテ、ミノン、雪肌精、乳液先行型など厳選10選。",
        "footer_name": "高保湿乳液"
    },
    {
        "url": "/winter-face-oil",
        "file": "winter-face-oil.html",
        "title": "🌿 保湿力の強さで肌乾燥とさようなら！皮脂枯れ砂漠肌を救済する高保湿美容オイルランク10",
        "desc": "ハーバー高品位スクワラン、メルヴィータアルガンオイル、RMKなど、冬の肌を柔らかく包み込む神フェイスオイル10選。",
        "footer_name": "美容オイル"
    },
    {
        "url": "/winter-repair-balm",
        "file": "winter-repair-balm.html",
        "title": "🛡️ 保湿力の強さで肌乾燥とさようなら！粉吹き・皮剥け・肌荒れを鉄壁ガードする高保湿リペアバームランク10",
        "desc": "イハダ薬用バーム、キュレル、ラロッシュポゼB5など、冬の深刻な乾燥トラブルを即効レスキューするリペアバーム10選。",
        "footer_name": "リペアバーム"
    },
    {
        "url": "/winter-bath-care",
        "file": "winter-bath-care.html",
        "title": "🛁 保湿力の強さで肌乾燥とさようなら！入浴中から全身うるおう高保湿入浴剤ランク10",
        "desc": "冬のお風呂上がりの過乾燥を防ぐ！BARTH、クナイプ、アユーラなど美容液成分高配合の神入浴剤10選。",
        "footer_name": "高保湿入浴剤"
    },
    {
        "url": "/winter-face-wash",
        "file": "winter-face-wash.html",
        "title": "🫧 保湿力の強さで肌乾燥とさようなら！洗い上がりもしっとり続く高保湿洗顔料ランク10",
        "desc": "洗顔後のつっぱり・粉吹きを防ぐ！カネボウコンフォートストレッチィ、オバジ、ファンケルなど冬用洗顔10選。",
        "footer_name": "高保湿洗顔料"
    },
    {
        "url": "/winter-face-mist",
        "file": "winter-face-mist.html",
        "title": "💧 保湿力の強さで肌乾燥とさようなら！日中の暖房砂漠化を防ぐ高保湿ミスト化粧水ランク10",
        "desc": "メイクの上から微細ミストで水分補給！ダルバ、エリクシール、キュレルなど携帯必須の保湿ミスト10選。",
        "footer_name": "ミスト化粧水"
    },
    {
        "url": "/winter-lotion",
        "file": "winter-lotion.html",
        "title": "💧 保湿力の強さで肌乾燥とさようなら！冬の乾燥肌をうるおす高保湿化粧水ランク10",
        "desc": "イプサ、アクセーヌ、オルビスなど、冬の乾いた角質層へぐんぐん浸透する高保湿化粧水10選。",
        "footer_name": "高保湿化粧水"
    },
    {
        "url": "/winter-cleansing",
        "file": "winter-cleansing.html",
        "title": "🍯 洗うほど肌がモチモチ潤う！冬の粉吹き・つっぱりを防ぐ高保湿クレンジング10選",
        "desc": "冬のクレンジングでうるおいを奪わない！シュウウエムラ、DUO、ファンケルなど厳選10選。",
        "footer_name": "高保湿クレンジング"
    },
    {
        "url": "/winter-day-cream",
        "file": "winter-day-cream.html",
        "title": "☀️ 暖房乾燥と冬紫外線をダブル遮断！夕方まで潤いが続く朝用デイクリーム10選",
        "desc": "朝の仕込みで一日中乾燥知らず！カネボウ、エリクシールなど化粧下地にもなるデイクリーム。",
        "footer_name": "朝用デイクリーム"
    },
    {
        "url": "/winter-moisture-cream",
        "file": "winter-moisture-cream.html",
        "title": "🧴 保湿力の強さで肌乾燥とさようなら！保湿力高めフェイスクリームランク10",
        "desc": "11月・12月の厳しい寒さと暖房による肌乾燥を徹底ブロック！キールズ、キュレル、コスメデコルテなど高保湿クリーム10選。",
        "footer_name": "高保湿クリーム"
    },
    {
        "url": "/winter-serum-booster",
        "file": "winter-serum-booster.html",
        "title": "💧 ゴワつく冬の砂漠肌を即ほぐす！浸透力を劇的に高める導入美容液・ブースター10選",
        "desc": "硬くなった冬の角質をほぐし、化粧水の浸透を劇的アップ！コスメデコルテリポソーム、タカミなど。",
        "footer_name": "導入美容液"
    },
    {
        "url": "/winter-face-mask",
        "file": "winter-face-mask.html",
        "title": "💧 水分爆弾で砂漠肌を即リセット！翌朝の化粧ノリが変わる集中高保湿シートマスク10選",
        "desc": "真冬の緊急レスキュー！ルルルンプレシャス、VT、メディヒールなど濃厚美容液パック。",
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
        elif '<section id="internal-links"' in content:
            content = re.sub(r'(<section id="internal-links".*?</section>)', r'\1\n\n    ' + new_related_section, content, flags=re.DOTALL)
        
        # フッターリンクの置換
        if '<div class="footer-links">' in content:
            content = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, content, flags=re.DOTALL)
        elif '<div class="footer-inner">' in content:
            content = re.sub(r'(<footer class="site-footer">\s*<div class="footer-inner">)', r'\1\n    ' + footer_links_html, content, flags=re.DOTALL)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Updated internal links and footer in: {file_path}")

    print("\nAll articles internal links updated successfully!")

if __name__ == "__main__":
    update_links()
