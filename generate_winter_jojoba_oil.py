import json
import re

with open("fetched_3new_nov_dec_shea_jojoba_urea_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_jojoba_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 累計販売数トップの国民的ピュアオイル！ポンプ式で全身に惜しみなく使える最高傑作",
        "catch": "無印良品が誇るベストセラースキンケア。植物由来100%の軽やかな使い心地で冬の肌を柔らかく包む",
        "brand_name": "無印良品 (MUJI)",
        "capacity": "200ml (ホホバオイル)",
        "type": "精製ピュアホホバオイル・無香料・無着色",
        "features": "ホホバ種子油100%、精製脱色・脱臭処方、使いやすい大容量ポンプボトル、アレルギーテスト済み",
        "value": "日本のスキンケア界でホホバオイルの認知度を一気に高めた殿堂入りアイテム。大容量200mlで顔から髪・ボディまで全身を贅沢にうるおす",
        "desc_p1": "11月から12月にかけて湿度が急落し、皮脂分泌が夏の3分の1以下まで激減する真冬の肌。乾燥によって角質が硬くなり、化粧水が弾かれて浸透しにくくなる『冬のインナードライ』に悩む方に、まず手にとってほしいのが無印良品のホホバオイルです。",
        "desc_p2": "ホホバの種子から搾った油を国内で丁寧に精製し、サラリとした肌なじみの良いテクスチャーに仕上げています。オイル特有の重さやベタつきがほとんどなく、肌に乗せた瞬間にスッと吸い込まれるように角層へ浸透。化粧水前のブースター（導入液）として使えば、硬くなった角質が瞬時にほぐれ、後から重ねる化粧水の引き込み力が劇的に向上します。片手で手軽にプッシュできるポンプ式ノズルも、冬の忙しい毎日に嬉しい設計です。",
        "target": "オイルのベタつきが苦手な方、洗顔後の導入液（ブースター）として使いたい方、大容量で惜しみなく全身に使い倒したい方",
        "point": "洗顔後、タオルドライした直後の肌にわずか1プッシュを全顔になじませてから化粧水を重ねてください。水分と油分が乳化し、吸い付くようなモチモチ肌が完成します。"
    },
    {
        "rank": 2,
        "tag": "🥇 アルゼンチン産OIA認定オーガニック！黄金色の一番搾り未精製プレミアムホホバ",
        "catch": "世界基準の最高品質。熱を加えず低温圧搾で抽出したビタミン・アミノ酸・ミネラルが息づく最高峰",
        "brand_name": "INCA OIL (インカオイル)",
        "capacity": "120ml (オーガニック ホホバオイル ゴールド)",
        "type": "OIA認定・未精製ゴールデンホホバオイル",
        "features": "アルゼンチン産有機栽培ホホバ種子油100%、コールドプレス（低温圧搾）製法、未脱色・未脱臭、OIAオーガニック認証",
        "value": "エステサロンや高級スパでプロフェッショナルが指名買いする本物のゴールデンホホバ。天然のカロテノイドやビタミンEが冬のエイジング肌に活力を注入",
        "desc_p1": "南米アルゼンチンの肥沃な大地で有機栽培されたホホバの実だけを厳選し、昔ながらのコールドプレス製法で丁寧に搾油されたインカオイルのオーガニックホホバ。美容のプロフェッショナルたちが『ホホバオイルの最高峰』と称賛を惜しまない名品です。",
        "desc_p2": "精製処理を一切行わないため、黄金色に輝くオイルの中には、抗酸化ビタミンEや各種ミネラル、肌のハリを支えるアミノ酸がそのまま凝縮されています。肌に乗せると、ナッツを思わせるほのかな自然の香りが広がり、こっくりとした濃密なヴェールが真冬の冷風から肌細胞を保護。頭皮マッサージに使用すれば、毛穴に固まった酸化皮脂を浮かせつつ、冬のフケ・かゆみを防いで健やかな美髪の土台を整えます。",
        "target": "本物の未精製オーガニック品質を求める方、冬の乾燥小ジワやハリ不足が気になるエイジングケア世代、サロン品質の頭皮クレンジングをしたい方",
        "point": "週に1回、シャンプー前の乾いた頭皮に500円玉大を馴染ませて指の腹でマッサージ。その後蒸しタオルで5分蒸らしてから洗髪すると、頭皮がふっくら軽やかに蘇ります。"
    },
    {
        "rank": 3,
        "tag": "🌿 フランスECOCERT認証取得！安心と安全を極めた純度100%ゴールデンオイル",
        "catch": "東京・檜原村のヘッドスパ発。徹底した品質管理で届ける無添加・未精製ピュアゴールド",
        "brand_name": "spa hinoki (スパヒノキ)",
        "capacity": "100ml (オーガニック ホホバオイル)",
        "type": "ECOCERT認証・未精製オーガニックホホバオイル",
        "features": "有機栽培ホホバ種子油、エコサート認証、コールドプレス一番搾り、遮光ボトル採用",
        "value": "第三者機関の厳格なオーガニック基準をクリア。紫外線からオイルの品質を守る遮光瓶入りで、搾りたてのフレッシュな美容成分を最後の一滴まで保持",
        "desc_p1": "豊かな自然に囲まれた東京・檜原村のサロン発祥ブランド『spa hinoki』。徹底的に原料のトレーサビリティにこだわり、世界最大の有機認証機関ECOCERTの認証を正式に取得した信頼のゴールデンホホバオイルです。",
        "desc_p2": "未精製ならではの美しい黄金色と、肌への心地よいなじみの良さが特徴。皮脂の構成成分であるワックスエステルが豊富に含まれているため、肌のバリア機能が低下しやすい真冬の敏感肌にも刺激なく溶け込みます。品質劣化を防ぐ遮光ボトルを採用しているため、デリケートな天然ビタミンが酸化せず、常に最高鮮度の状態で肌をケアできます。",
        "target": "厳格なオーガニック認証にこだわる方、酸化に強い高品質なオイルを長く大切に使いたい方、季節の変わり目に肌がゆらぎやすい敏感肌の方",
        "point": "夜のお手入れの最後に、手のひらで温めたオイル2〜3滴を顔全体に優しく密着させてください。翌朝の洗顔後も内側からのふっくら感が長時間持続します。"
    },
    {
        "rank": 4,
        "tag": "🏺 サロン業務用を直販！プロが絶賛する鮮度と浸透力を誇る低温圧搾ゴールデン",
        "catch": "マカダミ屋のこだわり品質。中間マージンをカットした鮮度抜群の純度100%植物性ワックス",
        "brand_name": "マカダミ屋 (Macadamia-ya)",
        "capacity": "80ml (未精製 ゴールデンホホバオイル)",
        "type": "未精製・天然無添加・コールドプレスホホバオイル",
        "features": "未精製ホホバ種子油100%、低温圧搾抽出、アルミパウチ/遮光容器、国内充填・品質検査済み",
        "value": "エステやアロママッサージの現場で使われるプロ仕様のキャリアオイル。新鮮な状態で小分け充填され、滑らかな伸びと抜群の保湿シールド力を発揮",
        "desc_p1": "全国のエステサロンやリラクゼーション施設に植物油を供給するオイル専門ブランド『マカダミ屋』。プロが施術で使用する高鮮度の未精製ゴールデンホホバを、個人向けに使いやすいサイズで展開しています。",
        "desc_p2": "一番搾りのゴールデンホホバのみを使用し、熱を加えないコールドプレスで抽出。ワックスエステル特有の浸透力とエモリエント効果が際立っており、カサカサに乾いたひじや膝、かかとの角質にしっとり馴染んで柔らかく解きほぐします。ボディマッサージ用としても滑りが非常に良く、真冬の血行不良による冷えやむくみケアにも最適です。",
        "target": "プロ仕様の高品質オイルを手頃な価格で試したい方、お風呂上がりのボディマッサージを日課にしたい方、角質のゴワつきを柔らかくしたい方",
        "point": "入浴後、肌にまだ水滴が少し残っている状態で全身に滑らせるようにマッサージ。水とオイルが混ざり合い、ベタつきのない極上のシルク肌へと整います。"
    },
    {
        "rank": 5,
        "tag": "🌲 アロマテラピーの世界的権威！徹底した有機栽培で育てられたプレミアムゴールド",
        "catch": "生活の木が厳選する確かな原料。肌本来の自活力を高めるリッチな未精製ホホバオイル",
        "brand_name": "生活の木 (Tree of life)",
        "capacity": "100ml (ホホバオイル・ゴールデン)",
        "type": "有機栽培・未精製ゴールデンホホバオイル",
        "features": "イスラエル・エジプト産有機ホホバ種子油、生活の木厳格基準クリア、低温圧搾法、ドロッパー付きボトル",
        "value": "ハーブとアロマのパイオニアが届ける最高品質。オーガニック農場で大切に育てられたホホバの栄養を余すところなく肌へ届ける贅沢な1本",
        "desc_p1": "長年日本のオーガニックコスメとアロマテラピー文化を牽引してきた『生活の木』。そのホホバオイル・ゴールデンは、世界中の産地から厳選した最高グレードの有機栽培ホホバ種子のみを使用しています。",
        "desc_p2": "砂漠の過酷な気候に耐え抜いたホホバの生命力が凝縮された濃厚な黄金色。肌に塗布するとすばやく馴染んで薄い保護膜を作り、冬の乾燥による小ジワを目立たなく整えます。生活の木ならではのドロッパー付き容器は、1滴ずつ正確に計量できるため、手持ちのクリームや乳液に1滴混ぜて保湿力をブーストさせる使い方も非常にスマートに行えます。",
        "target": "信頼できる有名ブランドのオーガニックコスメを選びたい方、手持ちのスキンケアアイテムにブレンドして保湿力を強化したい方",
        "point": "普段使っている冬用乳液やクリームに、このゴールデンホホバを1滴だけ垂らして混ぜ合わせてから塗布。即席のリッチ保湿クリームにグレードアップします。"
    },
    {
        "rank": 6,
        "tag": "💼 旅行やジム・オフィス置きに最適！無印良品の使い勝手抜群な中容量ボトル",
        "catch": "使い切りやすい100mlサイズ。酸化知らずのフレッシュな状態で冬の間フル稼働",
        "brand_name": "無印良品 (MUJI)",
        "capacity": "100ml (ホホバオイル)",
        "type": "精製ピュアホホバオイル・携帯＆使い切りサイズ",
        "features": "ホホバ種子油100%、精製無臭タイプ、ワンタッチキャップ、旅行・持ち運び対応",
        "value": "1シーズンでちょうど使い切れるベストな容量。無印良品ならではの無駄のないシンプルなボトルで、ポーチやデスクの引き出しにもスマートに常備可能",
        "desc_p1": "『オイルは大容量だと酸化や使い切れなさが心配』という方に最も選ばれているのが、無印良品の100mlボトルです。冬の約2〜3ヶ月間の集中ケアにちょうど良いサイズ感で、常に新鮮な状態で使い切ることができます。",
        "desc_p2": "200mlと同様に極めて高度に精製されたピュアオイルで、においやベタつきが一切ありません。オフィスの暖房で午後から目元や口元が乾いて突っ張る際、指先に1滴取ってトントンとなじませるだけで、メイクを崩さず自然なツヤと潤いをリチャージ。冬の出張や年末年始の帰省にもかさばらずに連れて行ける万能選手です。",
        "target": "オイル初心者で少量から試してみたい方、日中のオフィス乾燥対策としてデスクに置きたい方、旅行や帰省用のコスメを探している方",
        "point": "午後のメイク直しの際、綿棒の先に1滴染み込ませてヨレたアイメイクや乾燥した口角を優しく拭き取ると、綺麗に修正しつつ即座に保湿できます。"
    },
    {
        "rank": 7,
        "tag": "🇺🇸 米国サプリ大手が誇る大人気ピュアオイル！高品質×お値打ち価格のアメリカンベストセラー",
        "catch": "NOW Foodsのモイスチャライジングオイル。100%ピュアな潤いで冬の乾燥肌をマルチに救済",
        "brand_name": "NOW Foods (ナウフーズ)",
        "capacity": "118ml (100% ピュア モイスチャライジング ホホバオイル)",
        "type": "輸入ピュアホホバオイル・万能モイスチャライザー",
        "features": "ピュアホホバ種子油100%、ヘキサンフリー抽出、遺伝子組み換え不使用、UV保護ボトル",
        "value": "世界中のヘビーユーザーから支持される高コスパ。高品質な植物性ワックスエステルを手軽な価格で毎日のスキンケア・ボディケアに取り入れられる",
        "desc_p1": "世界的なウェルネスブランドとして名高いアメリカのナウフーズ。そのスキンケア部門で常にトップクラスの販売実績を誇るのが、この100%ピュアモイスチャライジングホホバオイルです。",
        "desc_p2": "低温圧搾技術によって抽出され、肌の毛穴を詰まらせないノンコメドジェニックな性質を持ちます。シャンプー後の濡れた髪に数滴なじませてからドライヤーで乾かせば、冬特有のパサつきや静電気をしっかり防止し、毛先までまとまりのある艶髪へ。手肌や爪の甘皮ケア、シェービング時の肌保護としても万能に使える実力派です。",
        "target": "コストパフォーマンスを最重視する方、ヘアケア（アウトバストリートメント）としても使いたい方、海外コスメの実力を試したい方",
        "point": "お風呂上がりのタオルドライした濡れた髪の毛先に2〜3滴をなじませてからブロー。冬の熱風ダメージを防ぎ、サロン帰りのようなツヤが宿ります。"
    },
    {
        "rank": 8,
        "tag": "🔬 敏感肌のための究極精製！サラサラの極上テクスチャーで肌刺激を極限まで低減",
        "catch": "自然化粧品研究所のプロ仕様。不純物を極限まで取り除いたピュアクリアホホバオイル",
        "brand_name": "自然化粧品研究所",
        "capacity": "100ml (精製ホホバオイル)",
        "type": "高純度精製ホホバオイル・超低刺激クリアタイプ",
        "features": "精製ホホバ種子油100%、無色・無臭、酸価・過酸化物価極小、手作り化粧品原料対応",
        "value": "化粧品原料メーカーならではの徹底した精製技術。未精製オイルに含まれる微量アレルゲン成分を完全に除去し、赤みが出やすい超敏感肌でも安心して使用可能",
        "desc_p1": "『オイルを使うと肌が赤くなりやすい』『未精製の植物成分にアレルギーを起こしたことがある』というデリケート肌の方に向けて開発された、原料メーカー基準の超高純度精製ホホバオイルです。",
        "desc_p2": "水のように透明で、オイルとは思えないほどサラッとした極上のテクスチャー。肌に乗せると皮脂膜の一部のように素早くなじみ、油膜感を残さずサラサラの感触を保ちながら角層の水分を守り抜きます。香りが全くないため、香料が苦手な方や、他のスキンケアアイテムの香りを邪魔したくない方にも最適です。",
        "target": "超敏感肌で肌トラブルを起こしやすい方、オイル特有の重さや香りが苦手な方、自作の美容オイルのベースとして使いたい方",
        "point": "洗顔直後の素肌に数滴馴染ませることで、寒さで硬直した角質層を刺激なく柔らかくほぐし、その後のスキンケア全体の浸透力を高めます。"
    },
    {
        "rank": 9,
        "tag": "🧪 高濃度スキンケアのKISOが放つ！オーガニック低温圧搾のフレッシュゴールデン",
        "catch": "基礎化粧品研究所の皮膚科学アプローチ。天然の栄養素を壊さず搾油したピュア美容オイル",
        "brand_name": "KISO (キソ)",
        "capacity": "50ml (オーガニック ゴールデン ホホバオイル)",
        "type": "有機認証・低温圧搾未精製ホホバオイル",
        "features": "未精製ゴールデンホホバ油、コールドプレス製法、スポイト式遮光瓶、国内充填・品質管理",
        "value": "成分重視のスキンケアマニアから熱烈な支持を集めるKISO。スポイト式ボトルを採用し、1滴単位で衛生的に肌へ届けるプレミアム仕様",
        "desc_p1": "高濃度原液スキンケアで知られる国内実力派ブランド『KISO』が手がけるオーガニックゴールデンホホバオイル。原材料の選定から圧搾、国内での充填・検品まで一貫して厳しい基準で管理されています。",
        "desc_p2": "鮮やかな黄金色は、天然のカロテノイドやビタミンEが熱破壊されずに残っている証拠。スポイト式容器を採用しているため、空気に触れにくく衛生的に1滴ずつ調整できます。冬の毛穴の黒ずみや角栓が気になる場合、ホホバオイルで優しくクルクルとマッサージすることで、固まった角栓を溶かし出しながら潤いをチャージできます。",
        "target": "スポイト式で衛生的に使いたい方、冬の毛穴の黒ずみ・角栓の詰まりをケアしたい方、成分重視のスキンケアを好む方",
        "point": "入浴時、湯船に浸かりながら小鼻の周りにホホバオイルを馴染ませて優しく指の腹でくるくるマッサージ。毛穴の奥の角栓がポロポロと浮き上がります。"
    },
    {
        "rank": 10,
        "tag": "🌱 アロマセラピーのベースオイルに最適！自然そのままの生命力を宿す未精製ゴールド",
        "catch": "イーズアロマのオーガニックホホバ。豊かなエモリエント効果で真冬の肌を柔らかく整える",
        "brand_name": "ease aroma (イーズアロマ)",
        "capacity": "100ml (未精製 ホホバオイル)",
        "type": "未精製キャリアオイル・アロマセラピー仕様",
        "features": "未精製ゴールデンホホバ油100%、低温圧搾、アロマブレンド対応、高品質エコ容器",
        "value": "アロマ専門店が厳選した未精製ホホバ。精油を希釈するキャリアオイルとしてはもちろん、単体でも極めて高い保湿力と肌の柔軟化効果を発揮",
        "desc_p1": "アロマセラピー専門ショップ『ease aroma』が直輸入する未精製ホホバオイル。サロンでのトリートメント用として厳選された上質なゴールデンホホバは、一般ユーザーからも高い評価を獲得しています。",
        "desc_p2": "自然の恵みをそのまま閉じ込めた未精製オイルは、ワックスエステルの密度が高く、真冬の粉吹き肌やひび割れやすいかかと・ひじに抜群の密着力を発揮します。お好みの精油（ラベンダーやフランキンセンス等）を数滴垂らして混ぜれば、自分だけの至高の冬用アロママッサージオイルが簡単に完成します。",
        "target": "アロマオイルとブレンドしてオリジナルの冬オイルを作りたい方、ひじやかかとの頑固な乾燥をケアしたい方",
        "point": "ホホバオイル10mlにお好みの精油を1〜2滴ブレンド。お風呂上がりのデコルテや肩に優しく塗り広げると、芳醇な香りと高い保湿力で極上のリラックスタイムが訪れます。"
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
    "headline": "保湿力の強さで肌乾燥とさようなら！皮脂膜を補い真冬の肌を柔らかく包む高保湿ホホバオイルランク10",
    "description": "11月・12月の冬本番に急減する皮脂膜を補修！人間の皮脂と同じ『ワックスエステル』を豊富に含む高保湿ホホバオイル10選を徹底比較！無印良品、インカオイル、spa hinoki、生活の木、KISOなど、未精製ゴールデンから高純度精製クリアまで、ブースター・頭皮・クレンジング・全身保湿を叶える名品を厳選。",
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
    "name": "冬の高保湿ホホバオイル おすすめランキング10選",
    "itemListElement": item_list_elements
}

# HTML Generation
html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！皮脂膜を補い真冬の肌を柔らかく包む高保湿ホホバオイルランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬本番に急減する皮脂膜を補修！人間の皮脂と同じ『ワックスエステル』を豊富に含む高保湿ホホバオイル10選を徹底比較！無印良品、インカオイル、spa hinoki、生活の木、KISOなど、未精製ゴールデンから高純度精製クリアまで、ブースター・頭皮・クレンジング・全身保湿を叶える名品を厳選。">
  <meta name="keywords" content="ホホバオイル,ゴールデンホホバ,冬 保湿オイル,無印良品 ホホバオイル,インカオイル,ワックスエステル,ブースターオイル,頭皮クレンジング,おすすめ 2026">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-jojoba-oil">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！皮脂膜を補い真冬の肌を柔らかく包む高保湿ホホバオイルランク10">
  <meta property="og:description" content="11月・12月の皮脂枯れ肌を救う！人間の皮脂成分ワックスエステルを補給する高保湿ホホバオイル10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-jojoba-oil">
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
      --primary: #c9933b;
      --primary-dark: #8c6116;
      --primary-light: #fdf6e7;
      --accent: #e5a93c;
      --text: #2a2621;
      --text-sub: #665f54;
      --bg: #fdfbf7;
      --card-bg: #ffffff;
      --border: #f0e1c8;
      --shadow: 0 4px 20px rgba(140, 97, 22, 0.08);
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
      background: #fdfaf2;
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
      background: #fdfaf2;
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
      background: #fdfaf2;
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
      background: #e5a93c;
    }}
    .ranking-card:nth-child(2) .rank-number {{
      background: #c9933b;
    }}
    .ranking-card:nth-child(3) .rank-number {{
      background: #a97722;
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
      background: #fdfaf2;
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
      background: #fffdf5;
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
      background: #fdfaf2;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px 16px;
      text-decoration: none;
      color: var(--text);
      transition: all 0.2s;
    }}
    .internal-card:hover {{
      border-color: var(--primary);
      background: #fbf2dc;
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
      <li><a href="/winter-shea-butter">シアバター</a></li>
      <li><a href="/winter-squalane-oil">スクワランオイル</a></li>
      <li><a href="/winter-ceramide-lotion">セラミド化粧水</a></li>
    </ul>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">TOP</a> &gt; <a href="/winter-face-oil">冬の美容オイル特集</a> &gt; <span>高保湿ホホバオイル</span>
</div>

<main class="container">
  <article>
    <header class="article-header">
      <span class="badge">2026年冬 最新決定版 / 11〜12月集中皮脂ケア</span>
      <h1>保湿力の強さで肌乾燥とさようなら！皮脂膜を補い真冬の肌を柔らかく包む高保湿ホホバオイルランク10</h1>
      <div class="meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証機関: 冬コスメ徹底比較ラボ 編集部</span>
        <span>対象: 皮脂枯れ・インナードライ・ゴワつき砂漠肌</span>
      </div>
      <div class="lead-box">
        <p><strong>「洗顔後すぐに肌がつっぱる」「化粧水が肌表面で浮いてしまい、角層の奥まで入っていかない……」</strong></p>
        <p>11月から12月は、気温低下に伴って皮脂腺の活動が鈍り、肌表面を守る「皮脂分泌量」が年間で最も激減する季節です。皮脂膜を失った素肌は無防備となり、角質が硬く硬化して化粧水を弾く『ゴワつき砂漠化』を起こします。</p>
        <p>この冬の皮脂不足を解消する最も理にかなった特効薬が、植物界で唯一人間の皮脂成分と同じ<strong>「ワックスエステル」</strong>を豊富に含有する<strong>高保湿ホホバオイル</strong>です。皮膚に馴染みやすく、ブースター（導入液）として使えば硬くなった肌を瞬時に柔らかくほぐし、化粧水の浸透を劇的にサポートします。本記事では、楽天APIから都度取得した最新データに基づき、黄金色の未精製ゴールデンから高純度精製クリアまで、真冬に選ぶべき高保湿ホホバオイル10選を徹底比較します。</p>
      </div>
    </header>

    <!-- 科学的背景・解説セクション -->
    <section class="content-section">
      <h2>🧬 なぜホホバオイルは「肌なじみNo.1」と呼ばれるのか？</h2>
      <p>ホホバオイルは「オイル」と呼ばれていますが、化学的には油脂（トリグリセリド）ではなく、高級脂肪酸と高級アルコールが結合した<strong>『液状植物性ワックスエステル』</strong>に分類されます。この特殊な構造こそが、他の植物オイルにはない驚異的な美肌効果を生み出しています。</p>
      
      <div class="feature-grid">
        <div class="feature-card">
          <h4>1. 人間の皮脂の20〜30%を占める成分</h4>
          <p>私たちの健康な皮膚を守る皮脂膜の約20〜30%はワックスエステルで構成されています。ホホバオイルはこの成分を植物界で唯一大量に含むため、肌が「自分自身の皮脂」と錯覚するほど親和性が高く、スーッと吸い込まれます。</p>
        </div>
        <div class="feature-card">
          <h4>2. 驚異的な酸化安定性と耐熱性</h4>
          <p>通常の植物油は空気中の酸素や熱によって徐々に酸化（過酸化脂質化）しますが、ホホバのワックスエステルは極めて酸化しにくく、数年放置しても品質がほぼ劣化しません。冬場に長く安心して使えます。</p>
        </div>
        <div class="feature-card">
          <h4>3. 角質を柔らかくほぐすブースター機能</h4>
          <p>寒さで硬直した角質層の細胞間脂質にすばやく入り込み、細胞同士の結合を柔軟にほぐします。洗顔後すぐに塗布することで、後から使う化粧水や美容液の通り道を整えます。</p>
        </div>
        <div class="feature-card">
          <h4>4. ノンコメドジェニック＆毛穴クレンジング</h4>
          <p>毛穴を塞ぎにくい特性があり、アクネ菌のエサになりにくい油分です。さらに、冬の冷気で固まった毛穴の角栓や酸化皮脂を溶かし出すディープクレンジングとしても極めて優秀です。</p>
        </div>
      </div>

      <h3>✨ 「ゴールデン（未精製）」と「クリア（精製）」の選び分け</h3>
      <p>ホホバオイルには、美しい黄金色の「ゴールデン（未精製）」と、透明な「クリア（精製）」の2種類が存在します。</p>
      <ul style="padding-left: 20px; margin-bottom: 16px; font-size: 0.95rem;">
        <li style="margin-bottom: 8px;"><strong>ゴールデンホホバ（未精製）：</strong>ホホバの種子を低温圧搾（コールドプレス）し、化学的処理を行わず抽出したオイル。ビタミンA・D・E、アミノ酸、ミネラルが丸ごと残っており、冬のエイジングケアや濃密な栄養補給を求める方に最適です。</li>
        <li><strong>クリアホホバ（精製）：</strong>未精製オイルから加熱・蒸留等の精製技術で色と香りをカットしたオイル。テクスチャーがよりサラサラでベタつかず、アレルギー反応のリスクが極めて低いため、超敏感肌の方や化粧水前のブースターにぴったりです。</li>
      </ul>
    </section>

    <!-- ランキング一覧 -->
    <section>
      <h2 style="font-size: 1.5rem; color: var(--primary-dark); margin: 36px 0 24px; text-align: center;">
        🏆 冬の高保湿ホホバオイル おすすめランキング10選
      </h2>
"""

# ランキングカード
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
              <div class="spec-item"><span class="spec-label">商品タイプ:</span> {p['type']}</div>
              <div class="spec-item"><span class="spec-label">抽出・処方:</span> {p['features']}</div>
              <div class="spec-item"><span class="spec-label">独自価値:</span> {p['value']}</div>
            </div>

            <div class="product-desc">
              <p>{p['desc_p1']}</p>
              <p>{p['desc_p2']}</p>
            </div>

            <div class="user-point">
              <strong>🎯 こんな方・シーンに最適:</strong> {p['target']}
            </div>

            <div class="user-point" style="background: #fbf5e6; border-left-color: var(--primary);">
              <strong>✨ プロ直伝・冬の使い方のコツ:</strong> {p['point']}
            </div>
          </div>
        </div>
      </article>
"""

html_content += f"""
    </section>

    <!-- スペック徹底比較表 -->
    <section class="content-section">
      <h2>📊 高保湿ホホバオイル10選 スペック徹底比較一覧表</h2>
      <p>各ホホバオイルの精製タイプ、容量、楽天参考価格、推奨される使い道を分かりやすくまとめました。</p>
      
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位・ブランド</th>
              <th>精製タイプ</th>
              <th>内容量</th>
              <th>楽天参考価格</th>
              <th>特徴・用途</th>
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

    <!-- 冬の効果的活用術ステップ -->
    <section class="content-section">
      <h2>❄️ 真冬の肌をモチモチに変える！ホホバオイルの3大活用術</h2>
      <p>ホホバオイルは単なる『乳液代わりのフタ』にとどまらず、スキンケアのあらゆる工程で効果を発揮します。冬の美肌を作る代表的な活用法を解説します。</p>

      <div class="step-box">
        <div class="step-num">1</div>
        <div class="step-text">
          <h4>【ブースター導入】洗顔後すぐの1滴で化粧水をぐんぐん引き込む</h4>
          <p>洗顔後、タオルドライした直後の肌にホホバオイルを1〜2滴なじませます。硬くなった角質がほぐれ、後から使う化粧水の浸透ルートが開かれます。化粧水を重ねると肌の上でみずみずしく乳化し、内側から押し返すような弾力が生まれます。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">2</div>
        <div class="step-text">
          <h4>【毛穴＆頭皮クレンジング】入浴中のオイルパックで角栓オフ</h4>
          <p>湯船に浸かりながら、小鼻やTゾーン、頭皮にホホバオイルを塗布して優しくマッサージ。体温と蒸気で毛穴が開き、冬の寒さで固まった古い皮脂や角栓が負担なく溶け出します。その後洗顔・シャンプーをすれば、すっきりつるんとした素肌と頭皮に。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">3</div>
        <div class="step-text">
          <h4>【アウトバスヘアケア】ドライヤーの熱ダメージと静電気を遮断</h4>
          <p>お風呂上がりにタオルドライした毛先に1〜2滴揉み込んでからブロー。ワックスエステルが髪のキューティクルを均一にコーティングし、冬の乾燥による静電気のパチパチや枝毛・パサつきを一日中ブロックします。</p>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="content-section">
      <h2>❓ 高保湿ホホバオイルに関するよくある質問（FAQ）</h2>
      
      <div class="faq-item">
        <div class="faq-q">Q1. ホホバオイルとスクワランオイルはどう違いますか？どちらが冬に向いていますか？</div>
        <div class="faq-a">
          スクワランオイルは人間の皮脂膜の「スクワレン（炭化水素）」を補うもので、粒子が極めて細かくサラサラした浸透感が特徴です。一方、ホホバオイルは皮脂膜の約20〜30%を占める「ワックスエステル」であり、角質を柔軟にほぐすブースター効果や頭皮クレンジング、ヘアケアまでマルチにこなします。真冬の「肌のゴワつきや化粧水の弾き」に悩む方はホホバオイル、「軽やかなツヤ膜でフタをしたい」方はスクワランオイルがおすすめです。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q2. 冬になるとホホバオイルが白く固まることがありますが、品質に問題はありませんか？</div>
        <div class="faq-a">
          全く問題ありません。ホホバオイルは純度が高いワックスエステルであるため、約7〜10℃以下になると自然に白く結晶化して固まります。これは添加物のないピュアな証拠です。暖かい部屋に置くか、容器ごとぬるま湯につければ元通りの透明な液体に戻り、成分や品質は一切劣化しません。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q3. 日中にホホバオイルを塗ると「油焼け」を起こしませんか？</div>
        <div class="faq-a">
          油焼けは、不純物や酸化しやすい油脂（不飽和脂肪酸）が紫外線によって変質することで起こります。ホホバオイルは酸化安定性が極めて高く、紫外線に当たっても変質しないため、朝のメイク前や日中の外出時に使用しても油焼けの心配は一切ありません。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q4. オイルクレンジングとしてメイク落としにも使えますか？</div>
        <div class="faq-a">
          はい、極めて贅沢なクレンジングとして活用できます。乾いた肌に500円玉大を優しくなじませると、ファンデーションや皮脂汚れが浮き上がります。市販のクレンジングと違って界面活性剤を含まないため、ティッシュで優しく押さえてからぬるま湯で洗顔石鹸を泡立てて落としてください。肌の潤いを奪わずにメイクオフできます。
        </div>
      </div>
    </section>

    <!-- 内部リンク -->
    <section class="content-section">
      <h2>🔗 あわせて読みたい！冬の乾燥対策おすすめ関連記事</h2>
      <p>冬のスキンケアは、肌質や部位に合わせた最適な油分と水分のチャージが鍵を握ります。あわせて読みたい人気記事はこちらです。</p>
      
      <div class="internal-link-grid">
        <a href="/winter-shea-butter" class="internal-card">
          <h5>高保湿シアバターランク10</h5>
          <p>天然の濃厚ベールで顔・唇・全身を密封保護するオーガニックバーム特集。</p>
        </a>
        <a href="/winter-squalane-oil" class="internal-card">
          <h5>高純度スクワランオイルランク10</h5>
          <p>たった1滴で極上のツヤ膜を形成するピュアオイル比較。</p>
        </a>
        <a href="/winter-urea-cream" class="internal-card">
          <h5>高保湿尿素クリームランク10</h5>
          <p>ガサガサかかと・ひじの硬化角質を柔らかくほぐす集中補修クリーム。</p>
        </a>
        <a href="/winter-ceramide-lotion" class="internal-card">
          <h5>高保湿セラミド化粧水ランク10</h5>
          <p>角層のバリアを整え深層から潤す、冬の最強化粧水特集。</p>
        </a>
        <a href="/winter-face-oil" class="internal-card">
          <h5>冬の美容オイルおすすめ総合</h5>
          <p>乾燥知らずのツヤ肌を作る、冬のフェイスオイル徹底ガイド。</p>
        </a>
        <a href="/winter-booster-oil" class="internal-card">
          <h5>冬の導入・ブースターオイル特集</h5>
          <p>ゴワつく砂漠肌を即ほぐす、化粧水前の浸透促進オイル名作集。</p>
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

with open("winter-jojoba-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-jojoba-oil.html")
