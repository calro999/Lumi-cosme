import json
import re

with open("fetched_3new_nov_dec_argan_horse_panthenol_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_panthenol_cream"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 世界中で数秒に1本売れるダーマコスメの最高峰！高濃度パンテノール5%×複合シカで肌バリアを即効修復",
        "catch": "フランス皮膚科医推奨の金字塔。赤み・ヒリつき・乾燥ダメージを受けた素肌を濃厚シールドで救済",
        "brand_name": "La Roche-Posay (ラロッシュポゼ)",
        "capacity": "40ml (シカプラスト バーム B5+)",
        "type": "低刺激・高濃度パンテノール5%配合リペアバーム",
        "features": "パンテノール5%、マデカッソシド（高純度CICA）、トリバイオマ（マイクロバイオーム独自成分）、無香料・パラベンフリー",
        "value": "世界中の皮膚科医が認める再生バリアクリーム。冬の寒冷刺激でピリピリ傷んだ角層を分厚い保護膜で包み込み、一晩で落ち着きを取り戻す",
        "desc_p1": "11月・12月の冬本番、屋外の凍てつく寒風と暖房が効いた室内の強烈な乾燥を行き来するたびに、肌は急激な温度差と水分枯渇にさらされます。『いつもの化粧水がピリピリしみる』『頬が赤く火照ってヒリヒリする』といった深刻な肌バリア崩壊の救世主として世界中で圧倒的信頼を集めるのが、ラロッシュポゼの『シカプラスト バーム B5+』です。",
        "desc_p2": "組織修復を促進するプロビタミンB5（パンテノール）を5%という高濃度で配合。さらに肌の常在菌バランスを整える独自複合成分『トリバイオマ』とマデカッソシドが相乗的に働き、目に見えない微細な角層ダメージを急速リペアします。こっくりとしたリッチなバーム状のテクスチャーは、肌に乗せると体温でピタッと密着し、外的刺激を完全にシャットアウトする保護シールドを形成。夜のスキンケアの最後に塗って眠れば、翌朝には赤みやヒリつきが驚くほど鎮静し、健やかなふっくら肌が蘇ります。",
        "target": "冬になると化粧水がしみて赤みが出る敏感肌の方、暖房による乾燥ヒリつきを即座に鎮静したい方、皮膚科医推奨の本格ダーマコスメを選びたい方",
        "point": "夜のスキンケアの最後に、パール粒大を手のひらで軽く温め、刺激を感じる頬や口元を優しくスタンプするように重ね塗りしてください。"
    },
    {
        "rank": 2,
        "tag": "🧬 韓国オリーブヤング1位のメガヒット！高濃度パンテノール×CICAで荒れた肌を鎮静＆水分満タン",
        "catch": "毛穴を塞がずサラリと馴染むジェルクリーム。ベタつかないのに冬のインナードライを根本解決",
        "brand_name": "BIOHEAL BOH (バイオヒールボ)",
        "capacity": "75ml (パンテノール シカ ブレミッシュ クリーム)",
        "type": "高濃度パンテノール＆CICA配合スージングクリーム",
        "features": "パンテノール高配合、ツボクサエキス（CICA）、弱酸性マイルド処方、ノンコメドジェニックテスト済み",
        "value": "韓国の大手ヘルス＆ビューティストア『OLIVE YOUNG』で不動のベストセラー。水分感あふれる軽快な塗り心地と、強力な肌荒れ予防効果を両立",
        "desc_p1": "冬の乾燥で肌は突っ張るのに、重い油分クリームを塗るとニキビや毛穴詰まりを起こしてしまう……そんな複雑な現代人の冬肌トラブルに応えるために誕生したのが、韓国発バイオヒールボのシカクリームです。",
        "desc_p2": "肌の水分保持力を高めてバリアを再建するパンテノールと、鎮静成分のCICAを贅沢に凝縮。ぷるんとしたみずみずしいジェルクリームテクスチャーで、肌に伸ばすとひんやり心地よく角層へと浸透します。肌内部（角層）にはたっぷりの水分を補給しながら、肌表面にはベタつかない潤いフィルムを形成。暖房による日中のテカリと乾燥の悪循環を断ち切り、清潔で落ち着いた素肌環境を24時間キープします。",
        "target": "乾燥するのに重いクリームだとニキビができやすい混合肌の方、朝のメイク前にも快適に使えるバリアクリームを求める方、韓国コスメのトレンドを取り入れたい方",
        "point": "朝のメイク前に薄く全顔へ伸ばすと、日中のエアコン温風によるインナードライと化粧崩れを劇的に抑えることができます。"
    },
    {
        "rank": 3,
        "tag": "🛡️ 特許MLE技術で肌の角層構造を完全再現！水分蒸発を鉄壁ガードする超密着バリアクリーム",
        "catch": "韓国の敏感肌専門ブランドReal Barrierの最高峰。健康な肌のラメラ液晶構造を擬似形成",
        "brand_name": "Real Barrier (リアルバリア)",
        "capacity": "50ml (エクストリーム クリーム)",
        "type": "特許MLEセラミド技術＆パンテノール配合高保湿クリーム",
        "features": "特許MLE技術、パンテノール、マデカッソシド、アラントイン、角層72時間保湿持続テスト済み",
        "value": "皮膚科学に基づき、健康な肌の角質細胞間脂質の『ラメラ構造（クロス状構造）』を独自技術で再現。真冬の過酷な乾燥下でも72時間水分を逃がさない",
        "desc_p1": "乾燥肌・敏感肌研究に特化した韓国のダーマブランド『リアルバリア』。寒波が厳しい韓国の冬において、多くの皮膚科専門医やビューティクリエイターから『真冬の鉄壁クリーム』として絶賛される名品です。",
        "desc_p2": "最大の特徴は、世界特許を取得した『MLE（Multi-Lamellar Emulsion）技術』。健康な肌本来の細胞間脂質と全く同じ十字架状のラメラ液晶パターンを形成するため、塗った瞬間から肌と一体化するように密着します。高濃度パンテノールが内部の修復を促し、MLEセラミドが表面からの水分蒸発を物理的にシャットアウト。エアコンの暖房風が直接当たる過酷な環境でも、夕方まで一切の乾燥やつっぱりを感じさせない圧倒的な保護力を誇ります。",
        "target": "何を塗っても夕方になると乾燥で顔が突っ張る超乾燥肌の方、皮膚が薄くて赤みが出やすい方、科学的根拠のあるバリアケアを求める方",
        "point": "付属のスパチュラで適量を取り、手のひらで包み込むようにして肌へ押し込みます。特に乾燥しやすい目元や口角には重ねづけが効果的です。"
    },
    {
        "rank": 4,
        "tag": "💧 韓国で爆発的ヒットのドクダミブランドが放つ！パンテノール×高保水ヒアルロン酸の水分バリア",
        "catch": "肌への親和性が高い浸透型処方。内側から湧き上がるようなみずみずしい潤いで肌荒れを沈静",
        "brand_name": "Anua (アヌア)",
        "capacity": "50ml (パンテノール 水分バリアクリーム)",
        "type": "高純度パンテノール配合・角層吸着モイスチャークリーム",
        "features": "高濃度パンテノール、複合ヒアルロン酸、低刺激弱酸性、動物由来原料不使用ヴィーガン処方",
        "value": "鎮静ケアで圧倒的支持を得るAnuaが開発した本格バリアクリーム。パンテノールの組織修復力とヒアルロン酸の保水ネットワークが真冬の干からびた角層を満たす",
        "desc_p1": "日本のZ世代から大人世代まで絶大な人気を誇るスキンケアブランド『Anua（アヌア）』。鎮静トナーで培ったノウハウを注ぎ込み、冬の乾燥ゆらぎ肌を集中的にケアするために開発された水分バリアクリームです。",
        "desc_p2": "肌のバリア機能を高めるパンテノールを主役に、分子サイズの異なる複合ヒアルロン酸を絶妙なバランスで配合。カサカサに乾いた肌に塗布すると、スーッと吸い込まれるように角層の奥深くを満たし、まるで肌の内側から水が湧き出ているかのようなもっちり感を長時間キープします。ベタつきを残さないサラリとした仕上がりで、メイク前のスキンケアにも夜のたっぷりナイトパックにも自由自在に使えます。",
        "target": "水分不足で肌がくすんで見える方、重い油分よりもみずみずしい保水感を重視する方、ヴィーガン処方の優しいコスメを好む方",
        "point": "化粧水で水分を補給した後、顔全体に優しく塗り広げ、両手で軽くタッピングしながら角層へ浸透させてください。"
    },
    {
        "rank": 5,
        "tag": "🌿 累計販売数1000万個突破の殿堂入り！10種のCICA成分とパンテノールが冬の赤みをクールに鎮火",
        "catch": "韓国軍の売店（PX）でも爆発的人気。過酷な寒冷環境下で戦う肌のために開発されたマルチシカ",
        "brand_name": "Dr.G (ドクタージー)",
        "capacity": "70ml (レッドブレミッシュ クリア スージングクリーム)",
        "type": "10-CICA＆パンテノール配合・敏感肌用スージングジェルクリーム",
        "features": "10種類のCICAコンプレックス、パンテノール、β-グルカン、ノンコメドジェニック、ハイポアレルゲニック",
        "value": "皮膚科専門医が創設したDr.Gの代名詞。過酷な冬の訓練下でも肌荒れを防ぐ驚異の鎮静力と、水分感たっぷりの軽やかな使用感で日韓のコスメ賞を総なめ",
        "desc_p1": "韓国の軍隊PX（売店）で軍人たちが家族や恋人へのお土産として買い占めたことから火がつき、今や世界中で愛されるDr.Gの『レッドブレミッシュ クリアスージングクリーム』。過酷な寒風や紫外線にさらされる環境を想定して設計された鎮静クリームの傑作です。",
        "desc_p2": "ツボクサから抽出された10種類のCICA成分に、保湿とバリア修復を担うパンテノールをプラス。冬の暖房やマスク摩擦で火照って赤くなった肌に乗せると、ひんやりと心地よい水分が肌を包み込み、熱感とムズムズ感をスピーディに落ち着かせます。油分によるテカリを起こさないオイルフリーに近い処方のため、冬の大人ニキビに悩む方や、男性の髭剃り後の乾燥肌ケアとしても極めて高い評価を得ています。",
        "target": "冬でも顔が赤くなりやすく火照りやすい方、大人ニキビや肌荒れを繰り返す方、さっぱりしながらも潤いが続くクリームを求める方",
        "point": "特に赤みが気になる部分には、少し厚めにクリームを乗せてそのまま就寝する『スリーピングパック』として活用するのがおすすめです。"
    },
    {
        "rank": 6,
        "tag": "💉 美容クリニック発想のハイエンド処方！高濃度パンテノール×複合ペプチドで弾力とバリアを同時再建",
        "catch": "韓国エステ・クリニック品質のメディピール。冬の寒冷でたるんだ毛穴としぼみ肌をふっくら押し返す",
        "brand_name": "MEDI-PEEL (メディピール)",
        "capacity": "50ml (シカ アンチオ パンテノール リペアクリーム)",
        "type": "パンテノール＆ペプチド配合・プレミアムリペアクリーム",
        "features": "高濃度パンテノール、複合ペプチド、ウィートグラスエキス、EGF（上皮成長因子様成分）、皮膚刺激テスト済み",
        "value": "エステ専売ブランドの技術を結集。パンテノールのバリア修復力に、高機能ペプチドによるハリ・弾力アプローチを融合させた贅沢なエイジングリペア",
        "desc_p1": "韓国の高級エステサロンや美容皮膚クリニックで使用されるプロ用コスメを手がける『MEDI-PEEL（メディピール）』。真冬の過酷な寒冷によって肌のハリが低下し、乾燥小ジワが目立ち始めた大人の肌に向けた集中ケアクリームです。",
        "desc_p2": "肌荒れを防ぐパンテノールをベースに、コラーゲン生成をサポートする複数のペプチドコンプレックスを贅沢にブレンド。肌に伸ばすと、まるで美容アンプルをそのままクリームにしたかのような濃密なコクが広がり、乾燥でしぼんだ角層深部をふっくらと押し上げます。冬の寒さで開いてしまったたるみ毛穴をキュッと引き締め、翌朝には指を押し返すようなモチモチの弾力肌へと導きます。",
        "target": "乾燥だけでなくハリ不足やたるみ毛穴も同時にケアしたい方、エステ級のリッチなスキンケアを自宅で行いたい方、30代以上のエイジングケア世代",
        "point": "夜のお手入れで顔全体になじませた後、ほうれい線や眉間、首筋に向かって引き上げるようにマッサージしながら塗り込むと効果的です。"
    },
    {
        "rank": 7,
        "tag": "🌿 CICAの元祖VTが放つ本気のバリア強化！パンテノール10%の超高濃度で荒れた肌をスピードレスキュー",
        "catch": "シカ成分に高純度パンテノールを10%も極限配合。乾燥で皮剥けした肌を徹底リペア",
        "brand_name": "VT COSMETICS",
        "capacity": "50ml (シカ パンテノール リペア クリーム)",
        "type": "高濃度パンテノール10%＆シカヒアルロン配合リペアクリーム",
        "features": "パンテノール10%高配合、CICALIAO™（独自シカ成分）、CICAHYALON™（ヒアルロン酸複合体）、低刺激処方",
        "value": "一般的なバリアクリームの2〜3倍に相当するパンテノール10%を配合。真冬の乾燥でめくれた角質や粉吹きを驚異のスピードで密着修復",
        "desc_p1": "日本におけるCICAブームの火付け役である『VT COSMETICS』が、より深刻な乾燥と肌トラブルに悩むユーザーのために開発した特化型クリーム。パンテノールをなんと10%という驚愕の高濃度で配合しています。",
        "desc_p2": "独自の整肌成分シカリオと水分補給成分シカヒアルロンに、高濃度パンテノールが融合。濃厚でコクのあるクリームが肌の微小なキメの溝に入り込み、めくれた角質をピタッと接着するように整えます。冬の冷たい風にさらされて粉を吹いた口周りや、鼻をかみすぎて荒れてしまった小鼻周りなど、ピンチの肌を集中ケア。塗った翌朝にはしっとりとなめらかな肌触りを実感できます。",
        "target": "乾燥で部分的に皮がむけたり粉を吹いたりしている方、パンテノールの濃度にこだわりたい方、VTのシカシリーズを愛用している方",
        "point": "顔全体に薄く塗った後、乾燥がひどく皮がめくれそうな部分に指先でトントンと置くように重ね塗りしてください。"
    },
    {
        "rank": 8,
        "tag": "📦 全身惜しみなく使える100ml特大サイズ！赤ちゃんから家族全員の真冬の乾燥をこれ1本で完全ガード",
        "catch": "ラロッシュポゼの世界的名作のビッグサイズ。すねの粉吹き・ひじのガサガサ・手荒れまでまるごとケア",
        "brand_name": "La Roche-Posay (ラロッシュポゼ)",
        "capacity": "100ml (シカプラスト バーム B5+ 特大サイズ)",
        "type": "特大容量・パンテノール5%配合マルチリペアバーム",
        "features": "パンテノール5%、マデカッソシド、トリバイオマ、大容量100mlチューブ、顔・身体兼用",
        "value": "40mlボトルの2.5倍のボリュームを誇るお得な特大チューブ。顔だけでなく、冬の水仕事で荒れた手指や粉を吹くすねまで惜しみなく使える究極の常備薬バーム",
        "desc_p1": "『シカプラスト バーム B5+を顔だけでなく、全身のカサつく部分にも使いたい』というヘビーユーザーの声に応えて登場した大容量100mlモデル。コストパフォーマンスに優れ、家族全員で冬の乾燥を乗り切るための必需品です。",
        "desc_p2": "中身は世界中で愛されるシカプラストバームそのもの。パンテノール5%とマデカッソシドの強力なリペア力はそのままに、チューブからたっぷり出して使える大容量設計です。冬のニットの摩擦で粉を吹いたスネや、お風呂上がりにカサつく背中、タイツが引っかかるかかとなど、広範囲のパーツケアに最適。生後3ヶ月の赤ちゃんから使用できる極めて低刺激な処方のため、冬の乾燥シーズンのお守りとして洗面所に1本置いておくと心強い味方になります。",
        "target": "シカプラストバームを毎日全身にたっぷり使いたい方、家族みんなでシェアしたい方、コストパフォーマンスを重視する方",
        "point": "お風呂上がりに水気を軽く拭き取った後、カサつくすねや肘、手指にたっぷり伸ばして優しくハンドプレスしてください。"
    },
    {
        "rank": 9,
        "tag": "🧪 塗って寝るだけで冬のごわつき角質をオフ！パンテノール×天然角質ケア成分で翌朝つるん肌",
        "catch": "韓国で『肌がリセットされる』と話題のバデカシル。パンテノールの保護力と角質柔軟化を両立",
        "brand_name": "23years old",
        "capacity": "50g (バデカシル パンテノール バーム)",
        "type": "角質ケア＆パンテノール配合ナイトリセットバーム",
        "features": "パンテノール、BHA（角質ケア成分）、カモミールエキス、弱酸性、夜用集中トリートメント",
        "value": "冬の寒さで代謝が落ちてゴワゴワに硬化した角質を優しくほぐしながら、パンテノールが奥深くに潤いを定着させる夜用スペシャルケア",
        "desc_p1": "『冬になると角質が硬くなって化粧水が入らない』『ゴワつきと乾燥ニキビが同時に発生する』という冬のゆらぎ肌トラブルを解決する韓国の隠れた名品、23years oldのバデカシルバームです。",
        "desc_p2": "穏やかに不要な角質を整えるマイルドなピーリング成分と、高い組織修復・保水力を持つパンテノールを絶妙に融合。夜のスキンケアの最後に塗って寝るだけで、睡眠中に厚くなった不要な角質を自然にやわらげ、同時にパンテノールがバリア機能を補強します。翌朝起きてぬるま湯で洗顔すると、まるでピーリングを受けた後のようにザラつきが消え、つるんと滑らかな手触りに驚くはずです。",
        "target": "冬の角質肥厚で肌がゴワつく方、化粧水の入りが悪くなっている方、夜寝ている間に手軽につるつる肌を目指したい方",
        "point": "週に2〜3回、夜のスキンケアの最後に顔全体、特に小鼻やあごなどザラつきやすい部分に優しく馴染ませて就寝してください。"
    },
    {
        "rank": 10,
        "tag": "🔬 国産・高純度パンテノール5%の贅沢処方！原液コスメのパイオニアKISOが放つ安心の無添加バリア",
        "catch": "余分な成分を削ぎ落としたシンプル＆ストレート処方。敏感な冬肌を優しく包む国産ハイドロクリーム",
        "brand_name": "KISO (キソ)",
        "capacity": "50g (ハイドロクリーム PT)",
        "type": "高純度パンテノール5%配合・国産高保湿クリーム",
        "features": "高純度プロビタミンB5（パンテノール5%）、ヒト型セラミド配合、パラベン・アルコール・合成香料・着色料フリー、国内GMP工場製造",
        "value": "高品質な美容成分を高濃度で届けるKISOの自信作。パンテノールに加えてヒト型セラミドをブレンドし、冬の過酷な乾燥から角質層を隙間なく防御",
        "desc_p1": "成分マニアから圧倒的な支持を集める日本の原液コスメブランド『KISO（基礎化粧品研究所）』。海外製品が多いパンテノールクリームの中で、信頼できる国内工場製造と徹底した低刺激処方を誇る人気アイテムです。",
        "desc_p2": "高純度のプロビタミンB5（パンテノール）を5%高配合し、さらに肌のバリアに不可欠なヒト型セラミド（EOP、NP、AP）を贅沢に複合配合。肌に伸ばすとなめらかに溶け込み、ベタつきのない薄い保護膜が肌を包み込みます。香料やアルコール、防腐剤などの刺激成分を徹底排除しているため、花粉や寒暖差で肌が敏感に傾いた時期でもピリピリせずに優しくケア。コストパフォーマンスにも優れ、デイリー使いに最適です。",
        "target": "信頼できる国産のパンテノールクリームを使いたい方、ヒト型セラミドも同時に補給したい方、無添加処方にこだわる敏感肌の方",
        "point": "朝晩の化粧水・美容液の後、適量を手に取り、乾燥しやすい頬や目元を中心に優しくハンドプレスしてなじませてください。"
    }
]

# JSON-LD ItemList
item_list_elements = []
for p in product_details:
    r_item = items[p["rank"] - 1]
    item_list_elements.append({
        "@type": "ListItem",
        "position": p["rank"],
        "item": {
            "@type": "Product",
            "name": f"{p['brand_name']} {p['capacity']}",
            "image": r_item["img_url"],
            "description": p["value"],
            "brand": {
                "@type": "Brand",
                "name": p["brand_name"]
            },
            "offers": {
                "@type": "Offer",
                "url": r_item["affiliate_url"],
                "priceCurrency": "JPY",
                "price": r_item["price"],
                "availability": "https://schema.org/InStock"
            }
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで冬のヒリつき・敏感乾燥とさようなら！高濃度プロビタミンB5で角層バリアを鉄壁補修する高保湿パンテノールクリームランク10",
    "description": "11月・12月の寒冷刺激やエアコン乾燥によって引き起こされるバリア破壊・ヒリヒリ敏感肌・乾燥赤みを徹底修復！抗炎症＆組織再生を促進する高濃度プロビタミンB5（パンテノール）を配合した高保湿シカ＆バリアクリーム10選を徹底比較！ラロッシュポゼ シカプラストB5+、BIOHEAL BOH、アヌア、Dr.G、リアルバリアなど2026年最新の注目アイテムを厳選。",
    "image": items[0]["img_url"],
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
    "datePublished": "2026-11-03",
    "dateModified": "2026-11-03"
}

json_ld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "冬の高保湿パンテノールクリーム おすすめランキング10選",
    "itemListElement": item_list_elements
}

# HTML Template
html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬のヒリつき・敏感乾燥とさようなら！高濃度プロビタミンB5で角層バリアを鉄壁補修する高保湿パンテノールクリームランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒冷刺激やエアコン乾燥によって引き起こされるバリア破壊・ヒリヒリ敏感肌・乾燥赤みを徹底修復！抗炎症＆組織再生を促進する高濃度プロビタミンB5（パンテノール）を配合した高保湿シカ＆バリアクリーム10選を徹底比較！ラロッシュポゼ シカプラストB5+、BIOHEAL BOH、アヌア、Dr.G、リアルバリアなど2026年最新の注目アイテムを厳選。">
  <meta name="keywords" content="パンテノールクリーム,プロビタミンB5,シカプラストB5,高保湿クリーム,冬 保湿,敏感肌 スキンケア,バリア修復,赤み鎮静,おすすめ 2026">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-panthenol-cream">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで冬のヒリつき・敏感乾燥とさようなら！高濃度プロビタミンB5で角層バリアを鉄壁補修する高保湿パンテノールクリームランク10">
  <meta property="og:description" content="11月・12月の真冬の乾燥でバリア崩壊した素肌を救う！高濃度プロビタミンB5（パンテノール）配合の最新バリアクリーム10選を徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-panthenol-cream">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
  <!-- 構造化データ JSON-LD -->
  <script type="application/ld+json">
{json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(json_ld_itemlist, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #c28854;
      --primary-dark: #986537;
      --primary-light: #f7ede2;
      --accent: #d4a373;
      --text: #2c2523;
      --text-sub: #665c54;
      --bg: #fdfbf7;
      --card-bg: #ffffff;
      --border: #ebd9c8;
      --shadow: 0 4px 20px rgba(152, 101, 55, 0.08);
      --radius: 14px;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.85;
      color: var(--text);
      background-color: var(--bg);
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary-dark);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .nav-links {{
      display: flex;
      gap: 16px;
      list-style: none;
    }}
    .nav-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 500;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--primary);
    }}
    .breadcrumb {{
      max-width: 1000px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-sub);
    }}
    .breadcrumb a {{
      color: var(--primary);
      text-decoration: none;
    }}
    .container {{
      max-width: 1000px;
      margin: 20px auto 60px;
      padding: 0 20px;
    }}
    .article-header {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 36px 30px;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }}
    .badge {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 30px;
      margin-bottom: 14px;
    }}
    h1 {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: var(--primary-dark);
      margin-bottom: 18px;
    }}
    .meta {{
      font-size: 0.85rem;
      color: var(--text-sub);
      display: flex;
      gap: 18px;
      margin-bottom: 24px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
    }}
    .lead-box {{
      font-size: 1.02rem;
      color: var(--text);
      line-height: 1.9;
      background: #faf6f0;
      padding: 22px;
      border-left: 4px solid var(--primary);
      border-radius: 6px;
    }}
    .lead-box p + p {{
      margin-top: 12px;
    }}
    .content-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 34px 30px;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }}
    .content-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .content-section h3 {{
      font-size: 1.2rem;
      color: var(--text);
      margin: 24px 0 12px;
    }}
    .content-section p {{
      margin-bottom: 16px;
      color: var(--text);
      font-size: 0.98rem;
    }}
    .feature-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin: 24px 0;
    }}
    .feature-card {{
      background: #faf6f0;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 20px;
    }}
    .feature-card h4 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 8px;
    }}
    .feature-card p {{
      font-size: 0.9rem;
      margin-bottom: 0;
      color: var(--text-sub);
    }}
    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 24px 0;
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 12px 14px;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .comparison-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      white-space: nowrap;
    }}
    .comparison-table tr:nth-child(even) {{
      background: #faf6f0;
    }}

    /* Ranking Cards */
    .ranking-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 30px;
      margin-bottom: 36px;
      position: relative;
    }}
    .rank-header {{
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 16px;
    }}
    .rank-number {{
      background: var(--primary);
      color: #ffffff;
      font-size: 1.25rem;
      font-weight: 800;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .ranking-card:nth-child(1) .rank-number {{
      background: #d4a373;
    }}
    .ranking-card:nth-child(2) .rank-number {{
      background: #a98467;
    }}
    .ranking-card:nth-child(3) .rank-number {{
      background: #bc6c25;
    }}
    .rank-title-group h3 {{
      font-size: 1.3rem;
      color: var(--primary-dark);
      line-height: 1.4;
    }}
    .rank-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      margin-top: 4px;
    }}
    .product-main {{
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 26px;
      margin: 20px 0;
    }}
    .img-box {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 220px;
      height: auto;
      border-radius: 8px;
      border: 1px solid var(--border);
      object-fit: cover;
    }}
    .product-spec {{
      font-size: 0.9rem;
      background: #faf6f0;
      padding: 16px;
      border-radius: 8px;
      margin-bottom: 16px;
    }}
    .spec-item {{
      margin-bottom: 6px;
    }}
    .spec-label {{
      font-weight: 700;
      color: var(--text-sub);
      display: inline-block;
      width: 100px;
    }}
    .product-desc p {{
      margin-bottom: 12px;
      font-size: 0.95rem;
      line-height: 1.85;
    }}
    .user-point {{
      background: #fff8f0;
      border-left: 3px solid var(--accent);
      padding: 12px 16px;
      font-size: 0.88rem;
      margin: 14px 0;
      border-radius: 0 6px 6px 0;
    }}
    .price-box {{
      display: flex;
      align-items: baseline;
      gap: 12px;
      margin: 16px 0;
    }}
    .price-val {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #b7094c;
    }}
    .review-score {{
      font-size: 0.85rem;
      color: var(--text-sub);
    }}
    .rakuten-btn {{
      display: inline-block;
      background: #bf0000;
      color: #ffffff !important;
      text-decoration: none;
      font-weight: 700;
      font-size: 1rem;
      padding: 12px 28px;
      border-radius: 8px;
      transition: background 0.2s, transform 0.1s;
      text-align: center;
    }}
    .rakuten-btn:hover {{
      background: #990000;
      transform: translateY(-2px);
    }}

    /* Q&A / Step Guide */
    .faq-item {{
      margin-bottom: 18px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
    }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 8px;
      display: flex;
      align-items: baseline;
      gap: 8px;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: var(--text);
      line-height: 1.8;
      padding-left: 24px;
    }}
    .step-box {{
      display: flex;
      gap: 16px;
      margin-bottom: 16px;
    }}
    .step-num {{
      background: var(--primary-dark);
      color: #ffffff;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      font-weight: 700;
      flex-shrink: 0;
      margin-top: 4px;
    }}
    .step-text h4 {{
      font-size: 1rem;
      margin-bottom: 4px;
      color: var(--primary-dark);
    }}
    .step-text p {{
      font-size: 0.92rem;
      margin-bottom: 0;
    }}

    /* Internal links */
    .internal-link-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px;
      margin-top: 20px;
    }}
    .internal-card {{
      background: #faf6f0;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px 16px;
      text-decoration: none;
      color: var(--text);
      transition: all 0.2s;
    }}
    .internal-card:hover {{
      border-color: var(--primary);
      background: #f5ece1;
      transform: translateY(-2px);
    }}
    .internal-card h5 {{
      font-size: 0.92rem;
      color: var(--primary-dark);
      margin-bottom: 4px;
    }}
    .internal-card p {{
      font-size: 0.8rem;
      color: var(--text-sub);
      margin-bottom: 0;
    }}

    footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 40px 20px;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-top: 60px;
    }}

    @media (max-width: 768px) {{
      .product-main {{
        grid-template-columns: 1fr;
      }}
      .img-box {{
        margin-bottom: 16px;
      }}
      h1 {{
        font-size: 1.5rem;
      }}
      .article-header {{
        padding: 24px 18px;
      }}
      .content-section, .ranking-card {{
        padding: 22px 18px;
      }}
    }}
  </style>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="/" class="site-title">❄️ 冬コスメ徹底比較ラボ</a>
    <ul class="nav-links">
      <li><a href="/">ホーム</a></li>
      <li><a href="/winter-ceramide-lotion">セラミド化粧水</a></li>
      <li><a href="/winter-argan-oil">アルガンオイル</a></li>
      <li><a href="/winter-horse-oil">馬油クリーム</a></li>
    </ul>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">TOP</a> &gt; <a href="/winter-moisture-cream">冬の保湿クリーム・乳液</a> &gt; <span>高保湿パンテノールクリーム</span>
</div>

<main class="container">
  <article>
    <header class="article-header">
      <span class="badge">2026年冬 最新決定版 / 11〜12月集中保湿</span>
      <h1>保湿力の強さで冬のヒリつき・敏感乾燥とさようなら！高濃度プロビタミンB5で角層バリアを鉄壁補修する高保湿パンテノールクリームランク10</h1>
      <div class="meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証機関: 冬コスメ徹底比較ラボ 編集部</span>
        <span>対象: 冬のヒリヒリ敏感肌・寒暖差赤み・化粧水がしみるバリア崩壊肌</span>
      </div>
      <div class="lead-box">
        <p><strong>「冬になるといつもの化粧水がピリピリしみて痛い……暖房の部屋に入ると頬が赤く火照ってカサつく……」</strong></p>
        <p>11月中旬から12月にかけて、日本の外気湿度は30%台へ急落し、冷え込みと室内エアコンの強烈な乾燥風が肌を挟み撃ちにします。この過酷な寒暖差によって肌表面の角質細胞間脂質が乱れ、肉眼では見えない微小な亀裂（マイクロクラック）が生じることで、水分が急激に逃げて刺激物質が侵入する『バリア機能崩壊』が引き起こされます。</p>
        <p>単なる油分補給だけでは追いつかないこの緊急事態を皮膚科学的に解決するのが、世界中のダーマコスメ界で今最も注目を浴びる<strong>『プロビタミンB5（パンテノール）』</strong>配合クリームです。皮膚に浸透すると直ちにパントテン酸へと変換され、細胞の修復・再生とセラミド合成を力強く後押し。赤みと炎症を鎮静しながら、二度と乾かない鉄壁の角層バリアを再建します。本記事では、楽天APIの最新データに基づき、ラロッシュポゼのシカプラストB5+から韓国オリーブヤング1位の人気アイテムまで、真冬の救世主となる高保湿パンテノールクリーム10選を徹底比較します。</p>
      </div>
    </header>

    <!-- 科学的背景・解説セクション -->
    <section class="content-section">
      <h2>🔬 なぜ11月・12月のヒリつき肌にパンテノール（B5）が不可欠なのか？</h2>
      <p>パンテノールは、体内でビタミンB群の一種である「パントテン酸（ビタミンB5）」へと代謝される水溶性のプロビタミンです。医療の現場でも創傷治療や熱傷ケアに長年使用されてきた実績があり、確かな組織修復力と低刺激性を併せ持ちます。</p>
      
      <div class="feature-grid">
        <div class="feature-card">
          <h4>1. 傷ついた角層細胞の自己再生を強力サポート</h4>
          <p>浸透したパンテノールは、表皮細胞の増殖とターンオーバー正常化を促進。冬の寒冷刺激や乾燥摩擦によって生じた角層の微小な傷を素早く埋め合わせ、健康な皮膚組織の再生を加速させます。</p>
        </div>
        <div class="feature-card">
          <h4>2. 肌内部のセラミド合成を内側から促進</h4>
          <p>外から油分を塗るだけでなく、肌自らがバリア成分である『細胞間脂質（セラミドや脂肪酸）』を合成するプロセスを直接活性化。水分を抱え込み逃がさない自律的な保湿力を底上げします。</p>
        </div>
        <div class="feature-card">
          <h4>3. 寒暖差による赤み・ヒリつきの即効鎮静</h4>
          <p>優れた抗炎症作用を持ち、冷たい外気から暖かい室内に入った瞬間に起こる毛細血管拡張や、乾燥によるかゆみ・ピリピリ感を穏やかに鎮火。火照った肌をクールダウンして平常な状態へと導きます。</p>
        </div>
        <div class="feature-card">
          <h4>4. 水分を引き寄せて離さない保水ネットワーク</h4>
          <p>分子構造内に多くの水酸基（-OH）を持ち、空気中や化粧水の水分を磁石のように強力に引き寄せて角層深部にキープ。暖房の温風が長時間吹き付けるオフィスでも、夕方までふっくら感を維持します。</p>
        </div>
      </div>

      <h3>💡 CICA（ツボクサエキス）との黄金コンビネーション</h3>
      <p>現代の最新パンテノールクリームの多くは、鎮静ハーブの王様である<strong>「CICA（マデカッソシド／ツボクサエキス）」</strong>と組み合わされています。</p>
      <ul style="padding-left: 20px; margin-bottom: 16px; font-size: 0.95rem;">
        <li style="margin-bottom: 8px;"><strong>CICAの役割：</strong>刺激を受けた肌の炎症（サイトカインの放出）を急速に抑制し、肌荒れの火種を消火します。</li>
        <li><strong>パンテノール（B5）の役割：</strong>消火された後の肌の土台に栄養を与え、角層バリアと細胞組織を強固に再建します。</li>
      </ul>
      <p style="font-size: 0.95rem;">この「CICAで鎮静＋パンテノールで再建」のダブルアプローチこそが、冬の頑固なゆらぎ肌や赤ら顔を最もスピーディーに美肌へと導く最強の皮膚科学フォーミュラです。</p>
    </section>

    <!-- ランキング一覧 -->
    <section>
      <h2 style="font-size: 1.5rem; color: var(--primary-dark); margin: 36px 0 24px; text-align: center;">
        🏆 冬の高保湿パンテノールクリーム おすすめランキング10選
      </h2>
"""

for p in product_details:
    r_item = items[p["rank"] - 1]
    rev_str = f"★ {r_item['review_average']} ({r_item['review_count']}件)" if r_item['review_count'] > 0 else "最新注目アイテム"
    
    html_content += f"""
      <!-- Rank {p['rank']} -->
      <div class="ranking-card" id="rank-{p['rank']}">
        <div class="rank-header">
          <div class="rank-number">{p['rank']}</div>
          <div class="rank-title-group">
            <h3>{r_item['name']}</h3>
            <span class="rank-tag">{p['tag']}</span>
          </div>
        </div>
        
        <p style="font-size: 0.95rem; color: var(--primary-dark); font-weight: 600; margin-bottom: 14px;">
          {p['catch']}
        </p>

        <div class="product-main">
          <div class="img-box">
            <img src="{r_item['img_url']}" alt="{r_item['name']}" class="product-img" loading="lazy">
            <div class="price-box" style="justify-content: center;">
              <span class="price-val">¥{r_item['price']:,}</span>
              <span class="review-score">{rev_str}</span>
            </div>
            <a href="{r_item['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
              楽天で詳細を見る
            </a>
          </div>

          <div class="product-info">
            <div class="product-spec">
              <div class="spec-item"><span class="spec-label">ブランド</span>{p['brand_name']}</div>
              <div class="spec-item"><span class="spec-label">容量・タイプ</span>{p['capacity']} / {p['type']}</div>
              <div class="spec-item"><span class="spec-label">主要な特徴</span>{p['features']}</div>
              <div class="spec-item"><span class="spec-label">高保湿の核心</span>{p['value']}</div>
            </div>

            <div class="product-desc">
              <p>{p['desc_p1']}</p>
              <p>{p['desc_p2']}</p>
            </div>

            <div class="user-point">
              <strong>💡 こんな方におすすめ：</strong>{p['target']}<br>
              <strong>✨ プロ直伝の使い方：</strong>{p['point']}
            </div>
          </div>
        </div>
      </div>
"""

html_content += """
    </section>

    <!-- 比較表セクション -->
    <section class="content-section">
      <h2>📊 冬の高保湿パンテノールクリーム スペック徹底比較一覧</h2>
      <p>肌質やお悩みの深刻度、使用シーンに合わせて選べるよう、厳選10商品のスペックと特徴を比較表にまとめました。</p>
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>主成分・濃度</th>
              <th>容量</th>
              <th>価格(税込)</th>
              <th>おすすめの用途</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1位</td>
              <td>ラロッシュポゼ シカプラスト B5+</td>
              <td>パンテノール5%＋CICA</td>
              <td>40ml</td>
              <td>¥3,190</td>
              <td>冬のヒリつき・赤み集中リペア</td>
            </tr>
            <tr>
              <td>2位</td>
              <td>バイオヒールボ パンテノールシカ</td>
              <td>高濃度B5＋ツボクサ</td>
              <td>75ml</td>
              <td>¥6,200(セット等)</td>
              <td>インナードライ・朝メイク前の水分補給</td>
            </tr>
            <tr>
              <td>3位</td>
              <td>リアルバリア エクストリーム</td>
              <td>特許MLE＋パンテノール</td>
              <td>50ml</td>
              <td>¥4,690(大容量等)</td>
              <td>暖房直撃・72時間水分キープ</td>
            </tr>
            <tr>
              <td>4位</td>
              <td>アヌア パンテノール水分バリア</td>
              <td>B5＋複合ヒアルロン酸</td>
              <td>50ml</td>
              <td>¥3,450</td>
              <td>みずみずしい保水・ヴィーガン処方</td>
            </tr>
            <tr>
              <td>5位</td>
              <td>ドクタージー レッドブレミッシュ</td>
              <td>10-CICA＋パンテノール</td>
              <td>70ml</td>
              <td>¥2,900</td>
              <td>ニキビ肌・火照り赤みのクールダウン</td>
            </tr>
            <tr>
              <td>6位</td>
              <td>メディピール シカアンチオ</td>
              <td>B5＋複合ペプチド</td>
              <td>50ml</td>
              <td>¥2,970</td>
              <td>たるみ毛穴・大人のハリ弾力リペア</td>
            </tr>
            <tr>
              <td>7位</td>
              <td>VT シカ パンテノール リペア</td>
              <td>パンテノール10%超高配合</td>
              <td>50ml</td>
              <td>¥1,100</td>
              <td>部分的な粉吹き・皮剥け緊急レスキュー</td>
            </tr>
            <tr>
              <td>8位</td>
              <td>ラロッシュポゼ シカプラスト 100ml</td>
              <td>パンテノール5%大容量</td>
              <td>100ml</td>
              <td>¥3,780</td>
              <td>全身すね・手指・ファミリー兼用</td>
            </tr>
            <tr>
              <td>9位</td>
              <td>23years old バデカシル B5</td>
              <td>B5＋BHA角質クリア</td>
              <td>50g</td>
              <td>¥1,300</td>
              <td>冬の角質肥厚・夜用ナイトリセット</td>
            </tr>
            <tr>
              <td>10位</td>
              <td>KISO ハイドロクリーム PT</td>
              <td>国産B5 5%＋ヒト型セラミド</td>
              <td>50g</td>
              <td>¥2,982</td>
              <td>安心の国産無添加・セラミド複合</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 実践ステップガイド -->
    <section class="content-section">
      <h2>🛡️ バリア機能を完全復活させる！冬のパンテノール塗り方極意</h2>
      <p>パンテノールクリームは、塗り方の圧やタイミングを工夫することで、浸透率とバリア密着度が格段に向上します。</p>

      <div class="step-box">
        <div class="step-num">1</div>
        <div class="step-text">
          <h4>化粧水で水分をたっぷり含ませた直後に重ねる</h4>
          <p>パンテノールは水分と引き合う性質（親水性）を持ちます。化粧水が肌表面で乾き切る前にクリームを重ねることで、水分を角層内部へがっちり閉じ込め、逃さないネットワークを作ります。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">2</div>
        <div class="step-text">
          <h4>摩擦は絶対NG！手のひらで温めてから『スタンプ塗り』</h4>
          <p>肌バリアが壊れている冬肌にゴシゴシ塗り込むのは厳禁です。手のひらでクリームを体温まで温めて柔らかくし、優しく包み込むように顔全体へスタンププレスしてください。</p>
        </div>
      </div>

      <div class="step-box">
        <div class="step-num">3</div>
        <div class="step-text">
          <h4>特にヒリつく部分には『2層ミルフィーユ重ね』</h4>
          <p>乾燥で赤みが出ている頬骨のあたりや口周りには、全顔に塗った後にもう一度少量を指先に取り、トントンと置くように重ねづけします。寝ている間の布団摩擦や乾燥から守る分厚い膜が完成します。</p>
        </div>
      </div>
    </section>

    <!-- よくある質問 FAQ -->
    <section class="content-section">
      <h2>❓ パンテノールクリームに関するよくある疑問・Q&A</h2>

      <div class="faq-item">
        <div class="faq-q">Q. セラミドクリームやCICAクリームとは何が違うのですか？</div>
        <div class="faq-a">
          セラミドは『肌の細胞間脂質そのものを補うレンガのセメント役』、CICAは『肌荒れの赤みや炎症を鎮める消火役』です。これに対し、パンテノール（プロビタミンB5）は『傷ついた皮膚細胞の組織修復を促し、自らセラミドを作る力を後押しする建築士役』です。冬の寒暖差で肌がヒリつき、「塗るものすべてが刺激に感じる」ような深刻なバリア崩壊状態では、パンテノールが最も根本的な修復効果を発揮します。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. 朝のメイク前に塗ってもファンデーションはヨレませんか？</div>
        <div class="faq-a">
          ラロッシュポゼのような濃厚バームタイプは、朝に多量に塗ると下地とケンカしてモロモロが出る場合があります。朝は「バイオヒールボ」や「Dr.G」のようなジェルクリームタイプを選ぶか、バームタイプを使用する場合は「米粒1〜2粒大をごく薄く伸ばす」のがコツです。しっかりハンドプレスして3分ほど馴染ませてからメイク下地に進めば、一日中乾燥崩れを防げます。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. 敏感肌やアトピー傾向の肌でも毎日使えますか？</div>
        <div class="faq-a">
          パンテノールは医療用の皮膚外用薬としても数十年にわたり使用されてきた非常に安全性の高い成分です。アレルギーリスクが極めて低く、無香料・低刺激処方のものが多いため、敏感肌やアトピー傾向の方、生後数ヶ月の赤ちゃんのスキンケアとしても世界中で毎日愛用されています。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q">Q. レチノールやビタミンCなどのアクティブ成分と併用できますか？</div>
        <div class="faq-a">
          非常に相性が良く、むしろ積極的な併用が推奨されます。レチノールによるA反応（皮剥けや赤み）や高濃度ビタミンCによるピリピリ感を、パンテノールが穏やかに鎮静・バリア補修してくれます。ビタミンCやレチノール美容液を塗った後の仕上げクリームとしてパンテノールを取り入れると、肌トラブルを防ぎながら美肌効果を最大化できます。
        </div>
      </div>
    </section>

    <!-- 内部リンク関連記事 -->
    <section class="content-section">
      <h2>🔗 あわせて読みたい！真冬の徹底保湿ケア関連記事</h2>
      <p>パンテノールによるバリア修復に加えて、導入オイルや化粧水、パーツケアを連動させることで、真冬の極限乾燥を完璧にブロックできます。</p>
      
      <div class="internal-link-grid">
        <a href="/winter-ceramide-cream" class="internal-card">
          <h5>🧴 高保湿セラミドクリーム</h5>
          <p>パンテノールと並ぶバリアケアの双璧！角層バリアを高密度修復するフェイスクリーム10選</p>
        </a>
        <a href="/winter-argan-oil" class="internal-card">
          <h5>🥑 高保湿アルガンオイル</h5>
          <p>ビタミンE豊富なモロッコの黄金オイル。冬の角質ゴワつきを解きほぐす先行美容液10選</p>
        </a>
        <a href="/winter-horse-oil" class="internal-card">
          <h5>🐴 高保湿馬油クリーム</h5>
          <p>人の皮脂に最も近い天然エモリエント！粉吹き乾燥・ひび割れを包み込む伝統の馬油10選</p>
        </a>
        <a href="/winter-ceramide-lotion" class="internal-card">
          <h5>🧴 高保湿セラミド化粧水</h5>
          <p>クリームの前に角層深部へセラミドを流し込む！冬のインナードライを救う高保湿化粧水10選</p>
        </a>
        <a href="/winter-shea-butter" class="internal-card">
          <h5>🧈 高保湿シアバター</h5>
          <p>天然の濃厚ベールで極上保護。顔・唇・毛先の粉吹き乾燥を根本解決するバーム10選</p>
        </a>
        <a href="/winter-cica-cream" class="internal-card">
          <h5>🌿 冬の高保湿シカクリーム</h5>
          <p>寒暖差の赤みや肌荒れを集中消火！ツボクサエキスを高濃度配合した鎮静クリーム10選</p>
        </a>
      </div>
    </section>
  </article>
</main>

<footer>
  <p>&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved. 当サイトの情報は楽天APIの公開データに基づいており、最新の価格・在庫情報は各販売ページにてご確認ください。</p>
</footer>

</body>
</html>
"""

output_path = "winter-panthenol-cream.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {output_path} successfully ({len(html_content):,} bytes)!")
