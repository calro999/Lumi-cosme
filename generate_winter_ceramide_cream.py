import json
import re

with open("fetched_3new_nov_dec_ceramide_peptide_hair_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_ceramide_cream"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 敏感肌・乾燥性肌の不動の守護神！消炎成分×セラミド機能で粉吹きをピタッと鎮静",
        "catch": "赤み・ヒリつき・粉吹きが起こる真冬のレスキュークリーム。ふわっと軽やかなのに鉄壁の保水膜を形成",
        "brand_name": "Curel (キュレル)",
        "capacity": "40g (潤浸保湿フェイスクリーム / 医薬部外品)",
        "type": "医薬部外品・薬用セラミド機能成分配合高保湿フェイスクリーム",
        "features": "セラミド機能成分（ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド）、ユーカリエキス、アラントイン（消炎有効成分）",
        "value": "花王の30年以上にわたるセラミド研究の結晶。冬の寒風で角層バリアが崩壊した超敏感肌でも刺激を感じず、吸い付くような潤いが一日中持続",
        "desc_p1": "11月から12月にかけて湿度が20%台まで急落すると、皮膚の最外層にある角質細胞間脂質の主成分『セラミド』が減少し、バリア機能が著しく低下します。少しの冷風や摩擦でも顔が赤くほてり、メイクの上から粉を吹いてしまうような深刻な冬の敏感肌に、最も信頼できる処方として皮膚科医からも支持されるのがキュレルの『潤浸保湿フェイスクリーム』です。",
        "desc_p2": "独自の『セラミド機能成分』が角層の深部までじんわり浸透し、隙間だらけになった細胞間を満たして水分蒸散を徹底ブロック。さらに消炎有効成分アラントインが、冬の乾燥によって引き起こされる目に見えない微細な炎症を穏やかに鎮めます。驚くべきはまるでスフレのように軽やかでベタつきのないテクスチャー。朝のメイク前にたっぷり塗り込んでもファンデーションがヨレず、夜までふっくらと柔らかいモチ肌をキープできます。",
        "target": "冬になると洗顔後すぐに肌がつっぱる方、粉吹きや赤みが出やすい敏感肌の方、ベタつく重いクリームが苦手な方",
        "point": "化粧水や乳液で肌を整えた後、直径約2cm程度を手のひらに取り、顔全体に優しく包み込むようになじませます。特に乾燥しやすい目元や口元には重ね付けが効果的です。"
    },
    {
        "rank": 2,
        "tag": "🔬 独自のセラミド微細カプセルが肌の上でとろける！120時間潤い持続の韓国No.1ダーマクリーム",
        "catch": "目に見えるセラミドカプセルが角層の隙間を埋め尽くし、寒冷地の過酷な乾燥環境でも強靭な肌バリアを再建",
        "brand_name": "AESTURA (エストラ)",
        "capacity": "80ml (アトバリア365 クリーム)",
        "type": "高密度セラミドカプセル配合・皮膚科領域発想バリア強化クリーム",
        "features": "Triple Lipid-Capsule（セラミド・コレステロール・脂肪酸の生体模倣比率）、スフィンゴ脂質、ナイアシンアミド",
        "value": "韓国のアモーレパシフィック皮膚科学研究所が開発。人間の細胞間脂質構造を完璧に再現したカプセルが、冬の砂漠肌を瞬時に柔らかく満たす",
        "desc_p1": "韓国の厳しい氷点下環境で鍛え上げられ、オリーブヤングや美容皮膚科で圧倒的な支持を集めるのがエストラの『アトバリア365 クリーム』です。冬の寒暖差やエアコンの温風は、肌内部の脂質バランスを破壊し、何を塗っても数時間後には乾燥してしまう『乾燥ループ』を引き起こします。",
        "desc_p2": "チューブから出すと目に見える微細な白色のカプセル『Triple Lipid-Capsule』が特徴。肌に伸ばすと体温でカプセルがすっと溶け崩れ、セラミド・コレステロール・脂肪酸という皮膚のバリア3大成分が黄金比率で角層の隙間に浸透します。表面に油膜のギトギト感を残さず、内側がみっちりと詰まったような弾力感と密封感を実現。夜塗って眠れば、翌朝の洗顔時まで潤いのシールドがしっかりと肌を守り抜きます。",
        "target": "朝メイクしても昼過ぎには頬が乾燥して突っ張る方、冬のインナードライに悩む方、濃厚な保湿感と浸透力の両方を求める方",
        "point": "スキンケアの最後に適量を手に取り、手のひらでカプセルを温めながら顔全体に優しくハンドプレスしてなじませます。夜は少し厚めに塗ってスリーピングパックとしても活躍します。"
    },
    {
        "rank": 3,
        "tag": "🌿 5種のヒト型セラミド×大豆由来成分！濃密なコクで乾いた角層を潤す無添加処方",
        "catch": "松山油脂が誇る高純度スキンケア。角質層の水分保持力を根本から底上げするリッチな保湿力",
        "brand_name": "松山油脂 (M mark)",
        "capacity": "50g (肌をうるおす保湿スキンケア 保湿クリーム)",
        "type": "5種のヒト型セラミド＆大豆発酵エキス配合・低刺激高保湿クリーム",
        "features": "ヒト型セラミド1・2・3・5・6II、大豆胚芽抽出液、ダイズ種子エキス、シア脂、スクワラン、アルコール・香料フリー",
        "value": "角層の脂質と同等構造を持つヒト型セラミドを5種も贅沢配合。固めのリッチなバーム状クリームが肌の上でとろけ、真冬の厳しい乾きを封じ込める",
        "desc_p1": "創業100年を超える日本の老舗油脂メーカー・松山油脂が手掛ける『肌をうるおす保湿スキンケア』シリーズ。その中でも保湿クリームは、プチプラとは思えない贅沢な成分構成で美容専門家からも高い評価を受けています。12月の本格的な寒波で肌の水分量が底を突いた時、角層の土台から再構築してくれる実力派です。",
        "desc_p2": "人間の肌に存在するセラミドと全く同じ立体構造を持つ5種類のヒト型セラミド（EOP、NG、NP、AG、AP）をバランスよく配合。さらに大豆由来の保湿成分とシアバター、スクワランが加わり、濃厚でコクのあるクリームが乾いた肌をぴたりと密閉します。アルコール、香料、着色料、鉱物油、パラベンを一切使わない無添加処方のため、冬の乾燥でデリケートになった目元や口元にも安心。使い続けることで肌本来の保水力が育ちます。",
        "target": "ヒト型セラミドを高濃度で補給したい方、無添加・低刺激で肌に優しい処方を好む方、優れたコスパで毎日惜しみなく使いたい方",
        "point": "あずき粒大を指先に取り、手のひらで軽く温めてから顔全体に馴染ませます。特に乾燥が気になるフェイスラインやほうれい線周りには指の腹で重ね付けを。"
    },
    {
        "rank": 4,
        "tag": "🧱 特許MLE技術で皮膚構造を完全再現！冬の暖房直撃でも乾燥を寄せ付けない鉄壁クリーム",
        "catch": "リアルバリアの独自技術が角層のラメラ構造を整え、外的刺激を跳ね返す強靭なバリアを構築",
        "brand_name": "Real Barrier (リアルバリア)",
        "capacity": "50ml (エクストリーム クリーム)",
        "type": "特許MLEバリア再建・高密度密着セラミドクリーム",
        "features": "独自開発セラミド複合体（MLE技術）、パンテノール、マデカッソシド、アラントイン、弱酸性",
        "value": "本物の皮膚脂質ラメラ構造をクロス状に再現する国際特許MLE技術。冬の乾燥でボロボロになった角層のすき間を物理的・生化学的に修復",
        "desc_p1": "冬のオフィスのエアコン暖房直下で長時間仕事をしていると、肌から水分が激しく奪われ、夕方には頬がこわばってつっぱり感を覚えます。リアルバリアの『エクストリーム クリーム』は、皮膚科学の最先端であるMLE（Multi Lamellar Emulsion）技術によって、傷ついた皮膚のバリア膜を根本から再構築するために作られた高機能クリームです。",
        "desc_p2": "一般的なクリームの乳化構造とは異なり、人間の健康な皮膚と同じ『十字架状のラメラ液晶構造』を形成。肌に塗布した瞬間、細胞間脂質と一体化するように密着し、冬の乾燥外気による水分の蒸散を遮断します。高濃度のパンテノールとマデカッソシドが配合されているため、暖房や寒さでピリつく肌を素早くクールダウンし、健やかな状態へと導きます。しっとりするのにベタつかず、ベルベットのような滑らかな仕上がりが特徴です。",
        "target": "暖房の風が当たる環境で一日中過ごす方、肌のキメが乱れてツヤを失っている方、皮膚バリアの根本修復を目指したい方",
        "point": "付属のスパチュラで適量を取り、手のひらで温めてから顔の内側から外側へ包み込むようにハンドプレス。乾燥が気になる首元まで伸ばすのがおすすめです。"
    },
    {
        "rank": 5,
        "tag": "💎 5種のヒト型セラミドを高濃度ラメラ配合！濃密な潤いでふっくらハリ肌へ導くエイジング保湿",
        "catch": "ミネラルコスメのエトヴォスが贈る最高峰の保湿力。シアバターと植物オイルが肌を濃密ラッピング",
        "brand_name": "ETVOS (エトヴォス)",
        "capacity": "30g (モイスチャライジングクリーム)",
        "type": "ヒト型セラミド高配合・リッチエモリエント保湿クリーム",
        "features": "5種のヒト型セラミド（1・2・3・5・6II）、シアバター、マカデミアナッツ脂肪酸フィトステリル、ヒアルロン酸Na、天然ラベンダー精油",
        "value": "エトヴォスのスキンケアの神髄。ラメラ液晶構造でカプセル化されたヒト型セラミドが角層深部まで溶け込み、冬の乾燥小ジワをふっくら持ち上げる",
        "desc_p1": "11月から12月にかけて気温が下がると、皮脂分泌量が急激に落ち込み、大人の肌は『水分不足』と『油分不足』の二重苦に直面します。この冬枯れ肌に対して、贅沢な油分と高濃度セラミドを絶妙なバランスで補給してくれるのがエトヴォスの『モイスチャライジングクリーム』です。",
        "desc_p2": "肌との親和性に優れた5種のヒト型セラミドをバランスよく配合し、さらにシアバターやマカデミアナッツオイルなどの上質な植物油がリッチな保護膜を形成。こっくりとしたリッチな感触のクリームが肌にピタッと吸い付き、夜の睡眠中に日中の寒暖差ダメージをじっくり修復します。ほのかに香る天然ラベンダーの穏やかなアロマが、真冬のスキンケア時間を優雅なリラックスタイムへと昇華させます。",
        "target": "30代以上の大人の乾燥小ジワやハリ不足に悩む方、オイルとセラミドの両方でリッチに保湿したい方、精油の心地よい香りに癒されたい方",
        "point": "パール粒大を手のひらに取り、温めて柔らかくしてから顔全体になじませます。目尻やほうれい線など、乾燥しやすい部分には指先でトントンと優しく押し込むように重ねてください。"
    },
    {
        "rank": 6,
        "tag": "🌿 8種の天然型セラミドを贅沢配合！製薬会社の皮膚科学で超乾燥肌を集中レスキュー",
        "catch": "ロート製薬のセラミド研究の集大成。洗顔や入浴で失われやすいバリア成分を補給し、カサつきを即ブロック",
        "brand_name": "ロート製薬 ケアセラ",
        "capacity": "70g (ケアセラ AP高保湿フェイス＆ボディクリーム)",
        "type": "8種の天然型セラミド配合・薬用バリア集中補修クリーム",
        "features": "天然型セラミド（セラミド1・2・3・6II・EOS・カプロオイルフィトスフィンゴシン・カプロオイルスフィンゴシン）、ペプチドCP、弱酸性・パラベンフリー",
        "value": "ドラッグストアで手に入る最高峰のセラミド配合数。顔だけでなく乾燥が深刻な首や手元まで、これ1本で冬の粉吹きを徹底解決",
        "desc_p1": "ロート製薬が皮膚のバリア機能低下に本気で向き合って開発した『ケアセラ AP』シリーズ。その中でも高保湿クリームは、8種類もの天然型セラミド（セラミドプラスを含む）を配合した圧巻の処方設計で、美容感度の高い層から絶大な信頼を寄せられています。",
        "desc_p2": "肌のセラミド産生を促すペプチドCPと、失われたセラミドをダイレクトに補う複合セラミドが相乗効果を発揮。こっくりと濃厚なクリームが肌に伸び広がり、見えない保護フィルムのように密着して外部刺激から皮膚を防御します。顔のスキンケアはもちろん、冬に乾燥してヒビ割れそうな指先や口元、首元など全身のパーツケアにも惜しみなく使える70gのたっぷりサイズ。頑固なカサつきを翌朝にはしっとり柔らかな素肌へと導きます。",
        "target": "どんなクリームを使っても時間が経つと乾燥してしまう方、顔から首・手元までマルチに高保湿ケアしたい方、製薬会社の確かな成分設計を重視する方",
        "point": "スキンケアの仕上げに適量を顔全体に塗布。乾燥によるかゆみや粉吹きが出やすい頬やあご周りには少し厚めに塗り伸ばすのがポイントです。"
    },
    {
        "rank": 7,
        "tag": "🌸 創業40年のサロン品質！冬のトラブル肌を穏やかに整える濃密エモリエントクリーム",
        "catch": "皮膚トラブル専門サロンから生まれた名品。上質なスクワランとセラミドが肌本来の治癒力を高める",
        "brand_name": "シェルクルール (Cher-Couleur)",
        "capacity": "30g (ナチュレポウ デュオクリーム)",
        "type": "サロン専売品質・弱酸性高保湿バリアエモリエントクリーム",
        "features": "天然セラミド、高精製スクワラン、バイオ成分、ビフィズス菌培養溶解質、無香料・低刺激",
        "value": "アトピー肌や頑固な肌荒れに悩む女性たちに長年愛され続ける隠れた名品。冬の環境ストレスで過敏になった角質層をやさしく鎮静",
        "desc_p1": "冬の乾燥が進むと、普段の化粧品が急にしみたり、痒みを伴う肌荒れに悩まされる方が増えます。全国のコスメセレクトショップやサロンで熱烈なファンを持つシェルクルールの『ナチュレポウ デュオクリーム』は、そうした不安定なゆらぎ肌を救うために誕生した低刺激クリームです。",
        "desc_p2": "不純物を極限まで取り除いた高品質の天然スクワランとセラミドが、皮脂膜の代わりとなって肌表面を優しくラッピング。さらにビフィズス菌培養液などのバイオ成分が常在菌バランスを整え、冬の寒暖差に負けない強い素肌を育みます。非常にコクがあるのに肌の上で滑らかに伸び、塗った直後から肌が落ち着くような安らぎ感を与えてくれます。",
        "target": "冬の寒暖差で肌が敏感になり赤みや痒みが出やすい方、サロン品質の上質なクリームを試したい方、余計な添加物を避けたい方",
        "point": "手のひらに大豆粒大を取り、顔全体を温めるようにハンドプレスしながら馴染ませます。赤みのある部分には擦らず置くように塗布してください。"
    },
    {
        "rank": 8,
        "tag": "🔬 ヒト型セラミド原液をそのままクリーム化！成分主義ブランドが贈る高純度バリア",
        "catch": "余計な装飾を排した高濃度設計。カサつく冬の角層にセラミド本来の保水力をダイレクト注入",
        "brand_name": "KISO (キソ)",
        "capacity": "50g (ハイドロクリーム セラミド)",
        "type": "高濃度ヒト型セラミド配合・原液コスメバリアクリーム",
        "features": "ヒト型セラミド（EOP、NP、AP）、フィトスフィンゴシン、ヒアルロン酸Na、スクワラン、7つの無添加",
        "value": "日本の原液スキンケアのトップランナーKISOによる高純度クリーム。無香料・無着色で、セラミドの恵みだけを真っ直ぐ肌に届ける",
        "desc_p1": "コスメの成分配合率にこだわるスキンケアマニアから絶賛されているのが、KISOの『ハイドロクリーム セラミド』です。冬の肌乾燥を乗り切るためには、肌の脂質構造に近いセラミドを十分な濃度で補給することが不可欠。本製品はその理想をストレートに具現化しています。",
        "desc_p2": "3種のヒト型セラミドとバリア機能を補佐するフィトスフィンゴシンを高濃度でブレンド。白くなめらかなクリームが肌のすみずみまでスルスルと行き渡り、乾燥でカチコチに硬くなった角質細胞を瞬時に柔らかく解きほぐします。ベタつきが少なく後肌がサラリとしているため、朝のメイク前にも夜の集中ケアにも使い勝手抜群。1,000円台という驚異的な価格設定でリピーターが後を絶ちません。",
        "target": "成分の純度や濃度にこだわりたい方、コスパ最強のヒト型セラミドクリームを探している方、ベタつかない使用感を好む方",
        "point": "化粧水の後に適量を手に取り、顔全体から首元にかけて優しく引き上げるようになじませます。乾燥が気になる部分には重ね付けが推奨されます。"
    },
    {
        "rank": 9,
        "tag": "🛡️ パンテノール5%×シカ成分の鉄壁シールド！冬の肌荒れ・マスク擦れを即座に修復",
        "catch": "世界中で愛されるレスキューバリア。高純度パンテノールが角層の修復を早め、乾燥刺激を完全遮断",
        "brand_name": "LA ROCHE-POSAY (ラロッシュポゼ)",
        "capacity": "40ml (シカプラスト リペアクリーム B5+)",
        "type": "皮膚科学発想・高濃度パンテノール＆シカ配合リペアバリアクリーム",
        "features": "高濃度パンテノール（プロビタミンB5）5%、マデカッソシド（ツボクサエキス）、トリビオマ（プレバイオティクス複合体）、シアバター",
        "value": "美容医療後のデリケートな肌ケアにも使用される世界的大ベストセラー。寒風や乾燥で皮剥けした肌を瞬時に保護し、肌荒れの連鎖を断ち切る",
        "desc_p1": "フランスの湧水ラロッシュポゼターマルウォーターをベースにしたダーマコスメブランド。世界各国の皮膚科医が推奨する『シカプラスト リペアクリーム B5+』は、冬の過酷な乾燥による皮剥けや赤み、ヒリヒリ感を一瞬で包み込んで沈静化させる集中リペアクリームです。",
        "desc_p2": "組織修復を促す高濃度パンテノール（5%）と、ツボクサ由来のマデカッソシドが傷ついた角層バリアを素早く再建。シアバター配合のこっくりとしたテクスチャーが肌の上に保護膜を張り、冬の冷たい外気や衣類の摩擦刺激を物理的に遮断します。夜のスキンケアの仕上げにたっぷり塗って眠ると、翌朝には赤みや皮剥けが落ち着き、なめらかで均一な肌トーンを取り戻すことができます。",
        "target": "冬の乾燥で鼻の下や口周りの皮が剥けてしまう方、寒風による赤みや刺激を感じやすい方、美容施術後の敏感な肌を守りたい方",
        "point": "朝晩の洗顔後、化粧水の後に適量を手に取り、患部をこすらないように優しく包み込むように塗布します。特に肌荒れがひどい部位には厚めにのせるバームパックが効果的です。"
    },
    {
        "rank": 10,
        "tag": "🐘 566gの大容量で家族全員全身うるおう！世界中で愛される超高保湿モイスチャライジング",
        "catch": "ナイアシンアミドとパンテノールを新配合。真冬の過酷な粉吹き乾燥をこっくり濃厚な油分膜でガード",
        "brand_name": "Cetaphil (セタフィル)",
        "capacity": "566g (モイスチャライジングクリーム)",
        "type": "低刺激・敏感肌用全身高保湿モイスチャライジングクリーム",
        "features": "ナイアシンアミド、パンテノール、グリセリン、アーモンド油、無香料・低刺激処方",
        "value": "製薬会社ガルデルマが皮膚科学に基づき開発。角層の水分と油分を長時間逃さないリッチなコクで、真冬の粉吹き肌をシルクのような柔肌へ",
        "desc_p1": "世界70カ国以上で愛用される敏感肌用スキンケアブランド・セタフィルの大ベストセラー『モイスチャライジングクリーム』。真冬になると顔だけでなく、すねや腕、背中まで全身が粉を吹いて痒くなるという深刻な全身乾燥に悩む方に最適な大容量クリームです。",
        "desc_p2": "ナイアシンアミド、パンテノール、高純度グリセリンを組み合わせた独自の『モイスチャーバリア処方』により、角層深部へ素早く浸透しながら表面を上質なアーモンド油がラッピング。こっくりとした濃厚なテクスチャーでありながら、肌に伸ばすと体温でするりと馴染み、ベタつきを残さず長時間しっとり感が持続します。566gというメガサイズなので、顔のケアからお風呂上がりのボディケアまで贅沢に使い倒せます。",
        "target": "顔だけでなく全身の粉吹きや乾燥かゆみに悩む方、大容量で家族全員でたっぷり使いたい方、海外皮膚科医推奨の王道保湿を求める方",
        "point": "入浴後や洗顔後、水分が肌に残っているうちにたっぷりと手に取り、全身や顔に優しく伸ばします。乾燥が激しいひじ、かかと、ひざには円を描くようにマッサージしながら塗り込むと効果的です。"
    }
]

faq_items = [
    {
        "q": "セラミドクリームと一般的な保湿クリーム（乳液やワセリン）の決定的な違いは何ですか？",
        "a": "一般的な乳液やワセリンは、主に油分で肌の表面に膜を張り『水分の蒸発を防ぐ（エモリエント効果）』のが目的です。これに対してセラミドクリームは、肌本来の角質細胞間脂質の主成分である『セラミド』を直接補給し、角層内部で水分を挟み込んで逃さない『ラメラ構造（バリア機能）』を物理的・生化学的に修復・再建します。そのため、表面はしっとりしているのに内側が突っ張る『インナードライ』や、冬の寒風による粉吹き・赤み・ヒリつきに対して根本的な解決力を発揮します。"
    },
    {
        "q": "ヒト型セラミドと天然セラミド、疑似セラミド（セラミド機能成分）はどう選べば良いですか？",
        "a": "目的と肌質に合わせて選ぶのがベストです。『ヒト型セラミド（セラミドNP、AP、EOP等）』は人間の肌に存在するセラミドと全く同じ立体構造を持つため、肌馴染みと保水修復スピードが最も優れています。『天然セラミド（セレブロシド等）』は動物や植物由来で親和性が高く、肌を柔らかくほぐす力に長けています。また花王キュレルなどに配合される『セラミド機能成分（疑似セラミド）』は、安定性が極めて高く低刺激で、敏感肌でも安心かつ高濃度で毎日続けやすいという大きなメリットがあります。"
    },
    {
        "q": "冬（11月〜12月）にセラミドクリームを使う最適なタイミングと効果的な塗り方は？",
        "a": "朝晩のスキンケアの『最後のステップ』として使用します。化粧水や美容液で十分に水分を補給した直後、手のひらでクリームを軽く温めてから顔全体を包み込むようにハンドプレスして馴染ませるのが鉄則です。擦るように塗り広げると摩擦刺激でバリア機能を傷めるため、優しく押し込むように塗布してください。特に乾燥しやすい目元、口元、頬骨の高い位置には、少量を指先でトントンと重ね塗り（ミルフィーユ塗り）すると、暖房直下でも一日中乾燥知らずで過ごせます。"
    },
    {
        "q": "脂性肌（オイリー肌）や混合肌でも、冬はセラミドクリームを使うべきですか？",
        "a": "はい、強く推奨されます。冬のオイリー肌の多くは、エアコンや寒気によって角層の水分が失われた結果、肌が危機感を覚えて過剰に皮脂を分泌してしまう『インナードライ』状態です。セラミドクリームで角層の水分保持力を整えることで、過剰な皮脂分泌が自然と抑制され、テカリや毛穴開き、メイク崩れが劇的に改善します。オイリー肌の方は、本ランキング第1位のキュレルのようにジェルとクリームの中間のような軽やかな質感のものを選ぶと快適に使用できます。"
    },
    {
        "q": "敏感肌で新しいクリームを使うと赤みやピリつきが出やすいのですが、安心な選び方は？",
        "a": "アルコール（エタノール）、合成香料、着色料、強い防腐剤が無添加の『低刺激・弱酸性設計』のものを選んでください。本ランキングで紹介している『キュレル』『松山油脂』『ケアセラ』『ラロッシュポゼ』などは、アレルギーテスト済みや敏感肌パッチテスト済みで、刺激を徹底的に抑えた処方になっています。初めて使用する際は、いきなり全顔に塗るのではなく、夜に入浴後、フェイスラインや腕の内側でパッチテストを行ってから使用するとより安全です。"
    }
]

# JSON-LD構造化データ
json_ld_products = []
for p, item in zip(product_details, items):
    json_ld_products.append({
        "@type": "Product",
        "name": f"{p['brand_name']} {p['capacity']}",
        "image": item['image'],
        "description": p['value'],
        "brand": {
            "@type": "Brand",
            "name": p['brand_name']
        },
        "offers": {
            "@type": "Offer",
            "url": item['affiliateUrl'],
            "priceCurrency": "JPY",
            "price": item['price'],
            "availability": "https://schema.org/InStock"
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで冬の肌荒れ・粉吹き乾燥とさようなら！角層バリアを高密度修復する高保湿セラミドクリームランク10",
    "description": "11月・12月の冬本番に深刻化する冷気と暖房による角層バリア破壊・粉吹き乾燥・ヒリつき肌を徹底解決！ヒト型セラミドや高濃度セラミドを贅沢配合した高保湿フェイスクリーム10選を徹底比較！キュレル、AESTURA、松山油脂、リアルバリア、エトヴォス、ケアセラなど、真冬でも一日中もっちり潤い肌が続く至高のクリームを厳選。",
    "image": items[0]['image'],
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
    "datePublished": "2026-11-02",
    "dateModified": "2026-11-02"
}

json_ld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "冬の高保湿セラミドクリーム おすすめランキング10選",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "item": prod
        } for idx, prod in enumerate(json_ld_products)
    ]
}

json_ld_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["a"]
            }
        } for item in faq_items
    ]
}

cards_html = []
for p, item in zip(product_details, items):
    cards_html.append(f"""
      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge-wrap">
          <span class="rank-badge rank-{p['rank']}">第{p['rank']}位</span>
          <span class="feature-tag">{p['tag']}</span>
        </div>
        <h3 class="product-name">{p['brand_name']} {p['capacity']}</h3>
        <p class="product-catch">{p['catch']}</p>
        
        <div class="product-body">
          <div class="product-img-box">
            <img src="{item['image']}" alt="{p['brand_name']} {p['capacity']} 高保湿セラミドクリーム" class="product-img" loading="lazy" width="280" height="280">
          </div>
          <div class="product-meta">
            <table class="meta-table">
              <tr>
                <th>タイプ</th>
                <td>{p['type']}</td>
              </tr>
              <tr>
                <th>主要成分</th>
                <td>{p['features']}</td>
              </tr>
              <tr>
                <th>容量 / 実勢価格</th>
                <td>{p['capacity']} / <span class="price-val">¥{item['price']:,}</span> (税込・楽天市場最新)</td>
              </tr>
              <tr>
                <th>独自バリュー</th>
                <td>{p['value']}</td>
              </tr>
            </table>
          </div>
        </div>
        
        <div class="product-desc-box">
          <h4 class="desc-heading">🔍 冬（11月・12月）の肌悩みへのアプローチ＆使用感</h4>
          <p class="desc-text">{p['desc_p1']}</p>
          <p class="desc-text">{p['desc_p2']}</p>
          
          <div class="recommend-box">
            <div class="recommend-target">
              <span class="rec-icon">🎯</span>
              <strong>こんな方におすすめ：</strong> {p['target']}
            </div>
            <div class="recommend-usage">
              <span class="rec-icon">💡</span>
              <strong>効果を高めるプロの使い方：</strong> {p['point']}
            </div>
          </div>
        </div>

        <div class="cta-wrap">
          <a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            <span class="rakuten-icon">🛍️</span> 楽天市場で「{p['brand_name']}」の最安値・口コミを見る（¥{item['price']:,}〜）
          </a>
        </div>
      </article>
""")

table_rows = []
for p, item in zip(product_details, items):
    table_rows.append(f"""
            <tr>
              <td class="col-rank"><span class="table-rank rank-{p['rank']}">第{p['rank']}位</span></td>
              <td class="col-name"><strong>{p['brand_name']}</strong><br>{p['capacity']}</td>
              <td class="col-feat">{p['features']}</td>
              <td class="col-price">¥{item['price']:,}</td>
              <td class="col-btn"><a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="table-btn">楽天詳細</a></td>
            </tr>
""")

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の肌荒れ・粉吹き乾燥とさようなら！角層バリアを高密度修復する高保湿セラミドクリームランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬本番に深刻化する冷気と暖房による角層バリア破壊・粉吹き乾燥・ヒリつき肌を徹底解決！ヒト型セラミドや高濃度セラミドを贅沢配合した高保湿フェイスクリーム10選を徹底比較！キュレル、AESTURA、松山油脂、リアルバリア、エトヴォス、ケアセラなど、真冬でも一日中もっちり潤い肌が続く至高のクリームを厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-ceramide-cream">
  <meta name="robots" content="index, follow, max-image-preview:large">
  
  <!-- OGP & SNS -->
  <meta property="og:title" content="保湿力の強さで冬の肌荒れ・粉吹き乾燥とさようなら！角層バリアを高密度修復する高保湿セラミドクリームランク10">
  <meta property="og:description" content="11月・12月の冬本番の粉吹き乾燥・肌荒れを徹底解決！角層バリアを高密度修復する高保湿セラミドクリーム10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-ceramide-cream">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#2b6cb0">

  <!-- 構造化データ (JSON-LD) -->
  <script type="application/ld+json">
{json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(json_ld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(json_ld_faq, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #2b6cb0;
      --primary-light: #ebf8ff;
      --primary-dark: #1a365d;
      --text-main: #2d3748;
      --text-sub: #718096;
      --bg-page: #fbfbfc;
      --bg-card: #ffffff;
      --border: #edf2f7;
      --border-focus: #90cdf4;
      --shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
      --radius: 16px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif;
      background: var(--bg-page);
      color: var(--text-main);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}
    header.site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(10px);
      background-color: rgba(255, 255, 255, 0.95);
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-weight: 800;
      font-size: 1.25rem;
      color: var(--primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .header-nav a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .header-nav a:hover {{ color: var(--primary); }}
    
    .container {{
      max-width: 920px;
      margin: 0 auto;
      padding: 30px 20px 80px;
    }}
    
    .breadcrumbs {{
      display: flex;
      gap: 8px;
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 24px;
      flex-wrap: wrap;
    }}
    .breadcrumbs a {{
      color: var(--text-sub);
      text-decoration: none;
    }}
    .breadcrumbs a:hover {{ color: var(--primary); }}
    
    .article-header {{
      background: #ffffff;
      padding: 40px 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 40px;
      border: 1px solid var(--border);
    }}
    .header-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 16px;
    }}
    .article-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.45;
      color: #1a202c;
      margin-bottom: 20px;
    }}
    .article-lead {{
      font-size: 1.05rem;
      color: #4a5568;
      line-height: 1.85;
      margin-bottom: 24px;
    }}
    .meta-info {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: var(--text-sub);
      border-top: 1px solid var(--border);
      padding-top: 16px;
    }}
    
    .section-box {{
      background: #ffffff;
      padding: 36px 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 40px;
      border: 1px solid var(--border);
    }}
    .section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #1a202c;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--primary);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .content-p {{
      margin-bottom: 18px;
      font-size: 1rem;
      color: #4a5568;
    }}
    
    .mechanism-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 20px;
      margin-top: 24px;
    }}
    .mechanism-card {{
      background: #f7fafc;
      padding: 24px;
      border-radius: 12px;
      border-left: 4px solid var(--primary);
    }}
    .mech-title {{
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 10px;
    }}
    .mech-desc {{
      font-size: 0.95rem;
      color: #4a5568;
      line-height: 1.7;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 32px;
      margin-bottom: 40px;
      border: 1px solid var(--border);
      position: relative;
    }}
    .product-badge-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 14px;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: #4a5568;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 4px 14px;
      border-radius: 20px;
    }}
    .rank-badge.rank-1 {{ background: linear-gradient(135deg, #ecc94b, #d69e2e); }}
    .rank-badge.rank-2 {{ background: linear-gradient(135deg, #cbd5e0, #a0aec0); }}
    .rank-badge.rank-3 {{ background: linear-gradient(135deg, #ed8936, #dd6b20); }}
    .feature-tag {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--primary);
    }}
    .product-name {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #1a202c;
      margin-bottom: 8px;
      line-height: 1.4;
    }}
    .product-catch {{
      font-size: 1rem;
      color: var(--primary);
      font-weight: 700;
      margin-bottom: 24px;
    }}
    
    .product-body {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 28px;
      margin-bottom: 24px;
    }}
    @media (max-width: 768px) {{
      .product-body {{ grid-template-columns: 1fr; }}
      .product-img-box {{ text-align: center; }}
    }}
    .product-img-box {{
      background: #f7fafc;
      border-radius: 12px;
      padding: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--border);
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      object-fit: contain;
      border-radius: 8px;
      transition: transform 0.2s;
    }}
    .product-img:hover {{ transform: scale(1.03); }}
    
    .meta-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.95rem;
    }}
    .meta-table th {{
      width: 25%;
      padding: 10px 12px;
      background: #f7fafc;
      border-bottom: 1px solid var(--border);
      text-align: left;
      font-weight: 700;
      color: #4a5568;
    }}
    .meta-table td {{
      padding: 10px 12px;
      border-bottom: 1px solid var(--border);
      color: #2d3748;
    }}
    .price-val {{
      font-weight: 800;
      color: #e53e3e;
      font-size: 1.15rem;
    }}
    
    .product-desc-box {{
      background: #fcfdfd;
      border-radius: 12px;
      padding: 24px;
      border: 1px solid #edf2f7;
      margin-bottom: 24px;
    }}
    .desc-heading {{
      font-size: 1.1rem;
      font-weight: 800;
      color: #2d3748;
      margin-bottom: 14px;
    }}
    .desc-text {{
      font-size: 0.98rem;
      color: #4a5568;
      line-height: 1.8;
      margin-bottom: 14px;
    }}
    
    .recommend-box {{
      margin-top: 18px;
      padding-top: 18px;
      border-top: 1px dashed #e2e8f0;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .recommend-target, .recommend-usage {{
      font-size: 0.95rem;
      color: #4a5568;
      line-height: 1.7;
    }}
    .rec-icon {{ margin-right: 6px; }}
    
    .cta-wrap {{
      text-align: center;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: linear-gradient(135deg, #bf0000, #e60012);
      color: #ffffff;
      font-size: 1.05rem;
      font-weight: 800;
      padding: 16px 28px;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 4px 15px rgba(230, 0, 18, 0.3);
      transition: all 0.2s;
      width: 100%;
      max-width: 600px;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000, #cc0010);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(230, 0, 18, 0.4);
    }}
    
    .comparison-table-wrap {{
      overflow-x: auto;
      margin-top: 24px;
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.95rem;
      min-width: 650px;
    }}
    .comparison-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      padding: 12px 14px;
      text-align: left;
      font-weight: 700;
      border-bottom: 2px solid #cbd5e0;
    }}
    .comparison-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
    }}
    .table-rank {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 0.8rem;
      font-weight: 800;
      background: #edf2f7;
    }}
    .table-btn {{
      display: inline-block;
      background: #e60012;
      color: #ffffff;
      padding: 6px 14px;
      border-radius: 20px;
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 700;
    }}
    .table-btn:hover {{ background: #bf0000; }}
    
    .faq-item {{
      margin-bottom: 20px;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      background: #fcfdfd;
    }}
    .faq-q {{
      font-weight: 800;
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 10px;
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }}
    .faq-a {{
      font-size: 0.98rem;
      color: #4a5568;
      line-height: 1.8;
      padding-left: 28px;
    }}
    
    footer.site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 60px 20px 40px;
      margin-top: 60px;
    }}
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
    }}
    .footer-heading {{
      font-size: 1.15rem;
      font-weight: 800;
      color: #1a202c;
      margin-bottom: 20px;
      padding-bottom: 8px;
      border-bottom: 2px solid var(--primary);
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 12px;
      margin-bottom: 40px;
    }}
    .footer-links-grid a {{
      color: #4a5568;
      text-decoration: none;
      font-size: 0.9rem;
      transition: color 0.2s;
    }}
    .footer-links-grid a:hover {{ color: var(--primary); }}
    .footer-copy {{
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-sub);
      border-top: 1px solid var(--border);
      padding-top: 24px;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">
        <span>❄️</span> 冬コスメ徹底比較ラボ
      </a>
      <nav class="header-nav">
        <a href="/">← 総合トップへ戻る</a>
      </nav>
    </div>
  </header>

  <div class="container">
    <nav class="breadcrumbs" aria-label="パンくずリスト">
      <a href="/">トップ</a> <span>&gt;</span>
      <a href="/winter-moisture-cream">フェイスクリーム</a> <span>&gt;</span>
      <span>高保湿セラミドクリーム</span>
    </nav>

    <header class="article-header">
      <span class="header-tag">2026年冬・徹底検証</span>
      <h1 class="article-title">保湿力の強さで冬の肌荒れ・粉吹き乾燥とさようなら！角層バリアを高密度修復する高保湿セラミドクリームランク10</h1>
      <p class="article-lead">
        11月から12月にかけて急激に低下する外気温と室内暖房の直撃。この過酷な真冬の気候は、皮膚の最重要防御壁である『角層セラミド』を根こそぎ奪い去り、粉吹き・赤み・ヒリつきといったバリア破綻を引き起こします。本記事では、ヒト型セラミドや独自高浸透カプセルを配合した実力派フェイスクリーム10選を徹底検証！角層の隙間を高密度に修復し、一日中もっちり吸い付くような潤い美肌を叶える至高のセラミドクリームを厳選してご紹介します。
      </p>
      <div class="meta-info">
        <span>📅 2026年11月02日更新</span>
        <span>✍️ 冬コスメ徹底比較ラボ 編集部監修</span>
        <span>⏱️ 読了目安：約8分</span>
      </div>
    </header>

    <section class="section-box">
      <h2 class="section-title">❄️ 11月・12月に「セラミドクリーム」が絶対不可欠な科学的理由</h2>
      <p class="content-p">
        晩秋から初冬（11月〜12月）は、1年の中で最も肌のバリア機能が低下しやすい警戒期間です。外気の湿度は30%以下に落ち込み、オフィスや自宅ではエアコン暖房が終日稼働。温風が肌表面の水分を容赦なく奪い去るだけでなく、寒さによる末梢血流の悪化によって表皮細胞への栄養供給が停滞し、肌自らがセラミドを合成する能力そのものが衰えてしまいます。
      </p>
      <p class="content-p">
        水分を抱え込むセラミドが不足した角層は、レンガを繋ぐセメントが抜けたブロック塀のようなもの。隙間から肌内部の水分が激しく蒸散するだけでなく、外気中のホコリや花粉、衣類の摩擦といった微細な刺激が角層奥深くまで直接侵入し、赤みやかゆみ、粉吹き、ひりつきといった深刻な肌荒れを誘発します。
      </p>

      <div class="mechanism-grid">
        <div class="mechanism-card">
          <div class="mech-title">🧱 ラメラ構造の物理的再建</div>
          <div class="mech-desc">角層細胞の間を埋める『細胞間脂質』の約50%はセラミド。水分と脂質が交互に重なるラメラ構造を整えることで、外部刺激を跳ね返す強固な防御壁を蘇らせます。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">💧 湿度0%でも離さない保水力</div>
          <div class="mech-desc">ヒアルロン酸やコラーゲンが水分を『抱え込む』のに対し、セラミドは水分を『挟み込む』性質を持ちます。極限まで乾燥した砂漠のような暖房環境でも水分を蒸散させません。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">🛡️ インナードライと肌荒れの根本断絶</div>
          <div class="mech-desc">肌内部がカラカラに乾いて皮脂だけが浮いてしまうインナードライも、セラミドで角層の空洞を満たすことで過剰な皮脂分泌が鎮静化し、健やかなキメが復活します。</div>
        </div>
      </div>
    </section>

    <section class="section-box">
      <h2 class="section-title">🔍 失敗しない！冬の高保湿セラミドクリーム選び 3大チェック基準</h2>
      <div class="mechanism-grid">
        <div class="mechanism-card">
          <div class="mech-title">1. セラミドの種類と親和性</div>
          <div class="mech-desc">最もおすすめなのは人間の肌構造と同じ『ヒト型セラミド（NP、AP、EOP等）』。また敏感肌には低刺激で続けやすい『セラミド機能成分』や『天然セラミド』も抜群の安定感を発揮します。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">2. 脂質バランス（コレステロール・脂肪酸）</div>
          <div class="mech-desc">セラミド単体よりも、コレステロールや脂肪酸がバランスよく組み合わされた処方は、角層ラメラ構造の再現性が劇的に向上。AESTURAなどの高機能ダーマコスメが採用しています。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">3. メイク邪魔しない密着テクスチャー</div>
          <div class="mech-desc">油分でギトギトするだけのクリームは朝のメイク崩れの原因に。角層深部へすっと馴染み、表面にしなやかな保護膜を張るスフレ状や高密度バーム状のものが冬のデイリー使いに最適です。</div>
        </div>
      </div>
    </section>

    <!-- ランキング商品カード群 -->
    <section class="ranking-section">
      <h2 class="section-title">🏆 保湿力高め！高保湿セラミドクリーム おすすめ人気ランキング10選</h2>
      {"".join(cards_html)}
    </section>

    <section class="section-box">
      <h2 class="section-title">📊 高保湿セラミドクリーム 性能＆スペック徹底比較表</h2>
      <p class="content-p">
        今回厳選した10商品の配合成分、実勢価格、特徴を一覧表にまとめました。ご自身の肌状態やご予算に合わせて最適な1品をお選びください。
      </p>
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>主要配合成分</th>
              <th>実勢価格</th>
              <th>詳細リンク</th>
            </tr>
          </thead>
          <tbody>
            {"".join(table_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <section class="section-box">
      <h2 class="section-title">❓ 冬のセラミドクリーム活用法 よくある質問（FAQ）</h2>
      <div class="faq-list">
        {"".join([f'''
        <div class="faq-item">
          <div class="faq-q"><span>Q.</span> {item["q"]}</div>
          <div class="faq-a">{item["a"]}</div>
        </div>
        ''' for item in faq_items])}
      </div>
    </section>

    <section class="section-box">
      <h2 class="section-title">✨ 編集部まとめ：セラミドクリームで真冬も揺らがない強靭な潤い肌へ</h2>
      <p class="content-p">
        11月から12月にかけての本格的な冬の寒さと乾燥は、どんなにスキンケアを重ねても角層のバリア機能が壊れていれば水分はどんどん逃げていってしまいます。その乾きを根本から食い止め、肌本来の健やかさと弾力を取り戻す鍵こそが『セラミドクリーム』です。
      </p>
      <p class="content-p">
        朝のメイク前には薄くなじませて日中の暖房乾燥から肌を守り、夜は少し贅沢に塗り込んで就寝中の集中リペアを行う。この毎日の丁寧な積み重ねが、粉吹きや肌荒れ知らずのふっくら柔らかな素肌を育みます。ぜひ本ランキングを参考に、あなたの肌のバリアを力強く支えてくれる運命のセラミドクリームを見つけてみてください。
      </p>
    </section>
  </div>

  <footer class="site-footer">
    <div class="footer-inner">
      <h3 class="footer-heading">❄️ 冬コスメ徹底比較ラボ 全カテゴリ一覧</h3>
      <div class="footer-links-grid" id="footer-links">
        <!-- 内部リンク更新スクリプトにより自動展開 -->
      </div>
      <p class="footer-copy">© 2026 冬コスメ徹底比較ラボ. All rights reserved.</p>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-ceramide-cream.html", "w", encoding="utf-8") as f:
    f.write(full_html.strip())

print("Successfully generated winter-ceramide-cream.html")
