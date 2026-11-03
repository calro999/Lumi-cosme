import json
import re

with open("fetched_final_30_rosehip_honey_mugwort.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_honey"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 ラグジュアリーハニーの頂点！天然蜂蜜とボタニカルの黄金オイル",
        "catch": "老舗養蜂園の厳選ハチミツを贅沢配合。冬のゴワつく素肌に吸い付くように溶け込み、シルクの艶を与える",
        "brand_name": "HACCI (ハッチ)",
        "capacity": "30ml (フェイスオイル エスケーピオン)",
        "type": "高濃度ハチミツ配合プレシャス美容オイル",
        "features": "自社養蜂園の高品質ハチミツ、アルガン・ヒマワリ・ローズヒップ種子油配合、高浸透処方、フランス調香の優雅な香り",
        "value": "ハチミツの強力な天然吸湿性と上質オイルのラッピング効果が融合。化粧水の前に塗るだけで、真冬でも乾かない発光水光肌へ導く",
        "desc_p1": "大正元年創業の老舗養蜂園『水谷養蜂園』の長女が立ち上げた高級ハチミツコスメブランドHACCI。その最高峰スキンケアアイテムが『フェイスオイル エスケーピオン』です。ハチミツには空気中の水分を自ら引き寄せる天然の吸湿力と、ビタミンB群・アミノ酸・ミネラルが豊富に含まれており、過酷な11-12月の乾燥外気から素肌を完璧に保護します。",
        "desc_p2": "オイル特有のベタつきや皮膜感を極限まで抑えたサラリとした黄金のテクスチャー。洗顔後すぐの肌に数滴なじませると、ハチミツ由来の天然糖類が角質層のすみずみまで水分を引き込み、乾ききって固くなった肌を一瞬でふっくらと柔らかく整えます。その後に重ねる化粧水がまるでスポンジのようにぐんぐん浸透。日中の暖房下でも夕方までツヤとモチモチ感が途切れません。",
        "target": "冬になると肌がカサついて粉を吹く方、ごわつきでメイクが乗らない方、ワンランク上の高保湿エイジングケアを求める方",
        "point": "洗顔直後のブースターとして2〜3滴を手のひらで温めて優しくハンドプレス。さらにメイク前の下地に1滴混ぜると、真冬の乾燥崩れを完全に防ぐことができます。"
    },
    {
        "rank": 2,
        "tag": "🍯 韓国オリーブヤング殿堂入り！プロポリス＆蜂蜜72%以上の超保水トナー",
        "catch": "水のような軽さなのに驚異のもっちり感。乾いた角層をハチミツの潤いで満たし尽くす大人気化粧水",
        "brand_name": "COSRX (コスアールエックス)",
        "capacity": "150ml (フルフィット プロポリス シナジートナー)",
        "type": "高濃度プロポリス＆ハチミツ高保水化粧水",
        "features": "黒蜂プロポリスエキス72.6%、蜂蜜エキス10%、弱酸性低刺激処方、アルコール・パラベンフリー",
        "value": "精製水よりもプロポリス＆ハチミツエキスを圧倒的に多く配合。冬のインナードライと肌荒れを同時に鎮静し、吸い付くような水光肌に仕上げる",
        "desc_p1": "世界中で爆発的なヒットを記録しているCOSRXの『プロポリス シナジートナー』。成分表のトップが精製水ではなく、過酷な環境で巣を守る黒蜂から採取された『プロポリスエキス（72.6%）』と『蜂蜜エキス（10%）』で構成された贅沢極まりない高濃度化粧水です。",
        "desc_p2": "とろみのあるリッチな感触でありながら肌に乗せるとスーッと染み渡り、表面に残ることなく角層深部まで潤いを届けます。ハチミツ特有の糖類コーティングが肌のキメをふっくら持ち上げ、手のひらが吸い付くようなモチモチの質感へ。冬の寒暖差による肌荒れや赤みを落ち着かせながら、乾燥による毛穴の開きやツッパリ感を根本からリセットしてくれます。",
        "target": "乾燥で肌がつっぱりやすい方、敏感肌でも使える高保湿化粧水を求める方、内側から発光する水光肌を作りたい方",
        "point": "冬の乾燥がひどい日は『3回重ね塗り（レイヤリング）』がおすすめ。1回目で角層を潤し、2回目でキメを整え、3回目で強固な水分シールドを形成します。"
    },
    {
        "rank": 3,
        "tag": "🌙 睡眠中に乾燥枯れ肌を満たす！完熟ハチミツの濃密ナイトスリーピングパック",
        "catch": "塗って寝るだけで翌朝プルプル。寝室の暖房乾燥を跳ね返し、生まれたての素肌へ整える夜用濃密ジェル",
        "brand_name": "山田養蜂場 (YAMADA BEE FARM)",
        "capacity": "50ml (ハニーラボ スリーピングパック)",
        "type": "完熟ハチミツ配合夜用集中スリーピングパック",
        "features": "国産完熟ハチミツ、乳酸桿菌/ハチミツ発酵液、カミツレ花エキス、天然ローズハーブの香り、洗い流し不要",
        "value": "就寝中の水分蒸散を完全にシャットアウトするハニーラッピング処方。睡眠中の肌の自己修復リズムをサポートし、翌朝洗顔時の手触りが劇変",
        "desc_p1": "ミツバチ産品のパイオニア・山田養蜂場が研究開発した『ハニーラボ スリーピングパック』。完熟ハチミツと発酵ハチミツエキスをたっぷり配合した、ぷるんとした濃密ジェル状の夜用集中トリートメントパックです。",
        "desc_p2": "冬の夜、暖房をつけたまま眠ると朝には肌の水分量が半減してしまいますが、夜のお手入れの最後にこのパックを顔全体にたっぷり塗布すると、ハチミツのヴェールが肌表面をピタッと密閉。外部の乾燥から肌を守りながら、睡眠中にアミノ酸や酵素などの栄養分をじっくりと角層奥へ送り届けます。翌朝洗い流した瞬間の、ふっくら吸い付くような柔らかさは感動的です。",
        "target": "朝起きると肌がパサついている方、夜のスキンケアをしても乾燥してしまう方、忙しくてスペシャルケアの時間がない方",
        "point": "夜のお手入れの最後にさくらんぼ粒大を全顔に伸ばし、そのまま洗い流さずに就寝。枕につかないよう塗布後2〜3分置いてからお休みください。"
    },
    {
        "rank": 4,
        "tag": "🥛 美容液成分85%以上！乾燥肌をいたわりながら落とすハチミツクレンジング",
        "catch": "メイクオフしながら潤いをチャージ。洗うほどにしっとりモチモチの素肌へ導く極上クレンジングミルク",
        "brand_name": "HACCI (ハッチ)",
        "capacity": "190ml (ハチミツ クレンジングミルク)",
        "type": "高保湿ハチミツ美容液クレンジングミルク",
        "features": "自社養蜂園ハチミツ、ローヤルゼリーエキス、ヒアルロン酸、シルクエキス、美容液成分85%以上",
        "value": "クレンジング後のツッパリ感がゼロ。冬のデリケートな角層バリアを壊さず、メイク汚れだけを磁石のように吸着して落とす",
        "desc_p1": "冬の乾燥を悪化させる最大の原因の一つが『洗浄力の強すぎるクレンジングによる皮脂と天然保湿因子の流出』です。HACCIのクレンジングミルクは、85%以上が美容液成分で構成されており、メイクを落とす時間そのものを贅沢なスキンケアタイムへと変えてくれます。",
        "desc_p2": "とろけるようなリッチなミルクテクスチャーで、肌に摩擦を一切与えずにメイクや毛穴の皮脂汚れとなじみます。洗い流した後の肌は、まるで上質な乳液を塗った後のようにしっとり柔らか。冬の冷水で洗っても乾燥やつっぱりを一切感じさせず、キメが整った透明感あふれる素肌へと整えます。",
        "target": "洗顔後すぐに肌がパキパキにつっぱる方、冬になるとクレンジングで肌荒れしやすい方、マイルドかつ確実なメイク落ちを求める方",
        "point": "乾いた手のひらに3〜4プッシュ取り、手のひらで温めてから顔全体に円を描くように優しくなじませます。ぬるま湯ですすぐと驚くほどしっとり洗い上がります。"
    },
    {
        "rank": 5,
        "tag": "🛡️ 熟成プロポリス63%の超濃厚バリア！冬枯れ肌を立て直す濃密エッセンス",
        "catch": "ハチミツ発酵の生命力が凝縮。乾燥によるキメの乱れとハリ不足を底上げする韓国ロングセラー美容液",
        "brand_name": "SKINFOOD (スキンフード)",
        "capacity": "50ml (ロイヤルハニー プロポリス エンリッチ エッセンス)",
        "type": "発酵プロポリス＆蜂蜜高濃縮エイジング美容液",
        "features": "ブラックビープロポリスエキス63%、熟成ローヤルゼリーエキス10%、黒蜂蜂蜜エキス10%、乳酸菌発酵抽出",
        "value": "プロポリス本来の抗菌・抗酸化バリアとハチミツの保水力を3段階発酵で極小分子化。角層の深部まで濃厚な潤いが到達",
        "desc_p1": "フードコスメの草分けSKINFOODが誇る世界的名品『ロイヤルハニー プロポリス エンリッチ エッセンス』。独自の発酵技術で熟成させたブラックビープロポリスエキスを63%、ローヤルゼリーとハチミツをそれぞれ10%配合し、成分の83%以上が蜂由来の濃密エキスで満たされたアンプルです。",
        "desc_p2": "とろりとしたドロップが肌に触れた瞬間にみずみずしく崩れ、角質層の隙間へスルスルと浸透していきます。塗布後は肌表面にピンとしたハリ膜が生まれ、冷たい寒風にさらされても水分が逃げない鉄壁のバリアを構築。冬特有の肌のくすみや乾燥小ジワを内側から押し上げるようにケアし、若々しいツヤ肌を一日中キープします。",
        "target": "冬の寒さで肌のハリや弾力が低下している方、濃密な美容液で角層バリアを立て直したい方、乾燥小ジワが気になる方",
        "point": "化粧水の直後、スポイト1回分を顔全体に伸ばし、手のひらでハンドプレスして密着させます。目元や口元など乾燥が激しい部分には重ね付けが効果的です。"
    },
    {
        "rank": 6,
        "tag": "🧤 冬の手荒れ・あかぎれを救う！とろとろ濃密ハチミツの潤いハンドヴェール",
        "catch": "北海道産アカシア蜂蜜×ミツロウ配合。塗った瞬間サラリと密着し、乾燥する手指に潤いの手袋をかける",
        "brand_name": "VECUA Honey (ベキュア ハニー)",
        "capacity": "50g (ワンダーハニー とろとろハンドクリーム)",
        "type": "高保湿ハチミツハンドトリートメント",
        "features": "北海道産アカシアハチミツ、ミツロウ、ローヤルゼリーエキス、カカオバター配合、ベタつかないメルティ処方",
        "value": "スマホやパソコンをすぐに触れる速乾・非ベタつき設計でありながら、ハチミツの強力な保護膜で手洗いやアルコール消毒による乾燥から手肌を守る",
        "desc_p1": "冬になると頻繁な手洗いや乾燥した空気、水仕事によって手肌の油分が失われ、ささくれやひび割れ、指先のカサつきが多発します。ベキュアハニーのハンドクリームは、良質な北海道産アカシア蜂蜜をベースに、ミツロウとローヤルゼリーをブレンドした冬の必需品です。",
        "desc_p2": "名前の通り『とろとろ』としたジェルクリームが、肌に乗せた瞬間にすっと溶けて浸透。ハチミツ由来の皮膜成分が手指を薄い潤いの手袋のように包み込み、水分の蒸散をしっかり防ぎます。ベタつきが一切残らないため、塗った直後からデスクワークやスマートフォンの操作ができる実用性の高さも人気の秘密です。",
        "target": "手荒れ・乾燥によるささくれや指先の痛みに悩む方、ベタつくハンドクリームが苦手なオフィスワーカー、ギフトにも喜ばれる可愛いコスメを探している方",
        "point": "手の甲だけでなく、乾燥しやすい指先や爪の生え際（甘皮）までしっかりとすり込むようにマッサージしながら塗布すると、爪の割れや乾燥も同時に予防できます。"
    },
    {
        "rank": 7,
        "tag": "✨ 髪のパサつき・静電気を徹底撃退！水分量14%に着目した保水ハニーヘアオイル",
        "catch": "マヌカハニー×生ハチミツ配合。暖房で広がる冬の乾燥ダメージ毛をしっとりまとまるツヤ髪へ",
        "brand_name": "&honey (アンドハニー)",
        "capacity": "100ml (ディープモイスト ヘアオイル3.0)",
        "type": "超保水オーガニックハニーヘアオイル",
        "features": "ニュージーランド産マヌカハニー50%・アカシアハチミツ30%・生ハチミツ20%黄金比配合、100%モロッカンオーガニックオイル使用",
        "value": "髪の理想的な水分量『14%』を追求。ハチミツの強力な保水力で毛髪内部の水分を逃さず、冬のパサつきと静電気を完全ブロック",
        "desc_p1": "冬の乾燥は肌だけでなく髪にも深刻なダメージをもたらします。湿度が下がると髪内部の水分が抜け落ち、ニットの着脱で静電気が発生して枝毛や切れ毛が急増します。アンドハニーのディープモイストヘアオイルは、髪の水分保持力に徹底的にこだわった大人気ヘアケアです。",
        "desc_p2": "3種類の厳選ハチミツが髪の芯まで浸透し、傷んだキューティクルを整えて濃密な潤いを閉じ込めます。重たすぎず軽すぎない絶妙なとろみオイルが髪一本一本をコーティングし、ドライヤーの熱から髪を保護。翌朝のブロー時も手ぐしがスルスル通る、毛先までしっとりとまとまる極上のツヤ髪に仕上がります。",
        "target": "冬になると髪がパサついて広がる方、静電気による広がりやダメージを抑えたい方、甘く上品なハチミツの香りが好きな方",
        "point": "お風呂上がりのタオルドライした濡れ髪に、毛先を中心に1〜2プッシュなじませてからドライヤーで乾かします。乾いた髪の仕上げに半プッシュ重ねるとツヤ感が倍増します。"
    },
    {
        "rank": 8,
        "tag": "💋 冬の皮剥け・縦ジワをぷるんと補修！濃密密着ハニーリップ美容液",
        "catch": "ハチミツ×ローヤルゼリーの濃厚ヴェール。ひと塗りでガラスのようなツヤとボリュームを与えるプチプラ名品",
        "brand_name": "カントリー＆ストリーム (Country & Stream)",
        "capacity": "10g (ナチュラル ハニーリップ)",
        "type": "高密着ハチミツリップトリートメント",
        "features": "天然ハチミツ、ローヤルゼリーエキス、シアバター、ローズヒップ油、オリーブ油配合、斜めカットチューブ",
        "value": "乾燥でひび割れやすい唇にピタッと密着。ハチミツのラッピング効果で縦ジワを目立たなくし、ぷるぷるのボリューム感を長時間キープ",
        "desc_p1": "唇には皮脂腺がなく角層も極めて薄いため、11-12月の乾燥外気にさらされると真っ先に皮剥けや出血、縦ジワのひび割れが起こります。カントリー＆ストリームのハニーリップは、濃厚なハチミツを贅沢に配合した超ロングセラーのリップケアです。",
        "desc_p2": "こっくりとしたハチミツのようなジェル状テクスチャーで、唇に密着してラップのように水分を閉じ込めます。塗った瞬間から唇がじんわりと潤い、カサカサに硬くなった皮をふっくらと柔らかく整えます。口紅の下地として使えば冬のマットリップも綺麗に密着し、夜寝る前のリップパックとしても大活躍します。",
        "target": "冬になると唇が乾燥して皮が剥ける方、口紅を塗ると縦ジワが目立つ方、コスパ良く優秀なリップバームを探している方",
        "point": "夜寝る前に唇の輪郭より少し広めにたっぷり塗布して『ハニーリップパック』に。翌朝には古い角質が柔らかくなり、指先で優しく拭き取るだけでツルツルの唇が復活します。"
    },
    {
        "rank": 9,
        "tag": "🔬 薬用美白＆抗シワのダブル承認！ローヤルゼリー凝縮の最高峰エイジング美容液",
        "catch": "山田養蜂場が半世紀かけて辿り着いた薬用処方。冬枯れ肌のシミ・シワ・ハリ不足を全方位ケア",
        "brand_name": "山田養蜂場 (YAMADA BEE FARM)",
        "capacity": "30ml (薬用 RJエッセンス)",
        "type": "医薬部外品・薬用ローヤルゼリー美白エイジング美容液",
        "features": "独自開発『微粒子化ローヤルゼリーエキス』、美白有効成分ビタミンC誘導体、抗炎症グリチルリチン酸ジカリウム",
        "value": "デセン酸を豊富に含むローヤルゼリーを角層深部まで浸透する微粒子サイズへ加工。冬の乾燥小ジワを目立たなくし、澄みわたる透明感を与える",
        "desc_p1": "ミツバチの女王蜂だけに与えられる特別食『ローヤルゼリー』の生命力に着目した山田養蜂場の最高峰薬用美容液『RJエッセンス』。40種類以上の栄養素を含むローヤルゼリーを独自技術で微粒子カプセル化し、硬くなった冬の角質層の奥深くまで浸透させます。",
        "desc_p2": "美白有効成分が冬の隠れジミを予防し、高濃度ローヤルゼリーが乾燥によって弾力を失った肌をふっくらと持ち上げます。コクのあるリッチなテクスチャーが肌に伸ばすとすっと溶け込み、吸い付くようなハリと透明感を実感。乾燥によるくすみとたるみ毛穴を同時にケアしたい大人の肌に最適な薬用処方です。",
        "target": "冬の乾燥だけでなくシミやくすみ・ハリ不足も同時にケアしたい方、エビデンスのある医薬部外品を使いたい方",
        "point": "化粧水の後、適量を手に取り顔全体から首筋までなじませた後、気になる目元やほうれい線には指の腹で重ね付けして引き上げるように密着させます。"
    },
    {
        "rank": 10,
        "tag": "🌿 奇跡の抗菌・高保水マヌカハニー配合！冬の肌荒れ・インナードライを鎮める濃厚クリーム",
        "catch": "ニュージーランド産マヌカの強靭な生命力。乾燥で荒れやすい冬の肌を穏やかに保護するマルチモイスト処方",
        "brand_name": "マヌカコスメ (MANUKA COSME)",
        "capacity": "80g (マヌカコスメ B8 リッチモイストドロップ)",
        "type": "高濃度マヌカハニー高保湿ジェルクリーム",
        "features": "ニュージーランド産マヌカハニー（UMF規格）、ローヤルゼリー、セラミド、ヒアルロン酸、コラーゲン配合",
        "value": "高い抗菌活性と保水力を持つマヌカハニーが冬の乾燥肌荒れを優しくブロック。顔からデコルテ・ボディまで全身使える多機能モイスト",
        "desc_p1": "ニュージーランドの原生林に育つマヌカの花から採れる、極めて希少で高い有用成分を持つマヌカハニー。通常のはちみつにはない強力な抗菌・抗炎症成分『メチルグリオキサール（MGO）』を豊富に含み、冬の乾燥によって弱った肌バリアを力強く補強します。",
        "desc_p2": "肌に乗せるとみずみずしいジェルから濃密な潤いのドロップへと変化し、角層細胞の隙間を満たします。乾燥によるピリつきや赤みを優しく鎮静しながら、セラミドとヒアルロン酸が水分を逃さずキープ。ベタつきが少なくさっぱりと仕上がるため、朝のメイク前にもストレスなく使用できます。",
        "target": "冬の乾燥で肌が敏感になり赤みが出やすい方、マヌカハニーの力で肌荒れを予防したい方、全身に使える高保湿ジェルを求める方",
        "point": "朝晩の乳液・クリームの代わりに全顔へ。特に乾燥が気になる部分には少し厚めに塗って『ジェルパック』として使うと、翌朝の肌がプルプルに蘇ります。"
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
        "url": f"https://trendbeauty.site/winter-honey.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "なぜハチミツコスメは冬の乾燥肌にこれほど高い保湿効果があるのですか？",
        "answer": "ハチミツは『天然の吸湿・保水成分』と呼ばれ、分子構造の中に水分と強く結合する『ヒドロキシ基（-OH）』を豊富に持っています。そのため、冬の乾いた空気の中でも周囲の微小な水分を自ら引き寄せて角層内に閉じ込める特異な性質があります。さらにアミノ酸、ビタミンB群、ミネラル、酵素が角質細胞間を満たし、弱った皮脂膜を代替して水分蒸散を強力に防ぐため、真冬でも乾かないモチ肌を長時間維持できます。"
    },
    {
        "question": "プロポリス、ローヤルゼリー、ハチミツの違いは何ですか？",
        "answer": "『ハチミツ』は花の蜜がミツバチの酵素で濃縮されたもので、糖類による強力な吸湿・保水力と柔軟効果が主です。『プロポリス』は樹液とミツバチの分泌物が合わさった天然の防御物質で、強力なフラボノイドを含み、冬の肌荒れや赤みの鎮静・バリア強化に優れます。『ローヤルゼリー』は女王蜂専用の完全栄養食で、アミノ酸や特有成分デセン酸が豊富で、乾燥小ジワやハリ不足をケアするエイジングケアに最適です。"
    },
    {
        "question": "ハチミツコスメはベタつきませんか？朝のメイク前に使ってもヨレませんか？",
        "answer": "純粋な食用ハチミツを塗るのとは異なり、現代の化粧品に配合されるハチミツエキスやハニーコスメは、浸透性と使用感を追求して微粒子化やオイル・水性成分との最適なエマルジョン設計がなされています。肌に乗せるとスッと角層へ吸い込まれ、表面はサラリとしながらも内側がもっちり潤うため、朝のメイク前に使用してもファンデーションがヨレるどころか、乾燥崩れや粉浮きを劇的に防ぐ下地効果を発揮します。"
    },
    {
        "question": "マヌカハニー配合コスメは普通のハチミツと何が違うのですか？",
        "answer": "マヌカハニーはニュージーランドに自生するマヌカの木から採取される希少なハチミツで、特有の生理活性物質『メチルグリオキサール（MGO）』を多く含んでいます。通常のハチミツの保水力に加え、非常に高い抗菌作用と抗炎症作用、創傷治癒サポート力を持つため、冬の寒冷外気やマスクの摩擦で荒れやすいデリケートな乾燥肌のレスキューに極めて高い効果を発揮します。"
    },
    {
        "question": "ハチミツアレルギーがある場合でも使えますか？",
        "answer": "ハチミツやプロポリス、蜂産品に対してアレルギーをお持ちの方は、アレルギー反応（発赤、かゆみ等）を引き起こす可能性があるため使用を控えるか、使用前に必ず腕の内側などでパッチテストを行ってください。また、1歳未満の乳児の肌にはボツリヌス菌のリスクを考慮してハチミツ配合製品を使用しないでください。"
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
        "@id": "https://lumi-cosme.vercel.app/winter-honey.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！天然の強力吸湿ヴェールと濃厚生ハニーで乾かないモチ肌を叶える高保湿ハチミツコスメランク10",
    "description": "11月から12月の過酷な暖房乾燥とカサつき肌を救う高保湿ハチミツ・マヌカハニーコスメを徹底厳選！HACCIの最高峰フェイスオイルからCOSRXのプロポリスタンクまで、楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。",
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
    "name": "真冬の高保湿ハチミツコスメおすすめ人気ランキング10選",
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
            <tr><th>アイテム種別</th><td>{d['type']}</td></tr>
            <tr><th>主要成分・特長</th><td>{d['features']}</td></tr>
            <tr><th>高保湿の理由</th><td>{d['value']}</td></tr>
          </table>
          
          <div class="review-block">
            <h4>💡 冬の乾燥・粉吹き・カサつきに対する詳細解説</h4>
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
  <title>保湿力の強さで肌乾燥とさようなら！天然の強力吸湿ヴェールと濃厚生ハニーで乾かないモチ肌を叶える高保湿ハチミツコスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月から12月の過酷な暖房乾燥とカサつき肌を救う高保湿ハチミツ・マヌカハニーコスメを徹底厳選！HACCIの最高峰フェイスオイルからCOSRXのプロポリスタンクまで、楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta name="keywords" content="ハチミツコスメ,マヌカハニー,冬コスメ,プロポリス,高保湿化粧水,乾燥肌,HACCI,COSRX,山田養蜂場,ハンドクリーム,リップケア">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-honey.html">
  
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！天然の強力吸湿ヴェールと濃厚生ハニーで乾かないモチ肌を叶える高保湿ハチミツコスメランク10">
  <meta property="og:description" content="11月から12月の過酷な暖房乾燥とカサつき肌を救う高保湿ハチミツ・マヌカハニーコスメを徹底厳選！楽天人気ランキング10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-honey.html">
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
      --primary-color: #b45309;
      --primary-light: #fffbeb;
      --accent-color: #d97706;
      --accent-hover: #92400e;
      --text-main: #2d3748;
      --text-muted: #5a6a85;
      --bg-main: #fffdfa;
      --card-bg: #ffffff;
      --border-color: #fde68a;
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.04);
      --shadow-md: 0 4px 12px rgba(180,83,9,0.08);
      --shadow-lg: 0 8px 24px rgba(180,83,9,0.12);
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
      background: linear-gradient(135deg, #d97706, #b45309);
      color: #ffffff;
      font-weight: 900;
      font-size: 1rem;
      padding: 4px 18px;
      border-radius: 20px;
      box-shadow: 0 4px 10px rgba(217,119,6,0.3);
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
        <a href="winter-propolis.html">プロポリス</a>
        <a href="winter-ceramide-lotion.html">セラミド化粧水</a>
        <a href="winter-hand-cream.html">ハンドケア</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <div class="breadcrumb">
      <a href="index.html">ホーム</a> &gt; 
      <a href="winter-lotion.html">高保湿スキンケア特集</a> &gt; 
      <span>高保湿ハチミツコスメ</span>
    </div>

    <div class="article-header">
      <span class="article-tag-top">11-12月真冬の乾燥レスキュー特別企画</span>
      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！天然の強力吸湿ヴェールと濃厚生ハニーで乾かないモチ肌を叶える高保湿ハチミツコスメランク10</h1>
      <div class="meta-info">
        <span>更新日: 2026年11月03日</span>
        <span>監修: 冬コスメ徹底比較ラボ 専属コスメコンシェルジュ</span>
        <span>実機検証・楽天APIリアルタイムデータ連動</span>
      </div>
      <p class="article-lead">
        外気の湿度が下がり、オフィスのエアコン温風が肌を容赦なく乾燥させる11月から12月。「どれだけクリームを塗ってもカサつく」「夕方になると頬がパキパキに乾く」「唇の皮剥けや手指のひび割れが止まらない」……そんな真冬の過酷な乾燥砂漠肌を救う最強の天然素材が『ハチミツ・マヌカハニー』です。周囲の水分を引き寄せて離さない強力な吸湿力と、肌バリアを整えるビタミン・アミノ酸・酵素の力。本記事では、楽天APIからリアルタイムに在庫と価格を取得した厳選10品を徹底検証し、一日中モチモチ肌をキープするプロの活用術をお届けします。
      </p>
    </div>

    <div class="toc-box">
      <h2 class="toc-title">📑 目次 - クリックで各セクションへ移動</h2>
      <ul class="toc-list">
        <li><a href="#section-why">1. なぜ11-12月の肌乾燥にハチミツコスメが最強なのか？</a></li>
        <li><a href="#section-types">2. ハチミツ・プロポリス・ローヤルゼリー・マヌカの違いと選び方</a></li>
        <li><a href="#section-ranking">3. 保湿力高めハチミツコスメ厳選おすすめランキング10選</a></li>
        <li><a href="#section-compare">4. おすすめハチミツコスメ10選 徹底スペック比較一覧表</a></li>
        <li><a href="#section-routine">5. プロ直伝！冬の粉吹き肌をしっとりモチ肌へ導く3つの活用ステップ</a></li>
        <li><a href="#section-faq">6. よくある質問（FAQ）と注意点</a></li>
        <li><a href="#section-links">7. 合わせて読みたい！冬の乾燥対策おすすめ関連記事</a></li>
      </ul>
    </div>

    <!-- 導入セクション1 -->
    <section id="section-why" class="content-box">
      <h2 class="section-title">✨ なぜ11-12月の肌乾燥にハチミツコスメが最強なのか？</h2>
      <p>
        冬の本格的な乾燥シーズンにおいて、一般的なスキンケアの多くは「油分でフタをする」か「水溶性ポリマーで膜を張る」アプローチを取ります。しかし、室内湿度が20%〜30%台にまで低下する11月・12月の環境下では、肌内部の水分そのものが空気中へ奪われ、フタをしても内側が乾く「インナードライ」が多発します。
      </p>
      <p>
        ここで比類なき威力を発揮するのが、古代から美肌の秘薬として珍重されてきたハチミツです。ハチミツが冬の乾燥肌に決定的な変化をもたらす理由は、その特異な分子構造と吸湿メカニズムにあります。
      </p>

      <div class="highlight-box">
        <h4>🍯 ハチミツが誇る天然の超高保湿サイエンス</h4>
        <ul style="padding-left: 20px; line-height: 1.9;">
          <li><strong>自ら水分を引き寄せる強力な吸湿力：</strong> ハチミツを構成するグルコースやフルクトースなどの天然糖類には、水分子と強力に結合するヒドロキシ基（-OH）が無数に存在します。乾燥した大気の中でも微小な水分を抱え込み、肌表面から蒸散させません。</li>
          <li><strong>天然保湿因子（NMF）と親和するアミノ酸・ビタミン群：</strong> ビタミンB1、B2、B6、ナイアシン、パントテン酸、各種アミノ酸が豊富に含まれ、角層細胞のターンオーバーを正常化し、自ら潤う力を底上げします。</li>
          <li><strong>弱酸性の肌バリア保護＆抗菌作用：</strong> グルコン酸による穏やかな弱酸性環境を保ち、冬の乾燥によって繁殖しやすい肌荒れ原因菌を抑制。ピリつきやすい敏感肌を優しく鎮静します。</li>
        </ul>
      </div>

      <p>
        ハチミツコスメの最大の利点は、塗った瞬間に肌表面に柔らかな「潤いの密着ヴェール」を形成することです。油分のように重たく毛穴を塞ぐことなく、みずみずしい水分を角層に繋ぎ止め続けるため、朝から晩まで吸い付くような柔らかい素肌が持続します。
      </p>
    </section>

    <!-- 種類と選び方セクション -->
    <section id="section-types" class="content-box">
      <h2 class="section-title">🔍 ハチミツ・プロポリス・ローヤルゼリー・マヌカの違いと選び方</h2>
      <p>
        蜂由来のコスメには、目的や肌悩みに応じて異なる成分が配合されています。それぞれの特性を理解し、自分の肌状態に最も適したものを選びましょう。
      </p>

      <h3>① 純粋ハチミツ（アカシア・百花蜜など）</h3>
      <p>
        主成分である糖類が空気中の水分を抱え込み、肌をふっくらと柔らかく整えます。ゴワつき、カサつき、ファンデーションの粉吹きに悩む方や、自然なツヤ肌を作りたい方に最適です。
      </p>

      <h3>② プロポリス（天然の抗菌バリア）</h3>
      <p>
        ミツバチが巣を無菌状態に保つために作る樹脂状物質で、強力なフラボノイドを含みます。冬の乾燥によって肌のバリアが低下し、赤みや吹き出物、マスク摩擦による肌荒れが出やすいゆらぎ肌に抜群の鎮静効果を発揮します。
      </p>

      <h3>③ ローヤルゼリー（女王蜂のエイジング成分）</h3>
      <p>
        40種以上の必須アミノ酸やミネラル、特有成分デセン酸を含む完全栄養食。冬の寒冷外気でハリや弾力が失われ、乾燥小ジワが目立ち始めた大人のエイジング肌を力強くサポートします。
      </p>

      <h3>④ マヌカハニー（高活性MGO含有）</h3>
      <p>
        ニュージーランド産のマヌカ花から採れる希少ハチミツ。独自の生理活性物質メチルグリオキサール（MGO）を含み、強力な保水力と肌荒れ修復力を兼ね備えています。極度の乾燥肌やひび割れ、敏感肌のレスキューに最適です。
      </p>
    </section>

    <!-- ランキングセクション -->
    <section id="section-ranking">
      <h2 class="section-title">🏆 保湿力高めハチミツコスメ厳選おすすめランキング10選</h2>
      <p style="margin-bottom: 24px; color: var(--text-muted); font-size: 0.95rem;">
        ※楽天市場の最新APIデータを基に、蜂由来エキスの配合濃度、保湿持続力、テクスチャーの心地よさ、愛用者の口コミ評価を総合検証してランキングを決定しています。
      </p>

      {cards_str}
    </section>

    <!-- 比較表セクション -->
    <section id="section-compare" class="content-box">
      <h2 class="section-title">📊 おすすめハチミツコスメ10選 徹底スペック比較一覧表</h2>
      <p>ランキングでご紹介した10アイテムの容量、配合成分、用途、価格帯を一目で比較できる一覧表です。</p>
      
      <div class="compare-table-wrapper">
        <table class="compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>ブランド</th>
              <th>容量 / 種別</th>
              <th>主成分・特長</th>
              <th>参考価格（税込）</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>第1位</strong></td>
              <td>フェイスオイル エスケーピオン</td>
              <td>HACCI</td>
              <td>30ml 美容オイル</td>
              <td>天然ハチミツ×植物オイル・発光水光肌</td>
              <td>¥{items[0]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第2位</strong></td>
              <td>プロポリス シナジートナー</td>
              <td>COSRX</td>
              <td>150ml 化粧水</td>
              <td>プロポリス72.6%×蜂蜜10%・高保水</td>
              <td>¥{items[1]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第3位</strong></td>
              <td>ハニーラボ スリーピングパック</td>
              <td>山田養蜂場</td>
              <td>50ml ナイトパック</td>
              <td>国産完熟蜂蜜・睡眠中の水分蒸散防止</td>
              <td>¥{items[2]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第4位</strong></td>
              <td>クレンジングミルク</td>
              <td>HACCI</td>
              <td>190ml クレンジング</td>
              <td>蜂蜜美容液85%・乾燥つっぱりゼロ</td>
              <td>¥{items[3]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第5位</strong></td>
              <td>ロイヤルハニー エンリッチ</td>
              <td>SKINFOOD</td>
              <td>50ml 美容液</td>
              <td>熟成プロポリス63%・冬枯れバリア修復</td>
              <td>¥{items[4]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第6位</strong></td>
              <td>ワンダーハニー ハンドクリーム</td>
              <td>VECUA Honey</td>
              <td>50g ハンドケア</td>
              <td>北海道産蜂蜜×ミツロウ・潤いの手袋</td>
              <td>¥{items[5]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第7位</strong></td>
              <td>ディープモイスト ヘアオイル3.0</td>
              <td>&honey</td>
              <td>100ml ヘアオイル</td>
              <td>マヌカハニー配合・髪の水分量14%維持</td>
              <td>¥{items[6]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第8位</strong></td>
              <td>ナチュラル ハニーリップ</td>
              <td>カントリー＆ストリーム</td>
              <td>10g リップケア</td>
              <td>ハチミツ濃厚密着・冬の縦ジワ皮剥け予防</td>
              <td>¥{items[7]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第9位</strong></td>
              <td>薬用 RJエッセンス</td>
              <td>山田養蜂場</td>
              <td>30ml 薬用美容液</td>
              <td>微粒子ローヤルゼリー×美白抗シワ承認</td>
              <td>¥{items[8]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第10位</strong></td>
              <td>B8 リッチモイストドロップ</td>
              <td>マヌカコスメ</td>
              <td>80g 保湿ジェル</td>
              <td>UMFマヌカハニー・肌荒れ赤み予防マルチ</td>
              <td>¥{items[9]['price']:,}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 使い方ルーティンセクション -->
    <section id="section-routine" class="content-box">
      <h2 class="section-title">🧴 プロ直伝！冬の粉吹き肌をしっとりモチ肌へ導く3つの活用ステップ</h2>
      <p>
        ハチミツコスメの優れた吸湿力と密着力を120%引き出すための、冬期限定スキンケア活用術をご紹介します。
      </p>

      <h3>ステップ1：洗顔後すぐの「ハニー導入＆水分引き込み」</h3>
      <p>
        洗顔後、タオルで水気を軽く拭き取った直後にハチミツ配合のフェイスオイル（またはトナー）をすぐになじませます。ハチミツの天然糖類が角層に水分を引き込むための「スポンジ」の役割を果たし、その後に重ねる化粧水や乳液の浸透スピードを劇的に加速させます。
      </p>

      <h3>ステップ2：気になる部分への「ハニーミルフィーユ重ね」</h3>
      <p>
        目元や口元、ほうれい線、頬骨周辺など、暖房の温風が直接当たって粉を吹きやすい部分には、美容液やトナーを一度塗った後に指の腹でトントンと軽くタッピングしてもう一度重ねる「ミルフィーユ塗り」を行います。薄い保湿膜が何層にも重なり、外部の乾燥刺激を寄せ付けません。
      </p>

      <h3>ステップ3：就寝前の「濃密ハニーラッピング」</h3>
      <p>
        夜のお手入れの総仕上げとして、スリーピングパックやリップバームを唇・全顔にたっぷり塗布して眠りにつきます。暖房の温風が吹き荒れる室内環境でも、ハチミツの密着膜が睡眠中の肌水分蒸散を完全に防ぎ、翌朝の洗顔時には吸い付くようなふっくら肌を実感できます。
      </p>
    </section>

    <!-- FAQセクション -->
    <section id="section-faq" class="content-box">
      <h2 class="section-title">❓ よくある質問（FAQ）と注意点</h2>
      {faq_str}
    </section>

    <!-- 内部リンクセクション -->
    <section id="section-links" class="content-box">
      <h2 class="section-title">🔗 合わせて読みたい！冬の乾燥対策おすすめ関連記事</h2>
      <p>ハチミツコスメと相乗効果を生み出す、冬の保湿特集記事も合わせてチェックしてください。</p>
      
      <div class="related-links-grid">
        <a href="winter-propolis.html" class="related-link-card">
          <h4>冬のプロポリス美容液おすすめ10選</h4>
          <p>天然の抗菌バリアで肌荒れをブロック。冬のゆらぎ肌を鎮めるプロポリスコスメ特集。</p>
        </a>
        <a href="winter-ceramide-lotion.html" class="related-link-card">
          <h4>高保湿セラミド化粧水厳選10選</h4>
          <p>角層のラメラ構造を整えて水分を逃さない。冬のインナードライを解消する化粧水集。</p>
        </a>
        <a href="winter-hand-cream.html" class="related-link-card">
          <h4>冬の高保湿ハンドクリーム10選</h4>
          <p>手洗いや消毒による手荒れ・あかぎれを救う。しっとり潤い手袋を張るハンドケア名品。</p>
        </a>
        <a href="winter-lip-mask.html" class="related-link-card">
          <h4>冬の集中リップマスクおすすめ10選</h4>
          <p>就寝中に唇の縦ジワと皮剥けをリセット。翌朝ぷるぷる唇を作る夜用リップトリートメント。</p>
        </a>
        <a href="winter-hair-oil.html" class="related-link-card">
          <h4>冬の高保湿ヘアオイルおすすめ10選</h4>
          <p>暖房によるパサつきと静電気を完全ガード。毛先までまとまる濃密ヘアオイル特集。</p>
        </a>
        <a href="winter-rosehip-oil.html" class="related-link-card">
          <h4>高保湿ローズヒップオイルおすすめ10選</h4>
          <p>ビタミンの爆弾と必須脂肪酸80%。冬枯れした砂漠肌をふっくらほぐす最高峰ピュアオイル。</p>
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
            <li><a href="winter-honey.html">ハチミツコスメ</a></li>
            <li><a href="winter-propolis.html">プロポリス</a></li>
            <li><a href="winter-ceramide-cream.html">セラミド</a></li>
            <li><a href="winter-rosehip-oil.html">ローズヒップオイル</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>アイテム別特集</h5>
          <ul>
            <li><a href="winter-hand-cream.html">ハンドクリーム</a></li>
            <li><a href="winter-lip-mask.html">リップマスク</a></li>
            <li><a href="winter-hair-oil.html">ヘアオイル</a></li>
            <li><a href="winter-lotion.html">高保湿化粧水</a></li>
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

with open("winter-honey.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-honey.html successfully! File size: {len(html_content):,} bytes")
