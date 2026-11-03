import json
import re

with open("fetched_3new_nov_dec_proteoglycan_propolis_galactomyces_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_proteoglycan"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 高純度原液の最高峰！ヒアルロン酸を凌駕する保水力で冬のたるみ乾燥を跳ね返す",
        "catch": "角層深部へ吸い込まれるように浸透。冬の乾ききった肌に圧倒的な密度と弾力感を呼び戻す王道原液",
        "brand_name": "fracora (フラコラ)",
        "capacity": "30ml (プロテオグリカン原液)",
        "type": "高純度・高濃度プロテオグリカン美容液",
        "features": "国産サケ鼻軟骨由来プロテオグリカン100%原液、無香料・無着色・パラベンフリー・鉱物油フリー・界面活性剤フリー",
        "value": "水のようにサラリとした質感ながら、肌になじませた瞬間に角層細胞の間を潤いで満たし、ヒアルロン酸の約1.3倍といわれる保水力を発揮。真冬の冷風でもしぼまない肌土台を形成する",
        "desc_p1": "11月から12月にかけて湿度が20%近くまで低下すると、真皮や角層の水分保持ネットワークが弱まり、皮膚の菲薄化とともに乾燥小ジワが目立ち始めます。フラコラのプロテオグリカン原液は、かつて1g3,000万円とも言われた希少成分プロテオグリカンを、独自技術によって高純度かつ高濃度に抽出した先行美容原液です。",
        "desc_p2": "テクスチャーはまるで水のように澄み渡り、ベタつきが一切ありません。洗顔直後の素肌にのばすと、渇いたスポンジが水を吸い上げるように角層の奥深くまで素早く引き込まれます。プロテオグリカン特有のEGF様作用によって肌のターンオーバーサイクルを力強く後押しし、内側から押し返すようなピンとしたハリ感が定着。朝のメイク前に仕込むことで、夕方の目元・口元のファンデーション割れを劇的に防ぎます。",
        "target": "目尻や口元の乾燥小ジワが深く刻まれ始めた方、高保湿化粧水でも潤いが奥まで届かないインナードライ肌、ベタつく美容液が苦手な方",
        "point": "朝晩の洗顔直後、手のひらに5円玉〜1円玉大を出し、両手で軽く温めてから顔全体に押し込むようにハンドプレスします。目元やほうれい線には指の腹でトントンと重ねづけするのがコツです。"
    },
    {
        "rank": 2,
        "tag": "🔬 国産サケ軟骨由来の高濃度処方！自社ラボ直販だから実現した圧倒的コスパの保水原液",
        "catch": "余分な成分を一切削ぎ落とした無添加設計。冬の敏感に傾いた角層へピュアな潤いをダイレクト補給",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "20ml (プロテオグリカンエッセンス PG)",
        "type": "国産高濃度プロテオグリカン原液美容液",
        "features": "北海道・青森産サケ鼻軟骨抽出プロテオグリカン、国内自社工場生産、7つの無添加処方（アルコール・パラベン・シリコン等不使用）",
        "value": "原料メーカー発信ならではのハイエンドな濃度と純度。中間マージンをカットした適正価格で、真冬の毎日ケアに惜しみなくたっぷり使える",
        "desc_p1": "冬のスキンケアにおいて『毎日ケチらずしっかり使えること』は、バリア機能を崩壊させないための決定的な要素です。KISOのプロテオグリカンエッセンスPGは、国産の新鮮なサケ鼻軟骨から丁寧に抽出されたプロテオグリカンを贅沢にボトルに詰めた純粋原液です。",
        "desc_p2": "とろみ付け剤や増粘剤などの余計な添加物を一切排除しているため、肌に乗せた瞬間の浸透スピードが際立っています。角層の水分を保持する糖タンパク質が細胞間を隙間なく埋め尽くし、乾いて硬化した角層を柔軟にほぐします。既存の化粧水や乳液に1〜2滴混ぜて使うカスタム美容液としても極めて扱いやすく、肌のコンディションに合わせて自由自在に保水力をブーストできます。",
        "target": "原液美容を惜しみなくたっぷり継続したい方、成分重視でシンプルなスキンケアを好む方、真冬に既存の化粧水の保湿力不足を感じている方",
        "point": "洗顔直後のブースターとして使用するほか、手のひらでいつもの化粧水に2〜3滴ブレンドして使うと、化粧水全体の保水持続時間が大幅に向上します。"
    },
    {
        "rank": 3,
        "tag": "🌿 自然派処方のパイオニアが届ける！防腐剤無添加で敏感肌にも優しいピュア保水エキス",
        "catch": "角層の水分保持能を底上げ。暖房でカサつく肌をふっくらキメの整ったシルク肌へと導く",
        "brand_name": "自然化粧品研究所",
        "capacity": "30ml (プロテオグリカン原液)",
        "type": "無添加プロテオグリカン美容原液",
        "features": "高純度水溶性プロテオグリカン、パラベン・フェノキシエタノール完全フリー、全成分シンプル処方",
        "value": "手作り化粧品原料としても長年信頼される品質。刺激に敏感な冬の肌に摩擦や刺激を与えず、純粋な保水力のみを角層へ送り届ける",
        "desc_p1": "冷たい風と室内暖房の寒暖差に晒され続けると、肌のバリア機能が低下し、普段は何ともない化粧品でもピリピリとした刺激を感じやすくなります。自然化粧品研究所のプロテオグリカン原液は、肌に負担をかけない徹底的な低刺激設計を貫いたピュアな保水原液です。",
        "desc_p2": "肌につけた瞬間はみずみずしく軽やかですが、角層深部に浸透するにつれて肌表面がしっとりと吸い付くような感触に変化します。プロテオグリカンが持つコラーゲンやヒアルロン酸の産生サポート特性により、使い続けるほどに肌のキメが整い、内側から自然なツヤが立ち上がります。敏感肌でも赤みやヒリつきを起こさず、穏やかに保湿力を底上げできる冬の守り神的存在です。",
        "target": "冬になると肌が敏感になって化粧品がしみる方、無香料・完全無添加の原液を探している方、素肌の透明感とキメ細かさを取り戻したい方",
        "point": "化粧水を塗布した直後、手のひらに3〜4滴取り、擦らずに顔全体を包み込むように優しくハンドプレスしてください。首元やデコルテまで伸ばすのがおすすめです。"
    },
    {
        "rank": 4,
        "tag": "❄️ あおもりPGブランド認証取得！弘前大学の先端研究が生んだ超高純度リフト保水原液",
        "catch": "特許抽出技術で分子構造を損なわずに抽出。冬の乾燥しぼみ肌にふっくらとしたハリを充填",
        "brand_name": "北海道ナチュラルバイオ",
        "capacity": "20ml (ピュアプロテオグリカン 100%原液)",
        "type": "高純度サケ鼻軟骨プロテオグリカン原液",
        "features": "あおもりPGブランド認証マーク取得、氷点下抽出技術、ヒアルロン酸産生サポート",
        "value": "学術研究から生まれた特許技術を用い、熱変性を起こさず生に近い状態で抽出。分子構造がしっかり保たれているため、高い水分保持力を誇る",
        "desc_p1": "プロテオグリカン研究の発祥地である青森県・弘前大学の抽出技術を受け継ぎ、高品質の証である『あおもりPG』ブランド認証を取得した本格派原液です。11月・12月の厳しい寒さの中で、乾燥によりボリュームを失った大人の肌に密度の高い潤いを与えます。",
        "desc_p2": "抽出工程で分子が壊れていないため、水分子を捕獲する能力が極めて高く、真冬の乾いた空気の中でも肌内部の水分蒸散を強力にブロックします。つけた直後から肌表面がキュッと引き締まるような心地よいハリ感を覚え、夕方になっても目元や頬の乾燥による凹凸が目立ちません。上質な美容成分を肌深くまで届けたいエイジングケア世代の冬の必需品です。",
        "target": "乾燥による肌のしぼみ・ハリ不足が気になる40代・50代以上の方、科学的エビデンスのある認証成分を選びたい方",
        "point": "洗顔後、化粧水の前にブースターとして使用します。手のひらの体温で10秒ほど温めてから、下から上へとリフトアップするように馴染ませると効果的です。"
    },
    {
        "rank": 5,
        "tag": "💧 高濃度プロテオグリカンが肌密度を高める！乾燥による毛穴の開きとキメの乱れを一網打尽",
        "catch": "水分を蓄えるタンクを角層内に築く。翌朝の肌がプルプルに生まれ変わる濃密原液",
        "brand_name": "NATUDOR (ナチュドール)",
        "capacity": "20ml (プロテオグリカン原液)",
        "type": "高濃度プロテオグリカン原液美容液",
        "features": "国産水溶性プロテオグリカン原液、無添加（鉱物油・香料・着色料フリー）、スポイトボトル採用",
        "value": "正確な量を衛生的に吸い上げられる遮光スポイト瓶を採用。乾燥が進行しやすい真冬の肌に、一定濃度の潤いをブレずに安定供給する",
        "desc_p1": "乾燥が進むと角層のキメが粗くなり、毛穴が縦に流れる『たるみ毛穴』が目立つようになります。ナチュドールのプロテオグリカン原液は、肌の土台に水分を蓄積させて角層細胞をふっくら膨らませることで、キメの隙間を押し戻すアプローチをとります。",
        "desc_p2": "使いやすいスポイトタイプで、1回の使用量を正確に調整可能。肌になじませるとサラリと浸透し、ベタつきを残さずに内側だけがモチモチと潤う独特の質感を実感できます。朝のメイク崩れ予防にも夜の集中保湿にも対応し、冬のエアコン環境下でも肌が乾きを感じる暇を与えません。",
        "target": "乾燥による開き毛穴やキメの粗さが目立つ方、スポイト式で衛生的に使いたい方、混合肌でテカリと乾燥が同居している方",
        "point": "1回あたりスポイト半分（約3〜4滴）を目安に、Tゾーンを避けて乾燥しやすいUゾーンから順になじませます。乾燥が気になる部分は指先でトントンと重ねます。"
    },
    {
        "rank": 6,
        "tag": "💰 驚異のプチプラで惜しみなく全身に使える！プロテオグリカン100%の乾燥肌救済ボトル",
        "catch": "顔だけでなく首やデコルテまでたっぷり。冬の乾燥全身ケアを圧倒的な低コストで実現",
        "brand_name": "JAPAN GALS (ジャパンギャルズ)",
        "capacity": "25ml (ピュアビューエッセンス プロテオグリカン原液 100%)",
        "type": "ピュアビュー原液シリーズ 美容液",
        "features": "水溶性プロテオグリカン100%、日本製、プチプラ大容量ボトル",
        "value": "1,000円前後の手頃な価格でありながら、しっかりとプロテオグリカン原液を配合。冬のスキンケア代を抑えながら本格保水ケアを継続できる",
        "desc_p1": "『高機能な原液を使いたいけれど、価格が高すぎてチビチビとしか使えない…』という悩みを打ち破るのがジャパンギャルズのピュアビューエッセンスです。惜しみなくたっぷり使える価格帯を実現し、真冬の全身乾燥対策にも威力を発揮します。",
        "desc_p2": "サラッとした水感覚のテクスチャーで、コットンパックのブースター液として使ったり、手持ちのボディミルクに数滴垂らして腕やすねの粉吹き対策に活用するのもおすすめ。プロテオグリカンが持つ優れた水分保持力が肌を健やかに整え、カサつきがちな冬の皮膚をしなやかに守ります。",
        "target": "プチプラでプロテオグリカンの効果を試してみたい方、顔だけでなく首やデコルテ・手肌まで惜しみなく原液ケアをしたい方",
        "point": "朝晩の洗顔後にたっぷり1スポイト分を顔から首筋まで一気に伸ばします。コットンに精製水と本品を含ませて3分間ローションパックをすると潤いが爆発的にチャージされます。"
    },
    {
        "rank": 7,
        "tag": "🌟 ヒアルロン酸超えのうるおい保水力！複合保湿成分とのブレンドで相乗効果を狙う高機能美容液",
        "catch": "プロテオグリカン原液にヒアルロン酸・コラーゲンを調合。多角的な水分チャージで乾き知らずへ",
        "brand_name": "クルード (CRUDO)",
        "capacity": "30ml (プロテオグリカン原液配合 美容液)",
        "type": "多機能プロテオグリカン高保水セラム",
        "features": "プロテオグリカン高配合、加水分解エラスチン、浸透型ヒアルロン酸、低分子コラーゲン複合配合",
        "value": "単一成分だけでは補いきれない真冬の複合的な肌悩みにアプローチ。プロテオグリカンを軸にサポート保湿成分を絶妙な比率で配合",
        "desc_p1": "冬の乾燥は、単なる水分不足だけでなく、エラスチンやコラーゲンの減少による弾力低下と連動しています。クルードのプロテオグリカン美容液は、高濃度プロテオグリカンに加え、エラスチンや低分子ヒアルロン酸を贅沢にブレンドした高機能セラムです。",
        "desc_p2": "肌に乗せると適度なとろみがあり、滑らかに伸びて肌表面に薄いうるおいヴェールを形成します。プロテオグリカンが角層深部を潤し、ヒアルロン酸が表面の蒸発を防ぐ多重構造によって、暖房が効いた過酷なオフィス環境でも夕方までみずみずしい肌をキープできます。",
        "target": "原液単品よりも複数のリッチな保湿成分を一度に取り入れたい方、とろみのある美容液のテクスチャーが好きな方",
        "point": "化粧水のあと、1〜2プッシュを手にとり顔全体に優しくなじませます。ほうれい線や眉間の乾燥シワには、指先で引き上げるように馴染ませてください。"
    },
    {
        "rank": 8,
        "tag": "🏯 青森県産あおもりPG高配合！ローション全体が美容液級の保水力を誇る贅沢化粧液",
        "catch": "バシャバシャ使えて角層をプロテオグリカンで満たす。真冬のゴワつき肌をほぐす高保湿化粧水",
        "brand_name": "ラヴィプレスト",
        "capacity": "150ml (あおもりPG 高保湿ローション)",
        "type": "プロテオグリカン高配合薬用級化粧水",
        "features": "あおもりPGブランド認証サケ鼻軟骨エキス、グリコシルトレハロース、植物性セラミド配合",
        "value": "美容液並みのプロテオグリカン濃度を150mlの大容量化粧水に凝縮。洗顔後のファーストステップで肌の水分タンクをMAXまで引き上げる",
        "desc_p1": "毎日の化粧水ステップそのものでプロテオグリカンを大量に補給したいという乾燥肌の願いを形にした高保湿ローションです。青森の清冽な自然環境と先進の抽出技術から生まれた『あおもりPG』をふんだんに配合しています。",
        "desc_p2": "とろみのあるリッチな感触ですが、肌に広げるとパシャッと弾けて素早く角層へ吸い込まれます。トレハロースや植物性セラミドとの相乗効果により、寒さで硬直した冬の角層を解きほぐし、後から使う美容液やクリームの浸透力も大幅に高めます。",
        "target": "美容液を何ステップも重ねるのが面倒な方、化粧水だけで圧倒的な保水力とハリ感を実感したい乾燥肌の方",
        "point": "洗顔後、500円玉大を手にとり、2回に分けて重ねづけします。1回目で肌全体をほぐし、2回目で手のひらで密着させることで角層水分量が倍増します。"
    },
    {
        "rank": 9,
        "tag": "🛡️ プロテオグリカン×濃密エモリエントバター！角層内部の水分を絶対に逃さない鉄壁クリーム",
        "catch": "水分と油分をミルフィーユ状に密閉。真冬の過酷な外気から素肌を保護し続ける高保湿シールド",
        "brand_name": "リッチモイスト",
        "capacity": "50g (プロテオグリカン リペア モイストクリーム)",
        "type": "高保水プロテオグリカン濃密保護クリーム",
        "features": "水溶性プロテオグリカン、シア脂、スクワラン、高精製ミツロウ、アルガンオイル",
        "value": "プロテオグリカンの強力な保水ネットワークを、上質な植物油ヴェールで完全に包み込み、12月の氷点下に近い冷気でも乾燥蒸散をゼロに抑え込む",
        "desc_p1": "どれだけ水溶性の保水成分を補給しても、最後にフタをする油分膜が不十分であれば、冬の乾燥外気によって水分は奪われてしまいます。リッチモイストのモイストクリームは、プロテオグリカンの保水力と天然エモリエントバターの密封力を融合させた冬用濃密クリームです。",
        "desc_p2": "こっくりとしたバターのような質感ながら、体温でとろけて滑らかに伸びます。肌表面に薄い保護シールドを形成し、外気の乾燥刺激や衣類の摩擦から素肌を物理的に保護。就寝前に厚めに塗るナイトパックとして活用すれば、翌朝の洗顔時に信じられないほど柔らかく吸い付くような肌に出会えます。",
        "target": "夜スキンケアしても朝起きると肌が乾いている方、頬や口周りの粉吹きが止まらない超乾燥肌・冬の砂漠肌",
        "point": "スキンケアの一番最後に、パール粒大を手のひらで温めてから、顔全体を包み込むようにハンドプレスします。特にカサつく部位には重ね塗りしてください。"
    },
    {
        "rank": 10,
        "tag": "🧖‍♀️ 毎日の集中保水で肌のバリアを立て直す！プロテオグリカン原液を染み込ませた贅沢シートマスク",
        "catch": "たった10分で角層の水分密度が満タンに。冷えと乾燥で疲弊した冬肌を蘇らせるデイリーマスク",
        "brand_name": "MITOMO (美友)",
        "capacity": "30枚入 (プロテオグリカン エッセンスマスク)",
        "type": "集中高保湿プロテオグリカンフェイスシートマスク",
        "features": "天然コットン100%シート、プロテオグリカンエキス高配合、ヒアルロン酸、アロエエキス",
        "value": "1枚あたり数十円という驚異のコストパフォーマンスで、サロン級のプロテオグリカンパックを毎日お風呂上がりに実践できる",
        "desc_p1": "冬の乾燥ダメージを蓄積させない秘訣は、毎日の入浴後すぐに集中的な水分密封ケアを行うことです。MITOMOのプロテオグリカンエッセンスマスクは、肌触りの良い天然コットンシートにたっぷりの美容液を含ませた大容量デイリーパックです。",
        "desc_p2": "シートが顔の凹凸にピタッと高密着し、蒸発を防ぎながらプロテオグリカンと保湿成分を角層深部までじっくり送り込みます。10〜15分置いて剥がした後の肌は、まるでエステ帰りのようにひんやりと引き締まり、キメがふっくらと立ち上がります。日々の乾燥リセットに最適です。",
        "target": "毎日シートマスクで手軽に集中保湿したい方、お風呂上がりの急激な乾燥突っ張りを防ぎたい方",
        "point": "入浴後、軽く化粧水で肌を整えた後に密着させます。10〜15分後に剥がし、肌の上に残った美容液を手のひらでハンドプレスして馴染ませ、すぐに乳液やクリームでフタをします。"
    }
]

# JSON-LD構造化データ作成
faq_data = [
    {
        "q": "プロテオグリカンとはどのような成分ですか？ヒアルロン酸との最大の違いは何ですか？",
        "a": "プロテオグリカンは、コアタンパク質にコンドロイチン硫酸などのグリコサミノグリカンが結合した高分子の糖タンパク質です。かつては1gあたり約3,000万円もする超希少成分でしたが、サケ鼻軟骨からの抽出技術確立によりスキンケアに広く活用されるようになりました。ヒアルロン酸と比較して約1.3倍の水分保持力を持つだけでなく、分子サイズが柔軟で角層深部へ浸透しやすい点、さらに肌のターンオーバーやハリをサポートするEGF様作用を持つ点が決定的な違いです。11月・12月の冬枯れ肌に最適です。"
    },
    {
        "q": "原液美容液はどの順番でスキンケアに組み込むのが一番効果的ですか？",
        "a": "プロテオグリカン原液は、基本的に『洗顔直後（化粧水の前）』のブースター先行美容液として取り入れるのが最も効果的です。分子構造がみずみずしく肌なじみが良いため、洗顔後の素肌に直接なじませることで角層の浸透ルートを整え、その後に使用する化粧水や乳液の水分保持効果を倍増させます。"
    },
    {
        "q": "敏感肌やアトピー肌でも冬の乾燥対策として使用できますか？",
        "a": "プロテオグリカンは体内にもともと存在する成分と同系統の生体成分であり、生体親和性が非常に高いため刺激性が極めて低いのが特徴です。無添加処方の原液であれば、冬の冷風や暖房でバリア機能が低下し、敏感に傾いた肌や粉吹き肌でも優しく使用できます。心配な場合は腕の内側で簡易パッチテストを行ってからの使用をおすすめします。"
    },
    {
        "q": "ビタミンCやレチノールなどの他の美容成分と併用しても大丈夫ですか？",
        "a": "併用して全く問題ありません。むしろ、冬場のレチノールや高濃度ビタミンCによる乾燥や皮むけなどのA反応・刺激感を、プロテオグリカンの高い保水力とバリアサポート作用が穏やかに包み込んで和らげてくれます。洗顔後→プロテオグリカン原液→化粧水→ビタミンC/レチノール→乳液・クリームの順序がベストです。"
    },
    {
        "q": "11月・12月の過酷な乾燥環境でプロテオグリカンの保湿効果を長持ちさせる秘訣は？",
        "a": "プロテオグリカンは角層内部で水分を強固に抱え込む『給水タンク』の役割を果たしますが、表面からの水分蒸発を防ぐ油膜シールドが欠かせません。プロテオグリカンで深部を満たした後は、必ずスクワランオイルや高純度ワセリン、シアバター、セラミドクリームなどの上質な油分を重ねて『水分抱え込み＋密閉シールド』の2重構造を完成させることが冬の乾燥撃退の鉄則です。"
    }
]

schema_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸超えの保水力で乾燥小ジワを撃退する高純度プロテオグリカン原液ランク10",
    "description": "11月・12月の冬の乾燥枯れ肌に！ヒアルロン酸の約1.3倍の保水力とEGF様作用で乾燥小ジワを撃退する高純度プロテオグリカン原液10選を徹底比較。フラコラ、KISO、自然化粧品研究所、あおもりPG認証原液など厳選。",
    "image": items[0]["img_url"],
    "datePublished": "2026-11-03T12:00:00+09:00",
    "dateModified": "2026-11-03T12:00:00+09:00",
    "author": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ 編集部",
        "url": "https://lumi-cosme.vercel.app/"
    },
    "publisher": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-proteoglycan"
    }
}

schema_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": it["rank"],
            "name": it["name"],
            "item": {
                "@type": "Product",
                "name": it["name"],
                "image": it["img_url"],
                "offers": {
                    "@type": "Offer",
                    "priceCurrency": "JPY",
                    "price": str(it["price"]),
                    "availability": "https://schema.org/InStock",
                    "url": it["affiliate_url"]
                }
            }
        } for it in items
    ]
}

schema_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f["a"]
            }
        } for f in faq_data
    ]
}

schema_breadcrumb = {
    "@context": "https://schema.org",
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
            "name": "高純度プロテオグリカン原液ランク10",
            "item": "https://lumi-cosme.vercel.app/winter-proteoglycan"
        }
    ]
}

# 商品カードHTML構築
items_html = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    price_str = f"¥{it['price']:,}" if it['price'] > 0 else "オープン価格"
    
    items_html += f"""
    <!-- Rank {p['rank']} -->
    <div class="product-card" id="rank-{p['rank']}">
      <div class="product-rank-badge">第{p['rank']}位</div>
      <div class="product-header">
        <span class="product-tag">{p['tag']}</span>
        <h3 class="product-title">{p['catch']}</h3>
        <div class="product-meta">
          <span class="product-brand">ブランド: {p['brand_name']}</span>
          <span class="product-capacity">規格・容量: {p['capacity']}</span>
          <span class="product-type">タイプ: {p['type']}</span>
        </div>
      </div>

      <div class="product-body">
        <div class="product-img-wrap">
          <img src="{it['img_url']}" alt="{it['name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-price-box">
            <span class="price-label">楽天市場参考価格:</span>
            <span class="price-val">{price_str}</span>
            <span class="price-tax">(税込・送料込目安)</span>
          </div>
          <div class="product-features">
            <strong>主成分・処方特徴:</strong> {p['features']}
          </div>
          <div class="product-value-point">
            <strong>冬の高保湿アプローチ:</strong> {p['value']}
          </div>
        </div>
      </div>

      <div class="product-desc">
        <p class="desc-lead">{p['desc_p1']}</p>
        <p class="desc-detail">{p['desc_p2']}</p>
      </div>

      <div class="product-advice-grid">
        <div class="advice-box target-box">
          <div class="advice-title">💡 こんな肌悩みの方に最適</div>
          <p>{p['target']}</p>
        </div>
        <div class="advice-box usage-box">
          <div class="advice-title">🧴 保湿効果を最大化する使用法</div>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-cta">
        <a href="{it['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener nofollow">
          楽天市場で詳細・最安値をチェック <span>→</span>
        </a>
      </div>
    </div>
    """

# 比較テーブル作成
table_rows = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    price_str = f"¥{it['price']:,}" if it['price'] > 0 else "オープン価格"
    table_rows += f"""
    <tr>
      <td class="tbl-rank">第{p['rank']}位</td>
      <td class="tbl-name"><a href="#rank-{p['rank']}">{p['brand_name']}<br><strong>{p['capacity']}</strong></a></td>
      <td class="tbl-type">{p['type']}</td>
      <td class="tbl-feat">{p['features']}</td>
      <td class="tbl-price">{price_str}</td>
    </tr>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！ヒアルロン酸超えの保水力で乾燥小ジワを撃退する高純度プロテオグリカン原液ランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の真冬乾燥に！ヒアルロン酸の約1.3倍の保水力とEGF様作用で乾燥小ジワを撃退する高純度プロテオグリカン原液10選を徹底比較！フラコラ、KISO、自然化粧品研究所、あおもりPG認証原液など厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-proteoglycan">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- OGP -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！ヒアルロン酸超えの保水力で乾燥小ジワを撃退する高純度プロテオグリカン原液ランク10 | 冬コスメ徹底比較ラボ">
  <meta property="og:description" content="11月・12月の真冬乾燥に！ヒアルロン酸の約1.3倍の保水力とEGF様作用で乾燥小ジワを撃退する高純度プロテオグリカン原液10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-proteoglycan">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta name="twitter:card" content="summary_large_image">

  <!-- JSON-LD 構造化データ -->
  <script type="application/ld+json">
  {json.dumps(schema_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_faq, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_breadcrumb, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #0284c7;
      --primary-light: #e0f2fe;
      --primary-dark: #0369a1;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --bg-light: #f8fafc;
      --border-color: #e2e8f0;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --card-hover-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text-main);
      background-color: #f1f5f9;
    }}

    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .header-inner {{
      max-width: 1000px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .container {{
      max-width: 900px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .article-wrap {{
      background: #ffffff;
      padding: 3rem 2.5rem;
      border-radius: 12px;
      box-shadow: var(--card-shadow);
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}

    .breadcrumb a {{
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .article-title {{
      font-size: 1.85rem;
      line-height: 1.4;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.5rem;
    }}

    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border-color);
    }}

    .lead-box {{
      background: #f0f9ff;
      border-left: 4px solid var(--primary);
      padding: 1.5rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 2.5rem;
      font-size: 1.05rem;
      line-height: 1.8;
    }}

    .section-title {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #0f172a;
      margin: 3rem 0 1.5rem 0;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 2rem;
      margin-bottom: 3rem;
      position: relative;
      box-shadow: var(--card-shadow);
      transition: box-shadow 0.2s ease;
    }}

    .product-card:hover {{
      box-shadow: var(--card-hover-shadow);
    }}

    .product-rank-badge {{
      position: absolute;
      top: -12px;
      left: 1.5rem;
      background: #0284c7;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.9rem;
      padding: 0.25rem 1rem;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(2, 132, 199, 0.3);
    }}

    .product-header {{
      margin-top: 0.5rem;
      margin-bottom: 1.25rem;
    }}

    .product-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      margin-bottom: 0.5rem;
    }}

    .product-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.5;
      margin-bottom: 0.5rem;
    }}

    .product-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .product-body {{
      display: grid;
      grid-template-columns: 220px 1fr;
      gap: 1.5rem;
      align-items: center;
      margin-bottom: 1.5rem;
      background: var(--bg-light);
      padding: 1.25rem;
      border-radius: 8px;
    }}

    @media (max-width: 640px) {{
      .product-body {{
        grid-template-columns: 1fr;
      }}
      .article-wrap {{
        padding: 1.5rem 1rem;
      }}
    }}

    .product-img-wrap {{
      text-align: center;
      background: #ffffff;
      padding: 0.5rem;
      border-radius: 8px;
      border: 1px solid var(--border-color);
    }}

    .product-img {{
      max-width: 100%;
      height: auto;
      max-height: 200px;
      object-fit: contain;
    }}

    .product-price-box {{
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px dashed var(--border-color);
    }}

    .price-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #b91c1c;
    }}

    .price-tax {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .product-features, .product-value-point {{
      font-size: 0.95rem;
      line-height: 1.6;
    }}

    .product-desc {{
      margin: 1.5rem 0;
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
    }}

    .desc-lead {{
      margin-bottom: 1rem;
      font-weight: 500;
    }}

    .product-advice-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }}

    @media (max-width: 640px) {{
      .product-advice-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .advice-box {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.9rem;
      line-height: 1.6;
    }}

    .target-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}

    .usage-box {{
      background: #fdf2f8;
      border: 1px solid #fbcfe8;
      color: #9d174d;
    }}

    .advice-title {{
      font-weight: 700;
      margin-bottom: 0.35rem;
    }}

    .product-cta {{
      text-align: center;
      margin-top: 1.5rem;
    }}

    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: #ffffff;
      font-weight: 700;
      font-size: 1rem;
      padding: 0.85rem 2rem;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 420px;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 12px -2px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #d60000, #aa0000);
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 2rem 0;
    }}

    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      background: #ffffff;
    }}

    .comparison-table th, .comparison-table td {{
      padding: 0.85rem 0.75rem;
      border: 1px solid var(--border-color);
      text-align: left;
    }}

    .comparison-table th {{
      background: #f8fafc;
      color: #0f172a;
      font-weight: 700;
      white-space: nowrap;
    }}

    .tbl-rank {{
      font-weight: 700;
      color: var(--primary-dark);
      white-space: nowrap;
      text-align: center;
    }}

    .tbl-name a {{
      color: #0f172a;
      text-decoration: none;
    }}

    .tbl-name a:hover {{
      color: var(--primary);
    }}

    .tbl-price {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin: 2rem 0;
    }}

    .faq-item {{
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1.25rem;
    }}

    .faq-q {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-weight: 700;
      font-size: 1rem;
      color: #0f172a;
      margin-bottom: 0.5rem;
    }}

    .faq-q-badge {{
      background: #0284c7;
      color: #ffffff;
      font-size: 0.8rem;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      flex-shrink: 0;
    }}

    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
      padding-left: 2rem;
    }}

    .internal-links-box {{
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 2rem;
      margin-top: 3rem;
    }}

    .internal-links-title {{
      font-size: 1.2rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 1.25rem;
      text-align: center;
    }}

    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 0.85rem;
    }}

    .internal-link {{
      display: block;
      background: #ffffff;
      border: 1px solid var(--border-color);
      padding: 0.75rem 1rem;
      border-radius: 6px;
      text-decoration: none;
      color: #334155;
      font-size: 0.9rem;
      font-weight: 500;
      transition: all 0.2s ease;
    }}

    .internal-link:hover {{
      border-color: #0284c7;
      color: #0284c7;
      transform: translateY(-2px);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }}

    .site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border-color);
      padding: 2.5rem 0;
      margin-top: 4rem;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <span style="font-size: 0.85rem; color: #64748b;">2026年最新 保湿ランキング</span>
    </div>
  </header>

  <main class="container">
    <article class="article-wrap">
      <div class="breadcrumb">
        <a href="/">ホーム</a> &gt; <span>高純度プロテオグリカン原液ランク10</span>
      </div>

      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！ヒアルロン酸超えの保水力で乾燥小ジワを撃退する高純度プロテオグリカン原液ランク10</h1>

      <div class="article-meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証カテゴリー: 高保水美容液・プロテオグリカン原液</span>
        <span>監修: 冬コスメ徹底比較ラボ 編集部</span>
      </div>

      <div class="lead-box">
        <strong>【11月・12月の冬本番に深刻化するインナードライ・乾燥小ジワを根本解決！】</strong><br>
        外気温が一桁台まで冷え込み、オフィスやリビングのエアコン暖房が終日稼働する11月〜12月。「どれだけ入念に化粧水を叩き込んでも、午後になると目元や口元がカピカピに乾く」「笑ったあとの表情ジワが戻りにくく粉を吹いてしまう」という深刻な肌のしぼみ乾燥に悩まされる方が一気に急増します。<br><br>
        冬の過酷な低湿度環境下では、一般的な保水成分では角層内部の水分を捕まえきれず、外気へと奪われてしまいます。そこでいま、美容医療界や先進皮膚科学で『ヒアルロン酸を超える驚異の水分保持力』として絶大な信頼を誇るのが<strong>『プロテオグリカン』</strong>です。<br><br>
        かつて1g3,000万円とも称された奇跡の高分子糖タンパク質であり、ヒアルロン酸の約1.3倍の保水力とEGF（上皮成長因子）様作用を併せ持ちます。角層の奥深くで乾ききった細胞間を隙間なく満たし、真冬の乾燥小ジワを跳ね返す、2026年最新の厳選10品を徹底比較・ランキング化しました。
      </div>

      <h2 class="section-title">🧬 プロテオグリカンが冬の過酷な乾燥枯れ肌を救う3大保水メカニズム</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>プロテオグリカンは、コアタンパク質に多数のコンドロイチン硫酸などの糖鎖が結合した巨大な分子構造を持ち、皮膚の真皮や軟骨組織に多く存在する生体成分です。冬の過酷な乾燥環境において、従来のヒアルロン酸やコラーゲンにはない以下の3つの決定的な強みを発揮します。</p>
        <ul style="margin: 1rem 0 1rem 1.5rem;">
          <li><strong>1. ヒアルロン酸の約1.3倍に及ぶ圧倒的な水分抱え込み力：</strong> スポンジ状の立体的な分子構造の中に大量の水分子を強固にトラップ。湿度が20%を下回る極度に乾燥した室内環境でも、一度捕まえた水分を外気へ逃しません。</li>
          <li><strong>2. EGF様作用による角層ターンオーバーとハリの再建：</strong> 加齢や冬の寒冷血行不良によって乱れがちなターンオーバーサイクルをサポート。コラーゲンやヒアルロン酸の生成を促し、乾燥で菲薄化・しぼんだ角層を内側から押し上げる弾力感を付与します。</li>
          <li><strong>3. サラリと浸透する高分子の生体親和性：</strong> 高保水成分特有のベタつきや皮膜感がなく、洗顔直後の素肌に驚くほどスッと馴染む浸透特性。後から重ねる化粧水や乳液の浸透ルートを切り拓き、スキンケア全体の保水効率を劇的に底上げします。</li>
        </ul>
      </div>

      <h2 class="section-title">🏆 高純度プロテオグリカン原液・高保水コスメおすすめランキング10選</h2>

      {items_html}

      <h2 class="section-title">📊 高純度プロテオグリカンコスメ10品 徹底スペック比較表</h2>
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名・容量</th>
              <th>種別・タイプ</th>
              <th>主成分・処方特徴</th>
              <th>参考価格</th>
            </tr>
          </thead>
          <tbody>
            {table_rows}
          </tbody>
        </table>
      </div>

      <h2 class="section-title">💡 11月・12月の冬本番にプロテオグリカンの効果を最大化する使用法</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>ヒアルロン酸超えの保水力を誇るプロテオグリカンですが、冬の気候特性に合わせた正しいステップを踏むことで、その真価を120%引き出すことができます。</p>
        <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; margin-top: 1rem;">
          <h3 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: #0284c7;">① 洗顔直後、素肌の『ファーストステップ』で投入する</h3>
          <p>冬のお風呂上がりや洗顔直後は、急激な水分蒸発が始まります。タオルで水分を押さえた直後の無垢な肌に、まずプロテオグリカン原液をなじませてください。角層深部に水分タンクの土台を築くことで、その後の化粧水が驚くほどスムーズに吸い込まれます。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #0284c7;">② 手のひらの体温でじっくりハンドプレス</h3>
          <p>冬の冷たい手でパッティングすると角層が刺激され赤みの原因になります。手のひらで原液を人肌程度に温めてから、顔全体を包み込むように10秒間優しくプレス。体温によって浸透性が一段と向上します。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #0284c7;">③ 仕上げは必ず油分ヴェールで密閉する</h3>
          <p>プロテオグリカンが深部を潤した後は、高保湿乳液やセラミドクリーム、スクワランオイルなどの油分で必ずフタをしてください。「深部の強力保水＋表面の油膜シールド」が組み合わさることで、真冬のエアコン乾燥でも一日中モチモチの肌が持続します。</p>
        </div>
      </div>

      <h2 class="section-title">❓ 専門家が答える！プロテオグリカンコスメのよくある質問</h2>
      <div class="faq-list">
        {"".join([f'''
        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-badge">Q</span>
            <span>{f["q"]}</span>
          </div>
          <div class="faq-a">{f["a"]}</div>
        </div>
        ''' for f in faq_data])}
      </div>

      <div class="internal-links-box">
        <h3 class="internal-links-title">🔗 あわせて読みたい冬の高保湿スキンケア・コスメ特集</h3>
        <div class="internal-links-grid">
          <a href="/winter-heparinoid" class="internal-link">🩺 薬用ヘパリン類似物質コスメ10選</a>
          <a href="/winter-placenta" class="internal-link">✨ 高濃度プラセンタ原液10選</a>
          <a href="/winter-vaseline" class="internal-link">🛡️ 高純度ワセリン高保湿10選</a>
          <a href="/winter-ceramide-lotion" class="internal-link">🧴 高保湿セラミド化粧水10選</a>
          <a href="/winter-ceramide-cream" class="internal-link">🧴 高保湿セラミドクリーム10選</a>
          <a href="/winter-rice-power" class="internal-link">🌾 米発酵・ライスパワー高保湿10選</a>
          <a href="/winter-amino-acid" class="internal-link">💧 高浸透アミノ酸コスメ10選</a>
          <a href="/winter-squalane-oil" class="internal-link">✨ 高純度スクワランオイル10選</a>
          <a href="/winter-argan-oil" class="internal-link">🥑 高保湿アルガンオイル10選</a>
          <a href="/winter-panthenol-cream" class="internal-link">🧪 高保湿パンテノールクリーム10選</a>
          <a href="/winter-horse-oil" class="internal-link">🐴 高保湿馬油クリーム10選</a>
          <a href="/winter-shea-butter" class="internal-link">🧈 高保湿シアバター10選</a>
          <a href="/winter-urea-cream" class="internal-link">🦶 高保湿尿素クリーム10選</a>
          <a href="/winter-medicinal-lip" class="internal-link">💄 高保湿薬用リップクリーム10選</a>
          <a href="/winter-peptide-serum" class="internal-link">🧬 高保湿ペプチド美容液10選</a>
        </div>
      </div>

    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved.</p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #94a3b8;">当サイトは楽天市場アフィリエイトプログラムに参加しており、適格販売により収入を得ています。</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-proteoglycan.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-proteoglycan.html!")
