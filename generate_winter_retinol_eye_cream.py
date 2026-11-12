import json
import re

with open("fetched_3new_pdrn_retinol_panthenol.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_retinol_eye_cream"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🥇 日本で唯一の純粋レチノールシワ改善！真冬の深い目尻ジワを根本から押し上げる最高峰",
        "catch": "資生堂が30年以上の研究を経て完成させた医薬部外品の最高峰。熱や光に極めて不安定な『純粋レチノール』を特殊酸素遮断チューブで安定配合。冬の乾燥で折れ曲がった目元角層に自活力とヒアルロン酸を生み出し、ピンとした弾力を蘇らせる",
        "brand_name": "ELIXIR (資生堂 エリクシール)",
        "capacity": "15g (約75回分・医薬部外品)",
        "type": "純粋レチノール配合 薬用シワ改善アイ＆リンクルクリーム",
        "features": "薬用有効成分 純粋レチノール、コラーゲンGL、高密着バリア処方、特殊バックレスチューブ",
        "value": "日本で初めて『シワを改善する』効果が認可された信頼の有効成分。11月・12月の厳しい乾燥で深くなった目尻の笑いジワやまぶたのたるみを、角層奥深くからふっくらと押し戻す",
        "desc_p1": "冬の冷気と暖房にさらされると、皮膚の厚さがわずか0.02mmしかない目元の水分量は急激に低下。目元を動かすたびに角層の柔軟性が失われ、細かい線がやがて深い定着ジワへと進行します。エリクシールのレチノパワーリンクルクリームは、日本で唯一シワ改善効能を認められた『純粋レチノール』を配合。表皮で水分を抱え込むヒアルロン酸を生み出し、水分量を増やすことで硬くなった角層を内側から押し上げます。",
        "desc_p2": "クリームは体温でスッと伸びながらも、皮膚の薄い目元にとどまる絶妙な密着バーム処方を採用。酸素の侵入を一切許さない特殊なノズル機構により、最後の1滴までレチノールの高活性を維持します。朝晩米粒大を目元になじませるだけで、夕方のファンデーションの乾燥割れや目尻のちりめんジワが目に見えて目立たなくなります。",
        "target": "目尻の笑いジワや目の下の細かな乾燥ジワが定着してきた方、ドラッグストアやデパートで本気のシワ改善を始めたい方、確固たる医学的根拠のあるアイクリームを選びたい方",
        "point": "朝晩のお手入れの最後に使用します。小さなパール粒1コ分を指先にとり、目や口のまわりなどシワが気になる部分にやさしくなじませます。朝使用する場合は、レチノールの効果を守るために必ず日焼け止めやUV下地を重ねてください。"
    },
    {
        "rank": 2,
        "tag": "💰 プチプラ界の伝説！ピュアレチノール×豆乳発酵液で真冬の目元をふっくら満たす驚異のコスパ",
        "catch": "累計販売数数千万本を突破するなめらか本舗の傑作アイクリーム。高純度ピュアレチノールと豆乳発酵液を濃密クリームに配合し、千円前後の手頃な価格でありながら冬の乾燥くすみとちりめんジワを徹底撃退",
        "brand_name": "サナ なめらか本舗 (常盤薬品工業)",
        "capacity": "20g",
        "type": "ピュアレチノール×豆乳イソフラボン配合 高密着アイクリーム",
        "features": "ピュアレチノール、豆乳発酵液（イソフラボン含有）、ビタミンE誘導体（TPNa®）、密着ポリマー",
        "value": "惜しみなく毎日たっぷりと目元・まぶた・ほうれい線まで塗り込める神コスパ。密着ポリマーが目元にストレッチ膜を張り、ピンとしたハリ感を目元に即時付与",
        "desc_p1": "『アイクリームは高価で続けにくい』という常識を覆したのが、なめらか本舗のリンクルアイクリームNです。滋賀県産大豆たまほまれを使用した濃縮豆乳発酵液に加え、角層への浸透性に優れたピュアレチノールを厳選配合。乾燥によってスカスカになった目元のキメの隙間に、油分と水分を絶妙なバランスで補給します。",
        "desc_p2": "コクのあるテクスチャーが皮膚の上でピタッと密着し、瞬時に保護フィルムを形成。ビタミンE誘導体（TPNa®）が血行不良による青クマやくすみをサポートし、どんよりと暗くなりがちな冬の目元を明るくふっくらとした印象へ導きます。夜にたっぷり厚めに塗って『アイパック』として使うのも贅沢でおすすめです。",
        "target": "初めてアイクリームを使う20代〜30代の方、高価なアイクリームだとケチって少量しか塗れない方、目元だけでなく眉間やほうれい線にも広範囲に塗り込みたい方",
        "point": "スキンケアの最後に、指先に適量をとり、目元の気になる部分にやさしくトントンと叩き込むようになじませます。まぶたのキワからこめかみまで優しく引き上げるように伸ばすと、目元全体のハリ感がさらにアップします。"
    },
    {
        "rank": 3,
        "tag": "🔬 純粋レチノール0.2%高濃度配合！成分主義が生み出した全顔・首元まで使える大容量サイエンスクリーム",
        "catch": "高純度・高濃度原料にこだわる基礎化粧品研究所KISOの本格レチノールクリーム。純粋レチノール原液を0.2%という本格濃度で配合し、目元のちりめんジワから首元の乾燥横ジワまで徹底的にエイジングケア",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "50g (一般的なアイクリームの3倍以上)",
        "type": "純粋レチノール0.2%配合 高濃度エイジングフェイス＆アイクリーム",
        "features": "純粋レチノール（0.2%）、ツボクサエキス、オウゴン根エキス、スクワラン、ホホバ種子油",
        "value": "50gという大容量ボックス。目元・目尻だけでなく、首すじの横ジワやデコルテまで贅沢にレチノール密閉が可能。冬場の全身の小ジワ対策に比類なき満足感",
        "desc_p1": "目元用のアイクリームは通常15g程度で数千円〜1万円以上することが一般的ですが、KISOのスーパーリンクルクリームVAは50gという破格のボリュームを誇ります。主成分には安定化カプセルに内包された純粋レチノールを0.2%の高濃度で配合。角質層のターンオーバーを強力にバックアップし、冬の寒冷で鈍った肌の代謝を押し上げます。",
        "desc_p2": "さらにツボクサエキスをはじめとする7種のオーガニック認証エキスと、オリーブ由来スクワランが贅沢なエモリエントヴェールを形成。高濃度レチノール特有の乾燥や刺激感を植物性バリア成分がしっかりと緩和します。目元の深い悩みはもちろん、年齢が出やすい首元のシワにも惜しみなく塗布できる頼もしさがあります。",
        "target": "目元だけでなく首や額、眉間など顔全体の小ジワを一挙にケアしたい方、成分濃度にこだわったサイエンススキンケアが好きな方、大容量で長く使い続けたい方",
        "point": "夜のお手入れの最後、乳液やクリームの後に適量（パール粒大）を手に取り、目元や首元、気になる部分へ優しく伸ばします。レチノールを初めて使う方は、最初の2週間は2〜3日おきの夜のみ使用し、肌を慣らしていくのがベストです。"
    },
    {
        "rank": 4,
        "tag": "👑 日本初のシワ改善薬用有効成分ニールワン®！好中球エラスターゼを抑制し冬の真皮破壊を食い止める最高峰",
        "catch": "POLAが15年以上の歳月をかけて発見・開発した日本初認可のシワ改善有効成分『ニールワン®（三フッ化イソプロピルオキソプロピルアミノカルボニルピロリジンカルボニルメチルプロピルアミノカルボニルベンゾイルアミノ酢酸Na）』を配合。真冬の乾燥で激化する真皮分解を根本ブロック",
        "brand_name": "POLA (ポーラ)",
        "capacity": "20g (医薬部外品)",
        "type": "薬用有効成分ニールワン®配合 シワ改善集中美容液バーム",
        "features": "有効成分ニールワン®、ICユニット、コンドロイチン硫酸、無水処方高密着バーム",
        "value": "紫外線や乾燥で発生する酵素『好中球エラスターゼ』が真皮のコラーゲンを破壊するのを物理的に阻害。真冬の過酷な環境でも、シワの進行を根本から食い止め跳ね返す",
        "desc_p1": "冬の乾燥は、単に肌表面のカサつきにとどまらず、微小な炎症を引き起こして『好中球エラスターゼ』というコラーゲン分解酵素を過剰に活性化させます。これが真冬にシワが一気に深くなる隠れたメカニズムです。POLAのリンクルショット メディカル セラムは、この好中球エラスターゼの活性を直接阻害する唯一無二の有効成分ニールワン®を配合しています。",
        "desc_p2": "水を含まない完全無水処方で作られており、肌表面の水分をキャッチしてシワの奥深くへと成分が吸い込まれるように浸透。チューブの先端がシワに直接フィットするストレッチヘッド形状になっており、目元やほうれい線、眉間の溝に直接なぞるように塗り込めます。使い続けるほどに、シワの溝が押し上げられていく確かな手応えを感じられます。",
        "target": "すでに深く刻まれてしまった目尻のシワやほうれい線を本気で消したい方、美容医療の手前に最高峰の医薬部外品を投入したい方、本物志向の大人世代",
        "point": "朝晩のローション（化粧水）の後、乳液やクリームの前に使用します。シワをなぞるようにチューブから直接適量を出し、シワに対して直角（下から上、内から外）へ指先で優しく引き伸ばすように馴染ませてください。"
    },
    {
        "rank": 5,
        "tag": "🌏 韓国売上No.1国民的アイクリーム！超微細ナノカプセル化で顔全体に塗れる極上リッチフォーミュラ",
        "catch": "エステ発想スキンケアAHCが誇る、韓国で数秒に1本売れる国民的アイクリーム。毛穴の1/500という超微細ナノエマルジョン技術により、レチノールとヒト同一型コラーゲンを目元だけでなく顔全体に一瞬で吸い込ませる",
        "brand_name": "AHC (エーエイチシー)",
        "capacity": "30mL (アイクリーム フォー フェイス)",
        "type": "ナノカプセルレチノール×ヒト同一型コラーゲン配合 全顔アイクリーム",
        "features": "ナノカプセルレチノール、ヒト型コラーゲン、ペプチド複合体、マイクロエマルジョン処方",
        "value": "『アイクリームの贅沢な濃密栄養を顔全体に塗る』という贅沢設計。30mL入りで目元はもちろん、おでこや首元までシルクのような滑らかなツヤ膜で包み込む",
        "desc_p1": "エステサロンの集中アイケアプログラムを自宅で手軽に体験できるように設計されたのがAHCの『テン レボリューション リアル アイクリーム フォー フェイス』です。毛穴の何百分の一という極小サイズにナノ微細化されたエマルジョンが、寒さで硬くなった冬の角層にも驚くほど滑らかに溶け込みます。",
        "desc_p2": "成分にはレチノール誘導体をはじめ、ヒトの生体構造と同一のコラーゲン、複数のエイジングケアペプチドを贅沢にブレンド。テクスチャーはこってりとしたリッチ感がありながら、伸ばすと驚くほど軽やかに馴染んでベタつきを残しません。メイク前に薄く仕込むと、冬の目元コンシーラーのひび割れやヨレを完璧に防いでくれます。",
        "target": "顔全体に贅沢にアイクリームを塗り広げたい方、ベタつかないのに長時間乾かない上質なテクスチャーを求める方、韓国コスメの先端リフティング技術を体感したい方",
        "point": "化粧水や美容液の後、目元やほうれい線にポンポンと置くように馴染ませます。さらに乾燥が気になる日は、全顔にクリーム代わりに薄く伸ばしてハンドプレスすると、翌朝エステ帰りのようなモチモチのツヤ肌に仕上がります。"
    },
    {
        "rank": 6,
        "tag": "🌺 済州島の極寒を生き抜く寒蘭の生命力！植物性レチノール類似作用で敏感な目元を優しくリペア",
        "catch": "自然派韓国コスメInnisfree（イニスフリー）のロングセラーオーキッドシリーズ。雪の中でも花を咲かせる済州島の寒蘭から抽出したオーキッドエリクサー2.0™が、薄く敏感な冬の目元に弾力と濃密な潤いを供給",
        "brand_name": "Innisfree (イニスフリー)",
        "capacity": "30mL",
        "type": "寒蘭エキス×植物性エイジングケア成分配合 高密着アイクリーム",
        "features": "オーキッドエリクサー2.0™、ヒアルロン酸、シアバター、アデノシン",
        "value": "強いレチノールで皮剥けや赤みが出やすい超敏感肌でも安心。植物由来の抗酸化・弾力サポート成分が、寒冷による目元の乾燥小ジワを穏やかにふっくら修復",
        "desc_p1": "レチノールは高いシワ改善効果を持つ一方で、肌質によっては初期の使用で乾燥や皮剥け（A反応）を起こすことがあります。イニスフリーの済州オーキッドアイクリームは、雪が積もる厳しい冬の寒さの中で花を咲かせる寒蘭（オーキッド）の驚異的な生命力に着目。デリケートな目元をいたわりながら、確かなハリと潤いを与えます。",
        "desc_p2": "テクスチャーはまろやかでバターのように体温でとろける高密着クリーム。シアバター由来のエモリエント成分が目元の薄い皮膚に薄膜シールドを形成し、外気乾燥や摩擦から長時間守り抜きます。ほんのり上品なオーキッドの香りに包まれながら、心まで癒されるリラックスしたアイケアを楽しめます。",
        "target": "化学的な高濃度レチノールだと刺激を感じやすい敏感肌の方、自然由来成分で優しく目元の乾燥小ジワをケアしたい方、まぶたの乾燥や重みが気になる方",
        "point": "スキンケアの最後、適量を指先にとり、目頭から目尻に向かって優しくマッサージするように伸ばします。目頭や眉頭の下にあるツボを軽くプッシュしながら馴染ませると、目元の血行が促されてクマの改善にも効果的です。"
    },
    {
        "rank": 7,
        "tag": "✨ シワ改善×美白のW有効成分！ナイアシンアミドとピュアレチノールで冬の目元の影とくすみを一掃",
        "catch": "常盤薬品工業の医薬部外品アイクリーム。シワ改善と美白の有効成分ナイアシンアミドにピュアレチノールを融合。冬の寒さで血行が悪くなり、乾燥小ジワとともに影が落ちる目元をパッと明るくふっくらリフト",
        "brand_name": "サナ なめらか本舗 (常盤薬品工業)",
        "capacity": "20g (医薬部外品)",
        "type": "ナイアシンアミド×ピュアレチノール配合 薬用美白＆シワ改善アイクリーム",
        "features": "有効成分ナイアシンアミド、ピュアレチノール、豆乳発酵液、高密着リペア処方",
        "value": "千円以下で医薬部外品のシワ改善とメラニン生成抑制（美白）を同時達成。冬の乾燥ジワだけでなく、摩擦や血行不良による目元の色素沈着・くすみまで一網打尽",
        "desc_p1": "冬の目元は、乾燥による『ちりめんジワ』と、血行不良やアイメイクの摩擦による『色素沈着・くすみ』が同時に重なり、顔全体に暗い影を落とします。なめらか本舗の『薬用リンクルアイクリーム ホワイト』は、真皮コラーゲンの産生を促してシワを改善し、同時にメラニンの蓄積を抑える有効成分ナイアシンアミドを配合しています。",
        "desc_p2": "さらにブランドの代名詞であるピュアレチノールと豆乳発酵液が加わり、角層内部の水分量を強力にキープ。密着度の高いテクスチャーが目元に吸い付き、乾燥による小ジワを目立たなくさせます。朝晩惜しみなく使える価格帯でありながら、シワとシミの予防を同時に行える、冬の心強い味方です。",
        "target": "目元の乾燥ジワと茶クマ・くすみを同時にケアしたい方、プチプラで医薬部外品の本格処方を手に入れたい方、毎日のアイケアを習慣にしたい方",
        "point": "朝晩の洗顔後、化粧水や乳液で肌を整えた後に使用します。目頭から目尻にかけて、薬指を使って皮膚を引っ張らないように優しくトントンとなじませてください。ほうれい線や眉間への使用もおすすめです。"
    },
    {
        "rank": 8,
        "tag": "❤️ アスタキサンチンの強力抗酸化×濃密ホールド膜！冬のゆるんだまぶたを目元専用リッチクリームで引き上げ",
        "catch": "富士フイルムの写真技術とナノ皮膚科学を結集したアスタリフト。高濃度ナノアスタキサンチンとリコピンの赤い力に加え、まぶたの皮膚構造に合わせた密着ホールド膜が冬の乾燥によるたるみと目尻の溝を力強く保護",
        "brand_name": "ASTALIFT (富士フイルム アスタリフト)",
        "capacity": "15g",
        "type": "高濃度ナノアスタキサンチン×リコピン配合 濃厚目元リフトクリーム",
        "features": "ナノアスタキサンチン、ナノリコピン、3種のコラーゲン、メドウフォーム油、目元ホールドポリマー",
        "value": "ビタミンEの約1000倍の抗酸化力を持つアスタキサンチンが、冬の乾燥と酸化ストレスから目元のデリケートな毛細血管とコラーゲンを強力ガード",
        "desc_p1": "冬の暖房や冷たい風は、皮膚内部で活性酸素を発生させ、目元のコラーゲン繊維を劣化させます。アスタリフトのアクティブアイクリームSは、天然の赤い美肌成分アスタキサンチンをナノカプセル化して配合。角層深部までスムーズに浸透し、紫外線や乾燥ダメージを速やかに中和します。",
        "desc_p2": "テクスチャーは濃厚でコクがあり、指先にとるとしっかりとした弾力を感じられます。肌に乗せると体温で溶け出し、目元をキュッと引き締める『目元ホールド膜』を形成。夕方になるとまぶたが重く下がってくる方や、目尻の乾燥ジワが深くなる冬の過酷な環境でも、ピンとした若々しい目元を長時間キープします。",
        "target": "夕方になるとまぶたが重くたるむ方、PCやスマホ作業が多く目元の疲労・乾燥が激しい方、赤いアスタキサンチンの圧倒的なハリ感を実感したい方",
        "point": "スキンケアの最後に、米粒大を指先にとり、目頭から目尻、こめかみに向かって引き上げるように優しく伸ばします。下まぶただけでなく、上まぶたの骨のキワまで丁寧に塗り広げることで、目元全体の開きやすさがアップします。"
    },
    {
        "rank": 9,
        "tag": "🛡️ 医薬部外品消炎剤×セラミド機能カプセル！何を使ってもヒリつく冬の超敏感目元を濃密リペア",
        "catch": "乾燥性敏感肌研究のトップブランドCurel（キュレル）の目元集中クリーム。皮膚が薄く皮脂腺が極端に少ない目元のために開発された『モイストリペア処方』が、ひび割れそうな粉吹きまぶたにセラミドを満たし長時間密着",
        "brand_name": "Curel (キュレル / 花王)",
        "capacity": "25g (医薬部外品)",
        "type": "消炎有効成分×セラミド機能成分配合 低刺激薬用アイクリーム",
        "features": "消炎剤有効成分（アラントイン）、セラミド機能カプセル、ユーカリエキス、モイストリペア高密着ヴェール",
        "value": "冬の乾燥でアイシャドウが粉を吹き、化粧水すらピリつく目元を救済。こってりとした濃厚クリームが薄いまぶたに留まり、セラミドを補給し続けてバリアを再建",
        "desc_p1": "冬場、目元は瞬きによる絶え間ない運動と乾燥のせいで、皮膚炎や皮剥けを起こしやすい極めて繊細なエリアです。キュレルのモイストリペア アイクリームは、抗炎症有効成分アラントインを配合し、目元の赤みやヒリつきの火種を優しく鎮静。刺激を感じやすい季節でも安心して投入できます。",
        "desc_p2": "さらに微細カプセル化されたセラミド機能成分が、スカスカになった角層細胞の間を埋め尽くし、水分が外へ逃げるのをブロック。固めのこっくりとしたテクスチャーが皮膚表面に留まり、瞬きを繰り返してもヨレずに潤いのバリア膜をキープします。目元が荒れてメイクができない冬のレスキューケアとして必携の1本です。",
        "target": "目元が乾燥して粉を吹く・ピリピリしみる方、低刺激で無香料の安心できるアイクリームを探している方、敏感肌でレチノールの刺激が不安な方",
        "point": "化粧水や乳液の後に使用します。適量（片方の目元で直径約5mm）を指先にとり、目のまわりに優しくなじませます。特に乾燥が気になる目尻やまぶたには、擦らずに押さえるように重ね付けしてください。"
    },
    {
        "rank": 10,
        "tag": "🏷️ 千円以下の奇跡！有効成分ナイアシンアミド配合でシワ改善とシミ予防を両立する神コスパクリーム",
        "catch": "高品質プチプラの代名詞セザンヌが送り出した医薬部外品の傑作アイクリーム。有効成分ナイアシンアミドを配合し、シワ改善と美白ケアを千円以下の衝撃価格で提供。冬のデイリーアイケアに革命を起こす1本",
        "brand_name": "CEZANNE (セザンヌ)",
        "capacity": "20g (医薬部外品)",
        "type": "有効成分ナイアシンアミド配合 薬用シワ改善＆美白アイクリーム",
        "features": "有効成分ナイアシンアミド、レチノール誘導体、加水分解コラーゲン、ヒアルロン酸、高保湿シアバター",
        "value": "ドラッグストアで900円台で買える圧倒的低価格。学生から大人まで、惜しみなく毎朝晩のスキンケアに組み込んで、冬の目元・ほうれい線の乾燥ジワを未然にブロック",
        "desc_p1": "アイケアは高額なアイテムが多く、継続するのが難しいと感じている方に最適なのがセザンヌの『リンクルホワイトアイクリーム』です。医薬部外品の有効成分ナイアシンアミドが真皮に働きかけてコラーゲン産生を促進し、すでに気になり始めた小ジワを改善。同時にメラニンの生成を抑えてシミやくすみを予防します。",
        "desc_p2": "テクスチャーはみずみずしく伸び広がりながらも、シアバター配合によりしっかりとした潤いヴェールが持続。メイク前に使ってもファンデーションのヨレを引き起こさず、日中のエアコン乾燥から目元をガードします。この価格帯でありながら、レチノール誘導体やコラーゲンも贅沢に含まれており、コスパ重視派の冬の必需品です。",
        "target": "千円以下で本格的なシワ改善アイクリームを試したい方、毎朝のメイク前に使える軽やかで高保湿なアイクリームが欲しい方、ほうれい線予防を始めたい方",
        "point": "スキンケアの最後に、米粒大を手にとり、目元やほうれい線になじませます。朝のメイク前に使う場合は、薄く塗り広げて1〜2分置いて肌になじんでからベースメイクに進むと、ファンデーションのヨレを防げます。"
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
        "q": "なぜ冬になると目元や目尻に急に『ちりめんジワ』が増えるのですか？",
        "a": "目元の皮膚は頬の約3分の1（わずか0.02mm）の薄さしかなく、皮脂を分泌する皮脂腺がほとんど存在しません。そのため、11月〜12月の外気湿度の低下とエアコン暖房の温風を直接受けると、角層の水分が一瞬で蒸発してしまいます。さらに人間は1日に約1万5,000回から2万回のまばたきをしているため、柔軟性を失った乾いた目元皮膚が折り紙のように何度も折れ曲がり、細かなちりめんジワが急激に刻まれてしまうのです。"
    },
    {
        "q": "レチノール入りアイクリームは、冬の朝のメイク前に使っても大丈夫ですか？",
        "a": "純粋レチノール配合の製品（エリクシールなど）を朝使用する場合は、必ず日焼け止めやSPF・PA表示のある化粧下地を重ねて紫外線を防御することが必須条件です。レチノールは紫外線を受けると構造が壊れやすく、また肌の感受性が高まるためです。一方、セザンヌやなめらか本舗などのナイアシンアミド主体の製品やマイルドなレチノール誘導体製品は、朝のメイク前でも比較的安心して使用できます。朝に仕込むことで、夕方の目元ファンデーションの乾燥割れを予防できます。"
    },
    {
        "q": "レチノールアイクリームを塗るとピリピリしたり皮剥けしたり（A反応）しませんか？",
        "a": "レチノールを初めて使う方や肌が過敏になっている冬場は、細胞のターンオーバーが急激に活性化することで、一時的な赤み・乾燥・皮剥け（レチノイド反応/A反応）が起きることがあります。これを防ぐためには、『最初の2週間は2〜3日おきの夜のみ使用』『パール粒半分程度の少量から始める』『化粧水や乳液でしっかり保湿した後に重ねる（バッファリング処置）』というステップを踏むことが重要です。肌が慣れてくれば毎晩快適に使用できるようになります。"
    },
    {
        "q": "アイクリームは全顔用の保湿クリームで代用しても同じ効果がありますか？",
        "a": "全顔用のクリームだけでは目元のシワ対策としては不十分です。目元は皮膚が非常に薄く常に動いているため、全顔用のサラサラした乳液やクリームではすぐに蒸発・摩擦で消失してしまいます。目元専用アイクリームは、まばたきに耐えうる『高密着ポリマー』や『厚みのある油膜エモリエント基剤』で処方設計されており、成分が流動せず薄い皮膚の上に何時間も留まるように作られています。"
    },
    {
        "q": "アイクリームを塗る際、効果を高める正しい塗り方はありますか？",
        "a": "最も力が入りにくい『薬指の腹』を使い、皮膚を絶対に強く引っ張ったり擦ったりしないことが最大の鉄則です。米粒大をとり、目頭から目尻に向かって軽くトントンとピアノを弾くように優しくスタンプ塗りします。さらに、シワの溝を反対側の指で軽く広げながら、溝の奥へクリームを埋め込むように馴染ませると浸透率が大幅に向上します。"
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
            "headline": "保湿力の強さで肌乾燥とさようなら！純粋レチノールの角層深部ターンオーバー促進と密着リペアバーム処方で真冬の目元ちりめんジワをふっくら伸ばす保湿力高めレチノールアイクリームランク10",
            "description": "11月・12月の寒冷乾燥・エアコン暖房・まばたき摩擦による目元の小ジワ・ちりめんジワ・たるみを徹底撃退！エリクシール、ポーラ、なめらか本舗、KISO、AHC、アスタリフトまで最新実勢価格・口コミ・科学的シワ改善メカニズムを網羅。",
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
            "name": "真冬の高保湿レチノールアイクリームおすすめランキング10選",
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
                    "name": "高保湿レチノールアイクリーム特集",
                    "item": "https://lumi-cosme.vercel.app/winter-retinol-eye-cream"
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
            <span class="value-title">💡 11-12月の目元乾燥対策・即効価値</span>
            <p>{p['value']}</p>
          </div>
        </div>
      </div>
      <div class="product-desc-box">
        <h4>👁️ 美容科学＆テクスチャー詳細解説</h4>
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
  <title>保湿力の強さで肌乾燥とさようなら！純粋レチノールの角層深部ターンオーバー促進と密着リペアバーム処方で真冬の目元ちりめんジワをふっくら伸ばす保湿力高めレチノールアイクリームランク10 | LUMI COSMETICS LAB</title>
  <meta name="description" content="11月・12月の寒冷乾燥・エアコン暖房・まばたき摩擦による目元の小ジワ・ちりめんジワ・たるみを徹底撃退！エリクシール、ポーラ、なめらか本舗、KISO、AHC、アスタリフトまで最新実勢価格・口コミ・科学的シワ改善メカニズムを網羅。">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-retinol-eye-cream">
  <link rel="icon" href="/favicon.jpg">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！純粋レチノールの角層深部ターンオーバー促進と密着リペアバーム処方で真冬の目元ちりめんジワをふっくら伸ばす保湿力高めレチノールアイクリームランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥・エアコン暖房・まばたき摩擦による目元の小ジワ・ちりめんジワ・たるみを徹底撃退！エリクシール、ポーラ、なめらか本舗、KISO、AHC、アスタリフトまで最新実勢価格・口コミ・科学的シワ改善メカニズムを網羅。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-retinol-eye-cream">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="LUMI COSMETICS LAB">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！純粋レチノールの角層深部ターンオーバー促進と密着リペアバーム処方で真冬の目元ちりめんジワをふっくら伸ばす保湿力高めレチノールアイクリームランク10">
  <meta name="twitter:description" content="11月・12月の寒冷乾燥・エアコン暖房・まばたき摩擦による目元の小ジワ・ちりめんジワ・たるみを徹底撃退！エリクシール、ポーラ、なめらか本舗、KISO、AHC、アスタリフトまで最新実勢価格・口コミ・科学的シワ改善メカニズムを網羅。">
  <meta name="twitter:image" content="{items[0]['image_url']}">
  <script type="application/ld+json">
  {json.dumps(structured_data, ensure_ascii=False, indent=2)}
  </script>
  <style>
    :root {{
      --primary: #9333ea;
      --primary-dark: #7e22ce;
      --accent: #e11d48;
      --bg: #faf5ff;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #f3e8ff;
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
      background: linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 100%);
      border: 1px solid #d8b4fe;
      border-radius: var(--radius);
      padding: 40px 32px;
      margin-bottom: 40px;
    }}
    .hero-tag {{
      display: inline-block;
      background: #9333ea;
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
      color: #6b21a8;
      text-decoration: none;
      font-size: 0.92rem;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: #9333ea;
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
      background: #faf5ff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
    }}
    .science-card h4 {{
      font-size: 1.05rem;
      color: #7e22ce;
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
      background: #9333ea;
      color: #ffffff;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 8px;
    }}
    .product-tag {{
      background: #fdf4ff;
      color: #86198f;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 8px;
      border: 1px solid #f5d0fe;
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
      background: #fdf4ff;
      border: 1px solid #f5d0fe;
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 0.9rem;
      color: #701a75;
    }}
    .value-title {{
      font-weight: 700;
      display: block;
      margin-bottom: 4px;
    }}
    .product-desc-box {{
      background: #faf5ff;
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
      background: #f3e8ff;
      font-weight: 700;
      color: #581c87;
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
      background: linear-gradient(135deg, #9333ea 0%, #7e22ce 100%);
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
      color: #7e22ce;
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
      background: #faf5ff;
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
      color: #c084fc;
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
    <a href="/">ホーム</a> &gt; <span>高保湿レチノールアイクリーム特集</span>
  </div>

  <main>
    <div class="hero-section">
      <span class="hero-tag">👁️ 11月・12月 目元・まぶた・目尻集中リペア</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！純粋レチノールの角層深部ターンオーバー促進と密着リペアバーム処方で真冬の目元ちりめんジワをふっくら伸ばす保湿力高めレチノールアイクリームランク10</h1>
      <p class="hero-desc">
        気温が10℃を下回り、暖房の温風が直接顔に当たり始める11月から12月。最も過酷なダメージを受けるのが、皮膚の厚さがわずか0.02mmしかなく皮脂腺がほとんど存在しない『目元』です。日中のエアコン乾燥と約2万回のまばたき運動により、柔軟性を失った薄い皮膚は瞬く間にちりめんジワや深い目尻ジワへと定着してしまいます。本記事では、医薬部外品認可の純粋レチノールをはじめ、POLAニールワン®や高濃度ペプチドを配合した最高峰のアイクリーム10選を徹底検証しました。
      </p>
    </div>

    <div class="toc-box">
      <div class="toc-title">📑 目次・記事ナビゲーション</div>
      <ul class="toc-list">
        <li><a href="#science-guide">1. なぜ冬に目元のシワが急増するのか？皮膚科学メカニズム</a></li>
        <li><a href="#rank-1">第1位: エリクシール レチノパワー リンクルクリーム S</a></li>
        <li><a href="#rank-2">第2位: サナ なめらか本舗 リンクルアイクリーム N</a></li>
        <li><a href="#rank-3">第3位: KISO スーパーリンクルクリーム VA</a></li>
        <li><a href="#rank-4">第4位: POLA リンクルショット メディカル セラム N</a></li>
        <li><a href="#rank-5">第5位: AHC テン レボリューション リアル アイクリーム</a></li>
        <li><a href="#rank-6">第6位: イニスフリー 済州オーキッド アイクリーム</a></li>
        <li><a href="#rank-7">第7位: サナ なめらか本舗 薬用リンクルアイクリーム ホワイト</a></li>
        <li><a href="#rank-8">第8位: アスタリフト アイクリーム S</a></li>
        <li><a href="#rank-9">第9位: キュレル 潤浸保湿 モイストリペア アイクリーム</a></li>
        <li><a href="#rank-10">第10位: セザンヌ リンクルホワイトアイクリーム</a></li>
        <li><a href="#selection-matrix">2. 成分・テクスチャー別：冬のアイクリーム選び方マトリクス</a></li>
        <li><a href="#faq-section">3. よくある質問・Q&Aセクション</a></li>
      </ul>
    </div>

    <div class="science-box" id="science-guide">
      <h3>🔬 目元の皮膚は『ゆで卵の薄皮』同然！冬の乾燥崩壊とレチノールの作用原理</h3>
      <p>
        人間の顔の中で最も薄いのが目の周りの皮膚です。頬の皮膚の約3分の1という極薄構造でありながら、皮脂腺や汗腺が極めて少ないため、自前の皮脂膜を作ることができません。11月〜12月の湿度急低下は、目元からほぼすべての水分を奪い去ります。
      </p>
      <div class="science-grid">
        <div class="science-card">
          <h4>🧪 表皮ヒアルロン酸の産生促進</h4>
          <p>純粋レチノールは表皮細胞に直接働きかけ、自前の水分保持成分であるヒアルロン酸の合成を劇的に促進。水分を含んだ細胞がふっくらと膨らむことで、表面の小ジワを平坦化します。</p>
        </div>
        <div class="science-card">
          <h4>🧱 真皮コラーゲンの分解抑制</h4>
          <p>冬の乾燥と微小炎症は、コラーゲンを破壊する好中球エラスターゼを分泌させます。ニールワン®やレチノール誘導体は、この破壊シグナルを遮断し、ハリを支える真皮網目を守り抜きます。</p>
        </div>
        <div class="science-card">
          <h4>🛡️ まばたきに負けない密着バーム処方</h4>
          <p>通常のクリームでは瞬きの摩擦ですぐに擦れ落ちてしまいますが、高機能アイクリームは高粘着ポリマーとエモリエント成分を配合。薄膜のラッピングシールドとなって一日中目元を完全密閉します。</p>
        </div>
      </div>
    </div>

    <div class="products-section">
      {product_cards_html}
    </div>

    <div class="summary-box" id="selection-matrix">
      <h3>📊 成分・テクスチャー別：冬のアイクリーム選び方マトリクス</h3>
      <p>10製品の主要有効成分、配合タイプ、価格帯、推奨される肌悩みを一覧で比較しました。ご自身の目元の悩みの深さや肌の敏感度に合わせてお選びください。</p>
      <table class="summary-table">
        <thead>
          <tr>
            <th>順位 / 製品名</th>
            <th>主要シワ改善・保湿成分</th>
            <th>処方タイプ</th>
            <th>こんな目元のお悩みにおすすめ</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>第1位: エリクシール</td>
            <td>薬用 純粋レチノール</td>
            <td>医薬部外品・濃厚バーム</td>
            <td>すでに定着した深い目尻ジワ・笑いジワ</td>
          </tr>
          <tr>
            <td>第2位: なめらか本舗 リンクル</td>
            <td>ピュアレチノール×豆乳発酵液</td>
            <td>高密着プチプラクリーム</td>
            <td>20代〜30代の乾燥小ジワ予防・高コスパ</td>
          </tr>
          <tr>
            <td>第3位: KISO</td>
            <td>純粋レチノール0.2%高濃度</td>
            <td>大容量50gサイエンスクリーム</td>
            <td>目元・眉間・首元まで全顔に惜しみなく使用</td>
          </tr>
          <tr>
            <td>第4位: POLA リンクルショット</td>
            <td>有効成分 ニールワン®</td>
            <td>完全無水・ストレッチバーム</td>
            <td>本気のシワ改善・深化した目袋・ほうれい線</td>
          </tr>
          <tr>
            <td>第5位: AHC</td>
            <td>ナノレチノール×ヒト型コラーゲン</td>
            <td>全顔用超微細エマルジョン</td>
            <td>目元だけでなく顔全体のたるみ・毛穴ケア</td>
          </tr>
          <tr>
            <td>第6位: イニスフリー</td>
            <td>オーキッドエリクサー2.0™</td>
            <td>寒蘭植物性リッチクリーム</td>
            <td>レチノールの刺激が不安な敏感肌・まぶた乾燥</td>
          </tr>
          <tr>
            <td>第7位: なめらか本舗 ホワイト</td>
            <td>ナイアシンアミド×ピュアレチノール</td>
            <td>医薬部外品・美白＆シワ改善</td>
            <td>乾燥小ジワと茶クマ・目元のくすみ両方</td>
          </tr>
          <tr>
            <td>第8位: アスタリフト</td>
            <td>ナノアスタキサンチン×リコピン</td>
            <td>赤い濃厚ホールドクリーム</td>
            <td>夕方のまぶたのたるみ・重み・眼精疲労乾燥</td>
          </tr>
          <tr>
            <td>第9位: キュレル</td>
            <td>消炎剤（アラントイン）×セラミド</td>
            <td>医薬部外品・低刺激密着処方</td>
            <td>粉吹き・ピリピリしみる超敏感な目元</td>
          </tr>
          <tr>
            <td>第10位: セザンヌ</td>
            <td>ナイアシンアミド×レチノール誘導体</td>
            <td>千円以下の医薬部外品</td>
            <td>朝のメイク前に使える軽やかさ・神コスパ</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="summary-box" id="faq-section">
      <h3>❓ 高保湿レチノールアイクリームに関するよくある質問（FAQ）</h3>
      {faq_html}
    </div>

    <div class="hub-link-banner">
      <div>
        <h3 style="font-size:1.3rem;margin-bottom:8px;">👁️ 冬のアイケア＆目元集中美容液 総合ハブ</h3>
        <p style="font-size:0.95rem;opacity:0.95;">目元用美容液、アイパッチ、ホットアイマスクまで、真冬の繊細な目元を守り抜く総合特集はこちらからご覧いただけます。</p>
      </div>
      <a href="/winter-eye-cream" class="hub-link-btn">アイケア特集トップへ →</a>
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

with open("winter-retinol-eye-cream.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-retinol-eye-cream.html!")
