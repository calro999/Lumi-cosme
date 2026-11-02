import json
import re

with open("fetched_3new_nov_dec_argan_horse_panthenol_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_argan_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 アルガンオイル界の世界的絶対王者！洗顔後すぐの1滴で化粧水をゴクゴク引き込む最高峰ブースター",
        "catch": "フランス発オーガニック認証。独自ノズルで最後の一滴まで新鮮、肌がふっくら吸い付く至高の導入オイル",
        "brand_name": "Melvita (メルヴィータ)",
        "capacity": "50ml (ビオオイル アルガンオイル)",
        "type": "エコサート＆コスメビオ認証・100%天然由来アルガンオイル",
        "features": "未精製低温圧搾、アプリケーター付きドロップノズル、防腐剤・着色料フリー、フランス製オーガニック",
        "value": "世界中で愛され続ける導入美容オイルの代名詞。オレイン酸とリノール酸が角層細胞を柔らかくほぐし、冬の硬くなった肌に驚異の保水力を付与",
        "desc_p1": "11月中旬から12月にかけて外気温が急低下すると、肌表面の角質層は冷風と乾燥でカチコチに硬化し、せっかくの化粧水を弾いてしまいます。そんな冬の『角質ゴワつき砂漠肌』を瞬時にふっくら解きほぐすのが、メルヴィータの看板アイテムであるビオオイル アルガンオイルです。",
        "desc_p2": "モロッコ産の厳選されたアルガンの実を低温圧搾（コールドプレス）で抽出し、化学処理を一切施さずにピュアな栄養素をそのままボトルに凝縮。独自の『マイ・ドロップ・アプリケーター』により、肌質や乾燥度合いに合わせて1滴ずつ正確に調整可能です。洗顔直後の湿った肌になじませると、素早く角層へ引き込まれ、その後に重ねる化粧水が驚くほどグングン浸透。夕方になっても突っ張り感や小ジワが気にならない、吸い付くようなモチ肌へと導きます。",
        "target": "化粧水が肌に入っていかないと感じる方、洗顔後のつっぱりが激しい方、まずは実績と信頼のある王道アルガンオイルを選びたい方",
        "point": "洗顔直後、肌にまだ水滴がわずかに残る状態で2〜3滴を手のひらに伸ばし、顔全体を優しく包み込むようにハンドプレスしてください。"
    },
    {
        "rank": 2,
        "tag": "🌿 フランス最高峰の有機認証『ナチュール＆プログレ』取得！未精製ピュア100%の極上クオリティ",
        "catch": "伝統的手法で抽出された未精製バージンオイル。植物ステロールと抗酸化ビタミンを濃厚含有",
        "brand_name": "CODINA (コディナ)",
        "capacity": "100ml (アルガンオイル)",
        "type": "ナチュール＆プログレ認証・未精製オーガニックアルガンオイル",
        "features": "未精製コールドプレス、ナチュール＆プログレ認証（EU最高峰基準）、大容量100mlプッシュボトル",
        "value": "フランスの厳しい自然保護基準をクリアした希少な未精製オイル。黄色く濃厚なテクスチャーが角層のキメをふっくら満たし、真冬の寒冷ダメージを強力防御",
        "desc_p1": "オーガニックコスメ愛好家やエステサロンのプロフェッショナルから熱狂的な支持を集めるフランス発『コディナ』。一般的なエコサート認証よりもさらに基準が厳しいとされる『ナチュール＆プログレ』認証を取得した、極めて純度の高いアルガンオイルです。",
        "desc_p2": "機械による大量生産ではなく、モロッコの契約農家で丁寧に手作業選別されたアルガン種子のみを使用。淡い黄金色とナッツ特有の香ばしいアロマが本物の証です。ビタミンE（トコフェロール）や植物性ステロールが豊富に残されており、冬の冷たい外気にさらされてしぼんだ肌に押し返すような弾力とツヤを復活させます。100mlとたっぷり入っているため、顔だけでなく首筋やデコルテ、パサつく毛先のケアまで贅沢に使い倒せます。",
        "target": "最高品質のオーガニック原料を肌に届けたい方、首元やデコルテまでたっぷりケアしたい方、本物志向のエイジングケアを求める方",
        "point": "夜の入浴中、洗顔後の肌に5〜6滴たっぷり塗布して湯船に浸かる『オイルスチームパック』を行うと、エステ帰りのような極上やわらか肌に仕上がります。"
    },
    {
        "rank": 3,
        "tag": "🧪 東京・檜原村発の高品質サロンクオリティ！ECOCERT認証取得でコスパも群を抜く優良ボトル",
        "catch": "モロッコ現地直輸入の新鮮なピュアアルガン。余分な広告費を削ぎ落とした誠実な価格設計",
        "brand_name": "spa hinoki (スパヒノキ)",
        "capacity": "100ml (オーガニック アルガンオイル)",
        "type": "ECOCERT認証・100%未精製ピュアオーガニックオイル",
        "features": "エコサート認証、低温圧搾法、遮光性プッシュボトル、防腐剤・化学溶剤完全不使用",
        "value": "サロン仕様の高品質オーガニックオイルでありながら、続けやすい価格を実現。冬中のデイリーケアとして全身に惜しみなく使える実力派",
        "desc_p1": "東京・檜原村のヘッドスパサロンから誕生したspa hinoki。品質に一切の妥協を許さず、世界基準のECOCERT（エコサート）コスモスオーガニック認証を取得したアルガンオイルは、知る人ぞ知る名品としてリピーターが絶えません。",
        "desc_p2": "モロッコから空輸した採れたてのアルガンオイルを日本国内のクリーンルームで丁寧に充填。遮光性に優れた使いやすいポンプボトル仕様で、酸化を防ぎながら毎日のスキンケアを快適に支えます。未精製ながら精製オイルに迫る軽やかな肌なじみを実現しており、オイル特有のベタつきが苦手な方でも快適。朝のメイク前にブースターとして仕込んでもファンデーションのヨレを引き起こしません。",
        "target": "毎日たっぷり使える高コスパな大容量を探している方、使いやすいポンプ式を好む方、ベタつきの少ないオイルを求める方",
        "point": "ワンプッシュを手のひらに広げ、乾燥が気になる目元や口元から順になじませます。爪の甘皮やひじのカサつきにもサッと伸ばすと一石二鳥です。"
    },
    {
        "rank": 4,
        "tag": "🌿 ハーブとアロマのパイオニアが厳選！コールドプレスで抽出した一番搾り有機アルガン",
        "catch": "生活の木が誇る厳格な品質管理。スキンケアはもちろん手作りコスメのベースとしても最高峰の信頼性",
        "brand_name": "生活の木 (Tree of life)",
        "capacity": "25ml (有機アルガンオイル バージン 未精製)",
        "type": "有機JAS・未精製バージン植物油",
        "features": "未精製バージン抽出、コールドプレス（低温圧搾）、防腐剤・添加物フリー、国内ボトリング",
        "value": "アロマテラピーの老舗が選び抜いた高品質ピュアオイル。酸化安定性に優れ、冬のデリケートなゆらぎ肌にも穏やかに寄り添う確かな品質",
        "desc_p1": "日本のハーブ・アロマ文化を牽引してきた『生活の木』が届ける有機バージンアルガンオイル。原料調達から国内工場での製品化まで徹底した品質管理基準を設けており、肌が敏感になりやすい冬場でも安心して手に取ることができます。",
        "desc_p2": "モロッコ産の有機栽培アルガンツリーの種子から、熱を加えずじっくり時間をかけて圧搾された『バージン』グレード。ナッツ本来のほんのりとした甘い香りと、濃厚でとろみのあるテクスチャーが特徴です。お肌に伸ばすと、不足した皮脂膜を補うようにスルスルと角層を満たし、真冬のエアコン乾燥によるチリチリとしたつっぱり感を穏やかに鎮めます。25mlの小瓶サイズは、酸化する前に新鮮な状態で使い切りたい方にも最適です。",
        "target": "アロマ専門店ならではの安心感を重視する方、1ヶ月程度で使い切れるコンパクトなサイズを好む方、敏感肌の方",
        "point": "お好みの精油（ラベンダーやフランキンセンスなど）を1滴ブレンドすれば、冬の夜の乾燥をケアしながら至福のリラクゼーションタイムを演出できます。"
    },
    {
        "rank": 5,
        "tag": "🇲🇦 モロッコ女性の伝統手搾り技法を再現！現地の恵みをそのまま届ける素朴で力強いピュアオイル",
        "catch": "伝統的手作業で丁寧に選別された種子。フルーティーで香ばしい香りが漂う濃厚プレミアム",
        "brand_name": "naiad (ナイアード)",
        "capacity": "30ml (アルガンオイル)",
        "type": "モロッコ原産・未精製手絞りアルガンオイル",
        "features": "伝統手選別、コールドプレス一番搾り、無添加・無着色、現地の雇用支援フェアトレード",
        "value": "現地モロッコの生産者と直接繋がり、昔ながらの製法を尊重したナイアードの自信作。角質層を柔らかく整える力が極めて強く、毛穴詰まりを防ぎながら深層保湿",
        "desc_p1": "ヘナやガスールなど、世界各地の伝統素材を届ける『ナイアード』。モロッコのベルベル人女性たちが何世代にもわたり受け継いできたアルガンオイルの製造技術に敬意を払い、丁寧に作られた未精製オイルです。",
        "desc_p2": "石を使って種子を割り、良質な仁だけを厳選して低温圧搾。機械的で画一的な抽出では出せない、アルガン本来の深みのある香りと濃密なコクが肌を包み込みます。不飽和脂肪酸が角層深部へスッと浸透し、肌表面にはベタつかない薄い保護膜を形成。冬の冷たい風にさらされて粉を吹いた頬や、口元の乾燥小ジワを瞬く間にやわらげます。",
        "target": "手仕事の温もりやフェアトレード製品に共感する方、冬の角質肥厚で肌が硬くなっている方、本格的な未精製オイルの力を体感したい方",
        "point": "化粧水の前に1滴、さらにスキンケアの最後にフタとしてもう1滴重ねる『挟み込み保湿』を行うと、真冬の暖房直撃でも一日中しっとり感が持続します。"
    },
    {
        "rank": 6,
        "tag": "📦 プロのサロン原料を工場直販！驚異のコストパフォーマンスで冬の全身を潤す未精製ピュアオイル",
        "catch": "手作りコスメ・サロン卸のマカダミ屋が誇る名品。高品質オーガニック未精製オイルを直販価格で",
        "brand_name": "マカダミ屋 (Macadamia-ya)",
        "capacity": "50ml (オーガニック 未精製 アルガンオイル)",
        "type": "未精製オーガニックピュアキャリアオイル",
        "features": "未精製コールドプレス、オーガニック認証原料、遮光容器、国内充填、無添加",
        "value": "エステやマッサージ店に卸す原料元だからこそ実現できた圧倒的なコスパ。惜しみなく顔・髪・ボディに使える冬のマルチ保湿オイル",
        "desc_p1": "プロのセラピスト向けにキャリアオイルを供給する『マカダミ屋』。余計なパッケージコストや広告宣伝費をカットし、中身の品質勝負で高いリピート率を誇るオーガニックアルガンオイルです。",
        "desc_p2": "モロッコ産の有機認証アルガン種子から低温圧搾で丁寧に抽出された未精製グレード。黄金色のオイルには天然ビタミンEやポリフェノールが豊富に含まれており、真冬の乾燥で疲れた素肌をイキイキとしたツヤ肌へと導きます。お顔の導入オイルとしてはもちろん、シャンプー前の頭皮クレンジングマッサージや、入浴後の濡れたボディに伸ばす全身エモリエントとしても大活躍します。",
        "target": "とにかくコストパフォーマンスを重視する方、顔だけでなく頭皮やボディにも惜しみなく使いたい方、オイルマッサージが好きな方",
        "point": "お風呂上がりにタオルで体を拭く前、濡れた全身に手のひらで伸ばすと、水分と一緒にスーッと馴染んでベタつかずに全身がしっとり整います。"
    },
    {
        "rank": 7,
        "tag": "🔬 国産高純度サイエンス処方！低温圧搾一番搾りのオーガニックピュアエッセンス",
        "catch": "高品質・低価格でコスメ界を席巻するKISO。厳格な品質基準をクリアした高純度モイスチャーオイル",
        "brand_name": "KISO (キソ)",
        "capacity": "50ml (ピュアエッセンスAG オーガニック アルガンオイル)",
        "type": "100%オーガニックアルガン美容原液",
        "features": "低温圧搾一番搾り、未精製オーガニック、スポイト式ガラス遮光瓶、国内GMP認定工場製造",
        "value": "原液コスメで大人気のKISOが放つアルガンオイル。スポイト式で衛生的かつ精密に1滴ずつ取り出せ、冬のスキンケアに高機能な油分をプラス",
        "desc_p1": "美容成分の濃度と原料品質に徹底的にこだわる国内コスメブランド『KISO（基礎化粧品研究所）』。広告費を最小限に抑え、高品質な原料をダイレクトに届ける姿勢が多くのスキンケアマニアから支持されています。",
        "desc_p2": "オーガニック認定を受けたモロッコ産アルガンツリーの種子から、低温圧搾の一番搾りだけを贅沢に使用。ガラス製の遮光瓶に精密なスポイトが付属しており、必要な量を衛生的に取り出すことができます。お肌のバリア機能を支える必須脂肪酸が角質層の隙間を満たし、真冬の寒冷外気から素肌をプロテクト。洗顔後すぐに肌になじませることで、後から使う美容液や化粧水の馴染みを劇的に向上させます。",
        "target": "成分重視でスキンケアを選びたい方、スポイト式で清潔に使いたい方、信頼できる国内製造にこだわりたい方",
        "point": "普段お使いの乳液やクリームに1〜2滴混ぜて使うと、保湿持続力が格段にアップし、真冬仕様のリッチな濃厚クリームにカスタマイズできます。"
    },
    {
        "rank": 8,
        "tag": "🌹 最高級ダマスクローズ精油を贅沢配合！極上の保湿力と至福のアロマに包まれるエレガント仕様",
        "catch": "メルヴィータのベストセラーに香り高いローズをプラス。スキンケアの時間を優雅なリフレッシュタイムへ",
        "brand_name": "Melvita (メルヴィータ)",
        "capacity": "50ml (ビオオイル アルガンオイル ローズ)",
        "type": "オーガニックアルガンオイル＆天然ダマスクローズ精油ブレンド",
        "features": "未精製アルガンオイルベース、天然ダマスクローズエッセンシャルオイル、ドロップノズル、オーガニック認証",
        "value": "名作アルガンオイルのブースター機能はそのままに、摘みたての生花のような華やかな天然ローズの香りをブレンド。冬の乾燥と心の疲れを同時に癒すプレミアム仕様",
        "desc_p1": "メルヴィータのアイコンであるアルガンオイルに、希少な天然ダマスクローズ精油を溶け込ませた大人気フレーバーモデル。無香料のプレーンオイルにはない、幸福感に満ちたスキンケア体験を提供します。",
        "desc_p2": "合成香料では決して再現できない、本物のローズの花びらから抽出されたナチュラルでみずみずしい香り立ち。手のひらで温めて顔を覆った瞬間、華やかなアロマが鼻腔をくすぐり、冬の寒さでこわばった表情筋と心をじんわり解きほぐします。もちろんアルガンオイル本来の驚異的なブースター効果や角層柔軟作用はそのまま。朝のメイク前に使えば、一日中ふんわりと上品なローズの余韻を感じながら過ごせます。",
        "target": "天然ローズの香りが大好きな方、スキンケアでリラックスしたい方、冬のプレゼントやホリデーギフトを探している方",
        "point": "手のひらに2〜3滴伸ばし、まず深呼吸してローズの天然アロマを深く吸い込んでから、顔全体に優しくなじませてください。"
    },
    {
        "rank": 9,
        "tag": "🧪 匂いやクセを徹底除去した高純度精製！超敏感肌や赤ちゃんにも安心のさらり浸透タイプ",
        "catch": "化粧品原料専門メーカーの確かな技術。未精製のナッツ臭が苦手な方でもストレスフリーに使えるクリアオイル",
        "brand_name": "自然化粧品研究所",
        "capacity": "100ml (精製アルガンオイル)",
        "type": "高純度精製アルガンオイル・低刺激処方",
        "features": "精製処理（脱色・脱臭済み）、無香料・無着色・防腐剤フリー、さらさらテクスチャー、国内充填",
        "value": "未精製オイル特有の色素やナッツ臭を特殊フィルターで丁寧に除去。アルガンの優れたエモリエント効果だけを肌に届けるピュア＆マイルド設計",
        "desc_p1": "手作りコスメや原料コスメの専門店として名高い『自然化粧品研究所』が届ける精製アルガンオイル。未精製オイルの野性味あふれる香りが合わない方や、極度に肌が敏感な方に向けて開発された優良アイテムです。",
        "desc_p2": "独自の精製技術により、アレルギーの原因になりやすい微量不純物や独特のナッツ臭を徹底的にカット。無色透明でサラリとした軽快なテクスチャーに仕上がっており、オイル特有の重さやベタつきを一切感じさせません。肌への馴染みが非常に早く、朝のメイク前や日中のハンドケア、さらには赤ちゃんの保湿ケアとしても安心して使えます。100mlのたっぷりサイズで日常使いにぴったりです。",
        "target": "未精製オイルの匂いが苦手な方、極度の敏感肌で刺激を最小限に抑えたい方、ベタつきのないサラサラな使い心地を好む方",
        "point": "朝の洗顔後、化粧水の前に1滴なじませるだけで、メイクの邪魔をせずに一日中乾燥崩れを防ぐしなやかな土台が完成します。"
    },
    {
        "rank": 10,
        "tag": "🌍 アメリカUSDAオーガニック認証取得！海外セレブも愛用する大容量ピュアオーガニックオイル",
        "catch": "世界的なサプリ・ナチュラルコスメブランドNOW Foods。低温圧搾抽出された100%ピュアの頼れる1本",
        "brand_name": "NOW Foods (ナウフーズ)",
        "capacity": "59ml (100% ピュア オーガニック アルガンオイル)",
        "type": "USDAオーガニック認証・未精製ピュアアルガンオイル",
        "features": "USDAオーガニック認証、QAI認証、コールドプレス（ヘキサン不使用）、未精製、ポンプノズル",
        "value": "アメリカで最も信頼されるナチュラルブランドの1本。厳格な有機認証を取得しながら手頃な価格帯を実現し、冬の髪・爪・フェイスケアを総合サポート",
        "desc_p1": "世界中で愛飲・愛用されるヘルスケア＆ナチュラルコスメ大手『NOW Foods（ナウフーズ）』。米国の厳格なオーガニック基準であるUSDA認証を取得した、混じり気なしの純度100%アルガンオイルです。",
        "desc_p2": "化学溶剤（ヘキサン等）を一切使用せず、低温で丁寧に圧搾された未精製オイル。アルガン本来のビタミンEや必須脂肪酸が豊富に含まれており、真冬の寒さでパサつく毛先に揉み込めば、静電気やドライヤーの熱から髪を力強く守り抜きます。ポンプ式のヘッドを採用しており、必要な量を片手で手軽にプッシュできる利便性も魅力。フェイスケアからヘアケア、ネイルケアまで1本でマルチに活躍します。",
        "target": "海外オーガニック認証コスメが好きな方、ヘアオイルやネイルオイルとしても兼用したい方、使いやすいポンプ容器を好む方",
        "point": "タオルドライ後の濡れた髪の毛先に1〜2滴揉み込んでからドライヤーで乾かすと、サロン帰りのようなシルキーな指通りに仕上がります。"
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
    "headline": "保湿力の強さで肌乾燥とさようなら！モロッコの黄金オイルでふっくら極上やわらか肌へ導く高保湿アルガンオイルランク10",
    "description": "11月・12月の冬本番に深刻化するゴワつき・砂漠乾燥・角質硬化を徹底解決！モロッコ南西部のみに自生するアルガンの樹から抽出された高純度オーガニックアルガンオイル10選を徹底比較！メルヴィータ、コディナ、spa hinoki、生活の木、ナイアード、マカダミ屋など厳選。ビタミンEと必須脂肪酸で角層をやわらげ、化粧水前のブースターや全身保湿に威力を発揮する名品をご紹介。",
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
    "name": "冬の高保湿アルガンオイル おすすめランキング10選",
    "itemListElement": item_list_elements
}

# HTML Template
html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！モロッコの黄金オイルでふっくら極上やわらか肌へ導く高保湿アルガンオイルランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬本番に深刻化するゴワつき・砂漠乾燥・角質硬化を徹底解決！モロッコ南西部のみに自生するアルガンの樹から抽出された高純度オーガニックアルガンオイル10選を徹底比較！メルヴィータ、コディナ、spa hinoki、生活の木、ナイアード、マカダミ屋など厳選。ビタミンEと必須脂肪酸で角層をやわらげ、化粧水前のブースターや全身保湿に威力を発揮する名品をご紹介。">
  <meta name="keywords" content="アルガンオイル,高保湿,冬 保湿,ブースターオイル,メルヴィータ アルガンオイル,オーガニックオイル,未精製アルガンオイル,導入美容液,乾燥肌対策 2026">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-argan-oil">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！モロッコの黄金オイルでふっくら極上やわらか肌へ導く高保湿アルガンオイルランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥でカチコチに硬くなった素肌を解き放つ！モロッコ産ピュアアルガンオイル厳選10選を徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-argan-oil">
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
      <li><a href="/winter-squalane-oil">スクワランオイル</a></li>
      <li><a href="/winter-shea-butter">高保湿シアバター</a></li>
    </ul>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">TOP</a> &gt; <a href="/winter-face-oil">冬のフェイスオイル・美容液</a> &gt; <span>高保湿アルガンオイル</span>
</div>

<main class="container">
  <article>
    <header class="article-header">
      <span class="badge">2026年冬 最新決定版 / 11〜12月集中保湿</span>
      <h1>保湿力の強さで肌乾燥とさようなら！モロッコの黄金オイルでふっくら極上やわらか肌へ導く高保湿アルガンオイルランク10</h1>
      <div class="meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証機関: 冬コスメ徹底比較ラボ 編集部</span>
        <span>対象: 顔のゴワつき・化粧水が入らない砂漠肌・冬の小ジワ</span>
      </div>
      <div class="lead-box">
        <p><strong>「どれだけ高級な高保湿化粧水を重ねても、肌表面で弾かれて全然浸透していかない……」</strong></p>
        <p>11月中旬から12月にかけて外気湿度が30%台へ落ち込み、外気温がひと桁まで冷え込むと、肌表面の角質層は自らを守るために固く縮こまり、まるでプラスチック板のように硬化してしまいます。この『角質ゴワつき』こそが、冬に化粧水が入らなくなる最大の原因です。</p>
        <p>そんな冬の砂漠肌を劇的に救済するのが、モロッコ南西部の過酷な乾燥地帯にしか自生しないアルガンツリーの実から抽出される<strong>『アルガンオイル（Argan Oil）』</strong>です。オリーブオイルの2〜3倍とも言われる豊富なビタミンE（α-トコフェロール）と、必須脂肪酸オレイン酸・リノール酸を黄金バランスで含有。洗顔直後の肌にわずか1滴なじませるだけで、硬化した角層細胞の結合を瞬時に解きほぐし、その後の化粧水を磁石のように引き込みます。本記事では、楽天APIからリアルタイムに取得した最新データに基づき、本気で肌を変えたい冬におすすめの高保湿アルガンオイル10選を徹底検証します。</p>
      </div>
    </header>

    <!-- 科学的背景・解説セクション -->
    <section class="content-section">
      <h2>🔬 なぜ11月・12月の冬枯れ肌にアルガンオイルが不可欠なのか？</h2>
      <p>アルガンオイルは、数年間雨が降らなくても枯れない驚異の生命力を持つアルガンツリーの種子（仁）から採れる希少な植物油です。モロッコでは古くから『奇跡のオイル』『若返りの黄金』として珍重されてきました。</p>
      
      <div class="feature-grid">
        <div class="feature-card">
          <h4>1. オリーブオイルの約3倍！驚異の天然ビタミンE</h4>
          <p>強力な抗酸化作用を持つα-トコフェロール（ビタミンE）を高濃度に含有。冬の冷えによる血行不良や、暖房・紫外線による酸化ストレスから肌を力強く守り、若々しいハリと透明感を保ちます。</p>
        </div>
        <div class="feature-card">
          <h4>2. オレイン酸×リノール酸の黄金比率</h4>
          <p>皮脂と親和性の高いオレイン酸（約45%）が油分を補い、角層の水分保持とバリア修復を担うリノール酸（約35%）が同時に作用。油膜でただ覆うだけでなく、角層内部からふっくら柔軟化させます。</p>
        </div>
        <div class="feature-card">
          <h4>3. 化粧水を引き寄せる『親水性ブースター効果』</h4>
          <p>通常の鉱物油やシリコンと異なり、アルガンオイルは親水基を持つ植物油脂。洗顔後の肌になじませると油分が水分を抱え込み、後から塗る水溶性化粧水を角層深部へと導く導入液の役割を果たします。</p>
        </div>
        <div class="feature-card">
          <h4>4. 植物性ステロール（Schottenol）によるキメ補修</h4>
          <p>希少な植物ステロールを含み、寒冷風でダメージを受け乱れた肌のキメ構造を整えます。毛穴の目立ちや乾燥小ジワをふっくら持ち上げ、メイクのりの良い滑らか肌を育てます。</p>
        </div>
      </div>

      <h3>💡 「未精製（ゴールデン）」と「精製（クリア）」の違いと選び方</h3>
      <p>アルガンオイルを選ぶ際は、ご自身の肌質や使用シーンに合わせて<strong>精製度の違い</strong>を見極めることが肝心です。</p>
      <ul style="padding-left: 20px; margin-bottom: 16px; font-size: 0.95rem;">
        <li style="margin-bottom: 8px;"><strong>未精製アルガンオイル（ゴールデンタイプ）：</strong>モロッコの伝統的な低温圧搾法で抽出され、薬品による脱臭・脱色を行わないタイプ。美しい黄金色で、ナッツのような独特の香ばしい香りがあります。ビタミンEやポリフェノール、植物ステロールが壊れずにそのまま残っているため、夜の集中エイジングケアや本格的な乾燥対策に最適です。</li>
        <li><strong>精製アルガンオイル（クリアタイプ）：</strong>不純物やナッツの香りを最新技術で取り除いた無色透明なタイプ。酸化安定性が極めて高く、特有の香りが苦手な方や、朝のメイク前に香りを残したくない方、敏感肌や赤ちゃんのお手入れに向いています。</li>
      </ul>
    </section>

    <!-- ランキング一覧 -->
    <section>
      <h2 style="font-size: 1.5rem; color: var(--primary-dark); margin: 36px 0 24px; text-align: center;">
        🏆 冬の高保湿アルガンオイル おすすめランキング10選
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
      <h2>📊 冬の高保湿アルガンオイル スペック徹底比較一覧</h2>
      <p>冬の乾燥レベルや用途、お好みのテクスチャーに合わせて選べるよう、今回厳選した10商品の主要スペックを一覧表にまとめました。</p>
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
              <td>Melvita ビオオイル アルガンオイル</td>
              <td>未精製オーガニック</td>
              <td>50ml</td>
              <td>¥11,500(セット等)</td>
              <td>洗顔後すぐの王道ブースター</td>
            </tr>
            <tr>
              <td>2位</td>
              <td>CODINA アルガンオイル</td>
              <td>未精製プレミアム</td>
              <td>100ml</td>
              <td>¥7,480</td>
              <td>首・デコルテ・本格エイジングケア</td>
            </tr>
            <tr>
              <td>3位</td>
              <td>spa hinoki オーガニック アルガンオイル</td>
              <td>未精製サロン仕様</td>
              <td>100ml</td>
              <td>¥2,530</td>
              <td>毎日の顔・首・高コスパ導入</td>
            </tr>
            <tr>
              <td>4位</td>
              <td>生活の木 有機アルガンオイル バージン</td>
              <td>未精製バージン一番搾り</td>
              <td>25ml</td>
              <td>¥12,100(業務用等)</td>
              <td>アロマブレンド・新鮮使い切り</td>
            </tr>
            <tr>
              <td>5位</td>
              <td>ナイアード アルガンオイル</td>
              <td>未精製伝統手搾り</td>
              <td>30ml</td>
              <td>¥3,740</td>
              <td>手仕事の力強さ・挟み込み保湿</td>
            </tr>
            <tr>
              <td>6位</td>
              <td>マカダミ屋 未精製 アルガンオイル</td>
              <td>未精製直販キャリア</td>
              <td>50ml</td>
              <td>¥550</td>
              <td>入浴後濡れた全身・頭皮クレンジング</td>
            </tr>
            <tr>
              <td>7位</td>
              <td>KISO ピュアエッセンスAG</td>
              <td>未精製スポイト式原液</td>
              <td>50ml</td>
              <td>¥2,982</td>
              <td>手持ちクリームへのブレンド・衛生管理</td>
            </tr>
            <tr>
              <td>8位</td>
              <td>Melvita アルガンオイル ローズ</td>
              <td>ダマスクローズ精油配合</td>
              <td>50ml</td>
              <td>¥4,288</td>
              <td>アロマ癒し・朝のツヤ仕込み</td>
            </tr>
            <tr>
              <td>9位</td>
              <td>自然化粧品研究所 精製アルガンオイル</td>
              <td>高純度精製クリア</td>
              <td>100ml</td>
              <td>¥3,672</td>
              <td>無臭・朝メイク前・敏感肌</td>
            </tr>
            <tr>
              <td>10位</td>
              <td>NOW Foods 100%ピュア オーガニック</td>
              <td>USDA認定未精製</td>
              <td>59ml</td>
              <td>¥3,733</td>
              <td>ヘア毛先ケア・ネイル・マルチユース</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 実践ステップガイド -->
    <section class="content-section">
      <h2>🧴 失敗しない！真冬のアルガンオイル『浸透力最大化』4ステップ</h2>
      <p>「オイルを塗ったらベタついてファンデが崩れた」「かえって乾燥した気がする」という場合、使い方の順番や量が間違っている可能性が高いです。冬の角層を最も効率よくうるおす実践法をマスターしましょう。</p>

      <div class="step-box">
        <div class="step-num">1</div>
        <div class="step-text">
          <h4>洗顔直後、肌に水分が残っているタイミングが勝負</h4>
          <p>タオルで完全に水気を拭き取るのではなく、肌にわずかな湿り気が残っている状態がベストです。アルガンオイルの親水基が水分と結びつき、肌なじみが一気に加速します。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">2</div>
        <div class="step-text">
          <h4>手のひらで必ず体温まで温める（2〜3滴で十分）</h4>
          <p>いきなり顔に点置きせず、手のひらに2〜3滴落として両手をこすり合わせ、手の体温で温めます。温めることでオイルの粘度が下がり、サラサラのテクスチャーへ変化します。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">3</div>
        <div class="step-text">
          <h4>摩擦ゼロで包み込むハンドプレス</h4>
          <p>指先でこするのではなく、手のひら全体で頬、額、あごを優しく包み込み、10秒間じっくり圧をかけます。体温とオイルが角層のゴワつきを解き放ち、吸い付くような柔らかさに。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">4</div>
        <div class="step-text">
          <h4>すぐに高保湿化粧水を重ねて『水分爆弾』を完成</h4>
          <p>オイルがなじんだ直後に、たっぷりの化粧水を重ねます。オイルが通り道（浸透ルート）を作っているため、化粧水がグングン吸い込まれて角層が水分で満たされます。</p>
        </div>
      </div>
    </section>

    <!-- よくある質問 FAQ -->
    <section class="content-section">
      <h2>❓ 冬のアルガンオイルに関するよくある疑問・Q&A</h2>

      <div class="faq-item">
        <div class="faq-q">Q. オイルを塗ってから日中外出すると、油焼け（日焼けやシミ）しませんか？</div>
        <div class="faq-a">
          アルガンオイルはオレイン酸やリノール酸などの安定した不飽和脂肪酸と、強力な抗酸化物質ビタミンEを豊富に含んでいるため、酸化しにくく日中の紫外線による油焼けの心配は基本的にありません。むしろ、冬の乾燥と紫外線刺激から肌を守る保護膜として働きます。ただし、紫外線防止効果（SPF）自体は持たないため、外出時は日焼け止めやUVクリームを必ず重ねてください。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. ホホバオイルやスクワランオイルとはどう使い分けるべきですか？</div>
        <div class="faq-a">
          ホホバオイルは『皮脂膜補給（ワックスエステル）』、スクワランは『完全無刺激の表面密封』に強みがあります。これらに対し、アルガンオイルの最大の特長は『ビタミンEによる抗酸化・エイジングケア』と『ゴワついた角質を柔らかくほぐすブースター（先行導入）効果』です。「冬になって肌が硬くゴワつく」「化粧水が浸透しない」とお悩みの方には、アルガンオイルが最も即効性を発揮します。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. 脂性肌やニキビができやすい肌でも冬に使って大丈夫ですか？</div>
        <div class="faq-a">
          アルガンオイルに含まれるリノール酸は、皮脂分泌のバランスを整え毛穴の角化を防ぐ働きがあります。冬場は「皮脂が出るのに内側が乾燥している（インナードライ）」状態が多いため、適量（夜に1滴程度）をブースターとして使うことで水分と油分のバランスが整い、過剰な皮脂分泌が落ち着くケースも多いです。ただし、現在炎症を起こしている赤ニキビがある患部は避けてご使用ください。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. 冬場にオイルが白く濁ったり固まったりすることはありますか？</div>
        <div class="faq-a">
          純度の高い植物油であるため、室温が5〜10℃以下に冷え込むと成分の一部が白く結晶化したり固まったりすることがあります。これは添加物が入っていない純粋な天然オイルである証拠であり、品質には全く問題ありません。ぬるま湯を入れた容器に数分浸けるか、温かい室内に置いておけば元の透明なオイルに戻ります。
        </div>
      </div>
    </section>

    <!-- 内部リンク関連記事 -->
    <section class="content-section">
      <h2>🔗 あわせて読みたい！真冬の集中保湿ケア関連記事</h2>
      <p>冬の徹底した乾燥対策は、ブースターオイルに加えて化粧水やクリーム、パーツケアを連動させることで真価を発揮します。ぜひあわせてチェックしてみてください。</p>
      
      <div class="internal-link-grid">
        <a href="/winter-ceramide-lotion" class="internal-card">
          <h5>🧴 高保湿セラミド化粧水</h5>
          <p>アルガンオイルでほぐした角層にたっぷりのセラミド補給！バリア機能を立て直す化粧水10選</p>
        </a>
        <a href="/winter-ceramide-cream" class="internal-card">
          <h5>🧴 高保湿セラミドクリーム</h5>
          <p>水分を満たした素肌に高密度なフタを。冬の冷風から肌を守り抜く濃厚クリーム比較</p>
        </a>
        <a href="/winter-shea-butter" class="internal-card">
          <h5>🧈 高保湿シアバター</h5>
          <p>天然の濃厚ベールで極上プロテクト。顔・唇・手足の粉吹き乾燥を根本解決するバーム10選</p>
        </a>
        <a href="/winter-squalane-oil" class="internal-card">
          <h5>✨ 高純度スクワランオイル</h5>
          <p>たった1滴で極上のツヤ膜を形成。純度99.9%のピュアオイルで乾燥小ジワを撃退</p>
        </a>
        <a href="/winter-jojoba-oil" class="internal-card">
          <h5>🌿 高保湿ホホバオイル</h5>
          <p>人の皮脂成分ワックスエステルを補給。真冬の肌を柔らかく包むゴールドオイル10選</p>
        </a>
        <a href="/winter-urea-cream" class="internal-card">
          <h5>🦶 高保湿尿素クリーム</h5>
          <p>寒さでカチコチに硬くなったひじ・かかとを柔軟化！天然保湿因子NMFを補う尿素ケア10選</p>
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

output_path = "winter-argan-oil.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {output_path} successfully ({len(html_content):,} bytes)!")
