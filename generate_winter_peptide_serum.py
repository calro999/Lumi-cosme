import json
import re

with open("fetched_3new_nov_dec_ceramide_peptide_hair_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_peptide_serum"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 多重ペプチド技術の世界的金字塔！大人の冬枯れ小ジワを多角的に押し返す",
        "catch": "旧ビュッフェの進化形。マトリキシル・シンエイク・ヒアルロン酸が凝縮された贅沢セラム",
        "brand_name": "The Ordinary (ジオーディナリー)",
        "capacity": "30ml (マルチペプチド + HA セラム)",
        "type": "高濃度マルチペプチド＆多重ヒアルロン酸配合・集中エイジングセラム",
        "features": "Matrixyl 3000、シンエイクペプチド、ARGIRELOXペプチド、複数分子ヒアルロン酸、アミノ酸",
        "value": "世界中のスキンケア愛好家を熱狂させた成分特化美容液。冬の寒冷でこわばった表情筋周辺をほぐし、乾燥による浅いシワから深い刻まれジワまで包括アプローチ",
        "desc_p1": "11月から12月にかけて気温が一段と低下すると、顔の筋肉や皮膚が寒さで収縮し、笑った時や話した時にできる表情ジワが乾燥によってそのまま形状記憶されやすくなります。一般的な保湿美容液では追いつかないこの『冬の乾燥ジワ進行』に、世界的なメガヒットを記録しているのがThe Ordinaryの『マルチペプチド + HA セラム』です。",
        "desc_p2": "肌の弾力線維をサポートするマトリキシル複合体、塗るボトックスとも称されるアルジレロックスペプチド、そして多様な分子サイズのヒアルロン酸を高濃度ブレンド。少しとろみのあるリッチなテクスチャーが肌に触れた瞬間に素早く馴染み、乾燥でペタンコにしぼんだ角層細胞をふっくらと持ち上げます。毎日の朝晩のお手入れに組み込むことで、暖房による夕方の目尻やほうれい線のファンデーション割れを防ぎ、弾力に満ちたハリツヤ肌へと導きます。",
        "target": "冬になると目元やほうれい線の小ジワが目立ち始める方、高機能ペプチドを本格的な濃度で試したい方、化粧崩れやシワ落ちを防ぎたい方",
        "point": "朝晩の洗顔後、化粧水の直後に数滴を手に取り、顔全体から首筋にかけて塗布。特に乾燥小ジワが気になる目尻や口元には、指先で優しくトントンと押し込むように重ね付けしてください。"
    },
    {
        "rank": 2,
        "tag": "🧬 韓国オリーブヤング1位の塗るハイフ！独自ペプチドが真冬のたるみ毛穴をキュッと引き締める",
        "catch": "バイオヒールボが誇るタンタン（ハリ弾力）技術。乳酸菌バイオームと複合ペプチドが輪郭をサポート",
        "brand_name": "BIOHEAL BOH (バイオヒールボ)",
        "capacity": "30ml (プロバイオダーム コラーゲン リフティング アンプル)",
        "type": "特許バイオーム＆独自ペプチド配合・高密着リフティングアンプル",
        "features": "プロバイオダーム（特許乳酸菌）、12種の複合ペプチド、低分子コラーゲン、エラスチン",
        "value": "『塗るハイフ』としてSNSで話題沸騰。冬の寒さで代謝が落ち、重力に負けて広がる乾燥毛穴を内側からぎゅっと引き締める",
        "desc_p1": "真冬の冷えは皮膚温を低下させ、コラーゲンやエラスチンの産生スピードをダウンさせます。その結果、頬の毛穴が縦に伸びて楕円形に広がり、顔全体が疲れた印象を与えてしまいます。韓国のヘルス＆ビューティストア『オリーブヤング』で弾力ケア部門を独占するバイオヒールボのアンプルは、この冬のたるみ毛穴・しぼみ肌の救世主です。",
        "desc_p2": "独自のプロバイオティクス発酵成分と、厳選された12種類のペプチドコンプレックスが肌の弾力構造に働きかけます。糸を引くような濃密なとろみがありながら、肌に乗せると不思議なほどスッと吸い込まれ、ベタつきを残さずピンとしたハリ膜を形成。夜塗って寝ると、翌朝鏡を見た瞬間に頬の位置が高くなったような密度の高さを実感できます。",
        "target": "冬の乾燥で頬の毛穴が縦に流れて目立つ方、フェイスラインのもたつきが気になる方、韓国の最先端リフティングスキンケアを体験したい方",
        "point": "化粧水で肌を整えた後、スポイトで頬と額に直接滴下し、顔の中心からこめかみに向かって優しく引き上げるようになじませます。同シリーズのタンタンクリームとの併用で効果が倍増します。"
    },
    {
        "rank": 3,
        "tag": "✨ 3重コラーゲン×高保湿ペプチド！真冬の乾いた肌にガラスのような水光ツヤを宿す",
        "catch": "メディキューブの超濃密スキンケア。異なる分子量のコラーゲンとペプチドが24時間輝きをキープ",
        "brand_name": "medicube (メディキューブ)",
        "capacity": "55ml (トリプル コラーゲン セラム)",
        "type": "高純度3重コラーゲン＆ペプチド配合・水光弾力セラム",
        "features": "高分子・中分子・低分子コラーゲン（20,000ppm）、アセチルヘキサペプチド、アデノシン、ナイアシンアミド",
        "value": "肌の深層から表面まで各層に合わせたコラーゲンとペプチドを配置。冬の暖房直下でも乾燥せず、内側から発光するような極上のツヤ肌へ",
        "desc_p1": "11月以降の乾燥外気は、肌表面の水分だけでなく、みずみずしい光の反射（キメの均一さ）を奪い去り、顔全体をどんよりとくすませます。メディキューブの『トリプル コラーゲン セラム』は、肌に潤いと光を宿すために設計された、まさに冬のための水光美容液です。",
        "desc_p2": "超低分子から高分子まで3段階のコラーゲンを贅沢に20,000ppm配合し、ペプチドがそのコラーゲンの働きを力強くバックアップ。乳白色のとろりとしたリッチな美容液が肌に密着し、角層の隙間を水分で満たしながら上質なツヤのヴェールを形成します。乾燥によるゴワつきが一掃され、ファンデーションを重ねた時にまるで内側から光を放つような透明感あふれるベースメイクが完成します。",
        "target": "冬になると肌がくすんで生気がなくなる方、乾燥によるキメの乱れを即効リセットしたい方、韓国アイドルのような水光肌に憧れる方",
        "point": "洗顔後、化粧水の後に1〜2プッシュを顔全体に伸ばし、手のひらで温めながら優しくハンドプレス。乾燥しやすいハイライトゾーン（頬骨の上）に薄く重ねると自然なツヤが引き立ちます。"
    },
    {
        "rank": 4,
        "tag": "🔬 天然マイクロニードル×リフティングペプチド！美容成分を角層深層へダイレクト注入",
        "catch": "大ヒットリードルショットのエイジング特化版。チクチク心地よい刺激とともにペプチドが深部へ浸透",
        "brand_name": "VT COSMETICS (ブイトー)",
        "capacity": "30ml (リードルショット リフティング セラム)",
        "type": "天然スピキュール配合・高浸透ペプチドリフティングセラム",
        "features": "CICA REEDLE（天然シリカ微細針）、VDSリフティングペプチド複合体、ヒアルロン酸、エラスチン",
        "value": "角層の浸透障壁を微細針が物理的に突破。冬の硬くなった角質層の奥深くまでリフティングペプチドを送り届ける最新イノベーション",
        "desc_p1": "冬の寒さで角質が分厚く硬くなると、どれほど高級な美容液を塗っても肌表面で滑ってしまい、奥まで浸透しない『浸透の停滞』が起こります。この課題をクリアしたのが、美容界に旋風を巻き起こしたVTのリードルショットシリーズから登場した『リフティング セラム』です。",
        "desc_p2": "天然の微細針（スピキュール）が肌を心地よく刺激しながら美容成分の通り道をつくり、独自のVDSリフティングペプチドが角層の深部へとダイレクトにデリバリーされます。塗布直後は微細なチクチク感がありますが、これが肌の目覚めの合図。翌朝には肌の内側から跳ね返るような弾力と、引き締まったキメを体感できます。冬のたるみや小ジワを本気で攻めたい方に最適なアプローチです。",
        "target": "冬になってスキンケアの浸透が悪くなったと感じる方、本格的なホームエステ級のリフトケアをしたい方、話題の針コスメを試したい方",
        "point": "夜の洗顔後、化粧水で肌を整えた後に適量を手に取り、顔全体に塗り広げた後、指の腹で垂直に押し込むようにハンドプレスします。目元や口元は擦らないように注意してください。"
    },
    {
        "rank": 5,
        "tag": "🌿 ビフィズス菌発酵エキス×多重ペプチド！冬の寒暖差に負けない強靭な肌基礎力を育てる",
        "catch": "魔女工場の名品アンプル。発酵サイエンスとペプチドが角層バリアを強固にし、ハリ密度を底上げ",
        "brand_name": "manyo (魔女工場)",
        "capacity": "50ml (ビフィダ バイオーム コンプレックス アンプル)",
        "type": "発酵マイクロバイオーム＆多機能ペプチド配合・肌バリア修復アンプル",
        "features": "ビフィズス菌培養溶解質、5種のプロバイオティクス、アセチルヘキサペプチド-8、カッパーペプチド、10重ヒアルロン酸",
        "value": "敏感肌でも安心して毎日使える発酵ペプチド設計。冬の寒暖差ストレスで乱れがちな肌の常在菌環境を整え、ふっくらとした健康的なキメを蘇らせる",
        "desc_p1": "冬の朝の凍える冷気から、暖房の効いた室内への移動。この急激な寒暖差は肌の自律神経を疲弊させ、バリア機能を急激に弱らせます。韓国コスメ界で数え切れないほどのベストコスメを獲得し続ける魔女工場の『ビフィダ バイオーム コンプレックス アンプル』は、肌の土台そのものを強化する名品です。",
        "desc_p2": "高濃度のビフィズス菌発酵エキスに、筋肉の緊張を穏やかに和らげるアセチルヘキサペプチド-8や、組織修復を助ける銅ペプチドを贅沢にブレンド。肌に乗せるとウォータリーでみずみずしく、肌荒れを防ぎながら角層細胞のすき間を潤いで満たします。刺激感が一切ないため、冬の寒風でデリケートに傾いた肌でも心地よく使え、使い続けるほどに日中の乾燥に揺らがない強い肌が育ちます。",
        "target": "冬の寒暖差で肌が荒れやすく赤みが出やすい方、発酵コスメの肌育効果を実感したい方、低刺激でハリケアを始めたい方",
        "point": "朝晩の洗顔後、化粧水の後にスポイト1回分を取り、手のひらで顔全体を包み込むように馴染ませます。冬場は首筋やデコルテまで広げるのがおすすめです。"
    },
    {
        "rank": 6,
        "tag": "🔬 国産・高濃度ペプチド原液100%！成分主義ブランドが贈る直球ハリ弾力ブースト",
        "catch": "余計な添加物を一切排除。塗るボトックス成分をダイレクトに肌へ届ける贅沢原液",
        "brand_name": "KISO (キソ)",
        "capacity": "30ml (ピュアエッセンス PE ペプチド 原液)",
        "type": "高純度アセチルヘキサペプチド-8原液100%配合・エイジング特化セラム",
        "features": "アセチルヘキサペプチド-8（アルジルリン）高濃度原液、グリセリン、無香料・無着色・パラベンフリー",
        "value": "成分特化ブランドKISOの真骨頂。美容クリニックのボトックス注射に着想を得たペプチド成分を、余分な混ぜ物なしで肌に届けられる直球アプローチ",
        "desc_p1": "『特定の成分だけを高濃度でピンポイントに使いたい』というコスメ愛好家から圧倒的な支持を集めるKISO。その中でも冬の小ジワ対策として注文が殺到するのが『ピュアエッセンス PE ペプチド 原液』です。12月の寒さで深く刻まれる額や眉間、目元の乾燥小ジワに原液パワーが直撃します。",
        "desc_p2": "成分表の主役であるアセチルヘキサペプチド-8は、神経伝達物質の過剰な放出を抑え、筋肉のこわばりによるシワの形成を予防するアプローチで知られます。さらりとした軽やかな液状で、手持ちの化粧水やクリームに数滴混ぜてカスタマイズすることも可能。無添加処方で肌への負担がなく、真冬の乾燥で硬くなった皮膚をふっくらとほぐし、ピンとした張りを蘇らせます。",
        "target": "表情ジワや眉間のシワが気になり始めた方、成分特化の原液コスメを愛用する方、手持ちのスキンケアをパワーアップさせたい方",
        "point": "化粧水の直後、スポイトから直接気になるシワ（目尻、眉間、額、ほうれい線）に1〜2滴落とし、指先で優しく馴染ませます。手持ちのクリームに2滴混ぜて使うのもおすすめです。"
    },
    {
        "rank": 7,
        "tag": "🧱 マトリキシル3000×アルジルリンの黄金タッグ！高濃度ペプチドで大人のハリ密度を再建",
        "catch": "韓国コスデバハの成分特化アンプル。アロエベラ葉エキスベースで冬の乾燥肌を徹底鎮静＆リフト",
        "brand_name": "Cos De BAHA (コスデバハ)",
        "capacity": "30ml (ペプチド フェイシャル セラム (P))",
        "type": "高濃度マトリキシル＆アルジルリン配合・オーガニック高保湿セラム",
        "features": "マトリキシル3000、アルジルリン、オーガニックアロエベラ葉エキスベース、ヒアルロン酸、ベタイン",
        "value": "精製水ではなくオーガニックアロエベラ葉エキスをベースに使用。高濃度ペプチドの引き締め効果とアロエの深い保湿・鎮静効果が冬の乾燥肌を救済",
        "desc_p1": "成分濃度とコストパフォーマンスの高さで世界的な人気を誇る韓国のダーマコスメ・コスデバハ。冬の乾燥とエイジングサインに同時に立ち向かうために作られたのが『ペプチド フェイシャル セラム (P)』です。",
        "desc_p2": "肌の土台を支えるマトリキシル3000と表情ジワに働きかけるアルジルリンを高濃度で配合。ベースに精製水ではなくアロエベラ葉エキスを採用しているため、冬の寒風で炎症を起こしがちなデリケートな素肌を優しく鎮静しながら、角層の奥まで濃密な潤いを届けてくれます。少しとろみのあるジェル状で肌にピタッと密着し、時間が経っても乾燥しない持続的なもっちり感を叶えます。",
        "target": "コスパに優れた高濃度ペプチド美容液を探している方、冬の乾燥と同時に赤みや肌荒れもケアしたい方、アロエの保湿力が好きな方",
        "point": "朝晩の化粧水後、適量を手に取り顔全体に優しく塗り広げます。夜はほうれい線やフェイスラインに沿って下から上へ引き上げるようにマッサージを。"
    },
    {
        "rank": 8,
        "tag": "🌿 ドクダミ77%×浸透ペプチドで鎮静保湿！冬のゆらぎ肌を整えながらキメ密度を回復",
        "catch": "アヌアの大人気鎮静アンプル。冬の寒暖差による赤み・乾燥トラブルを優しく包み込む",
        "brand_name": "Anua (アヌア)",
        "capacity": "30ml (ドクダミ 77% スージング アンプル)",
        "type": "高濃度ドクダミエキス＆ペプチド配合・低刺激鎮静高保湿アンプル",
        "features": "ドクダミエキス77%、パンテノール、セラミドNP、ヒアルロン酸、低刺激ペプチド",
        "value": "赤みや乾燥トラブルが多発する冬のゆらぎ肌に。ドクダミの圧倒的な鎮静力とペプチドのハリ修復効果で、荒れ知らずの滑らか肌をキープ",
        "desc_p1": "冬は乾燥だけでなく、マスクの摩擦や室外と室内の温度差によって、肌が赤く火照ったりプツプツとした肌荒れが起こりやすい季節です。韓国の自然派スキンケアアヌアの『ドクダミ 77% スージング アンプル』は、そんな冬の不安定な肌を穏やかに整えてくれる救世主です。",
        "desc_p2": "肌鎮静効果に優れたドクダミエキスを77%も配合し、さらに角層バリアを支えるセラミドやペプチドが肌の水分保持力を高めます。軽やかでみずみずしいテクスチャーでありながら、肌に伸ばすと角質層へすばやく浸透し、乾燥で火照った皮膚を瞬時にクールダウン。刺激に弱い敏感肌の方でも毎日安心して使える、真冬の守り神のような美容液です。",
        "target": "冬になると乾燥で顔が赤くなりやすい方、ニキビや肌荒れを繰り返しやすい方、さっぱりしながらもしっかり潤う美容液を好む方",
        "point": "洗顔後、化粧水で肌を整えた後に適量を顔全体に優しくハンドプレス。赤みが出ている部分にはコットンに含ませて部分パックするのもおすすめです。"
    },
    {
        "rank": 9,
        "tag": "🍊 青みかんビタミンC×ペプチド！冬のどんより乾燥くすみを晴らして透明ツヤ肌へ",
        "catch": "グーダルのメガヒット美容液。済州島青みかんエキスとペプチドが肌の明度とハリをダブルサポート",
        "brand_name": "goodal (グーダル)",
        "capacity": "30ml (グリーンタンジェリン ビタC ダークスポット ケア セラム)",
        "type": "青みかんエキス70%＆ペプチド配合・高保湿トーンアップセラム",
        "features": "済州青みかんエキス（ビタミンC誘導体）、ナイアシンアミド4%、アルブチン、アデノシン、ペプチド",
        "value": "冬の寒さで血行不良になりくすみがちな素肌を、たっぷりのビタミンCとペプチドの相乗効果でパッと明るい発光美肌へ導く",
        "desc_p1": "12月の真冬は、寒さによる血流停滞と乾燥によって、肌の透明感が著しく失われ、顔色が悪く見えがちです。韓国コスメの王道ビタミンCセラムとして名高いグーダルの『グリーンタンジェリン ビタC セラム』は、冬のどんより肌を一掃するビタミン爆弾です。",
        "desc_p2": "完熟前の青みかんから抽出したフレッシュなビタミンCと、肌の弾力を支えるペプチド、ナイアシンアミドが贅沢に共演。ジェル状のぷるぷるしたテクスチャーで、ビタミン特有のピリピリ感がほとんどないマイルド処方です。朝のメイク前に塗ることで日中の酸化ダメージを防ぎ、夕方になってもくすまない透明感あふれるツヤ肌を一日中キープできます。",
        "target": "冬の寒さで顔色がくすんで疲れて見えやすい方、シミ予防とハリケアを同時に行いたい方、敏感肌でも使えるビタミンCを探している方",
        "point": "朝晩の化粧水の後に1〜2プッシュを全顔になじませます。朝使用する際は、上から日焼け止めやUVクリームを重ねることで紫外線・乾燥対策が完璧になります。"
    },
    {
        "rank": 10,
        "tag": "🐌 カタツムリ粘液×ペプチドの驚異の再生力！冬のガサガサ深刻ダメージを集中リペア",
        "catch": "ネイチャーリパブリックのロングセラー。濃厚なスネイルパワーが荒れた肌をふっくら再生",
        "brand_name": "NATURE REPUBLIC (ネイチャーリパブリック)",
        "capacity": "40ml (スネイル ソリューション エッセンス)",
        "type": "高濃度カタツムリ分泌液＆ペプチド配合・高密着集中リペアエッセンス",
        "features": "カタツムリ粘液ろ過物、ムチン、複合ペプチド、アデノシン、ヒアルロン酸",
        "value": "冬の冷気でダメージを受けた角層をカタツムリの自己修復成分ムチンがラッピング。ペプチドとの相乗効果で、もっちりとした弾力を蘇らせる",
        "desc_p1": "冬の寒風に長時間さらされて肌がカサカサに毛羽立ってしまった極限の乾燥状態に、古くから圧倒的な再生力で愛されてきたのがネイチャーリパブリックの『スネイル ソリューション エッセンス』です。",
        "desc_p2": "傷ついた皮膚を素早く修復するカタツムリの粘液成分（ムチン）と、弾力を高めるペプチドを高濃度に配合。糸を引くような独特のとろみがあるエッセンスが肌にピタッと吸着し、乾燥で荒れた皮膚表面を滑らかな潤いの膜でシールドします。翌朝には肌が内側からふっくらと押し返してくるようなもっちり感を実感でき、冬の過酷な環境から肌を守り抜きます。",
        "target": "冬の乾燥で肌がゴワつき皮剥けしそうな方、リッチで粘りのある濃厚なテクスチャーが好きな方、肌の再生・修復力を高めたい方",
        "point": "化粧水の後に適量を手に取り、顔全体に軽くパッティングしながら馴染ませます。特に乾燥しやすい頬や目元には重ね付けして水分を閉じ込めてください。"
    }
]

faq_items = [
    {
        "q": "ペプチド美容液とレチノール美容液、ビタミンC美容液はどう使い分ければ良いですか？",
        "a": "ペプチドは『肌への刺激が極めて少なく、乾燥小ジワやハリ低下をふっくら押し上げる』成分です。レチノールはターンオーバー促進に優れますが冬は皮剥けや乾燥のリスクが高くなります。またビタミンCは毛穴やくすみに効果的ですが、乾燥肌には少し刺激に感じることがあります。そのため、乾燥が深刻化する11月〜12月は『朝はペプチド＋ビタミンC、夜はペプチド＋高保湿クリーム』という組み合わせが最も低刺激で確実なハリツヤ効果を発揮します。"
    },
    {
        "q": "ペプチド美容液を塗ると、なぜ冬の乾燥小ジワや表情ジワが改善するのですか？",
        "a": "ペプチドはアミノ酸が複数結合した分子で、肌のコラーゲンやエラスチンの生成を促進するシグナルを出します。特に『アセチルヘキサペプチド-8（アルジルリン）』や『シンエイク』などは、表情筋の緊張を和らげる働きがあり、冬の乾燥によって形状記憶されがちな目尻や眉間、ほうれい線のシワを物理的・生理学的にほぐしてふっくらと押し戻す効果を発揮します。"
    },
    {
        "q": "ペプチド美容液を使う最適なタイミングとスキンケアの順番は？",
        "a": "洗顔後、化粧水で肌を十分に潤した『直後』に使用するのがベストです。角層が水分で満たされている状態でペプチド美容液を塗布することで、水溶性のペプチド成分が角層奥深くまでスムーズに浸透します。その後、乳液やセラミドクリームなどの油分で蓋をして、美容成分と水分をしっかり閉じ込めてください。"
    },
    {
        "q": "20代でも冬のペプチド美容液は使うべきですか？それとも30代以降向けですか？",
        "a": "20代の方にも冬の予防ケアとして強くおすすめします。冬の暖房下で長時間スマホやPCを見ていると、無意識のうちに眉間や目元に小ジワが刻まれます。ペプチドは刺激がなく肌のバリア機能を高めるアミノ酸結合体であるため、若いうちから取り入れることで将来の本格的な深いシワやたるみを効果的に防ぐことができます。"
    },
    {
        "q": "敏感肌でもペプチド美容液は毎日使えますか？",
        "a": "はい、ペプチドは元々生体内に存在するアミノ酸の結合体であるため、レチノールや高濃度酸（AHA/BHA）のような刺激反応（A反応や皮剥け）が起きにくいのが大きな特徴です。本記事でご紹介しているThe Ordinary、バイオヒールボ、魔女工場、アヌアなどは低刺激処方で作られており、冬の敏感肌でも毎日朝晩安心してお使いいただけます。"
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
    "headline": "保湿力の強さで冬の乾燥小ジワ・刻まれジワとさようなら！塗るボトックス発想でふっくら押し返す高保湿ペプチド美容液ランク10",
    "description": "11月・12月の寒冷と暖房乾燥による表情ジワの定着・大人の乾燥小ジワ・ハリ低下を徹底解決！ボトックス注射発想のシンエイクやアセチルヘキサペプチド、複合ペプチドを高濃度配合した高保湿ペプチド美容液10選を徹底比較！The Ordinary、BIOHEAL BOH、メディキューブ、VT、魔女工場など、真冬でも内側から押し返す弾力美肌へ導く至高のセラムを厳選。",
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
    "name": "冬の高保湿ペプチド美容液 おすすめランキング10選",
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
            <img src="{item['image']}" alt="{p['brand_name']} {p['capacity']} 高保湿ペプチド美容液" class="product-img" loading="lazy" width="280" height="280">
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
  <title>保湿力の強さで冬の乾燥小ジワ・刻まれジワとさようなら！塗るボトックス発想でふっくら押し返す高保湿ペプチド美容液ランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒冷と暖房乾燥による表情ジワの定着・大人の乾燥小ジワ・ハリ低下を徹底解決！ボトックス注射発想のシンエイクやアセチルヘキサペプチド、複合ペプチドを高濃度配合した高保湿ペプチド美容液10選を徹底比較！The Ordinary、BIOHEAL BOH、メディキューブ、VT、魔女工場など、真冬でも内側から押し返す弾力美肌へ導く至高のセラムを厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-peptide-serum">
  <meta name="robots" content="index, follow, max-image-preview:large">
  
  <!-- OGP & SNS -->
  <meta property="og:title" content="保湿力の強さで冬の乾燥小ジワ・刻まれジワとさようなら！塗るボトックス発想でふっくら押し返す高保湿ペプチド美容液ランク10">
  <meta property="og:description" content="11月・12月の冬の乾燥小ジワ・ハリ低下を徹底解決！塗るボトックス発想でふっくら押し返す高保湿ペプチド美容液10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-peptide-serum">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#6b46c1">

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
      --primary: #6b46c1;
      --primary-light: #faf5ff;
      --primary-dark: #44337a;
      --text-main: #2d3748;
      --text-sub: #718096;
      --bg-page: #fbfbfc;
      --bg-card: #ffffff;
      --border: #edf2f7;
      --border-focus: #d6bcfa;
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
      <a href="/winter-hydrating-serum">美容液</a> <span>&gt;</span>
      <span>高保湿ペプチド美容液</span>
    </nav>

    <header class="article-header">
      <span class="header-tag">2026年冬・徹底検証</span>
      <h1 class="article-title">保湿力の強さで冬の乾燥小ジワ・刻まれジワとさようなら！塗るボトックス発想でふっくら押し返す高保湿ペプチド美容液ランク10</h1>
      <p class="article-lead">
        11月から12月にかけての本格的な寒さと暖房の乾燥直撃。気温低下による血行不良と乾燥が重なると、表情の動きによって生じる浅いシワがそのまま深く刻まれ、夕方にはファンデーションが割れてしまう深刻なエイジング悩みが多発します。本記事では、塗るボトックス発想のアセチルヘキサペプチドやマトリキシル、複合シグナルペプチドを配合した高保湿ペプチド美容液10選を徹底検証！角層の奥からふっくらと押し返すような極上のハリ弾力を叶える名品をご紹介します。
      </p>
      <div class="meta-info">
        <span>📅 2026年11月02日更新</span>
        <span>✍️ 冬コスメ徹底比較ラボ 編集部監修</span>
        <span>⏱️ 読了目安：約8分</span>
      </div>
    </header>

    <section class="section-box">
      <h2 class="section-title">❄️ 11月・12月に「ペプチド美容液」が選ばれる科学的理由</h2>
      <p class="content-p">
        真冬の過酷な寒さは、皮膚表面の毛細血管を収縮させて血流を滞らせ、真皮層の線維芽細胞の働きを鈍化させます。その結果、肌の弾力を支えるコラーゲンやエラスチンの産生スピードが落ち込み、暖房の温風によって角層の水分が蒸散すると、目元・眉間・ほうれい線に『ちりめんジワ』や『表情ジワの定着』が一気に進行します。
      </p>
      <p class="content-p">
        ペプチドは、複数のアミノ酸が結合した生体内シグナル物質。真冬の過酷な乾燥環境でも、肌の奥へ『コラーゲンやエラスチンを補強せよ』という指令を直接伝達し、細胞レベルで押し返すようなハリ弾力を促します。さらに、神経伝達物質を穏やかにコントロールする神経ペプチド（アルジルリン等）は、寒さでこわばった表情筋周辺を柔らかく保ち、シワが深く刻まれるのを未然にブロックします。
      </p>

      <div class="mechanism-grid">
        <div class="mechanism-card">
          <div class="mech-title">🧬 コラーゲン産生シグナルの活性化</div>
          <div class="mech-desc">マトリキシルをはじめとするシグナルペプチドが、冬の寒冷で活動が低下した角層奥の細胞に働きかけ、内側から弾力線維の密度を向上させます。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">💉 塗るボトックス発想の表情筋ケア</div>
          <div class="mech-desc">アセチルヘキサペプチド-8やシンエイクが、目尻や眉間などの表情の癖による筋収縮をマイルドに緩和。乾燥によって定着しがちなシワの形状記憶を防ぎます。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">🌿 レチノールよりも低刺激で安心</div>
          <div class="mech-desc">冬場は皮剥けや赤みが出やすいレチノールに比べ、ペプチドは生体親和性が高く刺激が極小。乾燥で敏感に傾いた冬肌でも毎日朝晩安心して使用できます。</div>
        </div>
      </div>
    </section>

    <section class="section-box">
      <h2 class="section-title">🔍 失敗しない！冬の高保湿ペプチド美容液選び 3大チェック基準</h2>
      <div class="mechanism-grid">
        <div class="mechanism-card">
          <div class="mech-title">1. ペプチドの種類と複合配合</div>
          <div class="mech-desc">シワ対策の神経ペプチド（アルジルリン）、ハリ密度のシグナルペプチド（マトリキシル）、組織修復の銅ペプチドなど、複数のペプチドがブレンドされた処方が最も高い相乗効果を発揮します。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">2. 水分補給成分（HA・コラーゲン）の共存</div>
          <div class="mech-desc">ペプチド単体だけでなく、多重ヒアルロン酸や加水分解コラーゲンが同時に配合されていることで、肌内部の水分量を一気に引き上げ、瞬時にふっくら感を体感できます。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">3. 朝晩使える浸透テクスチャー</div>
          <div class="mech-desc">メイク前の朝にもたっぷり使えてヨレない、浸透性の高いウォータリージェルやリキッド状のものがおすすめ。朝の投入が日中のエアコン暖房によるシワ割れを防ぐ最大の鍵です。</div>
        </div>
      </div>
    </section>

    <!-- ランキング商品カード群 -->
    <section class="ranking-section">
      <h2 class="section-title">🏆 保湿力高め！高保湿ペプチド美容液 おすすめ人気ランキング10選</h2>
      {"".join(cards_html)}
    </section>

    <section class="section-box">
      <h2 class="section-title">📊 高保湿ペプチド美容液 性能＆スペック徹底比較表</h2>
      <p class="content-p">
        今回厳選した10商品の配合成分、実勢価格、特徴を一覧表にまとめました。ご自身の肌状態や目的に合わせて最適な1本をお選びください。
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
      <h2 class="section-title">❓ 冬のペプチド美容液活用法 よくある質問（FAQ）</h2>
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
      <h2 class="section-title">✨ 編集部まとめ：ペプチド美容液で真冬も押し返すようなハリ艶肌へ</h2>
      <p class="content-p">
        11月から12月にかけての冷気と暖房のダブルパンチは、肌の表面だけでなく奥深くの弾力組織にまでダメージを与え、乾燥小ジワを深刻化させます。この冬のエイジングサインに対して、肌の奥から活力と弾力を呼び覚ましてくれるのが『ペプチド美容液』です。
      </p>
      <p class="content-p">
        刺激を心配することなく毎日惜しみなく使えるペプチドは、大人の冬のスキンケアにおける最高のパートナー。朝のメイク前に仕込んで夕方のシワ落ちを防ぎ、夜はたっぷりと重ね付けて翌朝の弾力を形状記憶させる。ぜひ本ランキングからあなたにぴったりのペプチド美容液を選び、乾燥に負けないふっくら押し返すハリ美肌を手に入れてください。
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

with open("winter-peptide-serum.html", "w", encoding="utf-8") as f:
    f.write(full_html.strip())

print("Successfully generated winter-peptide-serum.html")
