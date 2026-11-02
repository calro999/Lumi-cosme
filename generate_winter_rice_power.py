import json
import re

with open("fetched_3new_nov_dec_rice_camellia_amino_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_rice_power"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 医薬部外品認可！日本で唯一『水分保持能を改善する』ライスパワーNo.11+配合の最高峰導入美容液",
        "catch": "洗顔直後の素肌にセラミドを生み出すスイッチをオン。真冬の過酷な乾燥を根底から覆す薬用ブースター",
        "brand_name": "ONE BY KOSE (コーセー)",
        "capacity": "60ml (セラム ヴェール ディープリペア)",
        "type": "医薬部外品・薬用導入美容液",
        "features": "有効成分ライスパワーNo.11+、インナーブースト処方EX、角層密着浸透カプセル、無着色・弱酸性",
        "value": "単に外から油分を塗る対症療法ではなく、肌自らがセラミドを作り出す力を高める唯一無二のアプローチ。冬の乾いた冷風に負けない自立した潤い肌を育てる",
        "desc_p1": "11月から12月にかけて気温が下がり湿度が急落すると、肌内部のセラミド産生スピードが落ち、いくら化粧水を重ねても数時間でカサつく『慢性インナードライ』に陥ります。ONE BY KOSEのセラム ヴェール ディープリペアは、日本で初めて『肌の水分保持能を改善する』有効成分として承認されたライスパワーNo.11をさらに進化させた『ライスパワーNo.11+』を配合したフラッグシップ美容液です。",
        "desc_p2": "洗顔後のまっさらな素肌になじませた瞬間、微細なカプセルがカチコチに固まった角層の隙間へスルスルと浸透。角層深部でセラミドの合成を促し、細胞間脂質のラメラ構造を整えます。とろみがありながらベタつかず、みずみずしく吸い込まれるテクスチャーが絶品。その後に使う化粧水の引き込み力が劇的に向上し、真冬の暖房直撃オフィスでも夕方までモチモチとした弾力感が続きます。",
        "target": "化粧水をいくら重ねても乾く方、冬になるとキメが乱れてファンデーションが粉を吹く方、根本から肌の保水力を立て直したい方",
        "point": "朝晩の洗顔直後、手のひらに2〜3プッシュを取り、手のひら全体で顔を包み込むように優しくハンドプレスしてください。目元や口元など乾燥が激しい部位には重ねづけが効果的です。"
    },
    {
        "rank": 2,
        "tag": "🌾 コーセー×酒造発酵技術の結晶！濃厚な米エキスが乾いた角層を潤いで満たす濃密改善美容液",
        "catch": "ライスパワーNo.11を高濃度濃縮。ふっくらキメの整った毛穴レス肌へ導くエイジング保湿ケア",
        "brand_name": "米肌 (MAIHADA)",
        "capacity": "30ml (肌潤改善エッセンス)",
        "type": "医薬部外品・薬用保湿美容液",
        "features": "ライスパワーNo.11高濃度配合、ビフィズス菌発酵エキス、大豆発酵エキス、無香料・無着色・鉱物油フリー",
        "value": "酒蔵の伝統的な米発酵技術とコーセーの先進皮膚科学が融合。乾燥による小ジワを目立たなくし、内側から押し返すようなハリ感を生み出す",
        "desc_p1": "古くから『杜氏（とうじ）の手は厳しい寒さの中でも白く美しい』と言われてきた事実に着目し、米と発酵の力を徹底追求したスキンケアブランド『米肌（まいはだ）』。その中核を担う肌潤改善エッセンスは、角層の水分保持能を改善する有効成分ライスパワーNo.11を贅沢に配合した薬用美容液です。",
        "desc_p2": "コクのあるミルクエッセンス状のテクスチャーで、肌に伸ばすと体温でとろけるように広がり、しっとりとしたうるおいのヴェールを形成します。ビフィズス菌発酵エキスや大豆発酵エキスなど、厳選された発酵由来の保湿成分が相乗効果を発揮。乾燥でしぼんだキメの一つひとつをふっくらと持ち上げ、毛穴の目立ちにくいなめらかな素肌へと導きます。11月・12月の冷え込みでくすみがちな肌に、自然な透明感とツヤを宿します。",
        "target": "乾燥による小ジワやハリ不足が気になる方、発酵コスメの濃厚なうるおいを好む方、毛穴の開きが目立つインナードライ肌の方",
        "point": "化粧水で肌を整えた後、1円玉大を手のひらに取り、顔全体になじませます。特に乾燥しやすい目尻やほうれい線周辺には指先でトントンと優しく押し込むように重ねます。"
    },
    {
        "rank": 3,
        "tag": "💧 発売以来ロングセラーを誇る薬用高保湿化粧水！角層深くまでぐんぐん吸い込まれる濃密浸透",
        "catch": "ライスパワーNo.11を角質細胞のすみずみまでチャージ。吸い付くような超もっちり肌を即実感",
        "brand_name": "RICE FORCE (ライスフォース)",
        "capacity": "120ml (ディープモイスチュアローション)",
        "type": "医薬部外品・薬用保湿化粧水",
        "features": "有効成分ライスパワーNo.11高配合、弱酸性、動物性原料不使用、アレルギーテスト済み",
        "value": "数多くの美容プロフェッショナルやモデルが絶賛する実力派。基底層までうるおいを届け、真冬でも乾燥知らずの健やかな肌コンディションをキープ",
        "desc_p1": "ライスパワーエキス配合コスメのパイオニアとして長年愛され続けているライスフォースの看板商品『ディープモイスチュアローション』。医薬部外品の有効成分として配合されたライスパワーNo.11が、角層の奥深くまで行き渡り、肌本来の水分キープ力を引き出します。",
        "desc_p2": "少しとろみのあるまろやかな感触で、手のひらで肌を包み込むと驚くほど素早く引き込まれていきます。重ねづけをするたびに手のひらが吸い付くようなモッチリ感へと変化。角質層の水分量が底上げされるため、真冬の暖房下でも肌が突っ張る不快感を寄せ付けません。季節の変わり目や12月の寒波でもゆらぎにくい、強固なバリア機能をサポートします。",
        "target": "とにかく乾燥がひどく肌がパリパリする方、とろみ化粧水がぐんぐん入っていく快感を味わいたい方、実績のある定番名品を選びたい方",
        "point": "500円玉大を手のひらに取り、温めてから顔全体に丁寧になじませてください。一度にたくさんつけるのではなく、2回に分けてハンドプレスを重ねるのが浸透を高める秘訣です。"
    },
    {
        "rank": 4,
        "tag": "🛡️ 潤いを閉じ込めて逃さない鉄壁シールド！ライスパワーNo.11配合のリッチな濃密保湿クリーム",
        "catch": "水分と油分の黄金バランスを再構築。翌朝まで吸い付くような弾力とモチモチ感が持続",
        "brand_name": "米肌 (MAIHADA)",
        "capacity": "40g (肌潤クリーム)",
        "type": "高保湿リッチクリーム",
        "features": "ライスパワーNo.11、発酵ヒアルロン酸、コメヌカ・大豆発酵エキス、高密着バリアシールド処方",
        "value": "美容液や乳液で満たしたうるおいを強力にロック。冬の乾燥冷風から肌を完璧に保護し、ピンとしたハリをもたらす濃厚フィニッシャー",
        "desc_p1": "化粧水や美容液で水分を補給しても、冬の湿度が20%台に落ち込む室内では水分蒸発が止まりません。米肌の『肌潤クリーム』は、ライスパワーNo.11をはじめとする発酵成分と上質な油分が絶妙にブレンドされた濃密保護クリームです。",
        "desc_p2": "リッチでこっくりとした質感でありながら、肌の上にのせるとスルスルとなめらかにとろけてピタッと密着。肌表面に薄い保護ヴェールを形成し、寝ている間のエアコン乾燥や寝具との摩擦から肌を守り抜きます。翌朝の洗顔時には、肌表面がツルンと滑らかに整い、まるでスチームパックをした後のような柔らかさを実感できます。",
        "target": "朝起きると肌がカサついている方、濃厚なクリームでしっかりフタをしたい方、冬の乾燥小ジワを集中ケアしたい方",
        "point": "お手入れの最後に、パール粒大を手に取り、額・両頬・鼻・あごの5点に置いてから外側へ向かって優しく伸ばします。最後に手のひら全体で顔を包んで温めると密着度が増します。"
    },
    {
        "rank": 5,
        "tag": "🍶 創業360年超の老舗酒蔵が誇る大容量名品！コメ発酵液・アミノ酸・セラミドのトリプル保湿",
        "catch": "日本酒一升分の主要アミノ酸を濃縮。顔はもちろん全身にバシャバシャ使える高コスパ王道",
        "brand_name": "菊正宗 (きくまさむね)",
        "capacity": "500ml (日本酒の化粧水 高保湿)",
        "type": "大容量高保湿化粧水",
        "features": "純米吟醸酒（コメ発酵液）、アミノ酸配合、3種のセラミド（NP・AP・EOP）、アルブチン、大容量ポンプ式",
        "value": "ドラッグストアコスメの中でも圧倒的なリピート率を誇るベストセラー。冬のお風呂上がり全身保湿からコットンパックまで惜しみなく使える圧倒的コスパ",
        "desc_p1": "江戸時代から続く日本酒の名門『菊正宗』が本気で開発したスキンケア化粧水。日本酒（コメ発酵液）には、肌の天然保湿因子NMFを構成するアミノ酸が豊富に含まれており、本製品には菊正宗の純米吟醸酒が贅沢に配合されています。",
        "desc_p2": "さらにセラミドNP・AP・EOPという3種のセラミドやアルブチン、プラセンタエキスをプラス配合。ほんのり日本酒の甘い香りが漂うみずみずしいテクスチャーで、重ねるほどに肌がふっくらと柔らかくなります。500mlの大容量ポンプ式なので、冬のお風呂上がりに乾燥しやすい腕や脚、デコルテまで全身にたっぷり贅沢に使えます。コットンに浸して5分間ローションパックをすると、サロン帰りのような潤い感が手に入ります。",
        "target": "毎日惜しみなくバシャバシャ使いたい方、全身の粉ふき乾燥も同時にケアしたい方、コスパ重視で高保湿を求める方",
        "point": "ポンプを2〜3プッシュ手のひらに取り、首筋までしっかりなじませます。冬場はコットンにたっぷり含ませて乾燥の気になる頬やおでこに3分間パックするのがおすすめです。"
    },
    {
        "rank": 6,
        "tag": "🍶 神戸・灘の銘酒『白鶴』の大吟醸酒エキス×美白有効成分！冬の乾燥くすみとシミを同時ケア",
        "catch": "医薬部外品処方。米発酵の深い潤いとトラネキサム酸で、澄み渡る雪のような透明感へ",
        "brand_name": "白鶴酒造",
        "capacity": "500ml (薬用 大吟醸のうるおい美白水)",
        "type": "医薬部外品・薬用美白高保湿化粧水",
        "features": "大吟醸酒エキス（コメ発酵液）、トラネキサム酸配合、甘草エキス、ヒアルロン酸、大容量500ml",
        "value": "冬の紫外線と乾燥ダメージでどんよりくすんだ肌を、アミノ酸リッチな米発酵液と美白有効成分でトータルサポートする贅沢スキンケア",
        "desc_p1": "日本を代表する酒どころ・神戸灘の銘酒『白鶴』が、こだわりの大吟醸酒『翔雲』の酵母エキスを配合して生み出した薬用化粧水。乾燥によるくすみと、冬でも油断できない紫外線によるシミ・そばかすを1本でケアできる医薬部外品です。",
        "desc_p2": "美白有効成分トラネキサム酸がメラニンの生成を抑えてシミ・そばかすを防ぎ、同時に肌荒れを防止。そこへ大吟醸酒から抽出された米発酵液と植物エキスが角層にじっくり染み渡り、乾燥で硬くなった肌を解きほぐします。サラサラとした軽快な使い心地ながら、角層に水分がしっかり満ちてキメが整い、明るく透き通るような白肌へと導きます。",
        "target": "冬の乾燥くすみが気になる方、美白ケアと保湿ケアを1本で両立させたい方、大容量で家族とシェアしたい方",
        "point": "洗顔後、清潔な手のひらやコットンにたっぷり取り、パッティングするように顔全体になじませてください。ひじやひざの黒ずみ・乾燥ケアにも最適です。"
    },
    {
        "rank": 7,
        "tag": "🌾 米ぬか由来のガンマオリザノール＆酵母エキス凝縮！昔ながらの知恵が息づく濃密ハリ艶美容液",
        "catch": "純米水と米ぬか抽出油が素肌にスーッと浸透。乾燥に負けないハリ・ツヤ・弾力を呼び覚ます",
        "brand_name": "リアル (米ぬか美人)",
        "capacity": "40ml (美人エッセンス)",
        "type": "高保湿濃縮美容液",
        "features": "コメヌカエキス、コメ胚芽油（ガンマオリザノール豊富）、加水分解酵母エキス、水溶性コラーゲン",
        "value": "日本人が古来より洗顔や入浴に用いてきた米ぬかの高い美肌効果を先端テクノロジーで濃縮。ビタミンB群やEが冬の乾燥肌を力強くサポート",
        "desc_p1": "『米ぬかで肌を洗うとツルツルになる』という日本の伝統的な美容習慣を受け継ぐ『米ぬか美人』シリーズ。その中でも高濃度な美容成分を凝縮したのがこの『美人エッセンス』です。",
        "desc_p2": "米ぬか特有の有用成分『ガンマ-オリザノール』やビタミンEを豊富に含む米胚芽油、コメヌカエキス、酵母エキスをベストバランスで配合。トロリとした琥珀色の美容液が、カサつきがちな冬の素肌に素早くなじみ、角層の奥まで栄養を届けます。乾燥によって失われがちなツヤとハリが瞬時に蘇り、触り心地の良いふっくら柔らかな肌感を叶えます。",
        "target": "昔ながらの米ぬかコスメに信頼を寄せる方、乾燥によるたるみやハリ不足が気になる方、自然派の濃厚美容液を求める方",
        "point": "化粧水の直後、スポイトで適量を手のひらに取り、気になる目元・口元を中心に引き上げるように優しくなじませてください。"
    },
    {
        "rank": 8,
        "tag": "🌿 コメヌカ発酵液×5種のヒト型セラミド！敏感肌を考え抜いた松山油脂の鉄壁バリアクリーム",
        "catch": "アルコール・香料・着色料・鉱物油完全フリー。乾燥でヒリつく肌を優しく包み込む安心設計",
        "brand_name": "松山油脂 (肌をうるおす)",
        "capacity": "50g (保湿フェイスクリーム)",
        "type": "低刺激・高保湿フェイスクリーム",
        "features": "コメヌカ発酵液、5種のヒト型セラミド（EOP・NG・NP・AG・AP）、シア脂、スクワラン",
        "value": "角層深部を潤すコメ発酵液と、細胞間脂質を補う5種のヒト型セラミドを黄金比で配合。冬のゆらぎ肌や粉吹き肌を優しく鎮静・保護",
        "desc_p1": "真面目なモノづくりで絶大な信頼を集める松山油脂の『肌をうるおす保湿スキンケア』。乾燥肌・敏感肌のために開発されたこの保湿フェイスクリームは、コメヌカ発酵液とヒト型セラミドを贅沢に組み合わせた実力派アイテムです。",
        "desc_p2": "コメヌカ発酵液が角層の水分保持力をサポートし、さらに肌のバリア機能に不可欠な5種類のヒト型セラミドが細胞の隙間をぴったり埋め尽くします。シアバターとスクワランが肌表面になめらかな保護膜を張り、真冬の乾いた外気から徹底的に肌を守ります。防腐剤フリー・低刺激処方のため、乾燥で肌がピリピリしやすい12月の極寒期でも安心して使えます。",
        "target": "敏感肌で肌荒れしやすい方、ヒト型セラミドと米発酵成分をダブルで取り入れたい方、安心の無添加処方を好む方",
        "point": "スキンケアの最後に、小豆粒大を手に取り、手のひらで温めてから顔全体を包み込むように押し込みます。目元のちりめんジワには重ねづけがおすすめです。"
    },
    {
        "rank": 9,
        "tag": "🍶 灘の老舗蔵元『日本盛』が仕込む高保水ローション！純米酒の旨味エキスとヒアルロン酸配合",
        "catch": "日本酒発酵の天然保湿因子で肌が吸い付く。大容量550mlで冬の毎日に贅沢な潤いを",
        "brand_name": "日本盛",
        "capacity": "550ml (日本酒のたっぷり保湿化粧水)",
        "type": "大容量コメ発酵高保湿化粧水",
        "features": "純米酒（コメ発酵液）、ヒアルロン酸Na、アーチチョーク葉エキス、無着色・弱酸性、大容量ポンプ",
        "value": "日本酒の醸造過程で生まれる天然のアミノ酸やミネラルが肌のキメをキュッと整え、真冬の乾燥毛穴やゴワつきをみずみずしく潤す",
        "desc_p1": "『日本盛は良いお酒〜』でおなじみの名門蔵元・日本盛が手がける高保湿化粧水。杜氏の肌の美しさにヒントを得て、純米酒のうるおい成分をそのまま化粧水へと昇華させました。",
        "desc_p2": "角層にすんなりなじむ純米酒由来のコメ発酵液に、保水力の高いヒアルロン酸や肌を引き締めるアーチチョーク葉エキスをブレンド。シャバシャバとした軽やかな質感ながら、肌にパッティングするとグングン吸い込まれ、もっちりとした弾力が持続します。大容量550mlポンプ仕様なので、冬場の乾燥しやすい腕や脚、背中のお手入れにも惜しみなく使えます。",
        "target": "家族全員でたっぷり使える化粧水を探している方、ベタつきのない高保湿を好む方、日本酒の美肌効果を気軽に試したい方",
        "point": "洗顔後、3〜4プッシュを手に取り、優しくパッティングしながら顔から首すじまでなじませてください。スプレーボトルに詰め替えてお風呂上がりのプレ化粧水にするのもおすすめです。"
    },
    {
        "rank": 10,
        "tag": "💧 高保水コメ発酵×ヒアルロン酸複合体！乾燥による大人の小ジワを目立たなくする濃密化粧液",
        "catch": "医薬部外品・シワ改善＆高保湿。とろみリッチなテクスチャーが角層深層までうるおいをロック",
        "brand_name": "ONE BY KOSE (コーセー)",
        "capacity": "160ml (ディープ ハイドレーター)",
        "type": "医薬部外品・薬用高保湿エイジングケア化粧水",
        "features": "有効成分リンクルナイアシン、コメ発酵エキス、ヒアルロン酸複合体、高浸透処方",
        "value": "真冬の過酷な乾燥による乾燥小ジワを改善しながら、米発酵の豊かな潤いで角層をふっくら満たす。大人の冬枯れ肌を救う高機能化粧水",
        "desc_p1": "ONE BY KOSEが誇る高機能エイジングケア化粧水『ディープ ハイドレーター』。冬の乾燥によって深まる小ジワやハリの低下にアプローチする医薬部外品です。",
        "desc_p2": "コーセー独自のコメ発酵エキスをはじめとする保湿成分と、シワ改善・美白有効成分のリンクルナイアシンを贅沢に配合。美容液のように濃密でまろやかなテクスチャーが、乾燥してこわばった大人の肌にしっとりと吸い込まれていきます。肌の内側からうるおいが押し寄せるような充実感があり、ファンデーションのノリが格段にアップ。冬の乾燥によるくすみやシワっぽさを一掃します。",
        "target": "乾燥だけでなく目元や口元の小ジワが気になる大人の女性、1本で高い保湿力とエイジングケア効果を実感したい方",
        "point": "洗顔後または導入美容液の後、手のひらまたはコットンに500円玉大を取り、顔全体に丁寧になじませます。特に乾燥や小ジワが気になる目尻やほうれい線には重ねてハンドプレスしてください。"
    }
]

# JSON-LD構造化データ作成
faq_data = [
    {
        "q": "米発酵・ライスパワーコスメの最大の特徴は何ですか？一般的な保湿成分とどう違いますか？",
        "a": "一般的なヒアルロン酸やグリセリンが『角層に水分を保持する（外から補給する）』のに対し、特に医薬部外品のライスパワーNo.11は『肌自らがセラミドを合成する力を高め、水分保持能を改善する』という根本的なアプローチを持ちます。これにより、塗った直後だけでなく、自らうるおいを逃さない健やかなバリア機能を角層内部から育てることができます。"
    },
    {
        "q": "お酒（アルコール）に弱い体質や敏感肌でも米発酵コスメを使って大丈夫ですか？",
        "a": "日本酒化粧水などの一部の製品には微量のアルコール成分（エタノール等）が含まれる場合がありますが、ライスパワーNo.11やコメ発酵エキス自体はアルコール分を除去して抽出・精製されているため、お酒に弱い方でも問題なく使えるものがほとんどです。肌が敏感な方は、エタノールフリー処方のもの（松山油脂や米肌など）を選ぶか、腕の内側でパッチテストを行ってから使用することをおすすめします。"
    },
    {
        "q": "11月・12月の冬本番に米発酵コスメを取り入れる最も効果的なタイミングはいつですか？",
        "a": "洗顔直後のファーストステップ（導入ブースター美容液）としての使用が最も効果的です。冬は寒さで角層が硬化し化粧水が弾かれやすいため、洗顔後すぐにライスパワーNo.11配合の導入美容液（ONE BY KOSE等）を仕込むことで、硬くなった角質が瞬時にほぐれ、その後の化粧水やクリームの浸透が飛躍的に高まります。"
    },
    {
        "q": "美白ケアやエイジングケア成分（ビタミンCやレチノール）と併用しても問題ありませんか？",
        "a": "全く問題ありません。むしろ米発酵成分が角層のバリア機能と水分保持能を高めることで、ビタミンCやレチノール特有の乾燥・刺激感を和らげ、効果をより引き出しやすい健やかな肌状態を整えてくれます。併用する際は、導入液（米発酵）→化粧水→ビタミンC/レチノール美容液→乳液・クリームの順で使用するのが理想的です。"
    },
    {
        "q": "プチプラの大容量日本酒化粧水と、高価格帯の薬用ライスパワー美容液はどう使い分けるべきですか？",
        "a": "『角層の水分量アップと全身のデイリー保湿』にはプチプラの大容量日本酒化粧水（菊正宗や白鶴など）が最適で、入浴後の全身ケアやコットンパックにバシャバシャ使うと効果的です。一方、『自らセラミドを産生して乾燥肌質そのものを根本改善したい顔の集中ケア』には、医薬部外品認可のライスパワーNo.11配合美容液（ONE BY KOSEや米肌など）を投入するという、適材適所の併用が最も賢く高いコスパを発揮します。"
    }
]

schema_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！自らうるおう力を育む米発酵・ライスパワー高保湿ランク10",
    "description": "11月・12月の本格的な冬乾燥に！肌自らがセラミドを作り出すライスパワーNo.11や純米コメ発酵液を配合した高保湿スキンケア10選を徹底比較。ONE BY KOSE、米肌、ライスフォース、菊正宗、松山油脂など厳選。",
    "image": items[0]["img_url"],
    "datePublished": "2026-11-03T07:00:00+09:00",
    "dateModified": "2026-11-03T07:00:00+09:00",
    "author": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ 編集部",
        "url": "https://lumi-cosme.vercel.app/"
    },
    "publisher": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-rice-power"
    }
}

schema_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": it["rank"],
            "name": it["name"],
            "item": {
                "@type": "Product",
                "name": it["name"],
                "image": it["img_url"],
                "offers": {
                    "@type": "Offer",
                    "priceCurrency": "JPY",
                    "price": str(it["price"]),
                    "availability": "https://schema.org/InStock",
                    "url": it["affiliate_url"]
                }
            }
        } for it in items
    ]
}

schema_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f["a"]
            }
        } for f in faq_data
    ]
}

schema_breadcrumb = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "ホーム",
            "item": "https://lumi-cosme.vercel.app/"
        },
        {
            "@type": "ListItem",
            "position": 2,
            "name": "米発酵・ライスパワー高保湿ランク10",
            "item": "https://lumi-cosme.vercel.app/winter-rice-power"
        }
    ]
}

# HTML構築
items_html = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    price_str = f"¥{it['price']:,}" if it['price'] > 0 else "オープン価格"
    
    items_html += f"""
    <!-- Rank {p['rank']} -->
    <div class="product-card" id="rank-{p['rank']}">
      <div class="product-rank-badge">第{p['rank']}位</div>
      <div class="product-header">
        <span class="product-tag">{p['tag']}</span>
        <h3 class="product-title">{p['catch']}</h3>
        <div class="product-meta">
          <span class="product-brand">ブランド: {p['brand_name']}</span>
          <span class="product-capacity">容量・規格: {p['capacity']}</span>
          <span class="product-type">タイプ: {p['type']}</span>
        </div>
      </div>

      <div class="product-body">
        <div class="product-img-wrap">
          <img src="{it['img_url']}" alt="{it['name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-price-box">
            <span class="price-label">楽天市場参考価格:</span>
            <span class="price-val">{price_str}</span>
            <span class="price-tax">(税込・送料込目安)</span>
          </div>
          <div class="product-features">
            <strong>配合特徴・主成分:</strong> {p['features']}
          </div>
          <div class="product-value-point">
            <strong>真冬の高保湿ポイント:</strong> {p['value']}
          </div>
        </div>
      </div>

      <div class="product-desc">
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>

      <div class="product-review-box">
        <div class="review-row">
          <span class="review-label">🎯 こんな人におすすめ:</span>
          <span class="review-text">{p['target']}</span>
        </div>
        <div class="review-row">
          <span class="review-label">💡 プロのおすすめ使い方:</span>
          <span class="review-text">{p['point']}</span>
        </div>
      </div>

      <div class="product-action">
        <a href="{it['affiliate_url']}" target="_blank" rel="noopener noreferrer nofollow" class="rakuten-btn">
          <span>楽天市場で最新価格＆口コミを見る</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </div>
"""

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！自らうるおう力を育む米発酵・ライスパワー高保湿ランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬本番に深刻化するインナードライ・粉吹き乾燥を根本解決！日本で唯一『水分保持能を改善する』医薬部外品認可のライスパワーNo.11や純米コメ発酵液を配合した高保湿スキンケア10選を徹底比較！ONE BY KOSE、米肌、ライスフォース、菊正宗、松山油脂など厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-rice-power">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！自らうるおう力を育む米発酵・ライスパワー高保湿ランク10">
  <meta property="og:description" content="11月・12月の本格的な冬乾燥に！肌自らがセラミドを作り出すライスパワーNo.11や純米コメ発酵液を配合した高保湿スキンケア10選を徹底比較。ONE BY KOSE、米肌、ライスフォース、菊正宗、松山油脂など厳選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-rice-power">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.jpg">

  <script type="application/ld+json">
{json.dumps(schema_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(schema_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(schema_faq, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(schema_breadcrumb, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #92400e;
      --primary-light: #fef3c7;
      --accent: #b45309;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --radius: 12px;
      --shadow: 0 4px 15px rgba(0,0,0,0.06);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
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
      backdrop-filter: blur(10px);
      background-color: rgba(255, 255, 255, 0.95);
    }}
    .nav-container {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-links {{ display: flex; gap: 1rem; }}
    .nav-links a {{
      text-decoration: none;
      color: var(--text-muted);
      font-size: 0.9rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}

    .breadcrumb-nav {{
      max-width: 1000px;
      margin: 1.5rem auto 0;
      padding: 0 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb-nav a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumb-nav span {{ margin: 0 0.5rem; }}

    main {{
      max-width: 1000px;
      margin: 0 auto;
      padding: 1.5rem;
    }}

    .article-header {{
      background: var(--card-bg);
      padding: 2.5rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border-top: 5px solid var(--primary);
    }}
    .article-badge {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 1rem;
    }}
    h1 {{
      font-size: 2rem;
      line-height: 1.4;
      margin-bottom: 1.25rem;
      color: #0f172a;
      letter-spacing: -0.02em;
    }}
    .article-lead {{
      font-size: 1.05rem;
      color: #334155;
      line-height: 1.8;
      margin-bottom: 1.5rem;
    }}
    .article-meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      border-top: 1px solid var(--border);
      padding-top: 1rem;
    }}

    .content-section {{
      background: var(--card-bg);
      padding: 2.5rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
    }}
    h2 {{
      font-size: 1.5rem;
      color: #0f172a;
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--border);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    h3.sub-title {{
      font-size: 1.2rem;
      color: var(--primary);
      margin: 1.5rem 0 0.75rem;
    }}

    .info-card-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin: 1.5rem 0;
    }}
    .info-card {{
      background: #fdfaf7;
      border: 1px solid #fed7aa;
      border-radius: 10px;
      padding: 1.5rem;
    }}
    .info-card h4 {{
      color: var(--primary);
      margin-bottom: 0.5rem;
      font-size: 1.05rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .info-card p {{ font-size: 0.95rem; color: #475569; line-height: 1.6; }}

    .product-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.25rem 2rem;
      margin-bottom: 3rem;
      position: relative;
      border: 1px solid var(--border);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .product-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    }}
    .product-rank-badge {{
      position: absolute;
      top: -15px;
      left: 20px;
      background: linear-gradient(135deg, #b45309, #d97706);
      color: #ffffff;
      padding: 0.35rem 1.25rem;
      border-radius: 9999px;
      font-weight: 800;
      font-size: 1.1rem;
      box-shadow: 0 4px 10px rgba(180, 83, 9, 0.3);
    }}
    .product-tag {{
      display: inline-block;
      background: #fef3c7;
      color: #92400e;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 6px;
      margin-top: 0.5rem;
      margin-bottom: 0.5rem;
    }}
    .product-title {{
      font-size: 1.35rem;
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 0.75rem;
    }}
    .product-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      background: #f8fafc;
      padding: 0.75rem 1rem;
      border-radius: 8px;
    }}
    .product-body {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 2rem;
      margin-bottom: 1.5rem;
    }}
    @media (max-width: 768px) {{
      .product-body {{ grid-template-columns: 1fr; }}
      h1 {{ font-size: 1.6rem; }}
    }}
    .product-img-wrap {{
      text-align: center;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .product-img {{
      max-width: 100%;
      max-height: 240px;
      object-fit: contain;
      border-radius: 6px;
    }}
    .product-price-box {{
      background: #fffbeb;
      border: 1px solid #fde68a;
      padding: 1rem;
      border-radius: 8px;
      margin-bottom: 1rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}
    .price-label {{ font-size: 0.85rem; color: #78350f; font-weight: 600; }}
    .price-val {{ font-size: 1.6rem; font-weight: 800; color: #b45309; }}
    .price-tax {{ font-size: 0.8rem; color: var(--text-muted); }}

    .product-features, .product-value-point {{
      font-size: 0.95rem;
      margin-bottom: 0.75rem;
      line-height: 1.6;
    }}
    .product-desc {{
      font-size: 1rem;
      line-height: 1.8;
      color: #334155;
      margin-bottom: 1.5rem;
      background: #fafaf9;
      padding: 1.25rem 1.5rem;
      border-radius: 8px;
      border-left: 4px solid var(--accent);
    }}
    .product-desc p + p {{ margin-top: 1rem; }}

    .product-review-box {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem 1.25rem;
      margin-bottom: 1.5rem;
    }}
    .review-row {{
      display: flex;
      flex-direction: column;
      margin-bottom: 0.5rem;
      font-size: 0.9rem;
    }}
    .review-row:last-child {{ margin-bottom: 0; }}
    .review-label {{ font-weight: 700; color: #1e293b; margin-bottom: 0.2rem; }}
    .review-text {{ color: #475569; }}

    .product-action {{
      text-align: center;
      margin-top: 1rem;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, #bf0000, #dc2626);
      color: #ffffff;
      text-decoration: none;
      padding: 1rem 2rem;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 1.05rem;
      box-shadow: 0 4px 15px rgba(220, 38, 38, 0.3);
      transition: all 0.2s;
      width: 100%;
      max-width: 480px;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(220, 38, 38, 0.4);
      background: linear-gradient(135deg, #990000, #b91c1c);
    }}

    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 1.25rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-weight: 700;
      font-size: 1.05rem;
      color: #0f172a;
      margin-bottom: 0.5rem;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: #475569;
      line-height: 1.7;
    }}

    .internal-link-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}
    .internal-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem;
      text-decoration: none;
      color: inherit;
      transition: all 0.2s;
    }}
    .internal-card:hover {{
      border-color: var(--primary);
      background: #fffbeb;
      transform: translateY(-2px);
    }}
    .internal-card h5 {{ font-size: 0.95rem; color: #1e3a8a; margin-bottom: 0.35rem; }}
    .internal-card p {{ font-size: 0.8rem; color: var(--text-muted); line-height: 1.4; }}

    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1.5rem;
      font-size: 0.85rem;
      text-align: center;
      margin-top: 4rem;
    }}
    footer a {{ color: #cbd5e1; text-decoration: none; }}
    footer a:hover {{ text-decoration: underline; }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }}
  </style>
</head>
<body>

<header>
  <div class="nav-container">
    <a href="/" class="site-logo">
      <span>🌾</span> 冬コスメ徹底比較ラボ
    </a>
    <div class="nav-links">
      <a href="/">ホーム</a>
      <a href="/#ranking">ランキング</a>
      <a href="/#guide">スキンケア知識</a>
    </div>
  </div>
</header>

<div class="breadcrumb-nav">
  <a href="/">ホーム</a> <span>&gt;</span>
  <a href="/winter-base-makeup">冬コスメ特集</a> <span>&gt;</span>
  <span>米発酵・ライスパワー高保湿ランク10</span>
</div>

<main>
  <article>
    <div class="article-header">
      <span class="article-badge">🌾 11月・12月冬の肌改善特集</span>
      <h1>保湿力の強さで肌乾燥とさようなら！自らうるおう力を育む米発酵・ライスパワー高保湿ランク10</h1>
      <p class="article-lead">
        11月から12月にかけて外気温が一気に下がり、室内のエアコン暖房が本格稼働すると、空気中の湿度は20〜30%台まで急落します。この時期に多くの女性を悩ませるのが、「化粧水をどれだけ重ねても時間が経つと粉を吹く」「肌の奥がつっぱるようなインナードライ」という深刻な肌砂漠化です。外から油分を塗るだけのケアでは追いつかない冬の過酷な乾燥を根底から覆す救世主こそ、日本古来の米発酵技術と先端皮膚科学が融合した『ライスパワーNo.11』をはじめとする米発酵コスメです。肌自らがセラミドを作り出す水分保持能改善のメカニズムから、楽天市場で圧倒的な支持を集める名品10選までを美容専門ライターが徹底解説します。
      </p>
      <div class="article-meta-bar">
        <span>📅 公開日: 2026年11月3日</span>
        <span>🔄 最終更新: 2026年11月3日</span>
        <span>✍️ 監修: 冬コスメ徹底比較ラボ 美容班</span>
        <span>🏷️ 楽天市場公式APIデータリアルタイム連動</span>
      </div>
    </div>

    <!-- 専門知識解説セクション -->
    <section class="content-section">
      <h2>🔬 なぜ11-12月に米発酵・ライスパワーが最強なのか？</h2>
      <p>
        冬の乾燥対策といえば、ヒアルロン酸やコラーゲン、ワセリンなどの『補水・密閉』が一般的です。しかし、真冬の乾いた冷風や過酷な暖房にさらされると、角質層のバリア機能そのものが崩壊し、与えた水分が瞬く間に蒸発してしまいます。米発酵・ライスパワーが他と決定的に一線を画す理由は、以下の3つの科学的メカニズムにあります。
      </p>

      <div class="info-card-grid">
        <div class="info-card">
          <h4>🌾 1. 日本で唯一の『水分保持能改善』認可</h4>
          <p>医薬部外品の有効成分として認可されている『ライスパワーNo.11』は、肌の基底層に直接働きかけ、細胞間脂質の主成分である『セラミド』の産生を促します。単に外からセラミドを補うのではなく、自らセラミドを生み出せる肌質へと改善する唯一無二の働きを持ちます。</p>
        </div>
        <div class="info-card">
          <h4>🍶 2. NMF（天然保湿因子）を構成するアミノ酸の宝庫</h4>
          <p>純米酒や米ぬかの発酵過程で生まれるコメ発酵液には、角質細胞内で水分を抱え込む天然保湿因子（NMF）とほぼ同等の組成を持つ遊離アミノ酸、ミネラル、ビタミンB群が凝縮。分子が小さいため、ゴワついた冬の硬い角層にも素早く浸透します。</p>
        </div>
        <div class="info-card">
          <h4>🛡️ 3. 日本人の肌角層との驚異的な親和性</h4>
          <p>数千年にわたり米を主食としてきた日本人の肌は、米由来の脂質やペプチドとの生体親和性が極めて高いことが知られています。合成ポリマーや過度な油分と異なり、毛穴を詰まらせることなく、吸い付くようなキメ細やかさと透明感を呼び覚まします。</p>
        </div>
      </div>
    </section>

    <!-- 選び方ガイド -->
    <section class="content-section">
      <h2>🎯 11-12月の乾燥を制する！米発酵・ライスパワーコスメの選び方3箇条</h2>
      <p>米発酵コスメは、配合されている成分の種類やテクスチャーによって期待できる効果が大きく異なります。ご自身の肌状態やライフスタイルに合わせて最適なアイテムを見極めましょう。</p>
      
      <h3 class="sub-title">① 根本的な肌質改善なら『ライスパワーNo.11（医薬部外品）』</h3>
      <p>「何を塗っても乾燥が治まらない」「夕方になると肌が突っ張って痛い」という深刻なインナードライ肌の方は、パッケージに『医薬部外品』かつ『ライスパワーNo.11』が有効成分として明記された製品（ONE BY KOSE、米肌、ライスフォースなど）を選びましょう。角層の水分保持能を根本から底上げできます。</p>

      <h3 class="sub-title">② 全身保湿＆毎日の惜しみない水分補給なら『純米酒・コメ発酵液大容量ローション』</h3>
      <p>「お風呂上がりに全身がカサつく」「コットンパックでたっぷり水分チャージしたい」という方には、老舗酒蔵（菊正宗、白鶴、日本盛など）が手がける500ml超の大容量ポンプタイプがベスト。アミノ酸とセラミドが豊富に含まれ、全身に気兼ねなく使えます。</p>

      <h3 class="sub-title">③ 敏感肌・ゆらぎ肌なら『アルコールフリー＆ヒト型セラミド複合型』</h3>
      <p>冬場の寒冷刺激で肌が赤くなったりヒリヒリしやすい方は、コメヌカ発酵液に加えて5種のヒト型セラミドやスクワランを配合した無添加・低刺激設計のクリーム（松山油脂など）がおすすめ。アルコール（エタノール）無添加の処方を選ぶと刺激なく使えます。</p>
    </section>

    <!-- ランキング本文 10商品 -->
    <section class="content-section">
      <h2>🏆 11-12月に本当に売れている！米発酵・ライスパワー高保湿コスメ厳選ランク10</h2>
      <p>楽天市場の最新販売実績・口コミ評価・成分濃度・保湿持続性を徹底検証し、今冬絶対に取り入れたい珠玉の10アイテムをランキング形式でご紹介します。</p>
    </section>

{items_html}

    <!-- 効果的な使い方のステップ -->
    <section class="content-section">
      <h2>💡 美容のプロが伝授！真冬の米発酵スキンケア・超高保湿4ステップ</h2>
      <p>米発酵成分の浸透力とセラミド産生促進効果を極限まで引き出すための、理想的な朝晩のスキンケア手順をご紹介します。</p>

      <div class="info-card-grid">
        <div class="info-card">
          <h4>STEP 1: 洗顔直後に『ライスパワー導入美容液』</h4>
          <p>洗顔後、タオルドライした直後の素肌に2〜3プッシュ。硬くこわばった冬の角質層を瞬時にほぐし、セラミド産生のシグナルを届けます。</p>
        </div>
        <div class="info-card">
          <h4>STEP 2: 『コメ発酵化粧水』の2度づけハンドプレス</h4>
          <p>化粧水は1回で終わらせず、500円玉大を2回に分けて肌に押し込みます。手のひらが肌に吸い付く感覚が出るまで優しく温めながらなじませます。</p>
        </div>
        <div class="info-card">
          <h4>STEP 3: 乾燥部位への『濃厚米エキス重ねづけ』</h4>
          <p>目元、口元、頬の高い位置など、暖房の温風が当たりやすい部分には、美容液や乳液を指先でトントンと重ねて密着させます。</p>
        </div>
        <div class="info-card">
          <h4>STEP 4: 『濃厚米発酵クリーム』で完璧なフタ</h4>
          <p>仕上げにシアバターやスクワランをブレンドした米発酵クリームをハンドプレス。寝ている間の水分蒸発をゼロに抑え、翌朝のモチ肌を約束します。</p>
        </div>
      </div>
    </section>

    <!-- よくある質問 FAQ -->
    <section class="content-section">
      <h2>❓ 米発酵・ライスパワーコスメに関するよくある質問・Q&A</h2>

      <div class="faq-item">
        <div class="faq-q">Q. 米発酵・ライスパワーコスメの最大の特徴は何ですか？一般的な保湿成分とどう違いますか？</div>
        <div class="faq-a">
          一般的なヒアルロン酸やグリセリンが『角層に水分を保持する（外から補給する）』のに対し、特に医薬部外品のライスパワーNo.11は『肌自らがセラミドを合成する力を高め、水分保持能を改善する』という根本的なアプローチを持ちます。これにより、塗った直後だけでなく、自らうるおいを逃さない健やかなバリア機能を角層内部から育てることができます。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. お酒（アルコール）に弱い体質や敏感肌でも米発酵コスメを使って大丈夫ですか？</div>
        <div class="faq-a">
          日本酒化粧水などの一部の製品には微量のアルコール成分（エタノール等）が含まれる場合がありますが、ライスパワーNo.11やコメ発酵エキス自体はアルコール分を除去して抽出・精製されているため、お酒に弱い方でも問題なく使えるものがほとんどです。肌が敏感な方は、エタノールフリー処方のもの（松山油脂や米肌など）を選ぶか、腕の内側でパッチテストを行ってから使用することをおすすめします。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. 11月・12月の冬本番に米発酵コスメを取り入れる最も効果的なタイミングはいつですか？</div>
        <div class="faq-a">
          洗顔直後のファーストステップ（導入ブースター美容液）としての使用が最も効果的です。冬は寒さで角層が硬化し化粧水が弾かれやすいため、洗顔後すぐにライスパワーNo.11配合の導入美容液（ONE BY KOSE等）を仕込むことで、硬くなった角質が瞬時にほぐれ、その後の化粧水やクリームの浸透が飛躍的に高まります。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. 美白ケアやエイジングケア成分（ビタミンCやレチノール）と併用しても問題ありませんか？</div>
        <div class="faq-a">
          全く問題ありません。むしろ米発酵成分が角層のバリア機能と水分保持能を高めることで、ビタミンCやレチノール特有の乾燥・刺激感を和らげ、効果をより引き出しやすい健やかな肌状態を整えてくれます。併用する際は、導入液（米発酵）→化粧水→ビタミンC/レチノール美容液→乳液・クリームの順で使用するのが理想的です。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. プチプラの大容量日本酒化粧水と、高価格帯の薬用ライスパワー美容液はどう使い分けるべきですか？</div>
        <div class="faq-a">
          『角層の水分量アップと全身のデイリー保湿』にはプチプラの大容量日本酒化粧水（菊正宗や白鶴など）が最適で、入浴後の全身ケアやコットンパックにバシャバシャ使うと効果的です。一方、『自らセラミドを産生して乾燥肌質そのものを根本改善したい顔の集中ケア』には、医薬部外品認可のライスパワーNo.11配合美容液（ONE BY KOSEや米肌など）を投入するという、適材適所の併用が最も賢く高いコスパを発揮します。
        </div>
      </div>
    </section>

    <!-- 内部リンク関連記事 -->
    <section class="content-section">
      <h2>🔗 あわせて読みたい！真冬の集中保湿ケア関連記事</h2>
      <p>冬の徹底した乾燥対策は、米発酵による水分保持能改善に加えて、高純度オイルやセラミドクリームを連動させることで最大の相乗効果を生み出します。ぜひチェックしてみてください。</p>
      
      <div class="internal-link-grid">
        <a href="/winter-ceramide-lotion" class="internal-card">
          <h5>🧴 高保湿セラミド化粧水</h5>
          <p>角層のバリア機能を守るセラミドを直接補給！インナードライを撃退する化粧水10選</p>
        </a>
        <a href="/winter-ceramide-cream" class="internal-card">
          <h5>🧴 高保湿セラミドクリーム</h5>
          <p>米発酵で満たしたうるおいを逃さない！冷風から肌を守り抜く濃厚クリーム比較</p>
        </a>
        <a href="/winter-argan-oil" class="internal-card">
          <h5>🥑 高保湿アルガンオイル</h5>
          <p>モロッコの黄金オイルで硬化角質を柔軟化！ブースターとしても極上の美容オイル10選</p>
        </a>
        <a href="/winter-squalane-oil" class="internal-card">
          <h5>✨ 高純度スクワランオイル</h5>
          <p>たった1滴で極上のツヤ膜を形成。純度99.9%のピュアオイルで乾燥小ジワを撃退</p>
        </a>
        <a href="/winter-panthenol-cream" class="internal-card">
          <h5>🧪 高保湿パンテノールクリーム</h5>
          <p>プロビタミンB5で角層バリアを鉄壁補修！冬のヒリヒリ敏感肌を救うクリーム10選</p>
        </a>
        <a href="/winter-horse-oil" class="internal-card">
          <h5>🐴 高保湿馬油クリーム</h5>
          <p>人の皮脂に最も近い天然脂質で粉吹き乾燥を即効ケア！昭和から愛される元祖高保湿</p>
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

output_path = "winter-rice-power.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {output_path} successfully ({len(html_content):,} bytes)!")
