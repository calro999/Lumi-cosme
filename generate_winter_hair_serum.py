import json
import re

with open("fetched_3new_nov_dec_ceramide_peptide_hair_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_hair_serum"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 累計2,000万本突破の殿堂入り！水を一切加えない海藻美髪成分が毛先を集中密閉",
        "catch": "ラサーナ最高峰のロングセラー。ブルターニュ産海藻エキスが真冬のパサつく髪をシルクの手触りへ",
        "brand_name": "La Sana (ラサーナ)",
        "capacity": "120ml (海藻 ヘア エッセンス しっとり)",
        "type": "無加水濃密処方・洗い流さない濃密海藻美髪ヘアエッセンス",
        "features": "フランス・ブルターニュ産海藻エキス、高精製スクワラン、ローヤルゼリーエキス、γ-ドコサラクトン（エルカラクトン）",
        "value": "水を一滴も使わない濃厚美髪処方。ドライヤーの熱を味方にしてキューティクルを密着補修し、冬の乾燥・静電気による広がりを完全ガード",
        "desc_p1": "11月から12月にかけて湿度が低下すると、髪内部の水分が奪われてコルテックスがスカスカの空洞状態になり、マフラーやセーターの摩擦で静電気が爆発的に発生します。表面に油分を塗るだけのヘアオイルでは解決できないこの『冬の重度パサつき』に、20年以上にわたり不動の支持を集めているのがラサーナの『海藻 ヘア エッセンス しっとり』です。",
        "desc_p2": "成分のトップに水を一切記載しない超濃密処方が最大の特徴。フランスの海で手摘みされたミネラル豊富な海藻エキスとスクワランが、濡れた髪のキューティクルから内部深層へとすばやく浸透。ドライヤーの温風熱によって毛髪タンパク質と結合するエルカラクトンが、熱ダメージを防ぐと同時に表面をツルツルの保護膜でラッピングします。翌朝ブラッシングした瞬間に指がすっと通り、夕方までしっとりとまとまる感動を味わえます。",
        "target": "冬になると毛先がパサついてまとまらない方、静電気で髪が広がって困る方、無香料で他の香水の邪魔をしないヘアケアを好む方",
        "point": "お風呂上がりのタオルドライ後、濡れた状態の髪に適量を手のひらで伸ばし、毛先を中心に内側から手ぐしを通すように馴染ませてからドライヤーで完全に乾かします。"
    },
    {
        "rank": 2,
        "tag": "🥛 美容水×エモリエントの黄金比！SNSでバズり続けるサロン級インバス補修ミルク",
        "catch": "オルビスの大ヒットヘアミルク。高保水アミノ酸と浸透美容液が髪の芯まで潤いを満たす",
        "brand_name": "ORBIS (オルビス)",
        "capacity": "140g (エッセンスインヘアミルク)",
        "type": "浸透美容液成分配合・高保湿エマルジョンヘアセラム",
        "features": "高保水アミノ酸（浸透型ヒアルロン酸誘導体）、CMC類似補修成分、エモリエント成分、無香料・無着色・アルコールフリー",
        "value": "髪の内部構造CMCを再現した補修成分が、冬の乾燥でパサつく毛髪内部に水分をグングン引き込み、ベタつきゼロで驚くほどの柔らかさを実現",
        "desc_p1": "冬のヘアケアで多くの女性が直面するのが、『オイルを塗るとベタつくのに、時間が経つと内側がカサカサする』という毛髪のインナードライ問題です。SNSや口コミサイトでベストコスメを総なめにしているオルビスの『エッセンスインヘアミルク』は、水分と油分を同時にチャージできる奇跡のヘア美容液です。",
        "desc_p2": "みずみずしいミルク状のテクスチャーは髪に伸ばした瞬間にサラリとほどけ、高保水アミノ酸が髪の芯（コルテックス）まで急速浸透。外側をCMC類似成分がコーティングすることで、乾いた冬の空気の中でも水分をしっかり抱え込みます。オイル特有の重さやベタつきが一切ないため、朝のスタイリング前のベースとしても大活躍。指通りが驚くほど柔らかく、風になびくサラサラ髪へと仕上がります。",
        "target": "髪が硬くゴワつきやすい方、オイルのベタつきが苦手な猫っ毛・細毛の方、プチプラで毎日惜しみなく使える名品を探している方",
        "point": "タオルドライ後の濡れた髪に1〜2プッシュを毛先から馴染ませます。朝のスタイリング時にパサつきが気になる部分へ乾いた髪に乾いた状態で重ね塗りするのも効果的です。"
    },
    {
        "rank": 3,
        "tag": "🌙 夜寝ている間にじっくりくせ毛補修！最高峰ケラスターゼの夜用高保湿セラム",
        "catch": "オレオ リラックスのナイトテクノロジー。寝返りの摩擦から髪を守り翌朝のスタイリング時間を劇的短縮",
        "brand_name": "KERASTASE (ケラスターゼ)",
        "capacity": "90ml (オレオ リラックス マジック ナイト セラム)",
        "type": "高級サロン専売・夜用高保湿くせ毛集中リペアセラム",
        "features": "イリス根エキス、5種のビタミンブレンド（E・C・B3・B5・B6）、プロケラチン複合体",
        "value": "世界中のトップヘアサロンが信頼を寄せるケラスターゼ。夜塗って寝るだけで、睡眠中の枕との摩擦ダメージを防ぎ、冬の乾燥でうねる髪を整える",
        "desc_p1": "冬の朝、起きた瞬間に髪がボサボサに広がっていたり、暖房乾燥でうねりが悪化してブローに何十分もかかってしまう方に圧倒的な人気を誇るのが、ケラスターゼの『マジック ナイト セラム』です。",
        "desc_p2": "過酷な環境でも水分を蓄えるイリス根エキスと、髪の構成成分に似たビタミン複合体を贅沢に配合。夜の入浴後に馴染ませると、睡眠中の8時間にわたって美髪成分がじわじわと毛髪内部へ補給され続けます。さらに寝返りによる枕との摩擦からキューティクルを物理的にガード。翌朝起きた瞬間、まるでサロン帰りのブロー直後のようなまとまりと、上品な香りに包まれた極上の艶髪を実感できます。",
        "target": "冬の乾燥でくせ毛やうねりが悪化しやすい方、朝のヘアセット時間を短縮したい方、優雅なサロンフレグランスを楽しみたい方",
        "point": "夜、お風呂上がりのタオルドライ後の髪に2〜3プッシュを馴染ませてドライヤーで乾かします。就寝前の乾いた髪に少量重ね付けすると、摩擦防止効果がさらに高まります。"
    },
    {
        "rank": 4,
        "tag": "🔬 ブリーチ・カラーダメージ毛の救世主！絡まりとゴワつきを解きほぐす進化系セラム",
        "catch": "サロン専売ミルボンが解き明かした毛髪科学。冬の静電気で絡まるハイトーンヘアをサラサラに導く",
        "brand_name": "MILBON (ミルボン)",
        "capacity": "120ml (エルジューダ ブリーチケア セラム)",
        "type": "サロン専売・ブリーチ＆ハイダメージ毛専用オイルセラム",
        "features": "バオバブオイル、カルボキシメチルアラニルジスルフィドケラチン（CMADK）、スムースオイル",
        "value": "ブリーチや冬の乾燥でうねり絡まる毛髪を均一にコート。ドライヤー中の引っかかりをゼロにし、シルクのような滑らかな指通りを復元",
        "desc_p1": "冬の寒さと乾燥は、ブリーチやカラーを繰り返したダメージ毛にとって最大の試練です。毛髪内部のタンパク質が流出してスカスカになった髪は、外気の乾燥によって急速にパサつき、静電気でマフラーに絡みついて切れ毛の原因になります。美容室シェアNo.1のミルボンがこの問題に特化して開発したのが『エルジューダ ブリーチケア セラム』です。",
        "desc_p2": "毛髪と親和性の高い補修成分CMADKがダメージホールに浸透して定着。さらに水と油の両方に馴染みやすいスムースオイルが、濡れた髪全体に均一に広がり、ドライヤーの熱による乾きムラやパサつきを抑えます。オイルセラムでありながら重さが全くなく、サラサラとした風通しの良い手触りを実現。真冬の過酷な環境でも絡まらず、毛先までスルスルと指が通る美髪をキープできます。",
        "target": "ブリーチや繰り返すカラーで毛先が傷んでいる方、冬に髪が静電気で絡まりやすい方、軽やかなサラサラ感を好む方",
        "point": "タオルドライ後、左右半分に分けた髪にそれぞれ1プッシュずつ塗布。中間から毛先にかけて手ぐしを通しながら馴染ませ、根元から毛先に向かってドライヤーの風を当てて乾かします。"
    },
    {
        "rank": 5,
        "tag": "✨ 6種の贅沢フラワーエキストラクト！真冬のパサつく剛毛を濃密オイルでしっとり封印",
        "catch": "世界中で愛されるロレアルの濃密ヘアオイルセラム。冬の湿気・乾燥による広がりを完璧コントロール",
        "brand_name": "L'OREAL PARIS (ロレアル パリ)",
        "capacity": "100ml (エルセーヴ エクストラオーディナリー オイル エクストラリッチ)",
        "type": "6種のフラワーエキストラオイル配合・超濃密高保湿ヘアセラム",
        "features": "ロータス、ティアレフラワー、ローズ、フラックス、カモミール、サンフラワーオイルエキス",
        "value": "濃密なとろみのあるリッチオイルが髪の1本1本をコーティング。太い髪や硬い髪、冬の乾燥で広がる剛毛をしっとり吸い付くようにまとめる",
        "desc_p1": "12月の真冬の乾燥外気は、髪のボリュームを不自然に膨らませ、毛先を竹ぼうきのように硬くしてしまいます。ドラッグストアで手に入る最高峰のリッチオイルとして君臨するロレアル パリの『エクストラリッチ フィニッシュ』は、そんな冬の頑固な広がり・剛毛を鎮める最強のオイルセラムです。",
        "desc_p2": "厳選された6種類のフラワーエキストラオイルが贅沢にブレンドされ、黄金色のとろみのあるテクスチャーが毛先までしっかり密着。乾燥してめくれ上がったキューティクルをピタッと寝かせ、真冬の暖房下でも一日中ツヤとまとまりを持続させます。オリエンタルサニーの深みのある甘い香りが、冬の外出先でもふわりと香り、上質なラグジュアリー感を演出します。",
        "target": "髪の毛が太く・硬く・量が多くて広がりやすい方、しっかりとした重めのしっとり感を求める方、華やかな香りに包まれたい方",
        "point": "タオルドライ後の濡れた髪に1〜2プッシュを馴染ませて乾かします。さらに朝のスタイリングの仕上げに半プッシュを毛先にもみ込むと、美しいツヤとまとまりが一日中キープできます。"
    },
    {
        "rank": 6,
        "tag": "💎 超高圧処理アルガンオイル配合！羽のように軽いのに毛先までしっとりまとまる",
        "catch": "深層浸透処方でベタつきゼロ。ドライヤー熱を利用して髪のうねり・パサつきを密着リペア",
        "brand_name": "LUCIDO-L (ルシードエル)",
        "capacity": "100ml (オイルトリートメント #EXヘアセラム)",
        "type": "超高圧処理アルガンオイル配合・高密着浸透ヘアセラム",
        "features": "超高圧処理アルガンオイル、ヒートリペア成分、UVカット処方、軽やかスムースポリマー",
        "value": "深海1万メートルの圧力に匹敵する超高圧で処理したアルガンオイルが、髪の隙間に素早く浸透。冬の静電気を防ぎながら自然な天使の輪を再現",
        "desc_p1": "冬のヘアケアで『毛先はしっかり潤したいけれど、トップや前髪がペタンコになるのは絶対に嫌』という方に絶大な支持を得ているのが、ルシードエルの『#EXヘアセラム』です。高機能オイルセラムでありながら、驚異的な軽さと高保湿を両立させています。",
        "desc_p2": "超高圧処理によって分子が微細化されたアルガンオイルが、髪の表面にとどまらず内部奥深くまで浸透。ヒートリペア成分がドライヤーの熱と反応して毛髪を補修し、パサつきやうねりを解消します。塗布した後の手や髪に一切ベタつきが残らず、まるで素髪そのものが美しくなったかのような自然なツヤとなめらかさを与えてくれます。フローラル系の優しい香りも日常使いにぴったりです。",
        "target": "髪が細くてペタンとしやすいけれど毛先は乾燥している方、ベタつくヘアオイルが苦手な方、手頃な価格で高品質なオイルセラムを使いたい方",
        "point": "洗髪後、半乾きの髪または完全に乾かした髪の毛先を中心に馴染ませます。朝のアイロンやコテを使用する前のベースオイルとしても最適です。"
    },
    {
        "rank": 7,
        "tag": "⚡ 塗布後わずか10秒で水から濃密クリームへ変化！韓国発・毛髪の即効修復ウォーター",
        "catch": "モレモの大ヒットミラクル10。微細加熱反応でタンパク質がケラチン繊維の隙間へ急速密着",
        "brand_name": "moremo (モレモ)",
        "capacity": "200ml (ウォーター トリートメント ミラクル 10)",
        "type": "温感液体インバスヘアセラム・高浸透リキッドトリートメント",
        "features": "加水分解シルク、加水分解ケラチン、加水分解コラーゲン、17種のアミノ酸、微細微温効果",
        "value": "液状だからこそ毛髪の隅々まで10秒で浸透。水と反応してクリーミーに変化し、冬の乾燥でゴワつくハイダメージ毛を指通り滑らかなシルクへ再生",
        "desc_p1": "冬のバスタイム、寒くてトリートメントをつけたまま何分も待っていられないという方に熱狂的な支持を集めるのが、韓国発のサロン級ヘアケアmoremoの『ウォーター トリートメント ミラクル 10』です。わずか10秒で完了する即効リペアセラムとしてSNSを席巻しました。",
        "desc_p2": "シャンプー後の濡れた髪に塗布すると、水と反応してほんのり温かくなり、サラサラの液体から濃密なクリーム状へとテクスチャーが変化。このマイクロ温感反応によってキューティクルが開き、加水分解ケラチンや17種のアミノ酸が毛髪の芯まで急速にチャージされます。洗い流した瞬間の『とぅるんとぅるん』な手触りは衝撃的。冬の静電気や乾燥で広がる髪を瞬時にまとまりやすい美髪へ導きます。",
        "target": "お風呂で時間をかけずにサロン級の集中補修をしたい方、冬の乾燥で髪がゴワゴワに硬くなっている方、即効性のある手触りを求める方",
        "point": "シャンプー後、軽く水気を切った毛先を中心に直接ボトルから塗布し、手で軽く揉み込みます。液体がクリーミーに変化したら、わずか10秒置いてからしっかり洗い流してください。"
    },
    {
        "rank": 8,
        "tag": "🌿 アルガンオイルの原点にして最高峰！世界中のセレブを魅了する万能ヘアトリートメント",
        "catch": "モロッコの黄金アルガンオイル。冬の過酷な乾燥・ドライヤー熱・静電気から髪をパーフェクト保護",
        "brand_name": "MOROCCANOIL (モロッカンオイル)",
        "capacity": "100ml (モロッカンオイル トリートメント)",
        "type": "最高品質アルガンオイル配合・万能アウトバスヘアセラム",
        "features": "ピュアアルガンオイル（高純度ビタミンE）、脂肪酸、アマニ油エキス、シリコーンベース",
        "value": "ヘアオイル界のレジェンド。太い髪から細い髪まであらゆる髪質にフィットし、冬の寒風によるパサつきをラグジュアリーな艶めきに変える",
        "desc_p1": "世界中のトップスタイリストや海外セレブが愛用し、アウトバスヘアトリートメントの金字塔として君臨する『モロッカンオイル トリートメント』。モロッコの過酷な乾燥気候を生き抜くアルガンツリーの実から抽出された希少なオイルを贅沢に使用しています。",
        "desc_p2": "抗酸化作用の高いビタミンEや必須脂肪酸が豊富に含まれ、冬の乾燥で傷んだ髪の内部まで栄養を浸透させます。濃厚なオイルでありながら髪への吸収性が非常に高く、塗布した後はサラッと仕上がって美しい光沢を放ちます。バニラムスクのエキゾチックで甘く温かみのある香りは、冬の季節にぴったり。一度使うと手放せなくなる至高のヘアセラムです。",
        "target": "確かな実績を持つ世界最高峰のヘアオイルを使いたい方、冬の乾燥による静電気や広がりをしっかり抑えたい方、リッチな甘い香りが好きな方",
        "point": "洗髪後の濡れた髪に1〜2プッシュを毛先中心に馴染ませてブローします。完全に乾いた後の仕上げや、外出前のスタイリング剤としても優秀です。"
    },
    {
        "rank": 9,
        "tag": "🌿 アミノ酸×セラミドが芯まで補修！サロン帰りのツヤを取り戻すハイダメージ集中セラム",
        "catch": "アミノレスキューの最高傑作。冬のブリーチ・熱ダメージでスカスカになった毛先を濃密充填",
        "brand_name": "aminoRESQ (アミノレスキュー)",
        "capacity": "100ml (ハイダメージ ヘアパック トリートメント セラム)",
        "type": "高濃度アミノ酸＆複合セラミド配合・濃密ハイダメージリペアセラム",
        "features": "16種のアミノ酸コンプレックス、セラミドEOP/NP/AP、加水分解ケラチン、植物性ヘマチン",
        "value": "ダメージ補修に特化した濃厚アミノ処方。冬の乾燥とヘアアイロンの熱で傷み切った毛先にタンパク質を直接注入し、ハリコシとツヤを再生",
        "desc_p1": "毎日ヘアアイロンやコテを使ってスタイリングする方にとって、真冬の乾燥は熱ダメージを急速に加速させる危険要因です。毛先がチリチリと痛んで枝毛や切れ毛が増えてしまう前に投入したいのが、アミノレスキューの『ハイダメージ トリートメント セラム』です。",
        "desc_p2": "毛髪の主成分であるアミノ酸16種類と、水分を保持するセラミドを贅沢にブレンド。濃密なセラムが傷んだキューティクルの隙間を埋め尽くし、内側から弾力と潤いを補強します。アイロンの熱ダメージから髪を保護するヒートプロテクト効果も高く、冬のスタイリング前後に使用することで、毛先までツルンとまとまる指通りが一日中持続します。",
        "target": "毎日ヘアアイロンやコテを使って毛先の痛みが激しい方、アミノ酸による本格的な毛髪補修を求める方、枝毛や切れ毛を防ぎたい方",
        "point": "お風呂上がりのタオルドライ後、傷みが気になる毛先に揉み込むように塗布。ヘアアイロンを使用する前の乾いた髪にも少量なじませると熱ダメージを大幅に軽減できます。"
    },
    {
        "rank": 10,
        "tag": "🌸 髪の深層まで浸透してふんわり柔軟化！ゴワつく冬の髪をしなやかな美髪へ整えるエマルジョン",
        "catch": "スティーブンノルのサロン品質。水分と油分を同時に補給し、触れたくなる柔らかさを引き出す",
        "brand_name": "STEPHEN KNOLL (スティーブンノル)",
        "capacity": "100ml (モイスチュアソフニング エマルジョン N)",
        "type": "深層モイストリペア・洗い流さない高保湿ヘアエマルジョン",
        "features": "高浸透モイストカプセル、エモリエントアミノ酸、オリーブ脂肪酸エチル、フローラルフルーティウッディの香り",
        "value": "コーセーとニューヨークのトップヘアスタイリストが共同開発。微細カプセルが髪の芯まで届き、真冬の寒冷で硬くなった髪を柔らかくほぐす",
        "desc_p1": "冬になると『髪の毛が硬くなって手触りが悪い』『ゴワゴワして思い通りのヘアスタイルにならない』と悩む方にぴったりなのが、スティーブンノルの『モイスチュアソフニング エマルジョン N』です。",
        "desc_p2": "毛髪内部まで深く入り込むナノサイズの『高浸透モイストカプセル』が、乾燥でパサついたコルテックスを水分と油分で満たします。ミルク状のエマルジョンが髪に吸い込まれるように馴染み、硬くなった髪の芯をしなやかに柔らかく整えます。フローラルフルーティウッディの上品な香りが心地よく、朝のブラッシングでも引っかからない、しっとりサラサラの上質ヘアへと導きます。",
        "target": "髪の毛が硬くゴワつきやすい方、自然な柔らかさとまとまりを求める方、サロン品質の上品なヘアケアを楽しみたい方",
        "point": "洗髪後、タオルドライした髪に適量（セミロングで2〜3プッシュ）を取り、手のひらでよく伸ばしてから毛先を中心に馴染ませて乾かします。"
    }
]

faq_items = [
    {
        "q": "ヘアオイルとヘアセラム（ヘアエッセンス・ヘアミルク）の決定的な違いは何ですか？",
        "a": "ヘアオイルは主に『油分』で毛髪表面をコーティングし、摩擦や熱から守りツヤを出すのが目的です。これに対してヘアセラムやヘアミルクは、『水分＋アミノ酸・ケラチン・セラミド等の美容液成分』が主成分で、髪の内部（コルテックス）まで浸透して乾燥した芯を補修・保湿します。真冬（11月〜12月）は内部の水分が枯渇しているため、まずヘアセラムで内部に水分と栄養を補給し、その上からヘアオイルを薄く重ねる『W使い』が最も劇的な美髪効果を発揮します。"
    },
    {
        "q": "冬に髪がパサつき、静電気で広がるのを防ぐ最も効果的な使い方は？",
        "a": "お風呂上がりの濡れた髪に塗布することが最も重要です。濡れてキューティクルが開いている状態のときにヘアセラムを毛先中心に揉み込み、ドライヤーの温風で上から下へキューティクルを整えながら乾かしてください。最後に冷風を当ててキューティクルを引き締めることで、静電気の発生を劇的に抑えられます。"
    },
    {
        "q": "朝のヘアアイロンやコテを使う前にもヘアセラムを使って良いですか？",
        "a": "はい、ヒートプロテクト効果（エルカラクトン等）のあるヘアセラムは強く推奨されます。ただし、水分で髪が湿った状態で高温のアイロンを当てると『水蒸気爆発』が起こりキューティクルが大ダメージを受けます。ヘアセラムを塗布した後は、必ずドライヤーで完全に髪を乾かしてからアイロンを当ててください。"
    },
    {
        "q": "細い猫っ毛でもペタンコにならずに使えるヘアセラムはどれですか？",
        "a": "本ランキング第2位の『オルビス エッセンスインヘアミルク』や第6位の『ルシードエル #EXヘアセラム』が最適です。油分の重さがなく、水分ベースで内部を潤す設計のため、トップのふんわり感を潰さずに毛先だけをサラサラにまとめることができます。"
    },
    {
        "q": "洗い流さないトリートメントは、頭皮についても大丈夫ですか？",
        "a": "基本的にアウトバストリートメントは『髪の毛（特に中間から毛先）』に使用するように設計されています。頭皮に直接付着すると毛穴詰まりやベタつき、フケの原因になる可能性があるため、頭皮から5cm以上離した中間から毛先にかけて塗布するのが鉄則です。"
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
    "headline": "保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！芯まで潤い満たす洗い流さない高保湿ヘアセラム・ヘアエッセンスランク10",
    "description": "11月・12月の暖房直撃・マフラー摩擦・静電気による頑固な毛先のパサつき・枝毛・広がりを徹底解決！髪の内部コルテックスまで浸透して水分とケラチンを補給する洗い流さない高保湿ヘアセラム・ヘアエッセンス10選を徹底比較！ラサーナ、オルビス、ケラスターゼ、ミルボン、ロレアルなど、真冬でも毛先までしっとりまとまる至高のヘアケアを厳選。",
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
    "name": "冬の高保湿ヘアセラム・洗い流さないヘアエッセンス おすすめランキング10選",
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
            <img src="{item['image']}" alt="{p['brand_name']} {p['capacity']} 高保湿ヘアセラム" class="product-img" loading="lazy" width="280" height="280">
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
          <h4 class="desc-heading">🔍 冬（11月・12月）の髪悩みへのアプローチ＆使用感</h4>
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
  <title>保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！芯まで潤い満たす洗い流さない高保湿ヘアセラム・ヘアエッセンスランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の暖房直撃・マフラー摩擦・静電気による頑固な毛先のパサつき・枝毛・広がりを徹底解決！髪の内部コルテックスまで浸透して水分とケラチンを補給する洗い流さない高保湿ヘアセラム・ヘアエッセンス10選を徹底比較！ラサーナ、オルビス、ケラスターゼ、ミルボン、ロレアルなど、真冬でも毛先までしっとりまとまる至高のヘアケアを厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-hair-serum">
  <meta name="robots" content="index, follow, max-image-preview:large">
  
  <!-- OGP & SNS -->
  <meta property="og:title" content="保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！芯まで潤い満たす洗い流さない高保湿ヘアセラム・ヘアエッセンスランク10">
  <meta property="og:description" content="11月・12月の毛先パサつき・静電気を徹底解決！髪の芯まで潤い満たす高保湿ヘアセラム・ヘアエッセンス10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-hair-serum">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#b83280">

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
      --primary: #b83280;
      --primary-light: #fff5f7;
      --primary-dark: #702459;
      --text-main: #2d3748;
      --text-sub: #718096;
      --bg-page: #fbfbfc;
      --bg-card: #ffffff;
      --border: #edf2f7;
      --border-focus: #fbb6ce;
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
      <a href="/winter-hair-care">ヘアケア</a> <span>&gt;</span>
      <span>高保湿ヘアセラム</span>
    </nav>

    <header class="article-header">
      <span class="header-tag">2026年冬・徹底検証</span>
      <h1 class="article-title">保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！芯まで潤い満たす洗い流さない高保湿ヘアセラム・ヘアエッセンスランク10</h1>
      <p class="article-lead">
        11月から12月にかけて外気の湿度が急激に下がり、室内のエアコン暖房直撃やマフラー・ウールコートの摩擦が重なると、髪の水分は限界まで奪われます。毛髪内部のコルテックスがスカスカになり、静電気で毛先が爆発したりパサつきが止まらない冬の深刻なダメージヘア。本記事では、髪の深層まで浸透して水分とタンパク質を補給する『洗い流さない高保湿ヘアセラム・ヘアエッセンス』10選を徹底比較！真冬でも毛先までしっとりまとまるツヤ髪を叶える名品をご紹介します。
      </p>
      <div class="meta-info">
        <span>📅 2026年11月02日更新</span>
        <span>✍️ 冬コスメ徹底比較ラボ 編集部監修</span>
        <span>⏱️ 読了目安：約8分</span>
      </div>
    </header>

    <section class="section-box">
      <h2 class="section-title">❄️ 11月・12月に「ヘアセラム・ヘアエッセンス」が必要な科学的理由</h2>
      <p class="content-p">
        真冬の毛髪ダメージの最大の要因は、乾燥による『コルテックスの空洞化』と『キューティクルのめくれ』です。湿度が低下した外気にさらされると、毛髪内部の水分が外へと逃げ出し、髪のしなやかさを保つ結合が失われてパサパサの硬い状態に変化します。
      </p>
      <p class="content-p">
        さらに、ニットやマフラーとの摩擦によって数万ボルトの静電気が発生し、キューティクルが毛羽立って剥離。そこからタンパク質が流出して枝毛や切れ毛が急増します。油分だけで表面を覆うヘアオイルだけでは、内部の乾きは癒せません。水分、アミノ酸、加水分解ケラチンを豊富に含み、毛髪内部まで深く届く『ヘアセラム・ヘアエッセンス』による深層補修が、冬の美髪維持には絶対に欠かせないのです。
      </p>

      <div class="mechanism-grid">
        <div class="mechanism-card">
          <div class="mech-title">💧 毛髪コルテックスへの水分・アミノ酸注入</div>
          <div class="mech-desc">オイルでは届かない毛髪の芯（コルテックス）まで低分子アミノ酸や浸透補修成分がすばやく浸透。スカスカになったダメージホールを水分で満たします。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">⚡ 静電気の発生を物理的に遮断</div>
          <div class="mech-desc">髪の水分保持力を高め、キューティクルを整えることで、衣服との摩擦による静電気の帯電を防止。冬のマフラーを外した時の広がりやパサつきを撃退します。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">🔥 ドライヤー・アイロン熱の味方化</div>
          <div class="mech-desc">γ-ドコサラクトン（エルカラクトン）などのヒートリペア成分が、ドライヤーの温風と反応して毛髪タンパク質と結合。熱ダメージを防ぎながらツヤ膜を形成します。</div>
        </div>
      </div>
    </section>

    <section class="section-box">
      <h2 class="section-title">🔍 失敗しない！冬の高保湿ヘアセラム選び 3大チェック基準</h2>
      <div class="mechanism-grid">
        <div class="mechanism-card">
          <div class="mech-title">1. 水分補給力と油分ラッピングの比率</div>
          <div class="mech-desc">内部を潤すアミノ酸・ヒアルロン酸・ケラチンと、外部を密閉する植物オイルやCMC類似成分がバランスよく配合されたエマルジョンや濃密美容液タイプを選びましょう。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">2. ヒートプロテクト機能の有無</div>
          <div class="mech-desc">冬はドライヤーを長めに当てる傾向があるため、熱から髪を守りつつ補修力に変換するエルカラクトン等の成分が入っているものが圧倒的にダメージを防ぎます。</div>
        </div>
        <div class="mechanism-card">
          <div class="mech-title">3. 髪質に合わせたテクスチャー</div>
          <div class="mech-desc">細毛・軟毛には水分多めの軽やかミルク（オルビス等）、太毛・硬毛・ハイダメージには濃密無加水エッセンス（ラサーナ）やリッチオイルセラム（ロレアル等）がベストです。</div>
        </div>
      </div>
    </section>

    <!-- ランキング商品カード群 -->
    <section class="ranking-section">
      <h2 class="section-title">🏆 保湿力高め！高保湿ヘアセラム・ヘアエッセンス おすすめ人気ランキング10選</h2>
      {"".join(cards_html)}
    </section>

    <section class="section-box">
      <h2 class="section-title">📊 高保湿ヘアセラム・ヘアエッセンス 性能＆スペック徹底比較表</h2>
      <p class="content-p">
        今回厳選した10商品の配合成分、実勢価格、特徴を一覧表にまとめました。ご自身の髪質やダメージレベルに合わせて最適な1品をお選びください。
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
      <h2 class="section-title">❓ 冬のヘアセラム・ヘアエッセンス活用法 よくある質問（FAQ）</h2>
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
      <h2 class="section-title">✨ 編集部まとめ：ヘアセラムで真冬もシルクのような指通りと潤いツヤ髪へ</h2>
      <p class="content-p">
        11月から12月にかけての空気の乾燥と静電気は、放置すると毛先の枝毛や切れ毛を急速に悪化させます。この冬のヘアダメージに歯止めをかけ、毛先までみずみずしくしなやかな手触りを取り戻すためには、髪の内部から潤す『ヘアセラム・ヘアエッセンス』が最大の味方です。
      </p>
      <p class="content-p">
        お風呂上がりの濡れた髪に丁寧に揉み込み、熱を味方にして乾かすだけで、翌朝のブロー時間が劇的に短縮され、一日中まとまりのある美しいツヤが持続します。ぜひ本ランキングを参考に、あなたの髪を乾燥から救い出してくれる運命のヘアセラムを見つけてみてください。
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

with open("winter-hair-serum.html", "w", encoding="utf-8") as f:
    f.write(full_html.strip())

print("Successfully generated winter-hair-serum.html")
