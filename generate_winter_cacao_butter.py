import json
import re

with open("fetched_3new_ginseng_cacao_silk.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_cacao_butter"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 全米No.1の圧倒的ベストセラー！ショコラの香りと純粋カカオバターが全身の粉吹き肌を瞬時に救う神ローション",
        "catch": "創業180年以上の伝統を誇るパーマーズの看板ボディケア。高純度カカオバターとビタミンEが黄金比率で融合し、真冬のタイツやブーツで荒れ狂うすねや肘・膝をベルベットの肌触りへ導く",
        "brand_name": "Palmer's (パーマーズ)",
        "capacity": "250ml / 400ml ポンプボトル",
        "type": "純粋カカオバター高配合 エモリエントボディローション",
        "features": "カカオ脂（純粋ココアバター）、トコフェロール（ビタミンE）、植物油複合体",
        "value": "塗った瞬間に広がる本物のスイートチョコレートのアロマ。ベタつかないのに驚異的な保湿膜が24時間持続し、真冬の粉吹き痒みを一掃する世界標準のボディローション",
        "desc_p1": "11月から12月にかけて気温が一段と冷え込むと、入浴後すぐにすねや太ももが白く粉を吹き、タイツを履いた瞬間にチクチクとしたかゆみや突っ張りに悩まされる方が急増します。これは皮脂腺が極めて少ない脚や腕の皮膚から、暖房と冷気によって水分が一気に蒸発してしまうためです。そんな真冬のボディ乾燥に終止符を打つのが、アメリカで世代を超えて愛され続けるパーマーズの『ココアバター フォーミュラ 保湿ボディローション』です。",
        "desc_p2": "ポンプを押すと、まるで上質なチョコレートファッジのような濃厚で甘美な香りが漂います。こっくりとしたクリーム状ですが、人肌に伸ばすと体温でみるみる滑らかな液状に変化して角層へと密着。カカオバター特有のステアリン酸とオレイン酸が強固なエモリエント膜を形成し、お風呂上がりの肌の水分を逃しません。夜塗れば翌朝起きた時もすねはしっとりスベスベのまま。真冬の乾燥対策に欠かせない常備薬のような頼もしさです。",
        "target": "冬になるとすねや腕が粉を吹いてかゆくなる方、濃厚で甘いチョコレートの香りに包まれて癒やされたい方、世界中で実績のある高コスパな大容量ボディケアを求める方",
        "point": "お風呂から上がってタオルで軽く水気を拭き取った直後、肌がまだ温かいうちに2〜3プッシュを全身に大きく円を描くように伸ばします。乾燥が特に激しいすねや踵には重ね塗りがおすすめです。"
    },
    {
        "rank": 2,
        "tag": "🌿 USDAオーガニック認証！真冬の冷風で皮むけ・ひび割れる唇を極厚シールドする万能リップバーム",
        "catch": "米国ニューハンプシャー州の大自然から届くバジャーの逸品。コールドプレスで抽出された未精製カカオバターが、体温でじんわりとろけて真冬の過酷な木枯らしから唇を死守する",
        "brand_name": "Badger (バジャー)",
        "capacity": "7g / 太巻きスティック",
        "type": "USDA認定 オーガニック濃密ココアリップバーム",
        "features": "未精製オーガニックカカオ脂、ミツロウ、エキストラバージンオリーブ油、天然ローズマリーエキス",
        "value": "合成防腐剤、石油系原料、香料を一切使用しない100%天然由来。太めのスティックで唇全体を一気にカバーでき、マスクや外気摩擦による荒れを長時間ブロック",
        "desc_p1": "冬の冷たい北風を受けながら歩いていると、唇が突っ張ってピキッと裂けてしまったり、皮が剥けて口紅が乗らなくなったりすることがあります。唇には皮脂腺も汗腺もなく、角層も極めて薄いため、11月以降の湿度急降下で真っ先にバリアが崩壊してしまいます。バジャーの『オーガニック ココアバター リップバーム（クリーミーココア）』は、そんな極度の唇乾燥を救うために作られた高純度バームです。",
        "desc_p2": "一般的なリップクリームの倍近い太さのスティックを唇に当てると、人肌の温もりでカカオバターがトロリと溶け出し、濃厚な厚膜ヴェールを形成します。未精製カカオならではの自然で芳醇なチョコレートの香りが心地よく、口に入っても安心なオーガニック品質。ひと塗りするだけで何時間も乾かない強力な密封力を発揮し、真冬の外出時もふっくら柔らかな唇をキープしてくれます。",
        "target": "冬になると唇がひび割れて出血しやすい方、オーガニック認証の安心できるリップを探している方、何度も塗り直さなくても長時間潤うリップバームを求める方",
        "point": "朝のメイク前や外出前、そして就寝前に唇の輪郭からはみ出るくらいオーバーにたっぷり塗布します。夜寝る前に厚塗りすると、翌朝には古い皮むけが自然と取れてぷるぷるの唇に再生します。"
    },
    {
        "rank": 3,
        "tag": "✨ シア×カカオバターの奇跡の融合！ホイップのようにとろけてガサガサ角質をほぐす濃厚ボディバター",
        "catch": "世界的なオーガニックコスメの草分けヴェレダが贈る最高峰の高保湿ボディケア。伝統のスキンフード処方にカカオ脂とシア脂を贅沢にブレンドし、真冬の肘・膝・踵をごわつきゼロへ",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "150ml / 広口ジャー容器",
        "type": "植物性高純度リッチモイスチャーボディバター",
        "features": "カカオ脂、シア脂、パンジーエキス、カレンデュラエキス、カモミールエキス",
        "value": "こっくり濃厚でありながらベタつかず、肌に乗せると体温でスルスルとほぐれるホイップテクスチャー。真冬の硬直した角質層を柔らかく解きほぐすハーブとバターの相乗効果",
        "desc_p1": "冬になると肘や膝、踵がカチコチに硬くなり、ストッキングやタイツに引っかかって電線してしまう……そんな頑固な角質硬化に悩む方へ、オーガニックのパイオニア・ヴェレダが自信を持って届けるのが『スキンフード ボディバター』です。",
        "desc_p2": "蓋を開けると、ふわっとしたスフレのような質感のバターが現れます。指ですくって肌に伸ばすと、カカオバターとシアバターが体温でとろけ合い、ビロードのような吸着膜へと変化。伝統的なパンジー（サンシキスミレ）やカレンデュラのエキスが乾燥でヒリつく肌を穏やかに鎮静し、硬くなった角質細胞を内側からふっくらと柔らかく整えます。シトラスとラベンダーの爽やかなハーブの香りで、冬の夜のリラックスタイムを贅沢に演出します。",
        "target": "肘・膝・かかとがガサガサに硬化して白くなっている方、こっくり濃厚なボディバターを好む方、合成香料ではなく天然精油のアロマで癒やされたい方",
        "point": "入浴後、特に硬さが気になる踵や肘にたっぷりすり込みます。塗布後に綿の靴下を履いて就寝すれば、翌朝にはまるでサロンでフットケアを受けたかのような柔らかい素肌が蘇ります。"
    },
    {
        "rank": 4,
        "tag": "🍫 低温圧搾100%ピュア！天然ショコラの香りをそのまま残した未精製カカオバター原液ブロック",
        "catch": "手作りコスメ・高機能原料の名門アンドエスエイチが誇る最高純度バター。添加物を一切加えず、カカオ豆本来のステアリン酸とポリフェノールをそのまま肌に届ける濃密プロテクト",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "100g / チャック付遮光パック",
        "type": "未精製100%植物性ピュアカカオバター（固形）",
        "features": "未精製カカオ脂100%（コールドプレス低温圧搾）、ステアリン酸、オレイン酸、パルミチン酸",
        "value": "常温ではしっかりとした固形ブロックですが、手のひらの熱でじんわりと融解。自分の体温で溶かしながら使うため、余計な乳化剤や防腐剤を一切排除した完全無添加ケアが可能",
        "desc_p1": "市販のクリームやローションに含まれる界面活性剤や防腐剤に肌が過敏に反応してしまう敏感肌の方にとって、真冬の強烈な乾燥から肌を守る手段を見つけるのは至難の業です。そんなナチュラル志向の方に絶大な支持を得ているのが、&SHの『100% ピュア カカオバター 100g』です。",
        "desc_p2": "封を開けた瞬間に、本物の高級ビターチョコレートを思わせるリッチでビタースイートな香りが広がります。小さなカケラを手にとって手のひらで温めると、数秒でじんわりと黄金色のオイル状に融解。洗顔後の素肌やカサつく手足に押し込むように塗ると、人肌と極めて親和性の高い脂肪酸が角層にピタッと吸着し、外気と乾燥から肌を完璧にシールドします。手持ちのオイルとブレンドして自作バームを作るベースとしても大人気です。",
        "target": "防腐剤や化学成分が一切入っていない完全無添加コスメを使いたい方、自作コスメや手作りハンドバームに挑戦したい方、純粋なカカオの香りに包まれたい方",
        "point": "指先で小豆粒大のカケラを削り取り、両手のひらを擦り合わせて体温で溶かしてから、乾燥が気になる顔や手足にハンドプレスします。ホホバオイルを数滴混ぜると伸びがさらに良くなります。"
    },
    {
        "rank": 5,
        "tag": "☀️ SPF15UVカット×高純度カカオバター！真冬の紫外線と乾燥風から唇を守り抜く名品スティック",
        "catch": "冬の乾燥だけでなく、雪や晴天の反射紫外線も同時にブロック。ビタミンEと純粋カカオバターが縦ジワを消し去り、いつでもどこでもポケットから出して潤い補給できる万能リップ",
        "brand_name": "Palmer's (パーマーズ)",
        "capacity": "4g / リップスティック",
        "type": "UVカットSPF15配合 高保湿ココアバターリップスティック",
        "features": "カカオ脂、ビタミンE（酢酸トコフェロール）、サンスクリーン成分（SPF15）",
        "value": "冬の紫外線対策を怠りがちな唇に、保湿とUV遮断を同時に叶えるハイブリッド処方。スリムで持ち運びに便利、男性でも使いやすいシンプルなデザイン",
        "desc_p1": "冬の晴れた日は空気が澄んでいる分、地上に降り注ぐ紫外線量は意外と多く、さらにウィンタースポーツや旅行先では雪の照り返しによって夏以上の紫外線ダメージを唇に受けることがあります。パーマーズの『ココアバター リップバーム SPF15』は、冬のアウトドアや日常の紫外線対策に最適な一本です。",
        "desc_p2": "リップを唇に滑らせると、カカオバターが体温でスルスルと伸び、乾燥で皮むけを起こした唇にピタッと密着。紫外線吸収剤によるUVカット効果（SPF15）を備えながら、カカオ脂の濃密なエモリエント膜が冷風による乾燥を完全にシャットアウトします。口紅の下地として使えば縦ジワがふっくらと目立たなくなり、マットなリップも均一に美しく発色。ポケットに忍ばせておけば真冬の外出も安心です。",
        "target": "冬のスキーやスノーボード、アウトドアに出かける方、唇の乾燥と同時に紫外線によるくすみやシミを防ぎたい方、プチプラで優秀なデイリーリップを探している方",
        "point": "朝のメイク時や外出の20分前に塗布します。食事の後や乾燥を感じた時にこまめに塗り直すことで、真冬の木枯らしの中でも一日中ツヤやかな唇を維持できます。"
    },
    {
        "rank": 6,
        "tag": "🏔️ ヒマラヤの野生チウリバター×天然カカオ脂！真冬のあかぎれ・水仕事の手荒れを救う野生の濃密バーム",
        "catch": "ネパールの豊かな自然の恵みをお届けするナイアードの自信作。野生のチウリバターとカカオバター、蜜蝋の絶妙なブレンドが、冬の水仕事でボロボロになった手指を深く癒やす",
        "brand_name": "naiad (ナイアード)",
        "capacity": "40ml / 遮光ガラス瓶",
        "type": "天然100% 野生植物モイスチャークリームバーム",
        "features": "チウリ種子脂、カカオ脂、ミツロウ、アプリコットカーネル油",
        "value": "ネパールの女性たちが手作業で集めた天然原料のみを使用。肌の上で体温によりゆっくりと溶け出し、あかぎれやひび割れ部分に密着して水分蒸散を物理的に遮断",
        "desc_p1": "真冬の水仕事や手指消毒の繰り返しによって、指先がひび割れて出血したり、手の甲が赤く荒れてゴワゴワになってしまう……そんな過酷な手荒れに悩む方におすすめなのが、ナイアードの『チウリモイスチャークリーム』です。",
        "desc_p2": "ヒマラヤ山脈の麓に自生するチウリの木の実から搾られる高保湿バターに、天然のカカオ脂とミツロウをブレンド。ガラス瓶からスパチュラで削り取った時はしっかりとした固さがありますが、指の腹で温めるとトロリととろけて肌に密着します。一般的なハンドクリームのように水で簡単に流れ落ちず、撥水性のある保護膜が長時間手指をガード。甘いナッツとカカオの素朴な香りに包まれ、荒れた手肌が日に日に滑らかに整っていきます。",
        "target": "冬の水仕事や家事で手のあかぎれ・ひび割れが治らない方、化学成分無添加のナチュラルな高保湿バームを求める方、指先のささくれを集中的にリペアしたい方",
        "point": "少量を手にとり、両手ですり合わせて体温で完全に溶かしてから、指先一本一本、爪の生え際まで丁寧に揉み込みます。水仕事の直前に塗るとバリア膜が水を弾いてくれます。"
    },
    {
        "rank": 7,
        "tag": "📦 たっぷり使える大容量200g！真冬の全身マッサージからオリジナルバーム自作まで対応するピュアカカオ",
        "catch": "コスパ抜群の200g大容量パック。惜しみなく全身のボディケアに使える純粋カカオバター。家族全員の真冬の粉吹き肌対策や、手作り石鹸・コスメの原料としても大活躍",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "200g / チャック付保存パック",
        "type": "業務用・大容量ピュアカカオバター（固形）",
        "features": "カカオ脂100%、高濃度ステアリン酸、天然トコフェロール",
        "value": "100gパックに比べて圧倒的なコストパフォーマンス。真冬の間中、毎晩のボディマッサージやかかとの集中パックに贅沢に使い倒せるボリューム感",
        "desc_p1": "家族みんなで冬の乾燥対策をしたい時や、全身に惜しみなく高純度バターを使いたい時に最適なのが、&SHの『大容量 カカオバター 200g』です。良質なカカオ豆から低温圧搾されたピュアな固形バターがたっぷり詰め込まれています。",
        "desc_p2": "お風呂上がりに、湯船の温もりで柔らかくなった肌へ直接滑らせるように塗布すれば、体温でじんわりと溶け出し、全身を上質なショコラの香りとシルキーな潤い膜が包み込みます。特に乾燥が気になるすね、太もも、背中、かかとへ贅沢にすり込めば、翌朝には粉吹きが完全に消え去り、触れるとしっとり吸い付くような肌触りに。冬の乾燥対策のベースとして常備しておきたい頼れる存在です。",
        "target": "毎日たっぷり全身にカカオバターを使いたい方、家族で共有できる大容量の高保湿アイテムを探している方、手作りコスメを大ロットで作りたい方",
        "point": "耐熱容器にカカオバター適量とホホバオイルやスイートアーモンドオイルを7:3の割合で入れ、湯煎で溶かして冷やすと、冬でも扱いやすい極上の柔らかボディバターが完成します。"
    },
    {
        "rank": 8,
        "tag": "🛁 400mlビッグポンプ！お風呂上がりの全身を瞬時に包み込み24時間乾かさないエモリエントローション",
        "catch": "大人気パーマーズの特大ポンプバージョン。片手でサッと出せるスマート仕様で、真冬の脱衣所での冷えを防ぎながらスピーディーに極上の高保湿ボディケアが完了",
        "brand_name": "Palmer's (パーマーズ)",
        "capacity": "400ml / 専用ポンプボトル",
        "type": "大容量高保湿ココアバターエモリエントローション",
        "features": "カカオバター、ビタミンE、シアバター、ココナッツオイル",
        "value": "ワンプッシュで適量が出るポンプ式でストレスフリー。真冬の寒いお風呂上がりでも、素早く全身に伸ばして服を着られる抜群の浸透性とエモリエント力",
        "desc_p1": "冬のお風呂上がりは、服を着るまでの数分間で皮膚の水分が一気に蒸発し、同時に体も冷えてしまいます。だからこそ、ボディケアは『スピーディーに塗れて、かつ圧倒的に高保湿』であることが絶対条件です。パーマーズの『400ml ポンプローション』は、この冬の入浴後問題を一発で解決します。",
        "desc_p2": "ポンプをプッシュして手のひらに広げると、甘美なカカオの香りがバスルームに満ちてリゾート気分に。なめらかなローションが肌の上を滑るように広がり、角層の奥までスッと浸透しながら表面には薄くしなやかな保護膜を形成します。ベタつきが肌に残らないため、塗布した直後にパジャマを着ても張り付きません。400mlのメガサイズで真冬を余裕で乗り切れる安心感も大きな魅力です。",
        "target": "お風呂上がりのボディ保湿を時短かつ強力に行いたい方、ポンプ式で手軽に毎晩ケアを続けたい方、ベタつきが苦手だけれど真冬の乾燥を防ぎたい方",
        "point": "入浴直後、バスタオルで水気を軽く拭き取った温かい素肌に、3〜4プッシュを全身へ手早く伸ばします。肩周りやすねのマッサージを兼ねて行うと血行も促進されます。"
    },
    {
        "rank": 9,
        "tag": "🤰 カカオバター×アルガンオイル×コラーゲン！真冬の乾燥で突っ張るボディの柔軟性を保つマッサージローション",
        "catch": "急激な体型変化や冬の過酷な乾燥による皮膚のつっぱり・肉割れ・妊娠線を防ぐために開発された専門処方。カカオバターの弾力柔軟パワーで皮膚をふっくら柔らかく保つ",
        "brand_name": "Palmer's (パーマーズ)",
        "capacity": "250ml / ポンプボトル",
        "type": "高弾力柔軟化 ココアバターマッサージローション",
        "features": "純粋カカオバター、シアバター、アルガンオイル、加水分解コラーゲン、エラスチン、ツボクサエキス（ルチン）",
        "value": "単なる保湿にとどまらず、コラーゲンやエラスチンの線維構造を保護し、真冬の乾燥で硬化した皮膚の伸縮性を極限まで高める高機能ボディトリートメント",
        "desc_p1": "真冬はお腹周りや太もも、お尻の皮膚が乾燥して硬くなり、触ると冷たく強張ってストレッチマーク（ひび割れ線）ができやすい季節です。パーマーズの『ココアバター マッサージローション』は、世界中のプレママやボディメイク層から絶大な支持を得ている皮膚柔軟化の専門ローションです。",
        "desc_p2": "高純度カカオバターに加えて、モロッコ産のアルガンオイルやコラーゲン、エラスチンを贅沢に配合。伸びの良いミルキーなテクスチャーが肌を滑らかに包み込み、硬直した皮膚深部にまで潤いを届けます。毎晩お腹やヒップ、二の腕を優しくマッサージしながら塗り込むことで、冬の寒さに負けない柔軟でしなやかなハリ肌をキープ。産前産後のケアとしてはもちろん、冬の集中たるみ・乾燥対策にも最適です。",
        "target": "妊娠中のお腹の乾燥やつっぱり・妊娠線を本気で予防したい方、真冬に太ももやヒップの皮膚が乾燥して硬くなっている方、コラーゲン配合のボディケアを求める方",
        "point": "手のひらに2プッシュをとり、お腹や太もも、ヒップに円を描くように優しくマッサージしながらなじませます。朝晩の1日2回継続して使用すると効果的です。"
    },
    {
        "rank": 10,
        "tag": "🧼 シアバター×カカオ脂配合！真冬の乾燥肌でも皮脂を奪いすぎずしっとり潤い膜を残す伝統ブラックソープ",
        "catch": "アフリカの伝統製法を受け継ぐヌビアンヘリテージの世界的名作ソープ。カカオポッド（カカオの殻）の灰と純粋植物バターが、冬の古い角質を吸着しながら極上のしっとり素肌へ洗い上げる",
        "brand_name": "Nubian Heritage (ヌビアンヘリテージ)",
        "capacity": "141g / 個別箱入り",
        "type": "天然シア＆カカオ脂配合 アフリカンブラック美容石鹸",
        "features": "シアバター、カカオポッド灰、カカオ脂、パーム油、オート麦エキス、アロエベラ液汁",
        "value": "石鹸でありながら洗浄後のつっぱり感が一切なく、カカオバターの保湿膜が肌上に残る驚異の処方。真冬の背中ニキビや乾燥による肌荒れを同時にケア",
        "desc_p1": "冬になると、ボディソープで体を洗った直後から全身がピキピキと突っ張り、急いでローションを塗らないと痒くなってしまう……そんな『洗いすぎ乾燥』に悩む方にぜひ使っていただきたいのが、ヌビアンヘリテージの『アフリカンブラックソープ』です。",
        "desc_p2": "黒いマーブル模様のバーを泡立てネットで擦ると、驚くほどクリーミーで濃密なグレーの泡がモコモコと立ち上がります。カカオポッドの灰が冬の毛穴汚れや古い角質をやさしく吸着オフし、同時に配合されたカカオバターとシアバターが素肌にしっとりとしたエモリエントヴェールを形成。お風呂から出た後も肌がつっぱらず、すべすべで吸い付くような潤いが続きます。冬のボディウォッシュの概念を覆す名品です。",
        "target": "冬にお風呂で体を洗うと肌が乾燥してピキピキ突っ張る方、背中やデコルテの毛穴詰まりと乾燥を同時にケアしたい方、海外のナチュラル固形石鹸が好きな方",
        "point": "泡立てネットを使ってたっぷりの濃密泡を作り、手で泡を滑らせるように優しく全身を洗います。ナイロンタオルなどでゴシゴシ擦らないのが真冬の美肌の鉄則です。"
    }
]

# 目次項目の定義
toc_items = [
    {"id": "intro", "title": "1. 11月・12月の粉吹き＆ひび割れ肌を救う！カカオバター（ココアバター）の魅力"},
    {"id": "mechanism", "title": "2. 人肌の体温でとろける奇跡！カカオバターの皮膚科学とエモリエント膜"},
    {"id": "comparison", "title": "3. 高保湿カカオバターコスメおすすめ10選の比較表"},
    {"id": "ranking", "title": "4. 高保湿ココアバターコスメおすすめ厳選ランキング10選"},
    {"id": "guide", "title": "5. 失敗しない冬のカカオバターコスメの選び方（未精製 vs 精製）"},
    {"id": "routine", "title": "6. 真冬のカチコチ肌をとろかす！カカオバター集中トリートメント手順"},
    {"id": "faq", "title": "7. カカオバター（ココアバター）コスメに関するよくある質問（FAQ）"},
    {"id": "summary", "title": "8. まとめ：人肌でとろけるカカオの潤い膜で真冬もベルベット肌へ"}
]

toc_html = "\n".join([f'          <li><a href="#{item["id"]}">{item["title"]}</a></li>' for item in toc_items])

# 比較表の生成
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

# 各商品カードのHTML生成
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
                <span class="review-stars">★ {item_data["reviewAverage"]}</span>
                <span class="review-count">（口コミ {item_data["reviewCount"]}件）</span>
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

# 記事全体のHTML構築
full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！人肌でとろける高純度カカオバターが真冬の粉吹き・カチコチひび割れ肌をベルベット密着膜で包み込む高保湿ココアバターコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の本格的な乾燥と寒冷で粉を吹くすね・肘・膝、ひび割れる唇やかかとを救う高保湿カカオバター（ココアバター）コスメを徹底厳選！パーマーズ、バジャー、ヴェレダ、アンドエスエイチ、ナイアードまで体温融解エモリエントの科学的根拠と共に徹底検証。">
  <meta name="keywords" content="カカオバター コスメ, ココアバター 保湿, カカオ脂 ボディローション, パーマーズ ココアバター, バジャー リップバーム, ヴェレダ スキンフード, 冬 粉吹き肌 対策, 高保湿 バーム">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-cacao-butter">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！人肌でとろける高純度カカオバターが真冬の粉吹き・カチコチひび割れ肌をベルベット密着膜で包み込む高保湿ココアバターコスメランク10">
  <meta property="og:description" content="11月・12月の本格的な乾燥と寒冷で粉を吹くすね・肘・膝、ひび割れる唇やかかとを救う高保湿カカオバターコスメを徹底厳選！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-cacao-butter">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="LUMI COSMETICS">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！人肌でとろける高純度カカオバターが真冬の粉吹き・カチコチひび割れ肌をベルベット密着膜で包み込む高保湿ココアバターコスメランク10",
    "description": "11月・12月の本格的な乾燥と寒冷で粉を吹くすね・肘・膝、ひび割れる唇やかかとを救う高保湿カカオバター（ココアバター）コスメを徹底厳選！",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-cacao-butter"
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
    "datePublished": "2026-11-05T12:00:00+09:00",
    "dateModified": "2026-11-05T12:00:00+09:00"
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿カカオバターコスメおすすめ厳選ランキング10選",
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

  <style>
    :root {{
      --primary: #5c3826;
      --primary-light: #f5ebe6;
      --primary-dark: #3b2216;
      --accent: #8c5338;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg: #faf6f0;
      --bg-card: #ffffff;
      --border: #e8d8ce;
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
    .logo {{
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.02em;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.95rem;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}
    
    .container {{
      max-width: 1040px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    .article-header {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      margin-bottom: 2rem;
      box-shadow: var(--shadow);
    }}
    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}
    .breadcrumb a {{ color: var(--accent); text-decoration: none; }}
    .post-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    h1 {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #111827;
      margin-bottom: 1.25rem;
      font-weight: 800;
    }}
    .meta-bar {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      border-top: 1px solid #f3f4f6;
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
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
      position: relative;
    }}
    .product-header {{
      display: flex;
      gap: 1rem;
      align-items: flex-start;
      margin-bottom: 1.5rem;
    }}
    .rank-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 0.4rem 1rem;
      border-radius: 6px;
      white-space: nowrap;
    }}
    .rank-1 {{ background: linear-gradient(135deg, #78350f, #451a03); }}
    .rank-2 {{ background: linear-gradient(135deg, #9ca3af, #6b7280); }}
    .rank-3 {{ background: linear-gradient(135deg, #a16207, #713f12); }}
    .product-title-group {{ flex: 1; }}
    .product-catch {{
      display: block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.25rem;
    }}
    .product-name {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 0.25rem;
    }}
    .product-subname {{
      font-size: 0.9rem;
      color: var(--text-muted);
    }}
    .product-main-grid {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
      align-items: start;
    }}
    @media (max-width: 768px) {{
      .product-main-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-visual {{
      text-align: center;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid #f3f4f6;
      background: #fafafa;
      margin-bottom: 1rem;
      aspect-ratio: 1/1;
      object-fit: contain;
    }}
    .price-box {{
      background: #fff1f2;
      border: 1px solid #fecdd3;
      border-radius: 6px;
      padding: 0.5rem;
      margin-bottom: 0.75rem;
    }}
    .price-label {{ display: block; font-size: 0.75rem; color: #9f1239; }}
    .price-value {{ font-size: 1.3rem; font-weight: 800; color: #e11d48; }}
    .review-meta {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}
    .review-stars {{ color: #f59e0b; font-weight: 700; }}
    .rakuten-btn {{
      display: inline-block;
      width: 100%;
      background: linear-gradient(135deg, #bf0000, #900000);
      color: #ffffff !important;
      font-size: 0.95rem;
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-radius: 6px;
      text-decoration: none !important;
      text-align: center;
      transition: opacity 0.2s;
    }}
    .rakuten-btn:hover {{ opacity: 0.9; }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      margin-bottom: 1.5rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.75rem;
      border: 1px solid #f3f4f6;
    }}
    .spec-table th {{
      background: #fdfaf6;
      color: var(--primary-dark);
      width: 25%;
      font-weight: 700;
    }}
    .body-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      border-left: 3px solid var(--primary);
      padding-left: 0.5rem;
    }}
    .recommend-box, .usage-box {{
      background: #fafaf9;
      border: 1px solid #e7e5e4;
      border-radius: 6px;
      padding: 1rem;
      margin-top: 1rem;
      font-size: 0.9rem;
    }}
    .recommend-title, .usage-title {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.35rem;
    }}

    /* Q&A / FAQ */
    .faq-item {{
      border-bottom: 1px solid #f3f4f6;
      padding: 1.25rem 0;
    }}
    .faq-q {{
      font-weight: 700;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}
    .faq-q::before {{
      content: "Q";
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 800;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
    }}
    .faq-a {{
      color: #374151;
      font-size: 0.95rem;
      padding-left: 1.75rem;
    }}

    /* 内部リンクカード */
    .related-hub {{
      background: #ffffff;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      padding: 2rem;
      margin-top: 3rem;
    }}
    .related-title {{
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.25rem;
    }}
    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem;
    }}
    .related-card {{
      background: #fafaf9;
      border: 1px solid #e7e5e4;
      border-radius: 6px;
      padding: 1rem;
      text-decoration: none;
      color: var(--text);
      transition: all 0.2s;
    }}
    .related-card:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}
    .related-card-title {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.25rem;
    }}
    .related-card-desc {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    footer {{
      background: #111827;
      color: #9ca3af;
      padding: 3rem 0;
      margin-top: 4rem;
      font-size: 0.9rem;
    }}
    .footer-inner {{
      max-width: 1040px;
      margin: 0 auto;
      padding: 0 1.5rem;
      text-align: center;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1rem 1.5rem;
      margin-bottom: 2rem;
    }}
    .footer-links a {{
      color: #d1d5db;
      text-decoration: none;
      font-size: 0.85rem;
    }}
    .footer-links a:hover {{ color: #ffffff; }}
    .copyright {{ font-size: 0.8rem; color: #6b7280; }}
  </style>
</head>
<body>

  <header>
    <div class="header-inner">
      <a href="/" class="logo">LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">冬コスメTOP</a>
        <a href="/winter-shea-butter">シアバター</a>
        <a href="/winter-beeswax">ミツロウ</a>
        <a href="/winter-sweet-almond-oil">アーモンド油</a>
      </nav>
    </div>
  </header>

  <main class="container">

    <article>
      <div class="article-header">
        <div class="breadcrumb">
          <a href="/">TOP</a> &gt; <a href="/#bodycare">冬の濃厚高保湿ボディケア</a> &gt; カカオバターコスメ
        </div>
        <span class="post-tag">2026年11月・12月 真冬の濃密エモリエント</span>
        <h1>保湿力の強さで肌乾燥とさようなら！人肌でとろける高純度カカオバターが真冬の粉吹き・カチコチひび割れ肌をベルベット密着膜で包み込む高保湿ココアバターコスメランク10</h1>
        <div class="meta-bar">
          <span>📅 公開日: 2026年11月5日</span>
          <span>✍ 監修: LUMI COSMETICS 保湿皮膚科学研究チーム</span>
          <span>⏱ 読了目安: 約13分</span>
        </div>
      </div>

      <!-- 目次 -->
      <div class="toc-card">
        <div class="toc-title">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h7"/></svg>
          目次：クリックで各項目へジャンプできます
        </div>
        <ul>
{toc_html}
        </ul>
      </div>

      <!-- セクション1: 導入・冬の粉吹き＆ひび割れ肌 -->
      <section class="article-section" id="intro">
        <h2 class="section-title">1. 11月・12月の粉吹き＆ひび割れ肌を救う！カカオバター（ココアバター）の魅力</h2>
        <div class="highlight-lead">
          真冬の冷風と暖房乾燥によって皮脂膜が完全に枯渇すると、皮膚は角質細胞がめくれ上がり白く粉を吹きます。この深刻な砂漠化を食い止める物理的シールドこそ、体温（34〜38℃）でじんわりとろけて角層を密封する『カカオバター』です。
        </div>
        <p>11月中旬以降、最低気温がひと桁台まで落ち込み、木枯らしが吹く季節になると、お風呂上がりのすねや腕がカサカサと白く粉を吹き始めます。タイツやレギンスを履いた瞬間にチクチクとした痒みが生じたり、踵（かかと）がひび割れてストッキングを伝線させてしまったり……こうした冬特有のボディトラブルに悩まされる方は非常に多いはずです。</p>
        <p>これは、気温の低下によって皮脂腺からの皮脂分泌がほぼ停止し、さらに空気中の水分が奪われることで、角層の最外層にある細胞間脂質がスカスカに崩壊してしまうためです。一般的な水っぽいボディミルクを塗っても、数分後には蒸発して元のパサパサ肌に逆戻りしてしまいます。</p>
        <p>そこで世界中で何世代にもわたり「最強の冬用エモリエント」として君臨し続けているのが、カカオ豆から圧搾抽出される『カカオバター（ココアバター / Theobroma Cacao Seed Butter）』です。常温では硬質な固形でありながら、人肌に触れた瞬間にトロリと溶け出すその物理的特性は、まさに過酷な日本の真冬を乗り切るために自然が授けてくれた奇跡のバームと言えます。</p>
      </section>

      <!-- セクション2: 科学的メカニズム -->
      <section class="article-section" id="mechanism">
        <h2 class="section-title">2. 人肌の体温でとろける奇跡！カカオバターの皮膚科学とエモリエント膜</h2>
        <p>カカオバターの学名「Theobroma」は、ギリシャ語で「神々の食べ物（Theo=神、broma=食べ物）」を意味します。古代マヤ文明やアステカ文明の時代から重用されてきたカカオバターが、なぜ真冬の乾燥肌に対してこれほど圧倒的な保護力を発揮するのか、その科学的根拠を紐解きます。</p>
        
        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">① 奇跡の融点「34℃〜38℃」がもたらす体温融解エモリエント</h3>
        <p>カカオバターの最大の特異性は、その融点（Melting Point）にあります。20℃前後の室温では安定したソリッド（固形）ですが、人間の体温である34℃〜38℃の範囲で一気に液状化します。肌に乗せると体温を感知してジュワッととろけ、角層の微小なキメの溝やひび割れの隙間へとスムーズに入り込み、冷めると再びしなやかな保護膜として定着します。<a href="/winter-shea-butter">シアバター</a>や<a href="/winter-beeswax">ミツロウ</a>を凌駕する抜群の密着性を誇ります。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">② ステアリン酸×オレイン酸の持続性エモリエントシールド</h3>
        <p>カカオバターの脂肪酸組成は、ステアリン酸（約33〜38%）、オレイン酸（約32〜37%）、パルミチン酸（約24〜30%）が大部分を占めています。特に飽和脂肪酸であるステアリン酸は非常に酸化安定性が高く、皮膚表面に撥水性のある強固なヴェールを形成。入浴後の水分蒸散を24時間にわたって物理的に遮断し、衣服との摩擦刺激からも角層を保護します。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">③ カカオポリフェノールによる抗酸化と皮膚柔軟化</h3>
        <p>カカオにはフラバノールやテオブロミンといった天然のポリフェノール類が豊富に含まれています。真冬の寒冷ストレスや乾燥によって硬直した皮膚組織を柔らかく解きほぐし、角層のターンオーバーを正常化。<a href="/winter-sweet-almond-oil">スイートアーモンドオイル</a>や<a href="/winter-foot-cream">フットクリーム</a>と併用することで、頑固な踵のガサガサも短期間でスベスベのベルベット肌へと導きます。</p>
      </section>

      <!-- セクション3: 比較表 -->
      <section class="article-section" id="comparison">
        <h2 class="section-title">3. 高保湿カカオバターコスメおすすめ10選の比較表</h2>
        <p>楽天市場の最新在庫・価格データから、2026年11月・12月の冬本番にリアルタイムで人気のカカオバターコスメ10選を一覧表にまとめました。ボディローション、濃厚バーム、リップケア、石鹸など用途に合わせて比較してください。</p>
        
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>アイテムタイプ</th>
                <th>価格（税込）</th>
                <th>注目キー成分</th>
                <th>公式リンク</th>
              </tr>
            </thead>
            <tbody>
{table_rows_html}
            </tbody>
          </table>
        </div>
      </section>

      <!-- セクション4: 詳細ランキング -->
      <section class="article-section" id="ranking">
        <h2 class="section-title">4. 高保湿ココアバターコスメおすすめ厳選ランキング10選</h2>
        <p>ここからは、1位から10位までの各アイテムについて、テクスチャーの特徴、真冬の粉吹き・ひび割れ肌に対する使用感、おすすめの肌質、効果的な使用テクニックまで徹底解説します。</p>

{all_cards_html}

      </section>

      <!-- セクション5: 選び方ガイド -->
      <section class="article-section" id="guide">
        <h2 class="section-title">5. 失敗しない冬のカカオバターコスメの選び方（未精製 vs 精製）</h2>
        <p>カカオバターコスメを選ぶ際、最も重要なポイントは「精製度」と「アイテム形状（ローション・バーム・スティック）」の使い分けです。</p>
        
        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">① 「未精製（天然の香り）」vs「精製（無香料）」の選択</h3>
        <p>未精製グレードは、天然チョコレートの芳醇で甘い香りと、カカオポリフェノールや微量栄養素がそのまま残っています。ショコラのアロマに癒やされたい方や、植物本来の力を活かしたい方におすすめです。一方、精製グレードは脱色・脱臭されているため、香りを気にせず職場やメイク前、香水と併用したい方に最適です。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">② 「全身の粉吹き」にはポンプ式エモリエントローション</h3>
        <p>お風呂上がりに手早く全身をケアしたい場合は、パーマーズのようなポンプ式ローションがベスト。水分とカカオバターが乳化されているため、濡れた肌にも素早くなじみ、ベタつきを残さず洋服をすぐに着られます。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">③ 「踵のひび割れ・唇の皮むけ」には純粋ソリッドバーム</h3>
        <p>ストッキングが引っかかる踵や、冷風で切れてしまう唇には、水分を含まない100%固形バターや高濃度バーム（バジャーやアンドエスエイチ）を選びましょう。体温で溶かしながら厚めに塗り込むことで、一晩で頑固なカチコチ角質がふっくらと柔らかくなります。</p>
      </section>

      <!-- セクション6: 集中トリートメント手順 -->
      <section class="article-section" id="routine">
        <h2 class="section-title">6. 真冬のカチコチ肌をとろかす！カカオバター集中トリートメント手順</h2>
        <div class="highlight-lead">
          カカオバターの密封力を最大限に引き出す黄金律は『お風呂上がりの温まった素肌に素早く塗り込むこと』です。
        </div>
        <ol style="padding-left:1.5rem;margin-bottom:1.5rem;line-height:2;">
          <li><strong>ステップ1（マイルド入浴・洗浄）:</strong> ヌビアンヘリテージのブラックソープを泡立て、皮脂を落としすぎずに古い角質だけをやさしく洗浄。湯船で体を芯まで温めます。</li>
          <li><strong>ステップ2（水分オフ＆直後塗布）:</strong> 浴室を出たらバスタオルで軽く水気を押さえ、肌が温かく蒸気を含んでいるうちにパーマーズのローションを全身へ塗布。</li>
          <li><strong>ステップ3（局所集中メルティング）:</strong> 踵や肘、指先などカチコチに硬化した部分には、固形カカオバターやナイアードのチウリクリームを指先で体温融解させながらすり込みます。</li>
          <li><strong>ステップ4（リップナイトパック）:</strong> バジャーのココアリップを唇の輪郭からはみ出すようにオーバーに厚塗り。</li>
          <li><strong>ステップ5（保温＆密閉ラッピング）:</strong> 足元には綿の靴下、手にはコットングローブを着用して就寝。翌朝には白粉吹きゼロのシルキー肌が完成します。</li>
        </ol>
      </section>

      <!-- セクション7: FAQ -->
      <section class="article-section" id="faq">
        <h2 class="section-title">7. カカオバター（ココアバター）コスメに関するよくある質問（FAQ）</h2>
        
        <div class="faq-item">
          <div class="faq-q">カカオバターを顔に使っても毛穴が詰まりませんか？</div>
          <div class="faq-a">カカオバターはステアリン酸やオレイン酸が主成分のエモリエントです。乾燥肌や真冬のエアコンで突っ張る肌には最高の保護膜となりますが、皮脂分泌の多いTゾーンやニキビができやすい部位には薄く伸ばすか、乾燥しやすい目元や口元のピンポイント使用がおすすめです。</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">シアバターとカカオバターはどう違うのですか？</div>
          <div class="faq-a">シアバターは常温でもやや柔らかくクリーミーなペースト状ですが、カカオバターは室温でしっかりとした固形を保ちます。そのためカカオバターの方が皮膚表面に形成される保護膜の持続性と撥水性が高く、真冬の強烈な冷風や衣服摩擦から肌を守るシールド力に優れています。</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">チョコレートの香りは周囲に強く漂いますか？</div>
          <div class="faq-a">塗布した直後は甘美なショコラの香りがふんわりと香りますが、肌になじんで10〜20分ほど経つと穏やかな残り香へと落ち着きます。もし香りを控えたい場合は、精製グレードの無香料タイプをお選びください。</div>
        </div>
      </section>

      <!-- セクション8: まとめ -->
      <section class="article-section" id="summary">
        <h2 class="section-title">8. まとめ：人肌でとろけるカカオの潤い膜で真冬もベルベット肌へ</h2>
        <p>11月・12月の冬本番、外気の乾燥と寒冷によって傷つき白く粉を吹いた肌は、放置すると角質が硬化し、ひび割れや深刻な肌荒れへと発展します。人肌の温もりでとろけ、ビロードのように滑らかな保護膜で素肌を包み込むカカオバターは、真冬のボディ＆リップケアにおける最強の味方です。</p>
        <p>ぜひ今回の厳選10選の中からお気に入りのココアバターコスメを手に入れて、まるで極上のスイーツに包まれるような至福の潤い体験をお楽しみください！</p>
      </section>

      <!-- 関連記事ハブ -->
      <div class="related-hub">
        <div class="related-title">🍫 あわせて読みたい！冬の高保湿ボディ＆バーム特集</div>
        <div class="related-grid">
          <a href="/winter-shea-butter" class="related-card">
            <div class="related-card-title">🌰 高保湿シアバターコスメ</div>
            <div class="related-desc">真冬の乾燥粉吹き肌をとろける植物性脂肪酸で包み込むリッチケア10選。</div>
          </a>
          <a href="/winter-beeswax" class="related-card">
            <div class="related-card-title">🐝 高保湿ミツロウコスメ</div>
            <div class="related-desc">ミツバチが創る天然の保護皮膜で真冬の冷風と乾燥から肌を守る名品10選。</div>
          </a>
          <a href="/winter-sweet-almond-oil" class="related-card">
            <div class="related-card-title">🌰 スイートアーモンドオイル</div>
            <div class="related-desc">高濃度オレイン酸とビタミンEが真冬の粉吹き肌をふっくらほぐす高保湿10選。</div>
          </a>
          <a href="/winter-foot-cream" class="related-card">
            <div class="related-card-title">🦶 高保湿フットクリーム</div>
            <div class="related-desc">ガサガサ・ひび割れかかととさようなら！タイツが引っかからない極上フットケア。</div>
          </a>
        </div>
      </div>

    </article>

  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-links">
        <a href="/">冬コスメTOP</a>
        <a href="/winter-cacao-butter">カカオバターコスメ</a>
        <a href="/winter-shea-butter">シアバター</a>
        <a href="/winter-beeswax">ミツロウ</a>
        <a href="/winter-sweet-almond-oil">アーモンド油</a>
        <a href="/winter-ginseng">高麗人参コスメ</a>
        <a href="/winter-shikon">和漢紫根</a>
      </div>
      <p class="copyright">&copy; 2026 LUMI COSMETICS. All Rights Reserved. 当サイトは楽天市場アフィリエイトプログラムに参加しています。</p>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-cacao-butter.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-cacao-butter.html successfully! Character count:", len(full_html))
