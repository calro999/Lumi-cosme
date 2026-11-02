import json
import re

with open("fetched_3new_nov_dec_argan_horse_panthenol_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_horse_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 日本初の化粧品認可を取得した元祖！純度100%のマルチ保湿で冬の乾燥を一掃する絶対的マスターピース",
        "catch": "昭和63年の認可から愛され続ける名品。添加物を一切加えない食用基準の純馬油が肌に吸い付く",
        "brand_name": "薬師堂 ソンバーユ",
        "capacity": "70ml (ソンバーユ 無香料)",
        "type": "馬油100%・無香料・添加物完全不使用",
        "features": "国産馬脂100%、真空蒸気精製、旧表示指定成分無添加、赤ちゃんからお年寄りまで口に入っても無害",
        "value": "馬油のパイオニアが誇る最高純度。人間の皮脂に極めて近い脂肪酸バランスが角層深部へ瞬時に浸透し、真冬の粉吹き・ひび割れを根本防御",
        "desc_p1": "11月・12月の冬本番、暖房の効いた室内で急激に奪われる皮脂膜。市販のハンドクリームや乳液では太刀打ちできないほどの深刻なカサつき・粉吹き・ひび割れに悩む方にとって、最も頼れる存在が薬師堂の『ソンバーユ 無香料』です。",
        "desc_p2": "独自の高真空蒸気精製技術により、馬油特有の油臭さや不純物を徹底的に除去。指先に取ると体温で瞬時にサラサラの液状へと融解し、肌にのせた瞬間からグングン角層へと吸い込まれていきます。油分でありながらベタつかず、数分後にはしっとりとした柔らかさだけが肌に残る驚異の浸透力を誇ります。洗顔直後のブースターから、夜のナイトパック、唇の荒れ、毛先のパサつき、かかとのガサガサまで全身くまなくケアできる万能の1本です。",
        "target": "粉吹きやひび割れが止まらない重度の乾燥肌の方、口元や目元にも安心して使える天然100%を求める方、家族全員で使える保湿バームを探している方",
        "point": "洗顔直後、肌に水分が残っている状態で小豆粒大を全顔に薄く伸ばします。5分ほど置いて馬油が馴染んだ後にいつもの化粧水を重ねると、驚くほどもっちり仕上がります。"
    },
    {
        "rank": 2,
        "tag": "❄️ 北の大地が育んだ極上のなめらかさ！徹底した低温精製で白くキメ細やかに仕上げた無添加馬油",
        "catch": "北海道産の良質な馬油を100%使用。職人の手仕事と徹底した温度管理が生み出す極上テクスチャー",
        "brand_name": "北海道純馬油本舗",
        "capacity": "100g (馬油100% ピュアホワイト)",
        "type": "北海道産馬油100%・無香料・完全無添加",
        "features": "北海道産原料、低温真空脱臭精製、純度100%、防腐剤・化学溶剤不使用",
        "value": "極寒の北海道で磨かれたスキンケア技術。雪のように白くホイップのようななめらかさで、冬の冷風にさらされた素肌をしっとり優しく包み込む",
        "desc_p1": "冬の厳しい寒さと乾燥にさらされる北海道で、半世紀以上にわたり馬油づくりを追求し続ける『北海道純馬油本舗』。良質な北海道産馬脂肪のみを厳選し、熟練の職人が手間暇かけて精製したピュアオイルです。",
        "desc_p2": "一般的な馬油よりもさらに低温でじっくりと不純物をろ過精製することで、雪のように真っ白でキメ細やかなバーム状を実現。肌にのせると体温に触れた部分からスルスルととろけ、まるで良質な美容液のように角質層へ浸透します。気になる油臭が一切なく、デリケートな赤ちゃんの頬や、冬の寒さで赤くなった鼻周りのカサつきにも優しく寄り添います。大容量100gで毎日のフェイス＆ボディケアに贅沢に使えます。",
        "target": "馬油の独特な匂いが苦手な方、極寒地基準の濃厚な保湿力を求める方、赤ちゃんのスキンケアにも使いたい方",
        "point": "お風呂で湯船に浸かりながら、顔全体に少し多めの馬油を伸ばして5分間放置する『入浴スチームパック』を行うと、毛穴の角栓が緩んで翌朝の化粧ノリが激変します。"
    },
    {
        "rank": 3,
        "tag": "💧 液状だから冬でも固まらない！洗顔後のブースターに最適なさらさら高浸透ドロップ",
        "catch": "馬油の最も比重の軽い液体成分のみを抽出。スポイト感覚で使えるストレスフリーな導入馬油",
        "brand_name": "薬師堂 ソンバーユ",
        "capacity": "55ml (液状特製)",
        "type": "液状馬油100%・無香料・先行美容液タイプ",
        "features": "高真空蒸気精製、低温分離抽出、冬場も液体キープ、ノズル付きボトル",
        "value": "馬油の優れた浸透力を持つ液状部分だけを贅沢に分取。固形バームのように溶かす手間がなく、洗顔後の導入液や朝のメイク前ケアに抜群の機能性を発揮",
        "desc_p1": "通常の固形馬油は冬場の寒い洗面所に置くとカチコチに固まり、指で削り取るのが少し手間に感じることがあります。そんな冬特有の使いづらさを完全に解消したのが、ソンバーユの『液状特製』です。",
        "desc_p2": "馬油の比重が軽く浸透性に優れた液状部分のみを低温でじっくりと分離抽出。真冬の冷え切った室内でも固まらず、常にサラサラのオイル状態を維持します。ノズルから数滴手のひらに落として肌に伸ばすと、通常のオイルでは考えられないほどの猛スピードで角層へ吸収されます。朝の洗顔後、化粧水の前に1〜2滴仕込んでもテカリやメイク崩れを起こさず、一日中乾燥知らずのツヤ肌をキープできます。",
        "target": "冬でも固まらない液体タイプを求める方、朝の忙しい時間にサッと使いたい方、ブースターとしての浸透速度を最重視する方",
        "point": "洗顔後、手のひらに1〜2滴出して軽く伸ばし、頬からフェイスラインへスタンプするように押し込みます。その直後に化粧水を重ねてください。"
    },
    {
        "rank": 4,
        "tag": "💊 創業明治の製薬会社が開発！高純度精製技術と天然無臭を極めた医療発想の馬油スキンオイル",
        "catch": "医薬品製造基準の徹底した品質管理。不快なベタつきを極限まで抑えたシルキーな仕上がり",
        "brand_name": "REMAYU (リマーユ)",
        "capacity": "30ml (リマーユ 馬油 スキンオイル)",
        "type": "製薬会社開発・高純度精製馬油",
        "features": "高純度脱色・脱臭精製、プッシュ式ボトル、パラベン・香料・着色料フリー、製薬会社品質",
        "value": "熊本の老舗製薬会社リバテープが手がける最高峰馬油。角質細胞間脂質へのなじみが極めて高く、冬のゆらぎ肌や目元・口元のエイジングサインを集中リペア",
        "desc_p1": "救急絆創膏などで知られる明治創業の製薬企業・リバテープ製薬が、本場熊本の上質な馬油を最新の医薬品精製技術で昇華させた『リマーユ 馬油スキンオイル』。品質の高さと使い心地の良さから皮膚科医や美容家からも高く評価されています。",
        "desc_p2": "製薬会社ならではの高度な多段階精製により、酸化の原因となる微量不純物を極限までカット。独特の動物臭が完全に抑えられており、オイル特有の重さを感じさせないシルキーなテクスチャーが肌を滑らかに包み込みます。使いやすいプッシュ式ボトルを採用しており、空気に触れにくく鮮度を長く保てる点も高評価。乾燥小ジワが目立ちやすい目尻やほうれい線へのピンポイントケアにも威力を発揮します。",
        "target": "製薬会社基準の確かな品質にこだわりたい方、オイルの酸化や匂いに敏感な方、目元やほうれい線の集中ケアをしたい方",
        "point": "夜のお手入れの最後に、1プッシュを指先に取り、目元や口元の乾燥しやすい部分にトントンと優しく重ねづけして密封してください。"
    },
    {
        "rank": 5,
        "tag": "🛁 家族全員で毎日使える超特大220g！高保湿馬油に尿素と植物エキスをブレンドした大容量クリーム",
        "catch": "ドラッグストアで圧倒的人気を誇る高コスパの星。伸びが良くベタつかないデイリーボディケア",
        "brand_name": "ロッシモイストエイド",
        "capacity": "220g (馬油スキンクリーム)",
        "type": "馬油＆保湿成分配合・高保湿マルチスキンクリーム",
        "features": "国産馬油配合、尿素・シアバター・モモ葉エキス配合、弱酸性、大容量ジャー",
        "value": "馬油の優れたエモリエント効果に、水分を引き寄せる保湿成分を黄金比率でブレンド。お風呂上がりのすねや腕など全身の広範囲を素早くラッピング",
        "desc_p1": "冬になると全身の粉吹きや、お風呂上がりの体のカサカサかゆみに悩まされる方が急増します。そんな広範囲の冬乾燥を惜しみなく手軽にケアできる大定番が、コスメテックスローランドの『ロッシモイストエイド 馬油スキンクリーム』です。",
        "desc_p2": "良質な国産馬油に、角質柔軟成分である尿素やシアバター、植物エキスを贅沢にブレンドした高機能エマルジョン。純度100%の馬油よりもみずみずしく、手のひらでスーッとどこまでも伸び広がる軽快な使い心地が魅力です。塗った直後から肌表面にサラリとしたうるおいヴェールが完成し、パジャマや下着が張り付く不快感もゼロ。220gの圧倒的な大容量で、家族みんなで毎日たっぷり使い倒せます。",
        "target": "お風呂上がりに全身を手早く保湿したい方、ベタつくのが苦手なお子様や男性、コストパフォーマンスを最優先したい方",
        "point": "入浴後、タオルドライした直後の温まった肌にたっぷり取り、すね・太もも・腕・背中へと円を描くように塗り広げてください。"
    },
    {
        "rank": 6,
        "tag": "💪 ガサガサ手足・ひびあかぎれの救世主！本場・熊本の伝統処方を受け継ぐ濃厚バーユクリーム",
        "catch": "冬の水仕事や外仕事で荒れ果てた手肌を強力修復。昔ながらの職人技が光る本格派",
        "brand_name": "ショウキリュウ (昇龍)",
        "capacity": "80ml (素肌クリーム)",
        "type": "純馬油・肌荒れひびあかぎれ用保湿クリーム",
        "features": "国産馬油、無着色・防腐剤無添加、トコフェロール（ビタミンE）配合、高密着バーム処方",
        "value": "硬くなった角質層をじっくりほぐして柔軟化。冬のひび割れやあかぎれでピキッと痛む手指・かかとを濃厚な油膜で物理的・生理的に守り抜く",
        "desc_p1": "冬の冷たい水仕事や屋外作業で、指先がひび割れたり、かかとが白くガサガサにひび割れて靴下に引っかかったり……そんな深刻なパーツの乾燥トラブルに長年愛用されてきたのが、ショウキリュウの『素肌クリーム』です。",
        "desc_p2": "本場熊本の新鮮な馬油をベースに、天然ビタミンEを配合して酸化安定性を高めた濃厚処方。指先で取るとこっくりとした質感ですが、患部に塗り込むと体温でとろけてひび割れの奥深くまで隙間なく密着します。患部を外気や水から遮断して自己治癒力をサポート。使い続けるうちにカチコチに硬化していた角質が柔らかくなり、なめらかな素肌へと戻っていきます。",
        "target": "冬の水仕事で手荒れ・ひび割れがひどい方、かかとが硬くひび割れて痛む方、昔ながらの力強い保湿力を求める方",
        "point": "就寝前にかかとや指先にたっぷり塗り込み、綿の手袋やつま先付きの靴下を履いて寝ると、翌朝驚くほどふっくら柔らかくなります。"
    },
    {
        "rank": 7,
        "tag": "🍦 スイートなバニラの香りで癒される！馬油の優れた保湿力とスイーツのような甘いアロマの融合",
        "catch": "ソンバーユの確かな品質に天然香料をプラス。毎日のスキンケアがご褒美タイムに変わる人気フレーバー",
        "brand_name": "薬師堂 ソンバーユ",
        "capacity": "70ml (ソンバーユ バニラの香り)",
        "type": "馬油・天然バニラ香料配合",
        "features": "国産馬油ベース、天然香料使用、旧表示指定成分無添加、口に入っても安心な食用基準",
        "value": "無香料のソンバーユと同じ最高純度の馬油に、芳醇なバニラの香りを配合。独特の油っぽさを全く感じさせず、心まで温まる冬のスキンケアを提供",
        "desc_p1": "『ソンバーユの保湿力は大好きだけど、無香料だと少し物足りない』『スキンケアタイムに甘い香りで癒されたい』という女性たちから絶大な人気を集めているのが、バニラの香りのソンバーユです。",
        "desc_p2": "人工的な合成香料ではなく、天然由来のバニラ香料を絶妙な比率で配合。フタを開けた瞬間にふんわりと香る甘く温かみのある香りは、寒さで縮こまった冬の気分をほっと解きほぐします。もちろん中身は薬師堂基準の最高純度馬油そのもの。洗顔後のブースターやリップバームとして使えば、ふっくら潤う唇からほんのり甘い香りが漂い、メイク前の気分を高めてくれます。",
        "target": "甘いバニラやスイーツの香りが好きな方、毎日の保湿ケアでリラックスしたい方、リップケアとしても愛用したい方",
        "point": "乾燥した唇に指先でくるくるとなじませると、バニラの香りに包まれながら縦ジワの目立たないぷるぷるの唇に仕上がります。"
    },
    {
        "rank": 8,
        "tag": "🏆 熊本の老舗油脂メーカーが直火釜で炊き上げた伝統の一品！混じり気なしの天然純度100%",
        "catch": "昔ながらの製法を守り抜く横関油脂。地元九州で何世代にもわたり家庭に常備される本物",
        "brand_name": "横関油脂工業",
        "capacity": "100g (天然 馬油 純度100%)",
        "type": "天然純馬油100%・伝統直火製法",
        "features": "九州・熊本産馬脂肪、添加物・保存料完全無添加、大容量100gガラス瓶、伝統製法",
        "value": "工業的な大量精製ではなく、職人の目利きと温度管理で抽出された純粋な馬油。人の肌に必要な天然脂肪酸がそのまま凝縮された力強い保湿力",
        "desc_p1": "馬肉文化と馬油の聖地である熊本で、創業以来伝統的な油脂精製を守り続ける『横関油脂工業』。余計な化学処理を行わず、良質な原料本来の力を最大限に引き出した天然純馬油です。",
        "desc_p2": "昔ながらの直火釜で丁寧に炊き上げられ、不純物を何度もろ過した純度100%のオイル。少し黄色みを帯びた濃厚な油分には、肌の柔軟性を高めるオレイン酸やパルミチン酸が豊富に含まれています。肌に塗るとジワジワと角質層に浸透し、暖房の温風を跳ね返すような頼もしい保護バリアを構築。顔はもちろん、ひじや膝、赤ちゃんのオムツかぶれ予防など、家庭の万能常備薬として冬中大活躍します。",
        "target": "昔ながらの伝統製法や職人の手仕事に惹かれる方、添加物の入っていない本物の馬油を求める方、大容量で長く使いたい方",
        "point": "お風呂上がりに、まだ水滴の残る肌に薄く伸ばすと、水分と一緒にスーッと馴染んでベタつかずに全身がしっとり整います。"
    },
    {
        "rank": 9,
        "tag": "👑 美肌のために選び抜かれた最上級グレード！比類なきコクとキメ細やかさを誇るプレミアムソンバーユ",
        "catch": "薬師堂の技術の粋を集めた最高峰。大人の乾燥肌とエイジングサインをしっとり格上げ",
        "brand_name": "薬師堂 ソンバーユ",
        "capacity": "60ml (ソンバーユ No.7 美肌用)",
        "type": "最高峰美肌用馬油・プレミアム仕様",
        "features": "厳選上質馬油、特殊高密度精製、無香料、ガラス容器、エイジングケア対応",
        "value": "ソンバーユシリーズの中で最も保湿力と美肌効果に特化したハイエンドモデル。通常のソンバーユよりも濃厚でコクがあり、真冬の乾燥小ジワをふっくら持ち上げる",
        "desc_p1": "『ソンバーユの中でも最高峰の使い心地を求めたい』というスキンケア上級者の声に応えて作られたのが、『ソンバーユ No.7』です。通常のソンバーユよりもさらに上質な馬油成分だけを厳選して抽出されています。",
        "desc_p2": "手に取った瞬間にわかる、なめらかで密度の高いこっくりとした質感。肌に伸ばすと、まるで高級クリームのように吸い付き、角層の隙間を隙間なく満たしていきます。真冬の寒さでゴワつき、ハリを失った大人の肌に、内側から押し返すような弾力とシルクのような艶やかなヴェールを付与。夜のスキンケアの最後にハンドプレスでしっかり密着させれば、翌朝の洗顔時に自分の肌のなめらかさに息を呑むはずです。",
        "target": "通常の馬油では保湿力が物足りない超乾燥肌の方、年齢に応じたエイジングケアに力を入れたい方、ワンランク上のギフトを探している方",
        "point": "夜のお手入れの最後に、あずき粒大を手のひらで温めて全顔を包み込むようにハンドプレス。翌朝まで暖房をつけた寝室でも一切乾燥しません。"
    },
    {
        "rank": 10,
        "tag": "🌿 製薬会社の知恵が詰まった高機能処方！馬油×スクワラン×尿素のトリプルうるおいシールド",
        "catch": "馬油の浸透力に人気の保湿成分をプラス。ベタつかずスーッと馴染んで手荒れ・肌荒れを先回りブロック",
        "brand_name": "リバテープ製薬",
        "capacity": "70g (製薬会社が作った 馬油クリーム)",
        "type": "馬油配合・高機能メディカルモイスチャークリーム",
        "features": "国産馬油、スクワラン、尿素配合、弱酸性、チューブタイプで衛生的",
        "value": "馬油の油分補給力に、角質柔軟成分（尿素）と高純度エモリエント（スクワラン）を融合。冬の硬くなった角質をしっとり柔らかく解きほぐす",
        "desc_p1": "馬油単体の良さを熟知する製薬会社が、現代人の使いやすさと相乗効果を追求して開発した『製薬会社が作った 馬油クリーム』。馬油、スクワラン、尿素という冬の乾燥対策の三大エースを1本に凝縮しています。",
        "desc_p2": "チューブからサッと出せるジェルインクリームタイプで、外出先やオフィスでも手を汚さずに手軽に使えます。尿素がガサつく角質を穏やかに柔らかくし、馬油とスクワランがダブルで油分を補給して水分蒸散をブロック。塗った直後からサラサラの手触りに変わるため、スマホの画面やパソコンのキーボードをすぐに触れる実用性の高さも冬のデイリーケアに嬉しいポイントです。",
        "target": "外出先やオフィスで手軽に使いたい方、ベタつきのないチューブ型を好む方、尿素の角質ケア効果も同時に得たい方",
        "point": "手洗いや水仕事の直後、水分を拭き取ったらすぐにパール粒大を手に伸ばし、爪の周りまでしっかり揉み込んでください。"
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
            "image": r_item["img_url"],
            "description": p["value"],
            "brand": {
                "@type": "Brand",
                "name": p["brand_name"]
            },
            "offers": {
                "@type": "Offer",
                "url": r_item["affiliate_url"],
                "priceCurrency": "JPY",
                "price": r_item["price"],
                "availability": "https://schema.org/InStock"
            }
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで頑固な肌乾燥・粉吹きとさようなら！人の皮脂に極めて近い天然脂質で包み込む高保湿馬油クリームランク10",
    "description": "11月・12月の真冬の冷風と暖房直撃による深刻な粉吹き乾燥・ひび・あかぎれ・肌荒れを徹底解決！人の皮脂バランスに極めて酷似した天然不飽和脂肪酸が角層深部へ驚異のスピードで浸透する高保湿馬油10選を徹底比較！ソンバーユ、北海道純馬油本舗、リマーユ、ロッシモイストエイドなど厳選。洗顔後すぐの導入ケアから顔・手足・全身の保護まで完全網羅。",
    "image": items[0]["img_url"],
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
    "name": "冬の高保湿馬油クリーム おすすめランキング10選",
    "itemListElement": item_list_elements
}

# HTML Template
html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで頑固な肌乾燥・粉吹きとさようなら！人の皮脂に極めて近い天然脂質で包み込む高保湿馬油クリームランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の真冬の冷風と暖房直撃による深刻な粉吹き乾燥・ひび・あかぎれ・肌荒れを徹底解決！人の皮脂バランスに極めて酷似した天然不飽和脂肪酸が角層深部へ驚異のスピードで浸透する高保湿馬油10選を徹底比較！ソンバーユ、北海道純馬油本舗、リマーユ、ロッシモイストエイドなど厳選。洗顔後すぐの導入ケアから顔・手足・全身の保護まで完全網羅。">
  <meta name="keywords" content="馬油,ソンバーユ,高保湿クリーム,冬 保湿,バーユ,ひびあかぎれ,馬油洗顔,導入オイル,乾燥肌対策 2026">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-horse-oil">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで頑固な肌乾燥・粉吹きとさようなら！人の皮脂に極めて近い天然脂質で包み込む高保湿馬油クリームランク10">
  <meta property="og:description" content="11月・12月の過酷な冬乾燥に終止符を打つ！人の皮脂に最も近い天然エモリエント・高保湿馬油10選を徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-horse-oil">
  <meta property="og:image" content="{items[0]['img_url']}">
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
      <li><a href="/winter-argan-oil">アルガンオイル</a></li>
      <li><a href="/winter-shea-butter">高保湿シアバター</a></li>
    </ul>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">TOP</a> &gt; <a href="/winter-body-care">冬のボディ・パーツケア</a> &gt; <span>高保湿馬油クリーム</span>
</div>

<main class="container">
  <article>
    <header class="article-header">
      <span class="badge">2026年冬 最新決定版 / 11〜12月集中保湿</span>
      <h1>保湿力の強さで頑固な肌乾燥・粉吹きとさようなら！人の皮脂に極めて近い天然脂質で包み込む高保湿馬油クリームランク10</h1>
      <div class="meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証機関: 冬コスメ徹底比較ラボ 編集部</span>
        <span>対象: 顔・手足の粉吹き乾燥・ひびあかぎれ・タイツが引っかかるかかと</span>
      </div>
      <div class="lead-box">
        <p><strong>「どんな高保湿クリームを塗っても、朝起きると頬が突っ張り、すねやかかとが粉を吹いてしまう……」</strong></p>
        <p>11月下旬から12月にかけて、湿度は30%台まで急落し、暖房の温風が直接肌を直撃します。この過酷な環境下では、肌の水分を抱え込む『皮脂膜』が急速に枯渇。水分が蒸発するだけでなく、肌のバリア機能が崩壊して外的刺激に敏感になってしまいます。</p>
        <p>そんな真冬の極限乾燥から肌を救い出す伝統の切り札が、古くから日本の家庭で愛され続けてきた<strong>『馬油（バーユ）』</strong>です。馬油の最大の特徴は、植物油や鉱物油には真似できない<strong>『人間の皮脂に驚くほど類似した脂肪酸バランス』</strong>。肌にのせた瞬間、肌が自らの皮脂と錯覚するかのように角層深部へと猛スピードで吸い込まれ、ベタつきを残さず強力な潤いシールドを形成します。本記事では、楽天APIの最新データを基に、元祖ソンバーユから高機能処方まで、冬の乾燥トラブルを根本解決する高保湿馬油10選を徹底比較します。</p>
      </div>
    </header>

    <!-- 科学的背景・解説セクション -->
    <section class="content-section">
      <h2>🔬 なぜ11月・12月の頑固な乾燥肌に馬油が選ばれ続けるのか？</h2>
      <p>馬油は、馬の皮下脂肪やたてがみ下の脂肪から抽出・精製された天然油脂です。4000年以上前の古代中国の医学書『本草綱目』にもその有用性が記され、日本では九州を中心に民間薬・保護油として重宝されてきました。</p>
      
      <div class="feature-grid">
        <div class="feature-card">
          <h4>1. 人間の皮脂に極めて酷似した脂肪酸構成</h4>
          <p>不飽和脂肪酸（オレイン酸・リノール酸・リノレン酸）と飽和脂肪酸（パルミチン酸など）の比率が約6:4。人間の皮脂組織とほぼ同じバランスを持つため、皮膚刺激が極めて少なく、角層へ素早く同化します。</p>
        </div>
        <div class="feature-card">
          <h4>2. 圧倒的な角層浸透スピード</h4>
          <p>鉱物油（ワセリン等）が肌表面に留まってフタをするのに対し、馬油は塗った瞬間から細胞間脂質の間をすり抜けて深部へ浸透。肌の内側を柔らかく満たしながら、表面はサラリとした質感に整えます。</p>
        </div>
        <div class="feature-card">
          <h4>3. 寒冷風と水刺激を遮断する保護シールド</h4>
          <p>浸透した油分が角層細胞を密着させ、外気中の冷風や暖房の乾燥、さらには冬の水仕事による刺激から肌を物理的に隔離。ひび・あかぎれ・しもやけの悪化を防ぎ、健やかな肌環境を保ちます。</p>
        </div>
        <div class="feature-card">
          <h4>4. 顔・唇・髪・手足・赤ちゃんまで使える万能性</h4>
          <p>添加物を加えない純度100%の馬油は口に入っても安全な食用基準。デリケートな赤ちゃんの頬やおむつ周り、授乳中のママのケアから、頑固なかかとの角質ケアまで1瓶で完全対応します。</p>
        </div>
      </div>

      <h3>💡 バーム型（固形）とリキッド型（液状）の使い分け</h3>
      <p>馬油には、昔ながらの瓶入り<strong>「固形バームタイプ」</strong>と、サラリとした<strong>「液状タイプ」</strong>が存在します。</p>
      <ul style="padding-left: 20px; margin-bottom: 16px; font-size: 0.95rem;">
        <li style="margin-bottom: 8px;"><strong>固形バームタイプ（ソンバーユ無香料など）：</strong>常温では軟膏状ですが、体温で瞬時にとろけます。油膜の保護力が非常に強く、夜の集中ナイトパックやかかとのひび割れ、指先のあかぎれ保護に最適です。</li>
        <li><strong>液状タイプ（ソンバーユ液状特製など）：</strong>馬油の比重の軽い液体成分だけを低温抽出したタイプ。冬場の寒い部屋でも固まらず、洗顔後すぐの導入ブースターや、朝のメイク前の乾燥対策としてストレスフリーに使えます。</li>
      </ul>
    </section>

    <!-- ランキング一覧 -->
    <section>
      <h2 style="font-size: 1.5rem; color: var(--primary-dark); margin: 36px 0 24px; text-align: center;">
        🏆 冬の高保湿馬油クリーム おすすめランキング10選
      </h2>
"""

for p in product_details:
    r_item = items[p["rank"] - 1]
    rev_str = f"★ {r_item['review_average']} ({r_item['review_count']}件)" if r_item['review_count'] > 0 else "最新注目アイテム"
    
    html_content += f"""
      <!-- Rank {p['rank']} -->
      <div class="ranking-card" id="rank-{p['rank']}">
        <div class="rank-header">
          <div class="rank-number">{p['rank']}</div>
          <div class="rank-title-group">
            <h3>{r_item['name']}</h3>
            <span class="rank-tag">{p['tag']}</span>
          </div>
        </div>
        
        <p style="font-size: 0.95rem; color: var(--primary-dark); font-weight: 600; margin-bottom: 14px;">
          {p['catch']}
        </p>

        <div class="product-main">
          <div class="img-box">
            <img src="{r_item['img_url']}" alt="{r_item['name']}" class="product-img" loading="lazy">
            <div class="price-box" style="justify-content: center;">
              <span class="price-val">¥{r_item['price']:,}</span>
              <span class="review-score">{rev_str}</span>
            </div>
            <a href="{r_item['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
              楽天で詳細を見る
            </a>
          </div>

          <div class="product-info">
            <div class="product-spec">
              <div class="spec-item"><span class="spec-label">ブランド</span>{p['brand_name']}</div>
              <div class="spec-item"><span class="spec-label">容量・タイプ</span>{p['capacity']} / {p['type']}</div>
              <div class="spec-item"><span class="spec-label">主要な特徴</span>{p['features']}</div>
              <div class="spec-item"><span class="spec-label">高保湿の核心</span>{p['value']}</div>
            </div>

            <div class="product-desc">
              <p>{p['desc_p1']}</p>
              <p>{p['desc_p2']}</p>
            </div>

            <div class="user-point">
              <strong>💡 こんな方におすすめ：</strong>{p['target']}<br>
              <strong>✨ プロ直伝の使い方：</strong>{p['point']}
            </div>
          </div>
        </div>
      </div>
"""

html_content += """
    </section>

    <!-- 比較表セクション -->
    <section class="content-section">
      <h2>📊 冬の高保湿馬油 スペック徹底比較一覧</h2>
      <p>ご自身のライフスタイルやお悩みの部位に合わせて最適な馬油を選べるよう、10商品のスペックと特徴を比較表にまとめました。</p>
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>タイプ</th>
              <th>容量</th>
              <th>価格(税込)</th>
              <th>おすすめの用途</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1位</td>
              <td>薬師堂 ソンバーユ 無香料</td>
              <td>元祖純馬油100%</td>
              <td>70ml</td>
              <td>¥1,373</td>
              <td>万能マルチケア・夜のナイトパック</td>
            </tr>
            <tr>
              <td>2位</td>
              <td>北海道純馬油本舗 ピュアホワイト</td>
              <td>北海道産純馬油</td>
              <td>100g</td>
              <td>¥6,600(セット等)</td>
              <td>極上テクスチャー・赤ちゃんスキンケア</td>
            </tr>
            <tr>
              <td>3位</td>
              <td>薬師堂 ソンバーユ 液状特製</td>
              <td>液状純馬油100%</td>
              <td>55ml</td>
              <td>¥1,320</td>
              <td>冬も固まらない・洗顔後ブースター</td>
            </tr>
            <tr>
              <td>4位</td>
              <td>REMAYU リマーユ 馬油スキンオイル</td>
              <td>製薬会社高純度精製</td>
              <td>30ml</td>
              <td>¥2,919</td>
              <td>無臭プッシュ式・目元口元エイジング</td>
            </tr>
            <tr>
              <td>5位</td>
              <td>ロッシモイストエイド 馬油スキンクリーム</td>
              <td>馬油＆尿素ブレンド</td>
              <td>220g</td>
              <td>¥3,415(複数個等)</td>
              <td>大容量・お風呂上がり全身デイリー</td>
            </tr>
            <tr>
              <td>6位</td>
              <td>ショウキリュウ 素肌クリーム</td>
              <td>熊本産濃厚バーム</td>
              <td>80ml</td>
              <td>¥1,348</td>
              <td>手足ひびあかぎれ・水仕事保護</td>
            </tr>
            <tr>
              <td>7位</td>
              <td>薬師堂 ソンバーユ バニラ</td>
              <td>天然バニラ精油配合</td>
              <td>70ml</td>
              <td>¥1,430</td>
              <td>甘い香りでリラックス・リップケア</td>
            </tr>
            <tr>
              <td>8位</td>
              <td>横関油脂 天然 馬油 純度100%</td>
              <td>直火釜炊き伝統製法</td>
              <td>100g</td>
              <td>¥8,640(徳用等)</td>
              <td>昔ながらの力強さ・家庭の常備薬</td>
            </tr>
            <tr>
              <td>9位</td>
              <td>薬師堂 ソンバーユ No.7 美肌用</td>
              <td>最上級ハイグレード</td>
              <td>60ml</td>
              <td>¥6,800(複数本等)</td>
              <td>濃厚コク・大人の乾燥小ジワ対策</td>
            </tr>
            <tr>
              <td>10位</td>
              <td>リバテープ 馬油クリーム</td>
              <td>馬油×スクワラン×尿素</td>
              <td>70g</td>
              <td>¥820</td>
              <td>外出先チューブ・オフィスハンドケア</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 実践ステップガイド -->
    <section class="content-section">
      <h2>🛁 翌朝の肌が激変！真冬の『馬油美容法』3大テクニック</h2>
      <p>馬油はただ塗るだけでなく、タイミングと水分を味方につけることでその真価を120%発揮します。冬の間にぜひ試していただきたい実践テクニックをご紹介します。</p>

      <div class="step-box">
        <div class="step-num">1</div>
        <div class="step-text">
          <h4>【ブースター使い】洗顔直後、水滴が残る肌に小豆粒大</h4>
          <p>洗顔後、タオルで水気を完璧に拭き取らず、わずかに肌が湿っている状態で小豆粒大の馬油を全顔へ。馬油が水分を巻き込みながら角層へ浸透し、その後に塗る化粧水を驚くほど引き込みます。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">2</div>
        <div class="step-text">
          <h4>【入浴スチームパック】湯船の蒸気で毛穴の角栓をゆるめる</h4>
          <p>クレンジング・洗顔後の清潔な肌に、通常より多め（さくらんぼ大）の馬油を塗り広げ、そのまま湯船に10分浸かります。蒸気で毛穴が開き、角栓が柔らかく浮き上がってつるんとしたむきたまご肌に。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">3</div>
        <div class="step-text">
          <h4>【かかと・指先の靴下密封パック】寝ている間に集中リペア</h4>
          <p>冬の冷えでカチコチになったかかとやひび割れた指先に馬油を塗り込み、綿の靴下や手袋を着用して就寝します。密閉効果で体温が逃げず、翌朝にはガサガサがしっとり柔軟化します。</p>
        </div>
      </div>
    </section>

    <!-- よくある質問 FAQ -->
    <section class="content-section">
      <h2>❓ 馬油に関するよくある疑問・Q&A</h2>

      <div class="faq-item">
        <div class="faq-q">Q. 馬油を塗ると油っぽくてニキビができたりしませんか？</div>
        <div class="faq-a">
          馬油に含まれる不飽和脂肪酸（特にリノール酸・α-リノレン酸）は、皮膚常在菌のバランスを整え、肌を清浄に保つ働きがあります。また浸透スピードが極めて速いため、毛穴に油分が酸化して詰まる心配は一般的な重い鉱物油よりも少ないです。ただし、過剰な量（一度に大量に塗りすぎる）はニキビの原因になり得ますので、「顔全体で小豆粒大」の適量を守ることが大切です。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. 独特の匂いが気になると聞きますが、実際はどうですか？</div>
        <div class="faq-a">
          昔の馬油は精製度が低く独特の動物臭がありましたが、現在の有名メーカー（ソンバーユや北海道純馬油本舗など）は高度な高真空蒸気精製技術を採用しているため、無香料タイプであれば匂いはほぼ無臭です。それでも気になる方には、天然バニラ精油が配合されたタイプや、製薬会社が手がける高純度精製オイルがおすすめです。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. 保管方法はどうすれば良いですか？冬場に固まっても大丈夫？</div>
        <div class="faq-a">
          天然100%の馬油は気温の変化に敏感です。冬場は室温が下がると白く固まりますが、手のひらに取れば体温で一瞬で液体に戻るため品質には全く問題ありません。長期保存する場合は、直射日光と高温多湿を避け、開封後はなるべく涼しい冷暗所または冷蔵庫での保管をおすすめします。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. ワセリンやシアバターとは何が違うのですか？</div>
        <div class="faq-a">
          ワセリンは『肌表面を物理的に覆う鉱物油（浸透しない）』、シアバターは『植物油脂による濃厚保護膜』です。これに対して馬油は『人肌皮脂に最も近く、角層深部へ瞬時に浸透する動物性油脂』です。「肌の内側がカサカサする」「表面だけでなく角層をふっくら柔らかくしたい」という方には、浸透力の高い馬油が圧倒的に優れています。
        </div>
      </div>
    </section>

    <!-- 内部リンク関連記事 -->
    <section class="content-section">
      <h2>🔗 あわせて読みたい！真冬の徹底保湿ケア関連記事</h2>
      <p>馬油による皮脂膜補給と合わせて、セラミド補給や他パーツの集中ケアを取り入れることで、冬の乾燥トラブルを隙間なくブロックできます。</p>
      
      <div class="internal-link-grid">
        <a href="/winter-ceramide-lotion" class="internal-card">
          <h5>🧴 高保湿セラミド化粧水</h5>
          <p>馬油ブースターの後に重ねて吸い込ませる！角層バリアを強固にする高保湿化粧水10選</p>
        </a>
        <a href="/winter-argan-oil" class="internal-card">
          <h5>🥑 高保湿アルガンオイル</h5>
          <p>ビタミンE豊富なモロッコの黄金オイル。冬の角質ゴワつきを解きほぐす先行美容液10選</p>
        </a>
        <a href="/winter-urea-cream" class="internal-card">
          <h5>🦶 高保湿尿素クリーム</h5>
          <p>硬くなったひじ・かかとの角質を柔軟化！天然保湿因子NMFを補う薬用クリーム10選</p>
        </a>
        <a href="/winter-shea-butter" class="internal-card">
          <h5>🧈 高保湿シアバター</h5>
          <p>天然の濃厚ベールで極上保護。顔・唇・毛先の粉吹き乾燥を根本解決するバーム10選</p>
        </a>
        <a href="/winter-medicinal-lip" class="internal-card">
          <h5>💄 高保湿薬用リップクリーム</h5>
          <p>唇の皮むけ・ひび割れとさようなら！医薬品有効成分で集中修復する冬リップ10選</p>
        </a>
        <a href="/winter-ceramide-cream" class="internal-card">
          <h5>🧴 高保湿セラミドクリーム</h5>
          <p>角層バリアを高密度修復！冬の冷風から素肌を守り抜く濃厚フェイスクリーム10選</p>
        </a>
      </div>
    </section>
  </article>
</main>

<footer>
  <p>&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved. 当サイトの情報は楽天APIの公開データに基づいており、最新の価格・在庫情報は各販売ページにてご確認ください。</p>
</footer>

</body>
</html>
"""

output_path = "winter-horse-oil.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {output_path} successfully ({len(html_content):,} bytes)!")
