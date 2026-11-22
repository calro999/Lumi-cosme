import json
import html

with open("fetched_3new_nov_dec_2026_1123.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

items = all_data["winter_cleansing_water"]["items"]

details = [
    {
        "rank": 1,
        "type_label": "敏感・乾燥肌向けミセラー水の原点",
        "display_name": "サンシビオ エイチツーオー D 500mL",
        "moist_agents": "キュウリ果実エキス、マンニトール、キシリトール、ラムノース（独自D.A.F複合体）",
        "free_spec": "無香料・無着色・アルコールフリー・オイルフリー・弱酸性",
        "wash_needed": "W洗顔不要（洗い流し不要）",
        "capacity": "500mL",
        "catchphrase": "楽天レビュー320件超・★4.6台を誇る大定番。皮脂を取りすぎず潤いバランスを保つ水クレンジングの王道",
        "text_1": "クレンジングウォーターというジャンルを世界中に広めたビオデルマの『サンシビオ エイチツーオー D』。メイクアップアーティストの楽屋やバックステージでも常備される名品ですが、冬の乾燥シーズンに改めて評価したいのが「皮膚の水分バランスを崩しにくい穏やかなミセル設計」です。肌の上で油性メイクだけをミセルの輪に閉じ込めて引き離すため、拭き取った直後の肌がキシまず、さらっとしながら内側に潤いが残ります。",
        "text_2": "今回確認した500mLボトルは¥1,650（調査時点）と大容量かつ手頃で、惜しみなくコットンにたっぷり染み込ませられるのが大きな利点。クレンジングウォーターは液量をケチるとコットン摩擦が起きてしまいますが、この価格帯なら朝晩惜しまずヒタヒタに使えます。11月・12月の寒い朝に冷たい水道水で洗顔したくない日の「拭き取り朝洗顔」としても大活躍します。",
        "scene_fit": "初めてクレンジングウォーターを試す方、朝の冷水洗顔を卒業して摩擦と乾燥を同時に減らしたい方",
        "usage_note": "500円玉大よりひと回り大きい量をコットンに含ませ、決してこすらず頬の上をそっと滑らせます。アイメイク部分は数秒押し当てて浮かせるのがコツです。"
    },
    {
        "rank": 2,
        "type_label": "温泉水×天然ハーブ美容液設計",
        "display_name": "クレンジングウォーター 380mL",
        "moist_agents": "出雲湯村温泉水（SPA水）、シラカンバ樹液、ヨモギ葉エキス、ローズマリー葉エキス",
        "free_spec": "無香料・無着色・石油系鉱物油不使用・アルコールフリー・オイルフリー",
        "wash_needed": "W洗顔不要（洗い流し不要）",
        "capacity": "380mL",
        "catchphrase": "出雲の温泉水と白樺樹液をベースにした国産名品。冬でも化粧水で拭いた後のようなしっとり感が続く",
        "text_1": "日本の映画・ドラマ撮影現場で女優たちの肌を長年支えてきた江原道（Koh Gen Do）の『クレンジングウォーター』。ベースとなる水にミネラル豊富な出雲湯村温泉水を採用し、さらに保湿力に優れたシラカンバ樹液（白樺樹液）や6種類のハーブエキス（セージ・ラベンダー・ヨモギ・ショウガ等）を配合しているため、拭き取り後とは思えないほどしっとりとした後肌に整います。",
        "text_2": "特に嬉しいのが、ワンプッシュでコットンを押し当てて適量を出せるディスペンサー仕様（380mLサイズ）の扱いやすさ（※販売仕様による）。冬の深夜、ヘトヘトになって帰宅したときもボトルを持ち上げる手間すらなくサッとコットンに含ませてオフでき、そのまま布団に入れるほどの保湿感とベタつきのなさを両立しています。",
        "scene_fit": "拭き取り後の「化粧水を塗ったような保湿感」を重視する方、国産・温泉水ベースの優しい使い心地を求める方",
        "usage_note": "マツエクにも対応したオイルフリー処方です。冬の夜は拭き取り後にそのまま寝ることも可能ですが、乾燥が強い日は上からクリームだけ薄く重ねると完璧です。"
    },
    {
        "rank": 3,
        "type_label": "ステージ仕様オフ力×高保湿コスパ",
        "display_name": "クレンジングウォーター 500mL",
        "moist_agents": "ローズマリー葉エキス、カミツレ花エキス、アロエベラ葉エキス（保湿・整肌）",
        "free_spec": "無香料・無着色・オイルフリー・アルコールフリー・パラベンフリー",
        "wash_needed": "W洗顔不要（洗い流し不要）",
        "capacity": "500mL",
        "catchphrase": "楽天レビュー175件超・★4.77の高評価。舞台用メイクも落とす実力と500mLで1,320円の圧倒的続けやすさ",
        "text_1": "バレエや舞台コスメから生まれたチャコットの『クレンジングウォーター』は、肌に優しい水ベースでありながら、落ちにくいベースメイクやポイントメイクにも素早く馴染む実力派として口コミ人気が高い1本です。今回の調査でも500mLで¥1,320、★4.77（175件超）と圧倒的なコストパフォーマンスと支持率を見せています。",
        "text_2": "高機能RO水（超純水レベルに精製された水）をベースに、ローズマリー葉エキスやカミツレ花エキス、アロエベラ葉エキスといった植物保湿成分を組み合わせているため、落ちの良さと肌当たりの柔らかさのバランスが秀逸。「舞台メイク用だから乾燥するのでは？」という先入観を覆すマイルドな質感で、11月・12月の普段使いからイベント時の濃いめメイク落としまで幅広く頼れます。",
        "scene_fit": "しっかりめの冬メイクを擦らず手早く落としたい方、大容量かつ1,500円以下で毎日気兼ねなく使いたい方",
        "usage_note": "濃いめのティントやウォータープルーフマスカラを使った日は、数秒〜10秒ほどコットンを目元・口元に優しく押し当ててから動かすと摩擦を防げます。"
    },
    {
        "rank": 4,
        "type_label": "ナイアシンアミド×浸透型ヒアルロン酸",
        "display_name": "ミセラー クレンジングウォーター セラムモイスト 400mL",
        "moist_agents": "ナイアシンアミド、加水分解ヒアルロン酸（浸透型ヒアルロン酸）、プルラン",
        "free_spec": "無香料・無着色・オイルフリー・アルコールフリー・パラベンフリー",
        "wash_needed": "W洗顔不要（化粧水機能まで1本）",
        "capacity": "400mL",
        "catchphrase": "美容液級保湿成分「ナイアシンアミド＋浸透型ヒアルロン酸」を配合。冬のカサつき肌をみずみずしく保護",
        "text_1": "ドラッグストアでも手軽に買えるビフェスタのクレンジングウォーターシリーズの中でも、乾燥肌・冬の保湿重視派向けに設計されたのが『セラムモイスト』です。化粧水由来の洗浄成分が作るミセル粒子がメイクや汚れを素早く浮き上がらせると同時に、整肌成分のナイアシンアミドと角層へ馴染みやすい加水分解ヒアルロン酸が素肌にうるおいを届けます。",
        "text_2": "さらに肌表面にみずみずしい保護ヴェールを作るプルランが配合されており、11月・12月の暖房が効いた部屋で使ってもツッパリ感が出にくいのが魅力。無香料・アルコールフリー・オイルフリーの低刺激処方でありながら、実勢価格¥990前後（調査時点）と1,000円を切るお財布への優しさも嬉しいポイントです。",
        "scene_fit": "予算1,000円前後で保湿力と成分の充実度を両立したい方、クレンジング〜化粧水までを1ステップで終えたい夜に",
        "usage_note": "コットンにたっぷり3プッシュほど取り、顔の内側から外側へ向かって力を抜いて撫でるように拭き取ります。詰め替え用も市販されているため経済的です。"
    },
    {
        "rank": 5,
        "type_label": "薬用・敏感肌用（医薬部外品）",
        "display_name": "エッセンスイン クレンジングウォーター 180mL (医薬部外品)",
        "moist_agents": "トラネキサム酸（有効成分）、グリチルリチン酸ジカリウム（有効成分）、H-スタビライジングA",
        "free_spec": "無香料・無着色・アルコール（エチルアルコール）無添加・パラベンフリー・低刺激設計",
        "wash_needed": "W洗顔不要（洗い流し不要）",
        "capacity": "180mL",
        "catchphrase": "資生堂dプログラムの薬用拭き取り水。有効成分が冬のゆらぎ・肌荒れを防ぎながら摩擦レスにメイクオフ",
        "text_1": "冬の寒暖差や空気の乾燥で「何を塗っても肌がピリピリしやすい」「赤みやカサつきが出ているのにメイクは落とさなければならない」というときに頼りになるのが、資生堂の敏感肌専門ブランド『dプログラム』の薬用クレンジングウォーターです。肌荒れ防止の有効成分であるトラネキサム酸とグリチルリチン酸ジカリウムを配合した医薬部外品仕様となっています。",
        "text_2": "まるでとろみのある化粧水のようなみずみずしいクッション感があり、コットンで滑らせたときの肌あたりが非常にマイルド。美肌菌に着目した保湿成分も組み込まれており、汚れだけでなく花粉やほこりといった微粒子まで絡め取りながら、洗い上がりはふんわり柔らかな素肌を保ちます。",
        "scene_fit": "冬に肌荒れや乾燥赤みを起こしやすい敏感肌の方、薬用有効成分入りの安心感ある日本ブランドを選びたい方",
        "usage_note": "コットンが乾いた状態で動かすと敏感肌には負担になるため、ディスペンサーでしっかり湿らせてから、なぞるように優しく拭き取ってください。"
    },
    {
        "rank": 6,
        "type_label": "デパコス最高峰トリートメントミセラー水",
        "display_name": "オーミセラーデマキアントヴィサージュ 200mL",
        "moist_agents": "スキンイルミネイター（加水分解シルク・真珠コンキオリン・テアニン等）、Wヒアルロン酸、ローズマリー水GL",
        "free_spec": "弱酸性処方・まつエク対応・天然ローズ＆希少ランの香り",
        "wash_needed": "W洗顔不要（洗い流し不要）",
        "capacity": "200mL",
        "catchphrase": "クレ・ド・ポー ボーテが誇る贅沢な美容液ミセラー水。洗うたびキメが整うような極上の透明感へ",
        "text_1": "「拭き取りクレンジング＝忙しい日の手抜きケア」という常識を覆し、スキンケアの格を一段引き上げてくれるラグジュアリーな1本がクレ・ド・ポー ボーテの『オーミセラーデマキアントヴィサージュ』です。ブランド独自の保湿・整肌複合成分「スキンイルミネイター」やWヒアルロン酸（ヒアルロン酸Na・アセチルヒアルロン酸Na）、弱酸性ローズマリー水GLが配合されています。",
        "text_2": "天然ローズや希少なランをイメージした清らかで上品な香りに包まれながらコットンで軽く拭うと、メイクや大気中の微粒子汚れがスッと消える一方で、素肌はまるで上質なローションでパッティングした直後のような瑞々しさに。年末年始のご褒美ケアや、冬の朝の贅沢な拭き取り洗顔としても圧倒的な満足感があります。",
        "scene_fit": "デパコス品質の保湿力と香りを楽しみながらケアしたい方、大人のくすみやキメの乱れを防ぎたい方",
        "usage_note": "朝の洗顔代わりとして使う場合はコットンに2プッシュほど取り、顔全体を軽く拭うだけでその後の美容液や乳液のノリが見違えます。"
    },
    {
        "rank": 7,
        "type_label": "天然温泉水ベース・乾燥肌特化処方",
        "display_name": "サーマル クレンジングウォーター (乾燥肌用) 250mL",
        "moist_agents": "ユリアージュ温泉水、クランベリー果実エキス、グリセリン",
        "free_spec": "アルコールフリー・パラベンフリー・眼科テスト済み（コンタクト対応）",
        "wash_needed": "W洗顔不要（洗い流し不要）",
        "capacity": "250mL",
        "catchphrase": "フランスの天然アイソトニック温泉水をベースに、乾燥肌向けの保湿エキスを配合した穏やかな使い心地",
        "text_1": "フランス南東部のアルプス山脈に湧き出る天然温泉水を主成分とするスキンケアブランド『ユリアージュ』の乾燥肌専用クレンジングウォーターです。ユリアージュの温泉水は人間の体液と浸透圧が近い「アイソトニック温泉水」であることが知られており、肌に乗せたときのなじみが非常に良く、拭き取り中も水分を奪いにくいのが特徴です。",
        "text_2": "さらに乾燥肌タイプには保湿成分であるクランベリー果実エキスを配合し、つっぱりやすい冬の素肌をしっとりと保護。眼科テスト済みでデリケートな目元にもしみにくく、フルーティーでほのかな清潔感ある香りで心地よくメイクオフができます。250mLで¥1,936前後（調査時点）と手に取りやすい価格も魅力です。",
        "scene_fit": "洗顔後に皮膚がパキパキにつっぱりやすい極度の乾燥肌の方、フランスのダーマコスメを試したい方",
        "usage_note": "乾燥が特に気になる12月は、夜のクレンジング後に洗い流さずそのまま保湿化粧水・乳液・クリームを重ねると温泉水の潤いを逃しにくくなります。"
    },
    {
        "rank": 8,
        "type_label": "弱酸性pH5.5×パンテンソシド鎮静",
        "display_name": "スンジョン クレンジングウォーター 300mL",
        "moist_agents": "パンテノール、マデカッソシド（ツボクサ由来）、チャ葉エキス",
        "free_spec": "10無添加処方（無香料・無着色・鉱物油・パラベン・シリコン等不使用）・弱酸性pH5.5・ヴィーガン認証",
        "wash_needed": "ノーウォッシュ設計（W洗顔不要）",
        "capacity": "300mL",
        "catchphrase": "楽天公式★4.7台の高評価。パンテノールとマデカッソシドの鎮静コンビが冬のゆらぎ肌を優しく守る",
        "text_1": "敏感肌ラインとして日本でもファンが多いエチュードの『スンジョン』シリーズから展開されている弱酸性（pH5.5）クレンジングウォーター。健康な素肌と同じ弱酸性バランスを保ちながらメイクをオフできるため、クレンジング後に肌が赤くなったりヒリヒリしたりしやすい冬場に心強い存在です。",
        "text_2": "注目すべきは保湿の「パンテノール」と整肌の「マデカッソシド」を組み合わせた通称パンテンソシド処方。さらに動物性原料や鉱物油、香料、シリコンなどを排除した10無添加・ヴィーガン設計になっており、朝の拭き取り洗顔にも夜のナチュラルメイクオフにも毎日安心して取り入れられます。",
        "scene_fit": "韓国の低刺激ヴィーガン処方を好む方、寒暖差や花粉・マスク擦れで肌が敏感に傾きやすい方",
        "usage_note": "コットンに十分含ませて頬や額を撫でるように拭き取ったあと、小鼻など皮脂が気になる部分は新しいきれいな面で軽く押さえると清潔に保てます。"
    },
    {
        "rank": 9,
        "type_label": "500mL大容量×トリプルミセラ角質ケア",
        "display_name": "ピュアソイビーン クレンジングウォーター 500mL",
        "moist_agents": "ヒアルロン酸Naクロスポリマー、ナシ花エキス、PHA（グルコノラクトン）・LHA（カプリロイルサリチル酸）",
        "free_spec": "100%ヴィーガン処方・弱酸性設計・大容量500mL",
        "wash_needed": "W洗顔不要（洗い流し不要）",
        "capacity": "500mL",
        "catchphrase": "楽天公式★4.85の高評価！500mL大容量で冬のゴワつき角質も穏やかに整えながら潤いを残す",
        "text_1": "クレンジングオイルで絶大な人気を誇る韓国ブランド『魔女工場（ma:nyo）』のクレンジングウォーターは、500mLのビッグサイズで公式★4.85（27件超）という高い評価を獲得しています。親水性と親油性を兼ね備えたトリプルミセラ工法により、日焼け止めやベースメイク、毛穴の老廃物まで素早くキャッチします。",
        "text_2": "冬場に嬉しいポイントが、水分保持をサポートするヒアルロン酸Naクロスポリマーや植物性エキスに加え、刺激が穏やかな次世代角質ケア成分であるPHA（グルコノラクトン）やLHAを少量バランスよく配合していること。寒さで角質が硬くくすみやすい11月・12月の肌を、こすらずつるんと柔らかな手触りへ導きます。",
        "scene_fit": "冬に角質が厚くなって肌がゴワつきやすい方、500mLの大容量を惜しみなく使いたい韓国スキンケア派の方",
        "usage_note": "ポンプ式や大容量ボトルは洗面所に置きやすく、帰宅してすぐメイクを落とす習慣づくりにぴったり。拭き取り後は軽くハンドプレスで水分を落ち着かせるとさらに馴染みます。"
    },
    {
        "rank": 10,
        "type_label": "皮膚科学発想・敏感な目元にも対応",
        "display_name": "ミセラーウォーター ウルトラ 200mL",
        "moist_agents": "ラ ロッシュ ポゼ ターマルウォーター（整肌・保湿）、グリセリン",
        "free_spec": "パラベンフリー・アルコールフリー・着色料フリー・石けん成分フリー",
        "wash_needed": "W洗顔不要（洗い流し不要）",
        "capacity": "200mL",
        "catchphrase": "敏感肌と敏感な目元を見据えた処方。グリセリンとターマルウォーターが拭き取り後の乾きをブロック",
        "text_1": "世界中の皮膚科医が採用する仏ダーマコスメブランド『ラ ロッシュ ポゼ』のミセラーウォーター。整肌成分として名高いラ ロッシュ ポゼ ターマルウォーターをベースに、保水力のあるグリセリンをしっかり組み合わせることで、汚れを浮かせたあとの肌表面を乾いた空気にさらさずしっとり保ちます。",
        "text_2": "※今回楽天市場から取得した出品商品はインポート表記（エファクラ ミセラーウォーター ウルトラ 敏感肌＆敏感な目元用）となっていますが、ミセラー粒子がメイクや大気中の汚れをやさしく取り除きつつ、アルコールやパラベン・石けん成分を使わない低刺激設計で敏感な目元にも配慮されています。冬の乾燥肌でもつっぱり感を抑えたい方におすすめです。",
        "scene_fit": "敏感肌でダーマコスメの信頼性を重視する方、目元周りにも安心して使えるアルコールフリー水クレンジングをお探しの方",
        "usage_note": "目元を拭くときは、液をたっぷり含ませたまつ毛の上で3〜5秒そっと止めてから下に流すようにすると、こすらず綺麗に落ちます。"
    }
]

article_title = "保湿力の強さで冬洗顔のつっぱりとさようなら！W洗顔不要の高保湿クレンジングウォーター（ミセラー水）ランク10【11月・12月】"
article_desc = "11月・12月の寒い洗面所で冷たい水洗顔がつらい夜や乾燥する朝に最適！ビオデルマ、江原道、チャコット、ビフェスタ、資生堂dプログラム、クレ・ド・ポー ボーテ、ユリアージュ、エチュード スンジョン、魔女工場、ラロッシュポゼまで高保湿クレンジングウォーター10選を徹底比較。"
canonical_url = "https://lumi-cosme.vercel.app/winter-cleansing-water"

json_ld_graph = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": article_title,
            "description": article_desc,
            "image": items[0]["image_url"],
            "datePublished": "2026-11-23T05:00:00+09:00",
            "dateModified": "2026-11-23T05:00:00+09:00",
            "author": {"@type": "Organization", "name": "Lumi Cosme 編集部"},
            "publisher": {
                "@type": "Organization",
                "name": "Lumi Cosme (ルミコスメ)",
                "logo": {"@type": "ImageObject", "url": "https://lumi-cosme.vercel.app/favicon.jpg"}
            }
        },
        {
            "@type": "ItemList",
            "name": "11月・12月向け高保湿クレンジングウォーター（ミセラー水）10選",
            "numberOfItems": 10,
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": it["rank"],
                    "item": {
                        "@type": "Product",
                        "name": f"{it['brand']} {det['display_name']}",
                        "image": it["image_url"],
                        "description": det["catchphrase"],
                        "brand": {"@type": "Brand", "name": it["brand"]},
                        "offers": {
                            "@type": "Offer",
                            "price": it["price"],
                            "priceCurrency": "JPY",
                            "availability": "https://schema.org/InStock",
                            "url": it["affiliate_url"]
                        },
                        **(
                            {
                                "aggregateRating": {
                                    "@type": "AggregateRating",
                                    "ratingValue": str(it["review_average"]),
                                    "reviewCount": int(it["review_count"])
                                }
                            }
                            if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
                            else {}
                        )
                    }
                }
                for it, det in zip(items, details)
            ]
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "クレンジングウォーターだけで冬のメイクは本当に落ちますか？W洗顔は必要ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "今回紹介した10製品はいずれも『ミセル構造（親油基と親水基を持つ微細な粒子）』でファンデーションや皮脂汚れを浮かせてコットンに絡め取る設計になっており、基本的にW洗顔不要（洗い流し不要）です。ただしウォータープルーフの強力なマスカラやティント口紅を使った日は、ポイントメイクリムーバーを併用すると摩擦を防げます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "コットンで拭き取ると、かえって冬は乾燥や摩擦ダメージが起きませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "摩擦を防ぐ鉄則は『コットンの裏までしっかり透けるほどの液量』を使うことです。液が足りないとコットンの繊維が直接肌をこすってしまいます。たっぷり含ませた大判コットンを肌にそっと乗せ、力を抜いて一方向に滑らせれば、冷たい水道水や熱いお湯で皮脂膜を流すよりも潤いを守りやすくなります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "11月・12月の朝洗顔の代わりにクレンジングウォーターを使っても良いですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい、冬の朝洗顔代わりとして非常に合理的です。就寝中に分泌された皮脂やホコリ、夜塗ったクリームの残りを水洗顔なしで穏やかにオフでき、同時に保湿成分（温泉水・ヒアルロン酸・ナイアシンアミド・パンテノールなど）を角層に残せます。拭き取った後はすぐに化粧水や乳液で保湿を仕上げましょう。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "拭き取り後にベタつきや界面活性剤が残る感覚が気になる場合はどうすればいいですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "製品設計上はそのまま保湿ステップへ進んで問題ありませんが、使用感が気になる場合はぬるま湯（32〜34℃程度）でさっと1〜2回すすぐか、精製水・ミスト化粧水を軽く吹きかけてティッシュで押さえてから乳液・クリームを重ねると快適です。"
                    }
                }
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://lumi-cosme.vercel.app/"},
                {"@type": "ListItem", "position": 2, "name": "冬の高保湿クレンジング特集", "item": "https://lumi-cosme.vercel.app/winter-cleansing"},
                {"@type": "ListItem", "position": 3, "name": "高保湿クレンジングウォーター10選", "item": canonical_url}
            ]
        }
    ]
}

table_rows = ""
for it, det in zip(items, details):
    table_rows += f"""            <tr>
              <td class="cw-rank">{it['rank']}位</td>
              <td><strong>{html.escape(it['brand'])}</strong><div class="cw-sub">{html.escape(det['display_name'])}</div></td>
              <td>{html.escape(det['moist_agents'])}</td>
              <td>{html.escape(det['free_spec'])}</td>
              <td class="cw-price">¥{it['price']:,}<div class="cw-sub">{html.escape(det['capacity'])}</div></td>
            </tr>
"""

cards_html = ""
for it, det in zip(items, details):
    rate_pill = (
        f'<span class="cw-rate">★ {it["review_average"]} ({it["review_count"]:,}件)</span>'
        if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
        else '<span class="cw-rate">楽天市場 在庫確認済</span>'
    )
    cards_html += f"""
      <article class="cw-card" id="item-{it['rank']}">
        <div class="cw-card-head">
          <div class="cw-badges">
            <span class="cw-rank-pill">第{it['rank']}位</span>
            <span class="cw-type-pill">{html.escape(det['type_label'])}</span>
            {rate_pill}
          </div>
          <h3>{html.escape(it['brand'])} {html.escape(det['display_name'])}</h3>
          <p class="cw-catch">{html.escape(det['catchphrase'])}</p>
        </div>

        <div class="cw-body-grid">
          <div class="cw-left">
            <div class="cw-img-wrap">
              <img src="{html.escape(it['image_url'])}" alt="{html.escape(it['brand'])} {html.escape(det['display_name'])}" class="product-img" loading="lazy">
            </div>
            <div class="cw-price-card">
              <span class="cw-p-lbl">楽天市場 最新確認価格（税込）</span>
              <span class="cw-p-val">¥{it['price']:,}</span>
            </div>
            <a href="{html.escape(it['affiliate_url'])}" target="_blank" rel="noopener noreferrer nofollow sponsored" class="rakuten-btn">
              楽天市場で最新価格・詳細を見る →
            </a>
            <div class="cw-sku">対象商品：{html.escape(it['item_name'][:52])}</div>
          </div>

          <div class="cw-right">
            <dl class="cw-specs">
              <div><dt>主要保湿・整肌成分</dt><dd>{html.escape(det['moist_agents'])}</dd></div>
              <div><dt>低刺激・フリー設計</dt><dd>{html.escape(det['free_spec'])}</dd></div>
              <div><dt>W洗顔の要否</dt><dd>{html.escape(det['wash_needed'])}</dd></div>
              <div><dt>容量</dt><dd>{html.escape(det['capacity'])}</dd></div>
            </dl>

            <div class="cw-prose">
              <p>{html.escape(det['text_1'])}</p>
              <p>{html.escape(det['text_2'])}</p>
            </div>

            <div class="cw-tips">
              <div class="cw-tip-box">
                <strong>冬のこんなシーンにおすすめ</strong>
                <p>{html.escape(det['scene_fit'])}</p>
              </div>
              <div class="cw-tip-box">
                <strong>乾燥・摩擦を防ぐ使い方のコツ</strong>
                <p>{html.escape(det['usage_note'])}</p>
              </div>
            </div>
          </div>
        </div>
      </article>
"""

html_doc = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(article_title)} | Lumi Cosme</title>
  <meta name="description" content="{html.escape(article_desc)}">
  <meta name="keywords" content="クレンジングウォーター 乾燥肌 冬, ミセラーウォーター 保湿, W洗顔不要 メイク落とし 11月 12月, ビオデルマ サンシビオ, 江原道 クレンジングウォーター, チャコット クレンジングウォーター, ビフェスタ セラムモイスト, dプログラム エッセンスイン クレンジングウォーター">
  <link rel="canonical" href="{canonical_url}">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Lumi Cosme (ルミコスメ)">
  <meta property="og:title" content="{html.escape(article_title)}">
  <meta property="og:description" content="{html.escape(article_desc)}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{html.escape(items[0]['image_url'])}">
  <meta property="og:locale" content="ja_JP">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
{json.dumps(json_ld_graph, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --ice: #0284c7;
      --ice-deep: #0c4a6e;
      --ice-soft: #f0f9ff;
      --ice-border: #bae6fd;
      --slate-bg: #f8fafc;
      --ink: #0f172a;
      --muted: #475569;
      --line: #e2e8f0;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      background: var(--slate-bg);
      color: var(--ink);
      line-height: 1.78;
    }}
    .top-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--line);
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .top-header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 13px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .site-brand {{ font-weight: 800; font-size: 1.12rem; color: var(--ice-deep); text-decoration: none; }}
    .top-nav {{ display: flex; gap: 14px; flex-wrap: wrap; font-size: 0.85rem; }}
    .top-nav a {{ color: var(--ice); font-weight: 700; text-decoration: none; }}
    .crumb {{ max-width: 1080px; margin: 14px auto 0; padding: 0 20px; font-size: 0.82rem; color: var(--muted); }}
    .crumb a {{ color: var(--ice); text-decoration: none; }}
    main {{ max-width: 1080px; margin: 20px auto 64px; padding: 0 20px; }}

    .cw-hero {{
      background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
      border: 1px solid var(--ice-border);
      border-radius: 16px;
      padding: 36px 30px;
      margin-bottom: 26px;
    }}
    .cw-tag {{
      display: inline-block;
      background: var(--ice);
      color: #fff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }}
    .cw-hero h1 {{
      font-size: 1.7rem;
      line-height: 1.42;
      color: var(--ice-deep);
      margin-bottom: 12px;
    }}
    .cw-meta {{ font-size: 0.84rem; color: var(--muted); margin-bottom: 14px; }}
    .cw-hero p {{ font-size: 0.96rem; margin-bottom: 10px; }}

    .quick-pick-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 14px;
      margin-bottom: 28px;
    }}
    .qp-card {{
      background: #fff;
      border: 1px solid var(--ice-border);
      border-top: 4px solid var(--ice);
      border-radius: 12px;
      padding: 16px 18px;
    }}
    .qp-label {{ font-size: 0.76rem; font-weight: 800; color: var(--ice); display: block; margin-bottom: 4px; }}
    .qp-card strong {{ display: block; font-size: 0.98rem; color: var(--ice-deep); margin-bottom: 6px; }}
    .qp-card p {{ font-size: 0.84rem; color: var(--muted); margin: 0; }}

    .cw-toc {{
      background: #fff;
      border: 1px solid var(--line);
      border-left: 5px solid var(--ice);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 28px;
    }}
    .cw-toc h2 {{ font-size: 1.05rem; color: var(--ice-deep); margin-bottom: 10px; }}
    .cw-toc ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 6px 18px;
    }}
    .cw-toc a {{ color: var(--ice); text-decoration: none; font-size: 0.91rem; font-weight: 600; }}

    .cw-section {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 28px;
      margin-bottom: 28px;
    }}
    .cw-section h2 {{
      font-size: 1.32rem;
      color: var(--ice-deep);
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--ice-soft);
    }}
    .cw-section p {{ font-size: 0.96rem; margin-bottom: 12px; }}

    .cw-3grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin-top: 14px;
    }}
    .cw-pillar {{
      background: var(--ice-soft);
      border: 1px solid var(--ice-border);
      border-radius: 12px;
      padding: 18px;
    }}
    .cw-pillar h3 {{ font-size: 1rem; color: var(--ice-deep); margin-bottom: 8px; }}
    .cw-pillar p {{ font-size: 0.88rem; margin: 0; }}

    .tbl-wrap {{ overflow-x: auto; margin-top: 14px; }}
    .cw-table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 740px;
      font-size: 0.87rem;
    }}
    .cw-table th {{
      background: var(--ice-deep);
      color: #fff;
      text-align: left;
      padding: 11px 12px;
    }}
    .cw-table td {{
      padding: 12px;
      border-bottom: 1px solid var(--line);
      vertical-align: top;
    }}
    .cw-table tr:nth-child(even) td {{ background: #f8fafc; }}
    .cw-rank {{ font-weight: 800; color: var(--ice); white-space: nowrap; }}
    .cw-price {{ font-weight: 700; color: var(--ice-deep); white-space: nowrap; }}
    .cw-sub {{ font-size: 0.77rem; color: var(--muted); font-weight: 400; margin-top: 2px; }}

    .rank-heading {{
      font-size: 1.4rem;
      color: var(--ice-deep);
      margin: 32px 0 18px;
      padding-left: 12px;
      border-left: 5px solid var(--ice);
    }}
    .cw-card {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 26px;
      margin-bottom: 24px;
      box-shadow: 0 2px 10px rgba(2, 132, 199, 0.05);
    }}
    .cw-card-head {{ margin-bottom: 18px; }}
    .cw-badges {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 10px; }}
    .cw-rank-pill {{
      background: var(--ice-deep);
      color: #fff;
      font-weight: 800;
      font-size: 0.8rem;
      padding: 4px 11px;
      border-radius: 6px;
    }}
    .cw-type-pill {{
      background: var(--ice-soft);
      color: var(--ice);
      border: 1px solid var(--ice-border);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .cw-rate {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #b45309;
      background: #fef3c7;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .cw-card-head h3 {{ font-size: 1.24rem; color: var(--ink); margin-bottom: 6px; }}
    .cw-catch {{ font-size: 0.92rem; color: var(--ice); font-weight: 700; }}

    .cw-body-grid {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 24px;
      align-items: start;
    }}
    .cw-img-wrap {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 12px;
      text-align: center;
      margin-bottom: 12px;
    }}
    .product-img {{ max-width: 100%; height: 210px; object-fit: contain; }}
    .cw-price-card {{
      background: var(--ice-soft);
      border-radius: 10px;
      padding: 10px 12px;
      text-align: center;
      margin-bottom: 10px;
    }}
    .cw-p-lbl {{ display: block; font-size: 0.74rem; color: var(--muted); }}
    .cw-p-val {{ font-size: 1.35rem; font-weight: 800; color: var(--ice-deep); }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      text-align: center;
      background: #bf0000;
      color: #fff;
      font-weight: 800;
      font-size: 0.9rem;
      padding: 12px 14px;
      border-radius: 8px;
      text-decoration: none;
    }}
    .rakuten-btn:hover {{ background: #990000; }}
    .cw-sku {{ margin-top: 8px; font-size: 0.72rem; color: var(--muted); line-height: 1.4; word-break: break-all; }}

    .cw-specs {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      background: #f8fafc;
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 12px 14px;
      margin-bottom: 14px;
      font-size: 0.84rem;
    }}
    .cw-specs div dt {{ font-size: 0.73rem; color: var(--muted); }}
    .cw-specs div dd {{ font-weight: 700; color: var(--ink); margin: 0; }}
    .cw-prose p {{ font-size: 0.94rem; margin-bottom: 10px; }}
    .cw-tips {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: 12px;
    }}
    .cw-tip-box {{
      background: var(--ice-soft);
      border: 1px solid var(--ice-border);
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 0.85rem;
    }}
    .cw-tip-box strong {{ display: block; color: var(--ice-deep); margin-bottom: 4px; }}
    .cw-tip-box p {{ margin: 0; font-size: 0.84rem; }}

    .cw-step-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 14px;
      margin-top: 14px;
    }}
    .cw-step {{
      background: #f8fafc;
      border: 1px solid var(--line);
      border-top: 4px solid var(--ice);
      border-radius: 10px;
      padding: 16px;
    }}
    .cw-step h3 {{ font-size: 0.96rem; color: var(--ice-deep); margin-bottom: 6px; }}
    .cw-step p {{ font-size: 0.86rem; margin: 0; }}

    .faq-row {{ border-bottom: 1px solid var(--line); padding: 14px 0; }}
    .faq-row:last-child {{ border-bottom: none; }}
    .faq-row h3 {{ font-size: 1rem; color: var(--ice-deep); margin-bottom: 6px; }}
    .faq-row p {{ font-size: 0.92rem; margin: 0; }}

    .internal-links-box {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 24px;
      margin-top: 32px;
    }}
    .internal-links-title {{ font-weight: 800; font-size: 1.08rem; color: var(--ice-deep); margin-bottom: 14px; }}
    .internal-links-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; }}
    .internal-link-card {{ border: 1px solid var(--line); border-radius: 10px; padding: 12px; text-decoration: none; display: block; }}
    .internal-link-card:hover {{ border-color: var(--ice); }}

    footer {{ background: #0f172a; color: #94a3b8; padding: 44px 20px 30px; font-size: 0.84rem; }}
    .footer-inner {{ max-width: 1080px; margin: 0 auto; }}
    .footer-title {{ color: #f8fafc; font-weight: 800; margin-bottom: 14px; }}
    .footer-links-grid {{ display: flex; flex-wrap: wrap; gap: 8px 14px; margin-bottom: 24px; }}
    .footer-links-grid a {{ color: #cbd5e1; text-decoration: none; font-size: 0.8rem; }}
    .footer-links-grid a:hover {{ color: #7dd3fc; text-decoration: underline; }}
    .copyright {{ border-top: 1px solid #1e293b; padding-top: 18px; text-align: center; font-size: 0.78rem; }}

    @media (max-width: 760px) {{
      .cw-hero {{ padding: 24px 18px; }}
      .cw-hero h1 {{ font-size: 1.32rem; }}
      .cw-body-grid, .cw-specs, .cw-tips {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header class="top-header">
    <div class="top-header-inner">
      <a href="/" class="site-brand">Lumi Cosme</a>
      <nav class="top-nav">
        <a href="/winter-cleansing">クレンジング総合</a>
        <a href="/winter-wipe-lotion">朝用ふき取り化粧水</a>
        <a href="/winter-point-makeup-remover">ポイントリムーバー</a>
      </nav>
    </div>
  </header>

  <nav class="crumb" aria-label="パンくずリスト">
    <a href="/">ホーム</a> &gt; <a href="/winter-cleansing">冬の高保湿クレンジング総合</a> &gt; <span>高保湿クレンジングウォーター10選</span>
  </nav>

  <main>
    <section class="cw-hero">
      <span class="cw-tag">2026年11月・12月 冬の摩擦レス・時短オフ特集</span>
      <h1>{html.escape(article_title)}</h1>
      <div class="cw-meta">更新日：<time datetime="2026-11-23">2026年11月23日</time> ／ 編集部・スキンケアリサーチ</div>
      <p>
        11月下旬から12月にかけて朝の気温がひと桁台まで落ち込むと、冷え切った洗面所で水道水を顔にかけるのも、あるいは乾燥を防ぐためにぬるま湯の温度を微調整するのも、毎日の小さなストレスになっていきます。年末に向けて仕事や忘年会が重なって遅く帰宅した夜などは、「いますぐ暖房の効いた部屋でメイクを落として眠りたい」と感じる日も増えるはずです。
      </p>
      <p>
        そんな冬の朝と夜を快適に変えてくれるのが、<strong>W洗顔不要・保湿成分ベースの高保湿クレンジングウォーター（ミセラー水）</strong>です。水で洗い流さなくても親油基と親水基のミセル粒子がメイクや汚れだけを絡め取り、肌に必要な皮脂膜やセラミドの流出を抑えてくれます。本記事では、ツッパリ感の少なさと低刺激処方にこだわって選んだ名品10本を、楽天市場の最新確認価格とともに徹底比較します。
      </p>
    </section>

    <section class="quick-pick-grid" aria-label="タイプ別おすすめ結論">
      <div class="qp-card">
        <span class="qp-label">王道＆コスパ最強</span>
        <strong>ビオデルマ サンシビオ / チャコット</strong>
        <p>500mLが1,300〜1,600円台。惜しみなくコットンをヒタヒタにできるため摩擦レスの入門に最適です。</p>
      </div>
      <div class="qp-card">
        <span class="qp-label">敏感・冬荒れ肌向け</span>
        <strong>dプログラム / ユリアージュ / スンジョン</strong>
        <p>薬用有効成分や温泉水・パンテンソシドなど、寒暖差でゆらぐ肌を守る低刺激設計が光ります。</p>
      </div>
      <div class="qp-card">
        <span class="qp-label">極上保湿＆朝洗顔兼用</span>
        <strong>江原道 / クレ・ド・ポー ボーテ</strong>
        <p>温泉水＋白樺樹液やスキンイルミネイター配合で、拭いた直後から化粧水をつけた後のような潤い感。</p>
      </div>
      <div class="qp-card">
        <span class="qp-label">高機能成分＆角質整え</strong>
        <strong>ビフェスタ セラムモイスト / 魔女工場</strong>
        <p>ナイアシンアミドやPHA配合で、冬にゴワつきやすい角質を穏やかに整えながらみずみずしくオフ。</p>
      </div>
    </section>

    <nav class="cw-toc" aria-label="目次">
      <h2>この記事でわかること</h2>
      <ul>
        <li><a href="#why-micellar">1. 冬にあえて「クレンジングウォーター」を選ぶ合理的理由</a></li>
        <li><a href="#how-to-choose">2. 乾燥肌が失敗しない高保湿ミセラー水 3つの見極め軸</a></li>
        <li><a href="#compare-matrix">3. 高保湿クレンジングウォーター10選 スペック比較表</a></li>
        <li><a href="#ranking-detail">4. 保湿力高めクレンジングウォーター厳選10選レビュー</a></li>
        <li><a href="#zero-friction">5. コットン摩擦をゼロにする冬の正しい拭き取り4手順</a></li>
        <li><a href="#cw-faq">6. クレンジングウォーターの疑問 Q&amp;A</a></li>
      </ul>
    </nav>

    <section class="cw-section" id="why-micellar">
      <h2>1. なぜ冬は「お湯すすぎ」より「高保湿ミセラー水」が乾きにくいのか</h2>
      <p>
        冬のクレンジング後に頬がつっぱる大きな原因は、実はクレンジング剤そのものだけでなく「すすぎに使うお湯の温度」にあります。寒い洗面所では無意識のうちに38〜40℃以上の熱いシャワーや蛇口のお湯で洗い流してしまいがちですが、皮脂が溶け出す温度を超えるお湯は角層の細胞間脂質やNMF（天然保湿因子）まで一気に洗い流してしまいます。
      </p>
      <p>
        一方、クレンジングウォーター（ミセラー水）は、水中に分散した<strong>ミセル粒子がファンデーションや皮脂汚れだけを包み込んでコットンへ移動させる</strong>ため、熱いお湯ですすぐ工程そのものを省略できます。さらに最新の製品はヒアルロン酸・ナイアシンアミド・温泉水・パンテノールといった化粧水レベルの保湿剤がベースになっているため、冬でも角層の水分を奪わずにメイクオフと朝洗顔を完了できるのが最大の強みです。
      </p>
    </section>

    <section class="cw-section" id="how-to-choose">
      <h2>2. 11月・12月の乾燥肌が押さえるべき3つの選び方</h2>
      <div class="cw-3grid">
        <div class="cw-pillar">
          <h3>① アルコール（エタノール）フリー＆オイルフリーを確認</h3>
          <p>拭き取り系は清涼感のためにアルコールが高配合な製品もありますが、冬の乾燥肌には揮発時の水分蒸散が負担になります。エタノール無添加の処方を選びましょう。</p>
        </div>
        <div class="cw-pillar">
          <h3>② 化粧水成分・温泉水・整肌成分の充実度</h3>
          <p>単なる「水＋洗浄剤」ではなく、江原道の温泉水・白樺樹液、ビフェスタのナイアシンアミド、dプログラムのトラネキサム酸など保湿・整肌軸で選ぶと後肌が変わります。</p>
        </div>
        <div class="cw-pillar">
          <h3>③ 惜しまず使える大容量（300〜500mL）と容器の使いやすさ</h3>
          <p>高級品でもケチって少量しか使わないとコットンの繊維摩擦で肌荒れします。毎日たっぷり濡らせる500mLや、片手で押せるポンプ型は非常に実用的です。</p>
        </div>
      </div>
    </section>

    <section class="cw-section" id="compare-matrix">
      <h2>3. 高保湿クレンジングウォーター10選 スペック比較表</h2>
      <p>主要保湿成分・フリー設計・楽天市場で確認した最新実勢価格（税込）を一覧で比較できます。</p>
      <div class="tbl-wrap">
        <table class="cw-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド / 商品名</th>
              <th>主要保湿・整肌成分</th>
              <th>フリー設計・特徴</th>
              <th>参考価格 / 容量</th>
            </tr>
          </thead>
          <tbody>
{table_rows}          </tbody>
        </table>
      </div>
    </section>

    <h2 class="rank-heading" id="ranking-detail">4. 保湿力高めクレンジングウォーター（ミセラー水）ランク10</h2>
    <section aria-label="クレンジングウォーター詳細ランキング">
{cards_html}    </section>

    <section class="cw-section" id="zero-friction">
      <h2>5. 冬の乾燥肌を傷めない「ヒタヒタ無摩擦コットン」4ステップ</h2>
      <div class="cw-step-grid">
        <div class="cw-step">
          <h3>Step 1：裏まで透ける量をたっぷり含ませる</h3>
          <p>コットンの表面だけでなく裏側までしっとり濡れる量が目安です。液が少ないとコットンの毛羽立ちが直接角層を傷つけてしまいます。</p>
        </div>
        <div class="cw-step">
          <h3>Step 2：目元・口元は5秒「押し当てて待つ」</h3>
          <p>ポイントメイクの上をいきなり擦るのはNG。湿らせたコットンをそっと乗せて5秒ほど待つとミセルがメイクを浮かせ、軽く滑らせるだけで落ちます。</p>
        </div>
        <div class="cw-step">
          <h3>Step 3：頬・額は中心から外側へ一方向になでる</h3>
          <p>ゴシゴシ往復させず、指の力を抜いて一方向にスーッと滑らせます。コットンが汚れたら必ずきれいな面や新しいコットンに持ち替えましょう。</p>
        </div>
        <div class="cw-step">
          <h3>Step 4：12月の夜は乳液・クリームで軽く蓋をする</h3>
          <p>W洗顔不要でそのまま寝られる設計がほとんどですが、暖房がついた部屋で過ごす冬場は、仕上げに乳液やセラミドクリームを薄く重ねると翌朝まで乾きません。</p>
        </div>
      </div>
    </section>

    <section class="cw-section" id="cw-faq">
      <h2>6. 冬のクレンジングウォーターに関するよくある質問</h2>
      <div class="faq-row">
        <h3>Q1. クレンジングウォーターだけで冬のメイクは本当に落ちますか？W洗顔は必要？</h3>
        <p>今回選定した10本はいずれもミセル構造でファンデーションや皮脂汚れを包み込んで落とすため、基本的にW洗顔不要です。ただし、落ちにくいウォータープルーフマスカラや密着ティントを使った日は専用のリムーバーを先に併用するとこすらず落とせます。</p>
      </div>
      <div class="faq-row">
        <h3>Q2. コットンで拭き取ると冬はかえって摩擦ダメージになりませんか？</h3>
        <p>摩擦の原因の9割は「液量不足」と「力の入れすぎ」です。裏面まで透けるほどたっぷり含ませ、重みだけで滑らせる意識を持てば、熱いお湯で皮脂膜を流すよりも冬の乾燥を防ぎやすくなります。</p>
      </div>
      <div class="faq-row">
        <h3>Q3. 朝洗顔の代わりに使っても大丈夫ですか？</h3>
        <p>はい、むしろ冬に非常に相性の良い使い方です。寝ている間の皮脂やホコリ、夜塗ったクリームの残りを冷たい水を使わずにオフでき、保湿成分を肌に残したまま朝のメイクに進めます。</p>
      </div>
      <div class="faq-row">
        <h3>Q4. 拭き取ったあとのベタつきが気になったときはどうすればいいですか？</h3>
        <p>そのまま次の保湿ケアへ進んで問題ありませんが、さっぱりさせたい場合は32〜34℃のぬるま湯で1〜2回軽くすすぐか、ミスト化粧水を吹きかけてティッシュで優しく押さえてから乳液を塗るのがおすすめです。</p>
      </div>
    </section>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬のクレンジング・拭き取り特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <a href="/winter-cleansing" class="internal-link-card">
          <div style="font-weight:700;color:#0c4a6e;margin-bottom:0.25rem;">冬の高保湿クレンジング総合10選</div>
          <div style="font-size:0.8rem;color:#475569;">バーム・ミルク・オイルも含めて徹底比較</div>
        </a>
        <a href="/winter-wipe-lotion" class="internal-link-card">
          <div style="font-weight:700;color:#0c4a6e;margin-bottom:0.25rem;">朝用ふき取り高保湿化粧水10選</div>
          <div style="font-size:0.8rem;color:#475569;">朝の冷たい水洗顔を卒業するしっとりケア</div>
        </a>
        <a href="/winter-point-makeup-remover" class="internal-link-card">
          <div style="font-weight:700;color:#0c4a6e;margin-bottom:0.25rem;">高保湿ポイントメイクリムーバー10選</div>
          <div style="font-size:0.8rem;color:#475569;">目元・口元の乾燥小ジワを防ぐ専用オフ</div>
        </a>
      </div>
    </div>
  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-title">Lumi Cosme (ルミコスメ) 冬の高保湿特集一覧</div>
      <div class="footer-links-grid" id="footer-links-box">
        <a href="/">トップページ</a>
      </div>
      <p class="copyright">&copy; 2026 Lumi Cosme (ルミコスメ) All Rights Reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-cleansing-water.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

print("Generated winter-cleansing-water.html successfully!")
