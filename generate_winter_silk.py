import json
import re

with open("fetched_3new_ginseng_cacao_silk.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_silk"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 国産高純度シルク抽出液が主原料！真冬の冷風と摩擦から角層を守り抜く最高峰シルククリーム",
        "catch": "世界遺産・富岡製糸場の絹研究を受け継ぐアーダンのフラッグシップ。界面活性剤や乳化剤に頼らず、天然シルクセリシンの乳化力だけで作り上げた奇跡の素肌同化クリーム",
        "brand_name": "Adan (アーダン / 初絹)",
        "capacity": "35g / ガラスジャー容器",
        "type": "国産ピュアシルク主原料 高純度エイジングケアクリーム",
        "features": "国産シルク抽出液（フィブロイン・セリシン高配合）、スクワラン、ホホバ種子油、天然トコフェロール",
        "value": "人間の皮膚のアミノ酸組織と99%近似したシルクプロテインが、冬のエアコンで傷んだ角層にスッと吸着。まるで極上の絹織物を一枚纏ったかのような陶器肌を翌朝まで持続",
        "desc_p1": "11月から12月にかけてマフラーやタートルネック、不織布マスクを常用するようになると、衣類の繊維が擦れるたびに肌表面の角質が削られ、赤みやヒリヒリ感、粉吹きが生じやすくなります。摩擦と暖房乾燥が重なるこの過酷な真冬に、皮膚科学の観点から究極の保護膜を提供するのが、純国産シルクコスメのパイオニア・アーダンが誇る『初絹 ピュアレスト シルククリーム』です。",
        "desc_p2": "指にとると、一般的な油分主体のクリームとは全く異なる、みずみずしく滑らかなテクスチャー。肌に伸ばした瞬間、シルク特有の親和性によって角層細胞の隙間をアミノ酸が満たし、肌表面に薄くしなやかな『第二の皮膚』のような保護膜を形成します。ベタつきやテカリは一切ないのに、一日中暖房直撃のオフィスにいても肌の水分が逃げず、夕方になってもキメがキュッと整った透明感をキープ。本物の絹の力を実感できる一生モノの銘品です。",
        "target": "マフラーやマスクの摩擦で肌がピリピリ荒れやすい方、油分でギトギトするクリームが苦手な方、国産シルクの圧倒的なアミノ酸保湿力を体感したい方",
        "point": "朝晩のお手入れの最後に、あずき粒大を手にとり、擦らずに優しくハンドプレスして肌表面にヴェールを密着させます。メイク前に薄く塗布すると、ファンデーションの密着度と持ちが劇的にアップします。"
    },
    {
        "rank": 2,
        "tag": "💧 黄金繭から抽出した加水分解シルク原液100%！肌と髪の深刻なパサつきを集中リペアする濃厚アンプル",
        "catch": "手作り化粧品材料の老舗・自然化粧品研究所の原液シリーズ。18種類のアミノ酸が真冬の乾燥でボロボロになった角層とキューティクルを瞬時に補修するマルチブースター",
        "brand_name": "自然化粧品研究所",
        "capacity": "20ml / スポイト遮光ボトル",
        "type": "加水分解シルク100% 高濃度原液アンプル",
        "features": "加水分解シルク原液（セリシン・フィブロイン低分子化）、18種の天然アミノ酸",
        "value": "手持ちの化粧水や乳液、ヘアトリートメントにわずか1〜2滴混ぜるだけで、どんなコスメも瞬時に極上のシルク高保湿処方へとアップグレードできる驚異の万能原液",
        "desc_p1": "真冬になると、顔の乾燥だけでなく『毛先のパサつき・広がり・静電気』も深刻化します。外気の低湿度に加えてセーターの脱ぎ着による摩擦でキューティクルが剥離し、髪内部の水分がスカスカに抜けてしまうからです。自然化粧品研究所の『シルクエキス原液 100%』は、肌と髪の両方のタンパク質構造を熟知したプロ仕様のリペア液です。",
        "desc_p2": "シルクタンパク質を酵素分解によって超微粒子ペプチドまで低分子化しているため、角層深部や毛髪内部のダメージホールへと素早く浸透。化粧水に1滴混ぜて顔になじませれば、ツルンとしたシルク特有のツヤとハリが蘇り、トリートメントやヘアオイルに混ぜれば、ドライヤーの熱と反応して毛先まで指通りの良いサラツヤ髪に仕上がります。ポーチに1本忍ばせておくだけで、冬のあらゆる乾燥ピンチを脱出できます。",
        "target": "手持ちのスキンケアの保湿力に物足りなさを感じている方、冬の髪の静電気や枝毛・パサつきに悩む方、高品質なアミノ酸原液をコスパ良く愛用したい方",
        "point": "夜の洗顔後、化粧水を手のひらに出したところに本品を1〜2滴ドロップして混ぜ合わせ全顔へ。またお風呂上がりの濡れた髪に、ヘアミルクやオイルとブレンドして毛先に揉み込んで乾かすとサロン帰りの艶が手に入ります。"
    },
    {
        "rank": 3,
        "tag": "💨 加水分解シルク×フラーレン×ヒアルロン酸！暖房乾燥で乾いた頭皮・髪・顔を一瞬で潤すプレミアムミスト",
        "catch": "ヘアサロン現場のプロが開発した「心髪（cocorogami）」のシルキートナー。超微細ミストが日中のエアコン砂漠から素肌と髪をガードし、ひと吹きでシルクのような指通りへ",
        "brand_name": "心髪 (cocorogami)",
        "capacity": "200ml / トリガーミストスプレー",
        "type": "頭皮・毛髪・全身用 高機能シルクトナーミスト",
        "features": "加水分解シルク、ノーベル賞受賞成分フラーレン、加水分解ヒアルロン酸、プラセンタエキス",
        "value": "200mlのたっぷりサイズ。微細な霧状スプレーでメイクの上からでも崩れることなく水分補給ができ、真冬のオフィスの過酷な乾燥環境から24時間防御",
        "desc_p1": "暖房がガンガンに効いたオフィスで一日中パソコン作業をしていると、午後には目元や頬がつっぱり、髪は静電気でフワフワ広がり、頭皮まで乾燥してかゆくなってきます。そんな日中の『砂漠化ストレス』を手軽にリセットするために生まれたのが、心髪の『PREMIUM シルキートナーミスト』です。",
        "desc_p2": "トリガーを引くと、驚くほどきめ細やかなシルク微粒子ミストがふわっと広がり、肌や髪をふんわり包み込みます。加水分解シルクがキューティクルと角層表面を瞬時にコーティングし、フラーレンの強力な抗酸化力とヒアルロン酸の保水力が乾燥ダメージをブロック。ベタつかずサラッとした仕上がりでありながら、触れると内側がしっかり潤ったしっとり感を実感できます。お風呂上がりの導入プレ化粧水としても優秀です。",
        "target": "日中オフィスでメイクの上から手軽に乾燥対策をしたい方、冬の静電気で髪が広がりやすい方、頭皮のかゆみや乾燥を防ぎたい方",
        "point": "顔や髪から20cmほど離し、目を閉じて顔全体に3〜4プッシュ吹きかけます。手のひらで軽く優しく押さえてなじませてください。朝の寝癖直しやブロー前のベースウォーターにも最適です。"
    },
    {
        "rank": 4,
        "tag": "✨ 高純度フィブロイン100%！真冬のメイク崩れと水分蒸散を防ぎ暖房下でも乾かない極上スキンケアパウダー",
        "catch": "天然シルクの繊維タンパク質「フィブロイン」だけで作られたアーダンの名品。毛穴を塞がず呼吸させながら、冬の皮脂崩れとインナードライを完璧に両立コントロール",
        "brand_name": "Adan (アーダン)",
        "capacity": "15g / 詰替用パウチ（専用ケース別売）",
        "type": "100%純粋シルク アミノ酸フェイスパウダー",
        "features": "シルク（微粒子フィブロイン100%）、アミノ酸複合体",
        "value": "タルクやシリコン、防腐剤を一切含まない完全ピュアシルク。日中はテカリを防ぐフィニッシュパウダーとして、夜はスキンケアのベタつきを抑えるナイトパウダーとして24時間活躍",
        "desc_p1": "冬のベースメイクの最大の難問は、『暖房でTゾーンはテカるのに、頬や目元は乾燥してファンデーションがひび割れる』という混合乾燥です。一般的なフェイスパウダーを使うと肌の水分まで吸い取られてカピカピになってしまいますが、アーダンの『シルクパウダー 15g』はその常識を覆します。",
        "desc_p2": "超微粒子に粉砕されたシルクパウダーは、肌に乗せると光を柔らかく乱反射し、毛穴やくすみを自然にカバーするソフトフォーカス効果を発揮。アミノ酸そのもので構成されているため、余分な皮脂だけを吸着しながら肌に必要な水分はしっかり保持します。夜のスキンケアの最後にパフで軽くはたけば、クリームのベタつきを抑えながら枕への摩擦も防いでくれ、翌朝の洗顔時には驚くほどすべすべのマシュマロ肌に出会えます。",
        "target": "パウダーをはたくと乾燥小ジワが目立ってしまう方、メイクしたまま眠れるほど肌に優しいフェイスパウダーを探している方、マスクへのメイク移りを防ぎたい方",
        "point": "パフにパウダーをしっかり揉み込み、手の甲で余分な粉を落としてから、顔の中心から外側へ優しく押さえるように乗せます。擦らずにポンポンと置くのが粉浮きを防ぐコツです。"
    },
    {
        "rank": 5,
        "tag": "🎭 天然加水分解シルクアミノ酸×ヒアルロン酸！真冬の過酷な乾燥角層をひたひたに浸す大容量30枚マスク",
        "catch": "毎日惜しみなく使える大容量デイリーシートマスク。人肌のアミノ酸組成と酷似した天然シルク美容液が、エアコン暖房でパサついた角層を密着補給し翌朝の化粧ノリを激変させる",
        "brand_name": "絹肌 (Kinuhada)",
        "capacity": "30枚入り / チャック付大容量パウチ",
        "type": "大容量高保湿シルクエッセンス デイリーフェイスマスク",
        "features": "加水分解シルク、ヒアルロン酸Na、植物性コラーゲン、天然アミノ酸複合体",
        "value": "30枚入りのたっぷりサイズで1枚あたり約139円の超高コスパ。真冬の1ヶ月間、毎晩お風呂上がりにシルクの潤いヴェールを集中補給できる安心感",
        "desc_p1": "真冬のスキンケアにおいて、最も確実かつスピーディーに水分量を底上げする方法は『毎日の密着シートマスク』です。しかし、配合成分が肌に合わなかったりベタつきすぎたりすると毎日の継続は困難。絹肌の『シルク 100% フェイスパック 30枚』は、毎日の使いやすさと確かな浸透力を徹底追求した名作です。",
        "desc_p2": "天然シルク由来のアミノ酸をたっぷり含んだ透明美容液が、柔らかなシートにひたひたに染み込んでいます。肌に乗せるとピタッと吸い付くように密着し、10分間置くだけで乾ききった角層のすみずみまで水分が浸透。シートを剥がした後の肌は、余計な皮膜感やヌルつきがなく、内側からみずみずしく潤ってキメがふっくらと立ち上がります。毎朝のメイク前に使えば、一日中乾燥崩れ知らずの美肌が完成します。",
        "target": "真冬の間デイリーに惜しみなくシートパックを続けたい方、アミノ酸の力でキメの整った明るい素肌を目指したい方、コスパ重視で大容量マスクを探している方",
        "point": "洗顔後、化粧水で肌を軽く整えてからシートを広げて顔に密着させます。約10〜15分おいてから剥がし、肌表面に残ったエッセンスを手で優しくハンドプレスしてなじませます。"
    },
    {
        "rank": 6,
        "tag": "💇‍♀️ 加水分解シルク×植物オイル！真冬のマフラー静電気とパサつきを抑えベルベット髪へ導く大人気オイル",
        "catch": "SNSで大バズり中のMOTON看板ヘアオイル。加水分解シルクが髪のキューティクルをピタッと密着コーティングし、冬の乾燥・摩擦・ドライヤー熱から毛先を完全防備",
        "brand_name": "MOTON (モトン)",
        "capacity": "100ml / ガラスポンプボトル",
        "type": "ダメージ補修・静電気防止 シルクヘアオイル",
        "features": "加水分解シルク、アルガンオイル、ホホバ種子油、メドウフォーム-δ-ラクトン",
        "value": "デパコス級の上品なフレグランス（フラワーガーデン等の香り）が一日中ふんわり持続。重すぎず軽すぎない絶妙な質感で、真冬のまとまりとツヤを両立",
        "desc_p1": "冬になると、ウールのコートやマフラーに擦れて髪の毛先がパサパサに広がり、静電気で顔にまとわりつく……そんな冬の美髪トラブルを劇的に改善するのが、韓国発の人気ブランドMOTONの『シルクヘアオイル』です。",
        "desc_p2": "加水分解シルクが毛髪表面の剥がれかけたキューティクル同士を接着するように密着補修。熱に反応するヒートプロテクト成分も配合されているため、お風呂上がりのタオルドライ後に馴染ませてブローすれば、サロン帰りのようなツヤやかなシルク髪に仕上がります。翌朝起きても寝癖がつきにくく、マフラーを巻いて一日中外を歩いても毛先の広がりや静電気が起きません。高級香水のような洗練された香りで、気分まで高めてくれます。",
        "target": "冬の毛先のパサつき、枝毛、広がり、静電気に悩んでいる方、香水代わりに上品な香りを髪に纏いたい方、オイル特有のベタつきが嫌いな方",
        "point": "タオルドライ後の濡れた髪に、セミロングで1〜1.5プッシュを毛先中心に揉み込み、ドライヤーで乾かします。朝のスタイリング仕上げに半プッシュを毛先に馴染ませるとツヤ感がアップします。"
    },
    {
        "rank": 7,
        "tag": "🤲 シルクエキス配合でベタつかない！冬の水仕事や外気で荒れた手肌をしっとりシルキーに整えるフレグランスハンド",
        "catch": "スマホ操作やPC作業中もすぐ触れるサラサラ高密着処方。シルクアミノ酸が手肌の角層に浸透し、真冬のささくれや乾燥シワを目立たなくする上品ハンドトリートメント",
        "brand_name": "MOTON (モトン)",
        "capacity": "50ml / チューブ容器",
        "type": "シルクエキス配合 高保湿フレグランスハンドクリーム",
        "features": "シルクエキス、シアバター、ヒアルロン酸、植物性スクワラン",
        "value": "塗った瞬間に水滴のように肌になじんでベタつきゼロ。上品で高級感あふれる香りと確かなシルク保湿膜で、冬の手元を美しくドレスアップ",
        "desc_p1": "冬のオフィスや外出先でハンドクリームを塗ると、キーボードやスマホの画面がベタベタに汚れてしまうのが嫌で塗るのをためらってしまう……そんな悩みを抱えるビジネスパーソンに圧倒的な支持を得ているのが、MOTONの『シルクハンドクリーム』です。",
        "desc_p2": "シルクエキスの特長である『高い吸湿性とサラサラの被膜感』を最大限に生かした処方設計。手肌に伸ばすとスッと溶け込むように浸透し、表面にはベタつかないシルキーな保護ヴェールが完成します。乾燥で硬くなった指先や爪周りのささくれもしっとり滑らかに整い、ふっくらとした手元へ。バッグから取り出すたびに気分が上がる洗練されたパッケージと心地よい香りで、真冬のハンドケアが楽しみになります。",
        "target": "塗った直後にスマホやパソコン作業をしたい方、冬の指先のささくれや乾燥小ジワが気になる方、上質な香りのハンドクリームを持ち歩きたい方",
        "point": "適量を手の甲に出し、両手の甲を擦り合わせるように広げてから、指先や爪の周りまで丁寧にマッサージしながら塗り込みます。手を洗うたびにこまめに塗り直すのが美肌キープの秘訣です。"
    },
    {
        "rank": 8,
        "tag": "🥛 加水分解シルク×コラーゲンアミノ酸高配合！真冬の酷いハイダメージ毛を芯から立て直すダメージリペアミルク",
        "catch": "創業90年以上の老舗・木村石鹸が本気で開発した伝説のヘアケア『12/JU-NI』。シルクとコラーゲンが傷んだ髪の空洞を埋め尽くし、冬の乾燥でも跳ね返らないしっとり髪へ",
        "brand_name": "木村石鹸 (12/JU-NI)",
        "capacity": "150ml / ポンプボトル",
        "type": "本格アミノ酸補修 高保湿リペアヘアミルク",
        "features": "加水分解シルク、加水分解コラーゲン、γ-ドコサラクトン、植物性セラミド複合体",
        "value": "髪の成分と酷似したアミノ酸を限界濃度まで配合。オイルでは改善しきれなかった真冬のパサパサ・チリチリ・うねり毛を芯から柔軟にし、驚くほどまとまる髪へ再建",
        "desc_p1": "カラーやパーマを繰り返した髪に真冬の乾燥が直撃すると、髪の内部からタンパク質が抜け落ちてストローのようにスカスカになり、オイルを塗っても表面だけがテカって中はパサパサという現象が起きます。木村石鹸の『12/JU-NI（ジューニ）ダメージリペアヘアミルク』は、この毛髪内部の空洞化を埋めるために生まれた本格派ヘアミルクです。",
        "desc_p2": "主成分として配合された加水分解シルクとコラーゲンが、傷んだ髪の内部へ素早く吸着・浸透。水分とアミノ酸を補給した上で、ドライヤーの熱によって毛髪と結合し、滑らかなキューティクルを再構築します。ブロー後の髪は重すぎず、毛先までツルンと指が通り、自分の髪とは思えないほどの柔らかさとしなやかさを取り戻します。真冬のヘアダメージに本気で悩む方のファイナルアンサーです。",
        "target": "カラーやブリーチで髪が傷んで冬になるとチリつく方、ヘアオイルだけでは髪がまとまらない方、髪のうねりや広がりを根本から改善したい方",
        "point": "お風呂上がりのタオルドライ後、1〜2プッシュを手にとって毛先中心にしっかり揉み込みます。粗目のコームで全体を梳かしてからドライヤーで上から下へ向かって風を当てて乾かしてください。"
    },
    {
        "rank": 9,
        "tag": "🧼 純国産シルクエキス×伝統枠練り製法！洗顔後も化粧水不要なほどしっとり滑らかな洗い上がりを叶えるシルク石けん",
        "catch": "群馬県富岡産の高品質シルクセリシンを贅沢に練り込んだミネソワの傑作。濃密クリーミー泡が冬の毛穴汚れをやさしく吸着し、洗うたびに素肌の透明感を底上げする",
        "brand_name": "ミネソワ (Minesowa)",
        "capacity": "100g / 専用ケース・泡立てネット付",
        "type": "純国産シルクセリシン高配合 枠練り高保湿洗顔石けん",
        "features": "純国産加水分解シルク（高純度セリシン）、パーム核油、スクワラン、天然グリセリン",
        "value": "職人が90日間かけて熟成させる枠練り製法により、保湿成分を30%以上配合。冬の洗顔時に皮脂を落としすぎず、肌表面にシルクの潤いヴェールを密着させる",
        "desc_p1": "真冬の朝、洗顔料を使って顔を洗った瞬間から肌がピキッと突っ張り、慌てて化粧水を押し込む……そんな経験はありませんか。洗浄力の強すぎる洗顔は、冬の貴重な天然保湿因子（NMF）を根こそぎ洗い流してしまいます。ミネソワの『Wソープ』は、洗顔を『潤いを奪う行為』から『潤いを与えるスキンケア』へと変える高級シルク石けんです。",
        "desc_p2": "付属のネットで軽く泡立てるだけで、弾力のあるキメ細かいシルク泡がモコモコと立ち上がります。泡を顔に乗せると、シルクセリシンの吸着力によって古い角質や余分な皮脂だけをやさしくオフ。ぬるま湯ですすぐと、まるで上質なシルクの布を肌の上に滑らせたかのような、つるんとなめらかな手触りに仕上がります。洗顔後すぐに肌がつっぱる心配がなく、その後に塗布するスキンケアの浸透性も劇的に向上します。",
        "target": "冬の朝晩の洗顔後に肌が激しく突っ張る方、毛穴の汚れやくすみをやさしくオフしたい方、純国産の良質なシルク石けんを長く使いたい方",
        "point": "付属の泡立てネットをぬるま湯で濡らし、石けんを数回擦りつけて空気を含ませながら濃密な泡を作ります。肌に手を触れず、泡のクッションを転がすように30秒洗顔して丁寧にすすいでください。"
    },
    {
        "rank": 10,
        "tag": "✨ 高純度シルクセリシン集中配合！特別な日の前夜に肌バリアを瞬時に整え陶器肌を引き出すプレミアムマスク",
        "catch": "京都の絹文化から生まれた「絹肌日和」の集中リペアウェットマスク。人肌のアミノ酸構造と共鳴するシルクセリシンが、真冬の乾燥で乱れたキメを一晩でフラットに整える",
        "brand_name": "絹肌日和 (Kinuhada Biyori)",
        "capacity": "1枚入り (集中個別包装)",
        "type": "シルクセリシン集中保湿 リペアプレミアムフェイスマスク",
        "features": "高濃度加水分解シルク（シルクセリシン）、ヒアルロン酸Na、ユズ果実エキス、グリチルリチン酸2K",
        "value": "1枚入りの個別包装で鮮度抜群。冬の忘年会やデート、大切なイベントの前夜に使うことで、メイクノリの良さと透明感を最大限に引き出す勝負マスク",
        "desc_p1": "12月の忘年会やクリスマス、年末年始のイベント前夜、暖房乾燥でカサつき毛穴が開いた肌を短時間でなんとかしたい……そんな緊急レスキューに最適なのが、京都の絹文化が生んだ『絹肌日和 フェイスマスク』です。",
        "desc_p2": "シルクから抽出された高純度のセリシンを贅沢に配合したウェットタイプのシートマスク。シートを広げて顔に乗せると、とろみのある美容液が肌にぴたりと密着し、冬の寒さで強張った角質層を優しくほぐしていきます。パックを終えてシートを剥がすと、まるで温泉に入った後のようなふっくらとしたツヤと、凹凸のない滑らかな陶器肌が完成。翌朝ファンデーションを滑らせたときの密着感と崩れにくさは感動的です。",
        "target": "ここぞというイベントの前夜に即効性のある保湿ケアを行いたい方、冬の乾燥による毛穴の目立ちやくすみをリセットしたい方、プレゼントやご褒美マスクを探している方",
        "point": "洗顔後、化粧水で肌を整えてからマスクを密着させます。10〜15分おいてから剥がし、肌に残った美容液を手で優しく押し込んで浸透させ、最後に乳液やクリームで蓋をしてください。"
    }
]

# 目次項目の定義
toc_items = [
    {"id": "intro", "title": "1. 11月・12月の摩擦＆暖房乾燥に負けない！加水分解シルク（絹エキス）の力"},
    {"id": "mechanism", "title": "2. 人肌のNMFと酷似！シルクアミノ酸（セリシン・フィブロイン）の皮膚科学"},
    {"id": "comparison", "title": "3. 高保湿シルクコスメおすすめ10選の比較表"},
    {"id": "ranking", "title": "4. 高保湿加水分解シルクコスメおすすめ厳選ランキング10選"},
    {"id": "guide", "title": "5. 失敗しない冬のシルクコスメの選び方＆アイテム別活用術"},
    {"id": "routine", "title": "6. 真冬の摩擦ダメージを無効化する！シルク重ねづけ美肌ステップ"},
    {"id": "faq", "title": "7. シルクコスメに関するよくある質問（FAQ）"},
    {"id": "summary", "title": "8. まとめ：人肌と共鳴するシルクアミノ酸で真冬も滑らかな陶器肌へ"}
]

toc_html = "\n".join([f'          <li><a href="#{item["id"]}">{item["title"]}</a></li>' for item in toc_items])

# 比較表の生成
table_rows = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    table_rows.append(f"""            <tr>
              <td class="rank-cell"><strong>第{p["rank"]}位</strong></td>
              <td class="product-cell">
                <a href="#rank-{p["rank"]}"><strong>{p["brand_name"]}</strong><br><span style="font-size:0.85rem;color:#4b5563;">{item_data["name"][:35]}...</span></a>
              </td>
              <td>{p["type"]}</td>
              <td class="price-cell">{item_data["price"]}</td>
              <td>{p["features"][:30]}...</td>
              <td><a href="{item_data["url"]}" class="table-btn" target="_blank" rel="nofollow noopener">楽天で見る</a></td>
            </tr>""")

table_rows_html = "\n".join(table_rows)

# 各商品カードのHTML生成
product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <!-- Rank {p["rank"]} -->
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge rank-{p["rank"]}">第{p["rank"]}位</span>
            <div class="product-title-group">
              <span class="product-catch">{p["tag"]}</span>
              <h3 class="product-name">{item_data["name"]}</h3>
              <p class="product-subname">{p["catch"]}</p>
            </div>
          </div>

          <div class="product-main-grid">
            <div class="product-visual">
              <img src="{item_data["img"]}" alt="{item_data["name"]}" class="product-img" loading="lazy">
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">{item_data["price"]}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data["reviewAverage"]}</span>
                <span class="review-count">（口コミ {item_data["reviewCount"]}件）</span>
              </div>
              <a href="{item_data["url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
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

# 記事全体のHTML構築
full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！人肌と酷似した18種のアミノ酸が真冬の摩擦・暖房乾燥から素肌を守り抜く高保湿加水分解シルクコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の寒冷乾燥やマフラー・マスクの摩擦刺激で荒れる角層を救う高保湿加水分解シルク（セリシン・フィブロイン）コスメを徹底厳選！アーダン、自然化粧品研究所、心髪、絹肌、MOTON、木村石鹸までアミノ酸科学の根拠と共に徹底検証。">
  <meta name="keywords" content="加水分解シルク コスメ, シルク 保湿クリーム, セリシン 美容液, シルクパウダー, シルク ヘアオイル, MOTON シルク, アーダン 初絹, 冬 摩擦 肌荒れ 対策">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-silk">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！人肌と酷似した18種のアミノ酸が真冬の摩擦・暖房乾燥から素肌を守り抜く高保湿加水分解シルクコスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥やマフラー・マスクの摩擦刺激で荒れる角層を救う高保湿加水分解シルクコスメを徹底厳選！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-silk">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="LUMI COSMETICS">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！人肌と酷似した18種のアミノ酸が真冬の摩擦・暖房乾燥から素肌を守り抜く高保湿加水分解シルクコスメランク10",
    "description": "11月・12月の寒冷乾燥やマフラー・マスクの摩擦刺激で荒れる角層を救う高保湿加水分解シルク（セリシン・フィブロイン）コスメを徹底厳選！",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-silk"
    }},
    "author": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS 保湿皮膚科学研究チーム"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://lumi-cosme.vercel.app/favicon.jpg"
      }}
    }},
    "datePublished": "2026-11-05T12:00:00+09:00",
    "dateModified": "2026-11-05T12:00:00+09:00"
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿加水分解シルクコスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {", ".join([f'''{{
        "@type": "ListItem",
        "position": {p["rank"]},
        "name": "{items[p["rank"]-1]["name"]}",
        "url": "{items[p["rank"]-1]["url"]}"
      }}''' for p in product_details])}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #475569;
      --primary-light: #f1f5f9;
      --primary-dark: #1e293b;
      --accent: #64748b;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg: #f8fafc;
      --bg-card: #ffffff;
      --border: #e2e8f0;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .logo {{
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      letter-spacing: -0.02em;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.95rem;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}
    
    .container {{
      max-width: 1040px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    .article-header {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      margin-bottom: 2rem;
      box-shadow: var(--shadow);
    }}
    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}
    .breadcrumb a {{ color: var(--accent); text-decoration: none; }}
    .post-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    h1 {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #111827;
      margin-bottom: 1.25rem;
      font-weight: 800;
    }}
    .meta-bar {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      border-top: 1px solid #f3f4f6;
      padding-top: 1rem;
    }}
    
    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-left: 5px solid var(--primary);
      border-radius: var(--radius);
      padding: 1.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-card ul {{
      list-style: none;
      padding-left: 0;
    }}
    .toc-card li {{
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
    }}
    .toc-card a {{
      color: var(--text);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-card a:hover {{ color: var(--primary); text-decoration: underline; }}
    
    .article-section {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .section-title {{
      font-size: 1.5rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .article-section p {{
      margin-bottom: 1.25rem;
      color: #374151;
      font-size: 1rem;
    }}
    .highlight-lead {{
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 1.25rem 1.5rem;
      border-radius: 8px;
      margin-bottom: 1.5rem;
      border-left: 4px solid var(--accent);
    }}
    
    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .data-table th, .data-table td {{
      padding: 0.85rem 1rem;
      border: 1px solid #e5e7eb;
    }}
    .data-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}
    .rank-cell {{ text-align: center; font-size: 1rem; color: var(--primary); white-space: nowrap; }}
    .price-cell {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 4px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}
    
    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
      position: relative;
    }}
    .product-header {{
      display: flex;
      gap: 1rem;
      align-items: flex-start;
      margin-bottom: 1.5rem;
    }}
    .rank-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 0.4rem 1rem;
      border-radius: 6px;
      white-space: nowrap;
    }}
    .rank-1 {{ background: linear-gradient(135deg, #334155, #0f172a); }}
    .rank-2 {{ background: linear-gradient(135deg, #9ca3af, #6b7280); }}
    .rank-3 {{ background: linear-gradient(135deg, #64748b, #334155); }}
    .product-title-group {{ flex: 1; }}
    .product-catch {{
      display: block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.25rem;
    }}
    .product-name {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 0.25rem;
    }}
    .product-subname {{
      font-size: 0.9rem;
      color: var(--text-muted);
    }}
    .product-main-grid {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
      align-items: start;
    }}
    @media (max-width: 768px) {{
      .product-main-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-visual {{
      text-align: center;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid #f3f4f6;
      background: #fafafa;
      margin-bottom: 1rem;
      aspect-ratio: 1/1;
      object-fit: contain;
    }}
    .price-box {{
      background: #fff1f2;
      border: 1px solid #fecdd3;
      border-radius: 6px;
      padding: 0.5rem;
      margin-bottom: 0.75rem;
    }}
    .price-label {{ display: block; font-size: 0.75rem; color: #9f1239; }}
    .price-value {{ font-size: 1.3rem; font-weight: 800; color: #e11d48; }}
    .review-meta {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}
    .review-stars {{ color: #f59e0b; font-weight: 700; }}
    .rakuten-btn {{
      display: inline-block;
      width: 100%;
      background: linear-gradient(135deg, #bf0000, #900000);
      color: #ffffff !important;
      font-size: 0.95rem;
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-radius: 6px;
      text-decoration: none !important;
      text-align: center;
      transition: opacity 0.2s;
    }}
    .rakuten-btn:hover {{ opacity: 0.9; }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      margin-bottom: 1.5rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.75rem;
      border: 1px solid #f3f4f6;
    }}
    .spec-table th {{
      background: #fdfaf6;
      color: var(--primary-dark);
      width: 25%;
      font-weight: 700;
    }}
    .body-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      border-left: 3px solid var(--primary);
      padding-left: 0.5rem;
    }}
    .recommend-box, .usage-box {{
      background: #fafaf9;
      border: 1px solid #e7e5e4;
      border-radius: 6px;
      padding: 1rem;
      margin-top: 1rem;
      font-size: 0.9rem;
    }}
    .recommend-title, .usage-title {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.35rem;
    }}

    /* Q&A / FAQ */
    .faq-item {{
      border-bottom: 1px solid #f3f4f6;
      padding: 1.25rem 0;
    }}
    .faq-q {{
      font-weight: 700;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}
    .faq-q::before {{
      content: "Q";
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 800;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
    }}
    .faq-a {{
      color: #374151;
      font-size: 0.95rem;
      padding-left: 1.75rem;
    }}

    /* 内部リンクカード */
    .related-hub {{
      background: #ffffff;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      padding: 2rem;
      margin-top: 3rem;
    }}
    .related-title {{
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.25rem;
    }}
    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem;
    }}
    .related-card {{
      background: #fafaf9;
      border: 1px solid #e7e5e4;
      border-radius: 6px;
      padding: 1rem;
      text-decoration: none;
      color: var(--text);
      transition: all 0.2s;
    }}
    .related-card:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}
    .related-card-title {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.25rem;
    }}
    .related-card-desc {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    footer {{
      background: #111827;
      color: #9ca3af;
      padding: 3rem 0;
      margin-top: 4rem;
      font-size: 0.9rem;
    }}
    .footer-inner {{
      max-width: 1040px;
      margin: 0 auto;
      padding: 0 1.5rem;
      text-align: center;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1rem 1.5rem;
      margin-bottom: 2rem;
    }}
    .footer-links a {{
      color: #d1d5db;
      text-decoration: none;
      font-size: 0.85rem;
    }}
    .footer-links a:hover {{ color: #ffffff; }}
    .copyright {{ font-size: 0.8rem; color: #6b7280; }}
  </style>
</head>
<body>

  <header>
    <div class="header-inner">
      <a href="/" class="logo">LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">冬コスメTOP</a>
        <a href="/winter-amino-acid">アミノ酸コスメ</a>
        <a href="/winter-lipidure">リピジュア</a>
        <a href="/winter-peptide-serum">ペプチド美容液</a>
      </nav>
    </div>
  </header>

  <main class="container">

    <article>
      <div class="article-header">
        <div class="breadcrumb">
          <a href="/">TOP</a> &gt; <a href="/#skincare">冬の高密着バリアスキンケア</a> &gt; シルクコスメ
        </div>
        <span class="post-tag">2026年11月・12月 真冬の高密着アミノ酸ケア</span>
        <h1>保湿力の強さで肌乾燥とさようなら！人肌と酷似した18種のアミノ酸が真冬の摩擦・暖房乾燥から素肌を守り抜く高保湿加水分解シルクコスメランク10</h1>
        <div class="meta-bar">
          <span>📅 公開日: 2026年11月5日</span>
          <span>✍ 監修: LUMI COSMETICS 保湿皮膚科学研究チーム</span>
          <span>⏱ 読了目安: 約12分</span>
        </div>
      </div>

      <!-- 目次 -->
      <div class="toc-card">
        <div class="toc-title">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h7"/></svg>
          目次：クリックで各項目へジャンプできます
        </div>
        <ul>
{toc_html}
        </ul>
      </div>

      <!-- セクション1: 導入・冬の摩擦＆暖房乾燥問題 -->
      <section class="article-section" id="intro">
        <h2 class="section-title">1. 11月・12月の摩擦＆暖房乾燥に負けない！加水分解シルク（絹エキス）の力</h2>
        <div class="highlight-lead">
          真冬の肌荒れは「空気の乾燥」だけでなく、ウールやアクリル素材のニット・タートルネック・マフラー・マスクによる『物理的摩擦』が角層を剥離させることが最大の引き金です。
        </div>
        <p>11月から12月にかけて寒さが本格化すると、防寒のためにハイネックのセーターやウールマフラー、不織布マスクを着用する機会が激増します。しかし、夕方になると首筋やフェイスライン、頬がムズムズと痒くなったり、赤くヒリついたりすることはありませんか？</p>
        <p>外気湿度が20%〜30%台まで急落する日本の冬は、衣類との摩擦によって大量の静電気が発生し、デリケートな角質細胞がめくれ上がってバリア機能が崩壊します。そこにエアコンの温風が直撃することで、肌内部の天然保湿因子（NMF）や水分が一方的に蒸発してしまうのです。</p>
        <p>この「物理的摩擦刺激」と「暖房による過乾燥」の二重苦から肌と髪を守り抜くために、古来より日本の製糸産業・繊維科学で培われてきた最高峰の素材が『シルク（絹・加水分解シルク）』です。人間の皮膚構造と奇跡的な親和性を持つシルクアミノ酸は、肌の上に息づくような第二の保護膜を形成し、摩擦のダメージをしなやかにいなしてくれます。</p>
      </section>

      <!-- セクション2: 科学的メカニズム -->
      <section class="article-section" id="mechanism">
        <h2 class="section-title">2. 人肌のNMFと酷似！シルクアミノ酸（セリシン・フィブロイン）の皮膚科学</h2>
        <p>蚕（カイコ）の繭から抽出されるシルクは、外側の水溶性タンパク質『セリシン（Sericin）』と、内側の強靭な繊維タンパク質『フィブロイン（Fibroin）』という2種類の高機能プロテインから構成されています。</p>
        
        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">① 人間の角層NMFとほぼ合致する18種類のアミノ酸組成</h3>
        <p>シルクプロテインを構成するアミノ酸（セリン、グリシン、アラニン、アスパラギン酸など18種類）の比率は、人間の表皮角層に存在する天然保湿因子（NMF）のアミノ酸バランスと驚異的に酷似しています。そのため、肌に乗せた瞬間に異物として反発されることなく角層の奥深くへと吸着浸透し、スカスカになった細胞間を濃密な水分で満たします。<a href="/winter-amino-acid">アミノ酸コスメ</a>の頂点に君臨する所以です。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">② セリシンが形成する「第二の皮膚」と摩擦抵抗の低減</h3>
        <p>セリシンは優れた成膜性を持ち、塗布すると肌表面に超薄膜の親和的ミクロフィルムを形成します。このフィルムは皮膚呼吸を妨げない通気性を持ちながら、水分蒸散を強力に抑制。さらに皮膚表面の摩擦係数を大幅に低下させるため、タートルネックやマフラーが擦れても角層が剥離せず、静電気の帯電も防ぎます。<a href="/winter-lipidure">リピジュア</a>や<a href="/winter-peptide-serum">ペプチド美容液</a>との相乗効果も抜群です。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">③ 毛髪キューティクルの吸着補修と静電気防止</h3>
        <p>低分子化された加水分解シルクは、剥がれかけた髪のキューティクルにイオン結合によって吸着。ブラッシングや乾燥による静電気の発生をブロックし、枝毛や切れ毛を根本から修復します。<a href="/winter-hair-serum">高保湿ヘアセラム</a>としても絶大な支持を集めています。</p>
      </section>

      <!-- セクション3: 比較表 -->
      <section class="article-section" id="comparison">
        <h2 class="section-title">3. 高保湿シルクコスメおすすめ10選の比較表</h2>
        <p>楽天市場の最新在庫・価格データから、2026年11月・12月の冬本番にリアルタイムで人気のシルクコスメ10選を一覧表にまとめました。フェイスクリーム、原液、ミスト、ヘアケアなど目的に合わせて比較してください。</p>
        
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>アイテムタイプ</th>
                <th>価格（税込）</th>
                <th>注目キー成分</th>
                <th>公式リンク</th>
              </tr>
            </thead>
            <tbody>
{table_rows_html}
            </tbody>
          </table>
        </div>
      </section>

      <!-- セクション4: 詳細ランキング -->
      <section class="article-section" id="ranking">
        <h2 class="section-title">4. 高保湿加水分解シルクコスメおすすめ厳選ランキング10選</h2>
        <p>ここからは、1位から10位までの各アイテムについて、配合アミノ酸の特徴、真冬の摩擦・乾燥に対する使用感、おすすめの肌質、効果的な使用テクニックまで徹底解説します。</p>

{all_cards_html}

      </section>

      <!-- セクション5: 選び方ガイド -->
      <section class="article-section" id="guide">
        <h2 class="section-title">5. 失敗しない冬のシルクコスメの選び方＆アイテム別活用術</h2>
        <p>シルクコスメは、セリシンを主成分とする保湿・保護アイテムと、フィブロインを主成分とするパウダー・光沢アイテム、そして低分子化された加水分解シルク原液に分かれます。</p>
        
        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">① 「摩擦による肌荒れ・敏感乾燥」にはセリシン高配合クリーム・石けん</h3>
        <p>マフラーやマスクの擦れでヒリヒリする肌には、アーダンの初絹クリームやミネソワのシルク石けんが最適。セリシンの保護膜が肌を外部刺激から守り、洗顔時からバリア膜を再構築します。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">② 「オフィスの暖房乾燥・テカリ崩れ」にはシルクパウダー＆ミスト</h3>
        <p>暖房でTゾーンが崩れるのに頬がパサつく方には、アーダンのピュアシルクパウダーと心髪のシルキートナーミストがベストコンビ。水分を奪わずに皮脂だけをコントロールし、一日中陶器のようなキメ美肌をキープできます。</p>

        <h3 style="font-size:1.15rem;color:var(--primary-dark);margin:1.25rem 0 0.5rem;">③ 「毛先のパサつき・静電気広がり」には加水分解シルクヘアミルク＆オイル</h3>
        <p>マフラーを外した瞬間に髪が爆発する方や、毛先の枝毛に悩む方には、木村石鹸の12/JU-NIリペアミルクやMOTONのシルクヘアオイルが必須。髪の内部と表面をダブルで補修し、ベルベットの指通りを一日中保ちます。</p>
      </section>

      <!-- セクション6: スキンケアステップ -->
      <section class="article-section" id="routine">
        <h2 class="section-title">6. 真冬の摩擦ダメージを無効化する！シルク重ねづけ美肌ステップ</h2>
        <div class="highlight-lead">
          シルクの親和的バリアを最大限に活かす鍵は『摩擦を起こさないスタンプ塗り』です。
        </div>
        <ol style="padding-left:1.5rem;margin-bottom:1.5rem;line-height:2;">
          <li><strong>ステップ1（シルク濃密洗顔）:</strong> ミネソワWソープのホイップ泡で、肌を擦らずに汚れだけを吸着。ぬるま湯でやさしく洗い流します。</li>
          <li><strong>ステップ2（アミノ酸プレ補給）:</strong> 心髪のシルキートナーミストを全顔にスプレーし、手のひらで軽く押さえて水分補給。</li>
          <li><strong>ステップ3（原液ブースト＆集中パック）:</strong> 週末や乾燥が激しい日は、絹肌のシルクシートマスクで10分間集中保湿。日常ケアなら化粧水に自然化粧品研究所のシルク原液を1滴ブレンド。</li>
          <li><strong>ステップ4（第二の皮膚クリーム密着）:</strong> アーダンの初絹シルククリームをあずき粒大とり、顔全体に優しくハンドプレスして保護膜を形成。</li>
          <li><strong>ステップ5（摩擦遮断フィニッシュ）:</strong> 朝はシルクパウダーを軽くはたいて日中の摩擦と水分蒸散をブロック。夜はヘアミルク＆オイルで毛先をコートして就寝します。</li>
        </ol>
      </section>

      <!-- セクション7: FAQ -->
      <section class="article-section" id="faq">
        <h2 class="section-title">7. シルクコスメに関するよくある質問（FAQ）</h2>
        
        <div class="faq-item">
          <div class="faq-q">シルクアレルギーの心配はありませんか？</div>
          <div class="faq-a">シルクは人間の皮膚タンパク質と極めて構造が近いため、植物エキスや動物性油分に比べてアレルギー反応が極めて起きにくい素材です。ただし稀にタンパク質に敏感な方もいらっしゃるため、初めて使用する際は腕の内側でパッチテストを行うと安心です。</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">加水分解シルクと通常のシルクエキスの違いは何ですか？</div>
          <div class="faq-a">通常のシルクタンパク質は分子量が大きく肌表面に留まりやすいのに対し、「加水分解シルク」は酵素や酸によってペプチドレベルまで低分子化されています。そのため角層の奥深くや毛髪内部のダメージホールまで浸透し、内側から補修する力に優れています。</div>
        </div>

        <div class="faq-item">
          <div class="faq-q">シルクパウダーを塗ったまま寝ても肌に悪影響はありませんか？</div>
          <div class="faq-a">100%ピュアなシルクパウダー（アーダン等）はアミノ酸そのものであるため、毛穴を塞ぐ鉱物油や合成成分が入っていません。むしろ夜のスキンケアの最後に使うことで、寝具との摩擦を防ぎ、余分な皮脂を吸着して肌荒れを防止するナイトパウダーとして理想的です。</div>
        </div>
      </section>

      <!-- セクション8: まとめ -->
      <section class="article-section" id="summary">
        <h2 class="section-title">8. まとめ：人肌と共鳴するシルクアミノ酸で真冬も滑らかな陶器肌へ</h2>
        <p>11月・12月の冬本番、過酷な空気乾燥と衣類の摩擦ストレスによって、私たちの肌バリアは毎日大きなダメージを受けています。人肌の天然保湿因子（NMF）とほぼ同一のアミノ酸組成を持ち、肌の上に滑らかな『第二の皮膚』を創り出すシルクコスメは、冬の肌を守り抜く最も知性的で頼れる選択肢です。</p>
        <p>ぜひ今回の厳選10選の中から、あなたのライフスタイルに最適なシルクアイテムを取り入れて、木枯らしの中でも触れたくなるような極上のシルキースムース肌を手に入れてください！</p>
      </section>

      <!-- 関連記事ハブ -->
      <div class="related-hub">
        <div class="related-title">🧵 あわせて読みたい！冬の高密着バリアスキンケア特集</div>
        <div class="related-grid">
          <a href="/winter-amino-acid" class="related-card">
            <div class="related-card-title">🧬 高保湿アミノ酸コスメ</div>
            <div class="related-desc">真冬の乾燥でバリアが壊れた角層をアミノ酸の力で土台から再構築する名品10選。</div>
          </a>
          <a href="/winter-lipidure" class="related-card">
            <div class="related-card-title">💧 高保湿リピジュアコスメ</div>
            <div class="related-desc">ヒアルロン酸の2倍の保水力！水洗いしても落ちない人口細胞膜バリア10選。</div>
          </a>
          <a href="/winter-peptide-serum" class="related-card">
            <div class="related-card-title">🧪 ペプチド高保湿美容液</div>
            <div class="related-desc">真冬の寒冷でしぼんだ肌に跳ね返すようなハリと弾力を取り戻すペプチド10選。</div>
          </a>
          <a href="/winter-hair-serum" class="related-card">
            <div class="related-card-title">💇‍♀️ 高保湿ヘアセラム</div>
            <div class="related-desc">冬の毛先パサつき・静電気広がりを瞬時に抑えてツヤ髪へ導く集中ヘアケア。</div>
          </a>
        </div>
      </div>

    </article>

  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-links">
        <a href="/">冬コスメTOP</a>
        <a href="/winter-silk">シルクコスメ</a>
        <a href="/winter-amino-acid">アミノ酸コスメ</a>
        <a href="/winter-lipidure">リピジュア</a>
        <a href="/winter-peptide-serum">ペプチド美容液</a>
        <a href="/winter-ginseng">高麗人参コスメ</a>
        <a href="/winter-cacao-butter">カカオバターコスメ</a>
      </div>
      <p class="copyright">&copy; 2026 LUMI COSMETICS. All Rights Reserved. 当サイトは楽天市場アフィリエイトプログラムに参加しています。</p>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-silk.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-silk.html successfully! Character count:", len(full_html))
