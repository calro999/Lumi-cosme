import json
import re

with open("fetched_final_30_manuka_prickly_calendula.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_manuka_honey"]["items"]

# 各商品ごとの完全オリジナルなレビュー＆詳細データ
product_details = [
    {
        "rank": 1,
        "tag": "🍯 生マヌカ蜜×生ローヤルゼリー！真冬の毛穴汚れを溶かし極上蜜膜で満たす最高峰バーム",
        "catch": "蜂蜜の老舗・山田養蜂場が本気で作った濃密生マヌカハニークレンジング。冬の冷え固まった角栓とメイクを体温でとろりとほぐし、洗い流した瞬間から吸い付くような満水肌へ",
        "brand_name": "山田養蜂場 (YAMADA BEE FARM)",
        "capacity": "75g / 専用スパチュラ付きジャー",
        "type": "高保湿生マヌカハニークレンジングバーム",
        "features": "ニュージーランド産生マヌカ蜂蜜、生ローヤルゼリーエキス、オリーブ果実油、ホホバ種子油、天然セラミド",
        "value": "山田養蜂場独自の非加熱生マヌカハニーと生ローヤルゼリーを贅沢にブレンド。クレンジングでありながらまるで美容液パックをした後のような濃厚な保湿ヴェールが肌に残る",
        "desc_p1": "11月から12月にかけて気温が急降下すると、肌の皮脂が固まって毛穴の黒ずみや角栓が目立ちやすくなる一方で、通常のクレンジングを使うと必要な油分まで奪われてツッパリや粉吹きを引き起こすというジレンマに陥ります。この冬の難問を鮮やかに解決してくれるのが、山田養蜂場の『マヌカハニー クレンジングバーム』です。フタを開けると、天然ハチミツのほんのり甘く奥深い香りが広がり、スパチュラですくった瞬間はしっかりした固形なのに、肌に乗せた瞬間に手のひらの温もりでトロ〜リと濃密な黄金オイルへと変化します。",
        "desc_p2": "生マヌカハニー特有の強い抗菌・整肌パワーと微細な浸透圧が、寒さで硬直した毛穴の奥深くに詰まった酸化皮脂をやさしく浮き上がらせます。一般的なバームクレンジングにありがちな『乳化不足でヌルつきが残る』『脱脂力が強すぎて洗い上がりが乾燥する』といった不満が一切なく、ぬるま湯ですすぐと汚れだけがスッと落ち、肌表面には上質なハニーヴェールがピンと張られたような、もっちり柔らかい弾力肌が出現します。ダブル洗顔不要で肌への摩擦を最小限に抑えられるのも、乾燥で皮膚が薄くなっている冬には極めて心強い設計です。",
        "target": "冬になるとクレンジング後のツッパリ感や皮むけに悩む方、毛穴の角栓詰まりと乾燥を同時にケアしたい方、本物の生蜂蜜の濃密なテクスチャーと香りで贅沢なスキンケアタイムを過ごしたい方",
        "point": "必ず手肌が乾いた状態で、サクランボ粒大を手に取り、手のひらで軽く温めてから顔全体に広げます。小鼻や眉間などザラつきが気になる部分は指の腹で円を描くように優しくマッサージし、少量のぬるま湯を加えて白く乳化させてから洗い流してください。"
    },
    {
        "rank": 2,
        "tag": "✨ 1本で濃密ハニーバリア！真冬の乾いた角層を潤すオールインワンエッセンス",
        "catch": "生マヌカ蜂蜜と生ローヤルゼリーを贅沢に配合した薬用級スキンケアエッセンス。冬の寒冷でこわばった肌深部へ素早く染み渡り、1ステップでふっくら押し返すハリ感を叶える",
        "brand_name": "山田養蜂場 (YAMADA BEE FARM)",
        "capacity": "80g / ディスペンサーボトル",
        "type": "高保湿マヌカハニーオールインワンエッセンスジェル",
        "features": "生マヌカハニー、生ローヤルゼリー、浸透型ヒアルロン酸、アミノ酸コンプレックス、ユズセラミド",
        "value": "化粧水・美容液・乳液・クリーム・パックの機能を兼ね備え、忙しい冬の朝晩でも瞬時にハニープロテクト膜を構築。肌のインナードライを根本から解消",
        "desc_p1": "乾燥がピークに達する11月・12月、スキンケアのステップを重ねる摩擦すら肌の刺激になってしまう敏感期におすすめなのが、山田養蜂場の『マヌカハニー エッセンスジェル』です。ニュージーランドの大自然で育まれた希少な生マヌカハニーに、必須アミノ酸やビタミンを豊富に含む生ローヤルゼリーを掛け合わせ、真冬の過酷な乾燥環境下でも角層の水分を絶対に逃さない設計になっています。",
        "desc_p2": "ジェルでありながら、肌に伸ばすと美容液とオイルが溶け合ったようなリッチなコクへと変化し、角層のすみずみまでスルスルと浸透。塗った直後から肌表面がツヤやかな保護膜で覆われ、暖房が効きっぱなしのオフィスでも夕方まで乾く気配がありません。ユズセラミドが乱れたキメを整え、乾燥によってくすんで見えがちな真冬の顔色をパッと明るい印象へと導いてくれます。",
        "target": "冬の朝晩のスキンケアを手早く済ませたいけれど保湿力には妥協したくない方、エアコン乾燥で夕方になると頬が痛くなる方、肌のキメとしぼみを同時に立て直したい方",
        "point": "洗顔後、2〜3プッシュを手にとり、顔の内側から外側へ優しく引き上げるように伸ばします。乾燥が目立つ目元や口元には、半プッシュ分を指先でトントンと重ねづけし、仕上げに両手で顔全体を10秒間包み込んで温めると浸透が劇的にアップします。"
    },
    {
        "rank": 3,
        "tag": "🛡️ MGO250+の医療グレード保水力！真冬の唇ひび割れ・皮むけを速攻レスキュー",
        "catch": "本場ニュージーランドのトップブランド『マヌカヘルス』が誇る超高純度リップバーム。寒風で荒れ果てた唇にピタッと密着し、濃密な抗菌・保湿蜜膜でガサガサ唇をつるんとリセット",
        "brand_name": "Manuka Health (マヌカヘルス)",
        "capacity": "4.5g / スティックタイプ",
        "type": "高機能メディカルマヌカハニーリップバーム",
        "features": "MGO250+マヌカハニー、天然ミツロウ、スイートアーモンド油、ホホバ種子油、ビタミンE",
        "value": "確かな抗菌力と抗炎症力を持つ天然MGO含有。医薬品レベルの保護力で、冬の木枯らしやマスク摩擦による唇の皮むけ・亀裂を根本ケア",
        "desc_p1": "11月に入ると真っ先に乾燥のダメージを受けるのが、皮脂腺がなく角層が極めて薄い『唇』です。リップクリームを何度塗り直しても皮がむける、笑うとピキッと唇の端が切れて痛いという深刻な悩みを抱える方から熱狂的な信頼を寄せられているのが、世界的なマヌカハニーブランド・マヌカヘルス社の『MGO250+ リップバーム』です。",
        "desc_p2": "最大の特徴は、一般的なハチミツ香料のリップとは一線を画す『高濃度MGO（メチルグリオキサール）250+』の配合です。天然ミツロウとアーモンドオイルがベースになっているため、体温でじわっととろけて唇の縦ジワの隙間まで隙間なく密着。荒れてヒリつく唇を穏やかに落ち着かせ、厚みのある保護膜が冷たい外気と水分蒸発を物理的にシャットアウトします。無香料・無着色で食事の前でも気兼ねなく使え、就寝前にたっぷり塗っておけば翌朝ぷるんとした赤ちゃんのような柔らかい唇が蘇ります。",
        "target": "真冬になると毎年唇のひび割れや皮むけに悩まされる方、一般的なリップクリームでは保湿持続力が足りないと感じる方、天然成分100%に近い安心処方を求める方",
        "point": "唇の輪郭からはみ出るくらい広めに、縦ジワに沿って上下に往復させながら優しく塗り込みます。夜寝る前は、唇をラップで3分間覆う『マヌカハニー温感リップパック』を行うと、頑固なガサガサ角質が一晩でふっくら滑らかになります。"
    },
    {
        "rank": 4,
        "tag": "🌿 2層式ブースターの黄金比！寒さで硬化した角層をほぐし潤いを呼び込む導入オイル",
        "catch": "無農薬ハーブエキス×高純度マヌカハニー×スクワランの美肌2層仕立て。冬の冷えでゴワついた肌を瞬時にやわらげ、後から使う化粧水の浸透力を爆発的に高める名作ブースター",
        "brand_name": "chant a charm (チャントアチャーム)",
        "capacity": "60ml / 2層式ボトル",
        "type": "高保水導入ハニー美容オイル",
        "features": "マヌカハニー、自社農場無農薬ハーブエキス（ゼニアオイ等）、植物性スクワラン、マカデミア種子油",
        "value": "オイル層とエッセンス層をシェイクして使う独自処方。オイルの柔軟効果とハチミツエッセンスの保水効果を同時に肌へ届け、ベタつきゼロのシルク肌へ",
        "desc_p1": "真冬に化粧水をいくら重ねても肌表面を滑るだけで入っていかないと感じる原因は、寒冷によって角層が冷え固まり、水分を吸着できなくなっているからです。チャントアチャームの『モイスト ブースターオイル』は、洗顔後すぐのまっさらな肌に使用する2層式の導入美容オイルで、植物の生命力とマヌカハニーの保水力を肌に送り届けます。",
        "desc_p2": "使う直前にボトルをよく振ると、黄金色のオイルと透明なエッセンスが混ざり合ってクリーミーなエマルジョン状に変化します。手のひらで馴染ませると、オイル特有の重さや油膜感が全くなく、スーッと角層へ吸い込まれるように浸透。マヌカハニーが肌内部の水分を引き寄せ、スクワランが硬くなった角質細胞の隙間をふんわり解きほぐします。これを使うとその後に重ねる化粧水がスポンジのようにグングン吸い込まれ、もっちり吸い付くような肌土台が完成します。",
        "target": "冬になると肌がゴワついて化粧水が弾かれてしまう方、オイル美容を試したいけれどベタつきが苦手な方、肌のキメと透明感を根本から底上げしたい方",
        "point": "洗顔直後、容器を上下にしっかり振って2層を均一に混ぜ合わせ、2〜3滴を手にとります。顔全体を手のひらで包み込むように優しくハンドプレスしたあと、すぐに通常の化粧水をたっぷり重ねてください。"
    },
    {
        "rank": 5,
        "tag": "🍯 濃密シアバター×高純度ハニー！冬の粉吹き・目元口元を狙い撃つ集中バーム",
        "catch": "高濃度マヌカハニーとリッチなシアバターを黄金比率でブレンド。指先の体温でじゅわっと溶け出し、真冬の極度な乾燥で粉を吹いた頬や目元に鉄壁の潤いシールドを形成",
        "brand_name": "マヌカコスメ (Manuka Cosme) / キハナクリーミーセラム",
        "capacity": "30g / ジャータイプ",
        "type": "高密着リペアバームクリーム",
        "features": "高純度マヌカハニー、天然シアバター、オリーブ果実油、ホホバ種子油、ビタミンE",
        "value": "水分蒸発を防ぐ天然ワックス構造と蜂蜜の吸湿力で、真冬の暖房直風にも負けない持続型エモリエントバリアを形成。持ち歩きにも便利なレスキューバーム",
        "desc_p1": "真冬の夕方、ふと鏡を見ると目尻の小ジワが乾燥でくっきり刻まれ、口角のまわりが白く粉を吹いてファンデーションが割れている…そんな緊急事態を即座に修復してくれるのが、高濃度マヌカハニーを配合したリッチな『モイストリペアバーム』です。",
        "desc_p2": "硬めのバームに見えますが、指先にとってくるくるとなじませると、人肌の温度でとろけてなめらかな濃密オイルバームへとトランスフォームします。マヌカハニーが肌の角質層に水分を留め、シアバターが強固な油分皮膜を形成するため、塗った瞬間から乾燥によるチリチリした痒みやつっぱり感がスーッと鎮静。メイクの上からでもトントンと薄く叩き込むだけで、粉吹きが一瞬で消え去り、上品な水光ツヤが蘇ります。",
        "target": "目元・口元の部分的な激しい乾燥や粉吹きに悩んでいる方、日中のメイク直し用のお守りコスメを探している方、冬の寒冷で肌がピリつきやすい方",
        "point": "朝晩のスキンケアの最後に、米粒大を指先で温めてから乾燥が気になる部分に優しくプレスします。日中のメイク直し時は、ティッシュで余分な皮脂を軽く押さえた後、本品を極少量トントンと馴染ませてからパウダーを重ねるとツヤ肌が復活します。"
    },
    {
        "rank": 6,
        "tag": "🐝 ぷるぷる蜜の滴！ハチミツ×ローヤルゼリーが叶えるプチプラ最強ハニーリップ",
        "catch": "チューブから出した瞬間、まるで絞りたてのハチミツを塗っているかのような濃厚密着感。冬の荒れがちな唇をぽってりボリューム感あるツヤ膜で包み込む名品ハニーリップ",
        "brand_name": "Country & Stream (カントリー&ストリーム)",
        "capacity": "10g / 斜めカットチューブ",
        "type": "高密着ハニーリップ美容液",
        "features": "天然ハチミツ、ローヤルゼリーエキス、オリーブ果実油、シア脂、カミツレ花エキス",
        "value": "ドラッグストアやバラエティショップで不動の人気を誇る高コスパコスメ。斜めカットチューブで塗りやすく、日中のグロス代わりや夜のリップパックに最適",
        "desc_p1": "プチプラコスメ界において『冬の唇荒れ対策ならこれ一択』とSNSでも絶大な支持を集め続けているカントリー＆ストリームの『ナチュラルハニー リップ』。チューブから押し出すと、透明感のある黄金色の濃厚ジェルがぷるんと顔を出し、唇に乗せるとほんのり甘いハチミツの香りが心地よく広がります。",
        "desc_p2": "斜めカットのチューブヘッドが唇のカーブに吸い付くようにフィットし、指を汚さずにムラなく均一に塗布できます。ハチミツとローヤルゼリーが荒れた唇の角層細胞を潤いで満たし、植物性オイルが分厚いガラスのようなツヤ膜を形成。冬の冷たい外気にさらされても水分が蒸発せず、縦ジワの目立たないふっくらとした唇が長時間続きます。口紅の下地として使えば色持ちが格段に良くなり、上から重ねればナチュラルなハニーグロスとしても大活躍します。",
        "target": "惜しみなく毎日何度も塗り直せる高コスパリッチリップを探している方、唇の縦ジワを消してふっくら見せたい方、甘く優しいハチミツの香りが好きな方",
        "point": "唇の中央にたっぷりと乗せ、左右に塗り広げたあと上下の唇をすり合わせて馴染ませます。夜は唇からはみ出すくらいたっぷり塗って就寝すると、翌朝の洗顔時に余分な古い角質がポロポロと優しくオフできます。"
    },
    {
        "rank": 7,
        "tag": "💧 濃密ハニーカプセルが弾ける！冬の肌荒れを防ぎ満水肌をキープする高保水ゲル",
        "catch": "マヌカハニーと浸透型コラーゲン、植物幹細胞エキスを凝縮。洗顔後の素肌に濃密なハニーヴェールを張り巡らせ、エアコン暖房の砂漠環境でも吸い付くような潤いを持続",
        "brand_name": "山田養蜂場 / マヌカコスメ",
        "capacity": "80g〜100g / ジャータイプ",
        "type": "高保湿マヌカハニーモイストジェル",
        "features": "マヌカハニーエキス、加水分解コラーゲン、ヒアルロン酸Na、セラミド3種、アルガンオイル",
        "value": "水分と油分のバランスを精密に設計した高機能モイスト処方。冬の乾燥でしぼんだキメをふっくら持ち上げ、一日中みずみずしいハリをキープ",
        "desc_p1": "冬の朝は寒くてスキンケアに時間をかけられないけれど、手抜きをすると日中の暖房で顔がパリパリに乾いてしまう…そんな現代人のライフスタイルに寄り添うのが、マヌカハニーを高配合した『モイストオールインワンジェル』です。みずみずしい透明感のあるジェルの中に、蜂蜜の濃厚な栄養成分が凝縮されています。",
        "desc_p2": "肌に乗せると体温でスーッと液状にほぐれ、角質層の深部へと一気に浸透。表面にベタベタした不快感を残さず、内側はたっぷりの水分で満たされ、外側はハニーシールドで守られているような絶妙な仕上がりを実現します。コラーゲンとセラミドが肌の土台を強化するため、冬の寒冷で開きがちな乾燥毛穴もキュッと引き締まり、メイクのノリが格段に向上します。",
        "target": "朝のスキンケアを1分で終わらせつつ冬の乾燥崩れを防ぎたい方、重すぎるクリームは苦手だけど化粧水だけでは物足りない方、肌にハリと弾力を取り戻したい方",
        "point": "洗顔後、付属のスパチュラでサクランボ大を手に取り、額・両頬・鼻・あごの5点に置いてから優しく全体に伸ばします。首筋やデコルテまで伸ばしてハンドプレスすると、冬のタートルネックやマフラーの摩擦による首の乾燥荒れも予防できます。"
    },
    {
        "rank": 8,
        "tag": "🌍 シアバター×天然ハチミツ！生活の木が贈るオーガニック濃厚リップバリア",
        "catch": "西アフリカ産精製シアバターと天然蜂蜜の濃密ブレンド。真冬の乾燥冷気からデリケートな唇を物理的かつエモリエントに守り抜く高保湿リップ",
        "brand_name": "生活の木 (Tree of life)",
        "capacity": "9g / アルミ缶・チューブ",
        "type": "高純度ボタニカルハニーリップバーム",
        "features": "天然シア脂、ハチミツ、ミツロウ、トコフェロール（天然ビタミンE）",
        "value": "ハーブとアロマのパイオニア『生活の木』が厳選した高純度原料。合成防腐剤・鉱物油・合成香料不使用で、唇本来のバリア機能を底上げ",
        "desc_p1": "アロマとハーブの老舗・生活の木が手がける『シアバター＆ハニー リップバーム』は、シンプルながら原料の品質の高さで多くのリピーターを惹きつける冬のロングセラーアイテムです。過酷なサバンナで水分を蓄えるシアの木の実から採れる濃厚なシアバターに、豊かな滋養を持つ天然ハチミツを贅沢にブレンドしています。",
        "desc_p2": "指先やスパチュラで触れるとコクのある固めのテクスチャーですが、唇に乗せた瞬間にじんわりと溶け出し、しっとりと吸い付くように馴染みます。シアバターが水分の蒸発を力強くブロックし、ハチミツが角層内部に潤いを引き留めるため、木枯らしが吹き荒れる真冬のアウトドアや自転車移動でも唇が乾きません。無添加処方で低刺激なため、唇が荒れて敏感になっている時でも安心して使用できます。",
        "target": "合成成分や香料を避けたいナチュラル志向の方、シンプルで飽きのこない高品質な保湿バームを求める方、唇だけでなく指先のささくれケアも兼ねたい方",
        "point": "少量を指先にとり、唇全体に優しく馴染ませます。余ったバームは爪の甘皮や指先にすり込むことで、冬のガサガサしたささくれや乾燥ひび割れも同時に防ぐことができます。"
    },
    {
        "rank": 9,
        "tag": "🌿 巣を守る天然プロポリス×生ハチミツ！荒れ狂う唇を優しく鎮静する薬草バーム",
        "catch": "ミツバチが創り出す天然の抗菌シールド『プロポリス』と生蜂蜜を配合。冬の寒冷刺激でピリピリと荒れてしまった敏感な唇を穏やかに整える名作リップ",
        "brand_name": "PRO HERB (プロハーブ)",
        "capacity": "4g / スティックタイプ",
        "type": "低刺激・高保湿プロポリスハニーリップ",
        "features": "プロポリスエキス、天然ハチミツ、ホホバ種子油、コメ胚芽油、アラントイン",
        "value": "無香料・無着色・天然由来成分主体。プロポリスの抗菌・保護作用とハチミツの保水力が融合し、冬の過酷な環境からデリケートな粘膜を守り抜く",
        "desc_p1": "ミツバチが巣を雑菌やウイルスから守るために樹液から創り出す『プロポリス』。このプロポリスの強力な自己防衛パワーに着目して作られたのが、プロハーブの『リップクリーム』です。真冬の寒さや乾燥、風邪気味で荒れてしまった唇をやさしくケアする救急箱のような存在として長年愛されています。",
        "desc_p2": "唇に触れるとなめらかに滑り、薄膜ながらもしっかりとした保護皮膜を形成。ハチミツが潤いを与え、プロポリスとアラントインが荒れて炎症を起こしそうな唇を優しく鎮静させます。ギトギトしたテカリやベタつきが出ないため、男性やリップメイクのベースとしても最適。冬の外出前にサッと塗るだけで、冷たい風に負けない健やかな唇を一日中キープできます。",
        "target": "唇が敏感で一般的なリップクリームが合わない方、プロポリスの天然の保護力を実感したい方、テカリやベタつきのない自然な仕上がりを好む方",
        "point": "乾燥を感じた時にいつでも唇に直接塗布します。口紅を塗る直前に薄く仕込んでおくと、色素沈着や乾燥による縦ジワ割れを綺麗に防ぐことができます。"
    },
    {
        "rank": 10,
        "tag": "🍯 ひたひたの蜜液で満水チャージ！朝晩の砂漠肌を救済する集中ハニーシートマスク",
        "catch": "高純度マヌカハニーエキスとローヤルゼリーを贅沢に染み込ませた大容量30枚入りBOX。真冬のエアコン暖房で干からびた肌細胞をリッチなハニーエッセンスで満たす集中ケア",
        "brand_name": "K-Secret / コスメプロ (CosmePro)",
        "capacity": "30枚入り (大容量エッセンス) / BOXタイプ",
        "type": "高保水デイリーマヌカハニーシートマスク",
        "features": "マヌカハニーエキス、加水分解ローヤルゼリータンパク、プロポリスエキス、3重ヒアルロン酸",
        "value": "30枚入りで毎日惜しみなく使える贅沢仕様。極細密着シートが顔の凹凸にぴったりフィットし、角層のすみずみまで蜂蜜の栄養を送り届ける",
        "desc_p1": "冬の乾燥を本気で防ぐなら、毎日のデイリーシートマスクが最も即効性のあるアプローチです。『ピュア マヌカハニー モイスチャーデイリーマスク』は、過酷な冬の砂漠肌のために設計された高保湿大容量シートマスクです。フタを開けると美容液がひたひたに浸かっており、贅沢な潤い感が視覚的にも伝わってきます。",
        "desc_p2": "植物由来のマイクロファイバーシートが肌に吸い付くように密着し、浮きやすい小鼻や口元のキワまでしっかりとカバー。マヌカハニーとローヤルゼリーの濃密なエキスが、寒さで縮こまった角層細胞をじっくりと潤します。約10分後はがすと、肌のトーンがパッと明るくなり、手のひらが吸い付くようなモチモチの満水肌へ。朝のメイク前に使えば、一日中ファンデーションが粉を吹かない完璧なツヤ肌土台が完成します。",
        "target": "毎日手軽に高保湿シートマスクで集中ケアしたい方、真冬のファンデーションの乾燥崩れや粉吹きに悩んでいる方、大容量でコスパ良く蜂蜜スキンケアを取り入れたい方",
        "point": "洗顔後、化粧水で肌を整えた後にシートを密着させます。10分ほど置いたらはがし、肌表面に残ったエッセンスを優しくハンドプレスで押し込みます。最後に必ず乳液やクリームで油分のフタをしてください。"
    }
]

# FAQ 生成
faqs = [
    {
        "q": "マヌカハニーコスメと、一般的なハチミツコスメの違いは何ですか？",
        "a": "最大の違いは、ニュージーランドに自生するマヌカの木の花からのみ採取される特有の抗菌・整肌成分『MGO（メチルグリオキサール）』の有無です。一般的なハチミツも高い保水力を持ちますが、マヌカハニーはさらに強力な抗炎症・皮膚修復サポート力を備えています。そのため、11月・12月の厳しい寒風や乾燥によって微小な炎症やひび割れを起こした『冬のトラブル肌』に対して、格段に高い鎮静・リペア効果を発揮します。"
    },
    {
        "q": "マヌカハニーや蜂蜜コスメは、肌がベタついたりニキビの原因になりませんか？",
        "a": "良質なマヌカハニーコスメは、糖類の強い親水性（水分を引き寄せて離さない力）を活かして設計されているため、肌に馴染ませると水分とともに角層深部へすっと浸透し、表面に油っぽい不快なベタつきを残しません。また、マヌカハニー自体が持つ天然の抗菌作用により、乾燥が原因で皮脂バランスが崩れる『冬の大人ニキビ』に対しても非常に衛生的に肌環境を整えてくれます。"
    },
    {
        "q": "11月〜12月のスキンケアで、マヌカハニーコスメを最も効果的に取り入れる順番は？",
        "a": "アイテムの形状によって異なりますが、クレンジングや洗顔で角質を柔軟にした後、導入オイル（チャントアチャーム）で肌をほぐし、化粧水やシートマスクでたっぷりと水分を浸透させ、最後にマヌカハニー配合のクリームやバーム（山田養蜂場やマヌカコスメ）で蓋をするのが理想的です。特に乾燥が気になる夜は、リップバームを唇に厚めに塗って就寝するだけで、翌朝の乾燥トラブルを劇的に防ぐことができます。"
    },
    {
        "q": "敏感肌やアトピー肌でもマヌカハニーコスメは使えますか？",
        "a": "天然由来成分が主体で低刺激設計のものが多く、皮膚の保護膜を強化してくれるため、乾燥性敏感肌の方に非常に適しています。ただし、稀にハチミツや蜂産品（プロポリス・ローヤルゼリーなど）に対してアレルギーをお持ちの方がいらっしゃいますので、重度のアレルギー体質の方や不安な方は、二の腕の内側などでパッチテストを行ってからのご使用をおすすめします。"
    }
]

# HTML テーブル行生成
table_rows = []
for it in items:
    r = it["rank"]
    p_info = next((p for p in product_details if p["rank"] == r), None)
    type_name = p_info["type"] if p_info else "高保湿コスメ"
    brand = it["brand"]
    name = it["display_name"].split(" (")[0]
    price = f"¥{it['price']:,}"
    img = it["image"]
    url = it["url"]
    
    row = f"""
    <tr>
      <td class="rank-num rank-{r}">{r}位</td>
      <td class="product-thumb"><a href="{url}" target="_blank" rel="nofollow noopener"><img src="{img}" alt="{name}" loading="lazy" width="80" height="80"></a></td>
      <td class="product-name-cell">
        <span class="product-brand">{brand}</span>
        <a href="{url}" target="_blank" rel="nofollow noopener" class="table-prod-link">{name}</a>
      </td>
      <td><span class="type-badge">{type_name}</span></td>
      <td class="product-price">{price}</td>
      <td><a href="{url}" target="_blank" rel="nofollow noopener" class="table-btn">楽天で見る</a></td>
    </tr>
    """
    table_rows.append(row)

table_joined = "\n".join(table_rows)

# 商品カード生成
cards = []
for it in items:
    r = it["rank"]
    p = next((x for x in product_details if x["rank"] == r), product_details[0])
    price = f"¥{it['price']:,}"
    img = it["image"]
    url = it["url"]
    shop = it["shop_name"]
    rate = it["review_rate"]
    reviews = it["review_count"]
    
    card = f"""
    <article class="product-card" id="rank-{r}">
      <div class="card-header">
        <div class="rank-badge rank-{r}">第{r}位</div>
        <div class="card-titles">
          <span class="card-tag">{p['tag']}</span>
          <h3 class="card-name">{it['display_name']}</h3>
        </div>
      </div>
      
      <p class="card-catch"><strong>【注目ポイント】</strong> {p['catch']}</p>
      
      <div class="card-body">
        <div class="card-image-box">
          <a href="{url}" target="_blank" rel="nofollow noopener">
            <img src="{img}" alt="{it['display_name']}" loading="lazy" width="300" height="300" class="product-img">
          </a>
          <div class="card-price-box">
            <span class="price-label">楽天市場参考価格</span>
            <span class="price-val">{price}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <div class="card-review-box">
            <span class="star-rating">★ {rate}</span>
            <span class="review-count">({reviews}件のレビュー)</span>
          </div>
          <a href="{url}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で最新価格をチェック ➔
          </a>
        </div>
        
        <div class="card-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{p['brand_name']}</td></tr>
            <tr><th>容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>注目保湿成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の保湿価値</th><td>{p['value']}</td></tr>
          </table>
          
          <div class="review-text-box">
            <h4>💡 美容皮膚・テクスチャー詳細レビュー</h4>
            <p>{p['desc_p1']}</p>
            <p>{p['desc_p2']}</p>
          </div>
          
          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ：</strong> {p['target']}
          </div>
          
          <div class="point-box">
            <strong>✨ 11-12月の効果的な使い方テクニック：</strong> {p['point']}
          </div>
        </div>
      </div>
    </article>
    """
    cards.append(card)

cards_joined = "\n".join(cards)

# FAQ HTML 生成
faq_items = []
for f in faqs:
    faq_html = f"""
    <div class="faq-item">
      <h3 class="faq-q"><span class="faq-q-badge">Q</span> {f['q']}</h3>
      <div class="faq-a"><span class="faq-a-badge">A</span> <p>{f['a']}</p></div>
    </div>
    """
    faq_items.append(faq_html)

faqs_joined = "\n".join(faq_items)

# 全体HTMLテンプレート

schema_items = []
for idx, it in enumerate(items, 1):
    schema_items.append({
        "@type": "ListItem",
        "position": idx,
        "name": it["display_name"],
        "url": f"https://lumi-cosme.vercel.app/winter-manuka-honey#rank-{it['rank']}",
        "image": it["image"]
    })

schema_faq = []
for f in faqs:
    schema_faq.append({
        "@type": "Question",
        "name": f["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f["a"]
        }
    })

schema_json = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "ItemList",
            "name": "保湿力の強さで肌乾燥とさようなら！メディカル級の濃密保水膜で真冬の荒れ肌を包み込む高純度マヌカハニーコスメランク10",
            "description": "11月・12月の暖房乾燥と冬の冷風で荒れ狂う乾燥肌を救う高純度マヌカハニーコスメを徹底厳選！山田養蜂場、マヌカヘルス、チャントアチャーム、生活の木まで厳選。",
            "numberOfItems": 10,
            "itemListElement": schema_items
        },
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！メディカル級の濃密保水膜で真冬の荒れ肌を包み込む高純度マヌカハニーコスメランク10",
            "description": "11月・12月の暖房乾燥と冬の冷風で荒れ狂う乾燥肌を救う高純度マヌカハニーコスメを徹底厳選！山田養蜂場、マヌカヘルス、チャントアチャーム、生活の木まで厳選。",
            "image": items[0]["image"],
            "datePublished": "2026-11-04T19:00:00+09:00",
            "dateModified": "2026-11-04T19:00:00+09:00",
            "inLanguage": "ja",
            "mainEntityOfPage": "https://lumi-cosme.vercel.app/winter-manuka-honey"
        },
        {
            "@type": "FAQPage",
            "mainEntity": schema_faq
        }
    ]
}, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！メディカル級の濃密保水膜で真冬の荒れ肌を包み込む高純度マヌカハニーコスメランク10 | Lumi Cosme</title>
  <meta name="description" content="11月・12月の過酷な暖房乾燥と冬の冷風で荒れ狂う乾燥肌を救う高純度マヌカハニーコスメを徹底厳選！山田養蜂場、マヌカヘルス、チャントアチャーム、カントリー＆ストリーム、生活の木まで、楽天市場で買える本物の高保湿10選を詳しく解説。">
  <meta name="keywords" content="マヌカハニー コスメ,冬 高保湿 スキンケア,11月 コスメ,12月 コスメ,マヌカハニー リップ,山田養蜂場 クレンジングバーム,真冬 保湿 ランキング">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-manuka-honey">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #d97706;
      --primary-dark: #b45309;
      --primary-light: #fef3c7;
      --accent: #f59e0b;
      --text-main: #1f2937;
      --text-sub: #4b5563;
      --text-light: #6b7280;
      --bg-page: #fffbeb;
      --bg-card: #ffffff;
      --border-color: #fde68a;
      --shadow-sm: 0 2px 4px rgba(217, 119, 6, 0.05);
      --shadow-md: 0 4px 12px rgba(217, 119, 6, 0.1);
      --shadow-lg: 0 10px 25px -5px rgba(217, 119, 6, 0.15);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.8;
      padding-bottom: 4rem;
    }}

    .site-header {{
      background: linear-gradient(135deg, #92400e 0%, #b45309 50%, #d97706 100%);
      color: #ffffff;
      padding: 2.2rem 1.5rem 2.8rem;
      text-align: center;
      box-shadow: 0 4px 20px rgba(180, 83, 9, 0.25);
    }}
    .site-header-nav {{
      max-width: 1100px;
      margin: 0 auto 1.25rem;
      text-align: left;
    }}
    .site-header-nav a {{
      color: #fef3c7;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }}
    .site-header-nav a:hover {{ text-decoration: underline; }}
    .header-badge {{
      display: inline-block;
      background: rgba(255,255,255,0.2);
      backdrop-filter: blur(8px);
      padding: 0.4rem 1.2rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 0.8rem;
    }}
    .site-title {{
      font-size: clamp(1.4rem, 4vw, 2.2rem);
      font-weight: 800;
      line-height: 1.35;
      margin-bottom: 1rem;
      text-shadow: 0 2px 4px rgba(0,0,0,0.15);
      max-width: 920px;
      margin-left: auto;
      margin-right: auto;
    }}
    .site-subtitle {{
      font-size: 0.95rem;
      color: #fef9c3;
      max-width: 820px;
      margin: 0 auto;
    }}

    .main-container {{
      max-width: 1040px;
      margin: -1.5rem auto 0;
      padding: 0 1rem;
    }}

    .toc-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 0.6rem;
    }}
    .toc-list a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: color 0.2s ease;
    }}
    .toc-list a:hover {{ color: var(--primary); text-decoration: underline; }}

    .intro-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .intro-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 0.5rem;
    }}
    .intro-section p {{
      margin-bottom: 1.2rem;
      color: var(--text-sub);
      font-size: 1rem;
    }}
    .intro-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin-top: 1.5rem;
    }}
    .intro-card {{
      background: #fefce8;
      border-left: 4px solid var(--primary);
      padding: 1.2rem;
      border-radius: var(--radius-sm);
    }}
    .intro-card h3 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}
    .intro-card p {{
      font-size: 0.9rem;
      color: var(--text-sub);
      margin-bottom: 0;
    }}

    .table-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2rem 1.5rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
      overflow-x: auto;
    }}
    .table-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 680px;
    }}
    .compare-table th, .compare-table td {{
      padding: 1rem 0.8rem;
      border-bottom: 1px solid var(--border-color);
      text-align: left;
      vertical-align: middle;
    }}
    .compare-table th {{
      background: #fef3c7;
      color: var(--primary-dark);
      font-weight: 700;
    }}
    .rank-num {{
      font-weight: 800;
      font-size: 1.1rem;
      white-space: nowrap;
    }}
    .rank-1 {{ color: #d97706; }}
    .rank-2 {{ color: #b45309; }}
    .rank-3 {{ color: #92400e; }}
    .product-thumb img {{
      border-radius: 6px;
      object-fit: cover;
      display: block;
      border: 1px solid #fed7aa;
    }}
    .product-name-cell {{ min-width: 220px; }}
    .product-brand {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-light);
      margin-bottom: 0.2rem;
    }}
    .table-prod-link {{
      color: var(--text-main);
      text-decoration: none;
      font-weight: 700;
      line-height: 1.4;
      display: block;
    }}
    .table-prod-link:hover {{ color: var(--primary); text-decoration: underline; }}
    .type-badge {{
      display: inline-block;
      background: #fef3c7;
      color: var(--primary-dark);
      font-size: 0.75rem;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      font-weight: 600;
    }}
    .product-price {{
      font-weight: 800;
      color: #b91c1c;
      font-size: 1rem;
      white-space: nowrap;
    }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      text-decoration: none;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
      transition: background 0.2s ease;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}

    .product-card {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--border-color);
      scroll-margin-top: 2rem;
    }}
    .card-header {{
      display: flex;
      align-items: flex-start;
      gap: 1.2rem;
      margin-bottom: 1.2rem;
      border-bottom: 1px dashed var(--border-color);
      padding-bottom: 1rem;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
      color: #ffffff;
      font-size: 1.25rem;
      font-weight: 800;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-sm);
      white-space: nowrap;
      box-shadow: 0 2px 6px rgba(217, 119, 6, 0.3);
    }}
    .card-titles {{ flex: 1; }}
    .card-tag {{
      display: inline-block;
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 0.3rem;
    }}
    .card-name {{
      font-size: 1.3rem;
      font-weight: 800;
      line-height: 1.4;
      color: var(--text-main);
    }}
    .card-catch {{
      background: #fefce8;
      border-left: 4px solid var(--accent);
      padding: 0.8rem 1rem;
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 1.5rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    }}

    .card-body {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .card-body {{ grid-template-columns: 1fr; }}
    }}
    .card-image-box {{
      text-align: center;
    }}
    .card-img, .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: var(--radius-md);
      border: 1px solid #fed7aa;
      margin-bottom: 1rem;
      transition: transform 0.2s ease;
    }}
    .card-img:hover {{ transform: scale(1.02); }}
    .card-price-box {{
      margin-bottom: 0.6rem;
    }}
    .price-label {{
      font-size: 0.8rem;
      color: var(--text-light);
      display: block;
    }}
    .price-val {{
      font-size: 1.6rem;
      font-weight: 800;
      color: #b91c1c;
    }}
    .price-tax {{
      font-size: 0.8rem;
      color: var(--text-light);
    }}
    .card-review-box {{
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 1rem;
    }}
    .star-rating {{ color: #d97706; font-weight: 700; }}
    .card-aff-btn, .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
      color: #ffffff;
      text-align: center;
      padding: 0.85rem 1rem;
      border-radius: var(--radius-sm);
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      box-shadow: 0 4px 10px rgba(180, 83, 9, 0.2);
      transition: all 0.2s ease;
    }}
    .card-aff-btn:hover, .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(180, 83, 9, 0.3);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      margin-bottom: 1.5rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.8rem;
      border-bottom: 1px solid var(--border-color);
      text-align: left;
    }}
    .spec-table th {{
      width: 25%;
      color: var(--primary-dark);
      background: #fefce8;
      font-weight: 700;
    }}
    .review-text-box {{
      background: #fffdf5;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 1.25rem;
      margin-bottom: 1.2rem;
    }}
    .review-text-box h4 {{
      font-size: 1rem;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
    }}
    .review-text-box p {{
      font-size: 0.92rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
      line-height: 1.7;
    }}
    .review-text-box p:last-child {{ margin-bottom: 0; }}
    .target-box, .point-box {{
      background: #fefce8;
      padding: 0.8rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.88rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
    }}
    .target-box strong, .point-box strong {{
      color: var(--primary-dark);
    }}

    .guide-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .guide-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 0.5rem;
    }}
    .guide-section p {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 1.2rem;
    }}
    .step-list {{
      counter-reset: step;
      list-style: none;
      display: grid;
      gap: 1rem;
    }}
    .step-item {{
      background: #fefce8;
      border-radius: var(--radius-sm);
      padding: 1.2rem 1.2rem 1.2rem 3.5rem;
      position: relative;
    }}
    .step-item::before {{
      counter-increment: step;
      content: counter(step);
      position: absolute;
      left: 1.2rem;
      top: 1.2rem;
      background: var(--primary);
      color: #ffffff;
      width: 1.8rem;
      height: 1.8rem;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.9rem;
    }}
    .step-item h3 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
    }}
    .step-item p {{
      font-size: 0.9rem;
      margin-bottom: 0;
    }}

    .faq-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .faq-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border-color);
      padding: 1.2rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      display: flex;
      align-items: flex-start;
      gap: 0.8rem;
      margin-bottom: 0.6rem;
    }}
    .faq-q-badge {{
      background: var(--primary);
      color: #ffffff;
      padding: 0.1rem 0.5rem;
      border-radius: 4px;
      font-size: 0.85rem;
    }}
    .faq-a {{
      display: flex;
      align-items: flex-start;
      gap: 0.8rem;
      color: var(--text-sub);
      font-size: 0.93rem;
    }}
    .faq-a-badge {{
      background: #fed7aa;
      color: #92400e;
      padding: 0.1rem 0.5rem;
      border-radius: 4px;
      font-size: 0.85rem;
      font-weight: 700;
    }}

    .related-links-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .related-links-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}
    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
    }}
    .related-card {{
      background: #fffdf5;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 1rem;
      text-decoration: none;
      transition: all 0.2s ease;
      display: block;
    }}
    .related-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
      border-color: var(--primary);
    }}
    .related-card h3 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
      line-height: 1.4;
    }}
    .related-card p {{
      font-size: 0.8rem;
      color: var(--text-light);
      margin-bottom: 0;
      line-height: 1.5;
    }}

    .site-footer {{
      background: #451a03;
      color: #fef3c7;
      text-align: center;
      padding: 3rem 1.5rem;
      font-size: 0.85rem;
      margin-top: 4rem;
    }}
    .site-footer a {{
      color: #fed7aa;
      text-decoration: none;
      margin: 0 0.5rem;
    }}
    .site-footer a:hover {{ text-decoration: underline; }}
  </style>

  <!-- JSON-LD 構造化データ -->
  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body>

  <header class="site-header">
    <div class="site-header-nav">
      <a href="/">🏠 Lumi Cosme ホームに戻る</a>
    </div>
    <span class="header-badge">2026-2027 冬の高保湿メディカルハニー特集</span>
    <h1 class="site-title">保湿力の強さで肌乾燥とさようなら！<br>メディカル級の濃密保水膜で真冬の荒れ肌を包み込む高純度マヌカハニーコスメランク10</h1>
    <p class="site-subtitle">11月〜12月の木枯らしと過酷なエアコン暖房にさらされた乾燥肌へ。野生のマヌカ花が宿す驚異のMGO抗菌力と濃密な天然蜜膜が、皮むけ・ひび割れ・ガサガサ角層を極上の潤いシールドで満たす最高峰のコスメを徹底比較！</p>
  </header>

  <main class="main-container">

    <!-- 目次 -->
    <nav class="toc-box">
      <h2 class="toc-title">📑 本記事の目次（タップで各商品へスキップ）</h2>
      <ul class="toc-list">
        <li><a href="#intro">🍯 なぜ11-12月の砂漠肌にマヌカハニーが最強なのか？</a></li>
        <li><a href="#table">📊 高保湿マヌカハニーコスメ10選 スペック比較表</a></li>
        <li><a href="#rank-1">第1位：山田養蜂場 マヌカハニークレンジングバーム</a></li>
        <li><a href="#rank-2">第2位：山田養蜂場 マヌカハニー エッセンスジェル</a></li>
        <li><a href="#rank-3">第3位：マヌカヘルス MGO250+ リップバーム</a></li>
        <li><a href="#rank-4">第4位：チャントアチャーム モイスト ブースターオイル</a></li>
        <li><a href="#rank-5">第5位：キハナクリーミーセラム マヌカハニーバーム</a></li>
        <li><a href="#rank-6">第6位：カントリー＆ストリーム ナチュラルハニーリップ</a></li>
        <li><a href="#rank-7">第7位：マヌカコスメ モイストオールインワンジェル</a></li>
        <li><a href="#rank-8">第8位：生活の木 シアバター＆ハニー リップバーム</a></li>
        <li><a href="#rank-9">第9位：プロハーブ リップクリーム</a></li>
        <li><a href="#rank-10">第10位：ピュア マヌカハニー モイスチャーデイリーマスク</a></li>
        <li><a href="#guide">💡 真冬の乾燥を跳ね返すマヌカハニースキンケア術</a></li>
        <li><a href="#faq">❓ よくある質問と皮膚科学的回答</a></li>
      </ul>
    </nav>

    <!-- 導入解説 -->
    <section class="intro-section" id="intro">
      <h2>🍯 なぜ11-12月の砂漠肌にマヌカハニーが最強の盾となるのか？</h2>
      <p>11月から12月へと季節が進むにつれ、外気の湿度は30%台にまで急落し、室内ではエアコン暖房の温風が絶え間なく肌の水分を奪い去ります。この時期に多くの女性を悩ませるのが、「どんなに化粧水を重ねても数時間でパリパリに乾く」「夕方になると口元や目元が粉を吹き、笑うと皮膚がひび割れそうに突っ張る」という深刻な砂漠化現象です。</p>
      <p>通常の保湿ケアで太刀打ちできない理由は、寒冷と乾燥によって角層細胞が萎縮し、細胞と細胞の間に目に見えない『マイクロクラック（微小な裂け目）』が生じているためです。亀裂が入った角層からは水分が際限なく蒸発し、外気中のチリやホコリが侵入して微小な炎症を引き起こします。この悪循環を断ち切るために美容皮膚界隈で熱烈な注目を浴びているのが、ニュージーランド原生植物の蜜から採れる『高純度マヌカハニー』です。</p>
      
      <div class="intro-grid">
        <div class="intro-card">
          <h3>🔬 1. 独自成分MGOによる微小炎症の鎮静</h3>
          <p>一般のハチミツにはほとんど含まれない天然生理活性物質『MGO（メチルグリオキサール）』を豊富に含有。冬の冷風や摩擦でピリピリと赤みを帯びた敏感肌を穏やかに鎮静させ、健やかなターンオーバーをサポートします。</p>
        </div>
        <div class="intro-card">
          <h3>💧 2. 強力な浸透圧と天然糖類の高保水シールド</h3>
          <p>マヌカハニーに含まれる果糖やブドウ糖などの微細多糖類は、周囲の水分分子を強力に抱え込む親水性を持っています。角層の奥深くに水分を固定し、暖房の風にさらされても蒸発させない鉄壁の保水膜を形成します。</p>
        </div>
        <div class="intro-card">
          <h3>🍯 3. 人間の皮脂膜と調和するエモリエント密閉</h3>
          <p>天然酵素やアミノ酸、ミネラルをバランス良く含むため、人工的なシリコンとは異なり肌の呼吸を妨げず、まるで生まれたての上質な皮脂膜のようにしなやかで柔らかい柔軟ヴェールをキープします。</p>
        </div>
      </div>
    </section>

    <!-- 比較表 -->
    <section class="table-section" id="table">
      <h2>📊 高保湿マヌカハニーコスメ10選 スペック徹底比較表</h2>
      <p style="font-size:0.9rem; color:var(--text-sub); margin-bottom:1rem;">※楽天市場公式取扱店・直営店の最新参考価格（税込）を表示しています。各商品リンクより現在のポイント還元率や在庫状況をご確認いただけます。</p>
      <table class="compare-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>画像</th>
            <th>商品名 / ブランド</th>
            <th>アイテム分類</th>
            <th>参考価格</th>
            <th>楽天詳細</th>
          </tr>
        </thead>
        <tbody>
          {table_joined}
        </tbody>
      </table>
    </section>

    <!-- 商品カード一覧 -->
    <section class="products-section">
      {cards_joined}
    </section>

    <!-- 効果的な使い方ガイド -->
    <section class="guide-section" id="guide">
      <h2>💡 真冬の乾燥を寄せ付けないマヌカハニースキンケア3大鉄則</h2>
      <p>高純度マヌカハニーのポテンシャルを120%引き出し、11月・12月の過酷な低湿度環境をモチモチの満水肌で乗り切るためのプロ直伝ルーティンです。</p>
      
      <div class="step-list">
        <div class="step-item">
          <h3>ステップ1：洗顔後3秒以内の『ブースター導入』で角層の受け入れ態勢を整える</h3>
          <p>冬の浴室を出た瞬間から肌の水分蒸発は急速に進行します。タオルで水気を軽く押さえたら、間髪を入れずにマヌカハニー配合の導入美容オイル（チャントアチャーム）を馴染ませてください。寒さで硬化した角質細胞がふんわりほぐれ、後から重ねる化粧水の浸透ルートが劇的に拓かれます。</p>
        </div>
        <div class="step-item">
          <h3>ステップ2：『水分＋ハチミツシートマスク』で角層細胞の隙間を満水化</h3>
          <p>暖房を長時間浴びた夜は、化粧水を手で塗るだけでなく、マヌカハニーとローヤルゼリーを贅沢に含んだシートマスクで5〜10分間集中パック。角層の奥深くにある細胞ひとつひとつに水分とアミノ酸を巡らせ、インナードライを根本から満水状態へとリセットします。</p>
        </div>
        <div class="step-item">
          <h3>ステップ3：就寝前の『ハニーバーム温感プレス』で密閉ロック</h3>
          <p>スキンケアの総仕上げとして、濃厚なマヌカハニーバームやクリームを手のひらに広げ、体温で温めてから顔全体を包み込むようにハンドプレス。特に乾燥が激しい目元・口元・唇には指先で重ねづけすることで、一晩中暖房をつけた寝室でも翌朝まで吸い付くようなモチ肌をキープできます。</p>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="faq-section" id="faq">
      <h2>❓ 高純度マヌカハニーコスメに関するよくある質問（FAQ）</h2>
      {faqs_joined}
    </section>

    <!-- 内部リンク -->
    <section class="related-links-section">
      <h2>🔗 あわせて読みたい！冬の徹底保湿・エイジングケア特集</h2>
      <div class="related-grid">
        <a href="/winter-resurrection-plant" class="related-card">
          <h3>🌵 復活草・トレハロースコスメ厳選10</h3>
          <p>砂漠の極限乾燥を生き抜くテマリカヒバの驚異的な保水力！冬の干からびた肌細胞を満水へ導く名品まとめ。</p>
        </a>
        <a href="/winter-beta-glucan" class="related-card">
          <h3>🔬 高保湿ベータグルカンコスメ厳選10</h3>
          <p>ヒアルロン酸を超える保水力とバリア修復力！冬の寒暖差ストレスと肌荒れを救う次世代セラム特集。</p>
        </a>
        <a href="/winter-avocado" class="related-card">
          <h3>🥑 濃厚アボカドコスメ厳選10</h3>
          <p>森のバターと呼ばれるオレイン酸の恵み。冬のゴワゴワ粉吹き肌をとろける柔軟膜で包み込む名品集。</p>
        </a>
        <a href="/winter-beeswax" class="related-card">
          <h3>🐝 高保湿ミツロウコスメ厳選10</h3>
          <p>ミツバチが創る天然の保護皮膜！真冬の冷風と乾燥を完全遮断する高密着バーム・クリーム特集。</p>
        </a>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <p>&copy; 2026-2027 Lumi Cosme (ルミコスメ) - 冬の乾燥対策・高保湿スキンケア専門ガイド</p>
    <p style="margin-top:0.5rem;">
      <a href="/">トップページ</a> | 
      <a href="/winter-resurrection-plant">復活草コスメ</a> | 
      <a href="/winter-beta-glucan">ベータグルカン</a> | 
      <a href="/winter-avocado">アボカドコスメ</a> | 
      <a href="/winter-manuka-honey">マヌカハニー</a>
    </p>
  </footer>

</body>
</html>
"""

with open("winter-manuka-honey.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated winter-manuka-honey.html successfully!")
