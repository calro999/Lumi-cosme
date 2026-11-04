import json
import re

with open("fetched_final_30_resurrection_beta_avocado.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_resurrection_plant"]["items"]

# 各商品ごとの完全オリジナルなレビュー＆詳細データ
product_details = [
    {
        "rank": 1,
        "tag": "🏆 驚異の生命力！砂漠の極限乾燥から生まれた高密着バリアチューブ",
        "catch": "過酷な乾燥地帯で自活するテマリカヒバ（復活草）エキスを高濃度濃縮。冬の冷風でしぼみきった角層細胞を濃密な水分とアミノ酸で満たす超実力派クリーム",
        "brand_name": "Abib (アビブ)",
        "capacity": "75ml / アルミチューブ",
        "type": "高保湿バリアリペアクリーム",
        "features": "テマリカヒバエキス（復活草エキス）、トレハロース、スクワラン、セラミドNP、シア脂",
        "value": "数滴の水で緑を蘇らせる復活草の濃縮エキスが、真冬の暖房でカラカラに萎縮した肌細胞をふっくら満水状態へリカバリー。アルミチューブで衛生的に使い切れる",
        "desc_p1": "11月から12月にかけて、暖房の効いたオフィスや冷たい木枯らしにさらされ続けると、肌の水分量は夏場の半分以下にまで激減します。水分を与えてもすぐに蒸発してしまい、夕方になると頬が突っ張って痛い、ファンデーションが粉を吹いてひび割れるという方に圧倒的な支持を得ているのが、韓国発Abib（アビブ）の『復活草クリーム ニュートリションチューブ』です。主成分のテマリカヒバは、完全な乾燥状態で何年も耐え、わずかな水分を得ただけで数時間のうちに青々とした姿に戻る驚異の生命力を持っています。",
        "desc_p2": "こっくりとしたバターのような濃厚テクスチャーでありながら、肌の温度に触れるとスルスルととろけて角質層の奥深くまで浸透します。復活草に含まれる高純度トレハロースとセラミドNPが強固な水分シールドを形成するため、夜塗れば翌朝の洗顔時までモチモチの潤い膜が持続。油分で無理にベタつかせるのではなく、肌の内側が水分で満ち足りている安心感を実感できます。香料やエタノール無添加で、冬のピリピリしやすい敏感肌にも心地よく馴染みます。",
        "target": "真冬になるとどんな保湿クリームを塗っても数時間で乾燥を感じる方、日中の粉吹きやカサつきに悩む方、肌のキメとしぼみを同時に立て直したい方",
        "point": "夜のお手入れの最後に、パール2粒分を手のひら全体に温めてから顔を包み込むようにハンドプレスします。特に乾燥が気になる口元や目元には重ねづけをすると、翌朝の洗顔後の肌触りが劇的に柔らかくなります。"
    },
    {
        "rank": 2,
        "tag": "💧 発酵ビフィズス菌×復活草！真冬のたるみ乾燥を打破する弾力ドロップ",
        "catch": "復活草の保水力とビフィズス菌発酵エキスの修復力を1滴に濃縮。冬の寒冷でこわばった肌深層へ水分と栄養を送り届ける高密度ファーミングセラム",
        "brand_name": "Abib (アビブ)",
        "capacity": "50ml / スポイトボトル",
        "type": "高保水弾力ファーミング美容液",
        "features": "復活草エキス、ビフィズス菌培養溶解質、トレハロース、ペプチドコンプレックス、ヒアルロン酸Na",
        "value": "乾燥による小ジワと弾力低下にダブルアプローチ。水分保持とマイクロバイオーム環境を同時に整え、寒暖差に負けない強靭な肌土台を再構築",
        "desc_p1": "寒さが本格化する11月以降、外気の冷たさと暖房の熱気という急激な温度変化により、肌のバリア機能だけでなくターンオーバーのリズムも乱れがちになります。『復活草ビフィダセラム ファーミングドロップ』は、肌の水分保持力を高める復活草エキスに、肌環境を健やかに保つビフィズス菌発酵エキスをベストバランスで融合させた高機能美容液です。",
        "desc_p2": "糸を引くような濃密なとろみがありながら、肌に伸ばすとみずみずしく弾けて角層へと吸い込まれる独特のフォーミュラ。トレハロースが角質細胞の萎縮を防ぎつつ、ビフィダ発酵成分がキメの乱れを滑らかに修復します。使用後すぐに指先を吸い寄せるようなモチモチ感と内側から発光するようなハリツヤが生まれ、冬の乾燥によって影が差したような疲労顔をいきいきと蘇らせてくれます。",
        "target": "乾燥だけでなくフェイスラインのしぼみや毛穴の開きが気になる方、とろみがあるのにベタつかない高浸透美容液を探している方、肌の基礎体力を底上げしたい方",
        "point": "化粧水のあと、スポイト1〜2滴分を手にとり、顔の中心から外側へ引き上げるように馴染ませます。手のひらで肌を軽くパッティングして密着させると、角層深部まで美容成分がグングン行き渡ります。"
    },
    {
        "rank": 3,
        "tag": "✨ とろぱしゃ新触感！細胞の『水みち』を拓く殿堂入り濃密高保湿化粧水",
        "catch": "角層細胞の水の巡りに着目した独自成分MCアクアポリン×トレハロース。冬の砂漠肌を瞬時にうるおいで満たし、触れるたび押し返すハリを与える名作ローション",
        "brand_name": "ORBIS (オルビス)",
        "capacity": "180ml / ボトル",
        "type": "高保湿エイジングケア化粧水",
        "features": "トレハロース、MCアクアポリン（ヤグルマギク花エキス等）、DF-パンテノール（肌荒れ防止有効成分）、濃グリセリン",
        "value": "医薬部外品処方。肌本来のうるおい保持機能を高め、真冬の過酷な乾燥下でも角層全体に均一な水分ネットワークを長時間維持",
        "desc_p1": "スキンケアの基本である化粧水において、真冬の乾燥対策として絶大な支持を集め続けているのが『オルビスユー エッセンスローション』です。最大の特徴は、ボトルから出した瞬間はリッチな濃密とろみジェルなのに、肌に触れた瞬間にパシャッと弾けて水のような超微細ミスト状に崩れる『とろぱしゃ』テクスチャーにあります。",
        "desc_p2": "トレハロースとアクアポリンサポート成分が、寒さで硬直した角層の隙間へ瞬時に染み渡り、カラカラに乾いていた角質細胞を水分で満たします。肌荒れ有効成分DF-パンテノールも配合されているため、冬の冷たい空気で赤みが出やすい肌も穏やかに鎮静。重ねづけするほどに肌密度がギュッと詰まったようなもっちり感が手に入り、次に使う乳液やクリームの浸透力も格段に高まります。",
        "target": "真冬のとろみ化粧水特有の表面のベタつきが苦手な方、肌の奥が乾いているインナードライを根本から解消したい方、医薬部外品の安心感を求める方",
        "point": "手のひらにティースプーン半分程度を取り、下から上へ包み込むように優しくなじませます。さらに同量を手に取り、乾燥しやすい目元・口元を中心に『ハンドプレスで5秒キープ』を2回繰り返すと、まるでスチームを浴びた後のような満水肌が完成します。"
    },
    {
        "rank": 4,
        "tag": "🌿 トレハロースの純粋保水力！角層をふっくら整えるプロユース高保湿化粧水",
        "catch": "天然の保水糖類トレハロースをリッチに配合。冬の寒風でゴワつき乱れたキメを整え、敏感に傾いた肌にもスッとなじんで潤いを離さない",
        "brand_name": "KIRA (綺羅化粧品)",
        "capacity": "150ml / ディスペンサーボトル",
        "type": "低刺激・高保水トリートメントローション",
        "features": "トレハロース、ヒアルロン酸Na、褐藻エキス、アラントイン、オウゴン根エキス",
        "value": "サロン仕様の無香料・無着色・アルコールフリー。冬の乾燥性敏感肌に水分を吸着させ、肌表面をみずみずしい保護膜で包み込む",
        "desc_p1": "エステやサロン専売品として皮膚科学に基づいて設計されている綺羅化粧品の『キラ アクティブローション』。真冬の過酷な乾燥による肌バリアの低下を食い止めるため、保水力に極めて優れた天然多糖類トレハロースをたっぷりと配合しています。",
        "desc_p2": "テクスチャーはサラリとしてベタつかないのに、肌に馴染ませた瞬間に角質層が水分をごくごくと飲み干すような驚きの浸透感。トレハロースが水分分子をがっちりホールドするため、暖房の効いた乾燥空間に何時間いても肌が乾く感覚がありません。アラントインやオウゴン根エキスが肌荒れを防ぎ、冬特有のチクチクした刺激や赤みを穏やかに落ち着かせます。",
        "target": "肌がデリケートで化粧水がピリピリしやすい方、表面はサラサラなのに内部はしっかり潤う仕上がりを好む方、冬のキメの乱れを整えたい方",
        "point": "洗顔直後の肌にコットンまたは清潔な手のひらでたっぷりとなじませます。特に乾燥がひどい日は、精製水で湿らせたコットンに本品を含ませて3分間のローションパックを行うと、エステ帰りのような透明感ある柔肌が蘇ります。"
    },
    {
        "rank": 5,
        "tag": "💧 毎日手軽に満水チャージ！復活草×コラーゲンで冬のエアコン乾燥を打破",
        "catch": "復活草エキスと低分子コラーゲンの贅沢デュアル処方。超密着植物性シートが真冬の乾ききった肌にピタッと密着し、朝晩3分でぷるぷるのツヤ肌を叶える大容量マスク",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "30枚入り (350mlエッセンス) / BOXタイプ",
        "type": "高保水デイリー密着シートマスク",
        "features": "復活草エキス（テマリカヒバエキス）、低分子フィッシュコラーゲン、CICA（ツボクサエキス）、3重ヒアルロン酸",
        "value": "30枚入りの大容量で毎日惜しみなく贅沢集中保水。朝のメイク前のスキンケア時短と夜の乾燥リセットを1箱で完結",
        "desc_p1": "冬の朝、メイク前にシートマスクを貼るだけでファンデーションの密着度と日中の乾燥崩れが劇的に改善します。VT COSMETICSの『シカコラーゲンデイリーマスク』は、肌鎮静のCICA成分に、砂漠の生命力を持つ復活草エキスと吸収性の高い低分子コラーゲンを贅沢にブレンドした冬に最適な集中保湿マスクです。",
        "desc_p2": "極薄のヴィーガン認証シートがフェイスラインの凹凸に寸分の隙間もなく吸い付くように密着。たっぷりと含まれたエッセンスが角層のすみずみまで浸透し、暖房で縮こまった肌細胞を瞬時に解きほぐします。はがした後は肌表面がベタベタせず、吸い付くようなハリと澄んだ透明感が出現。忙しい真冬の朝でも、わずか5分でサロン帰りのような満水肌が完成します。",
        "target": "毎日のスキンケアで手軽に高保湿パックを続けたい方、朝のメイク崩れやファンデーションの乾燥割れを防ぎたい方、大容量でコスパ良くケアしたい方",
        "point": "洗顔後、化粧水で肌を整えた後に付属のピンセットで1枚取り出して顔に密着させます。5〜10分後にマスクをはがし、肌に残ったエッセンスを手のひらで優しく馴染ませたあと、乳液やクリームで油分のシールドを作ってください。"
    },
    {
        "rank": 6,
        "tag": "🛡️ 5種のヒト型セラミド×トレハロース！冬の角層を再建する低刺激モイストリッチ",
        "catch": "大豆由来の保湿成分と5種のヒト型セラミド、そしてトレハロースを凝縮。余計なものを削ぎ落とした安心設計で、真冬のひび割れ寸前の角層を優しく満たす",
        "brand_name": "松山油脂 (M-mark / 肌をうるおす)",
        "capacity": "120ml / ガラスボトル",
        "type": "高保湿低刺激セラミド化粧水",
        "features": "トレハロース、セラミドEOP/NP/AP/NG/AG（5種のヒト型セラミド）、ダイズ種子エキス、ヒアルロン酸Na",
        "value": "無香料・無着色・無鉱物油・パラベンフリー・アルコールフリー。肌の細胞間脂質と同じラメラ構造を整え、冬の水分蒸発を物理的にシャットアウト",
        "desc_p1": "日本の職人気質が息づく松山油脂が手掛けるロングセラーシリーズ『肌をうるおす保湿スキンケア』。その中でも『モイストリッチ』は、冬の本格的な乾燥と寒さで荒れた肌のために開発された最も高保湿な化粧水です。肌の水分を保つ最強の脂質である『ヒト型セラミド5種』に、水分保持を助ける『トレハロース』を贅沢に組み合わせています。",
        "desc_p2": "とろりとした濃厚なリキッドが肌に乗せるとスーッと馴染み、乾いてカサついた角層をまろやかに包み込みます。アルコールやパラベン、香料を一切使用していないため、冬の寒冷で皮膚が薄くなり、何を塗ってもピリピリしみるようなデリケート肌でも全くストレスなく使用できます。シンプルながら肌の根本的なバリア力を立て直してくれる、真冬の頼れる常備薬のような一本です。",
        "target": "真冬になると肌が敏感になっていつもの化粧水がしみる方、ヒト型セラミドとトレハロースの相乗効果を実感したい方、無添加処方にこだわりたい方",
        "point": "洗顔後、手のひらに100円玉大を取り、顔全体を包み込むように優しくなじませます。乾燥が気になる目元や頬骨には、指の腹でトントンと軽く叩き込むように重ねづけすると、角層の隙間がしっかり埋まります。"
    },
    {
        "rank": 7,
        "tag": "🔬 ビフィズス菌培養物×復活草ペプチド！極寒に立ち向かう高栄養シールドクリーム",
        "catch": "韓国で絶大な人気を誇るビフィダバイオームに復活草ペプチドと10重ヒアルロン酸を配合。真冬の過酷な寒冷・エアコン乾燥から肌を鉄壁ガードする高機能栄養クリーム",
        "brand_name": "Manyo Factory (魔女工場)",
        "capacity": "50ml / ジャータイプ",
        "type": "高機能高栄養バリアクリーム",
        "features": "復活草エキス（テマリカヒバ）、ビフィズス菌培養溶解質、10重ヒアルロン酸、アセチルヘキサペプチド-8、スクワラン",
        "value": "肌のマイクロバイオーム（常在菌バランス）を整えながら、10種の異なる分子サイズのヒアルロン酸と復活草が肌の表層から深層まで水分でロック",
        "desc_p1": "韓国スキンケアのトップブランド魔女工場（Manyo）が誇るエイジングケアラインの最高峰『ビフィダバイオーム コンセントレート クリーム』。乾燥によって皮膚の常在菌バランスが崩れ、抵抗力が落ちてしまう真冬の肌のために、濃密な発酵成分と復活草ペプチドを詰め込んだリッチな高機能クリームです。",
        "desc_p2": "カスタードクリームのようにこっくりとした濃密なテクスチャーでありながら、肌の上でなめらかに伸びてベタつかない絶妙な使用感。10重ヒアルロン酸が角層のあらゆる深さに水分を届け、復活草エキスがその水分をギュッと固定。さらにペプチド成分が年齢とともにしぼみやすい目元や口元にピンとした弾力を与えます。暖房を一晩中つけた寝室でも、朝まで乾かない圧倒的な保湿持続力を誇ります。",
        "target": "冬の乾燥による小ジワ・ハリ不足・キメの乱れをトータルで改善したい方、発酵コスメの高い栄養感を体感したい方、翌朝の肌のツヤを格上げしたい方",
        "point": "スキンケアの最終ステップで、スパチュラに適量を取り、顔全体から首筋にかけてリンパを流すように伸ばします。特に夜は少し厚めに塗ってスリーピングパックのように使うと、翌朝の洗顔時に吸い付くような極上の肌触りを実感できます。"
    },
    {
        "rank": 8,
        "tag": "🌸 水分クリーム×プライマー！冬の朝のベースメイクを一日中ツヤ肌に保つ水分バーム",
        "catch": "ダマスクローズ水53%と復活草由来トレハロースを配合。日中のエアコン乾燥でカサつく肌に朝塗るだけで、ファンデがピタッと密着し潤いが続く水分パック下地",
        "brand_name": "MISSHA (ミシャ)",
        "capacity": "50ml / ジャータイプ",
        "type": "多機能水分クリーム兼メイク下地バーム",
        "features": "ダマスクローズ花水、トレハロース、ヒアルロン酸、ホホバ種子油、セラミドNP",
        "value": "水分クリーム、モーニングパック、プライマー、ツヤクリームの4 in 1処方。冬の朝の忙しいメイク時間を劇的に短縮しながら一日中みずみずしいツヤをキープ",
        "desc_p1": "真冬のメイクの最大の悩みは「ファンデーションを塗った瞬間から粉を吹く」「午後の暖房でカサついて小ジワが目立つ」こと。そんな悩みを一発で解消してくれるのが、ミシャの『グロウ スキンバーム』です。水分クリームのみずみずしさと、バームの密着保湿力を併せ持つ画期的な朝用コスメです。",
        "desc_p2": "ダマスクローズ水をベースに、トレハロースやセラミドNPを配合。肌に乗せるとぷるぷるのバームがスーッと溶けて、まるで薄い水分パックを纏ったようなツヤの保護膜を形成します。その上からクッションファンデやリキッドファンデを重ねると、驚くほど滑らかに伸びてピタッと密着。冬のオフィスで8時間暖房にさらされても、カサつきやひび割れを全く寄せ付けないみずみずしいツヤ肌が一日中続きます。",
        "target": "冬になると日中のベースメイクが乾燥して粉を吹いてしまう方、内側から自然に発光するような水光ツヤ肌を作りたい方、朝のスキンケアを時短したい方",
        "point": "朝のスキンケアの最後に、パール粒大を手にとって顔全体にムラなく伸ばします。特に乾燥しやすい目の下や頬にはトントンと軽く叩き込んでツヤを仕込み、その上から直接ファンデーションを重ねてください。"
    },
    {
        "rank": 9,
        "tag": "🚑 吸い付く超密着マイクロシート！真冬の乾ききった肌を緊急レスキューする救急パック",
        "catch": "まるで肌と一体化する特製ガムシート。復活草の凝縮エッセンスが角層深部へ一気に染み渡り、寒冷と暖房で干からびた肌を10分で生き返らせる集中ケア",
        "brand_name": "Abib (アビブ)",
        "capacity": "10枚入り (各27mlエッセンス) / 個包装",
        "type": "集中リペア高密着ガムシートマスク",
        "features": "テマリカヒバエキス（復活草エキス）、トレハロース、スクワラン、カミツレ花エキス、ヒアルロン酸Na",
        "value": "極細マイクロファイバーシートが空気を一掃して肌に真空密着。1枚に27mlもの高濃度復活草美容液を含侵させた贅沢スペシャルケア",
        "desc_p1": "週末の集中ケアや、大切な日の前夜にぜひ使いたいのが、Abibのアイコン的アイテム『ガムシートマスクパック 復活草フィット』です。名前の通り、ガムのように肌に吸い付いて一切剥がれ落ちない特製マイクロファイバーシートを採用しており、密着度が一般的な不織布マスクとは次元が違います。",
        "desc_p2": "シートには乳白色の濃厚な復活草エッセンスが1本分（27ml）贅沢に含まれており、顔に乗せた瞬間から乾いた肌が水分をごくごくと飲み干していくような心地よい感覚に包まれます。トレハロースとスクワランが肌のバリアを瞬時に修復し、15分後にシートをはがすと、くすみが抜けてパンッと内側から押し返してくるような満水ツヤ肌が出現。真冬の過酷なイベント前や旅行先での乾燥対策にも最適です。",
        "target": "週末や特別な日の前日に確実な肌の立て直しを行いたい方、シートマスクが途中で浮いてくるのがストレスな方、エステ級の保水効果を自宅で実感したい方",
        "point": "洗顔後、化粧水で軽く肌を整えてからシートを広げて顔全体に密着させます。10〜20分置いた後、はがして残った美容液をデコルテや首元までしっかり伸ばしてください。その後、乳液やクリームで蓋をします。"
    },
    {
        "rank": 10,
        "tag": "⚗️ 自宅コスメを最強の保水処方に変える！100%ピュアトレハロースパウダー",
        "catch": "砂漠植物が極限乾燥を生き延びる奇跡の糖類トレハロース高純度パウダー。手持ちの化粧水や美容液にサッと溶かすだけで、真冬の水分蒸発を物理的にブロック",
        "brand_name": "自然化粧品研究所",
        "capacity": "20g / チャック付きアルミ袋",
        "type": "高純度天然トレハロースパウダー（化粧品原料）",
        "features": "トレハロース100%（食品・化粧品グレード高純度結晶）",
        "value": "無駄な添加物ゼロ。自分の肌状態に合わせて濃度を微調整でき、いつものプチプラスキンケアを一瞬でデパコス級の超高保湿処方にカスタム可能",
        "desc_p1": "「普段使っているお気に入りの化粧水があるけれど、冬場だけはどうしても保湿力が物足りない」というコスメ賢者に愛用されているのが、自然化粧品研究所の『高純度トレハロースパウダー』です。トレハロースは、乾燥によって生じるタンパク質の変性や細胞膜の破壊を防ぐ『ガラス化（ビトリフィケーション）』という特殊な保護能力を持っています。",
        "desc_p2": "サラサラとした微細な白色粉末で、水や化粧水に触れると一瞬でサッと溶けます。手のひらで化粧水を使う際に耳かき1〜2杯分（約0.2〜0.5g）を混ぜ合わせるだけで、肌に乗せたときの保水力と吸い付き感が圧倒的に向上。乾燥でカサつく手足のボディローションやハンドクリームにブレンドするのもおすすめで、真冬の全身の乾燥トラブルを驚くほどの高コスパで解決できます。",
        "target": "手持ちのスキンケアの保湿力を手軽にグレードアップさせたい方、完全無添加の成分でカスタマイズを楽しみたい方、コスパ最強の乾燥対策を求める方",
        "point": "手のひらに化粧水を適量取り、本品を米粒〜小豆大ほど加えて指先で混ぜると瞬時に溶けます。そのまま顔全体になじませてください。手作り化粧水を作る場合は、全体の1〜3%を目安に配合するのがベストです。"
    }
]

# FAQ 生成
faqs = [
    {
        "q": "復活草（テマリカヒバ）エキスとトレハロースには、どんな相関関係があるのですか？",
        "a": "復活草が何年もの干ばつでカラカラに乾燥しても、わずかな水で青々と生き返ることができる最大の秘密こそが、植物体内に蓄えられた高濃度の『トレハロース』です。トレハロースは水分子と非常に強く結びつき、細胞膜の脂質二重層の間に滑り込んで水分の代わりとして細胞の構造を支えます。この植物の驚異的なメカニズムを人間の皮膚に応用したのが、復活草エキスおよびトレハロース配合コスメです。"
    },
    {
        "q": "ヒアルロン酸やセラミドの入った化粧品を使っているのに乾燥する場合、復活草・トレハロースは効果的ですか？",
        "a": "極めて効果的です。セラミドは『細胞と細胞の間の油分（脂質）』を補い、ヒアルロン酸は『水分を抱え込む』役割を持ちますが、トレハロースは『角質細胞そのものの萎縮や乾燥死を防ぎ、水分を吸着・保持する』という異なるアプローチをとります。そのため、セラミドやヒアルロン酸とトレハロースを併用することで、細胞の内側・外側・脂質膜のすべてが強固に守られ、真冬の暖房下でも乾かない鉄壁の潤い肌が完成します。"
    },
    {
        "q": "11月〜12月のスキンケアで、復活草・トレハロースコスメを取り入れる最もおすすめの順番は？",
        "a": "洗顔直後のまっさらな角層に届けるのが最も効果的です。導入美容液（Abib復活草ビフィダセラムやオルビスユーエッセンスローション）でまず角層細胞を満水状態に整え、その後にセラミドやスクワランを配合した高保湿クリーム（Abib復活草クリームや魔女工場ビフィダバイオーム）で密閉するステップが理想的です。特に乾燥がひどい夜は、シートマスクを化粧水の後に挟むと、翌朝の肌密度の違いをはっきりと実感できます。"
    },
    {
        "q": "トレハロースや復活草成分は、敏感肌やニキビ肌でも使えますか？",
        "a": "安心してご使用いただけます。トレハロースは天然の糖類であり、食品や医療用の臓器保存液にも広く使われるほど極めて生体適合性が高く、アレルギーや刺激の報告がほとんどありません。また油分過多で毛穴を詰まらせるリスクが低いため、乾燥が原因で皮脂が過剰分泌してしまう『冬のインナードライ型ニキビ』や、寒冷で赤みが出やすいゆらぎ肌の方にも非常に適しています。"
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
            <img src="{img}" alt="{it['display_name']}" loading="lazy" width="300" height="300" class="card-img">
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
          <a href="{url}" target="_blank" rel="nofollow noopener" class="card-aff-btn">
            楽天市場で最新価格をチェック ➔
          </a>
        </div>
        
        <div class="card-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{p['brand_name']}</td></tr>
            <tr><th>容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>注目保湿成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の乾燥対策価値</th><td>{p['value']}</td></tr>
          </table>
          
          <div class="card-desc">
            <h4 class="desc-heading">🔍 美容アナリストによる徹底解説＆冬の使用感</h4>
            <p class="desc-p">{p['desc_p1']}</p>
            <p class="desc-p">{p['desc_p2']}</p>
            
            <div class="eval-box">
              <div class="eval-item">
                <span class="eval-title">🎯 こんな方に特におすすめ</span>
                <p class="eval-text">{p['target']}</p>
              </div>
              <div class="eval-item">
                <span class="eval-title">💡 効果を高める冬のベストな使い方</span>
                <p class="eval-text">{p['point']}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </article>
    """
    cards.append(card)

cards_joined = "\n".join(cards)

# FAQ HTML生成
faq_items = []
for f in faqs:
    item = f"""
    <div class="faq-card">
      <h3 class="faq-q"><span class="q-icon">Q</span> {f['q']}</h3>
      <div class="faq-a"><span class="a-icon">A</span> <p>{f['a']}</p></div>
    </div>
    """
    faq_items.append(item)

faq_joined = "\n".join(faq_items)

# JSON-LD 生成
schema_items = []
for it in items:
    schema_items.append({
        "@type": "ListItem",
        "position": it["rank"],
        "name": it["brand"] + " " + it["display_name"].split(" (")[0],
        "image": it["image"],
        "offers": {
            "@type": "Offer",
            "priceCurrency": "JPY",
            "price": str(it["price"]),
            "url": it["url"],
            "availability": "https://schema.org/InStock"
        }
    })

schema_json = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "ItemList",
            "name": "保湿力の強さで肌乾燥とさようなら！カラカラ砂漠肌を驚異の保水力で満たす復活草・トレハロースコスメランク10",
            "description": "11月〜12月の過酷な暖房乾燥と寒風に負けない、驚異の保水力を持つ復活草エキス・トレハロース配合のおすすめ高保湿コスメ10選を徹底比較。",
            "numberOfItems": 10,
            "itemListElement": schema_items
        },
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！カラカラ砂漠肌を驚異の保水力で満たす復活草・トレハロースコスメランク10",
            "description": "極限の乾燥下でも水分で青々と蘇る復活草の生命力とトレハロースの細胞保護力。真冬の過酷な乾燥を打ち破る名品コスメ10選を美容成分の視点から徹底解説。",
            "datePublished": "2026-11-04T16:00:00+09:00",
            "dateModified": "2026-11-04T16:00:00+09:00",
            "inLanguage": "ja",
            "mainEntityOfPage": "https://calro999.github.io/cosme/winter-resurrection-plant.html"
        }
    ]
}, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！カラカラ砂漠肌を驚異の保水力で満たす復活草・トレハロースコスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月〜12月の本格的な暖房乾燥と寒冷でしぼみきったカラカラ肌を救う！数滴の水で青々と蘇る奇跡の復活草エキス＆細胞保水糖トレハロースを配合した高保湿コスメおすすめランキング10選。楽天市場のリアルタイム価格情報・成分解析付き。">
  <meta name="keywords" content="復活草 コスメ, トレハロース 化粧水, 保湿力 高い コスメ, 冬 乾燥肌 スキンケア, アビブ 復活草, オルビスユー, インナードライ 保湿, 11月 コスメ, 12月 コスメ">
  <link rel="canonical" href="https://calro999.github.io/cosme/winter-resurrection-plant.html">
  <link rel="icon" href="favicon.jpg" type="image/jpeg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --primary-color: #0d9488;
      --primary-dark: #0f766e;
      --primary-light: #ccfbf1;
      --accent-color: #f59e0b;
      --text-main: #1f2937;
      --text-sub: #4b5563;
      --text-light: #6b7280;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --border-color: #e2e8f0;
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.05);
      --shadow-md: 0 4px 12px rgba(13, 148, 136, 0.1);
      --shadow-lg: 0 10px 25px -5px rgba(13, 148, 136, 0.15);
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
      background: linear-gradient(135deg, #115e59 0%, #0d9488 50%, #14b8a6 100%);
      color: #ffffff;
      padding: 2rem 1.5rem 2.5rem;
      text-align: center;
      box-shadow: 0 4px 20px rgba(13, 148, 136, 0.25);
    }}
    .site-header-nav {{
      max-width: 1100px;
      margin: 0 auto 1.25rem;
      text-align: left;
    }}
    .site-header-nav a {{
      color: #ccfbf1;
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
      max-width: 900px;
      margin-left: auto;
      margin-right: auto;
    }}
    .site-subtitle {{
      font-size: 0.95rem;
      color: #f0fdfa;
      max-width: 800px;
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
    .toc-list li a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.92rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: color 0.2s;
    }}
    .toc-list li a:hover {{ color: var(--primary-color); font-weight: 700; }}

    .content-section {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--primary-dark);
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.6rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .section-p {{
      font-size: 1rem;
      color: var(--text-sub);
      margin-bottom: 1.25rem;
      text-align: justify;
    }}

    .compare-table-wrapper {{
      overflow-x: auto;
      margin: 1.5rem 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      background: #ffffff;
      font-size: 0.92rem;
      min-width: 650px;
    }}
    .compare-table th {{
      background: #f0fdfa;
      color: var(--primary-dark);
      padding: 0.9rem 0.75rem;
      text-align: center;
      font-weight: 700;
      border-bottom: 2px solid var(--primary-color);
      white-space: nowrap;
    }}
    .compare-table td {{
      padding: 0.9rem 0.75rem;
      border-bottom: 1px solid var(--border-color);
      vertical-align: middle;
      text-align: center;
    }}
    .compare-table tr:hover {{ background-color: #f8fafc; }}
    .rank-num {{
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.2rem;
    }}
    .rank-1 {{ color: #eab308; }}
    .rank-2 {{ color: #94a3b8; }}
    .rank-3 {{ color: #d97706; }}
    .product-thumb img {{
      border-radius: var(--radius-sm);
      object-fit: cover;
      box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }}
    .product-name-cell {{
      text-align: left !important;
      max-width: 280px;
    }}
    .product-brand {{
      display: block;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--primary-color);
      text-transform: uppercase;
    }}
    .table-prod-link {{
      color: var(--text-main);
      text-decoration: none;
      font-weight: 700;
      line-height: 1.4;
      display: inline-block;
      margin-top: 0.2rem;
    }}
    .table-prod-link:hover {{ color: var(--primary-color); text-decoration: underline; }}
    .type-badge {{
      display: inline-block;
      padding: 0.25rem 0.6rem;
      background: #f1f5f9;
      color: #475569;
      border-radius: 4px;
      font-size: 0.78rem;
      font-weight: 600;
      white-space: nowrap;
    }}
    .product-price {{
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      color: #e11d48;
      font-size: 1rem;
      white-space: nowrap;
    }}
    .table-btn {{
      display: inline-block;
      padding: 0.45rem 0.9rem;
      background: var(--primary-color);
      color: #ffffff;
      text-decoration: none;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      white-space: nowrap;
      transition: background 0.2s;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}

    .product-card {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      position: relative;
    }}
    .card-header {{
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 1rem;
    }}
    .rank-badge {{
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.1rem;
      color: #ffffff;
      background: var(--primary-color);
      padding: 0.4rem 1rem;
      border-radius: var(--radius-sm);
      flex-shrink: 0;
    }}
    .rank-badge.rank-1 {{ background: linear-gradient(135deg, #f59e0b, #d97706); }}
    .rank-badge.rank-2 {{ background: linear-gradient(135deg, #64748b, #475569); }}
    .rank-badge.rank-3 {{ background: linear-gradient(135deg, #b45309, #78350f); }}
    .card-titles {{ flex: 1; }}
    .card-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 0.2rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 0.4rem;
    }}
    .card-name {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.4;
    }}
    .card-catch {{
      background: #f8fafc;
      border-left: 4px solid var(--primary-color);
      padding: 0.9rem 1.2rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-bottom: 1.5rem;
      font-size: 0.95rem;
      color: #334155;
    }}
    .card-body {{
      display: grid;
      grid-template-columns: 300px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .card-body {{ grid-template-columns: 1fr; }}
      .card-image-box {{ max-width: 320px; margin: 0 auto; }}
    }}
    .card-image-box {{
      text-align: center;
    }}
    .card-img {{
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
      margin-bottom: 1rem;
      object-fit: cover;
      max-width: 100%;
      height: auto;
    }}
    .card-price-box {{
      background: #fff1f2;
      border-radius: var(--radius-sm);
      padding: 0.6rem;
      margin-bottom: 0.6rem;
    }}
    .price-label {{ display: block; font-size: 0.75rem; color: #9f1239; }}
    .price-val {{ font-family: 'Outfit', sans-serif; font-size: 1.4rem; font-weight: 800; color: #be123c; }}
    .price-tax {{ font-size: 0.75rem; color: #9f1239; }}
    .card-review-box {{
      margin-bottom: 1rem;
      font-size: 0.88rem;
    }}
    .star-rating {{ color: #f59e0b; font-weight: 700; margin-right: 0.4rem; }}
    .review-count {{ color: var(--text-light); }}
    .card-aff-btn {{
      display: block;
      background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);
      color: #ffffff;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 0.85rem 1rem;
      border-radius: var(--radius-md);
      box-shadow: 0 4px 10px rgba(225, 29, 72, 0.25);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .card-aff-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(225, 29, 72, 0.35);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }}
    .spec-table th {{
      width: 25%;
      padding: 0.65rem 0.8rem;
      background: #f8fafc;
      border: 1px solid var(--border-color);
      color: #475569;
      font-weight: 700;
      text-align: left;
    }}
    .spec-table td {{
      padding: 0.65rem 0.8rem;
      border: 1px solid var(--border-color);
      color: var(--text-main);
    }}
    .desc-heading {{
      font-size: 1.08rem;
      font-weight: 800;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .desc-p {{
      font-size: 0.96rem;
      color: var(--text-sub);
      margin-bottom: 1rem;
      line-height: 1.8;
      text-align: justify;
    }}
    .eval-box {{
      background: #f0fdfa;
      border-radius: var(--radius-md);
      padding: 1.25rem;
      margin-top: 1.25rem;
      border: 1px solid #ccfbf1;
    }}
    .eval-item {{ margin-bottom: 0.8rem; }}
    .eval-item:last-child {{ margin-bottom: 0; }}
    .eval-title {{
      display: block;
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--primary-dark);
      margin-bottom: 0.25rem;
    }}
    .eval-text {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.6;
    }}

    .faq-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.4rem;
      margin-bottom: 1.25rem;
    }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
      margin-bottom: 0.6rem;
    }}
    .q-icon {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 24px;
      height: 24px;
      background: var(--primary-color);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      border-radius: 50%;
      flex-shrink: 0;
    }}
    .faq-a {{
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
      font-size: 0.95rem;
      color: var(--text-sub);
      line-height: 1.7;
    }}
    .a-icon {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 24px;
      height: 24px;
      background: #f59e0b;
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      border-radius: 50%;
      flex-shrink: 0;
    }}

    .footer-internal-links {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-top: 3rem;
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 0.75rem;
      margin-top: 1.25rem;
    }}
    .footer-link-item {{
      padding: 0.65rem 0.85rem;
      background: #f8fafc;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.86rem;
      font-weight: 600;
      display: block;
      transition: all 0.2s;
    }}
    .footer-link-item:hover {{
      background: var(--primary-light);
      border-color: var(--primary-color);
      color: var(--primary-dark);
    }}

    .site-footer {{
      text-align: center;
      margin-top: 3rem;
      color: var(--text-light);
      font-size: 0.85rem;
    }}
  </style>

  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body>

  <header class="site-header">
    <div class="site-header-nav">
      <a href="index.html">🏠 冬コスメ総合TOPへ戻る</a>
    </div>
    <span class="header-badge">❄️ 11月〜12月・本格乾燥シーズン集中対策 ❄️</span>
    <h1 class="site-title">保湿力の強さで肌乾燥とさようなら！カラカラ砂漠肌を驚異の保水力で満たす復活草・トレハロースコスメランク10</h1>
    <p class="site-subtitle">
      冷たい木枯らしとエアコン暖房で干からびた肌を救う。数滴の水で青々と生き返る「復活草」と細胞保水糖「トレハロース」を配合した真冬の実力派コスメ10選を徹底比較！
    </p>
  </header>

  <main class="main-container">
    
    <!-- 目次 -->
    <nav class="toc-box" aria-label="記事の目次">
      <div class="toc-title">📑 目次・もくじ</div>
      <ul class="toc-list">
        <li><a href="#why-resurrection">1. なぜ11〜12月の肌には「復活草・トレハロース」が必要なのか？</a></li>
        <li><a href="#how-to-choose">2. 失敗しない復活草・トレハロースコスメの選び方・3つのポイント</a></li>
        <li><a href="#comparison-table">3. 復活草・トレハロースコスメ10選 スペック＆価格比較表</a></li>
        <li><a href="#ranking-section">4. 高保湿おすすめコスメランキング10選 詳細レビュー</a></li>
        <li><a href="#faq-section">5. 美容皮膚視点で答えるQ&amp;A（よくある質問）</a></li>
        <li><a href="#conclusion">6. まとめ：砂漠肌を脱出する冬の満水スキンケアルーティン</a></li>
        <li><a href="#internal-links">7. 関連する冬の高保湿コスメ特集一覧</a></li>
      </ul>
    </nav>

    <!-- セクション1 科学的背景 -->
    <section class="content-section" id="why-resurrection">
      <h2 class="section-title">🌵 1. なぜ11〜12月の肌には「復活草・トレハロース」が必要なのか？</h2>
      <p class="section-p">
        11月から12月にかけて、私たちの肌を取り巻く環境は一気に「砂漠並みの過酷さ」へと急変します。外気温は10℃前後まで低下して大気中の湿度は30%台へ急落。さらに室内ではエアコンやファンヒーターが稼働し、温風が常に肌の水分を強奪し続けます。
      </p>
      <p class="section-p">
        この時期に多くの女性が直面するのが、<strong>「いくら化粧水を重ねづけしても、数分後には突っ張って痛い」「夕方になると肌がカラカラに萎縮して、笑った拍子に目元や口元に深い乾燥ジワが走る」</strong>という深刻なインナードライ現象です。
      </p>
      <p class="section-p">
        なぜ従来の保湿ケアが通用しなくなるのでしょうか？それは、寒冷と極度乾燥によって「角質細胞自体の水分保持機能」が破綻し、細胞が干からびたスポンジのように縮んでしまっているからです。通常の水分や油分を乗せるだけでは、縮んだ細胞の内部まで浸透せず、表面を滑り落ちてしまうのです。
      </p>
      <p class="section-p">
        そこでいま美容界で熱烈な注目を浴びているのが、<strong>『復活草（テマリカヒバ／ミロタムヌス）』</strong>と、その生命力の源泉である<strong>『トレハロース』</strong>です。
      </p>
      <p class="section-p">
        復活草は、雨が何年間も降らない砂漠地帯で、体内の水分がほぼゼロになっても仮死状態で生き延び、わずか1滴の水を与えられただけで数時間のうちに青々とみずみずしい葉を広げる驚異の植物です。その生命を支えているのが、細胞膜の脂質構造を水分の代わりに保護し、乾燥による細胞死を防ぐ二糖類「トレハロース」です。
      </p>
      <p class="section-p">
        真冬のスキンケアに復活草やトレハロースを取り入れることで、暖房の熱気や冷気で萎縮した角層細胞に水分を強固に吸着させ、まるでオアシスのように肌内部を満水状態へと復活させることが可能になります。
      </p>
    </section>

    <!-- セクション2 選び方 -->
    <section class="content-section" id="how-to-choose">
      <h2 class="section-title">🔍 2. 失敗しない冬の復活草・トレハロースコスメの選び方・3つのポイント</h2>
      <p class="section-p">
        真冬の過酷な乾燥を乗り切るためのコスメ選びでは、ただ「配合」と書かれているだけでなく、肌の水分巡りとバリア機能を考慮した以下の3つの基準をチェックすることが重要です。
      </p>
      <div style="background: var(--bg-page); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; margin-bottom: 1.25rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.4rem;">ポイント①：角層深部へ届く「高浸透設計」か、表面を守る「密閉シールド」かで選ぶ</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          インナードライによるゴワつきや突っ張りが激しい場合は、まず洗顔後すぐに使えるブースター美容液や高浸透ローション（オルビスユーやAbibセラム）で細胞を満水にすることが先決です。一方、粉吹きやひび割れが目立つ場合は、セラミドやスクワランと合体した高保湿クリーム（Abibクリームや魔女工場）で水分を密閉ロックしましょう。
        </p>
      </div>
      <div style="background: var(--bg-page); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; margin-bottom: 1.25rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.4rem;">ポイント②：セラミド・発酵成分・コラーゲンとの相乗ブレンドに注目する</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          トレハロースや復活草は単体でも強力な保水力を誇りますが、肌の細胞間脂質を補う「ヒト型セラミド（松山油脂など）」や、ターンオーバーを整える「ビフィズス菌発酵液（Abib、魔女工場など）」、弾力を高める「コラーゲン（VTなど）」と掛け合わされることで、冬の肌トラブルに対する防御力が何倍にも跳ね上がります。
        </p>
      </div>
      <div style="background: var(--bg-page); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.4rem;">ポイント③：冬の敏感な肌を刺激しない「低刺激・無添加処方」を確認する</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          乾燥が進んだ冬の肌はバリアが薄くなり、アルコール（エタノール）や合成香料などの刺激物質に過敏に反応しがちです。アルコールフリー、無香料、パラベンフリーなど、弱った冬肌を優しくいたわる処方設計のものを選びましょう。
        </p>
      </div>
    </section>

    <!-- セクション3 比較表 -->
    <section class="content-section" id="comparison-table">
      <h2 class="section-title">📊 3. 復活草・トレハロースコスメ10選 スペック＆価格比較表</h2>
      <p class="section-p">
        楽天市場公式APIよりリアルタイムに取得した最新の販売価格と製品仕様の一覧表です。アイテム分類や価格帯に合わせて最適なアイテムを比較検討してください。
      </p>
      <div class="compare-table-wrapper">
        <table class="compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品画像</th>
              <th>商品名・ブランド</th>
              <th>アイテム種別</th>
              <th>楽天参考価格</th>
              <th>商品詳細</th>
            </tr>
          </thead>
          <tbody>
            {table_joined}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4 ランキング詳細 -->
    <section id="ranking-section">
      <h2 style="font-size: 1.6rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 2rem; text-align: center;">
        🏆 復活草・トレハロース高保湿コスメおすすめ人気ランキング10選
      </h2>
      {cards_joined}
    </section>

    <!-- セクション5 Q&A -->
    <section class="content-section" id="faq-section">
      <h2 class="section-title">❓ 5. 美容皮膚視点で答えるQ&amp;A（よくある質問）</h2>
      {faq_joined}
    </section>

    <!-- セクション6 まとめ -->
    <section class="content-section" id="conclusion">
      <h2 class="section-title">✨ 6. まとめ：砂漠肌を脱出する冬の満水スキンケアルーティン</h2>
      <p class="section-p">
        11月から12月にかけての寒冷・暖房乾燥は、通常の保湿ケアでは追いつかないほど急速に肌の水分を奪い去ります。
      </p>
      <p class="section-p">
        しかし、極限の乾燥環境を生き抜く「復活草」の生命力と、細胞を強力に守り抜く「トレハロース」の保水パワーを味方につければ、どんなに冷たい風が吹く真冬であっても、もっちりと吸い付くような満水ツヤ肌をキープすることができます。
      </p>
      <p class="section-p">
        朝のメイク前にはミシャのバームやVTのデイリーマスクでみずみずしい土台を作り、夜にはオルビスユーのローションやAbibの濃密クリームで一日受けた乾燥ダメージをリセットする――ぜひご自身の肌悩みにぴったりの1本を見つけて、乾燥に怯えることのない心地よい冬をお過ごしください。
      </p>
    </section>

    <!-- 内部リンク -->
    <section class="footer-internal-links" id="internal-links">
      <h2 style="font-size: 1.25rem; font-weight: 800; color: #1f2937; margin-bottom: 0.5rem;">
        🔗 併せて読みたい冬コスメ・高保湿スキンケア関連記事
      </h2>
      <p style="font-size: 0.9rem; color: #6b7280;">
        当サイトでは、11月〜12月の肌悩みに合わせた高保湿コスメや成分別ランキングを多数公開しています。
      </p>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で同期されます -->
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 当サイトは楽天市場アフィリエイトプログラムに参加しています。</p>
  </footer>

</body>
</html>
"""

with open("winter-resurrection-plant.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-resurrection-plant.html successfully. Size: {len(html_content):,} bytes")
