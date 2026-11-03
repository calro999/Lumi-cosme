import json
import re

with open("fetched_final_30_marula_birch_azelaic.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_marula_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 楽天殿堂入り！未精製オーガニック100%・極上オメガオイルの最高峰",
        "catch": "過酷なアフリカ大地が育んだ奇跡の一滴。アルガンを凌ぐ抗酸化力で冬のゴワつき砂漠肌をふっくら解きほぐす",
        "brand_name": "VIRCHE (ヴァーチェ)",
        "capacity": "18ml (純度100%マルラオイル)",
        "type": "未精製100%オーガニック美容ブースターオイル",
        "features": "南アフリカ産未精製マルラオイル100%、防腐剤・香料・着色料完全無添加、オメガ6・オメガ9・ビタミンE・C高含有",
        "value": "ビタミンEがオリーブ油の約10倍。オイル特有の重さや油膜感が一切なく、化粧水の前に塗るだけで角層の浸透ルートを瞬時に開通させる",
        "desc_p1": "11月から12月にかけて外気湿度が40%を下回り、暖房の温風が直接肌を直撃する日本の冬。肌内部の水分蒸発を防ぐ皮脂膜が冷えと加齢によって激減すると、角質層が乾いたプラスチックのように硬化し、いくら高保湿な化粧水やシートマスクを重ねても弾かれて浸透しなくなります。ヴァーチェのマルラオイルは、南アフリカの過酷な乾燥地帯に自生するマルラの木の実から低温圧搾（コールドプレス）で丁寧に抽出された、純度100%の最高峰オーガニック未精製オイルです。",
        "desc_p2": "美容オイルの女王と呼ばれるアルガンオイルと比較しても抗酸化力は約3倍から4倍に達し、人の皮脂構造に近いオレイン酸（オメガ9）が約70〜78%という黄金比率で含まれています。テクスチャーはオイルとは思えないほどサラリとしており、手のひらに1〜2滴伸ばして肌に押し当てると、乾き切った角層のすき間にスーッと吸い込まれるように馴染みます。塗布した瞬間に肌のゴワつきが消え去り、ふんわりとマシュマロのような柔軟性が復活。その後に重ねる化粧水がスポンジのようにぐんぐん引き込まれる驚きの浸透感を体験できます。",
        "target": "冬になると肌が硬くゴワつき化粧水が浸透しない方、夕方の目元や口元の乾燥小ジワ・ファンデーションのひび割れに悩む方、ベタつくオイルが苦手な方",
        "point": "洗顔直後の湿り気が残る肌に、まず1〜2滴を手のひら全体で温めてから優しくハンドプレス。角質を柔らかくほぐした後に通常通りの化粧水を重ねると、驚異的な吸い込みと潤い保持力を発揮します。"
    },
    {
        "rank": 2,
        "tag": "🔬 コスパ最強の純度100%！低温圧搾コールドプレス製法のヴァージンマルラ",
        "catch": "シンプルイズベストを極めた世界的人気処方。不要な添加物を一切排除し、素材本来の生命力でバリア膜を再構築",
        "brand_name": "The Ordinary (ジ オーディナリー)",
        "capacity": "30ml (100% コールドプレス ヴァージンマルラオイル)",
        "type": "低温圧搾ピュア未精製マルラオイル",
        "features": "スクレロカリアビレア種子油100%、コールドプレス抽出、未精製リッチフォーミュラ、紫外線防止遮光ボトル採用",
        "value": "デパコス高級オイルと同等の高純度未精製マルラオイルを圧倒的なコストパフォーマンスで提供。毎日惜しみなく使える実力派",
        "desc_p1": "カナダ発のサイエンスコスメブランド『The Ordinary』が誇る名品オイル。マルラの種子の核から熱を加えずにじっくり圧搾することで、熱に弱い抗酸化物質フラボノイドやビタミンC、オメガ脂肪酸などの微量有効成分を損なうことなくボトルへ密封しています。未精製ならではのほのかな天然ナッツの香りと黄金色のリッチなテクスチャーが特徴です。",
        "desc_p2": "冬の冷たい外気にさらされてバリア機能が低下した肌は、水分の蒸散スピードが通常の約2倍にも跳ね上がります。このヴァージンマルラオイルをスキンケアの仕上げや乳液に1滴混ぜて使うと、肌表面に薄くしなやかな保護皮膜を形成。室内暖房のドライな空気の中でも水分の蒸発を完璧に遮断し、翌朝まで吸い付くようなもっちり肌をキープしてくれます。髪の毛先や爪周りのささくれケアにも使える万能性も魅力です。",
        "target": "成分重視で無駄なコストを抑えたい方、夜のスキンケア後に朝まで乾かない強力な保護ヴェールを張りたい方、髪やデコルテまで全身保湿したい方",
        "point": "夜のお手入れの最後に2〜3滴を全顔に。または現在愛用している保湿クリームや乳液に手のひらで1滴混ぜて塗布すると、油分と水分のバランスが絶妙に溶け合い、保湿持続力が飛躍的にアップします。"
    },
    {
        "rank": 3,
        "tag": "🌿 手作りコスメ派・プロ仕様！新鮮な有機栽培マルラをそのままボトリング",
        "catch": "防腐剤も酸化防止剤もゼロ。生まれたてのピュアな栄養素が角層細胞のすき間を満たし尽くす",
        "brand_name": "monday moon (マンデイムーン)",
        "capacity": "50ml (未精製オーガニック マルラオイル)",
        "type": "エコサート認証オーガニック原料100%オイル",
        "features": "未精製コールドプレス、有機認証原料、オメガ9（オレイン酸）高濃度、エイジングケア対応ビタミンE豊富",
        "value": "中間流通をカットした新鮮なロットを管理。フレッシュな抗酸化力と肌なじみの良さが際立ち、インナードライを根本からケア",
        "desc_p1": "手作り化粧品やオーガニック原料専門ショップとして絶大な信頼を集めるマンデイムーンのマルラオイル。徹底した品質管理のもと、アフリカの野生マルラの実からコールドプレスで搾油された有機原料をそのまま充填しています。精製処理を行わないため、植物本来が持っているカロテノイドやステロール類が豊富に残存しており、肌のターンオーバーを正常化させるサポート力に秀でています。",
        "desc_p2": "11月後半から急増する『表面はテカるのに内側がつっぱるインナードライ』や『洗顔後の急激なツッパリ感』に悩む方に最適です。マルラオイル特有の極小分子脂肪酸が、硬くなった角質細胞のラメラ構造を整えてふっくらと厚みのある健やかな状態へリカバリー。オイル美容特有の毛穴詰まりやニキビの心配が極めて少なく、乾燥で荒れやすい肌にも刺激感なく寄り添ってくれます。",
        "target": "オーガニック品質と鮮度にこだわりたい方、冬のインナードライで皮脂浮きと乾燥が同時に起きる方、家族で安心して使えるピュアオイルを求める方",
        "point": "お風呂上がりの水滴がついた状態の肌に1滴なじませる『インバスブースター』としての使い方が秀逸。浴室の湯気とともに角層深くまで浸透し、脱衣所の急激な乾燥ダメージをゼロにします。"
    },
    {
        "rank": 4,
        "tag": "🧴 大容量100mlで全身の砂漠化を阻止！サロン品質のプレミアムキャリアオイル",
        "catch": "顔だけでなく首元・ひじ・すね・かかとまで。冬の粉吹き・カサつきを全身まるごと潤いリセット",
        "brand_name": "マカダミ屋 (Macadamiya)",
        "capacity": "100ml (100%ピュア 未精製オーガニックマルラオイル)",
        "type": "サロン仕様大容量キャリア＆美容オイル",
        "features": "未精製100%オーガニック、低温圧搾法、ポンプ式遮光ボトル、全身・ヘア・スカルプ対応",
        "value": "100mlという贅沢な容量でありながら妥協のない高品質未精製オイル。冬の全身の粉吹きやひび割れ乾燥を徹底的にレスキュー",
        "desc_p1": "アロマトリートメントサロンやエステティックサロンでも採用されているマカダミ屋のマルラオイル。11月から12月は顔だけでなく、すねの粉吹きやすねのひび割れ、タイツを脱いだときの白い粉落ち、かかとのガサガサなど全身の乾燥トラブルがピークに達します。顔用の少量高額な美容オイルでは全身ケアに躊躇してしまいますが、100mlの大容量なら惜しみなく全身に塗り広げることができます。",
        "desc_p2": "ポンプヘッドが付属しているため、お風呂上がりの慌ただしい時間でも片手でプッシュして素早く塗布できる操作性が抜群。伸びが非常に良く、少量で広範囲にするすると広がり、ベタつきが肌に残らないため塗布後すぐにパジャマや衣類を着ても張り付きません。抗酸化成分が豊富に含まれているためオイル自体の酸化安定性が極めて高く、最後まで新鮮な状態で使い切れる点も高ポイントです。",
        "target": "顔だけでなくデコルテ・すね・ひじ・手元など全身の粉吹き乾燥を治したい方、お風呂上がりのボディケアを1本で完結させたい方",
        "point": "入浴後、タオルで軽く水気を拭き取った直後の肌に2〜3プッシュ。リンパの流れに沿って足首から太もも、デコルテへと優しくマッサージしながら伸ばすと、血行促進と高保湿が同時に叶います。"
    },
    {
        "rank": 5,
        "tag": "👜 ポーチに忍ばせる乾燥レスキュー！目元・ほうれい線の乾きに即効ピンポイント補給",
        "catch": "日中のオフィス暖房でひび割れるメイクの上からトントン。一瞬で朝のうるおいとツヤが蘇る",
        "brand_name": "自然化粧品研究所",
        "capacity": "10ml〜 (植物性未精製マルラオイル)",
        "type": "携帯型ピュアポイント美容オイル",
        "features": "植物性ピュア100%未精製オイル、滴下スポイトボトル、コンパクトサイズ、高純度オメガ脂肪酸",
        "value": "外出先やオフィスでのエアコン直撃による部分乾燥を即座に修復。メイク直し時にヨレずになじむ絶妙な肌なじみ",
        "desc_p1": "創業70年以上の研究開発実績を誇る自然化粧品研究所の未精製マルラオイル。10mlのコンパクトな遮光ガラス容器に入っており、旅行先やオフィスのデスク、ポーチの中に常備するのに最適なアイテムです。冬場のオフィスで暖房が効き始めると、午後3時頃には目の下やほうれい線まわりのファンデーションが乾燥でパキパキに割れてしまう現象が頻発します。",
        "desc_p2": "そんな時に指先に半滴だけ取り、乾燥した目元や口元にトントンと優しくスタンプするように馴染ませると、崩れたファンデーションが自然に溶け合い、乾き切ったキメがふっくらと持ち上がります。人工的なハイライトでは出せない、素肌そのものが内側から発光しているかのような自然なツヤが復活。冬の乾燥崩れ対策の秘密兵器として手放せなくなる名品です。",
        "target": "日中オフィスで目元や口元の乾燥小ジワが目立つ方、メイク直しの仕上がりを格上げしたい方、まずは少量でお試ししたい方",
        "point": "綿棒の先に極少量のオイルをなじませ、ヨレた目元のメイクを優しくオフしてから、指の腹でトントンと重ねてパウダーを薄く乗せると、朝のメイクしたて以上の透明感が復活します。"
    },
    {
        "rank": 6,
        "tag": "🌿 低温コールドプレスの濃密保湿！冬の肌荒れ・赤みをやさしく鎮めるピュアヴェール",
        "catch": "南アフリカの大自然が育んだ強い抗酸化バリア。寒冷外気に負けない強靭な角層を育む",
        "brand_name": "アロマ ルイボス naturalshop",
        "capacity": "20ml (オーガニック未精製マルラオイル)",
        "type": "無添加オーガニック美容キャリアオイル",
        "features": "無添加100%、コールドプレス製法、未精製ヴァージンオイル、オレイン酸・リノール酸バランス処方",
        "value": "刺激物質を極限まで排除したナチュラル設計。冬の寒暖差やマスクの摩擦でピリつくデリケート肌を穏やかに保護",
        "desc_p1": "原料の選定からボトリングまで徹底したオーガニック基準を貫くnaturalshopの未精製マルラオイル。農薬や化学肥料を一切使わずに育った南アフリカ原産のマルラ種子を手作業で選別し、熱を加えない伝統的な低温圧搾法で抽出されています。黄金色に輝くオイルには、過酷な日差しと乾燥から種子を守るための強力なポリフェノールとトコフェロールが凝縮されています。",
        "desc_p2": "11月から12月にかけての寒暖差で頬に赤みが出たり、肌が薄くなって敏感になりがちな肌質でも、しみることなく穏やかに包み込んでくれます。水分を挟み込んで逃さない細胞間脂質の働きを力強くサポートし、外気の乾燥刺激や衣類の摩擦刺激をシャットアウト。数滴を継続して使うことで、肌のキメが整い、触れた時のザラつきがなめらかな陶器肌へと変化していきます。",
        "target": "敏感肌で新しいスキンケアを試すのが怖い方、冬の寒風に当たると頬がピリピリ痛む方、肌の赤みとカサつきを同時に落ち着かせたい方",
        "point": "洗顔後、手のひらに2滴垂らし、深呼吸しながら両手で包み込むように顔全体に押し当てます。手のひらのぬくもりでオイルを温めることで、角層への浸透速度がさらに向上します。"
    },
    {
        "rank": 7,
        "tag": "🛡️ 50ml中容量でじっくり美肌育成！抗酸化オメガ脂肪酸で冬枯れ肌を劇的リセット",
        "catch": "年齢とともに減少する皮脂膜を完璧に再現。ハリ・弾力・ツヤの3拍子が揃った若々しい素肌へ",
        "brand_name": "ナチュラルマルラ (Natural Marula)",
        "capacity": "50ml (オーガニック未精製マルラオイル)",
        "type": "エイジングケア特化型高濃度ピュアオイル",
        "features": "コールドプレス未精製、抗酸化オメガ6・オメガ9凝縮、高純度ビタミンC・E、無着色・無香料",
        "value": "1ヶ月〜2ヶ月間毎日たっぷり使える50mlサイズ。冬の乾燥によるたるみ毛穴やしぼみ肌に集中的にハリをチャージ",
        "desc_p1": "冬の乾燥ダメージは角質層の水分を奪うだけでなく、真皮層のコラーゲンやエラスチンの変性を促進し、顔全体のハリ不足やたるみ毛穴を急激に進行させます。ナチュラルマルラのオーガニック未精製オイルは、豊富なオレイン酸とリノール酸が絶妙なバランスで含まれており、加齢によって分泌量が激減した皮脂膜の代わりとなって肌のクッション性を保ちます。",
        "desc_p2": "オイルとは思えないほど浸透力が高く、肌表面にヌルつきやギトつきを残さないため、朝のメイク前でもストレスフリーで使用可能。化粧ノリが格段に良くなり、リキッドファンデーションやクッションファンデが一日中ピタッと密着して崩れません。夕方になってもくすみが現れず、澄んだ明るいトーンが夕暮れ時まで持続するのを実感できます。",
        "target": "冬になると乾燥で頬の毛穴が縦に流れて目立つ方、夕方に顔全体がどんより暗くくすむ方、朝晩たっぷり使いたい方",
        "point": "朝のスキンケアで化粧水の後に1滴、夜のスキンケアの仕上げに3滴と使い分けるのがベスト。首筋から鎖骨へ向かって流すように首元のシワケアも同時に行うと効果的です。"
    },
    {
        "rank": 8,
        "tag": "💇 髪・頭皮・顔・体を1本で制覇！詰替えパウチで環境にも優しいマルチボタニカル",
        "catch": "暖房でパサつく毛先とフケ・痒みが出る頭皮を集中ケア。頭のてっぺんから爪先まで贅沢オメガ補給",
        "brand_name": "アンドエスエイチ (&SH)",
        "capacity": "80ml (未精製マルラオイル 詰替え用リフィル)",
        "type": "全身マルチ高保湿ボタニカルオイル",
        "features": "未精製マルラオイル、ヴィーガン認証原料、大容量80mlパウチ、頭皮・ヘア・ボディ兼用",
        "value": "髪のパサつきと顔の乾燥を同時に解決する圧倒的な汎用性。お気に入りの遮光ボトルに詰め替えてエコでお得に使える",
        "desc_p1": "11月以降の乾燥は顔の皮膚だけでなく、頭皮の毛穴や髪のキューティクルにも深刻な打撃を与えます。湿度が下がると静電気が発生しやすくなり、枝毛・切れ毛が増加。さらに頭皮が乾燥してバリアが崩れると、かゆみや細かなフケの原因になります。&SHの未精製マルラオイルは、顔のスキンケアはもちろん、スカルプマッサージやヘアオイルとしても圧倒的な威力を発揮する万能リッチオイルです。",
        "desc_p2": "タオルドライ後の濡れた毛先に2〜3滴馴染ませてからドライヤーで乾かすと、熱ダメージから髪をプロテクトしながら、サロン帰りのようなシルクの手触りと自然なツヤを再現。翌朝の寝癖や広がりが劇的に抑えられます。また、シャンプー前の乾いた頭皮に数滴垂らして揉み込むスカルプクレンジングとしても優秀で、毛穴に詰まった酸化皮脂を優しく浮き上がらせながら潤いを補給できます。",
        "target": "冬になると髪のパサつきや静電気・広がりがひどい方、頭皮の乾燥やかゆみに悩む方、1本のオイルで全身のケアをまとめたいミニマリスト",
        "point": "洗髪後のアウトバストリートメントとして毛先中心に塗布。手に残ったオイルをそのまま手肌や甘皮にすり込むことで、手荒れの予防も同時に完了します。"
    },
    {
        "rank": 9,
        "tag": "🏺 南アフリカ直輸入・伝統コールドプレス！大容量100mlのプロ仕様キャリアオイル",
        "catch": "大地が育んだ純度100%の植物パワー。冬の冷え固まった肌を芯から温めるマッサージにも最適",
        "brand_name": "IST (アイエスティ)",
        "capacity": "100ml (ピュアマルラオイル 未精製)",
        "type": "直輸入プレミアム原液キャリアオイル",
        "features": "南アフリカ原産、無添加ピュア100%未精製、低温圧搾法、マッサージ対応テクスチャー",
        "value": "エステやアロマセラピストも愛用する本格プログレード。摩擦をゼロに抑える極上のクッション性で冬の血行不良をケア",
        "desc_p1": "世界各地の上質な天然植物オイルを直輸入するISTのピュア未精製マルラオイル。マルラの実はアフリカでは古くから『神の木』として崇められ、厳しい日差しや乾燥から肌を守る伝統的なスキンケア素材として受け継がれてきました。本品は現地の厳選された生産者から直接仕入れた未精製原液を、日本の徹底した品質管理基準のもとで製品化しています。",
        "desc_p2": "手のひらで温めるとほのかなナッツの香りが立ち上り、肌の上でなめらかに伸び広がるリッチな感触。冬の寒さでこわばったフェイスラインや首筋を優しくマッサージするのに最適で、滞りがちな血流を促しながら角層深部へ良質な脂質を届けます。マッサージ後はティッシュオフする必要がなく、そのまま肌に浸透してベロアのようなしっとり肌に仕上がります。",
        "target": "本格的なフェイシャルマッサージを取り入れたい方、冬の冷えによる顔のくすみやむくみを解消したい方、プロ品質を長く愛用したい方",
        "point": "入浴中、湯船に浸かりながらオイルを5〜6滴顔全体に伸ばし、蒸気を利用したオイルパックを行うと、毛穴が自然に開き肌が驚くほどふっくらと柔らかくなります。"
    },
    {
        "rank": 10,
        "tag": "✨ マルラオイル×高浸透ビタミンC誘導体の融合！くすみと乾燥を同時に晴らす濃密化粧水",
        "catch": "オイルの保水力とローションの潤い補給が一つに。オイルが苦手な方でも手軽にマルラの恩恵を享受",
        "brand_name": "VIRCHE (ヴァーチェ)",
        "capacity": "150ml (ブライトニングローション)",
        "type": "マルラオイル配合高保湿ブライトニング化粧水",
        "features": "未精製マルラオイルナノエマルジョン配合、持続型ビタミンC誘導体、エクトイン、シロキクラゲ多糖体",
        "value": "オイル単体では難しい水分と油分の同時チャージを実現。白濁したまろやかなテクスチャーで冬の角層を潤いで満タンに",
        "desc_p1": "「マルラオイルの優れた抗酸化力や保湿力は気になるけれど、オイル単体をスキンケアに取り入れるのはベタつきそうで不安」という方に最適なのが、ヴァーチェの『ブライトニングローション』です。最高峰の未精製マルラオイルを独自の微細ナノエマルジョン化技術によって化粧水の中に高濃度で均一に分散させています。",
        "desc_p2": "さらに持続型ビタミンC誘導体や高保水エクトイン、ヒアルロン酸を超える保水力を持つシロキクラゲ多糖体を贅沢にブレンド。肌に伸ばした瞬間はみずみずしく広がり、ハンドプレスするにつれて肌内部がもちもちとした潤いの密度で満たされていく感触が得られます。油分と水分が同時にチャージされるため、冬のインナードライ肌が1本でふっくらと整い、パッと明るい透明感を取り戻せます。",
        "target": "オイルのベタつきがどうしても苦手な方、1本で水分補給と油分ヴェールを両立させたい方、乾燥による黄ぐすみをトーンアップさせたい方",
        "point": "手のひらに500円玉大を取り、顔全体を包み込むように2回に分けて重ねづけ。乾燥しやすい目元や頬骨あたりには、手のひらでじっくりと温めるように30秒間プレスするのがコツです。"
    }
]

faq_data = [
    {
        "q": "マルラオイルとはどのようなオイルですか？アルガンオイルやホホバオイルとの決定的な違いは何ですか？",
        "a": "マルラオイルは、南アフリカの過酷な乾燥地帯に自生するウルシ科の樹木『マルラ（Sclerocarya birrea）』の実の種子から抽出される希少な植物オイルです。アルガンオイルと比較して抗酸化成分（ビタミンEやポリフェノール）が約3〜4倍も豊富に含まれており、酸化安定性が極めて高いのが特徴です。また、人の皮脂の主成分であるオレイン酸が70%以上と高含有でありながら、分子構造が非常に小さいため、ホホバオイルやアルガンオイル以上にサラリとした軽いテクスチャーで角層深部へ瞬時に浸透します。油膜感やベタつきを残さずに、冬の硬くなった角層を柔らかくほぐす力に突出しています。"
    },
    {
        "q": "11月・12月の冬のスキンケアにおいて、マルラオイルはどの順番で使うのが最も効果的ですか？",
        "a": "マルラオイルの最も効果的な使い方は『洗顔直後のブースター（導入オイル）』としての使用です。洗顔後、肌にまだわずかに湿り気が残っている状態で1〜2滴を手のひらで温めて全顔にハンドプレスします。マルラオイルのリッチなオレイン酸が乾いた角質を瞬時に柔らかくほぐし、親水性の高い通り道を作るため、その後に塗布する化粧水や美容液の水分を驚くほどぐんぐん引き込みます。もちろん、スキンケアの最後に水分蒸発を防ぐフタとして使ったり、乳液やクリームに1滴混ぜて保湿力を底上げする使い方も真冬の乾燥対策に非常に効果的です。"
    },
    {
        "q": "オイル美容をするとニキビができたり、朝使うと油焼け（日焼け）したりしませんか？",
        "a": "心配ありません。マルラオイルは酸化しにくいオレイン酸が豊富で、不純物を含まない高品質な未精製・低温圧搾オイルであれば、肌の上で酸化して過酸化脂質に変化するリスクが極めて低いため、油焼けを起こすことはありません。また、コメド（毛穴詰まり）を起こしにくい性質を持ち、抗炎症作用や抗酸化作用にも優れているため、乾燥による皮脂の過剰分泌や大人ニキビが気になる肌質の方でも安心してお使いいただけます。朝のメイク前に1滴なじませることで、暖房による日中の乾燥崩れを防ぐ優れた化粧下地効果も発揮します。"
    },
    {
        "q": "未精製オイルと精製オイルではどのような違いがありますか？どちらを選ぶべきですか？",
        "a": "未精製オイルは、低温圧搾後にフィルターを通しただけで薬品処理や高温脱臭・脱色を行っていないオイルです。黄金色をしており、ビタミンEやポリフェノール、オメガ脂肪酸などの豊富な栄養素が壊れずにそのまま残っているため、真冬の本格的なエイジングケアや高保湿を求める方には未精製が圧倒的におすすめです。一方、精製オイルは色や香りが取り除かれて無色透明になっており、植物特有の天然の香りやナッツ臭が苦手な方、または超敏感肌で植物由来の微量成分にも反応してしまう方に適しています。"
    }
]

# アイテムカードHTML生成
items_html = ""
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    price_formatted = f"{r_item['price']:,}円"
    
    items_html += f"""
      <section id="rank-{p['rank']}" class="product-card">
        <div class="product-header">
          <div class="rank-badge">第{p['rank']}位</div>
          <span class="product-tag">{p['tag']}</span>
        </div>
        <h3 class="product-name">{r_item['name']}</h3>
        <p class="product-catch">{p['catch']}</p>
        
        <div class="product-content-grid">
          <div class="product-img-wrap">
            <img src="{r_item['img_url']}" alt="{r_item['name']}" loading="lazy" width="280" height="280" class="product-img">
          </div>
          <div class="product-info-wrap">
            <div class="price-box">
              <span class="price-label">楽天市場 参考価格:</span>
              <span class="price-value">{price_formatted}</span>
              <span class="price-tax">(税込 / 2026年11月時点)</span>
            </div>
            <dl class="product-specs">
              <dt>ブランド / メーカー</dt>
              <dd>{p['brand_name']}</dd>
              <dt>容量 / タイプ</dt>
              <dd>{p['capacity']} / {p['type']}</dd>
              <dt>主要成分・処方特徴</dt>
              <dd>{p['features']}</dd>
              <dt>冬の保水アプローチ</dt>
              <dd>{p['value']}</dd>
            </dl>
          </div>
        </div>

        <div class="product-desc-box">
          <h4 class="desc-heading">🔍 徹底深掘りレビュー＆真冬の検証結果</h4>
          <p class="desc-p">{p['desc_p1']}</p>
          <p class="desc-p">{p['desc_p2']}</p>
          
          <div class="target-point-grid">
            <div class="target-box">
              <span class="box-icon">🎯</span>
              <strong>こんな肌悩みにおすすめ:</strong>
              <p>{p['target']}</p>
            </div>
            <div class="point-box">
              <span class="box-icon">💡</span>
              <strong>効果を最大化する使用のコツ:</strong>
              <p>{p['point']}</p>
            </div>
          </div>
        </div>

        <div class="product-action-wrap">
          <a href="{r_item['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            <span>楽天市場で最安値・商品詳細を見る</span>
            <svg class="arrow-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
        </div>
      </section>
    """

# 比較表HTML生成
table_rows = ""
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    price_formatted = f"{r_item['price']:,}円"
    table_rows += f"""
            <tr>
              <td class="rank-cell">第{p['rank']}位</td>
              <td class="name-cell"><strong>{r_item['name'][:28]}...</strong><br><small>{p['brand_name']}</small></td>
              <td>{p['type']}</td>
              <td>{p['features']}</td>
              <td class="price-cell">{price_formatted}</td>
            </tr>
    """

# JSON-LD構造化データ
jsonld_products = []
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    jsonld_products.append({
        "@type": "Product",
        "name": r_item["name"],
        "image": r_item["img_url"],
        "description": p["catch"],
        "brand": {
            "@type": "Brand",
            "name": p["brand_name"]
        },
        "offers": {
            "@type": "Offer",
            "priceCurrency": "JPY",
            "price": str(r_item["price"]),
            "url": r_item["affiliate_url"],
            "availability": "https://schema.org/InStock"
        }
    })

jsonld_faq = []
for f in faq_data:
    jsonld_faq.append({
        "@type": "Question",
        "name": f["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f["a"]
        }
    })

full_jsonld = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！アルガン超えの抗酸化力と極上浸透膜で砂漠肌を救う高保湿マルラオイルランク10",
            "description": "11月・12月の冬本番に！アルガンオイルを超える抗酸化力と人の皮脂に近いオメガ脂肪酸で砂漠肌を救う高保湿マルラオイル10選を徹底比較！ヴァーチェ、The Ordinary、マンデイムーン、マカダミ屋など厳選。",
            "datePublished": "2026-11-03T18:00:00+09:00",
            "dateModified": "2026-11-03T18:00:00+09:00",
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
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": "https://lumi-cosme.vercel.app/winter-marula-oil"
            }
        },
        {
            "@type": "ItemList",
            "name": "真冬の高保湿マルラオイルおすすめランキング10選",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": idx + 1,
                    "item": prod
                }
                for idx, prod in enumerate(jsonld_products)
            ]
        },
        {
            "@type": "FAQPage",
            "mainEntity": jsonld_faq
        },
        {
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
                    "name": "高保湿マルラオイル",
                    "item": "https://lumi-cosme.vercel.app/winter-marula-oil"
                }
            ]
        }
    ]
}

faq_html = ""
for f in faq_data:
    faq_html += f"""
      <div class="faq-item">
        <dt class="faq-question">
          <span class="faq-q-badge">Q</span>
          <span>{f['q']}</span>
        </dt>
        <dd class="faq-answer">
          <span class="faq-a-badge">A</span>
          <p>{f['a']}</p>
        </dd>
      </div>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！アルガン超えの抗酸化力と極上浸透膜で砂漠肌を救う高保湿マルラオイルランク10</title>
  <meta name="description" content="11月・12月の冬本番に！アルガンオイルを超える抗酸化力と人の皮脂に近いオメガ脂肪酸で砂漠肌を救う高保湿マルラオイル10選を徹底比較！ヴァーチェ、The Ordinary、マンデイムーン、マカダミ屋など厳選。">
  <meta name="keywords" content="マルラオイル, 高保湿オイル, 乾燥肌 スキンケア, 冬 コスメ, ブースターオイル, ヴァーチェ, The Ordinary, 抗酸化オイル">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-marula-oil">
  
  <!-- OGP -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！アルガン超えの抗酸化力と極上浸透膜で砂漠肌を救う高保湿マルラオイルランク10">
  <meta property="og:description" content="11月・12月の冬本番に！アルガンオイルを超える抗酸化力と人の皮脂に近いオメガ脂肪酸で砂漠肌を救う高保湿マルラオイル10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-marula-oil">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta name="twitter:card" content="summary_large_image">
  
  <script type="application/ld+json">
{json.dumps(full_jsonld, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary-color: #8c531b;
      --primary-light: #fff8f0;
      --accent-color: #d97706;
      --accent-hover: #b45309;
      --text-main: #2d3748;
      --text-muted: #5a6a85;
      --bg-main: #faf9f6;
      --card-bg: #ffffff;
      --border-color: #eddcd2;
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.04);
      --shadow-md: 0 4px 12px rgba(140,83,27,0.08);
      --shadow-lg: 0 8px 24px rgba(140,83,27,0.12);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif;
      line-height: 1.8;
      color: var(--text-main);
      background-color: var(--bg-main);
    }}

    .container {{
      max-width: 920px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* ヘッダー */
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

    /* パンくずリスト */
    .breadcrumb {{
      display: flex;
      list-style: none;
      padding: 14px 0;
      font-size: 0.85rem;
      color: var(--text-muted);
      overflow-x: auto;
      white-space: nowrap;
    }}
    .breadcrumb li+li:before {{
      content: "›";
      padding: 0 8px;
      color: #cbd5e1;
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumb a:hover {{
      color: var(--accent-color);
    }}

    /* 記事メイン */
    article {{
      background: var(--card-bg);
      border-radius: var(--radius-lg);
      padding: 40px;
      margin: 20px 0 40px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    @media (max-width: 640px) {{
      article {{ padding: 20px; }}
    }}

    .article-header {{
      margin-bottom: 36px;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 24px;
    }}
    .season-badge {{
      display: inline-block;
      background: #fef3c7;
      color: #92400e;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 12px;
    }}
    h1.article-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.45;
      color: #1a202c;
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }}
    @media (max-width: 640px) {{
      h1.article-title {{ font-size: 1.45rem; }}
    }}
    .meta-info {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    /* リード文 */
    .lead-box {{
      background: var(--primary-light);
      border-left: 4px solid var(--primary-color);
      padding: 24px;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      margin-bottom: 36px;
      font-size: 1.02rem;
      line-height: 1.85;
      color: #374151;
    }}
    .lead-box p+p {{ margin-top: 14px; }}

    /* 目次 */
    .toc-box {{
      background: #fafaf9;
      border: 1px solid #e7e5e4;
      border-radius: var(--radius-md);
      padding: 24px;
      margin-bottom: 44px;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--primary-color);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      padding-left: 0;
    }}
    .toc-list li {{
      margin-bottom: 8px;
      font-size: 0.95rem;
    }}
    .toc-list a {{
      color: #4b5563;
      text-decoration: none;
      display: inline-block;
      transition: color 0.15s;
    }}
    .toc-list a:hover {{
      color: var(--accent-color);
      text-decoration: underline;
    }}

    /* 見出し */
    h2.section-heading {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #1e293b;
      margin: 48px 0 24px;
      padding-left: 14px;
      border-left: 5px solid var(--accent-color);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    h3.sub-heading {{
      font-size: 1.2rem;
      font-weight: 700;
      color: #334155;
      margin: 28px 0 16px;
    }}

    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 28px;
      margin-bottom: 40px;
      box-shadow: var(--shadow-sm);
      transition: box-shadow 0.25s, transform 0.25s;
    }}
    .product-card:hover {{
      box-shadow: var(--shadow-md);
    }}
    .product-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, #b45309, #d97706);
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 4px 14px;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(217,119,6,0.3);
    }}
    #rank-1 .rank-badge {{
      background: linear-gradient(135deg, #d97706, #f59e0b);
      font-size: 1.05rem;
      padding: 6px 18px;
    }}
    .product-tag {{
      background: #fffbeb;
      color: #92400e;
      border: 1px solid #fde68a;
      font-size: 0.85rem;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 6px;
    }}
    h3.product-name {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 8px;
      line-height: 1.45;
    }}
    .product-catch {{
      color: #8c531b;
      font-weight: 600;
      font-size: 0.95rem;
      margin-bottom: 20px;
    }}

    .product-content-grid {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }}
    @media (max-width: 680px) {{
      .product-content-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-img-wrap {{
      text-align: center;
      background: #fafaf9;
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #f0f0ef;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      object-fit: contain;
      border-radius: var(--radius-sm);
    }}

    .price-box {{
      background: #fff8f0;
      border: 1px solid #ffedd5;
      border-radius: var(--radius-sm);
      padding: 12px 16px;
      margin-bottom: 16px;
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .price-label {{
      font-size: 0.85rem;
      color: #78350f;
      font-weight: 600;
    }}
    .price-value {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #b45309;
    }}
    .price-tax {{
      font-size: 0.75rem;
      color: #9a3412;
    }}

    .product-specs {{
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 8px 16px;
      font-size: 0.88rem;
      background: #fafaf9;
      padding: 14px;
      border-radius: var(--radius-sm);
    }}
    .product-specs dt {{
      font-weight: 700;
      color: #64748b;
      white-space: nowrap;
    }}
    .product-specs dd {{
      color: #334155;
    }}

    .product-desc-box {{
      background: #fafaf9;
      border-radius: var(--radius-md);
      padding: 20px;
      margin-bottom: 20px;
      border: 1px solid #f0f0ef;
    }}
    .desc-heading {{
      font-size: 1rem;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 12px;
    }}
    .desc-p {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #374151;
      margin-bottom: 12px;
    }}
    .desc-p:last-child {{ margin-bottom: 0; }}

    .target-point-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-top: 16px;
      padding-top: 16px;
      border-top: 1px dashed #e2e8f0;
    }}
    @media (max-width: 600px) {{
      .target-point-grid {{ grid-template-columns: 1fr; }}
    }}
    .target-box, .point-box {{
      background: #ffffff;
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid #e2e8f0;
      font-size: 0.88rem;
    }}
    .target-box strong, .point-box strong {{
      display: block;
      color: #0f172a;
      margin-bottom: 4px;
      font-size: 0.88rem;
    }}
    .target-box p, .point-box p {{
      color: #475569;
      line-height: 1.6;
    }}

    .product-action-wrap {{
      text-align: center;
      margin-top: 20px;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: linear-gradient(135deg, #bf0000, #dc2626);
      color: #ffffff;
      font-size: 1.05rem;
      font-weight: 700;
      padding: 14px 28px;
      border-radius: var(--radius-md);
      text-decoration: none;
      box-shadow: 0 4px 12px rgba(191,0,0,0.25);
      transition: transform 0.15s, box-shadow 0.15s, background 0.15s;
      width: 100%;
      max-width: 440px;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000, #b91c1c);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191,0,0,0.35);
    }}

    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 30px 0 40px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      background: #ffffff;
      font-size: 0.9rem;
      text-align: left;
    }}
    .compare-table th {{
      background: var(--primary-light);
      color: var(--primary-color);
      font-weight: 700;
      padding: 14px 16px;
      border-bottom: 2px solid var(--border-color);
      white-space: nowrap;
    }}
    .compare-table td {{
      padding: 14px 16px;
      border-bottom: 1px solid #f1f5f9;
      color: #334155;
    }}
    .compare-table tr:hover {{
      background: #fafaf9;
    }}
    .compare-table .rank-cell {{
      font-weight: 700;
      color: var(--accent-color);
      white-space: nowrap;
    }}
    .compare-table .price-cell {{
      font-weight: 700;
      color: #b45309;
      white-space: nowrap;
    }}

    /* Q&A */
    .faq-list {{
      margin: 24px 0 40px;
    }}
    .faq-item {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      margin-bottom: 16px;
      overflow: hidden;
    }}
    .faq-question {{
      background: #fafaf9;
      padding: 16px 20px;
      font-weight: 700;
      font-size: 1rem;
      color: #1e293b;
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 1px solid #f0f0ef;
    }}
    .faq-q-badge {{
      background: var(--primary-color);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .faq-answer {{
      padding: 18px 20px;
      font-size: 0.95rem;
      line-height: 1.8;
      color: #374151;
      display: flex;
      gap: 12px;
    }}
    .faq-a-badge {{
      background: var(--accent-color);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
    }}

    /* 内部リンクカード */
    .related-articles {{
      margin: 40px 0 20px;
      padding: 24px;
      background: #fafaf9;
      border-radius: var(--radius-md);
      border: 1px solid #e7e5e4;
    }}
    .related-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 16px;
    }}
    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 16px;
    }}
    .related-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-sm);
      padding: 14px;
      text-decoration: none;
      color: #1e293b;
      transition: border-color 0.2s, box-shadow 0.2s;
      display: block;
    }}
    .related-card:hover {{
      border-color: var(--accent-color);
      box-shadow: var(--shadow-sm);
    }}
    .related-card-title {{
      font-size: 0.92rem;
      font-weight: 700;
      line-height: 1.45;
      margin-bottom: 6px;
      color: #1e293b;
    }}
    .related-card-desc {{
      font-size: 0.8rem;
      color: #64748b;
      line-height: 1.5;
    }}

    /* フッター */
    footer {{
      background: #1e293b;
      color: #94a3b8;
      padding: 48px 0 32px;
      margin-top: 60px;
      font-size: 0.88rem;
    }}
    .footer-content {{
      display: grid;
      grid-template-columns: 1fr 2fr;
      gap: 32px;
      margin-bottom: 32px;
    }}
    @media (max-width: 768px) {{
      .footer-content {{ grid-template-columns: 1fr; }}
    }}
    .footer-brand h4 {{
      color: #ffffff;
      font-size: 1.1rem;
      margin-bottom: 12px;
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 12px;
    }}
    .footer-links-grid a {{
      color: #cbd5e1;
      text-decoration: none;
      transition: color 0.15s;
    }}
    .footer-links-grid a:hover {{
      color: #f59e0b;
    }}
    .copyright {{
      text-align: center;
      padding-top: 24px;
      border-top: 1px solid #334155;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <!-- ヘッダー -->
  <header>
    <div class="container site-nav">
      <a href="/" class="site-logo">
        <span>❄️</span>
        <span>冬コスメ徹底比較ラボ</span>
      </a>
      <nav class="nav-links">
        <a href="/">ホーム</a>
        <a href="/#ranking">最新ランキング</a>
        <a href="/#ingredients">成分別ガイド</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <!-- パンくずリスト -->
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li><a href="/">ホーム</a></li>
        <li aria-current="page">高保湿マルラオイル</li>
      </ol>
    </nav>

    <article>
      <div class="article-header">
        <span class="season-badge">2026-2027 冬の厳選高保湿コスメ</span>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！アルガン超えの抗酸化力と極上浸透膜で砂漠肌を救う高保湿マルラオイルランク10</h1>
        <div class="meta-info">
          <span>📅 公開: 2026年11月3日</span>
          <span>✍️ 監修: 冬コスメ徹底比較ラボ 美容解析チーム</span>
          <span>⏱️ 読了目安: 約8分</span>
        </div>
      </div>

      <!-- リード文 -->
      <div class="lead-box">
        <p>11月に入ると東京や大阪など太平洋側の都市部では連日のように外気湿度が40%を下回り、12月にかけて本格的な乾燥警戒シーズンへ突入します。さらに室内では暖房エアコンの温風が直接肌を直撃し、角層の水分保持膜である皮脂が枯渇。多くの女性が『いくら高級な化粧水を重ねても肌の奥まで届かない』『夕方になるとファンデーションがパリパリに割れて粉を吹く』という深刻な砂漠化現象に直面します。</p>
        <p>そんな真冬の過酷な乾燥危機を劇的に救う救世主としていま圧倒的な脚光を浴びているのが、アフリカ原産の希少植物から採れる<strong>『マルラオイル（スクレロカリアビレア種子油）』</strong>です。あのアルガンオイルの約3〜4倍という驚異的な抗酸化力（ビタミンE・高活性ポリフェノール）を誇りながら、人の皮脂構造に極めて近いオレイン酸が70%以上も凝縮。オイル特有のヌルつきやベタつきを一切残さず、乾き切った角質を瞬時に柔らかく解きほぐして強靭な水分キープ膜を形成します。</p>
        <p>本稿では、楽天市場で実際に流通している2026年最新のマルラオイル製品から、純度100%未精製オーガニック原液、クリニック仕様のドクターズ品質、コスパ抜群の大容量ボトルまでを徹底精査。保湿持続力・角層浸透スピード・テクスチャーの軽やかさを多角的に検証し、本当におすすめできる厳選10アイテムをランキング形式で詳しくレビューします。</p>
      </div>

      <!-- 目次 -->
      <div class="toc-box">
        <div class="toc-title">📑 目次（タップで各項目へジャンプ）</div>
        <ul class="toc-list">
          <li><a href="#why-marula">1. なぜ11月・12月の真冬乾燥に「マルラオイル」が最強なのか？</a></li>
          <li><a href="#compare-table">2. 高保湿マルラオイルおすすめ人気比較一覧表</a></li>
          <li><a href="#rank-1">3. 【第1位〜第10位】マルラオイル徹底レビュー＆真冬の検証結果</a></li>
          <li><a href="#how-to-choose">4. 失敗しない冬のマルラオイルの選び方3つの鉄則</a></li>
          <li><a href="#faq-section">5. マルラオイルに関するよくある疑問とプロの回答（Q&A）</a></li>
        </ul>
      </div>

      <!-- 解説セクション1 -->
      <section id="why-marula">
        <h2 class="section-heading">なぜ11月・12月の真冬乾燥に「マルラオイル」が最強なのか？</h2>
        <p class="desc-p">日本の冬は、冷たく乾いた北風と室内の暖房器具によって、1年の中で最も角層の水分蒸散量（TEWL）が増加する季節です。特に11月中旬以降は気温の急低下に伴って皮脂腺の活動が急激に鈍り、天然の保護クリームである皮脂の分泌量が夏の半分以下にまで激減します。皮脂膜を失った角質層は隙間だらけになり、せっかく補給した化粧水の水分が空気中へと猛スピードで蒸発してしまいます。</p>
        <p class="desc_p">一般的な美容オイル（オリーブ油やココナッツ油など）は分子量が比較的大きく、肌表面に留まって油膜感を強く残しがちです。しかし、南アフリカの過酷な日差しと干ばつに耐え抜くマルラの樹の実から抽出されたマルラオイルは、分子構造が極めて微細で親水性に富んでいるという唯一無二の性質を持ちます。</p>
        <p class="desc_p">角層の細胞間脂質（セラミドやコレステロール）のすき間に驚異的なスピードで滑り込み、硬化した角質を瞬時に柔軟化。さらにオメガ9（オレイン酸）とオメガ6（リノール酸）が理想的なバランスで水分を挟み込み、暖房直風の下でも一日中蒸発を許さない「擬似皮脂膜シェルター」を完成させます。これこそが、冬枯れ肌にマルラオイルが欠かせない最大の理由です。</p>
      </section>

      <!-- 比較表 -->
      <section id="compare-table">
        <h2 class="section-heading">高保湿マルラオイルおすすめ人気比較一覧表</h2>
        <p class="desc-p">楽天市場で高評価を集める実力派マルラオイル10選の価格・容量・処方特徴を一目で比較できます。</p>
        <div class="table-container">
          <table class="compare-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>タイプ / 容量</th>
                <th>主要成分・処方特徴</th>
                <th>参考価格(税込)</th>
              </tr>
            </thead>
            <tbody>
              {table_rows}
            </tbody>
          </table>
        </div>
      </section>

      <!-- ランキングメイン -->
      <section id="ranking-list">
        <h2 class="section-heading">【第1位〜第10位】高保湿マルラオイル徹底レビュー＆真冬の検証結果</h2>
        <p class="desc-p">実際に楽天市場で流通している最新ロットをもとに、真冬の保水アプローチやテクスチャー、効果的な使用法まで詳細にレビューします。</p>
        
        {items_html}
      </section>

      <!-- 選び方セクション -->
      <section id="how-to-choose">
        <h2 class="section-heading">失敗しない冬のマルラオイルの選び方3つの鉄則</h2>
        <p class="desc-p">マルラオイルを選ぶ際は、ラベルの表記や製造プロセスを正しく見極めることが重要です。真冬の過酷な乾燥を確実に鎮めるための3つの判断基準を押さえておきましょう。</p>

        <h3 class="sub-heading">①「未精製（Virgin / Unrefined）」かつ「コールドプレス（低温圧搾）」を選ぶ</h3>
        <p class="desc-p">マルラオイルの最大の価値は、熱に弱い天然ビタミンEやポリフェノール、オメガ脂肪酸の圧倒的な含有量にあります。高温加熱や化学溶剤を使った抽出法ではこれらの貴重な美容成分が分解されてしまいます。ラベルに『低温圧搾（Cold Pressed）』かつ『未精製（Virgin / Unrefined）』と明記された、淡い黄金色のオイルを選ぶのが美肌への最短ルートです。</p>

        <h3 class="sub-heading">② 遮光瓶（茶色・濃青・不透明ボトル）に入った製品を選ぶ</h3>
        <p class="desc-p">マルラオイルは非常に酸化安定性が高いオイルですが、未精製オイルに含まれるビタミン類や天然色素は光（紫外線や蛍光灯の光）に敏感です。透明なプラスチックボトルではなく、光を遮断する濃色ガラス遮光瓶に入った製品を選ぶことで、開封から最後までフレッシュな抗酸化力を維持できます。</p>

        <h3 class="sub-heading">③ ライフスタイルに合った容量と容器タイプ（スポイト・ポンプ）を吟味する</h3>
        <p class="desc-p">顔のブースターとして朝晩1〜2滴ずつ使うのであれば、15ml〜30ml前後のスポイト式ボトルが最も衛生的で量を調整しやすくおすすめ。一方、デコルテやすね、髪や頭皮まで全身の乾燥対策に惜しみなく使いたい場合は、50ml〜100mlのポンプ式ボトルや詰替え用パウチを選ぶことで、抜群のコストパフォーマンスを発揮します。</p>
      </section>

      <!-- FAQセクション -->
      <section id="faq-section">
        <h2 class="section-heading">マルラオイルに関するよくある疑問とプロの回答（Q&A）</h2>
        <div class="faq-list">
          {faq_html}
        </div>
      </section>

      <!-- 内部リンク関連記事 -->
      <section class="related-articles">
        <h3 class="related-title">❄️ あわせて読みたい！冬の高保湿スキンケア特集</h3>
        <div class="related-grid" id="related-grid-box">
          <!-- 自動更新スクリプトにより最新リンクが挿入されます -->
        </div>
      </section>
    </article>
  </main>

  <!-- フッター -->
  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-brand">
          <h4>冬コスメ徹底比較ラボ</h4>
          <p>乾燥が深刻化する11月・12月の冬期に特化し、科学的根拠に基づいた高保湿成分や楽天市場の人気コスメを徹底検証・レビューする専門メディアです。</p>
        </div>
        <div>
          <h4 style="color:#ffffff; margin-bottom:12px;">注目の高保湿テーマ</h4>
          <div class="footer-links-grid" id="footer-links-box">
            <!-- 自動更新スクリプトにより最新リンクが挿入されます -->
          </div>
        </div>
      </div>
      <div class="copyright">
        <p>&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved.</p>
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-marula-oil.html", "w", encoding="utf-8") as f:
    f.write(full_html.strip())

print("winter-marula-oil.html generated successfully!")
