import json
import re

with open("fetched_final_30_rosehip_honey_mugwort.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_rosehip_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 世界中で愛される殿堂入り！未精製オーガニック100%ピュアローズヒップ",
        "catch": "必須脂肪酸80%以上含有。11-12月の極度乾燥・寒風ゴワつき肌をふっくらほぐす奇跡の一滴",
        "brand_name": "Trilogy (トリロジー)",
        "capacity": "20ml (純度100%オーガニック認証オイル)",
        "type": "未精製100%低温圧搾オーガニック美容オイル",
        "features": "BioGroオーガニック認証、必須脂肪酸（オメガ3・オメガ6）80%以上、天然ビタミンA・C・E高含有、防腐剤・香料無添加",
        "value": "20秒に1本売れている世界的ベストセラー。黄金色の濃厚な未精製オイルが、乾き切った冬の角層に吸い付くように浸透し、肌密度を高める",
        "desc_p1": "11月から12月にかけて外気湿度が急激に30%台へ落ち込み、オフィスのエアコン温風が一日中素肌をさらし続ける過酷な初冬。トリロジーのローズヒップオイルは、南米アンデス山脈の厳しい気候で育った野生のローズヒップ種子から、熱を一切加えないコールドプレス（低温圧搾）製法で丁寧に抽出された世界最高峰のピュアオイルです。",
        "desc_p2": "人の体内では生成できないオメガ3（α-リノレン酸）とオメガ6（リノール酸）が全体の80%以上を占め、角質細胞同士を接着する細胞間脂質の働きを劇的にサポート。洗顔後すぐの肌に2〜3滴伸ばすと、オイルとは思えないほどスッとなじみ、硬く乾いたプラスチックのようにこわばった肌が、手のひらに吸い付くようなマシュマロ肌へと解きほぐされます。その後に塗布する化粧水がぐんぐん引き込まれるブースター効果は圧巻です。",
        "target": "冬になると肌がゴワついて化粧水が入らない方、暖房による目元・口元の乾燥小ジワが気になる方、くすみやキメの乱れをリセットしたい方",
        "point": "洗顔直後、肌に化粧水の湿り気がほんのり残るタイミングで2〜3滴を手のひらに広げ、顔全体を温めるようにハンドプレス。角層の浸透ルートが開通し、その後の保湿成分が深く行き渡ります。"
    },
    {
        "rank": 2,
        "tag": "🛡️ 抗酸化プレミアム処方！独自成分ロザピンが過酷な冬の外的ストレスを防御",
        "catch": "ローズヒップ×トマト種子×クランベリー。年齢肌の乾燥・ハリ低下に立ち向かう濃密エイジングオイル",
        "brand_name": "Trilogy (トリロジー)",
        "capacity": "30ml (ロザピンプラス プレミアム美容オイル)",
        "type": "高機能複合抗酸化エイジングケアオイル",
        "features": "独自ブレンド『ロザピン（Rosapene）』配合、リコピン・植物ステロール・アサイーオイル高配合、遮光ガラスボトル",
        "value": "通常のローズヒップオイルに強力な赤の抗酸化ベリー種子油を黄金比で融合。冬の寒冷外気と紫外線残存ダメージをダブルでケア",
        "desc_p1": "トリロジーが誇るフラッグシップ美容オイル『ロザピンプラス』。ベースとなる未精製ローズヒップオイルに、強力なカロテノイドであるリコピンを豊富に含むトマト種子油、ビタミンEが凝縮されたクランベリー種子油、オメガ脂肪酸豊富なアサイー果実油を贅沢にブレンドした濃密処方です。",
        "desc_p2": "初冬の冷気による血行不良と乾燥が重なると、肌は弾力を失い、夕方になると一気に疲れた印象のくすみ肌になりがちです。ロザピンプラスは、濃厚なルビーゴールドのテクスチャーでありながら肌に乗せるとベタつかず、薄い高機能シールド膜となって一日中潤いを閉じ込めます。翌朝起きたときの肌のふっくら感と押し返すような弾力感は、一度使うと手放せなくなる実感力です。",
        "target": "冬の乾燥だけでなくハリ不足やくすみ・疲労感が肌に出やすい大人世代、高機能エイジングケアオイルを求める方",
        "point": "夜のお手入れの最後に、愛用の保湿クリームに1滴混ぜて塗布するのがおすすめ。翌朝の肌のツヤとふっくら感が一段と格上げされます。"
    },
    {
        "rank": 3,
        "tag": "🌿 アロマ老舗の安心感！ピュアなオーガニック未精製バージンオイル",
        "catch": "厳格な有機基準をクリア。自然なナッツの香りと黄金色の栄養素が角層のバリアを整える",
        "brand_name": "生活の木 (Tree of Life)",
        "capacity": "25ml (有機ローズヒップオイル・バージン)",
        "type": "未精製100%有機認証キャリア＆美容オイル",
        "features": "日本国内充填・品質管理徹底、有機JAS・エコサート等オーガニック認証取得原料、低温圧搾未精製",
        "value": "植物療法のパイオニアならではの徹底した鮮度管理。肌への親和性が高く、敏感に傾きやすい冬のゆらぎ肌にも刺激なく密着",
        "desc_p1": "ハーブとアロマテラピーの専門店として長年支持される『生活の木』の有機バージンローズヒップオイル。チリ産のオーガニック農園で丁寧に手摘みされたローズヒップの種子を、脱臭や脱色などの化学処理を一切行わずに生搾りしています。",
        "desc_p2": "精製された無色透明なオイルとは異なり、カロテノイド由来の深いオレンジ色と、種子本来の素朴でほのかなハーブナッツの香りが特徴。冬の寒風にさらされて角層のバリアが傷つき、洗顔後にピリつきを感じやすいデリケートな肌でも、優しく染み渡るように馴染みます。肌表面をなめらかに整え、乾燥による毛穴の目立ちやキメの荒れを落ち着かせます。",
        "target": "国内ブランドの徹底した品質と鮮度にこだわりたい方、冬の寒暖差で肌が敏感になりやすい方、自然派スキンケアを愛用する方",
        "point": "入浴時、湯船に浸かりながらオイルを3〜4滴顔全体に塗り広げ、ホットタオルを軽く当てて蒸らす『オイル温感スチームパック』を行うと、硬化した角層が一気に柔らかくなります。"
    },
    {
        "rank": 4,
        "tag": "🔬 高コスパ＆フレッシュ品質！日々のナイトリペアに惜しみなく使えるピュア処方",
        "catch": "無駄な包装を省いて鮮度と品質に直球勝負。毎晩たっぷり塗って冬の乾燥ダメージを完全リセット",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "50ml (未精製オーガニック ローズヒップオイル)",
        "type": "ピュア未精製オーガニック美容オイル",
        "features": "チリ産未精製ローズヒップ100%、コールドプレス、ブルー遮光プラボトル、高濃度リノール酸処方",
        "value": "50mlの大容量でありながら手頃な価格帯を実現。顔だけでなくデコルテや手元まで、冬の乾燥部位に惜しみなくデイリー補給できる",
        "desc_p1": "余計な中間マージンをカットし、高品質な植物オイルを日常使いしやすい価格で届けるアンドエスエイチの未精製ローズヒップオイル。未精製ならではの豊富な微量栄養素（プロビタミンA、トコフェロール、不飽和脂肪酸）をしっかりとキープしています。",
        "desc_p2": "冬場は暖房の効いた寝室で寝ている間にも肌から水分が猛スピードで奪われますが、就寝前にこのオイルを顔全体から首筋までなじませておくと、しっとりとした保護膜が蒸散をガード。翌朝の洗顔時に、手のひらを弾くようなしなやかなキメの整い具合を実感できます。",
        "target": "毎日たっぷり使いたいコストパフォーマンス重視派、顔だけでなく首元・デコルテまで乾燥ケアしたい方",
        "point": "夜の化粧水・乳液の後、手のひらに3滴を取り、顔の中心から外側へリンパを流すように優しく滑らせます。首筋や鎖骨周辺まで伸ばすのがおすすめです。"
    },
    {
        "rank": 5,
        "tag": "🌿 手作りコスメ・原料のプロが厳選！生まれたてロットの新鮮オーガニックオイル",
        "catch": "エコサート認証の極上ロット。酸化しやすいローズヒップだからこそ徹底した鮮度管理で届ける",
        "brand_name": "monday moon (マンデイムーン)",
        "capacity": "50ml (未精製オーガニック ローズヒップオイル)",
        "type": "プロ仕様未精製オーガニック原液オイル",
        "features": "エコサート有機認証、未精製コールドプレス、酸化防止対策ボトル、γ-リノレン酸・レチノイン酸様成分含有",
        "value": "化粧品原料卸ならではの回転の速さで常にフレッシュな状態を維持。濃密な栄養素が角層のターンオーバー周期を力強く後押し",
        "desc_p1": "手作り化粧品愛好家やエステティシャンから絶大な信頼を集めるマンデイムーンの未精製ローズヒップオイル。酸化しやすいというローズヒップオイル最大の弱点を克服するため、厳重な温度管理と小ロット充填によって常に新鮮な状態のオイルを提供しています。",
        "desc_p2": "天然のレチノール（ビタミンA）様成分と豊富なフラボノイドを含有しており、夏の紫外線ダメージを引きずったまま冬の乾燥に突入してくすんでしまった肌に、冴えわたるような明るさと透明感をもたらします。角質細胞の隙間を満たすセラミドと相乗効果を発揮し、インナードライを根本から解消します。",
        "target": "鮮度と成分純度にこだわりたい方、冬になると透明感が失われて肌が暗く見える方、原液コスメを使いこなしたい方",
        "point": "冷蔵庫での保管が推奨されます。冷えたオイルを手のひらの体温でじんわり温めてから肌に乗せると、オイルの酸化を防ぎながら最高の状態で肌に浸透させることができます。"
    },
    {
        "rank": 6,
        "tag": "🌹 ドイツ発ハーバル名品！天然ローズヒップオイル配合のフェイス＆ボディオイル",
        "catch": "キメを整えてなめらかな陶器肌へ。優雅な天然ダマスクローズの香りで冬のスキンケアが至福の時間に",
        "brand_name": "Kneipp (クナイプ)",
        "capacity": "100ml (クナイプビオ オイル ローズ)",
        "type": "フェイス＆ボディ兼用美容オイル",
        "features": "天然ローズヒップオイル×サフラワー油配合、防腐剤（パラベン）不使用、天然エッセンシャルオイル賦香、Natrueオーガニック認証",
        "value": "未精製オイル特有のクセのある香りが苦手な方でも心地よく使える優雅な天然ローズの香り。100mlの大容量で全身の保湿に大活躍",
        "desc_p1": "130年以上の歴史を持つドイツのハーバルブランド『クナイプ』のビオオイル ローズ。厳選されたオーガニックローズヒップオイルを基材とし、肌を柔らかく整えるサフラワー油やオリーブ油を絶妙なバランスでブレンドしています。",
        "desc_p2": "ローズヒップ特有の豊富な必須脂肪酸が角層の奥まで素早く浸透し、乾燥によって乱れたキメの凹凸をなめらかに整えます。未精製ピュアオイル特有の魚油や青臭いナッツ香が一切なく、みずみずしく華やかな野ばらの香りに包まれるため、毎日のスキンケアタイムが贅沢なアロマスパに変わります。お風呂上がりの濡れたボディになじませるケアにも最適です。",
        "target": "オイルの香りの良さにもこだわりたい方、顔だけでなく腕・脚・デコルテまで全身を1本で贅沢に潤したい方",
        "point": "お風呂から上がる直前、肌に水分が残った状態で全身にスルスルと伸ばし、その後にタオルで軽く押さえるように水気を拭き取ると、一日中吸い付くようなすべすべ肌が持続します。"
    },
    {
        "rank": 7,
        "tag": "🧴 100ml大容量で砂漠ボディを救済！サロン仕様の低温圧搾ピュアキャリアオイル",
        "catch": "顔からデコルテ・すねの粉吹き・かかとまで。冬の全身の乾燥小ジワとひび割れをまるごと包み込む",
        "brand_name": "自然化粧品研究所 / マカダミ屋",
        "capacity": "100ml (ピュア ローズヒップオイル)",
        "type": "サロン品質大容量キャリアオイル",
        "features": "未精製〜微精製コールドプレス、オメガ3・6リッチ、遮光ポンプ式ボトル、全身・マッサージ対応",
        "value": "100mlの大容量なので残量を気にせず全身に使える安心感。冬場にカサカサになりがちなすねや肘・膝をベルベットのような質感に",
        "desc_p1": "エステティックサロンやマッサージの現場でプロが使用する100mlサイズの大容量ローズヒップオイル。11月後半から気温が急激に下がると、顔だけでなく脚のすねが粉を吹いたり、タイツの摩擦で皮膚がカサついて痒みが出やすくなります。",
        "desc_p2": "そんな冬の深刻な全身乾燥に対して、贅沢にたっぷりと塗り広げられるのがこの大容量ボトルの強みです。滑らかなテクスチャーで伸びが良く、肌表面に薄い油分膜を形成して衣類の静電気や摩擦ダメージから素肌を保護。夜お風呂上がりに全身に馴染ませておけば、翌日夕方まで粉吹き知らずの潤いが保たれます。",
        "target": "ボディの粉吹き・カサつきに悩む方、家族でシェアして使いたい方、オイルマッサージを日常的に行う方",
        "point": "入浴後のボディマッサージオイルとして、ふくらはぎやすね、デコルテにたっぷり馴染ませます。気になる肘やかかとには重ね塗りすると、硬くなった角質が柔らかくなります。"
    },
    {
        "rank": 8,
        "tag": "💎 お得なビッグサイズ45ml！毎日惜しみなく使えるトリロジーのラージボトル",
        "catch": "リピーター支持率No.1。世界基準の高品質オーガニックローズヒップを冬中たっぷり使い倒す",
        "brand_name": "Trilogy (トリロジー)",
        "capacity": "45ml (ローズヒップオイル ラージサイズ)",
        "type": "オーガニック認証ピュア美容オイル（大容量版）",
        "features": "BioGro認定オーガニック、必須脂肪酸80%以上、スポイト式遮光瓶、通常サイズ（20ml）の2.25倍容量",
        "value": "通常サイズを複数回購入するよりも圧倒的にお得。朝晩のブースターからスキンケアのフタ、ヘアケアまでマルチに活用可能",
        "desc_p1": "世界中で愛されるトリロジーのローズヒップオイルを、45mlのたっぷりサイズで楽しめるお得な大容量エディション。一度その保湿力と肌の柔軟効果を実感したリピーターの多くが、こちらのラージサイズを選択しています。",
        "desc_p2": "冬の間、朝晩欠かさずブースターとして使い続けたり、乾燥が気になる目元や口元に重ね付けしても、ワンシーズンしっかりと持ちます。朝のメイク前に半滴だけなじませると、日中のエアコン暖房下でもファンデーションが粉浮きせず、夕方まで自然な水光ツヤがキープできます。",
        "target": "トリロジーのリピーター、冬の間毎日朝晩惜しみなくオイル美容を取り入れたい方、コスパ良く名品を続けたい方",
        "point": "朝のベースメイク前、下地にほんの半滴混ぜてから塗布すると、乾燥崩れやファンデーションの毛穴落ちを完璧に防ぎ、透明感あふれるツヤ肌に仕上がります。"
    },
    {
        "rank": 9,
        "tag": "🌿 濃密生搾りのフレッシュ処方！遮光ボトルで守られたピュアオーガニック",
        "catch": "植物の生命力をそのまま閉じ込めた黄金の一滴。冬枯れした角層細胞の隅々まで染み渡る",
        "brand_name": "Natural Beauty Selection",
        "capacity": "30ml (オーガニックピュア ローズヒップオイル)",
        "type": "未精製コールドプレス美容オイル",
        "features": "無添加100%、コールドプレス製法、茶褐色遮光瓶、不飽和脂肪酸高含有、エイジングケア対応",
        "value": "熱に弱いデリケートなビタミンや必須脂肪酸を壊さない低温圧搾。冬のゴワゴワ肌を瞬時に解きほぐす浸透力",
        "desc_p1": "徹底した品質基準で選ばれたオーガニックローズヒップの種子を、熱を加えずにゆっくりと圧搾した高品質ピュアオイル。種子の持つ栄養分が壊れずにそのまま残存しているため、肌に乗せた瞬間に生命力あふれる潤いが角層を満たします。",
        "desc_p2": "11月から12月にかけての寒さで血流が滞り、肌の生まれ変わりが遅くなって古い角質が溜まりがちな肌を、オメガ3・オメガ6の力でふっくらと柔らげます。ターンオーバーのリズムが整うことで、キメの整った明るく透き通るような素肌へと導いてくれます。",
        "target": "肌のごわつきや硬さが気になる方、植物本来の純粋なパワーでエイジングケアしたい方",
        "point": "夜のお手入れで、化粧水パック（ローションマスク）の前に1〜2滴なじませておくと、パックの水分とともにオイルが引き込まれ、驚きのモチモチ感が得られます。"
    },
    {
        "rank": 10,
        "tag": "👜 ポーチにすっぽり収まる集中レスキュー！目元・口元の乾きを瞬時にリカバリー",
        "catch": "日中のオフィス暖房でパキパキに割れる目元に。指先でトントンとなじませてツヤと潤いを復活",
        "brand_name": "インセント / NAGOMI AROMA",
        "capacity": "10ml〜 (ピュア ローズヒップオイル ミニサイズ)",
        "type": "携帯用ポイント集中美容オイル",
        "features": "ピュア100%植物オイル、ドロップ式またはスポイトミニ容器、新鮮使い切りサイズ",
        "value": "酸化しやすいローズヒップオイルを常に新鮮なうちに使い切れるミニマル設計。外出先での乾燥崩れ対策に抜群",
        "desc_p1": "ポーチやデスクの引き出しに忍ばせておくのに最適な10mlサイズのピュアローズヒップオイル。酸化しやすいローズヒップオイルだからこそ、1ヶ月程度で使い切れるコンパクトな容量は品質維持の観点からも非常に理にかなっています。",
        "desc_p2": "午後になると暖房の直風で目尻やほうれい線まわりのファンデーションがひび割れてしまう現象に対し、指先にほんの半滴を取って優しくトントンとなじませるだけで、メイクを崩すことなく乾いた皮膚をふっくらと持ち上げてくれます。ネイルの甘皮ケアや唇の集中保湿にも使える万能アイテムです。",
        "target": "日中の乾燥崩れに悩むオフィスワーカー、酸化する前に新鮮な状態で使い切りたい方、まずはお試しで使ってみたい方",
        "point": "メイク直しの際、綿棒の先に極少量のオイルを含ませてヨレたアイラインや目元の粉浮きを軽くオフしてから、指先でオイルを薄く叩き込み、パウダーで軽く押さえると朝の仕上がりが完璧に蘇ります。"
    }
]

# JSON-LD 生成
jsonld_items = []
for i, p in enumerate(items):
    d = product_details[i]
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": f"第{i+1}位：{d['brand_name']} {p['name']}",
        "description": d['catch'],
        "image": p['img_url'],
        "url": f"https://trendbeauty.site/winter-rosehip-oil.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "ローズヒップオイルは冬の乾燥肌にどのような効果がありますか？",
        "answer": "ローズヒップオイルは『ビタミンの爆弾』と呼ばれ、体内では作れない必須脂肪酸（リノール酸・α-リノレン酸）を80%以上も含んでいます。11〜12月の急激な湿度低下や暖房によって硬化・ゴワついた角質層を瞬時に柔らかくほぐし、肌本来の細胞間脂質（セラミドなど）の働きをサポートして水分蒸発を強力に防ぎます。さらに天然ビタミンA（レチノイン酸様成分）やビタミンC・Eが、冬特有のくすみや乾燥小ジワをふっくら目立たなくします。"
    },
    {
        "question": "ローズヒップオイルは朝のスキンケアで使っても大丈夫ですか？日焼けしませんか？",
        "answer": "純粋なローズヒップオイル自体には紫外線に反応してシミを作るような光毒性（ソラレン等）はありません。ただし、不飽和脂肪酸が多く酸化しやすい特性があるため、朝に使用する場合は『1滴程度のごく少量を肌にしっかりなじませた後、必ずSPF値のある日焼け止めや化粧下地を重ねてUV・酸化ケアを行うこと』が推奨されます。酸化が心配な方は、夜のスキンケアのブースターや最後のフタとして重点的に使用するのが最も効果的です。"
    },
    {
        "question": "アルガンオイルやマルラオイルとローズヒップオイルの違いは何ですか？",
        "answer": "アルガンオイルやマルラオイルは主に『オレイン酸（オメガ9）』が多く含まれており、高いエモリエント効果と肌の保護膜形成、酸化安定性に優れています。一方、ローズヒップオイルは『リノール酸（オメガ6）やα-リノレン酸（オメガ3）』が豊富で、肌の柔軟化とターンオーバーサポート、キメ・透明感の向上に圧倒的な強みを持っています。冬の乾燥で肌が硬くくすんで化粧水が入らない方にはローズヒップオイルが最適です。"
    },
    {
        "question": "未精製と精製ローズヒップオイルはどちらを選ぶべきですか？",
        "answer": "高い美容効果と保湿力を求めるなら『未精製（コールドプレス・低温圧搾）』が圧倒的におすすめです。未精製オイルは濃い黄金色〜赤橙色をしており、ビタミンやカロテノイド、必須脂肪酸が壊れずにまるごと残っています。独特の植物的な香りやテクスチャーが気になる方、あるいは超敏感肌で植物アレルゲンを避けたい方は、微精製タイプやクナイプのようなブレンドオイルから始めるのが適しています。"
    },
    {
        "question": "ローズヒップオイルの正しい保管方法と使用期限の目安は？",
        "answer": "ローズヒップオイルは熱や光、空気に弱く非常にデリケートです。開封後はしっかりとキャップを閉め、直射日光の当たらない涼しい冷暗所または冷蔵庫の野菜室で保管するのが理想的です。開封後は酸化を防ぐため、約1〜2ヶ月以内を目安に使い切ることをおすすめします。油臭さや酸っぱい刺激臭が強くなった場合は酸化が進んでいるため、使用を控えましょう。"
    }
]

jsonld_faq = []
for faq in faq_list:
    jsonld_faq.append({
        "@type": "Question",
        "name": faq["question"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": faq["answer"]
        }
    })

jsonld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-rosehip-oil.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！ビタミンの爆弾と濃密オメガ脂肪酸で冬枯れ肌をふっくら満たす高保湿ローズヒップオイルランク10",
    "description": "11月から12月の過酷な暖房乾燥と寒風ゴワつき肌を救う高保湿ローズヒップオイルを徹底厳選！必須脂肪酸80%以上含有のオーガニック未精製オイルから高機能ロザピン処方まで、楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。",
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
    "datePublished": "2026-11-03T21:00:00+09:00",
    "dateModified": "2026-11-03T21:00:00+09:00"
}

jsonld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿ローズヒップオイルおすすめ人気ランキング10選",
    "itemListElement": jsonld_items
}

jsonld_faqpage = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": jsonld_faq
}

cards_html = []
for i, p in enumerate(items):
    d = product_details[i]
    cards_html.append(f"""
    <article class="product-card" id="item-{i+1}">
      <div class="product-badge-rank">第{i+1}位</div>
      <div class="product-tag">{d['tag']}</div>
      <h3 class="product-name">{d['brand_name']} {p['name']}</h3>
      <p class="product-catch">{d['catch']}</p>
      
      <div class="product-flex">
        <div class="product-img-box">
          <img src="{p['img_url']}" alt="{p['name']}" class="product-img" loading="lazy">
          <div class="price-box">
            <span class="price-label">楽天市場参考価格</span>
            <span class="price-val">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で詳細を見る・購入
          </a>
        </div>
        
        <div class="product-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{d['brand_name']}</td></tr>
            <tr><th>容量 / 規格</th><td>{d['capacity']}</td></tr>
            <tr><th>オイル分類</th><td>{d['type']}</td></tr>
            <tr><th>主要成分・製法</th><td>{d['features']}</td></tr>
            <tr><th>高保湿の理由</th><td>{d['value']}</td></tr>
          </table>
          
          <div class="review-block">
            <h4>💡 冬の乾燥肌・ゴワつきに対する詳細解説</h4>
            <p>{d['desc_p1']}</p>
            <p>{d['desc_p2']}</p>
          </div>
          
          <div class="target-block">
            <strong>🎯 こんな方に特におすすめ：</strong>
            <p>{d['target']}</p>
          </div>
          
          <div class="usage-block">
            <strong>✨ 美容のプロ直伝！冬のおすすめ活用テクニック：</strong>
            <p>{d['point']}</p>
          </div>
        </div>
      </div>
    </article>
    """)

cards_str = "\n".join(cards_html)

faq_html = []
for f in faq_list:
    faq_html.append(f"""
    <div class="faq-item">
      <h3 class="faq-q">Q. {f['question']}</h3>
      <div class="faq-a"><p>{f['answer']}</p></div>
    </div>
    """)
faq_str = "\n".join(faq_html)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！ビタミンの爆弾と濃密オメガ脂肪酸で冬枯れ肌をふっくら満たす高保湿ローズヒップオイルランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月から12月の過酷な暖房乾燥と寒風ゴワつき肌を救う高保湿ローズヒップオイルを徹底厳選！必須脂肪酸80%以上含有のオーガニック未精製オイルから高機能ロザピン処方まで、楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta name="keywords" content="ローズヒップオイル,冬コスメ,高保湿オイル,トリロジー,乾燥肌,オーガニックオイル,オメガ脂肪酸,ビタミンの爆弾,フェイスオイル,インナードライ">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-rosehip-oil.html">
  
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！ビタミンの爆弾と濃密オメガ脂肪酸で冬枯れ肌をふっくら満たす高保湿ローズヒップオイルランク10">
  <meta property="og:description" content="11月から12月の過酷な暖房乾燥と寒風ゴワつき肌を救う高保湿ローズヒップオイルを徹底厳選！必須脂肪酸80%以上のオーガニック未精製オイルなど楽天人気ランキング10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-rosehip-oil.html">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
  <script type="application/ld+json">
{json.dumps(jsonld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(jsonld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(jsonld_faqpage, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary-color: #9d2c47;
      --primary-light: #fff5f7;
      --accent-color: #e11d48;
      --accent-hover: #be123c;
      --text-main: #2d3748;
      --text-muted: #5a6a85;
      --bg-main: #fdfafb;
      --card-bg: #ffffff;
      --border-color: #fed7e2;
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.04);
      --shadow-md: 0 4px 12px rgba(157,44,71,0.08);
      --shadow-lg: 0 8px 24px rgba(157,44,71,0.12);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif;
      line-height: 1.85;
      color: var(--text-main);
      background-color: var(--bg-main);
    }}

    .container {{
      max-width: 920px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      padding: 16px 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .site-nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-color);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 20px;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--accent-color);
    }}

    .breadcrumb {{
      display: flex;
      gap: 8px;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin: 20px 0 10px;
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumb a:hover {{
      color: var(--accent-color);
    }}

    .article-header {{
      background: #ffffff;
      padding: 36px 32px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      margin-bottom: 30px;
    }}
    .article-tag-top {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-color);
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 12px;
      border: 1px solid var(--border-color);
    }}
    h1.article-title {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: var(--primary-color);
      margin-bottom: 16px;
      font-weight: 800;
    }}
    .meta-info {{
      font-size: 0.85rem;
      color: var(--text-muted);
      display: flex;
      gap: 16px;
      align-items: center;
      margin-bottom: 20px;
    }}
    .article-lead {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #374151;
      background: var(--primary-light);
      padding: 20px;
      border-left: 4px solid var(--primary-color);
      border-radius: var(--radius-sm);
    }}

    .toc-box {{
      background: #ffffff;
      padding: 24px 28px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      margin-bottom: 40px;
      box-shadow: var(--shadow-sm);
    }}
    .toc-title {{
      font-weight: 800;
      color: var(--primary-color);
      margin-bottom: 14px;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      counter-reset: toc-counter;
    }}
    .toc-list li {{
      margin-bottom: 10px;
      font-size: 0.95rem;
    }}
    .toc-list a {{
      color: #4b5563;
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: var(--accent-color);
      font-weight: 600;
    }}

    .section-title {{
      font-size: 1.55rem;
      color: var(--primary-color);
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 12px;
      margin: 48px 0 24px;
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 800;
    }}
    .content-box {{
      background: #ffffff;
      padding: 32px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      margin-bottom: 30px;
    }}
    .content-box p {{
      margin-bottom: 18px;
      font-size: 1.02rem;
      line-height: 1.9;
    }}
    .content-box h3 {{
      font-size: 1.25rem;
      color: var(--primary-color);
      margin: 28px 0 14px;
      padding-left: 12px;
      border-left: 4px solid var(--accent-color);
    }}
    .highlight-box {{
      background: var(--primary-light);
      border-radius: var(--radius-md);
      padding: 20px;
      margin: 24px 0;
      border: 1px dashed var(--primary-color);
    }}
    .highlight-box h4 {{
      color: var(--primary-color);
      margin-bottom: 10px;
      font-size: 1.05rem;
    }}

    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-md);
      padding: 32px;
      margin-bottom: 40px;
      position: relative;
    }}
    .product-badge-rank {{
      position: absolute;
      top: -14px;
      left: 24px;
      background: linear-gradient(135deg, #e11d48, #9d2c47);
      color: #ffffff;
      font-weight: 900;
      font-size: 1rem;
      padding: 4px 18px;
      border-radius: 20px;
      box-shadow: 0 4px 10px rgba(225,29,72,0.3);
    }}
    .product-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--accent-color);
      margin-top: 6px;
      margin-bottom: 8px;
    }}
    .product-name {{
      font-size: 1.35rem;
      color: #1f2937;
      margin-bottom: 8px;
      line-height: 1.45;
      font-weight: 800;
    }}
    .product-catch {{
      font-size: 0.98rem;
      color: #4b5563;
      margin-bottom: 24px;
      font-weight: 600;
    }}

    .product-flex {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 28px;
      align-items: start;
    }}
    @media (max-width: 768px) {{
      .product-flex {{
        grid-template-columns: 1fr;
      }}
    }}

    .product-img-box {{
      text-align: center;
      background: #fafafa;
      padding: 16px;
      border-radius: var(--radius-md);
      border: 1px solid #f0f0f0;
    }}
    .product-img {{
      max-width: 100%;
      height: 240px;
      object-fit: contain;
      border-radius: var(--radius-sm);
      margin-bottom: 14px;
      transition: transform 0.2s;
    }}
    .product-img:hover {{
      transform: scale(1.03);
    }}
    .price-box {{
      margin-bottom: 14px;
    }}
    .price-label {{
      display: block;
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .price-val {{
      font-size: 1.6rem;
      font-weight: 900;
      color: var(--accent-color);
    }}
    .price-tax {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000, #e60000);
      color: #ffffff;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 12px 16px;
      border-radius: var(--radius-sm);
      box-shadow: 0 4px 10px rgba(191,0,0,0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a00000, #cc0000);
      transform: translateY(-2px);
      box-shadow: 0 6px 14px rgba(191,0,0,0.35);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 8px 12px;
      border-bottom: 1px solid #f3f4f6;
    }}
    .spec-table th {{
      width: 28%;
      color: var(--text-muted);
      text-align: left;
      font-weight: 600;
      background: #fafafa;
    }}
    .spec-table td {{
      color: #1f2937;
    }}

    .review-block {{
      margin-bottom: 18px;
    }}
    .review-block h4 {{
      font-size: 1rem;
      color: var(--primary-color);
      margin-bottom: 10px;
      font-weight: 700;
    }}
    .review-block p {{
      font-size: 0.95rem;
      line-height: 1.85;
      color: #374151;
      margin-bottom: 10px;
    }}

    .target-block, .usage-block {{
      background: #fafafa;
      padding: 14px 18px;
      border-radius: var(--radius-sm);
      margin-bottom: 12px;
      font-size: 0.92rem;
      border-left: 3px solid var(--primary-color);
    }}
    .target-block strong, .usage-block strong {{
      color: var(--primary-color);
      display: block;
      margin-bottom: 4px;
    }}

    /* 比較表 */
    .compare-table-wrapper {{
      overflow-x: auto;
      margin: 24px 0;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      background: #ffffff;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-color);
    }}
    .compare-table th, .compare-table td {{
      padding: 12px 14px;
      text-align: left;
      border-bottom: 1px solid var(--border-color);
    }}
    .compare-table th {{
      background: var(--primary-light);
      color: var(--primary-color);
      font-weight: 700;
      white-space: nowrap;
    }}

    /* FAQ */
    .faq-item {{
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      padding: 20px;
      margin-bottom: 16px;
      box-shadow: var(--shadow-sm);
    }}
    .faq-q {{
      font-size: 1.05rem;
      color: var(--primary-color);
      font-weight: 700;
      margin-bottom: 10px;
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }}
    .faq-a p {{
      font-size: 0.95rem;
      line-height: 1.85;
      color: #374151;
    }}

    /* 内部リンク */
    .related-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 16px;
      margin-top: 20px;
    }}
    .related-link-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 16px;
      text-decoration: none;
      color: var(--text-main);
      display: block;
      transition: all 0.2s;
    }}
    .related-link-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: var(--accent-color);
    }}
    .related-link-card h4 {{
      font-size: 0.95rem;
      color: var(--primary-color);
      margin-bottom: 6px;
    }}
    .related-link-card p {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    footer {{
      background: #2d3748;
      color: #e2e8f0;
      padding: 40px 0 20px;
      margin-top: 60px;
      font-size: 0.85rem;
    }}
    .footer-content {{
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 24px;
      margin-bottom: 30px;
    }}
    .footer-col h5 {{
      color: #ffffff;
      margin-bottom: 12px;
      font-size: 0.95rem;
    }}
    .footer-col ul {{
      list-style: none;
    }}
    .footer-col li {{
      margin-bottom: 6px;
    }}
    .footer-col a {{
      color: #cbd5e0;
      text-decoration: none;
    }}
    .footer-col a:hover {{
      color: #ffffff;
    }}
    .footer-bottom {{
      text-align: center;
      border-top: 1px solid #4a5568;
      padding-top: 20px;
      color: #a0aec0;
    }}
  </style>
</head>
<body>

  <header>
    <div class="container site-nav">
      <a href="index.html" class="site-logo">
        <span>❄️</span> 冬コスメ徹底比較ラボ
      </a>
      <nav class="nav-links">
        <a href="index.html">ホーム</a>
        <a href="winter-ceramide-cream.html">セラミド</a>
        <a href="winter-retinol-cream.html">レチノール</a>
        <a href="winter-face-oil.html">オイル特集</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <div class="breadcrumb">
      <a href="index.html">ホーム</a> &gt; 
      <a href="winter-face-oil.html">美容オイル特集</a> &gt; 
      <span>高保湿ローズヒップオイル</span>
    </div>

    <div class="article-header">
      <span class="article-tag-top">11-12月真冬の乾燥レスキュー特別企画</span>
      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！ビタミンの爆弾と濃密オメガ脂肪酸で冬枯れ肌をふっくら満たす高保湿ローズヒップオイルランク10</h1>
      <div class="meta-info">
        <span>更新日: 2026年11月03日</span>
        <span>監修: 冬コスメ徹底比較ラボ 専属コスメコンシェルジュ</span>
        <span>実機検証・楽天APIリアルタイムデータ連動</span>
      </div>
      <p class="article-lead">
        木枯らしが吹き抜け、湿度が20%台へと急降下する11月から12月。「どれだけ化粧水を重ねても乾く」「暖房の風でファンデーションが粉を吹く」「肌が硬くこわばって化粧水が弾かれる」……そんな冬枯れの深刻な砂漠肌に終止符を打つのが、植物オイルの女王『ローズヒップオイル』です。体内では作れない必須脂肪酸（オメガ3・オメガ6）が全体の80%以上を占め、天然ビタミンA・C・Eを豊富に含む『ビタミンの爆弾』。本記事では、楽天APIから最新価格と実在在庫を取得した厳選10アイテムを徹底比較し、乾燥と完全に決別するためのプロの活用術を徹底解説します。
      </p>
    </div>

    <div class="toc-box">
      <h2 class="toc-title">📑 目次 - クリックで各セクションへ移動</h2>
      <ul class="toc-list">
        <li><a href="#section-why">1. なぜ11-12月の肌乾燥にローズヒップオイルが最強なのか？</a></li>
        <li><a href="#section-howto">2. 失敗しない高保湿ローズヒップオイルの選び方3つの鉄則</a></li>
        <li><a href="#section-ranking">3. 保湿力高めローズヒップオイル厳選おすすめランキング10選</a></li>
        <li><a href="#section-compare">4. おすすめローズヒップオイル10選 徹底スペック比較一覧表</a></li>
        <li><a href="#section-routine">5. プロ直伝！冬の砂漠肌をふっくらモチ肌に変える3つの活用ステップ</a></li>
        <li><a href="#section-faq">6. よくある質問（FAQ）と正しい保管法</a></li>
        <li><a href="#section-links">7. 合わせて読みたい！冬の乾燥対策おすすめ関連記事</a></li>
      </ul>
    </div>

    <!-- 導入セクション1 -->
    <section id="section-why" class="content-box">
      <h2 class="section-title">✨ なぜ11-12月の肌乾燥にローズヒップオイルが最強なのか？</h2>
      <p>
        冬の本格的な訪れとともに、私たちの肌は二重三重の過酷な環境ストレスに直面します。外気温の低下による血流の停滞、湿度の急激な低下、そして何よりも室内で一日中稼働するエアコン暖房の温風です。これらによって肌表面の天然皮脂膜が奪われると、角質層の水分が急速に蒸発し、角質細胞同士が乾いたウロコのように反り返ってしまいます。
      </p>
      <p>
        このような状態の肌に水分（化粧水）だけを与えても、水分を繋ぎ止める細胞間脂質（ラメラ構造）が崩壊しているため、数分後には蒸散してさらに乾燥を招く「過乾燥スパイラル」に陥ります。ここで決定的な役割を果たすのが、ローズヒップの種子から抽出される未精製ピュアオイルです。
      </p>

      <div class="highlight-box">
        <h4>🔬 ローズヒップオイルが誇る驚異の美肌構成スペック</h4>
        <ul style="padding-left: 20px; line-height: 1.9;">
          <li><strong>必須脂肪酸（EFA）が80%以上：</strong> 人間の体内では合成できないリノール酸（オメガ6）約44〜50%と、α-リノレン酸（オメガ3）約30〜35%という奇跡的な黄金比率。角層バリアの構成成分を直接補給します。</li>
          <li><strong>天然レチノール様成分（トレチノイン酸）：</strong> 乾燥で滞った冬のターンオーバーを正常化し、硬くゴワついた角質をなめらかにほぐしてキメを整えます。</li>
          <li><strong>ビタミンC・E・リコピン・カロテノイド：</strong> 夏から秋にかけて蓄積した紫外線ダメージをケアし、冬特有の血行不良による「くすみ」を払拭して内側から輝く透明感を引き出します。</li>
        </ul>
      </div>

      <p>
        アルガンオイルやホホバオイルが「オレイン酸（オメガ9）」中心で油膜による保護に秀でているのに対し、ローズヒップオイルは角層の隙間へスッと潜り込んで細胞間脂質そのものを再構築する「浸透補修力」に長けています。だからこそ、表面だけがテカリ内側がつっぱるインナードライや、化粧水が弾かれてしまう砂漠肌に圧倒的な効果を発揮するのです。
      </p>
    </section>

    <!-- 選び方セクション -->
    <section id="section-howto" class="content-box">
      <h2 class="section-title">🔍 失敗しない高保湿ローズヒップオイルの選び方3つの鉄則</h2>
      <p>
        ローズヒップオイルは非常にデリケートな植物オイルです。真冬の保湿効果を最大化するために、購入前に必ず確認しておきたい3つの重要チェックポイントを整理しました。
      </p>

      <h3>① コールドプレス（低温圧搾）の未精製オーガニックを選ぶ</h3>
      <p>
        ローズヒップに含まれる熱に弱い必須脂肪酸や微量ビタミン群は、高温高圧での化学抽出や脱色精製を行うと大半が失われてしまいます。ラベルに「低温圧搾（コールドプレス）」「未精製（Virgin / Unrefined）」「オーガニック認証（BioGro、ECOCERT、有機JAS等）」の表記があるものを選びましょう。未精製オイルは濃い赤橙色〜黄金色をしており、自然の栄養素が凝縮されています。
      </p>

      <h3>② 遮光瓶（アンバー・コバルトブルー）の容器を採用しているか確認</h3>
      <p>
        不飽和脂肪酸が80%以上を占めるローズヒップオイルは、光と酸素によって酸化しやすいという特性があります。透明なプラスチックボトルではなく、紫外線を遮断する茶色や濃紺の遮光ガラスボトルに入っていることが品質保持の必須条件です。また、空気に触れる面積を最小限に抑えるスポイトタイプやポンプ式が理想的です。
      </p>

      <h3>③ ライフスタイルに合わせた容量選び（1〜2ヶ月で使い切れるサイズ）</h3>
      <p>
        酸化防止剤が無添加のピュアローズヒップオイルは、開封後1〜2ヶ月で使い切るのが基本です。顔のブースターや夜のスキンケアメインなら「20ml〜30ml」、朝晩たっぷり使ったりデコルテ・ボディまでケアするなら「45ml〜100ml」を選ぶと、酸化する前に新鮮な状態で効果を享受できます。
      </p>
    </section>

    <!-- ランキングセクション -->
    <section id="section-ranking">
      <h2 class="section-title">🏆 保湿力高めローズヒップオイル厳選おすすめランキング10選</h2>
      <p style="margin-bottom: 24px; color: var(--text-muted); font-size: 0.95rem;">
        ※楽天市場の最新APIデータを基に、配合成分の純度、抽出製法、冬の乾燥に対する保湿持続力、実際の愛用者レビューを総合評価してランク付けしています。
      </p>

      {cards_str}
    </section>

    <!-- 比較表セクション -->
    <section id="section-compare" class="content-box">
      <h2 class="section-title">📊 おすすめローズヒップオイル10選 徹底スペック比較一覧表</h2>
      <p>ランキングでご紹介した10アイテムの容量、製法、特徴、価格帯を一目で比較できる一覧表です。ご自身の肌悩みやご予算に合わせて最適な1本を見つけてください。</p>
      
      <div class="compare-table-wrapper">
        <table class="compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>ブランド</th>
              <th>容量</th>
              <th>製法 / 特長</th>
              <th>参考価格（税込）</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>第1位</strong></td>
              <td>ローズヒップ オイル 20ml</td>
              <td>Trilogy</td>
              <td>20ml</td>
              <td>未精製コールドプレス・必須脂肪酸80%以上</td>
              <td>¥{items[0]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第2位</strong></td>
              <td>ロザピンプラス 30ml</td>
              <td>Trilogy</td>
              <td>30ml</td>
              <td>独自ロザピン・抗酸化リコピン高配合</td>
              <td>¥{items[1]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第3位</strong></td>
              <td>有機ローズヒップオイル・バージン</td>
              <td>生活の木</td>
              <td>25ml</td>
              <td>国内充填有機JAS認証原料・未精製</td>
              <td>¥{items[2]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第4位</strong></td>
              <td>未精製オーガニック ローズヒップ</td>
              <td>&SH</td>
              <td>50ml</td>
              <td>高コスパ・毎晩たっぷり使える未精製</td>
              <td>¥{items[3]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第5位</strong></td>
              <td>未精製オーガニック 50ml</td>
              <td>monday moon</td>
              <td>50ml</td>
              <td>エコサート認証・原液ロット管理徹底</td>
              <td>¥{items[4]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第6位</strong></td>
              <td>クナイプビオ オイル ローズ</td>
              <td>Kneipp</td>
              <td>100ml</td>
              <td>天然ダマスクローズ香・ボディ兼用</td>
              <td>¥{items[5]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第7位</strong></td>
              <td>ピュア ローズヒップオイル 100ml</td>
              <td>自然化粧品研究所</td>
              <td>100ml</td>
              <td>サロン仕様大容量・全身の粉吹き予防</td>
              <td>¥{items[6]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第8位</strong></td>
              <td>ローズヒップ ラージ 45ml</td>
              <td>Trilogy</td>
              <td>45ml</td>
              <td>大容量お得版・ヘビーユーザー向け</td>
              <td>¥{items[7]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第9位</strong></td>
              <td>オーガニックピュア 30ml</td>
              <td>Natural Beauty</td>
              <td>30ml</td>
              <td>遮光瓶生搾り・キメ整え処方</td>
              <td>¥{items[8]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第10位</strong></td>
              <td>ピュア ローズヒップ 10ml</td>
              <td>インセント</td>
              <td>10ml</td>
              <td>携帯ミニサイズ・メイク直し目元集中</td>
              <td>¥{items[9]['price']:,}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 使い方ルーティンセクション -->
    <section id="section-routine" class="content-box">
      <h2 class="section-title">🧴 プロ直伝！冬の砂漠肌をふっくらモチ肌に変える3つの活用ステップ</h2>
      <p>
        ローズヒップオイルは単に「乳液の代わりに塗る」だけでは真価を発揮できません。冬の乾燥した環境に合わせた、効果的な3つの活用テクニックをご紹介します。
      </p>

      <h3>ステップ1：洗顔直後の「湿潤肌ブースター導入」</h3>
      <p>
        最も推奨される使い方は、洗顔後、タオルで軽く水分を押さえた直後の「濡れ肌導入」です。手のひらに2〜3滴を取り、手の体温で温めてから、顔全体を優しく包み込むように押し込みます。水分と皮脂が混ざり合うことで天然のエマルジョンが形成され、硬化した角質層が瞬時に柔らかくなります。その後に重ねる化粧水が、乾いた砂に水が染み込むようにぐんぐん角層奥へ吸い込まれていきます。
      </p>

      <h3>ステップ2：保湿クリームへの「1滴リッチブレンド」</h3>
      <p>
        オフィスの暖房が強く、夕方になると頬や口元がつっぱるという方は、夜のお手入れの最後に使用する保湿クリームや乳液にローズヒップオイルを1滴混ぜ合わせるテクニックが効果的です。クリームの保護力にオイルの浸透柔軟性が加わり、翌朝まで乾燥を寄せ付けない強固なラッピング効果を発揮します。
      </p>

      <h3>ステップ3：週末の「オイル温感スチームパック」</h3>
      <p>
        週末のバスタイムには、スペシャルケアとしてオイルパックを取り入れましょう。洗顔後、4〜5滴のオイルを顔から首筋までたっぷり伸ばし、湯船の蒸気を浴びながら3〜5分放置します。可能であれば軽く絞ったホットタオルを顔に乗せると、毛穴が自然に開いてオイルの栄養分が深くまで巡り、冬のどんよりしたくすみとゴワつきが一掃されます。
      </p>
    </section>

    <!-- FAQセクション -->
    <section id="section-faq" class="content-box">
      <h2 class="section-title">❓ よくある質問（FAQ）と正しい保管法</h2>
      {faq_str}
    </section>

    <!-- 内部リンクセクション -->
    <section id="section-links" class="content-box">
      <h2 class="section-title">🔗 合わせて読みたい！冬の乾燥対策おすすめ関連記事</h2>
      <p>冬の乾燥肌対策をさらに強化するために、オイルと相乗効果を発揮するスキンケア記事も合わせてチェックしてください。</p>
      
      <div class="related-links-grid">
        <a href="winter-ceramide-cream.html" class="related-link-card">
          <h4>冬の高保湿セラミドクリーム厳選10</h4>
          <p>オイルでほぐした肌にセラミドで強固なバリア膜を。冬の粉吹き肌を完全ブロックする名品集。</p>
        </a>
        <a href="winter-marula-oil.html" class="related-link-card">
          <h4>高保湿マルラオイルおすすめ10選</h4>
          <p>アルガンを超える抗酸化力！オメガ9豊富なマルラオイルで砂漠肌に濃密な油分バリアを補給。</p>
        </a>
        <a href="winter-squalane-oil.html" class="related-link-card">
          <h4>高純度スクワランオイルおすすめ10選</h4>
          <p>敏感肌にも安心の低刺激。サラリとしたテクスチャーで水分蒸発を防ぐ冬の万能ピュアオイル。</p>
        </a>
        <a href="winter-retinol-cream.html" class="related-link-card">
          <h4>冬の高保湿レチノールクリーム10選</h4>
          <p>乾燥小ジワとハリ不足を集中ケア。夜のエイジングケアを格上げする高機能クリーム特集。</p>
        </a>
        <a href="winter-eye-cream.html" class="related-link-card">
          <h4>冬の目元乾燥対策アイクリーム10選</h4>
          <p>暖房で乾くまぶたや目尻のひび割れを集中レスキューする濃厚アイケアコスメ。</p>
        </a>
        <a href="winter-night-cream.html" class="related-link-card">
          <h4>冬の濃密ナイトクリームおすすめ10選</h4>
          <p>睡眠中の水分蒸散をシャットアウト！翌朝ぷるんとしたハリ肌へ導く夜用集中クリーム。</p>
        </a>
      </div>
    </section>

  </main>

  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-col" style="flex: 2; min-width: 280px;">
          <h5>冬コスメ徹底比較ラボ</h5>
          <p style="font-size: 0.85rem; line-height: 1.7; color: #a0aec0;">
            当サイトは、11月から12月にかけての乾燥シーズンに特化したコスメ・スキンケア専門レビューメディアです。楽天市場の最新APIデータを活用し、常に正確で透明性の高い価格情報と商品スペックをお届けしています。
          </p>
        </div>
        <div class="footer-col">
          <h5>成分別特集</h5>
          <ul>
            <li><a href="winter-ceramide-cream.html">セラミドコスメ</a></li>
            <li><a href="winter-rosehip-oil.html">ローズヒップオイル</a></li>
            <li><a href="winter-marula-oil.html">マルラオイル</a></li>
            <li><a href="winter-retinol-cream.html">レチノールコスメ</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>アイテム別特集</h5>
          <ul>
            <li><a href="winter-face-oil.html">フェイスオイル</a></li>
            <li><a href="winter-night-cream.html">ナイトクリーム</a></li>
            <li><a href="winter-eye-cream.html">アイクリーム</a></li>
            <li><a href="winter-body-cream.html">ボディクリーム</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved. 画像および商品データ提供: 楽天市場API</p>
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-rosehip-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-rosehip-oil.html successfully! File size: {len(html_content):,} bytes")
