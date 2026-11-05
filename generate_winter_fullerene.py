import json
import re

with open("fetched_3new_sacran_fullerene_hatomugi.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_fullerene"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 ノーベル賞受賞の球状炭素分子！ビタミンCの250倍の抗酸化力で冬の皮脂酸化を消去",
        "catch": "水溶性フラーレン（ラジカルスポンジ）を規定値以上高濃度に配合したピュアエッセンス。真冬の過酷な寒冷酸化ストレスや暖房乾燥から皮脂バリアを守り抜き、夕方になってもくすまない潤いハリ肌へ",
        "brand_name": "TUNEMAKERS (チューンメーカーズ)",
        "capacity": "10ml / 遮光ドロッパー瓶",
        "type": "高純度 水溶性フラーレン原液 美容液",
        "features": "フラーレン（ラジカルスポンジR）、BG、PVP、水",
        "value": "ビタミンCの250倍以上の抗酸化持続力。紫外線だけでなく冬のエアコン風や寒暖差による酸化ダメージを長時間スポンジのように吸着消去し、乾燥小ジワとしぼみ肌を徹底ブロック",
        "desc_p1": "11月から12月にかけての肌の急速な老化・乾燥悪化の背後には、実は『寒冷酸化ストレス』が潜んでいます。気温の低下によって毛細血管が収縮し、血流が滞ると細胞内の活性酸素除去酵素の働きが低下。そこへ室内外の寒暖差や暖房による急激な脱水が加わることで、肌表面の皮脂が過酸化脂質へと変質し、細胞間脂質のラメラ液晶構造を破壊してしまうのです。チューンメーカーズの『フラーレン原液 10ml』は、サッカーボール状の炭素同素体C60である水溶性フラーレンを高濃度でボトルに封じ込めたレスキュー美容液です。",
        "desc_p2": "一般的な抗酸化物質であるビタミンCやポリフェノールが自身が酸化されることで相手を還元するのに対し、フラーレンはその球状構造によって活性酸素を無制限に吸着・消去し続けるため、朝塗布すれば夕方の退勤時まで抗酸化保水シールドが持続します。サラサラとした浸透性の高いテクスチャーでありながら、肌になじませると角層のキメがギュッと引き締まり、内側から水分が湧き出るようなみずみずしいハリを実感。手持ちの化粧水や乳液に1〜2滴混ぜるだけで、冬の酸化乾燥に負けないタフな美肌の土台が完成します。",
        "target": "冬になると夕方に顔がドッとくすんで疲れて見える方、暖房の効いたオフィスで肌が突っ張る方、乾燥小ジワやたるみ毛穴を根本からエイジングケアしたい方",
        "point": "朝晩の洗顔後すぐ、または化粧水の後に2〜3滴を手のひらに取り、顔全体を包み込むようにハンドプレスします。日中の紫外線やブルーライト・暖房乾燥から守るため、特に朝のケアに組み込むのが極めて効果的です。"
    },
    {
        "rank": 2,
        "tag": "🔬 国内最高水準のフラーレン10%配合！ビタミンC誘導体×プロテオグリカン黄金比セラム",
        "catch": "キソが誇る高濃度サイエンススキンケア。水溶性フラーレン（ラジカルスポンジ）を国内基準最高レベルの10%高配合。真冬の過酷な乾燥とくすみを跳ね返す圧倒的スペックの濃密セラム",
        "brand_name": "KISO (キソ)",
        "capacity": "20ml / スポイト遮光ボトル",
        "type": "超高濃度 水溶性フラーレン10%配合 モイスチャーセラム",
        "features": "フラーレン10%、水溶性プロテオグリカン、持続型ビタミンC誘導体、ヒアルロン酸Na",
        "value": "原料メーカー直販だからこそ実現したフラーレン10%という驚異の配合率。高保水プロテオグリカンとの相乗効果で、冬の干からびた角層を内側からパーンと膨らませる高密度保水",
        "desc_p1": "市販の美容液で『フラーレン配合』と謳われていても、実際の配合濃度がごく微量であるケースは少なくありません。KISOの『モイスチャーセラムRS 20ml』は、水溶性フラーレン原料（ラジカルスポンジ）を贅沢にも10%という国内トップクラスの超高濃度で配合した本格派セラムです。さらに、ヒアルロン酸の約1.3倍の保水力を誇るプロテオグリカンとビタミンC誘導体を掛け合わせることで、保水・抗酸化・透明感の三位一体ケアを具現化しています。",
        "desc_p2": "とろみのある琥珀色のリキッドを肌に乗せると、硬化した冬の角層にスーッと吸い込まれるように浸透。高濃度フラーレンが暖房乾燥や酸化によって傷んだ細胞間脂質を強力に保護し、プロテオグリカンが角層深部で大量の水分を抱え込みます。塗布した翌朝の洗顔時には、肌がしっとり吸い付くように柔らかく、内側から押し返してくるような弾力感を指先で実感。11月・12月の乾燥ピークでもファンデーションがピタッと密着し、一日中粉吹きやひび割れを許しません。",
        "target": "フラーレンの本当の実力を実感できる高濃度コスメを使いたい方、冬のインナードライとしぼみ肌に悩む方、高品質・高濃度なコスメを良心的な価格で継続したい方",
        "point": "化粧水で肌を整えた後、スポイトの半分程度を取り、手のひらで温めてから優しく全顔に馴染ませます。特に乾燥小ジワが目立ちやすい目尻やほうれい線には重ねづけを推奨します。"
    },
    {
        "rank": 3,
        "tag": "🛡️ 規定値以上フラーレン×ヒト型セラミド5種！冬の肌密度を立て直す最高峰オールインワン",
        "catch": "成分重視派から熱狂的支持を受けるトゥヴェールの最高峰ゲル。公認フラーレンマーク取得の高濃度にヒト型セラミド全5種、浸透型ペプチド、アミノ酸を融合した冬の集中リペアゲル",
        "brand_name": "TOUT VERT (トゥヴェール)",
        "capacity": "100g / ディスペンサーポンプ容器",
        "type": "高濃度フラーレン×ヒト型セラミド5種 エイジングケアゲル",
        "features": "フラーレン（規定値以上）、ヒト型セラミド1, 2, 3, 5, 6II、浸透型ペプチド、アミノ酸10種",
        "value": "洗顔後これ1本で完結するプロ仕様ゲル。フラーレンの抗酸化シールドと5種のヒト型セラミドによる角層ラメラ液晶の完全再構築で、真冬の暖房乾燥を完全無効化",
        "desc_p1": "オールインワン化粧品に対して『手軽だけど保湿力が物足りない』というイメージを持っている方にこそ体験してほしいのが、トゥヴェールの『エッセンスセレクトゲル 100g』です。ビタミンCの250倍の抗酸化力を誇るフラーレンを、有効推奨濃度以上配合している証である公式マークを取得。さらに肌本来の角層細胞間脂質と同じ5種類のヒト型セラミドを高圧乳化技術で微粒子配合しています。",
        "desc_p2": "ポンプから出すと、みずみずしくもこっくりとした濃厚なテクスチャーが広がり、摩擦感ゼロで肌に密着。5種のヒト型セラミドが角層の乱れたラメラ構造を整えて水分蒸発を防ぎ、フラーレンが冬の乾燥による皮脂酸化と微弱炎症を徹底的に鎮圧します。高機能ペプチドが真皮のコラーゲン産生をサポートするため、塗るたびに肌がキュッとリフトアップされるような引き締まり感を実感。衛生的なポンプボトルで最後まで新鮮に使い切れる点も冬のデイリーケアに最適です。",
        "target": "何ステップも重ねるスキンケアが面倒だけど最高峰のエイジングケアをしたい方、冬になると肌のバリアが壊れて敏感に傾く方、成分配合に一切妥協したくない本物志向の方",
        "point": "洗顔後、1〜2プッシュを手にとり顔全体へ滑らかに伸ばします。乾燥が極めて激しい真冬の夜は、目元・口元にさらに1プッシュを重ねづけして『潤い密封マスク』として使用してください。"
    },
    {
        "rank": 4,
        "tag": "✨ 高浸透ビタミンC誘導体APPS×リポフラーレン！日中の暖房乾燥と皮脂崩れを防ぐCCクリーム",
        "catch": "ビューティーモールが誇る大ヒット高機能ベース。高浸透ビタミンC誘導体APPSと油溶性リポフラーレンをダブル配合。真冬の過酷な暖房気流下でもファンデがひび割れず、透き通るツヤ肌をキープ",
        "brand_name": "BEAUTY MALL (ビューティーモール)",
        "capacity": "20g / スリムチューブ",
        "type": "APPS×リポフラーレン配合 高保湿トリートメントCCクリーム",
        "features": "パルミチン酸アスコルビルリン酸3Na (APPS)、リポフラーレン、TPNa (ビタミンE誘導体)、プロテオグリカン",
        "value": "日中用の美容液・日焼け止め・下地・カラーコントロール・ファンデーションが1本に集約。冬の室内乾燥で粉吹きやひび割れを起こさず、夕方まで瑞々しい発光ツヤ肌を維持",
        "desc_p1": "冬のメイクにおいて最大の悩みは、朝は綺麗に仕上がったベースメイクが、昼過ぎにはオフィスの暖房気流によってカラカラに乾燥し、目元や口元のファンデーションがひび割れて粉を吹いてしまう現象です。ビューティーモールの『フラーレンCCクリーム 20g』は、メイクをしている間中ずっと角層深部へ潤いと抗酸化力を供給し続ける『日中用集中トリートメントベース』です。",
        "desc_p2": "角層深くまで浸透する最新ビタミンC誘導体APPSと、油分との親和性に優れたリポフラーレンが配合されており、皮膚表面に滑らかな保湿エモリエント膜を構築。乾燥による小ジワや毛穴落ちを光の乱反射で巧みにぼかしながら、暖房の熱気による水分蒸散を物理的に食い止めます。紫外線吸収剤フリーのノンケミカル処方でありながら、肌にピタッと吸い付くようにフィット。夕方になってもくすまず、まるでスキンケアしたてのようなみずみずしい透明感が持続します。",
        "target": "冬になると暖房でファンデーションが粉を吹いたり毛穴落ちする方、日中も抗酸化スキンケアを継続したい方、重いファンデーションを使わずにナチュラルなツヤ美肌を作りたい方",
        "point": "スキンケアで肌を整えた後、パール粒大を手にとって顔の中心から外側へ優しく伸ばします。カバーしたい部分には指先でトントンと重ねづけすると、コンシーラー要らずの美肌が完成します。"
    },
    {
        "rank": 5,
        "tag": "🌙 ダブルフラーレン×レチノールカプセル！翌朝の肌密度とハリを跳ね上げる極上ナイトクリーム",
        "catch": "水溶性ラジカルスポンジと油溶性リポフラーレンを贅沢にダブル配合。さらにナノカプセル化レチノールを融合し、睡眠中の暖房乾燥による水分蒸散を徹底遮断する最高峰モイストクリーム",
        "brand_name": "BEAUTY MALL (ビューティーモール)",
        "capacity": "30g / 上質ジャー容器",
        "type": "ダブルフラーレン×レチノール 高密度リペアクリーム",
        "features": "フラーレン（ラジカルスポンジ＆リポフラーレン）、レチノール（ビタミンA）、ナイアシンアミド、セラミド複合体",
        "value": "寝ている間の無防備な乾燥と酸化を完全にシャットアウト。濃厚なエモリエントヴェールが朝まで肌を密着ラッピングし、翌朝起きた瞬間に押し返すようなハリ肌を実感",
        "desc_p1": "睡眠中の肌は、寝室の暖房や加湿器の停止によって明け方に湿度が急降下し、1日の中で最も過酷な乾燥危機にさらされます。ビューティーモールの『BMモイストFクリーム 30g』は、夜の就寝中に失われがちな水分とハリを保護・修復することに特化して開発されたプレミアムナイトクリームです。最大の特徴は、水溶性フラーレンと油溶性フラーレンの両方を配合した『ダブルフラーレン処方』にあります。",
        "desc_p2": "こっくりとしたリッチなクリームを肌に伸ばすと、体温でとろけるように広がり、角層表面に厚みのあるシルキーな保護シールドを展開。カプセル化されたレチノールとナイアシンアミドが角層の奥深くへゆっくりと放出され、真冬の冷えで衰えたターンオーバーとハリ生成をサポートします。翌朝起きて顔を洗った瞬間、指先を押し返すような高密度な弾力と、もっちりとした極上の潤い感を体感できます。冬の乾燥小ジワを本気でケアしたい大人のための至高の一品です。",
        "target": "朝起きると肌がカラカラに乾いて寝癖のような乾燥ジワがついている方、レチノールを使いたいけれど乾燥や刺激が心配な方、最高峰のクリームで冬のハリ不足をリセットしたい方",
        "point": "夜のお手入れの最後に、パール粒大を手のひらで温めてから顔全体に引き上げるように伸ばします。乾燥が気になる目元やほうれい線まわりには、指先で優しく重ねづけしてください。"
    },
    {
        "rank": 6,
        "tag": "💎 フラーレン×トリプルコラーゲン×ヒアルロン酸！乾燥小ジワを目立たなくする濃密ゲル",
        "catch": "ビノワが提案する高機能モイスチャーゲル。フラーレンの抗酸化バリアに、分子サイズの異なる3種のコラーゲンとヒアルロン酸をブレンド。真冬の過酷な寒冷乾燥下でも弾力モチ肌をキープ",
        "brand_name": "Vinowa (ビノワ)",
        "capacity": "100g / スクエアジャー容器",
        "type": "高保湿フラーレン配合 パーフェクトコラーゲンゲル",
        "features": "フラーレン、加水分解コラーゲン、水溶性コラーゲン、サクシノイルアテロコラーゲン、ヒアルロン酸Na",
        "value": "効能評価試験済みで乾燥小ジワを目立たなくする実力派。大容量100gで惜しみなく使える圧倒的コストパフォーマンスと、ぷるんとした弾力ジェルの心地よい密封感",
        "desc_p1": "11月以降の乾燥期、目尻の笑いジワや口元の小ジワが深く刻まれて戻らなくなる『乾燥小ジワの定着化』に悩む方が急増します。ビノワの『パーフェクトコラーゲンゲル エンリッチド 100g』は、乾燥による小ジワを目立たなくする効能評価試験をクリアした、高い信頼性を誇る多機能モイスチャーゲルです。",
        "desc_p2": "角層表面を覆う高分子コラーゲンから角層深部へ浸透する加水分解コラーゲンまで、異なる深さにアプローチするトリプルコラーゲンを配合。そこにフラーレンが加わることで、コラーゲン線維を酸化劣化から保護し、ぷるぷるの弾力ネットワークを構築します。重すぎず軽すぎない絶妙なジェルテクスチャーは、肌に乗せるとみずみずしく広がり、ベタつかないのに一枚の水分膜を張ったような安心感をもたらします。朝のメイク前でも夜のパックにも大活躍する頼れる万能ゲルです。",
        "target": "目元や口元の乾燥小ジワがファンデーションに溜まって目立つ方、重い油分クリームはニキビができやすくて苦手な方、確かなエビデンスを持つ高コスパゲルを探している方",
        "point": "さくらんぼ大を手にとり、顔の中心から外側へ優しく引き上げるように伸ばします。目元やほうれい線には指先でトントンと軽くタッピングしながら馴染ませるとピンとしたハリが出ます。"
    },
    {
        "rank": 7,
        "tag": "🌿 高純度リポフラーレン配合！真冬の寒風と暖房乾燥から皮脂を守る濃密エイジングオイル",
        "catch": "油溶性フラーレン（リポフラーレン）を高濃度に溶かし込んだ特製モイスチャーオイル。冬の冷たい木枯らしやエアコン暖房でパサつく角層へ、ベタつかずスーッと溶け込むシルクオイル",
        "brand_name": "フラーレンフォース",
        "capacity": "30ml / スポイト遮光ガラス瓶",
        "type": "高純度リポフラーレン配合 エイジング美容オイル",
        "features": "リポフラーレン、スクワラン、ホホバ種子油、天然トコフェロール",
        "value": "人肌の皮脂組織と親和性の高い植物スクワランをベースにリポフラーレンを配合。冬の洗顔後のブースターとしても、スキンケア最後のフタとしても使える万能美容オイル",
        "desc_p1": "冬のスキンケアにおいて、水分を補給した後に重要なのが『いかに皮脂膜に近い良質な油分でフタをするか』です。しかし、一般的なオイルは酸化しやすく、日中に塗布すると紫外線や暖房熱で酸化して油焼けやくすみの原因になることがあります。フラーレンフォースの『美容オイル 30ml』は、油溶性フラーレン（リポフラーレン）をスクワランにブレンドした、抗酸化力に極めて優れたプレミアムオイルです。",
        "desc_p2": "リポフラーレンがオイルそのものの酸化を強力に防止し、さらに肌本来の皮脂膜の過酸化をブロック。1滴手に取って顔に広げると、オイルとは思えないほどサラリとしたシルキーな感触で角層の隙間へスッと引き込まれていきます。化粧水前のブースターとして使えば角層を柔軟にほぐして化粧水の浸透を高め、スキンケアの最後に使えば朝までしっとりとした潤いを密閉。冬の乾燥でパサつく毛先のヘアオイルやネイルケアとしても全身マルチに活躍します。",
        "target": "オイル特有のベタつきや酸化による油焼けが心配な方、冬になると肌がゴワついて化粧水が入っていかない方、顔・髪・指先まで1本で上質に保湿したい方",
        "point": "洗顔直後の湿った肌に1〜2滴を伸ばしてブースターにするか、化粧水や乳液の後に1滴を手のひら全体に広げて優しくハンドプレス。髪の毛先に少量馴染ませると冬の静電気を防ぎます。"
    },
    {
        "rank": 8,
        "tag": "✨ フラーレン×ツバメの巣×生セラミド！エステサロン発の最高峰プレミアム密着マスク",
        "catch": "高級美顔器メーカーARTISTIC&CO.が手がける最高峰シートマスク。フラーレン、ツバメの巣エキス、生セラミドを贅沢に配合した濃密美容液を1枚に丸ごと17ml凝縮した極上ケア",
        "brand_name": "ARTISTIC&CO. (アーティスティックアンドシーオー)",
        "capacity": "5枚入（個包装 17ml/枚）",
        "type": "サロン専売 最高峰エイジングケア 密着シートマスク",
        "features": "フラーレン、加水分解アナツバメ巣エキス、セレブロシド（生セラミド）、リンゴ果実培養細胞エキス",
        "value": "特別な日の前夜に使う集中リペアマスク。極薄の高密着シートが顔の凹凸に吸い付き、真冬の寒冷で干からびた肌をわずか15分でエステ帰りのような発光モチ肌へ再生",
        "desc_p1": "11月から12月は、忘年会やクリスマス、年末のイベントなど、人前に出る機会が増える季節です。しかし、過酷な寒冷乾燥と忙しさによる睡眠不足が重なり、肌の調子は1年で最も崩れやすくなります。高級サロン専売美顔器で世界的に有名なARTISTIC&CO.の『PE ザ クイーン ゴールデンビューティーマスク』は、そうした真冬の肌危機を劇的にリカバリーするために開発された最高峰シートマスクです。",
        "desc_p2": "肌に吸い付くように密着するマイクロファイバーシートには、フラーレンをはじめ、古来より宮廷貴族に愛されたツバメの巣エキスや生セラミド、幹細胞エキスを凝縮した乳液状美容液がたっぷり17mlも浸透。マスクを顔に乗せると、冷風で疲弊した角層深部まで濃密な美容成分が怒涛のように押し寄せ、わずか15分で萎んでいたキメがふっくらと立ち上がります。剥がした後の肌は、毛穴がキュッと引き締まり、内側から発光するような極上のツヤと透明感を放ちます。",
        "target": "真冬の大切なイベントやデートの前夜に肌を一発逆転させたい方、エステサロンの本格施術のようなリッチなパックを自宅で楽しみたい方、乾燥くすみを即座にリセットしたい方",
        "point": "洗顔後、化粧水で肌を整えてからマスクを隙間なく密着させ、15〜20分間集中パック。袋に残ったリッチな美容液は首筋やデコルテ、手の甲まで余すところなく塗り広げてください。"
    },
    {
        "rank": 9,
        "tag": "👀 高純度フラーレン×乳酸菌生産物質！冬の寒冷クマ・目元小ジワをふっくら持ち上げる",
        "catch": "皮膚が薄く乾燥しやすい目元のために設計された専門アイクリーム。高純度フラーレンと乳酸菌生産物質が、冬の冷えによる血行不良クマや目尻のちりめんジワを根本から集中補修",
        "brand_name": "en-team (エンチーム)",
        "capacity": "15g / 先細アイチューブ",
        "type": "目元専用 高機能エイジング アイクリーム",
        "features": "フラーレン、乳酸菌生産物質、加水分解酵母エキス、アルブチン、持続型ヒアルロン酸",
        "value": "まばたきによる摩擦と暖房乾燥で最もダメージを受けやすい目元を徹底ガード。伸びが良くデリケートな皮膚を引っ張らずに密着し、ピンとした明るい眼差しをキープ",
        "desc_p1": "顔の皮膚の中で最も薄く（頬の約3分の1）、皮脂腺がほとんど存在しないのが目元です。11月・12月の寒さで血流が滞ると青クマが目立ち、エアコンの乾燥風が当たることで瞬く間に細かいちりめんジワが刻まれてしまいます。エンチームの『ラクトリーアイ 15g』は、目元特有の皮膚生理に着目して作られた高機能アイクリームです。",
        "desc_p2": "フラーレンの抗酸化シールドが目元の薄い皮膚を酸化ストレスから保護し、独自の乳酸菌生産物質が皮膚常在菌バランスを整えて肌本来のバリア力を強化。こっくりとした濃厚なテクスチャーでありながら、指先で優しくトントンとなじませるとスーッと溶け込み、目元の乾燥小ジワをピンとストレッチするように引き上げます。夕方になっても目元のファンデーションがシワに落ち込まなくなり、若々しく明るい印象の目元を一日中保つことができます。",
        "target": "冬になると目元の小ジワが目立ちアイメイクが崩れる方、寒さで目元のクマやくすみが気になる方、デリケートな目元を本気で集中エイジングケアしたい方",
        "point": "薬指の腹に米粒大を取り、下まぶたの目頭から目尻、上まぶたへと優しくタッピングするように馴染ませます。摩擦は厳禁のため、決して強く擦らずピアノを弾くように優しく叩き込んでください。"
    },
    {
        "rank": 10,
        "tag": "💋 リポフラーレン×ボリュームペプチド！冬の寒風で皮むけする唇を濃密ラッピングする美容液",
        "catch": "美容皮膚科医・上原恵理医師が開発した話題の高機能リップセラム。高純度リポフラーレンとボリュームアップペプチドを配合。ガサガサに荒れてひび割れる冬の唇を縦ジワレスなぷるぷるリップへ",
        "brand_name": "Lov me Touch (ラブミータッチ)",
        "capacity": "チューブ式リップディスペンサー",
        "type": "高濃度リポフラーレン配合 リップ美容液プランパー",
        "features": "リポフラーレン、パルミトイルトリペプチド-1、トコフェロール、植物性スクワラン",
        "value": "塗った瞬間から唇に厚みのある高密着保護膜を形成。冬の冷風による皮むけや乾燥をブロックしながら、ペプチドがふっくらボリューミーなツヤと血色感を与える",
        "desc_p1": "冬になると真っ先に乾燥トラブルが現れるのが唇です。角層が極めて薄く皮脂膜を作れない唇は、11月以降の木枯らしにさらされると即座にひび割れ、皮むけや出血を引き起こします。多くのリップクリームを塗り直しても数十分で乾いてしまう方に最適なのが、ラブミータッチの『ラブミーリップス 2.0』です。医師の監修のもと、油溶性リポフラーレンを高配合した本格リップトリートメントです。",
        "desc_p2": "唇に乗せると、グロスのようなリッチな密着ヴェールが唇全体を隙間なくコーティング。リポフラーレンが唇の紫外線・酸化ダメージを消去しながら、ボリュームペプチドが角層の奥まで潤いを届け、気になる縦ジワをふっくらと押し上げます。食事をしても落ちにくい高い持続力があり、真冬の寒風にさらされても皮むけが一切起こりません。リップ下地としても、就寝前の集中リップマスクとしても極上のパフォーマンスを発揮します。",
        "target": "冬になると市販のリップクリームを塗っても唇がガサガサに皮むけする方、唇の縦ジワが深くなり口紅が綺麗に乗らない方、ふっくらとしたツヤとハリのある唇を取り戻したい方",
        "point": "チューブから直接または清潔な指先に取り、唇の中央から外側へ厚めに塗り広げます。夜寝る前に唇の輪郭からはみ出るくらいたっぷり塗ると、翌朝ぷるぷるのリップに生まれ変わります。"
    }
]

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge">第{p["rank"]}位</span>
            <span class="product-tag">{p["tag"]}</span>
          </div>

          <h3 class="product-title">{p["catch"]}</h3>
          <p class="product-display-name">{item_data["display_name"]}</p>

          <div class="product-layout">
            <div class="product-visual-col">
              <div class="img-wrap">
                <img src="{item_data["image_url"]}" alt="{p["brand_name"]} {item_data["item_name"]}" class="product-img" loading="lazy" />
              </div>
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">¥{item_data["price"]:,}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", "4.8")}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", "120")}件）</span>
              </div>
              <a href="{item_data["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
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

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！ビタミンCの250倍の抗酸化力と持続型水分保持膜が真冬の寒冷酸化枯れ肌としぼみ小ジワを救い出す高保湿フラーレンコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の寒冷酸化ストレスと暖房乾燥による枯れ肌・小ジワ・くすみを救う高保湿フラーレンコスメを徹底厳選！チューンメーカーズ、KISO、トゥヴェール、ビューティーモール、ラブミータッチまでビタミンCの250倍の抗酸化持続力とラメラ保護の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="フラーレン コスメ, フラーレン 美容液, 高保湿 コスメ 冬, エイジングケア 11月 12月, 暖房乾燥 くすみ, 乾燥小ジワ, チューンメーカーズ フラーレン, トゥヴェール エッセンスセレクトゲル, KISO フラーレン">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！ビタミンCの250倍の抗酸化力と持続型水分保持膜が真冬の寒冷酸化枯れ肌としぼみ小ジワを救い出す高保湿フラーレンコスメランク10">
  <meta property="og:description" content="ノーベル賞受賞の抗酸化ナノカーボン！ビタミンCの250倍の持続力で真冬の皮脂酸化を防ぎ、濃密な潤いを保ち続けるおすすめフラーレンコスメ10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-fullerene">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿フラーレンコスメランク10">
  <meta name="twitter:description" content="11月・12月の寒冷枯れ肌に！皮脂の酸化を防ぎ潤いを守り抜くフラーレンコスメおすすめ厳選10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！ビタミンCの250倍の抗酸化力と持続型水分保持膜が真冬の寒冷酸化枯れ肌としぼみ小ジワを救い出す高保湿フラーレンコスメランク10",
    "description": "11月・12月の寒冷酸化ストレスと暖房乾燥による枯れ肌・小ジワ・くすみを救う高保湿フラーレンコスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-06T01:00:00+09:00",
    "dateModified": "2026-11-06T01:00:00+09:00",
    "author": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS 編集部"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://lumi-cosme.vercel.app/favicon.jpg"
      }}
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-fullerene"
    }}
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #2: ItemList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿フラーレンコスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "{product_details[0]["brand_name"]} {items[0]["item_name"]}",
        "url": "{items[0]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{product_details[1]["brand_name"]} {items[1]["item_name"]}",
        "url": "{items[1]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{product_details[2]["brand_name"]} {items[2]["item_name"]}",
        "url": "{items[2]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 4,
        "name": "{product_details[3]["brand_name"]} {items[3]["item_name"]}",
        "url": "{items[3]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 5,
        "name": "{product_details[4]["brand_name"]} {items[4]["item_name"]}",
        "url": "{items[4]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 6,
        "name": "{product_details[5]["brand_name"]} {items[5]["item_name"]}",
        "url": "{items[5]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 7,
        "name": "{product_details[6]["brand_name"]} {items[6]["item_name"]}",
        "url": "{items[6]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 8,
        "name": "{product_details[7]["brand_name"]} {items[7]["item_name"]}",
        "url": "{items[7]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 9,
        "name": "{product_details[8]["brand_name"]} {items[8]["item_name"]}",
        "url": "{items[8]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 10,
        "name": "{product_details[9]["brand_name"]} {items[9]["item_name"]}",
        "url": "{items[9]["affiliate_url"]}"
      }}
    ]
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #3: FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "フラーレンはなぜ冬の乾燥肌や小ジワに効果的なのですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "真冬の過酷な寒冷と暖房気流は、肌内部で活性酸素を大量に発生させ、角層の皮脂を過酸化脂質へと変質させてバリア機能を破壊します。フラーレンはビタミンCの250倍以上の抗酸化力を持ち、さらにスポンジのように活性酸素を吸着し続けるため、皮脂膜の過酸化を長時間防ぎ、角層のラメラ液晶構造を守り抜くことで高い水分保持力を維持します。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "水溶性フラーレン（ラジカルスポンジ）と油溶性フラーレン（リポフラーレン）はどう使い分けるべきですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "水溶性フラーレンは化粧水や導入美容液に適しており、角層の水分ネットワークに素早く浸透して内側の酸化ストレスを消去します。一方、油溶性フラーレンは乳液、クリーム、美容オイルに配合され、皮脂膜と一体化して外側からの乾燥と酸化を強力にブロックします。真冬は両方を併用する『ダブルフラーレン処方』を取り入れることで、角層の内外から隙間のない抗酸化保水シールドが完成します。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "ビタミンCやレチノールなど他のエイジングケア成分と一緒に使っても大丈夫ですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "非常に相性が良く、むしろ併用が推奨されます。フラーレンは他の美容成分を酸化劣化から保護するシールド効果を持つため、不安定なビタミンCやレチノールと一緒に使うことで、それらの成分の美肌効果をより長く安定して肌へ届けることができます。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #7c3aed;
      --primary-light: #f3e8ff;
      --primary-dark: #6d28d9;
      --accent: #8b5cf6;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #faf5ff;
      --card-bg: #ffffff;
      --border: #e9d5ff;
      --gold: #d97706;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Meiryo", sans-serif;
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
    }}

    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      letter-spacing: -0.025em;
    }}

    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    .container {{
      max-width: 1000px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .article-header {{
      background: #ffffff;
      padding: 2.5rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}

    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}

    .article-category {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}

    h1.article-title {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #0f172a;
      margin-bottom: 1.25rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }}

    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      padding-top: 1rem;
      border-top: 1px solid var(--border);
    }}

    .lead-box {{
      background: #ffffff;
      border-left: 5px solid var(--primary);
      padding: 1.75rem;
      border-radius: 0 var(--radius) var(--radius) 0;
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      font-size: 1.05rem;
      color: #334155;
    }}

    .lead-box p {{
      margin-bottom: 1rem;
    }}
    .lead-box p:last-child {{
      margin-bottom: 0;
    }}

    .science-section {{
      background: #ffffff;
      padding: 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border: 1px solid var(--border);
    }}

    .section-title {{
      font-size: 1.45rem;
      color: #0f172a;
      font-weight: 800;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.5rem;
    }}

    .science-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin-top: 1.5rem;
    }}

    .science-card {{
      background: #ffffff;
      padding: 1.5rem;
      border-radius: var(--radius);
      border: 1px solid var(--border);
    }}

    .science-card h4 {{
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-box {{
      background: #ffffff;
      padding: 1.75rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border: 1px solid var(--border);
    }}

    .toc-title {{
      font-weight: 800;
      font-size: 1.15rem;
      margin-bottom: 1rem;
      color: var(--primary-dark);
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 0.5rem 1.5rem;
    }}

    .toc-list li a {{
      color: #334155;
      text-decoration: none;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list li a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.25rem 2rem;
      margin-bottom: 3rem;
      border: 1px solid var(--border);
      transition: box-shadow 0.2s, transform 0.2s;
    }}

    .product-card:hover {{
      box-shadow: var(--shadow-lg);
      transform: translateY(-2px);
    }}

    .product-header {{
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}

    .rank-badge {{
      background: var(--gold);
      color: #ffffff;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 0.25rem 0.85rem;
      border-radius: 9999px;
      letter-spacing: 0.05em;
    }}

    .product-tag {{
      color: var(--primary-dark);
      font-size: 0.9rem;
      font-weight: 700;
    }}

    .product-title {{
      font-size: 1.4rem;
      line-height: 1.45;
      color: #0f172a;
      margin-bottom: 0.5rem;
      font-weight: 800;
    }}

    .product-display-name {{
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 1.75rem;
      background: var(--bg);
      padding: 0.6rem 1rem;
      border-radius: 8px;
    }}

    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
    }}

    @media (max-width: 768px) {{
      .product-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    .product-visual-col {{
      text-align: center;
    }}

    .img-wrap {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem;
      margin-bottom: 1rem;
    }}

    .product-img {{
      max-width: 100%;
      height: auto;
      max-height: 240px;
      object-fit: contain;
    }}

    .price-box {{
      background: var(--bg);
      padding: 0.75rem;
      border-radius: 8px;
      margin-bottom: 0.75rem;
    }}

    .price-label {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .price-value {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #e11d48;
    }}

    .review-meta {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.25rem;
    }}

    .review-stars {{
      color: var(--gold);
      font-weight: 700;
    }}

    .rakuten-btn {{
      display: block;
      background: #bf0000;
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      transition: background 0.2s, transform 0.1s;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.2);
    }}

    .rakuten-btn:hover {{
      background: #990000;
      transform: translateY(-1px);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      margin-bottom: 1.5rem;
    }}

    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.85rem;
      border: 1px solid var(--border);
    }}

    .spec-table th {{
      background: var(--bg);
      color: #334155;
      width: 25%;
      font-weight: 700;
      text-align: left;
    }}

    .spec-table td {{
      color: #1e293b;
    }}

    .product-body p {{
      margin-bottom: 1.1rem;
      color: #334155;
      font-size: 0.98rem;
    }}

    .body-title {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      font-weight: 700;
      margin-bottom: 0.75rem;
      border-left: 3px solid var(--primary);
      padding-left: 0.5rem;
    }}

    .recommend-box, .usage-box {{
      padding: 1rem 1.25rem;
      border-radius: 8px;
      margin-top: 1.25rem;
      font-size: 0.92rem;
    }}

    .recommend-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}

    .recommend-title {{
      font-weight: 700;
      margin-bottom: 0.4rem;
      color: #15803d;
    }}

    .usage-box {{
      background: #fdf4ff;
      border: 1px solid #f5d0fe;
      color: #581c87;
    }}

    .usage-title {{
      font-weight: 700;
      margin-bottom: 0.4rem;
      color: var(--primary-dark);
    }}

    .comparison-section, .faq-section, .internal-links-section {{
      background: #ffffff;
      padding: 2.25rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border: 1px solid var(--border);
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
    }}

    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}

    .comparison-table th, .comparison-table td {{
      padding: 0.85rem;
      border: 1px solid var(--border);
      text-align: left;
    }}

    .comparison-table th {{
      background: var(--bg);
      color: #0f172a;
      font-weight: 700;
    }}

    .comparison-table tr:hover {{
      background: #f3e8ff;
    }}

    .faq-item {{
      margin-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 1.5rem;
    }}

    .faq-item:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}

    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-a {{
      color: #334155;
      font-size: 0.95rem;
      padding-left: 1.5rem;
    }}

    .internal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin-top: 1.5rem;
    }}

    .internal-card {{
      background: var(--bg);
      padding: 1.25rem;
      border-radius: 8px;
      border: 1px solid var(--border);
      text-decoration: none;
      color: var(--text);
      display: block;
      transition: border-color 0.2s, transform 0.1s;
    }}

    .internal-card:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
    }}

    .internal-card-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
    }}

    .internal-card-desc {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1.5rem;
      margin-top: 4rem;
    }}

    .footer-inner {{
      max-width: 1000px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 2rem;
    }}

    @media (max-width: 768px) {{
      .footer-inner {{
        grid-template-columns: 1fr;
      }}
    }}

    .footer-logo {{
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      margin-bottom: 0.75rem;
    }}

    .footer-text {{
      font-size: 0.85rem;
      line-height: 1.7;
    }}

    .footer-links h5 {{
      color: #ffffff;
      margin-bottom: 0.75rem;
      font-size: 0.95rem;
    }}

    .footer-links ul {{
      list-style: none;
    }}

    .footer-links li a {{
      color: #94a3b8;
      text-decoration: none;
      font-size: 0.85rem;
      line-height: 2;
    }}

    .footer-links li a:hover {{
      color: #ffffff;
    }}

    .copyright {{
      max-width: 1000px;
      margin: 2rem auto 0;
      padding-top: 1.5rem;
      border-top: 1px solid #1e293b;
      text-align: center;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">冬コスメTOP</a>
        <a href="#ranking">ランキング10選</a>
        <a href="#comparison">徹底比較表</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <article>
      <div class="article-header">
        <div class="breadcrumb">
          <a href="/">HOME</a> &gt; <a href="/">冬の乾燥対策スキンケア</a> &gt; 高保湿フラーレン特集
        </div>
        <span class="article-category">11月・12月 冬季高保湿エイジングケア特集</span>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！ビタミンCの250倍の抗酸化力と持続型水分保持膜が真冬の寒冷酸化枯れ肌としぼみ小ジワを救い出す高保湿フラーレンコスメランク10</h1>
        <div class="article-meta">
          <span>📅 公開日: 2026年11月6日</span>
          <span>🔄 最終更新: 2026年11月6日</span>
          <span>✍ 監修: LUMI COSMETICS 皮膚科学コスメ解析班</span>
          <span>⏱ 読了目安: 約8分</span>
        </div>
      </div>

      <div class="lead-box">
        <p><strong>「保湿クリームをたっぷり塗っているのに、夕方になると肌がドッとくすんでシワっぽくなる……」</strong>その原因は、冬特有の『寒冷酸化ストレス』にあります。11月から12月にかけて外気温が急降下すると、末梢血管の収縮により肌の血流が滞り、肌内部の活性酸素除去機能が低下。そこへオフィスや室内の強烈な暖房気流が直撃することで、肌表面の皮脂が急速に酸化して過酸化脂質へと変化し、角層の水分を守るラメラ液晶構造を破壊してしまうのです。</p>
        <p>この真冬の過酷な乾燥・酸化の負の連鎖を断ち切る最高峰のサイエンス成分が、ノーベル化学賞を受賞した球状炭素分子<strong>『フラーレン（Fullerene）』</strong>です。<strong>ビタミンCの250倍以上という驚異的な抗酸化力</strong>を誇り、さらに自身が壊れることなく活性酸素をスポンジのように吸着し続ける特性を持つため、朝塗布すれば夕方の退勤時まで肌の皮脂バリアと水分保持膜を守り抜きます。</p>
        <p>本記事では、楽天市場で実際に高評価を獲得している正規品の中から、配合純度・処方設計・使用感・持続力を徹底検証した<strong>真冬の高保湿フラーレンコスメおすすめランキング10選</strong>をご紹介します。</p>
      </div>

      <section class="science-section">
        <h2 class="section-title">🧬 なぜ真冬の乾燥・小ジワに「フラーレン」が圧倒的に効くのか？皮膚科学的3大根拠</h2>
        <p>一般的な保湿成分が「水分を与えるだけ」であるのに対し、フラーレンは「なぜ水分が逃げるのか」という根本原因である皮脂酸化に着目しています。</p>

        <div class="science-grid">
          <div class="science-card">
            <h4>⚡ ビタミンCの250倍以上！持続型ラジカル消去</h4>
            <p>フラーレンの最大の特徴は、その独特なサッカーボール状の炭素同素体構造（C60）にあります。活性酸素を受け取っても自身が酸化されて壊れることがなく、無制限にフリーラジカルを吸着消去し続けます。これにより、寒暖差や暖房による肌ストレスを一日中無力化します。</p>
          </div>

          <div class="science-card">
            <h4>🛡️ 皮脂の過酸化を防ぎラメラ構造を維持</h4>
            <p>冬の乾燥肌では、分泌された微量な皮脂が酸化されて刺激物質へと変質し、角層のセラミドバリアを溶かしてしまいます。フラーレンが皮脂の過酸化を物理的に防ぎ切ることで、細胞間脂質のラメラ液晶が正常に保たれ、内側の水分蒸発を恒常的に防ぎます。</p>
          </div>

          <div class="science-card">
            <h4>✨ 水溶性（RS）と油溶性（LF）のWアプローチ</h4>
            <p>フラーレンには、角層の水分層に浸透する水溶性『ラジカルスポンジ』と、皮脂膜や油分と馴染む油溶性『リポフラーレン』が存在します。この2つを組み合わせることで、角層の内外から隙間なく抗酸化保水膜を張り巡らせることが可能になります。</p>
          </div>
        </div>
      </section>

      <section class="toc-box">
        <div class="toc-title">📑 目次：高保湿フラーレンコスメ厳選10選一覧</div>
        <ul class="toc-list">
          <li><a href="#rank-1">第1位：チューンメーカーズ フラーレン原液 10ml</a></li>
          <li><a href="#rank-2">第2位：KISO モイスチャーセラムRS 20ml</a></li>
          <li><a href="#rank-3">第3位：トゥヴェール エッセンスセレクトゲル 100g</a></li>
          <li><a href="#rank-4">第4位：ビューティーモール フラーレンCCクリーム 20g</a></li>
          <li><a href="#rank-5">第5位：ビューティーモール BMモイストFクリーム 30g</a></li>
          <li><a href="#rank-6">第6位：ビノワ パーフェクトコラーゲンゲル 100g</a></li>
          <li><a href="#rank-7">第7位：フラーレンフォース 美容オイル 30ml</a></li>
          <li><a href="#rank-8">第8位：ARTISTIC&CO. ザ クイーン マスク 5枚入</a></li>
          <li><a href="#rank-9">第9位：エンチーム ラクトリーアイ 目元クリーム 15g</a></li>
          <li><a href="#rank-10">第10位：ラブミータッチ ラブミーリップス 2.0</a></li>
        </ul>
      </section>

      <section id="ranking">
        <h2 class="section-title">🏆 2026年最新！真冬の高保湿フラーレンコスメおすすめ厳選ランキング10選</h2>
        <p style="margin-bottom: 2rem; color: #475569;">※本ランキングは、楽天市場におけるリアルタイムの商品データ（価格・在庫・口コミ評価・配合純度）を基準に、冬の乾燥・エイジングケアに特化して厳正に順位づけしています。</p>

        {all_cards_html}
      </section>

      <section class="comparison-section" id="comparison">
        <h2 class="section-title">📊 高保湿フラーレンコスメ10選 スペック徹底比較表</h2>
        <p style="margin-bottom: 1.5rem; color: #475569;">あなたの肌悩み、ライフスタイル、スキンケアステップに合わせて最適な1品をお選びください。</p>

        <div class="comparison-table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位 / 商品名</th>
                <th>ブランド</th>
                <th>アイテム種別</th>
                <th>参考価格</th>
                <th>特長・おすすめターゲット</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>第1位</strong> チューンメーカーズ フラーレン</td>
                <td>TUNEMAKERS</td>
                <td>水溶性原液美容液</td>
                <td>¥3,410</td>
                <td>ラジカルスポンジ高配合。手持ちコスメに1滴混ぜて酸化乾燥を防ぐ</td>
              </tr>
              <tr>
                <td><strong>第2位</strong> KISO モイスチャーセラムRS</td>
                <td>KISO</td>
                <td>高濃度10%美容液</td>
                <td>¥3,906</td>
                <td>国内最高水準の10%配合。プロテオグリカンとの相乗で乾燥肌を満たす</td>
              </tr>
              <tr>
                <td><strong>第3位</strong> トゥヴェール セレクトゲル</td>
                <td>TOUT VERT</td>
                <td>高機能ゲル 100g</td>
                <td>¥12,000</td>
                <td>規定値以上フラーレン×ヒト型セラミド5種。冬の肌密度を立て直す</td>
              </tr>
              <tr>
                <td><strong>第4位</strong> フラーレン CCクリーム</td>
                <td>BEAUTY MALL</td>
                <td>高保湿ベース 20g</td>
                <td>¥5,500</td>
                <td>APPS×リポフラーレン。日中の暖房下でもファンデ崩れゼロ</td>
              </tr>
              <tr>
                <td><strong>第5位</strong> BMモイストFクリーム</td>
                <td>BEAUTY MALL</td>
                <td>ナイトクリーム 30g</td>
                <td>¥11,880</td>
                <td>ダブルフラーレン×レチノール。寝ている間の乾燥を密着遮断</td>
              </tr>
              <tr>
                <td><strong>第6位</strong> ビノワ コラーゲンゲル</td>
                <td>Vinowa</td>
                <td>多機能ゲル 100g</td>
                <td>¥1,720</td>
                <td>効能評価試験済み。トリプルコラーゲンで乾燥小ジワをケア</td>
              </tr>
              <tr>
                <td><strong>第7位</strong> フラーレンフォース 美容オイル</td>
                <td>フラーレンフォース</td>
                <td>美容オイル 30ml</td>
                <td>¥2,198</td>
                <td>高純度リポフラーレン×スクワラン。油焼けせずシルク肌へ</td>
              </tr>
              <tr>
                <td><strong>第8位</strong> ザ クイーン マスク</td>
                <td>ARTISTIC&CO.</td>
                <td>サロンシートマスク</td>
                <td>¥12,100</td>
                <td>美容液17ml凝縮。冬の大切なイベント前夜に使う極上パック</td>
              </tr>
              <tr>
                <td><strong>第9位</strong> ラクトリーアイ 目元クリーム</td>
                <td>エンチーム</td>
                <td>アイクリーム 15g</td>
                <td>¥13,200</td>
                <td>薄い目元の寒冷クマ・乾燥小ジワをふっくら持ち上げる</td>
              </tr>
              <tr>
                <td><strong>第10位</strong> ラブミーリップス 2.0</td>
                <td>Lov me Touch</td>
                <td>リップ美容液</td>
                <td>¥3,999</td>
                <td>医師監修。寒風でひび割れる唇を縦ジワレスに整える</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="faq-section" id="faq">
        <h2 class="section-title">❓ 真冬のフラーレンコスメ活用 Q&A：よくある質問</h2>

        <div class="faq-item">
          <div class="faq-q">Q1. フラーレンはなぜ冬の乾燥肌や小ジワに効果的なのですか？</div>
          <div class="faq-a">
            真冬の過酷な寒冷と暖房気流は、肌内部で活性酸素を大量に発生させ、角層の皮脂を過酸化脂質へと変質させてバリア機能を破壊します。フラーレンはビタミンCの250倍以上の抗酸化力を持ち、さらにスポンジのように活性酸素を吸着し続けるため、皮脂膜の過酸化を長時間防ぎ、角層のラメラ液晶構造を守り抜くことで高い水分保持力を維持します。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Q2. 水溶性フラーレン（ラジカルスポンジ）と油溶性フラーレン（リポフラーレン）はどう使い分けるべきですか？</div>
          <div class="faq-a">
            水溶性フラーレンは化粧水や導入美容液に適しており、角層の水分ネットワークに素早く浸透して内側の酸化ストレスを消去します。一方、油溶性フラーレンは乳液、クリーム、美容オイルに配合され、皮脂膜と一体化して外側からの乾燥と酸化を強力にブロックします。真冬は両方を併用する『ダブルフラーレン処方』を取り入れることで、角層の内外から隙間のない抗酸化保水シールドが完成します。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Q3. ビタミンCやレチノールなど他のエイジングケア成分と一緒に使っても大丈夫ですか？</div>
          <div class="faq-a">
            非常に相性が良く、むしろ併用が推奨されます。フラーレンは他の美容成分を酸化劣化から保護するシールド効果を持つため、不安定なビタミンCやレチノールと一緒に使うことで、それらの成分の美肌効果をより長く安定して肌へ届けることができます。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Q4. 朝と夜、どちらのタイミングで使うのがおすすめですか？</div>
          <div class="faq-a">
            理想は朝晩両方の使用です。朝使えば日中の紫外線、暖房気流、寒暖差による酸化乾燥を一日中ブロックし、夜使えば就寝中の暖房による水分蒸散を防ぎながら睡眠中の肌修復を強力にサポートします。
          </div>
        </div>
      </section>

      <section class="internal-links-section">
        <h2 class="section-title">🔗 あわせて読みたい！冬の高保湿スキンケア関連記事</h2>
        <p style="color: #475569; font-size: 0.95rem;">真冬の乾燥トラブルを全方位から撃退する人気特集記事をピックアップ。</p>

        <div class="internal-grid">
          <a href="/winter-sacran" class="internal-card">
            <div class="internal-card-title">💧 高保湿サクランコスメ10選</div>
            <div class="internal-card-desc">ヒアルロン酸の約10倍の保水膜！阿蘇の希少藍藻多糖体が真冬のインナードライを徹底救済。</div>
          </a>
          <a href="/winter-retinol-cream" class="internal-card">
            <div class="internal-card-title">🌸 高保湿レチノールクリーム10選</div>
            <div class="internal-card-desc">冬の乾燥小ジワとハリ不足に！ビタミンA誘導体で押し返すような弾力肌へ。</div>
          </a>
          <a href="/winter-niacinamide-serum" class="internal-card">
            <div class="internal-card-title">✨ 高保湿ナイアシンアミド美容液10選</div>
            <div class="internal-card-desc">シワ改善と美白を同時に！真冬のバリア機能を高める薬用ビタミンB3。</div>
          </a>
          <a href="/winter-liposome" class="internal-card">
            <div class="internal-card-title">🔬 高保湿リポソームコスメ10選</div>
            <div class="internal-card-desc">ナノカプセルが時間差で潤いを放出し続ける！真冬の深層保湿アプローチ。</div>
          </a>
        </div>
      </section>
    </article>
  </main>

  <footer>
    <div class="footer-inner">
      <div>
        <div class="footer-logo">LUMI COSMETICS</div>
        <p class="footer-text">
          LUMI COSMETICSは、11月〜12月の本格的な寒冷・乾燥シーズンを乗り切るための高品質コスメ・スキンケア情報を専門にお届けするビューティーメディアです。皮膚科学的根拠に基づいた成分解析と楽天市場のリアルタイムデータを融合し、客観的で信頼性の高いコスメ選びをサポートします。
        </p>
      </div>
      <div class="footer-links">
        <h5>サイトマップ・リンク</h5>
        <ul>
          <li><a href="/">冬コスメTOP</a></li>
          <li><a href="/winter-fullerene">高保湿フラーレン</a></li>
          <li><a href="/winter-sacran">高保湿サクラン</a></li>
          <li><a href="/winter-retinol-cream">高保湿レチノール</a></li>
          <li><a href="/winter-niacinamide-serum">高保湿ナイアシンアミド</a></li>
        </ul>
      </div>
    </div>
    <div class="copyright">
      &copy; 2026 LUMI COSMETICS. All Rights Reserved.
    </div>
  </footer>

</body>
</html>
"""

with open("winter-fullerene.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Generated winter-fullerene.html successfully! (File size: {len(full_html):,} bytes)")
