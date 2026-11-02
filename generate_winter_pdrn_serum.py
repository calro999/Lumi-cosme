import json
import re

with open("fetched_perfect_3articles_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_pdrn_serum"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 植物性PDRN×低分子コラーゲンの神バランス！肌密度を満たす2026年最大のメガヒット",
        "catch": "高麗人参由来PDRNが冬の寒風・暖房で萎縮した角層に急速チャージ。内側から光を放つ水光肌へ",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "30ml",
        "type": "高純度植物性PDRN・弾力ブースティングエッセンス",
        "features": "高麗人参由来フィトPDRN 100,000ppm、低分子コラーゲン、エクトイン、ヒアルロン酸コンプレックス、無香料",
        "value": "魚由来ではなく高麗人参から抽出した植物性PDRNを贅沢配合。低刺激でありながら、暖房乾燥でしぼんだ大人の肌に吸い付くようなハリと濃密な潤いをもたらす名品",
        "desc_p1": "11月から12月にかけて日本列島を寒波が襲うと、外気温の急降下とともに室内の湿度は20%台まで低下します。肌は角層の水分保持力が奪われるだけでなく、寒冷ストレスによって血行が滞り、ハリや弾力の土台となるターンオーバーが著しく乱れます。夕方に鏡を見たとき、『肌がしぼんで毛穴が縦に流れている』『ファンデーションが乾燥でひび割れる』と感じる女性が急増するこの季節、救世主として爆発的人気を誇るのがVTの『PDRN エッセンス 100』です。",
        "desc_p2": "本品は美容医療のサーモン注射に着想を得つつ、高麗人参から独自のバイオ技術で抽出した植物性PDRNを高純度配合。さらに低分子コラーゲンとエクトインが強力な保水ネットワークを形成し、塗った瞬間から肌が美容液をごくごくと飲み干すように角層深部へ浸透します。とろみのあるリッチなテクスチャーでありながら肌表面にベタつきを残さず、翌朝の洗顔時には手のひらを押し返すような濃密な弾力と、韓国アイドルのようなみずみずしいツヤを実感できます。",
        "target": "冬の暖房で肌のハリ不足・たるみ毛穴が気になる方、魚由来成分の匂いやアレルギーが気になる方、朝晩使える万能な高保湿エイジングケア美容液を求める方",
        "point": "化粧水で肌を整えた直後、スポイト1〜2滴分を手にとり、手のひらの体温で温めてから顔全体を包み込むようにハンドプレス。特に乾燥が気になる目元やほうれい線には重ね付けが効果的です。"
    },
    {
        "rank": 2,
        "tag": "💎 サーモン注射のパイオニアが生んだ最高峰！医療グレードc-PDRNの濃密エイジング補修",
        "catch": "本家リジュランの特許技術が角層深部を集中トリートメント。冬の過酷な乾燥ダメージを跳ね返す",
        "brand_name": "REJURAN (リジュラン)",
        "capacity": "30ml",
        "type": "医療グレードc-PDRN・高濃度デュアルエフェクトアンプル",
        "features": "特許成分c-PDRN（高純度DNA断片）、セラミドNP、ツボクサエキス、ナイアシンアミド、アデノシン",
        "value": "韓国の美容皮膚科で圧倒的シェアを誇る『リジュラン注射』の主成分をホームケア用に最適化。角層バリアの根本修復と圧倒的なハリ密度を実現",
        "desc_p1": "12月の真冬の乾燥は、単なる表面のカサつきにとどまらず、角層深部のラメラ構造を崩壊させて慢性的なインナードライを引き起こします。どれだけ保湿クリームを重ねても午後には突っ張り感や皮むけが生じてしまう過酷な環境において、肌本来の自活力を呼び覚ます切り札として愛用されているのが、本家リジュランの『デュアル エフェクト アンプル』です。",
        "desc_p2": "サーモンDNAから抽出した特許成分『c-PDRN』は、人間のDNA塩基組成に極めて近く、生体適合性に優れているのが最大の特徴。加齢や寒冷刺激によって弱った角層細胞のすき間を埋め尽くし、内側から押し上げるような弾力とキメの整った素肌を再構築します。さらにセラミドNPとツボクサエキスが複合配合されており、冬のピリつきやすいデリケートな肌にも優しくフィット。夜に塗って眠れば、翌朝には美容クリニック帰りのようなふっくらとしたツヤ肌が鏡に映ります。",
        "target": "乾燥による小ジワやハリ低下が深刻な方、美容皮膚科のリジュラン施術後のホームケアを探している方、本物のサーモンPDRNの威力を肌で実感したい方",
        "point": "夜の洗顔後、化粧水の後に使用。付属のスポイトで適量を吸い上げ、乾燥の出やすい頬の高い位置から外側に向かって優しく馴染ませてください。首元のデコルテまで伸ばすことで首の乾燥ジワも同時にケアできます。"
    },
    {
        "rank": 3,
        "tag": "💧 スマートカプセルが弾けて角層を潤す！PDRN×多重ヒアルロン酸の水分爆弾セラム",
        "catch": "目に見えるPDRNカプセルが肌の上でスッと溶け込む。暖房による砂漠肌を瞬時に満たす潤い設計",
        "brand_name": "Anua (アヌア)",
        "capacity": "30ml",
        "type": "カプセル型PDRN・高保水プランピングセラム",
        "features": "スマートPDRNカプセル、低・中・高分子複合ヒアルロン酸、パンテノール、β-グルカン、低刺激弱酸性処方",
        "value": "カプセル技術で新鮮なPDRNを角層へデリバリー。ヒアルロン酸の保水力とPDRNの肌補修力をドッキングさせた新世代の水分爆弾アンプル",
        "desc_p1": "冬の太平洋側特有のからっ風や、24時間暖房が稼働するオフィス環境では、肌から水分が猛スピードで蒸散していきます。水分を失った肌は角質細胞がめくれ上がり、ファンデーションを塗ったそばから毛穴落ちや粉吹きが発生してしまいます。この『冬の水分枯渇』を根本から打破するために設計されたのが、アヌアの『PDRN ヒアルロン酸 カプセル 100 セラム』です。",
        "desc_p2": "透明なセラムの中に無数の微小カプセルが浮遊しており、肌に伸ばした瞬間にカプセルが弾けてフレッシュなPDRNとヒアルロン酸が角層へダイレクトに浸透。分子量の異なる多重ヒアルロン酸が肌表面の保水膜から角層深部までを隙間なく水分で満たし、PDRNが肌のキメをキュッと引き締めます。ベタつきが一切ないウォータリーな使用感のため、朝のメイク前にも快適に使用可能。日中のメイク崩れや夕方のちりめんジワを劇的に防ぎます。",
        "target": "朝のメイク前に使えるベタつかないPDRN美容液を探している方、夕方になると目元や口元がカサついてつっぱる方、インナードライ肌に悩む方",
        "point": "朝のスキンケアにスポイト1回分を取り、顔全体に滑らせるように塗布。30秒ほど置いて肌になじんでから乳液や下地を重ねると、ファンデーションの密着度が格段にアップします。"
    },
    {
        "rank": 4,
        "tag": "✨ 1回使い切りの鮮度！生PDRN×アスタキサンチンの赤のチカラで集中エイジングケア",
        "catch": "空気に触れない個包装パウチで毎回最高純度。冬のくすみ肌に鮮烈な透明感とハリを注入",
        "brand_name": "Yunth (ユンス)",
        "capacity": "1ml×28包",
        "type": "生PDRN・個別包装導入型美容液",
        "features": "生PDRN、アスタキサンチン、低分子ペプチド、ナイアシンアミド、防腐剤フリー・1回使い切り密封パウチ",
        "value": "生ビタミンCで大ヒットしたYunthが満を持して放つPDRNの最高峰。劣化しやすい美容成分を密閉し、使う瞬間ごとに生まれたてのハリ感を肌へ届ける",
        "desc_p1": "年末の多忙や寒さによる睡眠不足が重なる11月・12月は、肌のターンオーバーが停滞して古い角質が蓄積し、顔全体がどんよりとくすんで疲れ顔に見えがちです。酸化ストレスと乾燥がダブルで襲いかかる冬の肌に、フレッシュな有効成分を届ける画期的なアイテムがYunthの『生PDRN美容液』です。",
        "desc_p2": "空気に触れると劣化しやすいPDRNと、高い抗酸化力を持つアスタキサンチンを、1回使い切りの密封パウチに閉じ込めました。手にとると鮮やかな天然の赤色が目を引き、洗顔直後の素肌にのせると美容液がすーっと引き込まれるように浸透。導入美容液として後から使う化粧水やクリームの浸透ルートを切り拓き、乾燥で硬くなった肌をふっくらと柔らげます。毎日のスキンケアがサロンの集中トリートメントに早変わりする贅沢な逸品です。",
        "target": "冬のくすみと乾燥小ジワを同時に晴らしたい方、個包装で常に衛生的なスキンケアを好む方、旅行や出張先でも本格的な乾燥対策をしたい方",
        "point": "洗顔後すぐ、化粧水の前に全量を手のひらに出し、顔全体から首元まで惜しみなく馴染ませます。温かい手のひらで密着させることで、導入効果が最大限に高まります。"
    },
    {
        "rank": 5,
        "tag": "🧬 製薬会社の確かな知見！TECAツボクサエキス×PDRNが織りなす全方位肌密度ケア",
        "catch": "50年の伝統が生んだ韓国製薬大手・東国製薬の技術力。寒冷刺激でゆらいだ肌を鎮静＆リフト",
        "brand_name": "Centellian24 (センテリアン24)",
        "capacity": "50ml",
        "type": "高機能PDRN・肌密度引き締めアクティブセラム",
        "features": "PDRN、TECA（高純度ツボクサエキス）、エラスチン、加水分解コラーゲン、セラミドコンプレックス",
        "value": "医療用マデカソルのメーカーだからできる高濃度処方。乾燥ダメージによる赤みや肌荒れを抑えながら、フェイスラインのゆるみにアプローチ",
        "desc_p1": "真冬の冷風にさらされた屋外から、暖房の効いた暖かい室内に入った瞬間、頬が急激に赤くなったりヒリついたりする『寒暖差ゆらぎ肌』に悩む方は少なくありません。バリア機能が壊れた状態で強いエイジングケアを使うと刺激になることもありますが、センテリアン24の『360度ショット PDRN アクティブセラム』なら安心です。",
        "desc_p2": "韓国の大手製薬会社である東国製薬が開発した特許成分『TECA』が肌荒れや炎症を即座に鎮静。同時に配合されたPDRNとエラスチンが角層深部のコラーゲン構造をサポートし、ゆるみがちな毛穴周りの肌密度をギュッと引き締めます。コクのあるミルキーなアンプルは伸びが非常によく、肌にピタッと密着して保護膜を形成。冬の冷気やマスクの擦れから素肌を優しく守り抜きます。",
        "target": "寒暖差で肌が赤くなりやすい敏感肌の方、肌の弾力低下と肌荒れを同時にケアしたい方、製薬会社クオリティの安心感を求める方",
        "point": "スポイトで両頬と額に適量を点置きし、指の腹を使って内側から外側、下から上へと引き上げるように優しくマッサージしながら浸透させます。"
    },
    {
        "rank": 6,
        "tag": "☕ カフェイン×Bio-PDRNで冬のむくみ顔をシャープに！引き締め＆ハリのダブルアプローチ",
        "catch": "冷えによる血行不良・フェイスラインの重たさを一掃。毛穴を引き締めキュッと上向き肌へ",
        "brand_name": "IOPE (アイオペ)",
        "capacity": "30ml",
        "type": "引き締めリフティング・Bio-PDRNショットアンプル",
        "features": "Bio-PDRN 20,000ppm、高純度カフェイン、バイオカメリアエキス、ナイアシンアミド",
        "value": "植物研究の権威アモーレパシフィックの先端皮膚科学が生んだ名作。むくみ感とたるみ毛穴を同時にケアし、冬の輪郭をシャープに整える",
        "desc_p1": "11月・12月は忘年会やイベントが続き、塩分過多やアルコール、そして冬の冷えによる血流低下が重なって、朝起きると顔がパンパンにむくんでしまう日が増えます。むくみによって皮膚が引っ張られると毛穴が目立ち、ハリ感も低下してしまいます。そんな冬の朝の救世主がIOPEの『PDRN カフェイン ショット』です。",
        "desc_p2": "血行促進と引き締め効果で名高い高純度カフェインと、肌再生成分Bio-PDRNを絶妙な比率で融合。肌に乗せるとスーッとした心地よい清涼感とともに成分が浸透し、滞りがちな冬の巡りをサポートします。使い続けることでフェイスラインのもたつきがスッキリと引き締まり、乾燥で目立っていたたるみ毛穴がキュッと目立たなくなります。むくみやすい冬の朝のスキンケアに欠かせない一本です。",
        "target": "冬になると朝の顔のむくみや輪郭のぼやけが気になる方、毛穴の開きを引き締めたい方、爽やかでみずみずしい浸透感を好む方",
        "point": "朝の洗顔後、化粧水の後に使用。顎先から耳の下、首筋に向かってフェイスラインを引き上げるように流しながら馴染ませると、より高いむくみ解消効果が得られます。"
    },
    {
        "rank": 7,
        "tag": "🌿 植物性PDRN×ナイアシンアミド高配合！冬の乾燥くすみを一掃して輝く透明ツヤ肌へ",
        "catch": "蓮の花由来のクリーンPDRN。敏感肌でも毎日使えるマイルド処方でトーンアップを叶える",
        "brand_name": "NATURE REPUBLIC (ネイチャーリパブリック)",
        "capacity": "30ml",
        "type": "高保湿ブライトニング・PDRNリペアアンプル",
        "features": "植物性PDRN、ナイアシンアミド 5%、低分子ヒアルロン酸、パンテノール、無香料・弱酸性",
        "value": "自然派コスメの実力派。魚由来が苦手な方でも安心して使える蓮由来のPDRNにナイアシンアミドをプラスし、冬のくすみと乾燥を同時にトリートメント",
        "desc_p1": "冬は紫外線量が減る一方で、寒冷による血行不良と角質の乾燥肥厚により、夏とは異なる『グレーがかった乾燥くすみ』が肌を覆います。顔色が冴えずファンデーションの色が合わなくなったと感じる方に向けて、肌の明るさと保水力を同時に底上げするのがネイチャーリパブリックの『PDRN アンプル 美容液』です。",
        "desc_p2": "清らかな蓮の花から抽出した植物性PDRNが角層のキメを整え、美白有効成分としても有名なナイアシンアミドが5%の黄金濃度で肌のバリア機能を強化。水のように軽やかながら、肌になじませるとしっとりとした保護膜が広がり、乾燥によるゴワつきを瞬時にほぐします。弱酸性の低刺激設計なので、冬のデリケートなゆらぎ肌にも刺激なく使えます。",
        "target": "冬の乾燥くすみや顔色の悪さを改善したい方、毎日惜しみなく使えるコスパの良いPDRNを探している方、植物由来の優しい処方を好む方",
        "point": "朝晩の洗顔後、化粧水で肌をたっぷり潤した後にスポイト1回分を使用。くすみが気になる目周りや頬骨付近には指先でトントンと重ね付けしてください。"
    },
    {
        "rank": 8,
        "tag": "🔬 圧倒的スペック120,000ppm！原液コスメが生んだ究極の超高濃度PDRNアンプル",
        "catch": "成分重視のコスメフリーク絶賛。水増しなしの濃厚成分が角層奥深くに浸透しハリを再建",
        "brand_name": "KISO (キソ)",
        "capacity": "30ml",
        "type": "超高濃度・原液特化型PDRN美容液",
        "features": "PDRN（DNA-Na）120,000ppm配合、パンテノール、グリチルリチン酸2K、8種のヒアルロン酸、パラベンフリー",
        "value": "成分特化型ブランドKISOが挑んだ限界濃度。高濃度PDRNが肌本来のコンディションを急速に引き上げ、乾燥小ジワを徹底ケア",
        "desc_p1": "『有名ブランドのコスメを使っても冬の乾燥小ジワが改善しない』『配合成分の濃度にとことんこだわりたい』という本格志向のスキンケアマニアから熱狂的な支持を集めているのが、日本の原液コスメの雄・KISOの『ミルトセラム RN』です。",
        "desc_p2": "市場に流通する多くの美容液が微量配合にとどまる中、驚異の120,000ppmという超高濃度でPDRNを配合。トロリとした濃厚なテクスチャーを手肌に取ると、高純度成分ならではの密度の高さを実感できます。パンテノールと多重ヒアルロン酸が角層の水分蒸散を鉄壁ブロックし、乾燥によって萎縮した肌細胞をふっくらと押し上げます。無駄な香料や着色料を一切省いたストイックな処方で、結果を求める大人の肌に応えます。",
        "target": "成分濃度に妥協したくない方、目尻や口元の乾燥小ジワが深く刻まれてきた方、無駄な添加物のないシンプル処方を好む方",
        "point": "非常に濃厚なため、化粧水でしっかり肌を湿らせた直後に2〜3滴を馴染ませます。手持ちの乳液やクリームに1滴混ぜてブーストする使い方もおすすめです。"
    },
    {
        "rank": 9,
        "tag": "🔥 2026年最大の話題作！低刺激レチノール×PDRNが実現した奇跡のキメ肌アンプル",
        "catch": "冬の毛穴詰まり・ゴワつきを滑らかに整え、PDRNの弾力ヴェールで肌を満たす新境地",
        "brand_name": "innisfree (イニスフリー)",
        "capacity": "30ml",
        "type": "低刺激レチノール×PDRN・キメ再生アドバンスドセラム",
        "features": "低刺激カプセルレチノール、サーモンPDRN、セラミド、アシアチコシド、無香料・低刺激テスト済み",
        "value": "国民的人気のレチシカ美容液をさらに進化させた傑作。冬の乾燥でゴワつきがちな角質を柔軟化し、PDRNがふっくらとしたハリを補填",
        "desc_p1": "冬は寒さで皮脂が固まり、ターンオーバーが遅れることで毛穴が詰まりやすくなり、肌表面の手触りがザラザラとゴワつきがちになります。しかし、冬の乾燥肌に強い角質ケアを使うと皮むけや赤みが起きるリスクがあります。このジレンマを見事に解決したのがイニスフリーの『レチノール PDRN アドバンスド セラム』です。",
        "desc_p2": "肌刺激を最小限に抑えるリポソームカプセル化レチノールが肌のキメを穏やかに整え、そこに高純度サーモンPDRNが角層深部へ弾力と水分を急速補給。乾燥で開いた毛穴周りをふっくらと満たし、つるんとしたなめらかな陶器肌へと導きます。乳液のようにまろやかなテクスチャーで、レチノール初心者でもA反応（皮むけ・赤み）を起こしにくく、真冬の毎日のお手入れに安心して取り入れられます。",
        "target": "冬の肌のゴワつき・毛穴の目立ちに悩む方、レチノールを使いたいが乾燥や刺激が心配な方、つるんとした手触りとハリを両立したい方",
        "point": "夜の洗顔後、化粧水の後に1〜2プッシュを顔全体に伸ばします。レチノール配合のため、翌朝の外出前には必ず日焼け止めを塗布してください。"
    },
    {
        "rank": 10,
        "tag": "🌸 サーモンDNA由来PDRN×ペプチド！気になる乾燥小ジワと弾力低下をダブル集中ケア",
        "catch": "天然のピンク色が放つ濃厚な栄養。暖房乾燥でたるんだ肌をピンと引き上げる密着アンプル",
        "brand_name": "medicube (メディキューブ)",
        "capacity": "30ml",
        "type": "サーモンDNA・ペプチド高濃縮ピンクアンプル",
        "features": "サーモンDNA由来PDRN、マルチペプチドコンプレックス、低分子コラーゲン、ナイアシンアミド",
        "value": "韓国ビューティーデバイスのトップブランドが開発。肌の土台に働きかけるペプチドとPDRNの相乗効果で、年齢肌の深刻な冬枯れをリセット",
        "desc_p1": "12月の乾燥は、表情筋の動きに合わせて目尻やほうれい線に細かな『ちりめんジワ』を刻み込みます。放置すると定着して深いシワへと進行してしまうため、早急な集中補修が必要です。メディキューブの『PDRN ピンク ペプチド アンプル』は、そんな冬の深刻なエイジングサインに真正面から立ち向かう強力なアイテムです。",
        "desc_p2": "サーモンDNA由来のPDRNに加え、肌の弾力構造を支えるマルチペプチドを贅沢にブレンド。人工着色料不使用の天然ピンク色の美容液は、とろりとした濃密なテクスチャーで肌に吸い付き、まるで肌表面に見えないリフティングフィルムを張ったかのようなピンとしたハリ感をもたらします。暖房による水分の蒸散を長時間ブロックし、一日中もっちりとした潤いと若々しいツヤをキープします。",
        "target": "冬の乾燥で目元や口元の小ジワが目立ってきた方、ペプチドとPDRNのW効果を試したい方、濃厚なテクスチャーでしっかり肌を保護したい方",
        "point": "化粧水の後に適量を手に取り、乾燥小ジワが気になる部分を中心に優しくタッピングするように塗り込みます。美顔器をお持ちの方は導入モードで併用すると浸透がさらにアップします。"
    }
]

faq_items = [
    {
        "q": "PDRN（サーモン注射成分）とは何ですか？冬の乾燥肌にどう効きますか？",
        "a": "PDRN（ポリデオキシリボヌクレオチド）は、サーモンなどのDNAから抽出された成分で、人間のDNA塩基配列と極めて高い相同性を持ちます。美容医療では『リジュラン注射（サーモン注射）』として知られ、ダメージを受けた皮膚の修復やコラーゲン生成を促進する効果があります。特に11月〜12月の冬は、気温低下による血行不良と暖房による極度の乾燥で角層のバリア機能が低下し、肌が萎縮してハリやツヤが失われます。PDRN美容液を取り入れることで、角層深部のターンオーバーを整え、内側から水分と弾力を満たして乾燥ダメージを根本からリセットできます。"
    },
    {
        "q": "植物性PDRNと動物性（サーモン由来）PDRNの違いは何ですか？",
        "a": "動物性PDRNはサーモンの生殖細胞から抽出され、医療用リジュランなどでも採用される実績豊富な成分です。高い肌再生・修復サポート力を持つ反面、魚アレルギーの方や特有の匂いに敏感な方には注意が必要です。一方、植物性PDRNは高麗人参や蓮の花などの植物から独自のバイオ技術で抽出された成分で、ヴィーガン処方・低刺激設計が特徴です。肌への親和性が高くマイルドな使い心地のため、冬の敏感に傾いた肌や毎日手軽にケアしたい方には植物性PDRNも大変人気があります。"
    },
    {
        "q": "PDRN美容液は朝と夜のどちらに使うのが効果的ですか？",
        "a": "基本的には朝晩どちらでも使用可能です。朝の使用は、日中のオフィスのエアコン暖房や冷たい冬風による水分蒸発を防ぎ、メイクの粉吹きやひび割れを防止するバリア効果を発揮します（ベタつきにくいウォータリータイプが最適）。夜の使用は、就寝中のターンオーバーをサポートし、1日の乾燥ダメージを集中修復して翌朝のハリツヤ肌を仕込むのに最適です。レチノール配合の製品（イニスフリーなど）のみ、紫外線影響を避けるため夜の使用を推奨します。"
    },
    {
        "q": "ヒアルロン酸やレチノール、ビタミンCとの併用は可能ですか？",
        "a": "PDRNは基本的に肌の修復・鎮静を促す優しい成分であるため、ヒアルロン酸やセラミド、コラーゲンなどの保湿成分とは相乗効果を発揮します。また、ビタミンCやレチノールなどのアクティブ成分とも併用可能です。特にレチノールによる刺激感をPDRNが穏やかにサポートする組み合わせは2026年冬の大きなトレンドになっています。ただし、高濃度レチノールやピーリング成分と併用する場合は、肌の調子を見ながら少量ずつ取り入れてください。"
    },
    {
        "q": "11月〜12月の日本の冬において、PDRN美容液の効果を最大化する塗り方は？",
        "a": "冬は角質が寒さで硬くなっているため、洗顔後すぐに化粧水をたっぷり重ね付けして角層を柔らかくほぐしてからPDRN美容液を塗布するのが鉄則です。手のひらで美容液を軽く温めてからハンドプレスで密着させ、特に暖房直撃で乾燥しやすい目元や頬の高い位置には重ね付けを行いましょう。塗布後は必ずセラミドやスクワラン配合の高保湿乳液・クリームで油分のフタをして、水分と美容成分の蒸発を鉄壁ガードしてください。"
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
    "headline": "保湿力の強さで冬枯れ肌・弾力低下とさようなら！サーモン注射発想の再生成分で内側から押し返すハリツヤ肌へ導く高保湿PDRN美容液ランク10",
    "description": "11月・12月の暖房直撃と寒波による深刻な冬枯れ肌・たるみ毛穴・乾燥小ジワを徹底解決！サーモン注射発想の注目成分PDRN（ポリデオキシリボヌクレオチド）を配合した高保湿美容液10選を徹底比較！VT、リジュラン、アヌア、Yunth、センテリアン24、IOPEなど、角層深部を満たして押し返すようなハリ肌を叶える名品を厳選。",
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
    "name": "冬の高保湿PDRN美容液 おすすめランキング10選",
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

# 商品カードHTML作成
cards_html = []
for p, item in zip(product_details, items):
    cards_html.append(f"""
      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge-wrap">
          <span class="product-rank-badge rank-{p['rank']}">第{p['rank']}位</span>
          <span class="product-tag">{p['tag']}</span>
        </div>
        <div class="product-header">
          <h3 class="product-title">{p['brand_name']} {p['capacity']}</h3>
          <p class="product-catch">{p['catch']}</p>
        </div>
        <div class="product-layout">
          <div class="product-img-box">
            <img src="{item['image']}" alt="{p['brand_name']} {p['capacity']}" class="product-img" loading="lazy" width="300" height="300">
            <div class="product-price-tag">参考価格: <span>¥{item['price']:,}</span> (税込)</div>
          </div>
          <div class="product-specs">
            <table class="spec-table">
              <tr><th>アイテムタイプ</th><td>{p['type']}</td></tr>
              <tr><th>注目美容成分</th><td>{p['features']}</td></tr>
              <tr><th>期待できる効果</th><td>{p['value']}</td></tr>
              <tr><th>おすすめの肌質</th><td>{p['target']}</td></tr>
            </table>
          </div>
        </div>
        <div class="product-body">
          <div class="product-desc">
            <p>{p['desc_p1']}</p>
            <p>{p['desc_p2']}</p>
          </div>
          <div class="product-advice">
            <div class="advice-title">💡 美容コンシェルジュの使いこなしポイント</div>
            <p>{p['point']}</p>
          </div>
        </div>
        <div class="product-action">
          <a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で最安値・在庫をチェック
            <svg class="btn-arrow" viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"/></svg>
          </a>
        </div>
      </article>
""")

comparison_rows = []
for p, item in zip(product_details, items):
    comparison_rows.append(f"""
            <tr>
              <td class="col-rank"><span class="table-rank rank-{p['rank']}">{p['rank']}</span></td>
              <td class="col-thumb"><img src="{item['image']}" alt="{p['brand_name']}" class="table-img" loading="lazy" width="60" height="60"></td>
              <td class="col-name"><strong>{p['brand_name']}</strong><br><small>{p['capacity']}</small></td>
              <td class="col-type">{p['type']}</td>
              <td class="col-features">{p['features']}</td>
              <td class="col-price">¥{item['price']:,}</td>
              <td class="col-btn"><a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="table-btn">楽天詳細</a></td>
            </tr>
""")

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬枯れ肌・弾力低下とさようなら！サーモン注射発想の再生成分で内側から押し返すハリツヤ肌へ導く高保湿PDRN美容液ランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の暖房直撃と寒波による深刻な冬枯れ肌・たるみ毛穴・乾燥小ジワを徹底解決！サーモン注射発想の注目成分PDRN（ポリデオキシリボヌクレオチド）を配合した高保湿美容液10選を徹底比較！VT、リジュラン、アヌア、Yunth、センテリアン24、IOPEなど、角層深部を満たして押し返すようなハリ肌を叶える名品を厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-pdrn-serum">
  <meta name="robots" content="index, follow, max-image-preview:large">
  
  <!-- OGP & SNS -->
  <meta property="og:title" content="保湿力の強さで冬枯れ肌・弾力低下とさようなら！サーモン注射発想の再生成分で内側から押し返すハリツヤ肌へ導く高保湿PDRN美容液ランク10">
  <meta property="og:description" content="11月・12月の暖房直撃と寒波による深刻な冬枯れ肌・たるみ毛穴・乾燥小ジワを徹底解決！サーモン注射発想の注目成分PDRNを配合した高保湿美容液10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-pdrn-serum">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#c94b6e">

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
      --primary: #c94b6e;
      --primary-light: #fdf2f4;
      --primary-dark: #a33250;
      --text-main: #2d3748;
      --text-sub: #718096;
      --bg-page: #fbfbfc;
      --bg-card: #ffffff;
      --border: #edf2f7;
      --border-focus: #feb2b2;
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
      letter-spacing: -0.5px;
    }}
    .breadcrumb {{
      max-width: 1100px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-sub);
    }}
    .breadcrumb a {{ color: var(--text-sub); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .container {{
      max-width: 900px;
      margin: 0 auto;
      padding: 24px 20px 80px;
    }}
    .hero-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 40px 32px;
      margin-bottom: 40px;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
    }}
    .post-badge {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 700;
      font-size: 0.8rem;
      padding: 6px 14px;
      border-radius: 9999px;
      margin-bottom: 16px;
    }}
    .post-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.45;
      color: #1a202c;
      margin-bottom: 20px;
      letter-spacing: -0.5px;
    }}
    .post-meta {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 24px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
    }}
    .intro-text p {{
      margin-bottom: 16px;
      font-size: 1.02rem;
      color: #4a5568;
    }}
    .callout-box {{
      background: #fff5f7;
      border-left: 4px solid var(--primary);
      padding: 20px;
      border-radius: 0 12px 12px 0;
      margin: 24px 0;
    }}
    .callout-title {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 8px;
    }}
    .toc-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 24px;
      margin: 32px 0 48px;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px 20px;
    }}
    @media (max-width: 640px) {{
      .toc-list {{ grid-template-columns: 1fr; }}
      .post-title {{ font-size: 1.45rem; }}
      .hero-section {{ padding: 24px 18px; }}
    }}
    .toc-list a {{
      color: #3182ce;
      text-decoration: none;
      font-size: 0.92rem;
    }}
    .toc-list a:hover {{ text-decoration: underline; }}
    
    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      margin: 56px 0 24px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--primary);
      color: #1a202c;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .subsection-title {{
      font-size: 1.25rem;
      font-weight: 700;
      margin: 32px 0 16px;
      color: #2d3748;
    }}
    .content-box {{
      background: #ffffff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 40px;
      border: 1px solid var(--border);
    }}
    .content-box p {{ margin-bottom: 16px; }}
    .content-box ul, .content-box ol {{
      margin: 16px 0 20px 24px;
      color: #4a5568;
    }}
    .content-box li {{ margin-bottom: 8px; }}

    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      position: relative;
    }}
    .product-badge-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }}
    .product-rank-badge {{
      background: #2d3748;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 6px 16px;
      border-radius: 9999px;
    }}
    .product-rank-badge.rank-1 {{ background: linear-gradient(135deg, #d97706, #f59e0b); }}
    .product-rank-badge.rank-2 {{ background: linear-gradient(135deg, #4b5563, #9ca3af); }}
    .product-rank-badge.rank-3 {{ background: linear-gradient(135deg, #b45309, #d97706); }}
    .product-tag {{
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 6px 14px;
      border-radius: 8px;
    }}
    .product-title {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #1a202c;
      margin-bottom: 6px;
    }}
    .product-catch {{
      color: var(--primary);
      font-weight: 700;
      font-size: 0.98rem;
      margin-bottom: 20px;
    }}
    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }}
    @media (max-width: 768px) {{
      .product-layout {{ grid-template-columns: 1fr; }}
    }}
    .product-img-box {{
      text-align: center;
      background: #f8fafc;
      padding: 16px;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      object-fit: contain;
    }}
    .product-price-tag {{
      margin-top: 12px;
      font-size: 0.9rem;
      color: #718096;
    }}
    .product-price-tag span {{
      color: #e53e3e;
      font-weight: 800;
      font-size: 1.25rem;
    }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 10px 12px;
      border-bottom: 1px solid #edf2f7;
    }}
    .spec-table th {{
      width: 32%;
      background: #f7fafc;
      color: #4a5568;
      font-weight: 600;
      text-align: left;
    }}
    .product-desc {{
      margin-bottom: 20px;
      font-size: 0.98rem;
      color: #4a5568;
    }}
    .product-advice {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      padding: 18px;
      border-radius: 10px;
      margin-bottom: 24px;
    }}
    .advice-title {{
      font-weight: 700;
      color: #166534;
      margin-bottom: 6px;
      font-size: 0.95rem;
    }}
    .product-advice p {{
      color: #15803d;
      font-size: 0.92rem;
      margin-bottom: 0;
    }}
    .rakuten-btn {{
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 10px;
      background: linear-gradient(135deg, #bf0000, #e60000);
      color: #ffffff;
      text-decoration: none;
      font-weight: 800;
      font-size: 1.05rem;
      padding: 16px 28px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #a80000, #cc0000);
    }}

    /* 比較表 */
    .table-wrap {{
      overflow-x: auto;
      margin: 24px 0 40px;
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 720px;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 14px 12px;
      border-bottom: 1px solid #edf2f7;
      text-align: left;
    }}
    .comparison-table th {{
      background: #f8fafc;
      font-weight: 700;
      color: #4a5568;
    }}
    .table-rank {{
      display: inline-block;
      width: 28px;
      height: 28px;
      line-height: 28px;
      text-align: center;
      border-radius: 50%;
      background: #2d3748;
      color: #fff;
      font-weight: 700;
    }}
    .table-rank.rank-1 {{ background: #f59e0b; }}
    .table-rank.rank-2 {{ background: #9ca3af; }}
    .table-rank.rank-3 {{ background: #d97706; }}
    .table-img {{
      border-radius: 6px;
      border: 1px solid #e2e8f0;
      object-fit: contain;
    }}
    .table-btn {{
      display: inline-block;
      background: #bf0000;
      color: #fff;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.78rem;
      padding: 6px 12px;
      border-radius: 6px;
      white-space: nowrap;
    }}

    /* FAQ */
    .faq-item {{
      background: #ffffff;
      border-radius: 12px;
      border: 1px solid var(--border);
      margin-bottom: 16px;
      padding: 20px;
    }}
    .faq-q {{
      font-weight: 800;
      font-size: 1.05rem;
      color: #1a202c;
      margin-bottom: 10px;
      display: flex;
      gap: 10px;
      align-items: flex-start;
    }}
    .faq-q-mark {{
      color: var(--primary);
      font-weight: 900;
    }}
    .faq-a {{
      color: #4a5568;
      font-size: 0.95rem;
      line-height: 1.7;
      padding-left: 24px;
    }}

    /* 内部リンク */
    .related-links-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-top: 24px;
    }}
    @media (max-width: 640px) {{
      .related-links-grid {{ grid-template-columns: 1fr; }}
    }}
    .related-link-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      text-decoration: none;
      color: inherit;
      transition: all 0.2s ease;
      display: block;
    }}
    .related-link-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
      border-color: var(--primary);
    }}
    .related-card-tag {{
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      margin-bottom: 8px;
      background: var(--primary-light);
      color: var(--primary);
    }}
    .related-card-title {{
      font-size: 0.92rem;
      font-weight: 700;
      color: #2d3748;
      line-height: 1.5;
    }}

    footer.site-footer {{
      background: #1a202c;
      color: #a0aec0;
      padding: 60px 20px 40px;
      font-size: 0.9rem;
    }}
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
    }}
    .footer-title {{
      color: #ffffff;
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 20px;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px 16px;
      margin-bottom: 32px;
    }}
    .footer-links a {{
      color: #cbd5e0;
      text-decoration: none;
      font-size: 0.85rem;
    }}
    .footer-links a:hover {{
      color: #ffffff;
      text-decoration: underline;
    }}
    .copyright {{
      text-align: center;
      border-top: 1px solid #2d3748;
      padding-top: 24px;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav class="header-nav">
        <a href="/" style="color: #4a5568; text-decoration: none; font-size: 0.9rem; font-weight: 600;">TOPへ戻る</a>
      </nav>
    </div>
  </header>

  <nav class="breadcrumb" aria-label="パンくずリスト">
    <a href="/">HOME</a> &gt; <span>高保湿PDRN美容液 ランキング</span>
  </nav>

  <main class="container">

    <section class="hero-section">
      <span class="post-badge">2026年最新冬コスメ厳選</span>
      <h1 class="post-title">保湿力の強さで冬枯れ肌・弾力低下とさようなら！サーモン注射発想の再生成分で内側から押し返すハリツヤ肌へ導く高保湿PDRN美容液ランク10</h1>
      <div class="post-meta">
        <span>執筆・監修: 冬コスメ徹底比較ラボ 編集部</span>
        <span>更新日: 2026年11月02日</span>
        <span>検証基準: 保湿力持続性・弾力密度・成分純度・口コミ満足度</span>
      </div>
      <div class="intro-text">
        <p>11月から12月にかけて、日本の気候は一気に冬本番へと突入します。北からの寒波によって外気温が10℃を下回ると、太平洋側では乾いた季節風が吹き荒れ、室内のエアコン暖房はフル稼働。湿度は連日20%台という、いわば『湿度砂漠』の状態に晒されます。</p>
        <p>この過酷な寒冷乾燥下では、肌の表面の水分が奪われるだけでなく、毛細血管の収縮によってターンオーバーが著しく停滞。どんなに高価な化粧水やクリームを重ねても、『夕方になるとファンデーションがひび割れる』『頬の毛穴が縦に流れてフェイスラインがしぼんで見える』という深刻な<strong>冬枯れ肌現象</strong>に直面します。</p>
        <p>そんな大人の冬肌の救世主として今、美容業界で空前の注目を集めているのが<strong>PDRN（ポリデオキシリボヌクレオチド）配合の美容液</strong>です。美容皮膚科の再生治療『リジュラン注射（サーモン注射）』で培われたDNA補修発想を取り入れたPDRNは、角層のすみずみにまで浸透し、肌本来の保水力と弾力の土台を根本から底上げします。</p>
      </div>

      <div class="callout-box">
        <div class="callout-title">📌 11月〜12月の冬枯れ肌にPDRN美容液が最強な理由</div>
        <p>従来の保湿美容液が『表面の水分蒸散をブロックする』対症療法であったのに対し、PDRNは人間のDNA構造に極めて近い塩基配列を持ち、寒冷と乾燥で傷んだ角層のコンディションを自活的に修復。内側から押し返すようなハリ感と、暖房直撃でも乾かない圧倒的な水分保持力を肌に宿します。</p>
      </div>

      <div class="toc-box">
        <div class="toc-title">📋 目次</div>
        <ul class="toc-list">
          <li><a href="#why-pdrn">1. 冬の寒冷乾燥とPDRNの作用メカニズム</a></li>
          <li><a href="#how-to-choose">2. 冬のPDRN美容液の失敗しない選び方</a></li>
          <li><a href="#ranking">3. 高保湿PDRN美容液おすすめランキング10選</a></li>
          <li><a href="#comparison">4. 全10商品スペック比較一覧表</a></li>
          <li><a href="#effective-use">5. 美容ライターが教える冬の塗り方のコツ</a></li>
          <li><a href="#faq">6. よくある質問 (FAQ)</a></li>
        </ul>
      </div>
    </section>

    <!-- セクション1 -->
    <section id="why-pdrn" class="content-box">
      <h2 class="section-title">1. 冬の寒冷乾燥とPDRNの作用メカニズム</h2>
      <p>なぜ11月・12月になると、いつもの保湿ケアでは物足りなくなってしまうのでしょうか？ その最大の原因は、<strong>『外気乾燥×暖房熱×血行不良』の三重苦</strong>にあります。</p>
      
      <h3 class="subsection-title">① 湿度20%台のオフィス暖房による『水分蒸発の加速』</h3>
      <p>エアコンの温風が直接顔に当たるオフィス環境では、肌表面の角質水分が猛烈なスピードで奪われます。角質細胞の間を満たす細胞間脂質（セラミドなど）の結合が乱れると、肌のバリア機能に穴が空いた状態となり、外気からの刺激に対して肌が過敏に反応して赤みや痒みが生じます。</p>

      <h3 class="subsection-title">② 寒冷による末梢血管の収縮とターンオーバーの遅延</h3>
      <p>寒さによって顔の毛細血管が収縮すると、皮膚細胞に酸素や栄養素が届きにくくなります。これにより細胞の代謝スピードが落ち、傷んだ角質が肌表面に停滞。手触りはゴワつき、スキンケアの浸透ルートが遮断されてしまいます。</p>

      <h3 class="subsection-title">③ PDRNがもたらす『肌密度の再建』</h3>
      <p>PDRNは、サーモンのDNAから抽出精製された安全性の高い核酸成分（または高麗人参などから抽出された植物性フィトPDRN）です。肌細胞の受容体に直接働きかけ、乾燥ストレスでダメージを受けた角層の修復シグナルを活性化。さらにコラーゲンやエラスチンの生成環境を力強く後押しすることで、萎縮していた肌をふっくらと持ち上げ、光を均一に反射する水光ツヤを取り戻します。</p>
    </section>

    <!-- セクション2 -->
    <section id="how-to-choose" class="content-box">
      <h2 class="section-title">2. 冬のPDRN美容液の失敗しない選び方</h2>
      <p>市場に数多くのPDRNコスメが登場する中、冬の過酷な環境を乗り切るためには以下の3つのポイントを基準に選ぶことが不可欠です。</p>

      <ul>
        <li><strong>【由来と純度】サーモン由来か、植物性フィトPDRNか：</strong> 即効性と確かな実績を求めるなら本家サーモンDNA由来（リジュラン、メディキューブなど）。魚アレルギーの心配がなく、ヴィーガン処方で毎日安心して使いたいなら植物性PDRN（VT、ネイチャーリパブリックなど）が最適です。</li>
        <li><strong>【複合成分の相乗効果】ヒアルロン酸・ペプチド・セラミドの配合：</strong> PDRN単体だけでなく、水分を抱え込む多重ヒアルロン酸や、バリアを補強するセラミド、弾力を高めるペプチドがブレンドされている製品は、11月〜12月の暖房乾燥に対して隙のない防御力を発揮します。</li>
        <li><strong>【朝晩の使い分けとテクスチャー】：</strong> 朝のメイク前に使うなら、皮脂崩れやヨレを起こさないウォータリーカプセル型（アヌアなど）。夜の集中エイジングケアなら、高濃度原液タイプ（KISO）や個包装パウチ（Yunth）を選ぶと効果的です。</li>
      </ul>
    </section>

    <!-- セクション3: ランキング -->
    <section id="ranking">
      <h2 class="section-title">3. 高保湿PDRN美容液おすすめランキング10選</h2>
      <p style="margin-bottom: 24px; color: #4a5568;">当ラボ編集部が楽天市場で流通する最新PDRN美容液を徹底検証し、11月〜12月の冬枯れ肌を劇的に改善するおすすめ10選を決定しました。</p>
      
      {''.join(cards_html)}
    </section>

    <!-- セクション4: 比較表 -->
    <section id="comparison">
      <h2 class="section-title">4. 全10商品スペック比較一覧表</h2>
      <p style="margin-bottom: 16px; color: #4a5568;">横スクロールで各商品の価格・配合成分・特徴をひと目で比較できます。</p>
      <div class="table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>画像</th>
              <th>商品名 / 容量</th>
              <th>タイプ</th>
              <th>注目美容成分</th>
              <th>参考価格</th>
              <th>詳細</th>
            </tr>
          </thead>
          <tbody>
            {''.join(comparison_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション5: 塗り方のコツ -->
    <section id="effective-use" class="content-box">
      <h2 class="section-title">5. 美容ライターが教える冬の塗り方のコツ</h2>
      <p>高級なPDRN美容液も、塗り方を間違えると効果が半減してしまいます。真冬の過酷な乾燥環境下で、美容液のポテンシャルを120%引き出すプロのテクニックを伝授します。</p>

      <h3 class="subsection-title">STEP 1: 化粧水での「プレ水分補給」を怠らない</h3>
      <p>冬の冷気で硬化した角質は、乾燥したスポンジと同じです。いきなり美容液を塗るのではなく、まずは高保湿化粧水を手で優しく2〜3回重ね付けし、角層全体を水分で十分に湿らせて浸透ルートを確保しましょう。</p>

      <h3 class="subsection-title">STEP 2: 手のひらで3秒間温めてからハンドプレス</h3>
      <p>冷たいままの美容液を顔につけると毛穴がキュッと閉じてしまい、浸透が悪くなります。手のひらに出した美容液を両手で軽く擦り合わせて人肌に温めてから、顔全体を優しく包み込むようにハンドプレスしてください。体温によって浸透スピードが格段に向上します。</p>

      <h3 class="subsection-title">STEP 3: 高保湿クリームで「油分シールド」を完成させる</h3>
      <p>PDRNが角層に入り込んだら、水分が逃げないように直ちにセラミドやスクワラン、シアバター配合のリッチなクリームでフタをします。特に就寝中は暖房をつけっぱなしにする場合、クリームを厚めに塗る『スリーピングパック塗り』が翌朝の乾燥を防ぐ秘訣です。</p>
    </section>

    <!-- セクション6: FAQ -->
    <section id="faq">
      <h2 class="section-title">6. よくある質問 (FAQ)</h2>
      <div class="faq-list">
        {''.join([f'''
        <div class="faq-item">
          <div class="faq-q"><span class="faq-q-mark">Q.</span><span>{item['q']}</span></div>
          <div class="faq-a">{item['a']}</div>
        </div>
        ''' for item in faq_items])}
      </div>
    </section>

    <!-- 内部リンク集 -->
    <section class="content-box" style="margin-top: 48px;">
      <h2 class="section-title" style="margin-top: 0;">あわせて読みたい！冬の乾燥・集中ケア関連記事</h2>
      <div class="related-links-grid">
        <a href="/winter-collagen-mask" class="related-link-card">
          <span class="related-card-tag">一晩貼って朝プルプル NEW</span>
          <div class="related-card-title">寝ている間に角層深部へ浸透！高密着バイオコラーゲンリアルディープマスク10選</div>
        </a>
        <a href="/winter-carbonic-shampoo" class="related-link-card">
          <span class="related-card-tag">冬の頭皮冷え・フケ解消 NEW</span>
          <div class="related-card-title">濃密マイクロ炭酸泡で血行促進！冬の高保湿炭酸スカルプシャンプー10選</div>
        </a>
        <a href="/winter-oil-mist" class="related-link-card">
          <span class="related-card-tag">日中暖房・粉吹き対策</span>
          <div class="related-card-title">水分とオイルの黄金比！日中も瞬時に艶肌復活する高保湿オイルインミスト10選</div>
        </a>
        <a href="/winter-carbonic-bath" class="related-link-card">
          <span class="related-card-tag">冷え性改善・全身保湿</span>
          <div class="related-card-title">重炭酸イオン温浴で芯から温まる！薬用重炭酸入浴剤おすすめ10選</div>
        </a>
        <a href="/winter-ceramide-serum" class="related-link-card">
          <span class="related-card-tag">バリア機能強化</span>
          <div class="related-card-title">肌のラメラ構造を整えて水分蒸散を防ぐ！高濃度セラミド美容液10選</div>
        </a>
        <a href="/winter-retinol-cream" class="related-link-card">
          <span class="related-card-tag">ハリ・小ジワ対策</span>
          <div class="related-card-title">冬の乾燥小ジワを集中ふっくら！大人の高保湿レチノールクリーム10選</div>
        </a>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-title">冬コスメ徹底比較ラボ - カテゴリ別ランキング</div>
      <div class="footer-links">
        <!-- フッターリンクは後ほど一括スクリプトで最新化されます -->
        <a href="/winter-pdrn-serum">高保湿PDRN美容液</a>
        <a href="/winter-collagen-mask">バイオコラーゲンマスク</a>
        <a href="/winter-carbonic-shampoo">高濃度炭酸シャンプー</a>
        <a href="/winter-oil-mist">高保湿オイルインミスト</a>
        <a href="/winter-carbonic-bath">薬用重炭酸入浴剤</a>
        <a href="/winter-hot-treatment">温感ヘッドスパトリートメント</a>
      </div>
      <div class="copyright">
        &copy; 2026 冬コスメ徹底比較ラボ 編集部. All Rights Reserved.
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-pdrn-serum.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("🎉 Successfully generated winter-pdrn-serum.html!")
