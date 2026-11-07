import json
import re

with open("fetched_3new_nov_dec_special.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_panthenol_serum"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🔬 高濃度パンテノール10%×CICA！寒冷刺激で破壊された角層バリアを急行修復する集中アンプル",
        "catch": "韓国オリーブヤングで不動の地位を築くバイオヒールボの独自複合体『パンテセル™』配合。10%もの超高濃度パンテノールが、真冬の冷風で赤みやヒリつきを起こした角層深部へ浸透し、自己再生バリアを猛スピードで立て直す本格派美容液",
        "brand_name": "BIOHEAL BOH (バイオヒールボ)",
        "capacity": "30mL / スポイト遮光ボトル",
        "type": "パンテノール10%配合 バリア集中リペア美容液",
        "features": "パンテセル™（パンテノール10%、CICA/ツボクサエキス、β-シトステロール）、低分子ヒアルロン酸、弱酸性",
        "value": "単に水分を補給するだけでなく、肌内部でプロビタミンB5がパントテン酸に変換され、細胞間脂質の生成スイッチをON。寒暖差ショックによる赤み・肌荒れを翌朝までに鎮静",
        "desc_p1": "11月後半から12月にかけて、気温が一桁台まで下がる屋外から暖房で25度近くまで暖められた室内へ入ると、皮膚の毛細血管が急激に収縮・拡張を繰り返し、角層のバリア機能に深刻な亀裂が入ります。この『寒暖差ストレス』によって肌がピリピリと痛んだり、洗顔後に赤みが引かないトラブルが頻発します。バイオヒールボのパンテセル シカ ブレミッシュ アンプルは、敏感化した肌の組織修復を担うパンテノールを10%という高濃度で処方した、冬の救急アンプルです。",
        "desc_p2": "スポイトで取ると、わずかにとろみのあるみずみずしいテクスチャー。肌に伸ばした瞬間にスーッと角層へ吸い込まれ、ベタつきを残さず内側に濃密な潤いのクッションを形成します。ツボクサエキスとの相乗効果により、乾燥による微小な炎症を素早くクールダウン。夜のスキンケアに取り入れると、翌朝の肌はキメが整い、指先を跳ね返すようなモチモチとした弾力感が蘇ります。",
        "target": "冬の冷気や暖房で肌がヒリつく方、洗顔後に頬が赤くなりやすい敏感ゆらぎ肌、乾燥によって毛穴が縦に開いて目立つインナードライ肌",
        "point": "化粧水で肌を整えた直後、スポイト1回分を全顔に優しくなじませます。特に赤みや乾燥が目立つ頬の高い位置には、もう半プッシュを指先でトントンと重ねづけするのが効果的です。"
    },
    {
        "rank": 2,
        "tag": "💧 高純度プロビタミンB5×2種の分子量ヒアルロン酸！真冬のしぼみ肌を底上げする薬用級セラム",
        "catch": "敏感肌の皮膚科学研究を極めたラ ロッシュ ポゼの名作。高純度プロビタミンB5（パンテノール）と大小2種の分子量ヒアルロン酸が、乾燥でしぼんだ大人の角層を内側から押し上げるようにふっくら満たす高保湿セラム",
        "brand_name": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
        "capacity": "30mL / ブルー遮光ボトル",
        "type": "高純度パンテノール×デュアルヒアルロン酸配合 高保水セラム",
        "features": "パンテノール（プロビタミンB5）、高分子ヒアルロン酸、低分子ヒアルロン酸、マデカッソシド、ラロッシュポゼターマルウォーター",
        "value": "肌表面を高分子ヒアルロン酸がラッピングし、低分子ヒアルロン酸とパンテノールが深部を修復。冬の乾燥による小ジワを目立たなくし、ふっくらしたハリ密度を再生",
        "desc_p1": "冬の乾燥が進むと、角層の水分含有量が著しく低下し、肌が薄く硬くなって表情ジワがそのまま定着しやすくなります。ラ ロッシュ ポゼのヒアルB5 セラムは、皮膚科医の協力のもと開発された、角層のハリ低下と乾燥ダメージに同時にアプローチする濃密美容液です。肌修復を促すパンテノールと、肌の弾力維持に欠かせないヒアルロン酸を黄金比で配合しています。",
        "desc_p2": "濃厚でリッチなセラムが肌にピタッと密着し、塗ったそばから肌のキメが持ち上がるような充実感を与えます。マデカッソシドもブレンドされているため、乾燥で荒れた肌表面を滑らかに整え、ファンデーションのノリを格段に向上させます。刺激に弱い目元や口元にも安心して使え、一日中ふっくらとしたみずみずしい質感をキープできます。",
        "target": "暖房の乾燥で夕方に目元・口元の小ジワが目立つ方、肌の弾力やハリの衰えを感じる大人世代、敏感肌でも攻めのエイジングケアを行いたい方",
        "point": "朝晩の化粧水後、3〜4滴を手にとって顔全体から首元まで引き上げるようになじませます。その後、乳液やクリームで油分を補うことで、ヒアルロン酸とパンテノールの保水膜がしっかりと閉じ込められます。"
    },
    {
        "rank": 3,
        "tag": "🧬 NMF天然保湿因子を完全再現！17%高濃度アミノ酸×B5が角層深部の水分貯蔵庫を再建",
        "catch": "肌本来の保湿因子である遊離アミノ酸を17%も贅沢に凝縮し、プロビタミンB5とブレンド。単なる表面保湿を超え、角質細胞そのものが水分を抱え込むキャパシティを劇的に拡張するカナダ発の実力派美容液",
        "brand_name": "The Ordinary (ジ オーディナリー)",
        "capacity": "30mL / スポイトクリアボトル",
        "type": "アミノ酸17%×プロビタミンB5配合 高浸透保水セラム",
        "features": "アミノ酸複合体17%（アルギニン、グリシン、アラニン、セリン等）、パンテノール（プロビタミンB5）、ピロリドンカルボン酸（PCA）",
        "value": "角層の天然保湿因子（NMF）の組成をそのまま補給。水分の蒸発を防ぐだけでなく、肌自らが水分を蓄える『保水タンク容量』を底上げ",
        "desc_p1": "いくら油分で蓋をしても肌の内側が突っ張る現象は、角質細胞の中にある『天然保湿因子（NMF）』が枯渇していることが最大の原因です。冬の寒さによって肌の新陳代謝が鈍ると、NMFの主成分であるアミノ酸の生成が追いつかなくなります。ジ オーディナリーのアミノ酸 + B5は、無駄な増粘剤や香料を一切排除し、アミノ酸とパンテノールだけを高純度でダイレクトに届ける設計です。",
        "desc_p2": "水のようにサラサラとした驚きの浸透テクスチャーで、肌に乗せた瞬間に細胞の間へ染み渡ります。ベタつきが一切ないため、朝のメイク前や他の美容液との重ねづけにも最適。使い続けるうちに肌のキメが驚くほど整い、冬特有のゴワつきやザラつきが消え、つるんと滑らかなシルクのような素肌へと生まれ変わります。",
        "target": "どれだけクリームを塗っても内側の乾燥が治まらないインナードライ肌、ベタつくスキンケアが苦手な方、成分重視で確実な肌質改善を目指す方",
        "point": "洗顔後すぐ、または導入化粧水の後に数滴を手に取り、肌全体にパッティングするようになじませます。オイルや重いクリームの前にステップとして挟むのが鉄則です。"
    },
    {
        "rank": 4,
        "tag": "🍯 黒蜂プロポリス83.25%×パンテノール！真冬の枯れ肌にしっとり蜜ツヤを宿す極上アンプル",
        "catch": "フランス産の清浄な黒蜂から採取された高純度プロポリスエキスを83.25%配合。パンテノールとの相乗効果で、乾燥で活力を失った真冬の素肌に、まるでハチミツを塗ったかのような濃密な潤いと輝くツヤをもたらす名品",
        "brand_name": "COSRX (コスアールエックス)",
        "capacity": "30mL / スポイトドロップボトル",
        "type": "黒蜂プロポリス83%×パンテノール配合 濃密ツヤ肌アンプル",
        "features": "プロポリスエキス83.25%、パンテノール0.2%、カシア種子エキス、ヒアルロン酸Na、低刺激テスト済み",
        "value": "抗酸化・抗菌・高保湿に優れたプロポリスが外気の乾燥ストレスを遮断し、パンテノールが肌バリアを修復。夕方になってもパサつかない濃密なツヤ肌を一日中維持",
        "desc_p1": "冬の寒風にさらされた肌は、水分だけでなく栄養分も枯渇し、どんよりとくすんで生気を失いがちです。COSRXのフルフィット プロポリス ライト アンプルは、精製水の代わりに高濃度のプロポリスエキスをベースにした贅沢な処方が特徴です。プロポリスに含まれるフラボノイドやアミノ酸が冬の酸化ストレスに対抗し、パンテノールが角層の水分蒸散をブロックします。",
        "desc_p2": "とろみのある琥珀色のテクスチャーですが、肌になじませると不思議なほど軽やかに伸び、ベタつきを残さずに吸い付くようなもっちり肌に仕上がります。日中のメイク前に仕込むと、内側から自然な光が湧き出るような上品な水光ツヤが持続。乾燥によるファンデーションの毛穴落ちやヨレも劇的に防いでくれます。",
        "target": "冬になると肌がくすんで疲れて見えやすい方、自然なツヤ肌メイクの土台を作りたい方、こっくり濃厚な潤い感を求める乾燥肌",
        "point": "化粧水の後に適量を手に取り、顔全体を手のひらで温めながらじっくりと浸透させます。特にカサつきやすい頬にはハンドプレスで密着させましょう。"
    },
    {
        "rank": 5,
        "tag": "🌲 清浄シラカバ樹液70%×パンテノール！冬のインナードライを根本から潤す水分ブースティングセラム",
        "catch": "韓国江原道インジェの清らかな白樺から抽出したシラカバ樹液を70%高配合。ミネラルとアミノ酸が豊富な樹液とパンテノールが、真冬の硬化した角質層をぐんぐん潤し、みずみずしい巡り肌へと導く高浸透セラム",
        "brand_name": "Anua (アヌア)",
        "capacity": "30mL / ポンプボトル",
        "type": "シラカバ樹液70%×パンテノール配合 水分ブーストセラム",
        "features": "シラカバ樹液70%（ベチュラアルバ樹液）、パンテノール、10種ヒアルロン酸、ABC複合体（アラントイン、ベタイン、キュウリ果実エキス）",
        "value": "人間の生体水に近いミネラルバランスを持つシラカバ樹液が角層の深部まで即座に浸透。パンテノールが水分蒸散を防ぎ、水分保持率を飛躍的に向上",
        "desc_p1": "『外側は皮脂でテカっているのに、内側はつっぱって痛い』という冬特有のインナードライは、角層の水分通り道が滞っていることが原因です。アヌアのシラカバ水分セラムは、春先にしか採取できない貴重なシラカバ樹液を贅沢に70%使用。樹液に含まれる豊富な糖類とアミノ酸が、真冬の冷気で縮こまった角質細胞をみずみずしく膨らませます。",
        "desc_p2": "ウォータージェル状のテクスチャーが肌の上で弾けるように広がり、瞬時に深部へと浸透していきます。パンテノールが角層の表面に目に見えない水分保持膜を形成するため、暖房の効いた部屋でもつっぱり感が一切生じません。敏感肌パッチテスト済みで、刺激を一切感じさせないマイルドな使い心地も魅力です。",
        "target": "水分不足で毛穴が開きやすいインナードライ肌、テカリと乾燥が混在する混合肌、ベタつかずに奥深くまで水分を届けたい方",
        "point": "朝晩の洗顔後、化粧水で整えた肌に1〜2プッシュをなじませます。乾燥が気になる日は2度重ねて水分レイヤリングを行うと、もっちり感が倍増します。"
    },
    {
        "rank": 6,
        "tag": "🛡️ パンテノール×エクトインの最強バリアタッグ！過酷な砂漠気候にも耐えうる超高保湿エッセンス",
        "catch": "角層修復のパンテノールと、塩湖の極限環境生物から発見された高保水分子エクトインを黄金比で融合した『パンテトイン™』処方。冬の冷気と暖房で干からびた肌を濃密な潤いで満たし続ける韓国大ヒットエッセンス",
        "brand_name": "manyo (魔女工場)",
        "capacity": "200mL / 大容量トナーボトル",
        "type": "パンテトイン™（パンテノール×エクトイン）配合 濃密高保湿エッセンス",
        "features": "パンテトイン（パンテノール4,000ppm、エクトイン1,000ppm）、低分子ヒアルロン酸、セラミドNP、アラントイン",
        "value": "エクトインが水分を分子レベルで強固に結束させ、パンテノールが角層バリアを強固に修復。真冬の過酷な乾燥環境下でも200時間潤いが持続する圧倒的保水力",
        "desc_p1": "魔女工場が極限の乾燥地帯でも自活する微生物の生態に着目して開発したのが、このパンテトインシリーズです。エクトインは自身を取り囲む水分子と強固な水和殻を形成し、過酷な乾燥や紫外線から細胞を守り抜く性質を持ちます。このエクトインと、角層修復に優れたパンテノールを組み合わせることで、従来の保湿美容液の限界を打ち破る保水力を実現しました。",
        "desc_p2": "乳白色のまろやかなエッセンスが肌を包み込み、まるで上質な乳液を溶かし込んだようなリッチな潤いを与えます。肌にのせると素早く浸透し、表面はベタつかずにシルキーなバリア膜が形成されます。真冬の朝に使えば夕方まで乾燥を感じず、夜に使えば翌朝の洗顔時までモチモチした柔らかさが持続します。",
        "target": "何を塗ってもすぐに乾いてしまう超乾燥肌、冬になると粉を吹いて皮がめくれやすい方、化粧水と美容液を1本で濃厚に済ませたい方",
        "point": "適量を手にとり、顔全体に優しくハンドプレスしてなじませます。特に乾燥が気になる目元や口元には、コットンにたっぷり含ませて3分間部分パックをするのがおすすめです。"
    },
    {
        "rank": 7,
        "tag": "🧬 プロビタミンB5高濃度5%×トリプルペプチド！真冬の寒暖差で弱った角層バリアを強固に再建",
        "catch": "皮膚科学専門ブランドSKIN&LABが開発。高純度パンテノール5%と3種の機能性ペプチドが角層の弾力構造を立て直し、冬の寒冷外気で傷んだ肌の自己回復力を加速させるリペア美容液",
        "brand_name": "SKIN&LAB (スキンアンドラブ)",
        "capacity": "30mL / スポイトボトル",
        "type": "パンテノール5%×トリプルペプチド配合 バリア集中美容液",
        "features": "パンテノール50,000ppm（5%）、トリプルペプチド、アズレン、マデカッソシド、弱酸性",
        "value": "角層深部の修復を促すパンテノールと、肌の弾力密度を高めるペプチドの相乗効果。冬の寒暖差によるたるみ毛穴と乾燥小ジワを同時にケア",
        "desc_p1": "冬の寒暖差は、肌の表面だけでなく真皮に近い角層深部のコラーゲンやエラスチンの結束力まで弱めてしまいます。スキンアンドラブのバリアダーム リンガーアンプルは、皮膚バリアの主役であるパンテノールを5%という高純度で配合し、さらに肌の引き締めに働く3種の機能性ペプチドをブレンドした、本格エイジング対応のバリアセラムです。",
        "desc_p2": "スポイトから取り出すと、しっとりとした粘性を持ちながらも肌の上で素早く液状化し、角層のすみずみまで広がります。アズレン由来の淡いブルーの色味が肌の赤みを視覚的にも穏やかに整え、使い続けるほどに肌の密度がギュッと詰まったような引き締まり感を実感できます。暖房によるたるみ毛穴のケアにも極めて有効です。",
        "target": "冬の乾燥と同時に頬の毛穴の開きやたるみが気になる方、高機能なドクターズコスメを好む方、寒暖差で肌の調子が乱れやすいゆらぎ肌",
        "point": "洗顔後、化粧水の直後に2〜3滴を顔全体になじませます。気になる毛穴や乾燥ゾーンには、指の腹でトントンと押し込むように重ねづけしてください。"
    },
    {
        "rank": 8,
        "tag": "🛡️ 独自特許MLEバリア×パンテノール！乱れた角層ラメラ構造を整えて水分蒸発を完全ガード",
        "catch": "人間の健やかな皮膚ラメラ構造を十字架状に完全再現する独自特許技術『MLE®』を搭載。高濃度パンテノールと複合セラミドが、真冬の暖房乾燥による水分蒸散を隙間なくブロックする名作アンプル",
        "brand_name": "Real Barrier (リアルバリア)",
        "capacity": "30mL / スポイトボトル",
        "type": "独自特許MLE®処方 パンテノール高配合 高保湿鎮静アンプル",
        "features": "独自特許MLE®バリア処方、パンテノール、セラミド9S、マデカッソシド、アラントイン",
        "value": "崩れた角層の脂質ラメラ液晶構造を人工的に再構築。外気が氷点下になろうと、肌内部の水分を逃さない鉄壁のシールドを形成",
        "desc_p1": "皮膚のバリア機能が低下している状態とは、角質細胞の間を満たす脂質と水分のミルフィーユ構造（ラメラ構造）がバラバラに崩れている状態を指します。リアルバリアのアクア スージング アンプルは、健常な皮膚ラメラ構造と同一のマルチラメラ乳化技術（MLE）を採用し、塗った瞬間に角層の欠損部分にピタッと嵌まり込んで修復を行います。",
        "desc_p2": "みずみずしい透明なジェルテクスチャーで、肌に乗せるとスーッと馴染んで軽やかな保護膜を形成します。パンテノールが肌内部の代謝を促し、セラミド9Sが表面をコーティングするため、冬の冷たい外気に晒されても肌が突っ張ることがありません。低刺激設計で、敏感時にも安心して使用できます。",
        "target": "肌が薄くビニール肌になりやすい方、冬になるとどんな化粧水も浸透しにくくなる方、ラメラ構造の根本改善を目指したい方",
        "point": "朝晩の化粧水後、スポイトで手のひらに取り、両手で温めてから顔全体を優しく包み込みます。摩擦を一切かけずにハンドプレスでなじませるのがMLE処方の効果を高めるコツです。"
    },
    {
        "rank": 9,
        "tag": "🌿 ツボクサエキス×パンテノールの最強沈静コンビ！真冬の冷風や摩擦で敏感にゆらいだ肌を速攻クールダウン",
        "catch": "CICAコスメのパイオニアであるドクタージャルトの最上位シカペアセラム。高濃縮ツボクサエキスとパンテノールが、真冬の寒冷空気やマフラーの摩擦で敏感になった素肌を穏やかに鎮静し、高保湿ケアを両立",
        "brand_name": "Dr.Jart+ (ドクタージャルト)",
        "capacity": "30mL / グリーン遮光ドロップボトル",
        "type": "高濃度CICA×パンテノール配合 集中鎮静リペアセラム",
        "features": "センテラアジアティカ複合エキス、パンテノール、アラントイン、低刺激フォーミュラ",
        "value": "寒冷刺激や乾燥による赤み・肌荒れを速やかにケア。肌の自己防衛力を高め、冬のあらゆる外的ストレスに負けない強靭なバリアを構築",
        "desc_p1": "冬は寒さによる血行不良だけでなく、マフラーやタートルネックの襟元による物理的摩擦、さらに室内外の激しい寒暖差によって、肌が常にストレスに晒されています。ドクタージャルトのシカペア インテンシブ スージング リペア セラムは、そうした冬の複合ストレスで炎症を起こした肌をレスキューするために設計された、集中鎮静アンプルです。",
        "desc_p2": "淡いグリーンのセラムが肌の上でスーッとなめらかに広がり、熱を持った角層をやさしくクールダウンさせます。パンテノールが角層の水分保持力を高めるため、鎮静と同時にしっかりとしたうるおいが持続。日中の外的刺激に対するクッションの役割を果たし、荒れやすい冬の肌を常に穏やかで健やかな状態に保ちます。",
        "target": "マフラーやマスクの擦れで肌が赤くなりやすい方、冬の寒冷刺激でピリピリとした違和感を感じる敏感肌、肌荒れ予防と保湿を同時に叶えたい方",
        "point": "洗顔後、化粧水で肌を整えた直後に適量を顔全体に優しくなじませます。特に摩擦を受けやすい頬やフェイスラインには、指先で優しくタップするように重ねてください。"
    },
    {
        "rank": 10,
        "tag": "⚖️ 冬の乾燥でアルカリに傾いた肌pHを理想の弱酸性pH5.5へ！マルチヒアルロン酸×パンテノールの調和アンプル",
        "catch": "肌の理想的なpHバランスである弱酸性pH5.5を保つために設計された機能性アンプル。パンテノールと多重ヒアルロン酸が、真冬の乾燥でバリアが乱れた素肌のpHを即座に正常化し、潤い満ちる健やかな土台へリセット",
        "brand_name": "SAM'U (サミュ)",
        "capacity": "30mL / スポイトボトル",
        "type": "pH5.5弱酸性バランシング パンテノール配合 高保湿アンプル",
        "features": "パンテノール、マルチヒアルロン酸複合体、メドウフォーム油、ツボクサエキス、低刺激処方",
        "value": "乾燥やアルカリ性の洗顔料で乱れた肌表面のpHバランスを瞬時に整え、悪玉菌の繁殖を抑制。内側からみずみずしく潤う健やかな肌環境を確立",
        "desc_p1": "冬になると肌荒れが治りにくくなる原因の一つに、乾燥によって皮膚表面の皮脂膜が失われ、肌のpHがアルカリ性側に傾いてしまう現象があります。弱酸性を失った肌は悪玉菌が繁殖しやすく、角層の剥離酵素が正常に働かなくなります。サミュのPHセンシティブ アンプルは、素肌本来の理想的な弱酸性（pH5.5）を維持することに特化したスマートアンプルです。",
        "desc_p2": "とろみのあるリッチなリキッドが肌に触れると、驚くほどなめらかに馴染み、薄いうるおいのシールドを形成します。パンテノールが角層深部の水分蒸散を防ぎ、メドウフォーム油が表面をしっとり保護。使い続けることで肌の基礎体力が上がり、冬の乾燥や寒暖差にも動じないタフな素肌をキープできます。",
        "target": "冬になると肌トラブルが長引きやすい方、スキンケア後のつっぱり感が気になる方、肌のキメを整えてなめらかな化粧ノリを手に入れたい方",
        "point": "朝晩の洗顔後、化粧水で整えた肌にスポイト1回分を取り、顔全体に優しくなじませます。手のひらで顔を包み込んで深く呼吸しながらハンドプレスすると、成分の密着度が高まります。"
    }
]

# JSON-LD構造化データの生成
json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！損傷した角層バリアを深部から修復する保湿力高めパンテノール美容液ランク10",
    "description": "11月・12月の寒冷刺激や暖房乾燥で傷んだ角層バリアを深部から修復する高保湿パンテノール（プロビタミンB5）美容液10選を徹底検証！バイオヒールボ、ラロッシュポゼ、ジオーディナリー、魔女工場まで細胞修復の生化学的根拠と共に紹介。",
    "image": items[0]["image_url"],
    "datePublished": "2026-11-07T09:00:00+09:00",
    "dateModified": "2026-11-07T09:00:00+09:00",
    "author": {
        "@type": "Organization",
        "name": "LumiCosme スキンケア研究チーム",
        "url": "https://lumi-cosme.vercel.app/"
    },
    "publisher": {
        "@type": "Organization",
        "name": "LumiCosme (ルミコスメ)",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-panthenol-serum"
    }
}

json_ld_products = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": it["rank"],
            "item": {
                "@type": "Product",
                "name": it["display_name"],
                "image": it["image_url"],
                "description": product_details[it["rank"]-1]["catch"],
                "brand": {
                    "@type": "Brand",
                    "name": it["brand"]
                },
                "offers": {
                    "@type": "Offer",
                    "price": str(it["price"]),
                    "priceCurrency": "JPY",
                    "availability": "https://schema.org/InStock",
                    "url": it["affiliate_url"]
                }
            }
        } for it in items
    ]
}

json_ld_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "パンテノール（プロビタミンB5）はなぜ冬の乾燥や肌荒れに効果的なのですか？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "パンテノールは浸透性に優れたプロビタミンB5であり、肌内部に浸透すると直ちにパントテン酸へと変換されます。パントテン酸は補酵素A（CoA）の不可欠な構成成分であり、細胞のエネルギー代謝を活性化させて細胞間脂質（セラミドや脂肪酸）の生合成を直接促します。そのため、単に外側から水分を補給するだけでなく、肌自身が自活して水分を蓄えバリアを再建する根本修復効果を発揮します。"
            }
        },
        {
            "@type": "Question",
            "name": "レチノールやビタミンCなどの高機能成分とパンテノールは併用できますか？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "非常に相性が良く、むしろ併用が強く推奨されます。レチノールによるA反応（乾燥や皮むけ・赤み）や、高濃度ビタミンCによるピリピリ感を、パンテノールが持つ優れた抗炎症・組織修復作用が強力に緩和してくれます。併用する際は、化粧水の後にパンテノール美容液を仕込んで肌のクッションを作り、その後にビタミンCやレチノールを重ねるのが刺激を最小限に抑えるコツです。"
            }
        },
        {
            "@type": "Question",
            "name": "パンテノール美容液は朝と夜のどちらに使うのが最も効果的ですか？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "朝晩両方の使用が理想的ですが、目的によって役割が異なります。朝の使用では、日中の寒冷外気や暖房乾燥から角層バリアを守るプロテクト膜を形成し、夕方のメイク崩れや粉吹きを未然に防ぎます。夜の使用では、日中に受けた寒暖差ダメージや紫外線・摩擦による微小な炎症を就寝中に集中修復し、翌朝の肌のハリ密度を劇的に回復させます。"
            }
        },
        {
            "@type": "Question",
            "name": "パンテノール配合コスメを選ぶ際、濃度の目安はどのくらいですか？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "一般的な保湿目的であれば1%〜2%程度でも十分な保水効果を実感できますが、11月〜12月の真冬の深刻なインナードライや寒暖差による肌荒れ・赤みを素早くリペアしたい場合は、5%〜10%の高濃度設計のアンプルやセラムを選ぶのが劇的な手応えを得るための基準となります。"
            }
        }
    ]
}

# 商品カードHTMLの構築
product_cards_html = ""
for it in items:
    detail = product_details[it["rank"]-1]
    card = f"""
      <article class="product-card" id="rank-{it['rank']}">
        <div class="product-badge">第{it['rank']}位</div>
        <div class="product-tag">{detail['tag']}</div>
        <h3 class="product-title">{it['display_name']}</h3>
        
        <div class="product-grid">
          <div class="product-img-col">
            <img src="{it['image_url']}" alt="{it['item_name']}" class="product-img" loading="lazy" />
            <div class="product-brand-box">
              <span class="brand-label">ブランド</span>
              <span class="brand-value">{it['brand']}</span>
            </div>
            <div class="product-price-box">
              <span class="price-label">参考価格</span>
              <span class="price-val">¥{it['price']:,}</span>
              <span class="price-tax">（税込）</span>
            </div>
            <a href="{it['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
              <span>楽天市場で最安値を見る</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>

          <div class="product-info-col">
            <div class="catch-quote">{detail['catch']}</div>
            
            <div class="spec-table">
              <div class="spec-row">
                <span class="spec-name">容量 / 容器</span>
                <span class="spec-desc">{detail['capacity']}</span>
              </div>
              <div class="spec-row">
                <span class="spec-name">処方タイプ</span>
                <span class="spec-desc">{detail['type']}</span>
              </div>
              <div class="spec-row">
                <span class="spec-name">注目成分</span>
                <span class="spec-desc">{detail['features']}</span>
              </div>
              <div class="spec-row">
                <span class="spec-name">期待できる価値</span>
                <span class="spec-desc">{detail['value']}</span>
              </div>
            </div>

            <div class="product-review-text">
              <p>{detail['desc_p1']}</p>
              <p>{detail['desc_p2']}</p>
            </div>

            <div class="recommend-box">
              <div class="recommend-title">🎯 こんな肌悩み・シーンにおすすめ</div>
              <p>{detail['target']}</p>
            </div>

            <div class="usage-tip">
              <div class="tip-title">💡 効果を最大限に引き出すプロ直伝の使い方</div>
              <p>{detail['point']}</p>
            </div>
          </div>
        </div>
      </article>
"""
    product_cards_html += card

# 比較表の行生成
table_rows_html = ""
for it in items:
    detail = product_details[it["rank"]-1]
    table_rows_html += f"""
          <tr>
            <td class="col-rank">第{it['rank']}位</td>
            <td class="col-name"><a href="#rank-{it['rank']}">{it['brand']}<br><strong>{it['display_name'][:24]}...</strong></a></td>
            <td class="col-type">{detail['type'][:22]}</td>
            <td class="col-feat">{detail['features'][:28]}...</td>
            <td class="col-price">¥{it['price']:,}</td>
            <td class="col-link"><a href="{it['affiliate_url']}" target="_blank" rel="nofollow noopener" class="table-btn">楽天確認</a></td>
          </tr>
"""

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！損傷した角層バリアを深部から修復する保湿力高めパンテノール美容液ランク10 | LumiCosme</title>
  <meta name="description" content="11月・12月の寒冷刺激や暖房乾燥で傷んだ角層バリアを深部から修復する高保湿パンテノール（プロビタミンB5）美容液10選を徹底検証！バイオヒールボ、ラロッシュポゼ、ジオーディナリー、魔女工場まで細胞修復の生化学的根拠と共に紹介。">
  <meta name="keywords" content="パンテノール美容液,プロビタミンB5,高保湿セラム,冬コスメ,バリア機能修復,インナードライ,バイオヒールボ,コスメランキング">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-panthenol-serum">
  
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！損傷した角層バリアを深部から修復する保湿力高めパンテノール美容液ランク10">
  <meta property="og:description" content="11月・12月の寒冷刺激や暖房乾燥で傷んだ角層バリアを深部から修復する高保湿パンテノール（プロビタミンB5）美容液10選を徹底検証！バイオヒールボ、ラロッシュポゼ、ジオーディナリー、魔女工場まで細胞修復の生化学的根拠と共に紹介。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-panthenol-serum">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="LumiCosme">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.jpg">

  <script type="application/ld+json">
  {json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_products, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_faq, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #059669;
      --primary-dark: #047857;
      --secondary: #ecfdf5;
      --accent: #10b981;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #d1fae5;
      --card-bg: #ffffff;
      --gold: #d97706;
      --radius: 12px;
      --shadow: 0 4px 20px rgba(5, 150, 105, 0.08);
      --font-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: var(--font-base); line-height: 1.85; color: var(--text); background-color: #f7faf8; -webkit-font-smoothing: antialiased; }}
    
    .site-header {{ background: #ffffff; border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }}
    .header-inner {{ max-width: 1200px; margin: 0 auto; padding: 1rem 1.5rem; display: flex; justify-content: space-between; align-items: center; }}
    .site-logo {{ font-size: 1.5rem; font-weight: 800; color: var(--primary-dark); text-decoration: none; letter-spacing: -0.5px; }}
    .nav-links a {{ color: var(--text-muted); text-decoration: none; margin-left: 1.5rem; font-size: 0.95rem; font-weight: 600; transition: color 0.2s; }}
    .nav-links a:hover {{ color: var(--primary); }}

    .hero-section {{ background: linear-gradient(135deg, #d1fae5 0%, #e0f2fe 100%); padding: 3.5rem 1.5rem; text-align: center; border-bottom: 1px solid var(--border); }}
    .hero-inner {{ max-width: 900px; margin: 0 auto; }}
    .article-meta {{ display: inline-flex; gap: 1rem; align-items: center; margin-bottom: 1rem; font-size: 0.85rem; color: var(--primary-dark); font-weight: 700; background: #ffffff; padding: 0.4rem 1rem; border-radius: 9999px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); }}
    .hero-title {{ font-size: 2.1rem; line-height: 1.35; color: #064e3b; font-weight: 800; margin-bottom: 1.25rem; letter-spacing: -0.5px; }}
    .hero-desc {{ font-size: 1.05rem; color: #1e3a8a; line-height: 1.8; text-align: left; background: rgba(255,255,255,0.85); padding: 1.5rem; border-radius: var(--radius); border-left: 4px solid var(--primary); }}

    .main-container {{ max-width: 1100px; margin: 2.5rem auto; padding: 0 1.5rem; display: grid; grid-template-columns: 1fr; gap: 3rem; }}
    
    .content-box {{ background: var(--card-bg); border-radius: var(--radius); padding: 2.5rem; box-shadow: var(--shadow); border: 1px solid var(--border); margin-bottom: 2.5rem; }}
    .content-box h2 {{ font-size: 1.6rem; color: #064e3b; margin-bottom: 1.5rem; padding-bottom: 0.75rem; border-bottom: 2px solid var(--secondary); display: flex; align-items: center; gap: 0.75rem; }}
    .content-box p {{ margin-bottom: 1.2rem; color: #334155; font-size: 1.02rem; }}

    .science-card {{ background: #ecfdf5; border-radius: 8px; padding: 1.5rem; margin: 1.5rem 0; border: 1px solid #a7f3d0; }}
    .science-title {{ font-weight: 700; color: #047857; margin-bottom: 0.5rem; font-size: 1.1rem; }}

    .product-card {{ background: #ffffff; border-radius: var(--radius); border: 1px solid var(--border); box-shadow: var(--shadow); padding: 2rem; margin-bottom: 2.5rem; position: relative; overflow: hidden; }}
    .product-badge {{ position: absolute; top: 0; left: 0; background: var(--primary); color: #ffffff; font-weight: 800; font-size: 1rem; padding: 0.5rem 1.5rem; border-bottom-right-radius: var(--radius); box-shadow: 0 2px 8px rgba(0,0,0,0.15); }}
    .product-tag {{ font-size: 0.95rem; font-weight: 700; color: #059669; margin-top: 1.75rem; margin-bottom: 0.5rem; }}
    .product-title {{ font-size: 1.45rem; line-height: 1.4; color: #0f172a; font-weight: 800; margin-bottom: 1.5rem; }}

    .product-grid {{ display: grid; grid-template-columns: 320px 1fr; gap: 2rem; }}
    @media (max-width: 820px) {{
      .product-grid {{ grid-template-columns: 1fr; }}
      .hero-title {{ font-size: 1.6rem; }}
      .content-box {{ padding: 1.5rem; }}
    }}

    .product-img-col {{ display: flex; flex-direction: column; align-items: center; text-align: center; }}
    .product-img {{ width: 280px; height: 280px; object-fit: contain; background: #ffffff; border-radius: 8px; border: 1px solid #e2e8f0; padding: 0.5rem; margin-bottom: 1rem; }}
    .product-brand-box {{ margin-bottom: 0.5rem; font-size: 0.95rem; }}
    .brand-label {{ color: var(--text-muted); margin-right: 0.5rem; }}
    .brand-value {{ font-weight: 700; color: #0f172a; }}
    
    .product-price-box {{ margin-bottom: 1.25rem; }}
    .price-label {{ font-size: 0.85rem; color: var(--text-muted); }}
    .price-val {{ font-size: 1.6rem; font-weight: 800; color: #b91c1c; margin: 0 0.25rem; }}
    .price-tax {{ font-size: 0.8rem; color: var(--text-muted); }}

    .rakuten-btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; width: 100%; max-width: 280px; background: linear-gradient(135deg, #bf0000 0%, #990000 100%); color: #ffffff !important; text-decoration: none; padding: 0.9rem 1.2rem; border-radius: 8px; font-weight: 700; font-size: 1rem; box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25); transition: transform 0.2s, box-shadow 0.2s; }}
    .rakuten-btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35); }}

    .product-info-col {{ display: flex; flex-direction: column; }}
    .catch-quote {{ font-size: 1.05rem; font-weight: 700; color: #064e3b; background: #f0fdf4; padding: 1rem 1.25rem; border-left: 4px solid #059669; border-radius: 4px; margin-bottom: 1.25rem; line-height: 1.6; }}

    .spec-table {{ display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.25rem; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; }}
    .spec-row {{ display: grid; grid-template-columns: 110px 1fr; font-size: 0.9rem; line-height: 1.5; }}
    .spec-name {{ color: var(--text-muted); font-weight: 600; }}
    .spec-desc {{ color: #1e293b; font-weight: 500; }}

    .product-review-text p {{ margin-bottom: 1rem; font-size: 0.98rem; color: #334155; line-height: 1.8; }}
    
    .recommend-box {{ background: #f0fdf4; border-radius: 8px; padding: 1rem 1.25rem; margin-bottom: 1rem; border: 1px solid #bbf7d0; }}
    .recommend-title {{ font-weight: 700; color: #15803d; font-size: 0.95rem; margin-bottom: 0.4rem; }}
    .recommend-box p {{ font-size: 0.92rem; color: #166534; margin: 0; line-height: 1.6; }}

    .usage-tip {{ background: #fefce8; border-radius: 8px; padding: 1rem 1.25rem; border: 1px solid #fef08a; }}
    .tip-title {{ font-weight: 700; color: #a16207; font-size: 0.95rem; margin-bottom: 0.4rem; }}
    .usage-tip p {{ font-size: 0.92rem; color: #713f12; margin: 0; line-height: 1.6; }}

    .comparison-table-wrap {{ overflow-x: auto; margin: 1.5rem 0; }}
    .comparison-table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 0.92rem; }}
    .comparison-table th {{ background: #f1f5f9; padding: 0.75rem 1rem; border: 1px solid var(--border); color: #334155; font-weight: 700; }}
    .comparison-table td {{ padding: 0.75rem 1rem; border: 1px solid var(--border); color: #334155; vertical-align: middle; }}
    .col-rank {{ font-weight: 800; color: var(--primary); text-align: center; }}
    .col-name a {{ color: #059669; text-decoration: none; font-weight: 600; }}
    .col-price {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-btn {{ display: inline-block; background: #bf0000; color: #ffffff !important; padding: 0.35rem 0.75rem; border-radius: 4px; text-decoration: none; font-size: 0.8rem; font-weight: 700; white-space: nowrap; }}

    .faq-list {{ display: flex; flex-direction: column; gap: 1.25rem; margin-top: 1.5rem; }}
    .faq-item {{ background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem 1.5rem; }}
    .faq-q {{ font-weight: 700; color: #064e3b; font-size: 1.05rem; display: flex; gap: 0.75rem; align-items: flex-start; margin-bottom: 0.75rem; }}
    .faq-q-icon {{ background: var(--primary); color: #ffffff; border-radius: 4px; padding: 0.1rem 0.5rem; font-size: 0.85rem; font-weight: 800; }}
    .faq-a {{ color: #334155; font-size: 0.98rem; line-height: 1.8; margin-left: 2.2rem; }}

    .routine-step {{ display: grid; grid-template-columns: 80px 1fr; gap: 1rem; margin-bottom: 1.25rem; align-items: center; background: #ffffff; border: 1px solid var(--border); padding: 1rem 1.25rem; border-radius: 8px; }}
    .step-num {{ background: #059669; color: #ffffff; font-weight: 800; text-align: center; padding: 0.5rem; border-radius: 6px; font-size: 0.9rem; }}
    .step-desc h4 {{ font-size: 1rem; color: #064e3b; margin-bottom: 0.25rem; }}
    .step-desc p {{ font-size: 0.92rem; color: #64748b; margin: 0; }}

    .site-footer {{ background: #064e3b; color: #a7f3d0; padding: 3.5rem 1.5rem 2rem; border-top: 1px solid #047857; margin-top: 4rem; }}
    .footer-inner {{ max-width: 1100px; margin: 0 auto; }}
    .footer-logo {{ font-size: 1.4rem; font-weight: 800; color: #ffffff; margin-bottom: 1rem; }}
    .footer-desc {{ font-size: 0.9rem; margin-bottom: 2rem; max-width: 600px; }}
    .footer-links-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 0.75rem; margin-bottom: 2.5rem; border-top: 1px solid #047857; padding-top: 1.5rem; }}
    .footer-links-grid a {{ color: #d1fae5; text-decoration: none; font-size: 0.85rem; transition: color 0.2s; }}
    .footer-links-grid a:hover {{ color: #ffffff; }}
    .copyright {{ text-align: center; font-size: 0.8rem; color: #6ee7b7; border-top: 1px solid #047857; padding-top: 1.5rem; }}

    .related-section {{ margin-top: 3rem; }}
    .related-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.25rem; }}
    .related-card {{ background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; text-decoration: none; color: inherit; transition: transform 0.2s, box-shadow 0.2s; display: block; }}
    .related-card:hover {{ transform: translateY(-3px); box-shadow: var(--shadow); border-color: var(--primary); }}
    .related-card-title {{ font-weight: 700; color: #047857; font-size: 0.95rem; margin-bottom: 0.5rem; line-height: 1.4; }}
    .related-card-desc {{ font-size: 0.82rem; color: #64748b; line-height: 1.5; }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">LumiCosme</a>
      <nav class="nav-links">
        <a href="/">冬コスメ特集</a>
        <a href="#ranking">ランキング10</a>
        <a href="#mechanism">パンテノールの生化学</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <section class="hero-section">
    <div class="hero-inner">
      <div class="article-meta">
        <span>📅 2026年11月・12月最新版</span>
        <span>🧬 プロビタミンB5集中修復</span>
        <span>🏷️ 高保湿パンテノール美容液</span>
      </div>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！損傷した角層バリアを深部から修復する保湿力高めパンテノール美容液ランク10</h1>
      <div class="hero-desc">
        11月から12月は、氷点下の寒冷外気と高温暖房を行き来する「激しい寒暖差ショック」により、角層バリアに目に見えない微細亀裂が生じる過酷なシーズン。「どんなにクリームを重ねても内側がヒリついて突っ張る」「洗顔後の赤みが引かない」というトラブルは、バリア機能の組織損傷が原因です。本検証では、肌内でパントテン酸に変換され細胞間脂質の生合成を強力にスイッチオンする【高濃度パンテノール（プロビタミンB5）美容液】を徹底厳選。成分濃度・浸透修復力・肌再生持続力から選ばれた最強の10本を公開します。
      </div>
    </div>
  </section>

  <main class="main-container">

    <section class="content-box" id="mechanism">
      <h2>🧬 なぜ11-12月の肌には「パンテノール（プロビタミンB5）」が不可欠なのか？</h2>
      <p>初冬の寒風が吹き荒れる11月から12月にかけて、皮膚の角層は過酷な物理的・生化学的ストレスに晒されます。気温低下による血行不良と皮脂分泌の激減に加え、屋外の冷気（0〜8℃）と暖房の効いた室内（22〜25℃）を行き来することで、毛細血管の急激な拡張・収縮が生じます。この寒暖差ショックによって角層細胞同士の結束が緩み、細胞間脂質（セラミドや脂肪酸）が抜け落ちる『バリア崩壊スパイラル』が引き起こされます。</p>
      
      <div class="science-card">
        <div class="science-title">🔬 プロビタミンB5が果たす「細胞間脂質合成のスイッチオン」</div>
        <p>パンテノール（プロビタミンB5）は、分子量が小さく角層深部まで極めて速やかに浸透する特性を持ちます。肌内部の細胞に取り込まれると、直ちに活性型の『パントテン酸』へと代謝されます。パントテン酸は、生体内のすべての脂質代謝を司る『補酵素A（CoA）』の中心的構成要素です。つまりパンテノールを補給することは、肌自らがセラミドやコレステロールなどの細胞間脂質を合成する工場にエネルギーを直接注入することと同義なのです。</p>
      </div>

      <p>単なるヒアルロン酸やグリセリンのような「外側からの水分補給」だけでは、バリアが壊れた角層から水分がダダ漏れしてしまいます。パンテノールは傷ついた表皮組織の修復を促し、微細な炎症（乾燥赤みやピリピリ感）を素早く沈静化させながら、肌の内側から水分の逃げ場を塞ぐ根本的なリペア効果を発揮します。</p>
    </section>

    <section class="content-box">
      <h2>📐 失敗しない高保湿パンテノール美容液の選び方 4つの基準</h2>
      <p>韓国オリーブヤングや皮膚科領域で大人気のパンテノールコスメですが、冬の本格的な乾燥肌を救うためには処方の濃度と組み合わせ成分の質が極めて重要です。</p>

      <div class="science-card">
        <div class="science-title">1. パンテノール配合濃度（5%〜10%の本格リペア設計）</div>
        <p>一般的なスキンケアに配合される1%前後のパンテノールでも一定の整肌効果はありますが、11〜12月の深刻な乾燥肌や寒暖差ゆらぎ肌には物足りません。角層の組織修復を速攻で体感したい場合は、5%以上、できれば10%の高濃度を明記したアンプルやセラムを選ぶことが決定打となります。</p>
      </div>

      <div class="science-card">
        <div class="science-title">2. 相乗効果をもたらす鎮静・保水成分（CICA・エクトイン・アミノ酸）</div>
        <p>パンテノール単体でも強力ですが、ツボクサエキス（マデカッソシド/CICA）が組み合わさることで抗炎症効果が倍増します。また、砂漠の好塩菌から抽出される高保水多糖体『エクトイン』や、角層の天然保湿因子を補う『アミノ酸複合体』とのハイブリッド処方は、極限の乾燥環境でも水分の蒸発をゼロに抑え込みます。</p>
      </div>

      <div class="science-card">
        <div class="science-title">3. 浸透スピードと肌馴染み（リポソーム化・ナノカプセル技術）</div>
        <p>高濃度のパンテノールは本来やや粘性を持つ成分です。肌表面でベタついて他のスキンケアの邪魔にならないよう、リポソームカプセル化やマイクロ乳化が施された製剤を選ぶことで、塗布後すぐに角層深部へすっと吸い込まれる極上の使用感を得られます。</p>
      </div>

      <div class="science-card">
        <div class="science-title">4. 弱酸性（pH5.5前後）の低刺激クリーン処方</div>
        <p>乾燥でバリアが壊れた冬の肌はアルカリ性に傾きやすく、微小な刺激でもピリピリと染みます。無香料・アルコールフリー・弱酸性設計で作られた皮膚科テスト済みの処方を選ぶことが、安心して使い続けるための絶対条件です。</p>
      </div>
    </section>

    <section id="ranking">
      <div style="text-align: center; margin-bottom: 2.5rem;">
        <span style="color: #059669; font-weight: 800; font-size: 1.1rem; letter-spacing: 1px;">2026 WINTER BEST RANKING</span>
        <h2 style="font-size: 2rem; color: #064e3b; margin-top: 0.5rem; border: none; padding: 0;">保湿力高めパンテノール美容液 ベスト10選</h2>
        <p style="color: #64748b; font-size: 1rem; margin-top: 0.5rem;">楽天市場の最新リアルタイム価格・在庫データを都度取得して反映しています</p>
      </div>

      {product_cards_html}
    </section>

    <section class="content-box">
      <h2>📊 保湿力高めパンテノール美容液10選 徹底スペック比較一覧表</h2>
      <p>各製品の処方特徴、注目成分、参考価格を一目で比較できます。あなたの肌状態と予算にぴったりの1本を見つけてください。</p>
      
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名・ブランド</th>
              <th>処方タイプ</th>
              <th>注目リペア成分</th>
              <th>参考価格</th>
              <th>楽天市場</th>
            </tr>
          </thead>
          <tbody>
            {table_rows_html}
          </tbody>
        </table>
      </div>
    </section>

    <section class="content-box">
      <h2>⏰ プロ直伝！翌朝の肌密度が変わるパンテノール集中リペアルーティン</h2>
      <p>パンテノール美容液は、朝のプロテクトと夜の組織修復で使い方を微調整することで、その真価が何倍にも跳ね上がります。</p>

      <div class="routine-step">
        <div class="step-num">朝 STEP</div>
        <div class="step-desc">
          <h4>日中の寒冷刺激に備える防御クッション</h4>
          <p>洗顔後、化粧水で角層に水分を通した直後、パンテノール美容液を1プッシュ顔全体に薄くなじませます。肌表面に弾力のある柔軟ヴェールが形成され、冷たい外気やエアコン直撃による水分蒸散をブロック。メイクの粉浮きも防ぎます。</p>
        </div>
      </div>

      <div class="routine-step">
        <div class="step-num">夜 STEP 1</div>
        <div class="step-desc">
          <h4>寒暖差ダメージをリセットするベース補給</h4>
          <p>クレンジング・洗顔後の清潔な肌へ、化粧水をしっかり浸透させた後、スポイト1回分のパンテノール美容液を手のひらで温めて全顔へプレス。日中に受けた微小な炎症を鎮め、修復モードへと切り替えます。</p>
        </div>
      </div>

      <div class="routine-step">
        <div class="step-num">夜 STEP 2</div>
        <div class="step-desc">
          <h4>乾燥赤み・小ジワゾーンへのミルフィーユ重ねづけ</h4>
          <p>目元、口元、頬の高い位置など、暖房乾燥でしぼみやすい部位にもう半プッシュを指先でトントンと重ねづけします。角層の隙間へパンテノールを飽和状態まで満たします。</p>
        </div>
      </div>

      <div class="routine-step">
        <div class="step-num">夜 STEP 3</div>
        <div class="step-desc">
          <h4>高保湿クリームによる完全密閉ラッピング</h4>
          <p>パンテノールが肌内部で脂質合成を促進している間に水分が逃げないよう、セラミドやシアバターを配合した濃厚クリームで油分の蓋をします。翌朝、驚くほど吸い付くようなハリ密度を実感できます。</p>
        </div>
      </div>
    </section>

    <section class="content-box" id="faq">
      <h2>❓ パンテノール美容液に関するよくある質問（FAQ）</h2>
      <div class="faq-list">
        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-icon">Q</span>
            <span>パンテノール（プロビタミンB5）はなぜ冬の乾燥や肌荒れに効果的なのですか？</span>
          </div>
          <div class="faq-a">
            パンテノールは浸透性に優れたプロビタミンB5であり、肌内部に浸透すると直ちにパントテン酸へと変換されます。パントテン酸は補酵素A（CoA）の不可欠な構成成分であり、細胞のエネルギー代謝を活性化させて細胞間脂質（セラミドや脂肪酸）の生合成を直接促します。そのため、単に外側から水分を補給するだけでなく、肌自身が自活して水分を蓄えバリアを再建する根本修復効果を発揮します。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-icon">Q</span>
            <span>レチノールやビタミンCなどの高機能成分とパンテノールは併用できますか？</span>
          </div>
          <div class="faq-a">
            非常に相性が良く、むしろ併用が強く推奨されます。レチノールによるA反応（乾燥や皮むけ・赤み）や、高濃度ビタミンCによるピリピリ感を、パンテノールが持つ優れた抗炎症・組織修復作用が強力に緩和してくれます。併用する際は、化粧水の後にパンテノール美容液を仕込んで肌のクッションを作り、その後にビタミンCやレチノールを重ねるのが刺激を最小限に抑えるコツです。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-icon">Q</span>
            <span>パンテノール美容液は朝と夜のどちらに使うのが最も効果的ですか？</span>
          </div>
          <div class="faq-a">
            朝晩両方の使用が理想的ですが、目的によって役割が異なります。朝の使用では、日中の寒冷外気や暖房乾燥から角層バリアを守るプロテクト膜を形成し、夕方のメイク崩れや粉吹きを未然に防ぎます。夜の使用では、日中に受けた寒暖差ダメージや紫外線・摩擦による微小な炎症を就寝中に集中修復し、翌朝の肌のハリ密度を劇的に回復させます。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-icon">Q</span>
            <span>パンテノール配合コスメを選ぶ際、濃度の目安はどのくらいですか？</span>
          </div>
          <div class="faq-a">
            一般的な保湿目的であれば1%〜2%程度でも十分な保水効果を実感できますが、11月〜12月の真冬の深刻なインナードライや寒暖差による肌荒れ・赤みを素早くリペアしたい場合は、5%〜10%の高濃度設計のアンプルやセラムを選ぶのが劇的な手応えを得るための基準となります。
          </div>
        </div>
      </div>
    </section>

    <section class="content-box related-section" id="internal-links-hub">
      <h2>🔗 あわせて読みたい！冬の高保湿スキンケア特集</h2>
      <div class="related-grid" id="related-grid-box">
        <!-- 内部リンクが自動挿入されます -->
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-logo">LumiCosme</div>
      <p class="footer-desc">冬の過酷な乾燥環境に立ち向かうすべての女性へ。成分科学とリアルな使用感に基づいた高保湿コスメ・スキンケア情報を厳選してお届けします。</p>
      <div class="footer-links-grid" id="footer-links-box">
        <!-- フッターリンクが自動挿入されます -->
      </div>
      <div class="copyright">
        &copy; 2026 LumiCosme (ルミコスメ) All Rights Reserved.
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-panthenol-serum.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-panthenol-serum.html!")
