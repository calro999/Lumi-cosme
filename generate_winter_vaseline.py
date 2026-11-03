import json
import re

with open("fetched_3new_nov_dec_heparinoid_vaseline_placenta_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_vaseline"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 精製度の最高峰！不純物を極限まで排除した眼科・皮膚科御用達の最高純度ワセリン",
        "catch": "アレルギーゼロを目指した最高品質。赤ちゃんの素肌から敏感な目元まで守り抜く鉄壁の保護膜",
        "brand_name": "日興リカ (SUNWHITE)",
        "capacity": "50g (サンホワイト P-1)",
        "type": "最高純度・高品質白色ワセリン",
        "features": "高精製白色ワセリン100%、無香料・無着色・保存料不使用、アレルギーテスト・パッチテスト済み、紫外線吸収なし",
        "value": "白色ワセリンをさらに高度精製し微量な不純物や酸化物を徹底除去。酸化・油焼けの心配が一切なく、真冬の極限乾燥から肌を完全シールド",
        "desc_p1": "11月から12月にかけて湿度が20%近くまで低下すると、どんな低刺激化粧品でもピリピリとしみる重度のバリア破壊に直面することがあります。日興リカの『サンホワイト P-1』は、一般的な白色ワセリンよりもさらに高度に精製され、不純物を極限まで取り除いたワセリンの最高峰グレードです。",
        "desc_p2": "体温でじんわりと柔らかくなり、肌表面に薄く均一な保護ヴェールを形成。外気の乾いた冷風やハウスダスト、花粉などのアレルゲンを物理的に遮断しながら、肌内部の水分蒸散をほぼゼロに抑え込みます。光毒性や酸化変質がないため、冬の朝のメイク前や日中の外出時にも安心して使用可能。超敏感肌やアトピー肌、冬枯れでボロボロになった肌の緊急レスキューとして絶対的な信頼を誇ります。",
        "target": "一般的な化粧水や乳液がしみて使えない超敏感肌の方、目元や唇の皮むけを刺激なく保護したい方、最高純度の安心感を求める方",
        "point": "米粒大ほどをごく少量手のひらに取り、両手をすり合わせて温めながら薄く伸ばします。擦るのではなく、顔全体を手のひらで優しく覆うようにスタンプづけするのが薄膜を均一に張る秘訣です。"
    },
    {
        "rank": 2,
        "tag": "🩺 医療現場で信頼されるピュアワセリン！伸びが良くベタつきを抑えた第3類医薬品",
        "catch": "皮膚科処方の定番軟膏を市販化。皮膚の油分を補い保護するデリケート肌のためのピュアシールド",
        "brand_name": "第一三共ヘルスケア (プロペト)",
        "capacity": "30g (プロペト ピュアベールa)",
        "type": "第3類医薬品・ピュアワセリン軟膏",
        "features": "白色ワセリンをさらに精製したピュアワセリン100%、防腐剤・酸化防止剤・着色料・香料無添加、第3類医薬品認可",
        "value": "目元・唇・手足のひび割れ・あかぎれに医薬品基準の保護効果。柔らかく滑らかな伸び心地で摩擦刺激を最小限に抑える",
        "desc_p1": "医療機関で広く皮膚保護薬として処方されている『プロペト』を、一般用医薬品（第3類医薬品）として手軽に購入できるようにしたのが第一三共ヘルスケアの『プロペト ピュアベールa』です。白色ワセリンからさらに精製を進めて純度を高めています。",
        "desc_p2": "通常の白色ワセリンよりもテクスチャーが柔らかく設計されており、カサついて荒れた肌の上でも引っかかることなくスルスルと滑らかに伸びます。薄い油膜となって水分蒸散を防ぎ、外部刺激から傷ついた角層を保護。30gのコンパクトなチューブタイプなので衛生的で、外出時の手指のあかぎれ予防や、冬の冷風でヒリつく頬の保護にも手軽に持ち運んで活用できます。",
        "target": "固いワセリンの伸びにくさが気になる方、手指のひび・あかぎれを治療・予防したい方、医薬品としての品質と安全性を求める方",
        "point": "乾燥やあかぎれが気になる部位に、少量を優しくすり込むように塗布します。お風呂上がりの水分が残っているタイミングで塗ると、水分を抱え込んだまま密封でき、よりしっとり感が持続します。"
    },
    {
        "rank": 3,
        "tag": "👶 生まれたての赤ちゃんから使える安心処方！柔らかく使いやすい大容量ワンタッチチューブ",
        "catch": "パラベンフリー＆不純物カット。家族みんなの冬の乾燥・肌荒れを優しく守る定番ワセリン",
        "brand_name": "健栄製薬 (KENEI)",
        "capacity": "100g (ベビーワセリン)",
        "type": "低刺激ピュアワセリン",
        "features": "白色ワセリン、無香料・無着色・パラベンフリー、ワンタッチキャップチューブ容器、アレルギーテスト済み",
        "value": "従来のジャー容器のような指ですくう不衛生さを解消したワンタッチチューブ。柔らかく絞り出せて顔・体・お尻まわりまで全身にマルチ対応",
        "desc_p1": "製薬メーカーの健栄製薬が、赤ちゃんのデリケートな素肌を考えて開発したベストセラー『ベビーワセリン』。従来の硬いワセリンのイメージを覆す、非常に柔らかく伸びの良い高純度ワセリンです。",
        "desc_p2": "香料・着色料・防腐剤を一切使用せず、純度の高い白色ワセリンのみを充填。片手で開閉できるワンタッチチューブ仕様のため、入浴後や外出先でもストレスフリーで素早く塗布できます。乳幼児のよだれかぶれや頬の乾燥対策はもちろん、大人の冬の粉吹き肌、ひじ・かかとの保湿、リップケアまで、一家に一本常備しておきたい真冬の必需品です。",
        "target": "乳幼児のお子様と一緒にスキンケアをしたい方、ジャー容器の衛生面が気になる方、柔らかく全身に伸ばしやすいワセリンを探している方",
        "point": "チューブから適量を押し出し、清潔な指先で乾燥部分に優しく伸ばします。乾燥がひどいすねや腕には、入浴直後まだ肌がしっとりしている状態で塗ると驚くほど滑らかになじみます。"
    },
    {
        "rank": 4,
        "tag": "🌍 150年以上の歴史を誇る世界標準！全身のあらゆる乾燥をブロックする元祖ピュアジェリー",
        "catch": "ミクロの保湿膜が角質層の隙間を密封。冬の乾燥冷風や暖房にびくともしない圧倒的バリア力",
        "brand_name": "Vaseline (ユニリーバ)",
        "capacity": "80g (オリジナル ピュアスキンジェリー)",
        "type": "高純度ピュアワセリン100%",
        "features": "ワセリン100%、無香料・無着色・防腐剤無添加、3回にわたる高度精製プロセス、アレルギーテスト済み",
        "value": "1870年の誕生以来世界中で愛され続けるスキンプロテクトの原点。圧倒的なコストパフォーマンスと確固たる皮膚保護力",
        "desc_p1": "世界中で肌の保護剤として親しまれているヴァセリンの代名詞『オリジナル ピュアスキンジェリー』。独自の3重精製プロセスにより、肌に不要な不純物を徹底的に取り除いた純度100%のナチュラルワセリンです。",
        "desc_p2": "こっくりとした濃厚なテクスチャーで、肌の上にしっかりとした保護膜を形成。冬の乾燥した空気や摩擦などの外的刺激を完全に遮断し、角層の水分が逃げるのを力強く防ぎます。唇の荒れ、かかとの角質ケア、指先のささくれ、花粉や鼻かみによる小鼻の赤みケアなど、真冬のあらゆる部位のレスキューアイテムとして圧倒的な実力を発揮します。",
        "target": "昔ながらの確かな保護力と重厚感を好む方、コスパ重視でたっぷり全身に使いたい方、ささくれやかかとの硬化に悩む方",
        "point": "手のひらでしっかり温めてオイル状に溶かしてから塗布すると、ベタつきが大幅に軽減され均一に密着します。就寝前にかかとに厚めに塗り、靴下を履いて寝ると翌朝ツルツルになります。"
    },
    {
        "rank": 5,
        "tag": "🌿 資生堂の先進技術！高精製ワセリン×抗炎症有効成分がとろける薬用バーム",
        "catch": "バーム特有のベタつきを解消。肌荒れ・ニキビを防ぎながらピタッと密着密封する大人気処方",
        "brand_name": "IHADA (資生堂イハダ)",
        "capacity": "20g (薬用バーム)",
        "type": "医薬部外品・薬用とろける高精製ワセリンバーム",
        "features": "高精製ワセリン配合、抗炎症有効成分グリチルレチン酸ステアリル、無香料・無着色・アルコールフリー・パラベンフリー",
        "value": "資生堂独自の高精製ワセリン技術により、従来のワセリンのようなギトギト感を完全に排除。なめらかにとろけて毛穴を塞がず肌荒れを防止",
        "desc_p1": "『ワセリンで保護したいけれど、ベタつきやニキビが心配』という声を覆した大ヒットコスメ、IHADAの薬用バーム。資生堂が誇る高度な精製技術で不純物を極限まで抑えた『高精製ワセリン』を配合した医薬部外品です。",
        "desc_p2": "肌に乗せると体温ですーっととろけて、まるで美容オイルのように軽やかに広がります。抗炎症有効成分のグリチルレチン酸ステアリルが、乾燥やマスク摩擦による肌荒れ・赤みを同時に鎮静。肌表面を密封しながらも毛穴を塞ぐような圧迫感が一切なく、メイク前にも安心して使えます。11月〜12月の急激な気温低下でゆらぎやすい肌を穏やかに守り抜きます。",
        "target": "ワセリン特有のベタつきや重さが苦手な方、肌荒れや大人ニキビができやすい敏感肌の方、日中やメイク前にも使いたい方",
        "point": "お手入れの最後に、指先で適量をすくい取り、両頬・額・あごの順に置いてから優しく伸ばします。乾燥が特に気になる目元や口元には、指の腹でトントンと重ねて密着させてください。"
    },
    {
        "rank": 6,
        "tag": "✨ 驚きのエアリー感！ワセリンなのにサラサラ伸びる日興リカの革新テクスチャー",
        "catch": "最高純度サンホワイトの保護力はそのまま。プッシュ式で使いやすく顔全体にスーッと伸びる",
        "brand_name": "日興リカ (SUNWHITE)",
        "capacity": "80g (サンホワイト シルキー Y-1)",
        "type": "高品質・エアリー高純度白色ワセリン",
        "features": "高精製白色ワセリン、無香料・無着色・無添加、プッシュ式ボトル容器、シルキーテクスチャー処方",
        "value": "特殊な製法により従来のサンホワイトP-1と同等の高純度を保ちながら、乳液のように滑らかでサラッとした伸び心地を実現",
        "desc_p1": "最高純度ワセリンの金字塔『サンホワイト』から誕生した新世代の『シルキー Y-1』。従来のワセリンの『伸びにくくて摩擦が気になる』『塗った直後に髪が顔に張り付く』という悩みを一挙に解決した画期的なアイテムです。",
        "desc_p2": "プッシュ式ボトルから出てくるワセリンは、驚くほど柔らかくシルクのような軽やかな質感。肌に伸ばすと瞬時に薄膜となって均一に広がり、サラリとした後肌に整います。高い水分蒸散抑制効果はそのまま維持されているため、真冬の強烈な乾燥風からもしっかり肌をガード。朝の忙しい時間でもサッと手早く全顔に塗布できる快適性が絶賛されています。",
        "target": "従来のワセリンのベタつきや固さに挫折した方、プッシュ容器で手軽に使いたい方、全顔にストレスなくサラッと伸ばしたい方",
        "point": "1プッシュを手のひらに取り、顔全体に滑らせるように優しく広げます。乳液やクリームの代わりとしても、スキンケアの最後の保護膜としても軽快に使用できます。"
    },
    {
        "rank": 7,
        "tag": "💋 ガサガサ唇の皮むけを即効シールド！塗りやすい斜めカットのピュアワセリンリップ",
        "catch": "添加物ゼロで口に入っても安心。真冬の冷風でひび割れる唇をぷるぷるに集中保護",
        "brand_name": "健栄製薬 (KENEI)",
        "capacity": "10g (ベビーワセリンリップ)",
        "type": "唇用高純度ピュアワセリン",
        "features": "白色ワセリン100%、無香料・無着色・パラベンフリー、唇にフィットする斜めカットチューブ",
        "value": "デリケートで角層が極めて薄い唇専用に設計。余計なメントールや香料を含まず、ひび割れた唇にも一切刺激を与えずに密封",
        "desc_p1": "11月から12月にかけて最も乾燥ダメージを受けやすい部位が『唇』です。皮脂腺がなく角層が薄い唇は、冬の冷風と暖房ですぐに皮がめくれ、出血やひび割れを起こします。健栄製薬の『ベビーワセリンリップ』は、不純物をカットしたピュアワセリンを唇専用のチューブに詰めた名品です。",
        "desc_p2": "唇の輪郭にぴったりフィットする斜めカット設計となっており、指を汚さずにいつでも直接塗布可能。体温でとろけてピタッと密着し、食事や会話でも取れにくい強固な保護ヴェールを張ります。無味無臭で刺激成分がゼロのため、皮がめくれてヒリつく唇でも痛みを感じることなく集中修復できます。リップ下地やおやすみ前のリップパックとしても極めて優秀です。",
        "target": "冬になると唇の皮がむけて血がにじむ方、メントールや香料入りリップで唇が荒れてしまう方、外出先で手軽に唇を保湿したい方",
        "point": "チューブから直接唇に当て、中央から外側へ向けて優しく滑らせます。夜寝る前は、唇の輪郭からはみ出すくらいたっぷり厚めに塗ると、翌朝ぷるんとした柔らかさが復活します。"
    },
    {
        "rank": 8,
        "tag": "🌿 刺激が少なく伸びが良い国産高純度！使いやすさと安心感を両立したチューブタイプ",
        "catch": "高圧水素化精製で不純物を極限低減。敏感肌の日常保湿に最適なワセリンHG",
        "brand_name": "大洋製薬 (TAIYO)",
        "capacity": "60g (ワセリンHG チューブ)",
        "type": "高品質精製白色ワセリン",
        "features": "高精製白色ワセリン、酸処理を行わない高圧水素化精製法、無香料・無着色・保存料不使用",
        "value": "薬品メーカー大洋製薬の高度な精製技術。従来の白色ワセリンよりも酸価が低く酸化しにくいため、デリケートな肌にも長時間の安心感",
        "desc_p1": "製薬メーカーとして定評のある大洋製薬が手がける『ワセリンHG』。不純物を取り除く精製工程に高圧水素化処理を採用し、酸性物質や刺激物質を徹底的に低減させた高品質な白色ワセリンです。",
        "desc_p2": "滑らかで均一なテクスチャーに仕上げられており、チューブから絞り出しやすく、肌に塗布する際もスムーズに広がります。敏感肌のフェイスケアはもちろん、冬場の水仕事で荒れた指先、靴擦れやかかとのガサガサ予防など、あらゆる皮膚の保護に大活躍。持ち運びに便利な60gスリムチューブで、日常のあらゆる乾燥シーンに寄り添います。",
        "target": "肌への刺激物質をとことん減らしたい方、チューブタイプで衛生的に使い続けたい方、水仕事が多く手荒れが深刻な方",
        "point": "指先に少量を取り、体温で温めてから患部に薄く伸ばします。水仕事の前に手に塗っておくと、水や洗剤の刺激を弾くバリアシールドとして機能します。"
    },
    {
        "rank": 9,
        "tag": "📦 日本薬局方基準の確かな品質！半世紀以上愛される安心の定番白色ワセリン",
        "catch": "医薬品基準の確固たる保護力。冬の皮膚の荒れ・ただれ・乾燥を根本から防ぐ",
        "brand_name": "健栄製薬 (KENEI)",
        "capacity": "50g (日本薬局方 白色ワセリン)",
        "type": "第3類医薬品・日本薬局方白色ワセリン",
        "features": "日局白色ワセリン100%、第3類医薬品、無香料・無着色、皮膚保護・手足の荒れ・ひび・あかぎれ効能効果",
        "value": "国が定める医薬品規格『日本薬局方』に完全合致。厳格な純度試験をクリアした信頼の第3類医薬品",
        "desc_p1": "日本の医療現場や調剤薬局で基剤としても広く使用されている、健栄製薬の『日本薬局方 白色ワセリン』。国の医薬品規格基準に厳格に適合した第3類医薬品です。",
        "desc_p2": "石油から得た炭化水素類の混合物を高度に脱色・精製したもので、皮膚表面に留まって水分の蒸発を防ぎ、物理的刺激から患部を守ります。手足のヒビ、あかぎれ、皮膚の荒れに対する確かな効能効果が認められており、冬の乾燥によって傷ついた皮膚のバリア機能を力強くサポートします。確かな医薬品クオリティを身近に常備したい方に最適です。",
        "target": "医薬品基準の確かな効果を求める方、手足のひび割れやあかぎれをしっかり防ぎたい方、実績ある王道アイテムを選びたい方",
        "point": "患部を清潔にした後、適量をそのまま優しく塗布してください。おやすみ前に乾燥の気になる部位に塗り、手袋や靴下を着用して就寝すると集中密閉ケアが可能です。"
    },
    {
        "rank": 10,
        "tag": "🧴 極小ワセリンジェリーを配合した高保湿ミルク！全身の乾燥を潤いで包み込む大容量400ml",
        "catch": "ワセリンの保護力×ローションのみずみずしさ。ベタつかずスーッとなじんで粉吹き肌を滑らかに",
        "brand_name": "Vaseline (ユニリーバ)",
        "capacity": "400ml (アドバンスドリペア ボディローション)",
        "type": "高保湿全身用ワセリンミルク",
        "features": "微小ワセリンジェリー配合、無香料処方、大容量400mlポンプ、角層深部浸透処方",
        "value": "固形ワセリンの圧倒的なバリア力を、全身に塗り広げやすいポンプ式乳液へと昇華。冬のお風呂上がりに一瞬で全身の粉吹き乾燥をケア",
        "desc_p1": "真冬になると、顔だけでなくすねや背中、腕など全身が粉を吹き、かゆみやカサつきが生じます。ヴァセリンの『アドバンスドリペア ボディーローション』は、微小化したワセリンジェリーを配合し、乳液の浸透力とワセリンの保護力を両立させた大容量ボディミルクです。",
        "desc_p2": "ポンプを押すとトロリとしたなめらかなローションが出てきて、肌の上を心地よくすべりながら素早く浸透。角層深部までうるおいを行き渡らせた後、表面に極薄のワセリン保護ヴェールを張るため、ベタつかず服がすぐに着られる快適さを実現しています。無香料で家族全員が使いやすく、400mlのビッグサイズで冬の毎日の全身保湿を力強く支えます。",
        "target": "冬になると全身の粉吹きやかゆみに悩む方、ワセリンを全身に手軽に塗りたい方、ベタつかず素早く服を着たい方",
        "point": "入浴後、タオルで軽く水気を拭き取った直後の湿り気がある肌に、1〜2プッシュを全身に伸ばします。すねやひじなど乾燥しやすい部位には重ねづけがおすすめです。"
    }
]

# JSON-LD構造化データ作成
faq_data = [
    {
        "q": "ワセリンの精製度の違い（黄色ワセリン、白色ワセリン、プロペト、サンホワイト）はどう選べばいいですか？",
        "a": "精製度は『黄色ワセリン ＜ 白色ワセリン ＜ プロペト ＜ サンホワイト』の順に高くなります。日常的なボディやかかとの保湿には『白色ワセリンやベビーワセリン』で十分ですが、目元や唇、荒れてヒリつく超敏感肌、アトピー肌、または赤ちゃんの顔には、不純物を極限まで除いた『プロペトやサンホワイト』を選ぶのが最も安全で安心です。"
    },
    {
        "q": "ワセリンを塗ると油焼け（シミ）の原因になりませんか？日中や朝に使っても大丈夫ですか？",
        "a": "現代の精製された白色ワセリンやサンホワイトは不純物が極めて微量のため、日光による油焼けの心配は基本的にありません。ただし、厚く塗りすぎるとファンデーションがヨレる原因になるため、朝のメイク前に使う場合は『米粒半分〜1粒程度をごく薄く手のひらで押し込む』のがきれいに仕上げるコツです。"
    },
    {
        "q": "ワセリン自体には肌に水分を与える効果はないのですか？",
        "a": "はい。ワセリンは炭化水素でできた油分シールドであり、水分や美容成分そのものは含みません。その代わり『肌内部から水分が蒸発するのを防ぐ力（経表皮水分蒸散量の抑制）』はあらゆる保湿成分の中でトップクラスです。そのため、洗顔後に化粧水や美容液でしっかり水分を補給した直後に、水分を閉じ込めるフタとしてワセリンを重ねるのが最も効果的な使い方です。"
    },
    {
        "q": "ワセリンを塗ると毛穴が詰まってニキビができませんか？",
        "a": "純度の高いワセリンは肌のアレルギー反応を起こしにくい不活性な成分ですが、皮脂の分泌が多いTゾーンなどに厚塗りしすぎると、毛穴を覆ってコメド（ニキビの初期段階）の原因になることがあります。皮脂が出やすい部位は避け、乾燥や粉吹きが気になる頬・目元・口元を中心に薄く塗布するのがベストです。"
    },
    {
        "q": "11月・12月の冬本番にワセリンを活用するプロおすすめの裏技はありますか？",
        "a": "『お風呂上がりの濡れた肌への薄塗り』と『就寝前のピンポイント部分パック』です。入浴直後、顔や体に微量の水分が残っている状態で米粒大のワセリンを手のひらで伸ばしてハンドプレスすると、驚くほどスッと伸びてベタつかず水分を抱え込みます。また、唇や目尻、かかとに少し厚めに塗ってラップや靴下で覆うと、翌朝驚くほどふっくら柔らかくなります。"
    }
]

schema_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！水分蒸発をゼロに抑えて冬の冷風から守り抜く高純度ワセリンランク10",
    "description": "11月・12月の真冬乾燥に！水分蒸発をゼロに抑えて外気刺激を完全遮断する高純度ワセリン10選を徹底比較。サンホワイト、プロペト、ベビーワセリン、IHADA薬用バームなど厳選。",
    "image": items[0]["img_url"],
    "datePublished": "2026-11-03T10:00:00+09:00",
    "dateModified": "2026-11-03T10:00:00+09:00",
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
        "@id": "https://lumi-cosme.vercel.app/winter-vaseline"
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
            "name": "高純度ワセリンランク10",
            "item": "https://lumi-cosme.vercel.app/winter-vaseline"
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
          <span class="product-capacity">規格・容量: {p['capacity']}</span>
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
            <strong>精製度・処方特徴:</strong> {p['features']}
          </div>
          <div class="product-value-point">
            <strong>真冬の密封保護力:</strong> {p['value']}
          </div>
        </div>
      </div>

      <div class="product-desc">
        <p class="desc-lead">{p['desc_p1']}</p>
        <p class="desc-detail">{p['desc_p2']}</p>
      </div>

      <div class="product-advice-grid">
        <div class="advice-box target-box">
          <div class="advice-title">💡 こんな肌悩みの方に最適</div>
          <p>{p['target']}</p>
        </div>
        <div class="advice-box usage-box">
          <div class="advice-title">🛡️ 密封力を最大化する使用法</div>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-cta">
        <a href="{it['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener nofollow">
          楽天市場で詳細・最安値をチェック <span>→</span>
        </a>
      </div>
    </div>
    """

# 比較テーブル作成
table_rows = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    price_str = f"¥{it['price']:,}" if it['price'] > 0 else "オープン価格"
    table_rows += f"""
    <tr>
      <td class="tbl-rank">第{p['rank']}位</td>
      <td class="tbl-name"><a href="#rank-{p['rank']}">{p['brand_name']}<br><strong>{p['capacity']}</strong></a></td>
      <td class="tbl-type">{p['type']}</td>
      <td class="tbl-feat">{p['features']}</td>
      <td class="tbl-price">{price_str}</td>
    </tr>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！水分蒸発をゼロに抑えて冬の冷風から守り抜く高純度ワセリンランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の真冬乾燥に！水分蒸発をゼロに抑えて外気刺激を完全遮断する高純度ワセリン10選を徹底比較！サンホワイト、プロペト、ベビーワセリン、IHADA薬用バームなど厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-vaseline">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- OGP -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！水分蒸発をゼロに抑えて冬の冷風から守り抜く高純度ワセリンランク10 | 冬コスメ徹底比較ラボ">
  <meta property="og:description" content="11月・12月の真冬乾燥に！水分蒸発をゼロに抑えて外気刺激を完全遮断する高純度ワセリン10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-vaseline">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta name="twitter:card" content="summary_large_image">

  <!-- JSON-LD 構造化データ -->
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
      --primary: #059669;
      --primary-light: #d1fae5;
      --primary-dark: #047857;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --bg-light: #f8fafc;
      --border-color: #e2e8f0;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --card-hover-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text-main);
      background-color: #f1f5f9;
    }}

    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .header-inner {{
      max-width: 1000px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .container {{
      max-width: 900px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .article-wrap {{
      background: #ffffff;
      padding: 3rem 2.5rem;
      border-radius: 12px;
      box-shadow: var(--card-shadow);
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}

    .breadcrumb a {{
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .article-title {{
      font-size: 1.85rem;
      line-height: 1.4;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.5rem;
    }}

    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border-color);
    }}

    .lead-box {{
      background: #ecfdf5;
      border-left: 4px solid var(--primary);
      padding: 1.5rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 2.5rem;
      font-size: 1.05rem;
      line-height: 1.8;
    }}

    .section-title {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #0f172a;
      margin: 3rem 0 1.5rem 0;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 2rem;
      margin-bottom: 3rem;
      position: relative;
      box-shadow: var(--card-shadow);
      transition: box-shadow 0.2s ease;
    }}

    .product-card:hover {{
      box-shadow: var(--card-hover-shadow);
    }}

    .product-rank-badge {{
      position: absolute;
      top: -12px;
      left: 20px;
      background: linear-gradient(135deg, #059669, #047857);
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 0.25rem 1rem;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(5, 150, 105, 0.3);
    }}

    .product-header {{
      margin-top: 0.5rem;
      margin-bottom: 1.5rem;
    }}

    .product-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: #047857;
      background: #d1fae5;
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      margin-bottom: 0.5rem;
    }}

    .product-title {{
      font-size: 1.3rem;
      font-weight: 700;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 0.5rem;
    }}

    .product-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .product-body {{
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 2rem;
      margin-bottom: 1.5rem;
    }}

    @media (max-width: 640px) {{
      .product-body {{
        grid-template-columns: 1fr;
      }}
      .article-wrap {{
        padding: 2rem 1.25rem;
      }}
      .article-title {{
        font-size: 1.5rem;
      }}
    }}

    .product-img-wrap {{
      text-align: center;
      background: #f8fafc;
      padding: 1rem;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .product-img {{
      max-width: 100%;
      max-height: 220px;
      object-fit: contain;
      border-radius: 4px;
    }}

    .product-info {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 0.75rem;
    }}

    .product-price-box {{
      background: #f8fafc;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}

    .price-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #b91c1c;
    }}

    .price-tax {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .product-features, .product-value-point {{
      font-size: 0.95rem;
      line-height: 1.6;
    }}

    .product-desc {{
      margin: 1.5rem 0;
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
    }}

    .desc-lead {{
      margin-bottom: 1rem;
      font-weight: 500;
    }}

    .product-advice-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }}

    @media (max-width: 640px) {{
      .product-advice-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .advice-box {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.9rem;
      line-height: 1.6;
    }}

    .target-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}

    .usage-box {{
      background: #fefce8;
      border: 1px solid #fef08a;
      color: #854d0e;
    }}

    .advice-title {{
      font-weight: 700;
      margin-bottom: 0.35rem;
    }}

    .product-cta {{
      text-align: center;
      margin-top: 1.5rem;
    }}

    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: #ffffff;
      font-weight: 700;
      font-size: 1rem;
      padding: 0.85rem 2rem;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 420px;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 12px -2px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #d60000, #aa0000);
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 2rem 0;
    }}

    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      background: #ffffff;
    }}

    .comparison-table th, .comparison-table td {{
      padding: 0.85rem 0.75rem;
      border: 1px solid var(--border-color);
      text-align: left;
    }}

    .comparison-table th {{
      background: #f8fafc;
      color: #0f172a;
      font-weight: 700;
      white-space: nowrap;
    }}

    .tbl-rank {{
      font-weight: 700;
      color: var(--primary-dark);
      white-space: nowrap;
      text-align: center;
    }}

    .tbl-name a {{
      color: #0f172a;
      text-decoration: none;
    }}

    .tbl-name a:hover {{
      color: var(--primary);
    }}

    .tbl-price {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin: 2rem 0;
    }}

    .faq-item {{
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1.25rem;
    }}

    .faq-q {{
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 0.5rem;
      display: flex;
      gap: 0.5rem;
    }}

    .faq-q-badge {{
      background: var(--primary);
      color: #ffffff;
      font-size: 0.75rem;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      height: fit-content;
    }}

    .faq-a {{
      color: #475569;
      font-size: 0.95rem;
      line-height: 1.7;
    }}

    .internal-links-box {{
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.5rem;
      margin-top: 3rem;
    }}

    .internal-links-title {{
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: #0f172a;
    }}

    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 0.75rem;
    }}

    .internal-link {{
      color: #047857;
      text-decoration: none;
      font-size: 0.85rem;
      padding: 0.4rem 0.6rem;
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      transition: all 0.2s;
    }}

    .internal-link:hover {{
      background: #d1fae5;
      border-color: #6ee7b7;
    }}

    .site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border-color);
      padding: 2rem 0;
      margin-top: 4rem;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav>
        <a href="/" style="text-decoration: none; color: #475569; font-size: 0.9rem; font-weight: 600;">TOPへ戻る</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <article class="article-wrap">
      <nav class="breadcrumb">
        <a href="/">ホーム</a> &gt; <span>高純度ワセリン高保湿ランク10</span>
      </nav>

      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！水分蒸発をゼロに抑えて冬の冷風から守り抜く高純度ワセリンランク10</h1>

      <div class="article-meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証カテゴリー: 高純度ワセリン・皮膚密封保護</span>
        <span>監修: 冬コスメ徹底比較ラボ 編集部</span>
      </div>

      <div class="lead-box">
        <strong>【11月・12月の極寒乾燥に！水分蒸発を物理的にシャットアウトする最強シールド】</strong><br>
        木枯らしが吹き荒れ、湿度が極限まで低下する11月〜12月。「どれほど高級な美容液や濃厚クリームを塗っても、暖房の風にさらされると数時間で肌が乾燥してパリパリになる」「粉吹きやひび割れで化粧水すらヒリヒリしみる」という経験はありませんか？<br><br>
        そんな真冬の極限乾燥から肌を救い出す最終兵器が<strong>『高純度ワセリン』</strong>です。ワセリンは肌内部に浸透せず、皮膚表面にとどまって強固な油膜を形成します。皮膚科学において「経表皮水分蒸散量（TEWL）を抑制する力」はあらゆる植物油や動物油を凌駕し、肌からの水分蒸散をほぼゼロに遮断します。<br><br>
        不純物を極限まで除いたサンホワイトP-1、医療用プロペト、大人気のベビーワセリン、ベタつきを解消したIHADA薬用バームまで、敏感肌でも安心して使える2026年最新の厳選10品を徹底比較・ランキング化しました。
      </div>

      <h2 class="section-title">🛡️ なぜワセリンは冬のスキンケアの「最後の砦」と呼ばれるのか？</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>ワセリンは石油から得られる炭化水素類の混合物を高度に精製した天然由来のミネラルオイルです。「石油由来」と聞くと刺激を心配される方もいますが、化学的に極めて安定しており不活性なため、酸化や変質が起こらず、アレルギー反応を起こすリスクが極めて低いのが最大の特徴です。冬の乾燥対策において以下の3つの圧倒的な強みを持ちます。</p>
        <ul style="margin: 1rem 0 1rem 1.5rem;">
          <li><strong>1. 経表皮水分蒸散（TEWL）の完全遮断：</strong> 肌表面に強固な疎水性フィルムを形成し、角層内の水分が外気へと逃げていくのを物理的に100%近くブロックします。</li>
          <li><strong>2. 外的刺激・アレルゲンの侵入阻止：</strong> 冬の冷たい外風、エアコンの温風、ホコリ、花粉、マスク摩擦などの物理的刺激が傷ついた角層に触れるのを防ぐバリアとなります。</li>
          <li><strong>3. 傷ついた素肌の自己修復環境づくり：</strong> 患部を密閉して潤った状態（湿潤環境）を保つことで、角層細胞のターンオーバーとバリア機能の自然回復を強力に後押しします。</li>
        </ul>
      </div>

      <h2 class="section-title">🏆 高純度ワセリン高保湿おすすめランキング10選</h2>

      {items_html}

      <h2 class="section-title">📊 高純度ワセリン10品 徹底スペック比較表</h2>
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名・容量</th>
              <th>種別・規格</th>
              <th>精製度・処方特徴</th>
              <th>参考価格</th>
            </tr>
          </thead>
          <tbody>
            {table_rows}
          </tbody>
        </table>
      </div>

      <h2 class="section-title">💡 べたつかない！冬のワセリンを快適に使いこなすプロのテクニック</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>「ワセリンはベタつくから苦手」という方の多くは、塗る量と塗り方に原因があります。ほんの少しの工夫で、ベタつきを最小限に抑えながら最高の保護効果を引き出すことができます。</p>
        <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; margin-top: 1rem;">
          <h3 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: #059669;">① 使用量は全顔で「米粒1粒分」が基本</h3>
          <p>ワセリンは伸びが良いため、たくさん塗る必要は全くありません。小豆大以上塗ってしまうとギトギト感やテカリの原因になります。まずは米粒半分〜1粒分から始め、手のひらで温めて透明なオイル状に溶かしてから使用してください。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #059669;">② 擦るのではなく「手のひらスタンプ塗り」</h3>
          <p>指先で肌を擦りながら伸ばそうとすると、肌に摩擦刺激を与えるだけでなくムラ付きの原因になります。両手のひらをすり合わせて薄膜を作った後、顔を優しく包み込むように手のひらを肌に密着（スタンプ）させて転写するのがプロの技です。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #059669;">③ 必ず「水分補給の後」に使う</h3>
          <p>ワセリン自体には肌に水分を与える作用はありません。洗顔後、化粧水や保湿美容液で水分をたっぷり補給した直後に、その水分を逃さないフタとしてワセリンを重ねてください。</p>
        </div>
      </div>

      <h2 class="section-title">❓ 専門家が答える！高純度ワセリンのよくある質問</h2>
      <div class="faq-list">
        {"".join([f'''
        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-badge">Q</span>
            <span>{f["q"]}</span>
          </div>
          <div class="faq-a">{f["a"]}</div>
        </div>
        ''' for f in faq_data])}
      </div>

      <div class="internal-links-box">
        <h3 class="internal-links-title">🔗 あわせて読みたい冬の高保湿スキンケア・コスメ特集</h3>
        <div class="internal-links-grid">
          <a href="/winter-heparinoid" class="internal-link">🧪 薬用ヘパリン類似物質コスメ10選</a>
          <a href="/winter-rice-power" class="internal-link">🌾 米発酵・ライスパワー高保湿10選</a>
          <a href="/winter-ceramide-cream" class="internal-link">🧴 高保湿セラミドクリーム10選</a>
          <a href="/winter-placenta" class="internal-link">✨ 高濃度プラセンタ原液10選</a>
          <a href="/winter-amino-acid" class="internal-link">💧 高浸透アミノ酸コスメ10選</a>
          <a href="/winter-squalane-oil" class="internal-link">✨ 高純度スクワランオイル10選</a>
          <a href="/winter-horse-oil" class="internal-link">🐴 高保湿馬油クリーム10選</a>
          <a href="/winter-shea-butter" class="internal-link">🧈 高保湿シアバター10選</a>
          <a href="/winter-argan-oil" class="internal-link">🥑 高保湿アルガンオイル10選</a>
          <a href="/winter-panthenol-cream" class="internal-link">🧪 高保湿パンテノールクリーム10選</a>
          <a href="/winter-urea-cream" class="internal-link">🦶 高保湿尿素クリーム10選</a>
          <a href="/winter-medicinal-lip" class="internal-link">💄 高保湿薬用リップクリーム10選</a>
          <a href="/winter-ceramide-lotion" class="internal-link">🧴 高保湿セラミド化粧水10選</a>
          <a href="/winter-peptide-serum" class="internal-link">🧬 高保湿ペプチド美容液10選</a>
        </div>
      </div>

    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved.</p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #94a3b8;">当サイトは楽天市場アフィリエイトプログラムに参加しており、適格販売により収入を得ています。</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-vaseline.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-vaseline.html!")
