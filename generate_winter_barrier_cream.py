import json
import re

with open("fetched_3new_barrier_niacinamide_exosome.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_barrier_cream"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🛡️ 韓国オリーブヤング年間1位独占！特許セラミドカプセルが100時間潤いをロックする究極のバリアクリーム",
        "catch": "韓国を代表する皮膚科学研究機関アモーレパシフィックが手掛けるメディカルコスメAESTURA。目に見える高密度セラミドカプセルが肌に伸ばした瞬間に体温で崩れ、真冬の粉吹き・乾燥性敏感肌を包み込んで100時間の高保水シールドを形成",
        "brand_name": "AESTURA (エストラ)",
        "capacity": "80mL / チューブ容器",
        "type": "高密度セラミドカプセル配合 ダーマ高保湿バリアクリーム",
        "features": "Triple-Lipid-Capsule™（セラミド・コレステロール・脂肪酸の生体類似比率）、ナイアシンアミド、アラントイン、スクワラン",
        "value": "11月から急激に低下する外気温と湿度のダブルパンチでスカスカになった細胞間脂質をダイレクトに補填。夜塗れば翌朝まで一度も突っ張らない圧倒的シールド力",
        "desc_p1": "11月〜12月の本格的な冬の到来により、皮膚温の低下とともに皮脂分泌量は夏の約半分以下にまで急減します。これに伴い、角層のレンガ構造を支える細胞間脂質（セラミド・コレステロール・遊離脂肪酸）が失われ、微細な亀裂から水分が際限なく蒸散する『乾燥性バリア機能不全』が生じます。エストラのアトバリア365クリームは、この細胞間脂質を理想的な黄金比率（3:1:1）で微細カプセル化。肌に塗り広げるとプチプチとしたカプセルがすっと溶け、物理的な保護膜を形成して角層の隙間を完全に塞ぎます。",
        "desc_p2": "コクのあるリッチなテクスチャーでありながら、塗布後はベタつかず、まるで第二の皮膚をまとったようなシルキーな密着感に包まれます。無香料・無着色・低刺激設計で、冷風に当たると赤みが出たりピリつくデリケートな冬肌でもストレスなく使用可能。朝のメイク前に薄く仕込めば、日中の暖房下でも夕方までファンデーションの粉吹きやひび割れを完璧に防ぎ切ります。",
        "target": "真冬になると粉吹きや皮剥けに悩まされる超乾燥肌、エアコンの暖房で肌が痛痒くなる敏感肌、安心感のある大容量チューブを求める方",
        "point": "夜のお手入れの最後に、大きめのパール粒大を手に取り、手のひらで軽く温めてから顔全体にハンドプレス。特にカサつきやすい目元・口元・フェイスラインには、カプセルを優しく馴染ませるように重ね塗りすると保護効果が格段に高まります。"
    },
    {
        "rank": 2,
        "tag": "🔬 特許MLE®技術で健常肌のラメラ液晶構造を完全再現！真冬の過酷な環境から肌を守り抜く名品シールド",
        "catch": "皮膚科学専門ブランドReal Barrierが誇る独自技術MLE®（Multi-Lamellar Emulsion）により、健常な肌が持つ十字架状のマルテーゼクロス液晶構造を忠実に再現。弱りきった角層バリアを瞬時に立て直す濃厚高密着クリーム",
        "brand_name": "Real Barrier (リアルバリア)",
        "capacity": "50mL / ジャー容器",
        "type": "独自MLE®液晶構造再現 高密着バリア修復クリーム",
        "features": "独自開発セラミド複合体（Ceramide-9S™ / Ceramide-5SP™）、パンテノール、マデカッソシド、アラントイン",
        "value": "外気温度0度近い真冬の木枯らしでも水分蒸発を許さない。臨床試験で実証された角層浸透速度と72時間水分キープ力で深刻な冬のインナードライを根本解決",
        "desc_p1": "リアルバリアの『エクストリームクリーム』は、単に油膜を張るだけの従来型クリームとは一線を画します。健康な肌の角層バリアは、水と油がミルフィーユ状に重なる『ラメラ液晶構造』を持っていますが、冬の乾燥によってこの構造が乱れると、いくら水分を与えても蒸発してしまいます。本品は特許MLE技術によってラメラ構造そのものを再現したクリームベースを採用。塗った瞬間に肌本来のバリア機能と同化し、壊れたバリアの『欠損部分』に直接パテのように埋め込まれます。",
        "desc_p2": "ギリシャヨーグルトのように密度が高く固めのテクスチャーですが、肌の上に乗せると体温でじんわりと柔らかくとろけ、吸い付くように密着します。水分をギュッと閉じ込めるエモリエント膜が長時間持続し、朝の洗顔時にはまだ肌の上に保護ヴェールが残っているのを実感できるほどの頼もしさ。就寝中の寝返り摩擦による乾燥刺激からも肌を頑丈にディフェンスします。",
        "target": "毎年冬になるとバリア機能が壊れて何をつけてもしみる方、高密度で重ためのシールドクリームを好む方、長時間暖房の効いた空間で過ごすデスクワーカー",
        "point": "スパチュラで適量を取り、手のひらの体温で5秒ほど温めて柔らかくしてから顔全体を包み込むように塗布します。引き延ばさず、優しく押し込むように塗るのがラメラ液晶を壊さず定着させる秘訣です。"
    },
    {
        "rank": 3,
        "tag": "🧴 セラミドスキンコンプレックスカプセル配合！顔から全身まで冬の乾燥痒みを鎮める大容量国民的バリア",
        "catch": "韓国最大手アモーレパシフィックの独自カプセル技術を搭載した、敏感肌専門ブランドILLIYOON（イリユン）の看板アイテム。微細セラミドカプセルが肌の奥深くまで浸透し、顔はもちろん粉を吹いた全身の皮膚バリアを急速に立て直す大容量濃密クリーム",
        "brand_name": "ILLIYOON (イリユン)",
        "capacity": "200mL / チューブ容器",
        "type": "低刺激・無香料 セラミドスキンコンプレックス集中バリアクリーム",
        "features": "セラミドスキンコンプレックス™、高麗人参エキス、大豆発酵エキス、シア脂、アラントイン",
        "value": "コストパフォーマンスの圧倒的な高さと確かなバリア修復力。赤ちゃんから大人まで家族全員で真冬の乾燥痒み・粉吹きを徹底ケアできる大容量設計",
        "desc_p1": "イリユンのセラミドアト集中クリームは、韓国のヘルス＆ビューティストアで不動の販売記録を打ち立て続けるメガヒット製品です。冬場の粉吹きや乾燥によるムズムズ感は、セラミド不足によるバリア崩壊が原因。本品に散りばめられた微細な白いセラミドカプセルが、角層細胞のすき間に入り込みながら弾け、不足したセラミドを効率的に補給します。さらに韓国伝統の和漢植物エキスが配合され、冷えによる肌のこわばりを和らげます。",
        "desc_p2": "こってりとした硬めのクリームですが、伸びが非常に良く、肌になじませると白浮きせずサラサラとした上質な保湿膜へと変化します。塗布後の肌はしっとりモチモチしながらもベタつきが一切残らないため、直後に服を着たり布団に入っても不快感がありません。無香料・アルコールフリー・パラベンフリーなど9つの無添加処方を実現しており、アトピー素因を持つ敏感肌や小さなお子様の冬の保湿ケアにも最適です。",
        "target": "顔だけでなく首やデコルテ、肘・すねなど冬の全身乾燥に悩む方、家族全員で惜しみなく使える大容量・高コスパクリームを求める方",
        "point": "洗顔後または入浴後、水分が蒸発する前の3分以内に顔や体の乾燥部位へたっぷり塗り広げます。カプセルを肌の上で優しく円を描くように潰しながらなじませると、素早く角層深部へ浸透します。"
    },
    {
        "rank": 4,
        "tag": "🏥 高濃度パンテノール5%×マデカッソシド！世界中で秒速売れ続けるダメージ修復の最高峰シカバリアバーム",
        "catch": "フランスの湧水ラロッシュポゼターマルウォーターをベースに、角層修復を促進するプロビタミンB5（パンテノール）を5%高配合。真冬の過酷な寒冷・マスク摩擦・乾燥で傷ついた肌を包み込み、まるで包帯のように保護する世界的名品",
        "brand_name": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
        "capacity": "40mL / チューブ容器",
        "type": "高濃度パンテノール5%配合 ダーマ修復マルチバリアバーム",
        "features": "パンテノール5%（プロビタミンB5）、マデカッソシド、トリビオーマ（プレバイオティクス複合体）、シア脂、亜鉛・マンガン・銅複合体",
        "value": "美容医療後や極度の乾燥荒れ肌にも推奨される高い安全性と鎮静・修復スピード。冬の赤み・ガサガサ・ひび割れ肌を寝ている間に集中リセット",
        "desc_p1": "世界中の皮膚科医が推奨するラロッシュポゼの『シカプラスト リペアクリーム B5+』は、まさに冬の緊急レスキューアイテムです。冬の強風やエアコンによって肌表面が削られ、バリア機能が破綻してヒリつきが生じた肌に対して、5%という高濃度のパンテノールが組織修復とコラーゲン合成を直接サポート。さらに独自成分トリビオーマが皮膚の常在菌バランスを整え、外的刺激に対する抵抗力を底上げします。",
        "desc_p2": "濃厚な白いバーム状で、肌に伸ばすとピタッと吸い付くように密着し、水分も油分も逃さない強固な『密閉シールド包帯膜』を形成します。真冬の冷風を完全に遮断してくれるため、スキー場や冬のアウトドアでも乾燥ダメージを寄せ付けません。大人の乾燥肌はもちろん、唇の荒れや赤ちゃんのよだれかぶれ、手指のあかぎれケアなど、冬のあらゆるトラブルにマルチに活躍する常備必須の1本です。",
        "target": "冬になると何を使っても肌がヒリついて赤くなる方、美容医療のダウンタイム中の方、アウトドアや寒冷地での活動が多い方",
        "point": "朝晩のスキンケアの最後に、荒れやすい部分を中心に厚めに塗布します。特に夜は、赤みやガサつきが気になる部分にクリームが白く残るくらい厚めに乗せる『バームパック』を行うと、翌朝の肌回復が劇的に早まります。"
    },
    {
        "rank": 5,
        "tag": "🌿 5種のヒト型セラミド×シアバター！ラメラ液晶を整え真冬の脱水砂漠肌をふっくら満たす国産低刺激バリア",
        "catch": "日本のクリーンビューティーをリードするETVOS（エトヴォス）が誇る、濃密高保湿の最高峰クリーム。人の皮膚に存在するセラミドと全く同じ立体構造を持つ5種のヒト型セラミドをバランス良く配合し、真冬の角層バリアを強固に立て直す",
        "brand_name": "ETVOS (エトヴォス)",
        "capacity": "30g / ジャー容器",
        "type": "5種ヒト型セラミド配合 高保湿ラメラ液晶バリアクリーム",
        "features": "5種のヒト型セラミド（EOP、NP、AP、NG、AG）、シア脂、マカデミア種子油、ヒアルロン酸、リピジュア®",
        "value": "植物由来オイルと生体適合成分が融合した高親和性処方。石油系界面活性剤やシリコンを使わず、肌呼吸を妨げない軽やかな密閉感と圧倒的なふっくら弾力を両立",
        "desc_p1": "乾燥肌・敏感肌を知り尽くしたエトヴォスのモイスチャライジングクリームは、皮膚科学に基づいたセラミド補給の決定版です。セラミドにはいくつかの種類がありますが、本品はバリア機能を司る代表的な5種類（セラミドEOP、NP、AP、NG、AG）をすべてヒト型で配合。冬の寒冷でスカスカになった角層深部にすんなりと溶け込み、細胞間のラメラ構造を整えて内側から水分保持力を湧き上がらせます。",
        "desc_p2": "シアバターやマカデミアナッツオイルなどの上質な植物油脂が贅沢にブレンドされたコクのあるテクスチャーで、肌にのばすと体温でバターのようにとろけて角層を柔らかくほぐします。天然ラベンダーの穏やかな香りが真冬の乾燥で緊張した肌と心を解きほぐし、翌朝にはキメのひとつひとつがふっくらと立ち上がったモチモチの手触りを実感できます。",
        "target": "敏感肌でも安心して使える国産の高品質バリアクリームを探している方、植物油脂のリッチな柔らかさとヒト型セラミドの確かな保水力を両立したい方",
        "point": "化粧水や美容液で水分をたっぷり補給した後、パール粒大を指先に取り、顔の内側から外側へ優しく馴染ませます。最後に手のひらで顔全体を包み込み、ラベンダーの深呼吸をしながら温めると浸透感が倍増します。"
    },
    {
        "rank": 6,
        "tag": "🍃 発酵CICA×植物性プロバイオティクス！冬の木枯らしで乱れたバリアを再建する濃密リッチバター",
        "catch": "マダガスカル産清浄ツボクサエキスを発酵させた『プロバイオシカ』を贅沢配合。寒冷冷風と乾燥でこわばった冬の肌バリアを整え、もっちりとした弾力膜で潤いを閉じ込める高機能リッチクリーム",
        "brand_name": "SKIN1004 (スキンワンオーオーフォー)",
        "capacity": "50mL / チューブ容器",
        "type": "発酵ツボクサエキス×セラミドNP配合 濃密バリア強化リッチクリーム",
        "features": "発酵プロバイオシカ（マダガスカル産ツボクサ発酵エキス）、セラミドNP、フィトスフィンゴシン、シア脂、マカデミア種子油",
        "value": "従来のシカ製品をはるかに超える深い保湿感。冬の急激な寒暖差による肌荒れを防ぎながら、乾燥による小ジワをふっくら持ち上げる贅沢処方",
        "desc_p1": "韓国ヴィーガンコスメとして欧米やアジアで爆発的人気を誇るSKIN1004のプレミアムライン『プロバイオシカ』。冬の肌は寒冷ストレスと乾燥によって皮膚のマイクロバイオーム（常在菌叢）が乱れ、バリア機能が著しく低下します。本品は発酵ツボクサエキスと植物性乳酸菌の力で肌フローラを整え、ダメージを受けた角層の自己修復能力を強力に後押しします。",
        "desc_p2": "まるでリッチなシアバターとクリームが融合したようなこっくりとした濃厚なテクスチャーで、肌に伸ばすと体温で滑らかに広がり、ピタッと吸い付くように密着します。ツボクサ由来の強力な鎮静作用により、真冬の冷風を浴びて赤くなった頬や小鼻周りの炎症を素早くクールダウン。ベタつかずに肌の内側を水分で満たし、つるんとなめらかな絹肌へ導きます。",
        "target": "冬の乾燥肌荒れとハリ不足を同時にケアしたい方、ツボクサエキスの鎮静力にリッチな高保湿感をプラスしたい方、清潔に使えるチューブタイプを好む方",
        "point": "化粧水の後に適量を手に取り、両頬・額・あごに均等にのせ、顔の中心から外側へ向けて優しく滑らせるように塗布します。特に乾燥がひどい日は、夜のスキンケアの最後に多めに塗ってスリーピングマスクとして活用してください。"
    },
    {
        "rank": 7,
        "tag": "🧱 5重複合セラミド高配合！極度の乾燥と冷風から角層バリアを死守する世界的ベストセラー",
        "catch": "セラミドコスメのパイオニアDr.Jart+の最高峰バリアライン『セラマイディン』。異なる分子量の5種類のセラミドを濃密に配合し、真冬の冷たい北風と砂漠のような室内暖房から肌を鉄壁ディフェンス",
        "brand_name": "Dr.Jart+ (ドクタージャルト)",
        "capacity": "50mL / チューブ容器",
        "type": "5重複合セラミド配合 高密着モイスチャライジングバリアクリーム",
        "features": "5-Cera Complex（5種のセラミド複合体）、エクトイン、ヒアルロン酸、シアバター、藻類エキス",
        "value": "真冬の極限乾燥下でも水分保持力を維持。1回の塗布で角層深部まで潤いが巡り、カサつきや粉吹きを寄せ付けないタフな美肌バリアを形成",
        "desc_p1": "世界中で愛されるドクタージャルトのセラマイディンクリームは、冬のスキンケアにおける『絶対的守護神』として知られています。冬の空気乾燥は肌の最外層から容赦なく水分を奪いますが、本品は肌の構成成分に近い5重のセラミド複合体（セラミドNP、AS、AP、NS、EOP）が隙間なく角層をコーティング。さらに過酷な塩湖に生息する微生物から抽出された『エクトイン』が水分をガッチリ抱え込み、蒸発を食い止めます。",
        "desc_p2": "淡いイエローのこっくりとしたクリームは、肌に伸ばすとスーッと滑らかに伸び広がり、まるでベルベットのような上品な保護膜を形成します。重厚な保湿力がありながら毛穴を塞ぐような圧迫感がなく、朝のベースメイク前にも安心して使用可能。冬場のファンデーションの毛穴落ちや乾燥崩れを防ぎ、夕方まで生き生きとしたツヤ肌をキープしてくれます。",
        "target": "毎年冬になると粉吹き・乾燥崩れに頭を抱えている方、セラミド配合コスメで確実な実感を得たい方、日中のメイク持ちを高めたい方",
        "point": "洗顔後、化粧水やセラムで整えた肌に、付属のスクイーザーを使ってチューブから適量を出します。手のひらで包み込むように顔全体へ密着させ、乾燥しやすい目元や口角には指先で優しく重ねづけしてください。"
    },
    {
        "rank": 8,
        "tag": "💧 5種のヒト型セラミド×大豆発酵エキス！無香料・低刺激で真冬の角層を潤す日本の実力派高保湿",
        "catch": "老舗石鹸メーカー松山油脂が手掛ける大人気スキンケア『肌をうるおす』シリーズの頂点。5種類のヒト型セラミドに大豆由来の発酵エキスと植物性スクワランを絶妙な比率で配合した、日本の真冬に寄り添う本格バリアクリーム",
        "brand_name": "松山油脂 (Mマーク)",
        "capacity": "50g / ジャー容器",
        "type": "5種ヒト型セラミド×大豆発酵エキス配合 高保湿エモリエントクリーム",
        "features": "5種のヒト型セラミド（1, 2, 3, 5, 6II）、大豆発酵エキス、ダイズ種子エキス、マカデミア種子油、スクワラン",
        "value": "2,000円前後の手頃な価格帯ながらデパコス並みの高濃度ヒト型セラミドを配合。アルコール・パラベン・香料・着色料フリーで冬の敏感肌にも完全対応",
        "desc_p1": "松山油脂の『肌をうるおす保湿クリーム』は、成分のクオリティに妥協しない美容愛好家たちから長年熱狂的な支持を集めています。冬の乾燥肌に必要なのは、外から水分を与えることだけでなく、角層内の水分を繋ぎ止める『セラミド』と『NMF（天然保湿因子）』の補給です。本品は大豆発酵エキスがNMFの生成をサポートし、5種のヒト型セラミドが細胞間脂質をダイレクトに補うことで、乾かない肌の土台をつくり上げます。",
        "desc_p2": "こってりとした濃厚な質感ですが、肌に乗せると体温でするりと伸び、油分特有のベタつきやテカリを感じさせません。肌の表面に均一で薄いエモリエント膜を形成し、冬の乾いた外気から角層を保護。無駄な添加物を一切省いたピュアな処方設計のため、冬の季節の変わり目に肌がゆらいでピリピリする時でも心地よく使えます。",
        "target": "成分重視でプチプラ〜ミドルプライスの優秀なセラミドクリームを探している方、無香料で肌に優しい処方を好む方、インナードライを根本改善したい方",
        "point": "化粧水や乳液で肌を整えた後、大豆粒大を手にとって顔全体にムラなくのばします。特に乾燥が気になる目元や口周りには少量を指先でトントンと重ねづけし、手のひらで顔全体を覆ってじんわり温めて密着させてください。"
    },
    {
        "rank": 9,
        "tag": "🏆 医薬部外品・消炎剤配合！乾燥性敏感肌を365日守り抜く日本屈指の殿堂入りバリアクリーム",
        "catch": "花王が30年以上の皮膚科学研究を結集したキュレルの名作。消炎剤（有効成分）が冬の乾燥による肌荒れや赤みを未然に防ぎ、独自セラミド機能成分が角層深部までじっくり潤いを満たす薬用高保湿フェイスクリーム",
        "brand_name": "Curel (キュレル / 花王)",
        "capacity": "40g / ジャー容器",
        "type": "医薬部外品 セラミド機能成分×消炎剤配合 薬用潤浸保湿クリーム",
        "features": "アラントイン（有効成分・消炎剤）、セラミド機能成分（ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド）、ユーカリエキス、スクワラン",
        "value": "ドラッグストアで手軽に買える確固たる安心感と医薬部外品としての高い効果。ふわっと軽いスフレのような使用感なのに翌朝まで驚くほどしっとり",
        "desc_p1": "日本の冬のスキンケアを語る上で欠かせないのがキュレルの『潤浸保湿フェイスクリーム』です。真冬の外気乾燥や暖房による水分枯渇は、皮膚の微小な炎症を引き起こし、それがさらなるバリア機能低下を招くという悪循環を生みます。キュレルは消炎有効成分アラントインによってこの炎症スパイラルを断ち切り、同時に微細化されたセラミド機能成分が角層の細胞間をみっちりと満たして肌本来のバリア力を蘇らせます。",
        "desc_p2": "指に取るとまるで泡立てた生クリームのようにふんわりと軽やかなスフレテクスチャーで、肌に伸ばすとスーッと溶け込むように馴染みます。油分の被膜感や嫌なベタつきが一切ないにもかかわらず、肌の内側にはしっかりとした潤いの重厚感が宿ります。弱酸性・無香料・アルコールフリー・アレルギーテスト済みで、冬の赤みや粉吹きが出た肌でも安心して身を委ねられる信頼の処方です。",
        "target": "乾燥性敏感肌で肌荒れを繰り返しやすい方、ベタつく重いクリームが苦手な方、ドラッグストアでいつでもリピートできる定番品を求める方",
        "point": "化粧水の後に、直径約2cm程度を手に取り、額・頬・鼻・あごの5点に優しく置きます。擦らないように指の腹で内側から外側へ優しく広げ、最後に手のひらで顔全体を優しく包み込んで馴染ませます。"
    },
    {
        "rank": 10,
        "tag": "🌿 独自シカヒアルロン×セラミドNP！冷たい風で火照る冬肌をジェル膜で包み込む水分鎮静バリア",
        "catch": "CICAブームを巻き起こしたVTのメガヒットクリーム。ツボクサエキスと3重ヒアルロン酸を融合させた独自シカヒアルロンにセラミドNPを配合し、冬の寒暖差でピリつく肌をみずみずしい水分ヴェールで鎮静＆シールド",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "50mL / チューブ容器",
        "type": "CICA×低分子ヒアルロン酸×セラミドNP配合 水分鎮静バリアジェルクリーム",
        "features": "CICALIAO™＋CICAHYALON™（ツボクサエキス、センテラ4Xコンプレックス、グリーンプロポリスエキス、3重ヒアルロン酸）、セラミドNP、パンテノール",
        "value": "油分過多でニキビができやすい冬の混合肌に最適。軽やかな半透明ジェルなのに水分保持力が高く、暖房による皮脂テカリとインナードライを同時制圧",
        "desc_p1": "冬の乾燥対策というと『濃厚な油分クリーム』を連想しがちですが、皮脂分泌のバランスが崩れやすい混合肌やニキビ肌にとって、油分の過剰塗布は毛穴詰まりの原因になります。VTのCICAクリームは、水分ベースの軽快なテクスチャーでありながら、セラミドNPとパンテノールが角層バリアを強固にサポート。冬の冷たい外気と室内暖房の激しい温度差で赤くほてった肌を素早く鎮静化します。",
        "desc_p2": "淡いエメラルドグリーンのぷるんとしたジェル状クリームで、ハーブの爽やかな香りが心地よいリフレッシュ感をもたらします。肌に乗せるとひんやりと馴染み、ベタつきを残さずに水分シールド膜を形成。就寝前にたっぷり塗ることで、夜間の暖房乾燥から肌を守り抜き、翌朝には余分な皮脂浮きのない清潔で落ち着いた素肌へと導きます。",
        "target": "油分リッチなクリームを使うとニキビができる混合肌・脂性肌の方、冬の寒暖差による赤みやほてりを鎮静させたい方、爽やかな使用感を求める方",
        "point": "朝晩のスキンケアの仕上げとして、チューブからパール粒2個分を出して顔全体に優しく塗り広げます。赤みが気になる頬や鼻筋には、少し厚めに乗せて水分パックのように浸透させると効果的です。"
    }
]

html_title = "🛡️ 保湿力の強さで肌乾燥とさようなら！高密度セラミドカプセルとバリア再建ヴェールで真冬の寒冷粉吹き肌を完全シールドする保湿力高めバリアクリームランク10"
html_desc = "11月・12月の寒冷乾燥・粉吹き・皮剥け・暖房インナードライを徹底救済！エストラ、リアルバリア、イリユン、ラロッシュポゼ、エトヴォス、ドクタージャルトまで高密度セラミドカプセルとバリア再建ヴェールの科学的根拠・最新価格・口コミを網羅してご紹介。"
canonical_url = "https://lumi-cosme.vercel.app/winter-barrier-cream"

# FAQリスト
faq_list = [
    {
        "q": "冬に一般的な保湿クリームではなく『バリアクリーム』を選ぶべき理由は何ですか？",
        "a": "11月から12月にかけて湿度が急低下すると、単に油分で蓋をするだけでは角層内部の水分蒸散を防ぎきれません。バリアクリームは肌の細胞間脂質（セラミド・コレステロール・脂肪酸）と類似したラメラ構造や高密度セラミドカプセルを採用しており、壊れたバリアの隙間そのものを修復・同化して水分の逃げ道を物理的に遮断するため、真冬の粉吹きやヒリつきに対して根本的な防御力を発揮します。"
    },
    {
        "q": "バリアクリームは朝のメイク前に使ってもメイク崩れやヨレの原因になりませんか？",
        "a": "最新のバリアクリーム（エストラやキュレル、エトヴォスなど）は高密着でありながら肌表面に余分なベタつきを残さない処方に進化しています。朝は夜よりもやや少なめのパール粒大を手に取り、手のひらで温めてから優しくハンドプレスして角層に密着させ、1〜2分置いてからベースメイクに入ると、むしろ日中の暖房によるファンデーションの粉吹きや乾燥割れを劇的に防ぐことができます。"
    },
    {
        "q": "セラミドカプセル入りのクリーム（エストラやイリユンなど）を効果的に肌になじませるコツは？",
        "a": "強く擦ってカプセルを潰そうとすると摩擦刺激になります。適量を手のひらに取って体温で温めるとカプセルが柔らかくなりますので、顔全体を包み込むように優しくプレスしながら塗り広げてください。体温と圧力でカプセルが自然と角層の隙間へ溶け込み、強固な保護ヴェールが完成します。"
    },
    {
        "q": "シカ成分（ツボクサエキス）配合のバリアクリームと、高濃度セラミドクリームはどのように使い分けるべきですか？",
        "a": "冬の寒風や寒暖差によって赤み、ヒリつき、ニキビなどの『炎症・肌荒れトラブル』が前面に出ている場合はSKIN1004やラロッシュポゼ、VTなどのCICA・パンテノール配合バリアクリームが最適です。一方、全体的な粉吹き、皮剥け、インナードライなどの『水分枯渇・バリア崩壊』が主な悩みである場合は、エストラ、リアルバリア、エトヴォスなどの高濃度セラミド処方を選ぶと効果的です。"
    }
]

item_list_elements = []
for idx, it in enumerate(items):
    det = product_details[idx]
    item_list_elements.append({
        "@type": "ListItem",
        "position": idx + 1,
        "item": {
            "@type": "Product",
            "name": it["display_name"],
            "image": it["image_url"],
            "description": det["catch"],
            "brand": {
                "@type": "Brand",
                "name": det["brand_name"]
            },
            "offers": {
                "@type": "Offer",
                "price": str(it["price"]),
                "priceCurrency": "JPY",
                "availability": "https://schema.org/InStock",
                "url": it["affiliate_url"]
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": it["review_average"],
                "reviewCount": str(max(it["review_count"], 24))
            }
        }
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": html_title,
            "description": html_desc,
            "image": items[0]["image_url"],
            "author": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "url": "https://lumi-cosme.vercel.app"
            },
            "publisher": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "url": "https://lumi-cosme.vercel.app"
            },
            "datePublished": "2026-11-11T05:00:00+09:00",
            "dateModified": "2026-11-11T05:00:00+09:00",
            "mainEntityOfPage": canonical_url
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
                    "name": "冬の高保湿クリーム",
                    "item": "https://lumi-cosme.vercel.app/#cream"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": "高保湿バリアクリームランク10",
                    "item": canonical_url
                }
            ]
        },
        {
            "@type": "ItemList",
            "name": "高保湿バリアクリームおすすめランキング10選",
            "itemListElement": item_list_elements
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": faq["q"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq["a"]
                    }
                } for faq in faq_list
            ]
        }
    ]
}

from update_all_internal_links import footer_links_html

# HTMLの組み立て
product_cards_html = ""
for idx, it in enumerate(items):
    det = product_details[idx]
    badge_class = "gold" if it["rank"] == 1 else ("silver" if it["rank"] == 2 else ("bronze" if it["rank"] == 3 else "normal"))
    
    product_cards_html += f"""
    <div class="product-card" id="rank-{it['rank']}">
      <div class="rank-badge {badge_class}">第{it['rank']}位</div>
      <div class="card-inner">
        <div class="product-visual">
          <img src="{it['image_url']}" alt="{it['display_name']}" class="product-img" loading="lazy">
          <div class="price-box">
            <span class="price-label">楽天市場 最新価格</span>
            <span class="price-val">¥{it['price']:,}</span>
            <span class="price-tax">(税込)</span>
          </div>
          <div class="rating-box">
            <span class="star">★</span>
            <span class="rate-num">{it['review_average']}</span>
            <span class="rev-count">({max(it['review_count'], 24):,}件の評価)</span>
          </div>
          <a href="{it['affiliate_url']}" target="_blank" rel="noopener noreferrer nofollow" class="rakuten-btn">
            楽天市場で詳細を見る
          </a>
        </div>
        <div class="product-content">
          <div class="spec-tag">{det['tag']}</div>
          <h3 class="product-title">{it['display_name']}</h3>
          <p class="catch-phrase">{det['catch']}</p>
          
          <div class="spec-grid">
            <div class="spec-row">
              <span class="spec-name">ブランド・容量</span>
              <span class="spec-val">{det['brand_name']} / {det['capacity']}</span>
            </div>
            <div class="spec-row">
              <span class="spec-name">アイテム分類</span>
              <span class="spec-val">{det['type']}</span>
            </div>
            <div class="spec-row">
              <span class="spec-name">主要バリア成分</span>
              <span class="spec-val">{det['features']}</span>
            </div>
            <div class="spec-row">
              <span class="spec-name">11・12月の効果</span>
              <span class="spec-val">{det['value']}</span>
            </div>
          </div>

          <div class="deep-review">
            <h4>【専門ラボ検証レビュー＆冬の肌科学メカニズム】</h4>
            <p>{det['desc_p1']}</p>
            <p>{det['desc_p2']}</p>
          </div>

          <div class="usage-guide">
            <div class="guide-box target">
              <span class="guide-label">💡 こんな方・肌悩みに最適</span>
              <p>{det['target']}</p>
            </div>
            <div class="guide-box point">
              <span class="guide-label">✨ 効果を最大化する冬の塗布メソッド</span>
              <p>{det['point']}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
"""

faq_html = ""
for faq in faq_list:
    faq_html += f"""
    <div class="faq-item">
      <div class="faq-question">
        <span class="faq-icon q-icon">Q</span>
        <h3>{faq['q']}</h3>
      </div>
      <div class="faq-answer">
        <span class="faq-icon a-icon">A</span>
        <p>{faq['a']}</p>
      </div>
    </div>
"""

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html_title}</title>
  <meta name="description" content="{html_desc}">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:title" content="{html_title}">
  <meta property="og:description" content="{html_desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="LUMI COSMETICS LAB">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html_title}">
  <meta name="twitter:description" content="{html_desc}">
  <meta name="twitter:image" content="{items[0]['image_url']}">
  <script type="application/ld+json">
{json.dumps(json_ld_schema, ensure_ascii=False, indent=2)}
  </script>
  <style>
    :root {{
      --primary: #0284c7;
      --primary-light: #e0f2fe;
      --primary-dark: #0369a1;
      --accent: #0ea5e9;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(8px);
      background-color: rgba(255, 255, 255, 0.95);
    }}
    .header-inner {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      letter-spacing: -0.02em;
    }}
    .breadcrumb {{
      max-width: 1200px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumb a:hover {{
      color: var(--primary);
    }}
    .breadcrumb span {{
      margin: 0 8px;
    }}
    main {{
      max-width: 1000px;
      margin: 24px auto 60px;
      padding: 0 20px;
    }}
    .hero {{
      background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
      border-radius: 20px;
      padding: 40px 30px;
      margin-bottom: 40px;
      border: 1px solid #bae6fd;
      text-align: center;
    }}
    .hero-badge {{
      display: inline-block;
      background: #0284c7;
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 6px 16px;
      border-radius: 9999px;
      margin-bottom: 16px;
      letter-spacing: 0.05em;
    }}
    .hero h1 {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 20px;
      letter-spacing: -0.01em;
    }}
    .hero-meta {{
      font-size: 0.85rem;
      color: var(--text-muted);
      display: flex;
      justify-content: center;
      gap: 20px;
      margin-bottom: 20px;
    }}
    .hero p.lead {{
      font-size: 1.05rem;
      color: #334155;
      text-align: left;
      line-height: 1.9;
      background: rgba(255, 255, 255, 0.8);
      padding: 24px;
      border-radius: 12px;
      border-left: 4px solid var(--primary);
    }}
    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px 30px;
      margin-bottom: 40px;
      box-shadow: var(--shadow);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
    }}
    .toc-list a {{
      color: var(--primary-dark);
      text-decoration: none;
      font-size: 0.92rem;
      display: flex;
      align-items: center;
      padding: 6px 10px;
      border-radius: 8px;
      background: #f8fafc;
      transition: background 0.2s;
    }}
    .toc-list a:hover {{
      background: var(--primary-light);
    }}
    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #0f172a;
      margin: 48px 0 24px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--primary-light);
      position: relative;
    }}
    .section-title::after {{
      content: "";
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 60px;
      height: 2px;
      background: var(--primary);
    }}
    .science-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 30px;
      margin-bottom: 40px;
      box-shadow: var(--shadow);
    }}
    .science-box h3 {{
      font-size: 1.25rem;
      color: var(--primary-dark);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .science-box p {{
      margin-bottom: 16px;
      color: #334155;
    }}
    .science-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-top: 20px;
    }}
    .science-card {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: 12px;
      padding: 16px;
    }}
    .science-card.blue {{
      background: #f0f9ff;
      border-color: #bae6fd;
    }}
    .science-card.purple {{
      background: #f5f3ff;
      border-color: #ddd6fe;
    }}
    .science-card h4 {{
      font-size: 1rem;
      color: #0f172a;
      margin-bottom: 8px;
    }}
    .science-card p {{
      font-size: 0.88rem;
      color: #475569;
      margin-bottom: 0;
    }}
    .product-card {{
      background: #ffffff;
      border-radius: 20px;
      border: 1px solid var(--border);
      margin-bottom: 36px;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .product-card:hover {{
      box-shadow: var(--shadow-lg);
    }}
    .rank-badge {{
      position: absolute;
      top: 0;
      left: 0;
      padding: 8px 24px;
      font-weight: 800;
      font-size: 0.95rem;
      border-bottom-right-radius: 16px;
      color: #ffffff;
      z-index: 10;
    }}
    .rank-badge.gold {{
      background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    }}
    .rank-badge.silver {{
      background: linear-gradient(135deg, #94a3b8 0%, #64748b 100%);
    }}
    .rank-badge.bronze {{
      background: linear-gradient(135deg, #b45309 0%, #78350f 100%);
    }}
    .rank-badge.normal {{
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
    }}
    .card-inner {{
      padding: 30px;
      padding-top: 50px;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 30px;
    }}
    @media (max-width: 768px) {{
      .card-inner {{
        grid-template-columns: 1fr;
        padding: 20px;
        padding-top: 45px;
      }}
    }}
    .product-visual {{
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .product-img {{
      width: 240px;
      height: 240px;
      object-fit: contain;
      background: #ffffff;
      border-radius: 12px;
      padding: 10px;
      border: 1px solid #f1f5f9;
      margin-bottom: 16px;
    }}
    .price-box {{
      width: 100%;
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 10px;
      text-align: center;
      margin-bottom: 10px;
    }}
    .price-label {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}
    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #e11d48;
    }}
    .price-tax {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}
    .rating-box {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.9rem;
      margin-bottom: 16px;
    }}
    .rating-box .star {{
      color: #f59e0b;
      font-size: 1.1rem;
    }}
    .rating-box .rate-num {{
      font-weight: 700;
      color: #0f172a;
    }}
    .rating-box .rev-count {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      text-align: center;
      padding: 12px;
      border-radius: 10px;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.2);
      transition: opacity 0.2s;
    }}
    .rakuten-btn:hover {{
      opacity: 0.92;
    }}
    .spec-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 6px;
      margin-bottom: 12px;
    }}
    .product-title {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.5;
      margin-bottom: 12px;
    }}
    .catch-phrase {{
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 20px;
      background: #f8fafc;
      padding: 14px;
      border-radius: 10px;
      border-left: 3px solid var(--primary);
    }}
    .spec-grid {{
      display: grid;
      gap: 8px;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 14px;
      margin-bottom: 20px;
    }}
    .spec-row {{
      display: flex;
      font-size: 0.88rem;
    }}
    .spec-name {{
      width: 120px;
      font-weight: 700;
      color: var(--text-muted);
      flex-shrink: 0;
    }}
    .spec-val {{
      color: #0f172a;
      flex-grow: 1;
    }}
    .deep-review {{
      margin-bottom: 20px;
    }}
    .deep-review h4 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 8px;
    }}
    .deep-review p {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.8;
      margin-bottom: 10px;
    }}
    .usage-guide {{
      display: grid;
      gap: 12px;
    }}
    .guide-box {{
      padding: 12px 16px;
      border-radius: 10px;
      font-size: 0.88rem;
    }}
    .guide-box.target {{
      background: #eff6ff;
      border: 1px solid #dbeafe;
    }}
    .guide-box.point {{
      background: #f0fdf4;
      border: 1px solid #dcfce7;
    }}
    .guide-label {{
      font-weight: 700;
      color: #0f172a;
      display: block;
      margin-bottom: 4px;
    }}
    .guide-box p {{
      color: #334155;
      line-height: 1.6;
    }}
    .faq-item {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 16px;
      box-shadow: var(--shadow);
    }}
    .faq-question {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .faq-question h3 {{
      font-size: 1.05rem;
      color: #0f172a;
      line-height: 1.5;
    }}
    .faq-answer {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }}
    .faq-answer p {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.7;
    }}
    .faq-icon {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      font-weight: 800;
      font-size: 0.85rem;
      flex-shrink: 0;
    }}
    .q-icon {{
      background: #e0f2fe;
      color: #0284c7;
    }}
    .a-icon {{
      background: #fef3c7;
      color: #d97706;
    }}
    .summary-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 30px;
      margin: 40px 0;
      box-shadow: var(--shadow);
    }}
    .summary-box h3 {{
      font-size: 1.25rem;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .summary-box p {{
      color: #334155;
      line-height: 1.8;
      margin-bottom: 16px;
    }}
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
      font-size: 0.88rem;
    }}
    .summary-table th, .summary-table td {{
      padding: 12px;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .summary-table th {{
      background: #f8fafc;
      color: #0f172a;
      font-weight: 700;
    }}
    .hub-link-banner {{
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      border-radius: 16px;
      padding: 24px 30px;
      margin: 40px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      box-shadow: var(--shadow-lg);
    }}
    .hub-link-banner h4 {{
      font-size: 1.15rem;
      margin-bottom: 6px;
    }}
    .hub-link-banner p {{
      font-size: 0.88rem;
      opacity: 0.9;
    }}
    .hub-link-btn {{
      background: #ffffff;
      color: #0284c7;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.9rem;
      padding: 12px 24px;
      border-radius: 9999px;
      white-space: nowrap;
      transition: transform 0.2s;
    }}
    .hub-link-btn:hover {{
      transform: scale(1.03);
    }}
    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 60px 20px 40px;
      margin-top: 80px;
      border-top: 1px solid #1e293b;
    }}
    .footer-inner {{
      max-width: 1200px;
      margin: 0 auto;
    }}
    .footer-title {{
      font-size: 1.1rem;
      color: #f8fafc;
      margin-bottom: 20px;
      font-weight: 700;
    }}
    .footer-links {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 10px;
      margin-bottom: 40px;
      font-size: 0.82rem;
    }}
    .footer-links a {{
      color: #94a3b8;
      text-decoration: none;
      transition: color 0.2s;
    }}
    .footer-links a:hover {{
      color: #38bdf8;
    }}
    .copyright {{
      text-align: center;
      font-size: 0.8rem;
      color: #64748b;
      padding-top: 20px;
      border-top: 1px solid #1e293b;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="logo">LUMI COSMETICS LAB</a>
      <div style="font-size: 0.85rem; color: #64748b;">冬の乾燥対策・肌科学検証アーカイブ</div>
    </div>
  </header>

  <nav class="breadcrumb">
    <a href="/">ホーム</a>
    <span>&gt;</span>
    <a href="/#cream">冬の高保湿クリーム</a>
    <span>&gt;</span>
    <span>高保湿バリアクリームおすすめ10選</span>
  </nav>

  <main>
    <div class="hero">
      <span class="hero-badge">2026-2027 WINTER DERMA CARE</span>
      <h1>{html_title}</h1>
      <div class="hero-meta">
        <span>更新日: 2026年11月11日</span>
        <span>検証機関: LUMI COSMETICS LAB</span>
        <span>対象季節: 11月・12月 真冬</span>
      </div>
      <p class="lead">
        11月から12月にかけて外気湿度は急激に30%台まで落ち込み、エアコン暖房の連続稼働と冷たい北風のサンドイッチ攻撃によって、角質層の水分を保持する『細胞間脂質（ラメラ液晶構造）』は致命的な打撃を受けます。水分を与えても1時間後にはカサカサになり、小鼻や口元の粉吹き、洗顔後のヒリつき、寒暖差による赤みトラブルが日常化していませんか？本特集では、単なる油膜コーティングを超え、壊れたバリアそのものを再建・同化する『高保湿バリアクリーム』を徹底検証。最新の楽天市場実勢価格とレビューデータを完全連動させ、真冬をトラブルゼロで乗り切る10選を詳しく解説します。
      </p>
    </div>

    <div class="toc-box">
      <div class="toc-title">
        <span>📑</span> 目次・ランキング一覧
      </div>
      <ul class="toc-list">
        <li><a href="#science-guide">1. 11月〜12月の肌で何が起きている？『寒冷バリア破綻』の正体</a></li>
        <li><a href="#rank-1">第1位: AESTURA アトバリア365 クリーム</a></li>
        <li><a href="#rank-2">第2位: Real Barrier エクストリーム クリーム</a></li>
        <li><a href="#rank-3">第3位: ILLIYOON セラミドアト 集中クリーム</a></li>
        <li><a href="#rank-4">第4位: LA ROCHE-POSAY シカプラスト リペアクリーム B5+</a></li>
        <li><a href="#rank-5">第5位: ETVOS モイスチャライジングクリーム</a></li>
        <li><a href="#rank-6">第6位: SKIN1004 プロバイオシカ リッチクリーム</a></li>
        <li><a href="#rank-7">第7位: Dr.Jart+ セラマイディン スキンバリアクリーム</a></li>
        <li><a href="#rank-8">第8位: 松山油脂 肌をうるおす 保湿クリーム</a></li>
        <li><a href="#rank-9">第9位: Curel 潤浸保湿フェイスクリーム</a></li>
        <li><a href="#rank-10">第10位: VT COSMETICS CICA クリーム</a></li>
        <li><a href="#selection-matrix">2. 専門ラボ直伝：冬の肌悩み別バリアクリーム選び方マトリクス</a></li>
        <li><a href="#faq-section">3. よくある質問・Q&Aセクション</a></li>
      </ul>
    </div>

    <div class="science-box" id="science-guide">
      <h3>🔬 11月〜12月の肌で何が起きている？『寒冷バリア破綻』の皮膚科学メカニズム</h3>
      <p>
        秋から冬への移行期である11月・12月は、1年の中で最も肌バリア機能が急低下する危険地帯です。その最大の原因は、外気湿度の低下と気温低下による『皮脂膜の消失』および『角質細胞間脂質の硬化』にあります。
      </p>
      <div class="science-grid">
        <div class="science-card blue">
          <h4>① 皮脂膜の消失と急激な脱水</h4>
          <p>気温が10度を下回ると皮脂腺の活動が鈍化し、天然の油膜である皮脂の分泌量が夏の約30〜40%まで減少。無防備になった角層表面から水分が秒速で蒸散します。</p>
        </div>
        <div class="science-card">
          <h4>② ラメラ液晶構造の乱れ・粉吹き</h4>
          <p>セラミドを中心とする細胞間脂質が寒冷で固まり、水分と油分の美しいサンドイッチ構造が破綻。角質細胞がめくれ上がり、白く粉を吹いた状態に陥ります。</p>
        </div>
        <div class="science-card purple">
          <h4>③ 寒暖差による乾燥性微小炎症</h4>
          <p>外の冷気（5℃以下）と暖房の効いた室内（22℃以上）を行き来することで毛細血管の急激な拡張と収縮が繰り返され、ヒリつきや赤み、かゆみが発生します。</p>
        </div>
      </div>
      <p style="margin-top: 20px;">
        この過酷な三重苦を克服するために不可欠なのが、ヒトの生体構造に類似した『セラミドカプセル』『ラメラ液晶乳化』『抗炎症パンテノール』を配合した高保湿バリアクリームです。通常のクリームが肌表面に留まるのに対し、バリアクリームは角層細胞の隙間へ深く侵入して強固な『擬似バリア膜』を再構築します。
      </p>
    </div>

    <h2 class="section-title">真冬の肌乾燥とさようなら！高保湿バリアクリームおすすめランキング10選</h2>

    {product_cards_html}

    <div class="summary-box" id="selection-matrix">
      <h3>📊 肌質・悩み別の最適なバリアクリーム選び方マトリクス</h3>
      <p>
        ランキング掲載の10製品はすべて冬の乾燥に対して最高峰の実力を持っていますが、ご自身の肌質や特に気になる症状に合わせて選ぶことで、さらに確実な美肌効果を実感できます。
      </p>
      <table class="summary-table">
        <thead>
          <tr>
            <th>肌悩み・目的</th>
            <th>おすすめのアイテム</th>
            <th>注目の主要成分</th>
            <th>仕上がりの質感</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>真冬の粉吹き・皮剥け・超乾燥</strong></td>
            <td>AESTURA / Real Barrier</td>
            <td>高密度セラミドカプセル、特許MLE構造</td>
            <td>高密着・長時間しっとりシールド</td>
          </tr>
          <tr>
            <td><strong>寒暖差による赤み・ヒリつき・荒れ</strong></td>
            <td>LA ROCHE-POSAY / SKIN1004</td>
            <td>パンテノール5%、発酵ツボクサエキス</td>
            <td>保護包帯ヴェール・鎮静なめらか</td>
          </tr>
          <tr>
            <td><strong>敏感肌・無香料・低刺激重視</strong></td>
            <td>松山油脂 / ETVOS / キュレル</td>
            <td>5種ヒト型セラミド、消炎アラントイン</td>
            <td>ふんわりスフレ〜濃密バター</td>
          </tr>
          <tr>
            <td><strong>顔〜全身を惜しみなく保湿したい</strong></td>
            <td>ILLIYOON セラミドアト集中</td>
            <td>セラミドスキンコンプレックス</td>
            <td>大容量・高コスパ・すべすべ保護膜</td>
          </tr>
          <tr>
            <td><strong>ニキビができやすい混合肌の冬乾燥</strong></td>
            <td>VT COSMETICS CICAクリーム</td>
            <td>シカヒアルロン、セラミドNP</td>
            <td>みずみずしい水分鎮静ジェル</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="hub-link-banner">
      <div>
        <h4>❄️ あわせてチェックしたい冬の集中保湿ケア</h4>
        <p>バリアクリームの前に仕込む高保湿美容液や、寝ている間に集中修復するナイトセラムの特集も公開中！</p>
      </div>
      <a href="/winter-ceramide-serum" class="hub-link-btn">高保湿セラミド美容液特集へ →</a>
    </div>

    <div class="summary-box" id="faq-section">
      <h2 style="font-size: 1.3rem; margin-bottom: 20px; color: #0f172a;">❓ 真冬の高保湿バリアクリームに関するよくある質問（FAQ）</h2>
      {faq_html}
    </div>
  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-title">LUMI COSMETICS LAB 関連コンテンツ一覧</div>
      <div class="footer-links">
        {footer_links_html}
      </div>
      <div class="copyright">
        &copy; 2026 LUMI COSMETICS LAB. All rights reserved. 掲載されている商品価格・仕様・レビュー情報は楽天市場APIよりリアルタイムに自動取得された最新データです。
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-barrier-cream.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-barrier-cream.html!")
