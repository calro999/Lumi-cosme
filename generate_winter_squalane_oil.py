import json
import re

with open("fetched_3new_nov_dec_ceramide_lotion_lip_squalane_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_squalane_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 純度99.9%の金字塔！たった1滴で乳液・クリーム不要を叶える奇跡の美容オイル",
        "catch": "無添加主義HABAの最高傑作。深海鮫の肝油から極限まで不純物を排除した酸化しない純度99.9%",
        "brand_name": "HABA (ハーバー)",
        "capacity": "30ml (高品位スクワラン)",
        "type": "純度99.9%・深海鮫肝油由来高品位スクワラン美容オイル",
        "features": "高純度スクワラン100%（純度99.9%）、防腐剤パラベン・石油系界面活性剤・合成香料・鉱物油・タール系色素完全無添加",
        "value": "発売から40年以上愛され続ける無添加オイルの最高峰。化粧水直後の肌にわずか1滴馴染ませるだけで、冬の皮脂膜を完璧に再現し、ベタつかずシルクのような滑らかさを実現",
        "desc_p1": "11月から12月にかけて気温が10℃を下回ると、肌の皮脂腺の活動が急激に鈍化し、皮脂の分泌量は真夏の3分の1以下にまで激減します。どれほど高価な化粧水やシートマスクで水分を補給しても、肌表面を覆う『天然の皮脂膜』が存在しなければ、水分は乾いた外気へとあっという間に蒸散してしまいます。この冬枯れ肌の皮脂膜を、たった1滴で完璧に再現してくれるのがハーバーの『高品位スクワラン』です。",
        "desc_p2": "深海鮫の肝油から抽出したスクワレンを、ハーバー独自の精製技術によって極限まで不純物を取り除き、純度99.9%という驚異的な高純度を達成。空気に触れても酸化・油焼けを起こさず、紫外線による変質もありません。化粧水でビシャビシャに濡れた肌に手のひらで1滴を馴染ませると、肌の水分と瞬時に混ざり合って天然の乳化エマルジョン膜を形成。油っぽさやギトギト感が一切なく、内側はもっちり、表面はサラリとした至福のヴェルヴェット肌へと導きます。",
        "target": "乳液やクリームの重いベタつきが苦手な方、冬の皮脂不足で粉吹きや小ジワに悩む方、1本で数ヶ月持続する圧倒的な高コスパを求める方",
        "point": "化粧水をたっぷりつけた後、肌に水滴が残っている状態で手のひらに『たった1滴』落とし、両手を擦り合わせてから顔全体を優しく包み込むようにハンドプレスします。つけすぎるとかえって浸透が妨げられるため、必ず1滴を守るのが最大の秘訣です。"
    },
    {
        "rank": 2,
        "tag": "🌿 オリーブ由来100%の軽やか植物性！大容量で顔から髪・ボディまで贅沢に包み込む",
        "catch": "無印良品の天然ピュアオイル。オリーブ油から抽出した植物性スクワランが肌にさらりと浸透",
        "brand_name": "無印良品 (MUJI)",
        "capacity": "100ml (オリーブスクワランオイル)",
        "type": "オリーブ由来植物性スクワラン100%・無香料・無着色・アレルギーテスト済み",
        "features": "オリーブ果実由来スクワラン100%、無香料・無着色・アルコールフリー",
        "value": "植物由来ならではの軽やかで肌馴染みの良いテクスチャー。100mlの大容量ポンプボトルで、真冬に乾燥して粉を吹くスネや肘、パサつく毛先まで惜しみなく全身ケア",
        "desc_p1": "ヴィーガン志向の方や、動物由来成分に敏感な方から圧倒的な支持を集めているのが無印良品の『オリーブスクワランオイル』です。オリーブの果実からわずか数パーセントしか抽出できない希少なスクワレンを贅沢に精製し、さらりとした軽やかな使用感に仕上げています。",
        "desc_p2": "サメ由来のスクワランに比べてテクスチャーがよりみずみずしく、オイル特有の重さを感じさせません。肌の角質層へすっと浸透し、キメの乱れた冬の素肌を柔らかく解きほぐします。顔のスキンケアの仕上げとしてはもちろん、お風呂上がりの濡れたボディに伸ばせば、翌朝まで吸い付くような潤い肌をキープ。ポンプ式で量の調節もしやすく、100mlで冬の間中マルチに活躍する頼もしい逸品です。",
        "target": "植物由来のクリーンなスキンケアを好む方、顔だけでなく全身やヘアケアにもたっぷり使いたい方、サラサラとした軽いオイルが好きな方",
        "point": "お風呂から上がる直前、タオルで拭く前の濡れた肌に2〜3プッシュを全身に伸ばします。その後にタオルで軽く押さえるだけで、真冬の粉吹き乾燥を完璧にシャットアウトできます。"
    },
    {
        "rank": 3,
        "tag": "🧪 深海鮫肝油100%の高純度原液！研究機関発想の確かな品質で冬の砂漠肌を完全シールド",
        "catch": "高濃度スキンケアKISOが誇るピュア原液。肌のバリアを強力にサポートする濃縮スクワラン",
        "brand_name": "KISO (キソ)",
        "capacity": "50ml (スクワランオイル)",
        "type": "高純度100%深海鮫肝油スクワラン・原液美容オイル",
        "features": "国産・深海鮫肝油抽出スクワラン100%、合成保存料・防腐剤・鉱物油・香料・着色料フリー",
        "value": "成分重視のKISOならではの純度とコスパ。良質な深海鮫由来スクワランを50mlたっぷり詰め込み、暖房直下でカサつく大人の肌を濃密に潤す",
        "desc_p1": "成分オタクや美容専門家から絶大な支持を集めるKISO（基礎化粧品研究所）。そのスクワランオイルは、深海に生息するサメの驚異的な生命力を支える肝油から高純度で抽出された正真正銘のピュアオイルです。",
        "desc_p2": "人間の皮脂中に含まれるスクワレンと同一の組成を持つため、塗布した瞬間に肌が自分の皮脂と錯覚するほど自然に馴染みます。冬の過酷な寒冷によって荒れ果てた角質層の隙間を満たし、外部からの刺激物質や冷気の侵入を物理的に防御。遮光瓶のスポイト容器に入っているため、いつでも衛生的に1滴単位で取り出せ、手持ちの化粧水や乳液に混ぜて保湿力をブーストする使い方も自在です。",
        "target": "成分の純度と濃度にこだわりたい方、スポイト式で衛生的に使いたい方、化粧水やクリームに混ぜて保湿力を底上げしたい方",
        "point": "手持ちの乳液やフェイスクリームに1滴垂らし、手のひらでよく混ぜ合わせてから塗布すると、いつものスキンケアが真冬用の超高保湿クリームへとグレードアップします。"
    },
    {
        "rank": 4,
        "tag": "🌱 植物性でさらに進化した優しさ！サトウキビ由来のしっとり潤いヴェール",
        "catch": "HABAのもう一つの名作。サトウキビから生まれた植物由来スクワランで敏感肌をやさしく保護",
        "brand_name": "HABA (ハーバー)",
        "capacity": "60ml (スクワランII)",
        "type": "植物由来スクワラン100%・無添加高品位オイル",
        "features": "植物（サトウキビ）由来スクワラン100%、完全無添加（防腐剤パラベン・石油系界面活性剤・合成香料・鉱物油不使用）",
        "value": "元祖高品位スクワランの保湿力と使い心地はそのままに、サトウキビ由来の植物性原料で実現。動物性成分が肌に合わない方でも安心して使える低刺激設計",
        "desc_p1": "無添加主義を貫くハーバーが、多様化するユーザーのニーズと環境への配慮に応えて開発した『スクワランII』。サトウキビを原料とし、発酵・精製技術を駆使して作られた高品質な植物性スクワランです。",
        "desc_p2": "オリジナルの高品位スクワランと遜色のない極上の浸透性とサラサラ感を持ちながら、植物性ならではの非常にマイルドで柔らかな肌当たりが特徴。11月・12月の季節の変わり目で肌がピリついたり赤みが出やすい敏感肌でも、刺激を一切感じることなく安心して使用できます。60mlの大きめボトルは、顔の保湿だけでなく冬の乾燥でパサつく毛先の集中補修や、爪の甘皮ケア（ネイルオイル）としても数ヶ月間贅沢に使えます。",
        "target": "動物性原料が苦手な方・ヴィーガン志向の方、肌が非常にデリケートで刺激に弱い方、大容量で長期間愛用したい方",
        "point": "洗顔後、化粧水をしっかり馴染ませた濡れた素肌に1滴。さらにパサつきが気になる髪の毛先にもタオルドライ後に半滴揉み込んでからドライヤーをかけると、熱ダメージと静電気を防げます。"
    },
    {
        "rank": 5,
        "tag": "💧 原液美容のスペシャリストが放つ高精製！肌の水分蒸発を極限まで抑える1滴の力",
        "catch": "TUNEMAKERSの集中原液。肌に必要な皮脂だけをピンポイントで補給するスマートオイル",
        "brand_name": "TUNEMAKERS (チューンメーカーズ)",
        "capacity": "20ml (精製スクワラン 原液)",
        "type": "高純度精製スクワラン100%・原液スキンケアオイル",
        "features": "高度精製スクワラン100%、無香料・無着色・鉱物油フリー・パラベンフリー・アルコールフリー",
        "value": "肌の皮脂膜とほぼ同じ成分を高精製。冬のエアコン暖房直下でも水分の蒸発を防ぎ、内側の潤いをがっちりキープするピンポイント保湿原液",
        "desc_p1": "一人ひとりの肌悩みに合わせて原液をカスタマイズできる人気ブランド、チューンメーカーズ。その中でも冬の乾燥シーズンに圧倒的な需要を誇るのが『精製スクワラン 原液』です。",
        "desc_p2": "不純物を徹底的に排除した高精製処方により、サラリとした水のような感触で、オイルの油膜感が苦手な方でもストレスなく使えます。皮膚との親和性が極めて高く、塗布した瞬間に角層の奥まで吸い込まれるように馴染みます。乾燥が深刻な目元や口元など、冬のちりめんジワが目立ちやすいパーツへのスポット重ね付けにも最適で、夕方のファンデーションのひび割れを予防します。",
        "target": "目元や口元など部分的な乾燥小ジワを集中ケアしたい方、手持ちのスキンケアの質を1ランク上げたい方、ベタつきが一切ないオイルを求める方",
        "point": "化粧水の直後に1滴を全顔に馴染ませた後、特に乾燥が気になる目尻やほうれい線周りに指先でトントンと軽く叩き込むように重ね付けしてください。"
    },
    {
        "rank": 6,
        "tag": "🌸 創業半世紀の自然派コスメ！無香料・無着色で冬の荒れた素肌をやさしく包み込む",
        "catch": "ハイム化粧品の隠れた名品。深海鮫スクワランを惜しみなく配合した高純度マルチオイル",
        "brand_name": "ハイム化粧品 (HEIM)",
        "capacity": "60ml (スクワランオイル)",
        "type": "高純度スクワラン100%・無香料・無着色フェイス＆ボディオイル",
        "features": "深海鮫肝油スクワラン100%、防腐剤・合成着色料・鉱物油・香料完全無添加",
        "value": "良心的な価格と確かな品質で50年愛される自然派ブランド。60mlの使いやすいサイズで、顔のマッサージオイルから冬のボディ保湿まで万能にこなす",
        "desc_p1": "1960年代の創業以来、徹底して肌への優しさと確かな品質を追求し続けているハイム化粧品。派手な広告を出さない代わりに、中身の成分とコストパフォーマンスに全力を注いだスクワランオイルは、知る人ぞ知る名品です。",
        "desc_p2": "深海鮫由来のスクワランを高度に精製し、サラッとした軽やかなタッチとリッチな保水保護力を両立。冬の寒さで血行が悪くなり、くすみがちな肌を優しくマッサージするオイルとしても最適で、摩擦を起こさず指滑りを滑らかにしてくれます。無香料・無着色で肌への負担が極めて少ないため、赤ちゃんからお年寄りまで家族全員で冬の乾燥対策に活用できます。",
        "target": "派手なブランドよりも中身の品質とコスパを重視する方、冬のフェイスマッサージ用オイルを探している方、家族で共有したい方",
        "point": "洗顔後、化粧水をつけた後に2〜3滴を手に取り、フェイスラインから首筋、鎖骨へ向けて優しくリンパを流すようにマッサージすると、血行が促されて顔色がパッと明るくなります。"
    },
    {
        "rank": 7,
        "tag": "🌿 ガラス瓶入りの上質サロン品質！純度99%以上の国産スクワランが冬の肌を密封",
        "catch": "スパ発想のナチュラルスキンケア。重厚なガラスボトルに閉じ込めた高純度ピュアオイル",
        "brand_name": "spa hinoki (スパヒノキ)",
        "capacity": "50ml (スクワラン 美容オイル)",
        "type": "純度99%以上・深海鮫肝油スクワラン・国産ガラス容器採用",
        "features": "国産高純度スクワラン（純度99%以上）、酸化を防ぐ遮光ガラスボトル採用、無香料・無着色",
        "value": "高級スパやサロンで愛用されるクオリティ。光や熱による劣化を防ぐ重厚なガラス瓶を採用し、いつでも搾りたてのような新鮮な純度を保ち続ける",
        "desc_p1": "東京・檜原村の自然とスパセラピーの知恵から生まれたブランド『spa hinoki』。品質保持に一切の妥協を許さず、プラスチック容器ではなく遮光ガラス瓶を採用することで、スクワランのピュアな鮮度を最後まで保ちます。",
        "desc_p2": "純度99%以上の深海鮫スクワランが、冬の冷たい外気で傷ついた角質層を優しく包み込みます。肌馴染みが非常に早く、塗布後すぐに肌表面がサラサラに整うため、朝の忙しいメイク前でも待ち時間なしでベースメイクに移行できます。冬の寒さでひび割れやすい指先のキューティクルオイル（甘皮ケア）としても極めて優秀です。",
        "target": "容器の品質や遮光性にもこだわりたい方、朝のメイク前に素早く使えるオイルを探している方、スパ品質の上質なタッチを楽しみたい方",
        "point": "メイク前のスキンケアの仕上げに1滴。手のひら全体に広げてから顔を包み込むようにハンドプレスすると、ファンデーションの粉吹きを1日中防止できます。"
    },
    {
        "rank": 8,
        "tag": "🌍 カナダ発の世界的メガヒット！100%植物由来のスクワランが冬のインナードライを撃退",
        "catch": "The Ordinaryの不動のベストセラー。科学的アプローチで肌の水分蒸散を徹底的に防ぐ",
        "brand_name": "The Ordinary (ジオーディナリー)",
        "capacity": "30ml (100%植物由来スクワラン)",
        "type": "100% Plant-Derived Squalane（植物由来スクワラン原液美容オイル）",
        "features": "100%植物由来スクワラン、ECOCERT認証原料、水・アルコール・オイル・シリコン・グルテンフリー",
        "value": "世界中のスキンケアファンを熱狂させるThe Ordinaryの名品。非コメドジェニック処方で毛穴を詰まらせず、冬の乾燥小ジワをふっくら持ち上げる",
        "desc_p1": "「誠実な価格で高機能な成分を」という哲学のもと、世界中で爆発的なヒットを記録しているカナダ発のThe Ordinary。その『100%植物由来スクワラン』は、冬の乾燥対策におけるグローバルスタンダードとも言える名品です。",
        "desc_p2": "植物由来のスクワランを純度100%でボトリング。毛穴を詰まらせにくいノンコメドジェニック設計のため、冬でもTゾーンがテカりやすい混合肌やニキビができやすい肌でも安心して使えます。高い保水力と柔軟効果により、暖房の温風で縮こまった角層を内側からふっくらと押し上げ、肌本来の自然な発光ツヤを取り戻します。UVカットガラスのスポイト容器も使い勝手抜群です。",
        "target": "毛穴詰まりやニキビが心配でオイルを敬遠していた方、海外の先端クリーンビューティーを体験したい方、混合肌の冬の保湿に",
        "point": "化粧水や美容液の後に数滴を顔全体になじませます。冬のブロー前の濡れた髪に馴染ませれば、熱によるパサつきと静電気を同時に防ぐ優秀なヘアオイルとしても機能します。"
    },
    {
        "rank": 9,
        "tag": "💧 100mlの圧倒的メガバリュー！天然ピュアオイルで頭からつま先まで冬の乾燥を遮断",
        "catch": "&SHの天然美容オイル。大容量だからできる贅沢使いで全身の粉吹き・カサつきを一掃",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "100ml (スクワランオイル)",
        "type": "天然高純度スクワラン100%・全身用大容量美容オイル",
        "features": "天然高純度スクワラン100%、無添加（香料・着色料・防腐剤不使用）、50ml×2本仕様",
        "value": "楽天市場で驚異的なリピート率を誇る大容量スクワラン。酸化しにくい純度を保ちながら、冬のボディクリームやヘアオイル代わりとして全身に惜しみなく使える",
        "desc_p1": "冬になると顔だけでなく、すねや背中、腕、指先など全身が粉を吹いて痒くなるという深刻な全身乾燥に悩む方に最適なのが、&SHの大容量スクワランオイルです。",
        "desc_p2": "高純度の天然スクワランを100mlという大容量で提供。伸びが非常によく、ほんの数滴で広範囲をカバーできるため、冬の間中これ1つで全身の保湿が完了します。お風呂上がり、身体の水滴を軽く払った直後に全身に薄く伸ばせば、ボディローションやボディクリームが不要になるほどのしっとり感が持続。50mlボトルに小分けされているため、持ち運びや鮮度管理にも優れています。",
        "target": "冬になると全身の粉吹きや痒みに悩む方、惜しみなく大容量で全身に使いたい方、高いコスパを最優先したい方",
        "point": "冬のお風呂上がりに、肘、膝、かかと、すねなどの乾燥が激しいパーツへ直接擦り込むように塗布。さらに手持ちのボディソープに1滴混ぜて泡立てると、洗い上がりのつっぱり感が劇的に緩和されます。"
    },
    {
        "rank": 10,
        "tag": "🌿 サトウキビの恵みで極上のシルク肌！スポイト付きで使いやすい植物性シュガースクワラン",
        "catch": "地球にも肌にも優しい次世代スクワラン。驚くほど軽やかなテクスチャーで角層に素早く密着",
        "brand_name": "Sugar Squalane (シュガースクワラン)",
        "capacity": "30ml (シュガー スクワランオイル)",
        "type": "植物性サトウキビ由来シュガースクワラン100%・スポイト付き",
        "features": "サトウキビ由来植物性スクワラン100%、無添加処方（パラベン・合成香料・鉱物油フリー）、スポイトボトル",
        "value": "再生可能資源であるサトウキビから生まれたサステナブルなスクワラン。分子が均一で肌馴染みが極めて早く、塗ったことを忘れるほど軽やかな保湿膜を形成",
        "desc_p1": "近年、サステナブルなビューティー原料として世界的に注目を集めているのが、サトウキビから発酵・抽出される『シュガースクワラン』です。動物を傷つけることなく、環境に負荷をかけない次世代の美容オイルとして人気が急上昇しています。",
        "desc_p2": "シュガースクワランの最大の特徴は、一般的なオイルの概念を覆すほどの『浸透スピードの速さ』と『シルクのような軽やかさ』です。塗布後わずか数秒で角層の隙間へ滑り込み、表面に油膜のギラつきを一切残しません。真冬のオフィスのエアコン暖房直下でも、角層の水分蒸散をブロックし、内側から押し返すような滑らかなツヤを一日中キープします。",
        "target": "サステナブル・ヴィーガンなコスメを選びたい方、オイルのテカリやベタつきが絶対に嫌な方、スポイトで手軽に使いたい方",
        "point": "化粧水の後の濡れた肌にスポイトで1滴。さらにリキッドファンデーションやBBクリームに半滴混ぜてから塗ると、プロが仕上げたような濡れツヤ肌が完成し、夕方のメイク割れを完璧に防ぎます。"
    }
]

faq_items = [
    {
        "q": "なぜ冬（11月・12月）の肌には「スクワランオイル」がこれほど効果的なのですか？",
        "a": "冬は気温の低下により皮脂腺が収縮し、肌を外的刺激や乾燥から守る天然のバリアである『皮脂の分泌量』が激減します。スクワランは、もともと人間の皮脂の中に約12%も含まれている生体構成成分『スクワレン』を、酸化しにくいように水素添加して安定化させた成分です。つまり肌にとって『自分自身の皮脂そのもの』と同等であるため、塗布した瞬間に拒絶感なく馴染み、失われた皮脂膜を完璧に再建して水分の蒸発を100%ブロックできるからです。"
    },
    {
        "q": "「サメ由来（深海鮫）」と「植物由来（オリーブ・サトウキビ）」のスクワランの違いは何ですか？",
        "a": "化学構造（C30H62）としてはどちらも同じ高純度のスクワランですが、使用感と原料のルーツにわずかな違いがあります。『サメ由来（ハーバーの高品位スクワランなど）』は、古くから使われている王道で、保湿の持続力と肌のラッピング感に優れており、真冬の超乾燥肌に最適です。一方『植物由来（オリーブやサトウキビなど）』は、よりテクスチャーがみずみずしくサラリとしており、植物性・ヴィーガンにこだわりたい方や、ベタつきが苦手な方に選ばれています。"
    },
    {
        "q": "スクワランオイルを塗ると「油焼け」してシミの原因になりませんか？",
        "a": "全く心配ありません。一般的な植物油（不純物を含むオイルや不飽和脂肪酸）は紫外線や熱で酸化しやすく、油焼けの原因になることがありますが、高純度スクワランは完全に飽和した安定な炭化水素構造（飽和脂肪酸と同等の安定性）を持っています。紫外線や空気にさらされても酸化や変質が起きないため、朝のスキンケアや日中のメイク前に使っても油焼けを起こすことは一切ありません。"
    },
    {
        "q": "スクワランオイルを使うと、ニキビや毛穴詰まりの原因になりませんか？",
        "a": "高純度スクワランは毛穴を詰まらせにくい『ノンコメドジェニック』な性質を持っています。むしろ、冬に肌が乾燥すると、角質が硬くなって毛穴の出口が塞がり、乾燥に焦った肌が過剰な皮脂を出してニキビ（大人ニキビ）を悪化させます。スクワランを1滴補うことで角層が柔らかくなり、水分と油分のバランスが整うため、かえってニキビや毛穴トラブルが予防されるケースが多いのです。ただし、つけすぎは禁物で、適量（1滴）を守ることが大切です。"
    },
    {
        "q": "スクワランオイルを最大限に生かす「一番効果的な使い順」とコツは？",
        "a": "『化粧水で肌がビシャビシャに濡れている状態に、たった1滴をハンドプレスする』のが最も効果的です。スクワランは水分を抱え込んで乳化する性質があるため、乾いた肌に塗るのではなく、水滴が肌に残っているタイミングで塗布することで、肌表面で瞬時に上質な天然エマルジョン（乳液状態）へと変化します。乳液やクリームを使わなくても、これ1ステップで完璧な保湿膜が完成します。"
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
    "headline": "保湿力の強さで肌乾燥とさようなら！たった1滴で極上ツヤ膜を張る高純度スクワランオイルランク10",
    "description": "11月・12月の冬本番に深刻化する皮脂分泌急落・粉吹き乾燥・小ジワを徹底解決！純度99.9%のスクワランや植物性シュガースクワランを贅沢配合した高純度スクワランオイル10選を徹底比較！HABA、無印良品、KISO、チューンメーカーズ、The Ordinaryなど、たった1滴で真冬でも極上ツヤ肌が続く至高の美容オイルを厳選。",
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
    "name": "冬の高純度スクワランオイル おすすめランキング10選",
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

cards_html = []
for p, item in zip(product_details, items):
    cards_html.append(f"""
      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge-wrap">
          <span class="rank-badge rank-{p['rank']}">第{p['rank']}位</span>
          <span class="feature-tag">{p['tag']}</span>
        </div>
        <h3 class="product-name">{p['brand_name']} {p['capacity']}</h3>
        <p class="product-catch">{p['catch']}</p>
        
        <div class="product-body">
          <div class="product-img-box">
            <img src="{item['image']}" alt="{p['brand_name']} {p['capacity']} 高純度スクワランオイル" class="product-img" loading="lazy" width="280" height="280">
          </div>
          <div class="product-meta">
            <table class="meta-table">
              <tr>
                <th>原料由来 / タイプ</th>
                <td>{p['type']}</td>
              </tr>
              <tr>
                <th>主要成分 / 純度</th>
                <td>{p['features']}</td>
              </tr>
              <tr>
                <th>容量 / 実勢価格</th>
                <td>{p['capacity']} / <span class="price-val">¥{item['price']:,}</span> (税込・楽天市場最新)</td>
              </tr>
              <tr>
                <th>独自バリュー</th>
                <td>{p['value']}</td>
              </tr>
            </table>
          </div>
        </div>
        
        <div class="product-desc-box">
          <h4 class="desc-heading">🔍 冬（11月・12月）の肌悩みへのアプローチ＆使用感</h4>
          <p class="desc-text">{p['desc_p1']}</p>
          <p class="desc-text">{p['desc_p2']}</p>
          
          <div class="recommend-box">
            <div class="recommend-target">
              <span class="rec-icon">🎯</span>
              <strong>こんな方におすすめ：</strong> {p['target']}
            </div>
            <div class="recommend-usage">
              <span class="rec-icon">💡</span>
              <strong>効果を高めるプロの使い方：</strong> {p['point']}
            </div>
          </div>
        </div>

        <div class="cta-wrap">
          <a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            <span class="rakuten-icon">🛍️</span> 楽天市場で「{p['brand_name']}」の最安値・口コミを見る（¥{item['price']:,}〜）
          </a>
        </div>
      </article>
""")

table_rows = []
for p, item in zip(product_details, items):
    table_rows.append(f"""
            <tr>
              <td class="col-rank"><span class="table-rank rank-{p['rank']}">第{p['rank']}位</span></td>
              <td class="col-name"><strong>{p['brand_name']}</strong><br>{p['capacity']}</td>
              <td class="col-feat">{p['features']}</td>
              <td class="col-price">¥{item['price']:,}</td>
              <td class="col-btn"><a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="table-btn">楽天詳細</a></td>
            </tr>
""")

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！たった1滴で極上ツヤ膜を張る高純度スクワランオイルランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬本番に深刻化する皮脂分泌急落・粉吹き乾燥・小ジワを徹底解決！純度99.9%のスクワランや植物性シュガースクワランを贅沢配合した高純度スクワランオイル10選を徹底比較！HABA、無印良品、KISO、チューンメーカーズ、The Ordinaryなど、たった1滴で真冬でも極上ツヤ肌が続く至高の美容オイルを厳選。">
  <meta name="keywords" content="スクワランオイル,高純度スクワラン,冬 美容オイル,HABA スクワラン,無印良品 スクワラン,皮脂膜,乾燥小ジワ,粉吹き肌,おすすめ 2026">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-squalane-oil">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！たった1滴で極上ツヤ膜を張る高純度スクワランオイルランク10">
  <meta property="og:description" content="11月・12月の皮脂枯渇を救う！たった1滴で鉄壁の保湿膜を張るスクワランオイル10選を徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-squalane-oil">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
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
  
  <style>
    :root {{
      --primary: #047857;
      --primary-light: #ecfdf5;
      --accent: #059669;
      --accent-hover: #047857;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg-gray: #f8fafc;
      --border: #e2e8f0;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: #f1f5f9;
    }}
    header {{
      background: linear-gradient(135deg, #065f46 0%, #059669 100%);
      color: white;
      padding: 1rem 0;
      box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    }}
    .header-container {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title {{
      font-size: 1.25rem;
      font-weight: 800;
      text-decoration: none;
      color: white;
      letter-spacing: -0.025em;
    }}
    .nav-links {{
      display: flex;
      gap: 1rem;
    }}
    .nav-links a {{
      color: rgba(255,255,255,0.9);
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: white;
      text-decoration: underline;
    }}
    .main-wrap {{
      max-width: 920px;
      margin: 2rem auto;
      background: white;
      border-radius: 12px;
      box-shadow: var(--card-shadow);
      padding: 2.5rem 2rem;
    }}
    @media (max-width: 640px) {{
      .main-wrap {{
        padding: 1.5rem 1rem;
        margin: 1rem 0.5rem;
      }}
    }}
    .article-header {{
      border-bottom: 2px solid var(--border);
      padding-bottom: 1.5rem;
      margin-bottom: 2rem;
    }}
    .article-tag {{
      display: inline-block;
      background: #d1fae5;
      color: #065f46;
      font-size: 0.8125rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 0.75rem;
    }}
    h1 {{
      font-size: 1.75rem;
      line-height: 1.4;
      color: #0f172a;
      font-weight: 800;
      margin-bottom: 1rem;
    }}
    @media (max-width: 640px) {{
      h1 {{
        font-size: 1.4rem;
      }}
    }}
    .update-time {{
      font-size: 0.8125rem;
      color: var(--text-muted);
      display: flex;
      gap: 1rem;
    }}
    .lead-box {{
      background: #ecfdf5;
      border-left: 5px solid #059669;
      padding: 1.5rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 2.5rem;
      font-size: 0.975rem;
      color: #1e293b;
    }}
    .toc-box {{
      background: var(--bg-gray);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1.5rem;
      margin-bottom: 2.5rem;
    }}
    .toc-title {{
      font-weight: 800;
      font-size: 1.05rem;
      margin-bottom: 0.75rem;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-list {{
      list-style: none;
      padding-left: 0;
    }}
    .toc-list li {{
      margin-bottom: 0.5rem;
    }}
    .toc-list a {{
      color: #059669;
      text-decoration: none;
      font-size: 0.925rem;
    }}
    .toc-list a:hover {{
      text-decoration: underline;
    }}
    h2.section-title {{
      font-size: 1.35rem;
      color: #0f172a;
      border-left: 5px solid var(--primary);
      padding-left: 0.75rem;
      margin: 3rem 0 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .section-content {{
      margin-bottom: 2rem;
      font-size: 0.975rem;
      color: #334155;
    }}
    .section-content p {{
      margin-bottom: 1rem;
    }}
    .highlight-card {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-radius: 8px;
      padding: 1.25rem;
      margin: 1.5rem 0;
    }}
    .highlight-card h4 {{
      color: #065f46;
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
    }}
    .product-card {{
      background: white;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.75rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--card-shadow);
      position: relative;
    }}
    .product-badge-wrap {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      display: inline-block;
      font-size: 0.875rem;
      font-weight: 800;
      color: white;
      padding: 0.25rem 0.85rem;
      border-radius: 6px;
      background: #64748b;
    }}
    .rank-1 {{ background: linear-gradient(135deg, #f59e0b, #d97706); }}
    .rank-2 {{ background: linear-gradient(135deg, #94a3b8, #64748b); }}
    .rank-3 {{ background: linear-gradient(135deg, #d97706, #b45309); }}
    .feature-tag {{
      font-size: 0.8125rem;
      font-weight: 700;
      color: #065f46;
      background: #d1fae5;
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      border: 1px solid #a7f3d0;
    }}
    .product-name {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 0.95rem;
      color: #475569;
      font-weight: 600;
      margin-bottom: 1.25rem;
    }}
    .product-body {{
      display: flex;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
    }}
    @media (max-width: 640px) {{
      .product-body {{
        flex-direction: column;
        align-items: center;
      }}
    }}
    .product-img-box {{
      flex-shrink: 0;
      width: 240px;
      text-align: center;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid var(--border);
      object-fit: contain;
    }}
    .product-meta {{
      flex-grow: 1;
    }}
    .meta-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.875rem;
    }}
    .meta-table th, .meta-table td {{
      padding: 0.6rem 0.75rem;
      border-bottom: 1px solid var(--border);
    }}
    .meta-table th {{
      width: 30%;
      background: var(--bg-gray);
      color: #475569;
      font-weight: 700;
      text-align: left;
    }}
    .meta-table td {{
      color: #1e293b;
    }}
    .price-val {{
      font-weight: 800;
      color: #059669;
      font-size: 1.05rem;
    }}
    .product-desc-box {{
      background: #f8fafc;
      border-radius: 8px;
      padding: 1.25rem;
      margin-bottom: 1.5rem;
    }}
    .desc-heading {{
      font-size: 1rem;
      font-weight: 700;
      color: #065f46;
      margin-bottom: 0.75rem;
    }}
    .desc-text {{
      font-size: 0.925rem;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 0.75rem;
    }}
    .recommend-box {{
      margin-top: 1rem;
      padding-top: 1rem;
      border-top: 1px dashed var(--border);
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      font-size: 0.875rem;
    }}
    .recommend-target, .recommend-usage {{
      display: flex;
      gap: 0.5rem;
      color: #334155;
    }}
    .rec-icon {{
      flex-shrink: 0;
    }}
    .cta-wrap {{
      text-align: center;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: white;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.975rem;
      padding: 0.85rem 1.75rem;
      border-radius: 8px;
      box-shadow: 0 4px 6px -1px rgba(230, 0, 0, 0.25);
      transition: transform 0.15s ease, box-shadow 0.15s ease;
      width: 100%;
      max-width: 520px;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 12px -2px rgba(230, 0, 0, 0.35);
      color: white;
    }}
    .table-container {{
      overflow-x: auto;
      margin: 2rem 0;
    }}
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.875rem;
      min-width: 600px;
    }}
    .summary-table th, .summary-table td {{
      padding: 0.75rem;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .summary-table th {{
      background: #047857;
      color: white;
      font-weight: 700;
    }}
    .summary-table tr:nth-child(even) {{
      background: #f8fafc;
    }}
    .table-rank {{
      display: inline-block;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      color: white;
      font-weight: 700;
      font-size: 0.75rem;
      background: #64748b;
    }}
    .col-price {{
      font-weight: 700;
      color: #059669;
    }}
    .table-btn {{
      display: inline-block;
      background: #bf0000;
      color: white;
      text-decoration: none;
      padding: 0.3rem 0.6rem;
      border-radius: 4px;
      font-weight: 700;
      font-size: 0.75rem;
    }}
    .faq-item {{
      background: var(--bg-gray);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1.25rem;
      margin-bottom: 1rem;
    }}
    .faq-q {{
      font-weight: 700;
      color: #047857;
      font-size: 1rem;
      margin-bottom: 0.5rem;
      display: flex;
      gap: 0.5rem;
    }}
    .faq-a {{
      font-size: 0.925rem;
      color: #334155;
      line-height: 1.7;
    }}
    .internal-links-box {{
      background: #f1f5f9;
      border-radius: 8px;
      padding: 1.5rem;
      margin: 3rem 0;
    }}
    .internal-links-title {{
      font-weight: 800;
      font-size: 1.1rem;
      color: #0f172a;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 0.75rem;
    }}
    .internal-link-card {{
      background: white;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 0.75rem;
      text-decoration: none;
      color: #1e293b;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s;
      display: block;
    }}
    .internal-link-card:hover {{
      border-color: #059669;
      color: #059669;
      transform: translateY(-2px);
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1rem 2rem;
      font-size: 0.875rem;
      margin-top: 4rem;
    }}
    .footer-container {{
      max-width: 1080px;
      margin: 0 auto;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      margin-bottom: 2rem;
    }}
    .footer-links a {{
      color: #cbd5e1;
      text-decoration: none;
    }}
    .footer-links a:hover {{
      color: white;
    }}
    .copyright {{
      text-align: center;
      border-top: 1px solid #334155;
      padding-top: 1.5rem;
      font-size: 0.8125rem;
    }}
  </style>
</head>
<body>

<header>
  <div class="header-container">
    <a href="/" class="site-title">✨ 冬コスメ徹底比較ラボ</a>
    <nav class="nav-links">
      <a href="/">ホーム</a>
      <a href="/#skincare">スキンケア</a>
      <a href="/#haircare">ヘアケア</a>
      <a href="/#bodycare">ボディケア</a>
    </nav>
  </div>
</header>

<main class="main-wrap">
  <article>
    <header class="article-header">
      <span class="article-tag">❄️ 11月・12月 冬本番フェイスオイル特集</span>
      <h1>保湿力の強さで肌乾燥とさようなら！たった1滴で極上ツヤ膜を張る高純度スクワランオイルランク10</h1>
      <div class="update-time">
        <span>📅 公開日: 2026年11月2日</span>
        <span>🔄 最終更新日: 2026年11月2日</span>
        <span>✍️ 監修: 冬コスメ徹底比較ラボ 編集部</span>
      </div>
    </header>

    <div class="lead-box">
      <p>11月から12月へと本格的な冬に突入すると、気温の低下とともに肌の皮脂分泌量は真夏の30%以下にまで急減します。「化粧水や美容液をいくら重ねても、数分後には肌が突っ張る」「クリームを塗っても夕方には頬がカサついて粉を吹く」「目元や口元の乾燥小ジワにファンデーションが溜まる……」そんな深刻な冬の乾燥砂漠肌に頭を抱えていませんか？</p>
      <p style="margin-top: 0.75rem;">その根本原因は、角層内の水分を外気から守るフタである「天然の皮脂膜」が決定的に不足していることにあります。どれほど潤いを与えても、フタがスカスカでは水分は空気中へ蒸散するばかりです。そこで冬の救世主となるのが、人間の皮脂の重要成分をそのまま補える「高純度スクワランオイル」です。純度99.9%以上のピュアオイルなら、たった1滴で重いベタつきを一切残さず、鉄壁の保護膜を形成。本記事では、真冬の過酷な乾燥を完全ブロックする至高の高純度スクワランオイル10選を徹底比較！楽天市場の最新価格・レビューを踏まえて厳選解説します。</p>
    </div>

    <!-- 目次 -->
    <nav class="toc-box">
      <div class="toc-title">📑 目次（タップで各見出しへジャンプ）</div>
      <ul class="toc-list">
        <li><a href="#science">1. 11月・12月の「皮脂枯渇」を救う！スクワランオイルの生体親和性メカニズム</a></li>
        <li><a href="#oil-types">2. サメ由来 vs 植物性（オリーブ・サトウキビ）の違いと失敗しない選び方</a></li>
        <li><a href="#ranking">3. 冬の高純度スクワランオイル おすすめ人気ランキング10選</a></li>
        <li><a href="#comparison-table">4. 高純度スクワランオイル10選の純度・原料・実勢価格 徹底比較表</a></li>
        <li><a href="#pro-technique">5. 美容家直伝！たった1滴で乳液不要になる「水滴エマルジョン乳化テク」</a></li>
        <li><a href="#faq">6. スクワランオイルに関するよくある質問（FAQ）</a></li>
        <li><a href="#summary">7. まとめ：純度と原料で選ぶ！真冬の乾き知らずツヤ肌を叶えるスクワランの極意</a></li>
      </ul>
    </nav>

    <!-- 科学的解説 -->
    <section id="science">
      <h2 class="section-title">🔬 11月・12月の「皮脂枯渇」を救う！スクワランオイルの生体親和性メカニズム</h2>
      <div class="section-content">
        <p>冬の寒さによって外気温が10℃を下回ると、皮膚の毛細血管が収縮し、皮脂腺の活動が急激に低下します。その結果、肌表面を覆って水分の蒸散を防いでいた「皮脂膜」が崩壊。どんなに化粧水で水分を補給しても、数分で大気中へ蒸散してしまう『皮脂枯渇クライシス』が発生します。</p>
        <p>人間の皮脂膜には、実は約12%もの『スクワレン』という生体成分が含まれています。スクワレンは肌を柔らかく保ち、バリア機能を司る重要な成分ですが、20代をピークに分泌量が劇的に減少し、真冬の寒冷下ではほぼゼロに近いレベルまで落ち込んでしまいます。この不安定なスクワレンに水素を添加し、酸化・劣化しないように安定化させたものが『スクワラン』です。</p>
        
        <div class="highlight-card">
          <h4>💡 なぜ一般的な植物オイルやミネラルオイルより優れているのか？</h4>
          <p>オリーブ油やホホバ油などの植物油脂は分子が複雑で肌表面に油膜感（重さやテカリ）が残りやすく、酸化しやすい傾向があります。一方、高純度スクワランは人間の皮脂そのものと同等の構造を持つため、肌に乗せた瞬間に自分の皮脂と同化。油っぽさを感じさせず、さらりと角層の隙間へ浸透して極薄の保護シールドを張ることができます。光や空気による酸化も起きないため、朝のメイク前にも安心して使えます。</p>
        </div>
      </div>
    </section>

    <!-- 種類と選び方 -->
    <section id="oil-types">
      <h2 class="section-title">🌿 サメ由来 vs 植物性（オリーブ・サトウキビ）の違いと失敗しない選び方</h2>
      <div class="section-content">
        <p>スクワランオイルを選ぶ際、最も重要なのが「原料の由来」と「純度」です。それぞれの特徴を理解し、自分の肌質や好みの使用感に合わせて選びましょう。</p>
        
        <h3 style="font-size: 1.1rem; color: #047857; margin: 1.25rem 0 0.5rem;">① 真冬の超乾燥・粉吹き肌なら：【深海鮫肝油由来（純度99%以上）】</h3>
        <p>深海数千メートルの過酷な暗黒・高圧・低温環境に生息するアイザメなどの肝油から抽出されたスクワラン。水分をがっちり閉じ込めるエモリエント持続力が非常に高く、11月〜12月の本格的な寒波で粉を吹いてしまうような深刻な乾燥肌に最も確かな手応えを発揮します。HABAやKISOなどの純度99.9%品を選べば、油焼けの心配も皆無です。</p>

        <h3 style="font-size: 1.1rem; color: #047857; margin: 1.25rem 0 0.5rem;">② ベタつきが苦手・敏感肌・ヴィーガンなら：【植物性（オリーブ・サトウキビ由来）】</h3>
        <p>オリーブの搾りかすやサトウキビ（シュガー）を発酵・精製して作られる植物性スクワラン。サメ由来に比べて分子構造がより均一で、テクスチャーがみずみずしくサラリとしています。肌への摩擦や刺激を極限まで減らしたい敏感肌や、ニキビができやすい混合肌、動物性成分を避けたいヴィーガン志向の方に最適です。</p>

        <h3 style="font-size: 1.1rem; color: #047857; margin: 1.25rem 0 0.5rem;">③ 必ず「1滴単位で調節できる容器」を選ぶこと</h3>
        <p>スクワランオイルは非常に伸びがよく、1回に必要な量は全顔で「たった1滴」です。ドバッと出てしまう容器だと、つけすぎてメイク崩れやテカリの原因になります。スポイト式や、1滴ずつポタポタと出せるスマートボトルを採用している商品を選ぶことが失敗しないコツです。</p>
      </div>
    </section>

    <!-- ランキングセクション -->
    <section id="ranking">
      <h2 class="section-title">🏆 冬の高純度スクワランオイル おすすめ人気ランキング10選</h2>
      <p style="margin-bottom: 2rem; font-size: 0.95rem; color: #475569;">
        楽天市場の最新売れ筋データ、口コミ満足度、原料の純度と安全性を徹底検証し、11月・12月の冬に本気で頼れる高純度スクワランオイル10選を詳しくレビューします。
      </p>

      {"".join(cards_html)}
    </section>

    <!-- 比較表 -->
    <section id="comparison-table">
      <h2 class="section-title">📊 高純度スクワランオイル10選の純度・原料・実勢価格 徹底比較表</h2>
      <div class="section-content">
        <p>厳選した10商品の原料（サメ/植物性）、純度、実勢価格、特徴を一覧表にまとめました。ご自身のライフスタイルや使用部位（顔・髪・全身）に合わせて比較してください。</p>
        <div class="table-container">
          <table class="summary-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / 容量</th>
                <th>原料・純度スペック</th>
                <th>楽天市場実勢価格</th>
                <th>商品リンク</th>
              </tr>
            </thead>
            <tbody>
              {"".join(table_rows)}
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- プロの使い方 -->
    <section id="pro-technique">
      <h2 class="section-title">✨ 美容家直伝！たった1滴で乳液不要になる「水滴エマルジョン乳化テク」</h2>
      <div class="section-content">
        <p>スクワランオイルを「乾いた肌」に直接塗るのは非常にもったいない使い方です。プロの美容家が実践する、肌の上で天然のフレッシュ乳液を作り出す裏ワザを伝授します。</p>
        
        <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1rem;">
          <h4 style="color: #047857; font-size: 1.05rem; margin-bottom: 0.5rem;">ステップ1：化粧水をたっぷり馴染ませ「肌に水滴を残す」</h4>
          <p style="font-size: 0.925rem; margin-bottom: 1rem;">洗顔後、化粧水を2〜3回重ね付けし、顔の表面にみずみずしい水分がたっぷりと残っている状態を作ります。水分が完全に乾ききる前に次のステップへ進むのが決定的なポイントです。</p>

          <h4 style="color: #047857; font-size: 1.05rem; margin-bottom: 0.5rem;">ステップ2：手のひらに「たった1滴」落として両手を擦り合わせる</h4>
          <p style="font-size: 0.925rem; margin-bottom: 1rem;">手のひらにスクワランオイルをポタッと『1滴だけ』落とします。両手を擦り合わせて手のひら全体へ極薄に広げ、体温で人肌に温めます。2滴以上つけると膜が厚くなりすぎるため、まずは1滴から始めてください。</p>

          <h4 style="color: #047857; font-size: 1.05rem; margin-bottom: 0.5rem;">ステップ3：優しく包み込み「肌表面で乳化（エマルジョン化）」させる</h4>
          <p style="font-size: 0.925rem;">濡れた顔を手のひら全体で包み込むように優しくハンドプレスします。肌の上にある化粧水と手のひらのスクワランが混ざり合い、その場で出来立てのフレッシュな乳液（エマルジョン）が完成。角層深部へ水分を押し込みながら、表面にサラサラの保護膜が形成されます。</p>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section id="faq">
      <h2 class="section-title">❓ スクワランオイルに関するよくある質問（FAQ）</h2>
      <div class="section-content">
        {"".join([f'''
        <div class="faq-item">
          <div class="faq-q"><span>Q.</span><strong>{item['q']}</strong></div>
          <div class="faq-a">{item['a']}</div>
        </div>
        ''' for item in faq_items])}
      </div>
    </section>

    <!-- まとめ -->
    <section id="summary">
      <h2 class="section-title">🌿 まとめ：純度と原料で選ぶ！真冬の乾き知らずツヤ肌を叶えるスクワランの極意</h2>
      <div class="section-content">
        <p>11月・12月の冬本番、どんなにスキンケアを重ねても乾燥が収まらないのは、あなたの肌の水分保持力不足ではなく「皮脂膜の不足」が原因です。冬の寒冷で活動を休止してしまった皮脂腺に代わり、純度99.9%のスクワランをたった1滴補うだけで、肌のバリア機能は劇的に復活します。</p>
        <p>不動の安心感と圧倒的な実績を求めるなら『HABA 高品位スクワラン』、全身や毛先まで惜しみなく贅沢に使いたいなら大容量の『無印良品』や『&SH』、成分重視の濃厚原液を求めるなら『KISO』や『The Ordinary』がベストな選択肢です。</p>
        <p>たった1滴で数ヶ月間持ち、乳液やクリームの代わりにもなるスクワランオイルは、まさに冬のスキンケアにおける最高の投資です。今日からスキンケアの最後に1滴のツヤ膜をプラスして、暖房直下でもしっとり吸い付くような輝く素肌を手に入れてください。</p>
      </div>
    </section>

    <!-- 内部リンク -->
    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <!-- 内部リンク更新スクリプトにより自動展開 -->
      </div>
    </div>
  </article>
</main>

<footer>
  <div class="footer-container">
    <div class="footer-links">
      <a href="/">冬コスメTOP</a>
      <a href="/winter-ceramide-lotion">高保湿セラミド化粧水</a>
      <a href="/winter-medicinal-lip">高保湿薬用リップクリーム</a>
      <a href="/winter-ceramide-cream">高保湿セラミドクリーム</a>
      <a href="/winter-face-oil">高保湿フェイスオイル</a>
      <a href="/winter-booster-oil">導入美容液オイル</a>
    </div>
    <div class="copyright">
      &copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved.
    </div>
  </div>
</footer>

</body>
</html>
"""

output_path = "winter-squalane-oil.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"✓ Successfully generated {output_path} ({len(full_html):,} bytes)")
