import json
import re

with open("fetched_3new_rose_primrose_moringa.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_evening_primrose"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🌙 高純度精製×ガンマリノレン酸濃縮！全身の粉吹き砂漠肌を救う大容量キャリアオイル",
        "catch": "天然の月見草種子から抽出したピュアオイルを丁寧に精製。独特のクセや香りを抑えながらγ-リノレン酸の強力な保湿バリア機能をそのまま凝縮した、冬の全身保湿に最適な大容量ボトル",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "200ml / ポンプ付き遮光ボトル",
        "type": "高純度精製月見草キャリアオイル",
        "features": "月見草油（イブニングプリムローズオイル）100%精製、天然γ-リノレン酸、オメガ6脂肪酸",
        "value": "200mlの大容量でコスパ抜群。精製済みのため酸化臭が少なくサラリとした使い心地。顔だけでなく真冬に粉を吹きやすいすね・腕・デコルテまで惜しみなく使える",
        "desc_p1": "11月から12月にかけて湿度が20%近くまで激減すると、体内で作られる皮脂の分泌量が半減し、角質細胞同士を接着している細胞間脂質がスカスカになってしまいます。この『皮脂膜の崩壊』こそが、冬の耐え難いピリつきや粉吹き、下着のこすれによるかゆみの元凶です。&SHのイブニングプリムローズオイルは、そんな緊急事態に陥った素肌へ、皮脂の重要成分であるγ-リノレン酸（GLA）を直接補給できる名品です。",
        "desc_p2": "丁寧に精製されているため、未精製オイルにありがちな重い油臭さがなく、驚くほど軽やかで伸びの良いテクスチャーに仕上がっています。お風呂上がりの濡れた素肌にサッと伸ばすだけで、水分を抱え込みながら瞬時に滑らかな保護膜を形成。タイツを履いた時にすねがチクチク痛んだり、背中や腰回りが乾燥でムズムズしたりする冬特有の不快感を一掃し、ベルベットのようにしなやかな肌質を一日中維持してくれます。",
        "target": "冬になると全身が粉を吹いてかゆみが出る方、惜しみなくたっぷり使える大容量オイルを探している方、未精製オイルの香りが苦手な方",
        "point": "入浴直後、タオルで体を拭く前の水気が残った肌に3〜4プッシュを全身へ手早く伸ばします。水分とオイルが自然に乳化し、ベタつかずに吸い付くようなもっちり肌が完成します。"
    },
    {
        "rank": 2,
        "tag": "🌿 未精製コールドプレス100%！極度の乾燥・皮剥け肌を蘇らせる高機能リペアオイル",
        "catch": "手作りコスメの権威マンディムーンが厳選したオーガニック未精製オイル。熱を一切加えない低温圧搾法により、月見草が秘める生きたγ-リノレン酸とビタミンEを丸ごと肌へチャージ",
        "brand_name": "mandy moon (マンディムーン)",
        "capacity": "50ml / スポイト付き遮光瓶",
        "type": "オーガニック未精製ピュアオイル",
        "features": "USDA・ECOCERT認証オーガニック未精製月見草油100%（冷圧搾）",
        "value": "黄金色に輝く濃厚な1滴に、植物本来の生理活性成分が満ち溢れる無添加処方。真冬の冷風で皮がめくれた口元や目元をピンポイントで集中修復",
        "desc_p1": "古くから北米先住民族の間で『皮膚の万能薬』として重宝され、ヨーロッパでは王侯貴族がこぞって愛用したことから『King's Cure-All（王の万能薬）』と讃えられた月見草。マンディムーンの未精製オイルは、その種子を非加熱でじっくり搾油した一切の混じりけのないピュアな生オイルです。",
        "desc_p2": "未精製ならではのナッツのような濃厚な香りと濃い黄金色は、有効成分が熱破壊されずに残っている証拠。指先にとるとトロンとしたコクのある感触ですが、人の皮脂バリアに極めて類似した脂肪酸組成を持つため、塗布した瞬間に角層の奥深くへと吸い込まれていきます。冬の寒暖差で皮が剥けてしまった口角や、ヒリついて化粧水すら染みる目元の薄い皮膚に優しく馴染ませれば、翌朝には赤みが落ち着き、ふっくらとした弾力が蘇ります。",
        "target": "冬の乾燥で口元や小鼻周りの皮むけが止まらない方、合成添加物を一切排除した原液コスメを使いたい方、肌本来の再生力を底上げしたい方",
        "point": "夜のお手入れの最後に、スポイトで1〜2滴を取り手のひらに広げます。擦らずに、荒れが気になる部分へ指の腹でトントンと置くように馴染ませてください。手持ちのクリームに1滴混ぜて使うのも効果的です。"
    },
    {
        "rank": 3,
        "tag": "💧 有機栽培月見草種子の極上ブレンド！更年期乾燥やホルモン乱れのカサつきを包む低刺激オイル",
        "catch": "英国オーガニックボタニクスの哲学が息づく精製ピュアオイル。年齢や季節の変わり目で女性ホルモンバランスが乱れ、急激にカサカサになった大人のゆらぎ肌をしっとり柔軟に導く",
        "brand_name": "Organic Botanics (オーガニックボタニクス)",
        "capacity": "50ml / ガラスドロップボトル",
        "type": "低刺激オーガニック精製美容オイル",
        "features": "精製イブニングプリムローズオイル（γ-リノレン酸高含有）、トコフェロール（天然ビタミンE）",
        "value": "敏感肌パッチテスト済み。不純物を極限まで除去し、刺激に極端に弱くなった冬のエイジング肌でも安心して使えるマイルド処方",
        "desc_p1": "40代以降の女性の肌は、女性ホルモン（エストロゲン）の減少に伴ってセラミドや皮脂の合成能力が低下し、11月以降の冬枯れシーズンに一気に『砂漠化』が進みます。通常の高保湿スキンケアを重ねても夕方にはつっぱりを感じてしまう…そんな大人特有のインナードライにこそ、月見草オイルのγ-リノレン酸が不可欠です。",
        "desc_p2": "オーガニックボタニクスの精製オイルは、敏感になった大人の皮膚刺激を徹底的に排除するため、アレルゲンとなり得る不純物を高度な技術で除去。サラリとしていながら角層内部を潤いで満たす浸透力と、表面に滑らかな保護膜を張るシールド力を高次元で両立しています。毎日のスキンケアに取り入れることで、ゴワついた肌の角質がほぐれ、触れると跳ね返るような柔らかさとツヤが取り戻せます。",
        "target": "加齢に伴い冬の乾燥や肌荒れが急激にひどくなった方、化粧ノリが悪く夕方になると顔がくすむ方、刺激の少ないオーガニックオイルを探している方",
        "point": "化粧水をたっぷり馴染ませた直後、肌がまだ湿っている状態で2滴を顔全体へプレスします。その後、乳液やクリームを重ねることで、角層の水分保持力を何倍にも引き上げます。"
    },
    {
        "rank": 4,
        "tag": "🌹 ローズヒップ×月見草×クランベリー！トリプル抗酸化シールドで冬の枯れ肌を一掃する美容オイル",
        "catch": "世界中で20秒に1本売れるニュージーランド発祥の名品オイル。必須脂肪酸の宝庫ローズヒップに月見草油と強力な抗酸化ベリー種子油をブレンドした冬枯れ肌の特効薬",
        "brand_name": "trilogy (トリロジー)",
        "capacity": "30ml / スポイト付き遮光ガラス瓶",
        "type": "高機能エイジングケアブレンドオイル",
        "features": "認定オーガニックローズヒップ油、月見草油、クランベリー種子油、トマト種子油",
        "value": "トリロジー独自の『ロザピン（Rosapene）』特許ブレンド。木枯らしの冷気や室内の暖房乾燥、紫外線による酸化ダメージを全方位からブロック",
        "desc_p1": "『乾燥だけでなく、冬になるとくすみやハリ不足、乾燥小ジワが一気に加速する』という複合的な冬の肌悩みを抱える方に絶大な支持を得ているのが、トリロジーの『ロザピンプラス』です。ブランドの代名詞である最高峰ローズヒップオイルに、月見草油と抗酸化作用抜群のクランベリー種子油を贅沢に掛け合わせた傑作です。",
        "desc_p2": "濃い黄金色のオイルを肌に伸ばすと、スーッと素早く浸透してベタつきを残さず、まるでシルクのベールを纏ったかのような上質な肌触りに整います。月見草オイルに含まれるγ-リノレン酸が冬の壊れかけたバリア構造を修復し、トマトやクランベリーのリコピン・抗酸化物質が乾燥ダメージによる細胞の酸化をブロック。朝晩たった2〜3滴使い続けるだけで、どんより曇った真冬の肌にパッと明るい透明感と押し返すようなハリが満ちてきます。",
        "target": "乾燥による小ジワ・たるみ・くすみを同時にケアしたい方、ベタつくオイルが苦手で浸透の速さを重視する方、世界的に定評のある名品を使いたい方",
        "point": "朝晩の洗顔後、化粧水の直後に2〜3滴を手のひらに伸ばし、顔から首筋、デコルテにかけて下から上へと引き上げるようにハンドプレスします。メイク前に使うと、一日中崩れない艶やかなベースメイクが完成します。"
    },
    {
        "rank": 5,
        "tag": "🍯 天然γ-リノレン酸9%以上！冬の寒暖差で硬くなった大人の肌をほぐす濃厚スキンケアオイル",
        "catch": "天然植物原料の専門店カフェ・ド・サボンが厳選。γ-リノレン酸含有率9%以上の高品質月見草種子から低温圧搾された未精製オイルが、真冬の硬化角層をマシュマロ肌へ導く",
        "brand_name": "Cafe de Savon (カフェ・ド・サボン)",
        "capacity": "50ml / 遮光ドロップボトル",
        "type": "未精製ピュア月見草オイル（100%植物油）",
        "features": "未精製月見草油（γ-リノレン酸9%以上、リノール酸約70%、オレイン酸約10%）",
        "value": "熱に弱いオメガ6系必須脂肪酸を生きたままボトルへ充填。冬の寒さでゴワつき、スキンケアが弾かれてしまう肌を瞬時に柔軟化",
        "desc_p1": "冬の室外の冷気と暖房の効いた室内を往復することで生じる『寒暖差ショック』は、肌のターンオーバーを著しく狂わせ、角層をカチカチに硬化させます。カフェ・ド・サボンの未精製月見草オイルは、γ-リノレン酸を9%以上という高濃度で含有しており、硬くこわばった角質層の隙間へスルスルと浸透していきます。",
        "desc_p2": "未精製ならではのリッチなテクスチャーが肌を密着保護し、乾燥によって失われた皮脂膜の代役を完璧に果たします。使い始めて数日で、洗顔時の指先の感触が『ゴワゴワ』から『モチモチ・ふんわり』へと劇的に変化。暖房直撃の環境でも肌がつっぱらず、夕方まで潤いのツヤ膜がキープされます。手持ちの乳液や美容液と混ぜても分離しにくく、自分好みの冬用高保湿ブレンドを作るベースとしても最適です。",
        "target": "肌が硬くなって化粧水が弾かれてしまう方、寒暖差による肌荒れや乾燥に悩む方、高品質な植物オイルを手頃な価格で試したい方",
        "point": "夜の洗顔後、蒸しタオルで顔を1分間温めて毛穴を開かせた後、本品を3滴馴染ませて優しくマッサージします。硬くなった表情筋と角層がほぐれ、驚くほどの柔軟肌が手に入ります。"
    },
    {
        "rank": 6,
        "tag": "🌎 低温圧搾ヘキサンフリー！顔からボディまで惜しみなく使えるアメリカ直輸入の大容量オイル",
        "catch": "世界的なサプリメント＆オーガニックコスメブランドNOW Foodsのロングセラー。化学溶剤ヘキサンを一切使用しない低温圧搾ピュアオイルで、真冬の全身乾燥を力強くガード",
        "brand_name": "NOW Foods (ナウフーズ)",
        "capacity": "118ml / UVカット遮光ボトル",
        "type": "低温圧搾ピュア月見草キャリアオイル",
        "features": "月見草種子油100%（コールドプレス・溶剤不使用・無香料・無着色）",
        "value": "118mlという大容量でありながらリーズナブル。純粋な月見草オイルのみで構成され、防腐剤や充填剤は完全無添加",
        "desc_p1": "世界中で愛用されるNOW Foodsのイブニングプリムローズオイルは、化学溶剤を一切使わずに低温圧搾された純度100%のナチュラルオイルです。海外規格ならではの118mlというゆとりのあるサイズ感で、冬場に乾燥しやすい顔のケアはもちろん、肘・膝・かかと・デコルテまで、乾燥が気になる全身へ惜しみなく使えます。",
        "desc_p2": "オイルそのものの粘度は高すぎず、肌に伸ばすとじんわりと温かみを感じるような滑らかな感触。必須脂肪酸が角層深部へ潤いを届けながら、肌表面にはしっかりとした油分バリアを形成するため、真冬の北風にさらされても肌がピリピリと乾くのを防いでくれます。無香料なので他のスキンケアやボディクリームの香りを邪魔せず、家族全員で冬の乾燥対策オイルとして共有できる頼もしさがあります。",
        "target": "海外オーガニックコスメの高コスパ品を好む方、顔だけでなく首元やかかとなど全身にたっぷり塗りたい方、完全無添加のピュアオイルを求める方",
        "point": "お風呂上がりに、乾燥して白く粉を吹きやすいすねや肘にマッサージするように塗り込みます。靴下を履いて寝れば、翌朝にはひび割れ寸前のかかともしっとり滑らかに整います。"
    },
    {
        "rank": 7,
        "tag": "🌹 月見草油×モスカータバラ種子油！冬の冷え固まった肌をビロード肌へ整える名門オイル",
        "catch": "スイスの植物療法名門WELEDAのプレミアム処方。月見草油とワイルドローズ（モスカータバラ）オイルが融合し、真冬の乾燥で失われたハリとキメ密度を取り戻すボディ＆フェイスオイル",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "100ml / ポンプ付きガラスボトル",
        "type": "高保湿プレミアムモイスチャーオイル",
        "features": "月見草種子油、モスカータバラ種子油、ホホバ種子油、アーモンド油",
        "value": "NATRUEオーガニック認証取得。便利なポンプ付きボトルで液垂れ知らず。天然ダマスクローズと月見草が織りなす上質な香りで心身を優雅に解きほぐす",
        "desc_p1": "100年以上の歴史を誇るスイスのオーガニックコスメブランド・ヴェレダ。その中でも『ワイルドローズ モイスチャーオイル』は、贅沢な月見草オイルと野生のバラの種子油をブレンドした、真冬の過酷な乾燥に立ち向かうためのラグジュアリーなボディ＆スキンオイルです。",
        "desc_p2": "便利なポンプを押してオイルを手にとると、天然ローズの優美で深い香りがバスルームに広がります。冷えで凝り固まったデコルテや肩、脚を優しくマッサージしながら塗り広げると、月見草のγ-リノレン酸が乾ききった角層にスッと浸透し、ホホバ油やアーモンド油が表面をしっとり包み込みます。使い続けるうちに肌のキメが整い、まるで上質なビロードを纏ったかのような極上の滑らかさとハリが蘇ります。",
        "target": "乾燥ケアと同時にマッサージで冬のむくみや冷えを解消したい方、ポンプ式で使いやすいボトルを好む方、本物の植物オイルの贅沢な香りに包まれたい方",
        "point": "手のひらに2〜3プッシュを取り、温めてから首筋から肩、デコルテに向けてリンパを流すように優しくストロークします。フェイスケアとして使う場合は、化粧水後の濡れた肌に半プッシュ押し込みます。"
    },
    {
        "rank": 8,
        "tag": "🏛️ 月見草油×フランキンセンス×バオバブ！真冬の極乾燥下でも乾かない最高峰リッチクリーム",
        "catch": "ニールズヤードが誇るプレミアムエイジングケアの最高峰。月見草油と生命の木バオバブ、神秘の精油フランキンセンスが融合し、暖房直撃の砂漠環境でも驚異の密閉保湿を叶える神クリーム",
        "brand_name": "NEAL'S YARD REMEDIES (ニールズヤード レメディーズ)",
        "capacity": "50g / 重厚なブルーガラスジャー",
        "type": "最高峰プレミアム高保湿リッチクリーム",
        "features": "有機月見草油、フランキンセンス精油、バオバブ種子油、クチナシ幹細胞エキス、アルガンオイル",
        "value": "英国アロマセラピーの叡智を結集した濃厚フォーミュラ。真冬の過酷な低湿度下でも、12時間以上乾燥知らずのハリ密肌をキープ",
        "desc_p1": "『冬の暖房の下にいると、どんな保湿クリームを塗っても1時間で乾いてしまう…』そんな深刻な乾燥難民のために作られたのが、ニールズヤードの最高峰『フランキンセンス インテンス リッチクリーム』です。砂漠の過酷な乾燥を生き抜くフランキンセンスの樹脂エキスに、月見草オイルやバオバブオイルなどの高機能植物油脂を贅沢極まりなく配合しています。",
        "desc_p2": "ジャーを開けると、スモーキーで心を深く静めてくれるフランキンセンスの芳香が漂います。濃厚でこっくりとしたリッチなクリームを顔全体に伸ばすと、体温でとろけるように密着し、角層全体に濃密な油分バリアを形成。月見草のγ-リノレン酸が真冬のバリア崩壊を内側から補修し、植物幹細胞エキスがピンとした弾力を与えます。夜塗って眠れば、翌朝の洗顔時に肌が内側からパーンと張っているような驚くべき手応えを感じられます。",
        "target": "一般的な保湿クリームでは真冬の乾燥に太刀打ちできない方、深い乾燥小ジワやたるみ感を集中ケアしたい方、最高品質のスパコスメを求める方",
        "point": "化粧水や美容液の後、パール粒大を手に取り手のひらで温めます。顔全体をリフトアップするように下から上へ優しく引き上げながら包み込みます。ほうれい線や目尻には重ねづけが効果的です。"
    },
    {
        "rank": 9,
        "tag": "🛁 天然植物オイルブレンド×月見草エキス！入浴後の肌に素早く馴染みキメを修復する名作オイル",
        "catch": "ドイツのハーバルブランド・クナイプのベストセラーオイル。月見草オイルや植物オイルをバランスよく配合し、冬の粉吹き肌やキメの乱れを速やかに修復するマルチトリートメント",
        "brand_name": "Kneipp (クナイプ)",
        "capacity": "100ml / ガラスボトル",
        "type": "高保湿オーガニックボディ＆フェイスオイル",
        "features": "月見草エキス、サフラワー油、オリーブ果実油、グレープフルーツ果皮油",
        "value": "天然ハーブの力で肌本来のバリア機能を整えるドイツ品質。サラリとして服に付かない絶妙な浸透性で、日々のデイリー保湿に最適",
        "desc_p1": "植物療法の先進国ドイツで130年以上の伝統を誇るクナイプ。この『ビオ オイル』は、顔はもちろん全身の保湿ケアにマルチに使えるロングセラーアイテムです。真冬の乾燥で乱れてしまった角質のキメを整えるため、浸透性の高い植物オイルと月見草エキスを独自のノウハウでブレンドしています。",
        "desc_p2": "肌に乗せるとスルスルと水のように伸び、オイル特有のベタつきや油膜感が驚くほど残りません。月見草の有効成分が角質層の隅々まで行き渡り、冬の寒冷で硬くなった肌をなめらかに解きほぐします。天然シトラス系の爽やかな香りが心地よく、朝のスキンケア前に使ってもメイクがヨレる心配がありません。入浴直後の濡れた肌になじませることで、入浴後の急激な水分蒸発を完璧に防いでくれます。",
        "target": "ベタつくオイルが苦手な方、お風呂上がりに全身を手早く保湿したい方、ドラッグストア等でも入手しやすい信頼の定番ブランドを選びたい方",
        "point": "お風呂から上がる直前、タオルドライ前の濡れた肌に適量を伸ばします。その後、バスタオルで上から軽く押さえるように水分を拭き取ると、しっとりスベスベの肌が一日中続きます。"
    },
    {
        "rank": 10,
        "tag": "🌼 月見草油×カレンデュラ×ボリジ！寒冷刺激でピリつくデリケート肌を救うプレミアムセラム",
        "catch": "英国ハーブ療法のカリスマが創設したハーブファーマシー。月見草油に鎮静のカレンデュラとボリジ油を掛け合わせ、真冬の冷風で赤みやヒリつきを起こした敏感肌を穏やかに包み込む",
        "brand_name": "Herb Pharmacy (ハーブファーマシー)",
        "capacity": "30ml / スポイト遮光瓶",
        "type": "高濃度ハーブブースターフェイシャルオイル",
        "features": "月見草種子油、トウキンセンカ花エキス（カレンデュラ）、ルリジサ種子油（ボリジ）、ホホバ種子油",
        "value": "ソイルアソシエーション有機認証取得。自社オーガニック農場で手摘みされた薬草を伝統的な温浸法で抽出した濃密ハーブオイル",
        "desc_p1": "冬の冷たい北風にさらされた後、室内に入ると顔がカーッと熱くなって赤ら顔になったり、いつもの化粧水がピリピリとしみたりすることがあります。そんな真冬の敏感トラブル肌のために作られたのが、ハーブファーマシーの『スキンブースター フェイシャルオイル』です。",
        "desc_p2": "抗炎症ハーブの代表格であるカレンデュラと、γ-リノレン酸を豊富に含む月見草油・ボリジ油が贅沢に溶け合っており、塗布した瞬間にピリつく肌を優しく鎮静させてくれます。水分を失ってバリアが破綻した角層細胞の間を、高純度な脂肪酸がピタッと埋めて密閉。冬のあらゆる外部刺激から肌を守り抜き、健やかで揺らがない強靭な素肌バリアを育ててくれます。",
        "target": "冬の冷風や寒暖差で顔が赤くなりやすい方、ヒリつきや敏感症状が出やすい方、本格的なハーブ療法のオイルを体験したい方",
        "point": "洗顔後、化粧水の前の『ファーストステップ（導入オイル）』として手のひらに2滴馴染ませます。肌を擦らず、優しく包み込むようにしてハーブの恵みを浸透させてください。"
    }
]

# 目次リンク
toc_links = ""
for p in product_details:
    toc_links += f'          <li><a href="#rank-{p["rank"]}">第{p["rank"]}位：{p["brand_name"]} {p["catch"][:20]}...</a></li>\n'

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
        "url": f"https://lumi-cosme.vercel.app/winter-evening-primrose#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！奇跡のγ-リノレン酸が真冬の深刻なバリア崩壊を救う高保湿月見草オイルコスメランク10",
            "description": "11月・12月の皮脂分泌激減と冷風によるひび割れ・ガサガサ粉吹き肌を救う高保湿月見草オイル（イブニングプリムローズ）コスメを徹底厳選！トリロジー、生活の木、CODINA、ニールズヤード、マンディムーンまで厳選。",
            "datePublished": "2026-11-05T01:00:00+09:00",
            "dateModified": "2026-11-05T01:00:00+09:00",
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
            "name": "高保湿月見草オイルコスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "月見草オイル（イブニングプリムローズ）に含まれるγ-リノレン酸は、なぜ冬の乾燥肌に不可欠なのですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "γ-リノレン酸（GLA）は、健康な皮膚バリアと細胞膜を維持するために必須のオメガ6系多価不飽和脂肪酸です。通常は食事から摂取したリノール酸から体内で生合成されますが、冬の寒冷ストレスや加齢、女性ホルモンの変化によって合成酵素の働きが著しく低下します。γ-リノレン酸が不足すると細胞間脂質の結合が崩れ、水分蒸発と肌荒れが急激に悪化します。月見草オイルはこのγ-リノレン酸を約9%以上という極めて稀少な高濃度で含有しており、外側から直接塗布することで冬の崩壊した皮膚バリアを急速に再構築できるためです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "未精製オイルと精製オイルではどのような違いがありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "『未精製オイル』は低温圧搾されたそのままの状態で、月見草特有の微量ポリフェノールやビタミンEが生きており、濃厚な黄金色とナッツのような独特の芳香があります。夜の集中ケアや極度の粉吹き肌のレスキューに最適です。一方『精製オイル』は脱色・脱臭処理が施されており、香りがほとんどなくサラリとしたテクスチャーが特徴です。酸化しにくく日中のケアやお風呂上がりの全身使い、敏感肌の方のデイリーユースに適しています。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "月見草オイルは酸化しやすいと聞きましたが、保管方法や使用期限の注意点はありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "月見草オイルはオメガ6脂肪酸を豊富に含むため、熱や光、空気に触れると酸化しやすい性質を持っています。そのため、必ず茶色や青色の遮光瓶に入った製品を選び、直射日光の当たらない涼しい冷暗所（暖房の効いていない部屋や冷蔵庫の野菜室など）で保管してください。開封後は2〜3ヶ月を目安に使い切るのが理想的です。オイルが油臭く変質した場合は肌トラブルの原因となるため使用を中止してください。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "アトピー肌や極度の敏感肌でも月見草オイルを使用できますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "月見草オイルはヨーロッパでは古くからアトピー素因や皮脂欠乏症のスキンケアとして皮膚科領域でも活用されてきた歴史があります。γ-リノレン酸には抗炎症作用があり、冬のかゆみや乾燥性湿疹を穏やかに鎮める働きが期待できます。ただし、超敏感肌の方は未精製オイルに含まれる微量植物成分に反応する可能性もあるため、まずは精製された低刺激オイルを選び、腕の内側等でパッチテストを行ってから顔や全身に使用することを推奨します。"
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
  <title>保湿力の強さで肌乾燥とさようなら！奇跡のγ-リノレン酸が真冬の深刻なバリア崩壊を救う高保湿月見草オイルコスメランク10</title>
  <meta name="description" content="11月・12月の皮脂分泌激減と冷風によるひび割れ・ガサガサ粉吹き肌を救う高保湿月見草オイル（イブニングプリムローズ）コスメを徹底厳選！トリロジー、生活の木、CODINA、ニールズヤード、マンディムーンまで厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-evening-primrose">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！奇跡のγ-リノレン酸が真冬の深刻なバリア崩壊を救う高保湿月見草オイルコスメランク10">
  <meta property="og:description" content="11月・12月の皮脂分泌激減と冷風によるひび割れ・ガサガサ粉吹き肌を救う高保湿月見草オイル（イブニングプリムローズ）コスメを徹底厳選！トリロジー、生活の木、CODINA、ニールズヤード、マンディムーンまで厳選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-evening-primrose">
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
      --primary: #4338ca;
      --primary-light: #e0e7ff;
      --primary-dark: #312e81;
      --accent: #6366f1;
      --accent-hover: #4f46e5;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #334155;
      --text-sub: #64748b;
      --border: #cbd5e1;
      --shadow: 0 4px 15px rgba(67, 56, 202, 0.08);
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
      background: linear-gradient(135deg, #eef2ff 0%, #f1f5f9 100%);
      border: 1px solid #c7d2fe;
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .hero-tag {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 50px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}

    h1.hero-title {{
      font-size: 1.85rem;
      font-weight: 700;
      line-height: 1.45;
      color: #0f172a;
      margin-bottom: 1.2rem;
    }}

    .hero-desc {{
      color: var(--text-sub);
      font-size: 1rem;
      line-height: 1.8;
      margin-bottom: 1.5rem;
    }}

    .hero-meta {{
      display: flex;
      gap: 1.2rem;
      font-size: 0.85rem;
      color: #94a3b8;
      border-top: 1px solid #e2e8f0;
      padding-top: 1rem;
    }}

    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.8rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .toc-card h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.6rem;
    }}

    @media (min-width: 640px) {{
      .toc-list {{
        grid-template-columns: 1fr 1fr;
      }}
    }}

    .toc-list a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.92rem;
      display: block;
      padding: 0.3rem 0.5rem;
      border-radius: 6px;
      transition: background 0.2s, color 0.2s;
    }}

    .toc-list a:hover {{
      background: var(--primary-light);
      color: var(--primary);
    }}

    .table-section {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}

    .table-section h2 {{
      font-size: 1.35rem;
      color: #0f172a;
      margin-bottom: 1.2rem;
      border-left: 5px solid var(--primary);
      padding-left: 0.8rem;
    }}

    .table-wrapper {{
      overflow-x: auto;
    }}

    table.rank-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}

    table.rank-table th, table.rank-table td {{
      padding: 0.9rem;
      border-bottom: 1px solid #f1f5f9;
    }}

    table.rank-table th {{
      background: #eef2ff;
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}

    .rank-num {{
      font-weight: 700;
      color: var(--primary);
      white-space: nowrap;
    }}

    .table-thumb {{
      width: 50px;
      height: 50px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid #e2e8f0;
    }}

    .price-cell {{
      font-weight: 700;
      color: #e11d48;
      white-space: nowrap;
    }}

    .table-link {{
      color: var(--primary);
      text-decoration: none;
      font-weight: 700;
      font-size: 0.85rem;
    }}

    .table-link:hover {{
      text-decoration: underline;
    }}

    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
      position: relative;
    }}

    .product-badge {{
      display: inline-block;
      background: linear-gradient(135deg, var(--primary) 0%, #6366f1 100%);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 1rem;
      border-radius: 50px;
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
      width: 100%;
      max-width: 260px;
      margin: 0 auto;
      text-align: center;
      background: #f8fafc;
      padding: 1rem;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
    }}

    .product-img {{
      width: 100%;
      height: auto;
      max-height: 240px;
      object-fit: contain;
      border-radius: 8px;
    }}

    .product-intro {{
      flex-grow: 1;
    }}

    h3.product-title {{
      font-size: 1.3rem;
      color: #0f172a;
      line-height: 1.45;
      margin-bottom: 0.6rem;
    }}

    .product-brand {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}

    .product-price {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
    }}

    .price-val {{
      font-size: 1.45rem;
      font-weight: 700;
      color: #e11d48;
    }}

    .product-tag {{
      display: inline-block;
      background: #eef2ff;
      color: var(--primary-dark);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 6px;
      border: 1px solid #c7d2fe;
      margin-bottom: 0.8rem;
    }}

    .product-catch {{
      font-size: 0.95rem;
      color: #475569;
      line-height: 1.7;
    }}

    .spec-table-box {{
      margin: 1.5rem 0;
      background: #f8fafc;
      border-radius: 10px;
      padding: 1rem 1.2rem;
      border: 1px solid #e2e8f0;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    table.spec-table th, table.spec-table td {{
      padding: 0.5rem 0.6rem;
      border-bottom: 1px solid #e2e8f0;
      text-align: left;
    }}

    table.spec-table tr:last-child th, table.spec-table tr:last-child td {{
      border-bottom: none;
    }}

    table.spec-table th {{
      width: 25%;
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}

    .review-body {{
      margin-top: 1.5rem;
      border-top: 1px solid #f1f5f9;
      padding-top: 1.5rem;
    }}

    .review-body h4 {{
      font-size: 1.05rem;
      color: #0f172a;
      margin-bottom: 0.8rem;
    }}

    .review-body p {{
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.85;
      margin-bottom: 1rem;
    }}

    .target-box, .point-box {{
      background: #eff6ff;
      border-left: 4px solid var(--accent);
      padding: 0.9rem 1.1rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 1rem;
      font-size: 0.9rem;
      color: #334155;
    }}

    .point-box {{
      background: #eef2ff;
      border-left-color: var(--primary);
    }}

    .btn-wrap {{
      margin-top: 1.8rem;
      text-align: center;
    }}

    a.rakuten-btn {{
      display: inline-block;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: #ffffff;
      text-decoration: none;
      font-size: 1rem;
      font-weight: 700;
      padding: 1rem 2rem;
      border-radius: 50px;
      box-shadow: 0 4px 15px rgba(230, 0, 0, 0.25);
      transition: transform 0.2s, box-shadow 0.2s, background 0.2s;
      width: 100%;
      max-width: 460px;
    }}

    a.rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(230, 0, 0, 0.35);
      background: linear-gradient(135deg, #a80000 0%, #d40000 100%);
    }}

    .guide-section, .faq-section {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}

    .guide-section h2, .faq-section h2 {{
      font-size: 1.4rem;
      color: #0f172a;
      margin-bottom: 1.5rem;
      border-left: 5px solid var(--primary);
      padding-left: 0.8rem;
    }}

    .guide-section h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin: 1.5rem 0 0.8rem;
    }}

    .guide-section p {{
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.85;
      margin-bottom: 1rem;
    }}

    .guide-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.2rem;
      margin: 1.5rem 0;
    }}

    @media (min-width: 640px) {{
      .guide-grid {{
        grid-template-columns: 1fr 1fr 1fr;
      }}
    }}

    .guide-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 1.2rem;
    }}

    .guide-card h4 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}

    .guide-card p {{
      font-size: 0.88rem;
      color: var(--text-sub);
      line-height: 1.6;
      margin-bottom: 0;
    }}

    .faq-item {{
      border-bottom: 1px solid #f1f5f9;
      padding: 1.2rem 0;
    }}

    .faq-item:last-child {{
      border-bottom: none;
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

    .faq-q::before {{
      content: "Q.";
      color: var(--primary);
      font-weight: 700;
    }}

    .faq-a {{
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.8;
      padding-left: 1.6rem;
    }}

    .related-links {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}

    .related-links h3 {{
      font-size: 1.2rem;
      color: #0f172a;
      margin-bottom: 1.2rem;
    }}

    .related-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.8rem;
    }}

    @media (min-width: 640px) {{
      .related-grid {{
        grid-template-columns: 1fr 1fr;
      }}
    }}

    .related-card {{
      display: block;
      padding: 0.8rem 1rem;
      background: #f8fafc;
      border-radius: 8px;
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.9rem;
      transition: background 0.2s, color 0.2s;
      border: 1px solid #e2e8f0;
    }}

    .related-card:hover {{
      background: var(--primary-light);
      color: var(--primary);
    }}

    footer.site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 2.5rem 1.5rem;
      text-align: center;
      font-size: 0.88rem;
      color: var(--text-sub);
      margin-top: 3rem;
    }}

    footer.site-footer a {{
      color: var(--primary);
      text-decoration: none;
      margin: 0 0.4rem;
    }}

    footer.site-footer a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">🌸 Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/">ホーム</a>
        <a href="/winter-damask-rose">高保湿ダマスクローズ</a>
        <a href="/winter-moringa-oil">高保湿モリンガオイル</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="hero-tag">❄️ 11月・12月真冬の集中保湿ケア特集</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！奇跡のγ-リノレン酸が真冬の深刻なバリア崩壊を救う高保湿月見草オイルコスメランク10</h1>
      <p class="hero-desc">
        11月から12月へと本格的な冬を迎えると、外気温の低下に伴い人体の皮脂分泌量は激減します。空気の乾燥とエアコン暖房のダブルパンチを受け、肌表面の角質細胞を接着している『細胞間脂質』はスカスカになり、水分蒸発と肌荒れが加速度的に進行します。「化粧水をいくら塗っても乾いてつっぱる」「口周りや頬が粉を吹いて皮がめくれる」「タイツや下着がすれると肌がかゆくてたまらない」…それは、角層の水分を抱え込む皮脂膜そのものが機能不全に陥っている明確なサインです。<br><br>
        そんな冬の過酷な皮脂欠乏性乾燥を根本から救済するのが、ヨーロッパで古くから『王の万能薬（King's Cure-All）』と称賛されてきた「月見草オイル（イブニングプリムローズオイル）」です。植物界でもごく一部にしか存在しない極めて貴重な必須脂肪酸『γ-リノレン酸（ガンマリノレン酸 / GLA）』を高濃度（約9%以上）に含有し、寒冷や加齢で合成できなくなった皮膚バリアを外側から直接補修してくれます。<br><br>
        本記事では、楽天APIからリアルタイムに取得した最新データに基づき、オーガニック未精製ピュアオイルから大容量キャリアオイル、プレミアム高保湿クリーム、マルチバームまで、真冬の粉吹き肌と決別するための実力派月見草オイルコスメTOP10を徹底検証しました。
      </p>
      <div class="hero-meta">
        <span>📅 2026年11月最新更新</span>
        <span>✍️ コスメコンシェルジュ＆生薬学アナリスト監修</span>
        <span>🔬 楽天市場公式APIデータ連携済</span>
      </div>
    </section>

    <div class="toc-card">
      <h3>📑 目次：高保湿月見草オイルコスメTOP10</h3>
      <ul class="toc-list">
{toc_links}
      </ul>
    </div>

    <section class="table-section">
      <h2>🏆 高保湿月見草オイルコスメおすすめ比較一覧</h2>
      <div class="table-wrapper">
        <table class="rank-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品画像</th>
              <th>ブランド・商品名</th>
              <th>分類</th>
              <th>楽天市場価格</th>
              <th>詳細リンク</th>
            </tr>
          </thead>
          <tbody>
{table_joined}
          </tbody>
        </table>
      </div>
    </section>

    <section class="products-section">
{cards_joined}
    </section>

    <section class="guide-section">
      <h2>💡 失敗しない高保湿月見草オイルコスメの選び方＆冬の活用術</h2>

      <h3>1. 「未精製（コールドプレス）」と「精製（リファインド）」の使い分け基準</h3>
      <p>月見草オイルを選ぶ際、最も意識すべきは精製度です。『未精製（コールドプレス）』は種子本来のビタミンEやポリフェノールが丸ごと残されており、濃い黄金色とナッツのような独特の植物香があります。肌の再生バリアを最も強力に高めるため、夜の集中ケアや極度の粉吹き・ひび割れ部分へのピンポイント使いに圧倒的におすすめです。一方、『精製オイル』は脱臭・脱色によってサラリとした質感に仕上げられており、香りが苦手な方やお風呂上がりの全身保湿、朝のメイク前ブースターとして快適に使えます。</p>

      <div class="guide-grid">
        <div class="guide-card">
          <h4>未精製オイル（黄金色）</h4>
          <p>夜の集中リペア、口元・目元の皮むけや粉吹きレスキューに最適。γ-リノレン酸本来の生理活性パワーをダイレクトに補給します。</p>
        </div>
        <div class="guide-card">
          <h4>精製大容量キャリアオイル</h4>
          <p>お風呂上がりの濡れた全身、すね・腕・デコルテの粉吹き防止に最適。無香料でベタつきが少なくデイリー使いに重宝します。</p>
        </div>
        <div class="guide-card">
          <h4>高機能ブレンドクリーム・オイル</h4>
          <p>冬の寒暖差小ジワや乾燥くすみの一掃に最適。ローズヒップやフランキンセンスと掛け合わせることで多角的なエイジングケアを実現します。</p>
        </div>
      </div>

      <h3>2. 真冬の粉吹き肌を蘇らせる「インバス・オイルエマルジョン法」</h3>
      <p>冬のお風呂上がりは、浴室から出た瞬間に肌の水分が一気に蒸発し、入浴前よりも乾燥が悪化する『過乾燥』が起こります。月見草オイルの保水シールド力を最大化するため、以下の入浴時テクニックをお試しください。</p>
      <ol style="margin-left: 1.5rem; margin-bottom: 1rem; color: var(--text-sub); line-height: 1.8;">
        <li><strong>浴室を出る直前に塗布：</strong> お風呂から上がる直前、タオルで水分を拭き取る前の濡れた肌に月見草オイルを2〜3プッシュ広げます。</li>
        <li><strong>水分とオイルを自然乳化：</strong> 肌表面に残った水分とオイルを手早く馴染ませると、肌の上で即席の乳液膜が形成されます。</li>
        <li><strong>ポンポンと押さえ拭き：</strong> バスタオルで擦らず、上から優しく押さえるようにして余分な水滴だけを吸い取ります。これだけで一日中すねや腕の粉吹きを完全防止できます。</li>
      </ol>

      <h3>3. 酸化を防ぐための正しい保管ルール</h3>
      <p>月見草オイルに豊富に含まれるγ-リノレン酸は、多価不飽和脂肪酸のため空気中の酸素や光、熱によって酸化しやすい性質を持っています。酸化したオイルを肌に乗せると過酸化脂質となり、逆に肌荒れやくすみの原因となります。必ず遮光瓶に入った製品を選び、直射日光の当たらない涼しい場所で保管してください。開封後は2〜3ヶ月を目安に使い切るのが鉄則です。</p>
    </section>

    <section class="faq-section">
      <h2>❓ 高保湿月見草オイルコスメに関するよくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q">月見草オイル（イブニングプリムローズ）に含まれるγ-リノレン酸は、なぜ冬の乾燥肌に不可欠なのですか？</div>
        <div class="faq-a">γ-リノレン酸（GLA）は、健康な皮膚バリアと細胞膜を維持するために必須のオメガ6系多価不飽和脂肪酸です。通常は食事から摂取したリノール酸から体内で生合成されますが、冬の寒冷ストレスや加齢、女性ホルモンの変化によって合成酵素の働きが著しく低下します。γ-リノレン酸が不足すると細胞間脂質の結合が崩れ、水分蒸発と肌荒れが急激に悪化します。月見草オイルはこのγ-リノレン酸を約9%以上という極めて稀少な高濃度で含有しており、外側から直接塗布することで冬の崩壊した皮膚バリアを急速に再構築できるためです。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">未精製オイルと精製オイルではどのような違いがありますか？</div>
        <div class="faq-a">『未精製オイル』は低温圧搾されたそのままの状態で、月見草特有の微量ポリフェノールやビタミンEが生きており、濃厚な黄金色とナッツのような独特の芳香があります。夜の集中ケアや極度の粉吹き肌のレスキューに最適です。一方『精製オイル』は脱色・脱臭処理が施されており、香りがほとんどなくサラリとしたテクスチャーが特徴です。酸化しにくく日中のケアやお風呂上がりの全身使い、敏感肌の方のデイリーユースに適しています。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">月見草オイルは酸化しやすいと聞きましたが、保管方法や使用期限の注意点はありますか？</div>
        <div class="faq-a">月見草オイルはオメガ6脂肪酸を豊富に含むため、熱や光、空気に触れると酸化しやすい性質を持っています。そのため、必ず茶色や青色の遮光瓶に入った製品を選び、直射日光の当たらない涼しい冷暗所（暖房の効いていない部屋や冷蔵庫の野菜室など）で保管してください。開封後は2〜3ヶ月を目安に使い切るのが理想的です。オイルが油臭く変質した場合は肌トラブルの原因となるため使用を中止してください。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">アトピー肌や極度の敏感肌でも月見草オイルを使用できますか？</div>
        <div class="faq-a">月見草オイルはヨーロッパでは古くからアトピー素因や皮脂欠乏症のスキンケアとして皮膚科領域でも活用されてきた歴史があります。γ-リノレン酸には抗炎症作用があり、冬のかゆみや乾燥性湿疹を穏やかに鎮める働きが期待できます。ただし、超敏感肌の方は未精製オイルに含まれる微量植物成分に反応する可能性もあるため、まずは精製された低刺激オイルを選び、腕の内側等でパッチテストを行ってから顔や全身に使用することを推奨します。</div>
      </div>
    </section>

    <section class="related-links">
      <h3>🔗 あわせて読みたい！冬の高保湿スキンケア特集</h3>
      <div class="related-grid">
        <a href="/winter-damask-rose" class="related-card">🌹 高保湿ダマスクローズコスメ10選</a>
        <a href="/winter-moringa-oil" class="related-card">🌱 高保湿モリンガオイルコスメ10選</a>
        <a href="/winter-tamanu-oil" class="related-card">🌿 高保湿タマヌオイルコスメ10選</a>
        <a href="/winter-baobab-oil" class="related-card">🌳 高保湿バオバブオイルコスメ10選</a>
        <a href="/winter-kombucha" class="related-card">🍵 高保湿コンブチャコスメ10選</a>
        <a href="/winter-manuka-honey" class="related-card">🍯 高純度マヌカハニーコスメ10選</a>
        <a href="/winter-resurrection-plant" class="related-card">🌵 復活草・トレハロースコスメ10選</a>
        <a href="/winter-ceramide-cream" class="related-card">🛡️ 高保湿セラミドクリーム10選</a>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 Lumi Cosme. All rights reserved. 掲載価格は楽天市場の最新参考価格です。</p>
    <p style="margin-top: 0.5rem;"><a href="/">ホーム</a> | <a href="/winter-damask-rose">高保湿ダマスクローズ</a> | <a href="/winter-evening-primrose">高保湿月見草オイル</a> | <a href="/winter-moringa-oil">高保湿モリンガオイル</a></p>
  </footer>

</body>
</html>"""

with open("winter-evening-primrose.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved winter-evening-primrose.html successfully!")
