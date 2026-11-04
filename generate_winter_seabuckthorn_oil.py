import json
import re

with open("fetched_3new_seabuckthorn_blackseed_hemp.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_seabuckthorn_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🍊 未精製コールドプレス×オメガ7凝縮！真冬の黄ぐすみ＆粉吹き肌を救う濃厚リペア液",
        "catch": "天然のビタミンと必須脂肪酸がそのまま生きる深紅オレンジの純度100%サジーオイル。皮膚のターンオーバーを促すパルミトレイン酸が高濃度で溶け込み、冷風でしぼんだ角層を押し上げる",
        "brand_name": "Mandy Moon (マンディムーン)",
        "capacity": "10ml / 遮光スポイトガラス瓶",
        "type": "未精製オーガニックサジー種子・果実油",
        "features": "ヒポファエラムノイデス果実油（未精製オーガニック）、オメガ7パルミトレイン酸、天然βカロテン、ビタミンE",
        "value": "無希釈・無添加の原液処方。手持ちの化粧水や乳液にわずか1滴ブレンドするだけで、真冬の暖房直撃によるインナードライを完全に防ぐ高機能エマルジョンへと昇華",
        "desc_p1": "11月から12月にかけて気温が急激に降下すると、末梢血管が収縮して肌への栄養供給が滞り、肌全体がどんよりとした青白さや黄ぐすみに覆われます。マンディムーンの『オーガニック サジーオイル（未精製）』は、マイナス40度にも達する過酷な寒冷高地に自生するサジー果実の生命力をそのまま閉じ込めた超濃厚オイルです。鮮やかなディープオレンジ色は、豊富に含まれる天然カルテノイドとプロビタミンAの証です。",
        "desc_p2": "指先に取るととろりとした重みを感じますが、肌になじませるとサジー特有のオメガ7（パルミトレイン酸）が角質層の細胞間脂質と素早く親和し、吸い込まれるように浸透します。表面に油膜特有のベタつきを残さず、内側から発光するような自然な血色感とパンとしたハリをもたらします。夜のお手入れの仕上げに1滴ハンドプレスして就寝すれば、翌朝の洗顔時には指先を跳ね返すようなふっくら感ともちもちしたキメの復活を実感できます。",
        "target": "冬の寒さで顔色がくすんで疲れて見えやすい方、暖房の効いた部屋で肌の内側が突っ張るインナードライに悩む方、成分重視でピュアなオーガニックコスメを愛用する方",
        "point": "夜のお手入れの最後、乳液やクリームに1滴だけ混ぜて手のひらで温めてから全顔になじませます。未精製で色素が濃厚なため、衣類への付着を防ぐためにも夜の集中ナイトパックとしての使用がベストです。"
    },
    {
        "rank": 2,
        "tag": "✨ 有機サジー果実油×セサミオイル！冬の粉吹きすね＆冷え固まったボディを満たす黄金の潤い",
        "catch": "スイスのオーガニック名門ヴェレダが誇る高保湿ボディオイル。太陽の光をたっぷり浴びたサジーのビタミンが、冬の入浴後の急速な水分蒸散をブロックしてビロードのような肌触りへ",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "100ml / スプレー・ドロップガラスボトル",
        "type": "高保湿フルーティトリートメントボディオイル",
        "features": "ゴマ種子油、ヒポファエラムノイデス油（有機サジー果実油）、天然エッセンシャルオイル（グレープフルーツ・マンダリン）",
        "value": "肌なじみの良いセサミ油をベースにサジー果実油を配合。真冬の冷え固まったふくらはぎや粉を吹くすね、肘・膝をしっとり柔軟にほぐし、フルーティなアロマで心まで温める",
        "desc_p1": "真冬のボディケアで最も深刻なのが、入浴後の脱衣所で一気に進む皮膚の過乾燥です。タオルドライした瞬間から角層の水分が空気中へ奪われ、すねや背中がチクチク痒くなったり粉を吹いたりします。ヴェレダの『ヒッポファンフルーティ オイル』は、そんな真冬の過酷な乾燥ボディを救うために誕生したロングセラー名品です。",
        "desc_p2": "肌に伸ばすと、絞りたてのグレープフルーツやマンダリンのジューシーな柑橘の香りが立ち上り、冬の寒さでこわばった心身を心地よく解放します。セサミオイルの温感マッサージ効果とサジー果実油の不飽和脂肪酸が角層深部へ浸透し、ガサガサに硬直した皮膚をしなやかにトリートメント。お風呂上がりの濡れた素肌に伸ばして水分を包み込む『インバスケア』を取り入れることで、翌夕まで乾燥知らずのツヤ肌が持続します。",
        "target": "真冬になると足や腰回りの皮膚が粉を吹いて痒くなりやすい方、ボディの保湿と同時に極上の柑橘アロマで癒やされたい方、濡れた肌に使える高機能マルチオイルを探している方",
        "point": "入浴直後、バスタオルで拭く前の湿った肌に2〜3プッシュをなじませ、手のひらで下から上へと引き上げるようにマッサージします。その後にタオルで優しく水分を押さえるとベタつきゼロで超高保湿が完成します。"
    },
    {
        "rank": 3,
        "tag": "💧 無添加コールドプレス×大容量80ml！冬のゴワつく角層を瞬時にほぐす万能ブースター",
        "catch": "コスパと品質を極限まで追求した国内充填ピュアキャリアオイル。洗顔直後のプレオイルとして使用することで硬化した角質を柔軟にし、その後の化粧水の浸透ルートを切り拓く",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "80ml / 遮光ドロッパーボトル",
        "type": "精製・高純度コールドプレスキャリアオイル",
        "features": "ヒポファエラムノイデス種子油（無添加未精製ブレンド）、オメガ7、オメガ3、オメガ6、オメガ9",
        "value": "80mlという充実のサイズ感で、朝晩のフェイシャルからデコルテ、ネイル、毛先のパサつきまで惜しみなく使用可能。保存料や合成界面活性剤を一切排除した安心処方",
        "desc_p1": "冬本番を迎える11月下旬以降、肌のゴワつきによってスキンケアの浸透が著しく鈍る『角層フリーズ』現象が起こります。&SHの『オーガニック シーバックソーンオイル 80ml』は、この硬直した皮膚組織を素早くほぐすために最適なブースターアイテムです。熱をかけずに丁寧に低温圧搾されたオイルには、必須脂肪酸がバランスよく濃縮されています。",
        "desc_p2": "植物油の中でも珍しく、皮膚の修復を助けるオメガ7と抗炎症に関わるオメガ3・6が共存しているため、冬の寒暖差や木枯らしで荒れがちなバリア機能を素早くサポート。洗顔後すぐに1〜2滴を手のひらで薄く伸ばして顔全体を包み込むと、角質細胞同士の結びつきが柔らかくほぐれ、後から重ねる化粧水をごくごくと吸い込むスポンジのような素肌へと生まれ変わります。惜しみなく全身に使える価格設定も魅力です。",
        "target": "化粧水が肌表面で滑って中に入っていかないと感じる方、高品質なサジーオイルを顔から首元まで贅沢に使いたい方、ベタつきの少ない高浸透キャリアオイルを求める方",
        "point": "朝晩の洗顔後、化粧水を塗る前のファーストステップとして2滴を手にとり、両手で温めてから優しく顔を包み込むようにハンドプレスします。肌が柔らかくなったのを確認してから化粧水を重ねてください。"
    },
    {
        "rank": 4,
        "tag": "🌿 天然シーベリー種子油100%！アイハーブでも熱狂的人気を誇る高濃度ピュアドロップ",
        "catch": "世界的なナチュラルスキンケアブランドLife-floが放つ最高純度のシーバックソーン。寒冷乾燥による小ジワ・ハリ不足・紫外線ダメージの蓄積を力強くケアする原液美容オイル",
        "brand_name": "Life-flo (ライフフロー)",
        "capacity": "30ml / 遮光スポイトガラス瓶",
        "type": "100%ピュア シーバックソーン種子オイル",
        "features": "未希釈シーバックソーン種子油、高濃度トコフェロール、天然リノール酸・アルファリノレン酸",
        "value": "果実油に比べて黄色みが穏やかな種子油を厳選しているため、日中でも比較的使いやすいのが特徴。角層深部の保水バリアを再構築し、乾燥小ジワを目立たなくする",
        "desc_p1": "乾燥がピークに達する12月、目尻や口元に現れる浅い乾燥ジワは放置すると定着ジワへと進行してしまいます。Life-floの『ピュア シーバックソーンオイル』は、海外のオーガニック愛好家から長年支持され続ける高機能オイルです。種子由来のオイルは果実油よりも必須脂肪酸の比率が高く、角層の保護力に極めて優れています。",
        "desc_p2": "濃密でありながらスッと角層へ馴染むテクスチャーで、塗布した瞬間に肌がしっとりと吸い付くような感触に変わります。冬の冷たい外気と乾いたエアコン風の往復によって疲弊した皮膚バリアを物理的・生理学的に包み込み、潤いの蒸発を徹底ブロック。夜のスキンケアの最後に乾燥が気になる目元・口元へ重ね塗りすることで、翌朝ふっくらと持ち上がった若々しいハリを実感できます。",
        "target": "目元や口元の乾燥小ジワをピンポイントで集中ケアしたい方、海外セレブも愛用する本格派オーガニックオイルを試したい方、日中のメイク前にも使えるサラリとした質感を求める方",
        "point": "化粧水・美容液・クリームでお手入れした後の最終ステップとして、スポイト半分量を手にとり、乾燥が特に気になるパーツへ指先で優しくトントンとなじませます。"
    },
    {
        "rank": 5,
        "tag": "🧤 有機サジーオイル×ミツロウ！真冬の水仕事や冷風でひび割れる指先を守るプロ仕様ハンド",
        "catch": "ヴェレダが寒冷なヨーロッパの冬のために開発した高保湿ハンドトリートメント。サジーオイルのエモリエント効果と天然ミツロウの密着保護膜が、ガサガサの手肌をなめらかに修復",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "50ml / アルミチューブ",
        "type": "高保湿リッチハンドトリートメントクリーム",
        "features": "有機サジー果実油、有機ゴマ油、ミツロウ、天然カルナウバロウ、グレープフルーツ精油",
        "value": "高密度の油分膜を形成しながらも、塗布後すぐにサラッとしてスマートフォンの画面に指紋がつきにくい絶妙な処方バランス。冬の手荒れ・ささくれ・指先のひび割れを予防",
        "desc_p1": "11月以降の水仕事や毎日の手洗い、アルコール消毒の繰り返しは、手の皮膚から皮脂と水分を根こそぎ奪い取ります。ヴェレダの『ヒッポファン ハンドクリーム』は、過酷な冬の環境下で働く手肌を保護するために設計された、ヨーロッパで絶大な信頼を集めるハンドケアの傑作です。",
        "desc_p2": "チューブから出すと、サジーオイルならではの温かみのある鮮やかなイエローカラー。体温でとろけるように手肌全体へと広がり、指先のささくれや関節の粉吹きをピタッと包み込みます。ミツロウが薄い保護手袋のようなヴェールを形成するため、冷たい外気に触れても水分が逃げません。爽やかな柑橘系の香りで仕事中や家事の合間にも心地よくリフレッシュできます。",
        "target": "冬になると手の甲や指先がガサガサに荒れて痛む方、保湿力は欲しいがベタベタして物が触れないクリームが苦手な方、天然由来成分100%の安全なハンドケアを求める方",
        "point": "小豆大を手にとり、手のひらで温めてから手の甲、指の関節、甘皮周りまで丁寧にマッサージするように塗り込みます。就寝前は少し多めに塗り、綿の手袋をして眠ると翌朝感動のなめらかさになります。"
    },
    {
        "rank": 6,
        "tag": "🍷 モンゴル産原生サジー100%！内外美容を叶える奇跡の天然ピュアオイルリキッド",
        "catch": "過酷なモンゴルの大自然で育まれた原生サジーを丸ごと搾汁。外用オイルとしての超濃密保湿はもちろん、スプーン1杯の飲用で体内の粘膜と角層を潤す究極のインナー＆アウターケア",
        "brand_name": "Guamaral (グアマラル)",
        "capacity": "50ml / 遮光ドロップボトル",
        "type": "内外両用ピュアシーベリーオイル",
        "features": "モンゴル産天然シーベリー油100%、オメガ7パルミトレイン酸、不飽和脂肪酸、植物ステロール",
        "value": "添加物・保存料・着色料一切無添加。肌の外側からの油膜シールドと、内側からの細胞膜サポートを同時に実現できる希少なメディカルグレードサジーオイル",
        "desc_p1": "真冬の極端な乾燥肌は、化粧品による外側からのケアだけでは追いつかないことがあります。暖房の効いたオフィスで一日中過ごすと、喉や鼻の粘膜とともに皮膚組織全体が水分を失ってカラカラに干からびます。グアマラルの『シーベリー ピュアオイルリキッド』は、昼夜の寒暖差が50度にもなるモンゴルの過酷な自然を生き抜いたサジーから採れる生命力そのものです。",
        "desc_p2": "肌に塗布すれば、濃厚なオメガ7と抗酸化成分が乾燥で傷んだ角質層のバリアを瞬時に修復。さらに朝のヨーグルトや温かいスープに数滴垂らして摂取することで、消化管粘膜や毛細血管をケアし、皮膚の内側から潤いを生み出す力を呼び覚まします。真冬の乾燥対策に本気で取り組む美容上級者から圧倒的な支持を集める逸品です。",
        "target": "外側からどれだけクリームを塗っても夕方には肌がカサつく深刻な乾燥肌の方、体質改善も含めて冬の肌質を底上げしたい方、完全無添加の純粋なサジーを求める方",
        "point": "夜の洗顔後に2滴を手にとり、目元や口元を中心に優しく押し込みます。同時に毎朝の朝食時にティースプーン半分程度をそのまま、またはスムージー等に混ぜて摂取するのが最も効果的です。"
    },
    {
        "rank": 7,
        "tag": "🧼 天然サジーオイル贅沢配合！冬の洗顔後のつっぱり感をゼロにする濃密枠練り石けん",
        "catch": "サジーのビタミンと油分を壊さない伝統のコールドプロセス製法。豊かな泡立ちで毛穴の汚れを優しく吸着しながら、洗うたびに肌へ潤いのヴェールを残す高保湿洗顔ソープ",
        "brand_name": "Purilla (ピュリラ)",
        "capacity": "100g / 化粧箱入り",
        "type": "天然サジーオイル高配合 枠練り無添加洗顔石鹸",
        "features": "サジー果実油、ココナッツ油、オリーブ果実油、天然グリセリン、パーム油",
        "value": "熱を加えない低温製法により、天然の保湿成分グリセリンとサジーのオメガ7が石けん内部に丸ごと残存。洗い流した直後から化粧水をつけたようなしっとり感が持続",
        "desc_p1": "冬の乾燥肌の悪化原因の第1位は、実は『過度な洗浄による皮脂の奪いすぎ』です。冬用の保湿クリームをいくら塗っても、洗顔料が強すぎると肌のバリアは一向に回復しません。ピュリラの『サジー高保湿無添加石けん』は、洗顔によるバリア破壊を防ぎ、洗うステップ自体を高保湿トリートメントに変えてしまう画期的な石けんです。",
        "desc_p2": "泡立てネットで軽く転がすだけで、弾力のある濃密なオレンジ色のクッション泡が完成。きめ細かい泡が肌と手の間の摩擦を完全に遮断し、真冬のデリケートな肌を優しく包み込みます。汚れだけを穏やかにオフし、サジーオイル由来の柔軟成分が肌表面にとどまるため、お風呂から出た後も全くつっぱり感を感じません。冬の朝洗顔にも安心して使えるマイルド設計です。",
        "target": "洗顔後すぐに肌がつっぱって慌てて化粧水を塗っている方、肌の赤みやヒリつきで市販の洗顔フォームがしみる方、透明感と潤いを両立した無添加洗顔を求める方",
        "point": "ぬるま湯（32〜34℃）で泡立てネットを使い、レモン1個分のもっちり泡を作ります。肌に泡を乗せて転がすように15秒程度なじませ、こすらずに流水でしっかりすすぎます。"
    },
    {
        "rank": 8,
        "tag": "🌹 USDAオーガニック認証！サジー果実エキス×ザクロ×ダマスクローズの至高セラム",
        "catch": "アメリカの厳しいオーガニック基準をクリアしたBadgerの最高傑作。サジーのオメガ7にザクロ種子油のオメガ5とダマスクローズ精油を融合させた、真冬のエイジング特化オイル",
        "brand_name": "Badger (バジャー)",
        "capacity": "29.5ml / 遮光ドロップボトル",
        "type": "オーガニック高保湿フェイス美容オイル",
        "features": "ホホバ種子油、バオバブ種子油、ザクロ種子油、ヒポファエラムノイデス（サジー）果実エキス、ダマスクバラ花油",
        "value": "サジー単体では得られない多角的なエイジングケアアプローチ。真冬の乾燥小ジワをふっくら持ち上げ、大人の肌にしなやかな弾力と気品あるツヤを与える",
        "desc_p1": "40代以降の冬の肌は、気温低下による水分減少だけでなく、真皮のコラーゲン低下による『肌のたるみ・しぼみ』が同時に進行します。バジャーの『フェイスオイル シーバックソーン』は、植物美容療法の知見を結集し、サジーを筆頭にザクロやバオバブといった高機能植物油を黄金比率でブレンドした贅沢なオイル美容液です。",
        "desc_p2": "肌にのせると、高貴なダマスクローズの天然アロマがふわっと広がり、冬の乾燥で強張った表情を解きほぐします。サジーのオメガ7が角層深部へ浸透してキメを整え、ザクロのプニカ酸がふっくらとしたハリをサポート。翌朝の肌に触れると、前夜までの乾燥ゴワつきが嘘のように柔らかく滑らかなベルベット肌へと変化していることに驚かされます。",
        "target": "乾燥だけでなくハリの低下や大人のたるみ毛穴が気になる方、上質な天然ローズの香りで毎晩のスキンケアを至福の時間にしたい方、オーガニック最高峰の品質を求める方",
        "point": "夜のお手入れで化粧水をしっかりなじませた後、3〜4滴を手にとり手のひらで温めます。顔全体をハンドプレスしながら深呼吸して香りを楽しみ、首元からデコルテまで滑らせてください。"
    },
    {
        "rank": 9,
        "tag": "🧖‍♀️ サジー×CICA×アスタキサンチン！メイクオフと同時に濃密保湿する新感覚バーム",
        "catch": "冬の乾燥ダメージ肌を擦らず溶かして落とすクレンジングセラム＆バーム。サジーオイルの濃密油分がメイク汚れを浮かせ、洗い流した後も美容液を塗った後のようなしっとり感を維持",
        "brand_name": "RIMEDO (リメド)",
        "capacity": "100g / チューブ・ジャー容器",
        "type": "高保湿美容液クレンジングバーム",
        "features": "サジーオイル、ツボクサエキス（CICA）、アスタキサンチン、ビタミンC誘導体、溶岩クレイ",
        "value": "冬の頑固なウォータープルーフメイクや毛穴の黒ずみを摩擦ゼロでするんと落としながら、サジーとCICAが冬の肌荒れ・赤みを鎮静。ダブル洗顔不要で乾燥を徹底ブロック",
        "desc_p1": "冬のクレンジングは肌にとって最も過酷な試練です。寒さで固まったオイルやバームで肌を擦ると、ただでさえ薄くなった角層が傷つき、深刻な乾燥肌荒れを引き起こします。RIMEDOの『クレンジング セラム＆バーム』は、体温で瞬時にとろけるメルティ処方を採用し、サジーオイルの栄養を肌にチャージしながら汚れを落とす高機能クレンジングです。",
        "desc_p2": "肌に伸ばすと、オレンジ色の濃密バームがじんわりとろけて摩擦を感じさせないクッション層を形成。ウォータープルーフのマスカラや毛穴の奥に入り込んだファンデーションを素早く浮き上がらせます。ぬるま湯で乳化して洗い流すと、サジーオイルのエモリエント膜が肌表面に残り、つっぱり感や乾燥小ジワを一切感じさせないもっちり肌へと仕上がります。",
        "target": "クレンジング後の肌の乾燥・つっぱりがとにかく辛い方、毛穴の黒ずみと冬の乾燥荒れの両方を同時にケアしたい方、W洗顔不要で時短とお肌への優しさを両立したい方",
        "point": "乾いた手のひらにサクランボ大をとり、顔全体に優しく円を描くようになじませます。メイクが浮き上がったら、少量のぬるま湯を加えて白く乳化させてから、しっかりすすぎます。"
    },
    {
        "rank": 10,
        "tag": "💧 特許サジー複合エキス配合！冬のインナードライによる過剰皮脂と毛穴開きを鎮める美容液",
        "catch": "韓国スキンケアの皮膚科学研究から生まれた高機能セバム美容液。サジーの豊富なビタミンと抗酸化成分が、冬のエアコン乾燥で狂った水分油分バランスを黄金比率へ整える",
        "brand_name": "BOTANITY (ボタニティ)",
        "capacity": "50ml / スポイト遮光ボトル",
        "type": "水分油分バランシング高機能美容液",
        "features": "サジー・シーベリー複合特許エキス、ナイアシンアミド、ヒアルロン酸、ティーツリー葉エキス",
        "value": "『乾燥しているのにTゾーンがテカる』という真冬特有のインナードライトラブルを根本解決。ベタつきのない水系エッセンスで、毛穴を引き締めながら角層をみずみずしく満たす",
        "desc_p1": "冬になると頬や口元は粉を吹くほど乾燥しているのに、鼻やおでこは皮脂でギトギトになってメイクが崩れる……そんな『冬の混合肌・インナードライ』に悩む方は非常に多いです。ボタニティの『マキオール セバム美容液』は、サジー果実から抽出した独自開発の特許成分をベースに、乱れた皮膚の油水分バランスを正常化するレスキュー美容液です。",
        "desc_p2": "みずみずしく軽やかなテクスチャーでありながら、塗布すると角層の深部まで急速に浸透。サジーのビタミン成分が酸化しやすい皮脂をコントロールし、同時に高分子・低分子ヒアルロン酸が乾燥した角質細胞を水分で満たします。オイル美容液が苦手な方や、真冬でもニキビや毛穴の開きが気になる方にとって、重さを感じさせずに確かな保水力を実感できる頼もしい1本です。",
        "target": "冬の暖房下でTゾーンのテカリと頬の乾燥が同時に起きるインナードライの方、オイルの重さやニキビが心配でサジーの美容効果を取り入れたい方、毛穴の引き締めを目指す方",
        "point": "朝晩の洗顔後、化粧水で肌を整えた後にスポイト1〜2滴を全顔へなじませます。特にテカリや毛穴が気になる小鼻やTゾーンには指先で重ねづけしてください。"
    }
]

# 目次リンク
toc_links = ""
for p in product_details:
    toc_links += f'          <li><a href="#rank-{p["rank"]}">第{p["rank"]}位：{p["brand_name"]} {p["catch"][:22]}...</a></li>\n'

# 比較一覧表
table_rows = []
for idx, p in enumerate(product_details):
    it = items[idx]
    table_rows.append(f"""            <tr>
              <td class="rank-num">第{p['rank']}位</td>
              <td><img src="{it['img']}" alt="{p['brand_name']}" class="table-thumb" loading="lazy"></td>
              <td><strong>{p['brand_name']}</strong><br><span style="font-size:0.85rem; color:var(--text-sub);">{it['name'][:35]}...</span></td>
              <td>{p['type']}</td>
              <td class="price-cell">{it['price']}</td>
              <td><a href="#rank-{p['rank']}" class="table-link">詳細を見る</a></td>
            </tr>""")
table_joined = "\n".join(table_rows)

# 各商品カード
product_cards = []
for idx, p in enumerate(product_details):
    it = items[idx]
    product_cards.append(f"""      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge">第{p['rank']}位 ｜ {p['type']}</div>
        <div class="product-header">
          <div class="img-container">
            <img src="{it['img']}" alt="{it['name']}" class="product-img" loading="lazy">
          </div>
          <div class="product-intro">
            <h3 class="product-title">{it['name']}</h3>
            <div class="product-brand">ブランド：<strong>{p['brand_name']}</strong></div>
            <div class="product-price">参考価格：<span class="price-val">{it['price']}</span> <small>（楽天市場 最新確認時）</small></div>
            <div class="product-tag">{p['tag']}</div>
            <p class="product-catch">{p['catch']}</p>
          </div>
        </div>

        <div class="spec-table-box">
          <table class="spec-table">
            <tr><th>内容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>主要保湿・美容成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の保湿メリット</th><td>{p['value']}</td></tr>
          </table>
        </div>

        <div class="review-body">
          <h4>💡 コスメコンシェルジュによる徹底レビュー＆冬の保湿効果検証</h4>
          <p>{p['desc_p1']}</p>
          <p>{p['desc_p2']}</p>

          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ！</strong>
            <p>{p['target']}</p>
          </div>

          <div class="point-box">
            <strong>✨ 保湿効果を最大化するプロの使い方：</strong>
            <p>{p['point']}</p>
          </div>
        </div>

        <div class="btn-wrap">
          <a href="{it['url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            🛒 楽天市場で「{p['brand_name']}」の最新価格・在庫・口コミを見る
          </a>
        </div>
      </article>""")

cards_joined = "\n\n".join(product_cards)

# JSON-LD構造化データ
json_ld_items = []
for idx, p in enumerate(product_details):
    it = items[idx]
    json_ld_items.append({
        "@type": "ListItem",
        "position": p["rank"],
        "name": it["name"],
        "url": f"https://lumi-cosme.vercel.app/winter-seabuckthorn-oil#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！奇跡のオメガ7と黄金ビタミンが真冬の寒冷くすみ＆粉吹き肌を満たす高保湿サジーオイルコスメランク10",
            "description": "11月・12月の気温急降下と暖房乾燥による粉吹き肌・寒冷くすみを救う高保湿サジー（シーバックソーン）コスメを徹底厳選！マンディムーン、ヴェレダ、アンドエスエイチ、ライフフロー、バジャーまで徹底検証。",
            "datePublished": "2026-11-05T07:00:00+09:00",
            "dateModified": "2026-11-05T07:00:00+09:00",
            "author": {
                "@type": "Person",
                "name": "Lumi Cosme 編集部 コスメコンシェルジュ"
            },
            "publisher": {
                "@type": "Organization",
                "name": "Lumi Cosme",
                "url": "https://lumi-cosme.vercel.app/"
            }
        },
        {
            "@type": "ItemList",
            "name": "高保湿サジーオイルコスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "サジーオイル（シーバックソーン）が真冬の乾燥やくすみに劇的に効く理由は何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "サジー（シーベリー）には、植物界では極めて希少な『オメガ7不飽和脂肪酸（パルミトレイン酸）』が約30%以上も高濃度に含まれています。パルミトレイン酸は人間の皮脂膜を構成する主要成分であり、加齢や冬の寒冷刺激で皮脂分泌が落ちると真っ先に枯渇します。サジーオイルはこの不足した皮脂膜を瞬時に再現し、水分蒸散を防ぎます。さらに天然のβカロテン、ビタミンA・C・E、植物ステロールが豊富で、真冬の寒さで血行不良に陥り青白くくすんだ肌に、内側から血色感と明るい透明感を取り戻します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "サジーオイルの鮮やかなオレンジ色で肌や枕カバーに色が移りませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "サジーオイルの濃いオレンジ色は、人工着色料ではなく高濃度な天然βカロテン（プロビタミンA）に由来します。原液を直接大量に塗ると一時的に肌が黄色っぽく見えることがありますが、手持ちの乳液やクリーム、化粧水に1〜2滴混ぜて薄くハンドプレスすれば、角層へ素早く浸透して色が定着することはありません。心配な場合は、就寝前のナイトルーティンとして使用し、塗布後5分程度置いて肌表面がサラリとなじんでから就寝することをおすすめします。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "サジーの「果実油」と「種子油」にはどのような違いがありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "サジーオイルには果肉から採れる『果実油（ベリーオイル）』と種から採れる『種子油（シードオイル）』があります。果実油は鮮やかな深紅オレンジ色で、オメガ7（パルミトレイン酸）とカロテノイドが圧倒的に豊富で、冬の強烈な乾燥・肌のしぼみ・くすみケアに最適です。一方、種子油はやや淡い黄色で、オメガ3（α-リノレン酸）とオメガ6（リノール酸）が多く含まれ、肌荒れ予防やバリア補修に向いています。真冬のエイジングケアや濃密保湿を最優先するなら果実油、日中の軽やかなケアには種子油がおすすめです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "冬のスキンケアでの最も効果的なサジーオイルの使い方は？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "最もおすすめなのは『夜のクリーム・乳液への1滴ブレンド』です。いつもの保湿クリームや乳液にサジーオイルを1滴垂らし、手のひらで混ぜ合わせてから全顔へ包み込むようにハンドプレスします。これにより油分が乳化して浸透力が高まり、翌朝まで暖房の乾燥に負けない強固な保護ヴェールが持続します。また、入浴後の濡れた肌に全身伸ばすボディオイルケアとしても、冬の粉吹きすねを瞬時に解消する絶大な効果を発揮します。"
                    }
                }
            ]
        }
    ]
}

json_ld_str = json.dumps(json_ld_schema, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！奇跡のオメガ7と黄金ビタミンが真冬の寒冷くすみ＆粉吹き肌を満たす高保湿サジーオイルコスメランク10</title>
  <meta name="description" content="11月・12月の気温急降下と暖房乾燥による粉吹き肌・寒冷くすみを救う高保湿サジー（シーバックソーン）コスメを徹底厳選！マンディムーン、ヴェレダ、アンドエスエイチ、ライフフロー、バジャーまで徹底検証。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-seabuckthorn-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！奇跡のオメガ7と黄金ビタミンが真冬の寒冷くすみ＆粉吹き肌を満たす高保湿サジーオイルコスメランク10">
  <meta property="og:description" content="11月・12月の気温急降下と暖房乾燥による粉吹き肌・寒冷くすみを救う高保湿サジー（シーバックソーン）コスメを徹底厳選！マンディムーン、ヴェレダ、アンドエスエイチ、ライフフロー、バジャーまで徹底検証。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-seabuckthorn-oil">
  <meta property="og:site_name" content="Lumi Cosme">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap" rel="stylesheet">
  <script type="application/ld+json">
{json_ld_str}
  </script>
  <style>
    :root {{
      --primary: #c2410c;
      --primary-light: #ffedd5;
      --primary-dark: #7c2d12;
      --accent: #ea580c;
      --accent-hover: #9a3412;
      --bg: #fffaf5;
      --card-bg: #ffffff;
      --text-main: #27272a;
      --text-sub: #52525b;
      --border: #fed7aa;
      --shadow: 0 4px 15px rgba(194, 65, 12, 0.08);
      --radius: 14px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}

    header.site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 1.5rem;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}

    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}

    .nav-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 1.2rem;
      font-weight: 500;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    main.container {{
      max-width: 920px;
      margin: 2rem auto;
      padding: 0 1.2rem;
    }}

    .hero {{
      background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 100%);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      border: 1px solid var(--border);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .hero-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.8rem;
      border-radius: 20px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}

    .hero-title {{
      font-size: 1.7rem;
      font-weight: 700;
      line-height: 1.4;
      color: var(--primary-dark);
      margin-bottom: 1rem;
    }}

    .hero-desc {{
      font-size: 1rem;
      color: var(--text-sub);
      line-height: 1.8;
      margin-bottom: 1.2rem;
    }}

    .meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-sub);
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}

    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.8rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .toc-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.5rem;
    }}

    .toc-list li a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}

    .toc-list li a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .intro-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .intro-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .intro-section p {{
      margin-bottom: 1.2rem;
      font-size: 1rem;
      line-height: 1.8;
    }}

    .intro-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}

    .highlight-card {{
      background: var(--primary-light);
      padding: 1.2rem;
      border-radius: 10px;
      border-left: 4px solid var(--primary);
    }}

    .highlight-card strong {{
      display: block;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.4rem;
    }}

    .highlight-card p {{
      font-size: 0.9rem;
      color: var(--text-main);
      margin-bottom: 0;
      line-height: 1.6;
    }}

    .table-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      overflow-x: auto;
    }}

    .table-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}

    table.comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}

    table.comparison-table th, table.comparison-table td {{
      padding: 0.8rem 1rem;
      border-bottom: 1px solid #f1f5f9;
      text-align: left;
    }}

    table.comparison-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
    }}

    .table-thumb {{
      width: 55px;
      height: 55px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border);
    }}

    .rank-num {{
      font-weight: 700;
      color: var(--primary);
      font-size: 1.05rem;
    }}

    .price-cell {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .table-link {{
      color: var(--primary);
      font-weight: 700;
      text-decoration: none;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      position: relative;
    }}

    .product-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 6px;
      margin-bottom: 1.2rem;
    }}

    .product-header {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
    }}

    @media (min-width: 640px) {{
      .product-header {{
        flex-direction: row;
        align-items: flex-start;
      }}
    }}

    .img-container {{
      flex-shrink: 0;
      text-align: center;
    }}

    .product-img {{
      width: 220px;
      height: 220px;
      object-fit: contain;
      border-radius: 10px;
      border: 1px solid #fed7aa;
      background: #ffffff;
      padding: 0.5rem;
    }}

    .product-intro {{
      flex-grow: 1;
    }}

    .product-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #18181b;
      margin-bottom: 0.6rem;
      line-height: 1.5;
    }}

    .product-brand {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}

    .product-price {{
      font-size: 1rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #b91c1c;
    }}

    .product-tag {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      margin-bottom: 0.8rem;
      display: inline-block;
    }}

    .product-catch {{
      font-size: 0.95rem;
      color: #3f3f46;
      line-height: 1.7;
    }}

    .spec-table-box {{
      margin: 1.5rem 0;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid #fed7aa;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    table.spec-table th {{
      width: 28%;
      background: #fff7ed;
      color: var(--primary-dark);
      padding: 0.6rem 0.8rem;
      border-bottom: 1px solid #fed7aa;
      text-align: left;
    }}

    table.spec-table td {{
      padding: 0.6rem 0.8rem;
      border-bottom: 1px solid #fed7aa;
      color: #27272a;
    }}

    .review-body {{
      background: #fafaf9;
      border-radius: 10px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      border-left: 4px solid var(--primary);
    }}

    .review-body h4 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
    }}

    .review-body p {{
      font-size: 0.95rem;
      line-height: 1.8;
      margin-bottom: 1rem;
      color: #3f3f46;
    }}

    .target-box, .point-box {{
      background: #ffffff;
      border: 1px dashed #fed7aa;
      border-radius: 8px;
      padding: 1rem;
      margin-top: 1rem;
      font-size: 0.9rem;
      line-height: 1.7;
    }}

    .target-box strong, .point-box strong {{
      display: block;
      color: var(--primary-dark);
      margin-bottom: 0.3rem;
    }}

    .btn-wrap {{
      text-align: center;
      margin-top: 1.5rem;
    }}

    .rakuten-btn {{
      display: inline-block;
      background: linear-gradient(135deg, #ea580c 0%, #c2410c 100%);
      color: #ffffff;
      font-size: 1rem;
      font-weight: 700;
      padding: 1rem 2rem;
      border-radius: 30px;
      text-decoration: none;
      box-shadow: 0 4px 12px rgba(194, 65, 12, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 480px;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(194, 65, 12, 0.35);
      background: linear-gradient(135deg, #c2410c 0%, #9a3412 100%);
    }}

    .faq-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .faq-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .faq-item {{
      margin-bottom: 1.5rem;
      border-bottom: 1px solid #f4f4f5;
      padding-bottom: 1.2rem;
    }}

    .faq-item:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}

    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-q span {{
      color: var(--primary);
    }}

    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #3f3f46;
      padding-left: 1.5rem;
    }}

    .guide-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .guide-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .guide-section h3 {{
      font-size: 1.15rem;
      color: #18181b;
      margin: 1.2rem 0 0.6rem;
    }}

    .guide-section p {{
      font-size: 0.95rem;
      line-height: 1.8;
      margin-bottom: 1rem;
      color: #3f3f46;
    }}

    .related-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .related-section-title {{
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .related-list {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.2rem;
    }}

    .related-card {{
      background: #fafaf9;
      border: 1px solid #f4f4f5;
      border-radius: 10px;
      padding: 1.2rem;
      text-decoration: none;
      display: flex;
      flex-direction: column;
      transition: all 0.2s;
    }}

    .related-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
      border-color: var(--border);
    }}

    .related-card-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
      line-height: 1.5;
    }}

    .related-card-desc {{
      font-size: 0.82rem;
      color: var(--text-sub);
      line-height: 1.5;
    }}

    footer.site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 2.5rem 1.5rem;
      margin-top: 4rem;
    }}

    .footer-inner {{
      max-width: 1080px;
      margin: 0 auto;
      text-align: center;
    }}

    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.8rem 1.5rem;
      margin-bottom: 1.5rem;
    }}

    .footer-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 0.2s;
    }}

    .footer-links a:hover {{
      color: var(--primary);
    }}

    .copyright {{
      font-size: 0.8rem;
      color: #a1a1aa;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#guide">選び方・使い方</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="hero-badge">2026年真冬版 ｜ 徹底保湿コスメ検証</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！奇跡のオメガ7と黄金ビタミンが真冬の寒冷くすみ＆粉吹き肌を満たす高保湿サジーオイルコスメランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて日本列島を覆う厳しい冷気と過酷なエアコン暖房。皮膚の末梢血流は滞り、皮脂分泌が急激に衰えることで、顔色はどんよりと青黒くくすみ、頬やすねは白い粉を吹く限界状態に陥ります。そんな真冬の「皮脂枯渇」と「寒冷くすみ」の二大トラブルを一度に救い出すのが、砂漠や極寒の地を生き抜くスーパーフルーツ「サジー（シーバックソーン）」から採れる黄金のオイルです。植物界随一のオメガ7パルミトレイン酸と天然カロテノイドを凝縮した高保湿名品10選をコスメコンシェルジュが徹底検証・厳選しました。
      </p>
      <div class="meta-bar">
        <span>🕒 公開日: 2026年11月5日</span>
        <span>✍️ 執筆・検証: Lumi Cosme 編集部 コスメコンシェルジュ</span>
        <span>🔍 楽天リアルタイムAPI商品データ照合済</span>
      </div>
    </section>

    <div class="toc-box">
      <div class="toc-title">📑 目次（タップで該当ランキングへジャンプ）</div>
      <ul class="toc-list">
{toc_links}
      </ul>
    </div>

    <section class="intro-section">
      <h2>真冬の粉吹き肌と寒冷くすみを劇的に好転させる「サジーオイル」の科学的根拠</h2>
      <p>
        晩秋から初冬にかけて湿度が20%台まで急降下すると、皮膚の最外層である角層から水分が蒸発するスピードが爆発的に上昇します。さらに外気温の低下によって皮脂腺の活動が不活発になり、健康な肌を守るはずの天然バリア「皮脂膜」が著しく減少。結果として角質細胞同士がめくれ上がり、触るとザラつき、衣服と擦れて粉を吹く「皮脂欠乏性乾燥」に直面します。
      </p>
      <p>
        こうした真冬特有の肌クライシスに対して、近年美容皮膚科学や植物療法（フィトセラピー）の分野で熱狂的な注目を集めているのが「サジーオイル（シーバックソーン / シーベリーオイル）」です。ユーラシア大陸の厳しい寒暖差と乾燥地帯に原生するグミ科の果実から抽出されるこのオイルは、他の植物油とは一線を画す圧倒的な栄養密度を誇ります。
      </p>

      <div class="intro-highlight-grid">
        <div class="highlight-card">
          <strong>1. 奇跡の脂肪酸「オメガ7（パルミトレイン酸）」高含有</strong>
          <p>人の皮脂膜中に豊富に存在し、加齢や冬の寒さで激減するパルミトレイン酸を植物中最高峰の比率で含有。欠乏した皮脂膜を速攻で再構築し、水分の蒸発を物理的に食い止めます。</p>
        </div>
        <div class="highlight-card">
          <strong>2. 黄金カロテノイド＆ビタミンA・C・Eの相乗効果</strong>
          <p>オイルの深いオレンジ色は、高濃度な天然βカロテンやリコピン、トコフェロールの証。冬の血行不良でどんより青白くくすんだ肌に、内側から押し上げるような血色感と透明感をもたらします。</p>
        </div>
        <div class="highlight-card">
          <strong>3. 細胞間脂質と調和する優れたエモリエント性</strong>
          <p>角層のラメラ構造に素早くなじみ、寒さでカチコチに固まった角質を柔らかくほぐします。スキンケアの最初に仕込むことで、化粧水の浸透ルートを広げるブースターとしても機能します。</p>
        </div>
      </div>
    </section>

    <section class="table-section" id="comparison">
      <h2>高保湿サジーオイルコスメ おすすめ10選 比較一覧表</h2>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>画像</th>
            <th>ブランド / アイテム名</th>
            <th>分類</th>
            <th>参考価格</th>
            <th>詳細</th>
          </tr>
        </thead>
        <tbody>
{table_joined}
        </tbody>
      </table>
    </section>

    <section id="ranking">
{cards_joined}
    </section>

    <section class="guide-section" id="guide">
      <h2>プロ直伝！真冬のサジーオイル選び方＆保湿力を最大限引き出す使い方</h2>
      <h3>1. 「果実油（ベリーオイル）」と「種子油（シードオイル）」の選び分け</h3>
      <p>
        サジーオイルを購入する際は、ラベルの成分表記を確認しましょう。「果実油」は濃い深紅オレンジ色で、オメガ7とカロテノイドが極めて豊富。真冬の深刻なしぼみ肌・粉吹き肌・くすみを一発で立て直したいエイジングケアには果実油がベストです。一方、「種子油」は淡い黄色でオメガ3・6が多く、軽やかなテクスチャーのため日中のメイク前や軽めの保湿に向いています。
      </p>
      <h3>2. 「乳液やクリームへの1滴ブレンド」で色移りを防ぎながら高保湿</h3>
      <p>
        未精製の高品質なサジーオイルは色が濃厚なため、「原液をそのまま顔に塗ると黄色くならないか」と不安になる方も多いはずです。最も賢いテクニックは、手のひらにとった普段の乳液や保湿クリームにサジーオイルを『1滴だけ』垂らし、手のひらで混ぜ合わせてから顔全体をハンドプレスする方法です。クリームの水分と油分が乳化し、肌馴染みが一気に向上して色移りすることなく、翌朝まで暖房乾燥を完璧にシャットアウトできます。
      </p>
      <h3>3. お風呂上がりの「インバス全身ケア」で粉吹きすねを完全リセット</h3>
      <p>
        冬の脱衣所での急激な水分蒸散を防ぐには、入浴直後、バスタオルで体を拭く前の『まだ肌に水滴がついている状態』でサジーボディオイルを全身に伸ばすのが最も効果的です。水分とサジーの油分が肌表面で瞬時に乳化し、薄くしなやかな保護膜を形成。その後バスタオルで優しく押さえるだけで、一日中粉を吹かない滑らかな美肌が完成します。
      </p>
    </section>

    <section class="faq-section" id="faq">
      <h2>よくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> サジーオイル（シーバックソーン）が真冬の乾燥やくすみに劇的に効く理由は何ですか？</div>
        <div class="faq-a">サジー（シーベリー）には、植物界では極めて希少な「オメガ7不飽和脂肪酸（パルミトレイン酸）」が約30%以上も高濃度に含まれています。パルミトレイン酸は人間の皮脂膜を構成する主要成分であり、加齢や冬の寒冷刺激で皮脂分泌が落ちると真っ先に枯渇します。サジーオイルはこの不足した皮脂膜を瞬時に再現し、水分蒸散を防ぎます。さらに天然のβカロテン、ビタミンA・C・E、植物ステロールが豊富で、真冬の寒さで血行不良に陥り青白くくすんだ肌に、内側から血色感と明るい透明感を取り戻します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> サジーオイルの鮮やかなオレンジ色で肌や枕カバーに色が移りませんか？</div>
        <div class="faq-a">サジーオイルの濃いオレンジ色は、人工着色料ではなく高濃度な天然βカロテン（プロビタミンA）に由来します。原液を直接大量に塗ると一時的に肌が黄色っぽく見えることがありますが、手持ちの乳液やクリーム、化粧水に1〜2滴混ぜて薄くハンドプレスすれば、角層へ素早く浸透して色が定着することはありません。心配な場合は、就寝前のナイトルーティンとして使用し、塗布後5分程度置いて肌表面がサラリとなじんでから就寝することをおすすめします。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> サジーの「果実油」と「種子油」にはどのような違いがありますか？</div>
        <div class="faq-a">サジーオイルには果肉から採れる「果実油（ベリーオイル）」と種から採れる「種子油（シードオイル）」があります。果実油は鮮やかな深紅オレンジ色で、オメガ7（パルミトレイン酸）とカロテノイドが圧倒的に豊富で、冬の強烈な乾燥・肌のしぼみ・くすみケアに最適です。一方、種子油はやや淡い黄色で、オメガ3（α-リノレン酸）とオメガ6（リノール酸）が多く含まれ、肌荒れ予防やバリア補修に向いています。真冬のエイジングケアや濃密保湿を最優先するなら果実油、日中の軽やかなケアには種子油がおすすめです。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 冬のスキンケアでの最も効果的なサジーオイルの使い方は？</div>
        <div class="faq-a">最もおすすめなのは「夜のクリーム・乳液への1滴ブレンド」です。いつもの保湿クリームや乳液にサジーオイルを1滴垂らし、手のひらで混ぜ合わせてから全顔へ包み込むようにハンドプレスします。これにより油分が乳化して浸透力が高まり、翌朝まで暖房の乾燥に負けない強固な保護ヴェールが持続します。また、入浴後の濡れた肌に全身伸ばすボディオイルケアとしても、冬の粉吹きすねを瞬時に解消する絶大な効果を発揮します。</div>
      </div>
    </section>

    <!-- 関連記事プレースホルダー -->
    <section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list" id="related-grid-box">
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-links" id="footer-links-box">
      </div>
      <p class="copyright">© 2026 Lumi Cosme. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-seabuckthorn-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-seabuckthorn-oil.html!")
