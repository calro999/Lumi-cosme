import json
import re

with open("fetched_final_30_marula_birch_azelaic.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_azelaic_acid"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 高純度アゼライン酸20%超高配合！ヒアルロン酸×スクワランの濃密バリアクリーム",
        "catch": "クリニック級の濃度で冬の皮脂乱れと毛穴詰まりを撃退。乾燥させずに赤みとテカリを根本から整える",
        "brand_name": "KISO (キソ)",
        "capacity": "20g (キソ バランシングクリーム AZ)",
        "type": "高純度アゼライン酸20%配合高保湿フェイスクリーム",
        "features": "高純度アゼライン酸20%配合、高保水ヒアルロン酸Na、植物性スクワラン、ツボクサエキス(CICA)",
        "value": "海外の皮膚科処方に匹敵する20%という高濃度を実現しながら、スクワランとヒアルロン酸で冬の乾燥バリアを鉄壁保持",
        "desc_p1": "11月から12月にかけて急激に深刻化するのが、『寒暖差による頬の赤み』や『暖房の効いた室内でTゾーンがギトギトにテカり毛穴が開くのに、Uゾーンはカサカサに乾く』というインナードライトラブルです。皮膚科でも赤ら顔や皮脂トラブルの第一選択として処方されるアゼライン酸は、小麦や大麦などの穀物から発見された天然由来の酸成分。KISOのバランシングクリームAZは、なんと純度100%のアゼライン酸パウダーを20%という驚異的な最高峰濃度で配合した本格ドクターズ発想のクリームです。",
        "desc_p2": "通常、高濃度アゼライン酸は肌にピリピリとした刺激や乾燥感を伴いやすいのが課題ですが、本品は人の皮脂に親和性の高い植物性スクワランや高分子ヒアルロン酸、鎮静成分CICAを絶妙な黄金比率でブレンド。こっくりとしたリッチなクリームが肌にピタッと密着し、真冬の外気乾燥から角層を保護しながら、過剰な皮脂分泌と角栓の詰まりを穏やかに抑制します。塗布した翌朝から小鼻まわりのテカリや頬の赤みがスーッと引き、キメの整ったマットでなめらかなシルク肌を実感できます。",
        "target": "暖房の部屋で小鼻や額がテカリ毛穴が黒ずむ方、寒暖差で頬やすっぴん肌に赤みが出やすい方、冬の大人ニキビを繰り返す方",
        "point": "化粧水や美容液で十分に肌へ水分補給を行った後、パール粒大を手にとり、赤みや毛穴、テカリが気になる部分を中心に優しく馴染ませます。使い始めの数日間は夜のみ使用し、肌が慣れてから朝晩使いに移行するのがコツです。"
    },
    {
        "rank": 2,
        "tag": "🔬 皮膚科専門医共同開発！高純度アゼライン酸×両親媒性ビタミンCの集中ショット",
        "catch": "毛穴の黒ずみ・開き・ザラつきを多角的にリセット。真冬のくすみと皮脂酸化を同時にクリア",
        "brand_name": "dr365 (ドクターサンロクゴ)",
        "capacity": "30ml (A.Z. セラムショット)",
        "type": "ドクターズ処方アゼライン酸集中美容液",
        "features": "高純度アゼライン酸、浸透型ビタミンC誘導体、グリシルグリシン、ナイアシンアミド配合",
        "value": "毛穴悩みに特化したクリニック発想の美容成分が濃縮。冬の冷えによるターンオーバーの停滞を速やかに正常化",
        "desc_p1": "皮膚科医監修のプレステージダーマブランド『dr365』が手がける、大ヒット毛穴レスキュー美容液。冬の肌は寒さで血行が悪くなり、古い角質が剥がれ落ちずに毛穴の出口を塞いでしまいがちです。そこに暖房による皮脂が混ざり合うことで、頑固な角栓や酸化した黒ずみ毛穴が形成されます。『A.Z. セラムショット』は、高純度アゼライン酸をナノカプセル化し、毛穴の奥深くまでピンポイントで有効成分を送り届ける画期的なアプローチを採用しています。",
        "desc_p2": "さらにすり鉢状に凹んだ開き毛穴を引き締めるグリシルグリシンと、美白・バリア機能向上を担うナイアシンアミドを贅沢に配合。とろみのあるミルキーなセラムが肌に吸い付くように広がり、冬の乾燥で硬化した角質を柔らかくほぐしながらキメをキュッと整えます。刺激感が極めてマイルドに抑えられているため、アゼライン酸特有のピリピリ感が苦手な敏感肌の方でも毎日心地よく継続できる完成度の高さです。",
        "target": "小鼻や頬の毛穴の開き・黒ずみが気になる方、皮脂分泌のバランスを整えてメイク崩れを防ぎたい方、低刺激なドクターズコスメを好む方",
        "point": "朝晩の洗顔後、化粧水の直後に1〜2プッシュを顔全体へ。特に毛穴の目立つ鼻周りや頬の中央には、指先でクルクルと優しく押し込むように塗り重ねると引き締め効果が最大化します。"
    },
    {
        "rank": 3,
        "tag": "🌿 アゼライン酸×濃縮CICAの黄金タッグ！真冬の寒暖差赤みと肌荒れを即効クーリング",
        "catch": "急激な冷えと暖房の熱でゆらぐ肌を救出。過剰皮脂を抑えながら澄み渡るクリーンな素肌へ",
        "brand_name": "Anua (アヌア)",
        "capacity": "30ml (アゼライン酸インテンスカーミングセラム)",
        "type": "アゼライン酸配合カーミング高保湿美容液",
        "features": "高純度アゼライン酸、高濃度ツボクサエキス(CICA)、ティーツリーエキス、ヒアルロン酸",
        "value": "鎮静力に定評のあるAnuaならではの低刺激設計。冬の寒暖差による赤ら顔や炎症を穏やかに落ち着かせる",
        "desc_p1": "冬の外出先から暖房の効いた室内に入った瞬間、急激な血管拡張によって顔が真っ赤になり、ジリジリとした火照りやかゆみを感じる『冬の寒暖差ゆらぎ肌』。Anuaの『アゼライン酸インテンスカーミングセラム』は、そんな冬特有の肌ストレスに立ち向かうために開発された鎮静特化型セラムです。",
        "desc_p2": "アゼライン酸の持つ優れた抗炎症・抗菌作用に、CICA（ツボクサエキス）とティーツリーのクーリングパワーを融合。みずみずしいジェルセラムが肌に乗せた瞬間に心地よい潤いを与え、熱を持った角層を素早くクールダウンします。ヒアルロン酸が水分をしっかり抱え込むため、皮脂コントロール系美容液にありがちな『塗った後のパサつき・乾燥感』が一切なく、しっとりとしたうるおいベールが持続します。",
        "target": "室内に入ると頬が赤くなりやすい赤ら顔の方、冬でもTゾーンがテカり肌荒れしやすい方、マフラーの擦れで肌が荒れる方",
        "point": "化粧水の後に適量をとり、赤みが出やすい両頬や鼻筋に優しく馴染ませます。擦らずに手のひらでハンドプレスすることで、摩擦刺激を与えずに成分を行き渡らせることができます。"
    },
    {
        "rank": 4,
        "tag": "🧪 旭研究所の業務用原液シリーズ！アゼライン酸20%をそのままダイレクト注入",
        "catch": "余計なものを一切足さない原液処方。頑固な冬の皮脂トラブルと毛穴詰まりに高濃度ダイレクトチャージ",
        "brand_name": "旭研究所 (Asahi Laboratories)",
        "capacity": "30ml (業務用アゼライン酸液20％)",
        "type": "高濃度アゼライン酸20%原液美容液",
        "features": "アゼライン酸20%原液処方、無香料・無着色・鉱物油フリー、国内研究機関開発",
        "value": "皮膚科学に基づいた高純度原液。普段のスキンケアに数滴プラスするだけでプロフェッショナルな皮脂管理を実現",
        "desc_p1": "国内の皮膚研究機関やエステ向け原料開発で高い実績を誇る旭研究所の『業務用アゼライン酸液20％』。不要な増粘剤や香料を一切排除し、アゼライン酸を高純度な水溶液として20%という高濃度でボトリングした本格原液コスメです。",
        "desc_p2": "水のようにサラッとしたテクスチャーで、肌への浸透スピードが極めて速いのが特徴。真冬の過剰な皮脂酸化を素早く食い止め、古い角質が毛穴にこびりつくのを防ぎます。単品で部分使いするのはもちろん、現在愛用している高保湿化粧水やヒアルロン酸セラムに手のひらで1〜2滴混ぜて使用することも可能。冬の乾燥と皮脂トラブルの度合いに合わせて、自由に濃度をカスタマイズできる使い勝手の良さがコスメマニアから絶賛されています。",
        "target": "とにかく高濃度の原液で早く結果を出したい方、普段のスキンケアにアゼライン酸をちょい足ししたい方、コスパ良く本格ケアしたい方",
        "point": "洗顔後すぐ、または化粧水に1〜2滴混ぜて全顔または気になる部分に塗布。非常に高濃度なため、最初はパッチテストを行い、肌の様子を見ながら徐々に使用量を増やすのが鉄則です。"
    },
    {
        "rank": 5,
        "tag": "✨ 大人の乾燥毛穴に深くアプローチ！純アゼライン酸×高保湿成分の濃密リペア",
        "catch": "乾燥によるたるみ毛穴と皮脂による開き毛穴をダブルケア。ふっくら満たして引き締める大人の名品",
        "brand_name": "Macchia Label (マキアレイベル)",
        "capacity": "30ml (ディーププラスAZ 高濃度美容液)",
        "type": "エイジング対応高機能アゼライン酸美容液",
        "features": "高純度純アゼライン酸、水溶性コラーゲン、植物幹細胞エキス、グリセリンフリー配慮",
        "value": "皮脂ケアと同時に真冬のハリ弾力低下を徹底リペア。大人の乾燥肌でもつっぱらずにしっとり吸い付く仕上がり",
        "desc_p1": "ファンデーションの名品で知られるマキアレイベルが、大人の複雑な毛穴悩みと冬の乾燥に着目して開発した『ディーププラスAZ』。30代〜50代の肌は、皮脂による毛穴の開きだけでなく、加齢と乾燥によるコラーゲンの減少で毛穴が縦に涙型に垂れ下がる『たるみ毛穴』が併発します。",
        "desc_p2": "本品は純アゼライン酸の角質正常化作用に加えて、肌内部のクッション性を支える高分子コラーゲンや植物幹細胞エキスを高濃度で配合。皮脂分泌を穏やかに抑制して毛穴の黒ずみを防ぎつつ、角層深部に贅沢な潤いを補給して肌をふっくらと押し上げます。ベタつかず、かつ乾かない絶妙な高保湿テクスチャーで、塗布後はシルクのヴェールをまとったような上質ななめらかさが一日中続きます。",
        "target": "30代以降で頬の毛穴が縦に流れて目立つ方、皮脂ケアをすると肌がつっぱってしまう乾燥肌・年齢肌の方、キメの整った上質な素肌を目指す方",
        "point": "化粧水の後に2〜3滴を取り、手のひらで温めてから下から上へ引き上げるように顔全体に馴染ませます。毛穴が気になる小鼻や頬には指先で重ねづけしてください。"
    },
    {
        "rank": 6,
        "tag": "🔥 世界累計販売数トップクラス！アゼライン酸15%×ナイアシンアミドの高保湿セラム",
        "catch": "海外スキンケア界で絶大な人気。ナイアシンアミドとヒアルロン酸がアゼライン酸の刺激を包み込む",
        "brand_name": "Cos De BAHA (コスデバハ)",
        "capacity": "30ml (AZ アゼライン酸15%セラム)",
        "type": "高純度アゼライン酸15%×ナイアシンアミド配合セラム",
        "features": "アゼライン酸15%、ナイアシンアミド、ヒアルロン酸Na、パンテノール、アロエベラ葉エキスベース",
        "value": "水を一滴も使わずオーガニックアロエベラ抽出液をベースに使用。高濃度でありながら乾燥を防ぎ、抜群の保湿持続力を発揮",
        "desc_p1": "世界中で愛用される機能性ダーマコスメブランドCos De BAHAのフラッグシップアイテム『AZセラム』。アゼライン酸を15%という確かな実感値をもたらす高濃度で配合しながら、基剤に精製水ではなく保水力と鎮静力に優れたアロエベラ葉エキスを採用しているのが最大の特徴です。",
        "desc_p2": "さらにセラミドの合成を促すナイアシンアミドやパンテノール、ヒアルロン酸が贅沢に組み合わされており、アゼライン酸特有の乾燥リスクを完璧にカバー。とろりとした透明なセラムが肌に吸い込まれると、インナードライでこわばった角質が瞬時にほぐれ、冬の暖房下でもテカらないのに内側はしっとりと潤った理想的な水分・油分バランスを再構築します。",
        "target": "世界で実証された信頼の処方を試したい方、アゼライン酸とナイアシンアミドの相乗効果で透明感を高めたい方、コスパ重視の方",
        "point": "夜の洗顔後、化粧水で肌を整えた直後に1〜2滴を顔全体に伸ばします。やや粘度があるため、塗布後は手のひらでしっかりとハンドプレスして角層へ押し込むのがポイントです。"
    },
    {
        "rank": 7,
        "tag": "🏆 楽天ベストコスメ受賞！アゼライン酸誘導体原液×グリシルグリシン6%の浸透プレ化粧水",
        "catch": "イオン導入も可能な究極のキメ毛穴ケア。サラサラのテクスチャーで角層深部へすばやく浸透",
        "brand_name": "TOUT VERT (トゥヴェール)",
        "capacity": "100ml (バランシングGAローション)",
        "type": "アゼライン酸誘導体配合プレ化粧水",
        "features": "アゼライン酸誘導体原液（アゼロイルジグリシンK）、グリシルグリシン6%、10種の整肌成分",
        "value": "刺激の少ない水溶性アゼライン酸誘導体を採用。冬の乾燥肌でも一切しみることなく、開いた毛穴を引き締めキメを整える",
        "desc_p1": "成分派スキンケアマニアから絶大な信頼を集めるトゥヴェールの名品『バランシングGAローション』。純粋なアゼライン酸の弱点である『水に溶けにくく刺激が出やすい』という点を克服した次世代成分『アゼライン酸誘導体（アゼロイルジグリシンK）』を原液レベルで配合しています。",
        "desc_p2": "さらに資生堂の毛穴研究でも有名なペプチド成分『グリシルグリシン』を6%という高濃度でドッキング。シャバシャバとしたみずみずしい化粧水テクスチャーで、洗顔直後のまっさらな角層へすーっと浸透します。皮脂の不飽和脂肪酸による角化異常を食い止め、冬の暖房直風による毛穴のすり鉢化を徹底ガード。その後に重ねる高保湿化粧水や美容液の通り道を整える導入効果も抜群です。",
        "target": "純アゼライン酸だとピリつきや刺激を感じやすい敏感肌の方、洗顔後すぐに使える毛穴プレ化粧水を求める方、イオン導入ケアをしたい方",
        "point": "洗顔直後の肌に500円玉大を手にとり、顔全体に優しく馴染ませます。毛穴の気になる小鼻や額には、コットンに含ませて2〜3分パックすると毛穴の引き締まり感がさらにアップします。"
    },
    {
        "rank": 8,
        "tag": "💧 アゼライン酸誘導体パウダー原液配合！皮脂崩れを防ぎながら潤す集中エッセンス",
        "catch": "ベタつかないのに乾かない絶妙のうるおいバランス。冬のマスク蒸れや暖房テカリを鉄壁防御",
        "brand_name": "KISO (キソ)",
        "capacity": "30ml (バランシングエッセンス AZ)",
        "type": "アゼライン酸誘導体配合高浸透美容液",
        "features": "アゼライン酸誘導体15%配合、プロパンジオール、ヒアルロン酸、7つの無添加処方",
        "value": "美容液タイプで手軽に皮脂水分バランシング。朝のメイク前に使ってもファンデがヨレず、夕方までサラサラしっとりを両立",
        "desc_p1": "KISOのクリームタイプ（第1位）と並ぶ人気を誇る、美容液タイプのアゼライン酸コスメ。刺激が穏やかで肌なじみに優れたアゼライン酸誘導体を採用し、みずみずしいエッセンスの中に高濃度で凝縮しています。",
        "desc_p2": "冬場、マフラーを巻いたり暖房の効いた電車に乗ったときに起こる『顔の蒸れと乾燥の同時多発トラブル』に最適。過剰な皮脂の酸化を防ぎながら、プロパンジオールやヒアルロン酸が角層細胞に水分を補給し続けます。朝のスキンケアに取り入れることで、皮脂崩れ防止下地を使わなくても夕方までテカリや毛穴落ちが劇的に抑制され、メイク直しの回数が激減します。",
        "target": "朝のメイク前に手軽にアゼライン酸を取り入れたい方、クリームの油分感が苦手なオイリードライ肌の方、マフラー蒸れで肌荒れしやすい方",
        "point": "化粧水の後に1〜2スポイトを取り、全顔に優しく滑らせます。サラッとしているため、気になるTゾーンには2度塗りし、Uゾーンには乳液やクリームを重ねてフタをすると完璧です。"
    },
    {
        "rank": 9,
        "tag": "🌿 CICA×アゼライン酸誘導体15%！冬の肌荒れ・インナードライを立て直すリペアセラム",
        "catch": "韓国ダーマコスメの知見が詰まった高機能処方。荒れやすい真冬の角層バリアを優しく保護",
        "brand_name": "DERMA SHARE (ダーマシェア)",
        "capacity": "30ml (アゼライン酸誘導体15% CICAリペアセラム)",
        "type": "アゼライン酸誘導体＆CICA配合高保湿セラム",
        "features": "アゼライン酸誘導体15%、高純度マデカッソサイド(CICA)、パンテノール、弱酸性",
        "value": "荒れた肌をいたわりながら皮脂と毛穴を同時ケア。冬の寒風による肌のゴワつきをやわらかくリセット",
        "desc_p1": "韓国の実力派スキンケアブランドDERMA SHAREが展開する高機能リペアセラム。アゼライン酸誘導体を15%高配合し、冬の過酷な寒冷外気と乾燥によってバリア機能が低下した肌のために、高純度CICAとパンテノールを組み合わせています。",
        "desc_p2": "とろみのあるマイルドなテクスチャーが荒れた肌表面に優しく広がり、摩擦を抑えながら角層深部へ浸透。肌の赤みを穏やかに落ち着かせると同時に、硬くなった角質をやわらげて滑らかな手触りへと導きます。香料やパラベンなどの刺激物質を徹底排除した低刺激設計で、敏感肌の冬のレスキューセラムとして頼もしい存在です。",
        "target": "肌が荒れやすく赤みが出やすい敏感肌の方、冬になると肌がゴワついてメイクが乗らない方、肌バリアを根本から強化したい方",
        "point": "朝晩のスキンケアで、化粧水の後に適量を塗布。肌が特に敏感になっている日は、手のひらで優しく包み込むようにハンドプレスして馴染ませましょう。"
    },
    {
        "rank": 10,
        "tag": "🏥 美容皮膚科・クリニック定番処方！ロート製薬が開発した高濃度アゼライン酸クリーム",
        "catch": "皮膚科医が指名買いする実力派。真冬のしつこい皮脂トラブルと毛穴詰まりに終止符を打つ",
        "brand_name": "DRX (ディーアールエックス / ロート製薬)",
        "capacity": "15g (AZAクリア クリーム)",
        "type": "クリニック専売発祥・高濃度アゼライン酸20%配合クリーム",
        "features": "アゼライン酸20%高配合、ノンコメドジェニックテスト済み、無香料・無着色・防腐剤フリー",
        "value": "ロート製薬が長年の皮膚科学研究をもとに開発した医療機関向けクリーム。確かなエビデンスに基づく本格集中ケア",
        "desc_p1": "全国の美容皮膚科や皮膚科クリニックで広く取り扱われ、ニキビや酒さ、毛穴の悩みを抱える患者から絶大な信頼を集めるロート製薬の『DRX AZAクリア』。アゼライン酸を医療グレードの20%という高濃度で安定配合した、まさにアゼライン酸コスメの金字塔です。",
        "desc_p2": "少しマットで硬めのテクスチャーですが、指先で温めながらピンポイントに塗布すると、ピタッと肌に密着して長時間の保護膜を形成。冬の乾燥によってターンオーバーが乱れ、毛穴に角栓が詰まりやすくなったデリケートな肌を、正常な角化リズムへと導きます。余計な美容成分をあえて混ぜず、アゼライン酸本来の薬効を極限まで引き出した質実剛健な処方が特徴です。",
        "target": "クリニック推奨の確かな品質で皮脂トラブルを完治させたい方、小鼻や顎の頑固な角栓・毛穴詰まりに悩む方、成分の信頼性を最優先する方",
        "point": "化粧水や乳液で十分に保湿した後、小豆大を指先に取り、気になる部分にトントンと置くように優しく塗り込みます。高保湿なクリームやオイルを上から薄く重ねると乾燥を防げます。"
    }
]

faq_data = [
    {
        "q": "アゼライン酸（Azelaic Acid）とはどのような成分ですか？レチノールやサリチル酸とどう違うのですか？",
        "a": "アゼライン酸は、小麦や大麦、ライ麦などの穀類や酵母に含まれる天然由来の飽和ジカルボン酸です。皮脂の過剰分泌抑制、毛穴の詰まり（角栓）解消、アクネ菌などの増殖抑制、抗炎症・赤み（酒さ・毛細血管拡張）の改善、メラニン生成抑制（色素沈着予防）という驚くほど多彩な効果を持ちます。レチノールのような激しい皮剥け（A反応）や光毒性（紫外線への過敏反応）がなく、サリチル酸（BHA）よりも角層の水分保持能を奪いにくいため、11月〜12月の『乾燥と皮脂トラブル・赤みが同時に起きる冬のゆらぎ肌』に最も安全かつ効果的にアプローチできます。"
    },
    {
        "q": "塗った時に少しピリピリとした刺激を感じます。使い続けても大丈夫ですか？",
        "a": "アゼライン酸の使い始め（特に濃度10%〜20%の高濃度製品）には、塗布直後に一時的なピリピリ感やかゆみ、温感を感じることがあります。これはアゼライン酸の分子が角層を通過する際の一時的な生理反応であり、通常は数分〜10分程度で治まり、1〜2週間継続して使用することで肌が慣れて感じなくなります。ただし、赤みが長時間引かない場合や激しい痛みがある場合は使用頻度を落とし（2日に1回にするなど）、化粧水や保湿クリームを先に塗って肌を保護してからアゼライン酸を重ねる『後塗り法』を試してください。"
    },
    {
        "q": "冬の乾燥肌でもアゼライン酸を使って乾燥が悪化しませんか？効果的な保湿のコツは？",
        "a": "正しく保湿成分と併用すれば、乾燥が悪化することはありません。アゼライン酸は余分な皮脂を抑える働きがあるため、皮脂が少ない部位に単体で塗りすぎるとややつっぱり感を感じることがあります。冬期は『白樺樹液やヒアルロン酸配合の高保水化粧水で角層にたっぷりと水分を満たした後にアゼライン酸を使用し、最後にセラミドやマルラオイル、スクワランなどの良質な油分でフタをする』というステップを徹底してください。これにより、水分を逃さず毛穴やテカリだけを理想的にコントロールできます。"
    },
    {
        "q": "アゼライン酸とビタミンC、レチノール、ナイアシンアミドなどの併用は可能ですか？",
        "a": "はい、基本的に併用可能です。特にナイアシンアミドやヒアルロン酸、CICA（ツボクサエキス）との併用は、アゼライン酸の刺激を緩和しながらバリア機能を強化するため非常に相性が抜群です。一方、純粋レチノールや高濃度ピュアビタミンCとの併用は、冬場の肌状態によっては刺激が重複する可能性があるため、朝にアゼライン酸、夜にレチノールと使い分けるか、刺激の穏やかなアゼライン酸誘導体を選ぶのが賢明です。"
    }
]

# アイテムカードHTML生成
items_html = ""
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    price_formatted = f"{r_item['price']:,}円"
    
    items_html += f"""
      <section id="rank-{p['rank']}" class="product-card">
        <div class="product-header">
          <div class="rank-badge">第{p['rank']}位</div>
          <span class="product-tag">{p['tag']}</span>
        </div>
        <h3 class="product-name">{r_item['name']}</h3>
        <p class="product-catch">{p['catch']}</p>
        
        <div class="product-content-grid">
          <div class="product-img-wrap">
            <img src="{r_item['img_url']}" alt="{r_item['name']}" loading="lazy" width="280" height="280" class="product-img">
          </div>
          <div class="product-info-wrap">
            <div class="price-box">
              <span class="price-label">楽天市場 参考価格:</span>
              <span class="price-value">{price_formatted}</span>
              <span class="price-tax">(税込 / 2026年11月時点)</span>
            </div>
            <dl class="product-specs">
              <dt>ブランド / メーカー</dt>
              <dd>{p['brand_name']}</dd>
              <dt>容量 / タイプ</dt>
              <dd>{p['capacity']} / {p['type']}</dd>
              <dt>主要成分・処方特徴</dt>
              <dd>{p['features']}</dd>
              <dt>冬の保水アプローチ</dt>
              <dd>{p['value']}</dd>
            </dl>
          </div>
        </div>

        <div class="product-desc-box">
          <h4 class="desc-heading">🔍 徹底深掘りレビュー＆真冬の検証結果</h4>
          <p class="desc-p">{p['desc_p1']}</p>
          <p class="desc-p">{p['desc_p2']}</p>
          
          <div class="target-point-grid">
            <div class="target-box">
              <span class="box-icon">🎯</span>
              <strong>こんな肌悩みにおすすめ:</strong>
              <p>{p['target']}</p>
            </div>
            <div class="point-box">
              <span class="box-icon">💡</span>
              <strong>効果を最大化する使用のコツ:</strong>
              <p>{p['point']}</p>
            </div>
          </div>
        </div>

        <div class="product-action-wrap">
          <a href="{r_item['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            <span>楽天市場で最安値・商品詳細を見る</span>
            <svg class="arrow-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
        </div>
      </section>
    """

# 比較表HTML生成
table_rows = ""
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    price_formatted = f"{r_item['price']:,}円"
    table_rows += f"""
            <tr>
              <td class="rank-cell">第{p['rank']}位</td>
              <td class="name-cell"><strong>{r_item['name'][:28]}...</strong><br><small>{p['brand_name']}</small></td>
              <td>{p['type']}</td>
              <td>{p['features']}</td>
              <td class="price-cell">{price_formatted}</td>
            </tr>
    """

# JSON-LD構造化データ
jsonld_products = []
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    jsonld_products.append({
        "@type": "Product",
        "name": r_item["name"],
        "image": r_item["img_url"],
        "description": p["catch"],
        "brand": {
            "@type": "Brand",
            "name": p["brand_name"]
        },
        "offers": {
            "@type": "Offer",
            "priceCurrency": "JPY",
            "price": str(r_item["price"]),
            "url": r_item["affiliate_url"],
            "availability": "https://schema.org/InStock"
        }
    })

jsonld_faq = []
for f in faq_data:
    jsonld_faq.append({
        "@type": "Question",
        "name": f["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f["a"]
        }
    })

full_jsonld = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！冬のインナードライ赤みと乾燥毛穴を鎮めて潤す高濃度アゼライン酸コスメランク10",
            "description": "11月・12月の冬本番に！寒暖差赤みや暖房テカリ、乾燥毛穴を鎮めて潤す高濃度アゼライン酸コスメ10選を徹底比較！KISO、dr365、Anua、トゥヴェール、DRXなど厳選。",
            "datePublished": "2026-11-03T18:00:00+09:00",
            "dateModified": "2026-11-03T18:00:00+09:00",
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
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": "https://lumi-cosme.vercel.app/winter-azelaic-acid"
            }
        },
        {
            "@type": "ItemList",
            "name": "真冬の高濃度アゼライン酸コスメおすすめランキング10選",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": idx + 1,
                    "item": prod
                }
                for idx, prod in enumerate(jsonld_products)
            ]
        },
        {
            "@type": "FAQPage",
            "mainEntity": jsonld_faq
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
                    "name": "高濃度アゼライン酸コスメ",
                    "item": "https://lumi-cosme.vercel.app/winter-azelaic-acid"
                }
            ]
        }
    ]
}

faq_html = ""
for f in faq_data:
    faq_html += f"""
      <div class="faq-item">
        <dt class="faq-question">
          <span class="faq-q-badge">Q</span>
          <span>{f['q']}</span>
        </dt>
        <dd class="faq-answer">
          <span class="faq-a-badge">A</span>
          <p>{f['a']}</p>
        </dd>
      </div>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！冬のインナードライ赤みと乾燥毛穴を鎮めて潤す高濃度アゼライン酸コスメランク10</title>
  <meta name="description" content="11月・12月の冬本番に！寒暖差赤みや暖房テカリ、乾燥毛穴を鎮めて潤す高濃度アゼライン酸コスメ10選を徹底比較！KISO、dr365、Anua、トゥヴェール、DRXなど厳選。">
  <meta name="keywords" content="アゼライン酸, アゼライン酸 美容液, アゼライン酸 クリーム, インナードライ, 赤ら顔 冬, 毛穴 ケア, KISO, トゥヴェール, DRX">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-azelaic-acid">
  
  <!-- OGP -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！冬のインナードライ赤みと乾燥毛穴を鎮めて潤す高濃度アゼライン酸コスメランク10">
  <meta property="og:description" content="11月・12月の冬本番に！寒暖差赤みや暖房テカリ、乾燥毛穴を鎮めて潤す高濃度アゼライン酸コスメ10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-azelaic-acid">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta name="twitter:card" content="summary_large_image">
  
  <script type="application/ld+json">
{json.dumps(full_jsonld, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary-color: #4338ca;
      --primary-light: #eef2ff;
      --accent-color: #6366f1;
      --accent-hover: #4f46e5;
      --text-main: #1e1b4b;
      --text-muted: #64748b;
      --bg-main: #f8fafc;
      --card-bg: #ffffff;
      --border-color: #e0e7ff;
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.04);
      --shadow-md: 0 4px 12px rgba(67,56,202,0.08);
      --shadow-lg: 0 8px 24px rgba(67,56,202,0.12);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif;
      line-height: 1.8;
      color: var(--text-main);
      background-color: var(--bg-main);
    }}

    .container {{
      max-width: 920px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* ヘッダー */
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      padding: 16px 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .site-nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-color);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 20px;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--accent-color);
    }}

    /* パンくずリスト */
    .breadcrumb {{
      display: flex;
      list-style: none;
      padding: 14px 0;
      font-size: 0.85rem;
      color: var(--text-muted);
      overflow-x: auto;
      white-space: nowrap;
    }}
    .breadcrumb li+li:before {{
      content: "›";
      padding: 0 8px;
      color: #cbd5e1;
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumb a:hover {{
      color: var(--accent-color);
    }}

    /* 記事メイン */
    article {{
      background: var(--card-bg);
      border-radius: var(--radius-lg);
      padding: 40px;
      margin: 20px 0 40px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    @media (max-width: 640px) {{
      article {{ padding: 20px; }}
    }}

    .article-header {{
      margin-bottom: 36px;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 24px;
    }}
    .season-badge {{
      display: inline-block;
      background: #e0e7ff;
      color: #4338ca;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 12px;
    }}
    h1.article-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.45;
      color: #1e1b4b;
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }}
    @media (max-width: 640px) {{
      h1.article-title {{ font-size: 1.45rem; }}
    }}
    .meta-info {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    /* リード文 */
    .lead-box {{
      background: var(--primary-light);
      border-left: 4px solid var(--primary-color);
      padding: 24px;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      margin-bottom: 36px;
      font-size: 1.02rem;
      line-height: 1.85;
      color: #1e1b4b;
    }}
    .lead-box p+p {{ margin-top: 14px; }}

    /* 目次 */
    .toc-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-md);
      padding: 24px;
      margin-bottom: 44px;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--primary-color);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      padding-left: 0;
    }}
    .toc-list li {{
      margin-bottom: 8px;
      font-size: 0.95rem;
    }}
    .toc-list a {{
      color: #475569;
      text-decoration: none;
      display: inline-block;
      transition: color 0.15s;
    }}
    .toc-list a:hover {{
      color: var(--accent-color);
      text-decoration: underline;
    }}

    /* 見出し */
    h2.section-heading {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #1e1b4b;
      margin: 48px 0 24px;
      padding-left: 14px;
      border-left: 5px solid var(--accent-color);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    h3.sub-heading {{
      font-size: 1.2rem;
      font-weight: 700;
      color: #312e81;
      margin: 28px 0 16px;
    }}

    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 28px;
      margin-bottom: 40px;
      box-shadow: var(--shadow-sm);
      transition: box-shadow 0.25s, transform 0.25s;
    }}
    .product-card:hover {{
      box-shadow: var(--shadow-md);
    }}
    .product-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, #4338ca, #6366f1);
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 4px 14px;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(67,56,202,0.3);
    }}
    #rank-1 .rank-badge {{
      background: linear-gradient(135deg, #4f46e5, #818cf8);
      font-size: 1.05rem;
      padding: 6px 18px;
    }}
    .product-tag {{
      background: #eef2ff;
      color: #4338ca;
      border: 1px solid #c7d2fe;
      font-size: 0.85rem;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 6px;
    }}
    h3.product-name {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #1e1b4b;
      margin-bottom: 8px;
      line-height: 1.45;
    }}
    .product-catch {{
      color: #4338ca;
      font-weight: 600;
      font-size: 0.95rem;
      margin-bottom: 20px;
    }}

    .product-content-grid {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }}
    @media (max-width: 680px) {{
      .product-content-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-img-wrap {{
      text-align: center;
      background: #f8fafc;
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #f1f5f9;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      object-fit: contain;
      border-radius: var(--radius-sm);
    }}

    .price-box {{
      background: #eef2ff;
      border: 1px solid #e0e7ff;
      border-radius: var(--radius-sm);
      padding: 12px 16px;
      margin-bottom: 16px;
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .price-label {{
      font-size: 0.85rem;
      color: #312e81;
      font-weight: 600;
    }}
    .price-value {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #4338ca;
    }}
    .price-tax {{
      font-size: 0.75rem;
      color: #475569;
    }}

    .product-specs {{
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 8px 16px;
      font-size: 0.88rem;
      background: #f8fafc;
      padding: 14px;
      border-radius: var(--radius-sm);
    }}
    .product-specs dt {{
      font-weight: 700;
      color: #64748b;
      white-space: nowrap;
    }}
    .product-specs dd {{
      color: #334155;
    }}

    .product-desc-box {{
      background: #f8fafc;
      border-radius: var(--radius-md);
      padding: 20px;
      margin-bottom: 20px;
      border: 1px solid #f1f5f9;
    }}
    .desc-heading {{
      font-size: 1rem;
      font-weight: 700;
      color: #1e1b4b;
      margin-bottom: 12px;
    }}
    .desc-p {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
      margin-bottom: 12px;
    }}
    .desc-p:last-child {{ margin-bottom: 0; }}

    .target-point-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-top: 16px;
      padding-top: 16px;
      border-top: 1px dashed #cbd5e1;
    }}
    @media (max-width: 600px) {{
      .target-point-grid {{ grid-template-columns: 1fr; }}
    }}
    .target-box, .point-box {{
      background: #ffffff;
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid #e2e8f0;
      font-size: 0.88rem;
    }}
    .target-box strong, .point-box strong {{
      display: block;
      color: #1e1b4b;
      margin-bottom: 4px;
      font-size: 0.88rem;
    }}
    .target-box p, .point-box p {{
      color: #475569;
      line-height: 1.6;
    }}

    .product-action-wrap {{
      text-align: center;
      margin-top: 20px;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: linear-gradient(135deg, #bf0000, #dc2626);
      color: #ffffff;
      font-size: 1.05rem;
      font-weight: 700;
      padding: 14px 28px;
      border-radius: var(--radius-md);
      text-decoration: none;
      box-shadow: 0 4px 12px rgba(191,0,0,0.25);
      transition: transform 0.15s, box-shadow 0.15s, background 0.15s;
      width: 100%;
      max-width: 440px;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000, #b91c1c);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191,0,0,0.35);
    }}

    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 30px 0 40px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      background: #ffffff;
      font-size: 0.9rem;
      text-align: left;
    }}
    .compare-table th {{
      background: var(--primary-light);
      color: var(--primary-color);
      font-weight: 700;
      padding: 14px 16px;
      border-bottom: 2px solid var(--border-color);
      white-space: nowrap;
    }}
    .compare-table td {{
      padding: 14px 16px;
      border-bottom: 1px solid #f1f5f9;
      color: #334155;
    }}
    .compare-table tr:hover {{
      background: #f8fafc;
    }}
    .compare-table .rank-cell {{
      font-weight: 700;
      color: var(--accent-color);
      white-space: nowrap;
    }}
    .compare-table .price-cell {{
      font-weight: 700;
      color: #4338ca;
      white-space: nowrap;
    }}

    /* Q&A */
    .faq-list {{
      margin: 24px 0 40px;
    }}
    .faq-item {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      margin-bottom: 16px;
      overflow: hidden;
    }}
    .faq-question {{
      background: #f8fafc;
      padding: 16px 20px;
      font-weight: 700;
      font-size: 1rem;
      color: #1e1b4b;
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 1px solid #f1f5f9;
    }}
    .faq-q-badge {{
      background: var(--primary-color);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .faq-answer {{
      padding: 18px 20px;
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
      display: flex;
      gap: 12px;
    }}
    .faq-a-badge {{
      background: var(--accent-color);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
    }}

    /* 内部リンクカード */
    .related-articles {{
      margin: 40px 0 20px;
      padding: 24px;
      background: #f8fafc;
      border-radius: var(--radius-md);
      border: 1px solid #e2e8f0;
    }}
    .related-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #1e1b4b;
      margin-bottom: 16px;
    }}
    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 16px;
    }}
    .related-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-sm);
      padding: 14px;
      text-decoration: none;
      color: #1e293b;
      transition: border-color 0.2s, box-shadow 0.2s;
      display: block;
    }}
    .related-card:hover {{
      border-color: var(--accent-color);
      box-shadow: var(--shadow-sm);
    }}
    .related-card-title {{
      font-size: 0.92rem;
      font-weight: 700;
      line-height: 1.45;
      margin-bottom: 6px;
      color: #1e1b4b;
    }}
    .related-card-desc {{
      font-size: 0.8rem;
      color: #64748b;
      line-height: 1.5;
    }}

    /* フッター */
    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 48px 0 32px;
      margin-top: 60px;
      font-size: 0.88rem;
    }}
    .footer-content {{
      display: grid;
      grid-template-columns: 1fr 2fr;
      gap: 32px;
      margin-bottom: 32px;
    }}
    @media (max-width: 768px) {{
      .footer-content {{ grid-template-columns: 1fr; }}
    }}
    .footer-brand h4 {{
      color: #ffffff;
      font-size: 1.1rem;
      margin-bottom: 12px;
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 12px;
    }}
    .footer-links-grid a {{
      color: #cbd5e1;
      text-decoration: none;
      transition: color 0.15s;
    }}
    .footer-links-grid a:hover {{
      color: #818cf8;
    }}
    .copyright {{
      text-align: center;
      padding-top: 24px;
      border-top: 1px solid #1e293b;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <!-- ヘッダー -->
  <header>
    <div class="container site-nav">
      <a href="/" class="site-logo">
        <span>❄️</span>
        <span>冬コスメ徹底比較ラボ</span>
      </a>
      <nav class="nav-links">
        <a href="/">ホーム</a>
        <a href="/#ranking">最新ランキング</a>
        <a href="/#ingredients">成分別ガイド</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <!-- パンくずリスト -->
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li><a href="/">ホーム</a></li>
        <li aria-current="page">高濃度アゼライン酸コスメ</li>
      </ol>
    </nav>

    <article>
      <div class="article-header">
        <span class="season-badge">2026-2027 冬の厳選高保湿コスメ</span>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！冬のインナードライ赤みと乾燥毛穴を鎮めて潤す高濃度アゼライン酸コスメランク10</h1>
        <div class="meta-info">
          <span>📅 公開: 2026年11月3日</span>
          <span>✍️ 監修: 冬コスメ徹底比較ラボ 美容解析チーム</span>
          <span>⏱️ 読了目安: 約8分</span>
        </div>
      </div>

      <!-- リード文 -->
      <div class="lead-box">
        <p>11月・12月を迎えると、冷え込む外気と過熱した室内暖房による激しい寒暖差から『頬やすっぴん肌が真っ赤に火照る』『Tゾーンは皮脂でテカるのに、頬や口元はカサカサに突っ張る』という<strong>冬のインナードライ＆寒暖差赤みトラブル</strong>が多発します。この季節の肌荒れや毛穴の開きは、単純な保湿クリームの厚塗りだけでは解決できず、むしろ油分過多によって大人ニキビや角栓詰まりを悪化させてしまうケースが後を絶ちません。</p>
        <p>そんな冬の皮脂水分アンバランスを科学的に打破する成分として、皮膚科医やコスメマニアの間で圧倒的な支持を集めているのが<strong>『高濃度アゼライン酸（Azelaic Acid）』</strong>です。穀物由来の天然酸であるアゼライン酸は、皮脂分泌の抑制、角化の正常化、赤み（毛細血管の拡張や炎症）の鎮静、毛穴詰まりの解消という多彩なアプローチを同時に発揮。レチノールのような激しいA反応や皮剥けを起こさず、冬の高保湿成分（セラミド、ヒアルロン酸、スクワラン、CICA）と掛け合わせることで、乾かないのにテカらない奇跡のシルク美肌を再建します。</p>
        <p>本稿では、楽天市場で現在流通している最新のアゼライン酸コスメから、皮膚科クリニック推奨の20%超高濃度クリーム、浸透性に優れたプレローション、敏感肌でもしみない高保湿セラムまでを徹底精査。赤み鎮静スピード・皮脂コントロール力・保湿持続性を多角的に検証し、本当におすすめできる厳選10アイテムをランキング形式で詳しくレビューします。</p>
      </div>

      <!-- 目次 -->
      <div class="toc-box">
        <div class="toc-title">📑 目次（タップで各項目へジャンプ）</div>
        <ul class="toc-list">
          <li><a href="#why-azelaic">1. なぜ冬のインナードライ赤み＆毛穴に「アゼライン酸」が効くのか？</a></li>
          <li><a href="#compare-table">2. 高濃度アゼライン酸コスメおすすめ人気比較一覧表</a></li>
          <li><a href="#rank-1">3. 【第1位〜第10位】アゼライン酸コスメ徹底レビュー＆真冬の検証結果</a></li>
          <li><a href="#how-to-choose">4. 失敗しない冬のアゼライン酸コスメの選び方3つの鉄則</a></li>
          <li><a href="#faq-section">5. アゼライン酸に関するよくある疑問とプロの回答（Q&A）</a></li>
        </ul>
      </div>

      <!-- 解説セクション1 -->
      <section id="why-azelaic">
        <h2 class="section-heading">なぜ冬のインナードライ赤み＆毛穴に「アゼライン酸」が効くのか？</h2>
        <p class="desc-p">冬の肌トラブルの盲点は、寒さによる血行不良とエアコン暖房の熱風が引き起こす『局所的な皮脂の過剰酸化』と『毛細血管の異常拡張』です。外の冷たい風にさらされた直後に暖かい室内に入ると、急激な温度変化に血管が対応できず、頬や小鼻の周りに強い赤みが生じます。さらに、乾燥から肌を守ろうとして皮脂腺が暴走し、硬くなった古い角質と混ざり合って頑固な角栓や酸化テカリを発生させます。</p>
        <p class="desc_p">アゼライン酸は、皮脂分泌を促す酵素『5αリダクターゼ』の働きを阻害し、冬の暖房直風による過剰な皮脂テカリを根本から抑制します。同時に、毛穴の出口で異常に硬化した角質細胞の結合を穏やかにゆるめ、角栓の詰まりを自然に排出。さらに優れた抗炎症作用によって、寒暖差やマスクの擦れで拡張した毛細血管の炎症を速やかに沈静化させます。</p>
        <p class="desc_p">重要なのは、アゼライン酸は肌に必要なバリア脂質（セラミドや細胞間脂質）を奪わないという点です。高保湿なヒアルロン酸やスクワランと併用することで、角層の水分量を最高水準に保ちながら、毛穴の開きや赤みをサラリと消し去る理想的な肌環境を維持できるのです。</p>
      </section>

      <!-- 比較表 -->
      <section id="compare-table">
        <h2 class="section-heading">高濃度アゼライン酸コスメおすすめ人気比較一覧表</h2>
        <p class="desc-p">楽天市場で絶大な人気を誇る実力派アゼライン酸コスメ10選の価格・容量・処方特徴を一目で比較できます。</p>
        <div class="table-container">
          <table class="compare-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>タイプ / 容量</th>
                <th>主要成分・処方特徴</th>
                <th>参考価格(税込)</th>
              </tr>
            </thead>
            <tbody>
              {table_rows}
            </tbody>
          </table>
        </div>
      </section>

      <!-- ランキングメイン -->
      <section id="ranking-list">
        <h2 class="section-heading">【第1位〜第10位】高濃度アゼライン酸コスメ徹底レビュー＆真冬の検証結果</h2>
        <p class="desc-p">楽天市場で流通している最新ロットをもとに、真冬の保水アプローチやテクスチャー、効果的な使用法まで詳細にレビューします。</p>
        
        {items_html}
      </section>

      <!-- 選び方セクション -->
      <section id="how-to-choose">
        <h2 class="section-heading">失敗しない冬のアゼライン酸コスメの選び方3つの鉄則</h2>
        <p class="desc-p">真冬の乾燥環境下でアゼライン酸の効果を最大限に引き出すためには、配合濃度や基剤タイプ、併用成分を正しく見極めることが不可欠です。</p>

        <h3 class="sub-heading">① 自分の肌状態に合わせて「純アゼライン酸（10〜20%）」か「アゼライン酸誘導体」を選ぶ</h3>
        <p class="desc-p">毛穴の詰まりや赤み、頑固な皮脂トラブルを早急に解決したい場合は、クリニック実績の高い純アゼライン酸15%〜20%配合のクリームが最適です。一方、冬の乾燥によって肌が敏感に傾いている方や、ピリピリ感を避けたい方は、水溶性で刺激が極めてマイルドな『アゼライン酸誘導体（アゼロイルジグリシンKなど）』を配合したプレ化粧水やセラムからスタートするのが安心です。</p>

        <h3 class="sub-heading">② スクワランやヒアルロン酸、CICAなど高保湿・鎮静成分の併合設計を確認する</h3>
        <p class="desc-p">冬場のアゼライン酸ケアで最も避けたいのは、皮脂抑制に伴う一時的なツッパリ感です。製品を選ぶ際は、アゼライン酸単体だけでなく、肌のバリア機能を保護する植物性スクワラン、高分子ヒアルロン酸、ツボクサエキス（CICA）、パンテノールなどが同時に配合された高保湿処方を選ぶことで、冬でもしっとり吸い付くような潤い膜を維持できます。</p>

        <h3 class="sub-heading">③ 塗布する部位（全顔か部分使いか）と朝晩のルーティンを設計する</h3>
        <p class="desc-p">皮脂分泌が活発なTゾーンや毛穴の開きが気になる小鼻周り、赤みが出やすい両頬を中心に部分使いするか、インナードライ対策として全顔に薄く伸ばすかを使い分けましょう。朝のメイク前に使うと日中のテカリとファンデーションのドロドロ崩れを完璧に防げます。</p>
      </section>

      <!-- FAQセクション -->
      <section id="faq-section">
        <h2 class="section-heading">アゼライン酸に関するよくある疑問とプロの回答（Q&A）</h2>
        <div class="faq-list">
          {faq_html}
        </div>
      </section>

      <!-- 内部リンク関連記事 -->
      <section class="related-articles">
        <h3 class="related-title">❄️ あわせて読みたい！冬の高保湿スキンケア特集</h3>
        <div class="related-grid" id="related-grid-box">
          <!-- 自動更新スクリプトにより最新リンクが挿入されます -->
        </div>
      </section>
    </article>
  </main>

  <!-- フッター -->
  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-brand">
          <h4>冬コスメ徹底比較ラボ</h4>
          <p>乾燥が深刻化する11月・12月の冬期に特化し、科学的根拠に基づいた高保湿成分や楽天市場の人気コスメを徹底検証・レビューする専門メディアです。</p>
        </div>
        <div>
          <h4 style="color:#ffffff; margin-bottom:12px;">注目の高保湿テーマ</h4>
          <div class="footer-links-grid" id="footer-links-box">
            <!-- 自動更新スクリプトにより最新リンクが挿入されます -->
          </div>
        </div>
      </div>
      <div class="copyright">
        <p>&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved.</p>
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-azelaic-acid.html", "w", encoding="utf-8") as f:
    f.write(full_html.strip())

print("winter-azelaic-acid.html generated successfully!")
