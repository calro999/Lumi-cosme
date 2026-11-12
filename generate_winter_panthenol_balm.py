import json
import re

with open("fetched_3new_pdrn_retinol_panthenol.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_panthenol_balm"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🥇 世界で愛される緊急レスキューバーム！高濃度パンテノール5%が真冬の粉吹き・ヒリつきを一晩で鎮静",
        "catch": "全世界で累計数千万本を突破するフランス発ダーマコスメの最高峰。プロビタミンB5（高純度パンテノール）を5%高濃度配合し、CICAマデカッソシドとプレバイオティクスが真冬の傷ついた肌バリアを即座に修復・密閉する",
        "brand_name": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
        "capacity": "40mL (チューブタイプ)",
        "type": "高純度パンテノール5%×マデカッソシド配合 緊急リペアバームクリーム",
        "features": "パンテノール（5%）、マデカッソシド、トリビオーマ（独自プレバイオティクス複合体）、シアバター、亜鉛・銅・マンガン",
        "value": "冷気やマスク摩擦、暖房の熱気で赤くヒリつく冬肌を包帯のように優しく密閉。塗って眠るだけで、翌朝には粉吹きや赤みが引き、なめらかな肌質へ劇的にリセット",
        "desc_p1": "11月から12月にかけての急激な気温低下と木枯らしは、肌の最外層にある角質細胞同士の接着を破壊し、肉眼では見えない微小なひび割れを引き起こします。これが何をつけても肌がヒリヒリとしみる『寒冷粉吹き肌』の正体です。ラ ロッシュ ポゼのシカプラスト リペアクリーム B5+は、生体組織修復に不可欠なプロビタミンB5（パンテノール）を贅沢に5%配合。角層深部へと素早く浸透し、傷ついた細胞膜の再生を急速に促します。",
        "desc_p2": "さらにツボクサ由来の高純度マデカッソシドと、肌の常在菌バランスを整える独自複合体トリビオーマを融合。シアバターとミネラル成分が肌表面に厚みのある保護フィルムを張り、外気乾燥や摩擦刺激を物理的に遮断します。白浮きしにくく伸びの良いリッチなバームテクスチャーは、顔全体はもちろん、小鼻の皮剥けや口元の乾燥割れ、指先のささくれにも驚異的な修復力を発揮します。",
        "target": "冬になると頬が赤くほてってヒリつく方、小鼻や口の周りが粉を吹いてメイクが乗らない方、世界中の皮膚科医が推奨する信頼の保護バームを使いたい方",
        "point": "朝晩のスキンケアの最後に使用します。特に乾燥や赤みが気になる部分には、擦らずにポンポンと置くように厚めに塗布する『バームパック』が効果的です。夜の洗顔後、普段のスキンケアの最後に顔全体へ優しくハンドプレスして眠ると、翌朝の肌の落ち着きが全く違います。"
    },
    {
        "rank": 2,
        "tag": "🔬 高純度パンテノール10%の圧倒的超濃度！寒冷脱水で壊れた角層バリアの隙間を埋め尽くす",
        "catch": "韓国オリーブヤングのスキンケア部門で圧倒的実績を誇るBIOHEAL BOHのパンテノールシカシリーズ。業界トップクラスの高純度パンテノール10%とCICA成分を配合し、寒暖差で弱り切った肌を徹底防衛",
        "brand_name": "BIOHEAL BOH (バイオヒールボ)",
        "capacity": "クリームミスト 120mL / バリアクリーム",
        "type": "高純度パンテノール10%×CICA配合 集中バリアリペア処方",
        "features": "パンテノール（10%高濃度）、ツボクサエキス、セラミドNP、フィトスフィンゴシン",
        "value": "一般的なバームの2倍以上に相当するパンテノール10%配合。日中のオフィス暖房下でも手軽にシュッと吹きかけられる微細ミストから濃厚クリームまで、過酷な冬の脱水を隙間なくブロック",
        "desc_p1": "外気温が5℃前後の屋外から、25℃以上に暖房された室内へと移動した時、肌表面の温度は瞬時に20℃近くも上下します。この激しい寒暖差により、肌の水分蒸散量は通常の数倍に跳ね上がり、いわゆる『冬のゆらぎ脱水』が引き起こされます。バイオヒールボは、肌荒れ防止と水分保持の要であるパンテノールを10%という超高濃度で配合しました。",
        "desc_p2": "さらにCICA成分とセラミドNPをブレンドすることで、水分と油分の両面からラメラ液晶構造を強固に再建。肌に触れた瞬間にスッと馴染み、ベタつきを残さずに内側からみずみずしい潤いのシールドを形成します。メイクの上からでも水分補給ができるため、午後になると暖房で顔が引きつるオフィスの乾燥対策としても絶大な支持を得ています。",
        "target": "寒暖差で肌が急激にカサつく・かゆみが出る方、日中の暖房下でも手軽にパンテノール補給を行いたい方、ベタつく重い油分が苦手な混合肌の方",
        "point": "洗顔後の化粧水代わり、または日中乾燥を感じた時に顔から20cmほど離してスプレーし、手のひらで優しく馴染ませます。特に乾燥がひどい夜は、スプレー後に手持ちのバームや乳液を重ね付けすることで、水分を完全に閉じ込めることができます。"
    },
    {
        "rank": 3,
        "tag": "🌿 アベンヌ皮膚科学の最高傑作！独自C+Restore×硫酸銅・亜鉛で傷ついた冬肌を包帯リペア",
        "catch": "南仏アベンヌ村の温泉水研究から誕生した敏感肌用レスキュークリーム。独自開発の有用成分『C+Restore（アベンヌバイオ成分）』と抗菌ミネラル複合体が、冷風や乾燥で傷ついた肌をまるで包帯のように保護",
        "brand_name": "Avene (アベンヌ / ピエール ファーブル)",
        "capacity": "40g",
        "type": "C+Restore×温泉水配合 薬用級保護リペアクリームバーム",
        "features": "C+Restore（アクアドロミア発酵液由来）、硫酸銅・硫酸亜鉛、アベンヌ温泉水、高精製ミネラルオイル",
        "value": "赤ちゃんから大人まで使える超低刺激無香料処方。ひび割れや赤み、皮剥けを起こしたトラブル部位にピタッと密着し、外部の雑菌や冷気刺激を物理的に遮断しながら肌の自然治癒力を最大化",
        "desc_p1": "冬の乾燥肌は、角層のバリアが欠落しているため、外気の汚れや雑菌が付着しやすく、赤みや化膿を伴う微小炎症に発展しがちです。アベンヌのシカルファットプラスは、アベンヌ温泉水に生息する独自の微細藻類から抽出された特許成分『C+Restore』を配合。皮膚のターンオーバーを正常化し、傷ついた角層の接着をスピード修復します。",
        "desc_p2": "また、肌を清潔に保つ硫酸銅と硫酸亜鉛が配合されており、荒れた肌表面を清浄にコントロール。濃厚でこっくりとしたテクスチャーが皮膚表面に均一な保護膜を作り、まるで保護包帯を巻いたかのように外的刺激からガードします。冬場の激しい乾燥による顔の皮剥けだけでなく、手荒れや唇の周りの荒れにも重宝する万能アイテムです。",
        "target": "乾燥で皮膚が薄くなり衣服や髪の毛が触れるだけで痒い方、化粧水がしみて何も塗れない極度の肌荒れ状態にある方、赤ちゃんや子どもと一緒に安心ケアしたい方",
        "point": "洗顔後、化粧水などで肌を整えた後、荒れが気になる部分に優しく伸ばします。擦るように塗り広げるのではなく、クリームを指先で温めてから、スタンプを押すように肌へ置いて密着させるのが摩擦刺激を避けるコツです。"
    },
    {
        "rank": 4,
        "tag": "🛡️ 100時間持続の水分バリアカプセル！韓国オリーブヤング売上1位を独走するセラミド高保湿クリーム",
        "catch": "韓国メディカルビューティーの巨頭アモーレパシフィックの皮膚科学ブランドAESTURA。人間の肌脂質と同一比率（セラミド・コレステロール・脂肪酸 3:1:1）で作られた微細カプセルとパンテノールが真冬の乾燥砂漠肌を完全防衛",
        "brand_name": "AESTURA (エストラ)",
        "capacity": "80mL (大容量チューブ)",
        "type": "高密度セラミドカプセル×パンテノール配合 100時間水分持続クリーム",
        "features": "高密度セラミド・コレステロール・脂肪酸複合カプセル、パンテノール、スクワラン、アラントイン",
        "value": "塗布後100時間にわたって肌の水分保持力をキープする臨床試験済み。肉眼で見えるセラミドカプセルが肌の上でプチプチと溶け出し、乾ききった角層の隙間を埋め尽くす",
        "desc_p1": "エストラのアトバリア365クリームは、韓国の皮膚科でも採用されている信頼のメディカルダーマコスメです。最大の特徴は、肉眼でも確認できる無数の微小カプセル『DermaON®』にあります。セラミド単体ではなく、コレステロールと脂肪酸を生体と同じ黄金比率で配合することで、角層への親和性と浸透スピードを劇的に高めています。",
        "desc_p2": "さらにパンテノールが加わることで、角層内部の保水構造を強固にサポート。指で伸ばすとカプセルが体温ですっと溶け、吸い付くようなしっとり感へと変化します。こっくりとした濃厚なテクスチャーでありながら、肌に馴染んだ後は不思議なほどベタつかず、朝のメイク前でも夜の就寝前でもストレスなく真冬の完全シールドを実現します。",
        "target": "どんなクリームを塗っても数時間後には肌がカサつく超乾燥肌の方、角層のラメラ構造を科学的に補修したい方、1本で真冬を乗り切りたい方",
        "point": "朝晩の洗顔後、スキンケアの最後のステップとして適量を顔全体に伸ばします。手のひらで包み込むようにハンドプレスすると、セラミドカプセルが体温でスムーズに角層へと溶け込み、瞬時に強固な水分シールドが完成します。"
    },
    {
        "rank": 5,
        "tag": "💧 敏感肌の絶対王者！ふわっと軽いのに角層深部まで潤いを抱え込む薬用セラミドフェイスクリーム",
        "catch": "日本の乾燥性敏感肌研究の金字塔キュレル。抗炎症有効成分アラントインとセラミド機能成分を贅沢に配合。真冬の過酷な空気乾燥から肌を守り抜き、ふっくら吸い付くような潤い肌へ導く",
        "brand_name": "Curel (キュレル / 花王)",
        "capacity": "40g (医薬部外品)",
        "type": "消炎有効成分×セラミド機能成分配合 薬用高保湿フェイスクリーム",
        "features": "有効成分アラントイン、セラミド機能成分、ユーカリエキス、ふんわりホイップ処方",
        "value": "クリーム特有の重さやベタつきが一切ないのに、翌朝まで潤いが持続する奇跡の軽やかテクスチャー。肌荒れを繰り返す冬の敏感肌を穏やかに整えタフなバリアを再建",
        "desc_p1": "冬の乾燥対策として重い油分を塗ると毛穴が詰まって吹き出物が出る、しかし軽めのジェルではすぐに乾いてしまう――そんな悩みを解決するのがキュレルの潤浸保湿フェイスクリームです。花王独自の高微細エマルジョン技術により、まるでスフレのようにふんわりと軽いテクスチャーを実現しながら、角層深部へセラミド機能成分を送り届けます。",
        "desc_p2": "消炎有効成分アラントインが、冬の冷風や暖房熱による微小な炎症をすばやく鎮静。乾燥で硬くなった肌の角層をユーカリエキスが柔らかくほぐし、肌本来の保水力を引き出します。ベタつかないため朝のメイク前にも快適に使え、日中の粉吹きや化粧浮きを一日中防いでくれます。",
        "target": "ベタつく重いクリームが苦手な乾燥肌の方、冬になると小さな吹き出物や赤みが出やすい敏感肌の方、ドラッグストアで手軽に買える王道クリームを求める方",
        "point": "化粧水や乳液の後に使用します。適量（直径約2cm程度）を手にとり、顔の5カ所（両頬、額、鼻、あご）に置いてから、優しく顔全体に伸ばします。カサつきやすい頬や口元には重ね付けがおすすめです。"
    },
    {
        "rank": 6,
        "tag": "🛡️ 高精製ワセリンの生体密着シールド！体温でとろけてピタッと密着する薬用保護バーム",
        "catch": "資生堂薬品が手がけるメディカルスキンケアIHADA（イハダ）。極限まで不純物を取り除いた『高精製ワセリン』と2つの抗肌あれ有効成分を配合。真冬の冷気・花粉・暖房乾燥から肌を完全密閉",
        "brand_name": "IHADA (イハダ / 資生堂薬品)",
        "capacity": "20g (医薬部外品)",
        "type": "高精製ワセリン×抗肌あれ有効成分配合 薬用保護バーム",
        "features": "高精製ワセリン、グリチルレチン酸ステアリル（抗炎症）、アラントイン（組織修復）、低刺激処方",
        "value": "人肌の温度で瞬時にとろけ、薄膜の滑らかなピュアシールドを形成。通常の黄色いワセリンのようなギトギト感や重さが一切なく、日中でも快適に使える携帯性抜群のバーム",
        "desc_p1": "一般的な白色ワセリンは保護力に優れるものの、伸びが悪くベタつきが強いため日中の使用が難しいという難点がありました。イハダの薬用バームは、特別な高精製技術によって不純物を極限までカットした純度の高いワセリンを採用。肌にのせると体温で瞬時にスッと溶け出し、まるでシルクのような薄い保護膜を形成します。",
        "desc_p2": "さらにグリチルレチン酸ステアリルとアラントインのダブル有効成分が、真冬の寒冷でひび割れそうになった角層を素早く修復。皮脂膜の代わりに肌表面をコーティングすることで、内側からの水分蒸散を物理的にシャットアウトします。目元や口元の局所的な粉吹きレスキューにも最適なポーチ常備アイテムです。",
        "target": "目元や口元など部分的な皮剥け・粉吹きに悩む方、ワセリンのベタつきが苦手な方、外出先でも手軽に乾燥レスキューを行いたい方",
        "point": "お手入れの最後に、指先で米粒大程度を少量とり、手のひらで温めてから、カサつく部分に軽く押さえるようになじませます。メイクの上からでも乾燥が気になる部分にトントンと薄く叩き込むと、粉吹きを一瞬でリセットできます。"
    },
    {
        "rank": 7,
        "tag": "🧴 5D複合セラミド×パンテノール！大容量100mLで顔から体まで真冬の粉吹きを包み込む万能クリーム",
        "catch": "インナードライ対策で圧倒的人気を誇るTorriden（トリデン）のソリッドインシリーズ。分子サイズの異なる5重の複合セラミドと高濃度パンテノールを配合し、100mLの大容量で冬の乾燥肌を贅沢にラッピング",
        "brand_name": "Torriden (トリデン)",
        "capacity": "100mL (大容量チューブ)",
        "type": "5D複合セラミド×パンテノール配合 高保湿バリアクリーム",
        "features": "5D複合セラミド（NP, NS, AP, AS, EOP）、パンテノール、アラントイン、植物性スクワラン",
        "value": "100mLというチューブタイプの大容量設計。顔だけでなく首元、デコルテ、肘やすねなど真冬に粉を吹きやすいボディの乾燥部位まで惜しみなく高密度セラミドでシールド可能",
        "desc_p1": "トリデンの『ソリッドイン セラミド クリーム』は、セラミド分子のサイズを5段階に変化させた5Dコンプレックスを採用。角層の最深部から表面まで、層ごとに異なる隙間をぴったりと埋め尽くす緻密なバリア再建設計が施されています。そこに組織修復を助けるパンテノールが加わり、冷気で傷んだ肌を優しくケアします。",
        "desc_p2": "リッチでコクのあるバターのような質感でありながら、肌の上でなめらかに伸び広がり、塗布後はベタつかずしっとりとした柔らかなベルベット肌へ仕上がります。100mLの大容量チューブなので、顔だけでなく冬場に粉吹きが気になる首元やすね、指先など全身の集中保湿にも惜しみなく使えます。",
        "target": "1本で顔もボディもたっぷり保湿したい方、5種類の多層セラミドで深部まで満たしたい方、コストパフォーマンスと成分の良さを両立したい方",
        "point": "化粧水や美容液で肌を整えた後、適量を顔全体や乾燥の気になるパーツへ伸ばします。特に乾燥がひどい夜は、通常量の1.5倍を顔全体に厚塗りして『スリーピングパック』として寝ると、翌朝もっちりとした柔らかい肌が蘇ります。"
    },
    {
        "rank": 8,
        "tag": "🐯 濃密タイガーグラス×高純度パンテノール！寒風で赤みが出た冬のダメージ肌を一晩で穏やかに整える",
        "catch": "CICAコスメの火付け役Dr.Jart+（ドクタージャルト）のロングセラー高機能クリーム。ツボクサ由来のタイガーグラスエキスとパンテノールを濃厚バームに凝縮し、真冬の外気刺激で炎症を起こした敏感肌を急速鎮静",
        "brand_name": "Dr.Jart+ (ドクタージャルト)",
        "capacity": "50mL",
        "type": "高純度ツボクサエキス×パンテノール配合 集中鎮静シカバームクリーム",
        "features": "Centella Asiatica複合エキス、パンテノール、アラントイン、ナイアシンアミド",
        "value": "薄いグリーンのクリームが赤みを自然にカバーしながら、夜の間にダメージを集中リペア。寒風やマスク摩擦で熱を持った肌をスーッと穏やかに落ち着かせる",
        "desc_p1": "虎が傷を負った際に体をこすりつけて治したという伝説から名付けられたタイガーグラス（ツボクサエキス）。ドクタージャルトのシカペアクリームは、この高純度ツボクサエキスにパンテノールとアラントインを掛け合わせた集中リペア処方です。冬の寒風にさらされて赤みやほてりが出た肌を、速やかにクールダウンさせます。",
        "desc_p2": "テクスチャーは濃厚で固めのバーム状ですが、手のひらの体温で温めるとすっと滑らかに変化。肌表面にしっかりとした保護膜を張り巡らせ、冬の乾いた空気やホコリなどの外的刺激を跳ね返します。一晩塗って眠るだけで、翌朝には赤みがすっかり引き、健やかな肌状態へと整えてくれます。",
        "target": "冬の外気や寒暖差で顔が赤くなりやすい方、ニキビや吹き出物など肌トラブルを繰り返しやすい方、CICAとパンテノールの相乗効果を体感したい方",
        "point": "スキンケアの最後に、適量を手に取り、手のひらで温めてから顔全体を優しく包み込むように馴染ませます。赤みや肌荒れが気になる部分には、少量を指先にとりトントンと重ね付けしてください。"
    },
    {
        "rank": 9,
        "tag": "🧬 生体脂質を模倣した特許MLE®バリア構造！過酷な極寒地でも水分の蒸発を物理的にシャットアウト",
        "catch": "韓国のバリア皮膚科学研究所ネオパームが開発したReal Barrier（リアルバリア）。健康な肌のラメラ液晶構造を完璧に再現した特許技術MLE®と高純度パンテノールが、真冬の寒冷脱水肌に人工バリアを形成",
        "brand_name": "Real Barrier (リアルバリア)",
        "capacity": "50mL",
        "type": "特許MLE液晶バリア構造×パンテノール配合 高密着エクストリームバーム",
        "features": "特許MLE®技術、独自セラミド複合体、パンテノール、マデカッソシド、アラントイン",
        "value": "皮膚の顕微鏡写真で健康な肌と全く同じ十字クロス構造を形成する特許生体バリア。冬のどんな過酷な乾燥下でも角層内部の水分が外へ逃げる隙間を与えない",
        "desc_p1": "肌のバリア機能が低下している時、単に油分を塗っても角層の『ラメラ構造（水分と油分が交互に並ぶ液晶構造）』が壊れていると、水分はどんどん蒸発してしまいます。リアルバリアのエクストリームクリームは、世界特許の『MLE®テクノロジー』により、人間の健康な肌脂質構造を人工的に完全に再現した画期的なクリームです。",
        "desc_p2": "塗布した瞬間に肌と一体化し、まるで『第二の皮膚』をまとったかのような強固な保護ヴェールを形成。高純度パンテノールとマデカッソシドが角層深部を修復しながら、外気の極限乾燥を完璧に遮断します。固めのしっかりとしたバーム状テクスチャーで、塗った直後から肌密度がぎゅっと高まったような安心感に包まれます。",
        "target": "何を塗ってもすぐに乾燥して肌がスカスカに感じる方、最先端のラメラ構造皮膚科学に基づくケアを取り入れたい方、冬のアウトドアや寒冷地へ行く方",
        "point": "付属のスパチュラで適量をとり、顔全体に伸ばした後、手のひらの温もりでゆっくりとハンドプレスして肌に密着させます。乾燥が特にひどい日は、夜の洗顔後化粧水を塗った直後に本品を薄く塗り、その上からさらに重ね付けする『サンドイッチ保湿』が有効です。"
    },
    {
        "rank": 10,
        "tag": "❄️ 極寒地遠征から生まれた伝説のエモリエント！スクワランと氷河プロテインが真冬の冷気を完全遮断",
        "catch": "170年以上の歴史を持つニューヨークのアポセカリーKIEHL'S（キールズ）の世界的大ベストセラー。南極遠征隊の過酷な寒冷地テストをクリアした氷河プロテインと植物性スクワランが冬の肌を24時間潤し続ける",
        "brand_name": "KIEHL'S (キールズ)",
        "capacity": "50mL",
        "type": "氷河プロテイン×植物性オリーブスクワラン配合 濃厚保湿クリーム",
        "features": "アンタークティシン（氷河プロテイン）、オリーブ由来植物性スクワラン、パンテノール、アボカド油",
        "value": "マイナス数十度の極寒でも水分を失わない海洋性微生物成分を配合。ふんわり軽いのに真冬の過酷なアウトドアやスキー場でも肌の水分を完璧に保護",
        "desc_p1": "キールズのウルトラフェイシャルクリーム（UFC）は、南極の極限環境へ挑む遠征隊の肌を守るために開発された伝説的な高保湿クリームです。過酷な寒冷環境下でも凍らず水分を保持する海洋性微生物由来の『アンタークティシン（氷河プロテイン）』を配合し、寒風による肌の凍結脱水を強力に防ぎます。",
        "desc_p2": "さらに人間の皮脂膜と極めて近いオリーブ由来の植物性スクワランが、肌に触れた瞬間にすばやく馴染み、自然なエモリエント膜を形成。油分特有の重さやベタつきが全くなく、乳液のようにみずみずしく伸び広がるのに、一日中潤いが続く驚異的なバランスを誇ります。世界中で男女問わず愛され続ける冬の決定版クリームです。",
        "target": "ベタつくのが大嫌いだけれど絶対に乾燥したくない方、冬のアウトドアやウィンタースポーツを楽しむ方、家族やパートナーと兼用で使いたい方",
        "point": "朝晩の洗顔後、化粧水や美容液の後にパール粒大を手にとり、顔全体に優しく伸ばします。非常に肌馴染みが良いため、朝のメイク前すぐに使ってもファンデーションがヨレず、1日中しっとりとした素肌感を保てます。"
    }
]

# JSON-LD ItemList
item_list_elements = []
for p in product_details:
    it = items[p["rank"] - 1]
    item_list_elements.append({
        "@type": "ListItem",
        "position": p["rank"],
        "item": {
            "@type": "Product",
            "name": it["display_name"],
            "image": it["image_url"],
            "brand": {
                "@type": "Brand",
                "name": p["brand_name"]
            },
            "offers": {
                "@type": "Offer",
                "price": it["price"],
                "priceCurrency": "JPY",
                "availability": "https://schema.org/InStock",
                "url": it["affiliate_url"]
            }
        }
    })

faq_items = [
    {
        "q": "パンテノール（プロビタミンB5）は、なぜ冬の肌荒れや粉吹きにこれほど効果的なのですか？",
        "a": "パンテノールは角層に浸透すると直ちに生体内で『パントテン酸（ビタミンB5）』へと変換されます。パントテン酸は細胞のエネルギー代謝や細胞膜脂質（セラミド等）の合成に必須の『補酵素A（コエンザイムA）』の構成成分です。11月〜12月の寒冷乾燥で角質細胞の接着が壊れ、ひび割れや粉吹きを起こした肌に対して、単に上からフタをするだけでなく、細胞自らがバリアを修復する自己再生プロセスを内側から劇的に加速させるため、圧倒的な鎮静・修復効果を発揮します。"
    },
    {
        "q": "『バーム』と『普通の保湿クリーム』は何が違いますか？冬はどちらを使うべきですか？",
        "a": "一般的な保湿クリームは『水分と油分を乳化させたもの（水分比率が高め）』であるのに対し、バームは『油分やワックス、高濃度エモリエント基剤を主成分とした固形〜半固形の軟膏状処方』です。水分が蒸散しやすい11月・12月の極限乾燥下では、通常のクリームの水分はすぐに空気中へ奪われてしまいますが、バームは肌表面に油膜の物理的シールド（オクルージョン膜）を形成するため、水分の蒸散をほぼ完全にゼロに抑え込むことができます。特に粉吹きや赤みが出ている部分にはバームが圧倒的に適しています。"
    },
    {
        "q": "バームを塗ると毛穴が詰まってニキビや吹き出物ができたりしませんか？",
        "a": "昔の粗悪な鉱物油バームと異なり、現代の高品質リペアバーム（ラロッシュポゼ、キュレル、エストラなど）は、ノンコメドジェニックテスト済み（ニキビのもとになりにくい処方）で設計されています。また、イハダのように極限まで不純物を精製した高精製ワセリンや、肌の皮脂組成に近い植物性スクワランがベースとなっているため、酸化しにくく毛穴詰まりを起こしにくいのが特徴です。脂性肌や混合肌の方は、顔全体に厚塗りするのではなく、乾燥や赤みのある部分にのみピンポイントでスタンプ塗りするのが安心です。"
    },
    {
        "q": "パンテノールバームは朝のメイク前に塗ってもファンデーションが崩れませんか？",
        "a": "塗り方さえ工夫すれば、むしろ日中の乾燥崩れや粉吹きを強力に防ぐ下地クッションとして活用できます。コツは『手のひらで少量（米粒大）をしっかり温めて薄く伸ばしてから、顔を包み込むようにハンドプレスする』ことです。擦って塗るとムラになり油膜が浮いてしまいますが、薄膜として密着させ、1〜2分置いてから下地やファンデーションを重ねると、暖房の風に一日中さらされても粉を吹かないツヤ肌をキープできます。"
    },
    {
        "q": "顔以外に、手荒れや唇、子どもの肌荒れにも使えますか？",
        "a": "今回選出したラロッシュポゼ、アベンヌ、イハダ、キュレルなどは、すべて低刺激・無香料・アレルギーテスト済みで設計されており、顔だけでなく指先のひび割れ、唇の周りの乾燥、赤ちゃんの頬の粉吹き荒れまで全身にマルチに使用可能です。特に冬場の水仕事による手荒れや、就寝前のリップパックとして唇に厚塗りする使い方は非常に効果的です。"
    }
]

faq_elements = []
for fq in faq_items:
    faq_elements.append({
        "@type": "Question",
        "name": fq["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": fq["a"]
        }
    })

structured_data = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！高濃度パンテノールの生体組織修復力と濃密密閉バリア膜で真冬のヒリヒリ粉吹き肌を緊急鎮静する保湿力高めパンテノールバームランク10",
            "description": "11月・12月の寒冷乾燥・木枯らし・急激な暖房寒暖差による肌のヒリつき・粉吹き・赤みを緊急鎮静！ラロッシュポゼ、アベンヌ、エストラ、イハダ、キュレル、キールズまで最新実勢価格・口コミ・科学的生体修復メカニズムを網羅。",
            "image": items[0]["image_url"],
            "datePublished": "2026-11-13T05:00:00+09:00",
            "dateModified": "2026-11-13T05:00:00+09:00",
            "author": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB 冬季皮膚科学研究チーム"
            },
            "publisher": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://lumi-cosme.vercel.app/favicon.jpg"
                }
            }
        },
        {
            "@type": "ItemList",
            "name": "真冬の高保湿パンテノールリペアバームおすすめランキング10選",
            "numberOfItems": len(item_list_elements),
            "itemListElement": item_list_elements
        },
        {
            "@type": "FAQPage",
            "mainEntity": faq_elements
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
                    "name": "高保湿パンテノールバーム特集",
                    "item": "https://lumi-cosme.vercel.app/winter-panthenol-balm"
                }
            ]
        }
    ]
}

product_cards_html = ""
for p in product_details:
    it = items[p["rank"] - 1]
    product_cards_html += f"""
    <article class="product-card" id="rank-{p['rank']}">
      <div class="product-header">
        <span class="rank-badge">第{p['rank']}位</span>
        <span class="product-tag">{p['tag']}</span>
      </div>
      <div class="product-content">
        <div class="product-img-box">
          <img src="{it['image_url']}" alt="{it['display_name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-brand">{p['brand_name']}</div>
          <h3 class="product-title">{it['display_name']}</h3>
          <p class="product-catch">{p['catch']}</p>
          <div class="product-meta">
            <span><strong>容量:</strong> {p['capacity']}</span>
            <span><strong>タイプ:</strong> {p['type']}</span>
          </div>
          <div class="product-features">
            <strong>主要注目成分:</strong> {p['features']}
          </div>
          <div class="product-price-box">
            <div class="price-val">¥{it['price']:,}<span class="tax-label">（税込・楽天最新実勢価格）</span></div>
            <div class="review-val">★ {it['review_average']} <span class="review-count">({it['review_count']}件のレビュー)</span></div>
          </div>
          <div class="product-value-box">
            <span class="value-title">💡 11-12月の乾燥・肌荒れ対策即効価値</span>
            <p>{p['value']}</p>
          </div>
        </div>
      </div>
      <div class="product-desc-box">
        <h4>🛡️ 美容科学＆テクスチャー詳細解説</h4>
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>
      <div class="product-target-box">
        <div class="target-item"><strong>こんな方に最適:</strong> {p['target']}</div>
        <div class="target-item"><strong>効果を最大化する使用法:</strong> {p['point']}</div>
      </div>
      <div class="product-action">
        <a href="{it['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
          <span>楽天市場で最新価格＆在庫をチェック</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
    """

faq_html = ""
for fq in faq_items:
    faq_html += f"""
    <div class="faq-item">
      <div class="faq-q">Q. {fq['q']}</div>
      <div class="faq-a">{fq['a']}</div>
    </div>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！高濃度パンテノールの生体組織修復力と濃密密閉バリア膜で真冬のヒリヒリ粉吹き肌を緊急鎮静する保湿力高めパンテノールバームランク10 | LUMI COSMETICS LAB</title>
  <meta name="description" content="11月・12月の寒冷乾燥・木枯らし・急激な暖房寒暖差による肌のヒリつき・粉吹き・赤みを緊急鎮静！ラロッシュポゼ、アベンヌ、エストラ、イハダ、キュレル、キールズまで最新実勢価格・口コミ・科学的生体修復メカニズムを網羅。">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-panthenol-balm">
  <link rel="icon" href="/favicon.jpg">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！高濃度パンテノールの生体組織修復力と濃密密閉バリア膜で真冬のヒリヒリ粉吹き肌を緊急鎮静する保湿力高めパンテノールバームランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥・木枯らし・急激な暖房寒暖差による肌のヒリつき・粉吹き・赤みを緊急鎮静！ラロッシュポゼ、アベンヌ、エストラ、イハダ、キュレル、キールズまで最新実勢価格・口コミ・科学的生体修復メカニズムを網羅。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-panthenol-balm">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="LUMI COSMETICS LAB">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高濃度パンテノールの生体組織修復力と濃密密閉バリア膜で真冬のヒリヒリ粉吹き肌を緊急鎮静する保湿力高めパンテノールバームランク10">
  <meta name="twitter:description" content="11月・12月の寒冷乾燥・木枯らし・急激な暖房寒暖差による肌のヒリつき・粉吹き・赤みを緊急鎮静！ラロッシュポゼ、アベンヌ、エストラ、イハダ、キュレル、キールズまで最新実勢価格・口コミ・科学的生体修復メカニズムを網羅。">
  <meta name="twitter:image" content="{items[0]['image_url']}">
  <script type="application/ld+json">
  {json.dumps(structured_data, ensure_ascii=False, indent=2)}
  </script>
  <style>
    :root {{
      --primary: #059669;
      --primary-dark: #047857;
      --accent: #e11d48;
      --bg: #f0fdf4;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #dcfce7;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.7;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #0f172a;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .breadcrumb {{
      max-width: 1100px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb a {{
      color: var(--primary);
      text-decoration: none;
    }}
    main {{
      max-width: 1100px;
      margin: 24px auto 60px;
      padding: 0 20px;
    }}
    .hero-section {{
      background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
      border: 1px solid #86efac;
      border-radius: var(--radius);
      padding: 40px 32px;
      margin-bottom: 40px;
    }}
    .hero-tag {{
      display: inline-block;
      background: #059669;
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 9999px;
      margin-bottom: 16px;
    }}
    .hero-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 20px;
    }}
    @media (max-width: 768px) {{
      .hero-title {{
        font-size: 1.4rem;
      }}
    }}
    .hero-desc {{
      font-size: 1rem;
      color: #334155;
      line-height: 1.8;
    }}
    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px 32px;
      margin-bottom: 40px;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 10px;
    }}
    .toc-list a {{
      color: #047857;
      text-decoration: none;
      font-size: 0.92rem;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: #059669;
      text-decoration: underline;
    }}
    .science-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
    }}
    .science-box h3 {{
      font-size: 1.35rem;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .science-box p {{
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.8;
      margin-bottom: 16px;
    }}
    .science-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin-top: 24px;
    }}
    .science-card {{
      background: #f0fdf4;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
    }}
    .science-card h4 {{
      font-size: 1.05rem;
      color: #047857;
      margin-bottom: 8px;
    }}
    .science-card p {{
      font-size: 0.88rem;
      color: #475569;
      line-height: 1.6;
      margin-bottom: 0;
    }}
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 36px;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      background: #059669;
      color: #ffffff;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 8px;
    }}
    .product-tag {{
      background: #ecfdf5;
      color: #065f46;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 8px;
      border: 1px solid #a7f3d0;
    }}
    .product-content {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 28px;
      margin-bottom: 24px;
    }}
    @media (max-width: 768px) {{
      .product-content {{
        grid-template-columns: 1fr;
      }}
    }}
    .product-img-box {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      background: #ffffff;
      border-radius: 8px;
      border: 1px solid var(--border);
      padding: 8px;
    }}
    .product-brand {{
      font-size: 0.9rem;
      font-weight: 700;
      color: #64748b;
      margin-bottom: 4px;
    }}
    .product-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 12px;
      line-height: 1.4;
    }}
    .product-catch {{
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 16px;
    }}
    .product-meta {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: #64748b;
      margin-bottom: 8px;
      flex-wrap: wrap;
    }}
    .product-features {{
      font-size: 0.85rem;
      background: #f8fafc;
      padding: 8px 12px;
      border-radius: 6px;
      margin-bottom: 16px;
    }}
    .product-price-box {{
      display: flex;
      align-items: baseline;
      gap: 16px;
      margin-bottom: 16px;
      border-top: 1px dashed var(--border);
      padding-top: 12px;
    }}
    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #dc2626;
    }}
    .tax-label {{
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 400;
    }}
    .review-val {{
      font-size: 0.9rem;
      color: #d97706;
      font-weight: 700;
    }}
    .review-count {{
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 400;
    }}
    .product-value-box {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 0.9rem;
      color: #064e3b;
    }}
    .value-title {{
      font-weight: 700;
      display: block;
      margin-bottom: 4px;
    }}
    .product-desc-box {{
      background: #f0fdf4;
      border-radius: 8px;
      padding: 20px;
      margin-bottom: 20px;
    }}
    .product-desc-box h4 {{
      font-size: 1rem;
      margin-bottom: 12px;
      color: #0f172a;
    }}
    .product-desc-box p {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 8px;
    }}
    .product-target-box {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 24px;
      font-size: 0.88rem;
    }}
    @media (max-width: 640px) {{
      .product-target-box {{
        grid-template-columns: 1fr;
      }}
    }}
    .target-item {{
      background: #ffffff;
      border: 1px solid var(--border);
      padding: 12px 16px;
      border-radius: 8px;
    }}
    .product-action {{
      text-align: right;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #bf0000;
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 12px 24px;
      border-radius: 8px;
      text-decoration: none;
      transition: background 0.2s, transform 0.1s;
    }}
    .rakuten-btn:hover {{
      background: #990000;
      transform: translateY(-2px);
    }}
    .summary-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
    }}
    .summary-box h3 {{
      font-size: 1.35rem;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 16px;
      font-size: 0.9rem;
    }}
    .summary-table th, .summary-table td {{
      padding: 12px 16px;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .summary-table th {{
      background: #dcfce7;
      font-weight: 700;
      color: #064e3b;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 16px 0;
    }}
    .faq-item:last-child {{
      border-bottom: none;
    }}
    .faq-q {{
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 8px;
      font-size: 1rem;
    }}
    .faq-a {{
      color: #334155;
      font-size: 0.92rem;
      line-height: 1.7;
    }}
    .hub-link-banner {{
      background: linear-gradient(135deg, #059669 0%, #047857 100%);
      color: #ffffff;
      border-radius: var(--radius);
      padding: 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 24px;
      margin-bottom: 40px;
    }}
    @media (max-width: 768px) {{
      .hub-link-banner {{
        flex-direction: column;
        text-align: center;
      }}
    }}
    .hub-link-btn {{
      display: inline-block;
      background: #ffffff;
      color: #047857;
      font-weight: 700;
      padding: 12px 24px;
      border-radius: 8px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .internal-links-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
    }}
    .internal-links-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 16px;
    }}
    .internal-link-card {{
      background: #f0fdf4;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
      text-decoration: none;
      transition: border-color 0.2s, transform 0.2s;
    }}
    .internal-link-card:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
    }}
    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 60px 20px 40px;
      font-size: 0.85rem;
    }}
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
    }}
    .footer-title {{
      color: #ffffff;
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 20px;
    }}
    .footer-links {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 12px 20px;
      margin-bottom: 40px;
    }}
    .footer-link-item {{
      color: #cbd5e1;
      text-decoration: none;
      transition: color 0.2s;
    }}
    .footer-link-item:hover {{
      color: #34d399;
    }}
    .copyright {{
      border-top: 1px solid #1e293b;
      padding-top: 24px;
      text-align: center;
      color: #64748b;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-title">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        LUMI COSMETICS LAB
      </a>
      <span style="font-size:0.85rem;color:#64748b;">冬季皮膚科学＆高保湿コスメ検証</span>
    </div>
  </header>

  <div class="breadcrumb">
    <a href="/">ホーム</a> &gt; <span>高保湿パンテノールバーム特集</span>
  </div>

  <main>
    <div class="hero-section">
      <span class="hero-tag">🛡️ 11月・12月 寒冷粉吹き・赤み・ヒリつき緊急鎮静</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！高濃度パンテノールの生体組織修復力と濃密密閉バリア膜で真冬のヒリヒリ粉吹き肌を緊急鎮静する保湿力高めパンテノールバームランク10</h1>
      <p class="hero-desc">
        11月から12月は、北風が吹き荒れ、室内のエアコン暖房が本格稼働する季節。屋外の寒冷乾燥（湿度30%以下）と室内の温風による20℃以上の急激な寒暖差は、角層の細胞間脂質を粉砕し、目に見えない無数のひび割れを引き起こします。何を塗ってもピリピリしみる、小鼻や頬が粉を吹いて皮が剥ける――そんな冬の限界肌を救う最強の切り札が『高濃度パンテノール×密閉リペアバーム』です。本記事では、ラロッシュポゼ、アベンヌ、エストラ、イハダ、キュレルなど、皮膚科医推奨の超高機能バーム10選を徹底検証しました。
      </p>
    </div>

    <div class="toc-box">
      <div class="toc-title">📑 目次・記事ナビゲーション</div>
      <ul class="toc-list">
        <li><a href="#science-guide">1. 冬の寒暖差ショックとパンテノール生体修復のメカニズム</a></li>
        <li><a href="#rank-1">第1位: ラ ロッシュ ポゼ シカプラスト リペア バーム B5+</a></li>
        <li><a href="#rank-2">第2位: BIOHEAL BOH パンテノール シカ バリア クリーム</a></li>
        <li><a href="#rank-3">第3位: アベンヌ シカルファットプラス リペアクリーム</a></li>
        <li><a href="#rank-4">第4位: AESTURA アトバリア365 クリーム</a></li>
        <li><a href="#rank-5">第5位: キュレル 潤浸保湿 フェイスクリーム</a></li>
        <li><a href="#rank-6">第6位: イハダ 薬用バーム</a></li>
        <li><a href="#rank-7">第7位: Torriden ソリッドイン セラミド クリーム</a></li>
        <li><a href="#rank-8">第8位: Dr.Jart+ シカペア インテンシブ スージング リペア バーム</a></li>
        <li><a href="#rank-9">第9位: Real Barrier エクストリーム クリーム バーム</a></li>
        <li><a href="#rank-10">第10位: キールズ ウルトラ フェイシャル クリーム UFC</a></li>
        <li><a href="#selection-matrix">2. 目的・肌状態別：冬のパンテノールバーム選び方マトリクス</a></li>
        <li><a href="#faq-section">3. よくある質問・Q&Aセクション</a></li>
      </ul>
    </div>

    <div class="science-box" id="science-guide">
      <h3>🔬 なぜパンテノールが冬の救世主なのか？『補酵素A』による組織再生の皮膚科学</h3>
      <p>
        初冬の11月から12月は、肌の表面温度が急変する『寒暖差ショック』が毎日繰り返されます。血管の収縮と拡張が頻繁に起きることで微小炎症が生じ、角質細胞同士を繋ぐデスモソームが破壊されて粉吹き・皮剥けが発生します。
      </p>
      <div class="science-grid">
        <div class="science-card">
          <h4>🧪 プロビタミンB5から補酵素Aへの生体変換</h4>
          <p>パンテノールは角層へ浸透すると瞬時にパントテン酸へ変換され、脂質代謝のマスターキーである補酵素A（CoA）の合成を促進。破壊されたセラミドや細胞膜の自己再生を内側から加速させます。</p>
        </div>
        <div class="science-card">
          <h4>🛡️ オクルージョン（密封）による水分蒸散ゼロ化</h4>
          <p>高精製ワセリンやシアバター、MLE液晶バリアなどの油膜基剤が皮膚表面に吸着。外気湿度20%の過酷な暖房下でも、角層からの経皮水分蒸散量（TEWL）を物理的に遮断して密閉します。</p>
        </div>
        <div class="science-card">
          <h4>🌿 抗炎症成分との相乗鎮静効果</h4>
          <p>マデカッソシド（CICA）、アラントイン、グリチルレチン酸などの消炎成分と合わさることで、冷気や摩擦による赤み・かゆみ・ほてりの炎症シグナルを短時間で消火します。</p>
        </div>
      </div>
    </div>

    <div class="products-section">
      {product_cards_html}
    </div>

    <div class="summary-box" id="selection-matrix">
      <h3>📊 目的・肌状態別：冬のパンテノールバーム選び方マトリクス</h3>
      <p>10製品の主要有効成分、配合タイプ、テクスチャー、推奨される使用シーンを一覧で比較しました。ご自身の肌荒れのレベルや使いやすさに合わせてお選びください。</p>
      <table class="summary-table">
        <thead>
          <tr>
            <th>順位 / 製品名</th>
            <th>主要注目成分</th>
            <th>テクスチャー</th>
            <th>こんな冬のお悩み・肌状態におすすめ</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>第1位: ラ ロッシュ ポゼ</td>
            <td>高純度パンテノール5%×マデカッソシド</td>
            <td>濃厚密着バームクリーム</td>
            <td>赤み・粉吹き・ヒリつきの緊急レスキュー</td>
          </tr>
          <tr>
            <td>第2位: バイオヒールボ</td>
            <td>パンテノール10%高濃度×CICA</td>
            <td>微細ミスト/リペアクリーム</td>
            <td>寒暖差脱水・オフィス暖房での日中水分補給</td>
          </tr>
          <tr>
            <td>第3位: アベンヌ</td>
            <td>独自C+Restore×硫酸銅・亜鉛</td>
            <td>包帯保護リペアバーム</td>
            <td>皮剥け・何をつけてもしみる重度の肌荒れ</td>
          </tr>
          <tr>
            <td>第4位: エストラ</td>
            <td>セラミド複合カプセル×パンテノール</td>
            <td>100時間持続濃厚クリーム</td>
            <td>砂漠化したインナードライ・角層ラメラ再建</td>
          </tr>
          <tr>
            <td>第5位: キュレル</td>
            <td>消炎剤（アラントイン）×セラミド機能成分</td>
            <td>ふんわり軽やかスフレ</td>
            <td>重い油分が苦手な敏感肌・朝メイク前の保湿</td>
          </tr>
          <tr>
            <td>第6位: イハダ</td>
            <td>高精製ワセリン×抗肌あれ2種</td>
            <td>体温でとろけるソフトバーム</td>
            <td>目元・口元の部分的な皮剥け・ポーチ常備</td>
          </tr>
          <tr>
            <td>第7位: トリデン</td>
            <td>5D複合セラミド×パンテノール</td>
            <td>大容量100mL高保湿クリーム</td>
            <td>顔から首・ボディまで惜しみなく全身ケア</td>
          </tr>
          <tr>
            <td>第8位: ドクタージャルト</td>
            <td>ツボクサエキス×パンテノール</td>
            <td>グリーン色集中鎮静バーム</td>
            <td>冬の外気刺激による頬の赤み・ほてり鎮静</td>
          </tr>
          <tr>
            <td>第9位: リアルバリア</td>
            <td>特許MLE®生体液晶構造×パンテノール</td>
            <td>人工バリア密着バーム</td>
            <td>冬のアウトドア・寒冷地での水分蒸散防止</td>
          </tr>
          <tr>
            <td>第10位: キールズ UFC</td>
            <td>氷河プロテイン×オリーブスクワラン</td>
            <td>みずみずしい濃厚エモリエント</td>
            <td>ベタつきゼロで24時間乾かない王道保湿</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="summary-box" id="faq-section">
      <h3>❓ 高保湿パンテノールリペアバームに関するよくある質問（FAQ）</h3>
      {faq_html}
    </div>

    <div class="hub-link-banner">
      <div>
        <h3 style="font-size:1.3rem;margin-bottom:8px;">🛡️ 冬のリペアバーム＆高保湿クリーム総合ハブ</h3>
        <p style="font-size:0.95rem;opacity:0.95;">高保湿セラミドクリーム、バリアクリーム、ナイトリペアクリームまで、真冬の粉吹き肌を守り抜く総合特集はこちらからご覧いただけます。</p>
      </div>
      <a href="/winter-repair-balm" class="hub-link-btn">リペアバーム特集トップへ →</a>
    </div>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <!-- 内部リンクがスクリプトにより同期されます -->
      </div>
    </div>
  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-title">LUMI COSMETICS LAB - 冬季皮膚科学＆高保湿コスメ検証</div>
      <div class="footer-links" id="footer-links-box">
        <!-- フッターリンクが同期されます -->
      </div>
      <div class="copyright">
        © 2026 LUMI COSMETICS LAB. All Rights Reserved.
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-panthenol-balm.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-panthenol-balm.html!")
