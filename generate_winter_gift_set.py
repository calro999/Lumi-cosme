import json
import html

with open("fetched_3new_nov_dec_2026_1123.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

items = all_data["winter_gift_set"]["items"]

details = [
    {
        "rank": 1,
        "price_tier": "3,000円〜4,000円台・王道ギフト",
        "display_name": "シア＆フラワー ハンドクリーム ギフトセット (タオル・入浴剤等ラッピング付)",
        "set_contents": "ロクシタン ハンドクリーム30mL＋タオルハンカチ・入浴剤/バスフィズ等ギフトセット",
        "wrapping_info": "ギフトラッピング済み・メッセージ対応ショップあり",
        "scent_profile": "シア（やさしい石けん系）／ヴァーベナ・チェリー・ローズ等",
        "moist_power": "天然保湿成分シアバター（シア脂）高配合",
        "headline": "楽天レビュー550件超・★4.64！年齢や好みを問わず12月に最も選ばれる鉄板ハンドケアギフト",
        "story_1": "クリスマスプレゼントや忘年会の景品、お世話になった同僚への年末の挨拶まで、「迷ったらこれを選べば間違いない」と言われる王道中の王道がロクシタンのハンドクリームギフト。今回の楽天市場確認ではレビュー555件超・★4.64（¥3,800）と圧倒的な実績を誇り、30mLのハンドクリームにタオルハンカチやバスアイテムが組み合わさった実用性の高いセットが支持されています。",
        "story_2": "単なる見た目のかわいさだけでなく、ロクシタンの代名詞であるシアバター（シア脂）をはじめとした植物由来保湿成分が冬の乾いた指先や甘皮周りにしっかり密着し、手洗い・消毒が増える11月・12月の手肌をなめらかに保ちます。色選びが必要な口紅やファンデーションと違い、相手のパーソナルカラーを問わず喜ばれる「外さない冬ギフト」の筆頭です。",
        "best_recipient": "職場の先輩・同僚、友人へのクリスマスギフト、3,000円〜4,000円予算のお礼プレゼント",
        "gift_tip": "定番のシアは男女問わず好かれやすい香りですが、フェミニンな方にはローズやチェリーブロッサム、爽やかな方にはヴァーベナを選ぶとよりパーソナル感が出ます。"
    },
    {
        "rank": 2,
        "price_tier": "7,000円台・センス抜群の大本命",
        "display_name": "アンドラム (レスレクション) アロマティック ハンドバーム ギフトセット",
        "set_contents": "ハンドバーム（75mL）＋リップクリーム等（ラッピング込・手提げ袋付）",
        "wrapping_info": "ラッピング済み・イソップ手提げ袋付き",
        "scent_profile": "マンダリン・ローズマリー・シダーウッド（洗練された柑橘ウッディハーブ）",
        "moist_power": "アーモンド油・ヤシ油・シア脂・乳酸Naによる濃密保湿",
        "headline": "おしゃれな人がもらって一番嬉しいユニセックス名品。ラッピング＆ショッパー付きですぐ渡せる",
        "story_1": "性別や年齢を問わず「センスが良いギフト」の象徴として愛され続けるAesop（イソップ）。そのアイコンである『アンドラム アロマティック ハンドバーム（旧名レスレクション）』を中心としたギフトセットは、手提げ袋とラッピングがセットになっており（¥7,970・★4.65/55件）、12月の大切な方への贈り物としてすぐ手渡せる安心感があります。",
        "story_2": "マンダリンやローズマリー、シダーウッドが織りなす深呼吸したくなるようなハーブの香りに加え、肌馴染みの良い植物エモリエントオイル（アーモンド油・ヤシ油・シア脂等）が冬のガサガサ手肌をしっとり柔らげつつ、ベタつきを残さずPCやスマホ作業にもすぐ戻れる使用感が秀逸。甘すぎる香りが苦手な方や男性へのプレゼントにも最適です。",
        "best_recipient": "恋人・パートナー、おしゃれに敏感な友人、男性へのクリスマス・誕生日ギフト",
        "gift_tip": "アルミチューブの見た目がインテリアにも映えるため、デスクワークが多い方への贈り物にするとデスクに置いて毎日使ってもらいやすくなります。"
    },
    {
        "rank": 3,
        "price_tier": "5,000円台・憧れかわいいギフトBOX",
        "display_name": "ホワイトフローラル ハンドクリーム30g＆リップマスク/バーム 純正ギフトBOX入り",
        "set_contents": "ハンドクリーム 30g＋リップバーム/マスク（純正ギフトBOX・ショップバッグ付）",
        "wrapping_info": "ジルスチュアート純正ギフトBOX入り",
        "scent_profile": "ホワイトフローラル（純白の花々と甘く清潔感のある香り）",
        "moist_power": "アーモンド油・ヴァージンココナッツオイル・カカオバター・マドンナリリーエキス",
        "headline": "純正ギフトBOXを開けた瞬間から心躍る！冬の乾燥手肌とカサつく唇を同時に潤す最強ペア",
        "story_1": "「もらった瞬間のときめき」を何より大切にしたいなら、ジルスチュアートの純正ギフトBOX入りセット（¥5,380・レビュー99件超・★4.64）が圧倒的な華やかさを放ちます。人気のホワイトフローラルの香りで統一されたハンドクリーム（30g）とリップケアアイテムの2点は、11月・12月のポーチに毎日入れて持ち歩きたくなる実用性です。",
        "story_2": "デザイン性だけでなく保湿の作り込みも本格派。アーモンドオイルやカカオバター、ヴァージンココナッツオイルなどのコクのあるエモリエント成分が手先や唇の水分蒸発を防ぎ、冷たい木枯らしに吹かれてもふっくら柔らかな状態をキープします。箱を開ける前から純正ボックスの存在感があるため、クリスマスデートの贈り物にもぴったりです。",
        "best_recipient": "彼女・奥様、妹や女友達へのクリスマスプレゼント、大人可愛いテイストが好きな方",
        "gift_tip": "純正ギフトBOXがセットになった出品なら追加のラッピング手配が不要。持ち運ぶ際も箱が潰れないよう紙袋付きか確認しておくと安心です。"
    },
    {
        "rank": 4,
        "price_tier": "7,000円台・バスタイム贅沢3点セット",
        "display_name": "ボディスクラブ60g＋ハンドクリーム30mL＋バスボム 3点ギフトセット",
        "set_contents": "ボディスクラブ 60g＋ハンドクリーム 30mL＋バスボム（3点ギフトセット）",
        "wrapping_info": "正規品ギフトセット包装",
        "scent_profile": "パチュリ・ラベンダー・バニラ／デリケート・ジャスミン／グリーン・ローズ等",
        "moist_power": "死海の塩×アーモンド油・ホホバ油・ボラージ油＋シアバター",
        "headline": "限定ホリデーとは別枠で選べる定番人気！冬のバスタイムで全身つるん＆しっとり潤う3点ギフト",
        "story_1": "11月・12月の寒い夜にお風呂で自分を労わる時間を贈れるのがSABON（サボン）の定番ボディ＆ハンドギフトセット（¥7,140・★5.0）。限定クリスマスコフレは早めに完売しやすい一方、こちらの定番ラインの3点セットは年末直前でも手に入れやすく、使い切りやすい60gのミニボトルスクラブ＋30mLハンドクリーム＋バスボムという充実の内容です。",
        "story_2": "サボンのボディスクラブは死海の塩による角質ケアと同時にホホバ種子油・アーモンド油・ルリジサ種子油（ボラージ油）などの植物オイルが全身をコーティングするため、洗い流した直後からボディミルクを塗った後のようなしっとり感に。さらにシアバター主体のハンドクリームとバスボムまで揃うため、「冬の乾燥ケアをまるごと贈る」特別感があります。",
        "best_recipient": "お風呂時間が好きな方、ボディの乾燥やゴワつきを気にしている友人・パートナーへの本命ギフト",
        "gift_tip": "スクラブの定番香調の中で迷ったら、爽やかで万人受けしやすい「グリーン・ローズ」か清潔感ある「デリケート・ジャスミン」を選ぶのが安心です。"
    },
    {
        "rank": 5,
        "price_tier": "8,000円台・ハイブランド純正ラッピング",
        "display_name": "ミス ディオール ハンド クリーム 50mL (国内正規品・純正ラッピング済)",
        "set_contents": "ミス ディオール ハンド クリーム 50mL（丸型リニューアル品・純正ギフトラッピング済）",
        "wrapping_info": "Dior純正ラッピング済み（国内正規品）",
        "scent_profile": "センティフォリアローズを中心とした優雅で可憐なフローラルノート",
        "moist_power": "ローズウォーター・シアバター・植物由来グリセリンによる濃密ケア",
        "headline": "楽天レビュー150件超・★4.79！Dior純正ラッピングの特別感とローズの潤いが手元に広がる名品",
        "story_1": "「やっぱりハイブランドの純正ラッピングされたギフトを渡したい」という12月の贈り物ニーズで高い満足度を誇るのが、ディオールの『ミス ディオール ハンド クリーム』（¥8,680・レビュー154件・★4.79）。コロンとした丸みのある洗練フォルムにリニューアルされたパッケージは、バッグやポーチから取り出すたびに気分を高めてくれます。",
        "story_2": "香り豊かなローズウォーターをベースにシアバターなど濃密な保湿成分を配合しており、肌に伸ばすとクリームがすっと溶け込んで爪の先までしっとり保護。香水の代わりになるほど上品に香るため、普段香水をつけない方にも喜ばれます。国内正規品＆純正ラッピング対応なので、そのままクリスマスツリーの下やディナーの席で渡せる手軽さも強みです。",
        "best_recipient": "特別な相手へのクリスマスギフト、絶対に外したくないお祝い・お礼、ハイブランド好きの方",
        "gift_tip": "純正ラッピング付きの商品はショップによってリボンの色や限定ショッパーの有無が異なるため、購入時に確認しておくとより完璧です。"
    },
    {
        "rank": 6,
        "price_tier": "8,000円台・清潔感No.1日本発ナチュラルギフト",
        "display_name": "ハンドソープ＆ハンドクリーム ハンドケアギフトセット",
        "set_contents": "クレイハンドソープ/ハンドウォッシュ＋ハンドクリーム/美容液（箱入りギフトセット）",
        "wrapping_info": "SHIROギフトボックス入りセット",
        "scent_profile": "サボン（石けん）／ホワイトリリー（清楚な花）／ホワイトティー（上品な紅茶）",
        "moist_power": "がごめ昆布エキス（フコイダン）・アロエベラ液汁・シア脂・ホホバ油",
        "headline": "石けんと紅茶の香りで性別・年代問わず絶大な人気！冬の「手洗い→即保湿」を叶えるセット",
        "story_1": "日本発ナチュラルコスメブランドとして幅広い世代から絶大な支持を集めるSHIRO（シロ）。中でも冬のギフトとして実用性が高いのが、手を洗うたび潤いを守るハンドウォッシュと、みずみずしく手肌を整えるハンドクリームが組まれたギフトセット（¥8,800・★5.0）です。",
        "story_2": "SHIROのスキンケア・ボディケアの強みは、北海道産の「がごめ昆布」から抽出される保水多糖体（フコイダン）やアロエベラ・シア脂など、自然の素材を活かした潤い設計にあります。11月・12月は冷水やアルコール消毒で手荒れが加速しやすい季節だからこそ、「洗うアイテムと塗るアイテムが同じ清潔感ある香りで揃う」セットは日常の満足度をぐっと引き上げます。",
        "best_recipient": "清潔感やナチュラルさを好む方、結婚祝いや新居祝い兼クリスマスギフト、目上の方へのお礼",
        "gift_tip": "一番万人受けするのは爽やかな「サボン」や落ち着く「ホワイトティー」、少し女性らしさを添えたい場合は上品な「ホワイトリリー」が人気です。"
    },
    {
        "rank": 7,
        "price_tier": "5,000円〜6,000円台・冬の乾燥髪ケアギフト",
        "display_name": "ヘアドライタオル＆シャンプー・コンディショナー・ヘアミルク ギフトセット",
        "set_contents": "ヘアドライタオル1枚＋シャンプー・コンディショナー＋ヘアミルク ギフトセット",
        "wrapping_info": "公式系ギフトボックス仕様",
        "scent_profile": "シトラス・ラベンダー・イランイラン等のオーガニック精油ブレンド",
        "moist_power": "植物由来保湿オイル・アミノ酸系洗浄＋アウトバスヘアミルク保湿",
        "headline": "マフラー摩擦や静電気で髪がパサつく冬に嬉しい！タオル＋インバス＆アウトバスの充実ヘアギフト",
        "story_1": "ハンドクリームやリップのギフトは毎年もらいがち……という相手に差をつけられるのが、ジョンマスターオーガニックの『タオル＆ヘアケア ギフトセット』（¥5,980・レビュー★4.86）です。吸水性のあるヘアドライタオルに、シャンプー・コンディショナー、さらに冬の静電気やドライヤー熱から髪を守るヘアミルクまで揃った実用派セットとなっています。",
        "story_2": "11月・12月はタートルネックやマフラーとの摩擦、室内暖房による空気乾燥で毛先が急にゴワつきやすくなる季節。保湿力の高いヘアミルクと優しい洗い心地のヘアケアがセットになっていることで、受け取ったその夜から自宅のお風呂でリッチなヘアケア時間を体験してもらえます。",
        "best_recipient": "すでにハンドクリームをたくさん持っていそうな方、ロングヘアや冬の髪の乾燥・広がりに悩む方",
        "gift_tip": "消耗品であるヘアケアと毎日使えるタオルの組み合わせなので、相手の好みが読みにくい親戚や仕事仲間へのギフトにも重宝します。"
    },
    {
        "rank": 8,
        "price_tier": "6,000円台・本格英国オーガニック箱入り",
        "display_name": "ハンドケア トリオギフト (公式ギフト箱入り)",
        "set_contents": "オーガニックハンドクリーム・ハンド用美容液等トリオセット（ギフト箱入り）",
        "wrapping_info": "公式・数量限定ギフト箱入り",
        "scent_profile": "ワイルドローズ・ゼラニウム・オレンジ・フランキンセンス（本格アロマ精油）",
        "moist_power": "オーガニックローズヒップ油（カニナバラ果実油）・ヒアルロン酸・植物バター",
        "headline": "英国発オーガニックの老舗ニールズヤード公式ギフト。手肌のエイジングケアまで叶える濃厚処方",
        "story_1": "人工的な合成香料ではなく、本物のエッセンシャルオイル（精油）の香りで深い安らぎを贈りたいときに選びたいのが、英国発オーガニックブランド『ニールズヤード レメディーズ』の公式ギフト箱入りセット（¥6,930・★4.83）です。ブルーの象徴的なパッケージと温かみのあるギフトボックスは、大人の落ち着きを感じさせます。",
        "story_2": "人気のワイルドローズ系アイテムに含まれるローズヒップ油は「ビタミンの宝庫」とも呼ばれ、乾燥でくすみがちな冬の手肌や爪周りにツヤとハリをもたらしてくれます。ハンドクリームだけでなくハンド用美容液が組み合わされた贅沢なセットは、家事や仕事で手先を酷使する大人世代への感謝のギフトにぴったりです。",
        "best_recipient": "30代〜60代以上の大人世代、オーガニック志向・天然アロマが好きな方、お母様への冬ギフト",
        "gift_tip": "もっと気軽な2,000円台のプチギフトとして贈りたい場合は、同ブランドの「ワイルドローズ ハンドケアプチギフト（ギフト箱入り ¥2,200）」という選択肢もあります。"
    },
    {
        "rank": 9,
        "price_tier": "3,000円台・名入れ対応プチギフト",
        "display_name": "ハンカチ＆ハンドクリーム 名入れギフトセット",
        "set_contents": "ポール＆ジョー ハンカチ（名入れ刺繍対応）＋ハンドクリーム ギフトセット",
        "wrapping_info": "ギフト包装対応（ハンカチ名入れ可）",
        "scent_profile": "オレンジフラワーやハーブを基調とした心地よいシトラスフローラル",
        "moist_power": "古木オリーブオイル・オレンジフラワー水・シアバター",
        "headline": "3,000円台でハンカチへの「名入れ」まで可能！特別感と実用性を兼ねたプチプライス冬ギフト",
        "story_1": "「予算は3,000円台に抑えたいけれど、ちょっと気の利いた特別なプレゼントにしたい」というニーズに完璧に応えるのが、ポール＆ジョーの『名入れハンカチ＆ハンドクリーム ギフトセット』（¥3,280・★5.0）です。猫やクリザンテーム（西洋菊）など愛らしいデザインで人気のハンカチに名前を入れられるため、量産品とは違う「あなたのために選んだ感」が伝わります。",
        "story_2": "ハンドクリームも名品揃いのポール＆ジョーらしく、地中海の古木オリーブオイルやオレンジフラワー水、シア脂などの潤い成分を配合。ベタつかずさらっと馴染む使用感なので、外出先で手を拭いてそのまま塗れる「ハンカチ＋ハンドクリーム」の組み合わせは11月・12月の日常使いにおいて最高に相性が良いペアです。",
        "best_recipient": "友人へのクリスマスプレゼント、送別会・誕生日・ちょっとしたお礼（3,000円予算）",
        "gift_tip": "名入れ刺繍が入る場合は通常の即日発送より数日多く納期がかかることがあるため、12月中旬以降のクリスマス用は早めに注文を済ませるのが鉄則です。"
    },
    {
        "rank": 10,
        "price_tier": "4,000円台・冬の極上温浴＆保湿ギフト",
        "display_name": "ギフトセット バスエッセンス (メディテーションバス50mL・タオル・バッグ付)",
        "set_contents": "アユーラ メディテーションバス（浴用化粧料 50mL）＋タオル・ハンディバッグ付ギフト",
        "wrapping_info": "ギフトバッグ・タオル付きセット",
        "scent_profile": "ローズマリー・カモミール等の安らかなアロマティックハーブ",
        "moist_power": "保湿エモリエント成分配合・乳白色のまろやかな湯質で湯上がり肌しっとり",
        "headline": "冬ギフトの隠れた大ヒット！冷えた体を芯から温め、湯上がりの全身まで潤すアユーラの癒やしセット",
        "story_1": "「ハンドクリームやリップはすでに好みがあるかもしれない」という方へ贈って絶賛されやすいのが、アユーラの超ロングセラー入浴剤『メディテーションバス』を中心としたギフトセット（¥4,070・★5.0）。ハンディバッグとタオルが最初から付属しているため、見栄え良くスマートに渡すことができます。",
        "story_2": "2層式のオイル＆保湿エッセンスがお湯に溶け込むと乳白色の柔らかなお湯になり、ローズマリーやカモミールを中心とした穏やかなハーブの香りが浴室いっぱいに広がります。11月・12月の寒さでこわばった身体を芯から温めつつ、肌あたりの柔らかな保湿ベールで湯上がりのカサつき・かゆみまで和らげてくれる、まさに冬ならではの極上リラックスギフトです。",
        "best_recipient": "忙しく働いている友人・家族、冷え性や睡眠の質を気にしている方、年末年始の癒やしギフト",
        "gift_tip": "入浴剤タイプは「バスタブに浸かる習慣があるか」だけさりげなく確認しておくと、間違いなく喜んでもらえます。"
    }
]

article_title = "11月・12月の贈り物に外さない！冬の乾燥肌を潤す人気ブランド高保湿ハンド＆ボディ・リップギフトセット厳選10選"
article_desc = "クリスマスや忘年会・年末のお礼に喜ばれる定番人気ブランドの高保湿ギフトセットを厳選！ロクシタン、イソップ、ジルスチュアート、サボン、ディオール、SHIRO、ジョンマスターオーガニック、ニールズヤード、ポール＆ジョー、アユーラまで予算別・贈る相手別に最新価格で徹底比較。"
canonical_url = "https://lumi-cosme.vercel.app/winter-gift-set"

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
            "name": "11月・12月向け人気ブランド高保湿ギフトセット10選",
            "numberOfItems": 10,
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": it["rank"],
                    "item": {
                        "@type": "Product",
                        "name": f"{it['brand']} {det['display_name']}",
                        "image": it["image_url"],
                        "description": det["headline"],
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
                    "name": "クリスマスコフレと定番の高保湿ギフトセット、11月・12月の贈り物にはどちらがおすすめですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "限定デザインやメイクパレットを楽しみたい場合はクリスマスコフレが魅力的ですが、11月下旬〜12月はすでに人気コフレが完売していたり色選びが難しかったりするケースも多いです。ロクシタン、イソップ、SHIRO、SABON、ディオールなどの『定番・ギフトボックス入り高保湿ケアセット』は在庫が安定しており、相手の肌色やメイクの好みに左右されず確実に愛用してもらえるのが大きなメリットです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "予算3,000円〜5,000円前後で本当に高見えする冬ギフトはどれですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "3,000円〜4,000円台なら『ロクシタンのハンドクリームギフトセット（¥3,800）』『ポール＆ジョーの名入れハンカチ＆ハンドクリーム（¥3,280）』『アユーラのメディテーションバス ギフト（¥4,070）』、5,000円台なら純正BOX入りの『ジルスチュアート ホワイトフローラルセット（¥5,380）』や『ジョンマスターオーガニックのタオル＆ヘアケアギフト（¥5,980）』が見栄えと実用性の両面で非常に好評です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "男性へのプレゼントや、甘い香りが苦手な相手にも贈れる保湿ギフトはありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい。ユニセックスなハーブ＆ウッディ系が魅力の『イソップ（Aesop）アンドラム ハンドバーム ギフト』、清潔感のある石けんや紅茶の香りの『SHIRO サボン／ホワイトティー ギフト』、森のハーブ調が落ち着く『アユーラ メディテーションバス ギフト』は男女問わず喜ばれやすい香りです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "楽天市場でギフトセットを買うときに失敗しないチェックポイントは？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "①『純正BOX・ラッピング・手提げ袋（ショッパー）』が同梱されているか（箱なし訳あり品ではないか）、②12月はクリスマス直前に配送が混み合い、名入れ商品などは通常より日数がかかるため余裕を持って注文すること、の2点を商品ページで確認しておくと安心です。"
                    }
                }
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://lumi-cosme.vercel.app/"},
                {"@type": "ListItem", "position": 2, "name": "冬の手荒れ防止ハンドケア特集", "item": "https://lumi-cosme.vercel.app/winter-hand-care"},
                {"@type": "ListItem", "position": 3, "name": "11月・12月向け高保湿ギフトセット10選", "item": canonical_url}
            ]
        }
    ]
}

table_rows = ""
for it, det in zip(items, details):
    table_rows += f"""            <tr>
              <td class="gf-rank">{it['rank']}位</td>
              <td><strong>{html.escape(it['brand'])}</strong><div class="gf-sub">{html.escape(det['display_name'])}</div></td>
              <td>{html.escape(det['set_contents'])}</td>
              <td>{html.escape(det['scent_profile'])}</td>
              <td>{html.escape(det['wrapping_info'])}</td>
              <td class="gf-price">¥{it['price']:,}</td>
            </tr>
"""

cards_html = ""
for it, det in zip(items, details):
    rate_badge = (
        f'<span class="gf-rate">★ {it["review_average"]}（{it["review_count"]:,}件）</span>'
        if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
        else '<span class="gf-rate">楽天市場 在庫確認済</span>'
    )
    cards_html += f"""
      <article class="gf-card" id="gift-{it['rank']}">
        <div class="gf-card-top">
          <div class="gf-badges">
            <span class="gf-rank-badge">GIFT {it['rank']}</span>
            <span class="gf-tier-badge">{html.escape(det['price_tier'])}</span>
            {rate_badge}
          </div>
          <h3>{html.escape(it['brand'])} {html.escape(det['display_name'])}</h3>
          <p class="gf-headline">{html.escape(det['headline'])}</p>
        </div>

        <div class="gf-content-grid">
          <div class="gf-visual-col">
            <div class="gf-img-frame">
              <img src="{html.escape(it['image_url'])}" alt="{html.escape(it['brand'])} {html.escape(det['display_name'])}" class="product-img" loading="lazy">
            </div>
            <div class="gf-price-box">
              <span class="gf-p-cap">楽天市場 最新確認価格（税込）</span>
              <span class="gf-p-num">¥{it['price']:,}</span>
            </div>
            <a href="{html.escape(it['affiliate_url'])}" target="_blank" rel="noopener noreferrer nofollow sponsored" class="rakuten-btn">
              楽天市場でラッピング・詳細を見る →
            </a>
            <div class="gf-sku">掲載商品：{html.escape(it['item_name'][:52])}</div>
          </div>

          <div class="gf-detail-col">
            <div class="gf-meta-grid">
              <div><span>セット内容</span><strong>{html.escape(det['set_contents'])}</strong></div>
              <div><span>ラッピング・袋</span><strong>{html.escape(det['wrapping_info'])}</strong></div>
              <div><span>香りの系統</span><strong>{html.escape(det['scent_profile'])}</strong></div>
              <div><span>保湿ポイント</span><strong>{html.escape(det['moist_power'])}</strong></div>
            </div>

            <div class="gf-prose">
              <p>{html.escape(det['story_1'])}</p>
              <p>{html.escape(det['story_2'])}</p>
            </div>

            <div class="gf-advice-row">
              <div class="gf-advice-card">
                <strong>こんな贈る相手・シーンに最適</strong>
                <p>{html.escape(det['best_recipient'])}</p>
              </div>
              <div class="gf-advice-card">
                <strong>選び方・渡し方のワンポイント</strong>
                <p>{html.escape(det['gift_tip'])}</p>
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
  <meta name="keywords" content="クリスマスプレゼント コスメ ギフトセット, 冬 保湿 ギフト 女性, ロクシタン ハンドクリーム ギフト, イソップ ギフト, ジルスチュアート ギフト, サボン ギフト, ディオール ハンドクリーム ギフト, SHIRO ギフト, アユーラ ギフト">
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
      --forest: #15803d;
      --forest-deep: #14532d;
      --forest-soft: #f0fdf4;
      --forest-line: #bbf7d0;
      --gold: #b45309;
      --gold-soft: #fffbeb;
      --cream-bg: #fafaf9;
      --ink: #1c1917;
      --muted: #57534e;
      --border: #e7e5e4;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      background: var(--cream-bg);
      color: var(--ink);
      line-height: 1.78;
    }}
    .gf-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .gf-header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 13px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .gf-brand {{ font-weight: 800; font-size: 1.12rem; color: var(--forest-deep); text-decoration: none; }}
    .gf-nav {{ display: flex; gap: 14px; flex-wrap: wrap; font-size: 0.85rem; }}
    .gf-nav a {{ color: var(--forest); font-weight: 700; text-decoration: none; }}
    .gf-crumb {{ max-width: 1080px; margin: 14px auto 0; padding: 0 20px; font-size: 0.82rem; color: var(--muted); }}
    .gf-crumb a {{ color: var(--forest); text-decoration: none; }}
    main {{ max-width: 1080px; margin: 20px auto 64px; padding: 0 20px; }}

    .gf-hero {{
      background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 60%, #fefce8 100%);
      border: 1px solid var(--forest-line);
      border-radius: 18px;
      padding: 36px 30px;
      margin-bottom: 26px;
    }}
    .gf-tag {{
      display: inline-block;
      background: var(--forest-deep);
      color: #fef08a;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 13px;
      border-radius: 999px;
      margin-bottom: 12px;
    }}
    .gf-hero h1 {{
      font-size: 1.7rem;
      line-height: 1.42;
      color: var(--forest-deep);
      margin-bottom: 12px;
    }}
    .gf-hero-meta {{ font-size: 0.84rem; color: var(--muted); margin-bottom: 14px; }}
    .gf-hero p {{ font-size: 0.96rem; margin-bottom: 10px; }}

    .budget-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 14px;
      margin-bottom: 28px;
    }}
    .budget-box {{
      background: #fff;
      border: 1px solid var(--border);
      border-top: 4px solid var(--forest);
      border-radius: 12px;
      padding: 16px 18px;
    }}
    .budget-box span {{ font-size: 0.76rem; font-weight: 800; color: var(--gold); display: block; margin-bottom: 4px; }}
    .budget-box strong {{ display: block; font-size: 0.98rem; color: var(--forest-deep); margin-bottom: 6px; }}
    .budget-box p {{ font-size: 0.84rem; color: var(--muted); margin: 0; }}

    .gf-toc {{
      background: #fff;
      border: 1px solid var(--border);
      border-left: 5px solid var(--forest);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 28px;
    }}
    .gf-toc h2 {{ font-size: 1.05rem; color: var(--forest-deep); margin-bottom: 10px; }}
    .gf-toc ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 6px 18px;
    }}
    .gf-toc a {{ color: var(--forest); text-decoration: none; font-size: 0.91rem; font-weight: 600; }}

    .gf-section {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 28px;
      margin-bottom: 28px;
    }}
    .gf-section h2 {{
      font-size: 1.32rem;
      color: var(--forest-deep);
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--forest-soft);
    }}
    .gf-section p {{ font-size: 0.96rem; margin-bottom: 12px; }}

    .gf-3reasons {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin-top: 14px;
    }}
    .gf-reason {{
      background: var(--forest-soft);
      border: 1px solid var(--forest-line);
      border-radius: 12px;
      padding: 18px;
    }}
    .gf-reason h3 {{ font-size: 1rem; color: var(--forest-deep); margin-bottom: 8px; }}
    .gf-reason p {{ font-size: 0.88rem; margin: 0; }}

    .gf-tbl-wrap {{ overflow-x: auto; margin-top: 14px; }}
    .gf-table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 780px;
      font-size: 0.86rem;
    }}
    .gf-table th {{
      background: var(--forest-deep);
      color: #fff;
      text-align: left;
      padding: 11px 12px;
    }}
    .gf-table td {{
      padding: 12px;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }}
    .gf-table tr:nth-child(even) td {{ background: #fafaf9; }}
    .gf-rank {{ font-weight: 800; color: var(--forest); white-space: nowrap; }}
    .gf-price {{ font-weight: 700; color: var(--forest-deep); white-space: nowrap; }}
    .gf-sub {{ font-size: 0.77rem; color: var(--muted); font-weight: 400; margin-top: 2px; }}

    .gf-sec-title {{
      font-size: 1.4rem;
      color: var(--forest-deep);
      margin: 34px 0 18px;
      padding-left: 12px;
      border-left: 5px solid var(--forest);
    }}
    .gf-card {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 26px;
      margin-bottom: 24px;
      box-shadow: 0 2px 10px rgba(21, 128, 61, 0.05);
    }}
    .gf-card-top {{ margin-bottom: 18px; }}
    .gf-badges {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 10px; }}
    .gf-rank-badge {{
      background: var(--forest-deep);
      color: #fef08a;
      font-weight: 800;
      font-size: 0.8rem;
      padding: 4px 11px;
      border-radius: 6px;
    }}
    .gf-tier-badge {{
      background: var(--gold-soft);
      color: var(--gold);
      border: 1px solid #fde68a;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .gf-rate {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #b45309;
      background: #fef3c7;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .gf-card-top h3 {{ font-size: 1.24rem; color: var(--ink); margin-bottom: 6px; }}
    .gf-headline {{ font-size: 0.92rem; color: var(--forest); font-weight: 700; }}

    .gf-content-grid {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 24px;
      align-items: start;
    }}
    .gf-img-frame {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px;
      text-align: center;
      margin-bottom: 12px;
    }}
    .product-img {{ max-width: 100%; height: 210px; object-fit: contain; }}
    .gf-price-box {{
      background: var(--forest-soft);
      border-radius: 10px;
      padding: 10px 12px;
      text-align: center;
      margin-bottom: 10px;
    }}
    .gf-p-cap {{ display: block; font-size: 0.74rem; color: var(--muted); }}
    .gf-p-num {{ font-size: 1.35rem; font-weight: 800; color: var(--forest-deep); }}
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
    .gf-sku {{ margin-top: 8px; font-size: 0.72rem; color: var(--muted); line-height: 1.4; word-break: break-all; }}

    .gf-meta-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      background: #fafaf9;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 12px 14px;
      margin-bottom: 14px;
      font-size: 0.84rem;
    }}
    .gf-meta-grid div span {{ display: block; font-size: 0.73rem; color: var(--muted); }}
    .gf-prose p {{ font-size: 0.94rem; margin-bottom: 10px; }}

    .gf-advice-row {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: 12px;
    }}
    .gf-advice-card {{
      background: var(--forest-soft);
      border: 1px solid var(--forest-line);
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 0.85rem;
    }}
    .gf-advice-card strong {{ display: block; color: var(--forest-deep); margin-bottom: 4px; }}
    .gf-advice-card p {{ margin: 0; font-size: 0.84rem; }}

    .gf-checklist {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px;
      margin-top: 14px;
    }}
    .gf-check-item {{
      background: #fafaf9;
      border: 1px solid var(--border);
      border-top: 4px solid var(--gold);
      border-radius: 10px;
      padding: 16px;
    }}
    .gf-check-item h3 {{ font-size: 0.95rem; color: var(--forest-deep); margin-bottom: 6px; }}
    .gf-check-item p {{ font-size: 0.85rem; margin: 0; }}

    .faq-block {{ border-bottom: 1px solid var(--border); padding: 14px 0; }}
    .faq-block:last-child {{ border-bottom: none; }}
    .faq-block h3 {{ font-size: 1rem; color: var(--forest-deep); margin-bottom: 6px; }}
    .faq-block p {{ font-size: 0.92rem; margin: 0; }}

    .internal-links-box {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
      margin-top: 32px;
    }}
    .internal-links-title {{ font-weight: 800; font-size: 1.08rem; color: var(--forest-deep); margin-bottom: 14px; }}
    .internal-links-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; }}
    .internal-link-card {{ border: 1px solid var(--border); border-radius: 10px; padding: 12px; text-decoration: none; display: block; }}
    .internal-link-card:hover {{ border-color: var(--forest); }}

    footer {{ background: #141715; color: #a8a29e; padding: 44px 20px 30px; font-size: 0.84rem; }}
    .footer-inner {{ max-width: 1080px; margin: 0 auto; }}
    .footer-title {{ color: #fafaf9; font-weight: 800; margin-bottom: 14px; }}
    .footer-links-grid {{ display: flex; flex-wrap: wrap; gap: 8px 14px; margin-bottom: 24px; }}
    .footer-links-grid a {{ color: #d6d3d1; text-decoration: none; font-size: 0.8rem; }}
    .footer-links-grid a:hover {{ color: #86efac; text-decoration: underline; }}
    .copyright {{ border-top: 1px solid #292524; padding-top: 18px; text-align: center; font-size: 0.78rem; }}

    @media (max-width: 760px) {{
      .gf-hero {{ padding: 24px 18px; }}
      .gf-hero h1 {{ font-size: 1.32rem; }}
      .gf-content-grid, .gf-meta-grid, .gf-advice-row {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header class="gf-header">
    <div class="gf-header-inner">
      <a href="/" class="gf-brand">Lumi Cosme</a>
      <nav class="gf-nav">
        <a href="/winter-holiday-coffret">クリスマスコフレ特集</a>
        <a href="/winter-hand-care">ハンドケア総合</a>
        <a href="/winter-body-care">ボディケア総合</a>
      </nav>
    </div>
  </header>

  <nav class="gf-crumb" aria-label="パンくずリスト">
    <a href="/">ホーム</a> &gt; <a href="/winter-hand-care">冬の手荒れ防止ハンドケア特集</a> &gt; <span>人気ブランド高保湿ギフトセット10選</span>
  </nav>

  <main>
    <section class="gf-hero">
      <span class="gf-tag">2026年11月・12月 クリスマス＆年末ギフト特集</span>
      <h1>{html.escape(article_title)}</h1>
      <div class="gf-hero-meta">更新日：<time datetime="2026-11-23">2026年11月23日</time> ／ 編集部・ホリデーギフト企画</div>
      <p>
        11月後半から12月にかけて本格化する、クリスマスプレゼントや忘年会・送別会、お世話になった方への年末お礼のギフト選び。実は限定品のクリスマスコフレは11月中旬には予約終了や完売になってしまうことも多く、またメイク用品は相手の肌色や好みが合わないリスクもあります。
      </p>
      <p>
        そこで失敗しない最適解として選ばれているのが、<strong>人気ブランド定番の「高保湿ハンドケア・ボディケア・入浴剤ギフトセット」</strong>です。冬は誰の手肌やボディも乾燥しやすく、毎日消耗する実用品だからこそ相手の負担にならず素直に喜んでもらえます。本記事ではラッピング・専用BOXなどギフト仕様のまま贈れる名品10セットを、予算別・相手別にご紹介します。
      </p>
    </section>

    <section class="budget-grid" aria-label="予算別クイックガイド">
      <div class="budget-box">
        <span>予算 3,000円〜4,000円台</span>
        <strong>ロクシタン / ポール＆ジョー / アユーラ</strong>
        <p>職場のお礼や友人同士のクリスマス交換に最適。名入れハンカチや入浴剤など気が利いた選択肢が揃います。</p>
      </div>
      <div class="budget-box">
        <span>予算 5,000円〜6,000円台</span>
        <strong>ジルスチュアート / ジョンマスター / ニールズヤード</strong>
        <p>純正ギフトBOX入りの見た目の華やかさと実用性のバランスが抜群。女友達や家族への本命プレゼントに。</p>
      </div>
      <div class="budget-box">
        <span>予算 7,000円〜8,000円台</span>
        <strong>イソップ / SABON / ディオール / SHIRO</strong>
        <p>大切なパートナーや目上の方にも胸を張って渡せるラグジュアリー定番。手提げ袋や純正包装が魅力です。</p>
      </div>
    </section>

    <nav class="gf-toc" aria-label="目次">
      <h2>この記事でわかること</h2>
      <ul>
        <li><a href="#why-moist-gift">1. 11月・12月のプレゼントに「高保湿ケアギフト」が鉄板な理由</a></li>
        <li><a href="#gift-tips">2. 外さないブランド＆香りの選び方 3つのポイント</a></li>
        <li><a href="#gift-table">3. 人気ブランド高保湿ギフトセット10選 比較一覧表</a></li>
        <li><a href="#gift-ranking">4. 冬に喜ばれる高保湿コスメギフトセット厳選10選</a></li>
        <li><a href="#order-check">5. 12月配送で失敗しない楽天ギフト注文4チェック</a></li>
        <li><a href="#gf-faq">6. 冬ギフト選びのよくある疑問 Q&amp;A</a></li>
      </ul>
    </nav>

    <section class="gf-section" id="why-moist-gift">
      <h2>1. なぜ冬ギフトは「メイク品」より「高保湿パーツケアセット」が外さないのか</h2>
      <p>
        せっかく贈るなら相手が確実に毎日使ってくれるものを渡したいもの。しかしファンデーションやリップカラー、アイシャドウといったポイントメイクは、本人のパーソナルカラー（イエベ・ブルベ）や好みの質感に大きく左右されます。また、12月限定のコフレは人気集中で入手難になったり価格が跳ね上がったりすることもあります。
      </p>
      <p>
        その点、<strong>ハンドクリーム・リップバーム・ボディスクラブ・バスエッセンス・ヘアケアの定番ギフトセット</strong>は、11月・12月の乾燥シーズンに老若男女問わず必要とされるアイテムです。さらにブランド側がすでに美しい箱やラッピング仕様で展開している定番ギフトを選べば、見栄えの良さと確実な保湿力を両立できます。
      </p>
    </section>

    <section class="gf-section" id="gift-tips">
      <h2>2. 贈る相手に本当に喜ばれるギフトセット選び 3つの基準</h2>
      <div class="gf-3reasons">
        <div class="gf-reason">
          <h3>① 相手の「香りの許容範囲」をイメージする</h3>
          <p>甘いフローラルが好きならジルスチュアートやディオール、石けんや柑橘の清潔感ならSHIROやロクシタン、甘さを抑えたユニセックスな香りならイソップやアユーラが鉄板です。</p>
        </div>
        <div class="gf-reason">
          <h3>② すぐに手渡しできる「BOX・手提げ袋」の有無</h3>
          <p>職場やレストランで直接手渡す予定なら、商品本体が純正ボックスやラッピング包装に入っているか、ショッパー（手提げ袋）が付属しているかを事前に確認すると当日スマートです。</p>
        </div>
        <div class="gf-reason">
          <h3>③ 保湿成分の「普段使いしやすさ（ベタつきにくさ）」</h3>
          <p>シアバターや植物オイルによる高い保湿力を持ちながら、PC作業やスマホ操作の邪魔になりにくい肌馴染みの良さ（ロクシタン、イソップ、SHIRO等）は日常愛用率に直結します。</p>
        </div>
      </div>
    </section>

    <section class="gf-section" id="gift-table">
      <h2>3. 人気ブランド高保湿ギフトセット10選 比較表</h2>
      <p>セット内容・ラッピング対応・香りの方向性・楽天市場での最新価格（税込）をまとめました。</p>
      <div class="gf-tbl-wrap">
        <table class="gf-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド / ギフト名</th>
              <th>主なセット内容</th>
              <th>香りの傾向</th>
              <th>包装・袋仕様</th>
              <th>参考価格</th>
            </tr>
          </thead>
          <tbody>
{table_rows}          </tbody>
        </table>
      </div>
    </section>

    <h2 class="gf-sec-title" id="gift-ranking">4. 11月・12月に贈りたい高保湿コスメギフトセット10選</h2>
    <section aria-label="ギフトセット詳細ランキング">
{cards_html}    </section>

    <section class="gf-section" id="order-check">
      <h2>5. 12月のギフト配送で後悔しないための4つの確認事項</h2>
      <div class="gf-checklist">
        <div class="gf-check-item">
          <h3>Check 1：箱あり・ラッピング対応か</h3>
          <p>同じブランド名でも自宅用の「箱なし・簡易包装」が出品されていることがあります。商品名に「ギフトBOX」「ラッピング済」の記載があるか必ず確認しましょう。</p>
        </div>
        <div class="gf-check-item">
          <h3>Check 2：手提げ袋（ショッパー）の同梱</h3>
          <p>ネット注文で自宅へ届けてから手渡しする場合、ブランドの紙袋が付いているとそのままスマートに持ち運べます（付かない場合はギフト用バッグを別途用意すると安心）。</p>
        </div>
        <div class="gf-check-item">
          <h3>Check 3：名入れ・メッセージは納期に余裕を</h3>
          <p>ポール＆ジョーの名入れハンカチなどカスタム品は制作に数日かかります。12月20日〜25日に渡す予定なら、遅くとも12月上旬〜中旬前半の注文が安全です。</p>
        </div>
        <div class="gf-check-item">
          <h3>Check 4：相手宅へ直送する際の納品書設定</h3>
          <p>相手の自宅へ直接配送する際は、金額が記載された領収書や納品書が入らない「ギフト配送設定」を買い物かご内でチェックしておくのを忘れずに。</p>
        </div>
      </div>
    </section>

    <section class="gf-section" id="gf-faq">
      <h2>6. 冬の高保湿ギフトセットに関するFAQ</h2>
      <div class="faq-block">
        <h3>Q1. 限定クリスマスコフレと定番の保湿ギフトセット、どちらを選ぶべきですか？</h3>
        <p>メイクの色味を楽しみたい方へはコフレも素敵ですが、11月下旬〜12月は完売品が増え、色選びのハードルも上がります。ロクシタン、イソップ、SHIRO、SABON、ディオールなどの定番高保湿ギフトは在庫が安定しており、相手のパーソナルカラーに関わらず毎日使ってもらえる堅実さがあります。</p>
      </div>
      <div class="faq-block">
        <h3>Q2. 予算3,000円〜5,000円で安っぽく見えないものはありますか？</h3>
        <p>3,000円〜4,000円台なら『ロクシタンのハンドクリームギフト』『ポール＆ジョーの名入れハンカチセット』『アユーラのバスエッセンスギフト』、5,000円台なら純正BOX付きの『ジルスチュアート』や『ジョンマスターオーガニック』が価格以上の華やかさがあります。</p>
      </div>
      <div class="faq-block">
        <h3>Q3. 男性や目上の方へのプレゼントにも使えるブランドは？</h3>
        <p>ジェンダーレスに支持される『イソップ（アンドラム）』や、シンプルで清潔感ある『SHIRO（サボン／ホワイトティー）』、安らぐ森林系の香りの『アユーラ（メディテーションバス）』は男性や上司の方への贈り物としても非常に人気です。</p>
      </div>
      <div class="faq-block">
        <h3>Q4. 12月に注文する場合、いつ頃までに手配するのがベストですか？</h3>
        <p>ブラックフライデーや12月のスーパーSALE時期はギフト需要と物流が混み合います。特にクリスマス直前は配送遅延も起きやすいため、渡す日の1週間〜10日前までに手元に届くよう注文しておくのが安心です。</p>
      </div>
    </section>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬のギフト・パーツ保湿特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <a href="/winter-holiday-coffret" class="internal-link-card">
          <div style="font-weight:700;color:#14532d;margin-bottom:0.25rem;">限定クリスマスコフレ＆ホリデー10選</div>
          <div style="font-size:0.8rem;color:#57534e;">自分へのご褒美に華やかな限定コフレを比較</div>
        </a>
        <a href="/winter-hand-care" class="internal-link-card">
          <div style="font-weight:700;color:#14532d;margin-bottom:0.25rem;">冬の手荒れ防止ハンドケア総合10選</div>
          <div style="font-size:0.8rem;color:#57534e;">あかぎれ・ささくれを防ぐ本格ハンドクリーム</div>
        </a>
        <a href="/winter-mens-skincare" class="internal-link-card">
          <div style="font-weight:700;color:#14532d;margin-bottom:0.25rem;">メンズ高保湿スキンケア人気10選</div>
          <div style="font-size:0.8rem;color:#57534e;">男性への12月クリスマスギフトにも人気</div>
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

with open("winter-gift-set.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

print("Generated winter-gift-set.html successfully!")
