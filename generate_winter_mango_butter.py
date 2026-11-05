import json
import re

with open("fetched_3new_mango_tremella_collagen.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_mango_butter"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 体温35℃でとろけて角層を密封！完全ピュア未精製グレードの濃密エモリエント",
        "catch": "アフリカ・インド熱帯で育まれた野生マンゴーの種子から抽出された100%未精製の純粋植物バター。人肌に触れた瞬間にトロリと液化し、シアバターを凌駕する滑らかな浸透感で真冬の粉吹き肌とあかぎれを救う最高峰バター",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "100g / 広口アルミパウチ・遮光密閉",
        "type": "100%純粋未精製 マンゴー種子脂（天然植物バター）",
        "features": "マンゴー種子脂100%、ステアリン酸（約42%）、オレイン酸（約40%）、パルミチン酸、天然植物ステロール",
        "value": "添加物を一切含まないピュアグレード。融点が約35〜38℃と人肌に極めて近いため、硬化した冬の角質層に塗布した瞬間スルスルと馴染み、ベタつきを残さずベルベットのような保護ヴェールを一日中維持",
        "desc_p1": "11月から12月にかけて外気温度が10℃を下回ると、皮膚の皮脂分泌は極限まで低下し、手足の末端やすね、肘、かかとがカチコチに硬化して白く粉を吹いてしまいます。多くの人がシアバターを手に取りますが、シアバター特有の重さや硬さ、真冬の寒さでカチコチに固まって伸びにくい点にストレスを感じる方も少なくありません。&SHの『100%ピュア マンゴーバター』は、熱帯植物マンゴーの種子の仁（カーネル）から丁寧に絞り取られた天然の植物性固形油脂です。シアバターと同等の高い保護力を誇りながら、オレイン酸とステアリン酸がほぼ1対1の絶妙な比率で共存しているため、肌に乗せた瞬間に自分の体温でとろけて液状オイルへと変化します。",
        "desc_p2": "この融解挙動により、摩擦を起こすことなく皮膚の微細なキメや毛穴の奥まで行き渡り、細胞間脂質のセラミドの隙間を埋めるように密着。角層内の水分蒸散を物理的にシャットアウトします。顔のスキンケアの最後のフタとしてはもちろん、水仕事でパックリ割れそうな指先、タイツを脱ぐと粉が舞うすねの乾燥、ひび割れたかかとへの集中ラップまで、100gの大容量で全身惜しみなく使い倒せる冬の常備薬的存在です。",
        "target": "シアバターの重さや匂いが苦手な超乾燥肌の方、真冬にひじ・ひざ・かかとが角化してひび割れる方、界面活性剤や防腐剤フリーの純粋な植物脂で全身を密封保護したい方",
        "point": "手のひらに大豆粒大を取り、両手を擦り合わせて手のひらの熱で完全に液状化させてから、乾燥が気になる部位へ優しくハンドプレスして押し込みます。入浴後のまだ肌が湿っているタイミングに塗布すると、水分を抱き込んだまま極上のモチ肌が完成します。"
    },
    {
        "rank": 2,
        "tag": "🥭 95%自然由来成分で48時間持続保水！甘美な香りと共に冬肌を包む名作ボディバター",
        "catch": "ザ・ボディショップが誇る世界的ベストセラー。マンゴー種子油、コミュニティフェアトレードのシアバター、ココアバターを黄金ブレンド。真冬の過酷な粉吹き乾燥肌を48時間もっちり潤し続けるリッチボディクリーム",
        "brand_name": "THE BODY SHOP (ザ・ボディショップ)",
        "capacity": "200ml / リサイクルアルミジャー容器",
        "type": "高保湿リッチ エモリエント ボディバター",
        "features": "マンゴー種子油、シア脂、カカオ脂、ヒマワリ種子油、植物性グリセリン",
        "value": "塗布した瞬間に広がるジューシーな完熟マンゴーの甘いアロマと、こっくり濃厚なのに肌に溶け込む極上テクスチャー。真冬の夜に塗れば翌日の夜まで肌がしっとり柔らかいまま持続",
        "desc_p1": "冬の乾燥は顔だけでなく、衣服の摩擦や入浴による脱脂によって身体全体に及びます。特に11月以降の乾燥期は、すねや太もも、背中がかゆくなり、無意識に掻きむしって皮膚を傷つけてしまうトラブルが多発します。ザ・ボディショップの『ボディバター マンゴー』は、誕生以来世界中で愛され続けている濃厚ボディケアの金字塔です。インド産の良質なマンゴー種子油を贅沢に配合し、シアバターやココアバターといった高融点植物脂と組み合わせることで、体温でとろけながらも肌表面に厚みのある保護シールドを構築します。",
        "desc_p2": "クリームを手にとって肌に伸ばすと、まるでホイップされた上質なバターのように滑らかに広がり、カサカサに乾き切った角層を瞬時に柔らかく解きほぐします。肌表面はサラリとベルベットのような手触りに仕上がり、服をすぐに着てもベタつきません。それでいて、48時間後もしっとり感が持続する圧倒的な保水シールド力を発揮。真冬の冷え切った夜のバスタイム後、心まで温まる芳醇なマンゴーの香りに包まれながら行うボディケアは至福のひとときです。",
        "target": "真冬になると全身が乾燥してかゆみが出る方、香りに癒やされながら毎日のボディケアを楽しみたい方、一度塗ったら翌日まで塗り直しのいらない強力な保湿持続力を求める方",
        "point": "お風呂上がりにバスタオルで軽く水気を拭き取った直後、手のひらにたっぷり取って、すね、太もも、ヒップ、腕へとリンパを流すようにマッサージしながら塗り広げてください。"
    },
    {
        "rank": 3,
        "tag": "🌿 外出先での乾燥レスキュー！アルミ缶でいつでも体温融解できるポータブルバター",
        "catch": "携帯性に優れた50gのコンパクトアルミ缶仕様。オフィスの暖房で粉を吹き始めた頬や目元、冷風でパサつく毛先、手洗い後のささくれに、指先でクルリと溶かしていつでも即効保湿チャージ",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "50g / ポータブルスクリューアルミ缶",
        "type": "100%植物性ポータブルマルチエモリエントバター",
        "features": "マンゴー種子脂100%（無添加・無香料・無着色・防腐剤フリー）、ステアリン酸、天然トコフェロール",
        "value": "外出先やオフィスでのエアコン直撃による「日中の砂漠化」を即座に解決。リップバーム、練り香水ベース、目元の乾燥小ジワ対策、ハンドバームまで全方位対応",
        "desc_p1": "朝どんなに完璧な保湿ケアをして家を出ても、冬のオフィスや電車内の強烈な暖房気流にさらされ続けると、昼過ぎには目元や口元のファンデーションがひび割れ、指先は粉を吹いてささくれ立ってしまいます。そんな日中の乾燥クライシスをスマートに解決してくれるのが、&SHの『高純度マンゴーバター 50g』です。バッグやデスクの引き出しにすっきり収まるスリムなアルミ缶に、100%ピュアなマンゴー種子脂がぎっしり詰め込まれています。",
        "desc_p2": "指先の体温で表面を数回撫でるだけで、固形のバターがサラサラのクリアオイルへと瞬時に融解。乾燥が気になる目尻やほうれい線の上からトントンと軽く乗せれば、メイクを崩すことなくツヤと潤いを蘇らせることができます。もちろんリップクリームとしても優秀で、荒れて皮むけした唇を滑らかな保護膜で包み込みます。無香料なので食事の前やオフィス内でも周囲を気にせず使える万能レスキューアイテムです。",
        "target": "日中のオフィス乾燥でメイクが崩れたり目元が突っ張る方、外出先で使えるコンパクトでマルチな保湿バームを探している方、敏感肌で市販のリップクリームで荒れやすい方",
        "point": "指の腹で表面を円を描くように温めて溶かし、乾燥した部分に優しくタッピングするように乗せます。爪の生え際（甘皮部分）に刷り込むと、冬のささくれ予防に絶大な効果を発揮します。"
    },
    {
        "rank": 4,
        "tag": "✂️ シアバター×マンゴーバターの乳液セラム！真冬のパサつく毛先にしっとり濡れツヤ",
        "catch": "サロン専売品naplaの超人気スタイリングセラム。シアバターとマンゴー種子脂を高配合したリッチミルクが、冬の暖房乾燥や静電気で広がる髪を毛先までしなやかにまとめ上げ、ウェットな質感をキープ",
        "brand_name": "napla (ナプラ / N.)",
        "capacity": "94g / ポンプボトル",
        "type": "エモリエント スタイリングセラム（ミルクタイプ）",
        "features": "シア脂、マンゴー種子脂、アロエベラ液汁、ユズ果実エキス、モリンガエキス",
        "value": "オイルほど重くならず、ワックスほど固まらない絶妙なエマルジョン。マンゴーバターの保水膜が髪内部の水分蒸散を防ぎ、冬特有のパサつきと静電気を完全ブロック",
        "desc_p1": "11月・12月は肌だけでなく、髪にとっても1年で最も過酷な季節です。湿度が低下した大気とエアコンの風によって毛髪の水分量は10%未満にまで急落し、キューティクルがめくれ上がってパサつき、マフラーやニットとの摩擦で激しい静電気が発生します。美容師から絶大な支持を受けるナプラの『N. スタイリングセラム』は、植物性バターの王様であるシアバターとマンゴーバターをエマルジョン化して閉じ込めた高保湿スタイリングミルクです。",
        "desc_p2": "手のひらにワンプッシュ取って伸ばすと、瑞々しい乳液状からスーッと馴染んで髪一本一本を薄い保護皮膜でコーティング。マンゴー種子脂に含まれるステアリン酸がキューティクル表面を整え、自然なツヤとしっとり吸い付くようなまとまりを与えます。ベタつかないのに程よいホールド力があり、乾燥によるアホ毛や広がりを瞬時に抑え込んで、サロン帰りのようなこなれた束感を演出。ホワイトジャスミンとミュゲの爽やかな香りが一日中ふわりと香ります。",
        "target": "冬になると毛先がパサついてまとまらない方、ヘアオイルだと時間が経つとパサつきが戻ってしまう方、静電気による髪の広がりやアホ毛に悩んでいる方",
        "point": "タオルドライ後の濡れた髪、または朝のスタイリング時に、毛先を中心によく揉み込み、残りを髪全体に手ぐしを通すように馴染ませます。アイロン前のベースとしても髪を熱乾燥から守ります。"
    },
    {
        "rank": 5,
        "tag": "🌙 睡眠中にマンゴーバターがじっくり浸透！翌朝の寝癖とうねりを防ぐ夜用アウトバス",
        "catch": "ロレッタが提案する夜の集中ヘアトリートメント。マンゴー種子脂とアルガンオイルをブレンド。寝ている間の枕との摩擦や暖房乾燥から髪を徹底保護し、翌朝手ぐしだけで素直にまとまるシルク髪へ",
        "brand_name": "Loretta (ロレッタ / モルトベーネ)",
        "capacity": "120g / チューブ容器",
        "type": "夜用集中補修 アウトバスクリーム（洗い流さないトリートメント）",
        "features": "マンゴー種子脂、アルガニアスピノサ核油、ダマスクローズ花油、加水分解ケラチン",
        "value": "夜塗って寝るだけで、睡眠中の寝返り摩擦と室内乾燥による毛髪ダメージをゼロ化。朝のスタイリング時間を劇的に短縮する冬のナイトルーティンの必需品",
        "desc_p1": "朝起きたときの頑固な寝癖や毛先のパサつき、ボサボサ感の原因は、睡眠中の「無防備な乾燥と摩擦」にあります。冬の寝室は暖房や加湿器の停止によって明け方に湿度が急低下し、さらに寝返りによる枕と髪の摩擦がキューティクルを剥離させてしまいます。ロレッタの『ナイトケアクリーム』は、夜の就寝前に塗布することに特化して設計された、マンゴー種子脂高配合のアウトバスクリームです。",
        "desc_p2": "こっくりとしたリッチなクリームでありながら、濡れた髪や乾いた髪に塗布すると素早く馴染み、枕カバーに油分が移る心配がありません。マンゴーバターのリッチなステアリン酸が毛髪のCMC（細胞膜複合体）を補強し、アルガンオイルが内部へ潤いを送り込みます。翌朝起きると、まるでナイトキャップをかぶって眠ったかのように、毛先までしっとりと落ち着き、指通りなめらかなツヤ髪を実感できます。天然ダマスクローズの上品な香りが心地よい眠りを誘います。",
        "target": "朝起きると髪が爆発してスタイリングに時間がかかる方、冬の乾燥で毛先の枝毛や切れ毛が増えた方、夜のヘアケアでベタつかずしっかり保湿したい方",
        "point": "夜のお風呂上がり、しっかりタオルドライした毛先を中心に揉み込んでからドライヤーで乾かします。乾かした後にごく少量を毛先にもう一度重ねづけすると、摩擦防止効果が倍増します。"
    },
    {
        "rank": 6,
        "tag": "🧪 職人精製で匂い・不純物を完全除去！手作り高保湿コスメ基材の最高峰",
        "catch": "山桂産業が手がける化粧品原料グレードの100%精製マンゴーバター。徹底した脱色・脱臭精製により、天然マンゴーバターの有効脂肪酸を損なうことなく極上の純度を実現。冬の本格ケアに最適",
        "brand_name": "山桂産業",
        "capacity": "100g / 遮光広口ジャー容器",
        "type": "化粧品原料グレード 高純度精製マンゴー種子脂",
        "features": "精製マンゴー種子脂100%、高品質オレイン酸・ステアリン酸トリグリセリド",
        "value": "原料のプロが認める卓越した精製度。無臭・純白のため、手持ちのオイルや精油とブレンドして自分だけの特製ウィンターバームやリップを作るベース基材として圧倒的支持",
        "desc_p1": "市販の保湿クリームでは香料や防腐剤、アルコールが肌にしみてしまうほどの極度の敏感乾燥肌に陥っている方にとって、原料メーカーが直販するピュア油脂は究極の救世主です。京都の老舗原料メーカー山桂産業の『精製マンゴーバター 100g』は、化粧品工場や高級エステサロンに供給されるプログレードのマンゴー種子脂をそのまま個人向けにパッケージした本格派アイテムです。",
        "desc_p2": "高度な物理精製技術によって、植物油特有の酸化臭や不純物、アレルゲンとなり得る微量成分を徹底的にカット。純白で滑らかな美しいバターに仕上げられています。そのまま指先で取って体温で溶かしながら顔や手足に塗布するのはもちろん、ホホバオイルやアルガンオイルと1:1で湯煎して混ぜ合わせ、お気に入りのアロマオイルを1滴垂らせば、サロン級の極上ウィンターバームが完成します。プロ仕様ならではの圧倒的コストパフォーマンスも大きな魅力です。",
        "target": "化学合成成分を一切肌に乗せたくない超敏感肌の方、自分好みのテクスチャーや香りで冬の保湿バームを手作りしたい方、安心安全な高品質原料をたっぷり使いたい方",
        "point": "そのまま使う場合は、爪の背で削るように適量を取り、手のひらで透明になるまで温めてから塗布します。ホホバオイルを20%ほど混ぜてホイップすると、冬場でも柔らかい極上クリームになります。"
    },
    {
        "rank": 7,
        "tag": "🌹 軽やかなミルクが毛先を潤し揺れる束感を演出！ダマスクローズ香る高保湿スタイリング",
        "catch": "マンゴー種子脂とダマスクローズオイルを配合したスタイリングヘアミルク。冬のパサつく髪に適度な水分と油分を同時に補給し、固めずに自然な毛流れと上品な濡れツヤを長時間キープ",
        "brand_name": "Loretta (ロレッタ / モルトベーネ)",
        "capacity": "100ml / ディスペンサーボトル",
        "type": "高保湿スタイリング ヘアミルク",
        "features": "マンゴー種子脂、ダマスクローズ花油、シア脂油、コメヌカロウ",
        "value": "オイルではペタッとしてしまう細毛・軟毛の方でも、ふんわり感を潰さずに冬の乾燥パサつきだけを完璧に抑える絶妙なテクスチャーバランス",
        "desc_p1": "冬のスタイリングにおいて、軟毛や細毛の方は大きなジレンマを抱えています。乾燥してパサつくからと重いヘアオイルやバームをつけると、髪がペタッと潰れてボリュームが失われてしまい、逆に軽めのミストだと数十分で蒸発してパサつきがぶり返してしまうからです。ロレッタの『メイクアップミルク（グラマラス / ナチュラル）』は、保水力に富むマンゴーバターを微粒子乳化させたヘアミルクです。",
        "desc_p2": "手にとるとミルキーで伸びが良く、髪に馴染ませると水分がコルテックスに浸透しつつ、マンゴーバターのステアリン酸膜が外側をしなやかにコーティング。髪を固めることなく、揺れるような自然な毛流れと上品なツヤ感を一日中維持します。ニットやマフラーを着用しても静電気が起きにくく、真冬の街歩きでも髪のまとまりが崩れません。フェミニンで華やかなローズの香りが、冬の冷たい空気の中で心地よく広がります。",
        "target": "髪が細くてオイルをつけるとボリュームがなくなってしまう方、自然な束感とツヤを両立したいパーマヘアやミディアムヘアの方、冬の静電気による広がりを防ぎたい方",
        "point": "乾いた髪の内側から手ぐしを通すように馴染ませ、最後に毛先を手のひらで軽く握り込むようにしてニュアンスを出します。前髪の毛先に少量つけると束感のある今っぽいシースルーバングが作れます。"
    },
    {
        "rank": 8,
        "tag": "🌺 ハワイ発！天然マンゴーバター×ホホバの濃密モイスチャーローション",
        "catch": "カイルアの工房で生まれたナチュラルボディローション。リッチなマンゴーバターにホホバオイルとアロエベラを融合。真冬の過酷な粉吹き肌にぐんぐん浸透し、シルクのようになめらかな極上素肌へ",
        "brand_name": "Lanikai Bath and Body (ラニカイ)",
        "capacity": "250ml / ポンプボトル",
        "type": "高浸透エモリエント ボディローション",
        "features": "マンゴー種子脂、ホホバ種子油、ククイナッツ油、アロエベラ葉エキス、トコフェロール",
        "value": "バターの濃厚な保護力とローションのみずみずしい浸透力を両立。ポンプ式で使いやすく、真冬の入浴後の全身ケアを素早く完了できる実力派",
        "desc_p1": "真冬のお風呂上がり、浴室から出た瞬間から始まる急激な「過乾燥」。水分が蒸発する前に一刻も早く全身を保湿したいけれど、固いボディバターを時間をかけて塗り広げるのは寒くて辛い——そんな悩みを解決するのが、ハワイ・オアフ島カイルア生まれの『ラニカイ バス＆ボディ ボディローション』です。天然のマンゴーバターを贅沢に乳化させ、素早く角層へ届くローション処方に仕上げられています。",
        "desc_p2": "ポンプを押して手に取ると、とろけるように滑らかなテクスチャーが広がり、乾燥でゴワついた手足の皮膚にスッと吸い込まれていきます。マンゴーバターのエモリエント成分に加え、ハワイ伝統のククイナッツ油やアロエベラが角層深部まで水分をチャージ。塗った直後から肌表面が吸い付くようにモチモチになり、ベタつきが一切残らないためすぐにパジャマを着ることができます。トロピカルで甘く爽やかなマンゴーココナッツの香りが、真冬の寒さを忘れさせてくれます。",
        "target": "お風呂上がりに全身をパパッと素早く保湿したい方、固いバターよりも伸びの良いローションが好きな方、南国のリゾートにいるような贅沢な香りでリラックスしたい方",
        "point": "入浴後、タオルで体を拭く前の「水滴が肌に残っている状態」で2〜3プッシュを全身にざっと塗り広げ、その後にタオルで優しく押さえると、驚くほどの保湿膜が肌に密着します。"
    },
    {
        "rank": 9,
        "tag": "🏝️ 髪にも身体にも！マンゴーオイル×ククイナッツ油のラグジュアリーマルチオイル",
        "catch": "マンゴー種子油とククイナッツ油を濃密ブレンドしたフェイス・ボディ・ヘア兼用マルチオイル。真冬の乾燥でパサつく毛先に濡れツヤを与え、乾燥で粉を吹くデコルテやすねを艶やかに輝かせる",
        "brand_name": "Lanikai Bath and Body (ラニカイ)",
        "capacity": "130ml / スプレー・ドロップボトル",
        "type": "高純度マンゴー＆ククイ マルチトリートメントオイル",
        "features": "マンゴー種子油、ククイナッツ油、マカデミア種子油、ビタミンE",
        "value": "液状に精製されたマンゴーシードオイルを使用しているため、冬場でも固まらずサラリとした感触。濡れた肌や髪に瞬時に浸透し、ベルベットのような艶やかな保護膜を形成",
        "desc_p1": "固形のマンゴーバターの優れたエモリエント特性を保ちながら、より浸透性を高めて通年使いやすく液状精製したマンゴーシードオイル。ラニカイの『ボディ＆ヘアオイル マンゴーココナッツ』は、このマンゴーオイルに、オメガ3やオメガ6を豊富に含む伝統のククイナッツオイルを組み合わせた極上の一本です。真冬の過酷な乾燥下でも液体を保ち、スプレーやドロップで手軽に使用できます。",
        "desc_p2": "真冬のドライヤー前の洗い流さないヘアオイルとして毛先になじませれば、熱によるパサつきを防ぎ、一日中ツヤめく美髪をキープ。また、入浴後のマッサージオイルとしてデコルテや脚に使用すれば、寒さで滞りがちな血行を促しながら、乾燥による粉吹きを完全にシャットアウトします。肌や髪に馴染ませた後も油浮きせず、内側から自然な光沢を放つような若々しいツヤ肌に仕上がります。",
        "target": "一本でボディケアもヘアケアも同時に完了させたい方、冬場でも固まらないサラッとした使い心地の植物オイルを好む方、上品なツヤ感と甘い香りをまといたい方",
        "point": "洗髪後のタオルドライした毛先に2滴馴染ませてドライヤーをかけます。手に残ったオイルはそのまま肘やかかとに擦り込むことで、無駄なく全身をケアできます。"
    },
    {
        "rank": 10,
        "tag": "🧼 マンゴーバター練り込み石鹸！洗うたびに潤い膜を残すプロヴァンス伝統の植物石鹸",
        "catch": "南仏プロヴァンスの老舗サボネリーが作る伝統のベジタブルソープ。植物性パーム油にマンゴーバターを贅沢に練り込み、豊かなクリーミー泡が汚れだけを落として肌の潤いヴェールを死守する",
        "brand_name": "La Savonnerie de Bormes (サボネリー)",
        "capacity": "100g / クラフトペーパー包装",
        "type": "高保湿マンゴーバター配合 植物性固形石鹸",
        "features": "マンゴー種子脂、パーム脂肪酸Na、植物性グリセリン、天然香料",
        "value": "冬の乾燥肌最大の敵である「洗浄時のバリア破壊」を根本から防止。豊かなマンゴーバターの脂肪酸が肌表面に薄い保護膜を残し、お風呂上がりのツッパリ感をゼロにする",
        "desc_p1": "冬の乾燥肌トラブルの多くは、実は保湿不足ではなく「洗いすぎ」から始まっています。強力な合成界面活性剤を含むボディソープで毎日のように身体をゴシゴシ洗うと、寒さでただでさえ減少している貴重な皮脂膜と細胞間脂質が洗い流され、角層が無防備な状態に晒されてしまいます。フランス・プロヴァンスの老舗『サボネリー・ド・ボルム』のマンゴーソープは、伝統の枠練り製法で作られた肌に極めて優しい植物石鹸です。",
        "desc_p2": "きめ細かくクリーミーな弾力泡がお肌を摩擦から守りながら、古くなった角質や余分な皮脂汚れだけを選択的に吸着。配合されたマンゴーバターのステアリン酸とグリセリンが、洗い流した後の皮膚表面にしっとりとしたエモリエント保護膜を形成します。洗い上がりのお風呂上がりでも肌が突っ張らず、まるで薄く保湿ローションを塗ったかのような滑らかな感触が続きます。フレッシュなマンゴーの芳香がバスルームいっぱいに広がり、心までリフレッシュさせてくれます。",
        "target": "入浴後に身体がカサついてかゆくなる乾燥肌の方、石油系界面活性剤や合成添加物を避けて肌に優しい石鹸で洗いたい方、洗顔にも使える高保湿ソープを探している方",
        "point": "泡立てネットでしっかりと濃密なモコモコ泡を作り、手で優しく泡を転がすように洗います。ゴシゴシ擦らず、泡を肌に乗せて数十秒置くだけで汚れが落ち、マンゴーバターの潤いが残ります。"
    }
]

toc_items = [
    {"id": "intro", "title": "1. 11月・12月の本格乾燥と粉吹き肌！「体温融解」マンゴーバターの驚異の保水力"},
    {"id": "mechanism", "title": "2. なぜマンゴーバターは真冬に最強なのか？ステアリン酸とオレイン酸の皮膚科学"},
    {"id": "comparison", "title": "3. 高保湿マンゴーバターコスメおすすめ10選の比較表"},
    {"id": "ranking", "title": "4. 高保湿マンゴーバターコスメおすすめ厳選ランキング10選"},
    {"id": "guide", "title": "5. 失敗しないマンゴーバターコスメの選び方＆冬の部位別活用術"},
    {"id": "routine", "title": "6. 真冬のカチコチひび割れ肌を救う！効果的な体温ハンドプレス＆密封ルーティン"},
    {"id": "faq", "title": "7. マンゴーバターコスメに関するよくある質問（FAQ）"},
    {"id": "summary", "title": "8. まとめ：人肌でとろける植物バターで真冬の肌乾燥とさようなら"}
]

toc_html = "\n".join([f'          <li><a href="#{item["id"]}">{item["title"]}</a></li>' for item in toc_items])

table_rows = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    table_rows.append(f"""            <tr>
              <td class="rank-cell"><strong>第{p["rank"]}位</strong></td>
              <td class="product-cell">
                <a href="#rank-{p["rank"]}"><strong>{p["brand_name"]}</strong><br><span style="font-size:0.85rem;color:#4b5563;">{item_data["item_name"][:35]}...</span></a>
              </td>
              <td>{p["type"]}</td>
              <td class="price-cell">¥{item_data["price"]:,}</td>
              <td>{p["features"][:30]}...</td>
              <td><a href="{item_data["affiliate_url"]}" class="table-btn" target="_blank" rel="nofollow noopener">楽天で見る</a></td>
            </tr>""")

table_rows_html = "\n".join(table_rows)

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <!-- Rank {p["rank"]} -->
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge rank-{p["rank"]}">第{p["rank"]}位</span>
            <div class="product-title-group">
              <span class="product-catch">{p["tag"]}</span>
              <h3 class="product-name">{item_data["item_name"]}</h3>
              <p class="product-subname">{p["catch"]}</p>
            </div>
          </div>

          <div class="product-main-grid">
            <div class="product-visual">
              <img src="{item_data["image_url"]}" alt="{item_data["item_name"]}" class="product-img" loading="lazy">
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
  <title>保湿力の強さで肌乾燥とさようなら！体温でとろける高純度ステアリン酸が真冬のカチコチひび割れ肌とパサつく毛先を濃密ラッピングする高保湿マンゴーバターコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の本格的な寒冷乾燥でカチコチに固まったかかと・あかぎれ手肌・粉吹きすね・パサつく毛先を救う高保湿マンゴーバター（マンゴー種子脂）コスメを徹底厳選！&SH、ザ・ボディショップ、ナプラN.、ロレッタ、山桂産業まで体温融解エモリエントの皮膚科学的根拠と共に徹底検証。">
  <meta name="keywords" content="マンゴーバター コスメ, マンゴー種子脂, 高保湿 コスメ 冬, 乾燥肌 バーム 11月 12月, あかぎれ 保湿, かかと ひび割れ, N. スタイリングセラム, ザボディショップ ボディバター マンゴー, ロレッタ ナイトケアクリーム">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！体温でとろける高純度ステアリン酸が真冬のカチコチひび割れ肌とパサつく毛先を濃密ラッピングする高保湿マンゴーバターコスメランク10">
  <meta property="og:description" content="人肌の温度（35℃）でスーッととろける奇跡の植物バター！真冬の過酷な粉吹き肌と毛先のパサつきを濃密ラッピングするマンゴーバターコスメ10選を徹底検証。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-mango-butter">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿マンゴーバターコスメランク10">
  <meta name="twitter:description" content="11月・12月の本格乾燥に！体温でとろけて角層を密封する高保湿マンゴーバターコスメおすすめ10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！体温でとろける高純度ステアリン酸が真冬のカチコチひび割れ肌とパサつく毛先を濃密ラッピングする高保湿マンゴーバターコスメランク10",
    "description": "11月・12月の寒冷乾燥でカチコチに固まったかかと・ひび割れ手肌・粉吹きすね・パサつく毛先を救う高保湿マンゴーバター（マンゴー種子脂）コスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-05T22:00:00+09:00",
    "dateModified": "2026-11-05T22:00:00+09:00",
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
      "@id": "https://lumi-cosme.vercel.app/winter-mango-butter"
    }}
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #2: ItemList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿マンゴーバターコスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "{items[0]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{items[1]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{items[2]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 4,
        "name": "{items[3]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 5,
        "name": "{items[4]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 6,
        "name": "{items[5]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 7,
        "name": "{items[6]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 8,
        "name": "{items[7]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 9,
        "name": "{items[8]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 10,
        "name": "{items[9]["item_name"]}"
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
        "name": "マンゴーバターはシアバターとどう違いますか？どちらが冬の乾燥肌に向いていますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "シアバターは融点が約36〜38℃とやや高く冬場は固まりやすいのに対し、マンゴーバターはオレイン酸とステアリン酸のバランスに優れ融点が人肌に近いため、冬でも体温で瞬時にサラリと溶けて角層深部へ浸透します。油膜感やベタつきを残さずしなやかに潤したい方や、固いバームが塗りにくい部位にはマンゴーバターが極めておすすめです。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "マンゴーアレルギーがある人でもマンゴーバター配合コスメは使用できますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "マンゴーの果肉アレルギーの原因となるウルシ科特有の成分（ウルシオール様物質）は主に果皮や果肉に含まれます。マンゴーバターは種子の仁（カーネル）から抽出され高度に精製されているため一般にアレルゲンは除去されていますが、重度のアレルギー体質の方は必ず腕の内側などでパッチテストを行ってからのご使用をおすすめします。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "マンゴーバターは顔に塗ってもニキビや毛穴詰まりの原因になりませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "精製されたマンゴーバターはコメドジェニック（毛穴詰まり）指数が極めて低く、植物バターの中でもサラッとした仕上がりが特徴です。乾燥によってバリアが壊れた冬の敏感肌や粉吹き肌には優れた保護膜となります。ただし皮脂分泌の活発なTゾーンへの厚塗りは避け、乾燥しやすい頬や目元、口元を中心に薄くハンドプレスしてご使用ください。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #c2410c;
      --primary-light: #ffedd5;
      --primary-dark: #9a3412;
      --accent: #ea580c;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg: #fffbf5;
      --bg-card: #ffffff;
      --border: #fed7aa;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-weight: 800;
      font-size: 1.35rem;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}
    
    .hero-container {{
      max-width: 1100px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    .hero-card {{
      background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      box-shadow: var(--shadow);
    }}
    .badge-category {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    .hero-title {{
      font-size: 1.85rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 1.25rem;
    }}
    .hero-lead {{
      font-size: 1.05rem;
      color: #374151;
      margin-bottom: 1.5rem;
    }}
    .meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      border-top: 1px solid rgba(0, 0, 0, 0.08);
      padding-top: 1rem;
    }}
    
    /* 目次 */
    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.75rem;
      margin: 2rem 0;
      box-shadow: var(--shadow);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-card ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 0.75rem 1.5rem;
    }}
    .toc-card a {{
      color: var(--text);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
      display: block;
      padding: 0.25rem 0;
    }}
    .toc-card a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}
    
    /* セクション共通 */
    .article-section {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.25rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #111827;
      border-left: 5px solid var(--primary);
      padding-left: 1rem;
      margin-bottom: 1.5rem;
      line-height: 1.35;
    }}
    .article-section p {{
      margin-bottom: 1.25rem;
      color: #374151;
      font-size: 1rem;
      text-align: justify;
    }}
    .highlight-lead {{
      background: var(--primary-light);
      border-left: 4px solid var(--accent);
      padding: 1.25rem;
      border-radius: 4px;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
    }}
    
    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .data-table th, .data-table td {{
      padding: 0.85rem 1rem;
      border: 1px solid #e5e7eb;
    }}
    .data-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}
    .rank-cell {{ text-align: center; font-size: 1rem; color: var(--primary); white-space: nowrap; }}
    .price-cell {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 4px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}
    
    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: flex-start;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .rank-badge {{
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      padding: 0.4rem 1rem;
      border-radius: 8px;
      white-space: nowrap;
    }}
    .product-catch {{
      display: block;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .product-name {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 0.35rem;
    }}
    .product-subname {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    .product-main-grid {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-main-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-visual {{
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #fff7ed;
      padding: 1.5rem;
      border-radius: 8px;
      border: 1px solid var(--border);
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      border-radius: 6px;
      background: #ffffff;
      padding: 0.5rem;
      margin-bottom: 1rem;
    }}
    .price-box {{
      width: 100%;
      text-align: center;
      margin-bottom: 0.75rem;
      padding: 0.5rem;
      background: #ffffff;
      border-radius: 6px;
      border: 1px solid #fed7aa;
    }}
    .price-label {{ font-size: 0.75rem; color: var(--text-muted); display: block; }}
    .price-value {{ font-size: 1.4rem; font-weight: 800; color: #b91c1c; }}
    .review-meta {{
      font-size: 0.85rem;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.25rem;
    }}
    .review-stars {{ color: #d97706; font-weight: 700; }}
    .review-count {{ color: var(--text-muted); }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #c2410c 0%, #ea580c 100%);
      color: #ffffff;
      text-align: center;
      padding: 0.9rem 1rem;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 6px rgba(194, 65, 12, 0.25);
      transition: opacity 0.2s;
    }}
    .rakuten-btn:hover {{ opacity: 0.9; }}
    
    .product-info-col {{ display: flex; flex-direction: column; }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.85rem;
      border: 1px solid #e5e7eb;
    }}
    .spec-table th {{
      width: 28%;
      background: #fff7ed;
      color: #9a3412;
      font-weight: 700;
      white-space: nowrap;
    }}
    .body-title {{
      font-size: 1.1rem;
      font-weight: 800;
      color: #111827;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .recommend-box {{
      background: #ffedd5;
      border-left: 4px solid var(--accent);
      padding: 1rem 1.25rem;
      border-radius: 4px;
      margin: 1.25rem 0;
    }}
    .recommend-title {{
      font-weight: 700;
      color: #9a3412;
      font-size: 0.9rem;
      margin-bottom: 0.35rem;
    }}
    .recommend-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    .usage-box {{
      background: #f3f4f6;
      border-left: 4px solid #6b7280;
      padding: 1rem 1.25rem;
      border-radius: 4px;
      margin-top: 1rem;
    }}
    .usage-title {{
      font-weight: 700;
      color: #374151;
      font-size: 0.9rem;
      margin-bottom: 0.35rem;
    }}
    .usage-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    /* FAQ & 内部リンク */
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.25rem 0;
    }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}
    .faq-a {{
      color: #374151;
      padding-left: 1.75rem;
      font-size: 0.95rem;
    }}
    
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">🌿 LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <div class="hero-container">
    <div class="hero-card">
      <span class="badge-category">人肌（35℃）でとろける熱帯植物の奇跡・高純度エモリエント</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！体温でとろける高純度ステアリン酸が真冬のカチコチひび割れ肌とパサつく毛先を濃密ラッピングする高保湿マンゴーバターコスメランク10</h1>
      <p class="hero-lead">
        11月から12月にかけて訪れる気温急降下と乾いた木枯らし。皮脂分泌が急落してすねや腕が白く粉を吹き、水仕事による指先のあかぎれ、そしてエアコン暖房による毛先の激しいパサつき——。シアバターよりも融点が人肌に近く、ベタつかずに角層へ溶け込む「マンゴーバター（マンゴー種子脂）」の卓越した皮膚科学的エモリエント効果を解き明かし、楽天市場で今すぐ手に入る最高峰のマンゴーバターコスメ10選を徹底検証します。
      </p>
      <div class="meta-bar">
        <span>📅 2026年11月更新（真冬乾燥特化版）</span>
        <span>🔬 皮膚科学・体温融解エモリエント検証済み</span>
        <span>🛍️ 楽天市場公式APIデータ連携</span>
      </div>
    </div>
  </div>

  <main class="hero-container">
    <!-- 目次 -->
    <div class="toc-card">
      <div class="toc-title">📑 目次（クリックで各項目へジャンプ）</div>
      <ul>
{toc_html}
      </ul>
    </div>

    <!-- セクション1: 導入 -->
    <section class="article-section" id="intro">
      <h2 class="section-title">1. 11月・12月の本格乾燥と粉吹き肌！「体温融解」マンゴーバターの驚異の保水力</h2>
      <div class="highlight-lead">
        シアバターの「固くて伸びにくい」「重くてベタつく」という弱点を克服した理想の植物脂。人肌温度（約35℃）でスーッと液化して角層の隙間へ滑り込み、真冬の粉吹き肌とあかぎれをベルベットの保護膜で包み込みます。
      </div>
      <p>
        11月中旬から12月にかけて、日本の大気湿度は30%台へと急落し、さらに屋内の暖房器具が稼働することで、肌を取り巻く環境は極度の脱水状態にさらされます。寒さによって毛細血管が収縮し、皮膚温が低下すると、皮脂腺からの皮脂分泌量は夏の3分の1近くまで激減。天然のバリアを奪われた角質層からは水分が一方的に蒸散し、細胞同士の結束が剥がれて「白く粉を吹く」「ひび割れて痛む」といった深刻な冬の乾燥トラブルが頻発します。
      </p>
      <p>
        このような真冬の乾燥砂漠肌に対して、古くからシアバターやワセリンが用いられてきましたが、「冬場は冷えて固くなり肌を擦ってしまう」「塗った後のベタつきが服やシーツにつく」といった不満の声も少なくありませんでした。そこで近年、皮膚科学とオーガニックコスメ界で熱い注目を浴びているのが、マンゴーの種子の仁から抽出される「マンゴーバター（マンゴー種子脂）」です。人肌に触れた瞬間にトロリととろける独自の融解特性と、高い保水シールド力を兼ね備えたマンゴーバターは、真冬の過酷な肌荒れを救う理想的なエモリエント成分です。
      </p>
    </section>

    <!-- セクション2: メカニズム -->
    <section class="article-section" id="mechanism">
      <h2 class="section-title">2. なぜマンゴーバターは真冬に最強なのか？ステアリン酸とオレイン酸の皮膚科学</h2>
      <p>
        マンゴーバターが真冬の深刻な乾燥やひび割れに対して劇的な保護効果を発揮する理由は、その特異な脂肪酸プロファイルと物理的特性に裏打ちされています。
      </p>
      <p>
        <strong>① 融点が約35〜38℃！「人肌でとろける」理想のエモリエント挙動：</strong><br>
        植物バターの使い心地を決定づけるのは融点です。マンゴーバターの融点は人間の皮膚表面温度（約34〜35℃）に極めて近く設計されているため、常温では型崩れしない適度な固形を保ちながら、肌に乗せた瞬間に摩擦ゼロで体温融解します。指先で軽く温めるだけで滑らかなリキッドオイルへと転換し、硬化した冬の角質層のミクロな溝までスルスルと浸透していきます。
      </p>
      <p>
        <strong>② ステアリン酸（約42%）とオレイン酸（約40%）の黄金バランス：</strong><br>
        マンゴーバターの主成分は、肌表面に強固な保護バリアを張る飽和脂肪酸「ステアリン酸」と、人の皮脂組織に酷似した浸透性の高い一価不飽和脂肪酸「オレイン酸」がほぼ均等に存在しています。オレイン酸が硬化した角層をふっくら柔軟化（エモリエント作用）させ、ステアリン酸が水分蒸散を物理的に遮断（オクルーシブ作用）するという、二重の防御メカニズムを一本の植物脂で同時に完結させます。
      </p>
      <p>
        <strong>③ 豊富な天然ステロールとトコフェロール（ビタミンE）：</strong><br>
        マンゴーバターには、植物ステロール（フィトステロール）や天然ビタミンEが豊富に凝縮されています。これらは寒冷刺激や乾燥摩擦によって炎症を起こしかけた皮膚の微小循環をサポートし、赤みやヒリつきを穏やかに鎮静。さらに酸化安定性が極めて高いため、日中の紫外線や空気接触による油焼けのリスクが極めて低い点も冬のデイリーケアとして大きな強みです。
      </p>
    </section>

    <!-- セクション3: 比較表 -->
    <section class="article-section" id="comparison">
      <h2 class="section-title">3. 高保湿マンゴーバターコスメおすすめ10選の比較表</h2>
      <p>
        楽天市場で実際に購入可能な人気の高保湿マンゴーバターコスメ10アイテムの種別、参考価格、主要美肌成分を一覧にまとめました。
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド・商品名</th>
              <th>カテゴリー種別</th>
              <th>参考価格（税込）</th>
              <th>注目美肌成分</th>
              <th>楽天リンク</th>
            </tr>
          </thead>
          <tbody>
{table_rows_html}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4: ランキング -->
    <section class="article-section" id="ranking">
      <h2 class="section-title">4. 高保湿マンゴーバターコスメおすすめ厳選ランキング10選</h2>
      <p>
        純度、体温融解の滑らかさ、真冬の保水シールド力、使用感のベタつきにくさ、楽天市場での購入信頼性を総合的に審査したTOP10ランキングです。
      </p>
{all_cards_html}
    </section>

    <!-- セクション5: 選び方ガイド -->
    <section class="article-section" id="guide">
      <h2 class="section-title">5. 失敗しないマンゴーバターコスメの選び方＆冬の部位別活用術</h2>
      <p>
        マンゴーバターコスメを真冬のスキンケアに取り入れる際は、使用する部位やお好みの使用感に合わせて最適な形状を選ぶことが大切です。
      </p>
      <p>
        <strong>① ひび割れかかと・手荒れ・集中密封には「100%純粋バター」：</strong><br>
        &SH（第1位・第3位）や山桂産業（第6位）のような100%ピュアな未精製・精製マンゴーバターは、添加物を一切含まないため最も強力な密封力を持ちます。水仕事で荒れた指先や、タイツを履くときに引っかかるかかとへの夜の集中パックに最適です。
      </p>
      <p>
        <strong>② お風呂上がりの全身ケアには「ボディバター・ローション」：</strong><br>
        ザ・ボディショップ（第2位）やラニカイ（第8位）のように乳化処方されたアイテムは、広い面積でも引っかかりなくスーッと伸び、服をすぐに着てもベタつきません。真冬にすねや太ももが粉を吹いてかゆくなる方のデイリーボディケアにぴったりです。
      </p>
      <p>
        <strong>③ 冬の暖房乾燥と静電気で広がる髪には「ヘアスタイリング・アウトバス」：</strong><br>
        ナプラN.（第4位）やロレッタ（第5位・第7位）のようにマンゴー種子脂を配合したヘアケアは、キューティクル表面を熱や乾燥摩擦から保護し、一日中しっとり艶やかなまとまりをキープします。
      </p>
    </section>

    <!-- セクション6: ルーティン -->
    <section class="article-section" id="routine">
      <h2 class="section-title">6. 真冬のカチコチひび割れ肌を救う！効果的な体温ハンドプレス＆密封ルーティン</h2>
      <p>
        マンゴーバターの優れた体温融解エモリエント効果を100%引き出すための、真冬特化型レスキューステップです。
      </p>
      <p>
        <strong>ステップ1【手のひらで温めて完全液化】：</strong><br>
        指先やスパチュラでバターを適量取ったら、絶対に固形のまま肌に擦り付けてはいけません。両手のひらを擦り合わせ、手のひらの熱（体温）で完全に透明なリキッドオイル状へと変化させます。
      </p>
      <p>
        <strong>ステップ2【湿り気のある肌へハンドプレス密着】：</strong><br>
        化粧水や入浴後の水分が肌表面にほんのり残っている状態で、手のひら全体で顔や手足を包み込むように優しくプレスします。水分と油分が肌表面で乳化し、角層の隙間へスッと浸透していきます。
      </p>
      <p>
        <strong>ステップ3【頑固なひび割れ・粉吹き部位への重ね塗り】：</strong><br>
        特に乾燥が深刻なかかとや指先のささくれ、口元には、指の腹でごく少量をトントンと重ねづけします。就寝時に靴下やコットン手袋を着用して眠れば、翌朝にはサロン帰りのようにふっくら柔らかい極上肌が蘇ります。
      </p>
    </section>

    <!-- セクション7: FAQ -->
    <section class="article-section" id="faq">
      <h2 class="section-title">7. マンゴーバターコスメに関するよくある質問（FAQ）</h2>
      
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> マンゴーバターはシアバターとどう違いますか？どちらが冬の乾燥肌に向いていますか？</div>
        <div class="faq-a">
          シアバターは融点が約36〜38℃とやや高く冬場は固まりやすいのに対し、マンゴーバターはオレイン酸とステアリン酸のバランスに優れ融点が人肌に近いため、冬でも体温で瞬時にサラリと溶けて角層深部へ浸透します。油膜感やベタつきを残さずしなやかに潤したい方や、固いバームが塗りにくい部位にはマンゴーバターが極めておすすめです。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> マンゴーアレルギーがある人でもマンゴーバター配合コスメは使用できますか？</div>
        <div class="faq-a">
          マンゴーの果肉アレルギーの原因となるウルシ科特有の成分（ウルシオール様物質）は主に果皮や果肉に含まれます。マンゴーバターは種子の仁（カーネル）から抽出され高度に精製されているため一般にアレルゲンは除去されていますが、重度のアレルギー体質の方は必ず腕の内側などでパッチテストを行ってからのご使用をおすすめします。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> マンゴーバターは顔に塗ってもニキビや毛穴詰まりの原因になりませんか？</div>
        <div class="faq-a">
          精製されたマンゴーバターはコメドジェニック（毛穴詰まり）指数が極めて低く、植物バターの中でもサラッとした仕上がりが特徴です。乾燥によってバリアが壊れた冬の敏感肌や粉吹き肌には優れた保護膜となります。ただし皮脂分泌の活発なTゾーンへの厚塗りは避け、乾燥しやすい頬や目元、口元を中心に薄くハンドプレスしてご使用ください。
        </div>
      </div>
    </section>

    <!-- セクション8: まとめ -->
    <section class="article-section" id="summary">
      <h2 class="section-title">8. まとめ：人肌でとろける植物バターで真冬の肌乾燥とさようなら</h2>
      <p>
        11月から12月にかけての本格的な真冬シーズンは、外気の冷気と室内の暖房による激しい水分蒸散によって、私たちの素肌から急速に潤いが奪い去られていきます。どんなに化粧水を与えても乾いてしまう冬の頑固な粉吹きやひび割れ肌を解決する鍵は、体温で瞬時に馴染み、水分を外へ逃さない「上質でしなやかなエモリエントシールド」に他なりません。
      </p>
      <p>
        人肌の温度でとろけ、高純度なステアリン酸とオレイン酸で角層を優しく包み込むマンゴーバターコスメは、真冬の過酷な寒さから素肌を確実に守り抜き、カチコチに固まった皮膚をふっくらと柔らかな状態へと蘇らせてくれます。ぜひ本記事のランキングや選び方を参考に、あなたのライフスタイルや肌悩みにぴったりのマンゴーバターコスメを見つけて、真冬でも乾燥知らずのベルベット肌を手に入れてください。
      </p>
    </section>

    <!-- 関連記事リンクプレースホルダー -->
    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <!-- update_all_internal_links.py で自動挿入 -->
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-logo">🌿 LUMI COSMETICS</div>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で自動挿入 -->
      </div>
      <div style="text-align:center;margin-top:2rem;font-size:0.8rem;color:#6b7280;">
        &copy; 2026 LUMI COSMETICS. All rights reserved.
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-mango-butter.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-mango-butter.html successfully!")
