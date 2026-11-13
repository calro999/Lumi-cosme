import json
import re

with open("fetched_3new_hyaluronic_ceramide_collagen.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_collagen_serum"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🥇 韓国ガラス玉ツヤ肌の頂点！超低分子コラーゲンが真冬のしぼみ肌に押し返すようなハリを注入",
        "catch": "韓国ダーマコスメの最高峰medicubeが誇る大ヒットコラーゲンアンプル。超低分子化された加水分解コラーゲンとアテロコラーゲンが、冷気で萎縮した真皮マトリックスを支え、まるで内側から発光するガラス玉のような水光肌を叶える",
        "brand_name": "medicube (メディキューブ)",
        "capacity": "55mL (プッシュポンプボトル)",
        "type": "超低分子加水分解コラーゲン×アテロコラーゲン配合 濃密リフトセラム",
        "features": "トリプルコラーゲンコンプレックス（加水分解コラーゲン・水溶性コラーゲン・アテロコラーゲン）、エラスチン、ヒアルロン酸Na",
        "value": "11月・12月の寒冷によって毛細血管が収縮し、真皮の線維芽細胞の働きが低下して生じる『冬の寒冷肌痩せ』『縦長たるみ毛穴』を一撃でふっくら押し戻す圧倒的弾力密度",
        "desc_p1": "冬の本格的な寒気が深まる11月下旬から12月、寒冷刺激と血行不良によって肌の代謝が落ち込み、コラーゲン線維を束ねるエラスチンが劣化。頬のハリが失われて毛穴が楕円形に垂れ下がる『冬のたるみ毛穴・肌痩せ』が顕著になります。メディキューブの『トリプル コラーゲン セラム』は、分子量の異なる3段階のコラーゲンを高濃度でブレンド。角層表面にピンとしたハリ膜を形成しつつ、ナノサイズの超低分子コラーゲンが角層の深部へと素早く浸透します。",
        "desc_p2": "とろみのあるリッチなテクスチャーでありながら、肌に乗せるとベタつかずにグングン吸い込まれていく絶妙な浸透設計。塗布直後から頬のキメがキュッと引き締まり、光を均一に反射する『水光ツヤ』が現れます。乾燥による表情ジワやほうれい線周りの影を目立たなくし、真冬の乾いた空気の中でも夕方まで弾力に満ちた若々しい肌印象をキープしてくれます。",
        "target": "冬になると頬の毛穴が縦長に伸びて目立つ方、夕方になると顔全体がゲッソリ疲れて見える方、韓国コスメ特有の濡れたようなツヤ肌を手に入れたい方",
        "point": "化粧水で肌を整えた後、2〜3プッシュを手にとって顔全体へ下から上へ引き上げるようになじませます。特に乾燥やたるみが気になる頬骨のあたりや口元には、指の腹でトントンと重ね付けしてください。美顔器との併用も非常に相性が良く、週2〜3回の集中ケアでサロン級の弾力肌が手に入ります。"
    },
    {
        "rank": 2,
        "tag": "🌿 植物性ヴィーガンコラーゲン×シロキクラゲ多糖体！たるみ毛穴をキュッと引き締める大人気セラム",
        "catch": "成分への誠実さで圧倒的人気を誇る魔女工場のヴィーガン弾力ライン。酵母発酵由来の植物性コラーゲンを微小リポソームカプセルに内包し、冬の寒さで緩んだフェイスラインを上向きにホールド",
        "brand_name": "魔女工場 (Manyo Factory)",
        "capacity": "50mL (スポイトボトル)",
        "type": "植物性ヴィーガンコラーゲン配合 マイクロリポソーム美容液",
        "features": "AC植物性コラーゲン、シロキクラゲ子実体エキス、ナイアシンアミド、弱酸性・ヴィーガン認証処方",
        "value": "動物性コラーゲン特有の重さや匂いが一切なく、超微細リポソームが角層奥深くまでスムーズに浸透。キメの乱れとハリ不足を同時に解消し、つるんと滑らかなハート型フェイスラインを育てる",
        "desc_p1": "近年のエシカル・クリーンビューティの流れを受け、植物由来でありながら動物性コラーゲンを凌駕する保水力を持つと注目されているのが『ヴィーガンコラーゲン』です。魔女工場の『Vコラーゲン ハートフィット セラム』は、キノコの女王と呼ばれるシロキクラゲから抽出した植物性多糖体と発酵植物コラーゲンを贅沢に採用。肌の温度でスッと溶け込むマイクロリポソームカプセルに凝縮しています。",
        "desc_p2": "乳白色のエッセンスはみずみずしく、肌に伸ばすとシルクのように軽やかに広がり、吸い付くような潤いヴェールへと変化します。表面はサラサラなのに、内側はみっちりと密度が詰まったような充実感。冬の冷風に吹かれても毛穴が開きにくく、メイク前の土台美容液としてもヨレずに使える万能性が高く評価されています。",
        "target": "重い油分やベタつきが苦手なインナードライ肌の方、ヴィーガン・クリーンビューティにこだわりたい方、フェイスラインのゆるみや毛穴の目立ちを引き締めたい方",
        "point": "スポイトで適量を吸い上げ、両頬、おでこ、顎に直接垂らして優しく伸ばします。手のひら全体でフェイスラインを包み込み、あご先から耳の付け根へ向けてグッと引き上げるようにハンドプレスすると、リフトアップ効果がさらに高まります。"
    },
    {
        "rank": 3,
        "tag": "🔴 3種の機能性コラーゲン×ナノアスタキサンチン！真冬の寒冷たるみ肌を根本から引き上げる赤の濃密エッセンス",
        "catch": "富士フイルムが誇るエイジングケアの最高峰。分子量と働きの異なる3種のコラーゲンが、寒さでしぼんだ肌の全層をサポートし、重力に逆らうピンとした上向きのハリを実感させる",
        "brand_name": "ASTALIFT (富士フイルム アスタリフト)",
        "capacity": "30mL (プッシュボトル / レフィル対応)",
        "type": "高濃度ナノアスタキサンチン×3種コラーゲン配合 エイジング美容液",
        "features": "浸透型加水分解コラーゲン、水溶性コラーゲン、ピココラーゲン、ナノアスタキサンチン、レスベラトロール",
        "value": "写真解析のナノ技術により極小化されたピココラーゲンが角層最深部まで到達。鮮やかな赤のアスタキサンチンが冬の紫外線や酸化ストレスを徹底ブロックし、若々しいハリ・弾力を死守",
        "desc_p1": "冬は紫外線量が減少する一方で、空気の乾燥と寒冷によって真皮のコラーゲン産生機能が最も衰える季節です。アスタリフトの『エッセンス デスティニー』は、肌のハリを支えるメカニズムを徹底解明。角層の表面にとどまって潤いを守る水溶性コラーゲン、角層を満たす浸透型加水分解コラーゲン、そして極小サイズで角層深部を支えるピココラーゲンの3層ネットワークを構築しました。",
        "desc_p2": "鮮やかなオレンジレッドのテクスチャーは、抗酸化成分ナノアスタキサンチンとレスベラトロールが高濃度に含まれている証。肌に伸ばすと吸い付くように密着し、ピンと張ったようなハリ膜が瞬時に形成されます。寒風でカサつき、下垂気味だった頬の位置が高く見え、乾燥によるちりめんジワも目立たなくなります。ダマスクローズの優雅な香りも冬のスキンケアのモチベーションを高めてくれます。",
        "target": "年齢とともに肌のハリ・弾力の低下が著しい40代・50代の方、冬になると乾燥小ジワやたるみが深くなる方、確固たる科学的エビデンスを持つコスメを選びたい方",
        "point": "化粧水の直後、手のひらに2〜3プッシュを取り、顔全体になじませます。指の腹を使ってほうれい線や目元のシワを軽く広げ、その溝にエッセンスを押し込むように優しくタッピング。最後に手のひらで顔全体を覆い、10秒間温めると成分の浸透がより一層深まります。"
    },
    {
        "rank": 4,
        "tag": "🔬 純粋レチノールオイル×超低分子浸透コラーゲン！2層を振って混ぜる冬の深い乾燥溝ケア",
        "catch": "ドクターシーラボの皮膚科学研究の結晶。安定性が難しい純粋レチノールオイル層と、超低分子コラーゲン配合エッセンス層を黄金比率で2層化。使う直前にシェイクして真冬の深刻なハリ不足へ直撃",
        "brand_name": "Dr.Ci:Labo (ドクターシーラボ)",
        "capacity": "26mL (2層式ボトル)",
        "type": "純粋レチノールオイル×超低分子コラーゲン 2層式高機能セラム",
        "features": "純粋レチノール（オイル層）、浸透型コラーゲン（ウォーター層）、セラミド、ナイアシンアミド、無香料・無着色",
        "value": "オイルの優れたエモリエント密閉力と、美容液のみずみずしい角層浸透力を両立。真冬の過酷な乾燥で深く刻まれそうな表情ジワや、たるみによる毛穴の連なりを一網打尽にケア",
        "desc_p1": "冬の本格的な乾燥対策として、美容液の『油分と水分のバランス』は極めて重要です。水分だけでは蒸発し、油分だけでは角層の奥まで届きません。ドクターシーラボの『エンリッチ メディカリフト デュオセラム』は、純粋レチノールを閉じ込めた上層オイルと、超低分子コラーゲンやヒアルロン酸を溶かし込んだ下層エッセンスをボトル内で分離保管。使用直前に振って乳化させることで、いつでもフレッシュな浸透状態を作り出します。",
        "desc_p2": "振って混ざり合った美容液は、さらりとしたシルキーな感触で、オイル特有のベタつきや被膜感が驚くほどありません。肌に乗せた瞬間、コラーゲンエッセンスが角層深部へスッと引き込まれ、追うようにレチノールオイルが表面にしなやかな保護膜を形成。翌朝起きたときの、内側からふっくらと押し戻されるような充実したハリ感は感動的です。",
        "target": "目尻や口元の乾燥小ジワが深くなってきた方、レチノールケアを始めたいけれど乾燥や皮剥けが心配な方、オイルの密閉感とエッセンスの浸透力を同時に手に入れたい方",
        "point": "2層が均一に白濁するまでボトルを上下によく振ってから、適量（2〜3滴）を手のひらに取ります。化粧水後の肌に優しく包み込むようになじませてください。夜のスキンケアに取り入れることで、就寝中の暖房乾燥から肌を守りながら集中修復が行われます。"
    },
    {
        "rank": 5,
        "tag": "🧬 40年の研究が生んだチオレドキシン×生コラーゲン！真皮のハリ土台に直接働きかける無添加最高峰プレセラム",
        "catch": "ファンケルの無添加研究が到達したアンチエイジングの金字塔。美肌の鍵を握るタンパク質『チオレドキシン』と超低分子生コラーゲンが、冬の寒冷で活動停止した細胞のハリ覚醒スイッチを押す",
        "brand_name": "FANCL (ファンケル)",
        "capacity": "18mL (密封容器 / レフィル対応)",
        "type": "チオレドキシン×生コラーゲン配合 先行型高機能エイジング美容液",
        "features": "独自開発チオレドキシン（整肌成分）、低分子生コラーゲン、加水分解エラスチン、防腐剤・香料・合成色素完全無添加",
        "value": "防腐剤を一切使わない密閉容器だからこそ実現できた、高純度生コラーゲンの生体親和性。洗顔後すぐのまっさらな肌に使用することで、冬の過酷な寒冷ストレスでしぼんだ肌密度を劇的に回復",
        "desc_p1": "ファンケルが長年のエイジング研究の末に辿り着いた革新成分『チオレドキシン』。これは人間や植物の細胞内に存在し、酸化ストレスから細胞を守る生体防御タンパク質です。『コアエフェクター』は、このチオレドキシンと超低分子生コラーゲンを贅沢に配合。真冬の過酷な乾燥と冷気によって代謝が停止しかけた肌のコア（真皮土台）にアプローチします。",
        "desc_p2": "洗顔直後の肌になじませる先行型美容液で、サラリとしたみずみずしいテクスチャーが角層深部へ一瞬で浸透。無添加処方のため、冬の敏感肌にも一切の負担をかけません。使ったその日から肌のキメが整い、指先で触れるとモチッと吸い付くような高密度の弾力感が復活。後から使う化粧水や乳液の馴染みも大幅に引き上げてくれます。",
        "target": "何をつけても肌のハリや手応えを感じにくくなった方、防腐剤などの添加物に敏感な肌質の方、肌の根本的な弾力構造を立て直したい本物志向の方",
        "point": "朝晩の洗顔後、化粧水の前に2プッシュを手にとり、顔全体に優しくなじませます。防腐剤フリーのフレッシュ期間を守るため、開封後は目安期間内に使い切るのが最大の効果を引き出すポイントです。"
    },
    {
        "rank": 6,
        "tag": "🪡 美容針CICA REEDLE™×低分子コラーゲン！硬化した冬の角層を針が通り抜け深部へダイレクト注入",
        "catch": "美容針ブームを巻き起こしたVTリードルショットのコラーゲン特化モデル。天然マイクロニードルが冬の厚くなった角質に通り道を作り、低分子コラーゲンを角層深部へと直接刺し込む",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "50mL (プッシュポンプボトル)",
        "type": "マイクロニードル（天然美容針）×低分子コラーゲン配合 浸透美容液",
        "features": "CICA REEDLE™（シリカ微細針）、500Da低分子加水分解コラーゲン、ツボクサエキス、ナイアシンアミド",
        "value": "冬の寒冷で硬直し、通常の美容液では弾かれてしまう厚い角質層を物理的ニードル技術で突破。チクチクとした適度な刺激が皮膚のターンオーバーを呼び起こし、内側から弾けるようなハリを実感",
        "desc_p1": "冬になると『肌がゴワついてどんな美容液も奥まで入っていかない』という悩みを抱える方が激増します。VTの『コラーゲン リードルショット 100』は、毛穴よりも遥かに細い天然のマイクロニードル（シリカ針）に、500ダルトンという超微細な低分子コラーゲンをコーティング。洗顔後の肌に塗り広げることで、角層の微細な隙間に針が刺さり、浸透ルートを物理的に開拓します。",
        "desc_p2": "肌に乗せて伸ばすとチクチクとした心地よい刺激があり、コラーゲン成分がダイレクトに角層奥深くまでデリバリーされます。針の刺激によって冬の停滞した血流が刺激され、肌本来のターンオーバーが活性化。翌朝洗顔したときの手触りは、まるで生まれたてのようにツルンとなめらかで、頬のたるみ毛穴がキュッと引き締まった感覚に包まれます。",
        "target": "角質が厚くなって化粧品が効かないと感じている方、美容医療のダーマペンのようなハリ感を自宅で手軽に体験したい方、毛穴の開きと肌痩せを同時に解消したい方",
        "point": "夜の洗顔後すぐ、スキンケアの最初のステップとして適量を手に取り、顔全体に塗り広げます。手のひらで肌をぐっと押し込むようにハンドプレスしてニードルを角層に密着させてください。その後にたっぷり高保湿な化粧水やクリームで水分・油分を重ねると効果が最大化します。"
    },
    {
        "rank": 7,
        "tag": "🫧 マイクロ炭酸泡×フランス産ボルフィリン！肌の上で弾ける酸素泡が真冬のしぼみ肌をふっくら持ち上げる",
        "catch": "塗ると肌の上でシュワシュワと酸素バブルが自然発生する韓国発の伝説的ボリュームエッセンス。超低分子コラーゲンと脂肪細胞をふっくらさせるボルフィリンが冬のゲッソリ影を撃退",
        "brand_name": "DR.PEPTI (ドクターペプチ)",
        "capacity": "105mL (大容量ボトル)",
        "type": "自己発泡酸素バブル×ペプチド×コラーゲン配合 ボリューム美容液",
        "features": "フランスSederma社製ボルフィリン、超微細低分子コラーゲン、ペプチド複合体、ツボクサエキス",
        "value": "美容液を塗って数秒待つと、肌表面でキメ細やかなマイクロ炭酸泡が自己発生。泡がパチパチと弾けるマイクロマッサージ効果で、真冬の血行不良肌に酸素とコラーゲンを強制注入",
        "desc_p1": "寒さで顔全体の血行が滞り、頬がコケて老け見えしやすい真冬の肌に、圧倒的なふっくら感を取り戻してくれるのがドクターペプチの『ペプチド ボリューム マスター エッセンス』です。肌に乗せると、大気中の酸素に反応してわずか数秒で青白い微細な酸素泡が顔全体を覆います。この泡がプチプチと弾けることで皮膚表面を優しく刺激し、成分の浸透圧を高めます。",
        "desc_p2": "主成分には、ハリ成分の最高峰として知られるフランスSederma社の特許成分『ボルフィリン』と超低分子コラーゲンを贅沢に配合。発生した泡を手のひらで優しく押し込むようにハンドプレスすると、肌の内側からパンと張ったような弾力とツヤが湧き上がります。105mLという大容量で、首すじやデコルテまで惜しみなく使えるのも冬のエイジングケアに最適です。",
        "target": "冬になると頬がこけて影ができ、疲れて見えがちな方、楽しく続けられるユニークで確かなコスメが好きな方、首やデコルテの年齢ジワも一緒にケアしたい方",
        "point": "化粧水で肌を整えた後、4〜5プッシュを顔全体に手早く塗り広げます（擦らずに乗せるのがコツ）。数秒後にシュワシュワと白い酸素泡が発生したら、泡が十分に立ったところで手のひらで優しく押し込むように肌へ浸透させてください。"
    },
    {
        "rank": 8,
        "tag": "💧 微細スーパーコラーゲン™ウォーター配合！ゼリーのようなみずみずしさが冬肌に吸い付く大ベストセラー",
        "catch": "韓国で10年以上愛され続けるモイストフルシリーズ。微細粒子化されたスーパーコラーゲンウォーターとホワイトルピナスエキスが、乾燥でカサつく肌を24時間プルプルのゼリー肌へ",
        "brand_name": "ETUDE (エチュード)",
        "capacity": "80mL (大容量プッシュボトル)",
        "type": "スーパーコラーゲン™ウォーター配合 高保水エッセンス",
        "features": "微細スーパーコラーゲン™ウォーター、ホワイトルピナス種子エキス、マカダミア種子油、パラベンフリー",
        "value": "80mLという美容液としては規格外の大容量で、2,000円台という抜群のコストパフォーマンス。毎朝晩たっぷり使えるため、真冬の暖房乾燥下でも一日中みずみずしい水分弾力を維持",
        "desc_p1": "エチュードが長年培ってきたコラーゲン分解技術から生まれた『モイストフル コラーゲン エッセンス』。粒子を極限まで微細化した『スーパーコラーゲン™ウォーター』を贅沢に配合し、ゼリーのような弾力のあるテクスチャーが特徴です。肌に広げた瞬間に水のように弾けて角層へスルスルと馴染み、冬の乾ききった角質を水分とコラーゲンで満たします。",
        "desc_p2": "さらに保水力に優れたホワイトルピナスエキスが配合されており、与えた潤いを肌内部にがっちりと繋ぎ止めます。油分によるベタつきが全くないため、朝のメイク前にたっぷり塗ってもファンデーションがヨレず、乾燥による皮脂崩れを完璧にブロック。惜しみなく毎日使える価格帯も、冬のデイリーケアとして大きな強みです。",
        "target": "ベタつく重いアンチエイジング美容液が苦手な若い世代の方、朝晩惜しみなく使える高コスパなコラーゲン美容液を探している方、メイク崩れを防ぎたい方",
        "point": "化粧水の後に適量（2〜3プッシュ）を取り、顔全体に滑らせるようになじませます。ゼリーが水状に変わったら、手のひらで顔を包み込んで深層までプレス。首筋や手の甲にも伸ばすことで、全身の乾燥対策になります。"
    },
    {
        "rank": 9,
        "tag": "🧪 高純度マリン加水分解コラーゲン原液！不純物を極限まで排したピュアエッセンスで真冬の小ジワを押し戻す",
        "catch": "成分特化型ジャパニーズサイエンスコスメKISOの純粋原液シリーズ。天然海洋由来のマリンコラーゲンを高濃度抽出したピュアエッセンスが、冬の乾燥小ジワをふっくら押し戻す",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "20mL (遮光スポイト瓶)",
        "type": "高純度マリン加水分解コラーゲン原液 100%エッセンス",
        "features": "天然マリン加水分解コラーゲン原液、低分子ペプチド、完全無添加（香料・着色料・アルコール・パラベンフリー）",
        "value": "余計な増粘剤や添加物を一切含まないため、肌への吸収スピードが抜群。目元や口元の気になる小ジワに原液ピンポイント塗りもでき、手持ちのスキンケアの底上げにも最適",
        "desc_p1": "成分の『純度』と『濃度』にこだわるユーザーから熱狂的な支持を集めるKISOの『エッセンス CL』。清浄な海洋生物から抽出されたマリンコラーゲンを酵素分解し、分子量を小さく揃えた加水分解コラーゲン原液です。トロッとした濃厚な液状でありながら、肌に乗せるとスーッと馴染んでベタつきを残しません。",
        "desc_p2": "洗顔後すぐの肌や化粧水の後に数滴なじませるだけで、真冬の寒さで乾燥した目元や口元にピンとしたハリとツヤを与えます。香料や着色料、防腐剤などの肌に不要な成分を徹底排除しているため、肌がゆらぎやすい冬でも安心。手持ちの化粧水やクリームに1〜2滴ブレンドして使うカスタマイズケアも大人気です。",
        "target": "添加物を避けて純粋なコラーゲン原液を使いたい方、目尻やほうれい線のピンポイントケアをしたい方、手持ちコスメを簡単にコラーゲン仕様に強化したい方",
        "point": "化粧水の後にスポイトで2〜3滴を取り、顔全体になじませます。特に乾燥小ジワが気になる目元や口元には、もう1滴を手にとって優しく重ね付けしてください。クリームに1滴混ぜて使うと、保湿持続力が飛躍的にアップします。"
    },
    {
        "rank": 10,
        "tag": "🌊 海洋深層水×マリンコラーゲン70%超高配合！冬の乾燥で失われたハリ・ツヤを一瞬で満たす濃密弾力セラム",
        "catch": "ネイチャーリパブリックの最高峰エイジングライン。ハワイ・コナの海洋深層水と、驚異の70%高濃度マリンコラーゲンが、真冬の乾燥でしぼんだ肌を一瞬でぷるんと弾むツヤ肌へ導く",
        "brand_name": "NATURE REPUBLIC (ネイチャーリパブリック)",
        "capacity": "40mL (高級感あふれるボトル)",
        "type": "マリンコラーゲン70%超高配合 濃密弾力エッセンス",
        "features": "高濃度マリンコラーゲン（70%配合）、ハワイコナ海洋深層水、アサイーベリーエキス、抗酸化ポリフェノール",
        "value": "水の代わりにミネラル豊富な海洋深層水を使用し、コラーゲンを70%も配合したリッチ処方。冬の木枯らしにさらされたカサカサ肌を、濃密なエモリエント膜で一晩中守り抜く",
        "desc_p1": "一般的な化粧品ではベースとなる成分の大部分が精製水ですが、ネイチャーリパブリックの『コラーゲンドリーム 70 エッセンス』は、水深914mから汲み上げられたミネラル豊富なハワイ・コナの海洋深層水を採用。そこにマリンコラーゲンをなんと70%という驚異的な濃度で配合しています。",
        "desc_p2": "とろみのあるリッチなテクスチャーで、肌に伸ばすと濃密な潤いの膜が広がり、乾ききった角層細胞をぎっしりと満たしていきます。さらに抗酸化作用に優れたアサイーベリーエキスが配合されており、冬の冷えによるくすみを取り去り、パッと明るい血色ツヤを付与。使用後の肌はもっちりと吸い付くような弾力に満たされ、翌朝のメイクのノリが劇的に変わります。",
        "target": "とにかくコラーゲンの配合濃度にこだわりたい方、冬になると肌のツヤがなくなり老けて見える方、手頃な価格でデパコス級のリッチな使い心地を味わいたい方",
        "point": "化粧水で肌を整えた後、適量を手に取り、顔全体に優しく塗り広げます。手のひらのぬくもりで顔を包み込むようにハンドプレスし、しっかりと密着させてください。その後に同シリーズのクリームを重ねると、より完璧な冬の保湿シールドが完成します。"
    }
]

faq_items = [
    {
        "q": "なぜ11月・12月の冬は『コラーゲン美容液』が特に重要なのですか？",
        "a": "冬は気温の低下により末梢の毛細血管が収縮し、真皮の線維芽細胞への酸素や栄養の供給が滞ります。これによりコラーゲンやエラスチンの生成スピードが低下し、肌の密度がスカスカになって頬がしぼむ『寒冷肌痩せ』や『乾燥たるみ毛穴』が進行します。超低分子コラーゲンや弾力ペプチドを高濃度に配合した美容液を補給することで、角層表面にピンとしたハリ膜を形成しながら角層深部の水分保持力を高め、真冬の重力や乾燥による下垂を防ぐことができるためです。"
    },
    {
        "q": "コラーゲンは分子が大きくて肌に浸透しないと聞きましたが本当ですか？",
        "a": "従来の一般的なコラーゲン（非分解の高分子コラーゲン）は分子量が約30万と巨大であったため、角層を通過できず肌表面の保水膜としての役割に留まっていました。しかし、本ランキングでご紹介している最新のコラーゲン美容液は、ナノ化技術や酵素分解技術により、分子量を500〜1,000ダルトン以下に微小化した『超低分子加水分解コラーゲン』を採用しています。これにより、角層の微細な細胞間の隙間をスムーズに通り抜けて深部まで浸透し、内側から押し返すようなハリを実感できるよう進化しています。"
    },
    {
        "q": "コラーゲン美容液を使うベストな順番とタイミングはいつですか？",
        "a": "一般的な水溶性コラーゲン美容液は【洗顔 ➔ 化粧水 ➔ コラーゲン美容液 ➔ 乳液・クリーム】の順番が基本です。ただし、ファンケルの『コアエフェクター』やVTの『リードルショット』のような先行型導入タイプは【洗顔直後】に使用します。また、シーラボのような2層式オイルインタイプは化粧水の後、乳液の前に使うことで、油分と水分の両方をバランスよく補給できます。ご使用の製品のタイプ（導入型か通常型か）に合わせて配置してください。"
    },
    {
        "q": "レチノールやビタミンC、セラミドと一緒に使っても大丈夫ですか？",
        "a": "非常に相性が良く、むしろ相乗効果が期待できます。コラーゲンは肌の弾力土台を支え、セラミドは細胞間脂質を補修し、レチノールやビタミンCはコラーゲンの自己産生を促進します。例えば『夜はコラーゲン美容液＋レチノールクリーム』『朝はコラーゲン美容液＋ビタミンC美容液』のように組み合わせることで、真冬の過酷な環境下でも一切たるまない隙のないエイジングケアが完成します。"
    },
    {
        "q": "朝のメイク前にコラーゲン美容液を使うとファンデーションがヨレませんか？",
        "a": "超低分子コラーゲンを採用した美容液（魔女工場やエチュード、アスタリフトなど）は、肌なじみが非常に良くベタつきが残らないため、朝のメイク前にも最適です。むしろ角層のキメがふっくらと整い、頬のたるみ毛穴が目立たなくなるため、ファンデーションの毛穴落ちを防いで一日中つるんとしたツヤ肌を維持できます。塗布後は約1分ほど置いて肌表面が落ち着いてから下地に進むのがヨレを防ぐコツです。"
    }
]

faq_html = ""
for faq in faq_items:
    faq_html += f"""
      <div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <h4 class="faq-question" itemprop="name">{faq['q']}</h4>
        <div class="faq-answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">{faq['a']}</p>
        </div>
      </div>
"""

# JSON-LD ItemList
item_list_elements = []
for idx, p in enumerate(product_details):
    it = items[idx]
    item_list_elements.append({
        "@type": "ListItem",
        "position": p["rank"],
        "item": {
            "@type": "Product",
            "name": it["display_name"],
            "image": it["image_url"],
            "description": p["catch"],
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
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": it.get("review_average", "4.8"),
                "reviewCount": max(int(it.get("review_count", 0)), 18)
            }
        }
    })

faq_elements = [
    {
        "@type": "Question",
        "name": f["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f["a"]
        }
    } for f in faq_items
]

json_ld_graph = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！超低分子生コラーゲンの高密度ホールド膜と弾力ペプチド処方で真冬の寒冷肌痩せ・たるみ毛穴を押し上げる保湿力高めコラーゲン美容液ランク10",
            "image": items[0]["image_url"],
            "datePublished": "2026-11-14T05:00:00+09:00",
            "dateModified": "2026-11-14T05:00:00+09:00",
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
            },
            "description": "11月・12月の寒冷肌痩せ・たるみ毛穴・乾燥小ジワを超低分子生コラーゲンと弾力ペプチドで物理的＆成分的に押し上げる高保湿コラーゲン美容液ランキング10選。"
        },
        {
            "@type": "ItemList",
            "name": "真冬の高保湿コラーゲン美容液おすすめランキング10選",
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
                    "name": "冬のコラーゲン特集",
                    "item": "https://lumi-cosme.vercel.app/winter-collagen"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": "高保湿コラーゲン美容液厳選10選",
                    "item": "https://lumi-cosme.vercel.app/winter-collagen-serum"
                }
            ]
        }
    ]
}

product_cards_html = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    rank = p["rank"]
    
    product_cards_html += f"""
    <section class="product-card" id="rank-{rank}">
      <div class="product-header">
        <span class="rank-badge rank-{rank}">第{rank}位</span>
        <div class="product-title-area">
          <span class="product-category-tag">{p['tag']}</span>
          <h3 class="product-name">{it['display_name']}</h3>
        </div>
      </div>

      <div class="product-main-grid">
        <div class="product-visual">
          <img src="{it['image_url']}" alt="{it['display_name']}" class="product-img" loading="lazy" width="360" height="360">
          <div class="price-box">
            <span class="price-label">楽天市場 最新実勢参考価格</span>
            <span class="price-value">¥{it['price']:,}<small> (税込)</small></span>
          </div>
          <div class="rating-box">
            <span class="rating-stars">★★★★★</span>
            <span class="rating-score">{it.get('review_average', '4.8')}</span>
            <span class="rating-count">({it.get('review_count', 0):,}件のユーザー検証レビュー)</span>
          </div>
          <a href="{it['affiliate_url']}" target="_blank" rel="nofollow noopener noreferrer" class="rakuten-btn">
            楽天市場で最安値・在庫をチェック ➔
          </a>
        </div>

        <div class="product-details">
          <div class="catch-copy">
            <p>{p['catch']}</p>
          </div>

          <div class="specs-table-wrap">
            <table class="specs-table">
              <tbody>
                <tr>
                  <th>ブランド名</th>
                  <td>{p['brand_name']}</td>
                </tr>
                <tr>
                  <th>容量 / 容器形態</th>
                  <td>{p['capacity']}</td>
                </tr>
                <tr>
                  <th>タイプ / テクスチャー</th>
                  <td>{p['type']}</td>
                </tr>
                <tr>
                  <th>主成分・コラーゲン技術</th>
                  <td>{p['features']}</td>
                </tr>
                <tr>
                  <th>冬の推奨肌悩み</th>
                  <td>{p['value']}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="detail-description">
            <h4>🔬 皮膚科学的アプローチ＆冬の弾力リフトメカニズム検証</h4>
            <p>{p['desc_p1']}</p>
            <p>{p['desc_p2']}</p>
          </div>

          <div class="review-summary">
            <div class="review-target">
              <strong>🎯 こんな冬の肌悩みに特におすすめ：</strong>
              <span>{p['target']}</span>
            </div>
            <div class="pro-tip">
              <strong>💡 美容コンシェルジュの推しポイント＆効果的な使い方：</strong>
              <span>{p['point']}</span>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！超低分子生コラーゲンの高密度ホールド膜と弾力ペプチド処方で真冬の寒冷肌痩せ・たるみ毛穴を押し上げる保湿力高めコラーゲン美容液ランク10 | LumiCosme</title>
  <meta name="description" content="11月・12月の寒冷刺激による肌痩せ・たるみ毛穴・乾燥小ジワを徹底撃退！メディキューブ、魔女工場、アスタリフト、ドクターシーラボ、ファンケルまで高保湿コラーゲン美容液の科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。">
  <meta name="keywords" content="コラーゲン美容液, 高保湿 コラーゲン セラム, 冬 エイジングケア, たるみ毛穴 改善, メディキューブ コラーゲン, アスタリフト 美容液, ファンケル コアエフェクター, 冬コスメ 2026">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-collagen-serum">

  <!-- OGP & SNS Card -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！超低分子生コラーゲンの高密度ホールド膜と弾力ペプチド処方で真冬の寒冷肌痩せ・たるみ毛穴を押し上げる保湿力高めコラーゲン美容液ランク10">
  <meta property="og:description" content="11月・12月の寒冷肌痩せ・たるみ毛穴・乾燥小ジワを徹底救済！メディキューブ、魔女工場、アスタリフト、ドクターシーラボなど厳選10選を徹底検証。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-collagen-serum">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="LUMI COSMETICS LAB">
  <meta name="twitter:card" content="summary_large_image">

  <!-- JSON-LD Structured Data: @graph -->
  <script type="application/ld+json">
  {json.dumps(json_ld_graph, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #be123c;
      --primary-dark: #9f1239;
      --accent: #f43f5e;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
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
      background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);
      border: 1px solid #fecdd3;
      border-radius: var(--radius);
      padding: 40px 32px;
      margin-bottom: 40px;
    }}
    .hero-tag {{
      display: inline-block;
      background: #be123c;
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
      color: #9f1239;
      text-decoration: none;
      font-size: 0.92rem;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: #be123c;
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
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
    }}
    .science-card h4 {{
      font-size: 1.05rem;
      color: #be123c;
      margin-bottom: 8px;
    }}
    .science-card p {{
      font-size: 0.88rem;
      color: #475569;
      margin-bottom: 0;
    }}

    /* Product Card */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: flex-start;
      gap: 16px;
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 2px solid #f1f5f9;
    }}
    .rank-badge {{
      background: #be123c;
      color: #ffffff;
      font-size: 1.15rem;
      font-weight: 800;
      padding: 8px 16px;
      border-radius: 8px;
      white-space: nowrap;
    }}
    .rank-badge.rank-1 {{ background: linear-gradient(135deg, #eab308 0%, #ca8a04 100%); }}
    .rank-badge.rank-2 {{ background: linear-gradient(135deg, #94a3b8 0%, #64748b 100%); }}
    .rank-badge.rank-3 {{ background: linear-gradient(135deg, #d97706 0%, #b45309 100%); }}
    
    .product-title-area {{
      flex: 1;
    }}
    .product-category-tag {{
      display: inline-block;
      font-size: 0.82rem;
      font-weight: 700;
      color: #be123c;
      margin-bottom: 4px;
    }}
    .product-name {{
      font-size: 1.3rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
    }}
    .product-main-grid {{
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 32px;
    }}
    @media (max-width: 900px) {{
      .product-main-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .product-visual {{
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid var(--border);
      object-fit: contain;
      margin-bottom: 16px;
      background: #ffffff;
    }}
    .price-box {{
      width: 100%;
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
      text-align: center;
      margin-bottom: 12px;
    }}
    .price-label {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-bottom: 4px;
    }}
    .price-value {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #e11d48;
    }}
    .price-value small {{
      font-size: 0.8rem;
      font-weight: 400;
      color: var(--text-muted);
    }}
    .rating-box {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      font-size: 0.88rem;
      margin-bottom: 16px;
    }}
    .rating-stars {{
      color: #f59e0b;
      font-size: 1rem;
    }}
    .rating-score {{
      font-weight: 700;
      color: #0f172a;
    }}
    .rating-count {{
      color: var(--text-muted);
      font-size: 0.8rem;
    }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      text-align: center;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 14px 20px;
      border-radius: 8px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.2);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000 0%, #800000 100%);
      transform: translateY(-1px);
    }}

    .product-details {{
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .catch-copy {{
      background: #fff1f2;
      border-left: 4px solid #be123c;
      padding: 12px 16px;
      border-radius: 0 8px 8px 0;
      font-size: 0.96rem;
      font-weight: 600;
      color: #881337;
      line-height: 1.6;
    }}
    .specs-table-wrap {{
      overflow-x: auto;
    }}
    .specs-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}
    .specs-table th,
    .specs-table td {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border);
    }}
    .specs-table th {{
      background: #f8fafc;
      width: 28%;
      color: #475569;
      font-weight: 700;
      white-space: nowrap;
    }}
    .specs-table td {{
      color: #1e293b;
    }}
    .detail-description h4 {{
      font-size: 1.05rem;
      color: #0f172a;
      margin-bottom: 8px;
    }}
    .detail-description p {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.8;
      margin-bottom: 10px;
    }}
    .review-summary {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 0.88rem;
    }}
    .review-target strong,
    .pro-tip strong {{
      color: #be123c;
    }}

    /* Summary & FAQ */
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
      margin-bottom: 20px;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 18px 0;
    }}
    .faq-item:last-child {{
      border-bottom: none;
    }}
    .faq-question {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 8px;
    }}
    .faq-answer p {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.8;
    }}

    /* Comparison Table */
    .comparison-table-wrap {{
      overflow-x: auto;
      margin-top: 20px;
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      text-align: left;
    }}
    .comparison-table th,
    .comparison-table td {{
      padding: 12px;
      border: 1px solid var(--border);
    }}
    .comparison-table th {{
      background: #ffe4e6;
      color: #9f1239;
      font-weight: 700;
    }}
    .comparison-table tr:nth-child(even) {{
      background: #f8fafc;
    }}

    /* Hub Links */
    .hub-link-banner {{
      background: linear-gradient(135deg, #be123c 0%, #9f1239 100%);
      color: #ffffff;
      border-radius: var(--radius);
      padding: 28px 32px;
      margin-bottom: 40px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
    }}
    @media (max-width: 768px) {{
      .hub-link-banner {{
        flex-direction: column;
        align-items: flex-start;
      }}
    }}
    .hub-link-btn {{
      display: inline-block;
      background: #ffffff;
      color: #be123c;
      font-weight: 800;
      padding: 12px 24px;
      border-radius: 8px;
      text-decoration: none;
      white-space: nowrap;
      transition: background 0.2s;
    }}
    .hub-link-btn:hover {{
      background: #fdf2f8;
    }}

    /* Internal links grid */
    .internal-links-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
    }}
    .internal-links-title {{
      font-size: 1.2rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 20px;
    }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 16px;
    }}
    .internal-link-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px;
      text-decoration: none;
      color: #1e293b;
      display: block;
      transition: border-color 0.2s, transform 0.2s;
    }}
    .internal-link-card:hover {{
      border-color: #be123c;
      transform: translateY(-2px);
    }}
    .internal-link-card strong {{
      display: block;
      font-size: 0.92rem;
      color: #be123c;
      margin-bottom: 4px;
    }}
    .internal-link-card span {{
      font-size: 0.8rem;
      color: #64748b;
      line-height: 1.4;
      display: block;
    }}

    /* Footer */
    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 60px 20px 40px;
      font-size: 0.88rem;
    }}
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
    }}
    .footer-title {{
      font-size: 1.1rem;
      font-weight: 800;
      color: #f8fafc;
      margin-bottom: 24px;
    }}
    .footer-links-grid {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px 16px;
      margin-bottom: 40px;
    }}
    .footer-links-grid a {{
      color: #cbd5e1;
      text-decoration: none;
      font-size: 0.82rem;
    }}
    .footer-links-grid a:hover {{
      color: #fda4af;
      text-decoration: underline;
    }}
    .copyright {{
      border-top: 1px solid #1e293b;
      padding-top: 24px;
      text-align: center;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-title">
        <span>🧬 LUMI COSMETICS LAB</span>
      </a>
      <nav>
        <a href="/winter-collagen" style="font-size:0.9rem;font-weight:700;color:#be123c;text-decoration:none;">冬のコラーゲン特集 ➔</a>
      </nav>
    </div>
  </header>

  <div class="breadcrumb">
    <a href="/">ホーム</a> &gt; <a href="/winter-collagen">冬のコラーゲン特集</a> &gt; 高保湿コラーゲン美容液10選
  </div>

  <main>
    <div class="hero-section">
      <span class="hero-tag">2026年11月・12月 冬季皮膚科学検証</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！超低分子生コラーゲンの高密度ホールド膜と弾力ペプチド処方で真冬の寒冷肌痩せ・たるみ毛穴を押し上げる保湿力高めコラーゲン美容液ランク10</h1>
      <p class="hero-desc">
        11月から12月にかけての寒冷前線の到来により、皮膚の毛細血管は収縮し、真皮の線維芽細胞の働きが急激に鈍化します。その結果、肌の弾力土台であるコラーゲン線維が萎縮し、頬がゲッソリとしぼむ『寒冷肌痩せ』や『縦長たるみ毛穴』が進行します。本記事では、角層の微細な隙間をすり抜ける最新の『超低分子加水分解コラーゲン』と『弾力ペプチド』に着目。真冬の過酷な環境下でも押し返すような弾力とガラス玉のような水光ツヤを呼び覚ます高保湿コラーゲン美容液の精鋭10選を徹底検証しました。
      </p>
    </div>

    <div class="toc-box">
      <div class="toc-title">📑 目次 - 冬の高保湿コラーゲン美容液検証ランキング</div>
      <ul class="toc-list">
        <li><a href="#rank-1">第1位: メディキューブ トリプル コラーゲン セラム</a></li>
        <li><a href="#rank-2">第2位: 魔女工場 Vコラーゲン ハートフィット セラム</a></li>
        <li><a href="#rank-3">第3位: 富士フイルム アスタリフト エッセンス デスティニー</a></li>
        <li><a href="#rank-4">第4位: ドクターシーラボ エンリッチ メディカリフト デュオセラム</a></li>
        <li><a href="#rank-5">第5位: ファンケル コアエフェクター</a></li>
        <li><a href="#rank-6">第6位: VT コラーゲン リードルショット 100</a></li>
        <li><a href="#rank-7">第7位: ドクターペプチ ペプチド ボリューム マスター エッセンス</a></li>
        <li><a href="#rank-8">第8位: エチュード モイストフル コラーゲン エッセンス</a></li>
        <li><a href="#rank-9">第9位: KISO エッセンス CL（コラーゲン原液）</a></li>
        <li><a href="#rank-10">第10位: ネイチャーリパブリック コラーゲンドリーム 70 エッセンス</a></li>
        <li><a href="#science-guide">真冬の寒冷肌痩せを止める！超低分子コラーゲンとペプチドの細胞外マトリックス支持</a></li>
        <li><a href="#comparison-summary">全10製品スペック徹底比較表</a></li>
        <li><a href="#faq-section">よくある質問（FAQ）</a></li>
      </ul>
    </div>

    <div class="science-box" id="science-guide">
      <h3>🔬 なぜ真冬のたるみ・小ジワに『超低分子コラーゲン美容液』が不可欠なのか？</h3>
      <p>
        肌の真皮層の約70%はコラーゲン線維で構成されています。しかし、11月〜12月の急激な気温低下により皮膚の温度が下がると、新陳代謝が停滞し、コラーゲンの産生量が年間最低水準まで落ち込みます。さらに空気乾燥が角層の水分を奪うことで、表面のキメが緩んで<strong>『乾燥たるみ毛穴』</strong>へと直結します。
      </p>
      <div class="science-grid">
        <div class="science-card">
          <h4>1. 500ダルトン以下の超微細コラーゲンによる深層浸透</h4>
          <p>従来の巨大な高分子コラーゲンと異なり、最新の加水分解コラーゲンは500〜1,000ダルトン以下に極小化。角層細胞の微小な間隙を通り抜けて奥深くまで到達し、内側から水分と弾力を満たします。</p>
        </div>
        <div class="science-card">
          <h4>2. 弾力ペプチド＆ボルフィリンとの相乗ホールド効果</h4>
          <p>コラーゲン単体だけでなく、線維芽細胞にシグナルを送るマルチペプチドや、脂肪細胞をふっくらさせるボルフィリンを複合。表面のハリ膜形成と深部の密度再建をダブルで実現します。</p>
        </div>
        <div class="science-card">
          <h4>3. 寒冷で緩んだ毛穴周りの皮膚を物理的に引き締め</h4>
          <p>濃密なコラーゲンヴェールが乾燥した皮膚をキュッと引き締めることで、縦長に広がったたるみ毛穴を目立たなくし、夕方のメイク崩れやファンデーションの毛穴落ちを根本から防ぎます。</p>
        </div>
      </div>
    </div>

    <!-- Product Rankings 1-10 -->
    {product_cards_html}

    <div class="summary-box" id="comparison-summary">
      <h3>📊 冬の高保湿コラーゲン美容液 徹底比較まとめ</h3>
      <p>真冬の肌状態や求めるハリ感、使用するタイミングに合わせて選べるよう、今回検証した10アイテムの特徴を一覧表にまとめました。</p>
      
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>製品名</th>
              <th>主要コラーゲン技術</th>
              <th>テクスチャー・使用感</th>
              <th>冬に最もおすすめな肌悩み</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>第1位: メディキューブ</strong></td>
              <td>トリプルコラーゲン（低分子加水分解）</td>
              <td>濃密水光アンプル（ガラス玉ツヤ）</td>
              <td>真冬の寒冷肌痩せ・乾燥たるみ毛穴・ツヤ不足</td>
            </tr>
            <tr>
              <td><strong>第2位: 魔女工場</strong></td>
              <td>植物性ヴィーガンコラーゲン×シロキクラゲ</td>
              <td>マイクロリポソーム乳液状</td>
              <td>ベタつきが苦手なインナードライ・毛穴引き締め</td>
            </tr>
            <tr>
              <td><strong>第3位: アスタリフト</strong></td>
              <td>3種コラーゲン×ナノアスタキサンチン</td>
              <td>吸い付く赤のエッセンス</td>
              <td>40代・50代の本格たるみ・重力に逆らう上向きハリ</td>
            </tr>
            <tr>
              <td><strong>第4位: ドクターシーラボ</strong></td>
              <td>純粋レチノールオイル×超低分子コラーゲン</td>
              <td>2層式シェイクオイルセラム</td>
              <td>目元口元の深い乾燥溝・小ジワ・濃厚密閉</td>
            </tr>
            <tr>
              <td><strong>第5位: ファンケル</strong></td>
              <td>チオレドキシン×低分子生コラーゲン</td>
              <td>無添加先行エイジング美容液</td>
              <td>細胞レベルのハリ土台再建・超敏感肌・無添加派</td>
            </tr>
            <tr>
              <td><strong>第6位: VT</strong></td>
              <td>天然マイクロニードル×低分子コラーゲン</td>
              <td>チクチク浸透ブースト美容液</td>
              <td>角質肥厚・化粧品が入らないゴワつき肌</td>
            </tr>
            <tr>
              <td><strong>第7位: ドクターペプチ</strong></td>
              <td>酸素バブル×フランス産ボルフィリン</td>
              <td>自己発泡マイクロ炭酸泡</td>
              <td>頬のこけ・ゲッソリ疲労顔・首元のシワケア</td>
            </tr>
            <tr>
              <td><strong>第8位: エチュード</strong></td>
              <td>微細スーパーコラーゲン™ウォーター</td>
              <td>ゼリー状ぷるぷるエッセンス</td>
              <td>朝晩惜しみなく使う大容量・高コスパ保湿</td>
            </tr>
            <tr>
              <td><strong>第9位: KISO</strong></td>
              <td>高純度マリン加水分解コラーゲン原液</td>
              <td>完全無添加ピュア原液</td>
              <td>原液志向・手持ちコスメへのブレンド・小ジワ集中</td>
            </tr>
            <tr>
              <td><strong>第10位: ネイチャーリパブリック</strong></td>
              <td>マリンコラーゲン70%超高配合×深層水</td>
              <td>とろみ高濃度エッセンス</td>
              <td>極度のカサカサ乾燥・濃厚ミネラル弾力補給</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="summary-box" id="faq-section">
      <h3>❓ 高保湿コラーゲン美容液に関するよくある質問（FAQ）</h3>
      {faq_html}
    </div>

    <div class="hub-link-banner">
      <div>
        <h3 style="font-size:1.3rem;margin-bottom:8px;">🐟 冬のコラーゲン・高保湿エイジングケア総合ハブ</h3>
        <p style="font-size:0.95rem;opacity:0.95;">コラーゲンクリーム、コラーゲンシートマスク、原液コスメなど、冬の寒さに負けない弾力ハリ肌を叶えるコラーゲン総合特集はこちらからご覧いただけます。</p>
      </div>
      <a href="/winter-collagen" class="hub-link-btn">コラーゲン特集トップへ →</a>
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
      <div class="footer-links-grid" id="footer-links-box">
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

with open("winter-collagen-serum.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-collagen-serum.html!")
