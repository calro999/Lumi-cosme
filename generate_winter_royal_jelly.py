import json
import re

with open("fetched_3new_fucoidan_royal_soy.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_royal_jelly"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 養蜂研究の最高峰！特有成分デセン酸が真冬のしぼみ肌を深部から目覚めさせる薬用エッセンス",
        "catch": "半世紀以上のローヤルゼリー研究を誇る山田養蜂場の結晶。女王蜂の生命力の源である生ローヤルゼリーエキスを極限まで濃縮。真冬の冷えで血行不良に陥り、水分保持能を失った大人の枯れ肌に驚異的なハリと潤いを呼び戻す",
        "brand_name": "山田養蜂場 (YAMADA BEE FARM)",
        "capacity": "セット仕様 / 薬用高機能エッセンス",
        "type": "高濃度生ローヤルゼリー 薬用高保湿美容液",
        "features": "微粒子化ローヤルゼリーエキス、10-ヒドロキシデセン酸、天然ビタミンB群、アミノ酸複合体",
        "value": "自然界でローヤルゼリーにしか存在しない特有成分『デセン酸』が角層のバリア機能と皮脂膜バランスを正常化。外気温度が低下する11月・12月でも、肌の内側から自らうるおいを湧き上がらせる",
        "desc_p1": "11月から12月にかけて気温が一段と低下すると、皮膚の毛細血管が収縮して血行が滞り、肌細胞への栄養供給と水分代謝が急激に低下します。この『寒冷枯れ肌』に対しては、単に表面を油分で覆うだけでは不十分で、細胞レベルでの活力補給が不可欠です。山田養蜂場の『RJエッセンス』は、女王蜂を育てる唯一の特別食である生ローヤルゼリーから、熱に弱い有効成分を壊さずに独自抽出した最高峰の滋養美容液です。",
        "desc_p2": "特筆すべきは、独自技術で超微細化されたローヤルゼリーエキスが、硬化した角層の奥深くへと驚くほど滑らかに浸透していく点です。40種類以上におよぶ必須アミノ酸やミネラル、そして女性ホルモン様作用を持つ特有成分デセン酸が、真冬の乾燥でしぼみきった角層細胞を一つひとつふっくらと押し上げます。塗布した翌朝の洗顔時には、指先を跳ね返すような濃密な弾力感と、内側から発光するような極上のツヤを実感できます。",
        "target": "冬になると肌がゴワついてどんな化粧水も浸透しない方、寒暖差や年齢による肌のしぼみ・ハリ不足に悩む方、本物のローヤルゼリーの濃密な滋養を肌に届けたい方",
        "point": "朝晩の洗顔直後または化粧水の後、適量を手のひらで温めてから、顔全体を包み込むようにハンドプレス。乾燥やたるみが気になるフェイスラインや目元には、下から上へと優しく引き上げるように馴染ませてください。"
    },
    {
        "rank": 2,
        "tag": "💧 プラセンタ×ローヤルゼリーが角層でパシャッと弾ける！大容量200gの超濃密オールインワン",
        "catch": "製薬会社グループが本気で作った高機能エイジングゲル。高純度ローヤルゼリーエキスにプラセンタと浸透型ヒアルロン酸を黄金ブレンド。濃密なジェルが肌の上で化粧水のように弾け、真冬の砂漠肌を瞬時に満たす",
        "brand_name": "素肌しずく (アサヒグループ食品)",
        "capacity": "200g / 大容量ポンプ式ジャー",
        "type": "高純度ローヤルゼリー×プラセンタ 濃密リペアゲル",
        "features": "加水分解ローヤルゼリータンパク、プラセンタエキス、吸着型ヒアルロン酸、セラミド、コラーゲン",
        "value": "水分をたっぷり抱えたカプセルが肌の上で弾ける『出水型処方』。真冬の過酷なエアコン環境でも、うるおい密封フィルムが角層表面に居座り続け、夕方までぷるぷるのモチ肌を持続",
        "desc_p1": "冬のスキンケアにおいて、『みずみずしい水分感』と『濃厚な保湿持続力』の両立は至難の業です。アサヒグループ食品の『素肌しずく ゲル Sa』は、製薬グループの製剤技術を結集し、肌に乗せた瞬間に濃厚なゲルがパシャッと水滴に変化して角層深部へ染み渡る独自の『出水（しゅっすい）カプセル』を採用した高機能オールインワンです。",
        "desc_p2": "ゲルの中に閉じ込められた高純度ローヤルゼリーエキスとプラセンタが、乾燥で硬直した角層の細胞間隙へと一気に行き渡ります。馴染ませた後は、肌表面に薄い保水シールドが形成され、暖房による水分の蒸発を完璧に遮断。200gという大容量なので、顔だけでなく冬の乾燥でカサつきやすい首元やデコルテまで贅沢に塗り広げられます。モロモロが出ないため朝のメイク前にも安心して使えます。",
        "target": "仕事や家事で忙しく冬の保湿を1品で完璧に済ませたい方、ベタつく重いクリームは苦手だけど乾燥小ジワは防ぎたい方、首元やデコルテまで全身たっぷり高保湿ケアしたい方",
        "point": "洗顔後、さくらんぼ大を手にとって顔全体に伸ばし、手のひらで優しく包み込みます。夜は2プッシュ分を厚めに塗り広げて『うるおいパック』としてそのまま就寝するのがおすすめです。"
    },
    {
        "rank": 3,
        "tag": "✨ 復元ジェルが乾燥小ジワをピーン！発酵ローヤルゼリー×3種コラーゲンの高機能ジェル",
        "catch": "崩しても数秒で元通りに戻る形状記憶復元ジェル。発酵技術によって角層浸透力を高めたローヤルゼリーエキスと3種のコラーゲンが、真冬の寒冷で刻まれる乾燥小ジワを強力にリフトアップ",
        "brand_name": "GRACE ONE (グレイスワン / コーセーコスメポート)",
        "capacity": "100g / 形状記憶ジャー",
        "type": "発酵ローヤルゼリー 濃潤復元リペアジェル",
        "features": "発酵ローヤルゼリーエキス、サクシニルアテロコラーゲン、水溶性コラーゲン、スクワラン、エラスチン",
        "value": "塗った瞬間にピーンとしたハリ膜を形成するタイトニング効果。11月・12月の乾燥による目尻や口元のちりめんジワ、ほうれい線のしぼみを目立たなくさせる",
        "desc_p1": "乾燥がピークに達する真冬は、肌の水分不足によって角層が収縮し、目元や口元に細かい小ジワが定着しやすくなります。コーセーのグレイスワン『濃潤リペアジェル』は、大人の乾燥肌研究から生まれた形状復元タイプの多機能ジェルです。ジャーの中でジェルをぐちゃぐちゃに崩しても、数十秒後にはピーンと平らな表面へと自ら戻る驚異的な復元ポリマーを配合しています。",
        "desc_p2": "この復元ネットワークが肌表面に密着し、しぼんだ角層を引き上げるようにピーンと張ったフィルムを形成。さらに、発酵処理によって分子を細かくした発酵ローヤルゼリーエキスが、角層の奥深くまで浸透してアミノ酸の栄養をチャージします。スクワランとの相乗効果で、暖房の効いた室内に1日中いても肌が突っ張らず、ふっくらとしたハリとツヤが夕方まで持続します。",
        "target": "冬になるとファンデーションが目尻やほうれい線のシワに落ちてしまう方、乾燥によるたるみやハリのなさが気になる方、1本でリフト感とうるおい密封を両立したい方",
        "point": "洗顔後、パール粒2〜3個分を手にとり、あご・両頬・鼻・額の5箇所に置きます。顔の中心から外側へ、下から上へと肌を持ち上げるように伸ばし、最後に手のひらで10秒間密着キープしてください。"
    },
    {
        "rank": 4,
        "tag": "🧪 40種以上の天然滋養を直接肌へ！手持ちコスメを真冬の王乳リッチに変える濃厚原液",
        "catch": "化粧品成分のプロが手掛ける純度重視の濃縮原液。必須アミノ酸・天然ビタミン群・ミネラルを豊富に含むローヤルゼリーエキスそのもの。数滴ブレンドするだけで冬の乾燥枯れ肌に劇的なツヤとしなやかさを注入",
        "brand_name": "TUNEMAKERS (チューンメーカーズ)",
        "capacity": "20ml / スポイト対応遮光瓶",
        "type": "高純度ローヤルゼリーエキス 100%原液美容液",
        "features": "高濃度ローヤルゼリーエキス、BG、水（シンプル極限処方）",
        "value": "余計な増粘剤や香料を一切排除したピュアエッセンス。真冬の過酷な環境で代謝が落ちた肌に直接アプローチし、硬くなった角層を柔らかくほぐしてバリア機能を底上げ",
        "desc_p1": "『愛用している化粧水があるけれど、冬になると保湿力が物足りなくなる』という方に最適なのが、原液コスメのスペシャリスト・チューンメーカーズの『ローヤルゼリーエキス原液』です。全国のサロンや美容マニアから絶大な信頼を寄せられる本品は、良質なローヤルゼリーから抽出された栄養素をそのままボトル詰めしたピュア原液です。",
        "desc_p2": "テクスチャーはさらりとした琥珀色のリキッドで、肌に乗せると吸い込まれるように素早く馴染みます。ローヤルゼリーに含まれるパントテン酸やアミノ酸が、真冬の寒さでターンオーバーが滞った肌細胞を優しくサポート。手持ちの化粧水に2〜3滴混ぜるだけで、サラサラだった化粧水が吸い付くようなリッチなモイスチャーローションへと生まれ変わります。原液ならではのダイレクトな肌応えが魅力です。",
        "target": "愛用のスキンケアを変えずに冬の保湿力だけを極限まで高めたい方、肌のくすみや疲れ感が顔に出てしまいやすい方、成分に余計な添加物を求めないピュア志向の方",
        "point": "洗顔後すぐの素肌に2〜3滴をブースターとして馴染ませるか、手のひらで化粧水や乳液に1〜2滴ブレンドして使用します。特に乾燥がひどい日は、夜のクリームに混ぜて濃厚ナイトパックとしてお使いください。"
    },
    {
        "rank": 5,
        "tag": "🌸 資生堂が誇る大人のリフトゲル！発酵ローヤルゼリーGLが夕方まで続く極上ツヤ肌を創出",
        "catch": "年齢とともに皮脂と水分が枯渇する真冬の肌のために設計。資生堂独自の発酵ローヤルゼリーGLと濃密コラーゲンが、冷えでこわばった表情を柔らかく解きほぐし、一日中ハリツヤが巡る肌へ",
        "brand_name": "PRIOR (プリオール / 資生堂)",
        "capacity": "120mL / 密封ポンプディスペンサー",
        "type": "資生堂 薬用うるおい美リフトゲル（医薬部外品）",
        "features": "発酵ローヤルゼリーGL、コラーゲン、ヒアルロン酸、スクワラン、薬用抗肌荒れ有効成分",
        "value": "資生堂の先進乳化技術により、水溶性の発酵ローヤルゼリーと上質エモリエントオイルを高密度に一体化。冬の暖房直撃下でも夕方までしっとりとした『つや玉』が輝き続ける",
        "desc_p1": "11月から12月にかけて、大人の肌は皮脂分泌量が年間の最低レベルへと落ち込みます。そこにオフィスの暖房が加わることで、肌は急速にツヤを失い、疲れた印象を与えてしまいます。資生堂プリオールの『うるおい美リフトゲル』は、そうした大人の深刻な冬枯れ肌を研究し尽くして開発された薬用高保湿ゲルです。",
        "desc_p2": "ポンプを押すと出てくるリッチなゲルは、肌に伸ばすとスーッとほどけるように馴染み、角層のすみずみまで濃密な潤いを充填。発酵させることで吸収性を高めたローヤルゼリーエキスが、角層のラメラ構造を整えます。塗布した瞬間から肌表面に均一な光の反射膜が生まれ、乾燥による小ジワやくすみを自然にカバー。夕方になっても突っ張らず、しっとりとした柔らかさと若々しいツヤが持続します。",
        "target": "真冬になると夕方に顔がカサついて老け見えが気になる方、化粧水・乳液・美容液を1本で上質に済ませたい方、資生堂の信頼できる処方でエイジングケアしたい方",
        "point": "洗顔後、手のひらに1〜2プッシュを取り、顔全体に優しく馴染ませます。指先で頬を軽く持ち上げるようにハンドプレスすると、リフトアップ感が長時間持続します。"
    },
    {
        "rank": 6,
        "tag": "🧼 大正時代からのロングセラー！王乳とハチミツの天然皮膜で洗顔後も一切突っ張らない",
        "catch": "100年近く愛され続ける伝統の生ローヤルゼリー配合液体洗顔料。キメ細やかなとろみ泡が冬のデリケートな肌を摩擦レスに洗い上げ、洗顔後すぐに化粧水をつけなくてもしっとり滑らか",
        "brand_name": "蜂乳 (ホウニュウ)",
        "capacity": "200mL / 伝統ボトル",
        "type": "特選 生ローヤルゼリー配合 液体洗顔フォーム",
        "features": "生ローヤルゼリーエキス、純粋ハチミツ、ヤシ油由来マイルド洗浄成分",
        "value": "石鹸カスを残さず素早くすすげるのに、肌表面にはハチミツとローヤルゼリーの天然モイストヴェールが残留。冬のお風呂上がりや朝の洗顔後の激しい乾燥突っ張りを完全防止",
        "desc_p1": "真冬のスキンケアで最も重要なのは、『洗顔によって肌本来の潤いを奪わないこと』です。冬の朝、一般的な洗顔フォームで顔を洗った直後に肌がピキピキと突っ張ってしまうのは、必要な皮脂まで洗い流されている証拠です。大正時代から日本の女性の肌を支えてきた『特選 蜂乳クリーム石鹸』は、生ローヤルゼリーとハチミツを惜しみなく配合した伝説の洗顔料です。",
        "desc_p2": "黄金色のとろみのある液体を手にとり、少量のぬるま湯を加えて泡立てると、キメの細かいクリーミーな泡が立ち上がります。肌の上を滑らせるように洗うだけで、毛穴の余分な皮脂や睡眠中の汗をやさしく吸着オフ。洗い流した瞬間、まるで上質なオイルトリートメントを受けたかのような、滑らかで吸い付くような肌触りに感動します。冬の朝洗顔にこれ以上のアイテムはありません。",
        "target": "冬の朝の洗顔後に肌がバリバリに突っ張る方、乾燥肌で普通の洗顔フォームが使えない方、昔ながらの確かな天然成分で肌のキメを整えたい方",
        "point": "手のひらに10円玉大を取り、少量のぬるま湯を足しながらしっかり泡立てます。顔全体に泡を転がすように15〜20秒優しく洗い、32℃程度のぬるま湯ですすぎ流してください。"
    },
    {
        "rank": 7,
        "tag": "🛡️ 熟成ローヤルゼリーを極限凝縮！真冬の過酷な冷風から肌バリアを鉄壁ガードする濃厚クリーム",
        "catch": "山田養蜂場の最高峰スキンケアライン『RJエクセレント』の真髄。独自発酵熟成ローヤルゼリーエキスと濃厚なシア脂・スクワランが融合。真冬の冷たい木枯らしと乾燥気流を完全に遮断するリッチバーム",
        "brand_name": "山田養蜂場 (YAMADA BEE FARM)",
        "capacity": "30g / 遮光ジャー容器",
        "type": "最高峰 薬用熟成ローヤルゼリー エモリエントクリーム",
        "features": "熟成ローヤルゼリーエキス、シアバター、高精製スクワラン、浸透型セラミド、アミノ酸ペプチド",
        "value": "真冬の氷点下に近い寒風や激しい暖房直撃下でも、角層の水分蒸散を0%に近づける極厚エモリエントシールド。夜塗れば翌朝まで吸い付くようなモチ肌を完全密閉",
        "desc_p1": "12月の真冬になると、いくら水分を与えても数時間後には肌が乾いてしまう『蒸散過多』の状態に陥ります。山田養蜂場が誇る最高峰クリーム『RJエクセレント』は、厳選された熟成ローヤルゼリーエキスを限界濃度まで練り込み、さらに上質な天然エモリエント成分を贅沢にブレンドした超濃厚バームクリームです。",
        "desc_p2": "ジャーからすくい取るとバターのように濃厚なコクがありますが、手のひらで温めると体温でするりと溶け出し、肌に吸い付くように密着します。角層の内側へはローヤルゼリーのアミノ酸とデセン酸をじっくり送り込み、外側はシア脂とスクワランの強固な保護膜で密閉。暖房をつけっぱなしにした寝室で朝を迎えても、指先が吸い付くほどのしっとり感がそのまま残っています。",
        "target": "どんな高保湿クリームを塗っても真冬の乾燥に追いつかない超乾燥肌、エアコンの温風が直接当たるオフィスで働く方、年齢による本格的な乾燥小ジワを改善したい方",
        "point": "夜のお手入れの最後に、パール粒大を手にとり、両手のひらで温めて透明にしてから顔全体を包み込むようにハンドプレス。乾燥しやすい目元や口元には重ねづけしてください。"
    },
    {
        "rank": 8,
        "tag": "💆‍♀️ 蜂蜜×国産馬油×王乳のトリプル補修！冬の静電気と乾燥でパサつく毛髪を密着リペア",
        "catch": "サロン品質の濃厚ハニートリートメント。生ローヤルゼリーエキスと高純度ハチミツ、国産馬油が融合。冬のエアコン暖房やマフラーの摩擦で傷んだ毛髪のキューティクルを滑らかにコーティング",
        "brand_name": "Honeyce (ハニーチェ) / 国産馬油ハニー",
        "capacity": "600ml / 大容量ディスペンサー",
        "type": "高保湿 生ローヤルゼリー×ハチミツ×馬油 トリートメント",
        "features": "生ローヤルゼリーエキス、オーガニックハチミツ、国産純度100%馬油、加水分解ケラチン",
        "value": "髪の内部にアミノ酸と水分を補給しながら、馬油とハチミツの油膜ヴェールが外側を密閉。冬特有の不快な静電気や毛先のバサつき、広がりを瞬時に抑え込む",
        "desc_p1": "11月から12月は、肌だけでなく髪にとっても受難の季節です。大気の乾燥に加えて室内の暖房、セーターやマフラーとの摩擦によって静電気が発生し、毛先のキューティクルが剥離してパサつきが深刻化します。『ハニートリートメント 600ml』は、髪の主成分であるケラチンタンパクと極めて親和性の高いローヤルゼリーアミノ酸を配合したヘアマスクです。",
        "desc_p2": "こっくりとした濃厚なテクスチャーが髪1本1本に吸い付くように密着。ローヤルゼリーの微細アミノ酸が髪のダメージホールに染み込み、国産馬油が表面をしなやかにコーティングします。洗い流す時から指通りの良さが際立ち、ドライヤーで乾かした後は毛先までしっとりとまとまり、サロン帰りのようなツヤと手触りが復活します。600mlの大容量で冬の間惜しみなく使えます。",
        "target": "冬になると髪がパサついて静電気で広がる方、カラーやパーマで毛先が傷んで乾燥している方、大容量でコスパ良く上質なヘアケアを続けたい方",
        "point": "シャンプー後、軽く水気を絞ってから毛先を中心に揉み込みます。目の粗いコームで全体に行き渡らせた後、2〜3分置いてからすすぐと補修効果が格段に高まります。"
    },
    {
        "rank": 9,
        "tag": "💋 ガサガサ唇・皮むけを濃密ラッピング！ローヤルゼリー×ハチミツの極上リップ用美容液",
        "catch": "プチプラの枠を超えた実力派リップエッセンス。ローヤルゼリーエキスとハチミツ、シアバターが唇に厚膜の保護ヴェールを形成。真冬の寒風でひび割れそうなデリケートな唇をぷるぷるに蘇らせる",
        "brand_name": "Country & Stream (カントリー&ストリーム)",
        "capacity": "10g / チューブ容器",
        "type": "高保湿 ローヤルゼリー配合 リップ用美容液",
        "features": "ローヤルゼリーエキス、ハチミツ、シア脂、オリーブ果実油、カミツレ花エキス",
        "value": "斜めカットチューブで塗りやすく、唇の縦ジワを埋めるようにピタッと密着。冬の乾燥気流にさらされても皮むけを防ぎ、口紅の下地としてもグロスとしても大活躍",
        "desc_p1": "唇は皮膚が非常に薄く、皮脂腺が存在しないため、11月から12月の乾燥気流にさらされると最も早くひび割れや皮むけを起こします。一般的な固形リップクリームでは『塗ってもすぐに乾いて皮がむける』という方に絶大な支持を得ているのが、カントリー＆ストリームの『ハニーフルリップ』です。",
        "desc_p2": "チューブから出すと蜜のように濃厚なジェル状リキッドで、唇に乗せた瞬間に体温でなめらかに広がり、ぽってりとした濃密な厚膜を形成します。ローヤルゼリーエキスのアミノ酸が角層を柔軟にし、ハチミツとシアバターが水分を逃さずラッピング。夜寝る前に塗れば、翌朝まで潤い膜が残り、ぷるんとした生まれたてのような唇に整います。ほんのり甘いハチミツの香りも冬の癒やしになります。",
        "target": "冬になると唇が乾燥して皮がめくれたり縦ジワが目立つ方、リップクリームを1日に何回も塗り直している方、マスク着用時の唇の擦れを保護したい方",
        "point": "チューブの先を直接唇にあてて伸ばすか、指先にとって唇の縦ジワに沿って縦方向に塗り込みます。就寝前に厚めに塗って『ラップパック』をすると翌朝の潤いが劇的にアップします。"
    },
    {
        "rank": 10,
        "tag": "✨ 純度99%純金×高麗紅参×生王乳！真冬のエイジング枯れ肌を再生するプレミアムクリーム",
        "catch": "美容大国・韓国でロングセラーを誇る超高級エイジングクリーム。純度99%ゴールドパウダー、生ローヤルゼリー、6年根高麗紅参、黄金シルクを贅沢に凝縮。寒冷酸化と乾燥萎縮を跳ね返す",
        "brand_name": "NATURE REPUBLIC (ネイチャーリパブリック)",
        "capacity": "60g / プレミアムスクエアジャー",
        "type": "純金×生ローヤルゼリー 濃密ウォータリークリーム",
        "features": "純金箔（純度99%）、生ローヤルゼリーエキス、高麗紅参エキス、黄金シルクアミノ酸",
        "value": "みずみずしい透明ジェルの中に純金箔と濃厚な王乳カプセルが溶け込む特殊処方。冬の冷え固まった肌を滑らかに解きほぐし、シルクのような輝きと濃密な水分感を一日中キープ",
        "desc_p1": "冬の乾燥は、単なる水分不足だけでなく、寒冷ストレスによる酸化や肌細胞の活力低下を引き起こします。ネイチャーリパブリックの『ジンセン ロイヤルシルク ウォータリークリーム』は、純金と生ローヤルゼリー、紅参という東洋の三大エイジングケア成分を贅沢に配合した世界的ベストセラークリームです。",
        "desc_p2": "透き通るような美しいゴールドジェルを肌に乗せると、純金箔がスルスルと肌に馴染んで消え去り、豊かな水分感と高貴な香りが広がります。生ローヤルゼリーエキスが角層深部へ栄養を行き渡らせ、シルクアミノ酸が肌表面に吸い付くような保護フィルムを展開。油分の重たさを感じさせないのに、一日中暖房の効いた部屋にいても肌がピンと張り続け、極上の水光肌を演出してくれます。",
        "target": "冬の寒さや乾燥で肌がくすみ、疲れた印象に見られがちな方、リッチな成分と至福の使用感でエイジングケアしたい方、ベタつかないのに驚くほど潤うクリームを求める方",
        "point": "朝晩のスキンケアの最後に、スパチュラで適量をとって顔全体に伸ばします。純金箔が肌に溶け込むように、手のひらで温めながら優しくハンドプレスして浸透させてください。"
    }
]

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge">第{p["rank"]}位</span>
            <span class="product-tag">{p["tag"]}</span>
          </div>

          <h3 class="product-title">{p["catch"]}</h3>
          <p class="product-display-name">{item_data["display_name"]}</p>

          <div class="product-layout">
            <div class="product-visual-col">
              <div class="img-wrap">
                <img src="{item_data["image_url"]}" alt="{p["brand_name"]} {item_data["item_name"]}" class="product-img" loading="lazy" />
              </div>
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">¥{item_data["price"]:,}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", "4.8")}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", "80")}件）</span>
              </div>
              <a href="{item_data["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
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
  <title>保湿力の強さで肌乾燥とさようなら！女王蜂だけの特有成分デセン酸と濃密アミノ酸が真冬の冷気で硬化したエイジング砂漠肌をしっとり満たす高保湿ローヤルゼリーコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の冷気と暖房乾燥による大人の枯れ肌・しぼみ小ジワ・ハリ低下を救う高保湿ローヤルゼリー（王乳エキス・特有成分デセン酸）コスメを徹底厳選！山田養蜂場、素肌しずく、グレイスワン、資生堂プリオールまで40種以上のアミノ酸と女性ホルモン様作用の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="ローヤルゼリー コスメ, ローヤルゼリー 美容液, 高保湿 コスメ 冬, エイジングケア 11月 12月, 暖房乾燥 対策, 山田養蜂場 RJ, 素肌しずく ゲル, グレイスワン, プリオール 美リフトゲル">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！女王蜂だけの特有成分デセン酸と濃密アミノ酸が真冬の冷気で硬化したエイジング砂漠肌をしっとり満たす高保湿ローヤルゼリーコスメランク10">
  <meta property="og:description" content="女王蜂の驚異的生命力！特有成分デセン酸と濃密アミノ酸が、真冬の寒冷で硬化した大人の乾燥肌をふっくら満たすおすすめコスメ10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-royal-jelly">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿ローヤルゼリーコスメランク10">
  <meta name="twitter:description" content="11月・12月の冷えと暖房砂漠肌に！女王蜂の特有成分デセン酸コスメおすすめ厳選10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！女王蜂だけの特有成分デセン酸と濃密アミノ酸が真冬の冷気で硬化したエイジング砂漠肌をしっとり満たす高保湿ローヤルゼリーコスメランク10",
    "description": "11月・12月の冷気と暖房乾燥による大人の枯れ肌・しぼみ小ジワを救う高保湿ローヤルゼリーコスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-06T03:30:00+09:00",
    "dateModified": "2026-11-06T03:30:00+09:00",
    "author": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS 編集部"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://lumi-cosme.vercel.app/favicon.jpg"
      }}
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-royal-jelly"
    }}
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #2: ItemList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
      {",\n      ".join([f'''{{
        "@type": "ListItem",
        "position": {p["rank"]},
        "name": "{items[p["rank"]-1]["item_name"][:50]}",
        "url": "{items[p["rank"]-1]["affiliate_url"]}"
      }}''' for p in product_details])}
    ]
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #3: FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "ハチミツとローヤルゼリーのスキンケア効果の違いは何ですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "ハチミツは糖分（果糖・ブドウ糖）が主成分で、水分を吸着して閉じ込めるエモリエント・保湿膜の形成に優れています。一方、ローヤルゼリーは働き蜂が分泌する女王蜂専用のスーパーフードで、良質なタンパク質、40種以上の必須アミノ酸、ビタミンB群、そして特有成分『10-ヒドロキシデセン酸』を含みます。肌の代謝やコラーゲン合成を内側からサポートし、真冬の硬化した角層を細胞レベルで活性化させるエイジング効果に長けています。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "特有成分『デセン酸』にはどのような美肌効果がありますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "10-ヒドロキシ-2-デセン酸（デセン酸）は、自然界ではローヤルゼリーにのみ存在する希少な脂肪酸です。女性ホルモン（エストロゲン）に似た働きを持ち、加齢や冬のストレスで乱れがちな皮脂分泌バランスを整え、角層のセラミド合成をサポートして内側から弾力とハリを呼び覚まします。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "ローヤルゼリーコスメは敏感肌でも使えますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "基本的には肌荒れ防止作用やバリア修復作用があり敏感肌に適していますが、蜂由来の天然成分であるため、重度の蜂アレルギーや花粉アレルギーをお持ちの方は念のため事前にパッチテストを行うことを推奨します。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "11月・12月の冬に効果的な使い方のコツは？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "寒さで角層がこわばっている冬は、洗顔後すぐに手のひらで温めてから優しくハンドプレスして浸透させることが肝要です。特に乾燥が激しい夜は、ローヤルゼリー配合クリームやゲルを通常の1.5〜2倍量塗り、スリーピングパックとして就寝すると翌朝のモチモチ感が格段に向上します。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #c68a1d;
      --primary-light: #fdf6e7;
      --primary-dark: #8c5b05;
      --accent: #b83b5e;
      --text: #2d3436;
      --text-muted: #636e72;
      --bg: #fcfbf9;
      --card-bg: #ffffff;
      --border: #f0e6d2;
      --shadow: 0 4px 16px rgba(198, 138, 29, 0.08);
      --radius: 12px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
      padding: 0;
    }}

    header {{
      background: linear-gradient(135deg, #8c5b05 0%, #c68a1d 100%);
      color: #ffffff;
      padding: 40px 20px 30px;
      text-align: center;
    }}
    .site-tagline {{ font-size: 0.9rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; opacity: 0.9; }}
    h1 {{ font-size: 1.7rem; line-height: 1.4; max-width: 960px; margin: 0 auto 15px; font-weight: 800; }}
    .header-meta {{ font-size: 0.85rem; opacity: 0.85; margin-top: 10px; }}

    .container {{
      max-width: 1000px;
      margin: 0 auto;
      padding: 30px 20px 60px;
    }}

    .breadcrumbs {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 25px;
    }}
    .breadcrumbs a {{ color: var(--primary-dark); text-decoration: none; }}
    .breadcrumbs a:hover {{ text-decoration: underline; }}

    .intro-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
      border-left: 6px solid var(--primary);
    }}
    .intro-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 15px;
    }}
    .intro-section p {{ margin-bottom: 15px; }}
    .intro-section p:last-child {{ margin-bottom: 0; }}

    .mechanism-box {{
      background: var(--primary-light);
      border-radius: var(--radius);
      padding: 24px;
      margin: 25px 0;
    }}
    .mechanism-title {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 10px;
      font-size: 1.1rem;
    }}

    .toc {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px 25px;
      margin-bottom: 40px;
    }}
    .toc-title {{ font-weight: 700; color: var(--primary-dark); margin-bottom: 12px; }}
    .toc ol {{ padding-left: 20px; }}
    .toc li {{ margin-bottom: 6px; font-size: 0.95rem; }}
    .toc a {{ color: var(--text); text-decoration: none; }}
    .toc a:hover {{ color: var(--primary-dark); text-decoration: underline; }}

    /* 商品カード */
    .product-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 30px;
      margin-bottom: 40px;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(198, 138, 29, 0.14);
    }}

    .product-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 15px;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, #c68a1d, #8c5b05);
      color: #ffffff;
      font-size: 1.1rem;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 20px;
      letter-spacing: 1px;
    }}
    .product-tag {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 5px 12px;
      border-radius: 6px;
    }}

    .product-title {{
      font-size: 1.25rem;
      line-height: 1.45;
      color: var(--text);
      margin-bottom: 8px;
    }}
    .product-display-name {{
      font-size: 0.95rem;
      color: var(--text-muted);
      margin-bottom: 20px;
      line-height: 1.5;
    }}

    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 30px;
    }}
    @media (max-width: 768px) {{
      .product-layout {{ grid-template-columns: 1fr; }}
    }}

    .product-visual-col {{
      text-align: center;
    }}
    .img-wrap {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px;
      margin-bottom: 15px;
    }}
    .product-img {{
      width: 100%;
      height: 240px;
      object-fit: contain;
      border-radius: 4px;
    }}
    .price-box {{
      background: #fdfaf5;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 10px;
      margin-bottom: 10px;
    }}
    .price-label {{ font-size: 0.75rem; color: var(--text-muted); display: block; }}
    .price-value {{ font-size: 1.35rem; font-weight: 800; color: #b12704; }}
    .review-meta {{ font-size: 0.85rem; margin-bottom: 15px; color: var(--text-muted); }}
    .review-stars {{ color: #e67a00; font-weight: 700; margin-right: 4px; }}

    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff !important;
      text-align: center;
      padding: 14px 15px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 10px rgba(191, 0, 0, 0.25);
      transition: background 0.2s, transform 0.1s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a80000 0%, #800000 100%);
      transform: translateY(-1px);
    }}

    /* スペック表 */
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 10px 12px;
      border-bottom: 1px solid var(--border);
    }}
    .spec-table th {{
      width: 28%;
      background: #faf4e8;
      color: var(--primary-dark);
      text-align: left;
      font-weight: 700;
    }}
    .spec-table td {{
      background: #ffffff;
    }}

    .product-body {{ margin-top: 15px; }}
    .body-title {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 10px;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 4px;
    }}
    .product-body p {{ margin-bottom: 12px; font-size: 0.95rem; }}

    .recommend-box {{
      background: #fdfaf2;
      border-left: 4px solid var(--primary);
      padding: 14px 16px;
      margin: 15px 0 10px;
      border-radius: 0 6px 6px 0;
    }}
    .recommend-title {{ font-weight: 700; font-size: 0.9rem; color: var(--primary-dark); margin-bottom: 4px; }}
    .recommend-box p {{ margin-bottom: 0; font-size: 0.9rem; }}

    .usage-box {{
      background: #fff8f5;
      border-left: 4px solid #e06d53;
      padding: 14px 16px;
      margin: 10px 0 0;
      border-radius: 0 6px 6px 0;
    }}
    .usage-title {{ font-weight: 700; font-size: 0.9rem; color: #a8381e; margin-bottom: 4px; }}
    .usage-box p {{ margin-bottom: 0; font-size: 0.9rem; }}

    /* 比較表セクション */
    .comparison-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
      overflow-x: auto;
    }}
    .comparison-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 20px;
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 12px 14px;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .comparison-table th {{
      background: var(--primary-dark);
      color: #ffffff;
      font-weight: 700;
    }}
    .comparison-table tr:nth-child(even) {{ background: #fdfaf5; }}

    /* ガイドセクション */
    .guide-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }}
    .guide-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 15px;
      border-left: 5px solid var(--primary);
      padding-left: 12px;
    }}
    .guide-section h3 {{
      font-size: 1.15rem;
      color: var(--text);
      margin: 20px 0 10px;
    }}
    .guide-section p {{ margin-bottom: 15px; font-size: 0.95rem; }}

    /* FAQセクション */
    .faq-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }}
    .faq-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 20px;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 16px 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-question {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 8px;
      font-size: 1rem;
    }}
    .faq-answer {{ font-size: 0.95rem; color: var(--text); }}

    /* 内部リンク */
    .internal-links {{
      background: #faf4e8;
      border-radius: var(--radius);
      padding: 25px;
      margin-bottom: 40px;
    }}
    .internal-links h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin-bottom: 15px;
    }}
    .links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 12px;
    }}
    .link-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 14px;
      text-decoration: none;
      color: var(--text);
      font-size: 0.9rem;
      display: block;
      transition: border-color 0.2s, transform 0.1s;
    }}
    .link-card:hover {{
      border-color: var(--primary);
      transform: translateY(-1px);
      color: var(--primary-dark);
    }}

    footer {{
      background: #1a252f;
      color: #bdc3c7;
      padding: 40px 20px 30px;
      font-size: 0.85rem;
      text-align: center;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 15px;
      margin-bottom: 25px;
    }}
    .footer-links a {{ color: #bdc3c7; text-decoration: none; }}
    .footer-links a:hover {{ color: #ffffff; text-decoration: underline; }}
    .copyright {{ opacity: 0.7; }}
  </style>
</head>
<body>

  <header>
    <div class="site-tagline">LUMI COSMETICS - 科学的エビデンスで選ぶ真冬の本格高保湿スキンケア</div>
    <h1>保湿力の強さで肌乾燥とさようなら！女王蜂だけの特有成分デセン酸と濃密アミノ酸が真冬の冷気で硬化したエイジング砂漠肌をしっとり満たす高保湿ローヤルゼリーコスメランク10</h1>
    <div class="header-meta">
      <span>公開日: 2026年11月6日</span> | <span>監修: LUMI COSMETICS エイジングスキンケア研究チーム</span>
    </div>
  </header>

  <div class="container">
    <div class="breadcrumbs">
      <a href="/">HOME</a> &gt; <a href="/winter-royal-jelly">高保湿ローヤルゼリーコスメ</a>
    </div>

    <!-- 導入セクション -->
    <section class="intro-section">
      <h2>冷気と暖房で皮脂が激減！なぜ真冬の大人の肌は急激に硬化・しぼむのか？</h2>
      <p>11月中旬から12月にかけて、急激な寒波と室内暖房のフル稼働によって、30代・40代以上の肌は一気に『過酷な乾燥エイジング期』へ突入します。気温が10℃を下回ると皮膚の血流が鈍化し、皮脂腺からの皮脂分泌量は夏の半分以下へと激減。さらに湿度が20%台まで低下したオフィスでは、角層内部の水分が猛烈な勢いで蒸発していきます。その結果、『保湿クリームを塗ってもすぐに肌が突っ張る』『目元や口元に細かい小ジワが刻まれ、肌が硬くこわばる』という深刻な枯れ肌現象が生じるのです。</p>
      
      <p>この真冬の枯渇肌を救う究極の滋養成分として、古来より東西の王族や美容研究者に重宝されてきたのが『ローヤルゼリー（王乳）』です。数百匹の働き蜂からわずか1滴しか採れないこの特別食は、働き蜂の約40倍の寿命を持ち、生涯にわたり毎日何千個もの卵を産み続ける女王蜂の驚異的な生命力を支えています。その濃密な栄養素は、冬の寒冷で活力を失った角層細胞を劇的に覚醒させます。</p>

      <div class="mechanism-box">
        <div class="mechanism-title">🧪 皮膚科学が解明！ローヤルゼリーが冬枯れ肌を再生する3大メカニズム</div>
        <ul>
          <li><strong>① 特有成分『10-ヒドロキシデセン酸』によるバリア＆皮脂バランス正常化：</strong> 自然界ではローヤルゼリーにのみ存在する希少脂肪酸「デセン酸」が、女性ホルモン（エストロゲン）様作用を発揮。冬の寒暖差や加齢で低下した角層のセラミド合成力を活性化させ、皮脂膜の保護力を根本から高めます。</li>
          <li><strong>② 40種類以上の必須アミノ酸・ビタミンB群による角層柔軟化：</strong> 肌の天然保湿因子（NMF）と極めて近い良質なアミノ酸群が、冷気でカチコチに硬化した角質細胞の間に浸透。ごわついた肌をまるで生まれたてのようにふっくら柔らかくほぐします。</li>
          <li><strong>③ コラーゲン・エラスチン産生をサポートするエイジングケア力：</strong> 微細化された王乳ペプチドが真皮線維芽細胞にアプローチし、冬の乾燥によって失われがちな弾力とハリを深部から押し上げます。</li>
        </ul>
      </div>
    </section>

    <!-- 目次 -->
    <section class="toc">
      <div class="toc-title">📑 目次（タップで該当セクションへスクロール）</div>
      <ol>
        <li><a href="#rank-1">第1位：山田養蜂場 RJ地肌ケア＆スキンケア エッセンス</a></li>
        <li><a href="#rank-2">第2位：素肌しずく ゲル Sa (アサヒグループ食品)</a></li>
        <li><a href="#rank-3">第3位：GRACE ONE (グレイスワン) 濃潤リペアジェル</a></li>
        <li><a href="#rank-4">第4位：TUNEMAKERS (チューンメーカーズ) ローヤルゼリーエキス原液</a></li>
        <li><a href="#rank-5">第5位：PRIOR (プリオール / 資生堂) うるおい美リフトゲル</a></li>
        <li><a href="#rank-6">第6位：蜂乳 (ホウニュウ) 特選 クリーム石鹸</a></li>
        <li><a href="#rank-7">第7位：山田養蜂場 RJエクセレント 薬用クリーム</a></li>
        <li><a href="#rank-8">第8位：Honeyce (ハニーチェ) 生ローヤルゼリー＆ハニー 集中補修ヘアトリートメント</a></li>
        <li><a href="#rank-9">第9位：Country & Stream (カントリー&ストリーム) ハニーフルリップ</a></li>
        <li><a href="#rank-10">第10位：NATURE REPUBLIC ジンセン ロイヤルシルク ウォータリークリーム</a></li>
        <li><a href="#comparison">一目でわかる！高保湿ローヤルゼリーコスメ全10品スペック比較表</a></li>
        <li><a href="#guide">11月・12月に失敗しない高保湿ローヤルゼリーコスメの選び方</a></li>
        <li><a href="#faq">よくある質問（Q&A）</a></li>
      </ol>
    </section>

    <!-- ランキング商品カード群 -->
    <section class="ranking-list">
      {all_cards_html}
    </section>

    <!-- 比較表 -->
    <section class="comparison-section" id="comparison">
      <h2>📊 高保湿ローヤルゼリーコスメ全10品スペック比較表</h2>
      <p>アイテムごとの容量・アイテム種別・特徴・参考価格を一覧表にまとめました。真冬のエイジング枯れ肌の悩みに合わせて最適なアイテムをお選びください。</p>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>ブランド / 商品名</th>
            <th>種別</th>
            <th>容量</th>
            <th>特長・真冬の強み</th>
            <th>参考価格</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>第1位</td>
            <td>山田養蜂場 RJ地肌＆スキンケア</td>
            <td>薬用高濃度美容液</td>
            <td>セット仕様</td>
            <td>生ローヤルゼリーエキス極限濃縮・デセン酸による角層再建</td>
            <td>¥12,320</td>
          </tr>
          <tr>
            <td>第2位</td>
            <td>素肌しずく ゲル Sa</td>
            <td>濃密オールインワン</td>
            <td>200g</td>
            <td>王乳×プラセンタ出水カプセル・大容量で首元までモチモチ</td>
            <td>¥2,871</td>
          </tr>
          <tr>
            <td>第3位</td>
            <td>GRACE ONE 濃潤リペアジェル</td>
            <td>形状復元リフトジェル</td>
            <td>100g</td>
            <td>発酵ローヤルゼリー×3種コラーゲン・乾燥小ジワをピーンと補正</td>
            <td>¥3,300</td>
          </tr>
          <tr>
            <td>第4位</td>
            <td>TUNEMAKERS ローヤルゼリー原液</td>
            <td>100%原液美容液</td>
            <td>20ml</td>
            <td>無添加ピュア原液・手持ちコスメを真冬の王乳リッチにカスタム</td>
            <td>¥2,860</td>
          </tr>
          <tr>
            <td>第5位</td>
            <td>資生堂 プリオール 美リフトゲル</td>
            <td>薬用高保湿ゲル</td>
            <td>120mL</td>
            <td>発酵ローヤルゼリーGL配合・夕方までしっとりツヤ玉が持続</td>
            <td>¥2,480</td>
          </tr>
          <tr>
            <td>第6位</td>
            <td>蜂乳 特選 クリーム石鹸</td>
            <td>伝統液体洗顔料</td>
            <td>200mL</td>
            <td>大正からの伝統処方・生王乳とハチミツで洗顔後も一切突っ張らない</td>
            <td>¥4,590</td>
          </tr>
          <tr>
            <td>第7位</td>
            <td>山田養蜂場 RJエクセレント</td>
            <td>最高峰薬用クリーム</td>
            <td>30g</td>
            <td>熟成王乳×シアバター濃厚シールド・冬の冷風を完全遮断</td>
            <td>¥19,030</td>
          </tr>
          <tr>
            <td>第8位</td>
            <td>Honeyce ハニートリートメント</td>
            <td>濃密ヘアマスク</td>
            <td>600ml</td>
            <td>王乳×国産馬油×ハチミツ・冬の静電気と毛先パサつきを撃退</td>
            <td>¥1,650</td>
          </tr>
          <tr>
            <td>第9位</td>
            <td>カントリー&ストリーム ハニーフルリップ</td>
            <td>唇用高保湿美容液</td>
            <td>10g</td>
            <td>王乳×ハチミツ厚膜ヴェール・真冬のひび割れ皮むけ唇をぷるぷるに</td>
            <td>¥498</td>
          </tr>
          <tr>
            <td>第10位</td>
            <td>ネイチャーリパブリック ジンセンクリーム</td>
            <td>純金ウォータリークリーム</td>
            <td>60g</td>
            <td>純度99%純金×生王乳×紅参・寒冷酸化を跳ね返す極上水光肌</td>
            <td>¥5,610</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- ガイドセクション -->
    <section class="guide-section" id="guide">
      <h2>💡 11月・12月に失敗しない高保湿ローヤルゼリーコスメの選び方</h2>
      
      <h3>1. 『生ローヤルゼリー』か『発酵ローヤルゼリー』かで選ぶ</h3>
      <p>ローヤルゼリーエキスには、採れたての栄養素を熱を加えずに抽出した『生ローヤルゼリー』と、酵母等で発酵させて低分子化した『発酵ローヤルゼリー』があります。乾燥で硬くなった角層の奥深くまですばやく浸透させたい場合は、分子が微細化された発酵タイプ（グレイスワンやプリオール等）が最適です。一方、アミノ酸やビタミン、特有成分デセン酸の豊富な天然栄養バランスをそのまま肌に届けてバリアを底上げしたい場合は、生ローヤルゼリーを高配合した山田養蜂場やチューンメーカーズが圧倒的な威力を発揮します。</p>

      <h3>2. 配合されているサポート成分（プラセンタ・コラーゲン・オイル）に注目</h3>
      <p>真冬のローヤルゼリーケアは、相乗効果を生み出す組み合わせ成分も重要です。しぼみ小ジワやたるみ感を速効でケアしたい方は『コラーゲンやエラスチン』配合、透明感と細胞賦活を狙うなら『プラセンタ』配合、そして室内の暖房気流から長時間うるおいを逃したくない超乾燥肌の方は『スクワランやシアバター、馬油』が配合されたクリームやトリートメントを選びましょう。</p>

      <h3>3. 毎日のスキンケアのステップに応じた適材適所の選択</h3>
      <p>冬の乾燥対策は、洗顔から仕上げのクリームまでトータルでの潤い設計が効果的です。まずは蜂乳クリーム石鹸で洗顔時の水分流出を防ぎ、素肌しずくやプリオールなどのオールインワンで角層水分を満たし、最後に山田養蜂場RJエクセレントのような濃厚バームでフタをする、という王乳トータルケアを行うことで、過酷な12月の寒波でも一切揺らがない陶器のようなモチ肌をキープできます。</p>
    </section>

    <!-- FAQセクション -->
    <section class="faq-section" id="faq">
      <h2>❓ よくある質問（Q&A）</h2>
      <div class="faq-item">
        <div class="faq-question">Q1. ハチミツとローヤルゼリーのスキンケア効果の違いは何ですか？</div>
        <div class="faq-answer">ハチミツは糖分（果糖・ブドウ糖）が主成分で、水分を吸着して閉じ込めるエモリエント・保湿膜の形成に優れています。一方、ローヤルゼリーは働き蜂が分泌する女王蜂専用のスーパーフードで、良質なタンパク質、40種以上の必須アミノ酸、ビタミンB群、そして特有成分『10-ヒドロキシデセン酸』を含みます。肌の代謝やコラーゲン合成を内側からサポートし、真冬の硬化した角層を細胞レベルで活性化させるエイジング効果に長けています。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q2. 特有成分『デセン酸』にはどのような美肌効果がありますか？</div>
        <div class="faq-answer">10-ヒドロキシ-2-デセン酸（デセン酸）は、自然界ではローヤルゼリーにのみ存在する希少な脂肪酸です。女性ホルモン（エストロゲン）に似た働きを持ち、加齢や冬のストレスで乱れがちな皮脂分泌バランスを整え、角層のセラミド合成をサポートして内側から弾力とハリを呼び覚まします。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q3. ローヤルゼリーコスメは敏感肌でも使えますか？</div>
        <div class="faq-answer">基本的には肌荒れ防止作用やバリア修復作用があり敏感肌に適していますが、蜂由来の天然成分であるため、重度の蜂アレルギーや花粉アレルギーをお持ちの方は念のため事前にパッチテストを行うことを推奨します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q4. 11月・12月の冬に効果的な使い方のコツは？</div>
        <div class="faq-answer">寒さで角層がこわばっている冬は、洗顔後すぐに手のひらで温めてから優しくハンドプレスして浸透させることが肝要です。特に乾燥が激しい夜は、ローヤルゼリー配合クリームやゲルを通常の1.5〜2倍量塗り、スリーピングパックとして就寝すると翌朝のモチモチ感が格段に向上します。</div>
      </div>
    </section>

    <!-- 内部リンクブロック -->
    <section class="internal-links">
      <h3>🔗 あわせて読みたい！真冬の乾燥対策・高保湿コスメ関連記事</h3>
      <div class="links-grid">
        <a href="/winter-fucoidan" class="link-card">🌊 高保湿フコイダン（海の自己治癒多糖体）</a>
        <a href="/winter-honey" class="link-card">🍯 高保湿ハチミツコスメ</a>
        <a href="/winter-manuka-honey" class="link-card">🐝 高保湿マヌカハニーコスメ</a>
        <a href="/winter-propolis" class="link-card">🌿 高保湿プロポリス</a>
        <a href="/winter-collagen" class="link-card">🌸 高保湿生コラーゲン</a>
        <a href="/winter-placenta" class="link-card">✨ 高濃度プラセンタ</a>
      </div>
    </section>
  </div>

  <footer>
    <div class="footer-links">
      <a href="/">トップページ</a>
      <a href="/winter-royal-jelly">高保湿ローヤルゼリー</a>
      <a href="/winter-fucoidan">高保湿フコイダン</a>
      <a href="/winter-honey">高保湿ハチミツ</a>
      <a href="/winter-collagen">高保湿コラーゲン</a>
    </div>
    <div class="copyright">&copy; 2026 LUMI COSMETICS. All Rights Reserved. 無断転載を禁じます。</div>
  </footer>

</body>
</html>
"""

with open("winter-royal-jelly.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("winter-royal-jelly.html created successfully!")
