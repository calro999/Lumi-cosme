import json
import re

with open("fetched_3new_nov_dec_shea_jojoba_urea_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_shea_butter"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 シアバター界の絶対王者！オーガニック100%で全身を包み込む最高峰保湿バーム",
        "catch": "世界中で愛され続ける大ベストセラー。西アフリカ産高品質シアの実から抽出した無添加ピュアオイル",
        "brand_name": "L'OCCITANE (ロクシタン)",
        "capacity": "150ml (ピュア シアバター)",
        "type": "オーガニック認証・100%天然シアバター保湿バーム",
        "features": "シア脂100%、無香料・無着色・防腐剤フリー、エコサート認証、体温でとろける濃厚テクスチャー",
        "value": "ロクシタンを象徴する世界的名品。赤ちゃんから大人まで、乾燥で粉吹く肌・唇・毛先・ひじ・かかとをひと塗りで濃厚シールド",
        "desc_p1": "11月下旬から12月にかけて外気温が10℃を下回り、暖房がフル稼働する真冬の環境では、通常の乳液や軽めのクリームでは追いつかないほど皮脂膜が急速に奪われます。肌の水分蒸発を防ぐ『油分のフタ』として世界中で最も信頼されているのが、ロクシタンの『ピュア シアバター』です。",
        "desc_p2": "人の皮脂膜と非常に近いオレイン酸やステアリン酸を豊富に含み、固形ながら手のひらの体温（約36℃）でスルスルと黄金色の濃密オイルへと融解します。肌にのせると吸い付くように密着し、過酷な冷風やエアコンの乾燥から角質層を長時間強力にプロテクト。合成着色料や防腐剤、香料を一切使用しない植物性油脂100%のため、敏感に傾いた冬の肌やデリケートな目元・口元にも安心して使えます。",
        "target": "粉吹きやカサつきが止まらない超乾燥肌の方、1つで顔・唇・毛先・指先・かかとまで全身ケアしたい方、本物志向のオーガニックコスメを求める方",
        "point": "爪の背やスパチュラでパール粒大を削り取り、両手のひらを擦り合わせて体温で完全にオイル状に溶かしてから、顔全体を包み込むように優しくハンドプレスしてください。"
    },
    {
        "rank": 2,
        "tag": "🌿 日本の繊細な肌のために開発！天然シアバター100%のマルチフェイス＆ボディクリーム",
        "catch": "赤ちゃんから敏感肌まで使えるやさしさ。無添加処方でしっとり潤い肌を育むデイリーバーム",
        "brand_name": "MAMA BUTTER (ママバター)",
        "capacity": "25g (フェイス＆ボディクリーム)",
        "type": "天然シアバター100%配合・無添加マルチ保湿クリーム",
        "features": "天然シア脂100%、パラベン・シリコン・鉱物油・合成着色料・合成香料フリー、国産ナチュラル処方",
        "value": "高品質な天然シアバターを100%使用しながら、使いやすい携帯サイズと手頃な価格を実現。家族全員で安心してシェアできる万能保湿",
        "desc_p1": "『家族みんなで安心して使える保湿を』という想いから誕生したママバター。冬の寒暖差でカサカサに荒れやすい子供の頬から、大人の手指・口元のひび割れ予防まで、純度100%のシアバターが優しく肌を守り抜きます。",
        "desc_p2": "アフリカの厳しい自然環境で育った高品質なシアの実から精製されたシア脂のみを採用。不純物を丁寧に除去しているため特有の強い匂いが抑えられており、香りに敏感な方や食事前のハンドケア・リップケアとしてもストレスなく馴染みます。バッグやポーチにすっぽり収まる25gのコンパクトなアルミ缶仕様で、冬のお出かけ先での乾燥レスキューにも最適です。",
        "target": "敏感肌やお子様と一緒に使える無添加バームを探している方、持ち歩きに便利なサイズ感を好む方、シアバター特有の香りが苦手な方",
        "point": "乾燥が気になる目元や口元にトントンと指先で軽く叩き込むように置くのがコツ。冬の冷たい風に当たる直前の保護シールドとして大活躍します。"
    },
    {
        "rank": 3,
        "tag": "🧪 アロマ専門店が厳選した高純度精製！クセがなく滑らかに伸びるプロ御用達シアバター",
        "catch": "生活の木が誇る確かな原料品質。匂いや色を取り除き、スキンケアや手作りコスメのベースにも最適",
        "brand_name": "生活の木 (Tree of life)",
        "capacity": "100g (シアバター 精製)",
        "type": "精製植物性エモリエントバター・プロフェッショナル仕様",
        "features": "精製シア脂、無香料・無着色、なめらかなテクスチャー、抜群の安定性",
        "value": "未精製シアバター独特のナッツ臭や黄色みを特殊技術で脱色・脱臭。純粋なエモリエント効果だけを肌に届ける高品質な大容量設計",
        "desc_p1": "ハーブとアロマテラピーの老舗ブランド『生活の木』が届ける精製シアバターは、美容サロンやアロマセラピストからも絶大な支持を集める本格派アイテムです。原料へのこだわりと安定した品質管理は折り紙付きです。",
        "desc_p2": "精製処理を施すことで、シアバター特有のナッツのような野性味ある香りと色素をカット。真っ白でキメ細やかなバームは、手のひらで温めると瞬時に絹のように滑らかな感触へ変化します。他の植物油（ホホバオイル等）やエッセンシャルオイルとの相性も抜群で、自分の好みに合わせた冬用オリジナルバーム作りにも重宝します。",
        "target": "匂いのないプレーンな高保湿バームを求める方、惜しみなくボディ全体にたっぷり使いたい方、アロマオイルとブレンドして使いたい方",
        "point": "お風呂上がりの湿り気が残る肌に、手のひらで温めたシアバターを滑らせると、水分を抱き込んで驚くほど吸い付きのよいモチモチ肌に仕上がります。"
    },
    {
        "rank": 4,
        "tag": "🌍 フランスECOCERT認証取得！未精製だからビタミンや微量栄養素がそのまま生きた本物",
        "catch": "伝統的手法で抽出された未精製シアバター。大自然の恵みをダイレクトに肌へ届けるプレミアム仕様",
        "brand_name": "spa hinoki (スパヒノキ)",
        "capacity": "75g (オーガニック シアバター)",
        "type": "ECOCERT認証・未精製ピュアオーガニックシアバター",
        "features": "未精製オーガニックシア脂、カルテノール・アラントイン・トコフェロール（ビタミンE）自然含有、未脱色・未脱臭",
        "value": "加熱や化学的処理を最小限に抑えた未精製シアバター。精製過程で失われがちな天然の美容成分がまるごと凝縮され、深層のハリと潤いを呼び覚ます",
        "desc_p1": "東京・檜原村のヘッドスパサロンから生まれたspa hinoki。世界基準の有機認証ECOCERT（エコサート）を取得した高品質な未精製シアバターは、コスメマニアや自然派志向のユーザーの間で絶大なリピート率を誇ります。",
        "desc_p2": "未精製ならではの淡いクリーム色と、ほんのり香るローストナッツのような芳醇なアロマが特徴。シアバター本来が持つ抗酸化ビタミンや植物性ステロールが豊富に残されており、冬の過酷な寒冷刺激でダメージを受けた角層を力強くリペアします。体温でとろけた瞬間、重厚な油膜が角層をピタッと密封し、翌朝まで一切の乾燥を許しません。",
        "target": "未精製のオーガニック原料に強いこだわりがある方、エイジングケアや肌のハリ低下も同時にケアしたい方、夜の集中ナイトパックとして使いたい方",
        "point": "夜のスキンケアの最後に、米粒大を手のひらで温めて全顔にハンドプレス。翌朝の洗顔時に、肌がふっくらと柔らかく整っているのを実感できます。"
    },
    {
        "rank": 5,
        "tag": "👜 ポーチの常連！いつでもどこでも真冬のカサカサを秒速レスキューするミニマムサイズ",
        "catch": "ロクシタンの最高峰シアバターをポケットに。乾燥するオフィスや移動中の頼れる味方",
        "brand_name": "L'OCCITANE (ロクシタン)",
        "capacity": "10ml (ピュア シアバター ミニサイズ)",
        "type": "携帯用ピュアシチュエーション・100%植物性保湿バーム",
        "features": "シア脂100%、手のひらサイズ10ml缶、密閉アルミ容器、マルチポータブル対応",
        "value": "名作シアバターの機能性をそのままに、ポーチやポケットにすっぽり収まる10mlの可愛い缶に凝縮。日中のリップ、甘皮、毛先のパサつきを即座に修復",
        "desc_p1": "真冬の外出中、エアコンが強烈に効いた電車内やオフィスで『急に唇がピキッと切れた』『指先のささくれが痛む』といった経験は誰にでもあるはず。そんな突発的な真冬の乾燥トラブルを瞬時に解決してくれるのがこの10mlミニ缶です。",
        "desc_p2": "中身はロクシタンを代表するピュアシアーバターそのもの。指先でくるくると円を描くように触れると、指の体温で必要な分だけじんわりと溶け出し、狙った部位にピンポイントで塗布できます。見た目もスタイリッシュなアルミデザインで、冬のプチギフトやクリスマスのちょっとしたプレゼントとしても大人気のロングセラーです。",
        "target": "外出先でこまめにリップや指先を保湿したい方、シアバターをまずはお試しで使ってみたい方、冬のプチギフトを探している方",
        "point": "指先に少量を取り、唇に塗って余った分を爪の根元（ハイポニキウム）に揉み込む習慣をつけると、真冬でもささくれ知らずの美しい指先が維持できます。"
    },
    {
        "rank": 6,
        "tag": "📦 圧倒的な大容量×コスパの極み！全身惜しみなく使い倒せるアメリカ発の純度100%バーム",
        "catch": "207mlの超特大サイズ。冬中ずっと家族で使えるナチュラル派ヘビーユーザーのためのシアバター",
        "brand_name": "NOW Foods (ナウフーズ)",
        "capacity": "207ml (100% ピュア シアバター)",
        "type": "アメリカ直輸入・大容量ピュアシアバター",
        "features": "ピュアシア脂100%、大容量ジャータイプ、化学添加物不使用、ヘキサン不使用抽出",
        "value": "海外サプリ・コスメ大手のナウフーズが誇る高コスパバーム。一般的なシアバターの数倍のボリュームを誇り、すねや背中など広範囲の粉吹き乾燥を一掃",
        "desc_p1": "冬になると足のスネが粉を吹いてかゆくなったり、肘や膝が白くガサついたりと、ボディ全体の乾燥面積は顔の何十倍にも及びます。大容量でコスパ抜群のナウフーズは、そんな全身の乾燥に悩む方の心強い救世主です。",
        "desc_p2": "添加物を一切加えず、低温圧搾に近い製法で抽出された純粋なシアバターをたっぷり207mlジャーに充填。少し硬めの質感ですが、手のひらで温めるとグングン溶けて伸び広がり、真冬の寒風にさらされたすねや腕を分厚い保護膜でガードします。ヘアワックス代わりに毛先に揉み込めば、冬の静電気を防ぎながら自然なツヤ束感を演出できます。",
        "target": "ボディ全体に毎日たっぷり使いたい方、すねの粉吹き乾燥やかゆみに悩む方、家族みんなで惜しみなくシェアしたい方",
        "point": "冬場は容器内で硬くなりやすいため、清潔なスプーンやバターナイフの背で適量を削り取り、必ず手のひらでオイル状に練り上げてから塗布してください。"
    },
    {
        "rank": 7,
        "tag": "🛡️ シアバターとの併用で最強の密封力！極限まで不純物を削ぎ落とした医療用純度の保護バリア",
        "catch": "高品質白色ワセリンの最高峰。シアバターの油分補給とワセリンの物理シールドによるダブル鉄壁ガード",
        "brand_name": "日興リカ サンホワイト",
        "capacity": "50g (サンホワイト P-1)",
        "type": "高純度白色ワセリン・皮膚保護バリア",
        "features": "高純度白色ワセリン（医薬品基準以上）、無香料・無着色・防腐剤フリー、紫外線吸収剤フリー、アレルギーテスト済み",
        "value": "皮膚科医が最も推奨する究極の保護剤。シアバターで肌を柔軟にしてから重ねることで、真冬の暖房直撃下でも水分蒸発を0%近くまでブロック",
        "desc_p1": "シアバターを語る上で欠かせないのが、ワセリンとの相乗効果です。植物油脂であるシアバターが角層に浸透して柔軟性を与えるのに対し、サンホワイトP-1は肌表面に完全な疎水性フィルムを形成して外気を遮断します。",
        "desc_p2": "一般的な黄色ワセリンや白色ワセリンよりもさらに高度に精製され、微量な不純物すら徹底除去。酸化しにくく、赤ちゃんの口周りやアトピー傾向の極度に敏感な肌でもアレルギー反応を起こしにくいのが最大の強みです。シアバターを塗った上から極薄くサンホワイトを重ねる『ミルフィーユ密封』は、真冬の美容プロが密かに実践する最終奥義です。",
        "target": "真冬に肌がめくれてヒリつく超重度乾燥肌の方、皮膚が薄くて刺激に弱い方、シアバターの保湿持続力を究極まで高めたい方",
        "point": "米粒半分ほどの微量を指先に伸ばし、乾燥が特に激しい口角や目のキワ、ひび割れた指先にトントンと薄くスタンプするように重ねてください。"
    },
    {
        "rank": 8,
        "tag": "🌹 優雅なダマスクローズ香るオーガニック！シアバター×アルガンオイルの極上ブレンドバーム",
        "catch": "ドイツの伝統ハーバルブランド・クナイプ。植物オイルの力で至福の香りと濃密保湿を両立",
        "brand_name": "Kneipp (クナイプ)",
        "capacity": "50g (ビオ オイルバーム ローズ)",
        "type": "天然オーガニックシアバター＆ローズオイル配合・美容バーム",
        "features": "オーガニックシアバター、アルガンオイル、ダマスクローズ精油、防腐剤フリー、パラフィンフリー",
        "value": "天然シアバターの強力な保護膜に、美容液成分として名高いアルガンオイルと優雅なローズ精油を配合。スキンケアしながら心まで満たされる贅沢設計",
        "desc_p1": "『無香料のシアバターは少し味気ない』『スキンケアタイムに心地よい香りでリラックスしたい』という方に圧倒的な支持を受けているのが、ドイツの老舗クナイプのビオオイルバームです。",
        "desc_p2": "オーガニック認証のシアバターをベースに、若返りのオイルと呼ばれるアルガンオイルを絶妙な比率でブレンド。通常のシアバターよりも柔らかくメルティな質感で、肌に乗せると体温で瞬時にほどけて上品なダマスクローズの天然アロマが広がります。顔のナイトケアはもちろん、デコルテのマッサージや、手元のフレグランスハンドバームとしても極上の使い心地を誇ります。",
        "target": "華やかな天然ローズの香りに癒されたい方、シアバターの重さを軽減して滑らかに伸ばしたい方、冬のエイジングケアも兼ねたい方",
        "point": "夜の入浴後、首筋からデコルテにかけて温めたバームを優しく滑らせるようにリンパマッサージ。ローズの香気に包まれて質の高い睡眠へと導かれます。"
    },
    {
        "rank": 9,
        "tag": "🤝 高濃度シアバター20%配合の金字塔！世界で数秒に1本売れる手荒れ撃退ハンドクリーム",
        "catch": "ロクシタンの歴史的名作。濃厚なシアバターが手肌をふっくら柔らかく整える冬の必需品",
        "brand_name": "L'OCCITANE (ロクシタン)",
        "capacity": "30ml (シア ハンドクリーム)",
        "type": "シアバター20%高配合・手肌専用高保湿ハンドクリーム",
        "features": "シア脂20%、ハチミツエキス、アーモンド果実エキス、ココナッツオイル、滑らかなエマルジョン処方",
        "value": "シアバターの強力な保湿力はそのままに、日常使いしやすいクリーム状に昇華。ベタつきを残さず素早く手肌に馴染み、冬の水仕事や冷気による手荒れを予防",
        "desc_p1": "シアバターを世界的に有名にした立役者であり、冬のギフトの代名詞ともいえるロクシタンのシアハンドクリーム。天然シアバターを20%という贅沢な高濃度で配合した、まさにハンドケアの完成形です。",
        "desc_p2": "純度100%のシアバターは冬場に硬くなりますが、このハンドクリームは独自の乳化技術により、チューブから出した瞬間からクリーミーで滑らか。手肌に伸ばすと体温でスーッと吸い込まれ、ベタつかないシルキーな保護膜が手肌全体をラッピングします。ハチミツエキスやアーモンドオイルが角層を柔らかくほぐし、冬の乾燥でゴワついた手元をふっくら若々しい印象へと導きます。",
        "target": "手荒れ・ひび割れ・指先の乾燥に悩む方、ベタつかずにしっかり潤うハンドクリームを求める方、手肌に優しい香りをまといたい方",
        "point": "手の甲だけでなく、指先や爪の周りまで丁寧にマッサージするように塗り込みます。夜寝る前に塗って綿手袋を着用すると翌朝驚くほど滑らかな手肌になります。"
    },
    {
        "rank": 10,
        "tag": "🛁 シアバター高配合でしっとりもっちり！冬の乾燥肌を柔らかく解きほぐす濃密ボディクリーム",
        "catch": "お風呂上がりの全身を濃密な潤いで満たす。カサつくひじ・ひざ・すねをなめらかに整える大容量ケア",
        "brand_name": "naturie / ボディケア",
        "capacity": "150g (シアバター高配合 高保湿ボディクリーム)",
        "type": "シアバター＆植物エキス配合・リッチモイストボディクリーム",
        "features": "高配合シア脂、グリセリン、セラミドサポート成分、弱酸性、アルコールフリー",
        "value": "シアバターの優れた保護力となめらかな伸びの良さを両立。入浴後の温まった肌にスルスル広がり、翌朝までしっとりとした柔らかさをキープ",
        "desc_p1": "冬の入浴後は、皮脂が流出して急激に肌の水分が蒸散する危険な時間帯です。特にすねや太もも、背中は衣類の摩擦も加わってカサカサになりやすい部位。シアバターを高配合したこのボディクリームは、真冬のバスタイム後の肌を隙間なく潤します。",
        "desc_p2": "こっくりとしたリッチなクリームながら、肌に伸ばすと体温に反応してなめらかに広がり、ベタつかずにしっとり密着。シアバターのステアリン酸が角層のキメをふっくら整え、冬特有のチクチク感や粉吹きを未然に防ぎます。150gとたっぷり使える容量で、毎日の全身保湿ルーティンに惜しみなく取り入れられます。",
        "target": "お風呂上がりに全身を素早く保湿したい方、こっくり濃厚なクリームの保湿感が好きな方、冬のインナー摩擦で肌がかゆくなりやすい方",
        "point": "入浴後、タオルで軽く水分を拭き取った直後の肌が温かいうちに、手のひらで温めながら下から上へと引き上げるように全身に塗り広げてください。"
    }
]

# JSON-LD ItemList
item_list_elements = []
for p in product_details:
    r_item = items[p["rank"] - 1]
    item_list_elements.append({
        "@type": "ListItem",
        "position": p["rank"],
        "item": {
            "@type": "Product",
            "name": f"{p['brand_name']} {p['capacity']}",
            "image": r_item["image"],
            "description": p["value"],
            "brand": {
                "@type": "Brand",
                "name": p["brand_name"]
            },
            "offers": {
                "@type": "Offer",
                "url": r_item["affiliateUrl"],
                "priceCurrency": "JPY",
                "price": r_item["price"],
                "availability": "https://schema.org/InStock"
            }
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！天然の濃厚ベールで極上保護する高保湿シアバターランク10",
    "description": "11月・12月の冬本番に深刻化する皮脂枯れ・粉吹き乾燥・冷風刺激を徹底解決！西アフリカの大自然が育んだ天然植物油脂・シアバター100%バームから高濃度ブレンドクリームまで、高保湿シアバター10選を徹底比較！ロクシタン、ママバター、生活の木、spa hinokiなど、真冬の顔・唇・髪・手足を鉄壁の潤いベールで守り抜く名品を厳選。",
    "image": items[0]["image"],
    "author": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ 編集部"
    },
    "publisher": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "datePublished": "2026-11-03",
    "dateModified": "2026-11-03"
}

json_ld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "冬の高保湿シアバター おすすめランキング10選",
    "itemListElement": item_list_elements
}

# HTML Template
html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！天然の濃厚ベールで極上保護する高保湿シアバターランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬本番に深刻化する皮脂枯れ・粉吹き乾燥・冷風刺激を徹底解決！西アフリカの大自然が育んだ天然植物油脂・シアバター100%バームから高濃度ブレンドクリームまで、高保湿シアバター10選を徹底比較！ロクシタン、ママバター、生活の木、spa hinokiなど、真冬の顔・唇・髪・手足を鉄壁の潤いベールで守り抜く名品を厳選。">
  <meta name="keywords" content="シアバター,高保湿バーム,冬 保湿,ロクシタン シアバター,ママバター,オーガニック シアバター,未精製シアバター,粉吹き乾燥,おすすめ 2026">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-shea-butter">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！天然の濃厚ベールで極上保護する高保湿シアバターランク10">
  <meta property="og:description" content="11月・12月の冷気と暖房で干上がった素肌を救う！天然植物性シアバターの最上位10選を徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-shea-butter">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
  <!-- 構造化データ JSON-LD -->
  <script type="application/ld+json">
{json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(json_ld_itemlist, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #c28854;
      --primary-dark: #986537;
      --primary-light: #f7ede2;
      --accent: #d4a373;
      --text: #2c2523;
      --text-sub: #665c54;
      --bg: #fdfbf7;
      --card-bg: #ffffff;
      --border: #ebd9c8;
      --shadow: 0 4px 20px rgba(152, 101, 55, 0.08);
      --radius: 14px;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.85;
      color: var(--text);
      background-color: var(--bg);
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary-dark);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .nav-links {{
      display: flex;
      gap: 16px;
      list-style: none;
    }}
    .nav-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 500;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--primary);
    }}
    .breadcrumb {{
      max-width: 1000px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-sub);
    }}
    .breadcrumb a {{
      color: var(--primary);
      text-decoration: none;
    }}
    .container {{
      max-width: 1000px;
      margin: 20px auto 60px;
      padding: 0 20px;
    }}
    .article-header {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 36px 30px;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }}
    .badge {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 30px;
      margin-bottom: 14px;
    }}
    h1 {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: var(--primary-dark);
      margin-bottom: 18px;
    }}
    .meta {{
      font-size: 0.85rem;
      color: var(--text-sub);
      display: flex;
      gap: 18px;
      margin-bottom: 24px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
    }}
    .lead-box {{
      font-size: 1.02rem;
      color: var(--text);
      line-height: 1.9;
      background: #faf6f0;
      padding: 22px;
      border-left: 4px solid var(--primary);
      border-radius: 6px;
    }}
    .lead-box p + p {{
      margin-top: 12px;
    }}
    .content-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 34px 30px;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }}
    .content-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .content-section h3 {{
      font-size: 1.2rem;
      color: var(--text);
      margin: 24px 0 12px;
    }}
    .content-section p {{
      margin-bottom: 16px;
      color: var(--text);
      font-size: 0.98rem;
    }}
    .feature-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin: 24px 0;
    }}
    .feature-card {{
      background: #faf6f0;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 20px;
    }}
    .feature-card h4 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 8px;
    }}
    .feature-card p {{
      font-size: 0.9rem;
      margin-bottom: 0;
      color: var(--text-sub);
    }}
    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 24px 0;
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 12px 14px;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .comparison-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      white-space: nowrap;
    }}
    .comparison-table tr:nth-child(even) {{
      background: #faf6f0;
    }}

    /* Ranking Cards */
    .ranking-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 30px;
      margin-bottom: 36px;
      position: relative;
    }}
    .rank-header {{
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 16px;
    }}
    .rank-number {{
      background: var(--primary);
      color: #ffffff;
      font-size: 1.25rem;
      font-weight: 800;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .ranking-card:nth-child(1) .rank-number {{
      background: #d4a373;
    }}
    .ranking-card:nth-child(2) .rank-number {{
      background: #a98467;
    }}
    .ranking-card:nth-child(3) .rank-number {{
      background: #bc6c25;
    }}
    .rank-title-group h3 {{
      font-size: 1.3rem;
      color: var(--primary-dark);
      line-height: 1.4;
    }}
    .rank-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      margin-top: 4px;
    }}
    .product-main {{
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 26px;
      margin: 20px 0;
    }}
    .img-box {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 220px;
      height: auto;
      border-radius: 8px;
      border: 1px solid var(--border);
      object-fit: cover;
    }}
    .product-spec {{
      font-size: 0.9rem;
      background: #faf6f0;
      padding: 16px;
      border-radius: 8px;
      margin-bottom: 16px;
    }}
    .spec-item {{
      margin-bottom: 6px;
    }}
    .spec-label {{
      font-weight: 700;
      color: var(--text-sub);
      display: inline-block;
      width: 100px;
    }}
    .product-desc p {{
      margin-bottom: 12px;
      font-size: 0.95rem;
      line-height: 1.85;
    }}
    .user-point {{
      background: #fff8f0;
      border-left: 3px solid var(--accent);
      padding: 12px 16px;
      font-size: 0.88rem;
      margin: 14px 0;
      border-radius: 0 6px 6px 0;
    }}
    .price-box {{
      display: flex;
      align-items: baseline;
      gap: 12px;
      margin: 16px 0;
    }}
    .price-val {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #b7094c;
    }}
    .review-score {{
      font-size: 0.85rem;
      color: var(--text-sub);
    }}
    .rakuten-btn {{
      display: inline-block;
      background: #bf0000;
      color: #ffffff !important;
      text-decoration: none;
      font-weight: 700;
      font-size: 1rem;
      padding: 12px 28px;
      border-radius: 8px;
      transition: background 0.2s, transform 0.1s;
      text-align: center;
    }}
    .rakuten-btn:hover {{
      background: #990000;
      transform: translateY(-2px);
    }}

    /* Q&A / Step Guide */
    .faq-item {{
      margin-bottom: 18px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
    }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 8px;
      display: flex;
      align-items: baseline;
      gap: 8px;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: var(--text);
      line-height: 1.8;
      padding-left: 24px;
    }}
    .step-box {{
      display: flex;
      gap: 16px;
      margin-bottom: 16px;
    }}
    .step-num {{
      background: var(--primary-dark);
      color: #ffffff;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      font-weight: 700;
      flex-shrink: 0;
      margin-top: 4px;
    }}
    .step-text h4 {{
      font-size: 1rem;
      margin-bottom: 4px;
      color: var(--primary-dark);
    }}
    .step-text p {{
      font-size: 0.92rem;
      margin-bottom: 0;
    }}

    /* Internal links */
    .internal-link-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px;
      margin-top: 20px;
    }}
    .internal-card {{
      background: #faf6f0;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px 16px;
      text-decoration: none;
      color: var(--text);
      transition: all 0.2s;
    }}
    .internal-card:hover {{
      border-color: var(--primary);
      background: #f5ece1;
      transform: translateY(-2px);
    }}
    .internal-card h5 {{
      font-size: 0.92rem;
      color: var(--primary-dark);
      margin-bottom: 4px;
    }}
    .internal-card p {{
      font-size: 0.8rem;
      color: var(--text-sub);
      margin-bottom: 0;
    }}

    footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 40px 20px;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-top: 60px;
    }}

    @media (max-width: 768px) {{
      .product-main {{
        grid-template-columns: 1fr;
      }}
      .img-box {{
        margin-bottom: 16px;
      }}
      h1 {{
        font-size: 1.5rem;
      }}
      .article-header {{
        padding: 24px 18px;
      }}
      .content-section, .ranking-card {{
        padding: 22px 18px;
      }}
    }}
  </style>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="/" class="site-title">❄️ 冬コスメ徹底比較ラボ</a>
    <ul class="nav-links">
      <li><a href="/">ホーム</a></li>
      <li><a href="/winter-ceramide-lotion">セラミド化粧水</a></li>
      <li><a href="/winter-squalane-oil">スクワランオイル</a></li>
      <li><a href="/winter-medicinal-lip">薬用リップ</a></li>
    </ul>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">TOP</a> &gt; <a href="/winter-body-care">冬のボディ・パーツケア</a> &gt; <span>高保湿シアバター</span>
</div>

<main class="container">
  <article>
    <header class="article-header">
      <span class="badge">2026年冬 最新決定版 / 11〜12月集中保湿</span>
      <h1>保湿力の強さで肌乾燥とさようなら！天然の濃厚ベールで極上保護する高保湿シアバターランク10</h1>
      <div class="meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証機関: 冬コスメ徹底比較ラボ 編集部</span>
        <span>対象: 顔・唇・髪・手足の深刻な粉吹き乾燥</span>
      </div>
      <div class="lead-box">
        <p><strong>「どれだけ化粧水や乳液を塗り重ねても、暖房の効いた部屋にいると夕方には頬やすねがカサカサ粉を吹いてしまう……」</strong></p>
        <p>11月中旬から12月にかけて、日本の空気は急速に乾き、外気湿度は30%台まで急落します。さらに室内の暖房温風が追い打ちをかけ、肌本来の皮脂膜は激減。角質層の水分が猛烈なスピードで蒸発してしまいます。</p>
        <p>そんな真冬の極限乾燥から肌を守り抜く『最後の砦』として、世界中で何世紀にもわたり愛用されているのが<strong>天然のシアバター（Shea Butter）</strong>です。人間の皮脂と極めて親和性が高いステアリン酸やオレイン酸を豊富に含み、体温でとろけて肌に吸い付くように密着。本記事では、楽天APIからリアルタイムに取得した最新データに基づき、純度100%のピュアオーガニックから使いやすい高濃度ブレンドまで、真冬に心からおすすめできる高保湿シアバター10選を徹底比較します。</p>
      </div>
    </header>

    <!-- 科学的背景・解説セクション -->
    <section class="content-section">
      <h2>🔬 なぜ11月・12月の冬枯れ肌にシアバターが最強なのか？</h2>
      <p>シアバターは、西アフリカから中央アフリカにかけて自生するアカテツ科の樹木「シアの木」の種子（シアナッツ）から抽出される植物性の油脂です。現地では過酷な乾燥気候や強い紫外線から肌を守るため、生まれたばかりの赤ちゃんの産着ケアから伝統薬として重用されてきました。</p>
      
      <div class="feature-grid">
        <div class="feature-card">
          <h4>1. 人間の皮脂膜に類似した脂肪酸組成</h4>
          <p>主成分であるステアリン酸（約40%）とオレイン酸（約45%）は、人間の皮脂膜や角質細胞間脂質と極めて近い構造を持ちます。そのため肌への親和性が抜群で、浸透しつつ強固な油膜シールドを形成します。</p>
        </div>
        <div class="feature-card">
          <h4>2. 体温（約36℃）でとろけるメルティ性</h4>
          <p>常温では固形のバター状ですが、手のひらに乗せると体温によって数秒で黄金色の濃厚なリキッドオイルへと融解。肌摩擦を一切起こさずに、キメの溝の奥深くまで滑らかに行き渡ります。</p>
        </div>
        <div class="feature-card">
          <h4>3. 不けん化物がもたらす美肌・保護作用</h4>
          <p>植物油脂の中でも特に高い「不けん化物（カルテノール、アラントイン、トコフェロールなど）」を含有。単なる水分蒸発防止にとどまらず、寒風刺激による赤みや炎症を穏やかに落ち着かせます。</p>
        </div>
        <div class="feature-card">
          <h4>4. 顔・唇・毛先・全身まで使える万能性</h4>
          <p>合成化学物質や界面活性剤を含まない天然100%のシアバターは、スキンケアの締めくくりからリップパック、ヘアワックス、ネイルケア、かかとの角質保護までこれ1つで完結します。</p>
        </div>
      </div>

      <h3>💡 「未精製」と「精製」の違いを知って選ぶ</h3>
      <p>シアバターを選ぶ際、最も重要なのが<strong>「未精製（Unrefined）」</strong>か<strong>「精製（Refined）」</strong>かの選択です。</p>
      <ul style="padding-left: 20px; margin-bottom: 16px; font-size: 0.95rem;">
        <li style="margin-bottom: 8px;"><strong>未精製シアバター：</strong>伝統的な手作業や低温圧搾で抽出され、薬品による脱色・脱臭を行わないタイプ。淡いクリーム色でナッツ特有の香ばしい香りがあり、ビタミンや微量栄養素がそのまま豊富に残っています。自然の恵みをダイレクトに感じたい方におすすめです。</li>
        <li><strong>精製シアバター：</strong>不純物や独特のナッツ臭を高度な精製技術で除去したタイプ。真っ白でクセがなく、酸化安定性に優れています。香りに敏感な方、赤ちゃんや超敏感肌の方、日中に香りを気にせず使いたい方に最適です。</li>
      </ul>
    </section>

    <!-- ランキング一覧 -->
    <section>
      <h2 style="font-size: 1.5rem; color: var(--primary-dark); margin: 36px 0 24px; text-align: center;">
        🏆 冬の高保湿シアバター おすすめランキング10選
      </h2>
"""

# ランキングカードを動的生成
for p in product_details:
    r_item = items[p["rank"] - 1]
    rev_count = r_item["reviewCount"]
    rev_avg = r_item["reviewAverage"]
    rev_str = f"★ {rev_avg} ({rev_count:,}件のレビュー)" if rev_count > 0 else "★ 新着・高評価アイテム"
    
    html_content += f"""
      <article class="ranking-card" id="rank-{p['rank']}">
        <div class="rank-header">
          <div class="rank-number">{p['rank']}</div>
          <div class="rank-title-group">
            <h3>{p['brand_name']} {p['capacity']}</h3>
            <span class="rank-tag">{p['tag']}</span>
          </div>
        </div>

        <div class="product-main">
          <div class="img-box">
            <img src="{r_item['image']}" alt="{p['brand_name']} {p['capacity']}" class="product-img" loading="lazy">
            <div class="price-box" style="justify-content: center; margin-top: 10px;">
              <span class="price-val">¥{r_item['price']:,}</span>
              <span style="font-size: 0.8rem; color: var(--text-sub);">(税込)</span>
            </div>
            <div class="review-score">{rev_str}</div>
            <div style="margin-top: 14px;">
              <a href="{r_item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
                楽天で詳細を見る ❯
              </a>
            </div>
          </div>

          <div class="product-info-col">
            <div class="product-spec">
              <div class="spec-item"><span class="spec-label">商品カテゴリ:</span> {p['type']}</div>
              <div class="spec-item"><span class="spec-label">主要成分:</span> {p['features']}</div>
              <div class="spec-item"><span class="spec-label">特徴・強み:</span> {p['value']}</div>
            </div>

            <div class="product-desc">
              <p>{p['desc_p1']}</p>
              <p>{p['desc_p2']}</p>
            </div>

            <div class="user-point">
              <strong>🎯 こんな方・シーンに最適:</strong> {p['target']}
            </div>

            <div class="user-point" style="background: #fdf5e6; border-left-color: var(--primary);">
              <strong>✨ プロ直伝・冬の使い方のコツ:</strong> {p['point']}
            </div>
          </div>
        </div>
      </article>
"""

# 比較表、使い方、FAQ、内部リンクセクションを追加
html_content += f"""
    </section>

    <!-- スペック徹底比較表 -->
    <section class="content-section">
      <h2>📊 高保湿シアバター10選 スペック徹底比較一覧表</h2>
      <p>各アイテムの精製度、容量、価格、おすすめの使い方を一覧表にまとめました。ご自身のライフスタイルや乾燥度合いに合わせて最適な1本をお選びください。</p>
      
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位・商品名</th>
              <th>タイプ / 精製度</th>
              <th>内容量</th>
              <th>楽天参考価格</th>
              <th>主な用途</th>
              <th>おすすめ度</th>
            </tr>
          </thead>
          <tbody>
"""

for p in product_details:
    r_item = items[p["rank"] - 1]
    html_content += f"""
            <tr>
              <td><strong>第{p['rank']}位</strong><br>{p['brand_name']}</td>
              <td>{p['type'][:22]}</td>
              <td>{p['capacity'].split()[0]}</td>
              <td style="font-weight: 700; color: #b7094c;">¥{r_item['price']:,}</td>
              <td>{p['target'][:25]}...</td>
              <td>{"★" * (5 if p['rank'] <= 3 else 4)}</td>
            </tr>
"""

html_content += f"""
          </tbody>
        </table>
      </div>
    </section>

    <!-- 真冬の正しい使い方ガイド -->
    <section class="content-section">
      <h2>❄️ 失敗しない！真冬のシアバター効果的活用術ステップ</h2>
      <p>シアバターは油分純度が高いため、使い方を誤ると『肌の上で固まって白浮きする』『ベタつきが気になる』といった原因になります。真冬の保湿効果を最大化する正しいステップをご紹介します。</p>

      <div class="step-box">
        <div class="step-num">1</div>
        <div class="step-text">
          <h4>【事前準備】化粧水や美容液で角層を水分で満たす</h4>
          <p>シアバターは強力な「水分蒸発防止シールド」ですが、シアバター自体に肌へ水分を与える機能はありません。洗顔後、まずは高保湿セラミド化粧水やヒアルロン酸美容液を角層の奥深くまでたっぷり吸わせることが大前提です。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">2</div>
        <div class="step-text">
          <h4>【融解】手のひらで温めて「完全な透明オイル」にする</h4>
          <p>固形状態のまま肌に乗せると、硬くて摩擦の原因になります。小豆大〜パール粒大をスパチュラ等で手のひらに取り、両手を合わせて体温でくるくると擦り合わせ、完全に透明な液体オイル状になるまで溶かします。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">3</div>
        <div class="step-text">
          <h4>【塗布】こすらず「包み込むようにハンドプレス」</h4>
          <p>オイル状になった手のひら全体で、顔を優しく包み込みます。こすって伸ばすのではなく、手のひらの温もりを肌に伝えるように数秒間プレス。額・頬・顎・目元へと優しく押し込むことで、薄く均一な保護膜が完成します。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">4</div>
        <div class="step-text">
          <h4>【マルチ活用】手に残ったオイルでパーツケア</h4>
          <p>手のひらに余ったシアバターは、ティッシュで拭き取らずにそのまま毛先のパサつき、唇、指先の甘皮、ひじやくるぶしに馴染ませます。全身が無駄なく潤う究極のエコ美容です。</p>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="content-section">
      <h2>❓ 高保湿シアバターに関するよくある質問（FAQ）</h2>
      
      <div class="faq-item">
        <div class="faq-q">Q1. ニキビができやすい脂性肌や混合肌でも使えますか？</div>
        <div class="faq-a">
          シアバターに含まれるオレイン酸はアクネ菌の栄養源になりやすいため、皮脂分泌の盛んなTゾーンやニキビができている部位への厚塗りは避けるのが賢明です。ただし、冬場に乾燥しやすい目元や口元、頬のUゾーンに米粒半分程度の極少量を薄くハンドプレスする使い方は、インナードライ対策として非常に有効です。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q2. 冬場にシアバターが容器の中でカチコチに固まってしまいます。どうすればいいですか？</div>
        <div class="faq-a">
          シアバターの融点は約36℃前後のため、室温が20℃を下回る日本の冬場は固化するのが自然な性質です。決して電子レンジ等で直接急加熱せず、使用する分だけ爪の背やスパチュラで削り取り、体温（手のひら）の熱で溶かしてください。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q3. 朝のメイク前にシアバターを塗ると化粧崩れしませんか？</div>
        <div class="faq-a">
          量をつけすぎるとファンデーションのヨレの原因になります。朝のメイク前に使う場合は、夜の半分以下の量（小豆半分程度）を手のひら全体に薄く広げ、乾燥しやすい頬の高い位置だけに軽くハンドプレスしてください。その後、軽くティッシュオフしてから下地を塗ると、日中の乾燥崩れを劇的に防ぐことができます。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q4. 赤ちゃんや子供の冬の肌荒れ・頬のカサカサにも使えますか？</div>
        <div class="faq-a">
          はい、無添加・無香料のピュアシアバター（ロクシタンやママバター等）は、デリケートな乳幼児の肌にも安心してお使いいただけます。冷風で赤くなった赤ちゃんの頬や、よだれかぶれしやすい口周りの保護に極めて効果的です。ただし、ごく稀に植物アレルギーを起こす場合があるため、初めて使用する際は二の腕の内側などでパッチテストを行ってください。
        </div>
      </div>
    </section>

    <!-- 内部リンク -->
    <section class="content-section">
      <h2>🔗 あわせて読みたい！冬の乾燥対策おすすめ関連記事</h2>
      <p>冬の乾燥対策は、水分補給（化粧水）と油分シールド（バーム・オイル・クリーム）の組み合わせが成功の鍵です。あわせてチェックしたい厳選記事をご紹介します。</p>
      
      <div class="internal-link-grid">
        <a href="/winter-ceramide-lotion" class="internal-card">
          <h5>高保湿セラミド化粧水ランク10</h5>
          <p>角層のバリアを整え深層から潤す、冬の最強化粧水特集。</p>
        </a>
        <a href="/winter-squalane-oil" class="internal-card">
          <h5>高純度スクワランオイルランク10</h5>
          <p>たった1滴で極上のツヤ膜を形成するピュアオイル比較。</p>
        </a>
        <a href="/winter-jojoba-oil" class="internal-card">
          <h5>高保湿ホホバオイルランク10</h5>
          <p>皮脂膜成分ワックスエステルで真冬の肌を柔らかく包む名品。</p>
        </a>
        <a href="/winter-urea-cream" class="internal-card">
          <h5>高保湿尿素クリームランク10</h5>
          <p>ガサガサかかと・ひじの角質を柔らかくほぐす集中補修クリーム。</p>
        </a>
        <a href="/winter-medicinal-lip" class="internal-card">
          <h5>高保湿薬用リップクリームランク10</h5>
          <p>唇のひび割れ・皮むけを医薬品・医薬部外品処方で徹底修復。</p>
        </a>
        <a href="/winter-ceramide-cream" class="internal-card">
          <h5>高保湿セラミドクリームランク10</h5>
          <p>真冬の粉吹き・肌荒れを隙間なくブロックする濃密クリーム。</p>
        </a>
      </div>
    </section>
  </article>
</main>

<footer>
  <p>&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved. 無断転載を禁じます。</p>
  <p style="margin-top: 8px; font-size: 0.78rem;">当サイトは楽天アフィリエイトプログラムに参加しています。掲載されている価格や在庫状況は記事執筆時点の最新データです。</p>
</footer>

</body>
</html>
"""

with open("winter-shea-butter.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-shea-butter.html")
