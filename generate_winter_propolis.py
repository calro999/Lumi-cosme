import json
import re

with open("fetched_3new_nov_dec_proteoglycan_propolis_galactomyces_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_propolis"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 韓国ドクターズコスメの絶対王者！高純度プロポリスエキスが叶える極上の蜜光ツヤ肌",
        "catch": "暖房の乾燥に負けない濃厚密着ヴェール。粉吹き肌を瞬時に満たしツヤとハリを取り戻す名品アンプル",
        "brand_name": "CNP Laboratory (チャアンドパク)",
        "capacity": "15ml (プロポリス エナジー アクティブ アンプル)",
        "type": "高純度プロポリス高濃縮エナジーアンプル",
        "features": "高純度プロポリスエキス配合、ヒアルロン酸Na、β-グルカン、マデカッソシド、パラベン・ミネラルオイルフリー",
        "value": "皮膚科医プロデュースによる濃密処方。冬の冷えや乾燥で元気を失った肌細胞にアミノ酸とミネラルを送り込み、内側から発光するような水光ツヤを長時間維持する",
        "desc_p1": "11月から12月にかけて気温が下がり、湿度が急落すると、肌の皮脂分泌が激減してカサカサの粉吹きやツヤ不足に陥ります。韓国発の本格ドクターズコスメとして冬の乾燥肌から絶大な支持を集めるCNPのプロポリスアンプルは、蜂の巣から採取された上質なプロポリスエキスを高濃度に閉じ込めた集中保湿美容液です。",
        "desc_p2": "蜂蜜のようにとろりとした黄金色のテクスチャーですが、肌に伸ばすとスルスルと吸い付くように広がり、嫌なベタつきを残さずピタッと密着します。ヒアルロン酸やβ-グルカンが角層深部に水分を送り届けると同時に、プロポリスの濃厚な保護膜が肌表面に薄い蜜膜シールドを形成。暖房直撃のオフィス環境でも夕方までみずみずしいツヤ感が一切衰えません。メイク前のファンデーションに1滴混ぜる裏技も大人気です。",
        "target": "冬になると肌のツヤが完全に失われくすむ方、ファンデーションが粉を吹いて密着しない方、肌荒れと乾燥を同時にケアしたい敏感肌",
        "point": "化粧水で肌を整えた後、スポイトで1〜2滴を取り、手のひらで包み込むようにハンドプレスします。メイク前にリキッドファンデーションやBBクリームに1滴混ぜると、冬でも乾燥知らずのうるツヤ水光肌に仕上がります。"
    },
    {
        "rank": 2,
        "tag": "🍯 黒蜂プロポリスエキス83.25%の超高配合！水で薄めない贅沢処方で荒れた肌バリアを集中補修",
        "catch": "全成分の8割以上が黒蜂の恵み。冬の冷風で赤みやヒリつきを起こした肌を優しく鎮静・密封",
        "brand_name": "COSRX (コスアールエックス)",
        "capacity": "30ml (フルフィット プロポリス ライト アンプル)",
        "type": "黒蜂プロポリス高濃度鎮静保湿セラム",
        "features": "黒蜂プロポリスエキス83.25%、自然由来カッシア種子エキス、ヒアルロン酸、人工香料・人工着色料・アルコールフリー",
        "value": "精製水ベースではなくプロポリスエキスを高純度ベースとして使用。圧倒的な成分濃度で、真冬の寒暖差によるゆらぎ肌をふっくらモチモチに立て直す",
        "desc_p1": "真冬の外気温と暖房の効いた室内との極端な寒暖差は、肌の毛細血管を刺激し、赤みやヒリつきなどの乾燥トラブルを誘発します。COSRXのフルフィット プロポリス ライト アンプルは、厳しい寒さに耐え抜く黒蜂が作り出したプロポリスエキスを83.25%という圧倒的な高比率で配合した贅沢アンプルです。",
        "desc_p2": "名前の通り『ライト』で軽やかな肌馴染みを実現しながら、肌の奥底まで届く保湿力は超濃厚。プロポリス特有の抗菌・抗酸化フラボノイドが角層の微小な肌荒れを優しく鎮め、荒れたキメを整えます。塗布した翌朝は肌が手のひらに吸い付くような弾力と柔らかさが生まれ、洗顔後の肌がつるんと滑らかに整うのを実感できます。",
        "target": "重たいオイルやクリームが苦手だが真冬の乾燥を防ぎたい方、肌荒れや赤みが出やすい敏感肌、高濃度成分にこだわりたい方",
        "point": "朝晩の化粧水後、適量を顔全体に優しく塗り広げます。乾燥が気になる頬や口元には少量を重ねづけし、軽くパッティングして馴染ませると浸透が高まります。"
    },
    {
        "rank": 3,
        "tag": "🏺 熟成プロポリス63%発酵バリア！乳酸菌発酵の力で角層深部まで栄養を浸透させる発酵美容液",
        "catch": "30日間の熟成・発酵でパワーアップ。冬のゴワついた角層を柔らかくほぐし潤いを閉じ込める",
        "brand_name": "SKINFOOD (スキンフード)",
        "capacity": "50ml (ロイヤルハニー プロポリス エンリッチ エッセンス)",
        "type": "熟成発酵プロポリス高保湿エッセンス",
        "features": "熟成黒蜂プロポリス抽出物63%、熟成ローヤルゼリー抽出物10%、発酵蜂蜜抽出物10%",
        "value": "原料を30日間じっくり発酵・熟成させる独自工法を採用。分子が細分化されるため角層への浸透力が格段に向上し、冬枯れ肌のバリアを強固に再構築する",
        "desc_p1": "冬の乾燥肌は角質層が硬化して成分が浸透しにくくなるため、浸透性の高さが保湿ケアの鍵を握ります。スキンフードのロイヤルハニー プロポリス エンリッチ エッセンスは、プロポリス・ローヤルゼリー・ハチミツの3大ミツバチ恵み成分を30日間発酵熟成させ、粒子を極限まで微細化した本格エイジング保湿美容液です。",
        "desc_p2": "とろみのあるスポイトから出されたエッセンスは、肌に乗せた瞬間にスルスルとほどけるように角層深部へ浸透。発酵成分が乱れた肌の美肌菌バランスを整えながら、うるおいの持続力を最大化します。50mlの大容量なので、真冬の間惜しみなく朝晩使用でき、乾燥による小ジワやキメの乱れを根本からケアできます。",
        "target": "冬場に化粧水や美容液の肌なじみが悪く感じる方、50mlでたっぷりコスパ良く使いたい方、発酵コスメのハリ感を実感したい方",
        "point": "キャップを回すと自動で1回分が吸い上がるオートスポイトを採用。洗顔後の化粧水で肌を整えた後、顔全体に滑らせるように馴染ませてください。"
    },
    {
        "rank": 4,
        "tag": "🧬 プロポリス×乳酸菌ペプチドの先進リフティング！毛穴のたるみと冬のしぼみ肌を立体引き締め",
        "catch": "韓国オリーブヤング大ヒットの弾力セラム。乾燥で開いた毛穴をキュッと引き締める高保湿エイジングケア",
        "brand_name": "BIOHEAL BOH (バイオヒールボ)",
        "capacity": "30ml (プロバイオダーム タイトニング コラーゲン セラム)",
        "type": "プロポリス＆マイクロバイオーム弾力美容液",
        "features": "プロポリスエキス、特許成分プロバイオダーム（乳酸菌発酵物）、低分子コラーゲン、12種のペプチド複合体",
        "value": "バイオテクノロジーから生まれた美肌菌成分とプロポリスが融合。冬の乾燥によって弾力を失った皮膚構造を内側から引き上げ、毛穴の目立たないハリ肌へ",
        "desc_p1": "冬の乾燥は単なるカサつきにとどまらず、肌の真皮構造を支える弾力繊維を脆弱化させ、毛穴の開きやフェイスラインのたるみを加速させます。バイオヒールボのコラーゲンセラムは、プロポリスの濃密保水力に特許成分のマイクロバイオーム乳酸菌と12種のペプチドを配合した先進セラムです。",
        "desc_p2": "カプセル状の美容成分が肌の上ではじけ、濃密な潤いヴェールで肌をタイトに引き締めます。プロポリスが寒風から肌を守る保護膜を形成し、ペプチドが角層の弾力タンクを充填。使った瞬間から肌が上向きに引き上がるような心地よいテンションを感じられ、乾燥によるメイク崩れや毛穴落ちを完璧にブロックします。",
        "target": "冬の乾燥とともに毛穴の開きやフェイスラインの緩みが気になる方、高機能ペプチドとプロポリスの相乗効果を求める方",
        "point": "化粧水のあと、適量を取り頬やフェイスラインを下から上へ持ち上げるように馴染ませます。毛穴が気になる小鼻や眉間には指先で円を描くように塗り込むと引き締め効果が高まります。"
    },
    {
        "rank": 5,
        "tag": "🐌 ロイヤルゼリー×プロポリス×濃密黒カタツムリ！冬の過酷な肌枯れを立て直す大容量ファーストアンプル",
        "catch": "165mlのメガサイズで贅沢保湿。洗顔後の最初の1滴で冬の乾燥砂漠肌をオアシスへと変える",
        "brand_name": "Dr.G (ドクタージー)",
        "capacity": "165ml (ロイヤルブラックスネイル ファーストアンプル)",
        "type": "大容量プロポリス導入ブースターアンプル",
        "features": "プロポリスエキス、ローヤルゼリー、黒カタツムリムチン、ナイアシンアミド配合",
        "value": "165mlという大容量設計で、洗顔直後のブースターとして首やデコルテまで惜しみなく使用可能。カタツムリムチンとプロポリスが乾燥によるダメージを即時リペアする",
        "desc_p1": "冬のスキンケアにおいて『洗顔後最初の1分間』の乾燥対策は極めて重要です。ドクタージーのロイヤルブラックスネイル ファーストアンプルは、栄養価の高いプロポリスとローヤルゼリー、そして驚異的な保水・修復力を持つ黒カタツムリ成分を融合させたファーストステップ美容液です。",
        "desc_p2": "165mlという化粧水並みのビッグサイズでありながら、中身はれっきとした高濃度アンプル。とろみのあるテクスチャーが肌に伸ばした瞬間にスーッとほどけ、角層の水分保持力を瞬時に底上げします。ナイアシンアミド配合により冬のくすみも同時にブライトニングし、冴えた透明感のある素肌へと導きます。",
        "target": "洗顔後すぐに肌が突っ張る方、首やデコルテまでたっぷりアンプルで保湿したい方、透明感と弾力を同時に手に入れたい方",
        "point": "洗顔直後の無垢な肌に、500円玉大を手にとって顔全体から首元まで伸ばします。手で優しくパッティングして浸透させた後、通常のスキンケアに進んでください。"
    },
    {
        "rank": 6,
        "tag": "🌿 希少なブラジル産グリーンプロポリス採用！寒さでゆらぐ冬肌を植物の生命力で守る鎮静セラム",
        "catch": "抗酸化フラボノイドが最高水準。冬の冷気やマスク摩擦で荒れやすい肌を穏やかに整える",
        "brand_name": "NATURE REPUBLIC (ネイチャーリパブリック)",
        "capacity": "50ml (ハーブオロジー プロポリス エナジー セラム)",
        "type": "グリーンプロポリス鎮静高保湿セラム",
        "features": "ブラジル産最高級グリーンプロポリスエキス、CICA（ツボクサエキス）、ハーブ複合処方",
        "value": "一般的なプロポリスよりもフラボノイド含有量が高いとされるグリーンプロポリスを厳選。冬の外的刺激に負けない強靭な角層バリアを育てる",
        "desc_p1": "過酷な自然界で生き抜くブラジルの蜂が生み出す『グリーンプロポリス』は、フラボノイドの一種であるアルテピリンCを豊富に含み、プロポリスの中でも最高峰の抗酸化力を誇ります。ネイチャーリパブリックはこの希少なグリーンプロポリスを贅沢に配合しました。",
        "desc_p2": "みずみずしく清涼感のあるテクスチャーで、塗布した瞬間に肌の赤みや熱感を穏やかに鎮めながら、深い潤いで角層を満たします。ツボクサエキス（CICA）との相乗効果により、真冬の寒風やマフラー・マスクによる摩擦で弱った皮膚をいたわり、健やかなツヤ肌へと導きます。",
        "target": "冬の冷風で頬が赤くなりやすい方、ベタつきのない高保湿美容液を探している方、自然派ハーブの力で肌荒れを防ぎたい方",
        "point": "化粧水の後に2〜3滴を手にとり、肌を擦らないように優しくハンドプレスします。赤みが気になる頬には重ねて馴染ませてください。"
    },
    {
        "rank": 7,
        "tag": "✨ 24K純金ゴールド×発酵プロポリス！真冬の冷えによるくすみを吹き飛ばすリッチな黄金アンプル",
        "catch": "ゴールドの輝きが溶け込む濃密ジェル。血行不良で沈んだ冬の素肌に血色感と極上のツヤを宿す",
        "brand_name": "TONYMOLY (トニーモリー)",
        "capacity": "100ml (インテンス ケア ゴールド 24K スネール アンプル)",
        "type": "24K純金＆発酵プロポリス高保湿アンプル",
        "features": "24Kゴールド粉末、発酵プロポリスエキス、発酵カタツムリ粘液ろ過物、高麗人参エキス",
        "value": "純度99.9%の24K純金とプロポリスが融合。微弱電流効果で冬の滞りがちな肌代謝をサポートし、くすんだ肌を生き生きとした輝きで満たす",
        "desc_p1": "12月の寒さが本格化すると、毛細血管の収縮によって顔色が悪くなり、肌が土気色にくすんで見えがちです。トニーモリーのインテンスケアゴールドアンプルは、贅沢な24K純金箔と発酵プロポリスをブレンドした見た目にも華やかなエイジングケアアンプルです。",
        "desc_p2": "キラキラと輝く純金ゴールドが肌の温度でなめらかに溶け込み、プロポリスの栄養成分とともに角層奥深くまで浸透します。高麗人参エキスの活力サポートも加わり、冬の寒さに負けない生き生きとした血色感とハリツヤが素肌に宿ります。100mlという大容量で贅沢に使い続けられる点も魅力です。",
        "target": "冬になると顔色が冴えずどんよりくすむ方、ゴージャスな使用感でテンションを上げたい方、首元までエイジングケアしたい方",
        "point": "適量を手のひらに取り、金箔を潰すように両手ですり合わせてから顔全体に広げます。フェイスラインをマッサージしながら馴染ませると血行促進効果が高まります。"
    },
    {
        "rank": 8,
        "tag": "💛 カプセル密閉で鮮度をキープ！プロポリス×24Kゴールドの洗い流し集中ツヤパック",
        "catch": "1回分ずつ新鮮な蜜膜マスク。週1〜2回のスペシャルケアで乾燥・ゴワつきを一気にリセット",
        "brand_name": "VT COSMETICS (ブイトーク)",
        "capacity": "10個入 (プログロス ゴールド カプセル マスク)",
        "type": "プロポリス＆ゴールド集中トリートメントパック",
        "features": "ゴールドハニープログロス処方（プロポリス・ローヤルゼリー・24Kゴールド）、洗い流すクレイ＆クリームタイプ",
        "value": "個包装カプセルにより成分の酸化を防ぎ、毎回搾りたてのような新鮮なプロポリスの栄養を肌にチャージ。真冬のゴワついた古い角質を吸着しながら濃密保湿する",
        "desc_p1": "冬の寒さと乾燥で角質肥厚を起こした肌は、美容液をいくら塗っても弾かれてしまいます。VTのプログロス ゴールド カプセル マスクは、不要な角質を穏やかに整えながらプロポリスの濃密な栄養を送り込む、洗い流すタイプの贅沢フェイシャルマスクです。",
        "desc_p2": "ゴールドに輝くもっちりとしたテクスチャーが肌にピタッと密着し、10〜15分置く間に肌内部へうるおいをじっくり閉じ込めます。ぬるま湯で洗い流した瞬間、まるで磨き上げた陶器のように滑らかで、ハチミツの膜を張ったようなぷるんとした弾力肌が現れます。週末のご褒美ケアに最適です。",
        "target": "冬の乾燥で肌がゴワつき化粧ノリが最悪な方、週に1回の集中スペシャルケアで肌をリセットしたい方、個包装で旅行にも持参したい方",
        "point": "洗顔後、水気を拭き取った肌に目元・口元を避けて顔全体に均一に塗り広げます。10〜15分後にぬるま湯で優しく洗い流し、その後に通常のスキンケアを行ってください。"
    },
    {
        "rank": 9,
        "tag": "🐝 ミツバチの花粉（ビーポレン）エキス40%！高密度カプセルが弾ける濃厚抗酸化アンプル",
        "catch": "プロポリスを上回る栄養密度のスーパーフード。真冬の過酷な乾燥環境でも潤いが枯れない肌へ",
        "brand_name": "MISSHA (ミシャ)",
        "capacity": "40ml (ビーポレン リニュー アンプラー)",
        "type": "ビーポレン＆プロポリス超濃厚アンプラー",
        "features": "ビーポレン（花粉エキス）40%、グリーンプロポリスエキス、エーデルワイスカルス培養エキス、低刺激処方",
        "value": "ミシャ独自の『アンプラー』技術により、アンプルを超える粘りと濃密さを実現。糸を引くような濃厚エキスが肌表面に強力な保湿膜を形成する",
        "desc_p1": "ミツバチが自らの唾液と花粉を練り固めて作る『ビーポレン』は、タンパク質・アミノ酸・ビタミンが凝縮された天然のマルチ栄養素です。ミシャのビーポレン リニュー アンプラーは、このビーポレンエキスを40%も配合した超濃厚美容液です。",
        "desc_p2": "指に取るとトルコアイスのように糸を引く独特の粘性がありますが、肌に伸ばすと不思議なほど素早く馴染み、ベタつきを残さずピンとしたハリ膜を形成します。プロポリスとエーデルワイスエキスの相乗効果で、暖房直撃の過酷なオフィス環境でも乾燥を寄せ付けず、ふっくらとした若々しい素肌をキープします。",
        "target": "通常の美容液では保湿力が全く足りない超乾燥肌の方、糸引くほどの濃密なテクスチャーが好きな方、肌の弾力低下が深刻な方",
        "point": "化粧水の後、スポイトで適量を取り顔全体にスタンプを押すように優しく密着させます。手のひらの体温で押し込むと、肌の奥へ吸い込まれるように浸透します。"
    },
    {
        "rank": 10,
        "tag": "👑 生ローヤルゼリーカプセルが弾ける！プチプラで毎日使える蜜膜シールド導入エッセンス",
        "catch": "目に見える美容カプセルが角層で溶け出す。冬の乾燥肌にみずみずしい潤いと栄養をチャージ",
        "brand_name": "HOLIKA HOLIKA (ホリカホリカ)",
        "capacity": "50ml (ハニーロイヤルカプセル エッセンス)",
        "type": "ローヤルゼリーカプセル配合プロポリスエッセンス",
        "features": "プロポリスエキス、生ローヤルゼリー抽出カプセル、ハチミツエキス、天然保湿オイル",
        "value": "ボトルの中に浮かぶ黄金のローヤルゼリーカプセルが、ポンプを押すたびに弾けて新鮮な状態で肌へ届く。プチプラながら贅沢な蜜膜ケアを実現",
        "desc_p1": "冬の乾燥肌を毎日手軽にケアしたい方にぴったりなのが、ホリカホリカのハニーロイヤルカプセル エッセンスです。ボトルの中に浮かぶ無数の黄金カプセルが印象的で、使うたびにスキンケアが楽しくなる高コスパ美容液です。",
        "desc_p2": "肌に伸ばすとカプセルが体温でスーッと溶け、プロポリスとローヤルゼリーの濃厚な栄養成分が一気に放出されます。みずみずしいジェルベースのため、朝のメイク前でもヨレることなくスムーズに使用可能。一日中乾かないツヤ肌のベース作りを強力にアシストします。",
        "target": "カプセル入りの新感覚コスメを楽しみたい方、プチプラで毎日気兼ねなくプロポリスを取り入れたい方、朝の保湿ケアを時短したい方",
        "point": "朝晩の化粧水の後に1〜2プッシュを手に取り、カプセルを優しく潰しながら顔全体に塗り広げます。首や手元にもサッと伸ばすと乾燥小ジワを予防できます。"
    }
]

# JSON-LD構造化データ作成
faq_data = [
    {
        "q": "プロポリスとはどのような成分ですか？ハチミツやローヤルゼリーとの違いは何ですか？",
        "a": "プロポリスは、ミツバチが樹木の樹液や新芽を集め、自らの唾液酵素と混ぜ合わせて作る天然の防御物質です。巣の無菌状態を保つために使われるため、極めて高い抗菌・抗酸化作用とフラボノイド、アミノ酸、ミネラルを含みます。『ハチミツ＝糖分主体で水分を抱え込む保湿成分』『ローヤルゼリー＝女王蜂の栄養源でアミノ酸主体のエイジングケア成分』であるのに対し、『プロポリス＝肌荒れを防ぎ、天然の蜜膜シールドで水分蒸散と外的刺激を遮断する成分』という明確な違いがあります。11月・12月の冬の肌荒れ・粉吹きに最も頼もしい成分です。"
    },
    {
        "q": "プロポリスアンプルを使うと肌がベタつくことはありませんか？朝のメイク前にも使えますか？",
        "a": "多くの最新プロポリスアンプル（CNPやCOSRXなど）は、蜂蜜のような濃厚な見た目でありながら、肌に伸ばすと瞬時に角層へ浸透し、表面はサラリと吸い付くような水光ヴェールに変化するよう高度に設計されています。朝のメイク前にも全く問題なく使用でき、むしろファンデーションの密着度を高めて日中の暖房乾燥による粉吹きやヨレを強力に防いでくれます。"
    },
    {
        "q": "蜂アレルギーや敏感肌でもプロポリスコスメは使用できますか？",
        "a": "プロポリスはミツバチ由来の天然成分であるため、重度の蜂アレルギーやハチ毒に敏感な体質の方は注意が必要です。ただし、化粧品グレードに精製されたプロポリスエキスは不純物やアレルゲンが大幅に低減されています。敏感肌の方は、まず耳の後ろや二の腕の内側で24時間のパッチテストを行ってから顔に使用することをおすすめします。"
    },
    {
        "q": "プロポリスアンプルはスキンケアのどのステップで使うのが最も効果的ですか？",
        "a": "基本的に『化粧水の後、乳液やクリームの前』に使用するのが黄金ルールです。化粧水で角層にたっぷりと水分を補給した直後にプロポリスアンプルを重ねることで、プロポリスの蜜膜成分が水分を閉じ込め、その後の乳液・クリームの密閉効果を倍増させます。超乾燥肌の方は、洗顔直後のブースターとして使用するのも非常に効果的です。"
    },
    {
        "q": "11月・12月の真冬にプロポリスコスメで『水光ツヤ肌』を一日中キープする裏技は？",
        "a": "リキッドファンデーションやBBクリームを手の甲に出し、プロポリスアンプルを『1滴だけ』垂らして指先でしっかり混ぜ合わせてから肌に塗布するテクニックが美容のプロの間で大人気です。ベースメイク自体の保湿力と密着度が劇的に底上げされ、真冬の乾燥したオフィスでも粉吹きせず、内側から自然に発光するような極上のツヤ肌が一日中持続します。"
    }
]

schema_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！濃密な栄養と蜜膜ヴェールで肌荒れ・粉吹きを防ぐ高保湿プロポリスアンプルランク10",
    "description": "11月・12月の真冬乾燥・粉吹き・くすみに！濃密な栄養と蜜膜ヴェールで肌荒れを防ぎ極上の水光ツヤ肌を叶える高保湿プロポリスアンプル10選を徹底比較。CNP、COSRX、スキンフード、バイオヒールボなど厳選。",
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
        "@id": "https://lumi-cosme.vercel.app/winter-propolis"
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
            "name": "高保湿プロポリスアンプルランク10",
            "item": "https://lumi-cosme.vercel.app/winter-propolis"
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
  <title>保湿力の強さで肌乾燥とさようなら！濃密な栄養と蜜膜ヴェールで肌荒れ・粉吹きを防ぐ高保湿プロポリスアンプルランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の真冬乾燥に！濃密な栄養と蜜膜ヴェールで肌荒れ・粉吹きを防ぎ極上の水光ツヤ肌を叶える高保湿プロポリスアンプル10選を徹底比較！CNP、COSRX、スキンフード、バイオヒールボなど厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-propolis">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- OGP -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！濃密な栄養と蜜膜ヴェールで肌荒れ・粉吹きを防ぐ高保湿プロポリスアンプルランク10 | 冬コスメ徹底比較ラボ">
  <meta property="og:description" content="11月・12月の真冬乾燥に！濃密な栄養と蜜膜ヴェールで肌荒れ・粉吹きを防ぎ極上の水光ツヤ肌を叶える高保湿プロポリスアンプル10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-propolis">
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
      --primary: #d97706;
      --primary-light: #fef3c7;
      --primary-dark: #b45309;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --bg-light: #fffbeb;
      --border-color: #fde68a;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --card-hover-shadow: 0 10px 15px -3px rgba(217, 119, 6, 0.12), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
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
      background-color: #fdfbf7;
    }}

    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid #fed7aa;
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
      border: 1px solid #fef3c7;
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
      color: #78350f;
      margin-bottom: 1.5rem;
    }}

    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #fde68a;
    }}

    .lead-box {{
      background: #fffbeb;
      border-left: 4px solid var(--primary);
      padding: 1.5rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 2.5rem;
      font-size: 1.05rem;
      line-height: 1.8;
      color: #92400e;
    }}

    .section-title {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #78350f;
      margin: 3rem 0 1.5rem 0;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .product-card {{
      background: #ffffff;
      border: 1px solid #fde68a;
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
      background: #d97706;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.9rem;
      padding: 0.25rem 1rem;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(217, 119, 6, 0.3);
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
      border: 1px solid #fde68a;
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
      border-bottom: 1px dashed #fde68a;
    }}

    .price-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #b45309;
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
      background: #fffbeb;
      border: 1px solid #fde68a;
      color: #92400e;
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
      background: linear-gradient(135deg, #d97706, #b45309);
      color: #ffffff;
      font-weight: 700;
      font-size: 1rem;
      padding: 0.85rem 2rem;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(217, 119, 6, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 420px;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 12px -2px rgba(217, 119, 6, 0.35);
      background: linear-gradient(135deg, #f59e0b, #d97706);
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
      border: 1px solid #fde68a;
      text-align: left;
    }}

    .comparison-table th {{
      background: #fffbeb;
      color: #78350f;
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
      color: #b45309;
      white-space: nowrap;
    }}

    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin: 2rem 0;
    }}

    .faq-item {{
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-radius: 8px;
      padding: 1.25rem;
    }}

    .faq-q {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-weight: 700;
      font-size: 1rem;
      color: #78350f;
      margin-bottom: 0.5rem;
    }}

    .faq-q-badge {{
      background: #d97706;
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
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-radius: 12px;
      padding: 2rem;
      margin-top: 3rem;
    }}

    .internal-links-title {{
      font-size: 1.2rem;
      font-weight: 700;
      color: #78350f;
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
      border: 1px solid #fde68a;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      text-decoration: none;
      color: #334155;
      font-size: 0.9rem;
      font-weight: 500;
      transition: all 0.2s ease;
    }}

    .internal-link:hover {{
      border-color: #d97706;
      color: #d97706;
      transform: translateY(-2px);
      box-shadow: 0 2px 4px rgba(217, 119, 6, 0.1);
    }}

    .site-footer {{
      background: #ffffff;
      border-top: 1px solid #fed7aa;
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
      <span style="font-size: 0.85rem; color: #b45309;">2026年最新 保湿ランキング</span>
    </div>
  </header>

  <main class="container">
    <article class="article-wrap">
      <div class="breadcrumb">
        <a href="/">ホーム</a> &gt; <span>高保湿プロポリスアンプルランク10</span>
      </div>

      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！濃密な栄養と蜜膜ヴェールで肌荒れ・粉吹きを防ぐ高保湿プロポリスアンプルランク10</h1>

      <div class="article-meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証カテゴリー: 高保湿アンプル・プロポリス美容液</span>
        <span>監修: 冬コスメ徹底比較ラボ 編集部</span>
      </div>

      <div class="lead-box">
        <strong>【11月・12月の冬本番に深刻化する肌荒れ・粉吹き・ツヤ枯れを根本解決！】</strong><br>
        木枯らしが吹き抜け、朝晩の冷え込みが一段と厳しくなる11月〜12月。「肌がカサついてファンデーションがまだらに浮いてしまう」「暖房の効いた部屋にいると頬が突っ張り、顔全体がどんよりくすんで疲れて見える」という深刻な肌の栄養不足と乾燥に直面する方が急増します。<br><br>
        冬の寒冷環境では、皮脂分泌の低下だけでなく毛細血管の収縮による代謝ダウンが重なり、単なる水分補給だけでは肌のツヤと柔軟性を取り戻せません。そこで今冬、美容愛好家や韓国コスメ通から熱烈な支持を集めているのが<strong>『プロテクト＆グロウを両立する高純度プロポリス』</strong>です。<br><br>
        ミツバチが厳しい自然環境から巣を守るために生み出す天然の防御物質プロポリスは、豊富なフラボノイド、ビタミン、アミノ酸を含み、荒れた角層バリアを優しくいたわりながら、肌表面に薄い蜜膜ヴェールを形成。真冬の過酷な冷風や暖房直撃でも乾燥を寄せ付けず、内側から発光するような極上の水光ツヤ肌を叶える、2026年最新の厳選10品を徹底検証・ランキング化しました。
      </div>

      <h2 class="section-title">🐝 プロポリスが冬の過酷な肌荒れ・乾燥粉吹きを救う3大アプローチ</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>プロポリスは、植物の新芽や樹液とミツバチの分泌物が合わさった天然の多機能エキスです。人工的な合成保湿剤には真似のできない、以下の3つの独自メカニズムによって冬の乾燥肌を鉄壁に守り抜きます。</p>
        <ul style="margin: 1rem 0 1rem 1.5rem;">
          <li><strong>1. 濃密な蜜膜ヴェールによる水分蒸散の物理的遮断：</strong> 蜂蜜や樹脂由来の粘性エモリエント成分が、角層表面に吸い付くような保護シールドを形成。11月・12月の湿度が20%近くまで下がる超乾燥空気下でも、肌内部の水分蒸散を強力にストップします。</li>
          <li><strong>2. フラボノイドによる抗酸化と微小肌荒れの鎮静：</strong> 天然のフラボノイド（ケルセチン・アルテピリンC等）が豊富に含まれており、冷えや乾燥、摩擦刺激によって生じる角層の微小炎症を鎮静。粉吹きや赤み、ヒリつきの悪循環を断ち切ります。</li>
          <li><strong>3. 豊富なアミノ酸・ミネラルによる肌代謝とツヤの活性化：</strong> 寒冷刺激でターンオーバーが滞り、くすんだ肌細胞に天然の栄養素をダイレクト補給。内側から光を反射するような透明感と、指を弾き返すようなふっくらとした弾力をもたらします。</li>
        </ul>
      </div>

      <h2 class="section-title">🏆 高保湿プロポリスアンプル・濃密セラムおすすめランキング10選</h2>

      {items_html}

      <h2 class="section-title">📊 高保湿プロポリスアンプル10品 徹底スペック比較表</h2>
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

      <h2 class="section-title">💡 11月・12月の冬本番にプロポリスアンプルの効果を最大化する使用法</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>プロポリスアンプルの濃密な栄養と蜜膜ヴェールを活かし、冬でも乾かないうるツヤ肌をキープするための実践的テクニックをご紹介します。</p>
        <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 1.5rem; margin-top: 1rem;">
          <h3 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: #b45309;">① 化粧水が肌に残る『水分リッチ』な状態で重ねる</h3>
          <p>プロポリスアンプルは水分を抱え込んで逃さない性質があります。化粧水が肌になじんで完全に乾ききる前の、肌表面がまだみずみずしく潤っているタイミングで素早くアンプルを伸ばすと、水分と栄養が一体となって角層深部まで引き込まれます。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #b45309;">② ファンデーションに1滴ブレンドして『一日中崩れない蜜光肌』を作る</h3>
          <p>朝のベースメイク時、普段使っているリキッドファンデーションやBBクリームにプロポリスアンプルを1滴だけ混ぜてみてください。粉吹きや毛穴落ちを防ぎ、冬の暖房直撃オフィスでも夕方までツヤやかな水光美肌が持続します。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #b45309;">③ 夜はクリームに重ねて『スリーピングパック』化</h3>
          <p>夜のスキンケアの最終ステップとして、いつもの保湿クリームを塗った後、乾燥しやすい頬の高い位置や目元・口角にプロポリスアンプルを半滴トントンと重ねづけ。一晩中密閉パック効果が続き、翌朝の洗顔時の手触りが劇的に変わります。</p>
        </div>
      </div>

      <h2 class="section-title">❓ 専門家が答える！プロポリスコスメのよくある質問</h2>
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
          <a href="/winter-proteoglycan" class="internal-link">🧬 高純度プロテオグリカン原液10選</a>
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

with open("winter-propolis.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-propolis.html!")
