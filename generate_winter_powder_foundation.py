import json
import html

with open("fetched_3new_nov_dec_2026_1122.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

items = all_data["winter_powder_foundation"]["items"]

details = [
    {
        "rank": 1,
        "formula_type": "ムースプレス処方・美容液水ベース",
        "display_name": "ドラマティックパウダリー EX (レフィル)",
        "uv_spec": "SPF25・PA+++",
        "moist_agents": "スーパーヒアルロン酸（アセチルヒアルロン酸Na）、水溶性コラーゲン、ケイ酸（Li/Mg/Na）",
        "finish": "ふんわり自然なツヤ＆素肌感",
        "capacity": "9.3g（レフィル）",
        "lead_phrase": "「パウダーなのに粉っぽくない」の代名詞。ムース生まれの柔らか粉体が冬の頬にもスッと溶け込む",
        "review_p1": "パウダーファンデーションで必ず上位に名前が挙がる資生堂マキアージュの『ドラマティックパウダリー EX』。美容液水とパウダーを混ぜ合わせてムース状にしてからじっくり乾燥させる独自製法のため、固形でありながら肌に乗せた瞬間のふんわり感と密着力が段違いです。今回の楽天市場調査ではレフィル（オークル10）が¥2,435、レビュー150件超・★4.7台と安定した人気を保っています。",
        "review_p2": "スーパーヒアルロン酸や水溶性コラーゲンといった保湿成分が粉体とうまく馴染んでおり、11月・12月の乾燥した朝にサッと滑らせても、頬が白く浮いたり毛穴落ちしたりしにくいのが強み。時間がない冬の朝でもスポンジひと塗りで毛穴や色ムラを自然にぼかし、まるで素肌がきれいな人のようなツヤ感に仕上がります。",
        "best_match": "パウダーファンデの手軽さはそのままに粉っぽさを避けたい方、自然なツヤとカバー力のバランスを求める方",
        "winter_use": "水あり・水なし両用タイプですが、冬場はしっとりした保湿系下地（ドラマティックスキンセンサーベースのモイスト等）と合わせ、水なしスポンジで優しく滑らせるのが綺麗です。"
    },
    {
        "rank": 2,
        "formula_type": "粉体レス発想・保湿オイルインプレス",
        "display_name": "プリンプ パウダレスト (レフィル 10g)",
        "uv_spec": "SPF12・PA++",
        "moist_agents": "美容オイル・保湿エモリエント成分高配合（パウダーを溶け込ませるベース設計）",
        "finish": "湿度をまとったなめらかソフトマット〜生ツヤ",
        "capacity": "10g（レフィル）",
        "lead_phrase": "粉感ゼロを目指して作られたアルビオンの名品。重ねても厚ぼったくならず、冬肌にしっとり吸いつく",
        "review_p1": "「パウダレスト」という名前の通り、従来のパウダーファンデーションが抱えていた粉っぽさや乾きやすさを徹底的に削ぎ落としたアルビオンの人気モデル。パフやスポンジで表面をなでると、しっとり湿り気を帯びたような極細のベースが取れ、肌にのせるとスッと溶け込むように一体化する感覚があります。",
        "review_p2": "乾燥が深まる12月の頬は、夕方になると表情ジワに粉が溜まりやすいものですが、プリンプ パウダレストは粉体同士がパサパサに分離しにくく、時間が経つほどに肌の水分と馴染んで上品なツヤが引き立ちます。UVカット値（SPF12・PA++）は控えめなので、冬の日中でも日焼け止め効果のある保湿下地を仕込んでおくと完璧です。",
        "best_match": "デパコス級の上質な肌馴染みを求める方、夕方の目元・口元の乾燥ひび割れに悩んでいる方",
        "winter_use": "スポンジに力を入れず軽く1〜2回なでるだけで十分伸びます。乾燥が気になる頬は叩き込むように押さえ、額や小鼻は薄く滑らせると立体感が出ます。"
    },
    {
        "rank": 3,
        "formula_type": "トリートメントスキンケアパウダー処方",
        "display_name": "タンプードルエクラII (レフィル)",
        "uv_spec": "SPF25・PA++",
        "moist_agents": "スキンイルミネイター（加水分解シルク・真珠コンキオリン・テアニン等）配合",
        "finish": "内側から発光するような上品シルク肌",
        "capacity": "8g（レフィル）",
        "lead_phrase": "クレ・ド・ポー ボーテが誇る最高峰トリートメントパウダリー。乾燥する冬の空気の中でも肌が疲れて見えない",
        "review_p1": "パウダーファンデーションの概念を塗り替えるラグジュアリーな逸品として話題を集めるクレ・ド・ポー ボーテの『タンプードルエクラII』。パウダーの粒子ひとつひとつをスキンケア成分で包み込むような設計により、粉体とは思えないほどうるおいと光の反射が美しく、真冬の乾いたオフィスでもくすみにくいのが特徴です。",
        "review_p2": "レフィル価格¥9,240（調査時点）とハイエンド帯ではありますが、少量で肌のアラをふんわり消し去るカバー力と、夕方まで乾燥崩れを感じさせないフィット感は価格相応の満足度。忘年会やクリスマスディナー、年末年始の挨拶など「いつもより肌をきれいに見せたい12月のイベント」に頼れる主役ファンデーションです。",
        "best_match": "予算をかけてでも最高峰の乾燥耐性と上品なツヤを手に入れたい方、大人のくすみ・小ジワをカバーしたい方",
        "winter_use": "別売りの専用パンソー（ブラシ）でふんわり乗せると素肌感のある極上ツヤに、スポンジで乗せるときちんと感のある端正な肌に仕上がります。"
    },
    {
        "rank": 4,
        "formula_type": "皮脂を潤いに変えるモイスチュアコーティング処方",
        "display_name": "モイスチュア ヴェール LX (リフィル)",
        "uv_spec": "SPF32・PA+++",
        "moist_agents": "モイストチェンジパウダー、植物性スクワラン、保湿オイルコーティング",
        "finish": "つるんと明るい潤いヴェール",
        "capacity": "リフィル",
        "lead_phrase": "時間が経つほどツヤと潤いが増すロングセラー。乾燥くすみと夕方崩れに強い頼もしさ",
        "review_p1": "「時間が経つほどくすんでカサつく」という大人の悩みと長年向き合ってきたカバーマークの定番パウダーファンデーション『モイスチュア ヴェール LX』。最大の特色は、時間の経過とともに肌から出るわずかな皮脂を取り込んで、潤いと光沢感のある「明るいヴェール」に変えてしまう独自処方にあります。",
        "review_p2": "11月・12月は朝しっかり保湿しても昼過ぎには乾燥で顔色が沈みがちですが、このファンデーションは時間が経っても土気色にくすみにくく、むしろ肌になじんでツヤが増して見えると定評があります。SPF32・PA+++で冬の日常紫外線もしっかりカバーでき、シミや色ムラを隠すカバー力の高さも大人世代に支持される理由です。",
        "best_match": "午後の顔色のくすみ・乾燥テカリ崩れが気になる30代〜50代の方、カバー力と保湿力をどちらも妥協したくない方",
        "winter_use": "スポンジの半分にファンデを取り、顔の中心（頬の高い位置）から外側へスッと伸ばします。シミが気になる箇所だけ重ねトントンすると厚塗り感なく隠せます。"
    },
    {
        "rank": 5,
        "formula_type": "うるおい美容液成分配合シンクロ処方",
        "display_name": "シンクロフィット パクト EX (詰替え用 9g)",
        "uv_spec": "SPF26・PA++",
        "moist_agents": "ヒアルロン酸、コラーゲン、オリーブ果実油、リン脂質（保湿）",
        "finish": "毛穴レスでなめらかなソフトツヤ",
        "capacity": "9g（詰替え用）",
        "lead_phrase": "ヒアルロン酸・コラーゲン・オリーブ果実油を配合。カサついた冬の頬にもピタッと吸い付く密着設計",
        "review_p1": "コーセー『エスプリーク』のロングセラーを磨き上げた『シンクロフィット パクト EX』。どのような肌コンディションの日でも均一に密着するよう「スーパー化粧のり成分」と保湿オイルをバランスよく配合しており、寝不足や暖房乾燥で肌キメが乱れがちな12月の朝でもムラになりにくいのが魅力です。",
        "review_p2": "配合されているヒアルロン酸やコラーゲン、オリーブ果実油のおかげで、粉質がとてもしっとりクリーミー。毛穴を無理に厚塗りで埋めるのではなく、光と微細粉体でふんわり飛ばしてくれるため、ほうれい線や目尻にファンデーションが溜まりにくい仕上がりです。水あり・水なし両用で季節を問わず扱いやすい名品です。",
        "best_match": "朝のコンディションに左右されず手早く綺麗に仕上げたい方、毛穴カバーとしっとり密着の両方を重視する方",
        "winter_use": "小鼻や目の下など動きやすい部分は、スポンジに残ったごく少量を優しく押さえる程度に留めると夕方までヨレにくくなります。"
    },
    {
        "rank": 6,
        "formula_type": "密着オイルコート×光拡散ブライトパウダー",
        "display_name": "ブライトチャージ パウダー (9g)",
        "uv_spec": "SPF16・PA+++",
        "moist_agents": "保湿成分（ヒアルロン酸・アスナロ枝エキス等）、密着オイル処理粉体",
        "finish": "光を味方にした自然な素肌ツヤ",
        "capacity": "9g",
        "lead_phrase": "「テカリは防ぎたいけどカサカサは嫌」な冬肌に。楽天レビュー280件超が証明する密着感と崩れにくさ",
        "review_p1": "崩れにくさで有名な花王プリマヴィスタから登場し、楽天市場でもレビュー285件超・★4.67と高い支持を得ている『ブライトチャージ パウダー』。従来の皮脂固化特化モデルとは異なり、「粉っぽさを抑えながら光を味方につけて明るく均一に仕上げる」方向へ進化したモデルです。",
        "review_p2": "しっとりしたオイルコート処方のパウダーが肌の上を滑るように伸び、暖房が効いた室内でTゾーンが少し汗ばんだり皮脂が出たりしても、ドロドロに崩れず頬も粉を吹きにくい絶妙なバランスを実現しています。¥3,080（調査時点）という手に取りやすい価格帯で、日常の通勤・仕事用ファンデとして非常に完成度が高い一品です。",
        "best_match": "冬でも鼻や額は少しテカりやすく、頬は乾く混合肌の方、暖房の効いたオフィスで一日中お直ししにくい方",
        "winter_use": "専用スポンジの起毛面（柔らかい面）を使って最後に頬をそっとなでると、粉っぽさが消えて自然なツヤ感が増します。"
    },
    {
        "rank": 7,
        "formula_type": "ヒト型セラミド×ヒアルロン酸配合ミネラルプレスト",
        "display_name": "タイムレスフォギーミネラルファンデーション (リフィル・パフ付)",
        "uv_spec": "SPF50+・PA++++",
        "moist_agents": "ヒト型セラミド（セラミドNP/NG/AP）、ヒアルロン酸Na、ホホバ種子油、スクワラン",
        "finish": "セミマット〜上質なフォギー肌（石けんオフ対応）",
        "capacity": "リフィル（パフ付）",
        "lead_phrase": "敏感肌の味方エトヴォスの高保湿ミネラル。クレンジング不要の石けんオフ×SPF50+で冬の肌負担を減らす",
        "review_p1": "冬場の乾燥で肌がゆらぎ、「クレンジングを使うたびに頬がつっぱるのが辛い」と感じる方に絶大な支持を得ているのがエトヴォスの『タイムレスフォギーミネラルファンデーション』。保湿成分の王道である3種のヒト型セラミドやヒアルロン酸Na、ホホバ油などをミネラルパウダーに配合し、メイク中も角層の潤いを守る発想で作られています。",
        "review_p2": "それなのにSPF50+・PA++++という最高クラスのUVカット値を備えており、冬のスキー・初詣・雪の日の照り返し紫外線までしっかりガード。専用下地や石けんでオフできる低刺激設計（※他アイテムとの併用時は各仕様に準拠）ながら、気になる毛穴や赤みをふんわり霧がかったようにカバーしてくれる優秀作です。",
        "best_match": "冬の乾燥でクレンジング負担を減らしたい敏感肌の方、セラミド入りの石けんオフファンデーションを探している方",
        "winter_use": "付属のパフ（または両面パフの起毛面）に少しずつ取り、顔の内側から外側へ軽く押さえるように重ねるとフォギーな美肌に整います。"
    },
    {
        "rank": 8,
        "formula_type": "シルクアミノ酸×天然ミネラルパウダー",
        "display_name": "ミネラルシルクファンデーション (詰め替え用・パフ付)",
        "uv_spec": "SPF25・PA++",
        "moist_agents": "加水分解シルク、シルクパウダー、スクワラン、ホホバ種子油",
        "finish": "なめらかなツヤシルク肌（クレンジング不要）",
        "capacity": "12g目安（詰め替え用）",
        "lead_phrase": "楽天レビュー430件超の隠れた名品！天然シルクの保湿力で、乾燥小ジワが気になる大人肌を優しく包む",
        "review_p1": "京都発のミネラルコスメブランド・ヴァントルテ（VINTORTE）のロングセラー『ミネラルシルクファンデーション』。楽天市場で430件以上のレビュー（★4.5台）を集める人気商品で、最大の特徴は肌と親和性の高い「シルク（絹）」とミネラルをベースにスクワランやホホバ油を配合している点にあります。",
        "review_p2": "タルク・シリコン・紫外線吸収剤・界面活性剤・防腐剤などを使わないシンプル処方のため、乾燥してバリアが薄くなった11月・12月の肌にも負担をかけにくく、軽やかなのにしっとりした保湿感が続きます。プレスト型ながら粉が柔らかいため、付属のふわふわパフで押さえるように乗せると毛穴の凹凸を優しくカバーしてくれます。",
        "best_match": "40代〜60代以上で小ジワにファンデが入り込みやすい方、無添加・石けんオフの優しい付け心地を好む方",
        "winter_use": "パフを滑らせるより、乾燥しやすい頬にはスタンプを押すようにポンポンと優しく乗せていくと、シルクの上品なツヤが引き立ちます。"
    },
    {
        "rank": 9,
        "formula_type": "濃密リッチオイルコーティング処方",
        "display_name": "カシミアフィットファンデーション N (リフィル・専用パフ付 9g)",
        "uv_spec": "SPF20・PA++",
        "moist_agents": "保湿オイルコートパウダー（植物性エモリエント成分配合）",
        "finish": "カシミアのように柔らかくキメ細かなセミツヤ",
        "capacity": "9g（リフィル・専用パフ付）",
        "lead_phrase": "2,000円台前半とは思えないしっとり感。カシミアのセーターをまとうような心地よさの冬向け名品",
        "review_p1": "オルビスが「乾燥する秋冬でも気持ちよく使えるパウダーファンデーション」として展開し、根強いファンを抱える『カシミアフィットファンデーション N』。その名の通り、パウダーの粒子をリッチな保湿オイルでコーティングしており、肌に触れた瞬間からパサつきを感じさせない柔らかなフィット感が魅力です。",
        "review_p2": "リフィル（専用パフ付）が¥2,310（調査時点）とコストパフォーマンスに優れ、無香料・酸化しやすい油分を抑えた設計で肌荒れしにくいのも嬉しいポイント。薄付きで素肌感を残しながら、毛穴や冬の冷えくすみをふんわり均一に整えてくれるため、デイリーメイクから休日のちょっとしたお出かけまで幅広く活躍します。",
        "best_match": "2,000円台で乾燥しにくい高コスパのパウダーファンデを探している方、重たいカバー感より自然な素肌美が好きな方",
        "winter_use": "専用パフに適量を取り、顔の中心から外側へ優しく伸ばしたあと、乾燥が気になる口角や小鼻はパフを折って丁寧に密着させると崩れにくくなります。"
    },
    {
        "rank": 10,
        "formula_type": "うるおい成分配合・皮脂吸着×高カバーパクト",
        "display_name": "ウルトラカバーUVパクト (11g)",
        "uv_spec": "SPF35・PA++",
        "moist_agents": "ヒアルロン酸Na、スクワラン、ホホバ種子油、マカデミア種子油、カミツレ花エキス",
        "finish": "しっかりカバーのなめらかセミマット",
        "capacity": "11g（ケース・パフ付本体）",
        "lead_phrase": "880円（本体）でこの保湿成分量！スクワラン・ホホバ油・ヒアルロン酸配合で冬のお直しポーチにも最適",
        "review_p1": "プチプラの王者セザンヌの『ウルトラカバーUVパクト』は、ケースとパフが付いた本体で¥880（調査時点）という驚きの価格でありながら、スクワラン・ホホバ種子油・マカデミア種子油・ヒアルロン酸Naなど実に多彩な保湿成分を配合している隠れた実力派です。無香料・タール系色素不使用・アルコールフリーという配慮も光ります。",
        "review_p2": "「カバー力が高いプチプラパウダーは乾燥してパサパサになりやすい」という常識に反して、粉体がしっとり肌に密着し、冬の乾燥した電車内やオフィスで午後にお直し用として重ねても粉吹きを起こしにくいのが強み。持ち歩き用のポーチに1つ入れておけば、冬の夕方メイク直しに頼れる存在です。",
        "best_match": "1,000円以下でしっかりカバーと保湿成分を両立したい方、日中のメイク直し用コンパクトを探している方",
        "winter_use": "お直しで使う際は、まずティッシュで軽く皮脂や浮きを抑え、手持ちの保湿ミストをひと吹きして馴染ませてから本品を薄く重ねると、朝の仕上がりが蘇ります。"
    }
]

article_title = "保湿力の強さで粉吹き肌とさようなら！真冬もしっとり密着する保湿力高めパウダーファンデーションランク10【11月・12月】"
article_desc = "11月・12月の乾燥でも粉を吹かない！マキアージュ、アルビオン パウダレスト、クレ・ド・ポー ボーテ タンプードルエクラII、カバーマーク、エスプリーク、プリマヴィスタ、エトヴォス、ヴァントルテ、オルビス、セザンヌまで保湿力高めパウダーファンデーション10選を徹底比較。"
canonical_url = "https://lumi-cosme.vercel.app/winter-powder-foundation"

json_ld_graph = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": article_title,
            "description": article_desc,
            "image": items[0]["image_url"],
            "datePublished": "2026-11-22T05:00:00+09:00",
            "dateModified": "2026-11-22T05:00:00+09:00",
            "author": {"@type": "Organization", "name": "Lumi Cosme 編集部"},
            "publisher": {
                "@type": "Organization",
                "name": "Lumi Cosme (ルミコスメ)",
                "logo": {"@type": "ImageObject", "url": "https://lumi-cosme.vercel.app/favicon.jpg"}
            }
        },
        {
            "@type": "ItemList",
            "name": "11月・12月向け保湿力高めパウダーファンデーション10選",
            "numberOfItems": 10,
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": it["rank"],
                    "item": {
                        "@type": "Product",
                        "name": f"{it['brand']} {det['display_name']}",
                        "image": it["image_url"],
                        "description": det["lead_phrase"],
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
                    "name": "乾燥肌の人が11月・12月の冬にパウダーファンデーションを使っても粉を吹きませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "近年の高保湿パウダーファンデーションは、ムースプレス製法やオイルコーティング粉体、セラミド・ヒアルロン酸・スクワラン配合など保湿設計が大きく進化しており、冬の乾燥肌でもしっとり密着する製品が増えています。ただし、使う前の保湿下地を『しっとり系』に切り替え、スキンケア直後のベタつきが馴染んでから塗ることが重要です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "リキッドファンデーションとパウダーファンデーション、冬はどちらが良いですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "極度の乾燥肌でツヤと高い密閉感を重視する日はリキッドやクリームファンデが有利ですが、朝の時短・軽やかな付け心地・マスクやマフラーへの色移りの少なさ・日中のお直しのしやすさを求めるなら保湿力の高いパウダーファンデーションが圧倒的に快適です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "パウダーファンデーションを塗る際、スポンジとブラシはどちらが乾燥しにくいですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "乾燥が気になる冬場は、柔らかい毛足の長めなフェイスブラシや専用ファンデーションブラシを使うと余分な粉が落ち、より薄く均一にフィットするため粉っぽくなりにくくなります。スポンジを使う場合は擦らず『押さえるように滑らせる』のがコツです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "朝のスキンケア後にすぐ塗るとムラになるのはなぜですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "クリームや乳液の油分が肌表面に残ったままパウダーを重ねると、粉がその油分を吸ってダマ（ムラ）になりやすくなります。保湿ケアや下地を塗ったあと2〜3分待つか、軽くティッシュで余分な表面油分を押さえてからパウダーファンデーションを乗せると驚くほど均一に密着します。"
                    }
                }
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://lumi-cosme.vercel.app/"},
                {"@type": "ListItem", "position": 2, "name": "冬のベースメイク総合特集", "item": "https://lumi-cosme.vercel.app/winter-base-makeup"},
                {"@type": "ListItem", "position": 3, "name": "保湿力高めパウダーファンデーション10選", "item": canonical_url}
            ]
        }
    ]
}

rows_html = ""
for it, det in zip(items, details):
    rows_html += f"""            <tr>
              <td class="p-rank">#{it['rank']}</td>
              <td><strong>{html.escape(it['brand'])}</strong><div class="p-sub">{html.escape(det['display_name'])}</div></td>
              <td>{html.escape(det['formula_type'])}</td>
              <td>{html.escape(det['uv_spec'])}</td>
              <td>{html.escape(det['finish'])}</td>
              <td class="p-price">¥{it['price']:,}<div class="p-sub">{html.escape(det['capacity'])}</div></td>
            </tr>
"""

cards_html = ""
for it, det in zip(items, details):
    rate_html = (
        f'<span class="pf-rate">★ {it["review_average"]} ({it["review_count"]:,}件)</span>'
        if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
        else '<span class="pf-rate">楽天市場 在庫確認済</span>'
    )
    cards_html += f"""
      <article class="pf-card" id="rank-{it['rank']}">
        <div class="pf-head">
          <div class="pf-badge-line">
            <span class="pf-rank-tag">第{it['rank']}位</span>
            <span class="pf-type-tag">{html.escape(det['formula_type'])}</span>
            {rate_html}
          </div>
          <h3>{html.escape(it['brand'])} {html.escape(det['display_name'])}</h3>
          <p class="pf-lead">{html.escape(det['lead_phrase'])}</p>
        </div>

        <div class="pf-body">
          <div class="pf-media">
            <div class="pf-img-box">
              <img src="{html.escape(it['image_url'])}" alt="{html.escape(it['brand'])} {html.escape(det['display_name'])}" class="product-img" loading="lazy">
            </div>
            <div class="pf-price-panel">
              <span class="pf-p-lbl">楽天市場 最新確認価格（税込）</span>
              <span class="pf-p-val">¥{it['price']:,}</span>
            </div>
            <a href="{html.escape(it['affiliate_url'])}" target="_blank" rel="noopener noreferrer nofollow sponsored" class="rakuten-btn">
              楽天市場で色展開・詳細を見る →
            </a>
            <p class="pf-ref">取得商品：{html.escape(it['item_name'][:52])}</p>
          </div>

          <div class="pf-content">
            <div class="pf-spec-grid">
              <div><span>UVカット</span><strong>{html.escape(det['uv_spec'])}</strong></div>
              <div><span>容量・仕様</span><strong>{html.escape(det['capacity'])}</strong></div>
              <div><span>保湿・密着設計</span><strong>{html.escape(det['moist_agents'])}</strong></div>
              <div><span>仕上がり質感</span><strong>{html.escape(det['finish'])}</strong></div>
            </div>

            <div class="pf-prose">
              <p>{html.escape(det['review_p1'])}</p>
              <p>{html.escape(det['review_p2'])}</p>
            </div>

            <div class="pf-tips">
              <div class="pf-tip-card">
                <strong>特におすすめしたい方</strong>
                <p>{html.escape(det['best_match'])}</p>
              </div>
              <div class="pf-tip-card">
                <strong>真冬に粉を吹かせない塗り方</strong>
                <p>{html.escape(det['winter_use'])}</p>
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
  <meta name="keywords" content="パウダーファンデーション 乾燥しない 冬, 高保湿 パウダーファンデ, 粉吹きしない ファンデーション, マキアージュ ドラマティックパウダリー, アルビオン パウダレスト, タンプードルエクラII, エトヴォス, カバーマーク">
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
      --rose: #9f1239;
      --rose-deep: #881337;
      --rose-soft: #fff1f2;
      --rose-border: #fecdd3;
      --gold: #b45309;
      --bg: #fdfbfc;
      --ink: #1f2937;
      --muted: #52525b;
      --line: #e4e4e7;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.78;
    }}
    header.topbar {{
      background: #fff;
      border-bottom: 1px solid var(--line);
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .topbar-in {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 13px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .site-brand {{ font-weight: 800; font-size: 1.12rem; color: var(--rose-deep); text-decoration: none; }}
    .top-links {{ display: flex; gap: 14px; flex-wrap: wrap; font-size: 0.85rem; }}
    .top-links a {{ color: var(--rose); font-weight: 700; text-decoration: none; }}
    .crumb {{ max-width: 1080px; margin: 14px auto 0; padding: 0 20px; font-size: 0.82rem; color: var(--muted); }}
    .crumb a {{ color: var(--rose); text-decoration: none; }}
    main {{ max-width: 1080px; margin: 20px auto 64px; padding: 0 20px; }}

    .pf-hero {{
      background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);
      border: 1px solid var(--rose-border);
      border-radius: 16px;
      padding: 36px 30px;
      margin-bottom: 26px;
    }}
    .pf-pill {{
      display: inline-block;
      background: var(--rose);
      color: #fff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }}
    .pf-hero h1 {{
      font-size: 1.72rem;
      line-height: 1.42;
      color: var(--rose-deep);
      margin-bottom: 12px;
    }}
    .pf-meta {{ font-size: 0.84rem; color: var(--muted); margin-bottom: 14px; }}
    .pf-hero p {{ font-size: 0.96rem; margin-bottom: 10px; }}

    .toc-wrap {{
      background: #fff;
      border: 1px solid var(--line);
      border-left: 5px solid var(--rose);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 28px;
    }}
    .toc-wrap h2 {{ font-size: 1.05rem; color: var(--rose-deep); margin-bottom: 10px; }}
    .toc-wrap ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 6px 18px;
    }}
    .toc-wrap a {{ color: var(--rose); text-decoration: none; font-size: 0.92rem; font-weight: 600; }}

    .editorial-sec {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 28px;
      margin-bottom: 28px;
    }}
    .editorial-sec h2 {{
      font-size: 1.32rem;
      color: var(--rose-deep);
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--rose-soft);
    }}
    .editorial-sec p {{ font-size: 0.95rem; margin-bottom: 12px; }}

    .finish-3 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin-top: 14px;
    }}
    .finish-card {{
      background: var(--rose-soft);
      border: 1px solid var(--rose-border);
      border-radius: 12px;
      padding: 18px;
    }}
    .finish-card h3 {{ font-size: 1rem; color: var(--rose-deep); margin-bottom: 8px; }}
    .finish-card p {{ font-size: 0.88rem; margin: 0; }}

    .tbl-scroll {{ overflow-x: auto; margin-top: 14px; }}
    .pf-table {{ width: 100%; border-collapse: collapse; min-width: 740px; font-size: 0.87rem; }}
    .pf-table th {{ background: var(--rose-deep); color: #fff; text-align: left; padding: 11px 12px; }}
    .pf-table td {{ padding: 12px; border-bottom: 1px solid var(--line); vertical-align: top; }}
    .pf-table tr:nth-child(even) td {{ background: #fafafa; }}
    .p-rank {{ font-weight: 800; color: var(--rose); white-space: nowrap; }}
    .p-price {{ font-weight: 700; color: var(--rose-deep); white-space: nowrap; }}
    .p-sub {{ font-size: 0.78rem; color: var(--muted); font-weight: 400; margin-top: 2px; }}

    .sec-rank-title {{
      font-size: 1.4rem;
      color: var(--rose-deep);
      margin: 34px 0 18px;
      padding-left: 12px;
      border-left: 5px solid var(--rose);
    }}
    .pf-card {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 26px;
      margin-bottom: 24px;
      box-shadow: 0 2px 10px rgba(159, 18, 57, 0.04);
    }}
    .pf-head {{ margin-bottom: 18px; }}
    .pf-badge-line {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 10px; }}
    .pf-rank-tag {{
      background: var(--rose-deep);
      color: #fff;
      font-weight: 800;
      font-size: 0.82rem;
      padding: 4px 12px;
      border-radius: 6px;
    }}
    .pf-type-tag {{
      background: var(--rose-soft);
      color: var(--rose);
      border: 1px solid var(--rose-border);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .pf-rate {{
      background: #fef3c7;
      color: var(--gold);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .pf-head h3 {{ font-size: 1.24rem; margin-bottom: 6px; }}
    .pf-lead {{ font-size: 0.92rem; color: var(--rose); font-weight: 700; margin: 0; }}

    .pf-body {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 24px;
      align-items: start;
    }}
    .pf-img-box {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 12px;
      text-align: center;
      margin-bottom: 12px;
    }}
    .product-img {{ max-width: 100%; height: 210px; object-fit: contain; }}
    .pf-price-panel {{
      background: var(--rose-soft);
      border-radius: 10px;
      padding: 10px 12px;
      text-align: center;
      margin-bottom: 10px;
    }}
    .pf-p-lbl {{ display: block; font-size: 0.74rem; color: var(--muted); }}
    .pf-p-val {{ font-size: 1.35rem; font-weight: 800; color: var(--rose-deep); }}
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
    .pf-ref {{ margin-top: 8px; font-size: 0.72rem; color: var(--muted); line-height: 1.4; word-break: break-all; }}

    .pf-spec-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      background: #fafafa;
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 12px 14px;
      margin-bottom: 14px;
      font-size: 0.84rem;
    }}
    .pf-spec-grid div span {{ display: block; font-size: 0.74rem; color: var(--muted); }}
    .pf-prose p {{ font-size: 0.94rem; margin-bottom: 10px; }}
    .pf-tips {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: 12px;
    }}
    .pf-tip-card {{
      background: var(--rose-soft);
      border: 1px solid var(--rose-border);
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 0.84rem;
    }}
    .pf-tip-card strong {{ display: block; color: var(--rose-deep); margin-bottom: 4px; }}
    .pf-tip-card p {{ margin: 0; }}

    .tech-3 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin-top: 14px;
    }}
    .tech-box {{
      background: #fafafa;
      border: 1px solid var(--line);
      border-top: 4px solid var(--rose);
      border-radius: 10px;
      padding: 16px;
    }}
    .tech-box h3 {{ font-size: 0.98rem; color: var(--rose-deep); margin-bottom: 6px; }}
    .tech-box p {{ font-size: 0.87rem; margin: 0; }}

    .faq-item {{ border-bottom: 1px solid var(--line); padding: 14px 0; }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-item h3 {{ font-size: 1rem; color: var(--rose-deep); margin-bottom: 6px; }}
    .faq-item p {{ font-size: 0.92rem; margin: 0; }}

    .internal-links-box {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 24px;
      margin-top: 32px;
    }}
    .internal-links-title {{ font-weight: 800; font-size: 1.08rem; color: var(--rose-deep); margin-bottom: 14px; }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 12px;
    }}
    .internal-link-card {{
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 12px;
      text-decoration: none;
      display: block;
    }}
    .internal-link-card:hover {{ border-color: var(--rose); }}

    footer {{
      background: #18181b;
      color: #a1a1aa;
      padding: 44px 20px 30px;
      font-size: 0.84rem;
    }}
    .footer-inner {{ max-width: 1080px; margin: 0 auto; }}
    .footer-title {{ color: #fafafa; font-weight: 800; margin-bottom: 14px; }}
    .footer-links-grid {{ display: flex; flex-wrap: wrap; gap: 8px 14px; margin-bottom: 24px; }}
    .footer-links-grid a {{ color: #d4d4d8; text-decoration: none; font-size: 0.8rem; }}
    .footer-links-grid a:hover {{ color: #fda4af; text-decoration: underline; }}
    .copyright {{ border-top: 1px solid #27272a; padding-top: 18px; text-align: center; font-size: 0.78rem; }}

    @media (max-width: 760px) {{
      .pf-hero {{ padding: 24px 18px; }}
      .pf-hero h1 {{ font-size: 1.32rem; }}
      .pf-body, .pf-spec-grid, .pf-tips {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header class="topbar">
    <div class="topbar-in">
      <a href="/" class="site-brand">Lumi Cosme</a>
      <nav class="top-links">
        <a href="/winter-base-makeup">ベースメイク総合</a>
        <a href="/winter-makeup-primer">冬用化粧下地</a>
        <a href="/winter-powder">冬用パウダー</a>
      </nav>
    </div>
  </header>

  <nav class="crumb" aria-label="パンくずリスト">
    <a href="/">ホーム</a> &gt; <a href="/winter-base-makeup">冬のベースメイク特集</a> &gt; <span>保湿力高めパウダーファンデーション10選</span>
  </nav>

  <main>
    <section class="pf-hero">
      <span class="pf-pill">2026年11月・12月 粉吹きゼロの冬ベースメイク特集</span>
      <h1>{html.escape(article_title)}</h1>
      <div class="pf-meta">更新日：<time datetime="2026-11-22">2026年11月22日</time> ／ Lumi Cosme ベースメイク検証班</div>
      <p>
        「冬はリキッドやクッションじゃないと乾燥するから、パウダーファンデーションはお休みしている」という方は少なくありません。確かに一昔前のパウダーファンデは、皮脂吸着パウダーの比率が高くて冬場に塗ると頬や口周りが白く粉を吹きやすい傾向がありました。
      </p>
      <p>
        しかし近年のパウダーファンデーションは、美容液水と混ぜてムースから作る製法や、粒子ひとつひとつを保湿オイル・ヒト型セラミド・シルクアミノ酸で包む技術が飛躍的に進歩しています。朝の1分でサッと綺麗に仕上がってマフラーにも色移りしにくいのに、<strong>真冬でもしっとり密着する保湿力高めパウダーファンデーション10選</strong>を、楽天市場の最新確認価格とともにまとめました。
      </p>
    </section>

    <nav class="toc-wrap" aria-label="目次">
      <h2>この記事のガイド</h2>
      <ul>
        <li><a href="#powder-evolve">1. なぜ冬でも乾かない？最新パウダーファンデの保湿技術</a></li>
        <li><a href="#choose-finish">2. 仕上がり質感と肌負担で選ぶ3つのタイプ</a></li>
        <li><a href="#compare-matrix">3. 保湿力高めパウダーファンデーション10選 比較表</a></li>
        <li><a href="#ranking-10">4. 真冬におすすめの保湿パウダーファンデ10選</a></li>
        <li><a href="#no-flake-tech">5. 粉吹きを確実に防ぐ「朝の仕込み＆塗り方」3選</a></li>
        <li><a href="#faq">6. 冬のパウダーファンデーション Q&amp;A</a></li>
      </ul>
    </nav>

    <section class="editorial-sec" id="powder-evolve">
      <h2>1. なぜ「パウダー＝冬は乾燥する」常識が変わりつつあるのか</h2>
      <p>
        リキッドやクリームファンデーションが「油分と水分を含む液体」で肌を覆うのに対し、パウダーファンデーションが冬に敬遠されがちだった理由は、粉体が肌表面のわずかな皮脂や水分を吸い取ってパサつきやすい点にありました。特に11月・12月の低湿度な室内では、昼過ぎに小鼻の脇や口角がカサッと割れて見えやすくなります。
      </p>
      <p>
        ところが現在人気を集めている冬向けパウダーファンデは、粉体そのものに<strong>スクワラン・ホホバ油・ヒト型セラミド・ヒアルロン酸・シルクパウダー</strong>などをコーティングしたり、ムース状態から水分をゆっくり飛ばしてプレスしたりすることで、肌にのせた瞬間にクリームやリキッドに近いしっとりとした密着膜を作ります。手も汚れず、マスクやタートルネックへの色移りも少ないため、冬の定番として見直す人が増えています。
      </p>
    </section>

    <section class="editorial-sec" id="choose-finish">
      <h2>2. 好みの仕上がりとライフスタイルで選ぶ3つのタイプ</h2>
      <div class="finish-3">
        <div class="finish-card">
          <h3>① 粉感ゼロ・生ツヤ密着派（ムース／オイルイン）</h3>
          <p>マキアージュ、アルビオン パウダレスト、クレ・ド・ポー ボーテなどは粉っぽさを感じさせず、素肌が発光するような柔らかいツヤが出るため乾燥肌の毎日使いに最適です。</p>
        </div>
        <div class="finish-card">
          <h3>② 夕方のくすみ・崩れ防止派（高カバー・光拡散）</h3>
          <p>カバーマークやエスプリーク、プリマヴィスタは、冬の午後にくすみやすい肌色を明るく保ち、Tゾーンのテカリと頬の乾燥が混在する混合肌でも崩れにくい設計です。</p>
        </div>
        <div class="finish-card">
          <h3>③ 肌負担軽減・石けんオフ派（ミネラル＆セラミド）</h3>
          <p>エトヴォスやヴァントルテはセラミド・シルクなど保湿成分を抱えたミネラル処方で、冬場にクレンジングの洗浄力で乾燥したくない敏感肌の方から重宝されています。</p>
        </div>
      </div>
    </section>

    <section class="editorial-sec" id="compare-matrix">
      <h2>3. 保湿力高めパウダーファンデーション10選 スペック一覧</h2>
      <p>楽天市場の最新価格（レフィル／本体別）とUVカット値・仕上がり質感を比較できます。</p>
      <div class="tbl-scroll">
        <table class="pf-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド / 商品名</th>
              <th>保湿・粉体テクノロジー</th>
              <th>UVカット</th>
              <th>仕上がり質感</th>
              <th>参考価格 / 仕様</th>
            </tr>
          </thead>
          <tbody>
{rows_html}          </tbody>
        </table>
      </div>
    </section>

    <h2 class="sec-rank-title" id="ranking-10">4. 真冬もしっとり密着！保湿力高めパウダーファンデーション10選</h2>
    <section aria-label="パウダーファンデーション詳細レビュー">
{cards_html}    </section>

    <section class="editorial-sec" id="no-flake-tech">
      <h2>5. 11月・12月に粉吹きを絶対に防ぐ「朝の仕込み＆塗り方」3つのコツ</h2>
      <div class="tech-3">
        <div class="tech-box">
          <h3>コツ1：スキンケアの「2〜3分置き＆軽くティッシュ」</h3>
          <p>保湿クリームを塗ってすぐパウダーを重ねると油分に粉が引っかかりダマになります。2〜3分馴染ませたあと、Tゾーンや小鼻だけ軽くティッシュで押さえてから塗ると均一に伸びます。</p>
        </div>
        <div class="tech-box">
          <h3>コツ2：下地は「保湿系・美容液系」をセレクト</h3>
          <p>夏用の強い皮脂崩れ防止下地のまま冬用ファンデに変えても頬は乾きます。ポール＆ジョーやクレ・ド・ポー等の保湿プライマーで水分とツヤの土台を作ってから重ねてください。</p>
        </div>
        <div class="tech-box">
          <h3>コツ3：乾燥する頬は「押さえ塗り」またはブラシ</h3>
          <p>スポンジで頬をゴシゴシ横に擦ると、角層のめくれ（粉吹き）を起こしやすくなります。頬の高い位置から優しく押さえるように置くか、柔らかい大きめブラシで磨くように乗せるのが理想です。</p>
        </div>
      </div>
    </section>

    <section class="editorial-sec" id="faq">
      <h2>6. 冬のパウダーファンデーションに関するQ&amp;A</h2>
      <div class="faq-item">
        <h3>Q1. 本当に乾燥肌の私でも冬にパウダーファンデを使って大丈夫ですか？</h3>
        <p>今回ランクインしたマキアージュやアルビオン、カバーマーク、エトヴォスのような保湿成分・オイルコート処方のモデルなら、冬の乾燥肌でもしっとり仕上がりやすくなっています。あわせて保湿系下地と併用すると安心です。</p>
      </div>
      <div class="faq-item">
        <h3>Q2. 冬はリキッドファンデーションとパウダー、どちらが優れていますか？</h3>
        <p>真冬の極端な乾燥日のツヤ出しはリキッドが得意ですが、朝の手軽さ・マスクやマフラーへの色移りの少なさ・午後のお直しのしやすさではパウダーファンデーションに大きな利点があります。平日はパウダー、週末の外出はリキッドと使い分けるのも快適です。</p>
      </div>
      <div class="faq-item">
        <h3>Q3. スポンジとブラシ、冬場はどちらで塗るのがおすすめですか？</h3>
        <p>粉っぽさを極力なくしたい場合は、毛足の柔らかいファンデーションブラシでふんわり乗せると薄付きでツヤが出やすくなります。カバー力を出したい時はスポンジを使い、擦らず押さえて乗せてください。</p>
      </div>
      <div class="faq-item">
        <h3>Q4. パウダーファンデーションの仕上げにフェイスパウダーは必要ですか？</h3>
        <p>基本的には不要です。パウダーファンデーションの上からさらにルースパウダーを重ねると粉の層が厚くなり、11月・12月の乾燥した空気の下でカサつきやすくなります。どうしてもテカる小鼻だけ軽く乗せる程度に留めましょう。</p>
      </div>
    </section>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の乾燥崩れしないベースメイク特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <a href="/winter-base-makeup" class="internal-link-card">
          <strong>冬のベースメイク総合特集</strong>
          <span>乾燥崩れを防ぐファンデ＆下地の総まとめ</span>
        </a>
        <a href="/winter-makeup-primer" class="internal-link-card">
          <strong>冬の高保湿化粧下地特集</strong>
          <span>パウダーファンデを密着させる保湿プライマー</span>
        </a>
        <a href="/winter-powder" class="internal-link-card">
          <strong>冬の高保湿フェイスパウダー特集</strong>
          <span>うるおいを守るしっとり仕上げパウダー10選</span>
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

with open("winter-powder-foundation.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

print("Generated winter-powder-foundation.html successfully!")
