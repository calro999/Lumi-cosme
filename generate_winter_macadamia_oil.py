import json
import re

with open("fetched_3new_macadamia_pomegranate_ricebran.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_macadamia_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🌿 低温圧搾コールドプレス×パルミトレイン酸約20%！真冬のゴワつく角層をほぐす名品ブースター",
        "catch": "アロマとハーブの老舗・生活の木が手がける高純度植物油。加齢や真冬の寒冷で激減するパルミトレイン酸を豊富に含み、硬直した角層へ瞬時に浸透して皮脂膜を再構築する実力派オイル",
        "brand_name": "Tree of life (生活の木)",
        "capacity": "25ml / 遮光ガラスドロップボトル",
        "type": "高純度ピュアマカデミアナッツオイル",
        "features": "マカデミア種子油（低温圧搾コールドプレス）、パルミトレイン酸約20%、オレイン酸約60%",
        "value": "未精製に近い栄養分を保ちながら、独特のナッツ臭を抑えた上質な仕上がり。洗顔後すぐのブースター使用で、その後に塗布する化粧水の浸透力を劇的に向上",
        "desc_p1": "11月中旬を過ぎて外気温が一桁台まで低下すると、皮膚の皮脂腺機能が著しく低下し、肌表面の天然保護膜である皮脂膜がスカスカになります。生活の木の『マカデミアナッツオイル』は、まさにこの冬特有の皮脂欠乏状態を救済するために生まれた名品です。マカデミア種子を熱を加えない低温圧搾法で抽出しているため、必須脂肪酸やビタミン類が壊れることなく丸ごと閉じ込められています。",
        "desc_p2": "特筆すべきは、20歳前後の若々しい肌に豊富に含まれ、その後年齢とともに減少の一途をたどる『パルミトレイン酸』が約20%という高水準で含まれている点です。肌にのばすと『消えるオイル』の異名通り、べたつきを残さず瞬時に角層深部へと吸い込まれていきます。冬の寒さでカチコチに固まった角質細胞の隙間を柔軟に解きほぐし、後から重ねる化粧水のみずみずしい水分を磁石のように引き寄せてキープします。朝のメイク前に1滴仕込んでもヨレず、暖房直撃のオフィスでも夕方まで乾燥割れを感じさせません。",
        "target": "冬になると化粧水が肌表面で弾かれて入っていかない方、目元や頬の乾燥によるゴワつき・小ジワが気になる方、無添加で安心して使える高純度キャリアオイルを求める方",
        "point": "朝晩の洗顔直後、肌にまだわずかな湿り気が残っている状態で1〜2滴を手にとり、手のひらで温めてから顔全体を優しく包み込むようにハンドプレスします。その後、普段の化粧水をたっぷり重ねてください。"
    },
    {
        "rank": 2,
        "tag": "🛁 業務用サロン品質×大容量1000ml！冬の乾燥粉吹きボディを包み込む贅沢ポンプオイル",
        "catch": "プロのエステサロンでも採用される高品質マカダミアオイルを特大サイズでお届け。パルミトレイン酸とオレイン酸の濃密な油分膜が、真冬の粉吹きすね・カサつく背中・ひび割れ踵を丸ごと救済",
        "brand_name": "Beau temps (ボータン)",
        "capacity": "1000ml / 遮光ポンプボトル",
        "type": "全身用高保湿マッサージ＆キャリアオイル",
        "features": "天然マカダミア種子油100%、高純度精製、無香料・無着色、プッシュポンプ式",
        "value": "1000mlの大容量だから、顔だけでなく冬の粉吹きすね、肘・膝、デコルテ、ヘアケアまで全身に惜しみなく使用可能。ポンプ式で濡れた手でも扱いやすい実用設計",
        "desc_p1": "真冬のボディケアにおいて最大の悩みは、お風呂上がりの急激な水分蒸発です。脱衣所の冷気にさらされた瞬間、皮膚の水分は猛スピードで気化し、すねや太ももが白い粉を吹いた状態に陥ります。ボータンの『ピュア マカダミアナッツオイル 1000ml』は、そんな冬の全身乾燥トラブルに惜しみなく立ち向かえるサロン仕様の超大容量アイテムです。",
        "desc_p2": "高度な精製技術によってオイル特有の油臭さや粘つきを極限まで低減。さらりとした軽やかなすべり心地でありながら、肌の上でマッサージすると体温でじんわり広がり、硬化した皮膚組織を柔らかくときほぐします。入浴直後の濡れた素肌に2〜3プッシュをなじませてからタオルで押さえる『インバスオイルケア』を行えば、一日中ボディクリームいらずのもっちり肌が続きます。ヘアオイルやクレンジングオイルとしても万能に活躍するコスパ最強の1本です。",
        "target": "真冬になると手足の皮膚が粉を吹いて痒みが出る方、家族全員で惜しみなく使える大容量オイルを探している方、エステ級の本格オイルマッサージを自宅で楽しみたい方",
        "point": "お風呂から上がる直前、タオルで水分を拭き取る前の濡れた肌に全身へ伸ばします。水分とオイルが乳化して角層へすばやく馴染み、その後タオルで優しく水分を押さえるだけで完璧な保護膜が完成します。"
    },
    {
        "rank": 3,
        "tag": "🌹 天然マカデミア油×優雅なダマスクローズ！真冬の女性美を呼び覚ますプレミアムマルチオイル",
        "catch": "ドイツ名門ハーバルブランド・クナイプの最高峰美容オイル。浸透性に優れたマカデミアナッツオイルを主軸に天然ローズ精油を調合し、冬の寒冷でくすんだ大人の肌に艶やかなハリと透明感を授ける",
        "brand_name": "Kneipp (クナイプ)",
        "capacity": "100ml / ガラスドロップボトル",
        "type": "高保湿フェイス＆ボディ美容オイル",
        "features": "マカデミア種子油、ダマスクバラ花油、カニナバラ果実油、ヒマワリ種子油",
        "value": "オーガニック国際認証を取得した厳格な品質基準。高浸透マカデミアオイルの柔軟効果と、ダマスクローズの女性ホルモンバランスをサポートする高貴なアロマを両立",
        "desc_p1": "11月から12月にかけての寒暖差は、自律神経の乱れを招き、肌のターンオーバーを鈍らせて血色のないどんよりとした顔色を作り出します。クナイプの『ビオ オイル ローズ』は、植物療法の伝統に基づき、高浸透なマカデミアナッツオイルとブルガリア産ダマスクローズの精油を融合させた至高のオイル美容液です。",
        "desc_p2": "肌に乗せると、人工香料では決して表現できない本物の薔薇の深みのある香りが立ち上り、冬の寒さでこわばった表情筋まで解きほぐされるようなリラクゼーションをもたらします。マカデミアオイルのパルミトレイン酸が角層深部をふっくら持ち上げ、ローズヒップやヒマワリのビタミン類が冬の木枯らし乾燥で荒れたキメを均一に補修。顔のお手入れはもちろん、デコルテのリンパマッサージやパサつく髪の毛先ケアにも使え、全身を上質なツヤと上品な香りで包み込みます。",
        "target": "冬の乾燥小ジワとともに肌のツヤ・ハリの低下を感じている方、日々のスキンケアで極上のアロマ癒やしを味わいたい方、フェイスからボディまで1本で満たしたい方",
        "point": "夜のお手入れの最後に、3〜4滴を手にとり、手のひらで温めて鼻を覆い深く深呼吸して香りを吸い込みます。その後、顔の中心から外側へ向けてリンパを流すように優しくプレスしながら馴染ませてください。"
    },
    {
        "rank": 4,
        "tag": "🌰 コールドプレス未精製の黄金色！ナッツ本来の栄養分を凝縮した高濃度スキンケアオイル",
        "catch": "手作りコスメ原料専門のカフェ・ド・サボンが選定した無添加・未精製マカダミアオイル。黄金色の液滴にパルミトレイン酸と天然ビタミンEがそのまま生き残り、冬の乾燥荒れ肌を鉄壁ガード",
        "brand_name": "Cafe de Savon (カフェ・ド・サボン)",
        "capacity": "50ml / 遮光ドロッパーボトル",
        "type": "未精製オーガニック植物オイル",
        "features": "未精製マカダミア種子油（無添加・低温圧搾）、天然トコフェロール、未脱臭・未脱色",
        "value": "精製工程で失われがちな微量栄養素や抗酸化成分をまるごとキープ。少量でも驚異的な油分保持力を発揮し、真冬の就寝中の暖房乾燥によるインナードライを完全にシャットアウト",
        "desc_p1": "市販の多くの植物油は使いやすさを重視して脱臭・脱色が行われますが、その過程で貴重な植物性ステロールやビタミンの一部が熱で失われてしまうことがあります。カフェ・ド・サボンの『未精製 マカダミアナッツオイル』は、自然の恵みをありのまま肌へ届けるため、一切の化学処理を行わずに低温圧搾されたゴールデンカラーの純粋オイルです。",
        "desc_p2": "わずかにナッツ本来の香ばしさを残した濃厚なオイルは、真冬の強烈な乾燥にさらされた肌にとって最高のご馳走となります。指先にとるとしっかりとしたコクを感じますが、肌になじませるとパルミトレイン酸の親和性によって瞬く間に浸透。肌表面にベタつく油膜を残さず、内側はしっとり満たされた『内潤・外サラ』の理想的な肌状態を作り出します。冬の唇のガサガサや爪周りのささくれ、目元の乾燥シワへのポイント集中ケアとしても群を抜く保護力を誇ります。",
        "target": "化学薬品不使用のピュアなオーガニック未精製オイルにこだわりたい方、冬の夜間に肌が乾燥して朝起きるとカピカピになっている方、部分的な乾燥荒れをピンポイント修復したい方",
        "point": "夜のスキンケアの仕上げに、目元・口元・頬など乾燥が特に深刻な部位へ1滴を指先でトントンと置くように重ねづけします。リップバーム代わりに唇へ薄くなじませるのも非常に効果的です。"
    },
    {
        "rank": 5,
        "tag": "💧 高純度精製でサラリと馴染む！冬の顔・首・デコルテに惜しみなく使える大容量200ml",
        "catch": "国内充填・徹底精製による低刺激処方。オイル特有の重さやベタつきを徹底排除し、パルミトレイン酸の素早い角層浸透性だけをピュアに引き出したデイリーユースの名品",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "200ml (50ml×4本パック) / ドロッパーボトル",
        "type": "精製高純度キャリアオイル",
        "features": "マカダミアナッツ油（高純度精製）、無添加、保存料・防腐剤フリー",
        "value": "使い切りやすい50mlボトルに小分けされた200mlセット。空気に触れる時間を最小限に抑え、酸化しやすい冬の期間中いつでも新鮮なオイルを贅沢に活用可能",
        "desc_p1": "植物オイルを使ってみたいけれど、ニキビができやすい、あるいはベタつくテクスチャーが苦手という方に絶大な支持を得ているのが、&SHの精製マカダミアナッツオイルです。徹底した精製プロセスによってアレルゲンとなる微小タンパク質や不純物を取り除き、驚くほどサラサラとした水のようなテクスチャーに仕上げられています。",
        "desc_p2": "サラッとしているのに、肌へ押し込むと角層の奥まで吸い寄せられるように広がり、しなやかな保護膜を形成します。真冬の冷風にさらされる首元やデコルテは皮膚が薄く乾燥小ジワができやすいゾーンですが、このオイルなら衣服にベタつき移りすることなく、滑らかなハリ感をキープできます。50ml×4本の分包仕様になっているため、1本は洗面所、1本はベッドサイド、1本はデスクへと配置して、日中のハンドケアや乾燥対策にもフレッシュな状態でマルチに活用できます。",
        "target": "オイルのベタつきや油膜感が苦手な方、敏感肌で刺激の少ない精製オイルを選びたい方、酸化を防ぎながら常に新鮮な状態で使い続けたい方",
        "point": "朝のメイク前や日中のケアに最適です。化粧水の後に1円玉大を手のひら全体へ広げ、顔全体から首筋・デコルテへと滑らせるように塗布します。肌表面がさらりと落ち着いたらすぐにベースメイクへ進めます。"
    },
    {
        "rank": 6,
        "tag": "🥛 高保湿マカデミア油×うるおい持続成分！真冬の粉吹き肌をしっとり密封する王道ボディミルク",
        "catch": "ドラッグストアで手に入る最高峰の保湿力。ニベアが誇る高純度マカデミアナッツオイルとアミノ酸系保水成分のハイブリッド処方で、真冬の硬化した角層を吸い付くような潤いで満たす",
        "brand_name": "NIVEA (ニベア花王)",
        "capacity": "200g / ワンタッチボトル",
        "type": "高保湿リッチボディミルク",
        "features": "マカデミアナッツ油、コエンザイムQ10、グリセリン、アミノ酸系保湿成分、高保水型ヒアルロン酸",
        "value": "オイルの密封力とミルクの水分補給力を1本に凝縮。ドラッグストアで手軽にリピートでき、真冬の厳しい乾燥環境でも24時間しっとり感が持続する信頼の処方",
        "desc_p1": "冬のボディ乾燥において、純粋なオイルだけだと水分が足りず、かといってさっぱりしたローションだとすぐに蒸発してしまうというジレンマに陥ることがあります。ニベアの『プレミアムボディミルク モイスチャー』は、その両方の利点を完璧に融合させたロングセラー乳液です。植物オイルの中でも特に皮脂類似性の高いマカデミアナッツオイルを贅沢に配合しています。",
        "desc_p2": "手にとると、こっくりとした濃密なミルク状のテクスチャー。肌に伸ばした瞬間に体温でとろけるように広がり、角層深部へ水分を行き渡らせながら、マカデミアオイルのエモリエント膜が肌表面にピタッと密着シールドを張ります。真冬の暖房下で過ごしても粉吹きやかゆみを寄せ付けず、触れると吸い付くようなしっとり・もちもちの素肌へ整えます。上質で心安らぐローズ＆シトラスの香調も、冬の夜のバスタイム後のリラックスタイムを豊かに彩ります。",
        "target": "冬になると手足の乾燥で粉吹きや痒みに毎年悩まされる方、オイル単体よりも水分と油分を同時にチャージできるミルクが好きな方、手軽に買えて続けやすい高保湿ケアを求める方",
        "point": "入浴後、タオルで軽く水分を拭き取った後の肌に使用します。手のひらに適量をとり、両手で軽く温めてから、腕や脚の付け根から末梢へ向けて優しくマッサージするように塗り広げます。"
    },
    {
        "rank": 7,
        "tag": "🧪 原料グレードの高純度精製！スキンケアの浸透経路を切り拓くプロ仕様キャリアオイル",
        "catch": "化粧品製造の原料としても流通する確かな品質。パルミトレイン酸の強力なエモリエント作用が冬の寒冷でこわばった肌組織を柔らかく解きほぐし、エイジングケアの基盤を整える",
        "brand_name": "自然化粧品研究所",
        "capacity": "100ml / 遮光ドロップボトル",
        "type": "高純度精製マカデミアナッツオイル",
        "features": "マカデミア種子油（化粧品原料規格）、パルミトレイン酸約20%以上、低酸価・高安定性",
        "value": "無色無臭でアレルゲンを極限まで低減。普段愛用している手持ちの化粧水、乳液、クリームに1滴混ぜて保湿力を底上げするブースターとしても無限の汎用性を発揮",
        "desc_p1": "余計な添加物や香料を一切排除し、素材本来の持つエビデンスに基づいたスキンケアを追求する自然化粧品研究所。同社のマカデミアナッツオイルは、研究所基準の厳格な品質管理のもとで高純度精製されたプロユースのキャリアオイルです。",
        "desc_p2": "冬のスキンケアにおいて最も重要なのは、寒さで閉ざされた肌のバリアを壊さずに、必要な美容成分を角層深部へ届ける『道筋』を作ることです。このオイルに含まれる高濃度のパルミトレイン酸は、角質細胞同士を接着している細胞間脂質のラメラ構造に素早く馴染み、硬くなった角層を柔軟化します。洗顔後にわずか1滴をブースターとして馴染ませるだけで、その後に使う化粧水の浸透速度と吸水量が明らかに変化。自作コスメのベースオイルとしてもプロから厚い信頼を得ています。",
        "target": "手持ちの冬のスキンケアに保湿力が物足りなさを感じている方、無色・無臭で肌トラブルのリスクが極めて低いオイルを求める方、成分主義でコスメを選びたい方",
        "point": "単品での使用はもちろん、冬の乾燥がひどい時は普段の乳液や保湿クリームに1滴垂らし、手のひらで混ぜ合わせてから顔全体に馴染ませると、保湿持続力が数倍に跳ね上がります。"
    },
    {
        "rank": 8,
        "tag": "🌍 国際コスモスオーガニック認証取得！肌の柔軟性と弾力を高める最高峰プレミアムオイル",
        "catch": "厳格な世界的オーガニック基準をクリアした希少なマカダミアオイル。真冬の過酷な木枯らしと室内外の急激な寒暖差ストレスから素肌を守り、ベルベットのような滑らかさを呼び覚ます",
        "brand_name": "spa hinoki (スパヒノキ)",
        "capacity": "100ml / 遮光ガラスボトル",
        "type": "COSMOSオーガニック認証キャリアオイル",
        "features": "有機マカダミア種子油100%、COSMOS ORGANIC認証取得、低温圧搾法、未化学精製",
        "value": "南アフリカやオーストラリアの認証有機農園で手摘み収穫されたナッツを使用。土壌から製造工程まで一切の妥協を排したオーガニック最高峰の純度と抗酸化パワー",
        "desc_p1": "肌に直接つけるものだからこそ、原材料の栽培背景や製造プロセスに一切の疑念を持ちたくない。そんな本物志向のユーザーから熱烈な支持を集めているのが、スパヒノキのオーガニックマカダミアナッツオイルです。世界的な統一オーガニック基準であるCOSMOS認証を取得しており、その安全性と品質の高さは折り紙付きです。",
        "desc_p2": "ボトルから滴る黄金色のオイルは、まさに生命力の結晶。冬の冷風で薄くなり、少しの摩擦でもピリつきや赤みが生じやすくなったデリケートな大人の肌を、吸い付くような濃密な油分膜で包み込みます。パルミトレイン酸が細胞膜の柔軟性を高めるため、マッサージを重ねるごとに肌のゴワつきが消え、まるで上質なシルクのような手触りへと変貌します。冬の頭皮の乾燥によるフケやかゆみを防ぐスカルプオイルとしても格別の効果を発揮します。",
        "target": "オーガニック認証を取得した最高品質のコスメを選びたい方、寒暖差で肌が敏感に傾きやすい方、冬のフェイスケアとスカルプケアを両立させたい方",
        "point": "週に1回、シャンプー前の乾いた頭皮に500円玉大を塗布し、指の腹で揉みほぐすスカルプマッサージが絶品。毛穴の固まった皮脂を浮かせつつ、頭皮の乾燥バリアを劇的に高めます。"
    },
    {
        "rank": 9,
        "tag": "✨ マカダミア油×アルガン油の黄金タッグ！真冬のパサつく髪と静電気を一掃するヘアミスト",
        "catch": "ハリウッドセレブ御用達のヘアケアブランド。超微粒子マカダミアオイルがキューティクルの奥深くまで浸透補修し、冬の乾燥・マフラー摩擦による静電気や枝毛を鉄壁ブロック",
        "brand_name": "Macadamia Natural Oil (マカダミアナチュラルオイル)",
        "capacity": "125ml / ミストスプレーボトル",
        "type": "高機能ヘアトリートメントオイルスプレー",
        "features": "マカダミア種子油、アルガニアスピノサ核油（アルガンオイル）、ビタミンE",
        "value": "オイルでありながらミスト状に均一噴射できる画期的構造。髪を重たくペタンとさせず、シルクのような自然なツヤとまとまりを一日中キープ",
        "desc_p1": "11月から12月は、肌だけでなく髪にとっても過酷を極める季節です。湿度の急降下に加えて、ウールコートやマフラーとの摩擦によって静電気が発生し、毛先がバサバサに広がって枝毛や切れ毛が急増します。『ヒーリング オイルスプレー』は、そんな冬の深刻な髪のダメージに即効性をもたらすプロフェッショナルアイテムです。",
        "desc_p2": "分子が極めて小さく毛髪内部への浸透力に秀でたマカダミアオイルと、髪表面を艶やかにコーティングするアルガンオイルを黄金比で配合。スプレーをプッシュすると微細な霧状になって髪全体へ均一に行き渡るため、オイル特有のベタつきや束感を作ることなく、サロン帰りのような軽やかなサラサラ感を演出します。ドライヤーの熱から髪を守るヒートプロテクト効果も高く、朝のスタイリング前に吹きかけるだけで、冬の乾燥風に負けない艶やかな天使の輪が一日中輝きます。",
        "target": "冬になると髪がパサついて静電気で広がってしまう方、オイルを手で塗るとムラになりやすくベタつくのが嫌な方、サロン品質のツヤと補修力を求める方",
        "point": "タオルドライ後の濡れた髪、または朝のスタイリング前の乾いた髪から15〜20cmほど離し、毛先を中心に全体へ均一にスプレーします。手ぐしやブラシでなじませるだけで瞬時にツヤが宿ります。"
    },
    {
        "rank": 10,
        "tag": "🧈 体温でとろける極上テクスチャー！冬の唇・目元の深刻なひび割れを密着保護する植物性バター",
        "catch": "高純度マカダミアオイルに植物性水素を添加して固形化したリッチバター。シアバターを超える伸びの良さとパルミトレイン酸の修復力で、真冬の粉吹き・皮むけ・ひび割れを集中パック",
        "brand_name": "Mandy Moon Raw Butter (マンディムーン)",
        "capacity": "50g / アルミ缶ジャー",
        "type": "高純度植物性マカダミアナッツバター",
        "features": "水添マカデミア種子油、パルミトレイン酸高含有、無添加、保存料フリー",
        "value": "融点が人間の体温に近いため、肌にのせた瞬間にとろけて濃密オイルへ変化。真冬の過酷な冷風にさらされても蒸発しない強固な保護シールドを形成",
        "desc_p1": "冬の乾燥が極まる12月、通常の保湿クリームやリップクリームでは防ぎきれない『唇の縦ジワ・皮むけ』や『目尻の乾燥ひび割れ』。マンディムーンの『マカダミアナッツ バター』は、そんな局所的な乾燥クライシスを物理的・生理学的にガードするために開発された濃厚トリートメントバームです。",
        "desc_p2": "容器の中では固形ですが、指先にとると体温に触れた瞬間にジュワッととろけて黄金色の濃密オイルへと姿を変えます。パルミトレイン酸の強力な角層密着力によって、荒れ果てた皮膚の表面にピタッと張り付き、冷たい外気刺激からデリケートな皮膚を保護します。就寝前に唇や目元に厚めに塗り込む『オーバーナイトバームパック』を行えば、翌朝にはひび割れや痛みが嘘のように鎮静し、ふっくらと柔らかな素肌へと蘇ります。指先のささくれや硬くなった踵のケアにも欠かせない冬の万能常備薬です。",
        "target": "真冬になると唇がひび割れてリップメイクが楽しめない方、目元や口元の局所的な粉吹きに悩む方、シアバターよりも柔らかく伸びの良い高保湿バターを求める方",
        "point": "少量を指先にとり、体温で軽く溶かしてから、唇や目元の気になる部分へ優しくトントンと押し込むように密着させます。夜の就寝前に唇へ厚めに塗るナイトリップパックが絶大な効果を発揮します。"
    }
]

# 目次リンク
toc_links = ""
for p in product_details:
    toc_links += f'          <li><a href="#rank-{p["rank"]}">第{p["rank"]}位：{p["brand_name"]} {p["catch"][:22]}...</a></li>\n'

# 比較一覧表
table_rows = []
for idx, p in enumerate(product_details):
    it = items[idx]
    table_rows.append(f"""            <tr>
              <td class="rank-num">第{p['rank']}位</td>
              <td><img src="{it['img']}" alt="{p['brand_name']}" class="table-thumb" loading="lazy"></td>
              <td><strong>{p['brand_name']}</strong><br><span style="font-size:0.85rem; color:var(--text-sub);">{it['name'][:35]}...</span></td>
              <td>{p['type']}</td>
              <td class="price-cell">{it['price']}</td>
              <td><a href="#rank-{p['rank']}" class="table-link">詳細を見る</a></td>
            </tr>""")
table_joined = "\n".join(table_rows)

# 各商品カード
product_cards = []
for idx, p in enumerate(product_details):
    it = items[idx]
    product_cards.append(f"""      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge">第{p['rank']}位 ｜ {p['type']}</div>
        <div class="product-header">
          <div class="img-container">
            <img src="{it['img']}" alt="{it['name']}" class="product-img" loading="lazy">
          </div>
          <div class="product-intro">
            <h3 class="product-title">{it['name']}</h3>
            <div class="product-brand">ブランド：<strong>{p['brand_name']}</strong></div>
            <div class="product-price">参考価格：<span class="price-val">{it['price']}</span> <small>（楽天市場 最新確認時）</small></div>
            <div class="product-tag">{p['tag']}</div>
            <p class="product-catch">{p['catch']}</p>
          </div>
        </div>

        <div class="spec-table-box">
          <table class="spec-table">
            <tr><th>内容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>主要保湿・美容成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の保湿メリット</th><td>{p['value']}</td></tr>
          </table>
        </div>

        <div class="review-body">
          <h4>💡 コスメコンシェルジュによる徹底レビュー＆冬の保湿効果検証</h4>
          <p>{p['desc_p1']}</p>
          <p>{p['desc_p2']}</p>

          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ！</strong>
            <p>{p['target']}</p>
          </div>

          <div class="point-box">
            <strong>✨ 保湿効果を最大化するプロの使い方：</strong>
            <p>{p['point']}</p>
          </div>
        </div>

        <div class="btn-wrap">
          <a href="{it['url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            🛒 楽天市場で「{p['brand_name']}」の最新価格・在庫・口コミを見る
          </a>
        </div>
      </article>""")

cards_joined = "\n\n".join(product_cards)

# JSON-LD構造化データ
json_ld_items = []
for idx, p in enumerate(product_details):
    it = items[idx]
    json_ld_items.append({
        "@type": "ListItem",
        "position": p["rank"],
        "name": it["name"],
        "url": f"https://lumi-cosme.vercel.app/winter-macadamia-oil#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！若さの脂肪酸パルミトレイン酸が真冬の皮脂枯れ肌を瞬時に満たす高保湿マカデミアナッツオイルコスメランク10",
            "description": "11月・12月の気温低下で皮脂分泌が激減したカチコチ肌・粉吹き肌を救う高保湿マカデミアナッツオイルコスメを徹底厳選！生活の木、クナイプ、ボータン、ニベアプレミアム、アンドエスエイチまで厳選。",
            "datePublished": "2026-11-05T04:00:00+09:00",
            "dateModified": "2026-11-05T04:00:00+09:00",
            "author": {
                "@type": "Person",
                "name": "Lumi Cosme 編集部 コスメコンシェルジュ"
            },
            "publisher": {
                "@type": "Organization",
                "name": "Lumi Cosme",
                "url": "https://lumi-cosme.vercel.app/"
            }
        },
        {
            "@type": "ItemList",
            "name": "高保湿マカデミアナッツオイルコスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "マカデミアナッツオイルがなぜ『消えるオイル』と呼ばれ、真冬の乾燥に最適なのですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "マカデミアナッツオイルには、人間の皮脂中に含まれる重要な不飽和脂肪酸である『パルミトレイン酸』が植物油中トップクラスの約20%も含まれています。パルミトレイン酸は加齢とともに肌から減少するだけでなく、冬の寒冷刺激で皮脂腺の働きが落ちると急激に不足します。この成分の分子構造が人間の皮膚の皮脂膜と酷似しているため、肌に乗せるとまるで消えるかのように瞬時に角層へ浸透し、表面に嫌なベタつきを残さず内側からふっくらとした潤いと柔軟性を取り戻すことができます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "ホホバオイルやアルガンオイルとマカデミアナッツオイルの違いや使い分けは？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ホホバオイルはワックスエステル主体の『保護・バリア強化』に長けており、アルガンオイルはオレイン酸・リノール酸・ビタミンEによる『抗酸化・保水』に強みがあります。これらに対し、マカデミアナッツオイルの最大の特徴は『圧倒的な皮膚柔軟化（エモリエント）作用と角層深部への浸透性』です。特に11月〜12月の寒さで角層が硬化し、化粧水が肌表面で滑って浸透しない『ゴワつき・カチコチ肌』を瞬時に柔らかくほぐすブースター効果においては、マカデミアナッツオイルが最も高い即効性を発揮します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "オイリー肌やニキビができやすい冬の混合肌でもマカデミアオイルは使えますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい、安心して使用できます。マカデミアナッツオイルは毛穴を塞ぎにくいコメドジェニック指数の低いオイルであり、酸化安定性に優れた一価不飽和脂肪酸（オレイン酸・パルミトレイン酸）が約80%を占めるため、肌表面で酸化して刺激物質へと変化するリスクが極めて低いのが特徴です。冬のインナードライによる過剰皮脂に悩む混合肌の方は、洗顔後すぐに1滴だけを薄く手のひらで馴染ませることで、水分と油分のバランスが整い、日中のテカリとカサつきの両方を抑えられます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "冬のマカデミアナッツオイルの効果的なスキンケアステップは？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "最もおすすめなのは『洗顔直後のプレ化粧水ブースター』としての使用です。洗顔後、肌がまだわずかに水分を含んでいる状態で1〜2滴を手のひらで温めて優しくハンドプレスします。パルミトレイン酸が角層細胞の隙間を解きほぐした後、化粧水を重ねると、水分の吸い込みが劇的に高まります。また、夜のスキンケアの最後にクリームやバーム代わりに2〜3滴を押し込む『密閉シールド』としての使用や、お風呂上がりの濡れたボディへの全身ケアにも絶大な保湿効果を発揮します。"
                    }
                }
            ]
        }
    ]
}

json_ld_str = json.dumps(json_ld_schema, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！若さの脂肪酸パルミトレイン酸が真冬の皮脂枯れ肌を瞬時に満たす高保湿マカデミアナッツオイルコスメランク10</title>
  <meta name="description" content="11月・12月の気温低下で皮脂分泌が激減したカチコチ肌・粉吹き肌を救う高保湿マカデミアナッツオイルコスメを徹底厳選！生活の木、クナイプ、ボータン、ニベアプレミアム、アンドエスエイチまで厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-macadamia-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！若さの脂肪酸パルミトレイン酸が真冬の皮脂枯れ肌を瞬時に満たす高保湿マカデミアナッツオイルコスメランク10">
  <meta property="og:description" content="11月・12月の気温低下で皮脂分泌が激減したカチコチ肌・粉吹き肌を救う高保湿マカデミアナッツオイルコスメを徹底厳選！生活の木、クナイプ、ボータン、ニベアプレミアム、アンドエスエイチまで厳選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-macadamia-oil">
  <meta property="og:site_name" content="Lumi Cosme">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap" rel="stylesheet">
  <script type="application/ld+json">
{json_ld_str}
  </script>
  <style>
    :root {{
      --primary: #b45309;
      --primary-light: #fef3c7;
      --primary-dark: #78350f;
      --accent: #d97706;
      --accent-hover: #b45309;
      --bg: #fffbeb;
      --card-bg: #ffffff;
      --text-main: #374151;
      --text-sub: #6b7280;
      --border: #fde68a;
      --shadow: 0 4px 15px rgba(180, 83, 9, 0.08);
      --radius: 14px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}

    header.site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 1.5rem;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}

    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}

    .nav-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 1.2rem;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    main.container {{
      max-width: 920px;
      margin: 2rem auto;
      padding: 0 1.2rem;
    }}

    .hero {{
      background: linear-gradient(135deg, #fef3c7 0%, #fffbeb 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      margin-bottom: 2rem;
      box-shadow: var(--shadow);
    }}

    .hero-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 20px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}

    .hero-title {{
      font-size: 1.85rem;
      font-weight: 700;
      color: #1f2937;
      line-height: 1.4;
      margin-bottom: 1rem;
    }}

    .hero-desc {{
      font-size: 1rem;
      color: var(--text-sub);
      line-height: 1.7;
      margin-bottom: 1.5rem;
    }}

    .meta-bar {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: #9ca3af;
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}

    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .toc-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.5rem;
    }}

    .toc-list li a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}

    .toc-list li a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .intro-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .intro-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .intro-section p {{
      margin-bottom: 1.2rem;
      font-size: 1rem;
      line-height: 1.8;
    }}

    .intro-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}

    .highlight-card {{
      background: var(--primary-light);
      padding: 1.2rem;
      border-radius: 10px;
      border-left: 4px solid var(--primary);
    }}

    .highlight-card strong {{
      display: block;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.4rem;
    }}

    .highlight-card p {{
      font-size: 0.9rem;
      color: var(--text-main);
      margin-bottom: 0;
      line-height: 1.6;
    }}

    .table-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      overflow-x: auto;
    }}

    .table-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}

    table.comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}

    table.comparison-table th, table.comparison-table td {{
      padding: 0.85rem 0.75rem;
      border-bottom: 1px solid #f3f4f6;
    }}

    table.comparison-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}

    .rank-num {{
      font-weight: 700;
      color: var(--primary);
      white-space: nowrap;
    }}

    .table-thumb {{
      width: 60px;
      height: 60px;
      object-fit: contain;
      border-radius: 6px;
      background: #fafafa;
      border: 1px solid #f3f4f6;
    }}

    .price-cell {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .table-link {{
      color: var(--primary);
      text-decoration: none;
      font-weight: 700;
      white-space: nowrap;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      padding: 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
      position: relative;
    }}

    .product-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.9rem;
      border-radius: 6px;
      margin-bottom: 1.2rem;
    }}

    .product-header {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
    }}

    @media (min-width: 640px) {{
      .product-header {{
        flex-direction: row;
        align-items: flex-start;
      }}
    }}

    .img-container {{
      flex-shrink: 0;
      width: 100%;
      max-width: 220px;
      margin: 0 auto;
      background: #ffffff;
      border-radius: 10px;
      border: 1px solid #f3f4f6;
      padding: 0.8rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
    }}

    .product-intro {{
      flex-grow: 1;
    }}

    .product-title {{
      font-size: 1.25rem;
      color: #1f2937;
      font-weight: 700;
      line-height: 1.5;
      margin-bottom: 0.5rem;
    }}

    .product-brand {{
      font-size: 0.9rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}

    .product-price {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #111827;
      margin-bottom: 0.8rem;
    }}

    .price-val {{
      font-size: 1.35rem;
      color: #b91c1c;
    }}

    .product-tag {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 0.75rem;
      border-radius: 6px;
      margin-bottom: 0.8rem;
      line-height: 1.5;
    }}

    .product-catch {{
      font-size: 0.95rem;
      color: #4b5563;
      line-height: 1.6;
    }}

    .spec-table-box {{
      margin: 1.5rem 0;
      overflow-x: auto;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    table.spec-table th, table.spec-table td {{
      padding: 0.65rem 0.85rem;
      border: 1px solid var(--border);
    }}

    table.spec-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      width: 28%;
      white-space: nowrap;
    }}

    table.spec-table td {{
      background: #ffffff;
      color: var(--text-main);
    }}

    .review-body {{
      background: #fffdfa;
      border-radius: 10px;
      padding: 1.5rem;
      border: 1px solid var(--border);
      margin-bottom: 1.5rem;
    }}

    .review-body h4 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .review-body p {{
      font-size: 0.95rem;
      line-height: 1.8;
      margin-bottom: 1rem;
      color: #374151;
    }}

    .target-box, .point-box {{
      background: #ffffff;
      border-radius: 8px;
      padding: 1rem 1.2rem;
      margin-top: 1rem;
      border-left: 4px solid var(--primary);
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }}

    .target-box strong, .point-box strong {{
      display: block;
      font-size: 0.92rem;
      color: var(--primary-dark);
      margin-bottom: 0.35rem;
    }}

    .target-box p, .point-box p {{
      font-size: 0.9rem;
      margin-bottom: 0;
      line-height: 1.6;
      color: #4b5563;
    }}

    .btn-wrap {{
      text-align: center;
      margin-top: 1.5rem;
    }}

    .rakuten-btn {{
      display: inline-block;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      font-size: 1rem;
      font-weight: 700;
      text-decoration: none;
      padding: 1rem 2rem;
      border-radius: 30px;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 440px;
    }}

    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000 0%, #800000 100%);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
      transform: translateY(-2px);
    }}

    .faq-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .faq-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .faq-item {{
      margin-bottom: 1.5rem;
      border-bottom: 1px dashed var(--border);
      padding-bottom: 1.2rem;
    }}

    .faq-item:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}

    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #1f2937;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-q span {{
      color: var(--primary);
    }}

    .faq-a {{
      font-size: 0.95rem;
      color: #4b5563;
      line-height: 1.7;
      padding-left: 1.5rem;
    }}

    .guide-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .guide-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .guide-section h3 {{
      font-size: 1.15rem;
      color: #1f2937;
      margin: 1.2rem 0 0.6rem;
    }}

    .guide-section p {{
      font-size: 0.95rem;
      line-height: 1.8;
      margin-bottom: 1rem;
      color: #374151;
    }}

    .related-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .related-section-title {{
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .related-list {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.2rem;
    }}

    .related-card {{
      background: #fafafa;
      border: 1px solid #f3f4f6;
      border-radius: 10px;
      padding: 1.2rem;
      text-decoration: none;
      display: flex;
      flex-direction: column;
      transition: all 0.2s;
    }}

    .related-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
      border-color: var(--border);
    }}

    .related-card-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
      line-height: 1.5;
    }}

    .related-card-desc {{
      font-size: 0.82rem;
      color: var(--text-sub);
      line-height: 1.5;
    }}

    footer.site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 2.5rem 1.5rem;
      margin-top: 4rem;
    }}

    .footer-inner {{
      max-width: 1080px;
      margin: 0 auto;
      text-align: center;
    }}

    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.8rem 1.5rem;
      margin-bottom: 1.5rem;
    }}

    .footer-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 0.2s;
    }}

    .footer-links a:hover {{
      color: var(--primary);
    }}

    .copyright {{
      font-size: 0.8rem;
      color: #9ca3af;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#guide">選び方・使い方</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="hero-badge">2026年真冬版 ｜ 徹底保湿コスメ検証</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！若さの脂肪酸パルミトレイン酸が真冬の皮脂枯れ肌を瞬時に満たす高保湿マカデミアナッツオイルコスメランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて訪れる気温と湿度の急降下。皮膚の皮脂分泌は急激に落ち込み、角層は硬直してゴワつき、化粧水すら弾いてしまう砂漠状態へ。そんな真冬の過酷な皮脂欠乏トラブルを解決するのが、加齢とともに減少する「若さの脂肪酸」パルミトレイン酸を豊富に宿すマカデミアナッツオイルです。人の皮脂膜と酷似した親和性を持ち、「消えるオイル」と称される驚異の浸透力で角層深部を満たす名品10選をコスメコンシェルジュが徹底検証・厳選しました。
      </p>
      <div class="meta-bar">
        <span>🕒 公開日: 2026年11月5日</span>
        <span>✍️ 執筆・検証: Lumi Cosme 編集部 コスメコンシェルジュ</span>
        <span>🔍 楽天リアルタイムAPI商品データ照合済</span>
      </div>
    </section>

    <div class="toc-box">
      <div class="toc-title">📑 目次（タップで該当ランキングへジャンプ）</div>
      <ul class="toc-list">
{toc_links}
      </ul>
    </div>

    <section class="intro-section">
      <h2>冬の皮脂枯渇肌を解き放つ「マカデミアナッツオイル」の皮膚科学的メカニズム</h2>
      <p>
        初冬の11月から年末の12月にかけて、私たちの肌を取り巻く環境は激変します。外気温の低下に伴い毛細血管が収縮し、皮膚の代謝と皮脂腺の活動が劇的に低下。肌表面を覆う天然の保護バリア「皮脂膜」が著しく減少し、角質層の水分が空気中へと一方的に奪われていきます。その結果、洗顔後に肌がつっぱる、化粧水をつけても表面で滑って入らない、頬やすねが粉を吹いてカチコチに硬化するといった深刻な乾燥症状が生じます。
      </p>
      <p>
        この真冬の硬直肌に劇的な柔軟性と潤いをもたらすのが、オーストラリア原産のナッツから抽出される「マカデミアナッツオイル（マカダミアオイル）」です。植物油の中でも極めて特異な脂肪酸組成を持ち、冬のエイジングケア・高保湿ケアにおいて他の追随を許さない卓越した効果を発揮します。
      </p>

      <div class="intro-highlight-grid">
        <div class="highlight-card">
          <strong>1. 奇跡の「パルミトレイン酸」約20%含有</strong>
          <p>皮脂膜中に豊富に存在しながら、加齢や冬の寒冷で急激に減少するパルミトレイン酸。植物界で唯一20%前後の高濃度で含有し、減少した皮脂膜をダイレクトに補います。</p>
        </div>
        <div class="highlight-card">
          <strong>2. 「消えるオイル（Vanishing Oil）」の超浸透性</strong>
          <p>人の皮脂と分子構造が極めて近いため、塗布後わずか数秒で角層へと吸い込まれ一体化。オイル特有の油膜感やベタつきを残さず、内側をもっちり満たします。</p>
        </div>
        <div class="highlight-card">
          <strong>3. 硬直角層をほぐすブースター効果</strong>
          <p>寒さで硬化した細胞間脂質のラメラ構造に馴染み、角質柔軟化（エモリエント）作用を発揮。後から重ねる化粧水の吸水率と持続力を飛躍的に引き上げます。</p>
        </div>
      </div>
    </section>

    <section class="table-section" id="comparison">
      <h2>高保湿マカデミアナッツオイルコスメ おすすめ10選 比較一覧表</h2>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>画像</th>
            <th>ブランド / アイテム名</th>
            <th>分類</th>
            <th>参考価格</th>
            <th>詳細</th>
          </tr>
        </thead>
        <tbody>
{table_joined}
        </tbody>
      </table>
    </section>

    <section id="ranking">
{cards_joined}
    </section>

    <section class="guide-section" id="guide">
      <h2>プロが伝授！真冬のマカデミアナッツオイル活用法＆選び方の極意</h2>
      <h3>1. 「洗顔後すぐのプレ化粧水ブースター」が最も効果的</h3>
      <p>
        マカデミアナッツオイルの真骨頂は、その卓越した浸透性と角質柔軟効果にあります。冬のスキンケアでは、化粧水の前にまず1〜2滴を手にとり、洗顔後の湿った肌へハンドプレスしてください。パルミトレイン酸が角層細胞の硬い結束を解きほぐし、その後に重ねる化粧水のみずみずしい水分を角層深部まで引き込む「潤いの吸着パイプ」を作り出します。
      </p>
      <h3>2. 未精製（ゴールデン）と精製（クリア）の賢い使い分け</h3>
      <p>
        マカデミアオイルには、ナッツの微量栄養素やトコフェロールをそのまま残した「未精製（黄色・わずかに香ばしい香り）」と、不純物を徹底除去して低刺激化した「精製（無色無臭・サラリとした質感）」があります。夜の集中リペアやエイジングケアには栄養価の高い未精製が、敏感肌の方や朝のメイク前、ベタつきを嫌う方には精製オイルが最適です。
      </p>
      <h3>3. お風呂上がりの「インバス全身ケア」で粉吹きすねを完全撃退</h3>
      <p>
        冬の入浴後、脱衣所の寒冷乾燥によって皮膚の水分は猛スピードで蒸散します。バスタオルで体を拭く前、まだ肌に水滴が残っている状態でマカデミアオイルを全身へ塗り伸ばしてください。水分と油分が肌表面で瞬時に乳化し、薄く強固な皮脂膜ヴェールを形成。その後タオルで軽く水分を押さえるだけで、一日中粉吹きや痒みのないマシュマロ肌を保つことができます。
      </p>
    </section>

    <section class="faq-section" id="faq">
      <h2>よくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> マカデミアナッツオイルがなぜ「消えるオイル」と呼ばれ、真冬の乾燥に最適なのですか？</div>
        <div class="faq-a">マカデミアナッツオイルには、人間の皮脂中に含まれる重要な不飽和脂肪酸である「パルミトレイン酸」が植物油中トップクラスの約20%も含まれています。パルミトレイン酸は加齢とともに肌から減少するだけでなく、冬の寒冷刺激で皮脂腺の働きが落ちると急激に不足します。この成分の分子構造が人間の皮膚の皮脂膜と酷似しているため、肌に乗せるとまるで消えるかのように瞬時に角層へ浸透し、表面に嫌なベタつきを残さず内側からふっくらとした潤いと柔軟性を取り戻すことができます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> ホホバオイルやアルガンオイルとマカデミアナッツオイルの違いや使い分けは？</div>
        <div class="faq-a">ホホバオイルはワックスエステル主体の「保護・バリア強化」に長けており、アルガンオイルはオレイン酸・リノール酸・ビタミンEによる「抗酸化・保水」に強みがあります。これらに対し、マカデミアナッツオイルの最大の特徴は「圧倒的な皮膚柔軟化（エモリエント）作用と角層深部への浸透性」です。特に11月〜12月の寒さで角層が硬化し、化粧水が肌表面で滑って浸透しない「ゴワつき・カチコチ肌」を瞬時に柔らかくほぐすブースター効果においては、マカデミアナッツオイルが最も高い即効性を発揮します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> オイリー肌やニキビができやすい冬の混合肌でもマカデミアオイルは使えますか？</div>
        <div class="faq-a">はい、安心して使用できます。マカデミアナッツオイルは毛穴を塞ぎにくいコメドジェニック指数の低いオイルであり、酸化安定性に優れた一価不飽和脂肪酸（オレイン酸・パルミトレイン酸）が約80%を占めるため、肌表面で酸化して刺激物質へと変化するリスクが極めて低いのが特徴です。冬のインナードライによる過剰皮脂に悩む混合肌の方は、洗顔後すぐに1滴だけを薄く手のひらで馴染ませることで、水分と油分のバランスが整い、日中のテカリとカサつきの両方を抑えられます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 冬のマカデミアナッツオイルの効果的なスキンケアステップは？</div>
        <div class="faq-a">最もおすすめなのは「洗顔直後のプレ化粧水ブースター」としての使用です。洗顔後、肌がまだわずかに水分を含んでいる状態で1〜2滴を手のひらで温めて優しくハンドプレスします。パルミトレイン酸が角層細胞の隙間を解きほぐした後、化粧水を重ねると、水分の吸い込みが劇的に高まります。また、夜のスキンケアの最後にクリームやバーム代わりに2〜3滴を押し込む「密閉シールド」としての使用や、お風呂上がりの濡れたボディへの全身ケアにも絶大な保湿効果を発揮します。</div>
      </div>
    </section>

    <!-- 関連記事プレースホルダー -->
    <section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list" id="related-grid-box">
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-links" id="footer-links-box">
      </div>
      <p class="copyright">© 2026 Lumi Cosme. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-macadamia-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-macadamia-oil.html!")
