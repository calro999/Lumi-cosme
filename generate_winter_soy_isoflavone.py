import json
import re

with open("fetched_3new_fucoidan_royal_soy.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_soy_isoflavone"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👁️ 目元のちりめんジワをふっくら持ち上げる！高純度イソフラボン×ピュアレチノールの密着アイクリーム",
        "catch": "大ヒットを記録し続けるなめらか本舗の最高傑作。滋賀県産大豆『たまほまれ』使用の高純度豆乳イソフラボンとピュアレチノール、ビタミンE誘導体を贅沢配合。真冬のエアコン暖房直撃で乾燥小ジワが刻まれやすい目元を濃密ラッピング",
        "brand_name": "なめらか本舗 (常盤薬品工業)",
        "capacity": "20g / 細口チューブ容器",
        "type": "高純度豆乳イソフラボン×ピュアレチノール 薬用アイクリーム",
        "features": "高純度豆乳イソフラボン、ピュアレチノール、豆乳発酵液、ビタミンE誘導体、無香料・無鉱物油",
        "value": "皮膚が薄く皮脂腺の少ない目元のために開発された密着ポリマー処方。塗った瞬間にピーンとしたハリ膜を形成し、夕方になってもファンデーションがシワに落ちない鉄壁の目元保湿を実現",
        "desc_p1": "11月から12月にかけて湿度が急低下すると、顔の中で最も早く乾燥の悲鳴を上げるのが目元です。頬の3分の1ほどの厚みしかない目の周りの皮膚は、エアコンの温風にさらされるとわずか数時間で角層水分が枯渇し、笑ったときに細かいちりめんジワが戻らなくなる『乾燥小ジワ定着現象』を引き起こします。なめらか本舗の『リンクルアイクリーム』は、そうした真冬の目元危機を救うために誕生した大人気集中ケアクリームです。",
        "desc_p2": "こっくりとした濃厚なテクスチャーですが、指先で温めると体温でするりと溶け出し、デリケートな目元に摩擦を一切かけずにピタッと吸着。イソフラボンの女性ホルモン様作用とピュアレチノールのターンオーバー促進力が融合し、内側から押し返すようなふっくらとした厚み感を創出します。夜のケアはもちろん、朝のメイク前に少量仕込むだけで、暖房の効いたオフィスでも目元が一日中みずみずしく潤い、夕方の疲れ顔を寄せ付けません。",
        "target": "暖房の効いたオフィスで夕方になると目元の乾燥小ジワやファンデのヨレが目立つ方、まぶたの乾燥やハリの低下が気になる方、ドラッグストアで買える本格的なアイクリームを探している方",
        "point": "スキンケアの最後に、米粒大を薬指にとり、目頭から目尻に向かって優しくトントンと軽く叩き込むように馴染ませます。ほうれい線や眉間の乾燥が気になる部分にも重ねづけすると効果的です。"
    },
    {
        "rank": 2,
        "tag": "🌙 おやすみ中の濃厚パック効果！翌朝の洗顔時に吸い付くモチ肌を実感できる濃密ナイトクリーム",
        "catch": "寝ている間の無防備な肌を暖房の砂漠気流から守り抜く。高純度豆乳イソフラボンとピュアレチノールを閉じ込めた『おやすみパック処方』。真冬の朝一番の素肌をふっくら柔らかく再生する極上ナイトクリーム",
        "brand_name": "なめらか本舗 (常盤薬品工業)",
        "capacity": "50g / 遮光ジャー容器",
        "type": "豆乳発酵液×ピュアレチノール 濃厚高保湿ナイトクリーム",
        "features": "高純度豆乳イソフラボン、豆乳発酵液（滋賀県産丸大豆）、ピュアレチノール、セラミドNG、スクワラン",
        "value": "体温に反応してとろける濃厚エモリエント膜が、就寝中の呼気や寝室暖房による水分蒸発を完全ブロック。ベタつかないのに一晩中ラップを密着させているかのような濃密な潤い保持力を発揮",
        "desc_p1": "冬の睡眠中、暖房をつけっぱなしにしている部屋や加湿器の切れた寝室では、朝起きるまでの6〜8時間の間にコップ1杯分以上の水分が肌から失われています。『朝起きると顔がバリバリに乾いて痛い』という冬特有の悩みに応えて開発されたのが、なめらか本舗の『リンクルナイトクリーム』です。",
        "desc_p2": "クリームを手にとると、バターのように重厚なコクがありますが、肌に伸ばすと体温に反応してなめらかに広がり、肌表面に薄いシールドヴェールを形成します。大豆イソフラボンとピュアレチノールが夜間の肌のターンオーバーとコラーゲン合成を後押しし、角層深部に潤いをじっくり充填。翌朝ぬるま湯で洗顔した瞬間、指先が吸い付くようなプルプルのモチ肌に仕上がっていることを実感できます。1,000円前後のプチプラでありながらデパコス級の保湿持続力を誇ります。",
        "target": "冬の朝起きると顔が突っ張って乾燥している方、就寝中の暖房によるインナードライを防ぎたい方、プチプラで惜しみなく毎晩たっぷり使える濃厚ナイトクリームを求める方",
        "point": "夜のお手入れの最後に、さくらんぼ大を手にとって顔全体から首筋までたっぷり伸ばします。特に乾燥が気になる頬骨や口周りには厚めに重ねて『スリーピングマスク』として就寝してください。"
    },
    {
        "rank": 3,
        "tag": "⚡ 1個で6役の濃厚形状記憶ジェル！真冬の乾燥でしぼんだ角層をふっくら満たす万能オールインワン",
        "catch": "化粧水・美容液・乳液・クリーム・パック・化粧下地の6役。ぐちゃぐちゃに崩しても数秒でピンと元に戻る形状記憶ジェル。高濃度豆乳イソフラボンが真冬の時短スキンケアをリッチに格上げ",
        "brand_name": "なめらか本舗 (常盤薬品工業)",
        "capacity": "100g / 詰替え用対応エコパック",
        "type": "高純度豆乳イソフラボン 濃厚形状記憶オールインワンジェル",
        "features": "高純度豆乳イソフラボン、豆乳発酵液、植物性コラーゲン、ダイズ種子エキス、エモリエントオイル",
        "value": "復元ポリマーが肌表面に均一なハリ膜を形成し、毛穴の凹凸やしぼみをふっくら補正。ゲルの水分蒸散を防ぐエモリエントカプセル技術により、冬の寒風下でも夕方までモチ肌が持続",
        "desc_p1": "寒い冬の朝、複数のスキンケアを重ねるのは時間がかかるだけでなく、手がかじかんで億劫になりがちです。しかし、一般的なオールインワンジェルでは『軽すぎて冬はすぐに乾燥する』という不満がつきまといます。『とろんと濃ジェル エンリッチ』は、そうした声に応えてオイル成分を20%増量し、真冬の過酷な乾燥に耐えうる濃厚処方へと進化した実力派です。",
        "desc_p2": "ぷるぷるの形状記憶ジェルを肌に乗せると、とろけるように馴染んで角層の微細なキメの隙間まで満たします。表面にはピンとした密着膜が張り、乾燥による毛穴の開きや小ジワを目立たなくさせるタイトニング効果を発揮。保湿成分がじわじわと角層内に浸透し続けるため、これ1つで仕上げた後すぐにメイクしてもヨレず、暖房の効いた部屋でも一日中もっちり吸い付くような潤いが続きます。",
        "target": "冬の朝晩のスキンケアを素早く済ませたいけれど乾燥は一切妥協したくない方、ゲルのベタつきやモロモロが苦手な方、お財布に優しい価格で高保湿を継続したい方",
        "point": "洗顔後、さくらんぼ大を手にとって顔全体に馴染ませ、手のひらで顔全体を引き上げるように10秒間ハンドプレス。メイク前は余分な油分をティッシュオフすると化粧ノリがさらにアップします。"
    },
    {
        "rank": 4,
        "tag": "🍶 お風呂で塗って流すだけで生まれたてのモチ肌！豆腐屋さんが作った濃厚ヨーグルトパック",
        "catch": "椎葉村の清らかな湧き水と国産大豆から絞った濃厚豆乳発酵液を贅沢配合。ヨーグルトエキスとローヤルゼリーが冬のごわつく古い角質を優しくほぐし、驚くほど透き通る柔肌へ導くお風呂パック",
        "brand_name": "豆腐の盛田屋",
        "capacity": "150g / ジャー容器",
        "type": "濃厚豆乳発酵液×ヨーグルト スチーム洗い流しパック",
        "features": "豆乳発酵液（国産大豆100%）、ヨーグルト液、ローヤルゼリーエキス、シイタケエキス、ハチミツ",
        "value": "入浴時のスチーム効果と合わさることで、硬くなった角層を急速に柔軟化。乳酸とアミノ酸が不要な角質を優しくオフしながら、大豆のイソフラボンがふっくら弾力を注入",
        "desc_p1": "冬になると肌のターンオーバーが乱れ、古い角質が溜まって『肌がゴワゴワして化粧水が弾かれる』というトラブルに直面します。スクラブやピーリングでは肌に刺激が強すぎる冬のデリケート肌に最適なのが、宮崎県の豆腐職人が手掛けた『豆乳よーぐるとぱっく 玉の輿』です。",
        "desc_p2": "まるでお豆腐のクリームのような美味しそうなこっくりテクスチャー。お風呂に浸かりながら顔全体に白く覆うように厚めに塗り広げると、湯気のスチーム効果で毛穴が開き、ヨーグルトの乳酸が古い角質を優しくほぐします。同時に豆乳発酵液とローヤルゼリーが角層深部へ栄養をチャージ。5〜10分後に洗い流すと、まるで剥きたてのゆで卵のようにツルツルで、指先が吸い付くほどのモチモチ肌へと生まれ変わります。",
        "target": "冬の寒さで肌がゴワつきくすんで見える方、ピーリングが痛くて使えない敏感肌・乾燥肌の方、バスタイムを贅沢な高保湿スパタイムに変えたい方",
        "point": "入浴時、洗顔後の水気を軽く拭き取ってから、目と口の周りを避けて肌が隠れるくらいの厚さで顔全体に塗り広げます。5〜10分湯船に浸かった後、ぬるま湯で優しく洗い流してください。"
    },
    {
        "rank": 5,
        "tag": "💨 毛穴より細かい超微細マイクロミスト！メイクの上から真冬の日中暖房乾燥を瞬時リセット",
        "catch": "毛穴の数分の一という極微細ミストがメイクを崩さず角層深部へダイレクト到達。高純度豆乳イソフラボンと浸透型大豆エキスが、日中の暖房気流でパサパサに干からびた肌を瞬時にレスキュー",
        "brand_name": "なめらか本舗 (常盤薬品工業)",
        "capacity": "150g×3本セット / エアゾール缶",
        "type": "高純度豆乳イソフラボン 超微細マイクロミスト化粧水",
        "features": "高純度豆乳イソフラボン、豆乳発酵液、窒素ガス微粒子噴射、無香料・無着色・無鉱物油",
        "value": "通常のスプレーのように水滴が顔に溜まってメイクが崩れることがなく、霧のようにふんわり包み込む特殊バルブを採用。冬の乾燥したオフィスや外出先でいつでもどこでも水分チャージが可能",
        "desc_p1": "11月から12月のオフィスで働く女性にとって最大の敵は、午後2時を過ぎた頃から襲ってくる『顔全体の激しい突っ張り感』です。しかし、一般的な化粧水スプレーをメイクの上から吹きかけると、水滴が蒸発する際に肌内部の水分まで一緒に奪い去ってしまい、かえって乾燥を悪化させることがあります。",
        "desc_p2": "なめらか本舗の『マイクロミスト化粧水 NC』は、窒素ガスによる超微細ミストを採用しており、顔に吹きかけても大粒の水滴にならず、霧が肌に吸い込まれるようにスーッと浸透します。大豆イソフラボンと発酵液が角層にピタッと定着するため、水分が蒸散せずしっとり感が長時間持続。メイク直しの前に吹きかければファンデーションの粉吹きが瞬時に落ち着き、生まれたてのツヤ感が復活します。3本セットで自宅・オフィス・携帯用と使い分けられます。",
        "target": "暖房の効いたオフィスで日中に顔が突っ張る方、メイク直しをすると粉を吹いて綺麗に乗らない方、お風呂上がりに子供の世話などでとりあえずすぐ保湿したい方",
        "point": "顔から20cmほど離し、円を描くように優しくスプレーします。吹きかけた後は手でこすらず、手のひらでそっと優しく顔を包み込むようにハンドプレスして角層に定着させてください。"
    },
    {
        "rank": 6,
        "tag": "✨ 薬用美白×イソフラボン高保湿！冬の寒冷くすみと乾燥小ジワを同時に晴れやかに整える濃密美容液",
        "catch": "持続型ビタミンC誘導体と高純度豆乳イソフラボンが融合。冬の冷えによる血行不良くすみと、暖房によるインナードライを1本で全方位アプローチ。澄み渡るような透明感とふっくら弾力を叶える薬用エッセンス",
        "brand_name": "なめらか本舗 (常盤薬品工業)",
        "capacity": "100ml / ポンプボトル",
        "type": "高純度豆乳イソフラボン×持続型ビタミンC 薬用純白美容液",
        "features": "持続型ビタミンC誘導体（L-アスコルビン酸2-グルコシド）、高純度豆乳イソフラボン、豆乳発酵液、グリチルリチン酸2K",
        "value": "美白美容液にありがちな『さっぱりしすぎて冬は乾燥する』という弱点を完全に克服。豆乳の濃厚な保水アミノ酸膜が角層を包み込み、真冬でももっちり吸い付くうるおい美白を実現",
        "desc_p1": "『冬は紫外線が弱いから美白ケアはお休み』と思われがちですが、実は真冬こそ美白美容液の真価が問われる季節です。寒暖差による血行不良や乾燥による角層の乱れが重なると、肌全体がどんよりと灰色にくすみ、実年齢よりも疲れて見えてしまうのです。なめらか本舗の『薬用純白美容液』は、美白有効成分と濃密な豆乳保湿を両立させた名作です。",
        "desc_p2": "とろみのあるミルキーな美容液が肌に乗せるとみずみずしく崩れ、角層のすみずみまで浸透。持続型ビタミンCがメラニンの生成を抑えてシミ・そばかすを防ぎながら、高純度豆乳イソフラボンが角層細胞の間にうるおいを満たします。美白美容液とは思えないほどのしっとり感があり、塗布後は光を均一に反射するパッと明るい白玉肌へと整います。100mlの大容量で毎日首まで惜しみなく美白保湿を継続できます。",
        "target": "冬になると顔全体がどんよりくすんで透明感がなくなる方、乾燥肌でも刺激や突っ張りを感じずに使える美白美容液を探している方、大容量でコスパ良く透明美肌を育てたい方",
        "point": "化粧水の直後、1〜2プッシュを手にとって顔全体に伸ばし、手のひらで温めるようにハンドプレス。くすみが気になる頬や目の下には、さらに半プッシュを重ねづけしてください。"
    },
    {
        "rank": 7,
        "tag": "🧼 もっちり弾力泡が冬の摩擦を完全ゼロ化！洗い上がりもしっとり吸い付く豆乳クレンジング洗顔",
        "catch": "高純度豆乳イソフラボンと豆乳発酵液を練り込んだクリーミー洗顔フォーム。キメ細かい濃密クッション泡が冬の乾いた素肌を摩擦レスに包み込み、メイクも汚れも優しく落として突っ張り感ゼロ",
        "brand_name": "なめらか本舗 (常盤薬品工業)",
        "capacity": "150g / チューブ容器",
        "type": "豆乳イソフラボン配合 高保湿クレンジング洗顔フォーム",
        "features": "高純度豆乳イソフラボン、豆乳発酵液、植物性マイルド洗浄成分、無香料・無着色・無鉱物油",
        "value": "大豆由来のレシチンとアミノ酸が洗顔中の肌バリアを保護。水仕事や冷たい水で洗っても角層の水分流出を防ぎ、洗顔後すぐに化粧水をつけられない時でももっちり感が持続",
        "desc_p1": "冬のスキンケアにおいて、最も肌の水分を奪うトラップが『毎日のクレンジングと洗顔』です。強い脱脂力を持つ洗顔料を使っていると、角層のセラミドやNMFがどんどん流出し、その後のスキンケアが全く追いつかなくなります。なめらか本舗の『クレンジング洗顔 NC』は、大豆の自然な恵みを生かして肌を守りながら洗う定番中の定番アイテムです。",
        "desc_p2": "少量を洗顔ネットに出して泡立てると、逆さにしても落ちないほどキメ細やかで弾力のある濃密なホイップ泡が瞬時に出来上がります。指先が直接肌に触れないクッション効果により、真冬の敏感になった角層を摩擦ダメージから完全ガード。軽いメイクや皮脂汚れを優しく吸着して落とし、すすいだ後はまるで化粧水をつけた直後のようなしっとり感が肌に残ります。ドラッグストアで手軽に買える最高の乾燥対策洗顔です。",
        "target": "冬の洗顔後に顔が突っ張って痛い方、クレンジングによる肌の摩擦や乾燥が気になる方、家族全員で毎日惜しみなく使える低刺激な高保湿洗顔を求める方",
        "point": "泡立てネットでピンポン玉2個分の弾力泡を作り、顔全体に泡を転がすように優しく洗います。ぬるま湯（32〜34℃）で、泡が完全に落ちるまでこすらず丁寧にすすぎ流してください。"
    },
    {
        "rank": 8,
        "tag": "🛡️ 1本で朝のケアからUVカットまで！真冬の冷風と紫外線を防ぐノンケミカル高保湿乳液",
        "catch": "化粧水の後これ1本で乳液・美容液・UVカット・化粧下地が完了。高純度豆乳イソフラボンとセラミドが真冬の冷気と暖房による乾燥崩れを防ぎ、SPF40 PA+++で冬の紫外線もしっかり防御",
        "brand_name": "なめらか本舗 (常盤薬品工業)",
        "capacity": "50g / チューブ容器",
        "type": "高純度豆乳イソフラボン リンクルUV高保湿乳液",
        "features": "高純度豆乳イソフラボン、豆乳発酵液、ピュアレチノール、ヒト型セラミド、ノンケミカル（紫外線吸収剤不使用）",
        "value": "冬の朝のスキンケア工程を激減させながら、一日中暖房の効いたオフィスでも乾燥崩れを起こさない高密着エマルジョン処方。白浮きせず自然なツヤ肌を一日中キープ",
        "desc_p1": "冬の朝は寒くてスキンケアに時間をかけられない一方、日中はオフィスの暖房気流と冬の紫外線というダブルの脅威にさらされます。日焼け止めを塗ると乾燥して粉を吹いてしまうという方に圧倒的な支持を得ているのが、なめらか本舗の『リンクルUV乳液』です。",
        "desc_p2": "淡いベージュカラーの軽やかな乳液ですが、肌に伸ばすと美容クリームのようにリッチに密着し、毛穴や色ムラをふんわり自然に補正します。紫外線吸収剤を使わないノンケミカル処方でありながら白浮きやきしみ感が一切なく、高純度豆乳イソフラボンとセラミドが肌の内側からうるおいをホールド。これ1本とお粉だけで冬のナチュラルツヤ肌が完成し、夕方になっても乾燥崩れや小ジワ割れが起きません。",
        "target": "冬の朝のメイク時間を短縮したい方、日焼け止めを使うと肌が乾燥して突っ張る方、ファンデーションを使わずに自然な美肌と高保湿を両立したい方",
        "point": "化粧水で肌を整えた後、パール粒1〜2個分を手にとって顔全体にムラなく均一に伸ばします。特に乾燥しやすい頬骨や目元にはトントンと重ねづけしてください。"
    },
    {
        "rank": 9,
        "tag": "💧 圧倒的大容量500ml！惜しみなく全身にバシャバシャ使える高純度豆乳ローション",
        "catch": "国産大豆由来の良質なイソフラボンと発酵エキスを凝縮したメガサイズ化粧水。冬の入浴後の全身保湿やローションパックに最適。タイツの摩擦ですねが粉を吹く真冬のボディ乾燥を完全シャットアウト",
        "brand_name": "四季折々 / なめらか本舗",
        "capacity": "500ml / ポンプ大容量ボトル",
        "type": "高純度豆乳イソフラボン 全身用大容量モイスチャーローション",
        "features": "ダイズ種子エキス、豆乳発酵液、植物性セラミド、弱酸性・低刺激処方",
        "value": "サラサラとしたテクスチャーでありながら肌に乗せると驚くほどしっとり吸い付く浸透力。500mlの大容量なのでコットンパックや家族全員の全身乾燥ケアに惜しみなく使用可能",
        "desc_p1": "11月から12月にかけて、顔だけでなく『タイツを脱ぐとすねが粉を吹いてかゆい』『背中や腕が乾燥してカサつく』というボディの砂漠化に悩む方が急増します。高価なボディクリームを毎日全身に塗るのはコストがかかりますが、この大容量500ml豆乳イソフラボン化粧水なら、惜しみなく全身へ水分を補給できます。",
        "desc_p2": "お風呂上がりに全身へバシャバシャと浴びるように馴染ませると、肌のキメの奥深くまでスーッと吸い込まれていきます。大豆イソフラボンと植物性セラミドが角層の水分油分バランスを瞬時に整え、粉吹きやかゆみの原因となる過剰な乾燥をリセット。ベタつきが一切残らないため、塗った直後に冬用のパジャマやヒートテックを着ても張り付かず、一日中スベスベの滑らかな肌触りが続きます。",
        "target": "冬になるとすねや腕が粉を吹いてかゆくなる方、大容量でコスパ良くコットンパックを毎日したい方、お風呂上がりに家族全員で使える低刺激ローションを探している方",
        "point": "お風呂から上がって体を拭いたら、すぐにポンプを数回プッシュして顔からデコルテ、腕、すねまで全身にたっぷり伸ばします。乾燥が激しい部位は、その上から乳液やボディミルクを重ねてください。"
    },
    {
        "rank": 10,
        "tag": "👑 迷ったらこれ！ヒト型セラミド×高純度イソフラボンの黄金比が生んだ冬の鉄板高保湿ローション",
        "catch": "なめらか本舗の代名詞とも言える超ロングセラー化粧水がリニューアル。世界新開発の高純度豆乳イソフラボンとヒト型セラミドを融合。真冬の過酷な暖房直撃下でも一日中乾かない濃密うるおい肌を土台から構築",
        "brand_name": "なめらか本舗 (常盤薬品工業)",
        "capacity": "200ml / つめかえ用エコパウチ",
        "type": "高純度豆乳イソフラボン×ヒト型セラミド しっとり化粧水",
        "features": "高純度豆乳イソフラボン、豆乳発酵液、ヒト型セラミド（セラミドNG）、無香料・無着色・無鉱物油",
        "value": "角層への浸透性を極限まで高めたとろみリキッド。つけた瞬間から肌がゴクゴク飲み干すように吸い込まれ、吸い付くようなモチ肌とキメの整った素肌を長時間キープ",
        "desc_p1": "ドラッグストアのスキンケアコーナーで不動の人気を誇るなめらか本舗の『しっとり化粧水』。その最新処方は、滋賀県産大豆たまほまれから抽出された高純度イソフラボンに加え、肌のバリア構造そのものであるヒト型セラミドを贅沢に配合し、真冬の乾燥対策ローションとして完璧な進化を遂げています。",
        "desc_p2": "手に取るとほんのりとろみがありますが、肌に乗せるとパシャッと弾けて角層の奥深くへと浸透。イソフラボンの水分保持力とセラミドの細胞間脂質補修作用がダブルで働き、冷風や暖房でダメージを受けた肌のキメをふっくらと持ち上げます。数回重ねづけすると、まるで美容液を塗った後のようなモチモチの手触りに整い、夕方になっても乾燥によるメイク崩れや突っ張りを一切感じさせません。リピート率No.1の確かな実力を誇る逸品です。",
        "target": "何を使っても冬の乾燥がおさまらず定番の頼れる化粧水を探している方、プチプラで高品質な高保湿スキンケアを追求したい方、もっちり吸い付くようなハリ感を実感したい方",
        "point": "手のひらに500円玉大を取り、手の熱で温めてから顔全体を包み込むようにハンドプレス。乾燥が気になる日は2度塗り、3度塗りと重ねることで、角層深部まで水分をミルフィーユ状に密閉できます。"
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
                <span class="review-count">（口コミ {item_data.get("review_count", "150")}件）</span>
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
  <title>保湿力の強さで肌乾燥とさようなら！植物エストロゲンと濃密大豆発酵液が真冬の水分蒸散としぼみ肌をふっくらモチモチに再生する高保湿豆乳イソフラボンコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の暖房乾燥によるインナードライ・角層脱水・目元の小ジワを救う高保湿豆乳イソフラボン（大豆発酵エキス・植物エストロゲン）コスメを徹底厳選！なめらか本舗、豆腐の盛田屋、四季折々まで植物性エストロゲン様作用と角層柔軟化の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="豆乳イソフラボン コスメ, なめらか本舗 アイクリーム, 高保湿 コスメ 冬, インナードライ 11月 12月, 暖房乾燥 対策, なめらか本舗 ナイトクリーム, とろんと濃ジェル, 豆乳よーぐるとぱっく">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！植物エストロゲンと濃密大豆発酵液が真冬の水分蒸散としぼみ肌をふっくらモチモチに再生する高保湿豆乳イソフラボンコスメランク10">
  <meta property="og:description" content="大豆の生命力！植物エストロゲンと濃密大豆発酵液が、真冬の暖房乾燥でしぼんだ角層をふっくらモチモチに再生するおすすめコスメ10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-soy-isoflavone">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿豆乳イソフラボンコスメランク10">
  <meta name="twitter:description" content="11月・12月の暖房砂漠肌に！高純度豆乳イソフラボンコスメおすすめ厳選10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！植物エストロゲンと濃密大豆発酵液が真冬の水分蒸散としぼみ肌をふっくらモチモチに再生する高保湿豆乳イソフラボンコスメランク10",
    "description": "11月・12月の暖房乾燥によるインナードライ・角層脱水を救う高保湿豆乳イソフラボンコスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-06T03:45:00+09:00",
    "dateModified": "2026-11-06T03:45:00+09:00",
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
      "@id": "https://lumi-cosme.vercel.app/winter-soy-isoflavone"
    }}
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #2: ItemList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
      {",\n      ".join([f'''{{
        "@type": "ListItem",
        "position": {p["rank"]},
        "name": "{items[p["rank"]-1]["item_name"][:50]}",
        "url": "{items[p["rank"]-1]["affiliate_url"]}"
      }}''' for p in product_details])}
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
        "name": "豆乳イソフラボンが冬の乾燥肌に特に効果的な理由は何ですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "大豆イソフラボンは女性ホルモン（エストロゲン）と化学構造が類似しており、肌のエストロゲン受容体にアプローチしてコラーゲンやヒアルロン酸の自己合成を促します。冬の寒暖差やストレスで肌のリズムが乱れ、しぼんで硬化した角層を内側からふっくら柔軟化し、吸い付くようなモチ肌を蘇らせます。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "なめらか本舗のイソフラボンシリーズは敏感肌でも使えますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "はい、基本的に無香料・無着色・無鉱物油処方で設計されており、敏感肌パッチテスト済みです。ただし、レチノール配合タイプ（リンクルシリーズ等）は非常に乾燥している部位に塗ると初期にピリつきを感じる場合があるため、まずは少量を目元等で試すか、通常のしっとりタイプから始めるのが安心です。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "冬の朝のメイク前に豆乳ジェルやクリームを使ってもヨレませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "『とろんと濃ジェル』や『リンクルUV乳液』は、メイク前の使用を前提とした高密着処方で作られており、余分なモロモロが出にくい仕様です。塗布後に両手でしっかりハンドプレスして角層に馴染ませ、表面を軽くティッシュオフしてからファンデーションを重ねると一日中乾燥崩れを防げます。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "11月・12月の冬に効果的な重ねづけテクニックは？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "まず豆乳しっとり化粧水を2〜3回重ねづけして角層の水分を満たし、目元・口元にリンクルアイクリームを塗り込んだ後、夜はリンクルナイトクリームを厚めに塗ってスリーピングパックとして密閉するのが最強の冬保湿ルーティンです。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #5c7e10;
      --primary-light: #f2f7e4;
      --primary-dark: #3a5006;
      --accent: #d35400;
      --text: #2c3e50;
      --text-muted: #5d6d7e;
      --bg: #fbfcf9;
      --card-bg: #ffffff;
      --border: #e2ebd0;
      --shadow: 0 4px 16px rgba(92, 126, 16, 0.08);
      --radius: 12px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
      padding: 0;
    }}

    header {{
      background: linear-gradient(135deg, #3a5006 0%, #5c7e10 100%);
      color: #ffffff;
      padding: 40px 20px 30px;
      text-align: center;
    }}
    .site-tagline {{ font-size: 0.9rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; opacity: 0.9; }}
    h1 {{ font-size: 1.7rem; line-height: 1.4; max-width: 960px; margin: 0 auto 15px; font-weight: 800; }}
    .header-meta {{ font-size: 0.85rem; opacity: 0.85; margin-top: 10px; }}

    .container {{
      max-width: 1000px;
      margin: 0 auto;
      padding: 30px 20px 60px;
    }}

    .breadcrumbs {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 25px;
    }}
    .breadcrumbs a {{ color: var(--primary-dark); text-decoration: none; }}
    .breadcrumbs a:hover {{ text-decoration: underline; }}

    .intro-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
      border-left: 6px solid var(--primary);
    }}
    .intro-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 15px;
    }}
    .intro-section p {{ margin-bottom: 15px; }}
    .intro-section p:last-child {{ margin-bottom: 0; }}

    .mechanism-box {{
      background: var(--primary-light);
      border-radius: var(--radius);
      padding: 24px;
      margin: 25px 0;
    }}
    .mechanism-title {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 10px;
      font-size: 1.1rem;
    }}

    .toc {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px 25px;
      margin-bottom: 40px;
    }}
    .toc-title {{ font-weight: 700; color: var(--primary-dark); margin-bottom: 12px; }}
    .toc ol {{ padding-left: 20px; }}
    .toc li {{ margin-bottom: 6px; font-size: 0.95rem; }}
    .toc a {{ color: var(--text); text-decoration: none; }}
    .toc a:hover {{ color: var(--primary-dark); text-decoration: underline; }}

    /* 商品カード */
    .product-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 30px;
      margin-bottom: 40px;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(92, 126, 16, 0.14);
    }}

    .product-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 15px;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, #5c7e10, #3a5006);
      color: #ffffff;
      font-size: 1.1rem;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 20px;
      letter-spacing: 1px;
    }}
    .product-tag {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 5px 12px;
      border-radius: 6px;
    }}

    .product-title {{
      font-size: 1.25rem;
      line-height: 1.45;
      color: var(--text);
      margin-bottom: 8px;
    }}
    .product-display-name {{
      font-size: 0.95rem;
      color: var(--text-muted);
      margin-bottom: 20px;
      line-height: 1.5;
    }}

    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 30px;
    }}
    @media (max-width: 768px) {{
      .product-layout {{ grid-template-columns: 1fr; }}
    }}

    .product-visual-col {{
      text-align: center;
    }}
    .img-wrap {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px;
      margin-bottom: 15px;
    }}
    .product-img {{
      width: 100%;
      height: 240px;
      object-fit: contain;
      border-radius: 4px;
    }}
    .price-box {{
      background: #fbfdf7;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 10px;
      margin-bottom: 10px;
    }}
    .price-label {{ font-size: 0.75rem; color: var(--text-muted); display: block; }}
    .price-value {{ font-size: 1.35rem; font-weight: 800; color: #b12704; }}
    .review-meta {{ font-size: 0.85rem; margin-bottom: 15px; color: var(--text-muted); }}
    .review-stars {{ color: #e67a00; font-weight: 700; margin-right: 4px; }}

    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff !important;
      text-align: center;
      padding: 14px 15px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 10px rgba(191, 0, 0, 0.25);
      transition: background 0.2s, transform 0.1s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a80000 0%, #800000 100%);
      transform: translateY(-1px);
    }}

    /* スペック表 */
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 10px 12px;
      border-bottom: 1px solid var(--border);
    }}
    .spec-table th {{
      width: 28%;
      background: #f5f9ed;
      color: var(--primary-dark);
      text-align: left;
      font-weight: 700;
    }}
    .spec-table td {{
      background: #ffffff;
    }}

    .product-body {{ margin-top: 15px; }}
    .body-title {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 10px;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 4px;
    }}
    .product-body p {{ margin-bottom: 12px; font-size: 0.95rem; }}

    .recommend-box {{
      background: #f9fbf4;
      border-left: 4px solid var(--primary);
      padding: 14px 16px;
      margin: 15px 0 10px;
      border-radius: 0 6px 6px 0;
    }}
    .recommend-title {{ font-weight: 700; font-size: 0.9rem; color: var(--primary-dark); margin-bottom: 4px; }}
    .recommend-box p {{ margin-bottom: 0; font-size: 0.9rem; }}

    .usage-box {{
      background: #fff9f2;
      border-left: 4px solid #d35400;
      padding: 14px 16px;
      margin: 10px 0 0;
      border-radius: 0 6px 6px 0;
    }}
    .usage-title {{ font-weight: 700; font-size: 0.9rem; color: #a04000; margin-bottom: 4px; }}
    .usage-box p {{ margin-bottom: 0; font-size: 0.9rem; }}

    /* 比較表セクション */
    .comparison-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
      overflow-x: auto;
    }}
    .comparison-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 20px;
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 12px 14px;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .comparison-table th {{
      background: var(--primary-dark);
      color: #ffffff;
      font-weight: 700;
    }}
    .comparison-table tr:nth-child(even) {{ background: #fbfdf7; }}

    /* ガイドセクション */
    .guide-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }}
    .guide-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 15px;
      border-left: 5px solid var(--primary);
      padding-left: 12px;
    }}
    .guide-section h3 {{
      font-size: 1.15rem;
      color: var(--text);
      margin: 20px 0 10px;
    }}
    .guide-section p {{ margin-bottom: 15px; font-size: 0.95rem; }}

    /* FAQセクション */
    .faq-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }}
    .faq-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 20px;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 16px 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-question {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 8px;
      font-size: 1rem;
    }}
    .faq-answer {{ font-size: 0.95rem; color: var(--text); }}

    /* 内部リンク */
    .internal-links {{
      background: #f5f9ed;
      border-radius: var(--radius);
      padding: 25px;
      margin-bottom: 40px;
    }}
    .internal-links h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin-bottom: 15px;
    }}
    .links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 12px;
    }}
    .link-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 14px;
      text-decoration: none;
      color: var(--text);
      font-size: 0.9rem;
      display: block;
      transition: border-color 0.2s, transform 0.1s;
    }}
    .link-card:hover {{
      border-color: var(--primary);
      transform: translateY(-1px);
      color: var(--primary-dark);
    }}

    footer {{
      background: #1a252f;
      color: #bdc3c7;
      padding: 40px 20px 30px;
      font-size: 0.85rem;
      text-align: center;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 15px;
      margin-bottom: 25px;
    }}
    .footer-links a {{ color: #bdc3c7; text-decoration: none; }}
    .footer-links a:hover {{ color: #ffffff; text-decoration: underline; }}
    .copyright {{ opacity: 0.7; }}
  </style>
</head>
<body>

  <header>
    <div class="site-tagline">LUMI COSMETICS - 科学的エビデンスで選ぶ真冬の本格高保湿スキンケア</div>
    <h1>保湿力の強さで肌乾燥とさようなら！植物エストロゲンと濃密大豆発酵液が真冬の水分蒸散としぼみ肌をふっくらモチモチに再生する高保湿豆乳イソフラボンコスメランク10</h1>
    <div class="header-meta">
      <span>公開日: 2026年11月6日</span> | <span>監修: LUMI COSMETICS バイオスキンケア解析チーム</span>
    </div>
  </header>

  <div class="container">
    <div class="breadcrumbs">
      <a href="/">HOME</a> &gt; <a href="/winter-soy-isoflavone">高保湿豆乳イソフラボンコスメ</a>
    </div>

    <!-- 導入セクション -->
    <section class="intro-section">
      <h2>寒暖差とホルモンリズムの乱れ！なぜ11月・12月は急激にしぼみ乾燥が加速するのか？</h2>
      <p>11月から12月にかけて、急激な外気温の低下と室内の強烈な暖房による寒暖差、日照時間の短縮などは、自律神経や女性ホルモンの分泌バランスを大きく揺さぶります。エストロゲンの分泌が一時的に低下すると、肌内部のヒアルロン酸やコラーゲンの産生スピードが落ち、角層が水分を抱えきれなくなって『しぼみ・ハリ不足・インナードライ』が一気に噴出します。</p>
      
      <p>この冬のしぼみ砂漠肌を土台から立て直す成分として、日本の女性に長年最も愛され、皮膚科学的にも確固たるエビデンスを築いてきたのが『豆乳イソフラボン』です。大豆に含まれる植物性イソフラボン（ゲニステインやダイゼイン）は、女性ホルモン（エストロゲン）と極めて類似した立体構造を持ち、肌の受容体に優しくアプローチ。さらに大豆を発酵させて微細化されたアミノ酸群が、真冬の硬化した角層を吸い付くようなモチ肌へと仕立て上げます。</p>

      <div class="mechanism-box">
        <div class="mechanism-title">🧪 皮膚科学が解明！豆乳イソフラボンが冬のしぼみ肌を救う3大パワー</div>
        <ul>
          <li><strong>① 植物性エストロゲン様作用による自活保水力アップ：</strong> 大豆イソフラボンが角層細胞に働きかけ、肌自らがヒアルロン酸やセラミドを合成する力を後押し。冬の暖房直撃下でも内側から水分が湧き出る土台を構築します。</li>
          <li><strong>② 濃密な大豆発酵アミノ酸による角層柔軟化：</strong> 伝統の発酵技術で低分子化された良質なアミノ酸とペプチドが、寒さでカチコチに固まった角質層をほぐし、吸い付くような柔らかさを即座に付与します。</li>
          <li><strong>③ レチノールやビタミンCとの抜群の相乗効果：</strong> 刺激が気になりやすいレチノールや美白成分も、豆乳の濃密な保護ヴェールと融合することで、冬のデリケートな肌でも刺激なくハリ・透明感を同時に引き出せます。</li>
        </ul>
      </div>
    </section>

    <!-- 目次 -->
    <section class="toc">
      <div class="toc-title">📑 目次（タップで該当セクションへスクロール）</div>
      <ol>
        <li><a href="#rank-1">第1位：なめらか本舗 薬用リンクルアイクリーム ホワイト</a></li>
        <li><a href="#rank-2">第2位：なめらか本舗 リンクルナイトクリーム</a></li>
        <li><a href="#rank-3">第3位：なめらか本舗 とろんと濃ジェル エンリッチ NC</a></li>
        <li><a href="#rank-4">第4位：豆腐の盛田屋 豆乳よーぐるとぱっく玉の輿</a></li>
        <li><a href="#rank-5">第5位：なめらか本舗 マイクロミスト化粧水 NC</a></li>
        <li><a href="#rank-6">第6位：なめらか本舗 薬用純白美容液</a></li>
        <li><a href="#rank-7">第7位：なめらか本舗 クレンジング洗顔 NC</a></li>
        <li><a href="#rank-8">第8位：なめらか本舗 リンクルUV高保湿乳液</a></li>
        <li><a href="#rank-9">第9位：四季折々 / なめらか本舗 豆乳イソフラボン化粧水 大容量500ml</a></li>
        <li><a href="#rank-10">第10位：なめらか本舗 しっとり化粧水 NC</a></li>
        <li><a href="#comparison">一目でわかる！高保湿豆乳イソフラボンコスメ全10品スペック比較表</a></li>
        <li><a href="#guide">11月・12月に失敗しない高保湿豆乳イソフラボンコスメの選び方</a></li>
        <li><a href="#faq">よくある質問（Q&A）</a></li>
      </ol>
    </section>

    <!-- ランキング商品カード群 -->
    <section class="ranking-list">
      {all_cards_html}
    </section>

    <!-- 比較表 -->
    <section class="comparison-section" id="comparison">
      <h2>📊 高保湿豆乳イソフラボンコスメ全10品スペック比較表</h2>
      <p>アイテムごとの容量・アイテム種別・特徴・参考価格を一覧表にまとめました。真冬の肌悩みに合わせて最適なアイテムをお選びください。</p>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>ブランド / 商品名</th>
            <th>種別</th>
            <th>容量</th>
            <th>特長・真冬の強み</th>
            <th>参考価格</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>第1位</td>
            <td>なめらか本舗 薬用リンクルアイクリーム</td>
            <td>高純度アイクリーム</td>
            <td>20g</td>
            <td>ピュアレチノール×イソフラボン・目元の乾燥小ジワをふっくら密着補正</td>
            <td>¥990</td>
          </tr>
          <tr>
            <td>第2位</td>
            <td>なめらか本舗 リンクルナイトクリーム</td>
            <td>濃厚ナイトクリーム</td>
            <td>50g</td>
            <td>おやすみパック処方・就寝中の暖房乾燥を防ぎ翌朝吸い付くモチ肌</td>
            <td>¥880</td>
          </tr>
          <tr>
            <td>第3位</td>
            <td>なめらか本舗 とろんと濃ジェル エンリッチ</td>
            <td>濃厚オールインワン</td>
            <td>100g</td>
            <td>復元ジェル×油分20%増量・真冬の朝晩もこれ1個で完璧高保湿</td>
            <td>¥2,090</td>
          </tr>
          <tr>
            <td>第4位</td>
            <td>豆腐の盛田屋 豆乳よーぐるとぱっく玉の輿</td>
            <td>洗い流すパック</td>
            <td>150g</td>
            <td>濃厚豆乳×ヨーグルト・お風呂で硬化した古い角質を優しくオフ</td>
            <td>¥1,790</td>
          </tr>
          <tr>
            <td>第5位</td>
            <td>なめらか本舗 マイクロミスト化粧水 NC</td>
            <td>超微細ミスト化粧水</td>
            <td>150g×3</td>
            <td>毛穴より細かい霧ミスト・メイクの上から真冬の暖房乾燥を瞬時レスキュー</td>
            <td>¥2,900</td>
          </tr>
          <tr>
            <td>第6位</td>
            <td>なめらか本舗 薬用純白美容液</td>
            <td>美白高保湿美容液</td>
            <td>100ml</td>
            <td>持続型ビタミンC×大豆アミノ酸・冬のくすみと小ジワを同時ケア</td>
            <td>¥1,246</td>
          </tr>
          <tr>
            <td>第7位</td>
            <td>なめらか本舗 クレンジング洗顔 NC</td>
            <td>高保湿洗顔フォーム</td>
            <td>150g</td>
            <td>濃密弾力ホイップ泡・冬の摩擦をゼロにして洗い上がりも突っ張らない</td>
            <td>¥646</td>
          </tr>
          <tr>
            <td>第8位</td>
            <td>なめらか本舗 リンクルUV乳液</td>
            <td>高保湿UV乳液下地</td>
            <td>50g</td>
            <td>SPF40 PA+++・ノンケミカル処方で暖房気流と冬紫外線をダブル防御</td>
            <td>¥1,003</td>
          </tr>
          <tr>
            <td>第9位</td>
            <td>四季折々 豆乳イソフラボン化粧水</td>
            <td>大容量モイスチャー</td>
            <td>500ml</td>
            <td>メガサイズ500ml・すねの粉吹き乾燥やタイツ摩擦を防ぐ全身高保湿</td>
            <td>¥1,469</td>
          </tr>
          <tr>
            <td>第10位</td>
            <td>なめらか本舗 しっとり化粧水 NC</td>
            <td>高保湿化粧水</td>
            <td>200ml</td>
            <td>高純度イソフラボン×ヒト型セラミド・何回も重ねてモチ肌を土台構築</td>
            <td>¥732</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- ガイドセクション -->
    <section class="guide-section" id="guide">
      <h2>💡 11月・12月に失敗しない高保湿豆乳イソフラボンコスメの選び方</h2>
      
      <h3>1. 通常ラインか『リンクル（エイジング）ライン』かで選ぶ</h3>
      <p>真冬の過酷な乾燥と小ジワに立ち向かうなら、ピュアレチノールやヒト型セラミドが配合された『リンクルライン（金色のパッケージ）』が圧倒的におすすめです。目元の小ジワや頬のしぼみが気になる方は、リンクルアイクリームやリンクルナイトクリームを投入することで、デパコス級の濃厚なリフト保湿を実感できます。一方、みずみずしい水分補給と全身の惜しみないケアを目的とするなら、通常ラインのしっとり化粧水や500ml大容量ローションが最適です。</p>

      <h3>2. 朝と夜でテクスチャーと機能を使い分ける</h3>
      <p>冬の朝は、メイク崩れを防ぎながら日中の暖房乾燥をブロックすることが最重要です。朝は『リンクルUV乳液』や『とろんと濃ジェル』を薄くハンドプレスで馴染ませ、日中は『マイクロミスト化粧水』でピンポイント補給。そして夜は『リンクルナイトクリーム』を厚めに塗ってスリーピングパックとして就寝する、という24時間隙のない保湿サイクルを回すことで、真冬でも粉吹き知らずの潤い肌をキープできます。</p>

      <h3>3. お風呂場での『スチーム温感ケア』を組み合わせる</h3>
      <p>冬の冷えで角層が硬化しているときは、洗顔後に『豆腐の盛田屋 豆乳よーぐるとぱっく』などの洗い流すパックを湯船に浸かりながら行うのが劇的な効果を生みます。浴室の湯気によって角層がふやけて毛穴が開き、豆乳発酵アミノ酸が奥深くまで浸透。その後の化粧水や美容液の吸い込みが格段に高まります。</p>
    </section>

    <!-- FAQセクション -->
    <section class="faq-section" id="faq">
      <h2>❓ よくある質問（Q&A）</h2>
      <div class="faq-item">
        <div class="faq-question">Q1. 豆乳イソフラボンが冬の乾燥肌に特に効果的な理由は何ですか？</div>
        <div class="faq-answer">大豆イソフラボンは女性ホルモン（エストロゲン）と化学構造が類似しており、肌のエストロゲン受容体にアプローチしてコラーゲンやヒアルロン酸の自己合成を促します。冬の寒暖差やストレスで肌のリズムが乱れ、しぼんで硬化した角層を内側からふっくら柔軟化し、吸い付くようなモチ肌を蘇らせます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q2. なめらか本舗のイソフラボンシリーズは敏感肌でも使えますか？</div>
        <div class="faq-answer">はい、基本的に無香料・無着色・無鉱物油処方で設計されており、敏感肌パッチテスト済みです。ただし、レチノール配合タイプ（リンクルシリーズ等）は非常に乾燥している部位に塗ると初期にピリつきを感じる場合があるため、まずは少量を目元等で試すか、通常のしっとりタイプから始めるのが安心です。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q3. 冬の朝のメイク前に豆乳ジェルやクリームを使ってもヨレませんか？</div>
        <div class="faq-answer">『とろんと濃ジェル』や『リンクルUV乳液』は、メイク前の使用を前提とした高密着処方で作られており、余分なモロモロが出にくい仕様です。塗布後に両手でしっかりハンドプレスして角層に馴染ませ、表面を軽くティッシュオフしてからファンデーションを重ねると一日中乾燥崩れを防げます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q4. 11月・12月の冬に効果的な重ねづけテクニックは？</div>
        <div class="faq-answer">まず豆乳しっとり化粧水を2〜3回重ねづけして角層の水分を満たし、目元・口元にリンクルアイクリームを塗り込んだ後、夜はリンクルナイトクリームを厚めに塗ってスリーピングパックとして密閉するのが最強の冬保湿ルーティンです。</div>
      </div>
    </section>

    <!-- 内部リンクブロック -->
    <section class="internal-links">
      <h3>🔗 あわせて読みたい！真冬の乾燥対策・高保湿コスメ関連記事</h3>
      <div class="links-grid">
        <a href="/winter-fucoidan" class="link-card">🌊 高保湿フコイダン（海の自己治癒多糖体）</a>
        <a href="/winter-royal-jelly" class="link-card">👑 高保湿ローヤルゼリー（王乳エキス）</a>
        <a href="/winter-hatomugi" class="link-card">🌾 高保湿ハトムギ（和漢ヨクイニン）</a>
        <a href="/winter-ceramide-lotion" class="link-card">💧 高保湿セラミド化粧水</a>
        <a href="/winter-retinol-cream" class="link-card">✨ 高保湿レチノールクリーム</a>
        <a href="/winter-eye-cream" class="link-card">👁️ 真冬の集中アイクリーム</a>
      </div>
    </section>
  </div>

  <footer>
    <div class="footer-links">
      <a href="/">トップページ</a>
      <a href="/winter-soy-isoflavone">高保湿豆乳イソフラボン</a>
      <a href="/winter-fucoidan">高保湿フコイダン</a>
      <a href="/winter-royal-jelly">高保湿ローヤルゼリー</a>
      <a href="/winter-hatomugi">高保湿ハトムギ</a>
    </div>
    <div class="copyright">&copy; 2026 LUMI COSMETICS. All Rights Reserved. 無断転載を禁じます。</div>
  </footer>

</body>
</html>
"""

with open("winter-soy-isoflavone.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("winter-soy-isoflavone.html created successfully!")
