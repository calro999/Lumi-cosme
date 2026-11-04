import json
import re

with open("fetched_final_30_resurrection_beta_avocado.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_beta_glucan"]["items"]

# 各商品ごとの完全オリジナルなレビュー＆詳細データ
product_details = [
    {
        "rank": 1,
        "tag": "👑 次世代成分β-グルカンで劇的進化！世界最高峰の美肌回復プレセラム",
        "catch": "世界的人気美容液ジェニフィックが、驚異の修復力を持つ高純度β-グルカンを配合してフルリニューアル。真冬の過酷な寒冷ストレスと乾燥ダメージを秒速で立て直す",
        "brand_name": "LANCÔME (ランコム)",
        "capacity": "30ml / スポイト内蔵ボトル",
        "type": "高機能美肌修復ブースター美容液",
        "features": "高純度β-グルカン-CM、美肌菌プレ/プロバイオティクス、ヒアルロン酸、アデノシン",
        "value": "1滴に90兆個のβ-グルカンを凝縮。冬の寒暖差やエアコン乾燥で傷ついた肌バリアを急速修復し、吸い付くようななめらかさと弾力を注入",
        "desc_p1": "スキンケア界を震撼させたランコムの金字塔『ジェニフィック』が、医療分野の皮膚創傷治癒研究から着想を得て『ジェニフィック アルティメ』へと大進化を遂げました。その核となるキー成分こそが、次世代のスーパーリペア成分『β-グルカン（ベータグルカン）』です。11月から12月にかけて、屋外の氷点下近い寒風と、室内の25℃を超える暖房という強烈な温度差（最大20℃差）にさらされると、皮膚の毛細血管が収縮・拡張を繰り返し、肌のバリア機能は激しく消耗します。",
        "desc_p2": "肌に乗せた瞬間、シルクのように滑らかでみずみずしいリキッドが吸い込まれるように角層深部へと浸透。表面にベタつきを残さないのに、内側からギュッと密度が詰まったような強靭な弾力と水分感が湧き上がります。従来の美肌菌アプローチに加え、β-グルカンが乾燥による微小な炎症や肌荒れの火種を瞬時に消し去るため、使い続けるほどに赤みやゴワつきが消え、真冬でもトラブル知らずの澄んだキメ美肌をキープできます。",
        "target": "冬の寒暖差で肌が敏感に傾き赤みやザラつきが出る方、本気で肌の修復力とバリア力を底上げしたい方、最高峰のデパコス美容液の効果を実感したい方",
        "point": "朝晩の洗顔直後、まっさらな肌に自動充填スポイト1回分（1スポイト分）を顔全体に馴染ませます。手のひら全体で肌を包み込み、ゆっくりと深呼吸しながら温めるようにハンドプレスすると、成分が角層の奥深くへと浸透します。"
    },
    {
        "rank": 2,
        "tag": "💆‍♀️ プロのエステ現場で愛用される実力！300ml超特大の生β-グルカン原液美容液",
        "catch": "スエヒロタケから抽出した高純度β-グルカン（シゾフィラン）を贅沢配合。真冬の顔から首・デコルテまで濃密な保水クッションで包み込むサロン仕様セラム",
        "brand_name": "Spa treatment (スパトリートメント)",
        "capacity": "300ml / 大容量プッシュポンプ",
        "type": "サロン専売・高純度β-グルカン高保水美容液",
        "features": "シゾフィラン（キノコ由来β-グルカン）、ヒアルロン酸Na、植物エキス複合体",
        "value": "エステ業務用として開発された300mlの大容量。水分保持力はヒアルロン酸を凌駕し、真冬の全身の極度な乾燥・皮むけ・粉吹きを惜しみなくレスキュー",
        "desc_p1": "全国のエステティックサロンやクリニックのアフターケアとして絶大な信頼を集めるスパトリートメントの『βエッセンス』。キノコの一種であるスエヒロタケからバイオテクノロジーによって抽出された高純度β-グルカン「シゾフィラン」を主成分とする、プロフェッショナルユースの集中保水美容液です。",
        "desc_p2": "無色透明でとろみのある美容液を肌に乗せると、驚くほどスルスルと摩擦レスに伸び広がり、肌の上に『通気性のある保水ネット膜』を形成します。ヒアルロン酸よりも水分蒸発を防ぐ力が強く、エアコンの温風が直撃する環境でも水分を肌内にしっかりと閉じ込めます。大容量300mlボトルのため、顔だけでなく乾燥でチクチクしやすい首元やデコルテ、肘や手の甲までたっぷり贅沢に使えるのが最大の魅力です。",
        "target": "顔だけでなく首元やデコルテまでたっぷり惜しみなく保水したい方、エステサロン専売品の高い保湿力を自宅で実感したい方、冬の粉吹き肌を緊急鎮静したい方",
        "point": "化粧水の前後どちらでも使用可能です。洗顔後すぐに2プッシュを顔から首筋まで伸ばしてブースターとして使うか、化粧水の後に重ねて水分パックのように贅沢に馴染ませてください。美顔器の導入ジェルとしても抜群の相性を誇ります。"
    },
    {
        "rank": 3,
        "tag": "💧 水分保持力はヒアルロン酸の120%！100%ピュア酵母β-グルカンの神セラム",
        "catch": "余分な成分を一切加えず、100%純粋な発酵酵母由来β-グルカンのみをボトルに充填。冬の寒冷で干からびた肌深層へダイレクトに水分を吸着させる名作水分セラム",
        "brand_name": "iUNIK (アイユニック)",
        "capacity": "50ml / スポイトガラス瓶",
        "type": "100%純粋β-グルカン高保水美容液",
        "features": "酵母由来β-グルカン100%（水溶性多糖類水溶液）",
        "value": "ヒアルロン酸の約1.2倍の保水力を誇るピュア原液。肌の乾燥によるヒリつきや赤みを瞬時に落ち着かせ、インナードライを根本から解消",
        "desc_p1": "世界中のスキンケアオタクから「究極の水分セラム」と絶賛されている韓国iUNIK（アイユニック）の『ベータグルカン パワーモイスチャーセラム』。成分表を見ると驚くべきことに、酵母から抽出されたピュアなβ-グルカン水溶液が100%という、極限までシンプルを極めた処方です。",
        "desc_p2": "ヒアルロン酸特有の「乾燥した部屋で逆に肌の水分を奪う」という弱点を克服し、湿度が30%を下回る真冬の乾燥環境でも自重の何倍もの水分を抱え込み続けます。テクスチャーは濃厚なトロミがありながら、肌になじませるとスーッと浸透してベタつきが一切残りません。アレルギーテスト済みで刺激物が一切入っていないため、レチノール使用中の皮むけ時や、冬の寒風で肌が敏感になっているときでも安心して水分チャージができます。",
        "target": "ヒアルロン酸コスメでは保湿力が足りない・乾いてしまうと感じる方、成分数が少なく肌に優しいピュアな美容液を求める方、インナードライを解消したい方",
        "point": "朝晩の洗顔後、化粧水のあとにスポイト2〜3滴を手にとり、顔全体に優しくハンドプレスして馴染ませます。特に乾燥が気になる頬や口周りには2度塗りをすると、ふっくらとした水分クッションが肌の内側に出来上がります。"
    },
    {
        "rank": 4,
        "tag": "🛡️ 崩壊した肌バリアを完璧に再建！特許MLE×β-グルカンの鉄壁リペアクリーム",
        "catch": "皮膚科学に基づいた特許ラメラ技術MLEに高純度β-グルカンを配合。真冬の過酷な寒冷・乾燥で皮むけした角層の隙間をパズルのように埋め尽くす",
        "brand_name": "Real Barrier (リアルバリア)",
        "capacity": "50ml (+30ml増量セット) / ジャータイプ",
        "type": "高密着バリア機能再建クリーム",
        "features": "特許MLE複合セラミド、β-グルカン、アラントイン、パンテノール、フィトステロールズ",
        "value": "健康な皮膚の細胞間脂質と同一のマルタ十字構造を再現。冬の寒冷によって剥がれ落ちた角層のバリアを物理的に補修し、水分の蒸発を完全遮断",
        "desc_p1": "冬の本格的な乾燥で肌がチクチクと痛み、ファンデーションを塗るとウロコのように皮がめくれてしまう――そんな重度のバリア破綻肌を救うために皮膚科医と共同開発されたのが、韓国リアルバリアの『エクストリームクリーム』です。",
        "desc_p2": "こっくりと固めのリッチなバターテクスチャーですが、肌に乗せると体温でじんわりとろけて角質層に隙間なく密着します。特許技術MLEによってヒトの角層ラメラ構造と全く同じ脂質膜を形成し、そこに高保水のβ-グルカンと鎮静成分アラントインが浸透。暖房が効いた過酷な室内で一日中過ごしても、内側の水分が外へ逃げず、夕方になってもふっくら柔らかな手触りが続きます。",
        "target": "冬になると乾燥で皮膚がめくれたり粉を吹いてしまう方、肌の赤みやヒリつきに悩む方、翌朝まで絶対に乾かない超濃厚保湿クリームを探している方",
        "point": "付属のスパチュラでパール大を取り、手のひらで軽く温めてから顔全体に押し込むように塗布します。乾燥が深刻な部位には、バームを塗るように優しく重ねづけしてください。夜のナイトパックとしても最適です。"
    },
    {
        "rank": 5,
        "tag": "🍶 発酵美肌菌×高保水β-グルカン！冬のくすみとゴワつきを解きほぐす黄金比セラム",
        "catch": "天然酵母由来のガラクトミセス培養液に高純度β-グルカンを絶妙な比率でブレンド。真冬の寒さで血行が悪くなり、ゴワついてくすんだ冬枯れ肌を透明感あふれるモチ肌へ",
        "brand_name": "自然化粧品研究所 / ナチュラス",
        "capacity": "30ml / スポイト遮光瓶",
        "type": "発酵透明感×高保水エイジング美容液",
        "features": "ガラクトミセス培養液、β-グルカン、ヒアルロン酸Na、植物性BG",
        "value": "高級デパコスの代名詞であるガラクトミセス発酵液と、保水王β-グルカンを贅沢に同時配合。キメの乱れを滑らかに整えながら内側から発光するツヤ肌へ導く",
        "desc_p1": "冬になると乾燥だけでなく「顔色がどんより暗くくすむ」「肌が硬くゴワついてスキンケアが入っていかない」という複合的な悩みが噴出します。そんな冬枯れ肌の救世主として高い評価を得ているのが、自然化粧品研究所が手掛ける『ガラクトミセス×β-グルカン配合美容液』です。",
        "desc_p2": "米麹の発酵過程で生み出されるガラクトミセス培養液が、アミノ酸やミネラル、ペプチドを豊富に角層へ補給し、乱れたターンオーバーを滑らかにリセット。そこに高分子β-グルカンが潤いのヴェールを掛け合わせることで、硬直していた角質がみるみる柔らかく解きほぐされます。オイルフリーで水のようにみずみずしいのに、肌に馴染ませた後はまるで吸盤のように指に吸い付く高密度のモチモチ感が手に入ります。",
        "target": "冬の乾燥くすみや肌のゴワつきを同時にケアしたい方、SK-IIなどの発酵コスメが好きだがより高い保湿力を求める方、無香料・無添加の原液処方を好む方",
        "point": "洗顔直後または化粧水の後に、スポイトで3〜4滴を手にとり顔全体になじませます。小鼻の周りやあご先など、ザラつきやすい部分には指先で円を描くように優しく塗り込むと、キメが整ってつるんとした陶器肌に仕上がります。"
    },
    {
        "rank": 6,
        "tag": "🌿 10種のCICA×高純度β-グルカン！寒暖差でほてり赤らむ肌を冷涼鎮静する水分ジェル",
        "catch": "韓国オリーブヤングで数々の賞を受賞した名品シカクリーム。10種のツボクサ成分とβ-グルカンが、真冬の暖房によるほてりや寒風による赤みを優しくクールダウン",
        "brand_name": "Dr.G (ドクタージー)",
        "capacity": "70ml / ジャータイプ",
        "type": "低刺激・高水分鎮静シカジェルクリーム",
        "features": "10-CICAコンプレックス、高純度β-グルカン、エクトイン、ナイアシンアミド",
        "value": "毛穴を塞がないノンコメドジェニック処方。真冬の過剰な油分でニキビができやすい混合肌や、暖房の熱で赤ら顔になりやすい肌を水分で満たして鎮静",
        "desc_p1": "冬の乾燥対策といえば油分たっぷりの重いクリームが定番ですが、オイリー肌やニキビができやすい方にとっては「重すぎて毛穴が詰まる」「吹き出物ができる」というジレンマがあります。そんな肌質の方から熱狂的に支持されているのが、皮膚科医監修のDr.G『レッドブレミッシュ クリアスージングクリーム』です。",
        "desc_p2": "ぷるんとしたみずみずしいジェル状のクリームが、肌に乗せた瞬間に心地よい清涼感を与えて暖房による赤みやほてりを鎮静。10種類のCICA成分が肌荒れを防ぎ、高保水β-グルカンが角層内に水分を長時間キープします。油分に頼らず水分で満たす設計のため、夜たっぷり厚めに塗ってスリーピングマスクにしても翌朝ベタつかず、毛穴がきゅっと引き締まったみずみずしい透明肌を実感できます。",
        "target": "油分の多いクリームを使うとニキビができる方、暖房の効いた部屋で頬が赤くほてりやすい方、みずみずしい水分ジェルでしっかり保湿したい方",
        "point": "朝晩のスキンケアの最後に適量を顔全体に伸ばします。特に暖房の熱で赤みが出た日は、冷蔵庫で少し冷やしてから顔全体に厚めに塗る『水分スージングパック』として活用すると、即座に赤みが引いて毛穴が引き締まります。"
    },
    {
        "rank": 7,
        "tag": "🔬 ヒト型セラミド原液10%×β-グルカン！真冬のスカスカ角層を埋める濃厚エッセンス",
        "catch": "人の肌と同じ立体構造を持つ5種類のヒト型セラミドを10%という超高濃度で配合。β-グルカンとの相乗効果で、冬の木枯らしに負けない強靭な細胞間脂質を再構築",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "20ml / スポイト瓶",
        "type": "高濃度ヒト型セラミド×β-グルカン原液美容液",
        "features": "ヒト型セラミド（EOP/NP/AP/AS/NS）10%高配合、β-グルカン、水添レシチン、ヒアルロン酸Na",
        "value": "無駄な成分を徹底的に排除した高純度原液。真冬の洗顔後に1滴プラスするだけで、水分と油分のミルフィーユ構造を瞬時に修復し粉吹きをストップ",
        "desc_p1": "原料メーカー直販ならではの圧倒的な高濃度とコストパフォーマンスで支持されるKISO（基礎化粧品研究所）の『ヒトミドエッセンス X』。肌のバリアを司る最重要脂質「ヒト型セラミド」を5種類バランスよく10%も高濃度配合し、さらに水分保持を支えるβ-グルカンを掛け合わせた原液美容液です。",
        "desc_p2": "白濁したミルキーなリキッドは、肌になじませるとまるで吸い込まれるように角層細胞の隙間へと滑り込みます。寒さで角層がスカスカになり、水分を蓄えることができなくなった肌に、セラミドとβ-グルカンが新しいバリア壁を築き上げます。塗った直後から肌表面がふんわりと柔らかくなり、真冬の硬直したゴワつきが解消。手持ちの化粧水や乳液に1〜2滴ブレンドして使うことも可能です。",
        "target": "セラミドの本格的な補給を行いたい方、冬になると肌の粉吹きやキメの粗さが目立つ方、高品質な国内製造の原液コスメを求める方",
        "point": "洗顔後、化粧水の前に2〜3滴を手のひらに伸ばし、顔全体を包み込むように馴染ませます。特に乾燥しやすい目尻やほうれい線には指先で優しくトントンと叩き込むように重ねづけすると、ふっくらとしたハリが蘇ります。"
    },
    {
        "rank": 8,
        "tag": "⚡ 200時間超持続の極限シールド！パンテノール×エクトイン×β-グルカンの濃厚バーム",
        "catch": "砂漠肌を救うために開発された魔女工場の最高峰保湿ライン。高純度パンテノールと極限環境微生物エクトイン、β-グルカンが融合し、200時間しっとり潤い膜をキープ",
        "brand_name": "Manyo Factory (魔女工場)",
        "capacity": "80ml / 大容量チューブ",
        "type": "超高保湿バリアリペアバームクリーム",
        "features": "パンテノール（プロビタミンB5）、エクトイン、β-グルカン、マカデミア種子油、セラミドNP",
        "value": "肌バリアの修復と水分の密閉保持を極限まで追求。真冬の木枯らしや吹雪の日に外出しても一切肌が乾燥しない圧倒的なプロテクト力",
        "desc_p1": "韓国の大人気ブランド魔女工場が「極度の乾燥肌のために何ができるか」を突き詰めて開発した『パンテトイン ディープモイスチャークリーム』。肌修復を促すパンテノールと、塩湖の極限環境で生きる微生物の保護成分エクトインを黄金比でブレンドした特許成分「パンテトイン」に、高保水β-グルカンを配合した超濃厚クリームです。",
        "desc_p2": "チューブから出すと濃厚なバームのような固めのテクスチャーですが、肌に伸ばすと体温で滑らかにとろけてピタッと密着。肌の上に『第二の皮膚』のような保護膜を作り出し、室内の暖房による激しい水分蒸発を物理的にシャットアウトします。臨床試験で「200時間の保湿持続」が実証されている通り、夜塗って寝れば翌朝の洗顔時までモチモチの潤い膜が持続。チューブ容器で衛生的に持ち運べるのも嬉しいポイントです。",
        "target": "真冬に外出すると冷風で肌が痛くなる方、朝塗ったクリームが昼には乾いてしまう超乾燥肌の方、夜の濃厚な保湿パックとして使いたい方",
        "point": "スキンケアの最後に、さくらんぼ大を手のひらで温めてから顔全体を包み込むように塗布します。乾燥がひどい目元や口元には重ねづけし、手のひらでハンドプレスして密着度を高めてください。"
    },
    {
        "rank": 9,
        "tag": "🌿 荒れた冬肌を急速鎮静！ドクダミ77%×β-グルカンが叶えるみずみずしい水分満タン肌",
        "catch": "韓国や日本で累計数百万本を突破した超人気トナー。ドクダミエキスの抗炎症パワーにβ-グルカンとヒアルロン酸を融合し、冬の乾燥ニキビやゆらぎ肌を瞬時に整える",
        "brand_name": "Anua (アヌア)",
        "capacity": "250ml / クリアボトル",
        "type": "弱酸性・鎮静保水トリートメント化粧水",
        "features": "ドクダミエキス77%、β-グルカン、ヒアルロン酸Na、パンテノール、ツボクサエキス",
        "value": "弱酸性低刺激処方。冬の乾燥によって皮脂バランスが崩れ、大人ニキビや肌荒れを繰り返す肌をみずみずしく鎮静しながら奥深くまで水分を届ける",
        "desc_p1": "冬の乾燥は、カサつきだけでなく「角層が硬化して毛穴が詰まり、顎やフェイスラインに痛い乾燥ニキビができる」という厄介な肌トラブルを引き起こします。そんな冬のゆらぎ肌・肌荒れ対策として絶大な支持を集めているのが、Anuaの『ドクダミ 77% スージングトナー』です。",
        "desc_p2": "主成分に水ではなくドクダミエキスを77%も贅沢に使用し、さらに高保水のβ-グルカンを配合。シャバシャバとした軽やかな水のような感触でありながら、肌に乗せるとグングンと角層深くまで吸い込まれ、内側から水分で満たされる感覚を味わえます。ベタつきが一切ないため、何回重ねづけしても重くならず、火照った肌の熱をクールダウンしながら健やかな弱酸性状態へと整えてくれます。",
        "target": "冬の乾燥によって大人ニキビや吹き出物が出やすい方、重い化粧水が苦手でさっぱり奥まで潤したい方、コットンパックで赤みを鎮静させたい方",
        "point": "洗顔後、手のひらまたはコットンにたっぷり取り、優しくパッティングしながら馴染ませます。赤みや肌荒れが気になる部位には、薄手のコットンに本品を浸して3〜5分間ローションパックを行うと、赤みが驚くほど早く落ち着きます。"
    },
    {
        "rank": 10,
        "tag": "🍵 洗顔後3秒の水分チャージ！緑茶乳酸菌×ナノカプセルヒアルロン酸×β-グルカン",
        "catch": "チェジュ島の無農薬緑茶から生まれた美容水と乳酸菌発酵成分。β-グルカンが洗顔直後の無防備な肌に素早く浸透し、一日中乾かない水分バリアを形成する名品導入セラム",
        "brand_name": "innisfree (イニスフリー)",
        "capacity": "80ml / プッシュポンプ",
        "type": "水分バリアブースター導入美容液",
        "features": "緑茶乳酸菌発酵溶解質、ナノカプセルヒアルロン酸、β-グルカン、パンテノール、スクワラン",
        "value": "洗顔後すぐの角層に素早く浸透する瞬間ブースター。乾燥によるツッパリ感を瞬時に解消し、その後に使う化粧水の浸透力を何倍にも引き上げる",
        "desc_p1": "世界中で愛され続けるイニスフリーのNo.1メガヒット美容液『グリーンティーシード ヒアルロン セラム』。真冬の洗顔後は、肌を守る皮脂膜が洗い流され、わずか数十秒の間に急激な水分蒸散が始まります。そんな過酷な冬の入浴後・洗顔後すぐに使うファーストセラムとして最適です。",
        "desc_p2": "リニューアルにより、微細ナノカプセル化されたヒアルロン酸に加え、優れた水分保持力を持つβ-グルカンを新配合。みずみずしいジェル状のセラムが肌に乗せた瞬間にほどけるように浸透し、乾燥で硬くなった角層をふっくらとほぐします。これを使うと使わないとでは、その後に重ねる化粧水の吸い込み方がまるで変わり、真冬の暖房下でも夕方までみずみずしいツヤ肌がキープできます。",
        "target": "お風呂上がりや洗顔後に肌がすぐ突っ張ってしまう方、いつもの化粧水の浸透力を高めたい方、みずみずしく爽快な使い心地のブースターを求める方",
        "point": "朝晩の洗顔直後、タオルドライした肌に1〜2プッシュを手にとって顔全体に優しく馴染ませます。その後、すぐにいつもの化粧水と乳液を重ねることで、水分を逃さない強固なうるおいルートが完成します。"
    }
]

# FAQ 生成
faqs = [
    {
        "q": "β-グルカン（ベータグルカン）は、ヒアルロン酸と比べてどこが優れているのですか？",
        "a": "β-グルカンは酵母やキノコ、穀物から抽出される多糖類で、ヒアルロン酸の約1.2倍（20%増）という極めて高い水分保持能力を持っています。さらに決定的な違いは『環境に左右されない保水力』と『皮膚修復作用』です。ヒアルロン酸は湿度が極端に低い真冬の室内では肌の水分を奪って蒸散してしまうことがありますが、β-グルカンは強固な分子結合により低湿度下でも水分を離しません。また、皮膚の免疫細胞（マクロファージ等）に働きかけて肌バリアの自己修復を促進する機能も備えています。"
    },
    {
        "q": "11月〜12月の肌トラブル（赤み、ヒリヒリ、粉吹き）にβ-グルカンが推奨される理由は？",
        "a": "真冬は『屋外の冷気』と『室内の温風暖房』による激しい寒暖差によって毛細血管がダメージを受け、角層が薄くなり（菲薄化）、わずかな刺激でも赤みやヒリつきが生じます。β-グルカンは優れた抗炎症作用と皮膚修復能を持ち、傷ついた角層バリアを優しく保護しながら、通気性のある保水シールド膜を肌表面に形成します。これにより、刺激物質の侵入を防ぎつつ深層の水分を保持し、冬特有の赤みや粉吹きを速やかに鎮静させます。"
    },
    {
        "q": "レチノールやビタミンC、ピーリングコスメと一緒に使っても大丈夫ですか？",
        "a": "相性は抜群です。むしろレチノール使用時のA反応（皮むけ・赤み・乾燥）や、高濃度ビタミンCによるピリピリ感を和らげるためのバッファー（緩和剤）として、美容皮膚科でもβ-グルカンは強く推奨されています。刺激の強い攻めのエイジングケアを行う際は、β-グルカン配合のセラムやクリームを併用することで、肌荒れを防ぎながら高い美肌効果を引き出すことができます。"
    },
    {
        "q": "脂性肌やニキビ肌でも、β-グルカン配合コスメを使えますか？",
        "a": "非常に適しています。β-グルカンは油分（オイル）ではなく水溶性の多糖類であるため、重い油分のように毛穴を塞いでアクネ菌を増殖させる心配がありません。水分不足から皮脂が過剰分泌してしまうインナードライ肌や、冬の乾燥ニキビに悩む方でも、ノンコメドジェニック処方のジェルやセラム（Dr.GやiUNIKなど）を選ぶことで、さっぱりとした使用感で深層保水が叶います。"
    }
]

# HTML テーブル行生成
table_rows = []
for it in items:
    r = it["rank"]
    p_info = next((p for p in product_details if p["rank"] == r), None)
    type_name = p_info["type"] if p_info else "高保湿コスメ"
    brand = it["brand"]
    name = it["display_name"].split(" (")[0]
    price = f"¥{it['price']:,}"
    img = it["image"]
    url = it["url"]
    
    row = f"""
    <tr>
      <td class="rank-num rank-{r}">{r}位</td>
      <td class="product-thumb"><a href="{url}" target="_blank" rel="nofollow noopener"><img src="{img}" alt="{name}" loading="lazy" width="80" height="80"></a></td>
      <td class="product-name-cell">
        <span class="product-brand">{brand}</span>
        <a href="{url}" target="_blank" rel="nofollow noopener" class="table-prod-link">{name}</a>
      </td>
      <td><span class="type-badge">{type_name}</span></td>
      <td class="product-price">{price}</td>
      <td><a href="{url}" target="_blank" rel="nofollow noopener" class="table-btn">楽天で見る</a></td>
    </tr>
    """
    table_rows.append(row)

table_joined = "\n".join(table_rows)

# 商品カード生成
cards = []
for it in items:
    r = it["rank"]
    p = next((x for x in product_details if x["rank"] == r), product_details[0])
    price = f"¥{it['price']:,}"
    img = it["image"]
    url = it["url"]
    shop = it["shop_name"]
    rate = it["review_rate"]
    reviews = it["review_count"]
    
    card = f"""
    <article class="product-card" id="rank-{r}">
      <div class="card-header">
        <div class="rank-badge rank-{r}">第{r}位</div>
        <div class="card-titles">
          <span class="card-tag">{p['tag']}</span>
          <h3 class="card-name">{it['display_name']}</h3>
        </div>
      </div>
      
      <p class="card-catch"><strong>【注目ポイント】</strong> {p['catch']}</p>
      
      <div class="card-body">
        <div class="card-image-box">
          <a href="{url}" target="_blank" rel="nofollow noopener">
            <img src="{img}" alt="{it['display_name']}" loading="lazy" width="300" height="300" class="card-img">
          </a>
          <div class="card-price-box">
            <span class="price-label">楽天市場参考価格</span>
            <span class="price-val">{price}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <div class="card-review-box">
            <span class="star-rating">★ {rate}</span>
            <span class="review-count">({reviews}件のレビュー)</span>
          </div>
          <a href="{url}" target="_blank" rel="nofollow noopener" class="card-aff-btn">
            楽天市場で最新価格をチェック ➔
          </a>
        </div>
        
        <div class="card-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{p['brand_name']}</td></tr>
            <tr><th>容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>注目保湿・修復成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の肌バリア対策価値</th><td>{p['value']}</td></tr>
          </table>
          
          <div class="card-desc">
            <h4 class="desc-heading">🔍 美容皮膚サイエンスによる徹底解説＆冬の使用感</h4>
            <p class="desc-p">{p['desc_p1']}</p>
            <p class="desc-p">{p['desc_p2']}</p>
            
            <div class="eval-box">
              <div class="eval-item">
                <span class="eval-title">🎯 こんな方に特におすすめ</span>
                <p class="eval-text">{p['target']}</p>
              </div>
              <div class="eval-item">
                <span class="eval-title">💡 効果を高める冬のベストな使い方</span>
                <p class="eval-text">{p['point']}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </article>
    """
    cards.append(card)

cards_joined = "\n".join(cards)

# FAQ HTML生成
faq_items = []
for f in faqs:
    item = f"""
    <div class="faq-card">
      <h3 class="faq-q"><span class="q-icon">Q</span> {f['q']}</h3>
      <div class="faq-a"><span class="a-icon">A</span> <p>{f['a']}</p></div>
    </div>
    """
    faq_items.append(item)

faq_joined = "\n".join(faq_items)

# JSON-LD 生成
schema_items = []
for it in items:
    schema_items.append({
        "@type": "ListItem",
        "position": it["rank"],
        "name": it["brand"] + " " + it["display_name"].split(" (")[0],
        "image": it["image"],
        "offers": {
            "@type": "Offer",
            "priceCurrency": "JPY",
            "price": str(it["price"]),
            "url": it["url"],
            "availability": "https://schema.org/InStock"
        }
    })

schema_json = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "ItemList",
            "name": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸を超える水分保持力で冬のバリアを立て直す高保湿ベータグルカンコスメランク10",
            "description": "ヒアルロン酸の約1.2倍の保水力と自己治癒修復力を持つ次世代成分β-グルカン。真冬の過酷な寒冷とエアコン乾燥を打ち破る実力派コスメ10選を徹底比較。",
            "numberOfItems": 10,
            "itemListElement": schema_items
        },
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸を超える水分保持力で冬のバリアを立て直す高保湿ベータグルカンコスメランク10",
            "description": "冬の寒暖差で荒れた角層バリアを深層から修復。ヒアルロン酸以上の水分保持力を誇るβ-グルカン配合の人気スキンケア10選を皮膚科学の観点から詳細レビュー。",
            "datePublished": "2026-11-04T16:00:00+09:00",
            "dateModified": "2026-11-04T16:00:00+09:00",
            "inLanguage": "ja",
            "mainEntityOfPage": "https://calro999.github.io/cosme/winter-beta-glucan.html"
        }
    ]
}, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！ヒアルロン酸を超える水分保持力で冬のバリアを立て直す高保湿ベータグルカンコスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月〜12月の寒冷乾燥と暖房ダメージで弱った肌バリアを急速修復！ヒアルロン酸の約1.2倍の保水力を誇る次世代スーパー成分『β-グルカン（ベータグルカン）』配合の高保湿コスメ人気ランキング10選。楽天市場のリアルタイム価格情報・成分解析付き。">
  <meta name="keywords" content="ベータグルカン コスメ, β-グルカン 美容液, ランコム ジェニフィック アルティメ, iUNIK ベータグルカン, 保湿力 高い スキンケア, 冬 肌荒れ 鎮静, バリア機能 修復, 11月 コスメ, 12月 コスメ">
  <link rel="canonical" href="https://calro999.github.io/cosme/winter-beta-glucan.html">
  <link rel="icon" href="favicon.jpg" type="image/jpeg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --primary-color: #2563eb;
      --primary-dark: #1d4ed8;
      --primary-light: #dbeafe;
      --accent-color: #06b6d4;
      --text-main: #1e293b;
      --text-sub: #475569;
      --text-light: #64748b;
      --bg-page: #f1f5f9;
      --bg-card: #ffffff;
      --border-color: #cbd5e1;
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.05);
      --shadow-md: 0 4px 12px rgba(37, 99, 235, 0.1);
      --shadow-lg: 0 10px 25px -5px rgba(37, 99, 235, 0.15);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.8;
      padding-bottom: 4rem;
    }}

    .site-header {{
      background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #3b82f6 100%);
      color: #ffffff;
      padding: 2rem 1.5rem 2.5rem;
      text-align: center;
      box-shadow: 0 4px 20px rgba(37, 99, 235, 0.25);
    }}
    .site-header-nav {{
      max-width: 1100px;
      margin: 0 auto 1.25rem;
      text-align: left;
    }}
    .site-header-nav a {{
      color: #dbeafe;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }}
    .site-header-nav a:hover {{ text-decoration: underline; }}
    .header-badge {{
      display: inline-block;
      background: rgba(255,255,255,0.2);
      backdrop-filter: blur(8px);
      padding: 0.4rem 1.2rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 0.8rem;
    }}
    .site-title {{
      font-size: clamp(1.4rem, 4vw, 2.2rem);
      font-weight: 800;
      line-height: 1.35;
      margin-bottom: 1rem;
      text-shadow: 0 2px 4px rgba(0,0,0,0.15);
      max-width: 900px;
      margin-left: auto;
      margin-right: auto;
    }}
    .site-subtitle {{
      font-size: 0.95rem;
      color: #eff6ff;
      max-width: 800px;
      margin: 0 auto;
    }}

    .main-container {{
      max-width: 1040px;
      margin: -1.5rem auto 0;
      padding: 0 1rem;
    }}

    .toc-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 0.6rem;
    }}
    .toc-list li a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.92rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: color 0.2s;
    }}
    .toc-list li a:hover {{ color: var(--primary-color); font-weight: 700; }}

    .content-section {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--primary-dark);
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.6rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .section-p {{
      font-size: 1rem;
      color: var(--text-sub);
      margin-bottom: 1.25rem;
      text-align: justify;
    }}

    .compare-table-wrapper {{
      overflow-x: auto;
      margin: 1.5rem 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      background: #ffffff;
      font-size: 0.92rem;
      min-width: 650px;
    }}
    .compare-table th {{
      background: #eff6ff;
      color: var(--primary-dark);
      padding: 0.9rem 0.75rem;
      text-align: center;
      font-weight: 700;
      border-bottom: 2px solid var(--primary-color);
      white-space: nowrap;
    }}
    .compare-table td {{
      padding: 0.9rem 0.75rem;
      border-bottom: 1px solid var(--border-color);
      vertical-align: middle;
      text-align: center;
    }}
    .compare-table tr:hover {{ background-color: #f8fafc; }}
    .rank-num {{
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.2rem;
    }}
    .rank-1 {{ color: #eab308; }}
    .rank-2 {{ color: #94a3b8; }}
    .rank-3 {{ color: #d97706; }}
    .product-thumb img {{
      border-radius: var(--radius-sm);
      object-fit: cover;
      box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }}
    .product-name-cell {{
      text-align: left !important;
      max-width: 280px;
    }}
    .product-brand {{
      display: block;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--primary-color);
      text-transform: uppercase;
    }}
    .table-prod-link {{
      color: var(--text-main);
      text-decoration: none;
      font-weight: 700;
      line-height: 1.4;
      display: inline-block;
      margin-top: 0.2rem;
    }}
    .table-prod-link:hover {{ color: var(--primary-color); text-decoration: underline; }}
    .type-badge {{
      display: inline-block;
      padding: 0.25rem 0.6rem;
      background: #f1f5f9;
      color: #475569;
      border-radius: 4px;
      font-size: 0.78rem;
      font-weight: 600;
      white-space: nowrap;
    }}
    .product-price {{
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      color: #e11d48;
      font-size: 1rem;
      white-space: nowrap;
    }}
    .table-btn {{
      display: inline-block;
      padding: 0.45rem 0.9rem;
      background: var(--primary-color);
      color: #ffffff;
      text-decoration: none;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      white-space: nowrap;
      transition: background 0.2s;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}

    .product-card {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      position: relative;
    }}
    .card-header {{
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 1rem;
    }}
    .rank-badge {{
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.1rem;
      color: #ffffff;
      background: var(--primary-color);
      padding: 0.4rem 1rem;
      border-radius: var(--radius-sm);
      flex-shrink: 0;
    }}
    .rank-badge.rank-1 {{ background: linear-gradient(135deg, #f59e0b, #d97706); }}
    .rank-badge.rank-2 {{ background: linear-gradient(135deg, #64748b, #475569); }}
    .rank-badge.rank-3 {{ background: linear-gradient(135deg, #b45309, #78350f); }}
    .card-titles {{ flex: 1; }}
    .card-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 0.2rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 0.4rem;
    }}
    .card-name {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.4;
    }}
    .card-catch {{
      background: #f8fafc;
      border-left: 4px solid var(--primary-color);
      padding: 0.9rem 1.2rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-bottom: 1.5rem;
      font-size: 0.95rem;
      color: #334155;
    }}
    .card-body {{
      display: grid;
      grid-template-columns: 300px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .card-body {{ grid-template-columns: 1fr; }}
      .card-image-box {{ max-width: 320px; margin: 0 auto; }}
    }}
    .card-image-box {{
      text-align: center;
    }}
    .card-img {{
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
      margin-bottom: 1rem;
      object-fit: cover;
      max-width: 100%;
      height: auto;
    }}
    .card-price-box {{
      background: #fff1f2;
      border-radius: var(--radius-sm);
      padding: 0.6rem;
      margin-bottom: 0.6rem;
    }}
    .price-label {{ display: block; font-size: 0.75rem; color: #9f1239; }}
    .price-val {{ font-family: 'Outfit', sans-serif; font-size: 1.4rem; font-weight: 800; color: #be123c; }}
    .price-tax {{ font-size: 0.75rem; color: #9f1239; }}
    .card-review-box {{
      margin-bottom: 1rem;
      font-size: 0.88rem;
    }}
    .star-rating {{ color: #f59e0b; font-weight: 700; margin-right: 0.4rem; }}
    .review-count {{ color: var(--text-light); }}
    .card-aff-btn {{
      display: block;
      background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);
      color: #ffffff;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 0.85rem 1rem;
      border-radius: var(--radius-md);
      box-shadow: 0 4px 10px rgba(225, 29, 72, 0.25);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .card-aff-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(225, 29, 72, 0.35);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }}
    .spec-table th {{
      width: 25%;
      padding: 0.65rem 0.8rem;
      background: #f8fafc;
      border: 1px solid var(--border-color);
      color: #475569;
      font-weight: 700;
      text-align: left;
    }}
    .spec-table td {{
      padding: 0.65rem 0.8rem;
      border: 1px solid var(--border-color);
      color: var(--text-main);
    }}
    .desc-heading {{
      font-size: 1.08rem;
      font-weight: 800;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .desc-p {{
      font-size: 0.96rem;
      color: var(--text-sub);
      margin-bottom: 1rem;
      line-height: 1.8;
      text-align: justify;
    }}
    .eval-box {{
      background: #eff6ff;
      border-radius: var(--radius-md);
      padding: 1.25rem;
      margin-top: 1.25rem;
      border: 1px solid #bfdbfe;
    }}
    .eval-item {{ margin-bottom: 0.8rem; }}
    .eval-item:last-child {{ margin-bottom: 0; }}
    .eval-title {{
      display: block;
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--primary-dark);
      margin-bottom: 0.25rem;
    }}
    .eval-text {{
      font-size: 0.92rem;
      color: #1e293b;
      line-height: 1.6;
    }}

    .faq-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.4rem;
      margin-bottom: 1.25rem;
    }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
      margin-bottom: 0.6rem;
    }}
    .q-icon {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 24px;
      height: 24px;
      background: var(--primary-color);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      border-radius: 50%;
      flex-shrink: 0;
    }}
    .faq-a {{
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
      font-size: 0.95rem;
      color: var(--text-sub);
      line-height: 1.7;
    }}
    .a-icon {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 24px;
      height: 24px;
      background: #0284c7;
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      border-radius: 50%;
      flex-shrink: 0;
    }}

    .footer-internal-links {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-top: 3rem;
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 0.75rem;
      margin-top: 1.25rem;
    }}
    .footer-link-item {{
      padding: 0.65rem 0.85rem;
      background: #f8fafc;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.86rem;
      font-weight: 600;
      display: block;
      transition: all 0.2s;
    }}
    .footer-link-item:hover {{
      background: var(--primary-light);
      border-color: var(--primary-color);
      color: var(--primary-dark);
    }}

    .site-footer {{
      text-align: center;
      margin-top: 3rem;
      color: var(--text-light);
      font-size: 0.85rem;
    }}
  </style>

  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body>

  <header class="site-header">
    <div class="site-header-nav">
      <a href="index.html">🏠 冬コスメ総合TOPへ戻る</a>
    </div>
    <span class="header-badge">❄️ 11月〜12月・高保水＆バリア修復の切り札 ❄️</span>
    <h1 class="site-title">保湿力の強さで肌乾燥とさようなら！ヒアルロン酸を超える水分保持力で冬のバリアを立て直す高保湿ベータグルカンコスメランク10</h1>
    <p class="site-subtitle">
      ヒアルロン酸の約1.2倍の水分保持力と肌の自己治癒修復力。真冬の過酷な寒冷・寒暖差ストレスでボロボロになった肌バリアを救う「β-グルカン（ベータグルカン）」名品10選を徹底検証！
    </p>
  </header>

  <main class="main-container">
    
    <!-- 目次 -->
    <nav class="toc-box" aria-label="記事の目次">
      <div class="toc-title">📑 目次・もくじ</div>
      <ul class="toc-list">
        <li><a href="#why-beta-glucan">1. なぜヒアルロン酸ではなく「β-グルカン」なのか？冬肌への科学的効果</a></li>
        <li><a href="#how-to-choose">2. 失敗しない冬のβ-グルカンコスメの選び方・3つのポイント</a></li>
        <li><a href="#comparison-table">3. β-グルカンコスメ10選 スペック＆価格比較表</a></li>
        <li><a href="#ranking-section">4. 高保湿おすすめコスメランキング10選 詳細レビュー</a></li>
        <li><a href="#faq-section">5. 美容皮膚サイエンスで答えるQ&amp;A（よくある質問）</a></li>
        <li><a href="#conclusion">6. まとめ：寒暖差とエアコン乾燥に屈しない強靭な水分バリアの作り方</a></li>
        <li><a href="#internal-links">7. 関連する冬の高保湿コスメ特集一覧</a></li>
      </ul>
    </nav>

    <!-- セクション1 科学的背景 -->
    <section class="content-section" id="why-beta-glucan">
      <h2 class="section-title">🔬 1. なぜヒアルロン酸ではなく「β-グルカン」なのか？冬肌への科学的効果</h2>
      <p class="section-p">
        11月から12月にかけて、私たちの肌を襲う最大の脅威は「極端な寒暖差」と「暖房による湿度の蒸発」です。屋外では5℃前後の冷たい風にさらされて毛細血管がギュッと収縮し、室内に入ると25℃の暖房温風によって一気に血管が拡張します。
      </p>
      <p class="section-p">
        この激しい温度変化が日に何度も繰り返されることで、肌の角層バリアは物理的・生化学的に疲弊し、皮膚が薄くなる菲薄化（ひはくか）が進行。その結果、<strong>「何をつけてもピリピリとしみる」「頬が赤くほてって痒い」「粉を吹いて皮がめくれる」</strong>という深刻なバリア破綻状態に陥ります。
      </p>
      <p class="section-p">
        従来の保湿ケアとして定番の「ヒアルロン酸」は確かに優れた保水成分ですが、実は<strong>「湿度が極端に低い冬の暖房空間では、角層内の水分を逆に大気中へ放出してしまう」</strong>という弱点が存在します。
      </p>
      <p class="section-p">
        この冬の乾燥ジレンマを打破する成分として、世界の美容皮膚科学界でいま最も注目されているのが<strong>『β-グルカン（ベータグルカン）』</strong>です。
      </p>
      <p class="section-p">
        β-グルカンは酵母、キノコ（スエヒロタケ等）、オーツ麦などに含まれる天然の多糖類で、以下の圧倒的な優位性を持っています：
      </p>
      <ul style="padding-left: 1.5rem; margin-bottom: 1.25rem; color: var(--text-sub); line-height: 1.8;">
        <li><strong>ヒアルロン酸の約120%（20%増）の水分保持力：</strong> 低湿度環境下でも水分をガッチリと手放さず、肌深層まで高密度な水分クッションを構築します。</li>
        <li><strong>皮膚の自己修復＆鎮静メカニズムの起動：</strong> 傷ついた皮膚細胞や免疫細胞（ランゲルハンス細胞など）を活性化し、冬の寒冷で破綻した角層バリアの再生スピードを飛躍的に高めます。</li>
        <li><strong>通気性のある保水シールド膜：</strong> 肌呼吸を妨げることなく表面を薄い膜で覆い、冷風やアレルゲン、乾燥の物理的ダメージをシャットアウトします。</li>
      </ul>
      <p class="section-p">
        大手デパコスブランドのランコムが最高峰美容液『ジェニフィック』のメイン成分としてβ-グルカンを採用したことからも分かる通り、今期の冬スキンケアにおいて最も頼りになる革新的成分なのです。
      </p>
    </section>

    <!-- セクション2 選び方 -->
    <section class="content-section" id="how-to-choose">
      <h2 class="section-title">🔍 2. 失敗しない冬のβ-グルカンコスメの選び方・3つのポイント</h2>
      <p class="section-p">
        真冬の過酷な環境から肌を守り抜くために、製品を選ぶ際は以下の3つのポイントを基準にしましょう。
      </p>
      <div style="background: var(--bg-page); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; margin-bottom: 1.25rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.4rem;">ポイント①：純度と抽出源（酵母由来・キノコ由来・オーツ麦由来）をチェック</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          酵母由来の純度100%原液（iUNIKなど）は、アレルギーや刺激のリスクが極めて低く、敏感肌の深層保水に最適です。スエヒロタケ等のキノコ由来（シゾフィラン／スパトリートメントなど）は医療用創傷治癒にも使われる高い修復力を誇り、オーツ麦由来は肌をふっくら柔らかくするエモリエント効果に優れています。
        </p>
      </div>
      <div style="background: var(--bg-page); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; margin-bottom: 1.25rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.4rem;">ポイント②：肌悩みに合わせた「掛け合わせ成分（セラミド・CICA・パンテノール）」</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          乾燥による皮むけや粉吹きには「ヒト型セラミド（リアルバリア、KISO）」、暖房による赤みやほてりには「CICA・ドクダミ（Dr.G、Anua）」、極度の肌荒れ・インナードライには「パンテノール・エクトイン（魔女工場）」との相乗処方が劇的な効果を発揮します。
        </p>
      </div>
      <div style="background: var(--bg-page); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.4rem;">ポイント③：スキンケアルーティンにおける「投入ステップ」を意識する</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          洗顔直後のブースターとして角層深部へ送り込むセラムタイプ（ランコム、イニスフリー、iUNIK）か、スキンケアの最後にすべての潤いを閉じ込めるバーム・クリームタイプ（リアルバリア、魔女工場）か、ご自身の最も強化したいステップに合わせて選択しましょう。
        </p>
      </div>
    </section>

    <!-- セクション3 比較表 -->
    <section class="content-section" id="comparison-table">
      <h2 class="section-title">📊 3. β-グルカンコスメ10選 スペック＆価格比較表</h2>
      <p class="section-p">
        楽天市場公式APIよりリアルタイムに取得した最新の販売価格と製品仕様の一覧表です。テクスチャーや配合成分の違いを比較し、最適な1本を見つけてください。
      </p>
      <div class="compare-table-wrapper">
        <table class="compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品画像</th>
              <th>商品名・ブランド</th>
              <th>アイテム種別</th>
              <th>楽天参考価格</th>
              <th>商品詳細</th>
            </tr>
          </thead>
          <tbody>
            {table_joined}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4 ランキング詳細 -->
    <section id="ranking-section">
      <h2 style="font-size: 1.6rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 2rem; text-align: center;">
        🏆 高保湿β-グルカンコスメおすすめ人気ランキング10選
      </h2>
      {cards_joined}
    </section>

    <!-- セクション5 Q&A -->
    <section class="content-section" id="faq-section">
      <h2 class="section-title">❓ 5. 美容皮膚サイエンスで答えるQ&amp;A（よくある質問）</h2>
      {faq_joined}
    </section>

    <!-- セクション6 まとめ -->
    <section class="content-section" id="conclusion">
      <h2 class="section-title">✨ 6. まとめ：寒暖差とエアコン乾燥に屈しない強靭な水分バリアの作り方</h2>
      <p class="section-p">
        11月から12月にかけての寒冷・暖房期は、従来の水分補給だけでは肌のバリア破綻を食い止めることが困難です。
      </p>
      <p class="section-p">
        ヒアルロン酸を凌ぐ水分保持力と、傷ついた皮膚を自己修復へと導く「β-グルカン」を取り入れることで、暖房の熱気にも木枯らしの冷気にも負けない、モチモチと吸い付くような健やかな美肌を保つことができます。
      </p>
      <p class="section-p">
        洗顔直後のまっさらな素肌にランコムやiUNIKの美容液で深層保水を行い、リアルバリアや魔女工場のリッチなクリームで完璧なシールドを築く――ぜひこの冬はβ-グルカンの圧倒的な保護力を味方につけて、トラブル知らずの快適な冬をお過ごしください。
      </p>
    </section>

    <!-- 内部リンク -->
    <section class="footer-internal-links" id="internal-links">
      <h2 style="font-size: 1.25rem; font-weight: 800; color: #1f2937; margin-bottom: 0.5rem;">
        🔗 併せて読みたい冬コスメ・高保湿スキンケア関連記事
      </h2>
      <p style="font-size: 0.9rem; color: #6b7280;">
        当サイトでは、11月〜12月の肌悩みに合わせた高保湿コスメや成分別ランキングを多数公開しています。
      </p>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で同期されます -->
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 当サイトは楽天市場アフィリエイトプログラムに参加しています。</p>
  </footer>

</body>
</html>
"""

with open("winter-beta-glucan.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-beta-glucan.html successfully. Size: {len(html_content):,} bytes")
