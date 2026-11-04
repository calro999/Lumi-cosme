import json
import re

with open("fetched_final_30_manuka_prickly_calendula.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_calendula"]["items"]

# 各商品ごとの完全オリジナルなレビュー＆詳細データ
product_details = [
    {
        "rank": 1,
        "tag": "🌼 手摘みカレンデュラ花びら入り！寒暖差の赤み・ヒリつきを鎮静させる世界的ベストセラー",
        "catch": "ボトルの中に本物のカレンデュラの花びらが揺れるキールズの金字塔ローション。冬の冷風と暖房の寒暖差でピリつく敏感肌を穏やかに鎮静させ、健やかな満水肌へと整えるアルコールフリー化粧水",
        "brand_name": "Kiehl's (キールズ)",
        "capacity": "250ml / ボトル",
        "type": "高鎮静・高保湿ハーブトリートメント化粧水",
        "features": "手摘みカレンデュラ花びら（トウキンセンカ花エキス）、ゴボウ根エキス、アラントイン、加水分解コーンスターチ",
        "value": "1960年代の発売以来、世界中で愛され続ける名品。アルコールフリーで冬の薄くデリケートになった皮膚にも全くしみず、赤み・火照り・乾燥トラブルを速攻レスキュー",
        "desc_p1": "11月から12月にかけて、木枯らしが吹き付ける寒い屋外から暖房が効いた暖かい室内へ移動した瞬間、頬がカッと熱くなって赤ら顔になったり、皮膚がピリピリと突っ張って痛がゆくなったりする『寒暖差トラブル』に悩む方が急増します。この冬特有の皮膚毛細血管のパニックと微小炎症を穏やかに落ち着かせてくれる救世主が、キールズの『ハーバル トナー CL アルコールフリー』です。透明なボトルの中には、手摘みされたカレンデュラ（トウキンセンカ）の黄金色の花びらが贅沢に漂っています。",
        "desc_p2": "水のようにサラリとしたテクスチャーでありながら、肌にハンドプレスすると驚くほど角層へスーッと浸透。カレンデュラに含まれるフラボノイドやカロテノイドが、寒暖差やマスク摩擦で荒れ狂う肌の興奮をスッと鎮め、乱れたキメを均一に整えます。アルコール（エタノール）を一切使用していないため、冬の寒冷で皮膚が極度に薄くなり、普段のスキンケアがしみてしまう時でも安心してたっぷり使えます。重ねづけするほどに肌が穏やかに鎮まり、内側から澄み渡るようなクリアな潤いが満ちていきます。",
        "target": "真冬の寒暖差で頬の赤みやヒリつきが出やすい方、アルコール刺激に弱い敏感肌の方、肌の水分油分バランスを整えて肌荒れを未然に防ぎたい方",
        "point": "洗顔後、500円玉大を手のひらに取り、顔全体を包み込むように優しくハンドプレスします。赤みが気になる頬や鼻周りには、コットンにたっぷり含ませて3〜5分間ローションパックをすると、火照りがスッと引き、キメの整った陶器肌が復活します。"
    },
    {
        "rank": 2,
        "tag": "👶 赤ちゃんの頬から大人の乾燥荒れまで！有機カレンドラが守る伝統の高保湿クリーム",
        "catch": "オーガニックコスメの先駆者WELEDAが100年守り続ける伝統処方。有機カレンドラエキスとアーモンド油が、真冬の冷風でヒリつく肌にとろりと馴染み、濃密な保護膜で満たすフェイスクリーム",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "50ml / チューブタイプ",
        "type": "低刺激・高保護オーガニックフェイスクリーム",
        "features": "有機カレンドラ花エキス、アーモンド油、天然ミツロウ、ラノリン、トウキンセンカ花エキス",
        "value": "ヨーロッパの厳しいオーガニック認証『NATRUE』取得。合成保存料・合成着色料・合成香料不使用。皮膚が薄くデリケートな赤ちゃんの頬を守るために開発された絶対的な優しさと保湿力",
        "desc_p1": "真冬になると、冷たい外気によって肌の水分が奪われ、頬がりんごのように赤くカサカサに粉を吹いてしまう…そんな深刻な冬の乾燥性皮膚炎から肌を守り抜くために、ヨーロッパの家庭で常備薬のように愛され続けているのが、ヴェレダの『カレンドラ ベビーフェイシャルクリーム』です。『ベビー』という名がついていますが、実は真冬の乾燥に悩む大人の女性や美容のプロの間で『冬の最強レスキュークリーム』として熱烈な支持を集めています。",
        "desc_p2": "こっくりとした滑らかなクリームを肌に乗せると、天然のアーモンドオイルとミツロウが体温でじわっととろけ、乾燥した皮膚をふんわりと包み込みます。カレンドラエキスが冷風による肌のひび割れや赤みを穏やかに落ち着かせ、ラノリンが角層の水分蒸散を物理的にシャットアウト。夜塗って寝れば、翌朝の洗顔時までふっくらと柔らかいモチ肌がキープされ、冬の朝の洗顔後もしっとりした潤い膜が肌を守ってくれます。",
        "target": "冬になると頬が赤く粉を吹きやすい方、刺激の少ないオーガニック高保湿クリームを探している方、親子で一緒に使える安全安心なスキンケアを求める方",
        "point": "スキンケアの最後に、パール1粒大を指先にとり、温めてから乾燥が気になる頬や口元を中心に優しく伸ばします。化粧下地として薄く仕込むと、冬の冷たい外気から肌を物理的に保護し、一日中ファンデーションの乾燥割れを防ぎます。"
    },
    {
        "rank": 3,
        "tag": "🌿 太陽のハーブを濃密浸出！冷えた身体とこわばった肌をほぐす伝統マッサージオイル",
        "catch": "有機栽培されたカレンドラの花をヒマワリ種子油にじっくり漬け込んだ伝統のインフューズドオイル。真冬の冷えで血行が悪くなり硬くなった肌と全身をしっとり温めほぐす名作",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "100ml / ポンプ付き遮光ガラスボトル",
        "type": "高純度ボタニカルトリートメントオイル",
        "features": "トウキンセンカ花エキス（カレンドラ浸出油）、ヒマワリ種子油、カミツレ花エキス、天然エッセンシャルオイル",
        "value": "ポンプタイプで使いやすく酸化を防ぐ設計。顔はもちろん、首・デコルテ・全身のマッサージに使え、真冬の血行不良によるくすみとゴワつきを一掃",
        "desc_p1": "11月以降の寒さによって血流が滞ると、肌への栄養補給が滞り、顔色がどんよりとくすんで皮膚がカチカチに硬直してしまいます。そんな冬の『冷え枯れ肌』に血色感と濃密な潤いを取り戻してくれるのが、ヴェレダの『カレンドラ マッサージオイル』です。太陽の恵みをいっぱいに浴びて咲いた有機カレンドラの花を、肌馴染みの良い植物油にじっくりと漬け込んでエキスを抽出しています。",
        "desc_p2": "手のひらに取ると、黄金色に輝くオイルから柑橘系とハーブが心地よく調和した爽やかな香りが広がります。肌に滑らせると重たさを感じさせず、程よいグリップ感で凝り固まったフェイスラインや首筋をスムーズにマッサージできます。カレンドラとカモミールのダブル鎮静ハーブが肌荒れを防ぎ、ヒマワリ油のリッチな脂肪酸が乾燥した角層を驚くほど柔らかく解きほぐします。入浴後やお風呂の中でのオイルパックにも最適です。",
        "target": "寒さで顔色がくすみやすく血行を促進したい方、入浴後の全身乾燥ケアを贅沢に行いたい方、ハーブの香りで心身ともにリラックスしたい方",
        "point": "お風呂上がりの軽く湿り気が残る肌に適量を取り、顔からデコルテ、手足に向かって優しくリンパを流すようにマッサージします。湯船に浸かりながらオイルを顔全体に伸ばし、蒸しタオルを3分乗せる『ホットオイルパック』は冬の最高のご褒美ケアです。"
    },
    {
        "rank": 4,
        "tag": "🇬🇧 英国ソイルアソシエーション認定！真冬のデリケート肌を包み込むレスキューバーム",
        "catch": "英国名門ニールズヤードが誇るオーガニックカレンデュラクリーム。冷風でヒリつく頬やカサつく手肌に、植物の優しい高密度ヴェールがピタッと密着してバリア機能を再建",
        "brand_name": "NEAL'S YARD REMEDIES (ニールズヤード レメディーズ)",
        "capacity": "50g〜60ml / ジャータイプ",
        "type": "高機能オーガニックハーブクリーム",
        "features": "オーガニックカレンデュラ花エキス、アーモンド油、ミツロウ、ラノリン、レモン果皮油",
        "value": "英国で最も厳しいオーガニック基準をクリア。肌の自己回復力をサポートし、寒冷によるバリア機能低下を根本からケアする頼れる常備クリーム",
        "desc_p1": "イギリス・ロンドンのコヴェントガーデン発祥のオーガニックアポセカリー（薬局）ニールズヤード レメディーズ。植物療法（フィトセラピー）の知恵が凝縮された『カレンデュラ クリーム』は、冬になると肌が過敏になり、通常の化粧品ではピリピリとしみてしまう敏感肌の方から絶大な信頼を寄せられています。",
        "desc_p2": "クリームというよりはリッチなバームに近い、こっくりとした濃厚なテクスチャー。肌に伸ばすと、カレンデュラ本来のハーブの香りがふわりと立ち上り、荒れて赤くなった皮膚を優しく包み込みます。ミツロウとアーモンド油が外界の寒気や乾燥を物理的にブロックし、カレンデュラエキスが角層深部で微小な炎症を鎮静。塗布して数時間経っても肌の潤い膜が失われず、夕方になっても頬が乾燥で引きつることがありません。",
        "target": "真冬になるといつもの化粧品がしみて使えなくなる方、本格的な英国オーガニックハーブの品質を実感したい方、顔だけでなく手荒れや乾燥ひじのケアも兼ねたい方",
        "point": "化粧水や美容液で肌を整えた後、小豆粒大を手にとり、手のひらで温めて柔らかくしてから顔全体を優しく包み込むようにハンドプレスします。冬の外出前に特に乾燥しやすい頬骨に重ねづけしておくと、冷たい木枯らしから肌を守れます。"
    },
    {
        "rank": 5,
        "tag": "✨ 本物の花びらが古い角質を吸着！冬のくすみ毛穴をつるんと脱皮させる低刺激パック",
        "catch": "本物のカレンデュラ花びらとエキスを閉じ込めた低刺激ピールオフパック。冬の乾燥でゴワついた古い角質と毛穴汚れをやさしくオフし、剥がした瞬間からたまご肌へ",
        "brand_name": "APRILSKIN (エイプリルスキン)",
        "capacity": "100g / チューブタイプ",
        "type": "高鎮静カレンデュラピールオフパック",
        "features": "リアルカレンデュラ花びら、トウキンセンカ花エキス、ティーツリー葉油、ローズマリー葉エキス、ペパーミントエキス",
        "value": "低分子のゲル状シートが顔の凹凸に寸分の隙間もなく密着。無理に引き剥がすタイプではなく、カレンデュラの水分を角層に補給しながら優しくオフする安心処方",
        "desc_p1": "冬は乾燥によってターンオーバーが鈍り、古い角質が剥がれ落ちずに肌表面に堆積して、くすみやゴワつき、毛穴の詰まりを引き起こしやすくなります。しかし、冬のデリケートな肌に強いスクラブやピーリングを使うと、バリア機能をさらに傷つけてしまいます。そのジレンマを解消したのが、韓国エイプリルスキンの大ヒット作『リアル カレンデュラ ピールオフパック』です。",
        "desc_p2": "チューブから出すと、透き通った黄金色のジェルの中に、本物のカレンデュラの花びらがたっぷりと散りばめられています。付属のシリコンブラシで顔全体に均一に塗り広げると、カレンデュラの爽やかな香りに包まれながら徐々に乾いて薄いフィルム状へと変化。約20分後に端から優しく剥がすと、冬のゴワゴワした角質と余分な皮脂だけが吸着され、下からは生まれたてのようなつるんとした透明美肌が出現します。剥がした後もつっぱらず、しっとりとした水分感が続きます。",
        "target": "冬の乾燥で肌がゴワついてメイクノリが最悪な方、刺激の強い角質ケアは避けたい方、本物のハーブ花びら配合の贅沢パックを体験したい方",
        "point": "洗顔後、化粧水で肌を整えてから、目と口の周りを避けて顔全体に均一な厚みで伸ばします。約20〜30分完全に乾かした後、端からゆっくりと下から上へ剥がしてください。その後、いつもの乳液やクリームでしっかり保湿します。"
    },
    {
        "rank": 6,
        "tag": "🌿 大豆油にじっくり浸出！ひび割れ寸前の指先や角質を救う高純度ボタニカルオイル",
        "catch": "生活の木が厳選したカレンデュラの花を植物油にじっくり浸出させた高純度インフューズドオイル。冬の寒風でカサつく肘や踵、ひび割れ寸前の手肌を優しくケア",
        "brand_name": "生活の木 (Tree of life)",
        "capacity": "70ml / 遮光ボトル",
        "type": "ピュアボタニカルインフューズドオイル",
        "features": "トウキンセンカ花エキス、ダイズ油、トコフェロール（天然ビタミンE）",
        "value": "日本のハーブ界を牽引する生活の木の厳格な品質管理。刺激が極めて少なく、赤ちゃんや敏感肌のフェイス・ボディオイルとしてマルチに活躍",
        "desc_p1": "ハーブとアロマテラピーの専門店として名高い生活の木の『カレンデュラオイル（浸出油）』。良質な大豆油をベースに、カレンデュラの花に含まれる脂溶性の有効成分（カロテノイドやステロール）を時間をかけて丁寧に溶け込ませた、深みのある黄金色のスキンオイルです。",
        "desc_p2": "無香料で原料本来のほのかな植物の香りのみ。肌に乗せるとスルスルと滑らかに広がり、乾燥でささくれ立った角層を穏やかに満たしていきます。ダイズ油に含まれるビタミンEとレシチンが肌のバリアを補修し、カレンデュラ成分が冷えや乾燥による肌荒れを優しく防止。冬場の水仕事で荒れた指先のキューティクルオイルとして、また冬の入浴後の全身保湿オイルとして、一本あるだけで家族全員の真冬の乾燥対策をこなしてくれます。",
        "target": "無添加・無香料の純粋なハーブオイルを求める方、水仕事による手荒れや指先のひび割れを防ぎたい方、キャリアオイルとして手作りコスメに使いたい方",
        "point": "化粧水の後の保湿オイルとして、手のひらに2〜3滴を取り顔全体に優しくハンドプレスします。手荒れやささくれが気になる時は、指先に念入りに擦り込んでから綿の手袋をして就寝すると、翌朝驚くほど滑らかな手肌に蘇ります。"
    },
    {
        "rank": 7,
        "tag": "🌸 100%天然由来マルチバーム！冬のメイク前や日中の乾燥小ジワにとろけるツヤ膜",
        "catch": "トウキンセンカ花エキスとオーガニックシアバターを贅沢配合したスキンケア発想のマルチバーム。メイクの上からでも使え、真冬の乾燥でパサつく目元や頬に濡れツヤを宿す",
        "brand_name": "naturaglace (ナチュラグラッセ)",
        "capacity": "40g / チューブ・ジャー",
        "type": "高保湿エモリエントスキンケアバーム",
        "features": "トウキンセンカ花エキス（カレンデュラ）、シア脂、ホホバ種子油、スクワラン、カニナバラ果実油",
        "value": "100%天然由来原料。界面活性剤・合成ポリマー・鉱物油・パラベン不使用。乾燥によるメイク崩れを防ぎながら日中もスキンケア効果が持続",
        "desc_p1": "天然由来成分100%のミネラルコスメブランドとして大人気のナチュラグラッセが手がける『エモリエント クリームバーム』。植物の恵みを知り尽くした処方で、冬の過酷な乾燥環境下でも肌のみずみずしいツヤをキープするために、カレンデュラエキスと高純度シアバターを融合させています。",
        "desc_p2": "体温に触れるとスーッととろけるオイルリッチな質感。カレンデュラが日中の寒暖差ストレスから肌を守り、シアバターとホホバオイルが水分の蒸散をしっかり防ぎます。朝のベースメイクの前に乾燥しやすい目元や口元に仕込んでおけば、ファンデーションがピタッと密着して夕方まで粉吹き知らず。さらに、日中のメイクの上から乾燥が気になった時にも、指先に極少量とってトントンと馴染ませるだけで、まるでハイライトを入れたかのようなみずみずしいツヤ肌が復活します。",
        "target": "日中のファンデーションの乾燥割れや粉吹きに悩んでいる方、100%天然由来成分にこだわりたい方、メイクの上からも使える保湿バームを探している方",
        "point": "朝のスキンケアの最後に、米粒大を指先で温めてから目元やほうれい線に薄く叩き込みます。日中は乾燥を感じた部分に極少量をトントンと重ねづけすることで、メイクを崩さずにツヤと潤いをチャージできます。"
    },
    {
        "rank": 8,
        "tag": "🔬 手持ちの化粧水が冬の神コスメに化ける！寒暖差ストレスに挑む高濃度濃縮原液",
        "catch": "自然化粧品研究所が誇る高純度トウキンセンカ花エキス原液。普段愛用している化粧水やクリームに数滴加えるだけで、真冬の肌荒れ防止力と鎮静力を大幅に底上げ",
        "brand_name": "自然化粧品研究所",
        "capacity": "30ml / 遮光スポイトボトル",
        "type": "高濃度ボタニカル濃縮エキス原液",
        "features": "トウキンセンカ花エキス（カレンデュラ原液）、BG、水（植物抽出エキス）",
        "value": "無香料・無着色・防腐剤最小限設計。今使っているお気に入りのスキンケアを変えることなく、冬の寒暖差赤み・肌荒れ対策をピンポイントで強化できる高コスパ原液",
        "desc_p1": "『冬になるといつもの化粧水では保湿力が足りないけれど、新しい化粧品に変えて肌荒れするのが怖い』…そんな敏感肌の方に絶大な支持を得ているのが、自然化粧品研究所の『トウキンセンカ花エキス（カレンデュラエキス）原液』です。カレンデュラの花に含まれる有効成分を余すところなく高濃度に抽出したプロ仕様のコスメ原料です。",
        "desc_p2": "スポイトから取り出すと、サラリとした淡い琥珀色の液体で、肌にスッと浸透。いつもの化粧水を使う直前に手のひらで1〜2滴混ぜ合わせるだけで、肌荒れ防止効果と鎮静保湿力が格段にパワーアップします。冬の冷たい空気でピリピリとしみやすい肌も穏やかに落ち着き、赤みの出にくいタフな角層土台へと導いてくれます。30mlと大容量で、毎日惜しみなく使えるコストパフォーマンスの高さも大きな魅力です。",
        "target": "現在のスキンケアを変えずに冬の肌荒れ対策を強化したい方、成分重視で高濃度エキスを使いたい方、コスパ良くカレンデュラの美容効果を取り入れたい方",
        "point": "手のひらに化粧水を適量取った後、本品を1〜2滴垂らして混ぜ合わせ、顔全体に優しくハンドプレスします。シートマスクを使用する前に、赤みが気になる頬に直接原液を馴染ませておく『集中プレ美容液使い』も非常に効果的です。"
    },
    {
        "rank": 9,
        "tag": "🌼 冷風で荒れ狂う頬を包み込む！スイスの大自然が育んだ伝統のレスキューバーム",
        "catch": "ヴェレダのオーガニック栽培カレンドラを濃縮配合した軟膏タイプのマルチケアクリーム。冬の寒冷刺激で赤く荒れた頬や、ガサガサになった手肌を穏やかに整える名作",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "25g〜75ml / アルミチューブ",
        "type": "高密着ハーブスキンリペアバーム",
        "features": "有機カレンドラ花エキス、アーモンド油、ゴマ油、ミツロウ、酸化亜鉛",
        "value": "水分をはじく高密着バーム処方。冬の冷たい風や衣類の摩擦から肌を物理的に保護し、皮膚本来の健やかなターンオーバーをサポート",
        "desc_p1": "ヨーロッパの厳しい冬を乗り越えるための伝統的な家庭薬草学から生まれた、ヴェレダの『カレンドラ ケアクリーム』。長年多くの人々のデリケートな肌を守り続けてきた歴史あるハーブバームです。",
        "desc_p2": "アルミチューブから押し出すと、しっかりとした固さのある濃厚なバーム状。指先で温めると滑らかに伸びて、荒れた角層の隙間をぴったりと塞ぐように密着します。酸化亜鉛と天然ミツロウが外的刺激や水分の蒸発を物理的に防ぎ、カレンドラエキスが赤くヒリつく皮膚を穏やかにリセット。冬のアウトドアスポーツやスキー、真冬の自転車通勤などで冷風に晒される肌の頼れるシールドとして絶大な効果を発揮します。",
        "target": "冬の冷風で頬が赤くヒリヒリ痛くなりやすい方、屋外にいる時間が長く物理的な肌保護が必要な方、伝統的なハーブ軟膏の確かな安心感を求める方",
        "point": "外出の直前に、米粒大を指先で温めてから、冷風に直接当たる頬骨や鼻頭、唇の周りに薄く伸ばします。夜のスキンケアの最後に、荒れやすい部分にピンポイントで重ね塗りするナイトパック使いもおすすめです。"
    },
    {
        "rank": 10,
        "tag": "👑 世界最古のフィレンツェ薬局が誇る至高の逸品！赤ら顔を極上のヴェールで鎮静",
        "catch": "800年の歴史を誇るイタリア・フィレンツェの修道院薬局サンタ・マリア・ノヴェッラの名作。高濃度カレンデュラエキスとアーモンド油が、冬の冷風で赤く火照った肌を極上のヴェールで包む",
        "brand_name": "Santa Maria Novella (サンタ・マリア・ノヴェッラ)",
        "capacity": "100ml / ガラスジャー",
        "type": "最高峰プレミアムハーブ保湿クリーム",
        "features": "高純度カレンデュラ花エキス、スイートアーモンド油、天然エモリエント成分、植物性グリセリン",
        "value": "メディチ家にも愛されたフィレンツェの伝統製法。冬の寒冷で敏感になった肌を鎮静させながら、貴族のような気品ある滑らかさとハリを与える最高級クリーム",
        "desc_p1": "世界最古の薬局として知られるイタリア・フィレンツェのサンタ・マリア・ノヴェッラ。その長い歴史の中で、皮膚を鎮静し保護する目的で大切に受け継がれてきた名品が『クレマ カレンドラ』です。中世の修道士たちが薬草園で育てたカレンデュラの薬効を今に伝える、まさにハーブコスメの最高峰と呼ぶにふさわしいクリームです。",
        "desc_p2": "クラシカルなガラスジャーの蓋を開けると、優雅で穏やかな植物の香りが漂います。ホイップクリームのようにふんわりと柔らかいテクスチャーでありながら、肌に伸ばすと吸い付くように馴染み、上質なシルクのヴェールをまとったような極上の肌触りを実現。カレンデュラエキスが冬の寒暖差で赤ら顔になった肌を穏やかに鎮静させ、アーモンドオイルが角質層の奥深くまで豊かな油分を補給します。翌朝の肌の透明感と滑らかさは、一度使うと虜になる贅沢さです。",
        "target": "自分へのご褒美として最高級のスキンケアを楽しみたい方、真冬の赤ら顔や敏感症状を本気でケアしたい方、歴史と品格のある本物のハーブコスメを愛する方",
        "point": "夜のお手入れの最後に、パール大をスパチュラで取り、手のひらで温めてから顔全体から首筋にかけて優しくハンドプレスします。優雅なハーブの香りを深呼吸しながら馴染ませることで、真冬のストレスから解放される贅沢なリラクゼーションを味わえます。"
    }
]

# FAQ 生成
faqs = [
    {
        "q": "カレンデュラ（トウキンセンカ）は、冬の肌にどのような効果があるのですか？",
        "a": "カレンデュラは中世ヨーロッパから『皮膚のガードマン』と呼ばれ、火傷や肌荒れの治療に用いられてきた伝統ハーブです。最大の強みは、カロテノイドやフラボノイド、トリテルペンアルコールによる極めて高い『抗炎症・組織修復・毛細血管保護作用』にあります。11月・12月の厳しい寒暖差によって毛細血管が急激に伸縮し、赤ら顔やヒリつきを起こした真冬の肌を速やかに穏やかに整える効果があります。"
    },
    {
        "q": "キールズの化粧水のように、花びらが入っているコスメのメリットは何ですか？",
        "a": "抽出されたエキスだけでなく、植物の花びらそのものを浸漬させておくことで、ポリフェノールや微量栄養素がフレッシュな状態で液中に溶け出し続けます。また防腐剤やアルコールを最小限に抑えた処方が可能となり、冬の寒冷で皮膚が極度に薄くデリケートになった敏感肌でも、刺激を感じることなく角層の奥深くまで水分を浸透させることができます。"
    },
    {
        "q": "11月〜12月のスキンケアで、カレンデュラコスメを取り入れる最もおすすめの順番は？",
        "a": "洗顔直後のまっさらな角層にキールズのハーバルトナー（化粧水）をたっぷりとハンドプレスし、寒暖差の赤みを鎮静させます。その後、乾燥が気になる部分にヴェレダやニールズヤードのカレンデュラクリーム（またはバーム）を重ねて油分の保護膜を張るのが黄金ルートです。日中にメイクの上から乾燥を感じた時は、ナチュラグラッセのエモリエントバームを指先でトントンと重ねるとツヤ肌が復活します。"
    },
    {
        "q": "カレンデュラコスメはキク科アレルギーでも使えますか？",
        "a": "カレンデュラ（トウキンセンカ）はキク科の植物です。非常に低刺激で赤ちゃんにも使える優しいハーブですが、重度のキク科アレルギー（ブタクサ等）をお持ちの方は、念のため二の腕の内側などでパッチテストを行ってからご使用いただくことを推奨します。"
    }
]

# HTML テーブル行生成
table_rows = []
for it in items:
    r = it["rank"]
    p_info = next((p for p in product_details if p["rank"] == r), None)
    type_name = p_info["type"] if p_info else "高保湿コスメ"
    brand = it["brand"]
    name = it["display_name"].split(" (")[0]
    price = f"¥{it['price']:,}"
    img = it["image"]
    url = it["url"]
    
    row = f"""
    <tr>
      <td class="rank-num rank-{r}">{r}位</td>
      <td class="product-thumb"><a href="{url}" target="_blank" rel="nofollow noopener"><img src="{img}" alt="{name}" loading="lazy" width="80" height="80"></a></td>
      <td class="product-name-cell">
        <span class="product-brand">{brand}</span>
        <a href="{url}" target="_blank" rel="nofollow noopener" class="table-prod-link">{name}</a>
      </td>
      <td><span class="type-badge">{type_name}</span></td>
      <td class="product-price">{price}</td>
      <td><a href="{url}" target="_blank" rel="nofollow noopener" class="table-btn">楽天で見る</a></td>
    </tr>
    """
    table_rows.append(row)

table_joined = "\n".join(table_rows)

# 商品カード生成
cards = []
for it in items:
    r = it["rank"]
    p = next((x for x in product_details if x["rank"] == r), product_details[0])
    price = f"¥{it['price']:,}"
    img = it["image"]
    url = it["url"]
    shop = it["shop_name"]
    rate = it["review_rate"]
    reviews = it["review_count"]
    
    card = f"""
    <article class="product-card" id="rank-{r}">
      <div class="card-header">
        <div class="rank-badge rank-{r}">第{r}位</div>
        <div class="card-titles">
          <span class="card-tag">{p['tag']}</span>
          <h3 class="card-name">{it['display_name']}</h3>
        </div>
      </div>
      
      <p class="card-catch"><strong>【注目ポイント】</strong> {p['catch']}</p>
      
      <div class="card-body">
        <div class="card-image-box">
          <a href="{url}" target="_blank" rel="nofollow noopener">
            <img src="{img}" alt="{it['display_name']}" loading="lazy" width="300" height="300" class="product-img">
          </a>
          <div class="card-price-box">
            <span class="price-label">楽天市場参考価格</span>
            <span class="price-val">{price}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <div class="card-review-box">
            <span class="star-rating">★ {rate}</span>
            <span class="review-count">({reviews}件のレビュー)</span>
          </div>
          <a href="{url}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で最新価格をチェック ➔
          </a>
        </div>
        
        <div class="card-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{p['brand_name']}</td></tr>
            <tr><th>容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>注目保湿成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の保湿価値</th><td>{p['value']}</td></tr>
          </table>
          
          <div class="review-text-box">
            <h4>💡 美容皮膚・テクスチャー詳細レビュー</h4>
            <p>{p['desc_p1']}</p>
            <p>{p['desc_p2']}</p>
          </div>
          
          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ：</strong> {p['target']}
          </div>
          
          <div class="point-box">
            <strong>✨ 11-12月の効果的な使い方テクニック：</strong> {p['point']}
          </div>
        </div>
      </div>
    </article>
    """
    cards.append(card)

cards_joined = "\n".join(cards)

# FAQ HTML 生成
faq_items = []
for f in faqs:
    faq_html = f"""
    <div class="faq-item">
      <h3 class="faq-q"><span class="faq-q-badge">Q</span> {f['q']}</h3>
      <div class="faq-a"><span class="faq-a-badge">A</span> <p>{f['a']}</p></div>
    </div>
    """
    faq_items.append(faq_html)

faqs_joined = "\n".join(faq_items)

# 全体HTMLテンプレート（カレンデュラに合わせたマリーゴールドイエロー・ボタニカルアンバー系デザイン）

schema_items = []
for idx, it in enumerate(items, 1):
    schema_items.append({
        "@type": "ListItem",
        "position": idx,
        "name": it["display_name"],
        "url": f"https://lumi-cosme.vercel.app/winter-calendula#rank-{it['rank']}",
        "image": it["image"]
    })

schema_faq = []
for f in faqs:
    schema_faq.append({
        "@type": "Question",
        "name": f["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f["a"]
        }
    })

schema_json = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "ItemList",
            "name": "保湿力の強さで肌乾燥とさようなら！冬の冷風と寒暖差でピリつく敏感肌をしっとり鎮静させる高保湿カレンデュラコスメランク10",
            "description": "11月・12月の激しい寒暖差ショックと冬の冷風による赤ら顔・ヒリつき肌を救う高保湿カレンデュラコスメを徹底厳選！キールズ、ヴェレダ、ニールズヤードまで厳選。",
            "numberOfItems": 10,
            "itemListElement": schema_items
        },
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！冬の冷風と寒暖差でピリつく敏感肌をしっとり鎮静させる高保湿カレンデュラコスメランク10",
            "description": "11月・12月の激しい寒暖差ショックと冬の冷風による赤ら顔・ヒリつき肌を救う高保湿カレンデュラコスメを徹底厳選！キールズ、ヴェレダ、ニールズヤードまで厳選。",
            "image": items[0]["image"],
            "datePublished": "2026-11-04T19:00:00+09:00",
            "dateModified": "2026-11-04T19:00:00+09:00",
            "inLanguage": "ja",
            "mainEntityOfPage": "https://lumi-cosme.vercel.app/winter-calendula"
        },
        {
            "@type": "FAQPage",
            "mainEntity": schema_faq
        }
    ]
}, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！冬の冷風と寒暖差でピリつく敏感肌をしっとり鎮静させる高保湿カレンデュラコスメランク10 | Lumi Cosme</title>
  <meta name="description" content="11月・12月の激しい寒暖差ショックと冬の冷風による赤ら顔・ヒリつき肌を救う高保湿カレンデュラコスメを徹底厳選！キールズ、ヴェレダ、ニールズヤード、ナチュラグラッセ、サンタマリアノヴェッラまで、楽天市場で買える本物の高保湿10選を詳しく解説。">
  <meta name="keywords" content="カレンデュラ コスメ,トウキンセンカ スキンケア,キールズ カレンデュラ トナー,ヴェレダ カレンドラ,冬 寒暖差 肌荒れ,赤ら顔 保湿,敏感肌 化粧水">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-calendula">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #c25e00;
      --primary-dark: #8c3b00;
      --primary-light: #ffedd5;
      --accent: #f97316;
      --text-main: #27272a;
      --text-sub: #52525b;
      --text-light: #71717a;
      --bg-page: #fffaf5;
      --bg-card: #ffffff;
      --border-color: #fed7aa;
      --shadow-sm: 0 2px 4px rgba(194, 94, 0, 0.05);
      --shadow-md: 0 4px 12px rgba(194, 94, 0, 0.1);
      --shadow-lg: 0 10px 25px -5px rgba(194, 94, 0, 0.15);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.8;
      padding-bottom: 4rem;
    }}

    .site-header {{
      background: linear-gradient(135deg, #7c2d12 0%, #c25e00 50%, #ea580c 100%);
      color: #ffffff;
      padding: 2.2rem 1.5rem 2.8rem;
      text-align: center;
      box-shadow: 0 4px 20px rgba(124, 45, 18, 0.25);
    }}
    .site-header-nav {{
      max-width: 1100px;
      margin: 0 auto 1.25rem;
      text-align: left;
    }}
    .site-header-nav a {{
      color: #ffedd5;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }}
    .site-header-nav a:hover {{ text-decoration: underline; }}
    .header-badge {{
      display: inline-block;
      background: rgba(255,255,255,0.2);
      backdrop-filter: blur(8px);
      padding: 0.4rem 1.2rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 0.8rem;
    }}
    .site-title {{
      font-size: clamp(1.4rem, 4vw, 2.2rem);
      font-weight: 800;
      line-height: 1.35;
      margin-bottom: 1rem;
      text-shadow: 0 2px 4px rgba(0,0,0,0.15);
      max-width: 920px;
      margin-left: auto;
      margin-right: auto;
    }}
    .site-subtitle {{
      font-size: 0.95rem;
      color: #ffedd5;
      max-width: 820px;
      margin: 0 auto;
    }}

    .main-container {{
      max-width: 1040px;
      margin: -1.5rem auto 0;
      padding: 0 1rem;
    }}

    .toc-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 0.6rem;
    }}
    .toc-list a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: color 0.2s ease;
    }}
    .toc-list a:hover {{ color: var(--primary); text-decoration: underline; }}

    .intro-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .intro-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.5rem;
    }}
    .intro-section p {{
      margin-bottom: 1.2rem;
      color: var(--text-sub);
      font-size: 1rem;
    }}
    .intro-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin-top: 1.5rem;
    }}
    .intro-card {{
      background: #fff7ed;
      border-left: 4px solid var(--primary);
      padding: 1.2rem;
      border-radius: var(--radius-sm);
    }}
    .intro-card h3 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}
    .intro-card p {{
      font-size: 0.9rem;
      color: var(--text-sub);
      margin-bottom: 0;
    }}

    .table-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2rem 1.5rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
      overflow-x: auto;
    }}
    .table-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 680px;
    }}
    .compare-table th, .compare-table td {{
      padding: 1rem 0.8rem;
      border-bottom: 1px solid var(--border-color);
      text-align: left;
      vertical-align: middle;
    }}
    .compare-table th {{
      background: #ffedd5;
      color: var(--primary-dark);
      font-weight: 700;
    }}
    .rank-num {{
      font-weight: 800;
      font-size: 1.1rem;
      white-space: nowrap;
    }}
    .rank-1 {{ color: #c25e00; }}
    .rank-2 {{ color: #8c3b00; }}
    .rank-3 {{ color: #ea580c; }}
    .product-thumb img {{
      border-radius: 6px;
      object-fit: cover;
      display: block;
      border: 1px solid #fed7aa;
    }}
    .product-name-cell {{ min-width: 220px; }}
    .product-brand {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-light);
      margin-bottom: 0.2rem;
    }}
    .table-prod-link {{
      color: var(--text-main);
      text-decoration: none;
      font-weight: 700;
      line-height: 1.4;
      display: block;
    }}
    .table-prod-link:hover {{ color: var(--primary); text-decoration: underline; }}
    .type-badge {{
      display: inline-block;
      background: #ffedd5;
      color: var(--primary-dark);
      font-size: 0.75rem;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      font-weight: 600;
    }}
    .product-price {{
      font-weight: 800;
      color: #b91c1c;
      font-size: 1rem;
      white-space: nowrap;
    }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      text-decoration: none;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
      transition: background 0.2s ease;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}

    .product-card {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--border-color);
      scroll-margin-top: 2rem;
    }}
    .card-header {{
      display: flex;
      align-items: flex-start;
      gap: 1.2rem;
      margin-bottom: 1.2rem;
      border-bottom: 1px dashed var(--border-color);
      padding-bottom: 1rem;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
      color: #ffffff;
      font-size: 1.25rem;
      font-weight: 800;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-sm);
      white-space: nowrap;
      box-shadow: 0 2px 6px rgba(194, 94, 0, 0.3);
    }}
    .card-titles {{ flex: 1; }}
    .card-tag {{
      display: inline-block;
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 0.3rem;
    }}
    .card-name {{
      font-size: 1.3rem;
      font-weight: 800;
      line-height: 1.4;
      color: var(--text-main);
    }}
    .card-catch {{
      background: #fff7ed;
      border-left: 4px solid var(--primary);
      padding: 0.8rem 1rem;
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 1.5rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    }}

    .card-body {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .card-body {{ grid-template-columns: 1fr; }}
    }}
    .card-image-box {{
      text-align: center;
    }}
    .card-img, .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: var(--radius-md);
      border: 1px solid #fed7aa;
      margin-bottom: 1rem;
      transition: transform 0.2s ease;
    }}
    .card-img:hover {{ transform: scale(1.02); }}
    .card-price-box {{
      margin-bottom: 0.6rem;
    }}
    .price-label {{
      font-size: 0.8rem;
      color: var(--text-light);
      display: block;
    }}
    .price-val {{
      font-size: 1.6rem;
      font-weight: 800;
      color: #b91c1c;
    }}
    .price-tax {{
      font-size: 0.8rem;
      color: var(--text-light);
    }}
    .card-review-box {{
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 1rem;
    }}
    .star-rating {{ color: #ea580c; font-weight: 700; }}
    .card-aff-btn, .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #c25e00 0%, #8c3b00 100%);
      color: #ffffff;
      text-align: center;
      padding: 0.85rem 1rem;
      border-radius: var(--radius-sm);
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      box-shadow: 0 4px 10px rgba(140, 59, 0, 0.2);
      transition: all 0.2s ease;
    }}
    .card-aff-btn:hover, .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(140, 59, 0, 0.3);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      margin-bottom: 1.5rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.8rem;
      border-bottom: 1px solid var(--border-color);
      text-align: left;
    }}
    .spec-table th {{
      width: 25%;
      color: var(--primary-dark);
      background: #fff7ed;
      font-weight: 700;
    }}
    .review-text-box {{
      background: #fffdfa;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 1.25rem;
      margin-bottom: 1.2rem;
    }}
    .review-text-box h4 {{
      font-size: 1rem;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
    }}
    .review-text-box p {{
      font-size: 0.92rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
      line-height: 1.7;
    }}
    .review-text-box p:last-child {{ margin-bottom: 0; }}
    .target-box, .point-box {{
      background: #fff7ed;
      padding: 0.8rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.88rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
    }}
    .target-box strong, .point-box strong {{
      color: var(--primary-dark);
    }}

    .guide-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .guide-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.5rem;
    }}
    .guide-section p {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 1.2rem;
    }}
    .step-list {{
      counter-reset: step;
      list-style: none;
      display: grid;
      gap: 1rem;
    }}
    .step-item {{
      background: #fff7ed;
      border-radius: var(--radius-sm);
      padding: 1.2rem 1.2rem 1.2rem 3.5rem;
      position: relative;
    }}
    .step-item::before {{
      counter-increment: step;
      content: counter(step);
      position: absolute;
      left: 1.2rem;
      top: 1.2rem;
      background: var(--primary);
      color: #ffffff;
      width: 1.8rem;
      height: 1.8rem;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.9rem;
    }}
    .step-item h3 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
    }}
    .step-item p {{
      font-size: 0.9rem;
      margin-bottom: 0;
    }}

    .faq-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .faq-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border-color);
      padding: 1.2rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      display: flex;
      align-items: flex-start;
      gap: 0.8rem;
      margin-bottom: 0.6rem;
    }}
    .faq-q-badge {{
      background: var(--primary);
      color: #ffffff;
      padding: 0.1rem 0.5rem;
      border-radius: 4px;
      font-size: 0.85rem;
    }}
    .faq-a {{
      display: flex;
      align-items: flex-start;
      gap: 0.8rem;
      color: var(--text-sub);
      font-size: 0.93rem;
    }}
    .faq-a-badge {{
      background: #fed7aa;
      color: #8c3b00;
      padding: 0.1rem 0.5rem;
      border-radius: 4px;
      font-size: 0.85rem;
      font-weight: 700;
    }}

    .related-links-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .related-links-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}
    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
    }}
    .related-card {{
      background: #fffdfa;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 1rem;
      text-decoration: none;
      transition: all 0.2s ease;
      display: block;
    }}
    .related-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
      border-color: var(--primary);
    }}
    .related-card h3 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
      line-height: 1.4;
    }}
    .related-card p {{
      font-size: 0.8rem;
      color: var(--text-light);
      margin-bottom: 0;
      line-height: 1.5;
    }}

    .site-footer {{
      background: #431407;
      color: #ffedd5;
      text-align: center;
      padding: 3rem 1.5rem;
      font-size: 0.85rem;
      margin-top: 4rem;
    }}
    .site-footer a {{
      color: #fed7aa;
      text-decoration: none;
      margin: 0 0.5rem;
    }}
    .site-footer a:hover {{ text-decoration: underline; }}
  </style>

  <!-- JSON-LD 構造化データ -->
  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body>

  <header class="site-header">
    <div class="site-header-nav">
      <a href="/">🏠 Lumi Cosme ホームに戻る</a>
    </div>
    <span class="header-badge">2026-2027 冬の寒暖差レスキュー特集</span>
    <h1 class="site-title">保湿力の強さで肌乾燥とさようなら！<br>冬の冷風と寒暖差でピリつく敏感肌をしっとり鎮静させる高保湿カレンデュラコスメランク10</h1>
    <p class="site-subtitle">11月〜12月の木枯らしと過酷な室内暖房による激しい温度差で、頬の赤みやヒリつき・乾燥に悩む女性へ。古代から「皮膚のガードマン」と称されてきたカレンデュラ（トウキンセンカ）の自然治癒パワーが、傷ついた角層を速やかに鎮静し、濃密な潤いで包み込む至高のコスメを徹底比較！</p>
  </header>

  <main class="main-container">

    <!-- 目次 -->
    <nav class="toc-box">
      <h2 class="toc-title">📑 本記事の目次（タップで各商品へスキップ）</h2>
      <ul class="toc-list">
        <li><a href="#intro">🌼 なぜ冬の寒暖差肌にカレンデュラが不可欠なのか？</a></li>
        <li><a href="#table">📊 高保湿カレンデュラコスメ10選 スペック比較表</a></li>
        <li><a href="#rank-1">第1位：キールズ ハーバル トナー CL アルコールフリー</a></li>
        <li><a href="#rank-2">第2位：ヴェレダ カレンドラ ベビーフェイシャルクリーム</a></li>
        <li><a href="#rank-3">第3位：ヴェレダ カレンドラ マッサージオイル 100ml</a></li>
        <li><a href="#rank-4">第4位：ニールズヤード カレンデュラクリーム 50g</a></li>
        <li><a href="#rank-5">第5位：エイプリルスキン リアル カレンデュラ ピールオフパック</a></li>
        <li><a href="#rank-6">第6位：生活の木 カレンデュラオイル (浸出油) 70ml</a></li>
        <li><a href="#rank-7">第7位：ナチュラグラッセ エモリエント クリームバーム 40g</a></li>
        <li><a href="#rank-8">第8位：自然化粧品研究所 トウキンセンカ花エキス原液 30ml</a></li>
        <li><a href="#rank-9">第9位：ヴェレダ カレンドラ ケアクリーム 25g</a></li>
        <li><a href="#rank-10">第10位：サンタ・マリア・ノヴェッラ クレマ カレンドラ 100ml</a></li>
        <li><a href="#guide">💡 寒暖差に負けないカレンデュラ鎮静スキンケア術</a></li>
        <li><a href="#faq">❓ よくある質問と皮膚科学的回答</a></li>
      </ul>
    </nav>

    <!-- 導入解説 -->
    <section class="intro-section" id="intro">
      <h2>🌼 なぜ11-12月の『寒暖差ショック』にカレンデュラが最強の盾となるのか？</h2>
      <p>11月から12月にかけて、私たちの肌は一日のうちで最も過酷な温度変化に晒されます。0℃近くまで冷え込んだ屋外の木枯らしに直面した後、暖房が25℃前後に設定された室内や満員電車へ足を踏み入れると、わずか数分の間に20℃以上の急激な温度差が肌を直撃します。</p>
      <p>この急激な寒暖差により、皮膚表面の毛細血管が急激に収縮・拡張を繰り返し、自律神経の乱れとともに肌のバリア機能が崩壊。その結果、頬が真っ赤に火照ってカッと熱を持ったり、普段使っている低刺激なスキンケアでさえピリピリとしみて痛んだりする『冬の寒暖差ゆらぎ肌』が引き起こされます。</p>
      
      <div class="intro-grid">
        <div class="intro-card">
          <h3>🌿 1. カロテノイドとフラボノイドによる急速鎮静</h3>
          <p>鮮やかなオレンジ色の花びらに含まれるカロテノイドやフラボノイドが、寒暖差や摩擦によって発生した皮膚の微小炎症を素早く穏やかに鎮静。赤ら顔やヒリヒリ感をスッと落ち着かせます。</p>
        </div>
        <div class="intro-card">
          <h3>🔬 2. トリテルペンアルコールによる組織修復サポート</h3>
          <p>天然の抗炎症成分トリテルペンアルコールが、寒冷でひび割れそうになった角層細胞の再生を力強く後押し。弱り切った皮膚のバリア土台を健やかな状態へ立て直します。</p>
        </div>
        <div class="intro-card">
          <h3>🛡️ 3. 皮膚が薄いデリケート肌を包む保護シールド</h3>
          <p>ヨーロッパでは古くから赤ちゃんの皮膚保護薬として用いられるほど低刺激。アルコールや合成香料に頼らず、植物本来の優しいエモリエント膜で真冬の冷風を物理的にブロックします。</p>
        </div>
      </div>
    </section>

    <!-- 比較表 -->
    <section class="table-section" id="table">
      <h2>📊 高保湿カレンデュラコスメ10選 スペック徹底比較表</h2>
      <p style="font-size:0.9rem; color:var(--text-sub); margin-bottom:1rem;">※楽天市場公式取扱店・直営店の最新参考価格（税込）を表示しています。各商品リンクより現在のポイント還元率や在庫状況をご確認いただけます。</p>
      <table class="compare-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>画像</th>
            <th>商品名 / ブランド</th>
            <th>アイテム分類</th>
            <th>参考価格</th>
            <th>楽天詳細</th>
          </tr>
        </thead>
        <tbody>
          {table_joined}
        </tbody>
      </table>
    </section>

    <!-- 商品カード一覧 -->
    <section class="products-section">
      {cards_joined}
    </section>

    <!-- 効果的な使い方ガイド -->
    <section class="guide-section" id="guide">
      <h2>💡 寒暖差による赤み・ヒリつきを寄せ付けないカレンデュラスキンケア3大鉄則</h2>
      <p>冬の温度差ストレスから素肌を守り抜き、常に穏やかで澄んだツヤ肌をキープするためのプロ直伝ケアです。</p>
      
      <div class="step-list">
        <div class="step-item">
          <h3>ステップ1：帰宅後すぐの『冷ましハンドプレス』で火照りをリセット</h3>
          <p>寒い屋外から暖かい部屋に入って頬が赤く火照っている時は、手のひらでキールズのハーバルトナーをたっぷりと優しく押し込むように馴染ませます。摩擦を一切かけずに手のひらの体温でカレンデュラエキスを浸透させることで、拡張した毛細血管の興奮が穏やかに鎮まります。</p>
        </div>
        <div class="step-item">
          <h3>ステップ2：『3分間の局所ローションパック』でバリア破綻を即座に修復</h3>
          <p>特に赤みやヒリつきがひどい頬骨や小鼻の周りには、精製水で軽く湿らせたコットンにカレンデュラ化粧水（または自然化粧品研究所の原液を数滴垂らしたもの）をたっぷり含ませて3分パック。角層のすみずみに水分と抗炎症成分が行き渡り、キメの乱れを一瞬で整えます。</p>
        </div>
        <div class="step-item">
          <h3>ステップ3：天然ワックス系クリームによる『防寒ヴェール密閉』</h3>
          <p>水分の蒸発と冷風の直撃を防ぐため、ヴェレダやニールズヤードのカレンドラクリームを手のひら全体に温めてから顔を包み込みます。天然ミツロウと植物オイルが形成するしなやかな保護膜が、暖房の風にも負けない持続型エモリエントシールドを完成させます。</p>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="faq-section" id="faq">
      <h2>❓ 高保湿カレンデュラコスメに関するよくある質問（FAQ）</h2>
      {faqs_joined}
    </section>

    <!-- 内部リンク -->
    <section class="related-links-section">
      <h2>🔗 あわせて読みたい！冬の徹底保湿・エイジングケア特集</h2>
      <div class="related-grid">
        <a href="/winter-manuka-honey" class="related-card">
          <h3>🍯 高純度マヌカハニーコスメ厳選10</h3>
          <p>野生マヌカ花の驚異的なMGO抗菌力と蜜膜！冬のひび割れ・皮むけ・ガサガサ角層を救う最高峰コスメ特集。</p>
        </a>
        <a href="/winter-prickly-pear" class="related-card">
          <h3>🌵 高保湿ウチワサボテンオイルコスメ厳選10</h3>
          <p>アルガンオイルの1.6倍のビタミンEと保水力！過酷な砂漠植物の生命力で冬のしぼみ肌をふっくら満水へ。</p>
        </a>
        <a href="/winter-allantoin" class="related-card">
          <h3>🌿 高保湿アラントインコスメ厳選10</h3>
          <p>冷風と暖房寒暖差で荒れ狂う角層を鎮静＆保水バリアで満たす！キュレル、ミノン、イハダまで徹底比較。</p>
        </a>
        <a href="/winter-azulene" class="related-card">
          <h3>💙 高保湿アズレンコスメ厳選10</h3>
          <p>寒暖差の赤ら顔とヒリつく真冬の敏感肌を青の鎮静バリアで包み込む！クレアス、ダーマファーム厳選。</p>
        </a>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <p>&copy; 2026-2027 Lumi Cosme (ルミコスメ) - 冬の乾燥対策・高保湿スキンケア専門ガイド</p>
    <p style="margin-top:0.5rem;">
      <a href="/">トップページ</a> | 
      <a href="/winter-calendula">カレンデュラコスメ</a> | 
      <a href="/winter-prickly-pear">ウチワサボテンオイル</a> | 
      <a href="/winter-manuka-honey">マヌカハニー</a> | 
      <a href="/winter-allantoin">アラントイン</a>
    </p>
  </footer>

</body>
</html>
"""

with open("winter-calendula.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated winter-calendula.html successfully!")
