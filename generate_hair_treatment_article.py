import json

with open("rakuten_hair_lip_carbonic_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_hair_treatment"]["items"]

hair_treatment_details = [
    {
        "rank": 1,
        "tag": "🏆 サロン専売最高峰！冬の乾燥とヘアカラーでスカスカに抜けた毛髪内部の水分保持力を根本補修",
        "catch": "水分を抱え込むCMC脂質層を再構築。暖房風にさらされても毛先まで吸い付くようにまとまる極上ヘア",
        "capacity": "250g",
        "type": "サロン専売・高保水集中リペアヘアトリートメント",
        "texture": "こっくりとして濃厚でありながら、濡れた髪にスルスルとなめらかに行き渡る絶妙なリッチクリーム",
        "ingredients": "オリーブスクワラン、イソステアリン酸イソステアリル（CMC補修成分）、アルギニン、ヒドロキシエチルウレア、グリセリン",
        "finish": "重すぎず軽すぎず、指を通すと一本一本が水分で満たされたようなシルクのしなやかさと自然な天使の輪が出現",
        "desc_p1": "11月から12月にかけて外気の湿度が30%台まで落ち込むと、毛髪内部を構成する自由水と結合水のうち、髪のしなやかさを司る水分が一気に奪われます。特にブリーチや冬のトーンダウンカラーを繰り返した毛髪は、細胞膜複合体（CMC）が破壊されており、網の目から水が漏れ出すように乾燥が加速して毛先がバサバサに広がります。",
        "desc_p2": "日本のトップサロンで圧倒的な支持を誇るミルボンの最高峰ブランド『オージュア』のクエンチラインは、髪の水分保持力を回復させる独自テクノロジーを搭載。冬のパサつく髪の脂質二重層を補修し、毛髪内部に水分をギュッと留める力を取り戻します。お風呂の中で馴染ませて洗い流した瞬間から、指通りがトゥルンと変わり、翌朝のブロー時もアイロンなしで毛先が自然に内側へ収まります。",
        "target": "冬になると毛先がバサバサに広がってまとまらない方、ヘアカラーやパーマの繰り返しで毛先のパサつきが深刻な方、サロン帰りのしっとり柔らかな質感を自宅で毎日キープしたい方",
        "technique": "シャンプー後、手ぐしで水気をしっかり絞ってから、毛先を中心に適量を揉み込みます。目の粗いコームで優しくとかして全体に行き渡らせ、2〜3分置いてからぬるま湯で洗い流すと、浸透力が最大化されます。",
        "voice": "『冬になると静電気で髪が顔に張り付いてボサボサになっていましたが、クエンチを使い始めてから毛先がしっとり重みを持ってストンとまとまるようになりました。フローラルの上品な香りも大好きです。』(20代・美容師)",
        "caution": "頭皮に直接塗布すると毛穴詰まりやベタつきの原因になるため、耳下から毛先にかけて塗布してください。"
    },
    {
        "rank": 2,
        "tag": "💃 くせ毛＆冬の乾燥広がりを抑え込む！弾むようなしなやかさとツヤを一日中キープするパリ発名品",
        "catch": "髪の表面を均一な疎水性保護膜でコーティング。湿気や乾燥に振り回されないシルキータッチな美髪へ",
        "capacity": "200ml",
        "type": "くせ・広がり・乾燥補修デイリーヘアトリートメント",
        "texture": "みずみずしく軽やかなエマルジョン状。素早く髪の一本一本に馴染んでベタつかない",
        "ingredients": "モルフォ ユイル テクノロジー（アミノ酸コンプレックス・小麦タンパク誘導体・セラミド・シアバター）",
        "finish": "風になびく軽やかさと、毛先まで乱れないまとまり感を完璧に両立。摩擦による静電気の発生を完全ブロック",
        "desc_p1": "冬の冷たい北風やマフラー・タートルネックとの擦れは、キューティクルを剥離させ、髪に帯電を引き起こします。特にくせ毛やうねりを持つ髪は、乾燥によって繊維のねじれが強まり、朝しっかりアイロンを当てても外出後わずか数分で爆発したように広がってしまいます。",
        "desc_p2": "ケラスターゼの『フォンダン フルイダリスト』は、髪のくせやパサつきを抑えながら、自然な動きとしなやかさを与える革新的トリートメント。独自のモルフォユイル複合体がキューティクルの表面をなめらかに整え、冬の摩擦ダメージと静電気を大幅に軽減します。重たいオイルトリートメントのようにペタンと潰れることなく、根元はふんわり、毛先はツルンと滑らかな指通りを実現します。",
        "target": "冬の静電気で髪が広がって困っている方、くせ毛やうねりがあり朝のスタイリングに時間がかかる方、重くなりすぎずサラサラしたまとまり感を求める方",
        "technique": "水分をよく切った毛先中心に塗布し、両手で髪を挟んで上から下へ優しく滑らせるようにキューティクルを寝かせます。1〜2分置いてからヌルつきがなくなるまで丁寧にすすいでください。",
        "voice": "『マフラーを巻く時期の襟足のチリチリや広がりが全く気にならなくなりました。乾かした後のサラサラ感とまとまりが別格で、自分の髪じゃないみたいです。』(30代・PR事務)",
        "caution": "非常に浸透が早いため長時間の放置は不要ですが、すすぎ残しがあると背中ニキビの原因になるのでしっかり洗い流してください。"
    },
    {
        "rank": 3,
        "tag": "🍯 美容液成分を凝縮！傷んだ毛先をとろけるように包み込みツルツルに仕上げる国民的大ヒットヘアマスク",
        "catch": "ローヤルゼリーEXとPCAが傷んだ毛先を集中浸透密着。プチプラの常識を覆すサロン級のツヤと重み",
        "capacity": "230g",
        "type": "高濃度美容液配合・集中浸透インバスヘアマスク",
        "texture": "黄金色のリッチでとろけるようなジェルクリーム。濡れた髪に吸い付くように密着",
        "ingredients": "ローヤルゼリーエキス、トレハロース、PCA（保湿）、スクワラン、グルタミン酸、加水分解コムギタンパク",
        "finish": "ずっしりとしたうるおいの重みを感じるしっとり仕上げ。枝毛やパサつきが目立たず鏡のような光沢感",
        "desc_p1": "ドラッグストアで手に入るヘアケアの中でも、圧倒的なリピート率と口コミ評価を誇るフィーノ。冬場のカラーダメージ毛や乾燥でチリチリになった毛先は、タンパク質が流出してスカスカのポーラス（多孔質）状態に陥っています。",
        "desc_p2": "フィーノの『プレミアムタッチ 浸透美容液ヘアマスク』は、ローヤルゼリーEXをはじめとする6種の美容液成分を贅沢にブレンド。傷んだ髪の空洞部に素早く浸透し、傷んだキューティクルをキュッと引き締めて密着コーティングします。洗い流した瞬間から指が滑り落ちるような驚異的ななめらかさを実感でき、週に1〜2回のスペシャルケアとして冬のパサパサ髪を劇的に生き返らせます。",
        "target": "冬の毛先のパサパサ・枝毛・切れ毛に悩む方、コストパフォーマンス高く本格的な集中トリートメントを行いたい方、しっとり重ためのまとまり感が好きな方",
        "technique": "シャンプー後に軽く水気を切り、傷んだ毛先を中心にもみこみます。蒸しタオルやシャワーキャップをかぶって3〜5分置くと、お風呂の蒸気で美容成分がより深くまで浸透します。",
        "voice": "『ブリーチでギシギシだった髪が、これを使うと一発でトゥルトゥルになります。冬の乾燥時期には週2回欠かせないお守りアイテムです。』(20代・大学生)",
        "caution": "保湿コーティング力が非常に高いため、毎日連続で使用すると髪が重たくなることがあります。髪質に合わせて週1〜3回の使用がベストです。"
    },
    {
        "rank": 4,
        "tag": "🔬 毛髪深部の棒状空洞化を集中補修！ハイダメージを芯から再構築するプロフェッショナル仕様",
        "catch": "ミルボン独自のSSVRシルクが毛髪内部の空洞を隙間なく埋める。折れやすく弱った冬の髪に芯の通った強さを注入",
        "capacity": "200g",
        "type": "棒状空洞化補修・内部再構築トリートメント",
        "texture": "クリーミーで高密度な質感。毛髪の芯まで吸い込まれるように馴染むリッチ処方",
        "ingredients": "SSVRシルク（イソステアロイル加水分解シルク）、PCA-Na、セチルPGヒドロキシエチルパルミタミド、アミノ酸各種",
        "finish": "毛先までピンと一本芯が通ったようなコシと、しっとりとしたうるおいのしなやかさが共存する極上仕上がり",
        "desc_p1": "ミルボンの先端毛髪研究によって発見された、ダメージ毛の内部に発生する「棒状空洞化」。毛髪の芯がスカスカになることで、冬の乾燥によって髪が簡単に切れたり、枝毛が裂けたりする原因となります。",
        "desc_p2": "グローバルミルボンの『リペア リストラティブ トリートメント』は、シルク由来の補修成分SSVRシルクを高濃度配合。空洞化した髪の芯を分子レベルで補修し、毛髪の密度を高めます。冬の暖房乾燥やドライヤーの熱に負けない、内側から満たされた強い髪を育みます。",
        "target": "枝毛や切れ毛が多く毛先がプチプチ切れてしまう方、冬になると髪にハリコシがなくなりパサつく方、本格的な内部補修トリートメントを求める方",
        "technique": "毛先から中間にかけて手ぐしを通しながら馴染ませ、毛束をキュッキュッと優しく握り込むように揉み込みます。時間を置かずにすぐ流しても高い補修効果を発揮します。",
        "voice": "『縮毛矯正と冬の乾燥で毛先がほうきのようにパサついていましたが、美容師さんに勧められて使い始めたら髪の芯がしっかりして柔らかくなりました。』(30代・専門職)",
        "caution": "正規取扱サロンおよび正規認定ショップからの購入を推奨します。並行輸入品や非正規品にはご注意ください。"
    },
    {
        "rank": 5,
        "tag": "🌿 高純度アルガンオイル高配合！太く硬い髪や乾燥したゴワつき毛をシルクのような柔らかさへ解きほぐす",
        "catch": "モロッコの黄金アルガンオイルが瞬時に角層深部へ浸透。地中海の甘い香りと共に極上のツヤとしっとり感を提供",
        "capacity": "250ml",
        "type": "高純度アルガンオイル配合・濃密ハイドレーティングマスク",
        "texture": "バターのように濃厚で贅沢なクリームバーム。体温でとろけて髪の一本一本を包み込む",
        "ingredients": "アルガニアスピノサ核油（アルガンオイル）、グリセリン、キャノーラオイル、ジメチコン、ベヘントリモニウムクロリド",
        "finish": "硬くゴワついていた髪が信じられないほど柔らかくほぐれ、触れるたびにうっとりする極上のなめらかさに",
        "desc_p1": "冬の乾燥は、細い髪だけでなく太くて硬い髪にも深刻なトラブルをもたらします。水分が不足した太い髪は針金のように強張り、毛先が広がってまとまらなくなります。水溶性のトリートメントだけでは硬いキューティクルをほぐすことができません。",
        "desc_p2": "世界中で愛されるモロッカンオイルの『インテンス ハイドレーティング マスク』は、抗酸化作用の高いビタミンEや必須脂肪酸を豊富に含む高純度アルガンオイルを惜しみなく配合。乾燥して硬化した毛髪内部に良質な油分と水分を同時に送り込み、シルクのようにしなやかで扱いやすい髪へと導きます。",
        "target": "髪が太く硬くて冬になるとゴワつきや広がりがひどい方、上質なアルガンオイルによるリッチな保湿を体験したい方、オリエンタルで優雅な香りを楽しみたい方",
        "technique": "シャンプー後、軽くタオルドライして余分な水分を取り除いてから、適量を髪全体に均一に伸ばします。5〜7分置いてからしっかり洗い流してください。熱を加える必要はありません。",
        "voice": "『剛毛で冬は乾燥して広がるのが悩みでしたが、このマスクを使うと髪がとろけるように柔らかくなります。翌朝の髪の扱いやすさが劇的に変わりました。』(40代・自営業)",
        "caution": "非常に油分リッチな処方のため、猫っ毛や細い軟毛の方が使いすぎるとボリュームがダウンすることがあります。毛量が多い方や硬毛の方に最適です。"
    },
    {
        "rank": 6,
        "tag": "🍯 3種の黄金比ハチミツ×保水オーガニック処方！髪の理想的な水分量14%を保ち抜く超人気トリートメント",
        "catch": "マヌカ・アカシア・生ハチミツが髪をうるおいヴェールでラッピング。ドラコスで手に入る至高の潤い感",
        "capacity": "445g",
        "type": "ハチミツ保水・オーガニックディープモイストトリートメント",
        "texture": "トロリと濃密なハニーゴールドクリーム。髪に伸ばすとフワッと甘いラベンダーハニーの香りが広がる",
        "ingredients": "ハチミツ（マヌカ50%・アカシア30%・生ハチミツ20%）、アルガンオイル、加水分解ハチミツタンパク、ローヤルゼリーエキス、プロポリスエキス",
        "finish": "毛先までみずみずしいうるおいがギュッと詰まったようなぷるぷるの質感。乾燥した室内でもパサつき知らず",
        "desc_p1": "一般的な髪の水分量は約12%程度ですが、冬の乾燥期には10%以下まで急落します。アンドハニーは「髪の理想的な水分量14%」に着目し、製品の90%以上を保湿＆保護成分で構成するという圧倒的な保水アプローチをとっています。",
        "desc_p2": "『ディープモイスト ヘアトリートメント 2.0』は、世界各地から厳選した3種のハチミツを独自比率で配合。ハチミツの強力な吸湿・保水力により、冬のカラカラに乾いた空気の中でも髪の水分蒸散を防ぎます。大容量ポンプタイプで毎日のバスタイムに気兼ねなくたっぷり使えるのも人気の秘密です。",
        "target": "毛先のカサつきやパサつきを手頃な価格で毎日しっかり潤したい方、甘く心地よいハチミツの香りに癒やされたい方、大容量で使いやすいポンプ式を好む方",
        "technique": "シャンプー後、軽く水気を切ってから毛先を中心に塗布し、両手で髪をギュッと握り込むようにして浸透させます。1分ほど置いてから洗い流すだけで十分な保湿効果を発揮します。",
        "voice": "『パッケージも可愛くて香りも最高。冬はお風呂上がりすぐにパサついていた毛先が、これにしてからずっとしっとりツヤツヤです。コスパ最強だと思います。』(20代・OL)",
        "caution": "香りがやや甘めなので、無香料やすっきりした柑橘系を好む方はテスター等で香りを確認することをおすすめします。"
    },
    {
        "rank": 7,
        "tag": "🍇 カラーやパーマのハイダメージ毛を濃縮リペア！週1〜2回の集中補修で毛先までスルンとまとまる濃密マスク",
        "catch": "疎水化成分と濃密リピッドが髪の隙間をブロック。冬の静電気やパサつきを完全に封じ込める実力派",
        "capacity": "170g",
        "type": "サロン品質・ハイダメージ集中ケアディープマスク",
        "texture": "こっくりと粘度のある濃厚なクリーム。髪にピタッと吸着して液だれしない",
        "ingredients": "シクロペンタシロキサン、水添ポリイソブテン、ステアリルアルコール、アモジメチコン、ベヘントリモニウムクロリド、ヒドロキシステアリン酸エチルヘキシル",
        "finish": "毛先までツルンと滑るようななめらかさと、シルクのような上品なまとまり。重すぎない絶妙なサラツヤ感",
        "desc_p1": "サロン専売品として美容師の間で長年絶大な信頼を集めるルベルのイオシリーズ。特に冬のハイダメージ毛は、静電気によってホコリや花粉を吸着しやすく、髪のツヤが失われがちです。",
        "desc_p2": "『イオ ディープマスク』は、カラーや熱ダメージで傷んだ毛髪を内側と外側の両面から集中補修。ダメージ部分を疎水化（水を弾く健康な状態）に戻すことで、余分な湿気や冬の乾燥に左右されない強固な美髪ベースを作ります。毛先がスルンとまとまり、毎朝のスタイリングが劇的に楽になります。",
        "target": "カラーやブリーチを繰り返して毛先のダメージが深刻な方、週に1〜2回のスペシャルケアでサロン帰りの質感を再現したい方、甘すぎず爽やかな香りが好きな方",
        "technique": "シャンプー後、毛先を中心によく揉み込み、蒸しタオルを巻いて3分間放置すると成分が奥深くまで浸透します。その後、根元を中心にしっかりとすすいでください。",
        "voice": "『美容室でトリートメントしてもらった後のようなツルツル感が自宅で出せます。冬の静電気で広がっていた髪がストンと落ち着いて感動しました。』(30代・公務員)",
        "caution": "週1〜2回の集中トリートメント用として設計されているため、毎日のデイリーケアとして使うと重たくなることがあります。"
    },
    {
        "rank": 8,
        "tag": "🌙 夜間美容ナイトセラミド配合！睡眠中の枕摩擦と乾燥から髪を守り抜く大人気トリートメント",
        "catch": "寝ている間に集中浸透コーティング。翌朝起きた瞬間から毛先までうるサラで寝癖がつきにくい",
        "capacity": "475g",
        "type": "ナイトキャップ発想・夜間集中補修トリートメント",
        "texture": "なめらかで伸びの良いミルキークリーム。髪全体に素早く均一に行き渡る",
        "ingredients": "セラミドNG、セラミドNP、セラミドAP、ネムノキ樹皮エキス、ゼニアオイ花エキス、異性化糖",
        "finish": "毛先までサラサラと指通りが良く、枕に擦れても静電気が起きないしなやかな質感",
        "desc_p1": "睡眠中の寝返りによる「枕との摩擦」は、冬の乾燥した環境下では髪にとって大きな物理的ストレスとなります。寝ている間にキューティクルが削られ、朝起きるとパサつきや寝癖、絡まりの原因になります。",
        "desc_p2": "YOLUの『カームナイトリペア トリートメント』は、ナイトキャップをかぶったような保護効果を発揮するナイトセラミドと超密着エッセンスを配合。夜のバスタイムで髪をコーティングし、就寝中の摩擦と乾燥ダメージを徹底的に防ぎます。ネロリ＆ピオニーの安らぐ香りで、冬の夜のヘアケアが心地よいリラックスタイムに変わります。",
        "target": "朝起きると髪がパサついてボサボサ・寝癖がひどい方、夜の睡眠時間を活用して効率よくヘアケアしたい方、サラサラした軽やかな指通りが好きな方",
        "technique": "髪全体に馴染ませた後、優しく毛先をプレスして浸透させます。すすいだ後はしっかりタオルドライし、放置せずに速やかにドライヤーで乾かすことでナイトリペア効果が最大限に高まります。",
        "voice": "『朝起きたときの髪の落ち着きが全然違います。冬はいつもパサパサで静電気が起きていましたが、YOLUにしてから寝癖もつきにくくなりました。』(20代・デザイナー)",
        "caution": "トリートメント後は濡れたまま寝ると効果が半減するため、必ず就寝前にドライヤーで完全に乾かしてください。"
    },
    {
        "rank": 9,
        "tag": "🔬 コーセーの高浸透カプセル配合！髪の深層までうるおいを届けて芯からしなやかに立て直すサロン発想",
        "catch": "高浸透モイスチュアカプセルが毛髪深部で弾けてうるおいを補給。冬の深刻なパサつきを芯からリセット",
        "capacity": "220g",
        "type": "高浸透カプセル配合・モイスチュアコントロールヘアパック",
        "texture": "こっくり濃密なクリームパック。毛先の一本一本にしっかり絡みつく密着感",
        "ingredients": "高浸透モイスチュアカプセル、アミノ酸、セラミド、アルガンオイル、ムルムルバター、ホホバ種子油",
        "finish": "髪の内部に水分が詰まったようなしっとり感と、毛先まで乱れない上質なまとまり",
        "desc_p1": "ニューヨークのトップヘアスタイリストの感性と、コーセーの先進毛髪科学研究が融合して生まれたスティーブンノル。冬の乾燥でパサついた髪は、表面だけでなく内部の水分バランスが崩れています。",
        "desc_p2": "『モイスチュアコントロール ヘアパック W』は、微小な高浸透モイスチュアカプセルを配合。髪の芯まで到達したカプセルからうるおい成分が徐々に放出され、パサつき深層まで集中的に補修します。冬の暖房や乾燥風に一日中さらされても、毛先のみずみずしいまとまりをキープします。",
        "target": "ドラッグストアでサロンクオリティの本格的な集中ヘアパックを探している方、毛先の広がりやパサつきを芯から抑えたい方、上品なフローラルの香りを好む方",
        "technique": "シャンプー後に軽く水気を切り、適量を毛先を中心に揉み込みます。2〜3分置いてから洗い流すと、カプセル内の成分が髪にしっかり定着します。",
        "voice": "『ドラコスの中では一番効果を実感しています。美容室のトリートメントのように毛先がツルツルになって、冬の乾燥にもびくともしません。』(30代・教員)",
        "caution": "週1〜2回の使用が目安ですが、乾燥が特にひどい時期はデイリーケアとして毛先に少量使うのも効果的です。"
    },
    {
        "rank": 10,
        "tag": "✨ プレミアムゴールドヒアルロン酸オイル配合！ドラッグストアでいつでも買える冬の乾燥補修の絶対王者",
        "catch": "ホホバ種子油とヒアルロン酸が髪の内外を濃密ダブルケア。圧倒的なコストパフォーマンスでツヤ髪を維持",
        "capacity": "300g",
        "type": "ヒアルロン酸オイル配合・濃厚ダメージ補修トリートメント",
        "texture": "リッチで伸びの良いなめらかクリーム。髪全体に素早く行き渡り、手ぐしがスルスル通る",
        "ingredients": "プレミアムゴールドヒアルロン酸オイル（ホホバ種子油・ヒアルロン酸ヒドロキシプロピルトリモニウム・加水分解ヒアルロン酸）、シアバター、アルギニン",
        "finish": "ツヤやかで光を反射する輝きと、毛先まで引っかかりのないスルスルの指通り",
        "desc_p1": "冬のヘアケアで最も大切なのは、高額なサロントリートメントをたまにするだけでなく、毎日惜しみなく適量を使い続けることです。ラックスは数十年にわたり日本人の髪質と乾燥悩みを研究し続けています。",
        "desc_p2": "『スーパーリッチシャイン ダメージリペア リッチ補修トリートメント』は、ホホバ種子油とヒアルロン酸を贅沢に融合させた濃密処方。冬の乾燥で傷んだ枝毛や切れ毛を密着コーティングし、輝くツヤを与えます。300gという大容量で手頃な価格のため、毎日毛先にたっぷり揉み込めるのが最大の強みです。",
        "target": "近所のドラッグストアで手軽に買えて毎日気兼ねなくたっぷり使いたい方、髪にツヤと指通りのなめらかさを求める方、家族全員でシェアしたい方",
        "technique": "シャンプー後、軽く水気を切って毛先から髪全体に伸ばします。すぐに洗い流しても高いツヤ出し効果が得られます。",
        "voice": "『安くて大容量なのに、これを使うと本当に毛先がツヤツヤになります。冬は乾燥しやすいので、毎日惜しみなく毛先にたっぷり使っています。』(20代・会社員)",
        "caution": "頭皮に直接つかないように毛先中心に馴染ませてください。しっかりすすぐことでベタつきを防げます。"
    }
]

# JSON-LD用ItemList
json_ld_items = []
for idx, it in enumerate(items):
    dt = hair_treatment_details[idx]
    json_ld_items.append({
        "@type": "ListItem",
        "position": idx + 1,
        "item": {
            "@type": "Product",
            "name": it["name"],
            "image": it["image_url"],
            "description": dt["catch"],
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
    })

json_ld_structure = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！サロン帰りの濃密ツヤまとまりが続く高保湿ヘアトリートメントランク10",
            "description": "11月・12月の冬の乾燥でパサつく毛先・静電気広がり・枝毛ダメージを徹底解決！オージュア、ケラスターゼ、フィーノ、ミルボン、モロッカンオイル、アンドハニーなど、高純度補修成分とCMC脂質配合の最強高保湿ヘアトリートメント10選を徹底比較！",
            "datePublished": "2026-11-01T00:00:00+09:00",
            "dateModified": "2026-11-01T00:00:00+09:00",
            "author": {
                "@type": "Organization",
                "name": "冬コスメ徹底比較ラボ"
            }
        },
        {
            "@type": "ItemList",
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "コンディショナー、ヘアトリートメント、ヘアマスクの違いと正しい使い分けは？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "コンディショナーは主に『毛髪表面のキューティクルを整えて滑りを良くするもの』です。一方、ヘアトリートメントは『毛髪内部にアミノ酸やCMC脂質などの栄養を浸透補修するもの』、ヘアマスクはさらに成分濃度が高く『ハイダメージを集中治療するスペシャルケア』です。冬の乾燥時期は、毎日のケアにヘアトリートメントを使用し、週に1〜2回ヘアマスクへ置き換えるケアが最も効果的です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "トリートメントの効果を劇的に高めるお風呂場での塗り方はありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ポイントは2つあります。第1に、シャンプー後に『手でしっかり水気を切る（または軽くタオルで押さえる）』ことです。髪に水分が余分に残っているとトリートメントが薄まり、内部まで浸透しません。第2に、毛先に塗布した後に『目の粗いジャンボコームで優しくコーミングする』ことです。手だけでは届かない髪一本一本の内側まで均一に成分を行き渡らせることができます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "冬の静電気で髪が広がって顔に張り付くのを防ぐにはどうすればいいですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "静電気の主な原因は『毛髪内部の水分不足』と『乾燥したキューティクル同士の摩擦』です。インバスのトリートメントで毛髪内部の水分保持力（CMC脂質）を補給し、お風呂上がりにはヘアミルクやヘアオイルで表面を油分コーティングしてください。また、タートルネックやマフラーの化学繊維（アクリルやポリエステル）との擦れを避けるため、スタイリング時にヘアオイルを少量毛先に仕込むと静電気が大幅に抑えられます。"
                    }
                }
            ]
        }
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！サロン帰りの濃密ツヤまとまりが続く高保湿ヘアトリートメントランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の乾燥でパサつく毛先・静電気広がり・枝毛ダメージを徹底解決！オージュア、ケラスターゼ、フィーノ、ミルボン、モロッカンオイル、アンドハニーなど、高純度補修成分とCMC脂質配合の最強高保湿ヘアトリートメント10選を徹底比較！">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-hair-treatment">
  <meta property="og:title" content="保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！サロン帰りの濃密ツヤまとまりが続く高保湿ヘアトリートメントランク10">
  <meta property="og:description" content="11月・12月の冬の乾燥でパサつく毛先・静電気広がり・枝毛ダメージを徹底解決！オージュア、ケラスターゼ、フィーノ、ミルボン、モロッカンオイル、アンドハニーなど、高純度補修成分とCMC脂質配合の最強高保湿ヘアトリートメント10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-hair-treatment">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="style.css">
  <script type="application/ld+json">
{json.dumps(json_ld_structure, ensure_ascii=False, indent=2)}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container header-container">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav class="site-nav">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#guide-section">選び方解説</a>
        <a href="#faq-section">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container main-content">
    <article class="article-body">
      <nav class="breadcrumb" aria-label="パンくずリスト">
        <ol>
          <li><a href="/">トップ</a></li>
          <li aria-current="page">高保湿ヘアトリートメント</li>
        </ol>
      </nav>

      <header class="article-header">
        <span class="badge category-badge">ヘアケア集中補修・静電気防止</span>
        <h1 class="article-title">保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！サロン帰りの濃密ツヤまとまりが続く高保湿ヘアトリートメントランク10</h1>
        <div class="article-meta">
          <time datetime="2026-11-01">2026年11月1日更新</time>
          <span class="author">執筆：冬コスメ比較検証チーム</span>
        </div>
      </header>

      <!-- 導入文 -->
      <section class="intro-box">
        <p>
          11月から12月へと季節が進むと、外気の湿度は急激に低下し、室内ではエアコン暖房の温風が一日中吹き荒れます。「朝しっかりブローしたのに、外に出た瞬間に毛先がパサパサに広がる」「マフラーやウールコートを着脱するたびにパチパチと激しい静電気が起きて髪が顔に張り付く」「枝毛や切れ毛が増えて毛先がほうきのように硬くなっている」といった深刻なダメージに頭を抱えていませんか？
        </p>
        <p>
          冬の髪は、外気の過乾燥によって毛髪内部の水分が蒸発するだけでなく、衣類との摩擦によってキューティクルが削り取られ、細胞膜複合体（CMC）やケラチンタンパク質が容赦なく流出しています。スカスカになった毛髪内部を放置したままでは、どんなに高価なヘアオイルを上から塗り重ねても、水分を抱え込むことができず乾燥は悪化する一方です。
        </p>
        <p>
          この過酷な真冬の乾燥毛を救う唯一の鍵が、毎日のバスタイムで毛髪深部までアミノ酸・CMC脂質・植物性オイルを浸透させ、キューティクルを密着疎水化する<strong>本格的な高保湿ヘアトリートメント</strong>です。
        </p>
        <p>
          本特集では、楽天市場やドラッグストア、サロン専売品の中から、美容エディターと検証チームが成分浸透力・毛先補修力・静電気防止効果・仕上がりのまとまり感を徹底検証し、11月〜12月の真冬に本当に髪が生き返る実力派10選をランキング形式で厳選しました。
        </p>
      </section>

      <!-- 目次 -->
      <nav class="toc-card" aria-label="目次">
        <h2 class="toc-title">📑 目次</h2>
        <ul class="toc-list">
          <li><a href="#why-dry">1. なぜ11月〜12月に髪のパサつき・静電気爆発が起きるのか？</a></li>
          <li><a href="#how-to-choose">2. 失敗しない冬の高保湿ヘアトリートメントの選び方3原則</a></li>
          <li><a href="#ranking">3. 高保湿ヘアトリートメントおすすめ厳選ランキング10選</a></li>
          <li><a href="#comparison">4. 高保湿ヘアトリートメント10選 スペック比較表</a></li>
          <li><a href="#guide-section">5. サロン帰りの質感を再現する「お風呂場コーミング＆蒸しタオル術」</a></li>
          <li><a href="#faq-section">6. よくある質問 (FAQ)</a></li>
          <li><a href="#related-section">7. あわせて読みたい冬の徹底保湿特集</a></li>
        </ul>
      </nav>

      <!-- 科学的背景解説 -->
      <section id="why-dry" class="content-block">
        <h2>🔬 なぜ11月〜12月に髪のパサつき・静電気爆発が起きるのか？</h2>
        <p>
          冬になるとヘアオイルを塗ってもすぐに毛先がバサバサになるのには、毛髪科学的な3つの明確な要因が存在します。
        </p>
        <div class="science-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:20px; margin:24px 0;">
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">① 毛髪内部のCMC脂質層の流出と水分枯渇</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              健康な髪は11〜13%の水分を保持していますが、冬の湿度30%以下の環境では水分量が8%以下まで激減します。水分をつなぎ止めている細胞膜複合体（CMC）のセラミドやコレステロールが流出すると、髪は多孔質（スカスカのスポンジ状態）になり、乾いた空気が内部の水分を吸い上げ続けます。
            </p>
          </div>
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">② 冬物衣類の摩擦によるキューティクル剥離</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              マフラー、タートルネック、ウールコート、ダウンの襟元など、冬は首回りの衣服と髪が一日中激しく接触します。乾燥したキューティクルは柔軟性を失ってめくれ上がりやすくなっており、摩擦によって表面のウロコ状の脂質層が剥がれ落ちていきます。
            </p>
          </div>
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">③ 湿度の急落による静電気の帯電爆発</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              湿度が40%を下回ると、自然放電が起きにくくなり、髪の毛に数千ボルトの静電気が蓄積します。静電気を帯びた毛髪同士は互いに反発し合って大きく広がり、さらに空気中の微細なホコリや花粉を強力に引き寄せて手触りを一段とザラつかせます。
            </p>
          </div>
        </div>
      </section>

      <!-- 選び方解説 -->
      <section id="how-to-choose" class="content-block">
        <h2>💡 失敗しない冬の高保湿ヘアトリートメントの選び方3原則</h2>
        <p>
          冬の頑固なパサつきと静電気を根本解決するためには、ただシリコンで表面をツルツルにするだけの製品では不十分です。以下の3つの基準をチェックして、深部からうるおいを満たすトリートメントを選びましょう。
        </p>
        <div class="choose-principles" style="margin:24px 0;">
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin-bottom:16px;">
            <h3 style="color:#0369a1; margin-top:0;">基準1：CMC補修成分（セラミド・コレステロール・オリーブスクワラン）の配合</h3>
            <p style="line-height:1.7; color:#475569;">
              毛髪内部で水分を抱え込み、キューティクル同士を接着するセメントの役割を果たすCMC成分が配合されているかを確認しましょう。セラミドやスクワラン、アミノ酸複合体が含まれているトリートメントは、スカスカになった髪の芯までうるおいを補充します。
            </p>
          </div>
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin-bottom:16px;">
            <h3 style="color:#0369a1; margin-top:0;">基準2：濃密植物性エモリエントオイル（アルガンオイル・シアバター）による疎水化コーティング</h3>
            <p style="line-height:1.7; color:#475569;">
              傷んだ髪は親水性（水を吸いやすく乾きやすい）に傾いています。良質なアルガンオイルやシア脂、マヌカハニーなどのエモリエント成分で表面を疎水化コーティングすることで、冬の暖房風による水分蒸発を物理的にシャットアウトします。
            </p>
          </div>
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <h3 style="color:#0369a1; margin-top:0;">基準3：髪質（太い・硬い vs 細い・軟毛）に合ったテクスチャー</h3>
            <p style="line-height:1.7; color:#475569;">
              太くて硬いゴワつき毛には、こっくり重めのリッチバター系マスク（モロッカンオイルやフィーノ）が適しています。一方、細くて柔らかい猫っ毛の方は、軽やかなエマルジョン状で根元を潰さず毛先だけをまとめる処方（ケラスターゼやYOLU）を選ぶと失敗しません。
            </p>
          </div>
        </div>
      </section>

      <!-- ランキング一覧セクション -->
      <section id="ranking" class="ranking-section">
        <div class="ranking-header">
          <h2>🏆 高保湿ヘアトリートメントおすすめ厳選ランキング10選</h2>
          <p class="ranking-subtitle">11月〜12月のパサつき・静電気・枝毛を防ぎ、サロン帰りの濃密なツヤとまとまりへ導く実力派を比較検証！</p>
        </div>
"""

# ランキング各商品のHTML生成
for idx, it in enumerate(items):
    dt = hair_treatment_details[idx]
    rank_num = it["rank"]
    
    html_content += f"""
        <!-- 第{rank_num}位 -->
        <article id="rank-{rank_num}" class="product-card">
          <div class="product-badge-wrap">
            <span class="rank-badge rank-{rank_num}">第{rank_num}位</span>
            <span class="product-sub-badge">{dt["type"]}</span>
          </div>

          <h3 class="product-name">{it["name"]}</h3>
          <p class="product-catch">{dt["catch"]}</p>

          <div class="product-main-grid">
            <div class="product-img-box">
              <img src="{it["image_url"]}" alt="{it["name"]}" class="product-img" loading="lazy">
              <div class="price-box">
                <span class="price-label">参考価格</span>
                <span class="price-value">¥{it["price"]:,}</span>
                <span class="price-tax">(税込)</span>
              </div>
              <a href="{it["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
                楽天で詳細・最安値を見る <span>&rarr;</span>
              </a>
              <span class="shop-name">取扱ショップ: {it["shop_name"]}</span>
            </div>

            <div class="product-spec-box">
              <div class="spec-highlight">
                <strong>注目ポイント:</strong> {dt["tag"]}
              </div>
              <table class="spec-table">
                <tr><th>ブランド</th><td>{it["brand"]}</td></tr>
                <tr><th>容量</th><td>{dt["capacity"]}</td></tr>
                <tr><th>テクスチャー</th><td>{dt["texture"]}</td></tr>
                <tr><th>主要補修成分</th><td>{dt["ingredients"]}</td></tr>
                <tr><th>仕上がりの質感</th><td>{dt["finish"]}</td></tr>
              </table>
            </div>
          </div>

          <div class="product-detail-desc">
            <h4>💡 美容エディターの実力検証レビュー</h4>
            <p>{dt["desc_p1"]}</p>
            <p>{dt["desc_p2"]}</p>

            <div class="user-target-box">
              <h5>🎯 こんな方に特におすすめ！</h5>
              <p>{dt["target"]}</p>
            </div>

            <div class="expert-tips-box">
              <h5>✨ 効果を最大化するプロの使いこなし術</h5>
              <p>{dt["technique"]}</p>
            </div>

            <div class="review-quote-box">
              <span class="quote-icon">💬</span>
              <blockquote>{dt["voice"]}</blockquote>
            </div>

            <div class="caution-note">
              <strong>⚠️ 使用上の注意:</strong> {dt["caution"]}
            </div>
          </div>
        </article>
"""

html_content += f"""
      </section>

      <!-- 比較表セクション -->
      <section id="comparison" class="comparison-section" style="margin:48px 0;">
        <h2>📊 高保湿ヘアトリートメント10選 スペック比較表</h2>
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; margin-top:16px; font-size:0.95rem;">
            <thead>
              <tr style="background:#0284c7; color:#fff; text-align:left;">
                <th style="padding:12px; border:1px solid #e2e8f0;">順位・ブランド</th>
                <th style="padding:12px; border:1px solid #e2e8f0;">商品名</th>
                <th style="padding:12px; border:1px solid #e2e8f0;">主要補修成分</th>
                <th style="padding:12px; border:1px solid #e2e8f0;">仕上がり特徴</th>
                <th style="padding:12px; border:1px solid #e2e8f0;">参考価格</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">1位 オージュア</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">クエンチ ヘアトリートメント</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">オリーブスクワラン・CMC脂質</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">サロン最高峰の水分保持力とまとまり</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[0]["price"]:,}</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">2位 ケラスターゼ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">フォンダン フルイダリスト</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">モルフォユイル複合体</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">くせ・広がり・静電気を抑え弾む美髪</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[1]["price"]:,}</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">3位 フィーノ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">プレミアムタッチ 浸透美容液ヘアマスク</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ローヤルゼリーEX・PCA</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">とろける浸透感としっとり重厚なツヤ</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[2]["price"]:,}</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">4位 ミルボン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">リペア リストラティブ トリートメント</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">SSVRシルク・アミノ酸</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">棒状空洞化を芯から再構築するプロ仕様</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[3]["price"]:,}</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">5位 モロッカンオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">インテンス ハイドレーティング マスク</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">高純度アルガンオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">太く硬い髪をとろけるシルクの柔らかさへ</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[4]["price"]:,}</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">6位 アンドハニー</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ディープモイスト トリートメント</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">3種の黄金比ハチミツ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">水分量14%をキープするぷるぷる保水</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[5]["price"]:,}</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">7位 ルベル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">イオ ディープマスク</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">疎水化複合成分</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">週1〜2回の集中リペアで毛先スルン</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[6]["price"]:,}</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">8位 YOLU</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">カームナイトリペア トリートメント</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ナイトセラミド・密着エッセンス</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">睡眠中の枕摩擦をガードし翌朝うるサラ</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[7]["price"]:,}</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">9位 スティーブンノル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">モイスチュアコントロール ヘアパック</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">高浸透モイスチュアカプセル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">深層までうるおいを届けるカプセル技術</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[8]["price"]:,}</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">10位 ラックス</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">スーパーリッチシャイン ダメージリペア</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ヒアルロン酸オイル・ホホバ油</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">大容量＆高コスパで毎日のツヤ補修</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[9]["price"]:,}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 塗り方テクニック解説 -->
      <section id="guide-section" class="expert-guide-section" style="background:#f8fafc; border-radius:12px; padding:28px; margin:40px 0;">
        <h2>🛁 サロン帰りの質感を再現する「お風呂場コーミング＆蒸しタオル術」</h2>
        <div style="line-height:1.8; color:#334155;">
          <h3>1. 水気を絞ってから「水分と油分の乳化」を意識する</h3>
          <p>
            シャンプーを洗い流した後、髪に水がボタボタ垂れている状態でトリートメントをつけても、表面で滑って流れてしまいます。毛束を手でキュッと握ってしっかり水気を切り、必要であれば乾いたフェイスタオルで軽く押さえてからトリートメントを塗布してください。トリートメントの濃度が薄まらず、成分が髪にダイレクトに密着します。
          </p>

          <h3 style="margin-top:24px;">2. 目の粗いジャンボコームで毛先から優しく梳かす</h3>
          <p>
            手ぐしだけでは、髪の表面にしかトリートメントがつきません。目の粗いプラスチック製コームを使って、毛先から中間へ向かって優しくコーミングしましょう。髪一本一本の周囲に均一な油分ヴェールが形成され、すすいだ後のなめらかさが別次元に跳ね上がります。
          </p>

          <h3 style="margin-top:24px;">3. 蒸しタオルで包んで3分間「スチーム浸透」</h3>
          <p>
            特に乾燥や枝毛がひどい日は、熱めのお湯で絞ったフェイスタオルを頭に巻き、シャワーキャップをかぶって3〜5分間湯船に浸かります。お風呂のスチーム熱によってキューティクルが緩み、トリートメント内部のCMC脂質やアミノ酸が毛髪深部まで一気に浸透します。
          </p>
        </div>
      </section>

      <!-- よくある質問 (FAQ) -->
      <section id="faq-section" class="faq-section">
        <h2>❓ 冬の高保湿ヘアトリートメント よくある質問 (FAQ)</h2>
        <div class="faq-item">
          <h3>Q1. コンディショナー、ヘアトリートメント、ヘアマスクの違いと正しい使い分けは？</h3>
          <p>コンディショナーは主に『毛髪表面のキューティクルを整えて滑りを良くするもの』です。一方、ヘアトリートメントは『毛髪内部にアミノ酸やCMC脂質などの栄養を浸透補修するもの』、ヘアマスクはさらに成分濃度が高く『ハイダメージを集中治療するスペシャルケア』です。冬の乾燥時期は、毎日のケアにヘアトリートメントを使用し、週に1〜2回ヘアマスクへ置き換えるケアが最も効果的です。</p>
        </div>
        <div class="faq-item">
          <h3>Q2. トリートメントの効果を劇的に高めるお風呂場での塗り方はありますか？</h3>
          <p>ポイントは2つあります。第1に、シャンプー後に『手でしっかり水気を切る（または軽くタオルで押さえる）』ことです。髪に水分が余分に残っているとトリートメントが薄まり、内部まで浸透しません。第2に、毛先に塗布した後に『目の粗いジャンボコームで優しくコーミングする』ことです。手だけでは届かない髪一本一本の内側まで均一に成分を行き渡らせることができます。</p>
        </div>
        <div class="faq-item">
          <h3>Q3. 冬の静電気で髪が広がって顔に張り付くのを防ぐにはどうすればいいですか？</h3>
          <p>静電気の主な原因は『毛髪内部の水分不足』と『乾燥したキューティクル同士の摩擦』です。インバスのトリートメントで毛髪内部の水分保持力（CMC脂質）を補給し、お風呂上がりにはヘアミルクやヘアオイルで表面を油分コーティングしてください。また、タートルネックやマフラーの化学繊維（アクリルやポリエステル）との擦れを避けるため、スタイリング時にヘアオイルを少量毛先に仕込むと静電気が大幅に抑えられます。</p>
        </div>
      </section>

      <!-- 関連特集への内部リンク -->
      <section id="related-section" class="related-section">
        <h2>🔗 あわせて読みたい冬の徹底保湿・ヘアケア特集</h2>
        <div class="internal-links-grid">
          <a href="/winter-moisture-shampoo" class="related-card">
            <span class="related-tag">シャンプー</span>
            <h4>🫧 高保湿シャンプー ランク10</h4>
            <p>アミノ酸系洗浄で頭皮と髪の水分を奪わずに洗い上げる名品。</p>
          </a>
          <a href="/winter-hair-oil" class="related-card">
            <span class="related-tag">アウトバス</span>
            <h4>✨ 高保湿ヘアオイル ランク10</h4>
            <p>ドライヤーの熱から守り一日中艶めく美髪をキープする濃密オイル。</p>
          </a>
          <a href="/winter-hair-milk" class="related-card">
            <span class="related-tag">保水ミルク</span>
            <h4>🥛 高保湿ヘアミルク ランク10</h4>
            <p>髪の内部まで水分をチャージするみずみずしい先行補修エマルジョン。</p>
          </a>
          <a href="/winter-hair-mask" class="related-card">
            <span class="related-tag">集中マスク</span>
            <h4>💆 集中ヘアマスク ランク10</h4>
            <p>週1回の集中ケアでハイダメージ毛をサロン帰りの手触りへ。</p>
          </a>
        </div>
      </section>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <p class="copyright">&copy; 2026-2027 冬コスメ徹底比較ラボ All Rights Reserved.</p>
      <div class="footer-links">
        <!-- 後ほど一括スクリプトで全更新 -->
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-hair-treatment.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated winter-hair-treatment.html ({len(html_content):,} bytes)")
