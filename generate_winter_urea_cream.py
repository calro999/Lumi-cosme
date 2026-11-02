import json
import re

with open("fetched_3new_nov_dec_shea_jojoba_urea_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_urea_cream"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 尿素20%配合の圧倒的治療力！ガサガサかかと・ひび割れを治す医薬品の最高峰",
        "catch": "興和新薬のロングセラー第3類医薬品。硬くなった古い角質を溶かしながら水分を角層奥深くに抱え込む",
        "brand_name": "興和新薬 (Kowa)",
        "capacity": "150g (ケラチナミンコーワ 20%尿素配合クリーム)",
        "type": "第3類医薬品・尿素20%高配合角質柔軟治療クリーム",
        "features": "尿素20g（100g中）、流動パラフィン、セタノール、ステアリルアルコール、無香料",
        "value": "ドラッグストアで圧倒的な信頼を集める医薬品。ストッキングが引っかかるかかと、カチカチのひじ・くるぶしを数日で柔らかく再生",
        "desc_p1": "11月から12月にかけて、空気の乾燥と寒冷による血行不良が重なると、皮膚のターンオーバーが遅れて古い角質が剥がれ落ちずに蓄積します。特に皮脂腺が存在しない『かかと』や『ひじ・くるぶし』は、まるで鏡餅のようにカチコチに硬化し、歩くたびにパキッと痛みを伴うひび割れを起こします。この頑固な角化症に対して、医療用と同等の効果を発揮するのがケラチナミンコーワです。",
        "desc_p2": "OTC医薬品として最大濃度である『尿素20%』を配合。角質を構成するケラチンタンパク質の結合を穏やかに緩めて剥離を促す『角質融解作用』と、角質細胞内に大量の水分を引き寄せて離さない『強力な保水作用』のダブルアプローチを展開します。白く厚みのあるリッチなクリームですが、塗り込むと体温で滑らかに伸びて患部を密閉。数日間入浴後に塗り続けるだけで、ガチガサだったかかとが驚くほどふっくら滑らかな素肌へと蘇ります。",
        "target": "かかとが硬くひび割れてストッキングが破れる方、ひじや膝が白く粉を吹いてザラつく方、医薬品で根本治療したい方",
        "point": "お風呂上がりの角質がふやけて柔らかくなっているタイミングで、500円玉大をかかとにしっかり擦り込みます。その後靴下を履いて就寝する『ラップ密封療法』が劇的に効きます。"
    },
    {
        "rank": 2,
        "tag": "🔬 尿素10%×角質柔軟技術！ライオンの皮膚科学が息づく滑らか素肌クリーム",
        "catch": "フェルゼアシリーズの実力派。カサつく手肌やすねの粉吹き乾燥をみずみずしく柔軟化",
        "brand_name": "ライオン フェルゼア",
        "capacity": "80g (フェルゼア クリーム / 指定医薬部外品)",
        "type": "指定医薬部外品・尿素10%＆ビタミンE配合クリーム",
        "features": "尿素10%、トコフェロール酢酸エステル（ビタミンE）、グリチルリチン酸二カリウム、なめらか乳化ベース",
        "value": "尿素の角質軟化作用に血行促進ビタミンEをプラス。冬の冷えによる末端のゴワつきを改善し、ベタつかずスーッとなじむ絶妙なテクスチャー",
        "desc_p1": "冬の乾燥は手足の末端だけでなく、すねや二の腕など広範囲にわたる角質の硬化と粉吹きを引き起こします。ライオンのフェルゼアクリームは、毎日の生活動作を邪魔しない心地よい使用感と、確かな角質柔軟効果を両立させた指定医薬部外品です。",
        "desc_p2": "日常的な手荒れや粉吹きに最もバランスが良い『尿素10%』を採用。さらに末梢血行を促すビタミンEと抗炎症成分をブレンドすることで、寒さで巡りが悪くなった指先や足元を健やかに整えます。20%配合クリームに比べてサラッとした後肌に設計されているため、塗布後すぐにスマホを操作したり衣類を着たりしてもベタつきが気になりません。",
        "target": "すねの粉吹きや二の腕のザラつきが気になる方、ベタつくクリームが苦手な方、日中もこまめに手や体に塗りたい方",
        "point": "手のひらで温めてから、カサつくすねや腕にスーッと優しく撫でるように伸ばします。強く擦らず、肌のキメに沿って浸透させるのがポイントです。"
    },
    {
        "rank": 3,
        "tag": "🏆 100g大容量ジャーで家族全員の冬を守る！資生堂が誇る安心の指定医薬部外品",
        "catch": "資生堂のロングセラー尿素10%。ヒアルロン酸＆スクワラン配合で角質層をみずみずしくキープ",
        "brand_name": "資生堂 (SHISEIDO)",
        "capacity": "100g (尿素10%クリーム ジャー)",
        "type": "指定医薬部外品・尿素10%＆保湿成分配合薬用クリーム",
        "features": "尿素10%、ヒアルロン酸ナトリウム、スクワラン、無香料・無着色、ワンタッチ開閉ジャー",
        "value": "ドラッグストアで長年愛され続ける冬の定番。硬くなった手肌やかかとに素早く浸透し、しっとり感が長時間持続する信頼のスキンケア",
        "desc_p1": "日本のスキンケアを牽引する資生堂が、乾燥性皮膚トラブルのために開発した『尿素10%クリーム』。洗面所やリビングに1つ置いておけば、冬の家族全員の手荒れ・かかとのガサガサを丸ごと解決してくれる大黒柱です。",
        "desc_p2": "角質を柔らかくする尿素に加え、高保水成分ヒアルロン酸と肌なじみの良いスクワランを贅沢にブレンド。硬化した角質細胞の隙間を解きほぐしながら、潤いのバリア膜を形成して水分の逃げ道を塞ぎます。無香料で嫌なニオイや刺激がなく、料理の前後や就寝前など時間を選ばずに手軽に使える高い実用性が支持されています。",
        "target": "家族みんなでシェアできる大容量ボトルを探している方、無香料で清潔感のあるクリームを好む方、手荒れとかかとの両方を1つでケアしたい方",
        "point": "指先にたっぷり取り、手の甲を合わせるようにすり込みながら指一本一本をマッサージ。爪周りの硬くなった甘皮にも丁寧に塗り込むとささくれが防げます。"
    },
    {
        "rank": 4,
        "tag": "🩹 尿素20%×ビタミンEの黄金タッグ！ひび割れ寸前の硬化角質を集中補修するロートの名品",
        "catch": "メンソレータムの皮膚研究。ガチガチかかとやザラつくひじをしっとり滑らか素肌へ巻き戻す",
        "brand_name": "ロート製薬 メンソレータム",
        "capacity": "145g (メンソレータム やわらか素肌クリームU)",
        "type": "第3類医薬品・尿素20%＆ビタミンE配合角質治療クリーム",
        "features": "尿素20%、ビタミンE誘導体（トコフェロール酢酸エステル）、グリチルリチン酸二カリウム、なめらか高密着処方",
        "value": "ロート製薬の製薬技術を結集した145g大容量ジャー。尿素の高保水作用で角質をふやかして再生を早め、冬の重度なガサガサを徹底治療",
        "desc_p1": "冬になると『靴下のかかと部分がすぐ薄くなる』『かかとが割れて歩くのが辛い』という深刻な悩みを抱える方に、絶大な支持を得ているのがメンソレータムの『やわらか素肌クリームU』です。",
        "desc_p2": "尿素20%に加えて、血行を改善するビタミンE誘導体と炎症を抑えるグリチルリチン酸をバランスよく配合。角質の奥深くまで浸透して硬い皮膚をしなやかにほぐし、新陳代謝を促進して健やかな角層の生まれ変わりを助けます。こっくりとした濃厚なテクスチャーながら伸びがよく、皮膚表面にピタッと密着して長時間のシールド効果を発揮します。",
        "target": "重度のかかとのひび割れ・ガサガサを短期間で改善したい方、大容量で冬中たっぷり使いたい方、皮膚科レベルのケアを自宅でしたい方",
        "point": "入浴時、軽石やかかとヤスリで無理に削るのは逆効果（余計に角質が厚くなります）。このクリームを朝晩2回擦り込むだけで、自然に余分な角質がポロポロ落ちて滑らかになります。"
    },
    {
        "rank": 5,
        "tag": "💼 デイリーな手肌荒れに最適！尿素10%配合でベタつかず働く手を守るメディカルハンド",
        "catch": "アトリックスの薬用処方。水仕事や乾燥でゴワつく指先を柔らかく保つ冬の定番ハンドクリーム",
        "brand_name": "atrix (アトリックス)",
        "capacity": "60g (メディケイティッド 尿素10% ハンドクリーム)",
        "type": "医薬部外品・薬用尿素10%ハンドクリーム",
        "features": "尿素10%、ビタミンE、ヒアルロン酸、サラサラ浸透パウダー配合、無香料",
        "value": "花王アトリックスが追求した『ベタつかない高浸透感』。日中のパソコン作業や家事の合間でもストレスフリーに手指の角質をケアできる実力派",
        "desc_p1": "冬場の水仕事やアルコール消毒で指先が白く硬くなり、指紋が薄くなって紙がめくれない……そんな働く手の悩みに寄り添うのがアトリックスの尿素10%配合ハンドクリームです。",
        "desc_p2": "尿素が角質の水分保持力を引き上げ、ゴワつく指先の皮膚をしっとり柔軟化。独自のサラサラ浸透技術により、肌になじませた直後からスマホ画面や書類を触っても指紋やベタつきが残りません。ポーチやデスクの引き出しにすっきり入る60gチューブで、日中のこまめなハンドケアに欠かせない相棒です。",
        "target": "仕事や家事で手を頻繁に使う方、塗った直後にスマホやPCを操作したい方、指先のゴワつきやささくれを防ぎたい方",
        "point": "手を洗った直後の水分が完全に蒸発する前のタイミングで塗るのが効果的。指と指の間や爪の付け根まで丁寧に揉み込んでください。"
    },
    {
        "rank": 6,
        "tag": "🌿 天然ビタミンE×消炎成分の力！エーザイが誇る半世紀以上の超ロングセラー薬用クリーム",
        "catch": "昭和から愛される安心の黄緑ジャー。手・顔・首・全身の巡りを促して角質を柔らかく保つ",
        "brand_name": "Eisai (エーザイ)",
        "capacity": "100g (ザーネクリーム)",
        "type": "医薬部外品・天然ビタミンE＆消炎成分配合薬用スキンクリーム",
        "features": "天然ビタミンE（d-α-トコフェロール酢酸エステル）、グリチルリチン酸二カリウム、レシチン（保湿剤）、弱酸性",
        "value": "尿素クリームで刺激を感じる敏感肌の方に最適な角質ケア。血行を促進して肌本来のバリア機能と柔軟性を高める大ロングセラー名作",
        "desc_p1": "製薬会社エーザイが1954年の発売以来、70年以上にわたって日本人の肌を守り続けてきた『ザーネクリーム』。尿素そのものは含みませんが、天然ビタミンEの強力な血行促進作用と消炎作用により、硬くなった角質を穏やかに整える冬の至宝です。",
        "desc_p2": "大豆由来のレシチンと天然ビタミンEが角層奥深くまで浸透し、寒さで滞った末梢血流を活性化。肌本来の水分保持力を高め、乾燥による赤みやカサつきをしっとり鎮静します。尿素高配合クリーム特有のピリピリ感が苦手な方や、顔やデコルテなどのデリケートな皮膚の角質ケアとしても安心して使用できます。",
        "target": "尿素クリームでピリつきを感じやすい敏感肌の方、顔から全身までマルチに使いたい方、肌の血色感や巡りを改善したい方",
        "point": "お風呂上がりに、手のひらで温めたザーネクリームを首すじから鎖骨、肩にかけて優しくリンパマッサージするように伸ばすと全身がポカポカ温まります。"
    },
    {
        "rank": 7,
        "tag": "🛡️ 水を弾く密着バーム！セラミド3配合でガサガサかかとを集中密封する超高密着ケア",
        "catch": "第一三共ヘルスケアの皮膚科学。防腐剤無添加で硬いかかとに吸い付く濃密バーム処方",
        "brand_name": "第一三共ヘルスケア",
        "capacity": "20g (ロコベースリペア かかとケアバーム)",
        "type": "化粧品・超高密着かかと専用バーム",
        "features": "セラミド3、コレステロール、遊離脂肪酸（3大脂質成分配合）、パラフィン密着膜、防腐剤フリー",
        "value": "尿素で柔軟にした後の『フタ』としても最強。水分を一切含まない高密着処方で、歩行の摩擦でも落ちずに一日中かかとを保護し続ける",
        "desc_p1": "『普通の保湿クリームだと靴下やシーツに吸い取られて朝には乾いてしまう』という悩みに応えるため、第一三共ヘルスケアが開発したかかと専用の超硬度バームです。",
        "desc_p2": "あえて水を一切配合せず、角質細胞間脂質の3大成分（セラミド・コレステロール・遊離脂肪酸）を理想の比率でブレンド。肌に乗せると体温でジワリと溶け、頑固なかかとの溝にピタッと埋め込まれます。水や摩擦に極めて強い耐水性フィルムを形成するため、朝靴下を履いて出かけても夜まで潤いの密封状態が途切れません。",
        "target": "靴下や歩行摩擦ですぐに保湿が落ちてしまう方、セラミドでかかとのバリアを根本から立て直したい方、防腐剤無添加にこだわる方",
        "point": "ケラチナミン等の尿素クリームを塗って角質を柔軟にした後、その上からこのロコベースを重ねてフタをする『ダブル密着ケア』を行うと、数日でサロン級のツルスベかかとが完成します。"
    },
    {
        "rank": 8,
        "tag": "🎒 外出先でもサッと角質柔軟！資生堂尿素10%の持ち運びに便利な携帯チューブ",
        "catch": "バッグに入れて冬のお出かけへ。外出先での突然の手荒れや粉吹きを即効レスキュー",
        "brand_name": "資生堂 (SHISEIDO)",
        "capacity": "60g (尿素10%クリーム チューブ)",
        "type": "指定医薬部外品・尿素10%携帯用薬用クリーム",
        "features": "尿素10%、ヒアルロン酸Na、スクワラン配合、スリムチューブ、無香料",
        "value": "資生堂の高品質尿素10%クリームを携帯しやすいスリムなチューブに充填。外出先で指先やかかと、ひじの乾燥が気になった瞬間に清潔にピンポイント補給",
        "desc_p1": "冬の外出時、アウターの袖口と擦れて手首がカサついたり、タイツの摩擦で足首周りがチクチク痒くなったりすることがあります。そんな時にバッグからスッと取り出せるのが資生堂尿素10%のチューブタイプです。",
        "desc_p2": "ジャータイプと同じ高品質な尿素10%・ヒアルロン酸・スクワラン配合処方。空気に触れにくく衛生的なチューブ式なので、ネイルケアとして爪の根元に少量出したり、指先のひび割れ予備軍に直接塗布したりと、細やかなパーツケアに抜群の使い勝手を誇ります。",
        "target": "外出先やオフィスに常備したい方、ジャータイプに指を入れるのが衛生的に気になる方、小分けで持ち歩きたい方",
        "point": "冬のストッキングやタイツを履く直前、かかとやくるぶしに少量塗り込んでおくと、静電気が抑えられ摩擦による粉吹きや伝線を防ぐことができます。"
    },
    {
        "rank": 9,
        "tag": "🍯 シアバター×カカオバター配合！濃厚こってりヴェールで水を弾く手肌ガード",
        "catch": "メンソレータムの薬用ハンドベール。冬の過酷な水仕事や外気から手肌を鉄壁ブロック",
        "brand_name": "ロート製薬 メンソレータム",
        "capacity": "70g (メンソレータム 薬用ハンドベール 濃厚こってりクリーム)",
        "type": "医薬部外品・シアバター＆植物性油脂配合高密着ハンドクリーム",
        "features": "シアバター、カカオバター、ビタミンE誘導体、パンテノール（プロビタミンB5）、高密着バーム処方",
        "value": "尿素に加えて天然のシアバターを配合した濃厚処方。指先のひび割れやあかぎれを物理的にラッピングし、水を弾いて潤いを閉じ込める",
        "desc_p1": "冬場の食器洗いや洗濯などの家事、冷たい風にさらされる自転車の運転などで、手肌の油分は容赦なく奪われます。ロート製薬の『濃厚こってりクリーム』は、その名の通りリッチなコクで手肌を包み込む高密着処方です。",
        "desc_p2": "優れた保湿力を持つ天然シアバターとカカオバターを配合し、こってりとした重厚なクリームが肌のキメに入り込んで密着。水を弾くバリア膜を作るため、塗布した後に軽く水洗いをしても保湿効果が流れ落ちません。ビタミンEとパンテノールが荒れた角質をじっくり補修し、ふっくら吸い付くような手肌をキープします。",
        "target": "水仕事が多く手荒れ・あかぎれを繰り返す方、こっくり濃厚なクリームでしっかり守られている安心感が欲しい方",
        "point": "夜寝る前に両手に少し多め（サクランボ大）に塗り広げ、綿の手袋をして眠ると、翌朝エステ帰りのようなモチモチの手肌に生まれ変わります。"
    },
    {
        "rank": 10,
        "tag": "🍊 ビタミンB2の黄色い実力派！日本のひび・あかぎれを治し続ける国民的指定医薬部外品",
        "catch": "ユースキンの看板商品。4つの有効成分が冬のボロボロ手足を芯から修復する名品ボトル",
        "brand_name": "yuskin (ユースキン)",
        "capacity": "120g (ユースキン ボトル)",
        "type": "指定医薬部外品・ひび・あかぎれ・しもやけ治療クリーム",
        "features": "トコフェロール酢酸エステル（ビタミンE）、グリチルレチン酸、dl-カンフル、グリセリン、ビタミンB2（黄色味成分）",
        "value": "70年近く日本家庭の冬を支え続ける国民的指定医薬部外品。尿素とは異なるビタミンアプローチで、血行不良によるしもやけからひび割れまで徹底修復",
        "desc_p1": "『冬の黄色いクリーム』として老若男女問わず親しまれているユースキン。ひび、あかぎれ、しもやけを治すために設計された4つの有効成分が配合された、日本が世界に誇る治療系スキンケアです。",
        "desc_p2": "鮮やかな黄色は着色料ではなく、肌の修復を助ける水溶性ビタミンB2そのものの色です。清涼感のあるdl-カンフルの香りは、肌になじんで血行が良くなると数分で自然に消え去ります。水分と油分を黄金バランスで乳化させており、しっかり擦り込むことで白っぽさが消え、肌の内側が潤いで満たされてサラサラに変化します。120gのボトルタイプは冬の間ずっと惜しみなく使えます。",
        "target": "ひび割れ・あかぎれ・しもやけに本気で悩む方、尿素フリーで確かな治療効果を求める方、冬の全身マッサージに使いたい方",
        "point": "クリームが肌の上で白から透明に変わるまで、円を描くようにしっかりすり込む『ユースキンマッサージ』が効果的。血流が一気に改善して指先まで温まります。"
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
    "headline": "保湿力の強さでガサガサ角質とさようなら！硬くなったかかと・ひじをしっとり柔らかく整える高保湿尿素クリームランク10",
    "description": "11月・12月の寒冷乾燥でカチコチに硬化するガサガサかかと・ひび割れ・粉吹き肌を徹底解決！天然保湿因子NMFを補い角質を柔軟化する高保湿尿素クリーム10選を徹底比較！ケラチナミンコーワ、フェルゼア、資生堂尿素10%、メンソレータム、アトリックス、ユースキンなど、医薬品・指定医薬部外品の名品を厳選。",
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
    "name": "冬の高保湿尿素クリーム おすすめランキング10選",
    "itemListElement": item_list_elements
}

# HTML Generation
html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さでガサガサ角質とさようなら！硬くなったかかと・ひじをしっとり柔らかく整える高保湿尿素クリームランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒冷乾燥でカチコチに硬化するガサガサかかと・ひび割れ・粉吹き肌を徹底解決！天然保湿因子NMFを補い角質を柔軟化する高保湿尿素クリーム10選を徹底比較！ケラチナミンコーワ、フェルゼア、資生堂尿素10%、メンソレータム、アトリックス、ユースキンなど、医薬品・指定医薬部外品の名品を厳選。">
  <meta name="keywords" content="尿素クリーム,かかと ひび割れ,角質柔軟クリーム,ケラチナミン,フェルゼア,資生堂 尿素10,手荒れ 治療,冬 フットケア,おすすめ 2026">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-urea-cream">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さでガサガサ角質とさようなら！硬くなったかかと・ひじをしっとり柔らかく整える高保湿尿素クリームランク10">
  <meta property="og:description" content="11月・12月の硬化角質＆ひび割れを救う！角質柔軟・集中保水する高保湿尿素クリーム10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-urea-cream">
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
      --primary: #3d7068;
      --primary-dark: #244b45;
      --primary-light: #eaf3f1;
      --accent: #52948a;
      --text: #202c2a;
      --text-sub: #526360;
      --bg: #f7faf9;
      --card-bg: #ffffff;
      --border: #d2e4e1;
      --shadow: 0 4px 20px rgba(36, 75, 69, 0.08);
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
      background: #f1f7f6;
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
      background: #f1f7f6;
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
      background: #f1f7f6;
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
      background: #244b45;
    }}
    .ranking-card:nth-child(2) .rank-number {{
      background: #3d7068;
    }}
    .ranking-card:nth-child(3) .rank-number {{
      background: #52948a;
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
      background: #f1f7f6;
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
      background: #f5fbf9;
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
      background: #f1f7f6;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px 16px;
      text-decoration: none;
      color: var(--text);
      transition: all 0.2s;
    }}
    .internal-card:hover {{
      border-color: var(--primary);
      background: #e2eeec;
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
      <li><a href="/winter-jojoba-oil">ホホバオイル</a></li>
      <li><a href="/winter-foot-cream">フットクリーム</a></li>
    </ul>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">TOP</a> &gt; <a href="/winter-body-care">冬のボディ・パーツケア</a> &gt; <span>高保湿尿素クリーム</span>
</div>

<main class="container">
  <article>
    <header class="article-header">
      <span class="badge">2026年冬 最新決定版 / 11〜12月角質集中リペア</span>
      <h1>保湿力の強さでガサガサ角質とさようなら！硬くなったかかと・ひじをしっとり柔らかく整える高保湿尿素クリームランク10</h1>
      <div class="meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証機関: 冬コスメ徹底比較ラボ 編集部</span>
        <span>対象: かかとのひび割れ・ガサガサ角化症・ひじ膝の黒ずみゴワつき</span>
      </div>
      <div class="lead-box">
        <p><strong>「かかとが白くガサガサになり、ストッキングや靴下が引っかかって破れてしまう」「お風呂上がりに普通のボディクリームを塗っても、皮膚が硬くて浸透しない……」</strong></p>
        <p>11月中旬から12月にかけて、寒風による急激な湿度低下と、足先・指先の血行不良が重なることで、肌のターンオーバーは著しく遅延します。剥がれ落ちるはずの古い角質が何層にも積み重なって硬化し、皮脂腺のないかかとや、摩擦の多いひじ・くるぶしは『カチコチの鏡餅状態』へと進行します。</p>
        <p>油分だけのクリームをどれだけ塗り重ねても、分厚く硬化した角質には届きません。この冬の頑固な角質硬化を打ち破る唯一の鍵が、余分な角質を穏やかにほぐして溶かす<strong>「角質溶解作用」</strong>と、細胞内に水分を強力に引き寄せる<strong>「天然保湿因子（NMF）保水力」</strong>を兼ね備えた<strong>高保湿尿素クリーム</strong>です。本記事では、楽天APIからリアルタイムに取得した最新データに基づき、医薬品の20%配合からデイリーに使える10%配合、高密着バームまで、真冬に選ぶべき高保湿尿素クリーム10選を徹底比較します。</p>
      </div>
    </header>

    <!-- 科学的背景・解説セクション -->
    <section class="content-section">
      <h2>🧬 なぜ尿素（Urea）だけが「硬い角質」を柔らかく治せるのか？</h2>
      <p>尿素は、私たちの健康な皮膚角質細胞内に存在する<strong>『天然保湿因子（NMF）』の約7%</strong>を占める生体関連成分です。化粧品や医薬品に配合される尿素には、一般的な保湿剤には真似できない2つの特筆すべき皮膚科学的機能があります。</p>
      
      <div class="feature-grid">
        <div class="feature-card">
          <h4>1. ケラチンを緩める「角質溶解・柔軟作用」</h4>
          <p>硬くなった角質は、ケラチンというタンパク質が強固に結合して固まっています。尿素はこのケラチン同士の水素結合を穏やかに切断して緩め、硬化した余分な古い角質を自然にほぐして剥離を促します。</p>
        </div>
        <div class="feature-card">
          <h4>2. 水分を引き寄せて離さない「強力な親水保水力」</h4>
          <p>尿素分子は親水性が極めて高く、周囲の水分分子を強力に引き寄せて角層細胞内に抱え込みます。硬くなった皮膚組織に水分を無理なく行き渡らせ、内側からふっくらとした柔軟性を取り戻します。</p>
        </div>
        <div class="feature-card">
          <h4>3. ターンオーバー正常化による根本改善</h4>
          <p>分厚く滞留していた古い角質が取り除かれることで、乱れていた皮膚のターンオーバーサイクルが正常化。新しくみずみずしい角質細胞がスムーズに表面へと上がってくる健やかな代謝をサポートします。</p>
        </div>
        <div class="feature-card">
          <h4>4. ビタミンE・抗炎症成分との相乗効果</h4>
          <p>医薬品・指定医薬部外品の尿素クリームには、血行を促進するビタミンEや、炎症を鎮めるグリチルリチン酸が配合されています。寒さで冷えた末端の血行不良を改善し、ひび割れやあかぎれを早期に治療します。</p>
        </div>
      </div>

      <h3>💡 濃度で使い分ける！「尿素20%」と「尿素10%」の選び方</h3>
      <p>尿素クリームの効果を安全かつ最大限に引き出すためには、症状と部位に応じた『配合濃度の使い分け』が極めて重要です。</p>
      <ul style="padding-left: 20px; margin-bottom: 16px; font-size: 0.95rem;">
        <li style="margin-bottom: 8px;"><strong>尿素20%配合（第3類医薬品など）：</strong>かかとのひび割れ、くるぶしやひじの黒ずみ・肥厚、魚鱗癬状の頑固な硬化皮膚の集中治療に。短期間でガサガサ角質を柔らかくリセットしたい緊急ケアに最適です（※傷口や顔への使用は避けてください）。</li>
        <li><strong>尿素10%配合（指定医薬部外品・薬用ハンドクリームなど）：</strong>冬の日常的な手荒れ、すねの粉吹き、二の腕のザラつき予防に。刺激が少なくサラッとした使用感で、毎日のデイリーケアとして長く使い続けたい方に適しています。</li>
      </ul>
    </section>

    <!-- ランキング一覧 -->
    <section>
      <h2 style="font-size: 1.5rem; color: var(--primary-dark); margin: 36px 0 24px; text-align: center;">
        🏆 冬の高保湿尿素クリーム おすすめランキング10選
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
              <div class="spec-item"><span class="spec-label">薬効・分類:</span> {p['type']}</div>
              <div class="spec-item"><span class="spec-label">有効成分:</span> {p['features']}</div>
              <div class="spec-item"><span class="spec-label">治療価値:</span> {p['value']}</div>
            </div>

            <div class="product-desc">
              <p>{p['desc_p1']}</p>
              <p>{p['desc_p2']}</p>
            </div>

            <div class="user-point">
              <strong>🎯 こんな症状・部位に最適:</strong> {p['target']}
            </div>

            <div class="user-point" style="background: #eef6f4; border-left-color: var(--primary);">
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
      <h2>📊 高保湿尿素クリーム10選 スペック徹底比較一覧表</h2>
      <p>配合されている尿素濃度、医薬品区分、容量、価格、適した症状を比較表に整理しました。</p>
      
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位・商品名</th>
              <th>医薬品区分 / 尿素濃度</th>
              <th>内容量</th>
              <th>楽天参考価格</th>
              <th>適した部位・症状</th>
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

    <!-- 冬の正しい使い方ガイド -->
    <section class="content-section">
      <h2>❄️ ガサガサかかとを最速で治す！プロ推奨の4ステップ</h2>
      <p>尿素クリームの効果を短期間で体感するための正しい使用手順を解説します。間違ったセルフケアで肌を傷つけないようご注意ください。</p>

      <div class="step-box">
        <div class="step-num">1</div>
        <div class="step-text">
          <h4>【厳禁】無理に軽石やヤスリで削らない</h4>
          <p>硬くなったかかとを軽石や金属ヤスリでゴシゴシ削ると、皮膚の防御反応で角質がさらに厚く硬化してしまいます。削るのではなく、尿素の力で角質結合を緩めて自然に剥離させるのが皮膚科学の正攻法です。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">2</div>
        <div class="step-text">
          <h4>【塗布】入浴後10分以内にたっぷり擦り込む</h4>
          <p>湯船に浸かって角質が水分を含んで柔らかくなっている入浴後10分以内がゴールデンタイムです。患部にたっぷりクリームを乗せ、円を描くように優しくマッサージしながら角層の溝までしっかり擦り込みます。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">3</div>
        <div class="step-text">
          <h4>【密封】綿の靴下を履いて一晩ラッピング就寝</h4>
          <p>クリームを塗った後、通気性の良い綿の靴下を履いて就寝します。シーツにクリームが吸い取られるのを防ぎ、体温による温熱スチーム効果で尿素の浸透率が飛躍的に高まります。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">4</div>
        <div class="step-text">
          <h4>【維持】滑らかになったら保湿クリーム（シアバター・セラミド）へ移行</h4>
          <p>尿素20%クリームを1〜2週間塗布し、ガサガサ角質が取れて柔らかくなったら、日常のケアはシアバターやセラミドクリームなどの保護・保湿クリームへと切り替えます。常に角質を削りすぎないサイクル管理が大切です。</p>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="content-section">
      <h2>❓ 高保湿尿素クリームに関するよくある質問（FAQ）</h2>
      
      <div class="faq-item">
        <div class="faq-q">Q1. 尿素クリームを顔の乾燥小ジワに塗ってもいいですか？</div>
        <div class="faq-a">
          尿素20%などの高濃度クリームは、皮膚の薄い顔には刺激が強すぎ、赤みやヒリつきの原因になるため使用を避けてください。顔の乾燥には、セラミド化粧水やヒアルロン酸美容液、純度100%のシアバターやホホバオイルなど、皮膚バリアを守るアイテムを使用してください。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q2. ひび割れて血が出ている傷口に塗っても大丈夫ですか？</div>
        <div class="faq-a">
          血がにじんでいるような深い傷口や、赤く腫れてただれている部位に直接尿素クリームを塗ると、激しいしみる痛みを感じます。出血や化膿がある傷口には、まず白色ワセリン等で保護して傷がふさがってから、周りの硬くなった角質ケアとして尿素クリームをお使いください。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q3. 毎日ずっと使い続けても皮膚が薄くなったりしませんか？</div>
        <div class="faq-a">
          尿素20%配合などの治療用クリームは、硬い角質が改善するまでの短期集中使用（1〜2週間程度）が基本です。皮膚が柔らかく整った後は、尿素10%のデイリーハンドクリームや、シアバター、セラミドクリームなどの保湿・エモリエント剤に切り替えるのが皮膚科的にも推奨されます。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q4. 子供のかさつきや粉吹きにも使えますか？</div>
        <div class="faq-a">
          お子様の皮膚は大人に比べて非常に薄くデリケートなため、高濃度の尿素クリームは刺激になる場合があります。お子様の冬の乾燥には、刺激のないピュアシアバター、ホホバオイル、ワセリン、または小児用保湿剤の使用をおすすめします。
        </div>
      </div>
    </section>

    <!-- 内部リンク -->
    <section class="content-section">
      <h2>🔗 あわせて読みたい！冬の乾燥対策おすすめ関連記事</h2>
      <p>ガサガサ角質をリセットした後は、良質な水分と油分で毎日のバリアを守りましょう。あわせて読みたい人気記事はこちらです。</p>
      
      <div class="internal-link-grid">
        <a href="/winter-shea-butter" class="internal-card">
          <h5>高保湿シアバターランク10</h5>
          <p>天然の濃厚ベールで顔・唇・手足の乾燥を防ぐオーガニックバーム特集。</p>
        </a>
        <a href="/winter-jojoba-oil" class="internal-card">
          <h5>高保湿ホホバオイルランク10</h5>
          <p>皮脂膜成分ワックスエステルで真冬の肌を柔らかく包む名品。</p>
        </a>
        <a href="/winter-squalane-oil" class="internal-card">
          <h5>高純度スクワランオイルランク10</h5>
          <p>たった1滴で極上のツヤ膜を形成するピュアオイル比較。</p>
        </a>
        <a href="/winter-foot-cream" class="internal-card">
          <h5>冬のフットクリームおすすめ総合</h5>
          <p>冬のかかと・足裏の乾燥を徹底ケアするフット専用クリーム特集。</p>
        </a>
        <a href="/winter-hand-cream" class="internal-card">
          <h5>冬の高保湿ハンドクリーム特集</h5>
          <p>水仕事や寒風による手荒れを防ぐ、高機能ハンドクリーム決定版。</p>
        </a>
        <a href="/winter-body-cream" class="internal-card">
          <h5>冬の高保湿ボディクリーム特集</h5>
          <p>全身の粉吹き・カサつきを防ぐ、濃厚ボディクリーム名作選。</p>
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

with open("winter-urea-cream.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-urea-cream.html")
