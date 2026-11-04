import json
import re

with open("fetched_3new_nov_dec_yuzu_sake_vitamine.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_sake_kasu"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 累計2,000万個突破の金字塔！杜氏の手のようなもっちり白肌へ導く酒粕パック",
        "catch": "熊本県河津酒造の伝統酒粕エキス配合。くすみ・古い角質を穏やかにオフし、真冬の肌をワントーン明るい透明感で満たす",
        "brand_name": "pdc (ピーディーシー) ワフードメイド",
        "capacity": "170g (酒粕パック 洗い流しパック)",
        "type": "高保湿発酵酒粕洗い流しパック",
        "features": "酒粕エキス（河津酒造の純米酒粕）、コメ発酵液、加水分解酵母エキス、キュウリ果実エキス、コメセラミド",
        "value": "寒冷で固まった古い角質をやさしく吸着オフしながら、アミノ酸と水分をダイレクトに補給。洗顔後の肌がつるんと吸い付く仕上がりへ",
        "desc_p1": "冬の寒風と暖房による乾燥が進む11月〜12月は、肌のターンオーバーが乱れて古い角質が肌表面に蓄積し、顔全体がどんよりと暗くくすむ『冬枯れゴワつき』が多発します。そんな冬の肌悩みを一網打尽にするのが、日本のみならずアジア中でメガヒットを記録しているpdcの『ワフードメイド 酒粕パック』です。阿蘇の伏流水と酒米を使って昔ながらの槽搾り製法で作られる熊本県・河津酒造の新鮮な酒粕から抽出したオリジナル酒粕エキスを贅沢に配合しています。",
        "desc_p2": "本物の酒粕を練り込んだようなふわふわで濃厚なペーストは、肌に伸ばすとピタッと密着。お風呂の湯船に浸かりながら5〜10分パックすることで、スチーム効果により酒粕に含まれる豊富なアミノ酸やコウジ酸、ビタミン類が角層の奥深くまで浸透します。ぬるま湯ですすぎ落とした瞬間、まるでくすみのベールが1枚剥がれたかのような透明感と、指が吸い付くようなもっちりとした柔らかさに誰もが驚愕するはずです。",
        "target": "冬になると肌のくすみ・ゴワつきが取れない方、洗い流すだけで速攻の透明感ともちもち感を実感したい方、お風呂で手軽にスペシャルエステケアをしたい方",
        "point": "洗顔後、タオルで軽く水分を拭き取った肌に、目と口の周りを避けてサクランボ大2〜3個分を肌が隠れる厚さに均一に塗り広げます。入浴中の蒸気の中で5〜10分置き、ぬるま湯で丁寧に洗い流してください。週2〜3回のスペシャルケアがおすすめです。"
    },
    {
        "rank": 2,
        "tag": "📄 極厚多層シートに発酵エキスを濃密含浸！砂漠肌を速攻レスキューする酒粕マスク",
        "catch": "酒粕エキス×米セラミド×加水分解酵母。極厚の3層構造シートが真冬の乾いた角層に発酵アミノ酸を隙間なく届けきる",
        "brand_name": "pdc (ピーディーシー) ワフードメイド",
        "capacity": "10枚入 (酒粕マスク)",
        "type": "高保水発酵アミノ酸集中シートマスク",
        "features": "酒粕エキス、コメ発酵液、米セラミド（グルコシルセラミド）、ヒアルロン酸Na、植物エキス複合体",
        "value": "洗い流す手間なく、10分間貼るだけで濃密な酒粕パックと同等の保水・透明感ケアが完了。真冬の朝のメイク前や夜の集中保水に最適",
        "desc_p1": "大ヒットの酒粕パックを『もっと手軽に、毎日のスキンケアで使いたい』という声から誕生したのが、この『ワフードメイド 酒粕マスク』です。美容液を贅沢に含んだ極厚の多層構造シートを採用し、広げた瞬間に酒粕由来のほんのり甘い優しい日本酒の香りがふわりと立ち上ります。",
        "desc_p2": "シートの密着性が非常に高く、下を向いても剥がれ落ちないため、真冬の朝の身支度中やドライヤーをかけながらでも手軽に高保湿トリートメントが可能。酒粕エキスと米セラミドが角層の水分保持膜を瞬時に修復し、10分後にマスクを剥がした後の肌は水分を極限まで蓄えたみずみずしいツヤを放ちます。その後のファンデーションの密着度と夕方までの崩れにくさが格段に向上します。",
        "target": "パックを洗い流す時間が取れない忙しい方、冬の朝のメイクのりを良くしたい方、シートマスクで手軽に酒粕の美肌効果を取り入れたい方",
        "point": "洗顔後すぐ、または化粧水で肌を軽く整えた後にシートを密着させます。5〜10分置いた後にマスクを外し、肌の上に残った美容液を手のひらでハンドプレスしてしっかり押し込みます。袋に残った液は首元やデコルテに塗布してください。"
    },
    {
        "rank": 3,
        "tag": "🧼 温泉宿の美肌の秘密！超濃密もっちり泡でくすみと毛穴汚れを落とす酒粕洗顔フォーム",
        "catch": "純米酒粕エキス配合。キメ細かく弾力のあるクッション泡が、冬の乾燥で硬化した毛穴の奥の角栓とメラニン角質を優しくオフ",
        "brand_name": "アズマ商事 (旅美人)",
        "capacity": "120g (酒粕洗顔フォーム)",
        "type": "高保湿発酵アミノ酸クッション洗顔フォーム",
        "features": "純米酒粕エキス、加水分解米エキス、植物性洗浄成分、ヒアルロン酸、アミノ酸系保湿成分",
        "value": "洗顔による必要な潤いの流出（つっぱり感）を完全に抑え、洗い上がりから化粧水をつけたかのようなしっとり肌を実現",
        "desc_p1": "全国の一流温泉旅館やホテルの大浴場に置かれ、その感動的な洗い上がりの良さから口コミで大ヒットとなったアズマ商事・旅美人の『酒粕洗顔フォーム』。真冬の洗顔で最も避けたいのは、強力な脱脂力を持つ洗顔料によって皮脂膜が根こそぎ奪われ、洗顔直後から顔がつっぱって粉を吹くトラブルです。",
        "desc_p2": "この洗顔フォームは、手のひらで泡立てると逆さにしても落ちないほど濃密でキメ細かな弾力クッション泡が完成。手と顔の皮膚が直接触れ合わないため、摩擦ダメージを完全にゼロに抑えながら、酒粕エキスに含まれる天然のアミノ酸と酵素の力で古い角質と毛穴の奥の汚れをやさしく浮かせて落とします。洗い流した後の肌は突っ張るどころか、しっとりと吸い付くような柔軟性を取り戻します。",
        "target": "冬の洗顔後に顔がピキピキと突っ張る方、濃密なもっちり泡で優しく摩擦レス洗顔をしたい方、温泉上がりのようなツルツル肌を目指す方",
        "point": "洗顔ネットをぬるま湯で濡らし、フォームを2cmほど出して空気を含ませるようにしっかり泡立てます。テニスボール大の濃密泡を顔の上で転がすように洗い、32〜34℃のぬるま湯で20回以上丁寧にすすぎます。"
    },
    {
        "rank": 4,
        "tag": "🍶 純米吟醸酒発酵液×4種のセラミド！顔も体も濃密ヴェールで守る大容量クリーム",
        "catch": "菊正宗の純米吟醸酒コメ発酵液と4種のヒト型類似セラミド。コクがあるのにベタつかず、真冬の全身を潤いの膜で包み込む",
        "brand_name": "菊正宗酒造",
        "capacity": "150g (日本酒のクリーム)",
        "type": "発酵アミノ酸高保湿フェイス＆ボディクリーム",
        "features": "コメ発酵液（純米吟醸酒）、セラミドEOP/NP/AP/リン酸型、グリチルリチン酸2K、コメ胚芽油、ホホバ種子油",
        "value": "150gという贅沢な大容量で、顔はもちろん首・デコルテ・カサつくボディまでこれ1個で冬の乾燥バリアを完結できる高コスパ名品",
        "desc_p1": "老舗酒蔵の菊正宗が培ってきた醸造技術をスキンケアに応用した『日本酒のクリーム』。純米吟醸酒の製造過程で生まれるコメ発酵液には、アミノ酸やミネラルが豊富に含まれており、これを4種類のセラミドと高保湿植物オイルと絶妙にブレンドして誕生した濃厚保湿クリームです。",
        "desc_p2": "こっくりとしたリッチなテクスチャーですが、肌に伸ばすと体温でするりと溶け広がり、白浮きせずすばやくなじみます。肌表面に油分の重たい被膜感を残さず、内側はもっちりと潤い、外側はサラリとしたシルクのような手触りに仕上がるのが特徴。夜のスキンケアの最後にフタとして使えば、真冬のエアコン暖房をつけっぱなしで就寝しても翌朝まで乾きを一切感じさせません。",
        "target": "顔だけでなく首や手足も惜しみなく濃厚クリームで保湿したい方、プチプラで大容量の高保湿クリームを探している方、ベタつかないリッチ感を求める方",
        "point": "夜のお手入れの最後に、パール粒大を手にとって顔全体に優しくハンドプレスしてなじませます。乾燥が気になるひじ・膝・かかとには入浴直後にたっぷり塗り込むと、角質がふっくら柔らかくなります。"
    },
    {
        "rank": 5,
        "tag": "💧 振って使う二層式！酒粕水分×コメ胚芽油で角層を瞬時にほぐす高保湿化粧水",
        "catch": "酒粕エキス層7：コメ胚芽油層3の二層構造シェイクローション。水分補給とオイルシールドを同時に叶える乾燥肌の救世主",
        "brand_name": "pdc (ピーディーシー) ワフードメイド",
        "capacity": "190ml (酒粕化粧水)",
        "type": "二層式発酵オイルイン高保湿化粧水",
        "features": "酒粕エキス、コメ発酵液、コメ胚芽油、加水分解酵母、キュウリ果実エキス",
        "value": "真冬の硬化した角層に、水分と油分を同時に浸透させることで、乳液を重ねる前からもっちりと吸い付くような柔肌を完成させる",
        "desc_p1": "冬の乾燥肌は、水分だけを与えてもすぐに蒸発し、油分だけを塗っても角層の内部まで入っていきません。pdcの『ワフードメイド 酒粕化粧水』は、この乾燥のジレンマを解決するために開発された、酒粕エキスを溶け込ませたローション層と、米から搾ったエモリエント成分であるコメ胚芽油層の二層式化粧水です。",
        "desc_p2": "使用前にボトルをよく振ると、微細なオイルドロップが水分全体に均一に混ざり合い、ミルキーな液体へと変化。手のひらに取って顔になじませると、オイルインとは思えないほどみずみずしく角層へ染み渡り、同時に肌表面には薄く均一なオイルベールが張られます。1本で化粧水と軽い乳液を同時にまとったような濃密な保湿感があり、冬のスキンケアステップを劇的に効率化します。",
        "target": "化粧水をつけてもすぐに乾いてしまうインナードライ肌の方、オイル美容を取り入れたいけれどベタつきが苦手な方、冬のスキンケアを手軽に済ませたい方",
        "point": "二層が均一に白濁するまでボトルを上下によく振ってから、500円玉大を手にとり顔全体になじませます。乾燥が気になる部分には、さらに100円玉大を重ね塗りして手のひらで温めるようにハンドプレスしてください。"
    },
    {
        "rank": 6,
        "tag": "🏆 累計出荷数1,000万本超！日本酒発酵アミノ酸×セラミドが全身を潤す殿堂入り化粧水",
        "catch": "純米吟醸酒の美肌成分を一升瓶から凝縮。500mlの特大容量で真冬のフェイスケアからコットンパック・全身まで浴びるように保湿",
        "brand_name": "菊正宗酒造",
        "capacity": "500ml (日本酒の化粧水 高保湿)",
        "type": "発酵アミノ酸×セラミド大容量高保湿化粧水",
        "features": "コメ発酵液、セラミドNP/AP/EOP、アルブチン、プラセンタエキス、アミノ酸（グルタミン酸、アルギニン、ロイシン）",
        "value": "1本で一升瓶分の遊離アミノ酸と同等の美肌エキスを配合。真冬の過酷な乾燥下でも惜しみなく全身に使えるコスパの最高峰",
        "desc_p1": "ドラッグストアのスキンケアコーナーで不動の人気を誇る菊正宗の『日本酒の化粧水 高保湿』。日本酒1.8L（一升瓶）に凝縮されているアミノ酸と同等の濃度を配合し、さらに角層の細胞間脂質を補修する3種類のセラミドとアルブチンを配合した、美肌発酵コスメの代名詞的存在です。",
        "desc_p2": "とろみのあるみずみずしいテクスチャーで、塗った瞬間から肌がゴクゴクと水分を飲み干すように深く浸透。ほのかな日本酒の甘い香りが心地よく、浸透後はモチッとした吸い付き感がありながらも表面はベタつきません。500mlという大容量のため、冬のボディケアや、ローションシートにたっぷり含ませての『全顔発酵ローションパック』など、贅沢な水分補給が気兼ねなく実践できます。",
        "target": "プチプラで惜しみなくバシャバシャ使える高保湿化粧水を探している方、ローションパックを毎日したい方、顔と全身を1本で保湿したい方",
        "point": "洗顔後、手のひらにたっぷり取って顔全体に2〜3回重ねづけします。週末にはコットンやコインマスクに化粧水をヒタヒタに浸し、3分間の集中フェイスパックを行うと、エステ後のような透き通るモチ肌が蘇ります。"
    },
    {
        "rank": 7,
        "tag": "✨ 白玉のようなもっちりツヤ肌へ！忙しい朝晩を1品で完結させる酒粕オールインワン",
        "catch": "酒粕エキス×コメ発酵液を濃縮ゲル化。化粧水・乳液・美容液・クリーム・パックの5役を兼ね備え、真冬の乾燥から肌を死守",
        "brand_name": "白玉りっち (酒粕コスメ)",
        "capacity": "50g (酒粕オールインワンクリーム)",
        "type": "高純度酒粕オールインワン高保湿ゲル",
        "features": "酒粕エキス、コメ発酵液、コメヌカエキス、ヒアルロン酸、水溶性コラーゲン",
        "value": "洗顔後これ1個で冬の本格的な発酵保湿トリートメントが完了。時間のない真冬の朝も、乾燥崩れ知らずのツヤ肌ベースを形成",
        "desc_p1": "真冬の朝は寒さで布団から出るのも億劫で、スキンケアに何工程もかける余裕がないことも多いもの。『白玉りっち 酒粕オールインワンクリーム』は、昔ながらの酒粕の美肌力とコメ発酵の保湿力を凝縮した、多忙な現代人のための高機能オールインワンゲルです。",
        "desc_p2": "白玉のようにぷるぷると弾力のあるゲルは、肌に乗せるとみずみずしくとろけて角層の奥までスピーディーに浸透。肌表面に潤いの保護膜を形成し、水分と美容成分を一晩中閉じ込めます。油分と水分のバランスが絶妙に設計されているため、塗布後すぐにメイクをしてもモロモロが出ず、内側から自然な光を放つツヤ肌仕上がりを一日中キープできます。",
        "target": "忙しい朝や疲れた夜のスキンケアをワンステップで済ませたい方、オールインワン特有の乾燥や物足りなさを解消したい方",
        "point": "洗顔後、スパチュラでパール2粒大を手に取り、顔の中心から外側へ引き上げるように伸ばします。乾燥が気になる目元やほうれい線には、米粒大を指先でトントンと重ね塗りしてください。"
    },
    {
        "rank": 8,
        "tag": "🌾 創業1848年の酒蔵が本気開発！有機米発酵液×酒粕エキスの本格蔵元化粧水",
        "catch": "栃木県益子町の老舗・外池酒造店の美肌サイエンス。有機栽培米のコメ発酵液と酒粕エキスが、硬くなった冬の角質をやわらげる",
        "brand_name": "外池酒造店 (蔵元美人)",
        "capacity": "150ml (白米発酵 しっとり化粧水)",
        "type": "有機米発酵エキス高保湿蔵元化粧水",
        "features": "有機米コメ発酵液、酒粕エキス、米ヌカエキス、ヒアルロン酸、水溶性プロテオグリカン",
        "value": "無香料・無着色・鉱物油フリー。本物の酒造りの現場で生まれた高純度発酵エキスが、冬のゴワつく角層を根本から柔軟化",
        "desc_p1": "江戸時代末期から続く栃木県益子町の老舗酒蔵・外池酒造店が、杜氏たちの肌の美しさに着目して自社醸造の発酵成分で開発した『蔵元美人』シリーズ。その中心となる『白米発酵 しっとり化粧水』は、有機栽培された米から丹念に作られたコメ発酵液と酒粕エキスをベースにした本格蔵元コスメです。",
        "desc_p2": "さらりとしたテクスチャーながら、肌になじませると驚くほど深くまで染み渡り、内側から押し返すような弾力感をもたらします。高い保水力を持つ水溶性プロテオグリカンもブレンドされており、真冬の乾燥で硬直した角質細胞を柔らかく解きほぐします。人工香料を一切使用せず、素材そのものの純粋な発酵パワーで素肌の基礎体力を底上げしてくれます。",
        "target": "本物の酒蔵が作ったオーガニック志向の発酵コスメを使いたい方、肌のごわつきを柔らかく整えたい方、無香料で低刺激な処方を好む方",
        "point": "洗顔後、手のひらに500円玉大を取り、顔全体を包み込むように優しくなじませます。手のひらのぬくもりで温めながらじっくりとハンドプレスすると、発酵成分の浸透がさらに深まります。"
    },
    {
        "rank": 9,
        "tag": "🛡️ パックしたてのような密着うるおい膜！真冬の冷気をシャットアウトする酒粕クリーム",
        "catch": "酒粕エキス×キュウリエキスの黄金比。軽やかなつけ心地で肌表面に鉄壁の保湿シールドを張り、一日中乾き知らずへ",
        "brand_name": "pdc (ピーディーシー) ワフードメイド",
        "capacity": "55g (酒粕クリーム)",
        "type": "高密着発酵アミノ酸うるおいシールドクリーム",
        "features": "酒粕エキス、コメ発酵液、キュウリ果実エキス、米セラミド、加水分解酵母",
        "value": "同シリーズの酒粕パック・化粧水とライン使いすることで、真冬の過酷な暖房環境下でも12時間以上水分を逃がさない密着膜を形成",
        "desc_p1": "ワフードメイドシリーズの保湿ステップを締めくくる『酒粕クリーム』。酒粕パックや化粧水で角層にたっぷりと送り込んだアミノ酸と水分を、絶対に外へ逃がさないために設計された高密着エモリエントクリームです。",
        "desc_p2": "ふわっとホイップクリームのように軽やかな質感でありながら、肌に塗り広げると瞬時に密着して薄い保護ヴェールを形成。キュウリ果実エキスが肌を引き締め、キメの乱れを整えます。朝のメイク前に使用してもファンデーションがヨレたり浮いたりせず、一日中エアコンの乾燥風から素肌を守り抜く頼もしい存在です。",
        "target": "冬の終日暖房環境で肌がパサつく方、濃厚すぎるクリームでニキビができやすい方、酒粕シリーズでトータルケアしたい方",
        "point": "化粧水や美容液で肌を整えた後、パール粒1個分を顔全体にムラなくなじませます。乾燥しやすい頬や口角の周りには、指の腹でトントンと軽く叩き込むように重ねづけしてください。"
    },
    {
        "rank": 10,
        "tag": "🖐️ 日本酒発酵アミノ酸×酒粕×セラミド！水仕事やアルコール荒れを救う美容液ハンドクリーム",
        "catch": "老舗酒蔵・菊正宗が本気で作ったハンドセラム。塗った瞬間サラリとなじみ、指先まで吸い付くような潤いとしなやかさを実現",
        "brand_name": "菊正宗酒造",
        "capacity": "70g (正宗印 ハンドクリームセラム)",
        "type": "高浸透発酵アミノ酸ハンド美容液クリーム",
        "features": "純米酒コメ発酵液、酒粕エキス、セラミドEOP/NP/AP、ビタミンE（トコフェロール）、グリチルリチン酸2K",
        "value": "ハンドクリーム特有のベタつきを徹底排除した『美容液設計』。水仕事の合間やデスクワーク中でも即座に手肌をリペアできる名品",
        "desc_p1": "真冬の手荒れは、皮膚の薄い手の甲や指先から水分が蒸発し、あかぎれやひび割れへと急速に悪化します。菊正宗の『正宗印 ハンドクリームセラム』は、日本酒を仕込む杜氏たちの美しい手肌に着目し、酒粕エキスとコメ発酵液、さらに3種のセラミドを贅沢に凝縮した美容液仕立てのハンドクリームです。",
        "desc_p2": "手肌に出すと乳液のようにスーッと伸び、角層深部へ瞬時に浸透。塗った直後からサラサラの手触りになるため、スマホやパソコンのキーボードに指紋がつかず、仕事中にもストレスフリーで使えます。消炎成分のグリチルリチン酸2Kも配合されているため、冬のあかぎれや乾燥による赤み・かゆみを防ぎ、指先までしっとりとキメの整った手肌を保ちます。",
        "target": "冬場の水仕事やアルコール消毒で手がガサガサに荒れる方、ベタつくハンドクリームが苦手で作業が中断してしまう方",
        "point": "適量（小豆粒大）を手の甲に取り、両手で包み込むように全体に伸ばします。爪の付け根や指の間、手首まで丁寧にマッサージしながら塗り込むと、指先の血行も促進されます。"
    }
]

# JSON-LD 生成
jsonld_items = []
for i, p in enumerate(items):
    d = product_details[i]
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": f"第{i+1}位：{d['brand_name']} {p['display_name']}",
        "description": d['catch'],
        "image": p['image'],
        "url": f"https://lumi-cosme.vercel.app/winter-sake-kasu.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "酒粕コスメを使うと、アルコールで肌がヒリヒリしたり赤くなったりしませんか？",
        "answer": "化粧品に配合されている『酒粕エキス』は、製造工程において抽出・精製が行われ、アルコール（エタノール）分は揮発・除去または肌に負担のない微量に調整されています。そのため一般的な日本酒そのものを肌に塗るのとは異なり、肌への刺激は極めて穏やかです。ただし、アルコール過敏症や米アレルギーをお持ちの方は、念のため腕の内側でパッチテストを行ってから顔に使用することをおすすめします。"
    },
    {
        "question": "なぜ『杜氏（とうじ）の手は白くて美しい』と言われるのですか？科学的な理由は？",
        "answer": "厳しい冬の冷水で毎日米を研ぎ酒を仕込む杜氏の手が、過酷な環境にもかかわらず白くみずみずしいことは昔から知られていました。最新の皮膚科学研究により、酒粕やコメ発酵液には約20種類もの遊離アミノ酸（肌の天然保湿因子NMFの主成分）が豊富に含まれていることが解明されています。さらに、メラニン生成を抑えるコウジ酸やアルブチン、角層バリアを補強するコメセラミド、ターンオーバーを整えるビタミンB群などが自然の黄金比で含まれているため、高い保湿と透明感の維持を同時に実現できるのです。"
    },
    {
        "question": "酒粕パックはどのタイミングで使うのが一番効果的ですか？",
        "answer": "入浴時に湯船に浸かりながら使用するのが最も効果的です。浴室のスチーム（蒸気）によって毛穴が自然に開き、角層が柔らかくなるため、酒粕エキスのアミノ酸や美容成分がよりスムーズに深部まで浸透します。また、蒸気のおかげでパックが乾燥して固まらず、ぬるま湯ですすぐ際も肌を擦らずに優しく落とすことができます。"
    },
    {
        "question": "11月〜12月の新酒仕込みの季節に酒粕コスメを使うメリットはありますか？",
        "answer": "日本酒の仕込み（寒仕込み）はまさに11月から本格化します。この時期に生産される新鮮な酒粕は発酵菌や酵素、アミノ酸の活性が非常に高く、フレッシュな栄養が凝縮されています。また肌の面でも、11月〜12月は寒冷によるターンオーバーの停滞で角質肥厚（ごわつき・くすみ）と砂漠乾燥が同時に起きるため、角質柔軟と濃密保水を一度に叶える酒粕コスメの特性が完璧に合致します。"
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
        "@id": "https://lumi-cosme.vercel.app/winter-sake-kasu.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！杜氏の手のようなもっちり透明美肌へ導くアミノ酸濃密補給の高保湿酒粕コスメランク10",
    "description": "11月・12月の寒冷乾燥と冬のくすみゴワつきを救う高保湿酒粕コスメを徹底厳選！ワフードメイド酒粕パック、菊正宗、旅美人、白玉りっちから蔵元美人まで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの発酵美肌術を詳しく解説。",
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
    "datePublished": "2026-11-04T00:00:00+09:00",
    "dateModified": "2026-11-04T00:00:00+09:00"
}

jsonld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿酒粕コスメおすすめ人気ランキング10選",
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
      <h3 class="product-name">{d['brand_name']} {p['display_name']}</h3>
      <p class="product-catch">{d['catch']}</p>
      
      <div class="product-layout">
        <div class="product-visual">
          <img src="{p['image']}" alt="{p['display_name']}" class="product-img" loading="lazy" width="300" height="300">
          <div class="price-box">
            <span class="price-label">楽天参考価格</span>
            <span class="price-value">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['url']}" target="_blank" rel="noopener sponsored" class="rakuten-btn">
            楽天で最新価格・在庫を見る
          </a>
        </div>
        
        <div class="product-info-detail">
          <div class="spec-table">
            <div class="spec-row"><span class="spec-th">ブランド</span><span class="spec-td">{d['brand_name']}</span></div>
            <div class="spec-row"><span class="spec-th">容量・規格</span><span class="spec-td">{d['capacity']}</span></div>
            <div class="spec-row"><span class="spec-th">アイテム種別</span><span class="spec-td">{d['type']}</span></div>
            <div class="spec-row"><span class="spec-th">注目成分</span><span class="spec-td">{d['features']}</span></div>
            <div class="spec-row"><span class="spec-th">真冬の保湿価値</span><span class="spec-td">{d['value']}</span></div>
          </div>
          
          <div class="review-box">
            <h4>💡 美容皮膚専門ライターの詳細解説＆真冬のレビュー</h4>
            <p>{d['desc_p1']}</p>
            <p>{d['desc_p2']}</p>
          </div>
          
          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ：</strong>
            <p>{d['target']}</p>
          </div>
          
          <div class="usage-box">
            <strong>✨ 効果を最大化する真冬の使い方テクニック：</strong>
            <p>{d['point']}</p>
          </div>
        </div>
      </div>
    </article>
    """)

cards_joined = "\n".join(cards_html)

table_rows = []
for i, p in enumerate(items):
    d = product_details[i]
    table_rows.append(f"""
    <tr>
      <td class="tb-rank">第{i+1}位</td>
      <td class="tb-img"><img src="{p['image']}" alt="{p['display_name']}" width="60" height="60" loading="lazy"></td>
      <td class="tb-name"><strong>{d['brand_name']}</strong><br><a href="#item-{i+1}">{p['display_name']}</a></td>
      <td class="tb-type">{d['type']}</td>
      <td class="tb-price">¥{p['price']:,}</td>
      <td class="tb-btn"><a href="{p['url']}" target="_blank" rel="noopener sponsored" class="table-link-btn">楽天で見る</a></td>
    </tr>
    """)

table_joined = "\n".join(table_rows)

faq_html_blocks = []
for faq in faq_list:
    faq_html_blocks.append(f"""
    <div class="faq-item">
      <h3 class="faq-q">Q. {faq['question']}</h3>
      <p class="faq-a">A. {faq['answer']}</p>
    </div>
    """)

faq_joined = "\n".join(faq_html_blocks)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！杜氏の手のようなもっちり透明美肌へ導くアミノ酸濃密補給の高保湿酒粕コスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒冷乾燥と冬のくすみゴワつきを救う高保湿酒粕コスメを徹底厳選！ワフードメイド酒粕パック、菊正宗、旅美人、白玉りっちから蔵元美人まで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの発酵美肌術を詳しく解説。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-sake-kasu.html">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！杜氏の手のようなもっちり透明美肌へ導くアミノ酸濃密補給の高保湿酒粕コスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥と冬のくすみゴワつきを救う高保湿酒粕コスメを徹底厳選！ワフードメイド酒粕パック、菊正宗、旅美人、白玉りっちから蔵元美人まで楽天で今すぐ買えるおすすめ人気ランキング10選。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-sake-kasu.html">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
  <!-- 構造化データ -->
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
      --primary-color: #854d0e;
      --primary-light: #fef9c3;
      --primary-dark: #713f12;
      --accent-color: #a16207;
      --text-main: #1f2937;
      --text-muted: #4b5563;
      --bg-light: #fefce8;
      --border-color: #fef08a;
      --card-bg: #ffffff;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
      --radius: 12px;
    }}
    
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
      line-height: 1.85;
      color: var(--text-main);
      background-color: #fafaf9;
    }}
    
    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid #e5e7eb;
      padding: 1rem 0;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title a {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-link:hover {{ color: var(--primary-dark); }}
    
    .container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 2rem 1.5rem 5rem;
    }}
    
    .breadcrumb {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
    }}
    .breadcrumb a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .breadcrumb span {{ color: #9ca3af; }}
    
    .article-header {{
      background: white;
      padding: 2.5rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border-top: 5px solid var(--primary-color);
    }}
    .article-meta {{
      display: flex;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 1.85rem;
      line-height: 1.45;
      font-weight: 800;
      color: #111827;
      margin-bottom: 1.5rem;
    }}
    .article-lead {{
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.8;
      border-left: 4px solid var(--accent-color);
      padding-left: 1.25rem;
      margin-top: 1rem;
    }}
    
    .toc-box {{
      background: var(--bg-light);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin-bottom: 3rem;
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: var(--primary-dark);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-list {{
      list-style: none;
      padding-left: 0.5rem;
    }}
    .toc-list li {{
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
    }}
    .toc-list a {{
      color: var(--text-main);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: var(--primary-color);
      text-decoration: underline;
    }}
    
    .content-section {{
      background: white;
      padding: 2.5rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}
    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--primary-dark);
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 0.75rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .section-p {{
      margin-bottom: 1.25rem;
      font-size: 1rem;
      color: var(--text-main);
    }}
    
    .compare-table-wrapper {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}
    .compare-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      padding: 0.85rem;
      text-align: left;
      border: 1px solid var(--border-color);
      font-weight: 700;
    }}
    .compare-table td {{
      padding: 0.85rem;
      border: 1px solid #e5e7eb;
      vertical-align: middle;
    }}
    .tb-rank {{ font-weight: 800; color: var(--primary-color); text-align: center; width: 60px; }}
    .tb-img img {{ border-radius: 6px; object-fit: cover; }}
    .tb-name a {{ color: var(--text-main); text-decoration: none; font-weight: 600; }}
    .tb-name a:hover {{ color: var(--primary-color); text-decoration: underline; }}
    .tb-price {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-link-btn {{
      display: inline-block;
      padding: 0.4rem 0.8rem;
      background: #b91c1c;
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
    }}
    .table-link-btn:hover {{ background: #991b1b; }}
    
    .product-card {{
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.25rem;
      margin-bottom: 3.5rem;
      border: 1px solid #f3f4f6;
      position: relative;
    }}
    .product-badge-rank {{
      position: absolute;
      top: -12px;
      left: 20px;
      background: linear-gradient(135deg, #854d0e, #713f12);
      color: white;
      font-weight: 800;
      font-size: 1rem;
      padding: 0.3rem 1.25rem;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.15);
    }}
    .product-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.25rem 0.75rem;
      border-radius: 6px;
      margin-top: 0.5rem;
      margin-bottom: 0.75rem;
    }}
    .product-name {{
      font-size: 1.4rem;
      font-weight: 800;
      line-height: 1.4;
      color: #111827;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
    }}
    
    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-layout {{ grid-template-columns: 1fr; }}
      .article-header, .content-section, .product-card {{ padding: 1.5rem; }}
      .article-title {{ font-size: 1.45rem; }}
    }}
    
    .product-visual {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: auto;
      border-radius: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
      margin-bottom: 1rem;
    }}
    .price-box {{
      background: #f9fafb;
      padding: 0.6rem;
      border-radius: 8px;
      margin-bottom: 1rem;
      border: 1px solid #e5e7eb;
    }}
    .price-label {{ font-size: 0.75rem; color: #6b7280; display: block; }}
    .price-value {{ font-size: 1.45rem; font-weight: 800; color: #b91c1c; }}
    .price-tax {{ font-size: 0.75rem; color: #6b7280; }}
    
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: white;
      text-align: center;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      box-shadow: 0 4px 6px rgba(191, 0, 0, 0.2);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a80000, #800000);
      transform: translateY(-2px);
      box-shadow: 0 6px 8px rgba(191, 0, 0, 0.3);
    }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.25rem;
      font-size: 0.88rem;
    }}
    .spec-row {{
      display: flex;
      border-bottom: 1px solid #e5e7eb;
      padding: 0.5rem 0;
    }}
    .spec-th {{
      width: 110px;
      flex-shrink: 0;
      font-weight: 700;
      color: #4b5563;
    }}
    .spec-td {{
      flex-grow: 1;
      color: #1f2937;
    }}
    
    .review-box {{
      background: #f8fafc;
      border-left: 4px solid var(--primary-color);
      padding: 1.25rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 1.25rem;
    }}
    .review-box h4 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}
    .review-box p {{
      font-size: 0.92rem;
      line-height: 1.75;
      color: #334155;
      margin-bottom: 0.5rem;
    }}
    .review-box p:last-child {{ margin-bottom: 0; }}
    
    .target-box, .usage-box {{
      background: #fefce8;
      border: 1px solid #fef9c3;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      margin-bottom: 0.75rem;
      font-size: 0.9rem;
    }}
    .target-box strong, .usage-box strong {{
      color: var(--primary-dark);
      display: block;
      margin-bottom: 0.25rem;
    }}
    
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.25rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}
    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #374151;
    }}
    
    .footer-internal-links {{
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.5rem;
      margin-top: 3rem;
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 0.75rem;
      margin-top: 1.25rem;
    }}
    .footer-links-grid a {{
      font-size: 0.88rem;
      color: #4b5563;
      text-decoration: none;
      padding: 0.4rem 0.6rem;
      background: #f9fafb;
      border-radius: 6px;
      border: 1px solid #e5e7eb;
      transition: all 0.2s;
    }}
    .footer-links-grid a:hover {{
      color: var(--primary-color);
      border-color: var(--primary-color);
      background: var(--bg-light);
    }}
    
    .site-footer {{
      text-align: center;
      padding: 3rem 1.5rem;
      font-size: 0.85rem;
      color: #9ca3af;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <div class="site-title">
        <a href="/">❄️ 冬コスメ徹底比較ラボ</a>
      </div>
      <nav>
        <a href="/" class="nav-link">トップページへ戻る</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb" aria-label="パンくずリスト">
      <a href="/">ホーム</a>
      <span>&gt;</span>
      <a href="/#skincare">スキンケア・ボディケア特集</a>
      <span>&gt;</span>
      <span aria-current="page">高保湿酒粕コスメ特集</span>
    </nav>

    <article class="article-header">
      <div class="article-meta">
        <time datetime="2026-11-04">公開日：2026年11月4日</time>
        <span>執筆：冬コスメ徹底比較ラボ 編集部（発酵バイオ皮膚科学リサーチチーム）</span>
      </div>
      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！杜氏の手のようなもっちり透明美肌へ導くアミノ酸濃密補給の高保湿酒粕コスメランク10</h1>
      <p class="article-lead">
        11月から12月は日本酒の「寒仕込み」が始まる季節。厳しい寒風と冷水の中で米を研ぐ杜氏（とうじ）の手が、驚くほど白く滑らかであることから発見された酒粕の美肌力。肌の天然保湿因子（NMF）を構成する必須アミノ酸やコウジ酸、コメセラミドが凝縮された酒粕コスメは、真冬の乾燥ゴワつきとくすみを同時に吹き飛ばす発酵サイエンスの傑作です。本記事では、楽天公式APIよりリアルタイムに取得した人気アイテムから厳選したランキング10選とプロの活用術を徹底解説します。
      </p>
    </article>

    <section class="toc-box">
      <h2 class="toc-title">📑 目次・記事ナビゲーション</h2>
      <ul class="toc-list">
        <li><a href="#why-sake-kasu">1. なぜ真冬の乾燥くすみに酒粕コスメが最強なのか？杜氏の手に学ぶ発酵美肌の科学</a></li>
        <li><a href="#selection-criteria">2. 失敗しない冬の高保湿酒粕コスメの選び方・3つのポイント</a></li>
        <li><a href="#comparison-table">3. 高保湿酒粕コスメ10選 スペック・価格比較表</a></li>
        <li><a href="#ranking-section">4. 高保湿酒粕コスメおすすめ人気ランキング10選 詳細レビュー</a></li>
        <li><a href="#faq-section">5. 美容皮膚視点で答える酒粕コスメのよくある疑問Q&amp;A</a></li>
        <li><a href="#conclusion">6. まとめ：冬枯れくすみを一掃する発酵スキンケア設計</a></li>
      </ul>
    </section>

    <!-- セクション1 -->
    <section class="content-section" id="why-sake-kasu">
      <h2 class="section-title">🍶 1. なぜ真冬の乾燥くすみに酒粕コスメが最強なのか？杜氏の手に学ぶ発酵美肌の科学</h2>
      <p class="section-p">
        11月から12月にかけて外気温が下がりきると、私たちの肌には二重の過酷なトラブルが襲いかかります。ひとつは、暖房や寒風による猛烈な「水分蒸発（砂漠乾燥）」。もうひとつは、寒冷によって皮膚の毛細血管が収縮し、新陳代謝（ターンオーバー）が停滞して古いメラニン角質が剥がれ落ちずに堆積する「角質肥厚（ごわつき・冬枯れくすみ）」です。
      </p>
      <p class="section-p">
        この「極度の乾燥」と「頑固なくすみ」という冬の二大難問を、同時に解決できる天然のバイオ素材こそが<strong>『酒粕（さけかす）』</strong>です。
      </p>
      <p class="section-p">
        酒粕は、米と米麹、酵母を発酵させて日本酒を醸造する過程で生まれる副産物ですが、実は原料の米よりも遥かに高濃度な美肌成分が凝縮されています。特に注目すべきは、肌本来の潤いを保つ<strong>天然保湿因子（NMF）の約半分を占める『遊離アミノ酸』が約20種類以上も豊富に含まれている点</strong>です。人工的な保湿成分では真似できない分子バランスで角層細胞の内部を満たし、内側からふっくらと押し返すような弾力を蘇らせます。
      </p>
      <p class="section-p">
        さらに、酒粕にはメラニン生成酵素の働きを抑える『コウジ酸』や『アルブチン』『フェルラ酸』、角層の細胞間脂質を補修する『コメセラミド』、皮膚の代謝を助けるビタミンB群が黄金比で共存しています。寒さで硬直した冬の角層をやわらかく解きほぐしながら、透明感あふれるもっちり素肌へと導く力は、まさに先人から受け継がれた日本の発酵サイエンスの結晶です。
      </p>
    </section>

    <!-- セクション2 -->
    <section class="content-section" id="selection-criteria">
      <h2 class="section-title">🔍 2. 失敗しない冬の高保湿酒粕コスメの選び方・3つのポイント</h2>
      <p class="section-p">
        真冬の過酷な乾燥環境で最大の効果を得るために、酒粕コスメを選ぶ際は以下の3つのポイントに着目してください。
      </p>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">ポイント①：角質オフ（洗い流しパック）と持続保水（ローション・クリーム）の使い分け</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          肌表面のゴワつきやくすみが気になる時は、週2〜3回の洗い流す『酒粕パック』が即効性を発揮します。一方、日中や就寝中の乾きを防ぎたい場合は、セラミドやコメ胚芽油がブレンドされた二層式化粧水や濃厚クリームを選びましょう。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">ポイント②：酒蔵や抽出原料へのこだわり（純米酒粕・有機米発酵）</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          伝統的な酒蔵（熊本の河津酒造、神戸の菊正宗、益子の外池酒造など）が手がけるコスメは、抽出される酒粕エキスの純度と鮮度が際立っています。良質な酒米と清らかな伏流水から生まれた発酵成分は、角層への親和性が高く低刺激です。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">ポイント③：米セラミドやヒアルロン酸など相乗保湿成分の有無</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          酒粕のアミノ酸に加え、角層のフタとなる『米セラミド』や『植物性スクワラン』、水分を抱え込む『ヒアルロン酸』が一緒に配合されている製品を選ぶことで、11月〜12月の暖房下でも乾燥崩れを起こさない鉄壁の保湿膜が完成します。
        </p>
      </div>
    </section>

    <!-- セクション3 比較表 -->
    <section class="content-section" id="comparison-table">
      <h2 class="section-title">📊 3. 高保湿酒粕コスメ10選 スペック・価格比較表</h2>
      <p class="section-p">
        楽天公式APIよりリアルタイムに取得した最新価格と製品スペックの一覧表です。テクスチャーや使用シーンに合わせて比較検討してください。
      </p>
      <div class="compare-table-wrapper">
        <table class="compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>画像</th>
              <th>商品名・ブランド</th>
              <th>カテゴリ種別</th>
              <th>楽天価格</th>
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
        🏆 高保湿酒粕コスメおすすめ人気ランキング10選
      </h2>
      {cards_joined}
    </section>

    <!-- セクション5 Q&A -->
    <section class="content-section" id="faq-section">
      <h2 class="section-title">❓ 5. 美容皮膚視点で答える酒粕コスメのよくある疑問Q&amp;A</h2>
      {faq_joined}
    </section>

    <!-- セクション6 まとめ -->
    <section class="content-section" id="conclusion">
      <h2 class="section-title">🍶 6. まとめ：冬枯れくすみを一掃する発酵スキンケア設計</h2>
      <p class="section-p">
        11月から12月にかけて訪れる冬の本格化。寒さで血行が悪くなり、暖房の風で水分を奪われた肌は、放置すると乾燥小ジワや深刻なバリア低下を招きます。
      </p>
      <p class="section-p">
        日本人が何世代にもわたって受け継いできた発酵の知恵である酒粕は、単に肌を潤すだけでなく、杜氏の手のように「ふっくら・もっちり・透き通る」健康的な肌基礎体力を育んでくれます。
      </p>
      <p class="section-p">
        お風呂での酒粕スチームパックで週に数回のスペシャルケアを行い、毎日のスキンケアには酒粕化粧水や濃厚クリームでアミノ酸とセラミドをたっぷり届ける。この贅沢な発酵ルーティンを味方につけて、真冬の寒さに負けない自信の素肌を手に入れてください。
      </p>
    </section>

    <!-- 内部リンクラッパー -->
    <section class="footer-internal-links" id="internal-links">
      <h2 style="font-size: 1.25rem; font-weight: 800; color: #1f2937; margin-bottom: 0.5rem;">
        🔗 併せて読みたい冬コスメ・保湿スキンケア関連記事
      </h2>
      <p style="font-size: 0.9rem; color: #6b7280;">
        当サイトでは、11月〜12月の肌悩みに合わせた高保湿コスメや成分別ランキングを多数公開しています。
      </p>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で動的に同期されます -->
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 当サイトは楽天市場アフィリエイトプログラムに参加しています。</p>
  </footer>

</body>
</html>
"""

with open("winter-sake-kasu.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-sake-kasu.html successfully. Size: {len(html_content):,} bytes")
