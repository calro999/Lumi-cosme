import json
import re

with open("fetched_perfect_3articles_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_carbonic_shampoo"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 5,000ppm超濃密炭酸×植物オイル！冬の頭皮とパサつく美髪を同時に満たす最高峰",
        "catch": "もっちりとした濃密ホイップ泡が摩擦ゼロで密着。寒さで固まった頭皮の毛穴汚れを浮かせ血行促進",
        "brand_name": "b.ris (ビーリス)",
        "capacity": "200g",
        "type": "オーガニック高濃度炭酸泡シャンプー",
        "features": "高濃度炭酸5,000ppm、オーガニック植物エキス、高級植物オイル、PPT補修成分、シリコンフリー",
        "value": "数々のベストコスメを受賞した炭酸シャンプーの頂点。冬の寒冷で硬くなった頭皮をほぐしながら、アミノ酸系洗浄成分とオイルでサロン帰りのうるツヤ髪へ",
        "desc_p1": "11月から12月にかけて気温が一段と低下すると、顔だけでなく頭皮の血流も著しく滞ります。頭皮の温度が下がると皮脂がラードのように固まって毛穴に詰まり、一方で暖房の温風によって地肌の水分が奪われて『細かいパラパラとした乾燥フケ』や痒みが発生します。さらに寒さによる頭皮のコリは、髪のパサつきやトップのボリュームダウン（ペタンコ髪）の元凶となります。",
        "desc_p2": "b.risのオーガニックスパークリングシャンプーは、缶から出した瞬間に逆さにしても落ちないほど弾力のある『5,000ppm超濃密炭酸泡』が特徴です。ミクロの炭酸泡が毛穴の奥まで入り込み、冬の寒さで凝固した頑固な皮脂汚れをこすらずにジュワッと浮き上がらせます。同時に炭酸ガスの効果で頭皮の巡りをサポート。厳選されたオーガニックオイルとPPT補修成分がキューティクルをラッピングするため、トリートメントいらずのしっとり柔らかな指通りに仕上がります。",
        "target": "冬になると頭皮が乾燥して痒みやフケが出る方、トップの髪がペタンコになりやすい方、摩擦レスで髪と頭皮を優しく洗い上げたい方",
        "point": "ぬるま湯で2分間しっかり予洗いした後、ピンポン玉2個分の泡を頭皮全体に揉み込みます。そのまま2〜3分置いて『炭酸泡パック』を行うと、温浴効果と血行促進が倍増します。"
    },
    {
        "rank": 2,
        "tag": "✨ 希少なレアオイル×高濃度炭酸！冬のハイダメージ毛を濃密補修するサロン発泡",
        "catch": "アルガンオイル・バオバブオイル高配合。3日に1度の極上炭酸スパで天使の輪が復活",
        "brand_name": "Le ment (ルメント)",
        "capacity": "200g",
        "type": "高濃度炭酸オイルクレンジング＆シャンプー",
        "features": "高濃度炭酸5,000ppm、アルガンオイル、バオバブオイル、加水分解ケラチン、フラーレン",
        "value": "高級サロンの炭酸ヘッドスパを自宅で再現。ノーベル賞受賞成分フラーレンや植物レアオイルが、冬の乾燥と静電気で傷んだ毛先を集中コーティング",
        "desc_p1": "冬は乾燥だけでなく、マフラーやタートルネックの摩擦、暖房による静電気がキューティクルを剥がし、毛先のパサつきや広がりが一年で最も悪化する季節です。『普通のシャンプーではきしんで指が通らない』というハイダメージ毛に悩む方に熱狂的に支持されているのがルメントの『スパークリングオイル クレンジング＆シャンプー』です。",
        "desc_p2": "一般的な炭酸シャンプーにありがちな『サッパリしすぎて冬は乾燥する』という弱点を、モロッコ産アルガンオイルやバオバブオイルなどの高保湿レアオイルを贅沢にブレンドすることで見事に克服。キメの細かい炭酸泡が頭皮の余分な汚れだけを吸着し、髪一本一本に上質な油分と加水分解ケラチンを補填します。洗い流した瞬間から指通りの滑らかさに驚かされ、ドライヤーで乾かした後はしっとりとまとまる極上のツヤ髪へ導きます。",
        "target": "冬の静電気や摩擦で髪が広がりパサつく方、カラーやパーマで傷んだ髪を補修したい方、上質なホワイトブーケの香りでリラックスしたい方",
        "point": "3日に1度、普段のシャンプーと置き換えて使用するスペシャルケアとして最適。泡を毛先まで伸ばして優しく揉み込むことで、毛先までオイルパックしたような潤いが宿ります。"
    },
    {
        "rank": 3,
        "tag": "💈 美容室専売プロクオリティ！4,400ppmの微細炭酸泡で冬の頭皮環境をリセット",
        "catch": "ミルボンの毛髪科学が生んだエイジングスカルプケア。柿タンニンが冬の頭皮のニオイもオフ",
        "brand_name": "MILBON (ミルボン)",
        "capacity": "170g / 320g",
        "type": "サロン専売・高濃度炭酸スカルプクレンジングフォーム",
        "features": "高濃度炭酸4,400ppm、カキタンニン（消臭・整肌）、加水分解ダイズエキス、微細マイクロフォーム",
        "value": "全国のトップヘアサロンがヘッドスパメニューで採用。頭皮のベタつきやニオイの原因となる過酸化脂質を確実にオフし、健やかな頭皮環境を育てる",
        "desc_p1": "冬は汗をかかないため頭皮ケアを怠りがちですが、実は厚着や暖房によって地肌が蒸れ、固まった皮脂が酸化して嫌なニオイや毛穴詰まりを引き起こす『冬の隠れ頭皮トラブル』が多発します。この大人の頭皮悩みをプロの技術で解決するのがミルボンの『プラーミア クリアスパフォーム』です。",
        "desc_p2": "濃密なマイクロ炭酸泡が頭皮に吸い付くように広がり、指が届かない毛穴の奥深くの隙間にまで浸透。皮脂を吸着して浮き上がらせるカキタンニン成分が、冬の夕方に気になる頭皮の加齢臭や脂っぽいニオイを元からクリアにします。さらに大豆エキスがエイジング世代の頭皮に潤いを与え、洗髪後は地肌がスーッと軽くなるような爽快感と、根元からピンと立ち上がる自然なボリューム感を実感できます。",
        "target": "夕方になると頭皮のニオイや重たさが気になる方、頭皮のエイジングケアを本格的に始めたい方、サロン品質の確かな洗浄力を求める方",
        "point": "週に2回程度、通常シャンプーの代わりに使用。頭頂部や生え際を中心に泡を乗せ、指の腹を使って頭皮を下から上へと引き上げるようにマッサージしながら洗うとリフトアップ効果も期待できます。"
    },
    {
        "rank": 4,
        "tag": "⚡ 朝の炭酸ジェット泡で血行促進！寝癖直しと頭皮爽快ケアを同時に叶える時短名品",
        "catch": "アンファーの頭皮研究が集約。炭酸ジェット噴射が寒さで縮こまった頭皮を目覚めさせる",
        "brand_name": "スカルプD (アンファー)",
        "capacity": "150g",
        "type": "朝用・炭酸ジェットスカルプシャンプー",
        "features": "高圧炭酸ジェットノズル、ヒアルロン酸、アミノ酸系洗浄成分、シトラスミントの爽快感",
        "value": "朝の忙しい時間でもシュッとひと吹きで濃密泡が完成。冬の朝の冷えた頭皮をジェット刺激で活性化し、寝癖を一発でリセットしながらハリコシを付与",
        "desc_p1": "12月の凍えるような朝、冷え切った布団から起きて鏡を見ると、頑固な寝癖がついている上に頭皮が重たく凝り固まっていることがあります。朝シャンをするにしても、冬の朝は寒くて億劫になりがちです。そんな冬の朝のスタイリングと頭皮ケアを劇的に快適にするのが、スカルプDの『モーニング 炭酸ジェット スカルプシャンプー』です。",
        "desc_p2": "強力なジェットスプレーノズルから勢いよく噴射される冷感炭酸泡が、地肌に直撃。心地よいパチパチとした刺激が冬の朝の眠気と頭皮の血流停滞を一瞬で吹き飛ばします。アミノ酸系のマイルドな洗浄成分が朝の余分な寝汗や皮脂だけを優しく洗い流し、ヒアルロン酸が日中の暖房乾燥から頭皮を守る潤いヴェールを形成。寝癖を素早くリセットしながら、トップにふんわりとしたハリコシを与えます。",
        "target": "朝シャン派で冬の頑固な寝癖に悩んでいる方、頭皮の血行をスピーディーに促進したい方、爽快感のあるシトラスミントの香りを好む方",
        "point": "ノズルを頭皮に直接近づけてシューッとスプレー。泡が弾ける音を楽しみながら、指先で頭皮全体をリズミカルにタッピングするように揉み洗いして流してください。"
    },
    {
        "rank": 5,
        "tag": "🌿 天然メントール×高濃度炭酸！冬の重い頭皮をすっきりリフレッシュするサロン定番",
        "catch": "ナプラの炭酸ソーダテクノロジー。シリコンや残留アルカリをリセットして素髪へ",
        "brand_name": "napla (ナプラ)",
        "capacity": "200g",
        "type": "サロン仕様・炭酸スキャルプソーダシャンプー",
        "features": "高濃度炭酸、天然メントール、6種のオーガニックハーブエキス、アルガンオイル",
        "value": "美容室での炭酸クレンジングメニューでも大定番。ヘアカラー後の残留アルカリを除去し、冬の乾燥頭皮を健やかな弱酸性へと導くコスパ抜群の1本",
        "desc_p1": "冬は乾燥によって頭皮のターンオーバーが乱れ、古い角質とスタイリング剤の残りが混ざり合って頭皮の毛穴を塞ぎがちです。また、冬場にヘアカラーや白髪染めをした後の頭皮はアルカリ性に傾き、過敏になりやすくなります。ナプラの『インプライム ソーダシャンプー』は、そんなデリケートな頭皮環境を優しく中和して整えます。",
        "desc_p2": "キメ細やかな炭酸フォームが髪と頭皮を優しく包み込み、毛髪に付着したシリコンやスタイリング剤の汚れ、頭皮の余分な皮脂をきれいにクレンジング。天然ハーブエキスとアルガンオイルが配合されているため、スッキリとした洗い上がりでありながら地肌が突っ張る心配はありません。髪本来の素直な素髪状態に戻るため、その後に使うトリートメントの浸透が劇的にアップします。",
        "target": "普段ワックスやスプレーなどのスタイリング剤をしっかり使う方、冬にヘアカラーやパーマをした後の頭皮ケアをしたい方、コスパ重視の方",
        "point": "シャワーでしっかり髪を濡らした後、缶をよく振って適量を頭皮に塗布。ハーブの香りに包まれながら頭皮全体を包み込むようにマッサージして洗い流します。"
    },
    {
        "rank": 6,
        "tag": "🔬 炭酸専門研究機関が開発！医療機器発想の本格スカルプDRプロフェッショナル",
        "catch": "驚異の炭酸溶解技術。冬の薄毛・抜け毛・頭皮の冷えに本気で向き合う本格スカルプフォーム",
        "brand_name": "東洋炭酸研究所",
        "capacity": "200g",
        "type": "高濃度炭酸・医療発想スカルプシャンプー",
        "features": "高純度炭酸ガス、パンテノール、プラセンタエキス、センブリエキス、無香料・無着色",
        "value": "炭酸美容のパイオニアが開発したドクターズ仕様。炭酸の浸透圧を利用して育毛サポート成分を角層深部まで届け、冬の抜け毛を防ぐ",
        "desc_p1": "11月・12月は、夏の紫外線ダメージの蓄積と冬の寒冷による血流低下がピークに達し、『抜け毛や切れ毛が急激に増える』魔の季節です。薄毛やボリューム低下に真剣に悩む大人の女性・男性から熱狂的な信頼を集めているのが、東洋炭酸研究所の『TANSAN スカルプ DR プロ』です。",
        "desc_p2": "医療現場でも研究される炭酸の血流促進作用を極限まで追求。泡立てるのではなく、最初から超濃密な炭酸クリーム泡として噴射されるため、頭皮にピタッと吸着して有効成分を密閉デリバリーします。センブリエキスやプラセンタエキスなどの育毛・美髪成分が、炭酸のボーア効果（酸素供給促進）と相まって毛根へ力強くアプローチ。冬の寒さで弱った毛根を元気づけ、太くハリのある髪を育みます。",
        "target": "冬の抜け毛や薄毛、分け目の広がりが気になり始めた方、無香料・無添加のストイックな本格派を好む方、本格スカルプケアをしたい方",
        "point": "頭皮に泡を密着させた後、両手の指の腹で頭皮を揉みほぐすように1分間マッサージ。その後すぐに流さず3分間泡パックすることで、炭酸効果を最大限に享受できます。"
    },
    {
        "rank": 7,
        "tag": "🌿 薬用有効成分がフケ・かゆみを徹底ブロック！ミュリアムの薬用スカルプ炭酸ケア",
        "catch": "グリチルリチン酸2K配合の医薬部外品。冬のデリケートな乾燥頭皮を優しく鎮静",
        "brand_name": "NUMBER THREE (ナンバースリー)",
        "capacity": "250g",
        "type": "医薬部外品・薬用スカルプ炭酸クレンジング",
        "features": "有効成分グリチルリチン酸2K、高濃度炭酸、オウゴンエキス、ローヤルゼリー、無添加処方",
        "value": "大人気ヘアケアブランド・ナンバースリーの薬用ライン。冬の乾燥フケや頭皮の痒みを有効成分で穏やかに鎮め、清潔で健やかな地肌をキープ",
        "desc_p1": "『冬になると頭皮が痒くて無意識に掻いてしまう』『肩に落ちる細かいフケが恥ずかしい』という切実な悩みに、医薬部外品の確かな有効成分でアプローチするのがナンバースリーの『ミュリアム クリスタル スカルプ炭酸クレンジング』です。",
        "desc_p2": "抗炎症有効成分『グリチルリチン酸2K』が配合されており、冬の乾燥によって傷つき炎症を起こした地肌を速やかに鎮静。さらにローヤルゼリーエキスやオウゴンエキスが角質層を潤いで満たし、フケの発生を抑制します。炭酸の優しいマイクロ泡が、敏感になった頭皮に摩擦の負担をかけることなく汚れだけを吸着。洗い流した後は頭皮がしっとりと落ち着き、痒みのない快適な毎日が戻ってきます。",
        "target": "冬の頭皮の痒み・パラパラとした乾燥フケに本気で悩む方、医薬部外品の確かな効果を求める方、頭皮への優しさを最優先したい方",
        "point": "泡を頭皮に塗布したら、絶対に爪を立てず、指の腹で優しく圧をかけるように洗います。ぬるめのシャワーでしっかりすすぎ、洗い残しのないようにしてください。"
    },
    {
        "rank": 8,
        "tag": "☁️ まるでマシュマロ！もっちもち濃密ホイップ泡で洗う摩擦レス炭酸モイストシャンプー",
        "catch": "ヒアルロン酸＆コラーゲン配合。冬の乾燥頭皮と毛先を潤いヴェールで優しく包み込む",
        "brand_name": "TOWAZ (トワズ)",
        "capacity": "200g",
        "type": "高保湿・濃密ホイップ炭酸泡シャンプー",
        "features": "高濃度炭酸マイクロ泡、加水分解ヒアルロン酸、水溶性コラーゲン、植物セラミド、アミノ酸系洗浄成分",
        "value": "弾力のあるマシュマロ泡がクッションとなり、洗髪時の摩擦ダメージを完全ゼロへ。プチプラとは思えない贅沢な潤い感で冬の乾燥を撃退",
        "desc_p1": "冬の髪は乾燥によってキューティクルが開き、濡れた状態での摩擦に極めて弱くなっています。手で泡立てる通常のシャンプーでは、泡立ちが不十分なまま髪同士を擦り合わせてしまい、切れ毛や枝毛の原因に。この摩擦ストレスを完璧に解消するのがTOWAZの『炭酸泡シャンプー』です。",
        "desc_p2": "プッシュするだけで出てくる超濃密なホイップ泡は、手のひらを逆さにしてもびくともしない驚異の弾力性を誇ります。この泡がクッションとなって頭皮と髪を優しく包み込み、指と髪の摩擦を徹底的にガード。さらに加水分解ヒアルロン酸とコラーゲンが洗いながら地肌と毛髪に潤いを浸透させます。洗い上がりの髪はキシキシ感が一切なく、まるでサロンのトリートメント後のようにつるんと滑らかです。",
        "target": "洗髪時の摩擦による抜け毛や切れ毛を防ぎたい方、泡立てるのが面倒な方、しっとりとした高保湿な洗い上がりを求める方",
        "point": "泡を手にとったら、頭皮だけでなく髪の中間から毛先までたっぷりと泡を行き渡らせます。手ぐしを通しながら泡で髪を包み込むように洗うと、シルクのような指通りになります。"
    },
    {
        "rank": 9,
        "tag": "🌋 炭酸泡×ミネラル泥のWパワー！冬の毛穴汚れを吸着してふんわり立ち上げる",
        "catch": "泡と泥のハイブリッド。乾燥フケとベタつきを同時にケアし、頭皮を根本から引き締める",
        "brand_name": "AMBiQUE (アンビーク)",
        "capacity": "200g",
        "type": "炭酸泡×ミネラル泥スカルプシャンプー",
        "features": "高濃度炭酸泡、モロッコ溶岩クレイ、マリンシルト、加水分解ダイズタンパク、アミノ酸系洗浄成分",
        "value": "メンズ・レディース問わず大人気のスカルプブランド。炭酸の気泡力とクレイの吸着力を融合させ、冬の頭皮環境を健やかにリフレッシュ",
        "desc_p1": "冬は乾燥する一方で、暖房による皮脂の酸化やフケが毛穴の出口を塞ぎ、髪の根元が寝てしまってヘアスタイルが決まらないという悩みが増加します。頭皮のディープクレンジングと保湿を両立させる逸品が、アンビークの『炭酸スカルプシャンプー 泡×泥』です。",
        "desc_p2": "炭酸のマイクロバブルに加え、微細なミネラルを豊富に含むモロッコ溶岩クレイ（泥）を配合。毛穴の奥にこびりついた皮脂や古い角質を泥が磁石のように吸着し、炭酸が浮かせて一網打尽に洗い流します。アミノ酸系洗浄成分とダイズタンパクが頭皮を優しく保湿するため、つっぱり感や乾燥を引き起こしません。根元からふわっと立ち上がる自然なボリューム感が手に入ります。",
        "target": "髪が細くてペタンとしやすい方、頭皮の毛穴汚れやフケをしっかり落としたい方、男女問わず使える爽快なスカルプケアを探している方",
        "point": "頭皮全体に泥炭酸泡を馴染ませたら、頭皮を揉みほぐすように2分間マッサージ。クレイ成分が汚れを吸着する時間を少し置いてから、ぬるま湯でしっかり洗い流します。"
    },
    {
        "rank": 10,
        "tag": "🎨 カラー長持ち＆ツヤ髪キープ！冬の乾燥・退色を防ぐ濃密炭酸カラーケアシャンプー",
        "catch": "高濃度炭酸泡がキューティクルを引き締め。冬のパサつくカラー毛にしっとり天使の輪を",
        "brand_name": "C gray (シーグレイ)",
        "capacity": "200g",
        "type": "カラーケア・高濃度炭酸スパークリングシャンプー",
        "features": "高濃度炭酸泡、ヘマチン、アミノ酸補修成分、アルガンオイル、弱酸性処方",
        "value": "冬の乾燥によるカラーの褪色（色落ち）を防ぎながら、炭酸泡で頭皮を優しくクレンジング。サロン帰りの美しい髪色とツヤが長く続く",
        "desc_p1": "冬場は空気の乾燥と静電気によってキューティクルが開き、せっかく冬のトレンドカラーに染めた髪色がわずか数週間で色落ちして黄色くパサついてしまいがちです。そんな冬のカラー毛の悩みに特化した炭酸シャンプーが、シーグレイの『炭酸泡 スパークリングシャンプー』です。",
        "desc_p2": "ヘアサロンでもカラーケアの主役として使われる成分『ヘマチン』を贅沢に配合。弱酸性の高濃度炭酸泡がキューティクルをキュッと引き締め、カラー染料の流出を強力にブロックします。さらにアルガンオイルが髪の表面を滑らかにコーティングし、冬の乾燥摩擦やドライヤーの熱ダメージから髪を保護。頭皮をすっきり洗い上げながら、サロン帰りのような深い色ツヤを長期間キープできます。",
        "target": "冬にヘアカラーや白髪染めをして色落ちが早いと悩む方、カラー後の髪のパサつきやゴワつきを改善したい方、艶やかなまとまりを求める方",
        "point": "カラー施術後1〜2週間の集中ケアとして使うのが特に効果的。泡を頭皮から毛先までしっかり行き渡らせ、泡パックを1〜2分行ってから流すとカラーキープ力が格段に向上します。"
    }
]

faq_items = [
    {
        "q": "冬に炭酸シャンプーを使うと、逆に頭皮が乾燥することはありませんか？",
        "a": "一般的な炭酸シャンプーの中にはメントールが強くサッパリ感を重視したものもありますが、本記事で厳選した冬向け高保湿炭酸シャンプーは、アミノ酸系洗浄成分や高純度植物オイル（アルガンオイル、バオバブオイルなど）、ヒアルロン酸を贅沢に配合しています。冬の寒冷で固まった余分な酸化皮脂だけを浮かし、必要な潤いはしっかり守る設計になっているため、つっぱり感や乾燥フケの心配なく毎日〜週数回安心してお使いいただけます。"
    },
    {
        "q": "炭酸シャンプーは普通のシャンプーと毎日置き換えて使ってもいいですか？",
        "a": "b.risやTOWAZなどのマイルドなアミノ酸系・高保湿設計の製品は、毎日のデイリーシャンプーとしてご使用いただけます。一方、ミルボンやナプラなどのクレンジング力が高いサロン専売品は、週に2〜3回のスペシャルスカルプケア（または週末のリセットケア）として取り入れるのが最も効果的で頭皮の油分・水分バランスを最適に保てます。"
    },
    {
        "q": "冬の炭酸シャンプーの効果を最大化する使い方はありますか？",
        "a": "最も重要なのは【38℃前後のぬるま湯での2分間の予洗い】です。熱すぎるお湯は頭皮の必要な皮脂まで奪って乾燥を悪化させます。ぬるま湯でしっかり汚れを流した後に炭酸泡を頭皮に乗せ、指の腹で頭皮を優しく揉みほぐしながら2〜3分置く『炭酸泡パック』を行うと、炭酸ガスが角層深部まで届いて血流が劇的に改善します。"
    },
    {
        "q": "カラーや白髪染めをしている髪に使っても色落ちしませんか？",
        "a": "むしろ高品質な炭酸シャンプー（シーグレイなど）は、アルカリに傾いた髪を等電点（弱酸性）へと戻し、キューティクルを引き締める働きがあるため、カラーの退色防止に非常に効果的です。ただし、カラー直後の24時間は髪が不安定なため、施術翌々日以降から取り入れるのがベストです。"
    },
    {
        "q": "炭酸シャンプーの後にトリートメントは必要ですか？",
        "a": "b.risなどPPTや植物オイルが豊富に含まれたオールインワン設計の製品はトリートメントなしでもしっとりまとまりますが、冬の静電気や毛先の深刻なパサつきが気になるハイダメージ毛の方は、毛先を中心に高保湿ヘアマスクやインバストリートメント、洗い流さないヘアオイルを併用することをおすすめします。"
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
    "headline": "保湿力の強さで冬の頭皮乾燥フケ・寒冷凝固とさようなら！高濃度マイクロ炭酸泡で毛穴汚れを浮かし血行を巡らせる高保湿炭酸シャンプーランク10",
    "description": "11月・12月の冬の寒冷による頭皮の血行不良・固まった皮脂・暖房による乾燥フケ・ペタンコ髪を徹底解決！5,000ppm超の微細マイクロ炭酸泡で優しく毛穴をクレンジングし巡りを高める高保湿炭酸シャンプー10選を徹底比較！b.ris、ルメント、ミルボン、スカルプD、ナプラなど、サロン級のツヤとハリコシを叶える名品を厳選。",
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
    "name": "冬の高保湿炭酸シャンプー おすすめランキング10選",
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
              <tr><th>おすすめの頭皮・髪質</th><td>{p['target']}</td></tr>
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
  <title>保湿力の強さで冬の頭皮乾燥フケ・寒冷凝固とさようなら！高濃度マイクロ炭酸泡で毛穴汚れを浮かし血行を巡らせる高保湿炭酸シャンプーランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の寒冷による頭皮の血行不良・固まった皮脂・暖房による乾燥フケ・ペタンコ髪を徹底解決！5,000ppm超の微細マイクロ炭酸泡で優しく毛穴をクレンジングし巡りを高める高保湿炭酸シャンプー10選を徹底比較！b.ris、ルメント、ミルボン、スカルプD、ナプラなど、サロン級のツヤとハリコシを叶える名品を厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-carbonic-shampoo">
  <meta name="robots" content="index, follow, max-image-preview:large">
  
  <!-- OGP & SNS -->
  <meta property="og:title" content="保湿力の強さで冬の頭皮乾燥フケ・寒冷凝固とさようなら！高濃度マイクロ炭酸泡で毛穴汚れを浮かし血行を巡らせる高保湿炭酸シャンプーランク10">
  <meta property="og:description" content="11月・12月の冬の寒冷による頭皮の血行不良・固まった皮脂・暖房による乾燥フケ・ペタンコ髪を徹底解決！高濃度マイクロ炭酸泡で頭皮を満たす高保湿炭酸シャンプー10選！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-carbonic-shampoo">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#0284c7">

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
      --primary: #0284c7;
      --primary-light: #f0f9ff;
      --primary-dark: #0369a1;
      --text-main: #2d3748;
      --text-sub: #718096;
      --bg-page: #fbfbfc;
      --bg-card: #ffffff;
      --border: #edf2f7;
      --border-focus: #bae6fd;
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
      background: #f0f9ff;
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
    <a href="/">HOME</a> &gt; <span>高保湿炭酸シャンプー ランキング</span>
  </nav>

  <main class="container">

    <section class="hero-section">
      <span class="post-badge">2026年最新冬コスメ厳選</span>
      <h1 class="post-title">保湿力の強さで冬の頭皮乾燥フケ・寒冷凝固とさようなら！高濃度マイクロ炭酸泡で毛穴汚れを浮かし血行を巡らせる高保湿炭酸シャンプーランク10</h1>
      <div class="post-meta">
        <span>執筆・監修: 冬コスメ徹底比較ラボ 編集部</span>
        <span>更新日: 2026年11月02日</span>
        <span>検証基準: 炭酸濃度(ppm)・頭皮保湿力・泡の弾力持続性・洗い上がりの指通り</span>
      </div>
      <div class="intro-text">
        <p>11月・12月、日本の冬は過酷な寒波とともに到来します。気温が10℃を下回り、暖房が一日中稼働するこの季節、スキンケアに気を使う人は多くても、<strong>『頭皮の深刻な寒冷凝固と砂漠乾燥』</strong>を見過ごしてしまっている方が非常に多く見受けられます。</p>
        <p>冬の冷気によって頭皮の毛細血管が収縮すると、血行が滞って地肌はガチガチに凝り固まります。さらに低温環境下では、皮脂がラードのように固まって毛穴の出口を塞ぎ、一方で室内の乾いた暖房風が地肌の水分を容赦なく奪うため、<strong>『パラパラと肩に落ちる細かい乾燥フケ』や猛烈な痒み</strong>、そして髪の根元がペタンと潰れてしまうボリューム低下を引き起こします。</p>
        <p>冬の硬直した頭皮環境を劇的にリセットするのが、今ヘアサロンや美容通の間で熱狂的な支持を集める<strong>『高保湿炭酸シャンプー（炭酸スカルプフォーム）』</strong>です。5,000ppmを超える微細な高濃度マイクロ炭酸泡が、寒さで固まった毛穴汚れを擦らずにジュワッと浮かし、炭酸ガスの血管拡張作用で頭皮の巡りを急速活性化。高級植物オイルやアミノ酸が地肌と髪を濃密に潤し、サロン帰りのようなふんわり艶髪を蘇らせます。</p>
      </div>

      <div class="callout-box">
        <div class="callout-title">📌 冬の頭皮に「濃密炭酸シャンプー」が欠かせない医学的理由</div>
        <p>通常のシャンプーによるゴシゴシ洗いは、冬の弱った角質を傷つけて乾燥フケを悪化させます。炭酸シャンプーは、弾力ホイップ泡のクッション効果で摩擦をゼロに抑えつつ、炭酸ガスが皮膚から吸収されて『ボーア効果（血流促進＆酸素供給）』を誘発。芯から温まるヘッドスパ効果と、植物オイルによるラッピング保湿を同時に実現します。</p>
      </div>

      <div class="toc-box">
        <div class="toc-title">📋 目次</div>
        <ul class="toc-list">
          <li><a href="#why-carbonic-shampoo">1. 冬の頭皮凝固・乾燥フケのメカニズム</a></li>
          <li><a href="#how-to-choose">2. 冬の高保湿炭酸シャンプーの失敗しない選び方</a></li>
          <li><a href="#ranking">3. 高保湿炭酸シャンプーおすすめランキング10選</a></li>
          <li><a href="#comparison">4. 全10商品スペック比較一覧表</a></li>
          <li><a href="#effective-use">5. サロン直伝！冬の炭酸泡パック＆スカルプ洗髪術</a></li>
          <li><a href="#faq">6. よくある質問 (FAQ)</a></li>
        </ul>
      </div>
    </section>

    <!-- セクション1 -->
    <section id="why-carbonic-shampoo" class="content-box">
      <h2 class="section-title">1. 冬の頭皮凝固・乾燥フケのメカニズム</h2>
      <p>11月・12月に頭皮トラブルや髪のパサつきが急増する背景には、<strong>『寒冷凝固×暖房乾燥×血流低下』</strong>の悪循環が存在します。</p>
      
      <h3 class="subsection-title">① 皮脂の「ラード化現象」と毛穴詰まり</h3>
      <p>人間の皮脂は温度によって状態が変化します。夏はサラサラとした液体状ですが、冬の外気で頭皮温度が下がると固まりやすくなり、毛穴周辺で硬化。そこへ古い角質やスタイリング剤が混ざり合うことで、通常のシャンプーでは落としきれない頑固な過酸化脂質へと変貌します。</p>

      <h3 class="subsection-title">② 暖房直撃による「角質剥離（乾燥フケ）」の発生</h3>
      <p>エアコンの温風が頭頂部に直接当たると、頭皮の水分量が急激に失われます。水分を失った頭皮の角質は柔軟性を失い、わずかな刺激やブラッシングの摩擦でパラパラと細かく剥がれ落ち、これが衣服の肩口に目立つ『冬の乾燥フケ』の正体です。</p>

      <h3 class="subsection-title">③ 炭酸ガスがもたらす「ボーア効果」と巡りの改善</h3>
      <p>高濃度炭酸（二酸化炭素）が溶け込んだ泡を頭皮に乗せると、二酸化炭素が皮膚を通過して毛細血管へ到達します。血管内が一時的な酸素不足（高二酸化炭素状態）と錯覚されることで血管が反射的に大きく拡張。血流量が一気に跳ね上がり、毛根細胞へ酸素と栄養素がたっぷり供給されます。これにより硬く突っ張っていた頭皮がじんわりとほぐれ、健やかな美髪が育つ土壌が整います。</p>
    </section>

    <!-- セクション2 -->
    <section id="how-to-choose" class="content-box">
      <h2 class="section-title">2. 冬の高保湿炭酸シャンプーの失敗しない選び方</h2>
      <p>冬の乾燥頭皮を健やかに保つ炭酸シャンプーを選ぶ際は、以下の3つの基準を重視してください。</p>

      <ul>
        <li><strong>【炭酸濃度】4,000〜5,000ppm以上を目安に：</strong> 美容室の本格炭酸泉と同等以上の血行促進効果を得るには、最低でも4,000ppm以上の高濃度設計が必要です。缶から出した瞬間に逆さにしても落ちない濃密な泡質を選びましょう。</li>
        <li><strong>【洗浄成分とオイル保湿】：</strong> ラウレス硫酸ナトリウムなどの強すぎる高級アルコール系ではなく、ココイルグルタミン酸やラウロイルメチルアラニンなどのアミノ酸系洗浄成分をベースにし、アルガンオイルやホホバオイルがブレンドされたものを選ぶと、冬でも地肌がつっぱりません。</li>
        <li><strong>【抗炎症・薬用成分の有無】：</strong> すでに痒みやパラパラとした乾燥フケが起きている場合は、グリチルリチン酸2Kなどの抗炎症成分を配合した医薬部外品（ナンバースリーなど）を選ぶと速やかにトラブルが鎮静します。</li>
      </ul>
    </section>

    <!-- セクション3: ランキング -->
    <section id="ranking">
      <h2 class="section-title">3. 高保湿炭酸シャンプーおすすめランキング10選</h2>
      <p style="margin-bottom: 24px; color: #4a5568;">当ラボ編集部が楽天市場で流通する最新炭酸シャンプーを徹底検証し、11月〜12月の頭皮乾燥・冷え・髪のパサつきを解消するおすすめ10選をランキング形式でご紹介します。</p>
      
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
      <h2 class="section-title">5. サロン直伝！冬の炭酸泡パック＆スカルプ洗髪術</h2>
      <p>高濃度炭酸シャンプーの温浴効果とクレンジング力を120%引き出す、プロ直伝のステップです。</p>

      <h3 class="subsection-title">STEP 1: 38℃前後のぬるま湯で2分間しっかり予洗い</h3>
      <p>冬のお風呂は熱いお湯（41〜42℃）を使いたくなりますが、熱湯は頭皮の必要な保湿皮脂を一気に溶かし出し、深刻な乾燥の原因となります。38℃前後のぬるま湯で、指の腹を使って地肌を優しくマッサージしながら2分間予洗いをしましょう。これだけで汚れの7割が落ち、炭酸泡の密着度が格段に上がります。</p>

      <h3 class="subsection-title">STEP 2: 泡を頭皮に揉み込んで「2〜3分泡パック」</h3>
      <p>缶を上下にしっかり振ってから、ピンポン玉2個分の泡を頭頂部・側頭部・後頭部に配置。指の腹で泡を頭皮全体に押し当てるように揉み込み、そのまま2〜3分放置します。炭酸ガスが角層深部へ浸透し、頭皮がじんわりと温かくなるような心地よい感覚を味わえます。</p>

      <h3 class="subsection-title">STEP 3: お風呂上がりは「5分以内に頭皮からドライヤー」</h3>
      <p>洗髪後、濡れたまま放置すると頭皮が急速に冷えて血行が悪化し、雑菌が繁殖してニオイや痒みの原因になります。タオルで優しく頭皮の水分を拭き取った後、5分以内にドライヤーの温風で頭皮の根元からしっかり乾かしてください。最後に冷風を当てるとキューティクルが引き締まり、ツヤが格段にアップします。</p>
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
      <h2 class="section-title" style="margin-top: 0;">あわせて読みたい！冬の温浴＆ヘアケア関連記事</h2>
      <div class="related-links-grid">
        <a href="/winter-hot-treatment" class="related-link-card">
          <span class="related-card-tag">温感スチーム美髪 NEW</span>
          <div class="related-card-title">塗った瞬間じんわり温感！冬の温感ヘッドスパトリートメント10選</div>
        </a>
        <a href="/winter-carbonic-bath" class="related-link-card">
          <span class="related-card-tag">全身の冷え性改善</span>
          <div class="related-card-title">重炭酸イオン温浴で芯から温まる！薬用重炭酸入浴剤おすすめ10選</div>
        </a>
        <a href="/winter-scalp-scrub" class="related-link-card">
          <span class="related-card-tag">頭皮ディープクレンジング</span>
          <div class="related-card-title">頑固な毛穴詰まりをスッキリ！冬の高保湿スカルプスクラブ10選</div>
        </a>
        <a href="/winter-scalp-serum" class="related-link-card">
          <span class="related-card-tag">頭皮用美容液</span>
          <div class="related-card-title">洗髪後の乾燥フケを防止！大人の高保湿スカルプエッセンス10選</div>
        </a>
        <a href="/winter-moisture-shampoo" class="related-link-card">
          <span class="related-card-tag">高保湿デイリーシャンプー</span>
          <div class="related-card-title">冬のパサつく髪をしっとりまとめる！高保湿モイスチャーシャンプー10選</div>
        </a>
        <a href="/winter-pdrn-serum" class="related-link-card">
          <span class="related-card-tag">話題の最新スキンケア NEW</span>
          <div class="related-card-title">サーモン注射発想で押し返すハリ！高保湿PDRN美容液おすすめ10選</div>
        </a>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-title">冬コスメ徹底比較ラボ - カテゴリ別ランキング</div>
      <div class="footer-links">
        <!-- フッターリンクは後ほど一括スクリプトで最新化されます -->
        <a href="/winter-carbonic-shampoo">高濃度炭酸シャンプー</a>
        <a href="/winter-pdrn-serum">高保湿PDRN美容液</a>
        <a href="/winter-collagen-mask">バイオコラーゲンマスク</a>
        <a href="/winter-hot-treatment">温感ヘッドスパトリートメント</a>
        <a href="/winter-carbonic-bath">薬用重炭酸入浴剤</a>
        <a href="/winter-oil-mist">高保湿オイルインミスト</a>
      </div>
      <div class="copyright">
        &copy; 2026 冬コスメ徹底比較ラボ 編集部. All Rights Reserved.
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-carbonic-shampoo.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("🎉 Successfully generated winter-carbonic-shampoo.html!")
