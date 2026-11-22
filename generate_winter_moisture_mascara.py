import json
import html

with open("fetched_3new_nov_dec_2026_1123.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

items = all_data["winter_moisture_mascara"]["items"]

details = [
    {
        "rank": 1,
        "finish_style": "繊維入りロング・ツヤ感フィルム",
        "display_name": "塗るつけまつげ ファイバーウィッグ ウルトラロング E",
        "care_ingredients": "加水分解シルク、リンゴ果実エキス、ハチミツ（保湿成分）",
        "off_method": "お湯だけでスルッとオフ（フィルムタイプ）",
        "brush_type": "緩やかカーブの密集ファイバーブラシ",
        "lead_comment": "「お湯落ちロング」の代名詞。パンダ目を防ぎながらぬるま湯だけでスッとほどける名品",
        "review_1": "日本のフィルムマスカラ文化を切り開いたイミュ『デジャヴュ ファイバーウィッグ ウルトラロング E』。今回の調査では楽天市場でレビュー160件超・★4.5（¥1,650）と安定した支持を維持しています。最大の魅力は、皮脂・汗・涙をはじく丈夫なフィルム皮膜でありながら、38℃前後のぬるま湯でしっかりふやかすと力を入れずにスルスル落ちる点にあります。",
        "review_2": "保湿成分として加水分解シルクやハチミツ、リンゴ果実エキスなどを配合しており、冬の乾燥した空調下でも液がまつ毛の上でパサパサに粉落ちしにくいのが特長。たっぷりのファイバーが毛先になめらかに繋がり、自まつ毛がそのまま伸びたような自然な長さとツヤを演出するため、忘年会や年末ランチなど近くで見られるシーンにも好印象です。",
        "fit_person": "ゴシゴシ洗顔による目元の乾燥小ジワをとにかく避けたい方、自然な自まつ毛延長感を求める方",
        "off_advice": "シャワーを直接当てるのではなく、両手にぬるま湯をためてまつ毛を15秒ほど浸してから指の腹でそっと撫でると、根元から綺麗に外れます。"
    },
    {
        "rank": 2,
        "finish_style": "カール持続・繊細ロング（第3のマスカラ）",
        "display_name": "ロング＆カールマスカラ アドバンストフィルム",
        "care_ingredients": "ツバキオイル、ローヤルゼリーエキス、アルガンオイル、野バラオイル（まつ毛美容液成分）",
        "off_method": "お湯＋洗顔料（または普段の洗顔）でオフ",
        "brush_type": "日本人の目に合いやすいカーブブラシ",
        "lead_comment": "「カールを下げたくないけどオフは楽にしたい」冬派の味方。4種の美容液オイルでまつ毛を保護",
        "review_1": "強力なキープ力で知られるヒロインメイクの中で、クレンジング負担を抑えたい層から厚い支持を得ているのが『アドバンストフィルム』シリーズです（レビュー90件・★4.73）。水と皮脂に強い成分と、お湯でふやける成分を組み合わせた「第3のマスカラ」処方により、冬のマスク蒸気でカールがダレやすい悩みとオフのしにくさを見事に両立しています。",
        "review_2": "注目したいのがツバキオイル、ローヤルゼリーエキス、アルガンオイル、野バラオイル（カニナバラ果実油）という4種のまつ毛美容液成分が組み込まれていること。乾燥しやすい11月・12月でもまつ毛がゴワゴワになりにくく、艶やかなロング仕上がりが一日中続きます。",
        "fit_person": "お湯落ちマスカラだとカールがすぐ落ちてしまう直毛まつ毛の方、冬のマスク蒸気に耐えるキープ力も欲しい方",
        "off_advice": "純粋なお湯のみ設計ではなく「お湯＋洗顔料」仕様です。最初にぬるま湯で十分ふやかしたあと、いつもの泡洗顔料を優しく馴染ませると摩擦なく落とせます。"
    },
    {
        "rank": 3,
        "finish_style": "極細ブラシ・セパレート素まつ毛風",
        "display_name": "マイラッシュ アドバンスト",
        "care_ingredients": "加水分解シルク、パンテノール、リンゴ果実エキス、センブリエキス（保湿成分）",
        "off_method": "お湯だけで簡単オフ（フィルムタイプ）",
        "brush_type": "スリム設計・特殊ストレート極細ブラシ",
        "lead_comment": "楽天レビュー390件超・★4.68。1,100円という価格でパンテノール等の保湿成分とお湯オフを実現",
        "review_1": "「繊細さと価格と落としやすさのバランスで右に出るものはない」とリピーターが絶えないオペラの『マイラッシュ アドバンスト』。繊維無配合ながら、毛先がすっと細く伸びる速乾フィルム液とスリムな極細ブラシの組み合わせによって、下まつ毛や目尻の短い毛までダマにならず1本ずつ綺麗にキャッチしてくれます。",
        "review_2": "さらに加水分解シルクやパンテノール、センブリエキスといった保湿・まつ毛ケア成分を含んでおり、乾燥した冬の室内でもパリパリと固まりすぎないしなやかな仕上がり。税込¥1,100でレビュー393件・★4.68という実績は伊達ではなく、アイクリームやバームをたっぷり塗った冬の目元にもにじみにくい頼もしい1本です。",
        "fit_person": "下まつ毛やまぶたの際まで繊細に塗りたい方、1,000円台で毎日気兼ねなく使えるお湯落ち定番品をお探しの方",
        "off_advice": "繊維が入っていないため、お湯でふやかしたときに黒いカスが散らばりにくく、スルッと綺麗に流しやすいのが朝晩ともに快適です。"
    },
    {
        "rank": 4,
        "finish_style": "ふんわりセパレート＆上品ロング",
        "display_name": "パーフェクトエクステンション マスカラ (お湯オフタイプ)",
        "care_ingredients": "加水分解ヒアルロン酸、パンテノール、センブリエキス、ツバキ種子油、アルガンオイル等10種の美容液成分",
        "off_method": "お湯＋洗顔料でオフ可能（ふわふわフィルムタイプ）",
        "brush_type": "日本人の目の幅にフィットするコンパクトブラシ",
        "lead_comment": "10種類の美容液成分を贅沢配合。自まつ毛が増えたような「ふんわり柔らか仕上がり」が大人メイクに最適",
        "review_1": "ドラッグストアやバラエティショップでも大人気のD-UP（ディーアップ）『パーフェクトエクステンション マスカラ』。※シリーズにはウォータープルーフ版（for カール）もありますが、今回ピックアップした定番のブラック（無印）は、お湯でふやかして優しくオフできるフィルム処方です（レビュー★4.86）。",
        "review_2": "特筆すべきは加水分解ヒアルロン酸やパンテノール、ツバキ種子油、ホホバ種子油など10種類もの保湿美容液成分を配合している点。冬の冷たい風で乾燥しがちなまつ毛をコーティングして艶を保ちつつ、日本人の目幅に合わせたコンパクトブラシがまぶたに液がつく失敗を防いでくれます。重ね塗りしてもひじき状にならない洗練された仕上がりです。",
        "fit_person": "まつ毛への保湿成分の豊富さを重視する方、重ねてもダマにならない上品な大人アイメイクに仕上げたい方",
        "off_advice": "購入時は「for カール（ウォータープルーフ）」と間違えないよう確認を。ぬるま湯でしっかりふやかしてから洗顔するとストレスなくオフできます。"
    },
    {
        "rank": 5,
        "finish_style": "デパコス名品・細身ロング＆にじみ耐性",
        "display_name": "ラッシュ パワー マスカラ ロング ウェアリング フォーミュラ",
        "care_ingredients": "パンテノール、加水分解コムギタンパク、ホホバ種子油（保湿・コンディショニング成分）",
        "off_method": "38〜39℃のぬるま湯だけでスルンとオフ",
        "brush_type": "細身・日本人向け精密コンパクトブラシ",
        "lead_comment": "楽天レビュー1,600件超・★4.75を誇るデパコス界の絶対王者。冬の涙目や保湿クリームにもびくともしない耐性",
        "review_1": "デパートコスメのお湯落ちマスカラを語るうえで外せない不動の名作が、クリニークの『ラッシュ パワー マスカラ』。楽天市場でもレビュー1,615件超・★4.75という圧倒的な支持を集め続けています。11月・12月は外気と室内の温度差で涙目になったり、目元乾燥対策の濃厚なアイクリームによってマスカラが下まぶたに移りやすくなったりしますが、この製品は皮脂や涙に極めて強い処方です。",
        "review_2": "それでいて39℃前後のぬるま湯を数秒なじませると、フィルム膜がふやけてすっと外れるギャップが長年愛される理由。細身のコンパクトブラシは奥二重や一重のまぶたにも当たりにくく、根元から毛先まで凛とした清潔感のある上向きまつ毛を作ってくれます。",
        "fit_person": "冬の濃厚なアイクリームやコンシーラーを使うと夕方にパンダ目になりやすい方、信頼できるデパコス名品を求める方",
        "off_advice": "体温より少し高めの38〜39℃のお湯を含ませたコットンをまつ毛に数秒当てるか、お湯をたっぷり馴染ませてから指で挟んで外すのが最もスムーズです。"
    },
    {
        "rank": 6,
        "finish_style": "韓国アイドル風・透け感束感コーム",
        "display_name": "ヌードアイラッシュ (美容液成分配合フィルム処方)",
        "care_ingredients": "パンテノール、加水分解ケラチン、加水分解シルク、ビオチノイルトリペプチド-1等",
        "off_method": "お湯オフ対応フィルム（落ちにくい日はリムーバー併用推奨）",
        "brush_type": "束感を作りやすい両面コーム型",
        "lead_comment": "トレンドの「繊細な束感」とシアー発色が1本で完成。パンテノール・ケラチン配合で冬まつ毛も補修",
        "review_1": "人気メイクアップアーティストのウォン・ジョンヨ氏プロデュースで話題の『ヌードアイラッシュ』（公式ショップ★4.48・170件超）。コーム型のアプリケーターがまつ毛を根元から綺麗にとかし上げ、抜け感のあるシアーブラックやブラウン発色で今っぽい透明感ある目元を演出します。12月のクリスマスデートやイベントメイクにもぴったりのトレンド感です。",
        "review_2": "繊維入りながらパンテノールや加水分解ケラチン、加水分解シルクなどの保湿補修成分が配合されており、乾燥しやすい冬のまつ毛を健やかに整える設計になっています。なお本品は「お湯落ち（フィルム）＋ウォータープルーフ特性」を兼ね備えているためキープ力が非常に高い反面、重ね塗りした日はお湯だけでは少し残りやすいこともあるため、落ちにくいと感じたら無理に擦らずポイントメイクリムーバーを併用するのが目元に優しい使い方です。",
        "fit_person": "ピンセット要らずで上品な束感まつ毛を作りたい方、黒々しすぎないシアー発色の冬メイクを楽しみたい方",
        "off_advice": "薄塗りの日は38℃程度のぬるま湯で15〜20秒ふやかしてから指で優しく外し、しっかり重ね塗りした日はマスカラリムーバーを使うと摩擦ゼロで落とせます。"
    },
    {
        "rank": 7,
        "finish_style": "まつ毛美容液発想・ハリコシボリューム",
        "display_name": "スカルプD マスカラ ボリュームアップ (ピュアフリー系美容液設計)",
        "care_ingredients": "ピロリジニルジアミノピリミジンオキシド、ビオチノイルトリペプチド-1、パンテノール、シスチン、グルタミン酸",
        "off_method": "お湯で簡単に落とせるフィルムタイプ",
        "brush_type": "まつ毛の根元から持ち上げる密着ブラシ",
        "lead_comment": "スカルプDのまつ毛美容液と同じケア成分を搭載。「日中メイクしながら本格まつ毛保湿」を叶える1本",
        "review_1": "まつ毛美容液で圧倒的知名度を誇るアンファー『スカルプD』から展開されている、ケアとメイクを同時にこなすマスカラ。「冬は空気が乾燥してまつ毛までパサつき・切れ毛が増えた気がする」という悩みに対し、スカルプDのまつ毛美容液と共通の保湿成分（パンテノール、ビオチノイルトリペプチド-1、ピロリジニルジアミノピリミジンオキシド等）や、毛髪補修成分のシスチン・グルタミン酸を贅沢に配合しています。",
        "review_2": "さらにパラベン・アルコール・鉱物油・シリコン・香料・合成着色料を使わないフリー設計で、デリケートな冬の目元への配慮も徹底。ミツロウやカルナウバロウなどの保護成分がしなやかな膜を作り、繊維なしでも1本1本を太く見せてくれるため、夕方まで存在感のあるぱっちり目元が続きます。",
        "fit_person": "メイク時間そのものをまつ毛保湿ケアに変えたい方、アルコールや香料・繊維による目への刺激を避けたい方",
        "off_advice": "繊維フリー＆フィルム処方なので、ぬるま湯を馴染ませるとスルンとほぐれやすく、夜のリセットが驚くほど快適です。"
    },
    {
        "rank": 8,
        "finish_style": "保湿美容ミネラル×多彩な質感展開",
        "display_name": "MOTE MASCARA (モテマスカラ)",
        "care_ingredients": "エンドミネラル（天然ミネラル鉱石）、パンテノール、加水分解シルク等（タイプ別処方）",
        "off_method": "ぬるま湯で落とせるWPフィルム処方",
        "brush_type": "タイプ別に最適化されたスマートブラシ",
        "lead_comment": "楽天レビュー1,210件超・★4.68のベストセラー。独自の天然ミネラル成分で塗りながらまつ毛を整える",
        "review_1": "楽天市場でもレビュー1,216件超・★4.68という驚異的な人気を誇るUZU BY FLOWFUSHIの『MOTE MASCARA』。全ラインナップにブランド独自の天然由来ミネラル成分「エンドミネラル」が配合されており、メイク中もまつ毛まわりの潤いケアを意識した設計が多くのユーザーから支持され続けています。",
        "review_2": "水・湿気・皮脂に強い先進フィルム処方のため、11月・12月の冷たい風で涙が出やすい日や、満員電車・マスク内の湿気にさらされてもにじみにくいのが強み。しかもオフはぬるま湯だけでスルンと落とせるため、毎日使ってもまつ毛や目周りの皮膚が乾燥でくたびれにくい優秀なアイテムです。",
        "fit_person": "自分の理想の仕上がり（マイクロ・ボリューム・ロング・カラー）を選びたい方、実績ある定番人気品を使いたい方",
        "off_advice": "湯船に浸かって顔全体が温まったタイミングでぬるま湯を馴染ませると、皮膜が一気に柔らかくなって引っ張らずに落とせます。"
    },
    {
        "rank": 9,
        "finish_style": "石けん＆お湯オフ・低刺激ミネラル処方",
        "display_name": "ミネラルロングラッシュマスカラ",
        "care_ingredients": "パンテノール、ツバキ種子油、ホホバ種子油、シロキクラゲ多糖体、ポリクオタニウム-51（リピジュア）",
        "off_method": "お湯＆石けんでオフ可能",
        "brush_type": "根元からすくいやすいスリムカーブブラシ",
        "lead_comment": "シロキクラゲ多糖体やリピジュアまで配合！肌と同じく乾燥する冬のまつ毛を守り、お湯＋石けんで落ちる",
        "review_1": "敏感肌向けミネラルコスメとして信頼されるエトヴォス（ETVOS）の『ミネラルロングラッシュマスカラ』。まつ毛ケア成分の充実度は特筆もので、パンテノールやツバキ種子油・ホホバ種子油に加え、スキンケアでも高保湿成分として有名な「シロキクラゲ多糖体」や「リピジュア（ポリクオタニウム-51）」まで配合されています。",
        "review_2": "界面活性剤やタール系色素、シリコンなど目元の負担になりやすい成分を極力避けた設計でありながら、天然ミネラル色素による深みのある発色と速乾カールの仕上がりが美しく、冬の上品なアイメイクにぴったり。クレンジングオイル不要でお湯と洗顔料（石けん）だけでオフできるため、目元の皮膚が薄く乾燥小ジワができやすい方にも安心です。",
        "fit_person": "目元が敏感で一般のマスカラだと痒みや乾燥を感じやすい方、石けんオフのベースメイクと統一したい方",
        "off_advice": "お湯で軽くふやかしてから優しい泡洗顔で包み込むように洗うだけで、目元の皮膚を引っ張らずにすっきり落とせます。"
    },
    {
        "rank": 10,
        "finish_style": "エアリーファイバー・ふわっと上向きロング",
        "display_name": "ラッシュニスタ N (お湯オフフィルムタイプ)",
        "care_ingredients": "保湿・柔軟ケア成分（軽いエアリーフィルム設計）",
        "off_method": "お湯で簡単オフ（フィルムタイプ）",
        "brush_type": "上向きカールを捉えるコンパクトフットブラシ",
        "lead_comment": "楽天公式レビュー930件超・★4.55。羽根のように軽いファイバーが冬の自まつ毛を優しく長く伸ばす",
        "review_1": "メイベリン ニューヨークの中でも長年「お湯で落とせるロングマスカラの定番」として公式ショップで931件以上・★4.55の高評価を獲得し続けている『ラッシュニスタ N』。通常のリフト系ウォータープルーフと違い、重みの少ないエアリーな黒いファイバーを配合しているため、時間が経ってもまつ毛が重さで下がりにくいのが特徴です。",
        "review_2": "しなやかなフィルム液がまつ毛1本1本を薄く包み込んで保護するため、乾燥した暖房室でもパリパリにひび割れたり目の下に粉落ちしたりしにくい安定感があります。プチプラ帯（¥1,507前後）でありながら、コームなしでもセパレートした長いまつ毛に仕上がるため、忙しい12月の朝メイクの時短にも役立ちます。",
        "fit_person": "マスカラの重みでまつ毛がすぐ下がってしまう方、コスパ良く毎日使える軽い付け心地のお湯オフ品を探している方",
        "off_advice": "お湯をたっぷり含ませるとフィルムが一気に柔らかくなるため、洗顔前のシャワー時ではなく手でぬるま湯をすくって優しくオフするのがおすすめです。"
    }
]

article_title = "冬の目元乾燥とパンダ目を同時に防ぐ！まつ毛を労わるお湯落ち高保湿・美容液マスカラ厳選10選【11月・12月】"
article_desc = "11月・12月のクリスマスや忘年会メイクが増える一方、クレンジング摩擦は目元の乾燥小ジワの原因に。デジャヴュ、ヒロインメイク アドバンストフィルム、オペラ、D-UP、クリニーク、ウォンジョンヨ、スカルプD、UZU、エトヴォス、メイベリンまでお湯落ち＆保湿美容液成分配合マスカラ10選を徹底比較。"
canonical_url = "https://lumi-cosme.vercel.app/winter-moisture-mascara"

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
            "name": "11月・12月向けお湯落ち高保湿・美容液マスカラ10選",
            "numberOfItems": 10,
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": it["rank"],
                    "item": {
                        "@type": "Product",
                        "name": f"{it['brand']} {det['display_name']}",
                        "image": it["image_url"],
                        "description": det["lead_comment"],
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
                    "name": "冬にウォータープルーフより「お湯落ち（フィルム）マスカラ」が向いているのはなぜですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "11月・12月は皮膚が極端に薄い目元の水分が奪われやすく、乾燥小ジワ（ちりめんジワ）が目立つ季節です。落ちにくいウォータープルーフマスカラをオイルやコットンで毎日強くこすり落とすと、まぶたのバリア機能とまつ毛のキューティクルが傷みます。ぬるま湯でふやけるフィルムタイプなら摩擦を最小限に抑えられます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "お湯落ちマスカラは冬の涙目や保湿クリームでにじみませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "従来の水溶性マスカラと違い、近年のフィルムマスカラ（クリニーク ラッシュパワー、デジャヴュ、オペラ等）は皮脂や冷水・涙には溶けにくく、約38℃前後のぬるま湯でふやかして初めて外れる構造になっています。目元のアイクリームを塗ったあとティッシュやフェイスパウダーで軽くキワを押さえておくと、さらににじみにくくなります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "「お湯だけで落ちるタイプ」と「お湯＋洗顔料タイプ」は何が違いますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "『お湯だけタイプ（デジャヴュ、オペラ、クリニーク、メイベリン等）』はぬるま湯を10〜20秒なじませるだけでスッと外れます。一方、『お湯＋洗顔料タイプ（ヒロインメイク アドバンストフィルム等）』はカールキープ力や耐水性を高めた設計のため、お湯でふやかしたあとに泡洗顔料を馴染ませることで摩擦なく落とせます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "マスカラのオフ時にまつ毛が抜けたり切れたりしないコツはありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "一番大切なのは『乾いた状態で指で引っ張らないこと』と『熱すぎるシャワーを直接当てないこと』です。36〜38℃程度のぬるま湯を両手にためて目元に15秒ほど当てて膜を十分にふやかしてから、指の腹で毛先方向へそっと滑らせてオフし、お風呂上がりはまつ毛美容液で保湿してあげると冬でも健やかなまつ毛を保てます。"
                    }
                }
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://lumi-cosme.vercel.app/"},
                {"@type": "ListItem", "position": 2, "name": "冬のベース＆ポイントメイク総合", "item": "https://lumi-cosme.vercel.app/winter-base-makeup"},
                {"@type": "ListItem", "position": 3, "name": "お湯落ち高保湿・美容液マスカラ10選", "item": canonical_url}
            ]
        }
    ]
}

table_rows = ""
for it, det in zip(items, details):
    table_rows += f"""            <tr>
              <td class="ms-t-rank">#{it['rank']}</td>
              <td><strong>{html.escape(it['brand'])}</strong><div class="ms-sub">{html.escape(det['display_name'])}</div></td>
              <td>{html.escape(det['finish_style'])}</td>
              <td>{html.escape(det['off_method'])}</td>
              <td>{html.escape(det['care_ingredients'])}</td>
              <td class="ms-t-price">¥{it['price']:,}</td>
            </tr>
"""

cards_html = ""
for it, det in zip(items, details):
    rate_html = (
        f'<span class="ms-rate">★ {it["review_average"]}（{it["review_count"]:,}件）</span>'
        if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
        else '<span class="ms-rate">楽天市場 確認済</span>'
    )
    cards_html += f"""
      <article class="ms-card" id="mascara-{it['rank']}">
        <header class="ms-card-top">
          <div class="ms-tag-line">
            <span class="ms-rank-chip">RANK {it['rank']}</span>
            <span class="ms-finish-chip">{html.escape(det['finish_style'])}</span>
            {rate_html}
          </div>
          <h3>{html.escape(it['brand'])} {html.escape(det['display_name'])}</h3>
          <p class="ms-lead">{html.escape(det['lead_comment'])}</p>
        </header>

        <div class="ms-mid-row">
          <div class="ms-img-panel">
            <img src="{html.escape(it['image_url'])}" alt="{html.escape(it['brand'])} {html.escape(det['display_name'])}" class="product-img" loading="lazy">
            <div class="ms-price-strip">
              <span>楽天市場 最新価格（税込）</span>
              <strong>¥{it['price']:,}</strong>
            </div>
            <a href="{html.escape(it['affiliate_url'])}" target="_blank" rel="noopener noreferrer nofollow sponsored" class="rakuten-btn">
              楽天市場でカラー・在庫を見る →
            </a>
            <div class="ms-item-ref">取得SKU：{html.escape(it['item_name'][:52])}</div>
          </div>

          <div class="ms-info-panel">
            <div class="ms-spec-list">
              <div class="ms-spec-item"><span>オフ方法</span><strong>{html.escape(det['off_method'])}</strong></div>
              <div class="ms-spec-item"><span>ブラシ設計</span><strong>{html.escape(det['brush_type'])}</strong></div>
              <div class="ms-spec-item ms-wide"><span>主なまつ毛保湿・保護成分</span><strong>{html.escape(det['care_ingredients'])}</strong></div>
            </div>

            <div class="ms-story">
              <p>{html.escape(det['review_1'])}</p>
              <p>{html.escape(det['review_2'])}</p>
            </div>

            <div class="ms-bottom-notes">
              <div class="ms-note">
                <strong>向いている目元・仕上がり</strong>
                <p>{html.escape(det['fit_person'])}</p>
              </div>
              <div class="ms-note">
                <strong>摩擦を減らす冬の落とし方</strong>
                <p>{html.escape(det['off_advice'])}</p>
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
  <meta name="keywords" content="お湯落ちマスカラ おすすめ 冬, 美容液マスカラ 保湿, 乾燥しないマスカラ, デジャヴュ ファイバーウィッグ, ヒロインメイク アドバンストフィルム, クリニーク ラッシュパワー, ウォンジョンヨ ヌードアイラッシュ, エトヴォス マスカラ">
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
      --plum: #9d174d;
      --plum-deep: #831843;
      --plum-soft: #fdf2f8;
      --plum-border: #fbcfe8;
      --bg: #fffbfc;
      --ink: #1f2937;
      --muted: #4b5563;
      --line: #e5e7eb;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.78;
    }}
    .ms-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--line);
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .ms-header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 13px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .ms-logo {{ font-weight: 800; font-size: 1.12rem; color: var(--plum-deep); text-decoration: none; }}
    .ms-nav {{ display: flex; gap: 14px; flex-wrap: wrap; font-size: 0.85rem; }}
    .ms-nav a {{ color: var(--plum); font-weight: 700; text-decoration: none; }}
    .ms-crumb {{ max-width: 1080px; margin: 14px auto 0; padding: 0 20px; font-size: 0.82rem; color: var(--muted); }}
    .ms-crumb a {{ color: var(--plum); text-decoration: none; }}
    main {{ max-width: 1080px; margin: 20px auto 64px; padding: 0 20px; }}

    .ms-hero {{
      background: linear-gradient(135deg, #fdf2f8 0%, #fce7f3 100%);
      border: 1px solid var(--plum-border);
      border-radius: 18px;
      padding: 36px 30px;
      margin-bottom: 26px;
    }}
    .ms-badge {{
      display: inline-block;
      background: var(--plum);
      color: #fff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 13px;
      border-radius: 999px;
      margin-bottom: 12px;
    }}
    .ms-hero h1 {{
      font-size: 1.7rem;
      line-height: 1.42;
      color: var(--plum-deep);
      margin-bottom: 12px;
    }}
    .ms-hero-meta {{ font-size: 0.84rem; color: var(--muted); margin-bottom: 14px; }}
    .ms-hero p {{ font-size: 0.96rem; margin-bottom: 10px; }}

    .ms-toc {{
      background: #fff;
      border: 1px solid var(--line);
      border-left: 5px solid var(--plum);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 28px;
    }}
    .ms-toc h2 {{ font-size: 1.05rem; color: var(--plum-deep); margin-bottom: 10px; }}
    .ms-toc ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 6px 18px;
    }}
    .ms-toc a {{ color: var(--plum); text-decoration: none; font-size: 0.91rem; font-weight: 600; }}

    .ms-box {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 28px;
      margin-bottom: 28px;
    }}
    .ms-box h2 {{
      font-size: 1.32rem;
      color: var(--plum-deep);
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--plum-soft);
    }}
    .ms-box p {{ font-size: 0.96rem; margin-bottom: 12px; }}

    .ms-3axis {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin-top: 14px;
    }}
    .ms-axis-card {{
      background: var(--plum-soft);
      border: 1px solid var(--plum-border);
      border-radius: 12px;
      padding: 18px;
    }}
    .ms-axis-card h3 {{ font-size: 1rem; color: var(--plum-deep); margin-bottom: 8px; }}
    .ms-axis-card p {{ font-size: 0.88rem; margin: 0; }}

    .ms-tbl-scroll {{ overflow-x: auto; margin-top: 14px; }}
    .ms-table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 780px;
      font-size: 0.86rem;
    }}
    .ms-table th {{
      background: var(--plum-deep);
      color: #fff;
      text-align: left;
      padding: 11px 12px;
    }}
    .ms-table td {{
      padding: 12px;
      border-bottom: 1px solid var(--line);
      vertical-align: top;
    }}
    .ms-table tr:nth-child(even) td {{ background: #fdfafb; }}
    .ms-t-rank {{ font-weight: 800; color: var(--plum); white-space: nowrap; }}
    .ms-t-price {{ font-weight: 700; color: var(--plum-deep); white-space: nowrap; }}
    .ms-sub {{ font-size: 0.77rem; color: var(--muted); font-weight: 400; margin-top: 2px; }}

    .ms-sec-title {{
      font-size: 1.4rem;
      color: var(--plum-deep);
      margin: 34px 0 18px;
      padding-left: 12px;
      border-left: 5px solid var(--plum);
    }}
    .ms-card {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 26px;
      margin-bottom: 24px;
      box-shadow: 0 2px 10px rgba(157, 23, 77, 0.05);
    }}
    .ms-card-top {{ margin-bottom: 18px; border-bottom: 1px solid var(--plum-soft); padding-bottom: 14px; }}
    .ms-tag-line {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 8px; }}
    .ms-rank-chip {{
      background: var(--plum-deep);
      color: #fff;
      font-weight: 800;
      font-size: 0.8rem;
      padding: 4px 11px;
      border-radius: 6px;
    }}
    .ms-finish-chip {{
      background: var(--plum-soft);
      color: var(--plum);
      border: 1px solid var(--plum-border);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .ms-rate {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #b45309;
      background: #fef3c7;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .ms-card-top h3 {{ font-size: 1.24rem; color: var(--ink); margin-bottom: 6px; }}
    .ms-lead {{ font-size: 0.92rem; color: var(--plum); font-weight: 700; }}

    .ms-mid-row {{
      display: grid;
      grid-template-columns: 250px 1fr;
      gap: 24px;
      align-items: start;
    }}
    .ms-img-panel {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 12px;
      text-align: center;
    }}
    .product-img {{ max-width: 100%; height: 205px; object-fit: contain; margin-bottom: 10px; }}
    .ms-price-strip {{
      background: var(--plum-soft);
      border-radius: 8px;
      padding: 8px 10px;
      margin-bottom: 10px;
    }}
    .ms-price-strip span {{ display: block; font-size: 0.73rem; color: var(--muted); }}
    .ms-price-strip strong {{ font-size: 1.32rem; color: var(--plum-deep); font-weight: 800; }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      text-align: center;
      background: #bf0000;
      color: #fff;
      font-weight: 800;
      font-size: 0.88rem;
      padding: 12px;
      border-radius: 8px;
      text-decoration: none;
    }}
    .rakuten-btn:hover {{ background: #990000; }}
    .ms-item-ref {{ margin-top: 8px; font-size: 0.71rem; color: var(--muted); line-height: 1.4; text-align: left; word-break: break-all; }}

    .ms-spec-list {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      background: #f9fafb;
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 12px 14px;
      margin-bottom: 14px;
    }}
    .ms-spec-item span {{ display: block; font-size: 0.73rem; color: var(--muted); }}
    .ms-spec-item strong {{ font-size: 0.85rem; color: var(--ink); }}
    .ms-wide {{ grid-column: 1 / -1; }}
    .ms-story p {{ font-size: 0.94rem; margin-bottom: 10px; }}

    .ms-bottom-notes {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: 12px;
    }}
    .ms-note {{
      background: var(--plum-soft);
      border: 1px solid var(--plum-border);
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 0.85rem;
    }}
    .ms-note strong {{ display: block; color: var(--plum-deep); margin-bottom: 4px; }}
    .ms-note p {{ margin: 0; font-size: 0.84rem; }}

    .ms-care-steps {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 14px;
      margin-top: 14px;
    }}
    .ms-care-card {{
      background: #fdfafb;
      border: 1px solid var(--line);
      border-top: 4px solid var(--plum);
      border-radius: 10px;
      padding: 16px;
    }}
    .ms-care-card h3 {{ font-size: 0.96rem; color: var(--plum-deep); margin-bottom: 6px; }}
    .ms-care-card p {{ font-size: 0.86rem; margin: 0; }}

    .faq-unit {{ border-bottom: 1px solid var(--line); padding: 14px 0; }}
    .faq-unit:last-child {{ border-bottom: none; }}
    .faq-unit h3 {{ font-size: 1rem; color: var(--plum-deep); margin-bottom: 6px; }}
    .faq-unit p {{ font-size: 0.92rem; margin: 0; }}

    .internal-links-box {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 24px;
      margin-top: 32px;
    }}
    .internal-links-title {{ font-weight: 800; font-size: 1.08rem; color: var(--plum-deep); margin-bottom: 14px; }}
    .internal-links-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; }}
    .internal-link-card {{ border: 1px solid var(--line); border-radius: 10px; padding: 12px; text-decoration: none; display: block; }}
    .internal-link-card:hover {{ border-color: var(--plum); }}

    footer {{ background: #111827; color: #9ca3af; padding: 44px 20px 30px; font-size: 0.84rem; }}
    .footer-inner {{ max-width: 1080px; margin: 0 auto; }}
    .footer-title {{ color: #f9fafb; font-weight: 800; margin-bottom: 14px; }}
    .footer-links-grid {{ display: flex; flex-wrap: wrap; gap: 8px 14px; margin-bottom: 24px; }}
    .footer-links-grid a {{ color: #d1d5db; text-decoration: none; font-size: 0.8rem; }}
    .footer-links-grid a:hover {{ color: #f9a8d4; text-decoration: underline; }}
    .copyright {{ border-top: 1px solid #1f2937; padding-top: 18px; text-align: center; font-size: 0.78rem; }}

    @media (max-width: 760px) {{
      .ms-hero {{ padding: 24px 18px; }}
      .ms-hero h1 {{ font-size: 1.32rem; }}
      .ms-mid-row, .ms-spec-list, .ms-bottom-notes {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header class="ms-header">
    <div class="ms-header-inner">
      <a href="/" class="ms-logo">Lumi Cosme</a>
      <nav class="ms-nav">
        <a href="/winter-base-makeup">冬ベースメイク総合</a>
        <a href="/winter-eyelash-serum">まつ毛美容液特集</a>
        <a href="/winter-cream-eyeshadow">高保湿アイシャドウ</a>
      </nav>
    </div>
  </header>

  <nav class="ms-crumb" aria-label="パンくずリスト">
    <a href="/">ホーム</a> &gt; <a href="/winter-base-makeup">冬のベース＆ポイントメイク特集</a> &gt; <span>お湯落ち高保湿・美容液マスカラ10選</span>
  </nav>

  <main>
    <section class="ms-hero">
      <span class="ms-badge">2026年11月・12月 目元乾燥＆まつ毛ケア特集</span>
      <h1>{html.escape(article_title)}</h1>
      <div class="ms-hero-meta">更新日：<time datetime="2026-11-23">2026年11月23日</time> ／ 編集部・アイメイク検証チーム</div>
      <p>
        イルミネーションやクリスマスパーティー、年末の集まりが増える11月・12月は、目元をぱっちり印象的に見せたくなる季節。しかし一方で、真冬は顔の中で最も皮膚が薄く皮脂腺も少ない「まぶた・目のキワ」の乾燥が深刻になりやすい時期でもあります。強力なウォータープルーフマスカラを毎晩ゴシゴシ擦って落としていると、まつ毛の切れ毛だけでなく目元の乾燥小ジワ（ちりめんジワ）を深めるきっかけになりかねません。
      </p>
      <p>
        そこで冬場に重宝するのが、<strong>38℃前後のぬるま湯（またはお湯＋洗顔料）で負担なく外せて、パンテノールや加水分解シルク・植物オイルなどの保湿成分を配合した「お湯落ち美容液マスカラ」</strong>です。本記事では、冬の涙目や保湿アイクリームでも下まぶたににじみにくい実力派10本を厳選し、落とし方の注意点まで含めて比較しました。
      </p>
    </section>

    <nav class="ms-toc" aria-label="目次">
      <h2>この記事でわかること</h2>
      <ul>
        <li><a href="#why-film">1. 冬の目元乾燥と「マスカラの落とし方」の深い関係</a></li>
        <li><a href="#choose-rule">2. 11月・12月にお湯落ち美容液マスカラを選ぶ3基準</a></li>
        <li><a href="#spec-table">3. お湯落ち・美容液マスカラ10選 比較テーブル</a></li>
        <li><a href="#mascara-rank">4. まつ毛を労わるお湯落ち高保湿マスカラ厳選10選</a></li>
        <li><a href="#off-guide">5. まつ毛を守って綺麗に落とす38℃ぬるま湯オフ3原則</a></li>
        <li><a href="#ms-faq">6. お湯落ちマスカラのよくある疑問 Q&amp;A</a></li>
      </ul>
    </nav>

    <section class="ms-box" id="why-film">
      <h2>1. なぜ冬は「お湯落ち（フィルム処方）× 美容液成分」が理想的なのか</h2>
      <p>
        アイメイクを落とすとき、どうしても目元は一日の汚れの中で最後に強く触れやすいパーツです。特に冬場は気温低下によってクレンジングオイルやリムーバーの馴染みがゆっくりになりやすく、ついコットンや指先に力が入ってしまいがちです。まぶたの表皮は頬の約3分の1程度の薄さしかないため、毎日の摩擦はすぐにかさつきや色素くすみ、乾燥小ジワへ直結します。
      </p>
      <p>
        その点、<strong>フィルムタイプのマスカラは「汗・涙・皮脂には溶けず、38℃前後のぬるま湯でふやけるとチューブ状にほどける」</strong>という仕組みを持っています。さらに近年はパンテノール、加水分解ケラチン、加水分解シルク、ツバキ種子油、シロキクラゲ多糖体といった保湿・補修成分が処方内に組み込まれており、日中の乾燥風からまつ毛のキューティクルを守りながら目元の印象をしっかり引き立ててくれます。
      </p>
    </section>

    <section class="ms-box" id="choose-rule">
      <h2>2. にじまず・傷めない冬マスカラを見極める3つの視点</h2>
      <div class="ms-3axis">
        <div class="ms-axis-card">
          <h3>① 「完全お湯オフ」か「お湯＋洗顔料オフ」かを把握する</h3>
          <p>デジャヴュ、オペラ、クリニーク、メイベリンはお湯のみで外れやすく、ヒロインメイク アドバンストフィルムやエトヴォスはぬるま湯＋洗顔料（石けん）ですっきり落ちる設計です。カール耐性と落としやすさの好みで選び分けましょう。</p>
        </div>
        <div class="ms-axis-card">
          <h3>② まつ毛保湿・補修成分（パンテノール／シルク／オイル）</h3>
          <p>スカルプDやD-UP、エトヴォスはまつ毛美容液に近い保湿成分が豊富。冬場に液がパサパサと粉落ちしにくい点でも保湿成分入りの恩恵は大きいです。</p>
        </div>
        <div class="ms-axis-card">
          <h3>③ 冬の保湿アイクリームとの相性（耐皮脂フィルム）</h3>
          <p>冬の朝にアイクリームやリキッドコンシーラーをしっかり塗る方ほど、油分でマスカラが溶けやすくなります。クリニークやUZUなど耐皮脂性の高いフィルムを選ぶと夕方までパンダ目を防げます。</p>
        </div>
      </div>
    </section>

    <section class="ms-box" id="spec-table">
      <h2>3. お湯落ち高保湿・美容液マスカラ10選 比較一覧</h2>
      <p>仕上がり傾向・オフ方法・主な保湿ケア成分・楽天市場での最新価格（税込）を一覧で比較できます。</p>
      <div class="ms-tbl-scroll">
        <table class="ms-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド / 商品名</th>
              <th>仕上がりタイプ</th>
              <th>オフ方法</th>
              <th>主な保湿・補修成分</th>
              <th>参考価格</th>
            </tr>
          </thead>
          <tbody>
{table_rows}          </tbody>
        </table>
      </div>
    </section>

    <h2 class="ms-sec-title" id="mascara-rank">4. お湯落ち高保湿・美容液マスカラ厳選ランキング10選</h2>
    <section aria-label="マスカラ詳細ランキング">
{cards_html}    </section>

    <section class="ms-box" id="off-guide">
      <h2>5. まつ毛を傷めず綺麗に外す「38℃ぬるま湯オフ」3原則</h2>
      <div class="ms-care-steps">
        <div class="ms-care-card">
          <h3>原則1：いきなり擦らず「15秒ふやかす」</h3>
          <p>お湯落ちマスカラが落ちにくいと感じる最大の原因は、ふやかす時間不足です。両手にぬるま湯（37〜39℃）をため、目元にそっと15秒ほど浸してフィルム膜を柔らかくするのが鉄則です。</p>
        </div>
        <div class="ms-care-card">
          <h3>原則2：熱いシャワー直当て＆横ゴシは厳禁</h3>
          <p>41℃以上の熱いシャワーを顔に直接当てると、まぶたの保湿成分まで流出して乾燥小ジワの原因に。ふやかした後は指の腹でまつ毛を挟み、根元から毛先へ縦にそっと抜きます。</p>
        </div>
        <div class="ms-care-card">
          <h3>原則3：重ね塗りした日はリムーバーに頼る</h3>
          <p>イベントなどで2〜3度重ね塗りした日や、密着度の高いハイブリッド処方を使った日は、無理に指で引っ張らずポイントメイクリムーバーで数秒浮かせてから落とす方が結果的にまつ毛が長持ちします。</p>
        </div>
      </div>
    </section>

    <section class="ms-box" id="ms-faq">
      <h2>6. 冬の美容液・お湯落ちマスカラ Q&amp;A</h2>
      <div class="faq-unit">
        <h3>Q1. お湯落ちマスカラと保湿アイクリームを一緒に使うと下まぶたに付きませんか？</h3>
        <p>朝にこってりしたアイクリームを塗った直後にマスカラを塗ると、油分がマスカラの密着を妨げて下まぶたに移りやすくなります。朝のアイケア後は少し時間を置き、目のキワだけルースパウダーを極薄くブラシで乗せてサラッとさせてからマスカラを塗ると夕方まで綺麗に保てます。</p>
      </div>
      <div class="faq-unit">
        <h3>Q2. ウォータープルーフと比べると、冬の雪や冷たい風の涙目には弱いですか？</h3>
        <p>水ではなく「体温より少し高い38℃前後のぬるま湯」で初めてふやけるように設計されているため、冷たい冬の涙や雪の湿気には強い製品が多くあります（特にクリニーク ラッシュパワー、UZU、ヒロインメイク アドバンストフィルム等）。</p>
      </div>
      <div class="faq-unit">
        <h3>Q3. 本当にまつ毛美容液成分がマスカラに入っていて意味はありますか？</h3>
        <p>マスカラは日中の10時間以上まつ毛に密着し続けるアイテムです。パンテノールや加水分解シルク、ツバキ種子油などの保湿成分が入っていることで、冬の乾燥によるまつ毛のパサつき・ゴワつきやひび割れを防ぎ、ハリのある状態を保つサポートになります。</p>
      </div>
      <div class="faq-unit">
        <h3>Q4. 1本どのくらいの期間で買い替えるのが衛生的ですか？</h3>
        <p>目元に直接使うアイテムであり、開封後に空気に触れて少しずつ水分が飛ぶとダマや粉落ちが起きやすくなるため、毎日使う場合は開封後3ヶ月程度を目安に新しいものへ交換するのが目元の健康と仕上がりの美しさを保つポイントです。</p>
      </div>
    </section>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の目元ケア＆ベースメイク特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <a href="/winter-eyelash-serum" class="internal-link-card">
          <div style="font-weight:700;color:#831843;margin-bottom:0.25rem;">高保湿まつ毛美容液10選</div>
          <div style="font-size:0.8rem;color:#4b5563;">夜のまつ育と冬の切れ毛対策に</div>
        </a>
        <a href="/winter-point-makeup-remover" class="internal-link-card">
          <div style="font-weight:700;color:#831843;margin-bottom:0.25rem;">高保湿ポイントメイクリムーバー10選</div>
          <div style="font-size:0.8rem;color:#4b5563;">目元の乾燥小ジワを防ぐ優しい落とし方</div>
        </a>
        <a href="/winter-base-makeup" class="internal-link-card">
          <div style="font-weight:700;color:#831843;margin-bottom:0.25rem;">冬の高保湿ベースメイク総合10選</div>
          <div style="font-size:0.8rem;color:#4b5563;">暖房でもひび割れないファンデ＆下地</div>
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

with open("winter-moisture-mascara.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

print("Generated winter-moisture-mascara.html successfully!")
