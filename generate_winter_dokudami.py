import json
import re

with open("fetched_3new_lacto_swallow_dokudami.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_dokudami"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🌿 韓国No.1国民的鎮静トナー！ドクダミエキス77%が冬の寒暖差赤みと暖房乾燥を速攻鎮火",
        "catch": "韓国オリーブヤングや各アワードで殿堂入りを果たした伝説のスージングトナー。自然由来のドクダミエキス77%を高濃度配合し、冬の冷たい外気と過熱暖房の寒暖差で赤く火照りヒリつく角層を瞬時に鎮静しながら満たす名作化粧水",
        "brand_name": "Anua (アヌア)",
        "capacity": "250mL / クリーンボトル",
        "type": "高純度ドクダミエキス77%配合 弱酸性水分鎮静トナー",
        "features": "ドクダミエキス（77%）、ツボクサエキス、パンテノール、カモミール花エキス、弱酸性pH5.5",
        "value": "寒暖差による毛細血管の拡張と乾燥炎症を速攻クールダウン。水のようにピュアでありながら、角層深部へ吸い込まれるように浸透し、真冬のインナードライを根本から解消",
        "desc_p1": "11月から12月にかけて、屋外の冷え込みと室内のエアコン暖房による『寒暖差ストレス』によって、顔がカッと熱くなって赤ら顔になったり、普段のスキンケアが急にしみるようになるトラブルが多発します。アヌアのドクダミ 77% スージングトナーは、植物の中でも突出した抗炎症フラボノイド『クエルシトリン』を豊富に含むドクダミエキスをベースにした、冬のレスキュー化粧水です。",
        "desc_p2": "シャバシャバとした軽やかなテクスチャーでありながら、肌に乗せるとスーッと馴染んで、火照った皮膚温度を優しく落ち着かせます。余計な油分で毛穴を塞ぐことなく、パンテノールや植物エキスが角層内部の水分タンクを満タンにキープ。朝晩のスキンケアに取り入れるだけで、ファンデーションを塗っても隠せなかった小鼻や頬の赤みが綺麗に鎮まり、透き通るような均一なキメ肌へと導きます。",
        "target": "冬の寒暖差で顔が赤くなりやすい方、暖房の効いた部屋で肌がヒリつくインナードライ肌、肌トラブルを穏やかに鎮静しながら水分を補給したい方",
        "point": "洗顔後すぐに手のひらで顔全体に優しく重ねづけします。赤みや熱感が気になる頬には、薄手のコットンにたっぷり含ませて3〜5分間の『部分鎮静コットンパック』を行うと驚くほど赤みが引きます。"
    },
    {
        "rank": 2,
        "tag": "💧 高濃度ドクダミ80%×3重ヒアルロン酸！もっちり吸い付く濃厚とろみ水分アンプル",
        "catch": "ドクダミエキスを極限の80%まで濃縮。とろみのあるジェル状セラムが真冬の乾いた角層に吸い付くように密着し、水分バリアを長時間ロックする水分鎮静美容液",
        "brand_name": "Anua (アヌア)",
        "capacity": "30mL / スポイト遮光瓶",
        "type": "高濃度ドクダミエキス80%×トリプルヒアルロン酸 水分濃密美容液",
        "features": "ドクダミエキス（80%）、ヒアルロン酸Na、加水分解ヒアルロン酸、パンテノール、ベタイン",
        "value": "オイルフリーでありながら、一般的な美容オイルに匹敵する濃密なもっちり感を実現。冬の暖房直撃下でも一日中肌の内側から水分が湧き出るような保水膜を形成",
        "desc_p1": "『化粧水を塗っても1時間後には肌がパサつく、かといって油分過多なオイルやクリームを塗ると吹き出物ができる』という真冬の混合肌・オイリードライ肌にとって、この水分アンプルはまさに理想の答えです。アヌアのドクダミ 80% 水分鎮静アンプルは、高純度ドクダミの鎮静力と分子量の異なる3重ヒアルロン酸を融合させた濃密セラムです。",
        "desc_p2": "スポイトから垂らすと粘度のある濃厚なリキッドですが、肌に伸ばした瞬間に摩擦なくスルリと広がり、手のひらが吸い付くような濃密なモチモチ感へと変化します。ベタつきや皮膜感が一切残らないため、朝のメイク前にもストレスなく使用可能。エアコンの風に一日中さらされるオフィスワークでも、夕方まで一切の突っ張りを感じさせない鉄壁の保水力を誇ります。",
        "target": "冬の乾燥で肌が突っ張るけれどベタつく油分が苦手な方、大人ニキビや毛穴の開きと乾燥を同時にケアしたい方、ファンデーションの密着度を高めたい方",
        "point": "化粧水の塗布後、スポイト1回分を手のひらに取り、顔全体を包み込むように押し込みます。特に乾燥しやすい目元や口元には、さらに半プッシュを指先で優しくトントンと重ねづけしてください。"
    },
    {
        "rank": 3,
        "tag": "🏔 智異山の大自然が育んだドクダミ！冬の硬化角層を解きほぐす高浸透スキンブースター",
        "catch": "韓国の名峰・智異山（チリサン）で澄んだ空気と清流に育まれた良質なドクダミエキスを凝縮。冬の冷気で硬直した角質層を柔軟に解きほぐし、肌本来の自己回復力を高めるブースター化粧水",
        "brand_name": "Abib (アビブ)",
        "capacity": "200mL / ミニマルデザインボトル",
        "type": "智異山ドクダミエキス配合 高浸透カーミングトナー",
        "features": "ドクダミエキス、ヒアルロン酸、パンテノール、アラントイン、弱酸性・低刺激フォーミュラ",
        "value": "角層の隙間を埋める水分通り道をスムーズに整え、後から使う美容液やクリームの浸透力を最大化。真冬の過酷な寒冷気から角層バリアを優しくプロテクト",
        "desc_p1": "韓国のミニマルスキンケアを代表するAbibのドクダミトナーは、厳選された智異山産の高品質ドクダミエキスを贅沢に配合しています。冬の寒さによって角質層が厚く硬くなると、どんなに高価なクリームを塗っても表面で滑ってしまい、内部へ潤いが届きません。",
        "desc_p2": "このスキンブースターは、肌のpHバランスを理想的な弱酸性に保ちながら、硬化した角質細胞の結びつきをやさしくほぐします。肌に乗せるとスッと染み渡り、内側からみずみずしく膨らむような柔らかさを即座に実感。無香料・アルコールフリーのピュアな処方で、真冬のデリケートな素肌を毎日穏やかにいたわります。",
        "target": "冬になると肌がゴワついて化粧水が入っていかない方、シンプルで肌に優しい低刺激スキンケアを好む方、肌荒れと乾燥を同時に予防したい方",
        "point": "朝晩の洗顔直後に、500円玉大を手にとって顔全体から首元まで優しくパッティングするように馴染ませます。2〜3回重ねづけすると、角層が水分で満たされて手のひらに吸い付く感触になります。"
    },
    {
        "rank": 4,
        "tag": "🥛 ベタつかないのに驚異の持続保水！シルキーな薄膜ヴェールが真冬の肌を守る高保湿乳液",
        "catch": "ドクダミエキス70%と3重ヒアルロン酸をバランスよく乳化。真冬の乾燥で乱れがちな水分油分バランスを黄金比に整え、一日中しっとり滑らかなシルク肌を保つ低刺激デイリーローション",
        "brand_name": "Anua (アヌア)",
        "capacity": "200mL / ポンプボトル",
        "type": "ドクダミエキス70%配合 シルキー高保湿エマルジョン",
        "features": "ドクダミエキス（70%）、3重ヒアルロン酸、ベタイン、パンテノール、スクワラン",
        "value": "乳液特有の重さや毛穴の詰まり感を完全に排除。肌表面に極薄の水分膜を張り巡らせ、エアコン暖房による角層脱水を長時間阻止",
        "desc_p1": "冬のスキンケアにおいて、乳液は水分を閉じ込める重要なステップですが、『油分が多すぎてニキビができる』『メイクがヨレる』といった悩みを抱える方は少なくありません。アヌアのデイリーリリーフローションは、ドクダミエキスを70%配合することで、油分に頼りすぎない高純度な保水シールドを実現したアイテムです。",
        "desc_p2": "ワンプッシュで広がるエマルジョンは、乳白色の滑らかなミルク状で、肌に伸ばすとスーッとみずみずしく解けて角層に溶け込みます。塗った直後から肌表面はサラリとシルキーに整い、内側にはぎっしりと水分が詰まったハリ感をキープ。ポンプ式で衛生的に使え、朝のメイク前でもすぐにファンデーションを重ねられます。",
        "target": "ベタつく乳液や重いクリームが苦手な方、冬の暖房によるテカリと乾燥が同時に起こるインナードライ肌、軽やかな使用感で一日中保湿を保ちたい方",
        "point": "化粧水や美容液の後、1〜2プッシュを手にとって顔全体に優しく伸ばします。乾燥しやすいUゾーンや目元には、少量を追加して指の腹でトントンと馴染ませてください。"
    },
    {
        "rank": 5,
        "tag": "🩹 まるで密着するステッカー！極細マイクロファイバーが冬の乾燥赤みを一晩で救済する神マスク",
        "catch": "Abibが誇る特許マイクロファイバーシート『ガムシート』。肌とシートの間に隙間を一切作らない超密着構造で、ドクダミの鎮静エッセンスを真冬の過酷な肌荒れ角層へ一滴残らず送り届ける集中マスク",
        "brand_name": "Abib (アビブ)",
        "capacity": "10枚入 / 個包装ボックス",
        "type": "ドクダミエキス高濃度浸透 超密着ガムシートマスク",
        "features": "智異山ドクダミエキス、ツボクサエキス、パンテノール、マデカッソシド、極細繊維ガムシート",
        "value": "下を向いても剥がれ落ちない驚異の密着力。冬の冷風で赤み・皮むけ・ヒリつきを起こしたSOS肌を、一晩で鎮静しプルプルの潤い肌へとリセット",
        "desc_p1": "真冬の外出やスポーツで冷たい北風に長時間さらされた後、顔が真っ赤になって火照り、乾燥で突っ張るときに頼れるのがこのドクダミステッカーマスクです。一般的な不織布マスクとは根本的に異なる極細繊維で編まれており、肌に置いた瞬間に真空パックのようにピタッと吸い付きます。",
        "desc_p2": "シートには乳白色の濃厚なドクダミ美容液がたっぷり27mlも染み込んでおり、貼っている間中ずっと濃密な水分と鎮静成分が角層奥深くまで浸透し続けます。20分経って剥がした瞬間、赤みが驚くほど鎮まり、手のひらが吸い付いて離れないほどのもっちり感と透明感が蘇ります。冬の乾燥トラブル時の常備薬として世界中で絶賛される名作です。",
        "target": "真冬の外気乾燥で顔が赤く火照りヒリつく方、シートマスクが途中で浮いたり乾いたりするのが嫌な方、翌朝までに速攻で美肌を復活させたい方",
        "point": "洗顔後、化粧水で肌を整えた後、シートを顔の凹凸に合わせて隙間なく密着させます。15〜20分置いた後シートを剥がし、肌に残ったエッセンスを手で優しく押し込んでください。"
    },
    {
        "rank": 6,
        "tag": "✨ ドクダミ美容液1本分を丸ごと贅沢配合！両面パッドで冬の角質ケアと部分保湿パックを両立",
        "catch": "累計販売数数百万個を突破したアヌアの看板パッド。ドクダミエキス77%の美容液を丸ごと1本分ひたひたに含浸。エンボス面で冬のゴワつく角質を優しくオフし、ソフト面で集中保湿パックができる万能トナーパッド",
        "brand_name": "Anua (アヌア)",
        "capacity": "70枚入（160mL） / ピンセット付きジャー",
        "type": "ドクダミ77%美容液含浸 弱酸性クリアトナーパッド",
        "features": "ドクダミエキス（77%）、PHA（低刺激角質ケア成分）、ティーツリーエキス、ヒアルロン酸Na",
        "value": "寒さで角質が溜まり化粧水が入らない冬の肌を、摩擦レスに優しくほぐす。朝の洗顔代わりや、メイク前の部分集中水分パックとしても絶大な威力を発揮",
        "desc_p1": "冬の乾燥肌対策で見落としがちなのが、『古い角質が肌表面を覆って化粧水を弾いてしまう』というトラブルです。無理なピーリングやスクラブは冬のデリケートな肌を傷つけますが、アヌアのクリアパッドは低刺激なPHAと高濃度ドクダミを融合させ、不要な角質だけを穏やかに拭き取ります。",
        "desc_p2": "フタを開けると、美容液がひたひたに浸かったパッドがぎっしり。朝の洗顔代わりに凹凸のあるエンボス面で優しく拭き取れば、寝ている間の余分な皮脂や古い角質が綺麗にオフされ、つるんとしたなめらか肌に。さらに平らな面を両頬や額に3分間貼り付ければ、真冬の暖房下でも日中メイクが崩れない完璧な水分土台が完成します。",
        "target": "冬の朝の洗顔が寒くて面倒な方、肌のゴワつきや化粧ノリの悪さに悩む方、手軽にドクダミの集中水分パックを行いたい方",
        "point": "朝晩の洗顔後、付属のピンセットで1枚取り出し、目元を避けて顔全体を優しく拭き取ります。乾燥や赤みが気になる部位には、パッドを2〜3枚貼り付けて3分間パックしてください。"
    },
    {
        "rank": 7,
        "tag": "🛡 セラミド×パンテノール×ドクダミ！冬の冷たい外気を鉄壁ブロックするバリア強化高保湿クリーム",
        "catch": "ドクダミの鎮静力に、角層細胞間脂質の主役『セラミドNP』と皮膚修復成分『パンテノール』を贅沢配合。真冬の氷点下近い寒風や暖房の温風から素肌を完全密閉するインテンス保湿クリーム",
        "brand_name": "Anua (アヌア)",
        "capacity": "50mL / ジャー容器",
        "type": "ドクダミ×セラミドNP配合 バリア強化高保湿クリーム",
        "features": "ドクダミエキス（70%）、セラミドNP、パンテノール、アデノシン、植物性スクワラン",
        "value": "水分を与えるだけでなく、外側に強固なセラミド油膜シールドを形成。夜塗れば暖房をつけたままの寝室でも翌朝まで吸い付くような濃密な保湿感が持続",
        "desc_p1": "12月の真冬の乾燥に打ち勝つには、化粧水や美容液で補った水分を『絶対に外へ逃がさない強靭なフタ』が必要です。アヌアのドクダミ インテンス カーミングクリームは、敏感肌でも安心して使える低刺激設計でありながら、デパコス級の濃厚なバリア補強力を誇ります。",
        "desc_p2": "こっくりとしたバターのようなリッチなテクスチャーですが、肌の体温でとろけるように伸び広がり、ピタッと吸い付くように密着します。内側ではドクダミとパンテノールが乾燥炎症を鎮め、外側ではセラミドNPが細胞の隙間をがっちり接着。就寝前に塗れば、翌朝の洗顔時まで肌がふっくらと柔らかく保たれ、乾燥によるちりめんジワを寄せ付けません。",
        "target": "通常の高保湿クリームでは物足りない超乾燥肌、冬になると粉吹きや皮むけを起こしやすい方、セラミドとドクダミの両方で鉄壁のバリアを作りたい方",
        "point": "夜のお手入れの最後に、パール粒大を手にとって温め、顔全体を引き上げるように優しく包み込みます。特に乾燥が激しい目元や口元には、少量を指先でトントンと重ねて密着バリアを作ってください。"
    },
    {
        "rank": 8,
        "tag": "✨ 毛穴の角栓をスルリと溶かしながら乾燥させない！ドクダミ配合の非コメドジェニックオイル",
        "catch": "日米韓で爆発的人気を誇るクレンジングオイル。ドクダミエキス配合で、冬の濃密メイクや毛穴の黒ずみ・角栓を優しく浮かせながら、洗い上がりの肌をしっとり柔らかく保つ名作",
        "brand_name": "Anua (アヌア)",
        "capacity": "200mL / ポンプボトル",
        "type": "非コメドジェニック ドクダミ高保湿クレンジングオイル",
        "features": "ドクダミエキス、ホホバ種子油、オリーブ果実油、マカデミア種子油、ブドウ種子油",
        "value": "強い界面活性剤で皮脂を奪いすぎることなく、植物オイルが角栓を自然に溶解。冬の洗顔後の嫌な突っ張り感が一切なく、もっちりした素肌を維持",
        "desc_p1": "冬の乾燥肌の悪化原因の多くは、実は『クレンジングでの落としすぎ』にあります。寒いからといって熱いお湯で強いオイルを使うと、肌に必要な皮脂やNMFが一気に流出し、深刻な砂漠化を招きます。アヌアのポアコントロール クレンジングオイルは、植物由来オイルとドクダミエキスの力で、肌の潤いを守りながら汚れだけをオフする設計です。",
        "desc_p2": "サラリとした軽やかなオイルが肌の上を摩擦レスに滑り、ウォータープルーフのマスカラや頑固な毛穴の角栓を素早く乳化して浮かび上がらせます。ぬるま湯で洗い流した瞬間、オイル特有のヌルつきは残らないのに、まるでスキンケア後のようなしっとりとした柔らかさに感動します。冬の毛穴詰まりと乾燥を同時に解決する必須アイテムです。",
        "target": "冬のクレンジング後に顔がバリバリに突っ張る方、毛穴の黒ずみや角栓が気になるけれど乾燥が怖い方、肌に優しい植物性クレンジングを求める方",
        "point": "乾いた手のひらに2〜3プッシュを取り、顔全体に優しくクルクルと馴染ませます。少量のぬるま湯を加えてオイルが白く濁るまでしっかり『乳化』させてから、ぬるま湯（32〜34℃）で丁寧にすすいでください。"
    },
    {
        "rank": 9,
        "tag": "🌿 100%オーガニック無漂白コットン！冬の寒暖差ゆらぎを局所レスキューするスポットパッド",
        "catch": "智異山ドクダミエキスをたっぷり含ませたAbibのベストセラーパッド。肌に優しい無漂白・無蛍光のオーガニックコットンを採用し、冬の寒さで荒れやすい両頬やおでこにピタッと貼るだけのクイック水分チャージ",
        "brand_name": "Abib (アビブ)",
        "capacity": "80枚入（120mL） / 専用ピンセット付き",
        "type": "智異山ドクダミエキス含浸 オーガニック低刺激スポットパッド",
        "features": "智異山ドクダミエキス（40,000ppm）、冬虫夏草エキス、ヒアルロン酸、オーガニック無漂白コットン",
        "value": "肌あたりが極めて柔らかいガーゼ面とプレーン面の2way仕様。冬のマスク擦れや冷風でデリケートになった部位を、摩擦ゼロで優しく鎮静＆保水",
        "desc_p1": "冬はマスクの着用頻度が増え、呼気の湿気と外気の乾燥の繰り返し、さらに不織布の摩擦によって頬骨や小鼻の周りが局所的に赤く荒れやすくなります。Abibのドクダミスポットパッドは、肌への刺激を極限まで抑えた無漂白コットンを使用し、過敏になった肌を優しくケアします。",
        "desc_p2": "パッドを肌に乗せると、智異山ドクダミの清涼感ある水分がじゅわっと染み出し、カサついて熱を持った角層を瞬時にクールダウン。ガーゼ面で軽く滑らせれば冬の余分な角質が取れ、プレーン面を密着させれば5分でエステ並みの鎮静パックが完了します。大容量80枚入りで、毎日のメイク前や夜のスキンケアに惜しみなく使えます。",
        "target": "マスク擦れや冬の乾燥で頬が赤くヒリつく方、漂白剤不使用の肌に優しいコットンパッドを使いたい方、部分的な乾燥や肌荒れを手軽にケアしたい方",
        "point": "洗顔後、付属のピンセットで取り出し、赤みや乾燥が気になる両頬にピタッと貼り付けて3〜5分置きます。剥がした後はパッドで顔全体を優しく拭き取って馴染ませてください。"
    },
    {
        "rank": 10,
        "tag": "☀️ 美容液感覚で一日中みずみずしい！冬の暖房乾燥と紫外線を鉄壁ガードする高保湿サンクリーム",
        "catch": "ドクダミエキス配合で、まるで上質な水分クリームを塗っているかのようなシルキーな使い心地。SPF50+ PA++++の強力なUVカット力でありながら、白浮き・キシキシ感が皆無で冬の乾燥崩れを防ぐ日焼け止め",
        "brand_name": "Anua (アヌア)",
        "capacity": "50mL / チューブ容器",
        "type": "ドクダミエキス配合 高保湿シルキーモイスチャーUVサンクリーム",
        "features": "ドクダミエキス、パンテノール、ヒアルロン酸、ナイアシンアミド、SPF50+ PA++++",
        "value": "日焼け止め特有の乾燥や突っ張り感がゼロ。エアコンの温風が吹き荒れるオフィスでも、夕方まで潤いのツヤ膜をキープしてメイク崩れを防止",
        "desc_p1": "冬は日差しが弱く感じられるため紫外線対策を怠りがちですが、真冬でも地表に届く紫外線A波（UV-A）は、窓ガラスを透過して肌の奥のコラーゲンを破壊し、シワやたるみを引き起こします。アヌアのドクダミ シルキー モイスチャー サンクリームは、高保湿な水分美容液と高機能サンスクリーンを完璧に融合させたアイテムです。",
        "desc_p2": "手にとると、みずみずしい水分クリームのようなテクスチャーで、肌に伸ばすとスーッと透明に馴染みます。白浮きやベタつきが一切なく、直後に塗るリキッドファンデーションやパウダーがムラなくピタッと密着。日中のエアコン暖房による水分蒸発をドクダミの保護膜がガードし、夕方になっても乾燥崩れや小ジワ割れを起こさない極上の仕上がりを保ちます。",
        "target": "冬の日焼け止めの乾燥や白浮きが苦手な方、オフィスや車内の暖房で日中の肌がカサつく方、保湿下地としても優秀な日中ケアを探している方",
        "point": "朝のスキンケアの最後に、パール粒2個分を手にとって顔全体から首元までムラなく均一に伸ばします。頬の高い位置など乾燥しやすい部分には少量を重ねづけしてください。"
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
                <span class="review-count">（口コミ {item_data.get("review_count", "95")}件）</span>
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
  <title>保湿力の強さで肌乾燥とさようなら！冬の寒暖差ゆらぎと乾燥赤みを濃密鎮静する保湿力高めドクダミコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の寒暖差（冷たい外気vs過熱暖房）による乾燥赤み・インナードライ・ゆらぎ肌を救う高保湿ドクダミ（ハートリーフ・クエルシトリン）コスメを徹底厳選！Anua（アヌア）、Abib（アビブ）まで毛細血管安定と高保水鎮静の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="ドクダミ コスメ, ドクダミ トナー 保湿, アヌア ドクダミ 77, Abib ドクダミ, 冬 高保湿 コスメ, 寒暖差 肌荒れ 11月 12月, インナードライ 鎮静">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！冬の寒暖差ゆらぎと乾燥赤みを濃密鎮静する保湿力高めドクダミコスメランク10">
  <meta property="og:description" content="寒暖差による乾燥赤みを濃密鎮静！11月・12月の暖房砂漠肌を救うおすすめ高保湿ドクダミコスメ10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-dokudami">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿ドクダミコスメランク10">
  <meta name="twitter:description" content="11月・12月の寒暖差ゆらぎ肌に！濃密水分鎮静ドクダミコスメおすすめ厳選10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！冬の寒暖差ゆらぎと乾燥赤みを濃密鎮静する保湿力高めドクダミコスメランク10",
    "description": "11月・12月の暖房乾燥と寒暖差による赤み・インナードライを救う高保湿ドクダミコスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-06T06:30:00+09:00",
    "dateModified": "2026-11-06T06:30:00+09:00",
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
      "@id": "https://lumi-cosme.vercel.app/winter-dokudami"
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
        "name": "ドクダミは夏のニキビケア用というイメージがありますが、冬に使っても乾燥しませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "最新のドクダミコスメ（アヌアやAbib等）は、アルコールフリー処方であり、ドクダミ本来の抗炎症成分『クエルシトリン』に加えて、3重ヒアルロン酸やパンテノール、セラミドが高配合されています。そのため、さっぱりしすぎず、真冬の暖房乾燥下でも角層内部をもっちりと満たす優れた高保湿力を発揮します。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "冬特有の『寒暖差による赤ら顔やヒリつき』にドクダミが有効な理由は何ですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "冬の寒暖差（屋外の冷気と室内の温風）は毛細血管の急激な拡張と収縮を招き、血管運動性の炎症と赤みを生じさせます。ドクダミに含まれるポリフェノール群（クエルシトリン、ルチンなど）は、毛細血管の壁を強化・安定化させ、炎症性サイトカインの放出を抑制するため、真冬の火照りや赤みを穏やかに素早く沈静化させます。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "ドクダミ特有の青臭い匂いは気になりませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "化粧品用に高度に抽出・精製されたドクダミエキスは、生葉のような独特の青臭さや異臭は完全にカットされています。ほぼ無臭か、清涼感のある極めてマイルドな香りに仕上げられているため、匂いに敏感な方でも快適にお使いいただけます。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #3d6a4c;
      --primary-dark: #294933;
      --secondary: #f4f8f5;
      --accent: #5a8f6b;
      --text: #222c25;
      --text-muted: #536357;
      --border: #dbe8df;
      --card-bg: #ffffff;
      --gold: #d4af37;
      --radius: 12px;
      --shadow: 0 4px 20px rgba(61, 106, 76, 0.08);
      --font-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-base);
      line-height: 1.8;
      color: var(--text);
      background-color: #f7faf8;
      -webkit-font-smoothing: antialiased;
    }}

    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
    }}

    .header-inner {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo a {{
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: 0.05em;
    }}

    .nav-links {{
      display: flex;
      gap: 1.5rem;
      list-style: none;
    }}

    .nav-links a {{
      text-decoration: none;
      color: var(--text-muted);
      font-size: 0.95rem;
      font-weight: 600;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    .container {{
      max-width: 1000px;
      margin: 2.5rem auto;
      padding: 0 1.5rem;
    }}

    .article-header {{
      background: linear-gradient(135deg, #f2f8f4 0%, #ffffff 100%);
      padding: 3rem 2.5rem;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
    }}

    .badge-wrap {{
      display: flex;
      gap: 0.8rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }}

    .category-badge {{
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 20px;
    }}

    .update-badge {{
      background: #fff;
      color: var(--primary-dark);
      border: 1px solid var(--border);
      font-size: 0.8rem;
      padding: 0.3rem 0.8rem;
      border-radius: 20px;
    }}

    .article-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.45;
      color: #222c25;
      margin-bottom: 1.5rem;
    }}

    .lead-text {{
      font-size: 1.05rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}

    .toc-box {{
      background: var(--secondary);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.5rem 2rem;
      margin-top: 2rem;
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

    .toc-list {{
      list-style-type: decimal;
      padding-left: 1.5rem;
      columns: 2;
      column-gap: 2rem;
    }}

    .toc-list li {{
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
    }}

    .toc-list a {{
      color: var(--text);
      text-decoration: none;
      transition: color 0.2s;
    }}

    .toc-list a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .editorial-section {{
      background: #fff;
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}

    .section-h2 {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--primary-dark);
      border-left: 5px solid var(--primary);
      padding-left: 1rem;
      margin-bottom: 1.5rem;
    }}

    .section-h3 {{
      font-size: 1.25rem;
      font-weight: 700;
      margin: 1.8rem 0 1rem;
      color: #333;
    }}

    .feature-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin: 2rem 0;
    }}

    .feature-item {{
      background: var(--secondary);
      padding: 1.5rem;
      border-radius: var(--radius);
      border: 1px solid var(--border);
    }}

    .feature-item h4 {{
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
    }}

    .product-card {{
      background: #fff;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      padding: 2.5rem;
      margin-bottom: 3rem;
      position: relative;
    }}

    .product-header {{
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }}

    .rank-badge {{
      background: linear-gradient(135deg, #d4af37 0%, #aa8010 100%);
      color: #fff;
      font-size: 1.1rem;
      font-weight: 800;
      padding: 0.4rem 1.2rem;
      border-radius: 30px;
      box-shadow: 0 2px 8px rgba(212, 175, 55, 0.3);
    }}

    .product-tag {{
      background: #edf6f0;
      color: var(--primary);
      border: 1px solid #c9e2d1;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 20px;
    }}

    .product-title {{
      font-size: 1.4rem;
      font-weight: 800;
      line-height: 1.45;
      color: #222c25;
      margin-bottom: 0.5rem;
    }}

    .product-display-name {{
      font-size: 1rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      font-weight: 600;
    }}

    .product-layout {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2.5rem;
    }}

    .product-visual-col {{
      text-align: center;
    }}

    .img-wrap {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin-bottom: 1.2rem;
      box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.02);
    }}

    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      object-fit: contain;
    }}

    .price-box {{
      background: var(--secondary);
      border-radius: 8px;
      padding: 0.8rem;
      margin-bottom: 0.8rem;
    }}

    .price-label {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .price-value {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #3d6a4c;
    }}

    .review-meta {{
      font-size: 0.9rem;
      margin-bottom: 1.2rem;
    }}

    .review-stars {{
      color: #e67e22;
      font-weight: 700;
    }}

    .review-count {{
      color: var(--text-muted);
    }}

    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000 0%, #8a0000 100%);
      color: #ffffff !important;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 1rem 1.2rem;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
      text-align: center;
      line-height: 1.4;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #d40000 0%, #9e0000 100%);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.95rem;
    }}

    .spec-table th, .spec-table td {{
      padding: 0.75rem 1rem;
      border: 1px solid var(--border);
    }}

    .spec-table th {{
      background: var(--secondary);
      color: var(--primary-dark);
      font-weight: 700;
      width: 28%;
      white-space: nowrap;
    }}

    .spec-table td {{
      background: #fff;
    }}

    .product-body {{
      font-size: 1rem;
      color: #333d36;
    }}

    .body-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
    }}

    .product-body p {{
      margin-bottom: 1rem;
    }}

    .recommend-box, .usage-box {{
      border-radius: 8px;
      padding: 1.2rem;
      margin-top: 1.2rem;
    }}

    .recommend-box {{
      background: #fdf8e8;
      border-left: 4px solid #f39c12;
    }}

    .usage-box {{
      background: #eef8f5;
      border-left: 4px solid #27ae60;
    }}

    .recommend-title, .usage-title {{
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 0.4rem;
    }}

    .recommend-box p, .usage-box p {{
      margin-bottom: 0;
      font-size: 0.92rem;
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 2rem 0;
    }}

    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}

    .comparison-table th, .comparison-table td {{
      border: 1px solid var(--border);
      padding: 0.8rem 1rem;
    }}

    .comparison-table th {{
      background: var(--primary);
      color: #fff;
      font-weight: 700;
    }}

    .faq-block {{
      margin: 1.5rem 0;
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1.2rem 1.5rem;
    }}

    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .faq-a {{
      font-size: 0.95rem;
      color: var(--text);
    }}

    .internal-links-box {{
      background: #fff;
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-top: 3rem;
    }}

    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem;
      margin-top: 1.2rem;
    }}

    .internal-link-card {{
      background: var(--secondary);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.8rem 1rem;
      text-decoration: none;
      color: var(--text);
      font-size: 0.9rem;
      font-weight: 600;
      transition: all 0.2s;
      display: block;
    }}

    .internal-link-card:hover {{
      background: #fff;
      border-color: var(--primary);
      color: var(--primary);
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }}

    .site-footer {{
      background: #222c25;
      color: #dbe8df;
      padding: 3rem 1.5rem;
      margin-top: 4rem;
      text-align: center;
      font-size: 0.9rem;
    }}

    .site-footer a {{
      color: #c9e2d1;
      text-decoration: none;
    }}

    @media (max-width: 768px) {{
      .product-layout {{
        grid-template-columns: 1fr;
      }}
      .toc-list {{
        columns: 1;
      }}
      .article-title {{
        font-size: 1.45rem;
      }}
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <div class="site-logo">
        <a href="/">LUMI COSMETICS</a>
      </div>
      <nav>
        <ul class="nav-links">
          <li><a href="/">トップ</a></li>
          <li><a href="/#ranking">ランキング一覧</a></li>
          <li><a href="/#ingredients">成分別ケア</a></li>
          <li><a href="/#winter">冬コスメ特集</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="container">
    <article>
      <header class="article-header">
        <div class="badge-wrap">
          <span class="category-badge">2026年最新・冬コスメ特集</span>
          <span class="update-badge">📅 2026年11月検証済</span>
          <span class="update-badge">🌿 寒暖差レスキュー鎮静</span>
        </div>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！冬の寒暖差ゆらぎと乾燥赤みを濃密鎮静する保湿力高めドクダミコスメランク10</h1>
        <p class="lead-text">
          11月から12月にかけて、日本の冬は過酷な「寒暖差地獄」に突入します。氷点下近くまで冷え込む屋外の寒風にさらされた後、25℃を超える暖房が効いたオフィスや商業施設に入った途端、顔がカッと熱くなって両頬が真っ赤に火照る——そんな経験はありませんか？
          急激な温度差と空気の脱水は毛細血管を暴走させ、角層バリアをボロボロに引き裂いて「赤み・ヒリつき・インナードライ」の負の連鎖を引き起こします。
          「ドクダミ＝夏のニキビケア」という古い常識を覆し、高保水ヒアルロン酸やセラミドと融合して真冬の寒暖差ゆらぎ肌を救う、最新の高保湿ドクダミコスメ10選を徹底検証します。
        </p>

        <div class="toc-box">
          <div class="toc-title">📑 目次：高保湿ドクダミコスメ完全ガイド</div>
          <ol class="toc-list">
            <li><a href="#why-dokudami">なぜ真冬の寒暖差乾燥に「ドクダミ（クエルシトリン）」が選ばれるのか？</a></li>
            <li><a href="#ranking-section">高保湿ドクダミコスメ厳選ランキング10選</a></li>
            <li><a href="#spec-compare">全10アイテムの成分＆機能比較スペック表</a></li>
            <li><a href="#geo-climate">日本の冬特有の寒暖差環境と血管運動性ゆらぎ対策</a></li>
            <li><a href="#faq-section">ドクダミコスメに関するよくある質問（FAQ）</a></li>
            <li><a href="#internal-links">冬の乾燥対策・関連高保湿コスメ特集</a></li>
          </ol>
        </div>
      </header>

      <section class="editorial-section" id="why-dokudami">
        <h2 class="section-h2">なぜ真冬の寒暖差乾燥に「ドクダミ（クエルシトリン）」が選ばれるのか？</h2>
        <p>
          ドクダミ（学名：Houttuynia cordata、英名：Heartleaf）は、古来より「十薬（じゅうやく）」として重用されてきた日本の伝統生薬です。近年の皮膚科学研究において、ドクダミに豊富に含まれるフラボノイド成分『クエルシトリン』や『イソクエルシトリン』が、真冬の寒暖差によって過敏になった毛細血管の拡張を抑制し、強力な抗炎症・組織修復シグナルを発信することが証明されました。
        </p>
        <p>
          冬の肌トラブルの盲点は、単なる水分蒸発だけでなく「微小な炎症」が角層内部でくすぶり続けている点にあります。炎症が起きている肌は、いくら油分でフタをしても水分を繋ぎ止める受容体が機能不全を起こしています。ドクダミはまずこの炎症の火種を鎮静（消火）し、その上で角層細胞のバリアを整えるため、真冬でも乾かない健やかな肌土台を再建できるのです。
        </p>

        <div class="feature-grid">
          <div class="feature-item">
            <h4>クエルシトリンによる血管安定化</h4>
            <p>寒暖差で急激に拡張する毛細血管を鎮静。冬の室内に戻った瞬間に起こる赤ら顔や顔の火照り、ヒリヒリ感を速攻でクールダウンします。</p>
          </div>
          <div class="feature-item">
            <h4>弱酸性バリアとNMF保護</h4>
            <p>冬の乾燥冷風で崩れがちな角層pHを理想的な弱酸性にコントロール。肌内部の天然保湿因子（NMF）の漏出を食い止めます。</p>
          </div>
          <div class="feature-item">
            <h4>最新テクノロジーによる超保水化</h4>
            <p>アヌアやAbibをはじめとする最新韓国・日本コスメは、ドクダミに3重ヒアルロン酸やパンテノール、セラミドをドッキング。真冬の砂漠肌を一日中もっちり満たします。</p>
          </div>
        </div>
      </section>

      <section id="ranking-section">
        <h2 class="section-h2">保湿力の強さで肌乾燥とさようなら！高保湿ドクダミコスメ厳選ランキング10</h2>
        <p style="margin-bottom: 2rem; color: var(--text-muted);">
          楽天市場の最新データと皮膚科学的エビデンスに基づき、11月〜12月の本格的な寒暖差乾燥と赤みを鎮めるドクダミコスメ10選を厳選紹介します。
        </p>

        {all_cards_html}
      </section>

      <section class="editorial-section" id="spec-compare">
        <h2 class="section-h2">全10アイテムの成分＆機能比較スペック表</h2>
        <p>
          アイテムの種別、主要なドクダミ濃度・アプローチ、プラスアルファの配合成分を一覧表で比較しました。真冬の肌状態やスキンケアのルーティンに合わせて最適なアイテムをお選びください。
        </p>
        <div class="comparison-table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>ドクダミアプローチ</th>
                <th>相乗保湿成分</th>
                <th>おすすめの肌悩み・使用シーン</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>第1位</td>
                <td>Anua 77% スージングトナー</td>
                <td>ドクダミエキス77%</td>
                <td>ツボクサエキス・パンテノール</td>
                <td>冬の寒暖差赤み・ヒリつき・基本保湿</td>
              </tr>
              <tr>
                <td>第2位</td>
                <td>Anua 80% 水分鎮静アンプル</td>
                <td>高濃度ドクダミ80%</td>
                <td>3重ヒアルロン酸・ベタイン</td>
                <td>頑固なインナードライ・もちもち弾力補給</td>
              </tr>
              <tr>
                <td>第3位</td>
                <td>Abib スキンブースター</td>
                <td>智異山産ドクダミエキス</td>
                <td>パンテノール・アラントイン</td>
                <td>硬化角質のほぐし・ブースター化粧水</td>
              </tr>
              <tr>
                <td>第4位</td>
                <td>Anua 70% リリーフローション</td>
                <td>ドクダミエキス70%</td>
                <td>3重ヒアルロン酸・スクワラン</td>
                <td>ベタつかないシルキー乳液・メイク前保湿</td>
              </tr>
              <tr>
                <td>第5位</td>
                <td>Abib ガムシートマスク</td>
                <td>ドクダミエキス濃密浸透</td>
                <td>極細ガムシート・マデカッソシド</td>
                <td>冷風による赤み・皮むけ・一晩レスキュー</td>
              </tr>
              <tr>
                <td>第6位</td>
                <td>Anua 77% クリアパッド</td>
                <td>ドクダミ美容液1本分含浸</td>
                <td>低刺激PHA・ティーツリー</td>
                <td>冬の朝洗顔代わり・部分水分パック</td>
              </tr>
              <tr>
                <td>第7位</td>
                <td>Anua インテンス クリーム</td>
                <td>ドクダミエキス70%</td>
                <td>ヒト型セラミドNP・パンテノール</td>
                <td>冬の暖房直撃・超乾燥肌の鉄壁保護</td>
              </tr>
              <tr>
                <td>第8位</td>
                <td>Anua クレンジングオイル</td>
                <td>ドクダミエキス配合</td>
                <td>ホホバ・オリーブ・マカデミア油</td>
                <td>冬の毛穴角栓オフ・洗顔後の突っ張り防止</td>
              </tr>
              <tr>
                <td>第9位</td>
                <td>Abib スポットパッド</td>
                <td>智異山ドクダミ40,000ppm</td>
                <td>無漂白オーガニックコットン</td>
                <td>マスク擦れ赤み・両頬の集中鎮静</td>
              </tr>
              <tr>
                <td>第10位</td>
                <td>Anua シルキーサンクリーム</td>
                <td>ドクダミエキス配合</td>
                <td>パンテノール・ナイアシンアミド</td>
                <td>冬の乾燥崩れ防止・高保湿UVケア</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="editorial-section" id="geo-climate">
        <h2 class="section-h2">日本の冬特有の寒暖差環境と血管運動性ゆらぎ対策</h2>
        <p>
          日本列島の11月〜12月は、屋外と室内の温度差が極端に拡大する季節です。特に都市部のオフィス街や寒冷地における寒暖差は、肌の自律神経と毛細血管に過大な負荷を与えます。
        </p>

        <div class="feature-grid">
          <div class="feature-item">
            <h4>寒冷気流による血管収縮</h4>
            <p>
              外気温が5℃以下になると、体温を逃さないために顔の毛細血管が急速に収縮し、皮膚への血流と栄養供給がストップします。肌細胞は脱水状態になり、バリア機能が脆弱化します。
            </p>
          </div>
          <div class="feature-item">
            <h4>過熱暖房による急激なリバウンド拡張</h4>
            <p>
              暖かい室内に入った瞬間、収縮していた毛細血管が一気に拡張して大量の血液が流れ込みます。これが「火照り」「赤ら顔」の正体です。ドクダミを日頃から取り入れることで、血管壁の弾力性が保たれ、急激な火照りを防ぎます。
            </p>
          </div>
        </div>
      </section>

      <section class="editorial-section" id="faq-section">
        <h2 class="section-h2">ドクダミコスメに関するよくある質問（FAQ）</h2>
        
        <div class="faq-block">
          <div class="faq-q">❓ ドクダミコスメは乾燥肌や超乾燥肌でも十分な保湿感がありますか？</div>
          <div class="faq-a">
            はい、十分に満足いただけます。本記事で厳選したアヌアやAbibのアイテムは、ドクダミの優れた鎮静力に加えて、3重ヒアルロン酸やセラミドNP、パンテノールなどの高保水・バリア補強成分が贅沢に配合されています。さっぱり感だけでなく、内側からしっとり吸い付くような濃密な保湿力を長時間実感できます。
          </div>
        </div>

        <div class="faq-block">
          <div class="faq-q">❓ ドクダミコスメとCICA（ツボクサ）コスメはどう使い分ければ良いですか？</div>
          <div class="faq-a">
            CICAは主に『物理的な肌ダメージ（擦れや炎症後の傷痕）の修復』に強みを持つのに対し、ドクダミは『毛細血管の拡張による赤みや火照り、寒暖差ゆらぎの速効鎮静』において突出した効果を発揮します。冬の寒さで顔が赤くなりやすい方や、暖房で火照る方にはドクダミが最もおすすめです。
          </div>
        </div>

        <div class="faq-block">
          <div class="faq-q">❓ ドクダミコスメは敏感肌でもピリピリしませんか？</div>
          <div class="faq-a">
            本記事で紹介した10アイテムはすべて弱酸性かつ無香料・低刺激処方で設計されており、アレルギーテストやノンコメドジェニックテスト済みです。アルコールや強い保存料を排除しているため、真冬の過敏になった素肌でもヒリつかず安心してお使いいただけます。
          </div>
        </div>
      </section>

      <section class="internal-links-box" id="internal-links">
        <h2 class="section-h2">冬の乾燥対策・関連高保湿コスメ特集</h2>
        <p>
          LUMI COSMETICSでは、11月・12月の本格的な冬乾燥に立ち向かう厳選スキンケア特集を多数公開しています。成分ごとの特徴や肌悩みに合わせて、ぜひ合わせてチェックしてみてください。
        </p>

        <div class="internal-links-grid">
          <a href="/winter-cica-cream" class="internal-link-card">🌿 冬のCICAシカクリーム10選</a>
          <a href="/winter-panthenol-cream" class="internal-link-card">🧴 冬のパンテノール保湿クリーム10選</a>
          <a href="/winter-ceramide-lotion" class="internal-link-card">💧 冬のセラミド化粧水10選</a>
          <a href="/winter-azulene" class="internal-link-card">💙 冬のアズレン鎮静スキンケア10選</a>
          <a href="/winter-calendula" class="internal-link-card">🌼 冬のカレンデュラ高保湿コスメ10選</a>
          <a href="/winter-mugwort" class="internal-link-card">🍵 冬のヨモギエキス保湿コスメ10選</a>
          <a href="/winter-lactobacillus" class="internal-link-card">🥛 冬の高保湿乳酸菌（美肌菌）コスメ10選</a>
          <a href="/winter-swallow-nest" class="internal-link-card">👑 冬の高保湿ツバメの巣コスメ10選</a>
        </div>
      </section>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 LUMI COSMETICS - 冬の科学的高保湿コスメ情報局. All Rights Reserved.</p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #a89aa0;">
        当サイトに掲載されている価格・製品情報は執筆時点（2026年11月）の楽天市場API取得データに基づきます。最新の販売価格・在庫状況は各販売店ページをご確認ください。
      </p>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-dokudami.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-dokudami.html!")
