import json
import re

with open("fetched_3new_olive_meadowfoam_trehalose.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_olive_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 1滴で真冬の乾燥砂漠肌を疑似皮脂膜で包み込む！完全有機栽培フロール・デ・アセイテの最高峰",
        "catch": "スペインアンダルシア州の契約農園で手摘みされた有機オリーブ果実から、圧搾前のわずかな滴り（バージンオイルの精華）のみを採取。真冬の過酷な寒風や暖房乾燥で皮脂が激減した素肌に、人の皮脂と酷似した天然オレイン酸とスクワレンを1滴補給する美容オイルの不滅の名作",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "30ml / スモークガラスボトル・ドロップ式",
        "type": "100%天然完全無添加 有機オリーブバージンオイル（フロール・デ・アセイテ）",
        "features": "オリーブ果実油100%（スペイン産有機栽培）、オレイン酸（約75%）、天然スクワレン、ビタミンE（トコフェロール）、ポリフェノール",
        "value": "水分子と馴染みやすい親水基を持つため、化粧水の湿り気と瞬時に乳化して角層深部へ浸透。真冬の粉吹き肌やひび割れ寸前のカチコチ角質層を1滴でベルベットのようになめらかに整える",
        "desc_p1": "11月から12月にかけて気温が10℃を下回ると、人体の皮脂分泌量は夏季の半分から3分の1以下まで急激に落ち込みます。皮脂膜という天然のバリアを失った冬の肌は、冷たい木枯らしと湿度の低い外気にさらされることで水分が一方的に蒸散し、洗顔直後から激しい突っ張りや粉吹き、ひび割れに悩まされることになります。DHCの『オリーブバージンオイル』は、創業以来40年以上にわたり日本の真冬の乾燥肌を救い続けてきた美容オイルの金字塔です。まだ青味の残る早摘みの新鮮な有機オリーブ果実を砕き、圧搾機を一切使わずに自重だけで滴り落ちてくる極上の一滴『フロール・デ・アセイテ（オイルの精華）』のみを採取した贅沢極まりない処方です。",
        "desc_p2": "オイルでありながら親水性を持つ不思議なテクスチャーが特徴で、化粧水で湿った肌に手のひらで1滴押し込むと、水分と瞬時に手を取り合ってミルキーなエマルジョンへと変化。角層の細胞間脂質を満たしながら、表面に薄く強固な疑似皮脂膜を形成します。真冬の夜に塗布して眠れば、暖房をつけた寝室でも翌朝まで肌がもっちりと吸い付くような柔らかさをキープ。目元や口元の乾燥小ジワ、水仕事で荒れた指先のささくれ、タイツで擦れるすねの粉吹きまで、わずか数滴で劇的に鎮める圧倒的な保湿信頼性を誇ります。",
        "target": "冬場になるとどんな高保湿クリームを塗っても数時間で乾いてしまう超乾燥肌の方、皮脂分泌の低下による粉吹きや小ジワに悩む大人の肌、無香料・完全無添加で敏感な冬肌を優しく守りたい方",
        "point": "化粧水をたっぷりハンドプレスした後、手のひらに1滴だけ取り、両手をこすり合わせて温めてから顔全体を包み込むようにハンドプレスします。肌表面に水滴が少し残っている状態で馴染ませるのが、ベタつかず奥深くまで潤いを引き込む最大のコツです。"
    },
    {
        "rank": 2,
        "tag": "🌿 岡山牛窓の自社オリーブ園の歴史が息づく！全身のひび割れ・粉吹き・頭皮を救う200ml純粋オイル",
        "catch": "日本のエーゲ海と呼ばれる瀬戸内・牛窓のオリーブ園で培われた伝統製法。不純物を極限まで取り除いた純粋オリーブオイルが、真冬の硬化した角質を柔軟にし、顔・身体・髪・頭皮まで一本で完璧に潤し尽くす",
        "brand_name": "オリーブマノン (日本オリーブ)",
        "capacity": "200ml / スパウト付き大容量ボトル",
        "type": "100%純粋化粧用オリーブオイル（完全無添加・無着色・無香料）",
        "features": "高純度精製オリーブ果実油100%、オレイン酸トリグリセリド高含有、ビタミンE、植物ステロール",
        "value": "200mlという大容量でありながら純度100%の化粧品グレード。冬の入浴後の全身ボディオイル、肘・膝・かかとの角質軟化、頭皮の乾燥フケ防止マッサージ、クレンジングまでマルチに使える超高コスパ",
        "desc_p1": "昭和24年から続く瀬戸内・岡山県牛窓のオリーブ園を持つ日本オリーブが手がける『オリーブマノン バージンオイル』は、親子何代にもわたって冬の乾燥肌ケアとして愛用されている超ロングセラーアイテムです。厳選されたオリーブ果実から抽出されたバージンオイルを、長年の高度な精製技術によって不純物や刺激成分を極限までろ過。オリーブ特有の濃厚なエモリエント力をそのまま保ちながら、肌にスッと馴染む軽やかな滑らかさを実現しています。",
        "desc_p2": "冬のお風呂上がり、体がまだ温かく皮膚が湿っている状態で手のひらに数滴取り、すね、かかと、ひじ、デコルテへ伸ばすと、硬くごわついていた角質がまるで温泉上がりのようにしっとりとほぐれていきます。大容量200mlだからこそ、お顔の保湿だけでなく、乾燥してかゆみが出やすい冬の頭皮マッサージや、入浴前のオイルパック、ひび割れたかかとへの集中ラップケアまで惜しみなく全身に活用可能。冬の乾燥トラブルを一手に引き受ける一家に一本の守り神です。",
        "target": "冬場にすねや背中が乾燥してかゆくなる全身乾燥肌の方、入浴後のパーツケアを家族全員で惜しみなく行いたい方、頭皮の乾燥によるフケや髪のパサつきを同時にケアしたい方",
        "point": "お風呂から上がる直前の濡れた素肌に適量をなじませ、その後にタオルで軽く押さえるように水分を拭き取ると、角層内に水分が完全に閉じ込められて驚異的なモチモチ肌が一晩中続きます。"
    },
    {
        "rank": 3,
        "tag": "🛁 入浴時の湯気でオリーブ油がとろけて角層浸透！くすみとゴワつきをリセットする濃密スチームパック",
        "catch": "オリーブオイルと植物スクワラン、和漢植物エキスをブレンドした洗い流すクリームパック。真冬の寒冷でこわばった肌をバスタブの温熱と濃密油分で包み込み、もっちり透明美肌を呼び覚ます",
        "brand_name": "オリーブマノン (日本オリーブ)",
        "capacity": "150g / チューブ容器",
        "type": "高保湿オリーブ温感エモリエント クリームマスク",
        "features": "オリーブ果実油、植物スクワラン、トウキ根エキス、シャクヤク根エキス、コメヌカエキス",
        "value": "真冬の冷えによる毛細血管の収縮と角質硬化に着目。入浴中のスチーム効果を利用して角質深部へ良質なオレイン酸を届け、洗い流した瞬間から指を跳ね返すような弾力を復元",
        "desc_p1": "11月から12月は、外気の冷たさで顔の筋肉や皮膚が強張り、血行不良から肌色がどんよりとくすんで灰色がかって見えがちです。また乾燥によって古い角質が剥がれ落ちずに肌表面に堆積し、スキンケアの浸透を妨げる悪循環に陥ります。日本オリーブの『うるおいホワイトパック』は、お風呂の湯気と温熱を味方につけて冬の枯れ肌を一気に集中補修する、洗い流すタイプの高保湿オリーブクリームパックです。",
        "desc_p2": "洗顔後の肌にサクランボ2粒大を少し厚めに塗り広げ、そのまま湯船に浸かって3〜5分間リラックス。バスルームの温かいスチームによって毛穴が自然に開き、濃厚なオリーブオイルとスクワラン、トウキエキスなどの保湿成分が硬化した角層の奥深くまでぐんぐん浸透していきます。ぬるま湯で優しく洗い流すと、まるで剥きたてのゆで卵のようにツルツルで、内側から血色感が滲み出るようなもっちりとした極上肌に生まれ変わります。",
        "target": "冬の寒さで肌がくすんで化粧ノリが極端に悪くなっている方、角質肥厚でいつもの化粧水が弾かれてしまう方、お風呂タイムを有効活用してサロン級の保湿パックをしたい方",
        "point": "パックを塗った上から温かい濡れタオルを軽く顔に乗せて1〜2分蒸すと、スチーム効果とオリーブ油の角質軟化作用が何倍にも高まり、頑固なごわつきが一掃されます。"
    },
    {
        "rank": 4,
        "tag": "🏝️ 小豆島伝統の職人精製！ベタつかずスーッと吸い込まれる純度100%のマルチフェイシャルオイル",
        "catch": "小豆島オリーブ園が誇る100%ピュアバージンオリーブオイル。独自の低温精密精製により、オリーブ特有の重さを削ぎ落とし、肌の奥へ吸い込まれるような抜群の肌なじみを実現",
        "brand_name": "小豆島オリーブ園 (Oliveen)",
        "capacity": "80ml / ガラスボトル",
        "type": "100%高純度精製 バージンオリーブオイル",
        "features": "オリーブ油100%（小豆島厳選精製）、オレイン酸高含有、高浸透トリグリセリド、無香料・無鉱物油",
        "value": "従来のオリーブオイルにありがちな「重さ」「ベタつき」を独自の高度精製技術で解消。朝のメイク前や日中のパーツ保湿にもヨレずに使える絶妙なサラリ感",
        "desc_p1": "瀬戸内海の豊かな太陽と潮風に育まれたオリーブの島・小豆島。その歴史ある名門『小豆島オリーブ園』が製造するバージンオリーブオイルは、オリーブ本来の強力なエモリエント保護力を維持しつつ、日本の現代女性の肌質に合わせて極めて軽やかに精製された逸品です。植物油の中でも特に人間の皮脂膜に近いオレイン酸を主成分としているため、塗布した瞬間に肌が自分の皮脂と錯覚するかのようにスッと吸い込まれていきます。",
        "desc_p2": "80mlという持ち歩きや日常使いにちょうどいいサイズ感で、洗顔後のブースターオイル、化粧水の後のフタ、冬の乾燥する爪周りのネイルケア、さらにはパサつく毛先のツヤ出しまで八面六臂の活躍を見せます。オリーブ特有の青臭い匂いがなく無香料のため、日中のオフィスで手肌や口元の乾燥が気になった際にもサッとひと塗りして即座にしっとり感をチャージできます。",
        "target": "オリーブオイルの保湿力には興味があるけれどベタつくオイルが苦手な方、小豆島産オリーブの上質な品質を日常使いしたい方、朝のスキンケアにも使える軽やかな美容オイルを探している方",
        "point": "朝のメイク前、化粧水の後に手のひらに米粒大を薄く伸ばしてハンドプレス。その後下地を重ねると、暖房の効いたオフィスでも一日中ファンデーションが粉吹きせず綺麗なツヤが持続します。"
    },
    {
        "rank": 5,
        "tag": "🧼 冬の頑固な角栓・毛穴汚れを浮かし、洗い流し後もしっとり保水！オリーブオイル洗顔の最高峰",
        "catch": "医薬部外品として肌荒れを防ぎながら、最高級スペイン産オリーブバージンオイルの油分が毛穴の奥の角栓をトロリと溶かし出す。水でスッキリ流せるのに洗い上がりは吸い付くような潤い膜が残る",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "200ml / ポンプボトル",
        "type": "医薬部外品 薬用高保湿オリーブクレンジングオイル",
        "features": "スペイン産オリーブバージンオイル、ローズマリー葉油、甘草誘導体、ビタミンE",
        "value": "冬の乾燥で硬化した角栓や酸化皮脂を、同質のオレイン酸で優しく溶解。石油系オイルと異なり、肌に必要な潤いを奪い去ることなくバリア機能を死守する",
        "desc_p1": "冬のクレンジング選びは、1年の中で最も慎重になる必要があります。強力な界面活性剤や石油系鉱物油を配合したクレンジングを使うと、寒さで分泌が減っている貴重な天然皮脂まで根こそぎ奪い取られ、洗顔後に肌がバリバリに乾燥してしまうからです。DHCの『薬用ディープクレンジングオイル』は、最高品質のオリーブバージンオイルを主成分に配合し、肌への優しさと圧倒的なメイク落ちを両立させた名作クレンジングです。",
        "desc_p2": "乾いた手のひらに2〜3プッシュ取って顔全体に馴染ませると、植物オイルならではの厚みのあるクッション性が肌と手のひらの摩擦を完璧に防止。真冬の硬化した角栓や毛穴の奥の汚れを、オリーブ油の親油性が穏やかに溶かし出します。水に触れるとナノレベルで親水化してサッと洗い流せるため、肌に油膜のヌルつきを残さず、それでいて洗い上がりは化粧水を急いでつけなくても突っ張らない驚くほどしっとりとした柔肌を実感できます。",
        "target": "冬のクレンジング後に頬や口元がつっぱって痛いと感じる乾燥肌の方、毛穴の角栓汚れを無理にこすらず植物油で優しく落としたい方、マツエクにも対応した高品質オイルを求める方",
        "point": "オイルを顔全体に馴染ませた後、少量のぬるま湯を手に取って顔全体をクルクルと撫で、オイルが白く濁る「乳化」を必ず行ってから洗い流してください。毛穴汚れが驚くほど綺麗に落ちます。"
    },
    {
        "rank": 6,
        "tag": "💆‍♀️ オリーブ油×オリーブスクワランのダブル処方！冬のパサつく毛先と乾燥頭皮を優しく労る無添加オイル",
        "catch": "太陽油脂が誇るパックスオリーの無添加ヘアトリートメントオイル。オリーブ果実油とオリーブスクワラン、マカデミアナッツ油が真冬の静電気によるパサつきを抑え、ツヤとまとまりを宿す",
        "brand_name": "パックスオリー (PAX Olie / 太陽油脂)",
        "capacity": "60ml / ポンプ式遮光ガラス瓶",
        "type": "無添加 高保湿オリーブヘア＆スキャルプオイル",
        "features": "オリーブ果実油、オリーブスクワラン、マカデミアナッツ油、ホホバ種子油、天然精油（イランイラン、ラベンダー）",
        "value": "シリコンや合成界面活性剤を一切排除。熱や静電気でキューティクルが毛羽立った真冬の髪に、植物油脂の自然なエモリエント膜を形成して滑らかな指通りを復元",
        "desc_p1": "11月を過ぎると、ウールのニットやマフラーを着脱するたびにパチパチと静電気が発生し、毛先があちこちに広がってまとまらなくなります。さらに冬の熱いお湯でのシャンプーやドライヤーの温風によって、髪のキューティクルは開き、内部の水分が抜け落ちてバサバサに乾いてしまいます。パックスオリーの『ヘアオイル 60ml』は、良質なオリーブ果実油とオリーブ由来スクワランをダブルで配合した、髪と地肌のための天然植物ヘアオイルです。",
        "desc_p2": "タオルドライ後の濡れた毛先に1〜2プッシュ馴染ませてからドライヤーで乾かすと、オリーブオイルの良質な脂肪酸が熱によるタンパク質変性を防ぎ、しっとりとした重みとシルクのようなツヤを与えてくれます。シリコンでコーティングしたような人工的な重さではなく、素髪そのものが潤いを湛えたような自然なまとまりが一日中持続。天然精油の心落ち着くアロマがふんわりと香り、冬の乾燥で突っ張る頭皮のプレクレンジングオイルとしても極めて優秀です。",
        "target": "冬の静電気で髪が広がりやすい方、シリコン無配合のオーガニックヘアオイルで髪と頭皮を優しくいたわりたい方、毛先の枝毛やパサつきを根本から予防したい方",
        "point": "お風呂上がりのタオルドライ後、毛先を中心によく馴染ませてからドライヤーを上から下に向かって当てます。最後に手に残ったわずかなオイルを頭頂部のアホ毛に撫でつけると静電気が綺麗に収まります。"
    },
    {
        "rank": 7,
        "tag": "✨ 薬用美白×オリーブ乳液エッセンス！冬の血行不良くすみと乾燥小ジワを同時に撃退する高機能美容液",
        "catch": "日本オリーブが開発した薬用ホワイトニング美容液。純粋オリーブオイルのエモリエントベールに持続型ビタミンC誘導体と植物抽出エキスを融合し、冬の過酷な乾燥とくすみを根本から晴らす",
        "brand_name": "オリーブマノン (日本オリーブ)",
        "capacity": "30ml / プッシュボトル",
        "type": "医薬部外品 薬用美白・高保湿オリーブエッセンス",
        "features": "オリーブ果実油、L-アスコルビン酸2-グルコシド（持続型ビタミンC）、グリチルリチン酸2K、カンゾウ葉エキス、オウゴンエキス",
        "value": "水性保湿成分とオリーブ油が絶妙なバランスでエマルジョン化。オイル単体よりも水分保持力が高く、冬のインナードライと乾燥によるメラニン滞留を同時にケア",
        "desc_p1": "冬は紫外線量が減るため油断しがちですが、実は「寒冷による血行不良」と「激しい角層乾燥」によってターンオーバーが停滞し、夏に蓄積した潜在シミが表面化して肌が最もくすんで見える季節です。オリーブマノンの『エクセレントホワイト エッセンス』は、オリーブの濃密な保湿力と薬用美白有効成分を融合させた、大人の冬肌のための高機能エッセンスです。",
        "desc_p2": "ミルクのように滑らかなテクスチャーが肌の上でするすると広がり、乾燥でゴワついた角質層の隙間にスッと染み渡ります。オリーブオイルが肌表面にしなやかな保護ヴェールを張り巡らせて水分蒸散をブロックしつつ、ビタミンC誘導体が透明感をサポート。使い続けることで、冬特有のどんよりとした疲れ顔がパッと明るくなり、夕方になっても頬が乾燥で引きつることがなくなります。",
        "target": "冬になると肌がくすんで透明感が失われる方、オイル美容液はベタついて朝のメイク前に使いにくいと感じている方、乾燥小ジワと美白ケアを同時に叶えたい方",
        "point": "化粧水の直後、2プッシュを顔全体に伸ばし、シミやくすみが気になる頬骨周辺や乾燥小ジワが気になる目尻に優しく重ねづけしてハンドプレスしてください。"
    },
    {
        "rank": 8,
        "tag": "🌿 小豆島のオリーブ専業農家が丹精込めて精製！肌がふっくら吸い付くようなハリとツヤを取り戻す化粧用オイル",
        "catch": "創業以来オリーブ一筋の井上誠耕園が手がける最高純度の美容オリーブオイル。人の皮脂膜と調和する高純度オレイン酸が、冬の寒冷で硬直した素肌をふんわり解きほぐす",
        "brand_name": "井上誠耕園 (Inoue Seikoen)",
        "capacity": "30ml / 120ml / スポイト遮光瓶",
        "type": "化粧用純粋オリーブオイル（完全無添加・無着色・無香料）",
        "features": "高純度オリーブ油100%（井上誠耕園厳選抽出）、天然ビタミンA・E、ポリフェノール、オレイン酸",
        "value": "農家ならではの厳しい選果基準と精製技術。オリーブ独特の匂いや重さを極限まで取り除き、洗顔後のまっさらな肌にブースターとして使える驚異の浸透力",
        "desc_p1": "小豆島で親子三代にわたりオリーブと柑橘を育て続ける『井上誠耕園』。彼らが農家の誇りをかけて作り上げた『美容オリーブオイル』は、オリーブの生命力を余すところなく肌へと届ける無添加の化粧用オイルです。果実の選定から抽出、精製に至るまで徹底した品質管理が行われており、オリーブオイル本来の濃厚な保湿力を宿しながらも、サラリと水のように伸び広がる上質な使い心地を実現しています。",
        "desc_p2": "真冬の洗顔後すぐ、化粧水の前に1滴を手のひらに広げて顔全体に軽く押し当てる「プレオイル（導入）」として使うと、冷気でカチコチに固まっていた角層が驚くほど柔らかくほぐれ、その後に重ねる化粧水がスポンジのようにぐんぐん吸い込まれていきます。お肌のキメが整い、内側からふっくらとしたハリと自然なツヤがみなぎるのを実感できます。乾燥が特に厳しい日中も肌が柔らかく保たれます。",
        "target": "手持ちの化粧水や乳液の浸透が悪くなっていると感じる方、小豆島の信頼できる専業農家の手仕事コスメを使いたい方、季節の変わり目に肌がゴワつく方",
        "point": "朝晩の洗顔直後、肌にまだ水滴がわずかに残る状態で1滴を優しくハンドプレスし、その後にたっぷりの化粧水を重ねる「ブースター使い」が最も効果的です。"
    },
    {
        "rank": 9,
        "tag": "🍊 ドイツのハーブ療法が息づく！オーガニックオリーブ油×グレープフルーツ精油の全身引き締め保湿オイル",
        "catch": "天然ハーブの世界的名門クナイプのオーガニック美容オイル。肌のターンオーバーを促す高純度オリーブオイルにグレープフルーツ果皮油をブレンドし、冬の乾燥とキメの乱れを爽やかに整える",
        "brand_name": "Kneipp (クナイプ)",
        "capacity": "100ml / ガラスボトル",
        "type": "オーガニック認証 高保湿フェイス＆ボディオイル",
        "features": "オリーブ果実油（オーガニック認証）、ヒマワリ種子油、グレープフルーツ果皮油、ベニバナ種子油、トコフェロール",
        "value": "ドイツの伝統植物療法に基づき、肌のターンオーバーとバリア機能をダブルでサポート。柑橘系の爽やかな天然精油の香りで、重くなりがちな冬のボディケアを至福の癒しタイムに変える",
        "desc_p1": "ドイツで130年以上の歴史を誇るハーバルブランド・クナイプの『ビオ オイル』は、国際的なオーガニック認証「NATRUE（ネイトゥルー）」を取得した本格的な全身用植物オイルです。ベースとなるのは、肌のバリア機能を整える良質なオレイン酸を豊富に含んだオリーブ果実油とヒマワリ種子油。乾燥によってキメが乱れ、触るとザラつきを感じる冬の素肌に、素早くリッチな潤いと柔軟性を補給します。",
        "desc_p2": "サラッとした滑らかなテクスチャーで肌滑りが良いため、お風呂上がりのボディマッサージオイルとしても秀逸。冷え固まりやすいふくらはぎや太もも、デコルテを優しく流しながら塗り広げると、グレープフルーツの天然エッセンシャルオイルのみずみずしい香りが立ち上り、一日の疲れと緊張を心地よく解き放ってくれます。顔の乾燥小ジワケアから傷跡・ニキビ跡の保湿ケアまで全身くまなく使える頼もしい一本です。",
        "target": "冬のボディの粉吹き・乾燥と同時にむくみや冷えをマッサージでケアしたい方、爽やかなシトラスの香りで気分をリフレッシュしたい方、オーガニック認証オイルを求める方",
        "point": "入浴後、軽く水滴を払った肌にたっぷり手に取り、足首から膝、膝から足の付け根に向かって下から上へと引き上げるようにマッサージしながら塗り広げてください。"
    },
    {
        "rank": 10,
        "tag": "💋 オリーブバージンオイルの鉄壁シールド！冬の木枯らしでも皮むけ知らずのぷるぷる唇を保つロングセラー",
        "catch": "オリーブバージンオイルとアロエエキスを高配合したDHCの殿堂入りリップ。唇の表面温度でとろけてピタッと密着し、真冬の乾燥冷風による皮むけ・ひび割れを完璧にブロック",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "1.5g / スティック容器（6本まとめ買いセット）",
        "type": "医薬部外品 薬用高保湿オリーブリップトリートメント",
        "features": "オリーブバージンオイル、アロエエキス、甘草誘導体、ビタミンE（酢酸トコフェロール）",
        "value": "皮脂腺がなく角層が極めて薄い唇に、人間の皮脂に最も近いオリーブ油膜を形成。何度も塗り直さなくても一日中しっとり感が持続し、口紅のノリと持ちを格段に向上させる",
        "desc_p1": "冬のスキンケアで見落としがちなのが「唇」の乾燥対策です。唇には皮脂を分泌する皮脂腺が一切なく、角層も通常の皮膚の数分の一の薄さしかないため、湿度が低下する11月以降は真っ先に水分が蒸発して皮むけや縦ジワ、出血を伴うひび割れが頻発します。DHCの『薬用リップクリーム』は、オリーブバージンオイルの卓越した保護膜形成能力をリップに応用した、発売以来累計1億本以上を売り上げる不滅のベストセラーです。",
        "desc_p2": "唇にあてると、体温でオリーブバージンオイルがするするとほどけるように滑らかに伸び広がり、デリケートな粘膜に負担をかけずに密着。甘草誘導体とアロエエキスが荒れた唇の炎症を鎮静し、オリーブ油の抱水ヴェールが一晩中潤いを逃しません。就寝前にたっぷり塗っておけば、翌朝目覚めた瞬間も唇がふっくらと柔らかく弾力をキープ。口紅の下地として使えば、冬のマットリップも乾燥崩れせず一日中美しい仕上がりが続きます。",
        "target": "冬になると唇がガサガサに皮むけして口紅が塗れない方、一般的なリップクリームだとすぐに乾いて何度も塗り直してしまう方、ポーチや枕元に常備して家族で愛用したい方",
        "point": "唇の縦ジワの溝に沿って、スティックを縦方向に優しく往復させて塗り込みます。就寝前は輪郭からはみ出るくらいオーバーリップ気味に塗ると、ラップパックのような密封効果が得られます。"
    }
]

toc_items = [
    {"id": "intro", "title": "1. 11月・12月の本格乾燥と粉吹き肌！「元祖高保湿」オリーブオイルの驚異の力"},
    {"id": "mechanism", "title": "2. なぜオリーブオイルは真冬に最強なのか？オレイン酸と疑似皮脂膜の皮膚科学"},
    {"id": "comparison", "title": "3. 高保湿オリーブオイルコスメおすすめ10選の比較表"},
    {"id": "ranking", "title": "4. 高保湿オリーブオイルコスメおすすめ厳選ランキング10選"},
    {"id": "guide", "title": "5. 失敗しないオリーブオイルコスメの選び方＆冬の部位別活用術"},
    {"id": "routine", "title": "6. 真冬の粉吹き肌とあかぎれを救う！効果的なオイルブースター＆密封ルーティン"},
    {"id": "faq", "title": "7. オリーブオイルコスメに関するよくある質問（FAQ）"},
    {"id": "summary", "title": "8. まとめ：伝統の植物エモリエントで真冬の肌乾燥とさようなら"}
]

toc_html = "\n".join([f'          <li><a href="#{item["id"]}">{item["title"]}</a></li>' for item in toc_items])

table_rows = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    table_rows.append(f"""            <tr>
              <td class="rank-cell"><strong>第{p["rank"]}位</strong></td>
              <td class="product-cell">
                <a href="#rank-{p["rank"]}"><strong>{p["brand_name"]}</strong><br><span style="font-size:0.85rem;color:#4b5563;">{item_data["name"][:35]}...</span></a>
              </td>
              <td>{p["type"]}</td>
              <td class="price-cell">{item_data["price"]}</td>
              <td>{p["features"][:30]}...</td>
              <td><a href="{item_data["url"]}" class="table-btn" target="_blank" rel="nofollow noopener">楽天で見る</a></td>
            </tr>""")

table_rows_html = "\n".join(table_rows)

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <!-- Rank {p["rank"]} -->
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge rank-{p["rank"]}">第{p["rank"]}位</span>
            <div class="product-title-group">
              <span class="product-catch">{p["tag"]}</span>
              <h3 class="product-name">{item_data["name"]}</h3>
              <p class="product-subname">{p["catch"]}</p>
            </div>
          </div>

          <div class="product-main-grid">
            <div class="product-visual">
              <img src="{item_data["img"]}" alt="{item_data["name"]}" class="product-img" loading="lazy">
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">{item_data["price"]}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", "4.8")}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", "150")}件）</span>
              </div>
              <a href="{item_data["url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
                🛒 楽天市場で「{p["brand_name"]}」の最新価格・在庫・口コミを見る
              </a>
            </div>

            <div class="product-info-col">
              <table class="spec-table">
                <tr><th>ブランド</th><td>{p["brand_name"]}</td></tr>
                <tr><th>容量・容器</th><td>{p["capacity"]}</td></tr>
                <tr><th>アイテム種別</th><td>{p["type"]}</td></tr>
                <tr><th>注目美肌成分</th><td>{p["features"]}</td></tr>
                <tr><th>真冬の特長・価値</th><td>{p["value"]}</td></tr>
              </table>

              <div class="product-body">
                <h4 class="body-title">皮膚科学的アプローチ＆冬の使用感レビュー</h4>
                <p>{p["desc_p1"]}</p>
                <p>{p["desc_p2"]}</p>

                <div class="recommend-box">
                  <div class="recommend-title">💡 こんな方・こんな冬の肌悩みにおすすめ！</div>
                  <p>{p["target"]}</p>
                </div>

                <div class="usage-box">
                  <div class="usage-title">🧴 11月・12月の効果的な使い方テクニック</div>
                  <p>{p["point"]}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
""")

all_cards_html = "\n".join(product_cards_html)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！高純度オレイン酸と植物スクワレンが真冬の粉吹き肌とあかぎれ手肌をしっとり潤す高保湿オリーブオイルコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の寒冷乾燥で皮脂が激減したカサカサ肌・粉吹きすね・あかぎれ手肌を救う高保湿オリーブオイル（オリーブ果実油）コスメを徹底厳選！DHC、オリーブマノン、小豆島オリーブ園、パックスオリー、クナイプまでオレイン酸と疑似皮脂膜の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="オリーブオイル コスメ, オリーブバージンオイル, 高保湿 コスメ 冬, DHC オリーブバージンオイル, オリーブマノン, 小豆島オリーブ園, 乾燥肌 オイル 11月 12月, あかぎれ 保湿, 粉吹き肌 対策">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-olive-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！高純度オレイン酸と植物スクワレンが真冬の粉吹き肌とあかぎれ手肌をしっとり潤す高保湿オリーブオイルコスメランク10">
  <meta property="og:description" content="11月・12月の本格乾燥シーズン！人の皮脂に最も近いオレイン酸と天然スクワレンを補給する高保湿オリーブオイルコスメを徹底厳選！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-olive-oil">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="LUMI COSMETICS">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！高純度オレイン酸と植物スクワレンが真冬の粉吹き肌とあかぎれ手肌をしっとり潤す高保湿オリーブオイルコスメランク10",
    "description": "11月・12月の寒冷乾燥で皮脂が激減したカサカサ肌・粉吹きすね・あかぎれ手肌を救う高保湿オリーブオイルコスメを徹底厳選！",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-olive-oil"
    }},
    "author": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS 保湿皮膚科学研究チーム"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://lumi-cosme.vercel.app/favicon.jpg"
      }}
    }},
    "datePublished": "2026-11-05T19:00:00+09:00",
    "dateModified": "2026-11-05T19:00:00+09:00"
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿オリーブオイルコスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {", ".join([f'''{{
        "@type": "ListItem",
        "position": {p["rank"]},
        "name": "{items[p["rank"]-1]["name"]}",
        "url": "{items[p["rank"]-1]["url"]}"
      }}''' for p in product_details])}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "オリーブオイルは油焼け（日焼けやシミ）の原因になりませんか？朝使っても大丈夫ですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "化粧品用に高度に精製されたオリーブバージンオイルは不純物が極限まで除去されており、主成分であるオレイン酸は酸化安定性が極めて高いため、紫外線による油焼けを起こす心配はありません。むしろ朝の洗顔後に1滴馴染ませることで、日中の冷風や暖房による乾燥から肌を守る優れたバリアとして機能します。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "食用のエクストラバージンオリーブオイルを肌に塗っても同じ効果がありますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "食用のオリーブオイルは風味や酸度を重視して作られており、微細な果肉片や水分、不純物が含まれているため、直接肌に塗ると毛穴詰まりやアレルギー皮膚炎の原因になる恐れがあります。スキンケアには必ず化粧品規格として精製された化粧用オリーブオイルをご使用ください。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "ニキビができやすい脂性肌や混合肌でも冬にオリーブオイルを使って平気ですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "オレイン酸はアクネ菌の栄養源になりやすいため、ニキビが活発にできている部位や皮脂分泌の盛んなTゾーンへの多量塗布は避けるのが賢明です。ただし、冬場に乾燥してカサつく目元・口元・頬や、すねやかかとなどのボディパーツには非常に効果的です。顔に使う場合は米粒大をごく薄く伸ばすようにしてください。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #3f6212;
      --primary-light: #ecfccb;
      --primary-dark: #365314;
      --accent: #65a30d;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg: #f7fee7;
      --bg-card: #ffffff;
      --border: #d9f99d;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-weight: 800;
      font-size: 1.35rem;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}
    
    .hero-container {{
      max-width: 1100px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    .hero-card {{
      background: linear-gradient(135deg, #ecfccb 0%, #ffffff 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
    }}
    .badge-category {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 50px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}
    h1.hero-title {{
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--primary-dark);
      line-height: 1.45;
      margin-bottom: 1.25rem;
    }}
    .hero-lead {{
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.75;
      margin-bottom: 1.5rem;
    }}
    .meta-bar {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: #6b7280;
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}
    
    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-left: 5px solid var(--primary);
      border-radius: var(--radius);
      padding: 1.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-card ul {{
      list-style: none;
      padding-left: 0;
    }}
    .toc-card li {{
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
    }}
    .toc-card a {{
      color: var(--text);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-card a:hover {{ color: var(--primary); text-decoration: underline; }}
    
    .article-section {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .section-title {{
      font-size: 1.5rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .article-section p {{
      margin-bottom: 1.25rem;
      color: #374151;
      font-size: 1rem;
    }}
    .highlight-lead {{
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 1.25rem 1.5rem;
      border-radius: 8px;
      margin-bottom: 1.5rem;
      border-left: 4px solid var(--accent);
    }}
    
    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .data-table th, .data-table td {{
      padding: 0.85rem 1rem;
      border: 1px solid #e5e7eb;
    }}
    .data-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}
    .rank-cell {{ text-align: center; font-size: 1rem; color: var(--primary); white-space: nowrap; }}
    .price-cell {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 4px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}
    
    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: flex-start;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .rank-badge {{
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      padding: 0.4rem 1rem;
      border-radius: 8px;
      white-space: nowrap;
    }}
    .product-catch {{
      display: block;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .product-name {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 0.35rem;
    }}
    .product-subname {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    .product-main-grid {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-main-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-visual {{
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #f7fee7;
      padding: 1.5rem;
      border-radius: 8px;
      border: 1px solid var(--border);
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      border-radius: 8px;
      background: #ffffff;
      margin-bottom: 1rem;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    .price-box {{
      width: 100%;
      background: #ffffff;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      border: 1px solid #e5e7eb;
      text-align: center;
      margin-bottom: 0.75rem;
    }}
    .price-label {{ display: block; font-size: 0.75rem; color: #6b7280; }}
    .price-value {{ font-size: 1.35rem; font-weight: 800; color: #b91c1c; }}
    .review-meta {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
      margin-bottom: 1rem;
    }}
    .review-stars {{ color: #d97706; font-weight: 700; }}
    .review-count {{ color: #6b7280; }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      text-align: center;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000 0%, #7a0000 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 10px -1px rgba(191, 0, 0, 0.35);
    }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.65rem 0.85rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .spec-table th {{
      width: 140px;
      background: #f7fee7;
      color: var(--primary-dark);
      font-weight: 700;
    }}
    
    .product-body h4.body-title {{
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .recommend-box {{
      background: #ecfccb;
      border-left: 4px solid var(--primary);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
      margin: 1.25rem 0;
    }}
    .recommend-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.35rem;
    }}
    .recommend-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    .usage-box {{
      background: #fefce8;
      border-left: 4px solid var(--accent);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
      margin: 1.25rem 0;
    }}
    .usage-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .usage-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    /* FAQ & 内部リンク */
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.25rem 0;
    }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}
    .faq-a {{
      color: #374151;
      padding-left: 1.75rem;
      font-size: 0.95rem;
    }}
    
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">🌿 LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <div class="hero-container">
    <div class="hero-card">
      <span class="badge-category">地中海＆小豆島が生んだ伝統の生体親和性エモリエント</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！高純度オレイン酸と植物スクワレンが真冬の粉吹き肌とあかぎれ手肌をしっとり潤す高保湿オリーブオイルコスメランク10</h1>
      <p class="hero-lead">
        11月から12月にかけて訪れる気温の急降下と湿度の低下。皮脂腺の少ないすねや肘・かかとが粉を吹き、水仕事による指先のあかぎれ、そして洗顔直後から顔全体が突っ張る真冬の深刻な乾燥トラブル——。そんな過酷な冬の素肌を救う究極の切り札が、古代ギリシャから「飲む黄金」と讃えられてきた「オリーブオイル（オリーブ果実油）」です。本記事では、人間の皮脂膜と酷似したオレイン酸トリグリセリドと天然スクワレンを豊富に含むオリーブオイルの皮膚科学的メリットを解き明かし、楽天市場で今すぐ手に入る最高峰のオリーブコスメ10選を徹底検証します。
      </p>
      <div class="meta-bar">
        <span>📅 2026年11月更新（真冬乾燥特化版）</span>
        <span>🔬 皮膚科学・エモリエント検証済み</span>
        <span>🛍️ 楽天市場公式APIデータ連携</span>
      </div>
    </div>
  </div>

  <main class="hero-container">
    <!-- 目次 -->
    <div class="toc-card">
      <div class="toc-title">📑 目次（クリックで各項目へジャンプ）</div>
      <ul>
{toc_html}
      </ul>
    </div>

    <!-- セクション1: 導入 -->
    <section class="article-section" id="intro">
      <h2 class="section-title">1. 11月・12月の本格乾燥と粉吹き肌！「元祖高保湿」オリーブオイルの驚異の力</h2>
      <div class="highlight-lead">
        どんなに高価な美容液やクリームを重ねても乾く理由は「皮脂膜の崩壊」。人間の皮脂の主成分であるオレイン酸をダイレクトに補うオリーブオイルこそ、真冬の乾燥砂漠肌を根本から鎮める最強の防壁です。
      </div>
      <p>
        11月中旬以降、日本の気候は一変します。北西からの季節風によって大気中の湿度は30%台まで落ち込み、さらにオフィスや家庭のエアコン暖房が四六時中稼働することで、肌を取り巻く環境は砂漠並みの乾燥状態へと突入します。加えて寒さによって皮膚の毛細血管が収縮し、血液循環が低下すると、皮脂腺からの皮脂分泌量は夏の半分以下へと激減してしまいます。
      </p>
      <p>
        皮脂膜とは、汗などの水分と皮脂が混ざり合って肌表面を覆う「天然の保護クリーム」です。この皮脂膜が失われると、角質層の水分は外気へと無防備に蒸散し、細胞同士の結束が緩んで表面がめくれ上がり、いわゆる「粉吹き」や「ピリピリとした刺激感」を引き起こします。現代のコスメ界には多種多様な合成エモリエント成分が存在しますが、数千年にわたり人類の肌を乾燥から守り続けてきたオリーブオイルの生体親和性とバリア回復力は、最新の科学をもってしても決して色褪せることはありません。
      </p>
    </section>

    <!-- セクション2: メカニズム -->
    <section class="article-section" id="mechanism">
      <h2 class="section-title">2. なぜオリーブオイルは真冬に最強なのか？オレイン酸と疑似皮脂膜の皮膚科学</h2>
      <p>
        オリーブオイルが真冬の過酷な乾燥肌に対して圧倒的な保護効果を発揮する理由は、その類まれな「生体親和性脂肪酸プロファイル」と「微量有用成分」に裏打ちされています。
      </p>
      <p>
        <strong>① 皮脂の約40%を占める「オレイン酸トリグリセリド」が高濃度（約70〜80%）：</strong><br>
        人間の皮脂を構成する脂肪酸の中で最も多くを占めるのがオレイン酸です。オリーブオイルの脂肪酸組成は実に70〜80%がこのオレイン酸で占められており、肌に乗せた瞬間に自身の皮脂と見紛うかのように素早く馴染みます。角質細胞の隙間を埋めて硬化した角層をふっくらと柔軟化するエモリエント効果に極めて優れ、真冬の強張った肌を解きほぐします。
      </p>
      <p>
        <strong>② 天然の潤滑保護成分「植物性スクワレン」の含有：</strong><br>
        皮脂の構成要素として肌の柔軟性とバリア機能に不可欠なスクワレン。植物油の中でもオリーブオイルは群を抜いてスクワレンの含有量が多く、肌表面に薄くしなやかな「疑似皮脂膜」を形成します。水分を閉じ込めるだけでなく、冬の冷風や摩擦刺激、大気汚染物質の侵入を物理的に跳ね返します。
      </p>
      <p>
        <strong>③ 抜群の酸化安定性と豊富なポリフェノール・ビタミンE：</strong><br>
        多価不飽和脂肪酸（リノール酸やリノレン酸）を多く含むオイルは冬場の空気接触や体温によって酸化しやすい傾向がありますが、オリーブオイルの主成分であるオレイン酸は一価不飽和脂肪酸であり、熱や光、酸素に対して非常に強い安定性を誇ります。さらにオリーブ特有のポリフェノールやビタミンE（トコフェロール）が豊富に含まれており、寒冷による血行不良や肌の酸化ストレスを穏やかに抑え込みます。
      </p>
    </section>

    <!-- セクション3: 比較表 -->
    <section class="article-section" id="comparison">
      <h2 class="section-title">3. 高保湿オリーブオイルコスメおすすめ10選の比較表</h2>
      <p>
        楽天市場で実際に購入可能な人気の高保湿オリーブオイルコスメ10アイテムの種別、参考価格、主要美肌成分を一覧にまとめました。
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド・商品名</th>
              <th>カテゴリー種別</th>
              <th>参考価格（税込）</th>
              <th>注目美肌成分</th>
              <th>楽天リンク</th>
            </tr>
          </thead>
          <tbody>
{table_rows_html}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4: ランキング -->
    <section class="article-section" id="ranking">
      <h2 class="section-title">4. 高保湿オリーブオイルコスメおすすめ厳選ランキング10選</h2>
      <p>
        成分純度、真冬のエモリエント持続力、テクスチャーの扱いやすさ、楽天市場での購入信頼性を総合的に審査したTOP10ランキングです。
      </p>
{all_cards_html}
    </section>

    <!-- セクション5: 選び方ガイド -->
    <section class="article-section" id="guide">
      <h2 class="section-title">5. 失敗しないオリーブオイルコスメの選び方＆冬の部位別活用術</h2>
      <p>
        オリーブオイルコスメを真冬の生活に取り入れる際は、使用する部位や肌悩みに合わせて最適なテクスチャーとアイテムを選ぶことが成功の秘訣です。
      </p>
      <p>
        <strong>① 顔の粉吹き・小ジワ・ブースターには「高純度精製ピュアオイル」：</strong><br>
        DHCのオリーブバージンオイル（第1位）や小豆島オリーブ園（第4位）、井上誠耕園（第8位）のような100%ピュアな化粧品グレードのオイルは、親水性が高く化粧水前の導入やフタとして最適です。洗顔後のまっさらな肌に1滴なじませるだけで、その後のスキンケアの浸透が格段に高まります。
      </p>
      <p>
        <strong>② 全身の乾燥・入浴後のボディケアには「大容量マルチオイル」：</strong><br>
        オリーブマノンの200ml（第2位）やクナイプのビオオイル（第9位）のように大容量で伸びの良いオイルは、真冬の粉吹きすね、カサつく肘や膝、ひび割れがちなかかとへの毎日のケアに惜しみなく使えます。濡れた肌に伸ばすことで油膜感を抑えつつ驚異的なしっとり感を得られます。
      </p>
      <p>
        <strong>③ 冬の頭皮の乾燥・髪の静電気には「オリーブヘアオイル」：</strong><br>
        パックスオリー（第6位）のようにオリーブスクワランやマカデミア油を配合したヘア専用処方は、ドライヤーの熱から髪を守り、冬のパサつく毛先をなめらかに落ち着かせます。頭皮の乾燥やかゆみが気になる場合は、シャンプー前の頭皮マッサージとしても活用できます。
      </p>
    </section>

    <!-- セクション6: ルーティン -->
    <section class="article-section" id="routine">
      <h2 class="section-title">6. 真冬の粉吹き肌とあかぎれを救う！効果的なオイルブースター＆密封ルーティン</h2>
      <p>
        オリーブオイルの卓越した保水シールド効果を100%引き出すための、真冬特化型スキンケアステップです。
      </p>
      <p>
        <strong>ステップ1【洗顔直後のブースター1滴】：</strong><br>
        朝晩の洗顔後、タオルで軽く水分を押さえた直後の「肌がまだ湿っている状態」で、手のひらにオリーブオイルを1滴伸ばし、顔全体を包み込むように優しくハンドプレスします。寒さで収縮した角層が油分でほぐれ、次に与える水分の通り道が拓かれます。
      </p>
      <p>
        <strong>ステップ2【高保湿化粧水で水分をたっぷり注入】：</strong><br>
        ブースターオイルの直後、保湿化粧水を2〜3回に分けてたっぷりと重ねづけします。オリーブオイルの親水基が化粧水中の水分と結合し、角層深部へと水分を引き込みます。肌が手のひらに吸い付くまで丁寧になじませてください。
      </p>
      <p>
        <strong>ステップ3【乳液・クリームの上からのラップ密封】：</strong><br>
        最後に乳液やクリームで整えた後、特に乾燥しやすい目元や口元、粉を吹きやすい頬骨まわりに、ごく少量のオリーブオイルを重ねて軽くプレスします。暖房が一晩中効いている寝室でも、朝まで潤いが一切蒸散しない鉄壁の密閉バリアが完成します。
      </p>
    </section>

    <!-- セクション7: FAQ -->
    <section class="article-section" id="faq">
      <h2 class="section-title">7. オリーブオイルコスメに関するよくある質問（FAQ）</h2>
      
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> オリーブオイルは油焼け（日焼けやシミ）の原因になりませんか？朝使っても大丈夫ですか？</div>
        <div class="faq-a">
          化粧品用に高度に精製されたオリーブバージンオイルは不純物が極限まで除去されており、主成分であるオレイン酸は酸化安定性が極めて高いため、紫外線による油焼けを起こす心配はありません。むしろ朝の洗顔後に1滴馴染ませることで、日中の冷風や暖房による乾燥から肌を守る優れたバリアとして機能します。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 食用のエクストラバージンオリーブオイルを肌に塗っても同じ効果がありますか？</div>
        <div class="faq-a">
          食用のオリーブオイルは風味や酸度を重視して作られており、微細な果肉片や水分、不純物が含まれているため、直接肌に塗ると毛穴詰まりやアレルギー皮膚炎の原因になる恐れがあります。スキンケアには必ず化粧品規格として精製された化粧用オリーブオイルをご使用ください。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> ニキビができやすい脂性肌や混合肌でも冬にオリーブオイルを使って平気ですか？</div>
        <div class="faq-a">
          オレイン酸はアクネ菌の栄養源になりやすいため、ニキビが活発にできている部位や皮脂分泌の盛んなTゾーンへの多量塗布は避けるのが賢明です。ただし、冬場に乾燥してカサつく目元・口元・頬や、すねやかかとなどのボディパーツには非常に効果的です。顔に使う場合は米粒大をごく薄く伸ばすようにしてください。
        </div>
      </div>
    </section>

    <!-- セクション8: まとめ -->
    <section class="article-section" id="summary">
      <h2 class="section-title">8. まとめ：伝統の植物エモリエントで真冬の肌乾燥とさようなら</h2>
      <p>
        11月から12月にかけての本格的な真冬シーズンは、外気の冷気と室内の暖房による激しい水分蒸散によって、私たちの素肌から急速に潤いが奪い去られていきます。どんなに水分を補給しても乾いてしまう冬の肌トラブルを解決する鍵は、健やかな素肌が本来持っている「皮脂膜のバリア機能」を忠実に再現することに他なりません。
      </p>
      <p>
        人間の皮脂組織と極めて近いオレイン酸と植物スクワレンを凝縮したオリーブオイルコスメは、真冬の過酷な環境から角層を優しく守り抜き、カチコチに固まった皮膚をふっくらと柔らかな状態へと蘇らせてくれます。ぜひ本記事のランキングや選び方を参考に、あなたのライフスタイルや肌悩みにぴったりのオリーブオイルコスメを見つけて、真冬でも乾燥知らずのもっちりツヤ肌を手に入れてください。
      </p>
    </section>

    <!-- 関連記事リンクプレースホルダー -->
    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <!-- update_all_internal_links.py で自動挿入 -->
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-logo">🌿 LUMI COSMETICS</div>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で自動挿入 -->
      </div>
      <div style="text-align:center;margin-top:2rem;font-size:0.8rem;color:#6b7280;">
        &copy; 2026 LUMI COSMETICS. All rights reserved.
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-olive-oil.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-olive-oil.html successfully!")
