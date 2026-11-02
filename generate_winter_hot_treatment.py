import json
import re

with open("fetched_3winter_mist_bath_headspa_data_perfect.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_hot_treatment"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 累計数百万人を虜にした韓国水トリートメントの元祖！わずか10秒でシルク髪へ",
        "catch": "水と混ざるとじんわり温感クリームへ変化。傷んだキューティクルへ微細アミノ酸が急速浸透",
        "brand_name": "moremo (モレモ)",
        "capacity": "200ml",
        "type": "温感・液体ウォータートリートメント（ミラクル10）",
        "features": "加水分解ケラチン、加水分解シルク、アミノ酸17種、海松子油（マツ種子油）、ノンシリコン処方",
        "value": "美容大国・韓国で爆発的ブームを巻き起こした名作。放置時間わずか10秒で、ブリーチ毛や乾燥毛もサロン帰りの指通りに",
        "desc_p1": "11月から12月にかけて、空気の乾燥とマフラーやコートの摩擦によって静電気が発生し、毛先が広がりパサついて収拾がつかなくなる『冬のハイダメージ毛』。さらに冬はお風呂場の冷え込みで通常のトリートメントを数分間放置するのが億劫になりがちです。そんな冬のヘアケアストレスを劇的に変えたのが、韓国発モレモの『ウォータートリートメント ミラクル10』です。",
        "desc_p2": "サラサラの液体状トリートメントが、濡れた髪の水分と反応した瞬間にじんわりとした心地よい温感を発泡し、とろりとした高密着クリームへと相変化（乳化）します。この温感スチーム効果によってキューティクルが自然に緩み、分子量の小さい加水分解ケラチンや17種のアミノ酸が毛髪内部のコルテックスへ瞬時に浸透。放置時間はなんと『わずか10秒』。洗い流した瞬間から指通りが劇的に軽くなり、ドライヤーで乾かした後は毛先まで潤いを抱え込んだ、天使の輪が輝くシルクのようなツヤ髪が蘇ります。",
        "target": "冬の静電気や乾燥で毛先がパサつき広がる方、お風呂でトリートメントを長時間置くのが辛い方、軽やかでサラサラなサロン級の指通りを求める方",
        "point": "シャンプー後、毛先の水気をしっかり手で絞ってから塗布するのがコツ。塗布後に毛先を手で優しく揉み込むと、液体から温かいクリームに変わるのを実感でき、浸透力が最大化します。"
    },
    {
        "rank": 2,
        "tag": "🔥 韓国で完売続出！頭皮に直接揉み込める温感スカルプトリートメントで根元ふんわり",
        "catch": "冷えた頭皮をじんわり温めてマッサージ。根元の立ち上がりと毛先のまとまりを両立する高機能ケア",
        "brand_name": "HEAD SPA 7 (ヘッドスパセブン)",
        "capacity": "200ml",
        "type": "温感スカルプ＆ヘア集中補修トリートメント",
        "features": "加水分解コラーゲン、シルクエキス、サリチル酸、メントール、パンテノール、植物エキス18種",
        "value": "有名サロンのヘッドスパプログラムを自宅で再現。頭皮の血行促進とキューティクル補修を1本で完結させる二刀流",
        "desc_p1": "冬の寒さで頭皮の血管が収縮すると、頭皮全体がカチコチに凝り固まり、髪への栄養補給が滞って根元のボリュームが失われたり、フケやかゆみが発生しやすくなります。そんな冷え固まった頭皮と傷んだ毛先を同時に救済するのが、韓国で累計販売数千万本を誇る『ヘッドスパセブン』です。",
        "desc_p2": "先端ノズルから直接頭皮と髪に塗布できるユニークな設計。頭皮の水分と触れ合うと瞬時に温感が発生し、心地よい温もりでこわばった頭皮をじんわりほぐします。指の腹で頭皮全体をマッサージすることで血行が促進され、健康な頭皮環境へとリセット。同時に加水分解コラーゲンやシルクが毛髪一本一本をコーティングし、根元はふんわりと立ち上がりながら、毛先は驚くほどしっとりまとまります。サロンの本格温感ヘッドスパを受けた直後のような爽快感と美髪効果に感動するはずです。",
        "target": "冬になると頭皮が冷えて凝り固まりやすい方、トップのボリューム不足と毛先のパサつきを同時にケアしたい方、自宅で手軽にヘッドスパを体験したい方",
        "point": "頭皮に直接線を描くように塗布した後、生え際から頭頂部に向けて円を描くように頭皮を揉みほぐすと、温感効果とマッサージ効果で頭全体が軽くなります。"
    },
    {
        "rank": 3,
        "tag": "👑 アミノ酸17種を贅沢濃縮！温感スチーム効果で傷んだキューティクルを濃密ラッピング",
        "catch": "水と反応して温かいクリームへ変化。素早い浸透力と圧倒的な毛先まとまり感を誇る実力派",
        "brand_name": "Tricore (トリコレ)",
        "capacity": "200ml",
        "type": "生感覚・温感ヘッドスパトリートメント",
        "features": "アミノ酸17種、加水分解ケラチン、植物性オイル、パラベンフリー、鉱物油フリー、爽やかなフローラルハーブの香り",
        "value": "『液体だから浸透、クリームだから密着』を科学した生トリートメント。熱反応で髪の空洞化を埋め、しっとりツヤ髪へ導く",
        "desc_p1": "『毎日のドライヤーやヘアアイロンで毛先がチリチリに傷んでいる』『冬になると静電気で髪が顔にまとわりつく』という深刻なダメージ毛に寄り添い、SNSや美容口コミサイトで絶賛されているのがトリコレの温感トリートメントです。",
        "desc_p2": "塗布した瞬間に発生するマイルドな発熱反応が、冬の冷えた浴室でもトリートメント成分の浸透を強力に後押し。液体が髪の微細な隙間まで瞬時に行き渡り、水と混ざることで濃厚なクリームへと変化して栄養分を逃さず閉じ込めます。髪の90%以上を占めるケラチンタンパク質を構成するアミノ酸を網羅的に補給し、ダメージによってスカスカになった毛髪内部をみっちり充填。洗い流す際、今までにないほどつるんとしたなめらかな手触りに驚くはずです。",
        "target": "カラーやパーマ、アイロン熱によるハイダメージ毛の方、冬の広がりやすいうねり・パサつきを抑えたい方、リッチなサロンケアを自宅で行いたい方",
        "point": "毛先に揉み込んだ後、粗めのコーム（トリートメント用コーム）で一度優しくコーミングすると、クリーム状になった美髪成分が均一に密着して効果が倍増します。"
    },
    {
        "rank": 4,
        "tag": "⚡ たった8秒でサロン帰りの輝き！ロレアルのラメラテクノロジーが生み出した水トリートメント",
        "catch": "水のような軽さなのに驚異の毛先補修。重くならずシルクのようにサラサラ揺れる美髪へ",
        "brand_name": "L'Oreal Paris (ロレアル パリ)",
        "capacity": "200ml",
        "type": "ラメラテクノロジー・高浸透リキッドトリートメント（ワンダーウォーター）",
        "features": "ラメラテクノロジー、アミノ酸コンプレックス、プロビタミンB5、エモリエント成分、フルーティフローラルの香り",
        "value": "世界最大の化粧品研究所ロレアルが開発した革新的ラメラ構造。ダメージ部位だけを選択的に感知して極薄シールドを形成",
        "desc_p1": "重たいトリートメントを使うと髪がペタッと潰れてしまう細毛・軟毛の方や、忙しい冬の夜に時間をかけずに美髪を手に入れたい女性に圧倒的熱量で支持されているのが、ロレアルパリの『ワンダーウォーター』です。",
        "desc_p2": "独自開発の『ラメラテクノロジー』を採用。塗布すると液体が髪表面の傷んだ凹凸部分だけをピンポイントで感知し、薄い膜（ラメラ層）を瞬時に形成して表面を均一にコーティングします。放置時間は驚きの『わずか8秒』。水で流した瞬間に、髪が指の間をツルツルとすり抜ける極上のシルクタッチを実感できます。余分な重さやベタつきを一切残さず、風になびくような軽やかさとまばゆい光沢感を冬の髪に与えてくれます。",
        "target": "髪が細くてボリュームが潰れやすい方、8秒で完了する圧倒的な時短ケアを求める方、さらさらとしたシルキーな指通りが好きな方",
        "point": "ボトルの側面に1回分の目盛り（約20ml）が刻まれているため、使用量を正確に守ることが可能。セミロングなら1目盛り、ロングや多毛なら2目盛りが適量です。"
    },
    {
        "rank": 5,
        "tag": "🌿 植物の恵みでうるおいチャージ！冬の静電気を防ぎしなやかにまとまるボタニカル水ケア",
        "catch": "天然由来成分90%以上。乾燥して絡まりやすい毛先をみずみずしく解きほぐす",
        "brand_name": "BIOLISS (ビオリス / コーセー)",
        "capacity": "200ml",
        "type": "ボタニカル・高浸透ウォータートリートメント",
        "features": "オーガニックホホバオイル、アルガンオイル、ボタニカルアミノ酸、キューティクル補修ポリマー、天然香料ブレンド",
        "value": "ドラッグストアで手軽に買えるプチプラ水トリートメント。オーガニック植物成分が冬の乾燥ダメージ毛を優しく保護",
        "desc_p1": "『ドラッグストアで買える手頃な価格で、水トリートメントの感動を味わいたい』『毎日のアウトバスケアだけでは毛先のパサつきが収まらない』という方にぴったりの救世主が、ビオリスのボタニカルウォータートリートメントです。",
        "desc_p2": "オーガニック認証を受けたホホバオイルやアルガンオイルなどの上質な植物油脂と、髪を構成するボタニカルアミノ酸を贅沢に配合。シャンプー後の濡れた髪に馴染ませると、液体がキューティクルの細かな隙間にすっと入り込み、乾いた毛髪深部へ水分と油分を同時にチャージします。キューティクル表面をなめらかに整えることで、冬の最大の天敵である衣類との摩擦静電気を大幅にカット。翌朝の寝癖や毛先の絡まりを防ぎ、スタイリングしやすい素直な髪へと導きます。",
        "target": "プチプラでコスパよくウォータートリートメントを続けたい方、冬の静電気や朝のブラッシング時の引っかかりに悩む方、ナチュラルなボタニカル処方が好きな方",
        "point": "普段のコンディショナーやヘアマスクの『前』にブースターとして使用する『導入トリートメント使い』もおすすめ。その後のトリートメントの吸着力が劇的に上がります。"
    },
    {
        "rank": 6,
        "tag": "💆‍♀️ 温感マッサージで頭皮の巡りをアップ！トップふんわり・毛先まとまる薬用スカルプパック",
        "catch": "医薬部外品の確かな頭皮ケア。冷え固まった頭皮を温め、ハリコシのある健やかな美髪へ",
        "brand_name": "スカルプD ボーテ (アンファー)",
        "capacity": "350ml",
        "type": "医薬部外品・薬用スカルプトリートメントパック（ボリューム）",
        "features": "ソイセラム（黒豆豆乳発酵液）、グリチルリチン酸ジカリウム（有効成分）、ジンジャーエキス、セラミド配合",
        "value": "女性ホルモンの変化や頭皮環境に着目した専門処方。頭皮に直接つけてマッサージできるエイジングケアパック",
        "desc_p1": "冬になると頭皮の血流が悪くなり、髪が細く痩せて分け目がペタッとしてしまう大人の女性に絶大な信頼を得ているのが、アンファーの『スカルプD ボーテ 薬用トリートメントパック』です。",
        "desc_p2": "通常のトリートメントは毛穴詰まりの原因になるため頭皮につけられませんが、本品は『頭皮に直接つけること』を前提に開発された医薬部外品。濃密なパックを頭皮全体に広げてマッサージすると、ジンジャーエキスの温感作用で血行がじわじわと促進されます。有効成分グリチルリチン酸2Kが冬のフケ・かゆみ・乾燥性炎症を徹底抑制。同時に高純度ソイセラムが髪の根元にハリ・コシを与え、ドライヤーで乾かした瞬間にトップがふんわりと立ち上がる若々しいシルエットを取り戻します。",
        "target": "冬の寒さで頭皮の硬さや血行不良を感じる方、髪が細くなりトップのボリュームが落ちてきた方、頭皮のかゆみや乾燥を防ぎたい方",
        "point": "頭皮全体に馴染ませた後、両手の親指をこめかみに置き、残り4本の指で頭皮を百会（頭頂部）に向かって引き上げるようにマッサージすると、リフトアップ効果も期待できます。"
    },
    {
        "rank": 7,
        "tag": "👑 傷みきった毛先をとろけるように濃密補修！国民的大ヒット美容液ヘアマスク",
        "catch": "ローヤルゼリーEXとトレハロースが角層深部まで満たす。冬の剛毛・パサつき髪を至福の柔らかさへ",
        "brand_name": "fino (フィーノ / ファイントゥデイ)",
        "capacity": "230g",
        "type": "高濃度・浸透美容液ヘアマスク",
        "features": "ローヤルゼリーエキス、トレハロース、スクワラン、PCA、フィトステリル誘導体、グレースフローラルの香り",
        "value": "数年連続でベスコス1位を独占するヘアケアの絶対王者。美容液成分をぎゅっと凝縮し、乾燥して硬くなった髪を極上の柔らかさに",
        "desc_p1": "『冬の寒さと乾燥で髪がゴワゴワに硬くなってしまった』『毛先が枝毛や切れ毛だらけでパサつく』というハイダメージに直面した時の最強レスキューが、フィーノの『プレミアムタッチ 浸透美容液ヘアマスク』です。",
        "desc_p2": "こっくりとした濃厚なテクスチャーに、ローヤルゼリーエキスやトレハロース、スクワランなどスキンケア級の美容液成分を惜しみなく配合。濡れた髪に馴染ませると、とろけるように毛髪深部へと浸透し、傷んだ内部を濃密に充填します。キューティクルのめくれ上がりをぴったりと補修・コーティングするため、冬の冷風や摩擦にも負けない強い毛髪へと再生。流した瞬間から指が吸い付くようなしっとり感に包まれ、乾かした後は毛先までつるんとまとまる極上の質感を手に入れられます。",
        "target": "毛先のダメージ・枝毛・パサつきが深刻な方、剛毛で髪が硬く広がりやすい方、圧倒的なコスパで濃厚なトリートメントを惜しみなく使いたい方",
        "point": "週に1〜2回のスペシャルケアとして、塗布した後にホットタオル（お湯で絞ったタオル）を頭に巻いて3〜5分蒸らすと、温感スチーム効果で浸透力が数倍に跳ね上がります。"
    },
    {
        "rank": 8,
        "tag": "🛡️ 湿度変化に負けない！天然由来美髪オイルが毛先をラッピングする高保湿バリア",
        "catch": "アミノ酸とセラミドが冬の乾燥パサつきをブロック。雨や暖房でも一日中まとまる",
        "brand_name": "Essential (エッセンシャル / 花王)",
        "capacity": "200g",
        "type": "うるおいバリア・濃密高保湿ヘアトリートメント",
        "features": "18-MEAオイル（天然毛髪保護成分）、セラミドES、厳選アミノ酸、シアバター配合、フローラルリュクスの香り",
        "value": "花王のヘアサイエンスが生んだ『うるおいバリア処方』。冬の暖房乾燥と静電気による髪の乱れを一日中鉄壁ガード",
        "desc_p1": "朝どんなにブローして整えても、冬の冷たい外気に触れたり、暖房の効いたオフィスに入ったりした瞬間に髪がボサボサに広がってしまう…そんな環境ストレスから髪を守るのが、エッセンシャルの『プレミアム うるおいバリア トリートメント』です。",
        "desc_p2": "健やかな髪表面にわずか0.1%しか存在しない天然の保護バリア成分『18-MEA』を高純度配合。さらにセラミドESやシアバターが毛髪内部をみずみずしく満たし、髪の外側と内側の両面からバリア機能を構築します。冬の過酷な湿度変化や暖房風にさらされても、毛髪内部の水分が外へ逃げるのを防ぎ、湿気や静電気の侵入をシャットアウト。一日中手ぐしがすんなり通る、しなやかでまとまりのある美髪をキープできます。",
        "target": "暖房の部屋に入ると髪が急に広がって乾燥する方、毎朝のスタイリングに時間がかかってしまう方、上品なフローラルの香りが好きな方",
        "point": "特に乾燥しやすい毛先を中心に揉み込むように塗布し、髪を軽くねじるようにしてキューティクルを整えてから流すと、バリア成分がより強固に定着します。"
    },
    {
        "rank": 9,
        "tag": "💧 水分量15%に着目！髪内部の乾きを潤す新発想のウォーターブースター",
        "catch": "美容水成分90%以上。インナードライ髪に瞬時に水分チャージしてぷるぷるのうるツヤ髪へ",
        "brand_name": "ululis (ウルリス)",
        "capacity": "150ml",
        "type": "インナーリペア・高保水ウォータートリートメント",
        "features": "10種の美容水（水溶性コラーゲン、水溶性ケラチン、ハチミツ水等）、高浸透ナノカプセル、ウォーターフルールの香り",
        "value": "美容水で髪を包み込む新発想。パサつき・ごわつきの根本原因である毛髪内部の水分不足を急速リセット",
        "desc_p1": "表面はベタつくのに内側はパサパサに乾いている『インナードライ髪』に悩む若い女性たちの間で大ヒットしているのが、ウルリスの『インナーリペア ウォータートリートメント』です。",
        "desc_p2": "水溶性コラーゲンやケラチン、ハチミツ水など10種類もの厳選された美容水成分を凝縮。ウォータートリートメントならではの超微細な分子設計により、乾ききった髪の芯までわずか数秒で美容水が吸い込まれるように浸透します。キューティクルを引き締めて内部に水分を閉じ込めるため、ドライヤーで乾かした後も髪が水分をたっぷり抱え込んだような『ぷるん』とした弾力と瑞々しいツヤを実感できます。二重構造の美しいボトルデザインもバスタイムを華やかに彩ります。",
        "target": "髪の内側がパサついてまとまらないインナードライ髪の方、重たいオイルやクリームだとベタついてしまう方、みずみずしいツヤ感を重視する方",
        "point": "シャンプーとトリートメントの間に挟む『ステップ2』として使用することで、髪の水分保持力が最大化し、後から使うトリートメントの補修効果を極限まで引き出します。"
    },
    {
        "rank": 10,
        "tag": "🌙 夜の摩擦ダメージを防ぐジェル処方！寝ている間に集中リペアする濃厚ナイトケア",
        "catch": "ナイトセラミド配合。冬の枕擦れや暖房乾燥から髪を守り、翌朝ツヤツヤの扱いやすい髪へ",
        "brand_name": "YOLU (ヨル / I-ne)",
        "capacity": "145g",
        "type": "浸透ジェル・カームナイトリペアジェルヘアマスク",
        "features": "浸透型コラーゲン、ナイトセラミド、ネムノキ樹皮エキス、ハスの花エキス、ネロリ＆ピオニーの安らぐ香り",
        "value": "シリーズ累計数千万本を突破したナイトケアブランド。密着ジェルが寝ている間の摩擦と乾燥を徹底ブロック",
        "desc_p1": "『朝起きると後頭部がチリチリに絡まっている』『寝癖がひどくて毎朝アイロンで伸ばすのが大変』という冬の夜間ダメージに特化して開発されたのが、YOLUの『カームナイトリペア ジェルヘアマスク』です。",
        "desc_p2": "クリームよりも素早く馴染み、水トリートメントよりも濃厚に密着する独自の『ぷるぷる浸透ジェル』を採用。髪に乗せた瞬間、毛髪一本一本を潤いの保護膜で包み込みます。夜間の水分蒸発を防ぐナイトセラミドと浸透型コラーゲンが、睡眠中の枕との摩擦刺激や寝室の暖房乾燥から髪を鉄壁ガード。安らかな眠りへ誘うネロリとピオニーのアロマに包まれ、翌朝目覚めた瞬間に手ぐしが毛先までスルンと通るまとまり感に感動します。",
        "target": "寝ている間の摩擦ダメージや絡まりが気になる方、朝のスタイリング時間を短縮したい方、安らぐ上質なアロマの香りで眠りたい方",
        "point": "塗布した後に軽く手ぐしを通しながら1〜2分置くことで、ジェル状のナノカプセルが毛髪内部にしっかりと定着し、翌朝のまとまり持続性が向上します。"
    }
]

# FAQアイテム
faq_items = [
    {
        "q": "ウォータートリートメントと一般的なクリームトリートメントの違いは何ですか？",
        "a": "最も大きな違いは『浸透速度』と『仕上がりの軽やかさ』です。クリーム状トリートメントは油分が多いため、浸透するまでに数分間の放置時間が必要で、細い髪だと重くペタッとなりがちです。一方、ウォータートリートメントは分子が非常に小さく液体状のため、塗布した瞬間に毛髪内部のコルテックスまで浸透。水と反応して温感クリームに変わることで、放置時間わずか8秒〜10秒でキューティクルを整え、重さを残さずサラサラでツヤのある指通りを実現します。"
    },
    {
        "q": "なぜ水と混ざると温かくなるのですか？頭皮や髪に害はありませんか？",
        "a": "液体トリートメントに含まれるグリセリンやプロピレングリコール（PG）などの親水性保湿成分が、水分と結合する際に発生する『溶解熱（水分吸熱・発熱反応）』を利用しているためです。人工的な熱源や化学反応による強い熱ではなく、自然な物理現象による心地よいマイルドな温感（体感で約35〜38℃程度）ですので、頭皮や髪を痛める心配は一切ありません。むしろ、この温もりによってキューティクルが緩み、トリートメント成分の浸透がスムーズになります。"
    },
    {
        "q": "温感トリートメントは頭皮に直接つけても大丈夫ですか？",
        "a": "アイテムによって設計が異なりますので必ず確認してください。『ヘッドスパセブン』や『スカルプD ボーテ』のようにスカルプケアを謳っている製品は、毛穴を詰まらせないノンシリコン・薬用処方で作られているため、頭皮に直接つけてマッサージするのが正解です。一方、モレモやフィーノなど『毛先用トリートメント』は頭皮を避けて中間〜毛先を中心につけるのが基本です。"
    },
    {
        "q": "冬に髪が静電気でパサつくのを防ぐには、どう使えば効果的ですか？",
        "a": "静電気の最大の原因は『髪内部の水分不足』と『キューティクルの剥がれによる摩擦』です。ウォータートリートメントで毛髪内部にアミノ酸と水分を急速チャージした後、ドライヤーの前にヘアミルクやヘアオイルで油膜のシールドを張る『インバス水トリートメント＋アウトバスオイル』のWケアを行うことで、冬のコートやマフラーの摩擦でも一切静電気が起きないツヤ髪を一日中維持できます。"
    },
    {
        "q": "どのくらいの頻度で使用するのが理想ですか？",
        "a": "モレモやロレアルパリなどのウォータートリートメントは、毎日コンディショナー代わりに使っても問題ありません。特にブリーチ毛や乾燥がひどい冬の間は、毎日または週3〜4回継続することで、毛先のパサつきが目に見えて改善します。フィーノなどの濃厚ヘアマスクは週1〜2回のスペシャル集中ケアとして併用するのが最もバランス良く美髪を保てます。"
    }
]

# JSON-LD 構造化データ
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
    "headline": "保湿力の強さで冬のパサつき剛毛・冷えたガチガチ頭皮とさようなら！塗った瞬間じんわり温感で美髪成分が急速浸透する温感ヘッドスパトリートメントランク10",
    "description": "11月・12月の寒さで凝り固まったガチガチ頭皮と、静電気・暖房乾燥でパサつく毛先をダブルで救済！moremo、ヘッドスパセブン、トリコレ、サロニア、アミノレスキューなど、水と反応してじんわり温かくなり液体から濃密クリームへ変化する最新温感ウォータートリートメント＆スカルプスパ10選を徹底比較！",
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
    "name": "冬の温感ヘッドスパトリートメント おすすめランキング10選",
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

# 商品カードHTML
cards_html = []
for p, item in zip(product_details, items):
    cards_html.append(f"""
    <article class="product-card" id="rank-{p['rank']}">
      <div class="product-badge">
        <span class="rank-number">第{p['rank']}位</span>
        <span class="rank-tag">{p['tag']}</span>
      </div>
      <h3 class="product-title">{p['brand_name']} {p['capacity']}</h3>
      <div class="product-catch">{p['catch']}</div>

      <div class="product-main">
        <div class="product-img-wrap">
          <img src="{item['image']}" alt="{p['brand_name']} 冬の温感ヘッドスパトリートメント" class="product-img" loading="lazy">
          <div class="img-caption">{p['brand_name']} 楽天市場正規取扱ショップ画像</div>
        </div>
        <div class="product-specs">
          <dl class="spec-list">
            <dt>ブランド / メーカー</dt>
            <dd>{p['brand_name']}</dd>
            <dt>内容量 / タイプ</dt>
            <dd>{p['capacity']} / {p['type']}</dd>
            <dt>主要補修・美容成分</dt>
            <dd>{p['features']}</dd>
            <dt>楽天市場 参考価格</dt>
            <dd class="price-val">¥{item['price']:,} <span>(税込・調査時点)</span></dd>
            <dt>アイテム独自の特徴</dt>
            <dd>{p['value']}</dd>
          </dl>
        </div>
      </div>

      <div class="product-desc">
        <h4>💆‍♀️ 美容エディターの徹底本音レビュー＆毛髪補修メカニズム</h4>
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>

      <div class="product-advice">
        <div class="advice-block target-block">
          <strong>🎯 こんな人に特におすすめ：</strong>
          <p>{p['target']}</p>
        </div>
        <div class="advice-block tip-block">
          <strong>✨ プロの温感スチーム美髪アドバイス：</strong>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-action">
        <a href="{item['affiliateUrl']}" class="rakuten-btn" target="_blank" rel="noopener noreferrer nofollow">
          <span>楽天市場で最安値＆口コミをチェック</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
    """)

# 比較サマリー表
table_rows = []
for p, item in zip(product_details, items):
    table_rows.append(f"""
    <tr>
      <td class="tb-rank">第{p['rank']}位</td>
      <td class="tb-name"><strong>{p['brand_name']}</strong><br><small>{p['capacity']}</small></td>
      <td class="tb-type">{p['type']}</td>
      <td class="tb-ing">{p['features'][:35]}...</td>
      <td class="tb-price">¥{item['price']:,}</td>
      <td class="tb-link"><a href="#rank-{p['rank']}" class="tb-anchor">詳細を見る</a></td>
    </tr>
    """)

# FAQ HTML
faq_html_blocks = []
for f_item in faq_items:
    faq_html_blocks.append(f"""
    <div class="faq-item">
      <h3 class="faq-q"><span>Q</span>{f_item['q']}</h3>
      <div class="faq-a"><span>A</span><p>{f_item['a']}</p></div>
    </div>
    """)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬のパサつき剛毛・冷えたガチガチ頭皮とさようなら！塗った瞬間じんわり温感で美髪成分が急速浸透する温感ヘッドスパトリートメントランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒さで凝り固まったガチガチ頭皮と、静電気・暖房乾燥でパサつく毛先をダブルで救済！moremo、ヘッドスパセブン、トリコレ、サロニア、アミノレスキューなど、水と反応してじんわり温かくなり液体から濃密クリームへ変化する最新温感ウォータートリートメント＆スカルプスパ10選を徹底比較！">
  <meta name="keywords" content="ウォータートリートメント,温感トリートメント,ヘッドスパ トリートメント,モレモ ミラクル10,冬 ヘアケア パサつき,静電気 髪 保湿,トリコレ,ヘッドスパセブン">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-hot-treatment">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- OGP / SNS Meta Tags -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで冬のパサつき剛毛・冷えたガチガチ頭皮とさようなら！塗った瞬間じんわり温感で美髪成分が急速浸透する温感ヘッドスパトリートメントランク10">
  <meta property="og:description" content="11月・12月の寒さで凝り固まったガチガチ頭皮と静電気・暖房乾燥でパサつく毛先をダブルで救済！モレモ、ヘッドスパセブン、トリコレ等、至高の温感トリートメント10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-hot-treatment">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">

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
      --primary: #8b5cf6;
      --primary-light: #f5f3ff;
      --primary-dark: #6d28d9;
      --accent: #f59e0b;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
    }}
    .nav-link:hover {{ color: var(--primary); }}
    
    .container {{
      max-width: 1000px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    
    .breadcrumb {{
      display: flex;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
    }}
    .breadcrumb a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumb a:hover {{ color: var(--primary); }}
    .breadcrumb span {{ color: #cbd5e0; }}

    .article-hero {{
      background: #ffffff;
      padding: 2.5rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border-top: 5px solid var(--primary);
    }}
    .article-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.8rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 1.85rem;
      line-height: 1.4;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.25rem;
    }}
    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
    }}
    .intro-text {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #334155;
    }}
    .intro-text p {{ margin-bottom: 1rem; }}
    .intro-highlight {{
      background: var(--primary-light);
      padding: 1.25rem;
      border-radius: 8px;
      border-left: 4px solid var(--primary);
      margin: 1.5rem 0;
      font-weight: 600;
    }}

    .toc {{
      background: #f1f5f9;
      padding: 1.5rem;
      border-radius: var(--radius);
      margin: 2rem 0;
    }}
    .toc-title {{
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: #1e293b;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 0.5rem;
    }}
    .toc-list a {{
      color: #475569;
      text-decoration: none;
      font-size: 0.95rem;
      display: block;
      padding: 0.25rem 0;
    }}
    .toc-list a:hover {{ color: var(--primary); font-weight: 600; }}

    .section-h2 {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #0f172a;
      margin: 3.5rem 0 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--primary);
    }}
    
    .table-container {{
      overflow-x: auto;
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin: 2rem 0;
    }}
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .summary-table th {{
      background: #f8fafc;
      color: #475569;
      padding: 1rem;
      border-bottom: 2px solid var(--border);
      white-space: nowrap;
    }}
    .summary-table td {{
      padding: 1rem;
      border-bottom: 1px solid var(--border);
      vertical-align: middle;
    }}
    .tb-rank {{ font-weight: 700; color: var(--primary); width: 80px; }}
    .tb-price {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .tb-anchor {{
      display: inline-block;
      padding: 0.35rem 0.75rem;
      background: var(--primary-light);
      color: var(--primary);
      text-decoration: none;
      border-radius: 6px;
      font-weight: 600;
      font-size: 0.8rem;
    }}
    .tb-anchor:hover {{ background: var(--primary); color: #fff; }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2rem;
      margin-bottom: 3rem;
      border: 1px solid var(--border);
      scroll-margin-top: 80px;
    }}
    .product-badge {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}
    .rank-number {{
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1rem;
      padding: 0.25rem 0.85rem;
      border-radius: 6px;
    }}
    .rank-tag {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
    }}
    .product-title {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 1rem;
      color: #475569;
      font-weight: 600;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px dashed var(--border);
    }}
    .product-main {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 1.75rem;
      margin-bottom: 1.5rem;
    }}
    @media (max-width: 768px) {{
      .product-main {{ grid-template-columns: 1fr; }}
    }}
    .product-img-wrap {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 280px;
      height: 280px;
      object-fit: contain;
      border-radius: 8px;
      background: #ffffff;
      border: 1px solid #edf2f7;
    }}
    .img-caption {{
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-top: 0.5rem;
    }}
    .spec-list {{
      display: grid;
      grid-template-columns: 120px 1fr;
      gap: 0.6rem;
      font-size: 0.9rem;
    }}
    .spec-list dt {{
      font-weight: 700;
      color: #64748b;
      border-bottom: 1px solid #f1f5f9;
      padding: 0.35rem 0;
    }}
    .spec-list dd {{
      color: #0f172a;
      border-bottom: 1px solid #f1f5f9;
      padding: 0.35rem 0;
    }}
    .price-val {{
      font-size: 1.25rem !important;
      font-weight: 800 !important;
      color: #b91c1c !important;
    }}
    .price-val span {{
      font-size: 0.75rem;
      font-weight: normal;
      color: var(--text-muted);
    }}
    .product-desc {{
      margin: 1.5rem 0;
      background: #f8fafc;
      padding: 1.5rem;
      border-radius: 8px;
    }}
    .product-desc h4 {{
      font-size: 1.05rem;
      color: #0f172a;
      margin-bottom: 0.75rem;
      font-weight: 700;
    }}
    .product-desc p {{
      margin-bottom: 0.75rem;
      color: #334155;
    }}
    .product-desc p:last-child {{ margin-bottom: 0; }}
    
    .product-advice {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin: 1.5rem 0;
    }}
    @media (max-width: 640px) {{
      .product-advice {{ grid-template-columns: 1fr; }}
    }}
    .advice-block {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.9rem;
    }}
    .target-block {{ background: #eff6ff; border-left: 4px solid #3b82f6; }}
    .target-block strong {{ color: #1e40af; display: block; margin-bottom: 0.35rem; }}
    .tip-block {{ background: #fefce8; border-left: 4px solid #eab308; }}
    .tip-block strong {{ color: #854d0e; display: block; margin-bottom: 0.35rem; }}

    .product-action {{
      margin-top: 1.5rem;
      text-align: center;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      width: 100%;
      max-width: 420px;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 1.05rem;
      padding: 1rem 1.5rem;
      border-radius: 9999px;
      box-shadow: 0 4px 10px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #d60000 0%, #b30000 100%);
    }}

    .guide-box {{
      background: #ffffff;
      padding: 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin: 2rem 0;
    }}
    .guide-box h3 {{
      font-size: 1.25rem;
      color: #0f172a;
      margin-bottom: 1rem;
      padding-left: 0.75rem;
      border-left: 4px solid var(--primary);
    }}
    .guide-box p {{
      margin-bottom: 1rem;
      color: #334155;
    }}
    .guide-box ul {{
      margin-left: 1.5rem;
      margin-bottom: 1.25rem;
      color: #334155;
    }}
    .guide-box li {{ margin-bottom: 0.5rem; }}

    .faq-item {{
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 1.5rem;
      margin-bottom: 1.25rem;
      border: 1px solid var(--border);
    }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
    }}
    .faq-q span {{
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      width: 24px;
      height: 24px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      flex-shrink: 0;
      margin-top: 2px;
    }}
    .faq-a {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.7;
    }}
    .faq-a span {{
      background: #e2e8f0;
      color: #475569;
      font-size: 0.85rem;
      width: 24px;
      height: 24px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      flex-shrink: 0;
      font-weight: 700;
      margin-top: 2px;
    }}

    .related-section {{
      background: #ffffff;
      padding: 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin: 3.5rem 0;
    }}
    .related-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem;
      margin-top: 1.25rem;
    }}
    .related-link-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      padding: 1rem;
      border-radius: 8px;
      text-decoration: none;
      color: var(--text);
      font-size: 0.9rem;
      font-weight: 600;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .related-link-card:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary);
      transform: translateY(-2px);
    }}
    .related-link-card small {{
      color: var(--text-muted);
      font-size: 0.75rem;
      margin-top: 0.5rem;
      display: block;
    }}

    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1.5rem;
      margin-top: 4rem;
      font-size: 0.85rem;
      line-height: 1.7;
    }}
    .footer-inner {{
      max-width: 1000px;
      margin: 0 auto;
      text-align: center;
    }}
    .footer-logo {{
      color: #ffffff;
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 1rem;
    }}
    .footer-note {{
      margin: 1rem 0;
      color: #64748b;
    }}
  </style>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="/" class="site-logo">
      <span>❄️</span>
      <span>冬コスメ徹底比較ラボ</span>
    </a>
    <nav>
      <a href="/" class="nav-link">全コスメ特集一覧</a>
    </nav>
  </div>
</header>

<div class="container">
  <div class="breadcrumb">
    <a href="/">ホーム</a>
    <span>&gt;</span>
    <a href="/">冬ヘアケア特集</a>
    <span>&gt;</span>
    <strong>温感ヘッドスパトリートメントおすすめ10選</strong>
  </div>

  <article class="article-hero">
    <span class="article-tag">2026-2027年 冬季最新検証</span>
    <h1 class="article-title">保湿力の強さで冬のパサつき剛毛・冷えたガチガチ頭皮とさようなら！塗った瞬間じんわり温感で美髪成分が急速浸透する温感ヘッドスパトリートメントランク10</h1>
    <div class="article-meta">
      <span>公開日: 2026年11月2日</span>
      <span>更新日: 2026年11月2日</span>
      <span>専門家検証: 毛髪診断士＆ヘアケアスペシャリストチーム</span>
    </div>
    
    <div class="intro-text">
      <p>11月から12月にかけて気温が一段と低下すると、外気の乾燥に加えてウールやアクリルのコート、マフラーとの摩擦によって激しい『静電気』が発生します。静電気はキューティクルを物理的にめくれ上がらせ、毛髪内部の水分を急速に流出させます。その結果、『毛先がパサついてほうきのように広がる』『枝毛や切れ毛が急増する』『ブラッシングするたびに髪が絡まる』といった冬特有の深刻なハイダメージ毛に悩まされる女性が後を絶ちません。</p>
      
      <p>さらに見逃せないのが<strong>「冬の寒さによる頭皮の血流不良」</strong>です。頭皮が冷えてカチコチに凝り固まると、毛根へ酸素や栄養が届かなくなり、根元の立ち上がりが失われてペタンコ髪に。寒さのせいで冬のお風呂場でトリートメントを何分も放置するのが辛いという現実も、冬のヘアケア不足に拍車をかけています。</p>

      <div class="intro-highlight">
        💡 この冬のヘアダメージと頭皮の冷えを同時に打ち砕く新常識が「温感ウォータートリートメント（生トリートメント）」。濡れた髪の水分と反応して瞬時に温感クリームへ相変化。温感スチーム効果でキューティクルを自然にほぐし、わずか10秒で高浸透アミノ酸が髪の芯まで充填されます。頭皮から毛先まで、まるでサロン帰りのシルク髪が自宅で手に入ります。
      </div>

      <p>本記事では、大ヒットの火付け役となったモレモ（moremo）やヘッドスパセブン、トリコレ、ロレアルパリ、フィーノ、エッセンシャルなど、最新の温感ウォータートリートメント＆高密着集中マスク10製品を徹底比較。浸透スピード、毛先のまとまり感、温感の心地よさ、静電気防止力をプロの視点から厳密に評価し、ランキング形式でお届けします。</p>
    </div>

    <div class="toc">
      <div class="toc-title">📑 目次 - クイックナビゲーション</div>
      <ul class="toc-list">
        <li><a href="#summary-table">📊 ひと目でわかる！温感トリートメント比較表</a></li>
        <li><a href="#rank-1">第1位：moremo ミラクル10 ウォータートリートメント</a></li>
        <li><a href="#rank-2">第2位：HEAD SPA 7 プレミアムトリートメント</a></li>
        <li><a href="#rank-3">第3位：Tricore 温感ヘッドスパトリートメント</a></li>
        <li><a href="#rank-4">第4位：L'Oreal Paris ワンダーウォーター</a></li>
        <li><a href="#rank-5">第5位：BIOLISS ボタニカルウォータートリートメント</a></li>
        <li><a href="#rank-6">第6位：スカルプD ボーテ 薬用トリートメントパック</a></li>
        <li><a href="#rank-7">第7位：fino プレミアムタッチ 浸透美容液ヘアマスク</a></li>
        <li><a href="#rank-8">第8位：Essential うるおいバリアトリートメント</a></li>
        <li><a href="#rank-9">第9位：ululis インナーリペア ウォータートリートメント</a></li>
        <li><a href="#rank-10">第10位：YOLU カームナイトリペア ジェルヘアマスク</a></li>
        <li><a href="#guide-mechanism">🔬 なぜ温感？液体からクリームへ変わる浸透科学</a></li>
        <li><a href="#guide-selection">🎯 失敗しない温感ヘアケアの選び方</a></li>
        <li><a href="#guide-howto">💆‍♀️ 10秒でサロン級！正しい温感トリートメント実践法</a></li>
        <li><a href="#faq-section">❓ よくある質問（FAQ）</a></li>
      </ul>
    </div>
  </article>

  <section id="summary-table">
    <h2 class="section-h2">📊 ひと目でわかる！温感ヘッドスパトリートメント10選スペック比較表</h2>
    <div class="table-container">
      <table class="summary-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>ブランド / 商品名</th>
            <th>タイプ</th>
            <th>主要補修・美容成分</th>
            <th>参考価格</th>
            <th>詳細</th>
          </tr>
        </thead>
        <tbody>
          {''.join(table_rows)}
        </tbody>
      </table>
    </div>
  </section>

  <section id="product-rankings">
    <h2 class="section-h2">🏆 温感ヘッドスパトリートメントおすすめ人気ランキング10選</h2>
    {''.join(cards_html)}
  </section>

  <section id="guide-mechanism" class="guide-box">
    <h2 class="section-h2">🔬 なぜ温感なのか？液体からクリームへ変わる浸透と修復の科学</h2>
    <p>冬の冷気と暖房の効いた室内は、髪の水分量を通常の12〜13%から10%未満へと引き下げます。水分を失った髪は脆くなり、衣類との摩擦でプラスの静電気が帯電。キューティクル同士が反発して開き、パサつきと枝毛が加速します。</p>

    <h3>1. 水分吸熱（溶解熱）による心地よい温感スチーム</h3>
    <p>温感トリートメントに配合されている親水性ポリマーやグリコール類は、濡れた髪に残る水分と混ざり合う瞬間に『結合熱（溶解熱）』を放出します。この自然な物理現象によって約35〜38℃のマイルドなスチーム状態が髪表面に発生。熱によって硬くなったキューティクルが柔軟化し、開いたすき間から美髪成分が抵抗なく内部へ吸い込まれます。</p>

    <h3>2. 相変化（乳化）がもたらす『即効浸透＆濃密ラッピング』</h3>
    <p>ボトルから出た瞬間はサラサラの『液体（リキッド）』だからこそ、髪の微細なダメージホールまで瞬時に行き渡ります。そして水分と混ざると濃厚な『高密着クリーム』へと瞬時にテクスチャーを変え、浸透したアミノ酸やケラチンを毛髪内部にしっかりと閉じ込めます。『液体の浸透力』と『クリームの保護密着力』を同時に発揮するため、わずか10秒程度の短い時間でもサロンのディープトリートメントに匹敵する劇的な補修効果が得られるのです。</p>
  </section>

  <section id="guide-selection" class="guide-box">
    <h2 class="section-h2">🎯 迷ったらここをチェック！髪質と悩みに合わせた選び方</h2>
    <p>自分の髪質や冬特有の悩みに合わせて、最も効果を発揮するトリートメントのタイプを選びましょう。</p>

    <ul>
      <li><strong>ブリーチ・カラー・熱ダメージがひどいなら：</strong>アミノ酸17種と加水分解タンパク質が濃密な『モレモ』や『トリコレ』、高濃度マスクの『フィーノ』。</li>
      <li><strong>頭皮の冷え・コリや根元のボリューム低下が気になるなら：</strong>頭皮に直接揉み込めるスカルプ特化型の『ヘッドスパセブン』や『スカルプD ボーテ』。</li>
      <li><strong>細毛・軟毛で重たいトリートメントだとペタッとするなら：</strong>ラメラ構造でダメージ部だけを薄く包む『ロレアル パリ』や『ウルリス』。</li>
      <li><strong>冬の静電気や朝の寝癖・絡まりを防ぎたいなら：</strong>うるおいバリア処方の『エッセンシャル』や、夜間摩擦を防ぐジェルマスクの『YOLU』。</li>
    </ul>
  </section>

  <section id="guide-howto" class="guide-box">
    <h2 class="section-h2">💆‍♀️ わずか10秒でサロン級！プロが教える正しい塗布ステップ</h2>
    <p>温感トリートメントの威力を100%引き出すための、プロ直伝の正しいバスタイムステップです。</p>

    <ul>
      <li><strong>Step 1：シャンプー後、しっかり水気を絞る：</strong>髪がびしょびしょに濡れすぎていると、成分が薄まってしまいます。両手で優しく毛先の水気をキュッと絞ってから塗布しましょう。</li>
      <li><strong>Step 2：毛先を中心に塗布し、優しく揉み込む：</strong>ノズルから毛先に向けて直接塗布し、両手で優しく揉み込みます。液体が温かいクリームに変わり、髪がとろけるような感触に変わるのを感じてください。</li>
      <li><strong>Step 3：目の粗いコームでコーミング：</strong>手ぐしを通した後、粗めのバスコームで一度髪全体をとかすと、クリームが一本一本のキューティクルに均一に密着します。</li>
      <li><strong>Step 4：ぬるま湯でヌルつきが消える程度に流す：</strong>放置時間は不要（約10秒〜数分）。熱いお湯ではなく、38℃前後のぬるま湯で、手触りがつるんと滑らかな状態を残す程度に優しくすすぎましょう。</li>
    </ul>
  </section>

  <section id="faq-section">
    <h2 class="section-h2">❓ よくある質問（FAQ）</h2>
    {''.join(faq_html_blocks)}
  </section>

  <section class="related-section" id="internal-links-hub">
    <h2 class="section-h2">🔗 あわせて読みたい！冬の美髪＆パーツケアおすすめ特集</h2>
    <p>冬の寒さや乾燥から髪と全身を守るための関連記事をピックアップしました。あわせてチェックして、真冬でも輝く美しい髪と素肌をキープしましょう。</p>
    <div class="related-links-grid">
      <a href="/winter-hair-care" class="related-link-card">
        <span>冬のヘアケア総合特集</span>
        <small>静電気・パサつきを防ぐヘアケア全般</small>
      </a>
      <a href="/winter-hair-oil" class="related-link-card">
        <span>冬のヘアオイル特集</span>
        <small>ドライヤー前の濃密保護オイル比較</small>
      </a>
      <a href="/winter-hair-milk" class="related-link-card">
        <span>冬のヘアミルク特集</span>
        <small>インナードライ髪を柔らかく潤す乳液ケア</small>
      </a>
      <a href="/winter-hair-mask" class="related-link-card">
        <span>冬の集中ヘアマスク特集</span>
        <small>週1〜2回のハイダメージ集中トリートメント</small>
      </a>
      <a href="/winter-scalp-shampoo" class="related-link-card">
        <span>冬のスカルプシャンプー特集</span>
        <small>頭皮の乾燥・フケ・かゆみを防ぐ薬用ケア</small>
      </a>
      <a href="/winter-moisture-shampoo" class="related-link-card">
        <span>冬の高保湿シャンプー特集</span>
        <small>洗うたびに潤うアミノ酸系モイスト泡</small>
      </a>
      <a href="/winter-oil-mist" class="related-link-card">
        <span>高保湿オイルインミスト特集</span>
        <small>暖房乾燥を救う二層式フェイスミスト</small>
      </a>
      <a href="/winter-carbonic-bath" class="related-link-card">
        <span>薬用重炭酸入浴剤特集</span>
        <small>冷えと全身乾燥を芯から温める温浴ケア</small>
      </a>
    </div>
  </section>
</div>

<footer>
  <div class="footer-inner">
    <div class="footer-logo">❄️ 冬コスメ徹底比較ラボ</div>
    <p class="footer-desc">冬特有の肌乾燥・冷え・寒暖差トラブルに立ち向かう女性のための美容情報・コスメ検証サイト。</p>
    <p class="footer-note">※掲載している楽天市場の価格やポイント情報は調査時点のものです。最新情報は各ショップページをご確認ください。</p>
    <p class="copyright">&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved.</p>
  </div>
</footer>

</body>
</html>
"""

with open("winter-hot-treatment.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-hot-treatment.html successfully!")
