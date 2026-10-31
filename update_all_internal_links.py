import os
import re

ALL_ARTICLES = [
    {
        "url": "/winter-cleansing-oil",
        "file": "winter-cleansing-oil.html",
        "title": "🫧 保湿力の強さで冬の頑固な毛穴詰まり・洗い上がりの砂漠化とさようなら！摩擦レスでうるおい守る高保湿クレンジングオイルランク10",
        "desc": "11月・12月の寒さで固まった毛穴の角栓・皮脂詰まりや濃密メイクを摩擦レスに浮かせながら、リッチな植物美容オイルで洗い上がりのつっぱり・乾燥を防ぐ神高保湿クレンジングオイル10選を徹底比較！",
        "footer_name": "クレンジングオイル"
    },
    {
        "url": "/winter-body-milk",
        "file": "winter-body-milk.html",
        "title": "🧴 保湿力の強さで全身のカサカサ粉吹き・インナー摩擦乾燥とさようなら！スーッと浸透して服もすぐ着られる高保湿ボディミルクランク10",
        "desc": "11月・12月のタイツやヒートテックによる摩擦乾燥・すねの粉吹き・かゆみを撃退！水分と油分を黄金バランスで補給し、ベタつかず就寝前も快適に使える神高保湿ボディミルク・エマルジョン10選を徹底比較！",
        "footer_name": "高保湿ボディミルク"
    },
    {
        "url": "/winter-toner-pad",
        "file": "winter-toner-pad.html",
        "title": "💧 保湿力の強さで朝の乾燥ゴワつき・メイクの粉浮きとさようなら！貼るだけで水分爆弾チャージする高保湿トナーパッドランク10",
        "desc": "11月・12月の朝の暖房乾燥やインナードライによるメイクの粉浮き・毛穴目立ちを解決！美容液を贅沢に含んだパッドで部分パック＆角質ケアができる神高保湿トナーパッド10選を徹底比較！",
        "footer_name": "高保湿トナーパッド"
    },
    {
        "url": "/winter-night-cream",
        "file": "winter-night-cream.html",
        "title": "🌙 保湿力の強さで睡眠中の砂漠肌・乾燥小ジワとさようなら！翌朝もっちり吸い付く高保湿ナイトクリームランク10",
        "desc": "11月・12月の厳しい寒さと夜間暖房による砂漠化・乾燥小ジワを睡眠中に集中リペア！コスメデコルテ、KANEBO、エリクシール、キュレル、オルビス、SK-IIなど、翌朝ふっくらハリ肌へ導く高保湿ナイトクリーム厳選10選。",
        "footer_name": "ナイトクリーム"
    },
    {
        "url": "/winter-cleansing-milk",
        "file": "winter-cleansing-milk.html",
        "title": "🥛 保湿力の強さで冬の洗い上がりツッパリ・摩擦乾燥とさようなら！うるおい残して優しく落とす高保湿クレンジングミルクランク10",
        "desc": "11月・12月の洗顔後ツッパリ・摩擦ダメージ・乾燥小ジワを徹底解決！カバーマーク、カウブランド無添加、チャントアチャーム、シスレー、ヴェレダなど、美容液成分たっぷりでうるおいを守り抜く高保湿クレンジングミルク厳選10選。",
        "footer_name": "クレンジングミルク"
    },
    {
        "url": "/winter-hair-mist",
        "file": "winter-hair-mist.html",
        "title": "✨ 保湿力の強さで冬の静電気・毛先パサつきとさようなら！髪にうるおいヴェールをまとう高保湿ヘアミストランク10",
        "desc": "11月・12月の冬の静電気・マフラー摩擦・暖房乾燥による髪のパサパサ・ボサボサを瞬時に解消！ジルスチュアート、スティーブンノル、オルビス、ナプラ、ReFa、ラ・カスタなど、毛先までちゅるんとまとまる高保湿ヘアミスト厳選10選。",
        "footer_name": "高保湿ヘアミスト"
    },
    {
        "url": "/winter-cleansing-balm",
        "file": "winter-cleansing-balm.html",
        "title": "🫧 保湿力の強さで冬の突っ張り・乾燥小じわとさようなら！体温でとろけて毛穴汚れもつるんと落とす高保湿クレンジングバームランク10",
        "desc": "11月・12月の厳しい寒さと乾いた空気による洗顔後の急激なツッパリ・乾燥小じわを解決！DUO、パーフェクトワンフォーカス、ルルルン、クリニーク、バニラコ、KANEBOなど、体温でとろけて毛穴の角栓や濃密メイクを摩擦レスにオフしながら潤いヴェールで満たす高保湿クレンジングバーム厳選10選。",
        "footer_name": "クレンジングバーム"
    },
    {
        "url": "/winter-scalp-shampoo",
        "file": "winter-scalp-shampoo.html",
        "title": "🌿 保湿力の強さで頭皮乾燥・フケかゆみとさようなら！うるおい守る高保湿スカルプシャンプーランク10",
        "desc": "11月・12月の厳しい寒さとエアコン暖房による頭皮の砂漠化、乾性フケ、ムズムズするかゆみをブロック！haru、オージュア、キュレル、エトヴォス、カダソン、スカルプDなど、アミノ酸系洗浄成分とセラミド・植物エキスで頭皮のうるおいバリアを守り抜く高保湿スカルプシャンプー厳選10選。",
        "footer_name": "スカルプシャンプー"
    },
    {
        "url": "/winter-cica-cream",
        "file": "winter-cica-cream.html",
        "title": "🌱 保湿力の強さで冬の肌荒れ・寒風赤みとさようなら！肌バリアを集中強化する高保湿シカクリームランク10",
        "desc": "11月・12月の冷たい北風と暖房乾燥による赤ら顔、ヒリつき、粉吹き肌荒れを急速リペア！ラロッシュポゼ、VT、Dr.Jart+、アベンヌ、バイオヒールボ、Dr.Gなど、高純度ツボクサエキス（CICA）とパンテノール・セラミドで肌バリアを集中強化する高保湿シカクリーム厳選10選。",
        "footer_name": "シカクリーム"
    },
    {
        "url": "/winter-holiday-coffret",
        "file": "winter-holiday-coffret.html",
        "title": "🎁 贅沢なうるおいと輝きで真冬の乾燥肌・メイクを特別格上げ！11月12月限定ホリデーコレクション＆高保湿クリスマスコフレランク10",
        "desc": "11月・12月限定の争奪戦コフレを厳選！コスメデコルテ、ディオール、ルナソル、SABON、キールズ、SK-IIなど、冬の乾燥肌を高保湿ケアしながら特別な輝きを添える名品10選。",
        "footer_name": "クリスマスコフレ"
    },
    {
        "url": "/winter-enzyme-wash",
        "file": "winter-enzyme-wash.html",
        "title": "🫧 保湿力の強さで冬の角質ゴワつき・くすみ毛穴とさようなら！つっぱらず透明感を呼び覚ます高保湿酵素洗顔パウダーランク10",
        "desc": "冬の寒さと乾燥で硬くなった角質ゴワつき・くすみ毛穴を救う！オバジC、suisaiゴールド、ファンケル、カネボウ、estなど、つっぱらず透明感を呼び覚ます高保湿酵素洗顔10選。",
        "footer_name": "酵素洗顔パウダー"
    },
    {
        "url": "/winter-tinted-lip-balm",
        "file": "winter-tinted-lip-balm.html",
        "title": "💄 保湿力の強さで冬のカサカサ唇＆血色レスとさようなら！ひと塗りでぷるんと潤う高保湿カラーリップバームランク10",
        "desc": "冬の寒風・エアコン乾燥による唇の皮剥け・縦ジワ・血色不良を救う！ディオール、シャネル、KANEBO、NARS、ボビイ ブラウンなど、高保湿と透け感美発色を両立した神カラーリップバーム10選。",
        "footer_name": "カラーリップバーム"
    },
    {
        "url": "/winter-eyelash-serum",
        "file": "winter-eyelash-serum.html",
        "title": "👁️ 保湿力の強さで冬のまつ毛抜け・パサつき乾燥とさようなら！ハリ・コシ・密度感を呼び覚ます高保湿まつ毛美容液・アイラッシュセラムランク10",
        "desc": "冬の暖房乾燥・冷風・マスカラ摩擦で細く傷んだまつ毛を救う！ラッシュアディクト、エマーキット、ディオール、ランコム、コスメデコルテなど、キューティクルを高保湿補修して圧倒的なハリ・コシ・密度感を呼び覚ます神まつ毛美容液厳選10選。",
        "footer_name": "まつ毛美容液"
    },
    {
        "url": "/winter-point-makeup-remover",
        "file": "winter-point-makeup-remover.html",
        "title": "✨ 保湿力の強さで目元・口元の摩擦ダメージ＆乾燥小ジワとさようなら！デリケートな皮膚をうるおいで守り抜く高保湿ポイントメイクリムーバーランク10",
        "desc": "冬の乾燥小ジワ・色素沈着・唇の皮剥けの主因となるクレンジング摩擦を撃退！RMK、シャネル、クレ・ド・ポー ボーテ、ビフェスタ、ランコムなど、濃密アイメイクやティントをこすらずスルンと落として高保湿キープする神ポイントメイクリムーバー厳選10選。",
        "footer_name": "ポイントリムーバー"
    },
    {
        "url": "/winter-massage-cream",
        "file": "winter-massage-cream.html",
        "title": "💆‍♀️ 保湿力の強さで冬の冷えむくみ・乾燥くすみ・フェイスラインたるみとさようなら！巡りを高めてふっくら上向き肌へ導く高保湿フェイスマッサージクリームランク10",
        "desc": "冬の寒波による血行不良・冷え固まった筋肉のコリ・重たいむくみ・乾燥くすみを撃退！POLA B.A、SUQQU、資生堂エリクシール、コスメデコルテAQ、アルビオンエクシアなど、摩擦ゼロで巡りを高め上向き立体ハリ肌へ導く神マッサージクリーム厳選10選。",
        "footer_name": "マッサージクリーム"
    },
    {
        "url": "/winter-hand-serum",
        "file": "winter-hand-serum.html",
        "title": "🤲 保湿力の強さで手荒れ・老け手・乾燥シワとさようなら！スマホ操作もサラリと快適＆手肌のキメをふっくら満たす高保湿ハンド美容液・ハンドセラムランク10",
        "desc": "冬の寒風・手洗い・消毒による手荒れや乾燥小ジワを救う！SHIRO、アルビオンエクシア、アユーラ、オサジ、コスメデコルテなど、ベタつかずスマホも快適操作できる神高保湿ハンド美容液厳選10選。",
        "footer_name": "ハンド美容液"
    },
    {
        "url": "/winter-bath-oil",
        "file": "winter-bath-oil.html",
        "title": "🛁 保湿力の強さで冬の湯上がり乾燥・粉吹きとさようなら！お風呂に浸かるだけで全身シルク肌へ導く極上高保湿バスオイルランク10",
        "desc": "真冬の脱衣所での急激な乾燥・粉吹き・かゆみを救う！ジョーマローン、アユーラ、アロマセラピーアソシエイツ、ポールシェリー、ヴェレダなど、お風呂上がりボディクリーム不要の極上高保湿バスオイル厳選10選。",
        "footer_name": "高保湿バスオイル"
    },
    {
        "url": "/winter-body-butter",
        "file": "winter-body-butter.html",
        "title": "🧴 保湿力の強さで冬の粉吹き肌・乾燥かゆみとさようなら！こっくり濃厚ヴェールで全身を包み込む神高保湿ボディバターランク10",
        "desc": "真冬のすねの粉吹き・乾燥かゆみ・ひじひざのガサガサを救う！ザボディショップ、ローラメルシエ、キールズ、ロクシタン、サボンなど、こっくり濃厚エモリエント膜で一晩中うるおいを守り抜く神高保湿ボディバター厳選10選。",
        "footer_name": "高保湿ボディバター"
    },
    {
        "url": "/winter-hair-balm",
        "file": "winter-hair-balm.html",
        "title": "💆‍♀️ 保湿力の強さで毛先のパサつき・静電気・広がりとさようなら！冬の冷風から一日中うるおいキープ＆全身保湿できるマルチ高保湿ヘアバームランク10",
        "desc": "冬の寒風・乾燥・マフラー静電気でパサつく髪を救う！ザ・プロダクト、N.（エヌドット）、track（トラック）、ミルボンなど、毛先のうるおい束感キープから手肌・リップの保湿まで叶える神ヘアバーム厳選10選。",
        "footer_name": "高保湿ヘアバーム"
    },
    {
        "url": "/winter-hot-cleansing",
        "file": "winter-hot-cleansing.html",
        "title": "🫧 保湿＆温感スチーム効果で冬の冷え固まった毛穴・乾燥ゴワつきとさようなら！じんわり温めてうるおいを守り抜く高保湿温感クレンジングランク10",
        "desc": "冬の寒さで冷え固まった毛穴の角栓・乾燥ゴワつきを撃退！マナラ、DUO（デュオ）、スキンビル、ベネフィーク、ラフラなど、じんわり温感スチーム＆美容液成分90%超で洗い上げる高保湿温感クレンジング厳選10選。",
        "footer_name": "高保湿温感クレンジング"
    },
    {
        "url": "/winter-neck-cream",
        "file": "winter-neck-cream.html",
        "title": "✨ 保湿力の強さで首元の乾燥小ジワ・マフラー摩擦とさようなら！冬のタートルネック映えするハリツヤ肌へ導く高保湿ネック＆デコルテクリームランク10",
        "desc": "冬のタートルネックやマフラーのチクチク摩擦、乾燥で深まる首の横ジワを救う！クラランス、資生堂リバイタル、ポーラ、シスレー、肌美精など、首元専用の高保湿ネック＆デコルテクリーム厳選10選。",
        "footer_name": "高保湿ネッククリーム"
    },
    {
        "url": "/winter-lip-scrub",
        "file": "winter-lip-scrub.html",
        "title": "💄 保湿力の強さで唇のガサガサ皮剥け・縦ジワとさようなら！古い角質を優しくオフしてぷるんと潤う高保湿リップスクラブランク10",
        "desc": "冬の北風と暖房乾燥でガサガサに皮剥けした唇を救う！レブロン、キャンメイク、ディオール、LUSH、ハウスオブローゼなど高保湿リップスクラブ厳選10選。",
        "footer_name": "高保湿リップスクラブ"
    },
    {
        "url": "/winter-bb-cream",
        "file": "winter-bb-cream.html",
        "title": "✨ 保湿力の強さで冬の粉ふき・乾燥崩れとさようなら！1本で一日中うるツヤ肌が続く高保湿BB・CCクリームランク10",
        "desc": "冬の朝の冷え込みと乾燥によるファンデの粉吹き・ひび割れを撃退！コスメデコルテ、dプログラム、マキアージュ、ラロッシュポゼなど高保湿BB・CCクリーム厳選10選。",
        "footer_name": "高保湿BB・CCクリーム"
    },
    {
        "url": "/winter-carbonic-pack",
        "file": "winter-carbonic-pack.html",
        "title": "🫧 保湿＆血行促進で冬の冷えくすみ・ゴワつきとさようなら！サロン級の透明感と弾力を呼び覚ます高保湿炭酸パック・炭酸マスクランク10",
        "desc": "冬の寒波による血行不良・くすみ・ゴワつく角質を撃退！エニシーグローパック、EKATO、ドクターメディオンなど高保湿炭酸パック厳選10選。",
        "footer_name": "高保湿炭酸パック"
    },
    {
        "url": "/winter-uv-cream",
        "file": "winter-uv-cream.html",
        "title": "☀️ 保湿力の強さで冬の紫外線＆乾燥ツッパリとさようなら！まるで美容クリームな極上高保湿日焼け止め・UV美容液ランク10",
        "desc": "冬の乾燥と冷風に負けない！カネボウ ヴェイル オブ デイ、コスメデコルテ サンシェルター、オルビス、クレ・ド・ポー ボーテ、POLAなど高保湿UV10選。",
        "footer_name": "高保湿日焼け止め"
    },
    {
        "url": "/winter-wrinkle-cream",
        "file": "winter-wrinkle-cream.html",
        "title": "👁️ 保湿力の強さで冬の乾燥小ジワ・ほうれい線とさようなら！角層深く密着する高保湿シワ改善リンクルクリームランク10",
        "desc": "冬の乾燥小ジワ・ほうれい線・ちりめんジワを撃退！エリクシール レチノパワー、POLA リンクルショット、コスデコ iP.Shot、KANEBOなど薬用リンクル10選。",
        "footer_name": "シワ改善クリーム"
    },
    {
        "url": "/winter-body-wash",
        "file": "winter-body-wash.html",
        "title": "🛁 保湿力の強さで冬のお風呂上がり乾燥・かゆみとさようなら！うるおいを守ってしっとり洗い上げる高保湿ボディウォッシュランク10",
        "desc": "脱衣所でのかゆみ・すねの粉吹きを元から防ぐ！ケアセラ、ミノン、キュレル、SABON、ロクシタンなどセラミド保持泡ソープ＆シャワーオイル10選。",
        "footer_name": "高保湿ボディウォッシュ"
    },
    {
        "url": "/winter-make-keep-mist",
        "file": "winter-make-keep-mist.html",
        "title": "✨ 保湿力の強さで肌乾燥・粉吹きとさようなら！暖房直撃でもうるツヤ肌を一日中ロックする高保湿メイクキープミストランク10",
        "desc": "冬の暖房乾燥による粉吹き・ひび割れ・マフラー摩擦を完全防御！コーセー、コスメデコルテ、ディオール、クラランス、ダルバなど高保湿ミスト10選。",
        "footer_name": "メイクキープミスト"
    },
    {
        "url": "/winter-lip-oil",
        "file": "winter-lip-oil.html",
        "title": "💄 保湿力の強さで唇のガサガサ皮剥けとさようなら！濃密植物オイルでガラス玉のようなぷるツヤ唇を叶える高保湿リップオイルランク10",
        "desc": "冬の皮剥け・縦ジワを濃密植物オイルで集中トリートメント！クラランス、ディオール、ジバンシイ、シャネル、エクセルなど極上リップオイル10選。",
        "footer_name": "高保湿リップオイル"
    },
    {
        "url": "/winter-body-oil",
        "file": "winter-body-oil.html",
        "title": "🛁 保湿力の強さで全身の乾燥かゆみ・粉吹きとさようなら！お風呂上がりの肌をとろけるシルクへ導く高保湿ボディオイルランク10",
        "desc": "すねの粉吹き・乾燥かゆみ・冷えむくみを完全解消！ヴェレダ、クラランス、ニュクス、バイオイル、メルヴィータなど高保湿ボディオイル10選。",
        "footer_name": "高保湿ボディオイル"
    },
    {
        "url": "/winter-liquid-foundation",
        "file": "winter-liquid-foundation.html",
        "title": "✨ 保湿力の強さで肌乾燥・粉吹きとさようなら！美容液級のうるおいで一日中ひび割れ・毛穴落ちを防ぐ高保湿リキッドファンデーションランク10",
        "desc": "暖房直撃でも夕方の粉吹き・ひび割れ・毛穴落ちゼロ！資生堂エッセンススキングロウ、コスデコゼンウェアグロウ、ディオール、SUQQUなど美容液ファンデ10選。",
        "footer_name": "リキッドファンデ"
    },
    {
        "url": "/winter-cream-cheek",
        "file": "winter-cream-cheek.html",
        "title": "🌸 保湿力の強さで肌乾燥・寒暖差くすみとさようなら！冬の冷え切った頬にじゅわっと上気ツヤを仕込む高保湿チークランク10",
        "desc": "冬の寒暖差による青白いくすみやパウダーチークの粉浮きを一掃！シャネル、アディクション、コスデコ、ローラメルシエなど高保湿クリーム＆リキッドチーク10選。",
        "footer_name": "高保湿チーク"
    },
    {
        "url": "/winter-cream-eyeshadow",
        "file": "winter-cream-eyeshadow.html",
        "title": "👁️ 保湿力の強さでまぶたの乾燥・二重幅の粉落ちとさようなら！濡れツヤと透明感を一日中キープする高保湿アイシャドウランク10",
        "desc": "冬の乾燥まぶたや二重幅のシワ溜まりを完全解決！コスメデコルテアイグロウジェム、ローラメルシエキャビアスティックなど高保湿クリーム＆リキッドアイシャドウ10選。",
        "footer_name": "アイシャドウ"
    },
    {
        "url": "/winter-highlighter",
        "file": "winter-highlighter.html",
        "title": "✨ 保湿力の強さで冬の乾燥くすみ・粉浮きとさようなら！暖房下でも内側から発光する生ツヤを宿す高保湿ハイライトランク10",
        "desc": "暖房の乾燥でパウダーが粉浮き・小じわ崩れする冬の肌に！シャネルのボームエサンシエル、hince、ディオール、クレドポーなど、うるおい生ツヤを宿す高保湿ハイライト厳選10選。",
        "footer_name": "高保湿ハイライト"
    },
    {
        "url": "/winter-hair-oil",
        "file": "winter-hair-oil.html",
        "title": "💆‍♀️ 保湿力の強さで毛先のパサつき・静電気・マフラー摩擦とさようなら！真冬の髪を芯から守り抜く濃厚高保湿ヘアオイルランク10",
        "desc": "冬の北風・暖房・静電気・マフラー摩擦に負けない！モロッカンオイル、ミルボンエルジューダMO、ケラスターゼ、N.ポリッシュオイルなど濃厚高保湿ヘアオイル10選。",
        "footer_name": "高保湿ヘアオイル"
    },
    {
        "url": "/winter-lip-mask",
        "file": "winter-lip-mask.html",
        "title": "💄 保湿力の強さで唇のガサガサ皮剥け・縦ジワとさようなら！寝ている間に濃厚ラップで集中リペアする高保湿リップマスクランク10",
        "desc": "暖房の乾燥でカサカサ・皮剥け・縦ジワが目立つ唇を寝ている間に集中リペア！ラネージュ、キュレル、トリデン、CNP、タカミなど高保湿リップマスク10選。",
        "footer_name": "高保湿リップマスク"
    },
    {
        "url": "/winter-hair-milk",
        "file": "winter-hair-milk.html",
        "title": "💆‍♀️ 保湿力の強さで髪のパサつき・静電気とさようなら！冬の乾燥・マフラー摩擦を芯から防ぐ高保湿ヘアミルク＆アウトバストリートメントランク10",
        "desc": "オイルだけでは届かない毛髪内部へ水分＆CMCを集中補給！オルビス、ミルボンエルジューダ、N.シアミルク、ケラスターゼなど神ヘアミルク10選。",
        "footer_name": "高保湿ヘアミルク"
    },
    {
        "url": "/winter-cushion-foundation",
        "file": "winter-cushion-foundation.html",
        "title": "✨ 保湿力の強さで肌乾燥とさようなら！冬の暖房直撃でも夕方までひび割れない高保湿クッションファンデーション＆美容液ファンデランク10",
        "desc": "暖房の効いた部屋でも夕方まで乾燥割れ・粉吹き知らず！TIRTIRクリスタル、CLIOハイグロウ、ジョンセンムル、YSLなど美容液クッション10選。",
        "footer_name": "クッションファンデ"
    },
    {
        "url": "/winter-body-scrub",
        "file": "winter-body-scrub.html",
        "title": "🛁 保湿力の強さで全身のゴワつき・粉吹きとさようなら！入浴時に潤いオイルを仕込む高保湿ボディスクラブ＆角質ケアランク10",
        "desc": "頑固なひじ・ひざ・かかとの角質をオフし濃厚オイル膜で全身シールド！SABON、ハウスオブローゼ、LUSH、クナイプなど神スクラブ10選。",
        "footer_name": "ボディスクラブ"
    },
    {
        "url": "/winter-hydrating-serum",
        "file": "winter-hydrating-serum.html",
        "title": "💧 保湿力の強さで肌乾燥・砂漠化とさようなら！冬のバリア崩壊を集中救済する高保湿美容液＆高濃度アンプルランク10",
        "desc": "暖房直撃でカラカラの角層を集中救済！コスメデコルテリポソーム、トリデン、キュレル、エトヴォスなどセラミド＆ヒアルロン酸セラム10選。",
        "footer_name": "高保湿美容液"
    },
    {
        "url": "/winter-concealer",
        "file": "winter-concealer.html",
        "title": "👁️ 保湿力の強さで目元・口元の乾燥ひび割れとさようなら！冬の青クマ・くすみを潤いヴェールで消し去る高保湿コンシーラーランク10",
        "desc": "夕方の目元のちりめんジワ・地割れ割れに終止符！ディオールスキン、コスメデコルテ、NARS、アンドビーなど美容液コンシーラー10選。",
        "footer_name": "高保湿コンシーラー"
    },
    {
        "url": "/winter-lip-tint",
        "file": "winter-lip-tint.html",
        "title": "💄 保湿力の強さで唇の乾燥・皮剥け・血色レスとさようなら！真冬のイベントも一日中うるおい発色が続く高保湿リップティント＆美容液ルージュランク10",
        "desc": "皮剥け知らずで一日中落ちない！KATEリップモンスター、ロムアンドメルティングバーム、オペラ、ディオールなど高保湿ルージュ10選。",
        "footer_name": "高保湿リップティント"
    },
    {
        "url": "/winter-powder",
        "file": "winter-powder.html",
        "title": "✨ 保湿力の強さで肌乾燥・粉吹きとさようなら！暖房の乾燥に負けないしっとり高保湿フェイスパウダーランク10",
        "desc": "エアコン乾燥で粉吹き・小じわ割れする冬の肌に！コスメデコルテ、エレガンス、NARSなど美容液成分高配合の冬用高保湿パウダー10選。",
        "footer_name": "冬用パウダー"
    },
    {
        "url": "/winter-lip-plumper",
        "file": "winter-lip-plumper.html",
        "title": "💄 保湿力の強さで唇乾燥・縦ジワとさようなら！ぷるんとボリューミーに潤す高保湿リッププランパーランク10",
        "desc": "カサカサ・縦ジワ唇を瞬時にふっくらボリュームアップ！ディオール、クラランス、ヴィセ、ジルスチュアートなど神プランパー10選。",
        "footer_name": "リッププランパー"
    },
    {
        "url": "/winter-hair-mask",
        "file": "winter-hair-mask.html",
        "title": "💆‍♀️ 保湿力の強さで髪の乾燥・静電気とさようなら！真冬の毛先パサつき・広がりを芯から集中補修する高保湿ヘアマスク＆ヘアトリートメントランク10",
        "desc": "マフラー摩擦・静電気で広がるダメージ毛を芯から修復！フィーノ、fino、資生堂ツバキ、ケラスターゼ、オージュアなど神トリートメント10選。",
        "footer_name": "集中ヘアマスク"
    },
    {
        "url": "/winter-stick-serum",
        "file": "winter-stick-serum.html",
        "title": "✨ 保湿力の強さで肌乾燥とさようなら！日中いつでもメイクの上から乾燥小じわ・粉吹きを瞬時に消し去る高保湿スティック美容液ランク10",
        "desc": "暖房で乾いた目元・ほうれい線にひと塗り！イプサ、KAHI、カネボウなどポーチの必須アイテム10選。",
        "footer_name": "スティック美容液"
    },
    {
        "url": "/winter-scalp-serum",
        "file": "winter-scalp-serum.html",
        "title": "💆‍♀️ 保湿力の強さで頭皮乾燥とさようなら！冬のフケ・かゆみ・つっぱりを防ぎうるおい頭皮環境へ導く高保湿スカルプセラム・頭皮美容液ランク10",
        "desc": "冬の乾燥フケ・かゆみ・抜け毛を根本ケア！キュレル、アヴェダ、資生堂アデノバイタルなど頭皮用美容液10選。",
        "footer_name": "頭皮美容液"
    },
    {
        "url": "/winter-toneup-base",
        "file": "winter-toneup-base.html",
        "title": "🌸 保湿力の強さで肌乾燥とさようなら！冬の血色レス・乾燥くすみを払拭し夕方まで透き通るツヤ肌を保つ高保湿トーンアップ下地ランク10",
        "desc": "冬の青白い顔色に血色と透明感を注入！ラロッシュポゼ、コスメデコルテ、ポール＆ジョーなど神下地10選。",
        "footer_name": "トーンアップ下地"
    },
    {
        "url": "/winter-sleeping-mask",
        "file": "winter-sleeping-mask.html",
        "title": "🌙 【2026最新】寝ている間の濃厚ラッピングで肌乾燥とさようなら！翌朝もっちり吸いつく神スリーピングマスク＆夜用パック10選",
        "desc": "寝ている間の暖房砂漠から肌を救う！エリクシール、ラネージュ、ファミュなど翌朝の肌が激変する夜用マスク特集。",
        "footer_name": "スリーピングマスク"
    },
    {
        "url": "/winter-nail-oil",
        "file": "winter-nail-oil.html",
        "title": "💅 【2026最新】指先のささくれ・パサつきとさようなら！しっとりツヤ爪を育てる高保湿ネイルオイル＆キューティクルオイル10選",
        "desc": "乾燥で割れる爪・ささくれ・二枚爪を徹底ケア！uka、OPI、ロクシタンなどポーチに常備したいネイルオイル厳選。",
        "footer_name": "ネイルオイル"
    },
    {
        "url": "/winter-foot-cream",
        "file": "winter-foot-cream.html",
        "title": "🦶 【2026最新】ガサガサ・ひび割れかかととさようなら！タイツが引っかからない柔らか肌へ導く高保湿フットクリーム＆かかとケア10選",
        "desc": "タイツが電線するガサガサかかとを集中修復！ユースキン、ロコベース、ニュートロジーナなど冬の救世主フットケア。",
        "footer_name": "フットクリーム"
    },
    {
        "url": "/winter-emulsion",
        "file": "winter-emulsion.html",
        "title": "🧴 保湿力の強さで肌乾燥とさようなら！うるおい密封と柔らかツヤ肌を叶える高保湿乳液＆エマルジョン10選",
        "desc": "冬の粉吹き・インナードライを解消！コスメデコルテ、アルビオン、ミノン、イハダなど水分と油分を黄金バランスで補う乳液。",
        "footer_name": "高保湿乳液"
    },
    {
        "url": "/winter-face-oil",
        "file": "winter-face-oil.html",
        "title": "✨ 保湿力の強さで肌乾燥とさようなら！皮脂枯れ砂漠肌を救う極上高保湿フェイスオイル＆美容オイル10選",
        "desc": "化粧水が弾かれるゴワつき肌を即ほぐす！ハーバー高品位スクワラン、メルヴィータ、キールズなど冬の乾燥対策オイル。",
        "footer_name": "フェイスオイル"
    },
    {
        "url": "/winter-repair-balm",
        "file": "winter-repair-balm.html",
        "title": "🛡️ 保湿力の強さで肌乾燥とさようなら！粉吹き・ひび割れ皮剥けを緊急レスキューする高保湿リペアバーム10選",
        "desc": "皮剥け・粉吹き・花粉や寒暖差によるゆらぎ肌をワセリンや高精製オイルで完全密閉保護する神バーム特集。",
        "footer_name": "リペアバーム"
    },
    {
        "url": "/winter-bath-care",
        "file": "winter-bath-care.html",
        "title": "🛁 保湿力の強さで肌乾燥とさようなら！温活と全身うるおいバリアを叶える高保湿入浴剤＆バスミルク10選",
        "desc": "お風呂上がり急激に乾く全身の肌を浴槽の中で先回り保湿！BARTH、アユーラ、キュレル、クナイプなど温活＆高保湿入浴料。",
        "footer_name": "高保湿入浴剤"
    },
    {
        "url": "/winter-face-wash",
        "file": "winter-face-wash.html",
        "title": "🧼 保湿力の強さで肌乾燥とさようなら！冬のつっぱり・粉吹きを防ぐうるおい吸着・高保湿洗顔料10選",
        "desc": "洗顔後のつっぱり感ゼロ！カネボウコンフォートストレッチィ、オバジ、キュレルなどうるおいを守りながら汚れを落とす洗顔料。",
        "footer_name": "高保湿洗顔"
    },
    {
        "url": "/winter-face-mist",
        "file": "winter-face-mist.html",
        "title": "💦 保湿力の強さで肌乾燥とさようなら！暖房の砂漠化からメイクを守る高保湿ミスト化粧水10選",
        "desc": "日中オフィスでカサつく肌にメイクの上から水分補給！エリクシールつや玉ミスト、キュレル、コスメデコルテなど携帯ミスト。",
        "footer_name": "ミスト化粧水"
    },
    {
        "url": "/winter-lotion",
        "file": "winter-lotion.html",
        "title": "💧 冬の乾きを満たす高保湿化粧水＆浸透ローション10選",
        "desc": "角層深くまでぐんぐん浸透してうるおいを抱え込む！イプサ、オルビスユードット、アクセーヌなど人気ローション。",
        "footer_name": "高保湿化粧水"
    },
    {
        "url": "/winter-cleansing",
        "file": "winter-cleansing.html",
        "title": "🫧 冬の粉吹き・つっぱりを防ぐ高保湿クレンジング＆濃密バーム10選",
        "desc": "落とすケアで差がつく！シュウウエムラ、DUO、ファンケルなど洗い上がりしっとり肌が続くクレンジング。",
        "footer_name": "クレンジング"
    },
    {
        "url": "/winter-day-cream",
        "file": "winter-day-cream.html",
        "title": "☀️ 暖房乾燥と冬紫外線をダブル遮断！一日中しっとり続く高保湿UV美容液＆朝用デイクリーム10選",
        "desc": "朝のひと塗りで一日中乾燥知らず！カネボウフレッシュデイクリーム、オルビス、ランコムなど朝用クリーム特集。",
        "footer_name": "朝用デイクリーム"
    },
    {
        "url": "/winter-moisture-cream",
        "file": "winter-moisture-cream.html",
        "title": "🧴 保湿力の強さで肌乾燥とさようなら！真冬の乾き知らず肌をつくる高保湿フェイスクリーム＆濃密バーム10選",
        "desc": "スキンケアの最後に極上のうるおい膜を！キュレル、キールズ、コスメデコルテなど夜の濃厚保湿クリーム。",
        "footer_name": "フェイスクリーム"
    },
    {
        "url": "/winter-serum-booster",
        "file": "winter-serum-booster.html",
        "title": "✨ ゴワつく冬の砂漠肌を即ほぐす！浸透力を底上げする高保湿・導入先行美容液＆ブースター10選",
        "desc": "硬くなった冬の角質層を柔らかくほぐし化粧水の入りを劇的アップ！コスメデコルテ、タカミ、ソフィーナなど。",
        "footer_name": "導入美容液"
    },
    {
        "url": "/winter-face-mask",
        "file": "winter-face-mask.html",
        "title": "🎭 水分爆弾で砂漠肌を即リセット！翌朝の化粧ノリ激変・高保湿シートマスク＆夜用パック10選",
        "desc": "週1〜2回の集中水分補給！メディヒール、ルルルン、トリデンなど暖房でしぼんだ肌をふっくら満たすシートマスク。",
        "footer_name": "シートマスク"
    },
    {
        "url": "/winter-eye-cream",
        "file": "winter-eye-cream.html",
        "title": "👁️ 暖房直撃の目元・ほうれい線をふっくら密着！乾燥小じわ撃退・高保湿アイクリーム＆リンクルケア10選",
        "desc": "皮膚の薄い目元・口元のちりめんジワを集中ケア！ポーラリンクルショット、エリクシールレチノパワーなど。",
        "footer_name": "アイクリーム"
    },
    {
        "url": "/winter-base-makeup",
        "file": "winter-base-makeup.html",
        "title": "💄 冬の暖房でもひび割れない！夕方まで潤いツヤが続く高保湿ファンデーション＆美容液下地10選",
        "desc": "カサつき・粉吹き・毛穴落ちを防ぎ一日中うるおい発光！資生堂、クレドポー、ランコムなど冬のベースメイク特集。",
        "footer_name": "ベースメイク総合"
    },
    {
        "url": "/winter-lip-care",
        "file": "winter-lip-care.html",
        "title": "🎁 冬のガサガサ皮剥けに終止符！高保湿リップトリートメント＆濃密ティント10選",
        "desc": "皮脂腺のない唇を乾燥冷風から守る！ラネージュスリーピングマスク、ディオールマキシマイザーなど。",
        "footer_name": "リップケア総合"
    },
    {
        "url": "/winter-body-care",
        "file": "winter-body-care.html",
        "title": "🛁 すねの粉吹き・全身の乾燥かゆみにサヨナラ！高保湿ボディミルク＆濃厚ボディバター10選",
        "desc": "お風呂上がりの全身をうるおいで包み込む！ニュートロジーナ、ニベア、キュレル、サボンなど厳選。",
        "footer_name": "ボディケア総合"
    },
    {
        "url": "/winter-hair-care",
        "file": "winter-hair-care.html",
        "title": "🌿 冬の静電気・毛先パサつきと完全決別！高保湿ヘアオイル＆濃厚ヘアマスク10選",
        "desc": "マフラー摩擦や暖房で傷んだキューティクルを補修。モロッカンオイル、ケラスターゼ、オルビスなど。",
        "footer_name": "ヘアケア総合"
    },
    {
        "url": "/winter-hand-care",
        "file": "winter-hand-care.html",
        "title": "🤲 手荒れ・あかぎれ・ささくれ知らずへ！神ハンドクリーム＆ネイルケア10選",
        "desc": "水仕事や冷風で荒れた手先を即効リペア。ベタつかないデスク用から夜の集中補修バームまで。",
        "footer_name": "ハンドケア総合"
    },
    {
        "url": "/summer-cosme",
        "file": "summer-cosme.html",
        "title": "☀️ 夏の汗・皮脂でも崩れない！最新トレンドコスメ厳選10選",
        "desc": "皮脂崩れ防止下地やウォータープルーフコスメなど夏特有の肌悩みを解決する特集。",
        "footer_name": "夏コスメ"
    }
]

footer_links_html = '<div class="footer-links">\n      <a href="/">トップページ</a>\n' + "\n".join([f'      <a href="{a["url"]}">{a["footer_name"]}</a>' for a in ALL_ARTICLES]) + '\n    </div>'

def update_links():
    for target_article in ALL_ARTICLES:
        file_path = target_article["file"]
        if not os.path.exists(file_path):
            continue
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 関連記事リスト構築（自分自身を除く）
        related_cards = []
        for a in ALL_ARTICLES:
            if a["file"] == target_article["file"]:
                continue
            related_cards.append(f"""        <a href="{a['url']}" class="related-link-card">
          <div class="related-link-title">{a['title']}</div>
          <div class="related-link-desc">{a['desc']}</div>
        </a>""")

        new_related_section = f"""<section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list">
{chr(10).join(related_cards)}
      </div>
    </section>"""

        # 既存の関連記事セクションの置換
        if '<section id="related"' in content:
            content = re.sub(r'<section id="related".*?</section>', new_related_section, content, flags=re.DOTALL)
        elif '<section id="related-hub"' in content:
            content = re.sub(r'<section id="related-hub".*?</section>', new_related_section, content, flags=re.DOTALL)
        elif '<section id="internal-links"' in content:
            content = re.sub(r'(<section id="internal-links".*?</section>)', r'\1\n\n    ' + new_related_section, content, flags=re.DOTALL)
        elif '</main>' in content:
            content = content.replace('</main>', '    ' + new_related_section + '\n  </main>')
        
        # フッターリンクの置換
        if '<div class="footer-links">' in content:
            content = re.sub(r'<div class="footer-links">.*?</div>', footer_links_html, content, flags=re.DOTALL)
        elif '<div class="footer-inner">' in content:
            content = re.sub(r'(<footer class="site-footer">\s*<div class="footer-inner">)', r'\1\n    ' + footer_links_html, content, flags=re.DOTALL)
        elif '<footer class="site-footer">' in content:
            content = re.sub(r'(<footer class="site-footer">\s*<div class="container">)', r'\1\n    ' + footer_links_html, content, flags=re.DOTALL)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Updated internal links and footer in: {file_path}")

    print("\nAll articles internal links updated successfully!")

if __name__ == "__main__":
    update_links()
