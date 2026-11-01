import json
import re

with open("fetched_3nov_dec_needle_salt_gloss_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_bath_salt"]["items"]

salt_details = [
    {
        "rank": 1,
        "tag": "🏆 楽天総合1位独占！純度99%以上国産硫酸マグネシウムが冷えと粉吹きを芯から救済",
        "catch": "海水に含まれる必須ミネラル「エプソムソルト」100%。まるで美容液に全身浸かるような驚異のしっとり保湿温浴",
        "brand_name": "Sea Crystals (シークリスタルス)",
        "capacity": "大容量 2.2kg（約14回分）",
        "type": "純国産高純度エプソムソルト入浴料",
        "features": "硫酸マグネシウム（純度99.9%国産食品添加物基準）、着色料・香料・保存料完全無添加、追い焚き対応",
        "value": "エプソムソルト日本シェアNo.1。スプーン数杯で自宅の浴槽が本格タラソテラピースパに激変する圧倒的コスパ",
        "desc_p1": "11月から12月にかけて日本列島を寒波が覆う時期、どれだけ暖房を強めても手足の先が氷のように冷え、お風呂から上がった直後にすねや太もも、背中がカサカサと粉を吹き始めて猛烈なかゆみに襲われる――そんな『冬の入浴後過乾燥』と『芯冷え』に悩む方に、絶対的な支持を集めているのがシークリスタルスの国産エプソムソルトです。名前に「ソルト（塩）」と付いていますが、食塩（塩化ナトリウム）ではなく、海水から抽出される純粋なミネラル結晶「硫酸マグネシウム」そのものです。",
        "desc_p2": "浴槽にたっぷり溶かすと、無色透明のお湯が驚くほどまろやかで柔らかな肌当たりに変化。硫酸マグネシウムが皮膚表面のタンパク質と結合して目に見えない保護ベールを形成し、入浴中の発汗を促進しながら角層内部の水分蒸発を鉄壁ガードします。さらにマグネシウムが皮膚から経皮吸収されることで、毛細血管が拡張して体の芯まで温まり、お風呂から上がって布団に入るまでポカポカが持続。乾燥によるすねの粉吹きやかゆみが嘘のように鎮まり、吸い付くようなすべすべ美肌へ導かれます。塩分ゼロのため浴槽や風呂釜を痛めず、追い焚きや残り湯洗濯が可能な点も冬の毎日の入浴に最適な理由です。",
        "target": "お風呂上がりに肌が乾燥して粉を吹く・かゆみが出る方、手足の末端冷え性で夜眠れない方、敏感肌や赤ちゃんのいるご家庭",
        "point": "お湯の温度は38〜40℃のぬるめに設定し、150〜200g（付属スプーン約5杯）をしっかり溶かして15〜20分間肩まで浸かるのが、最も発汗と保湿を高める黄金ルールです。"
    },
    {
        "rank": 2,
        "tag": "🌙 ドイツ古代海水の天然岩塩×眠りのハーブ！極寒の夜を深い安眠としっとり潤いで包む",
        "catch": "2億5千万年前の地下海水から精製された純粋岩塩。ホップとバレリアンの深い鎮静アロマで心身をほぐす",
        "brand_name": "Kneipp (クナイプ)",
        "capacity": "ボトル 850g（約21回分）",
        "type": "天然岩塩×植物エッセンシャルオイル配合バスソルト",
        "features": "ルイーゼンハル産天然岩塩、ホップ球果エキス、コウスイガヤ油（バレリアン精油）、無鉱物油・パラベンフリー",
        "value": "ヨーロッパで130年以上の歴史を誇るメディカルハーブ処方。湯上がりのしっとり持続感と睡眠導入効果でリピーター多数",
        "desc_p1": "冬の寒さと年末のプレッシャーで自律神経が乱れ、夜ベッドに入っても体が冷えて眠れない、肌もゴワゴワに乾燥してくすんでいる…という夜に圧倒的な救いとなるのが、ドイツの国民的ハーバルブランド・クナイプの『バスソルト グーテナハト（ホップ＆バレリアンの香り）』です。主原料には、ドイツ・ルイーゼンハル塩鉱の地下460mに眠る、汚染のない古代海水から伝統の平釜製法で結晶化させた極めて純度の高い天然岩塩が使われています。",
        "desc_p2": "ミネラルをたっぷり抱え込んだ多孔質の岩塩結晶が、ヨーロッパで古くから「眠りのハーブ」として親しまれるホップとバレリアンの天然エッセンシャルオイルを贅沢に吸着。お湯に投入した瞬間、深みのある幻想的なブルーに染まり、スパイシーで温かみのあるウッディハーブの香りが浴室いっぱいに広がります。ミネラルヴェールが体熱の放散を防いで体の芯までじっくりと温め、湯上がり後も湯冷め知らず。乾燥で硬くなったひじやひざもしっとり柔らかくほぐれ、深い心地よい眠りへと誘われます。",
        "target": "冷えとストレスで寝つきが悪い方、ハーブの力で本格的なアロマ温浴を楽しみたい方、湯冷めによる肌の乾燥を防ぎたい方",
        "point": "深いブルーのお湯と温かい蒸気を深く胸いっぱいに吸い込みながら深呼吸することで、呼吸器と自律神経がリラックスし、血流促進効果がさらに倍増します。"
    },
    {
        "rank": 3,
        "tag": "💎 創業420年の老舗が誇る純度99.99%！シルクのような極上湯上がり肌へ導くラグジュアリーソルト",
        "catch": "徳島県鳴門の製薬技術が生んだ日本最高峰のエプソムソルト。お湯にとろみが生まれ肌を優雅に磨き上げる",
        "brand_name": "NEHAN TOKYO (ネハントウキョウ)",
        "capacity": "800g（約8回分）",
        "type": "国内最高純度エプソムソルト入浴料",
        "features": "硫酸マグネシウム（徳島県産純度99.99%）、完全無香料・無着色、製薬会社基準の精密精製",
        "value": "徳島県最古の歴史を持つ馬居化成が手掛けるハイエンドバスケア。ギフトや特別な日のセルフメンテナンスに選ばれる最高峰の質感",
        "desc_p1": "慶長4年（1599年）創業という400年以上の歴史を誇る徳島県の硫酸マグネシウムメーカー、馬居化成が東京・青山から発信するラグジュアリーバスブランド『NEHAN TOKYO』のシグネチャー『エプソルト（epsalt）』。一般的な工業用や輸入品とは一線を画し、製薬メーカーとしての厳格な医薬品・食品添加物基準のもとで国内精製された純度99.99%という驚異的なクオリティを誇ります。",
        "desc_p2": "お湯に入れた瞬間にサラサラと溶け去り、浴槽のお湯全体がまるで上質な美容液のようにトロリとなめらかな肌触りへと変化。無駄な添加物を一切排除したピュアなマグネシウムイオンが角層細胞のケラチンタンパクを優しく整え、冬の冷たい外気で硬化・ゴワついた全身の皮膚をシルクのように滑らかで吸い付くような手触りへと生まれ変わらせます。入浴後の肌のつっぱり感が皆無で、まるで高級旅館のアルカリ性単純温泉に浸かったかのような贅沢な美肌体感を味わえます。",
        "target": "肌が極めて敏感で香料や着色料に弱い方、国内最高峰の純度と安全性を求める方、大切な人への冬の温活ギフトを探している方",
        "point": "お好みの天然アロマオイル（ラベンダーやスイートオレンジなど）をエプソルトに2〜3滴垂らしてから浴槽に入れると、自分だけのオリジナル高保湿アロマバスが完成します。"
    },
    {
        "rank": 4,
        "tag": "🍊 天日塩×天然マンダリン精油！冬の乾いた肌を引き締めジューシーな果実香で満たすデイリー名品",
        "catch": "太陽の光で濃縮された天日塩のミネラルが肌をキュッと引き締め。甘く温かみのある柑橘精油で寒さを忘れる",
        "brand_name": "MARKS&WEB (マークスアンドウェブ)",
        "capacity": "スタンドパック 240g（約6〜8回分）",
        "type": "天日乾燥塩×天然精油ハーバルバスソルト",
        "features": "天日乾燥海塩、マンダリン精油、ラベンダー精油、合成着色料フリー、パラベンフリー",
        "value": "良質な自然派コスメを手頃な価格で提供するマークス＆ウェブの定番。日常のバスタイムを上質に格上げする絶妙なブレンド",
        "desc_p1": "シンプルで美しいライフスタイルを提案するマークス＆ウェブの『ハーバルバスソルト マンダリン/ラベンダー』は、海水から結晶化させた天日乾燥塩をベースに、植物から抽出した天然精油をブレンドした人気入浴料です。11月・12月の厳しい寒さの中で凝り固まった肩や背中の筋肉を、温かい湯気とミネラルソルトの温熱作用でじっくりほぐしてくれます。",
        "desc_p2": "海塩に含まれる微量ミネラル成分が肌表面をキュッと健やかに引き締めながら、塩の浸透圧効果によって湯上がりのポカポカ感を長時間保持。完熟したマンダリンオレンジのフレッシュな甘さと、穏やかなフレンチラベンダーのハーバルな香りが絶妙に調和し、冷えた心と体を優しく温め包み込みます。ジッパー付きのスタンドパックで湿気を防ぎ、毎日の気分に合わせて手軽に使える気配り設計も魅力です。",
        "target": "柑橘系のさわやかで温かみのある香りが好きな方、手頃な価格で毎日ハーブ温浴を続けたい方、お風呂上がりの肌の引き締めを求める方",
        "point": "半身浴のお供として、ぬるめのお湯に溶かして読書や音楽を聴きながら20分ほどゆっくり浸かると、驚くほどサラサラの良い汗が出てデトックスを実感できます。"
    },
    {
        "rank": 5,
        "tag": "🌹 死海のミネラル塩×贅沢ローズオイル！湯上がりの全身がもっちり吸い付くサボンの最高傑作",
        "catch": "塩分濃度30%以上の奇跡の湖・死海から採取。ミネラル結晶が溶け出し全身にラグジュアリーな潤いヴェールをまとう",
        "brand_name": "SABON (サボン)",
        "capacity": "ボトル 350g（専用木製スプーン付き）",
        "type": "死海ミネラルソルト×エッセンシャルオイルバスソルト",
        "features": "死海海塩（塩化マグネシウム・カリウム高含有）、ローズ花びらエキス、エッセンシャルアロマオイル",
        "value": "イスラエル発祥のボディケアの頂点SABON。美しいガラスボトルと付属スプーンでバスルームが海外ホテルのスパへ早変わり",
        "desc_p1": "死海の恵みを世界中に広めたボディケアの世界的権威、SABONの『バスソルト ローズ』。イスラエルとヨルダンの国境に位置する死海は、一般の海水の約10倍という圧倒的な塩分・ミネラル濃度を誇る神秘の湖です。その死海の海底から採取された天然塩には、皮膚のバリア機能を修復するマグネシウムや、肌の水分代謝を促進するカリウム、カルシウムなどの微量元素が通常の海塩とは比べものにならない密度で凝縮されています。",
        "desc_p2": "大粒のミネラル結晶と本物のローズの花びら、そして濃密なアロマオイルがお湯の中に優雅に溶け出し、浴室全体がエレガントなバラの庭園のような香りで満たされます。死海ソルト特有の強力な温熱・発汗作用によって毛穴の奥の老廃物を排出しつつ、ミネラルが角層をコーティング。お風呂から上がってタオルで軽く水分を拭き取った瞬間、まるで全身に高保湿ボディオイルを塗り伸ばしたかのような、もっちりと柔らかく吸い付くような肌ざわりに感動します。",
        "target": "冬のご褒美バスタイムを贅沢に過ごしたい方、乾燥でゴワついた全身の肌を柔らかく整えたい方、華やかなローズの香りに包まれたい方",
        "point": "付属の木製スプーンで2大さじほどを湯船に入れ、底に残った大粒のソルトを手のひらで拾ってかかとやひじに優しく馴染ませると、スクラブ効果で角質もつるつるになります。"
    },
    {
        "rank": 6,
        "tag": "🌊 ヨルダン死海最深層の完全無添加ソルト！マグネシウム含有率が驚異的で極寒の冷えを根絶",
        "catch": "天然ミネラルバランスを壊さずに採取した純度100%死海原塩。湯上がり後も湯冷め知らずの持続温熱",
        "brand_name": "BARAKA (バラカ)",
        "capacity": "500g（約5〜10回分）",
        "type": "天然100%死海海塩結晶バスソルト",
        "features": "ヨルダン死海塩100%（マグネシウム・カルシウム・カリウム等21種以上の天然ミネラル）、無香料・無着色・防腐剤完全無添加",
        "value": "高級ホテルスパやサロン専売としても名高いバラカ。香料や着色料を一切加えない原塩そのままの圧倒的な温まりパワー",
        "desc_p1": "ヨルダン国営企業と提携し、死海の中でも最もミネラル濃度が高いとされる最深層（海抜マイナス400m以下）の水から採取された『BARAKA ジョルダニアン デッドシーソルト』。他の死海ソルト製品と決定的に異なるのは、人工的な香料やオイルを一切添加せず、天然のクリスタル塩をそのままパッキングしている点にあります。",
        "desc_p2": "本品の成分分析表を見ると、なんと全体の40%以上がマグネシウムで占められており、塩化ナトリウム（食塩）の割合が極めて低いのが特徴です。そのため、肌への刺激やつっぱり感がなく、お湯がトロンとした感触に変化。お湯に浸かってわずか数分で体の芯からカッカと熱が巡り始め、冬の寒冷でこわばった関節や筋肉がじんわりとほぐれていきます。入浴後も体内に熱が蓄積された状態が長く続き、冷え性による寝つきの悪さを根本から改善します。",
        "target": "重度の冷え性で手足が冷たくて眠れない方、筋肉のコリや疲労感が抜けない方、添加物の入っていない本物の死海ソルトを試したい方",
        "point": "ぬるめのお湯に100gほど贅沢に投入し、15分ほど浸かった後に冷水シャワーを手足の先にサッとかける「温冷浴」を取り入れると、自律神経が整いさらに深い温まりを実感できます。"
    },
    {
        "rank": 7,
        "tag": "🤍 オホーツク海産の自然塩×上品リリー！ミネラル豊富な湯で肌をしっとり保湿する上質バス",
        "catch": "北海道オホーツクの澄んだ海から生まれた自然塩。SHIROの代表的なリリーの香りが浴室いっぱいに広がる",
        "brand_name": "SHIRO (シロ)",
        "capacity": "ジャー 400g（約10回分）",
        "type": "自然海塩×フレグランス高保湿バスソルト",
        "features": "オホーツク海産海塩、ホワイトリリー香料、ミネラル保湿成分、日本製",
        "value": "コスメ界で絶大な人気を誇るSHIROのバスアイテム。インテリアになじむ洗練されたパッケージと清潔感ある極上の香りで大人気",
        "desc_p1": "自然の素材をシンプルに活かす日本のエシカルコスメブランド・SHIROの『ホワイトリリー バスソルト』。北海道・オホーツク海の氷冷で清らかな海水をじっくりと結晶化させたミネラル豊富な自然塩を使用しており、日本の水質やお風呂文化に完璧にマッチした処方が施されています。",
        "desc_p2": "お湯に溶かすと、オホーツクの海塩が水道水の残留塩素の角を丸め、ふんわりと柔らかい肌当たりの湯へと変化。さらにSHIROの代名詞とも言える洗練されたフローラル「ホワイトリリー」の清潔感あふれる香りが浴室に広がり、冬の一日の終わりに溜まったメンタルストレスを穏やかに解き放ちます。肌の水分蒸発を防ぐマイルドなミネラル膜が全身をコートするため、入浴後も肌がカサつかず、翌朝までほのかに心地よい香りが素肌に残ります。",
        "target": "SHIROのホワイトリリーの香りが大好きな方、洗練されたデザインでバスルームをお洒落に彩りたい方、乾燥肌をやさしくいたわりたい方",
        "point": "お風呂から上がる直前に、浴槽のお湯を手ですくってデコルテや首筋にそっと馴染ませると、上品なリリーの香りを纏いながらベッドに入ることができます。"
    },
    {
        "rank": 8,
        "tag": "🌿 海塩×アユーラ独自の安らぎ森林香！冬の張り詰めた気分をほぐし湯冷めを防ぐ癒やしの名品",
        "catch": "東洋医学と瞑想発想が生み出したロングセラーのソルト版。植物精油のヴェールが全身をしっとり保湿シールド",
        "brand_name": "AYURA (アユーラ)",
        "capacity": "300g（約6回分）",
        "type": "瞑想アロマ×海塩メディテーションバスソルト",
        "features": "天日海塩、ローズマリー油、カモミール油、ローズウッド油、安らぎ複合アロマ",
        "value": "コスメ賞を総なめにするアユーラの調香技術。冬の寒さやストレスで張り詰めた交感神経を優位から副交感神経へと切り替える癒やしの極み",
        "desc_p1": "「お風呂で瞑想する」という新しいリフレッシュ体験を提唱し、数々のベストコスメ大賞を受賞してきたアユーラが誇る『メディテーションバスソルト』。天然の海塩に、ローズマリー、カモミール、ローズウッドなどをブレンドしたアユーラ独自のアロマティックハーブの香りを凝縮させた、冬の夜のスペシャルケア入浴料です。",
        "desc_p2": "浴槽にサラサラと注ぐと、心地よいグリーンの香りが広がり、呼吸が自然と深くなります。海塩の温熱発汗作用でじんわりと血行を促進しながら、お湯に溶け出したエッセンシャルオイル成分が肌表面に微細な潤いヴェールを形成。お風呂から出た後も湯冷めを防ぎ、すねや背中の乾燥カサつきを優しくブロックします。仕事や家事で頭がいっぱいになりがちな11月・12月の夜、心と肌を同時にリセットできる名品です。",
        "target": "精神的な緊張やストレスで全身がこわばっている方、アユーラの香りに癒やされたい方、湯上がりの過乾燥を防ぎたい方",
        "point": "照明を少し暗めにして浴室の扉を閉め、温かい蒸気を鼻から深く吸い込んで5秒止めてからゆっくり吐く「マインドフルネス呼吸」を行うと、深いリラクゼーションが得られます。"
    },
    {
        "rank": 9,
        "tag": "🌋 太古の地殻変動が生んだミネラル＆硫黄岩塩！まるで天然温泉のような発汗温浴と保湿力",
        "catch": "ヒマラヤ山脈の地下深くで3億年眠っていた天然ルビーソルト。豊富な還元力と硫黄の香りで自宅が本格湯治場に",
        "brand_name": "天然ヒマラヤ岩塩",
        "capacity": "大容量 1kg（約20〜25回分）",
        "type": "天然ヒマラヤルビー岩塩100%入浴料",
        "features": "ヒマラヤ産天然ブラック/ルビー岩塩（鉄分・カルシウム・カリウム・マグネシウム・天然硫黄）、酸化還元電位マイナス",
        "value": "人工的な添加物ゼロの天然100%岩塩。豊富なミネラルと硫黄成分による温泉効果を1回あたり約100円台で楽しめるコスパの王者",
        "desc_p1": "約3億年前の地殻変動によって海水がマグマの熱で焼き固められ、ヒマラヤ山脈の地下深くに封じ込められた奇跡の結晶『ヒマラヤ岩塩 ルビーソルト』。鉄分や銅、亜鉛などの微量ミネラルを極めて高濃度に含んでいるため美しいルビー色をしており、お湯に溶かすと微量の天然硫黄成分が温泉特有の心地よい香りを漂わせます。",
        "desc_p2": "本品の最大の特徴は、水道水の残留塩素を中和し、酸化還元電位を大きくマイナス（還元方向）へと傾ける強力な抗酸化温浴効果です。まるで山奥の秘湯・天然硫黄温泉に浸かっているかのような本格的な発汗と温まりをもたらし、冬の頑固な冷えや肩こり、関節の重たさを劇的にリフレッシュ。ミネラルが肌の角質層を柔らかくほぐし、湯上がり後は全身がツルツル＆スベスベの陶器肌に仕上がります。",
        "target": "自宅で手軽に本物の温泉気分を味わいたい方、冷えによる頑固なコリやむくみを改善したい方、大容量でコスパを重視する方",
        "point": "硫黄成分が含まれているため、大理石や一部の24時間風呂では使用を避け、入浴後は早めにお湯を抜いて浴槽をシャワーでサッと流すのが浴槽を美しく保つ秘訣です。"
    },
    {
        "rank": 10,
        "tag": "🌲 深みのあるオリエンタルウッディの温感アロマ！冬の乾燥肌をなめらかに包み込む大人の名品",
        "catch": "サンダルウッド（白檀）の優雅な温もり香×天然古代岩塩。冷えた夜をラグジュアリーな静寂と高保湿で満たす",
        "brand_name": "Kneipp (クナイプ)",
        "capacity": "ボトル 850g（約21回分）",
        "type": "天然岩塩×サンダルウッド精油バスソルト",
        "features": "ルイーゼンハル産天然岩塩、サンダルウッド精油、パチョリ精油、無着色・パラベンフリー",
        "value": "大人のリラックスタイムにふさわしい深遠なウッディアロマ。男女問わず愛される上品な香りと天然岩塩の確かな保温力",
        "desc_p1": "クナイプのバスソルトシリーズの中でも、特に冬の寒い夜や自分と向き合う静かな時間に愛用者が急増する隠れた名作『バスソルト サンダルウッドの香り』。古くから寺院や瞑想の場でお香として用いられてきた高貴な香木「白檀（サンダルウッド）」のエッセンシャルオイルに、大地の温もりを感じるパチョリをブレンドした重厚な香りが特徴です。",
        "desc_p2": "クナイプ独自の高純度天然岩塩がお湯に溶け込むことで、温熱効果が長時間持続。サンダルウッドの温かみのあるウッディノートが冷え切った体を芯から包み込み、冬の乾燥によってカサついた皮膚を穏やかに保護します。甘すぎない上品で落ち着いたアロマは男性にも非常に好評で、パートナーと一緒に楽しむ冬の温活バスアイテムとしても絶大な人気を誇ります。",
        "target": "甘い香りよりも深みのあるウッディ・お香のような香りを好む方、冷えた体を落ち着いた空間でじっくり温めたい方",
        "point": "お風呂から上がった後は、同じくウッディ系や無香料の高保湿ボディミルクを塗り伸ばすと、香りの余韻と肌の潤いがさらに長く続きます。"
    }
]

# 比較表データ生成
table_rows = []
for p, item in zip(salt_details, items):
    table_rows.append(f"""
    <tr>
      <td class="rank-cell">第{p['rank']}位</td>
      <td class="brand-cell"><strong>{p['brand_name']}</strong><br><small>{item['display_name'][:25]}...</small></td>
      <td class="price-cell">¥{item['price']:,}</td>
      <td>{p['type']}</td>
      <td>{p['capacity']}</td>
      <td>{p['features']}</td>
    </tr>
    """)

# 商品カードHTML生成
product_cards_html = []
for p, item in zip(salt_details, items):
    product_cards_html.append(f"""
    <article class="product-card" id="rank-{p['rank']}">
      <div class="product-badge">第{p['rank']}位</div>
      <div class="product-header">
        <span class="product-tag">{p['tag']}</span>
        <h3 class="product-title">{p['brand_name']} - {item['display_name']}</h3>
        <p class="product-catch">{p['catch']}</p>
      </div>

      <div class="product-main">
        <div class="product-image-wrap">
          <img src="{item['image_url']}" alt="{p['brand_name']} {item['display_name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-meta-list">
            <div class="meta-item"><span class="meta-label">参考価格：</span><span class="meta-value price-val">¥{item['price']:,}（税込）</span></div>
            <div class="meta-item"><span class="meta-label">内容量：</span><span class="meta-value">{p['capacity']}</span></div>
            <div class="meta-item"><span class="meta-label">ソルト種別：</span><span class="meta-value">{p['type']}</span></div>
            <div class="meta-item"><span class="meta-label">主要成分：</span><span class="meta-value">{p['features']}</span></div>
            <div class="meta-item"><span class="meta-label">取扱店舗：</span><span class="meta-value">{item['shop_name']}</span></div>
          </div>
          <div class="product-points">
            <h4>💡 ここが冬の冷え＆乾燥肌に効く注目ポイント！</h4>
            <p>{p['value']}</p>
          </div>
        </div>
      </div>

      <div class="product-description">
        <h4>【詳細解説＆本音レビュー】</h4>
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>

      <div class="product-advice">
        <div class="advice-block target-block">
          <strong>🎯 こんな人に特におすすめ：</strong>
          <p>{p['target']}</p>
        </div>
        <div class="advice-block tip-block">
          <strong>✨ プロの温浴アドバイス：</strong>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-action">
        <a href="{item['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener noreferrer nofollow">
          <span>楽天市場で最安値＆口コミをチェック</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
    """)

faq_items = [
    {
        "q": "エプソムソルトと普通のバスソルト（海塩・岩塩）の違いは何ですか？",
        "a": "名前に「ソルト」と付いていますが、成分が全く異なります。一般的なバスソルトは塩化ナトリウム（食塩と同じ成分）を含んだ海塩や岩塩ですが、エプソムソルトは塩分を含まない純度100%の『硫酸マグネシウム』という海水ミネラル化合物です。エプソムソルトは塩分ゼロのため浴槽や配管をサビさせず、追い焚きや残り湯での洗濯ができるのが大きなメリットです。一方、岩塩や死海ソルトは微量ミネラルや天然精油との相乗効果による高い発熱・保温効果に優れています。"
    },
    {
        "q": "冬の乾燥肌の場合、お風呂の温度は何℃がベストですか？",
        "a": "冬は寒いからと42℃以上の熱いお湯に入りがちですが、これは乾燥肌にとって最も危険です。42℃を超える高温湯は、肌表面を守っている皮脂膜やセラミドを一気に溶かし出してしまい、お風呂上がりの急激な乾燥（過乾燥）やかゆみの引き金になります。冬の美肌温浴の適温は『38℃〜40℃』のぬるめです。バスソルトやエプソムソルトを溶かせば、ぬるめのお湯でもミネラルの温熱効果によって体の芯までしっかり温まり、皮脂膜を壊さずに潤いを守ることができます。"
    },
    {
        "q": "バスソルトを入れたお風呂のお湯で、追い焚きや洗濯をしても大丈夫ですか？",
        "a": "エプソムソルト（硫酸マグネシウム）は塩分を含まないため、追い焚きや残り湯洗濯（すすぎは清水を使用）が可能です。しかし、天然海塩や岩塩、死海ソルトなどの塩化ナトリウムを含むバスソルトは、金属配管や風呂釜を痛める恐れがあるため、追い焚き機能をオフにし、入浴後は早めにお湯を抜いてシャワーで洗い流すことが推奨されます。各製品の注意書きを必ずご確認ください。"
    },
    {
        "q": "敏感肌やアトピー肌、小さな子どもでも使えますか？",
        "a": "無香料・無着色・高純度のエプソムソルト（シークリスタルスやNEHAN TOKYOなど）は、食品添加物基準を満たしており、水道水の残留塩素を緩和する作用もあるため、敏感肌や生後数ヶ月以降の赤ちゃんでも安心してお使いいただけます。ただし、傷や湿疹がある場合や、硫黄成分・高濃度の精油を含む製品は肌にしみることがありますので、最初は少量から試すかピュアなエプソムソルトを選ぶのが賢明です。"
    },
    {
        "q": "入浴後はシャワーで洗い流したほうがいいですか？そのまま上がるべき？",
        "a": "無添加のエプソムソルトや保湿系バスソルトの場合、肌表面にミネラルの保護ヴェールが形成されているため、シャワーで洗い流さずにそのまま上がるのが最も保湿効果を持続させるポイントです。ただし、大粒の塩の粒が肌に残っていたり、硫黄成分の香りを落としたい場合、または肌が極めて敏感な方は、ぬるめのシャワーでサッと流してからタオルで優しく押さえるように水分を拭き取ってください。"
    }
]

# JSON-LD 構造化データ
json_ld_products = []
for p, item in zip(salt_details, items):
    json_ld_products.append({
        "@type": "Product",
        "name": f"{p['brand_name']} {item['display_name']}",
        "image": item['image_url'],
        "description": p['catch'],
        "brand": {
            "@type": "Brand",
            "name": p['brand_name']
        },
        "offers": {
            "@type": "Offer",
            "price": str(item['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock",
            "url": item['affiliate_url']
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで冬の冷え性・全身カサつき乾燥とさようなら！マグネシウム＆ミネラル温浴で湯上がりしっとり極上肌へ導く高保湿バスソルトランク10",
    "description": "11月・12月の冬の寒冷による末端冷え性・入浴後の全身粉吹き乾燥・かゆみを徹底解決！シークリスタルス、クナイプ、NEHAN TOKYO、MARKS&WEB、SABON、BARAKA、SHIRO、アユーラなど、高純度エプソムソルトや死海ミネラルで芯まで温め肌をうるおす最強高保湿バスソルト10選を徹底比較！",
    "image": items[0]['image_url'],
    "author": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ"
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

json_ld_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": fq["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": fq["a"]
            }
        } for fq in faq_items
    ]
}

json_ld_breadcrumb = {
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
            "name": "高保湿バスソルト特集",
            "item": "https://lumi-cosme.vercel.app/winter-bath-salt"
        }
    ]
}

json_ld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "冬の高保湿バスソルトおすすめ人気ランキング10選",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "item": prod
        } for idx, prod in enumerate(json_ld_products)
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の冷え性・全身カサつき乾燥とさようなら！マグネシウム＆ミネラル温浴で湯上がりしっとり極上肌へ導く高保湿バスソルトランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の寒冷による末端冷え性・入浴後の全身粉吹き乾燥・かゆみを徹底解決！シークリスタルス、クナイプ、NEHAN TOKYO、MARKS&WEB、SABON、BARAKA、SHIRO、アユーラなど、高純度エプソムソルトや死海ミネラルで芯まで温め肌をうるおす最強高保湿バスソルト10選を徹底比較！">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-bath-salt">
  <link rel="icon" href="/favicon.jpg">
  <link rel="stylesheet" href="style.css">

  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで冬の冷え性・全身カサつき乾燥とさようなら！マグネシウム＆ミネラル温浴で湯上がりしっとり極上肌へ導く高保湿バスソルトランク10">
  <meta property="og:description" content="11月・12月の冬の冷え性・入浴後の全身粉吹き乾燥を徹底解決！高純度エプソムソルトや死海ミネラルで芯まで温め肌をうるおす最強高保湿バスソルト10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-bath-salt">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで冬の冷え性・全身カサつき乾燥とさようなら！高保湿バスソルトランク10">
  <meta name="twitter:description" content="11月・12月の冬の冷え性と湯上がり過乾燥を同時にリセット！最強高保湿バスソルト10選を本音レビュー！">
  <meta name="twitter:image" content="{items[0]['image_url']}">

  <!-- 構造化データ JSON-LD -->
  <script type="application/ld+json">
  {json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_faq, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_breadcrumb, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #0284c7;
      --primary-dark: #0369a1;
      --primary-light: #f0f9ff;
      --accent: #38bdf8;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --radius: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
      -webkit-font-smoothing: antialiased;
    }}

    .container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* ヘッダー */
    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 68px;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #0f172a;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .site-nav a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 500;
      transition: color 0.2s;
    }}
    .site-nav a:hover {{ color: var(--primary); }}

    /* パンくずリスト */
    .breadcrumb {{
      padding: 16px 0;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .breadcrumb span {{ margin: 0 8px; }}

    /* 記事ヘッダー */
    .article-header {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 40px;
      margin-bottom: 32px;
      box-shadow: var(--shadow);
      border: 1px solid #e2e8f0;
    }}
    .article-tag-wrap {{
      display: flex;
      gap: 8px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 700;
      background: var(--primary-light);
      color: var(--primary);
    }}
    .article-title {{
      font-size: 2rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .article-meta {{
      display: flex;
      gap: 16px;
      font-size: 0.9rem;
      color: var(--text-muted);
    }}

    /* 本文コンテンツ */
    .article-body {{
      display: flex;
      flex-direction: column;
      gap: 32px;
    }}

    .intro-box, .guide-box, .summary-box {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 36px;
      box-shadow: var(--shadow);
      border: 1px solid #e2e8f0;
    }}
    .intro-box p, .guide-item p, .summary-box p {{
      margin-bottom: 16px;
      font-size: 1.05rem;
    }}
    .intro-box p:last-child, .guide-item p:last-child, .summary-box p:last-child {{
      margin-bottom: 0;
    }}

    .guide-box h2, .ranking-section h2, .comparison-section h2, .faq-section h2, .summary-box h2 {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--primary-light);
      position: relative;
    }}
    .guide-box h2::after, .ranking-section h2::after, .comparison-section h2::after, .faq-section h2::after, .summary-box h2::after {{
      content: "";
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 60px;
      height: 2px;
      background: var(--primary);
    }}

    .guide-item {{
      margin-bottom: 24px;
    }}
    .guide-item:last-child {{
      margin-bottom: 0;
    }}
    .guide-item h3 {{
      font-size: 1.2rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* 比較表 */
    .table-wrap {{
      overflow-x: auto;
      margin-top: 16px;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.95rem;
      text-align: left;
      background: #ffffff;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 14px 16px;
      border-bottom: 1px solid #e2e8f0;
      vertical-align: middle;
    }}
    .comparison-table th {{
      background: #f8fafc;
      font-weight: 700;
      color: #334155;
      white-space: nowrap;
    }}
    .comparison-table tr:hover {{
      background-color: #f0f9ff;
    }}
    .rank-cell {{
      font-weight: 800;
      color: var(--primary);
      white-space: nowrap;
    }}
    .brand-cell strong {{
      color: #0f172a;
    }}
    .price-cell {{
      font-weight: 700;
      color: #e11d48;
      white-space: nowrap;
    }}

    /* ランキングカード */
    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 36px;
      box-shadow: var(--shadow);
      border: 1px solid #e2e8f0;
      position: relative;
      margin-bottom: 40px;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
    }}
    .product-badge {{
      position: absolute;
      top: -16px;
      left: 36px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: #ffffff;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 6px 20px;
      border-radius: 9999px;
      box-shadow: 0 4px 10px rgba(2, 132, 199, 0.3);
    }}
    .product-header {{
      margin-top: 10px;
      margin-bottom: 20px;
    }}
    .product-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 4px 12px;
      border-radius: 6px;
      margin-bottom: 8px;
    }}
    .product-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 8px;
    }}
    .product-catch {{
      font-size: 1rem;
      color: var(--primary-dark);
      font-weight: 600;
    }}

    .product-main {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 28px;
      margin-bottom: 24px;
      background: #f8fafc;
      padding: 24px;
      border-radius: 12px;
    }}
    @media (max-width: 768px) {{
      .product-main {{ grid-template-columns: 1fr; }}
      .article-header {{ padding: 24px; }}
      .article-title {{ font-size: 1.5rem; }}
      .product-card {{ padding: 24px; }}
    }}
    .product-image-wrap {{
      text-align: center;
      background: #ffffff;
      padding: 16px;
      border-radius: 8px;
      border: 1px solid #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .product-img {{
      max-width: 100%;
      max-height: 240px;
      object-fit: contain;
      border-radius: 4px;
    }}
    .product-meta-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 0.95rem;
      margin-bottom: 16px;
    }}
    .meta-item {{
      display: flex;
      gap: 8px;
    }}
    .meta-label {{
      font-weight: 700;
      color: #475569;
      min-width: 90px;
    }}
    .meta-value {{
      color: #0f172a;
    }}
    .price-val {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #e11d48;
    }}
    .product-points {{
      background: #ffffff;
      padding: 16px;
      border-radius: 8px;
      border-left: 4px solid var(--primary);
    }}
    .product-points h4 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 6px;
    }}
    .product-points p {{
      font-size: 0.9rem;
      color: #475569;
      line-height: 1.6;
    }}

    .product-description {{
      margin-bottom: 24px;
    }}
    .product-description h4 {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 12px;
    }}
    .product-description p {{
      font-size: 1rem;
      color: #334155;
      margin-bottom: 12px;
      line-height: 1.8;
    }}

    .product-advice {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 24px;
    }}
    @media (max-width: 640px) {{
      .product-advice {{ grid-template-columns: 1fr; }}
    }}
    .advice-block {{
      padding: 16px;
      border-radius: 8px;
      font-size: 0.9rem;
      line-height: 1.6;
    }}
    .target-block {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1e3a8a;
    }}
    .tip-block {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}
    .advice-block strong {{
      display: block;
      margin-bottom: 6px;
    }}

    .product-action {{
      text-align: center;
      margin-top: 20px;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      max-width: 440px;
      background: linear-gradient(135deg, #bf0000, #e60012);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 1.05rem;
      padding: 16px 24px;
      border-radius: 9999px;
      box-shadow: 0 4px 12px rgba(230, 0, 18, 0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a30000, #cc0010);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(230, 0, 18, 0.35);
    }}

    /* FAQ */
    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .faq-item {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 24px;
    }}
    .faq-q {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 12px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .faq-q span {{
      color: var(--primary);
      font-size: 1.3rem;
      line-height: 1;
    }}
    .faq-a {{
      font-size: 1rem;
      color: #334155;
      line-height: 1.8;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .faq-a span {{
      color: #e11d48;
      font-weight: 800;
      font-size: 1.1rem;
      line-height: 1;
    }}

    /* フッター */
    .site-footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 40px 0;
      margin-top: 60px;
      font-size: 0.9rem;
    }}
    .footer-inner {{
      text-align: center;
    }}
    .footer-copy {{
      margin-top: 16px;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="site-logo">
        <span>✨ 冬コスメ徹底比較ラボ</span>
      </a>
      <nav class="site-nav">
        <a href="/">トップページに戻る</a>
      </nav>
    </div>
  </header>

  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">ホーム</a>
      <span>&gt;</span>
      <a href="/winter-bath-salt">高保湿バスソルト特集</a>
    </nav>
  </div>

  <main class="container">
    <article class="article-body">
      <header class="article-header">
        <div class="article-tag-wrap">
          <span class="badge">冬の全身粉吹き乾燥予防</span>
          <span class="badge">マグネシウム温浴・冷え性改善</span>
          <span class="badge">2026年最新徹底検証</span>
        </div>
        <h1 class="article-title">保湿力の強さで冬の冷え性・全身カサつき乾燥とさようなら！マグネシウム＆ミネラル温浴で湯上がりしっとり極上肌へ導く高保湿バスソルトランク10</h1>
        <div class="article-meta">
          <time datetime="2026-11-02">2026年11月2日更新</time>
          <span class="author">執筆：冬コスメ比較検証チーム</span>
        </div>
      </header>

      <!-- 導入部 -->
      <section class="intro-box">
        <p>
          11月から12月へと本格的な冬将軍が到来する季節、毎晩のお風呂上がりに<strong>「すねや太ももが粉を吹いて白くなる」「パジャマを着た瞬間に背中や腕がチクチクとかゆくなる」「お風呂から上がって30分も経たないうちに足先が氷のように冷え切ってしまう」</strong>という深い不快感に悩まされていませんか。
        </p>
        <p>
          冬の入浴には、実は肌を急激に砂漠化させる大きな落とし穴が存在します。それが皮膚科学で指摘される<strong>「入浴後の過乾燥（過度な水分蒸発）」</strong>です。冷えた体を温めようとして熱いお湯に浸かると、皮膚の最も外側で潤いを守っている皮脂膜と細胞間脂質（セラミド）がお湯の中に溶け出してしまいます。その無防備な状態で浴室から出ると、湿度の低い冬の室気によって肌内部の水分が一気に吸い上げられ、入浴前よりも肌の水分量が激減してしまうのです。
        </p>
        <p>
          この過酷な「冬の冷え」と「湯上がり過乾燥」を同時に根底から解決するのが、近年美容界やアスリートの間で絶大な注目を集める<strong>「高保湿バスソルト＆エプソムソルト（硫酸マグネシウム）」</strong>です。海水や古代岩塩から抽出された純度の高いミネラル成分をお風呂に溶かすと、水道水の塩素の刺激を中和しながら、皮膚表面に目に見えない「疑似ミネラル保護膜」を形成。お湯から上がった瞬間の水分蒸発を物理的にシャットアウトします。
        </p>
        <p>
          さらに、マグネシウムなどの必須ミネラルが皮膚からじんわり経皮吸収されることで、毛細血管を広げて血流を促し、体の深部体温を効率よく上昇させます。ぬるめのお湯でも汗がじんわり吹き出し、湯冷めを防いで朝までポカポカが持続。湯上がり後のボディクリームが不要に思えるほどの極上のしっとり素肌へと生まれ変わります。本記事では、11月・12月の冬に本当に買うべき実力派の高保湿バスソルト10選を徹底検証し、ランキング形式で詳しくご紹介します。
        </p>
      </section>

      <!-- 特集セクション：なぜ冬の乾燥肌にマグネシウム温浴が最強なのか -->
      <section class="guide-box" id="guide-section">
        <h2>冬の「入浴後10分の過乾燥」を防ぐ！バスソルトが全身をしっとり包む3つの生化学的理由</h2>
        <div class="guide-item">
          <h3>1. 皮膚表面に「ミネラル被膜」を形成し、湯上がり直後の水分蒸散をブロック</h3>
          <p>
            入浴後の肌は、毛穴が開き角質層が水分を含んで膨らんでいますが、そのまま放置するとわずか10分間で急激に水分が蒸発し始めます。高保湿バスソルトに含まれるミネラルイオン（マグネシウム、ナトリウム、カルシウム等）は、皮膚表面のケラチンタンパク質と結びついて微細なベールを形成。このベールが天然の蓋となり、入浴でチャージした角層の水分が冬の乾燥した空気中へ逃げ出すのを強力に食い止めます。
          </p>
        </div>
        <div class="guide-item">
          <h3>2. マグネシウムの「経皮吸収」が皮膚のバリア機能（セラミド合成）をバックアップ</h3>
          <p>
            エプソムソルトの主成分である硫酸マグネシウムは、近年の皮膚科学研究において、皮膚から直接吸収されることが確認されています。マグネシウムは角質細胞間脂質の主成分であるセラミドの合成酵素を活性化する重要な補因子（コファクター）として働き、乾燥によってボロボロになった肌のバリア機能を角層レベルから立て直す手助けをします。
          </p>
        </div>
        <div class="guide-item">
          <h3>3. 水道水の残留塩素を緩和し、乾燥敏感肌へのチクチク刺激をゼロに</h3>
          <p>
            日本の水道水には殺菌のための塩素が含まれており、特に冬場の乾燥して敏感になった肌にはピリピリとした刺激や肌荒れの原因になります。天然ソルトやエプソムソルトに含まれるミネラル成分は、お湯の酸化還元電位を下げて塩素の角を優しく丸め、お湯全体をまろやかなトロミ湯へと変化させます。
          </p>
        </div>
      </section>

      <!-- 選び方ガイド -->
      <section class="guide-box">
        <h2>失敗しない！冬用高保湿バスソルトの賢い選び方3つの基準</h2>
        <div class="guide-item">
          <h3>① ソルトの原材料タイプを見極める（エプソムソルト vs 天然岩塩 vs 死海海塩）</h3>
          <p>
            バスソルトには大きく分けて3種類あります。「エプソムソルト（硫酸マグネシウム）」は塩分ゼロで浴槽を痛めず追い焚き・洗濯に最適。「天然岩塩（クナイプやヒマラヤ岩塩）」は太古の地層の豊富な微量元素で温熱保温力が圧倒的。「死海ソルト（デッドシーソルト）」は高濃度の塩化マグネシウムを含み、肌の引き締めと吸い付くような保湿感に優れます。ライフスタイルやお風呂の設備に合わせて選びましょう。
          </p>
        </div>
        <div class="guide-item">
          <h3>② 天然エッセンシャルオイル（精油）の香りと温感アロマ効果</h3>
          <p>
            冬のバスタイムは心身のリフレッシュ空間です。合成香料ではなく、ホップ、バレリアン、ラベンダー、サンダルウッド、マンダリンオレンジなどの100%植物由来の天然精油が配合されたものを選ぶと、湯気とともに立ち上るアロマが嗅覚を通じて自律神経に届き、副交感神経を優位にして質の高い睡眠へと導いてくれます。
          </p>
        </div>
        <div class="guide-item">
          <h3>③ コストパフォーマンスと内容量（毎日たっぷり使える大容量パック）</h3>
          <p>
            バスソルト、特にエプソムソルトは「適切な濃度（お湯の量の約0.1%〜0.2%＝1回あたり150g〜200g）」をしっかり入れないと本来の温浴・保湿効果が発揮されません。ケチらず毎日たっぷり使える大容量パック（2kg〜数kg）を日常用に、香りの高いプレミアムソルトを週末の特別なリラックス用に使い分けるのが最も賢い選択です。
          </p>
        </div>
      </section>

      <!-- 徹底比較表 -->
      <section id="comparison" class="comparison-section">
        <h2>【徹底比較】冬の冷え性と全身の乾燥を救う高保湿バスソルトスペック比較表</h2>
        <div class="table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>ブランド・商品名</th>
                <th>参考価格</th>
                <th>ソルト種別</th>
                <th>内容量</th>
                <th>主要成分・特徴</th>
              </tr>
            </thead>
            <tbody>
              {"".join(table_rows)}
            </tbody>
          </table>
        </div>
      </section>

      <!-- ランキング一覧 -->
      <section id="ranking" class="ranking-section">
        <h2>【2026年最新】11月・12月に買うべき高保湿バスソルトランキング10選</h2>
        {"".join(product_cards_html)}
      </section>

      <!-- 実践テクニック -->
      <section class="guide-box">
        <h2>効果を最大化！冬の肌をしっとり潤す「38〜40℃・20分間温浴メソッド」</h2>
        <div class="guide-item">
          <h3>ステップ1：入浴前にコップ1杯の常温水または白湯を飲む</h3>
          <p>
            高保湿バスソルトを入れたお風呂は非常に発汗作用が高いため、入浴前の水分補給が必須です。あらかじめコップ1杯の水分を摂っておくことで血液の巡りがスムーズになり、毛穴からの老廃物排出とミネラル吸収が格段に促進されます。
          </p>
        </div>
        <div class="guide-item">
          <h3>ステップ2：38〜40℃のぬるめのお湯にソルトを規定量しっかり溶かす</h3>
          <p>
            熱すぎるお湯は肌のセラミドを流出させるため、必ず40℃以下に設定します。規定量（エプソムソルトなら150〜200g、岩塩なら40〜50g）を投入し、手でよくかき混ぜて完全に結晶を溶かしてから湯船に浸かりましょう。
          </p>
        </div>
        <div class="guide-item">
          <h3>ステップ3：肩まで15〜20分浸かり、シャワーで流さず優しくタオルドライ</h3>
          <p>
            首筋までしっかり浸かって深呼吸を繰り返しながら15〜20分間入浴します。お風呂から上がる際は、肌表面に形成されたミネラルの保湿膜を洗い流さないよう、シャワーで流さずにそのままバスタオルで肌をポンポンと優しく押さえるように水分を拭き取るのがしっとり肌を長持ちさせる秘訣です。
          </p>
        </div>
      </section>

      <!-- FAQセクション -->
      <section id="faq-section" class="faq-section">
        <h2>よくある質問（FAQ）：高保湿バスソルトの疑問を徹底解決</h2>
        <div class="faq-list">
          {"".join([f'''
          <div class="faq-item">
            <h3 class="faq-q"><span>Q.</span> {fq["q"]}</h3>
            <p class="faq-a"><span>A.</span> {fq["a"]}</p>
          </div>
          ''' for fq in faq_items])}
        </div>
      </section>

      <!-- まとめセクション -->
      <section class="summary-box">
        <h2>まとめ：冬のバスタイムを「極上の全身美容温活」へとアップデートしよう</h2>
        <p>
          11月から12月にかけての厳しい寒さと乾燥は、放っておくと手足の冷え性や睡眠の浅さ、そして全身の粉吹き肌という形で私たちの心と体を蝕んでいきます。ただ体を洗って温まるだけのルーティンだったお風呂に、ミネラルと自然の恵みが凝縮された高保湿バスソルトを取り入れるだけで、毎晩のバスルームが一流スパのような極上スキンケア空間へと変貌します。
        </p>
        <p>
          今夜からのお風呂タイムを、冷え切った体を芯から解きほぐし、全身をうるおいベールで満たす特別なひとときへとアップグレードさせてください。翌朝布団から出た瞬間の手足の温もりと、すべすべになめらかな吸い付く素肌にきっと心から感動するはずです。
        </p>
      </section>

    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-inner">
      <p class="footer-copy">&copy; 2026 冬コスメ徹底比較ラボ - All Rights Reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-bath-salt.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✓ Created winter-bath-salt.html successfully!")
