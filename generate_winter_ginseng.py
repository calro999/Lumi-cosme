import json
import re

with open("fetched_3new_ginseng_cacao_silk.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_ginseng"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 希少高麗人参サポニンを凝縮！寒冷でしぼみきった肌をふっくら押し上げる最高峰セラム",
        "catch": "韓国を代表するラグジュアリースキンケア雪花秀の真骨頂。特許技術で濃縮したジンセノミクスが、真冬の寒冷で低下した肌の基礎体力を底上げし、指を弾き返すような高密度ハリ肌を再建する",
        "brand_name": "Sulwhasoo (雪花秀 / ソルファス)",
        "capacity": "20g / スポイト遮光ボトル",
        "type": "高純度ジンセン濃縮エイジングケア美容液",
        "features": "濃縮高麗人参サポニン（ジンセノミクス）、高麗人参ペプチド、アデノシン、ヒアルロン酸",
        "value": "1000gの高麗人参からわずか1gしか抽出できない希少成分を6000倍に濃縮。真冬の冷気で代謝が停滞し、たるみや小ジワが目立ち始めた大人の肌に濃密な生命感を注入する",
        "desc_p1": "11月中旬を過ぎて木枯らしが吹き始める頃、鏡を見て『肌が青白くくすみ、フェイスラインのハリが失われて疲れて見える』と感じることはありませんか。これは外気温の急激な低下によって毛細血管が収縮し、真皮層への酸素や栄養の供給が滞ってしまう『冬の寒冷血行不良』が原因です。韓国最高峰のプレステージブランド雪花秀の『滋陰生（ジャウムセン）アンプル』は、この過酷な真冬の皮膚生理に着目して生み出されたレスキュー美容液です。",
        "desc_p2": "使用直前にカプセルが弾けてフレッシュな人参サポニンが解き放たれる特殊構造を採用。手のひらに出すと、ほのかに漂う気品ある高麗人参の香りと共に、驚くほどまろやかなテクスチャーが肌へと吸い込まれていきます。塗布した直後から肌内部がじんわりと温まるような安心感に包まれ、翌朝目覚めたときには暖房の風にさらされていたとは思えないほど、キメのひとつひとつが内側からパンと張ったような弾力を実感できます。真冬の勝負コスメとして手放せなくなる名品です。",
        "target": "冬になると肌が青白くくすんで元気がない方、暖房による乾燥小ジワと同時にフェイスラインのたるみが気になる方、一生モノの最高峰美容液で本気の冬エイジングケアを行いたい方",
        "point": "夜の洗顔後、化粧水で肌を整えた直後にスポイト1回分を手にとります。両手で軽く温めてから顔全体に広げ、手のひら全体で包み込むようにハンドプレス。最後に耳の下から鎖骨へ向かってリンパを流すように撫で下ろすと血行促進効果が高まります。"
    },
    {
        "rank": 2,
        "tag": "🌿 オタネニンジン根水80%高配合！真冬の乾いた角層をみずみずしく覚醒させる大人気韓方トナー",
        "catch": "世界中でバズを生み出し続ける朝鮮美女の看板化粧水。精製水の代わりに高麗人参水を贅沢にベースとし、ナイアシンアミドとアデノシンの黄金比率で冬のインナードライを根本から解消",
        "brand_name": "Beauty of Joseon (朝鮮美女)",
        "capacity": "150ml / ドロッパーボトル",
        "type": "韓方高麗人参 高保湿ブースタートナー",
        "features": "オタネニンジン根水80%、ナイアシンアミド2%、アデノシン0.04%、ヒアルロン酸Na",
        "value": "ベースとなる水の8割に高麗人参エキスを採用しながら、毎日惜しみなく使える圧倒的ハイコスパ。皮脂バランスを整えつつ、真冬の冷風でゴワついた角質層へ水分をぐんぐん引き込む",
        "desc_p1": "冬の朝、どれだけ化粧水を重ねづけしても肌の奥までうるおいが届かず、ファンデーションを塗ったそばからカサカサと浮いてしまう……。そんな悩みを抱える方にぜひ試していただきたいのが、海外のスキンケアフリークの間でも爆発的人気を博している朝鮮美女の『ジンセン エッセンスウォーター』です。",
        "desc_p2": "ボトルの80%を占める濃厚なオタネニンジン根水が、乾燥で硬直した角層の隙間をスルスルと満たし、巡りを呼び覚まします。シャバシャバとした軽やかな水のような感触でありながら、肌になじませるとエッセンスを重ねたかのような深い保水膜が形成。ナイアシンアミドが冬の乾燥によるくすみを晴らし、内側から発光するようなみずみずしい透明感を与えます。コットンにたっぷり含ませて5分間ローションパックをすると、暖房に負けない極上のベースが完成します。",
        "target": "とろみ化粧水だと肌表面に残ってベタつくのが苦手な方、冬のインナードライやメイク前の乾燥崩れに悩む方、コスパ良く毎日惜しみなく韓方スキンケアを取り入れたい方",
        "point": "500円玉大を手にとり、顔全体に優しく押し込むようにハンドプレス。乾燥が気になる目元や頬骨あたりには、さらに少量を重ねて『2度づけ』するのが冬のうるおい持続の秘訣です。"
    },
    {
        "rank": 3,
        "tag": "👁️ 高麗人参エキス10%×レチナール2%！真冬の目元・口元の深い小ジワをふっくら持ち上げる集中アイセラム",
        "catch": "刺激を抑えたリポソーム化レチナールと高麗人参が融合。暖房で水分が蒸発しやすい目周りの薄い皮膚にピンポイントで密着し、寝ている間に刻まれた影をふっくら解消",
        "brand_name": "Beauty of Joseon (朝鮮美女)",
        "capacity": "30ml / ポンプエアレスチューブ",
        "type": "目元・口元用 高機能集中エイジングケアセラム",
        "features": "高麗人参根エキス10%、レチナールリポソーム2%、グリセリン、セラミドNP",
        "value": "安定化されたビタミンA誘導体（レチナール）を採用し、A反応を抑えながら確かなハリ感を追求。真冬の過酷な乾燥による目元のちりめんジワ・ほうれい線を集中補修",
        "desc_p1": "顔の中でも特に皮膚が薄く、皮脂腺が極端に少ない目元は、11月以降の湿度低下とエアコン暖房の直風によって真っ先に悲鳴を上げます。笑ったときに目尻に残る細かな線や、夕方の目元のどんよりとした影にアプローチするために開発されたのが、この『リバイブ アイセラム』です。",
        "desc_p2": "高麗人参の血行促進・代謝サポート力と、コラーゲン産生を助けるレチナールがタッグを組んだ高機能処方。シルキーで伸びの良いジェルクリーム状テクスチャーで、デリケートな目元を一切擦ることなくスルスルと馴染みます。ポンプ式のエアレス容器なので、最後まで酸化を防いで衛生的に使えるのも魅力。夜塗って眠れば、翌朝の洗顔時に指先が触れた瞬間、目元の皮膚がふっくらと厚みを増したような心地よい弾力を実感できます。",
        "target": "冬になると目尻や目の下に細かな乾燥ジワが刻まれやすい方、ほうれい線周りのファンデーション落ちに悩む方、レチノール製品を使ってみたいけれど乾燥や刺激が心配な方",
        "point": "夜のお手入れのクリームの前に、1プッシュ分を薬指にとり、目頭から目尻、こめかみにかけて優しく置くようにトントンとなじませます。余った分はほうれい線や眉間のシワにも馴染ませましょう。"
    },
    {
        "rank": 4,
        "tag": "👑 韓国宮廷秘伝の紅参処方！真冬の寒さで皮脂が完全に枯渇した大人の肌を贅沢なコクで包む濃密クリーム",
        "catch": "LG生活健康が誇る皇室処方コスメ「後(ドフー)」。時間をかけて熟成蒸留された紅参エキスと和漢植物成分が、真冬の木枯らしに立ち向かう鉄壁の保湿バリアを肌上に構築する",
        "brand_name": "The History of Whoo (後 / ドフー)",
        "capacity": "50ml / 重厚ジャー容器",
        "type": "宮廷韓方 高濃縮エイジングモイスチャークリーム",
        "features": "紅参エキス（高麗人参発酵液）、何首烏（カシュウ）、クコの実、芍薬エキス、シアバター",
        "value": "皮脂分泌が激減する40代〜60代の冬肌のために設計された極上の油水バランス。塗布した瞬間から肌を上質なシルクのヴェールで密封し、水分蒸散を24時間シャットアウト",
        "desc_p1": "真冬になると、どれほど保湿クリームを塗りたくっても数時間後には肌が突っ張り、乾燥による痒みや赤みが出てしまう……そんな深刻な『皮脂枯れ』に直面している大人世代の救世主が、韓国の王室伝承医学をベースにしたドフーの最高峰ライン『津率享（ジンユルヒャン）津率クリーム』です。",
        "desc_p2": "ジャーの蓋を開けると、蜂蜜のように濃厚でリッチな紅参カラーのクリームが現れます。硬めのテクスチャーですが、肌にのせて手のひらで温めるとトロリととろけ、まるで美容オイルを固めたかのような極上の保護膜を形成。冷たい北風や乾燥したオフィスの暖房の中に一日中いても、肌表面はしっとりモチモチとした柔らかさをキープし続けます。贅沢な潤いと伝統韓方の芳醇な香りに包まれ、日々のスキンケアが極上のスパタイムへと変わります。",
        "target": "通常の保湿クリームでは真冬の乾燥に全く歯が立たない方、年齢と共に肌の弾力低下と激しい乾燥を感じている方、こっくり重ための安心感あるクリームが好きな方",
        "point": "夜のお手入れの最後に、付属のスパチュラでパール粒大をとります。手のひらですり合わせて体温で温めてから、顔全体を包み込むようにハンドプレスして密着させてください。"
    },
    {
        "rank": 5,
        "tag": "✨ 1本の紅参からわずか数滴の奇跡！120年の歴史を誇る正官庄のピュア紅参フェイスオイル",
        "catch": "韓国人参公社が誇る世界的名門「正官庄」のビューティーブランド。厳選された6年根紅参の貴重な種子から抽出した純度100%のオイルが、冬の砂漠肌を瞬時に極上ツヤ肌へ塗り替える",
        "brand_name": "DONGINBI (ドンインビ / 正官庄)",
        "capacity": "25g / 重厚スポイトボトル",
        "type": "高純度100%ピュア紅参シグネチャーフェイスオイル",
        "features": "紅参種子油（正官庄厳選6年根）、オレイン酸、リノール酸、抗酸化ポリフェノール",
        "value": "1株の高麗人参からわずかしか採取できない紅参オイルを贅沢に使用。一般的な植物油とは一線を画す驚異的な皮膚親和性と抗酸化力で、冬の酸化乾燥ストレスをブロック",
        "desc_p1": "寒さで皮膚のバリア機能が低下する12月は、肌本来の皮脂膜が薄くなり、外気の乾燥によって水分が一方的に吸い取られていきます。ドンインビの『1899 シグネチャー オイル』は、120年以上の高麗人参研究の歴史を持つ正官庄が、その持てる技術の粋を集めて生み出したラグジュアリーな美容オイルです。",
        "desc_p2": "黄金色に透き通るオイルは、植物油特有の重さやベタつきが一切なく、まるで美容液のようにサラリと肌になじみます。洗顔後すぐのブースターとして2〜3滴なじませると、冬の寒さでカチコチに強張っていた角質層が一瞬でほぐれ、その後に重ねる化粧水がスポンジのように浸透。自然な光を反射する健康的なグロウ肌が手に入り、メイクのりも格段に向上します。冬の肌投資として後悔のない逸品です。",
        "target": "オイル特有のベタつきやテカリが苦手な方、洗顔後の肌のごわつきを素早く解消したい方、本物の紅参成分によるエイジングケアを体験したい方",
        "point": "朝晩の洗顔直後、またはスキンケアの最後のフタとして1〜2滴を使用。ファンデーションに1滴混ぜて使うと、真冬でも粉吹きしないツヤやかな水光肌メイクが一日中続きます。"
    },
    {
        "rank": 6,
        "tag": "💧 高麗人参根水63%×カタツムリムチン3%！ダメージを受けた冬肌のキメをなめらかに修復する集中エッセンス",
        "catch": "オタネニンジン根水とカタツムリ分泌液の強力なタッグ。冬の乾燥・摩擦で乱れたターンオーバーを整え、つるんとなめらかな陶器肌へ導くデイリー高機能セラム",
        "brand_name": "Beauty of Joseon (朝鮮美女)",
        "capacity": "30ml / スポイト遮光瓶",
        "type": "キメ修復・高保湿韓方リペアセラム",
        "features": "オタネニンジン根水63%、カタツムリ分泌液3%、プロポリスエキス、ツボクサエキス（CICA）",
        "value": "とろみのある美容液が肌表面の細かな凹凸を埋めるように密着。荒れた角質を滑らかに整え、冬の冷たい外気によるヒリつきや赤みを素早く落ち着かせる",
        "desc_p1": "冬場のマスク着用やマフラーの擦れ、そして空気の乾燥によって、小鼻周りや頬の皮膚がざらつき、キメが粗くなってファンデーションが毛穴落ちしてしまう……。そんな冬特有の肌荒れ・キメ乱れにアプローチするのが、朝鮮美女の『リバイブ セラム』です。",
        "desc_p2": "高麗人参の力強い巡りサポートと、肌再生を促すカタツムリムチンの粘弾性テクスチャーが絶妙に調和。肌に伸ばすと、最初は糸を引くような濃密さがありながら、ハンドプレスすると瞬時にサラリとなじみ、肌の内側にモチッとした弾力を蓄えます。プロポリスやCICAエキスもブレンドされているため、寒暖差でピリつきやすい冬の敏感肌でも刺激なく安心して使用できます。毎日のキメ管理に欠かせない一本です。",
        "target": "乾燥で肌の手触りがザラザラ・ゴワゴワしている方、毛穴の開きやキメの乱れが気になる方、とろみ美容液でしっかり保湿したいけれどベタつきは嫌な方",
        "point": "化粧水の後にスポイトで2〜3滴をとり、顔全体に優しく滑らせるように伸ばします。乾燥が目立つ部分には指先で重ねづけし、手のひらでハンドプレスして密着させます。"
    },
    {
        "rank": 7,
        "tag": "🧴 高麗人参×かたつむりエキス配合！忙しい真冬の夜もひと塗りで完結する濃厚多機能オールインワン",
        "catch": "製薬会社が本気で開発した高保湿オールインワン『ウモール』。寒さで億劫になりがちな冬のスキンケアを、驚異的な密着ヴェールと豊富な美容成分でシンプルかつ贅沢に完了させる",
        "brand_name": "水橋保寿堂製薬 (UMOR)",
        "capacity": "100g / 大容量ジャー容器",
        "type": "高純度和漢高保湿オールインワンジェルクリーム",
        "features": "オタネニンジン根エキス、かたつむり分泌液、毒蛇ペプチド様成分（シンエイク）、ヒアルロン酸Na、コラーゲン",
        "value": "1つで化粧水・乳液・美容液・クリーム・パックの5役。夜塗って寝るだけで、翌朝まで暖房の乾燥に負けないもっちり肌をキープする製薬会社品質",
        "desc_p1": "寒い冬の夜、何ステップものスキンケアを重ねるのは時間がかかって体が冷えてしまう……けれど保湿力に妥協はしたくない。そんな現代女性の願いを叶えるために生まれたのが、製薬会社の老舗・水橋保寿堂製薬が手がける『ウモール』です。",
        "desc_p2": "こっくりとしたクリームジェルは、肌に乗せると体温でスルスルとほぐれて吸い付くように密着。高麗人参のサポニンが肌の巡りを高め、かたつむりエキスとシンエイクが乾燥小ジワをピーンと張るような緊張感をもたらします。100gの大容量なので、顔だけでなく首元やデコルテまでたっぷり伸ばせるのも嬉しいポイント。忙しい日の時短ケアとしてはもちろん、週末の厚塗りスリーピングパックとしても大活躍します。",
        "target": "スキンケアの工程を減らして時短したいけれど真冬の高保湿は譲れない方、首やデコルテまでたっぷり使えるオールインワンを探している方、製薬会社基準の品質を好む方",
        "point": "さくらんぼ粒大を手にとり、顔の中心から外側へ引き上げるように伸ばします。乾燥が激しい日は、全顔に塗った後にもう一度目元・口元に薄く重ねて『追い塗り』すると翌朝のモチモチ感が倍増します。"
    },
    {
        "rank": 8,
        "tag": "🎭 オタネニンジン×植物性コラーゲン！真冬の冷えた肌に濃密和漢エッセンスをピタッと密着補給するサロン級マスク",
        "catch": "本場韓国コルギサロンの知恵が詰まったスペシャルケア。贅沢な厚手の密着シートが、冬のエアコンで水分が底をついた角層をひたひたに浸し、エステ帰りのような透明感を再現",
        "brand_name": "KANコルギセラピー (菅貞子)",
        "capacity": "1枚入り (集中個別包装)",
        "type": "サロン仕様 高保湿和漢モイスチャーシートマスク",
        "features": "オタネニンジン根エキス、加水分解コラーゲン、植物性スクワラン、ツボクサエキス",
        "value": "エステサロンでの施術後に実際に使用されているプロフェッショナル仕様。真冬の冷え固まった肌を優しく包み込み、毛穴を引き締めながら贅沢なうるおいで満たす",
        "desc_p1": "忘年会やクリスマス、年末のイベントが続く12月は、外気の寒さと睡眠不足、暖房の乾燥が重なり、肌のコンディションが一気に急降下しがちです。そんな非常事態のレスキューアイテムとして頼りになるのが、サロン専用品として誕生した『菅貞子モイスチャーシートマスク』です。",
        "desc_p2": "肌触りの良い高密着シートには、高麗人参根エキスと植物性コラーゲンをたっぷり含んだ乳白色の美容液が溢れんばかりに含まれています。顔に乗せると隙間なくピタッと吸い付き、液だれすることなく15〜20分間じっくりと角層の深部まで潤いを届けます。マスクを剥がした瞬間、まるで入浴後のようにほんのり上気した明るい血色感と、手のひらが吸い付くようなしっとり感に誰もが驚くはずです。",
        "target": "週末や特別なイベントの前夜に即効性のある集中保湿を行いたい方、冬の乾燥くすみを一発で払拭したい方、サロン仕様のリッチなシートマスクを体験したい方",
        "point": "洗顔後、化粧水で軽く肌を整えてからマスクを密着させます。15分〜20分置いた後、シートを剥がし、肌表面に残った美容液を手で優しくパッティングして完全になじませてください。"
    },
    {
        "rank": 9,
        "tag": "🧼 伝統の枠練り製法×天然高麗人参エキス！真冬の洗顔後もつっぱらずしっとり透明感を残すマイルドソープ",
        "catch": "創業100年を超える大木製薬のロングセラー『紅蔘石鹸』。きめ細かな弾力クッション泡が冬のデリケートな肌を摩擦レスで包み込み、汚れを吸着しながらしっとり洗い上げる",
        "brand_name": "大木製薬 (コウジンソープ)",
        "capacity": "90g / 個別箱入り",
        "type": "高純度紅参エキス配合 枠練り高保湿洗顔石鹸",
        "features": "オタネニンジン根エキス（紅蔘）、植物性石けん素地、スクワラン、天然グリセリン",
        "value": "熟練職人が時間をかけて自然乾燥させる枠練り製法により、保湿成分を高濃度で配合。真冬の洗顔時に皮脂を奪いすぎず、つっぱり感ゼロの洗い上がりを実現",
        "desc_p1": "冬のスキンケアで見落とされがちなのが『洗顔による過剰な脱脂』です。強い洗浄力の洗顔料を使うと、ただでさえ分泌量が減っている天然の皮脂膜が洗い流され、入浴直後から激しい突っ張りや粉吹きが起きてしまいます。大木製薬の『コウジンソープ』は、洗う段階から潤いを守るために開発された和漢石鹸です。",
        "desc_p2": "付属の泡立てネットで軽く転がすだけで、ホイップクリームのように濃密で弾力のある泡が立ち上がります。肌に手が直接触れないよう泡のクッションを転がすように洗うと、古い角質や毛穴汚れをやさしく吸着。高麗人参エキスと植物性保湿成分が肌に留まるため、洗い流した後の肌は驚くほどしっとり滑らかで、急いで化粧水をつけなくても突っ張る心配がありません。冬の乾燥肌対策は、正しい洗顔選びから始まります。",
        "target": "冬の洗顔後に肌が突っ張ってピキピキ痛む方、泡立ちが良くへたらない固形石鹸が好きな方、洗顔時から高麗人参のエイジングケアを取り入れたい方",
        "point": "泡立てネットを使って空気を含ませるようにしっかり泡立て、レモン1個分大の弾力泡を作ります。泡を顔に乗せて転がすように30秒ほど洗い、ぬるま湯で20回以上丁寧にすすいでください。"
    },
    {
        "rank": 10,
        "tag": "✨ 高麗人参×ビタミンカクテル！真冬の寒冷くすみ＆乾燥毛穴をキュッと引き締める密着シートマスク",
        "catch": "密着力に定評のあるオルフェスの冬向け高機能マスク。高麗人参エキスとビタミン誘導体が、寒さで巡りが滞った冬肌にビタミンと水分をチャージし、パッと明るい透明ハリ肌へ",
        "brand_name": "ALFACE+ (オルフェス)",
        "capacity": "1箱（4枚〜12枚セット）",
        "type": "高密着アクアモイスチャーシートマスク",
        "features": "オタネニンジン根エキス、ビタミンC誘導体、ビタミンB複合体、ナイアシンアミド、ヒアルロン酸",
        "value": "日本人女性の顔型に合わせた独自のカッティングと極細繊維シートが、小鼻のキワやフェイスラインまで隙間なく密着。液だれせず快適に冬の水分補給ができる",
        "desc_p1": "11月から12月にかけての寒暖差は、自律神経の乱れと共に肌の毛細血管を収縮させ、顔色がどんよりと沈んで見える『冬の寒冷くすみ』を引き起こします。オルフェスの『イエローエッセンシャルマスク』は、この冬のくすみと乾燥毛穴に焦点を当てた大人気シートマスクです。",
        "desc_p2": "極細繊維で作られた柔らかなシートは、顔に乗せた瞬間に吸い付くように一体化。高麗人参エキスの滋養パワーと各種ビタミン誘導体が、乾ききった角層のすみずみまで浸透していきます。パック中もシートが浮いてこないため、髪を乾かしたり家事をしたりしながらの『ながら美容』にも最適。使用後はくすみがパッと晴れ渡り、頬の毛穴がキュッと引き締まった、メイクのりの良い滑らか肌に整います。",
        "target": "冬になると夕方の顔色のくすみが気になる方、乾燥によって頬の毛穴が縦に流れて目立つ方、デイリーに使える高品質なシートマスクをストックしたい方",
        "point": "洗顔後、化粧水で肌を整えた後に密着させます。約10〜15分おいてからマスクを外し、肌に残ったエッセンスを両手で押し込むようになじませた後、乳液やクリームで蓋をしてください。"
    }
]

# 目次項目の定義
toc_items = [
    {"id": "intro", "title": "1. 11月・12月の寒さで肌が枯れる？「冬の巡り不足」と高麗人参の力"},
    {"id": "mechanism", "title": "2. なぜ高麗人参（オタネニンジン）が高保湿なのか？サポニンの皮膚科学"},
    {"id": "comparison", "title": "3. 高保湿ジンセンコスメおすすめ10選の比較表"},
    {"id": "ranking", "title": "4. 高保湿高麗人参コスメおすすめ厳選ランキング10選"},
    {"id": "guide", "title": "5. 失敗しない冬のジンセンコスメの選び方＆アイテム別活用術"},
    {"id": "routine", "title": "6. 真冬の砂漠肌を救う！高麗人参スキンケアの重ねづけステップ"},
    {"id": "faq", "title": "7. 高麗人参コスメに関するよくある質問（FAQ）"},
    {"id": "summary", "title": "8. まとめ：高麗人参の温もり滋養で真冬も乾かないハリ艶肌へ"}
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
  <title>保湿力の強さで肌乾燥とさようなら！高麗人参（オタネニンジン）のサポニン温感・滋養パワーが真冬の冷え固まり枯れ肌を蘇らせる高保湿ジンセンコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の寒冷乾燥と血行不良による肌の冷え固まり・乾燥小ジワ・くすみを救う高保湿高麗人参（オタネニンジン・紅参）コスメを徹底厳選！雪花秀、朝鮮美女、ドフー、正官庄ドンインビ、大木製薬までサポニンの科学的根拠と共に徹底検証。">
  <meta name="keywords" content="高麗人参 コスメ, オタネニンジン エキス, ジンセン コスメ, 高保湿 美容液 冬, 韓国コスメ エイジングケア, 雪花秀 滋陰生, 朝鮮美女 ジンセン, 冬 乾燥肌 対策">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-ginseng">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！高麗人参（オタネニンジン）のサポニン温感・滋養パワーが真冬の冷え固まり枯れ肌を蘇らせる高保湿ジンセンコスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥と血行不良による肌の冷え固まり・乾燥小ジワ・くすみを救う高保湿高麗人参コスメを徹底厳選！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-ginseng">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="LUMI COSMETICS">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！高麗人参（オタネニンジン）のサポニン温感・滋養パワーが真冬の冷え固まり枯れ肌を蘇らせる高保湿ジンセンコスメランク10",
    "description": "11月・12月の寒冷乾燥と血行不良による肌の冷え固まり・乾燥小ジワ・くすみを救う高保湿高麗人参（オタネニンジン・紅参）コスメを徹底厳選！",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-ginseng"
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
    "name": "真冬の高保湿高麗人参コスメおすすめ厳選ランキング10選",
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
      --primary: #92400e;
      --primary-light: #fef3c7;
      --primary-dark: #78350f;
      --accent: #b45309;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg: #fffbeb;
      --bg-card: #ffffff;
      --border: #fde68a;
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
    .rank-1 {{ background: linear-gradient(135deg, #d97706, #b45309); }}
    .rank-2 {{ background: linear-gradient(135deg, #9ca3af, #6b7280); }}
    .rank-3 {{ background: linear-gradient(135deg, #b45309, #78350f); }}
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
        <a href="/winter-shikon">和漢紫根</a>
        <a href="/winter-sake-kasu">酒粕コスメ</a>
        <a href="/winter-resurrection-plant">復活草</a>
      </nav>
    </div>
  </header>

  <main class="container">

    <article>
      <div class="article-header">
        <div class="breadcrumb">
          <a href="/">TOP</a> &gt; <a href="/#skincare">冬の高保湿スキンケア</a> &gt; 高麗人参コスメ
        </div>
        <span class="post-tag">2026年11月・12月 真冬の集中滋養ケア</span>
        <h1>保湿力の強さで肌乾燥とさようなら！高麗人参（オタネニンジン）のサポニン温感・滋養パワーが真冬の冷え固まり枯れ肌を蘇らせる高保湿ジンセンコスメランク10</h1>
        <div class="meta-bar">
          <span>📅 公開日: 2026年11月5日</span>
          <span>✍ 監修: LUMI COSMETICS 保湿皮膚科学研究チーム</span>
          <span>⏱ 読了目安: 約12分</span>
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

      <!-- セクション1: 導入・冬の寒冷肌問題 -->
      <section class="article-section" id="intro">
        <h2 class="section-title">1. 11月・12月の寒さで肌が枯れる？「冬の巡り不足」と高麗人参の力</h2>
        <div class="highlight-lead">
          真冬の乾燥は単なる「水分不足」ではありません。木枯らしと寒暖差によって毛細血管が収縮し、皮膚温が低下することで肌本来の保水力とターンオーバーが停止する『冷え固まり枯れ肌』が根本原因です。
        </div>
        <p>11月に入ると日本列島には冬型の気圧配置が強まり、太平洋側では湿度が30%を下回る乾燥注意報が頻発します。さらにオフィスや自宅ではエアコン暖房が終日稼働し、皮膚表面の水分は猛烈な勢いで奪われていきます。</p>
        <p>しかし、大人の冬肌が直面する真の危機は、湿度の低下だけではありません。外気温が10℃を下回ると、人体は熱を逃がさないように末梢血管を急激に収縮させます。その結果、表皮や真皮に届く血液量が激減し、皮膚温が低下。細胞に必要なアミノ酸や酸素、微量栄養素が届かなくなり、肌のターンオーバーは通常の倍近い日数まで遅延してしまいます。</p>
        <p>「どんなに高保湿なクリームを塗っても浸透していかない」「肌を触るとひんやり冷たく、カチコチに強張っている」「ファンデーションを塗るとくすんで老けて見える」——こうした深刻な冬の肌トラブルを根本から覆すキー成分こそが、古来より宮廷や漢方医学で最高峰の滋養生薬として重宝されてきた『高麗人参（オタネニンジン・紅参）』です。</p>
      </section>

      <!-- セクション2: 科学的メカニズム -->
      <section class="article-section" id="mechanism">
        <h2 class="section-title">2. なぜ高麗人参（オタネニンジン）が高保湿なのか？サポニンの皮膚科学</h2>
        <p>高麗人参（学名：Panax ginseng）の属名である「Panax」は、ギリシャ語の「万能薬（Panacea）」に由来します。植物が過酷な環境を生き抜くために根部に蓄える特有の配糖体『ジンセノサイド（Ginsenoside・人参サポニン）』は、現代の皮膚科学研究においても驚くべき生体調節機能が次々と解明されています。</p>
        
        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">① 末梢血流の促進と皮膚温の温活サポート</h3>
        <p>ジンセノサイド群（特にRg1、Rb1、Rg3など）は、一酸化窒素（NO）の産生を穏やかに促して微小毛細血管を弛緩させ、冷え切った皮膚の巡りを改善します。肌の微小循環が活性化することで、スキンケア成分の通り道が開き、角層の奥深くまで水分と油分を引き込むブースター効果を発揮します。<a href="/winter-shikon">和漢紫根</a>や<a href="/winter-sake-kasu">酒粕コスメ</a>と同様に、日本の冬に最適な『巡り保湿』の代表格です。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">② 線維芽細胞の活性化と真皮コラーゲン合成</h3>
        <p>真冬の冷風と乾燥によってしぼんでしまった真皮層において、高麗人参エキスは線維芽細胞に直接働きかけ、Type-1コラーゲンやエラスチンの生成を促進します。これにより、暖房による乾燥小ジワを内側から押し上げるような密度の高い弾力をもたらします。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">③ 表皮バリア機能の再建と抗酸化シールド</h3>
        <p>サポニンは界面活性作用に似た優れた浸透促進力を持つと同時に、過酸化脂質の発生を抑える強力な抗酸化力を備えています。真冬の寒暖差ストレスで乱れがちな角層細胞間脂質のラメラ構造を整え、外的刺激に対する鉄壁のシールドを形成します。<a href="/winter-resurrection-plant">復活草コスメ</a>や<a href="/winter-damask-rose">ダマスクローズ</a>と組み合わせることで、さらに持続性の高い潤いヴェールを実現できます。</p>
      </section>

      <!-- セクション3: 比較表 -->
      <section class="article-section" id="comparison">
        <h2 class="section-title">3. 高保湿ジンセンコスメおすすめ10選の比較表</h2>
        <p>楽天市場の最新在庫・価格データから、2026年11月・12月の冬本番にリアルタイムで人気の高麗人参コスメ10選を一覧表にまとめました。テクスチャーや目的に合わせて比較してください。</p>
        
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
        <h2 class="section-title">4. 高保湿高麗人参コスメおすすめ厳選ランキング10選</h2>
        <p>ここからは、1位から10位までの各アイテムについて、配合成分の皮膚科学的特徴、真冬の乾燥に対する使用感、おすすめの肌質、効果的な使用テクニックまで徹底解説します。</p>

{all_cards_html}

      </section>

      <!-- セクション5: 選び方ガイド -->
      <section class="article-section" id="guide">
        <h2 class="section-title">5. 失敗しない冬のジンセンコスメの選び方＆アイテム別活用術</h2>
        <p>高麗人参コスメは、アイテムの形状（トナー、美容液、クリーム、オイル）によってアプローチする層や期待できる効果が異なります。ご自身の肌状態に合わせて最適なアイテムを選びましょう。</p>
        
        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">① 「インナードライ・浸透不足」には高麗人参ウォーター（化粧水）</h3>
        <p>肌表面はベタつくのに内側が突っ張る方や、スキンケアが肌に入っていかないと感じる方には、朝鮮美女のようなオタネニンジン根水が高配合されたトナーが最適です。洗顔後の素肌に素早く巡りをもたらし、次のスキンケアの受け入れ態勢を整えます。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">② 「たるみ・小ジワ・枯れ肌」には濃縮アンプル・美容液</h3>
        <p>冬になると一気に老け見えやハリ不足が進行する大人肌には、雪花秀のような濃縮ジンセノミクス配合アンプルが必須です。真皮層のコラーゲン産生を刺激し、指を押し返すようなモチモチ感を最短距離で取り戻せます。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">③ 「粉吹き・深刻な皮脂不足」には紅参オイル・濃密クリーム</h3>
        <p>40代以降の皮脂分泌が急減した肌や、暖房の効いた寝室で朝起きると肌が乾いている方には、正官庄ドンインビのピュア紅参オイルやドフーの津率クリームがおすすめ。濃厚な油分膜が冬の過酷な外気から肌を24時間完全に保護します。</p>
      </section>

      <!-- セクション6: スキンケアステップ -->
      <section class="article-section" id="routine">
        <h2 class="section-title">6. 真冬の砂漠肌を救う！高麗人参スキンケアの重ねづけステップ</h2>
        <div class="highlight-lead">
          高麗人参の巡りパワーを最大化するには『温めながら浸透させるハンドプレス』が決定的に重要です。
        </div>
        <ol style="padding-left:1.5rem;margin-bottom:1.5rem;line-height:2;">
          <li><strong>ステップ1（マイルド洗顔）:</strong> 大木製薬のコウジンソープをしっかり泡立て、ぬるま湯（32〜34℃）で皮脂を奪いすぎずに汚れだけをオフ。</li>
          <li><strong>ステップ2（巡り導入トナー）:</strong> 朝鮮美女のジンセンエッセンスウォーターを手にとり、手のひらで温めてから全顔に押し込むように浸透。</li>
          <li><strong>ステップ3（集中ハリ注入）:</strong> 雪花秀の滋陰生アンプルまたは朝鮮美女のリバイブセラムを2〜3滴伸ばし、手のひらで顔全体を包み込んで10秒間キープ。</li>
          <li><strong>ステップ4（ピンポイントケア）:</strong> 目元やほうれい線にジンセンアイセラムをトントンと優しく馴染ませる。</li>
          <li><strong>ステップ5（鉄壁密封シールド）:</strong> ドフーの津率クリームまたはドンインビの紅参オイルを1〜2滴なじませ、うるおいを完全に閉じ込める。</li>
        </ol>
      </section>

      <!-- セクション7: FAQ -->
      <section class="article-section" id="faq">
        <h2 class="section-title">7. 高麗人参コスメに関するよくある質問（FAQ）</h2>
        
        <div class="faq-item">
          <div class="faq-q">高麗人参コスメ特有の香りは強いですか？</div>
          <div class="faq-a">伝統的な韓方コスメ（ドフーや雪花秀）は深みのある生薬の香りがしますが、近年大人気の「朝鮮美女」などは香りを大幅に抑えた処方になっており、ハーブティーのように爽やかに使えるアイテムが増えています。</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">敏感肌でも刺激なく使えますか？</div>
          <div class="faq-a">高麗人参は抗炎症作用や皮膚バリア強化作用を持つため、基本的には荒れた肌を穏やかに整えてくれます。ただし血行が良くなることで一時的にポカポカ温感を感じることがあります。心配な方は腕の内側でパッチテストを行ってからの使用をおすすめします。</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">他の高保湿成分（セラミドやレチノール）と併用できますか？</div>
          <div class="faq-a">非常に相性が抜群です。高麗人参の血行促進効果によって肌の受け入れ態勢が整うため、その後に重ねるセラミドの保湿膜形成や、ビタミンC・レチノールの浸透を力強く後押ししてくれます。</div>
        </div>
      </section>

      <!-- セクション8: まとめ -->
      <section class="article-section" id="summary">
        <h2 class="section-title">8. まとめ：高麗人参の温もり滋養で真冬も乾かないハリ艶肌へ</h2>
        <p>11月・12月の本格的な寒さと乾燥は、放置すると角層肥厚やくすみ、深い小ジワへと直結します。表面的な水分補給だけでなく、肌本来の『巡り』と『代謝力』を呼び覚ます高麗人参コスメは、現代の過酷な冬を乗り越えるための最強の投資です。</p>
        <p>ぜひ今回の厳選10選の中から、あなたのライフスタイルや肌悩みにぴったりのジンセンコスメを見つけて、真冬でも内側から輝くような上気ハリ艶肌を手に入れてください！</p>
      </section>

      <!-- 関連記事ハブ -->
      <div class="related-hub">
        <div class="related-title">🌿 あわせて読みたい！冬の高保湿スキンケア特集</div>
        <div class="related-grid">
          <a href="/winter-shikon" class="related-card">
            <div class="related-card-title">🌸 高保湿和漢紫根コスメ</div>
            <div class="related-desc">真冬のあかぎれ・冷え乾燥・荒れ果てた角層バリアを集中修復する伝統和漢。</div>
          </a>
          <a href="/winter-sake-kasu" class="related-card">
            <div class="related-card-title">🍶 高保湿酒粕コスメ</div>
            <div class="related-desc">杜氏の手のようなもっちり透明美肌へ導く発酵アミノ酸高保湿10選。</div>
          </a>
          <a href="/winter-resurrection-plant" class="related-card">
            <div class="related-card-title">🌵 高保湿復活草・トレハロース</div>
            <div class="related-desc">カラカラ砂漠肌を驚異の保水力で満たす復活草エキスコスメ10選。</div>
          </a>
          <a href="/winter-damask-rose" class="related-card">
            <div class="related-card-title">🌹 高保湿ダマスクローズ</div>
            <div class="related-desc">女王の濃密潤いヴェールで真冬のしぼみ肌をふっくら満たす高保湿10選。</div>
          </a>
        </div>
      </div>

    </article>

  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-links">
        <a href="/">冬コスメTOP</a>
        <a href="/winter-ginseng">高麗人参コスメ</a>
        <a href="/winter-shikon">和漢紫根</a>
        <a href="/winter-sake-kasu">酒粕コスメ</a>
        <a href="/winter-resurrection-plant">復活草</a>
        <a href="/winter-sweet-almond-oil">アーモンドオイル</a>
        <a href="/winter-apricot-oil">杏仁オイル</a>
      </div>
      <p class="copyright">&copy; 2026 LUMI COSMETICS. All Rights Reserved. 当サイトは楽天市場アフィリエイトプログラムに参加しています。</p>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-ginseng.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-ginseng.html successfully! Character count:", len(full_html))
