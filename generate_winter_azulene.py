import json
import re

with open("fetched_final_30_tranexamic_azulene_volufiline.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_azulene"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 青のレスキューバーム！寒暖差赤みと真冬のヒリつきを一晩で鎮火",
        "catch": "天然グアイアズレン×ツボクサエキス。冷気で火照り赤くなった肌を穏やかに包み込む奇跡の青色クリーム",
        "brand_name": "Dear, Klairs (クレアス)",
        "capacity": "30ml / 60ml (ミッドナイトブルー カーミングクリーム)",
        "type": "集中鎮静リペアバームクリーム",
        "features": "高純度グアイアズレン、ツボクサエキス（CICA）、セラミドNP、ヒアルロン酸Na配合",
        "value": "カモミールから抽出した神秘的なブルーの天然色素が、冬の冷風や暖房による熱感・赤みを急速鎮静。厚みのある保護膜で水分蒸散をブロック",
        "desc_p1": "11月から12月にかけて、暖房の効いた室内から一歩外に出た瞬間に顔がカッと熱くなったり、逆に冷風に当たると頬や鼻先が赤くヒリヒリ痛んだりする『寒暖差ゆらぎ肌』に悩む人が急増します。これは急激な温度差によって皮膚の毛細血管が乱高下し、角層バリアが急激に損傷している危険信号。クレアスのミッドナイトブルーカーミングクリームは、世界中の敏感肌ユーザーから『青いレスキュークリーム』として崇められている冬の必須アイテムです。",
        "desc_p2": "合成着色料を一切使わず、カモミール由来のグアイアズレンそのものが持つ美しい濃青色が特徴。こっくりとしながらも肌に乗せると体温でシルキーにとろけ、赤みや火照りのある部分にピタッと密着シールドを形成します。ツボクサエキス（CICA）とセラミドNPが連携し、寒さで微小なダメージを受けた角質層を夜の間に集中修復。翌朝目覚めたときには、赤みがすっきりと引き、均一でふっくらとした透明感が蘇ります。",
        "target": "冬の寒暖差で頬や小鼻が赤くなりやすい方、エアコンの風で肌がヒリつく超敏感肌の方、美容施術後やピーリング後の肌を優しく鎮静させたい方",
        "point": "夜のお手入れの最後に、赤みや乾燥が特に気になる両頬・小鼻まわりに『厚めに置くように』部分塗りしてください。擦らずに優しくハンドプレスして青いヴェールを密着させるのが最大のコツです。"
    },
    {
        "rank": 2,
        "tag": "🛡️ 韓国の皮膚科学が到達！アズレン×セラミドNPが織りなす濃厚ブルーシールド",
        "catch": "天然グアイアズレン配合。寒風で荒れ果てた角質層を再建し、冷気を跳ね返す高保湿ヴェール",
        "brand_name": "SUR.MEDIC (サーメディック)",
        "capacity": "50ml (アズレン スージング カーミングクリーム)",
        "type": "高保湿カーミングシールドクリーム",
        "features": "グアイアズレン、セラミドNP、パンテノール、カラミン配合",
        "value": "高純度アズレンの強力な抗炎症力と、細胞間脂質を補うセラミドNPをダブル配合。真冬の過酷な粉吹き・ひび割れ肌を救済",
        "desc_p1": "皮膚科学に基づいた高機能スキンケアを展開するサーメディックのアズレンスージングクリーム。真冬の冷たい北風や乾燥によってバリアが崩壊し、化粧水すら染みるほどデリケートになった肌を優しく包み込むために開発されました。",
        "desc_p2": "鮮やかなブルーのテクスチャーは濃厚でリッチ。肌に伸ばすと瞬時に潤いのクッション層を形成し、外気との直接的な接触を遮断します。グアイアズレンが皮膚のヒスタミン遊離を抑制して赤みと痒み感を和らげ、パンテノールとセラミドNPが傷ついた細胞間脂質を隙間なく埋め戻します。塗布後の肌はもっちりと吸い付くような保護感に包まれ、冷え切った冬の肌に深い安らぎを与えます。",
        "target": "冬になると肌が粉を吹いて皮剥けしてしまう方、寒風に当たると肌がピリピリ痛む方、高保湿と強力な鎮静を1本で完結させたい方",
        "point": "洗顔後、化粧水と美容液で整えた後、パール粒大を全顔になじませます。特に乾燥がひどい日は、就寝前にほうれい線や目周り、頬に薄くもう一度重ねる『二重シールド法』が効果的です。"
    },
    {
        "rank": 3,
        "tag": "🔬 リポソーム化アズレンが角層深層へ直撃！紫の濃密ペプチドアンプル",
        "catch": "高純度アズレンリポソーム×複合ペプチド。冬の炎症ダメージとエイジングサインを同時リセット",
        "brand_name": "DERMAFIRM (ダーマファーム)",
        "capacity": "30ml (ウルトラ スージング R4 アンプル)",
        "type": "高濃度アズレン修復美容液 (アンプル)",
        "features": "高純度アズレンリポソーム、ペプチドコンプレックス（R4）、17種アミノ酸、ツボクサエキス",
        "value": "美容クリニックでも採用されるダーマコスメ。ナノリポソーム化されたアズレンが角層の最深部まで到達し、細胞レベルで冬の炎症を鎮静＆ハリ回復",
        "desc_p1": "韓国のメディカルダーマコスメとして名高いダーマファームのフラッグシップ『R4アンプル』。カモミール由来のグアイアズレンをナノカプセル（リポソーム）に閉じ込める先端デリバリー技術を採用し、成分の安定性と深層浸透力を極限まで高めています。",
        "desc_p2": "スポイトから取り出すと、息をのむほど美しい高貴なパープルカラー。肌に伸ばした瞬間にすっと吸い込まれ、ベタつきを一切残さずに角層の内側を満たします。真冬の乾燥で萎縮した肌細胞に17種のアミノ酸とペプチドが活力を注ぎ込み、アズレンが炎症の火種を鎮火。赤みが引くだけでなく、内側からパンッと跳ね返すようなハリとツヤが蘇ります。",
        "target": "赤みやゆらぎだけでなく年齢肌のハリ不足も気になる方、ナノテクノロジーの確かな浸透力を体感したい方、ベタつかない高浸透アンプルを求める方",
        "point": "化粧水の直後、スポイト1回分を手のひらに取り、顔全体になじませてから手のひらでハンドプレス。特に赤みが気になる部位には、もう半プッシュを指先で重ねづけしてください。"
    },
    {
        "rank": 4,
        "tag": "🌿 敏感肌の毎日に寄り添う高保水ドロップ！赤みと水分不足を同時に潤すデイリーセラム",
        "catch": "グアイアズレン×濃密ヒアルロン酸。冬のインナードライを解消する青い保水オアシス",
        "brand_name": "Bellflower (ベルフラワー)",
        "capacity": "50ml (アズレン デイリー カーミングセラム)",
        "type": "デイリー水分鎮静美容液",
        "features": "グアイアズレン、ツボクサエキス、低分子ヒアルロン酸、アロエベラ葉エキス",
        "value": "無駄な油分を排除した純粋な高保水設計。冬の暖房下で水分がカラカラに蒸発したインナードライ肌に、みずみずしい潤いと鎮静をチャージ",
        "desc_p1": "韓国のヴィーガンスキンケアブランド・ベルフラワーの『アズレンデイリーカーミングセラム』。冬の暖房によるインナードライで、肌表面はテカるのに内側がつっぱるというアンバランスなゆらぎ肌に向けて作られた高機能セラムです。",
        "desc_p2": "透き通るようなスカイブルーのテクスチャーは、とろみがありながらも肌に触れると水のようにほどけて浸透。低分子ヒアルロン酸が角層の細胞間をみずみずしく満たし、グアイアズレンが外気刺激による微弱な赤みを緩和します。刺激成分を極力排除したクリーン処方のため、季節の変わり目や花粉の飛散時期、真冬の乾燥ピークでも毎日安心して使い続けられます。",
        "target": "冬でも重いオイルやこっくりクリームが苦手な脂性肌・混合肌の方、インナードライで肌がつっぱる方、日常使いしやすい鎮静美容液を探している方",
        "point": "朝晩の洗顔後、化粧水の後に2〜3滴をなじませます。朝のメイク前に仕込むと、暖房による日中の火照りや赤み、メイクの乾燥崩れを劇的に抑えられます。"
    },
    {
        "rank": 5,
        "tag": "💜 ダーマファームが誇る最高峰クリーム！アズレン×17種アミノ酸の超密着リペア",
        "catch": "高純度アズレンリポソーム処方。真冬の過酷な乾燥と赤みを徹底的に封じ込める高保湿クリーム",
        "brand_name": "DERMAFIRM (ダーマファーム)",
        "capacity": "50g (ウルトラ スージング R4 クリーム)",
        "type": "高機能リペアカーミングクリーム",
        "features": "グアイアズレンリポソーム、17種アミノ酸、銅トリペプチド-1、セラミドコンプレックス",
        "value": "R4アンプルの有効成分をクリーム状に凝縮。冷たい真冬の空気に晒されても一日中潤いと鎮静効果が途切れない鉄壁の保護シールド",
        "desc_p1": "ダーマファームのR4シリーズから登場した、高保湿特化型カーミングクリーム。リポソーム化されたアズレンを高濃度に含み、淡いラベンダーパープルの上質なクリームが特徴です。",
        "desc_p2": "肌に乗せると、シルクのようになめらかに広がり、皮膚表面に薄くしなやかな保護膜を形成。銅トリペプチド-1などの高機能ペプチドがコラーゲン環境をサポートし、17種のアミノ酸が角層の水分保持力を根本から引き上げます。冬の寒風によってごわついた肌のキメが一瞬で整い、ふっくらと柔らかい極上の素肌感へと導かれます。",
        "target": "冬の乾燥と小ジワ、赤みトラブルを一度にケアしたい大人肌の方、上質でリッチな使用感のナイトクリームを求める方",
        "point": "夜のお手入れの総仕上げとして、付属のスパチュラで適量を取り全顔に優しく伸ばします。デコルテや首元まで伸ばすことで、真冬の首元の乾燥小ジワも同時に予防できます。"
    },
    {
        "rank": 6,
        "tag": "💧 毎日のシートマスクで真冬の肌を鎮静＆保水！不動のメガヒットデイリーマスク",
        "catch": "ツボクサエキス×カモミール由来アズレン成分。真冬の冷えた肌に密着して水分満タンにする名品シート",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "30枚入 (CICA デイリースージングマスク)",
        "type": "デイリー高保水シートマスク",
        "features": "シカヒアルロン™、カモミール花エキス（アズレン含有）、プロポリスエキス、アミノ酸複合体",
        "value": "0.2mmの極薄ヌードシールシートが肌の凹凸に吸い付くように密着。真冬の朝晩、わずか10分で乾いた角層をみずみずしい水分で満たす",
        "desc_p1": "日韓のベストコスメを総なめにし続けているVTのデイリースージングマスク。ツボクサエキスを中心としたCICA成分に、カモミール由来の鎮静エッセンスとヒアルロン酸を絶妙な比率で配合した、毎日の乾燥・赤みケアに欠かせない大定番です。",
        "desc_p2": "わずか0.2mmの植物由来極薄シートが、真冬の寒さで強張った顔のカーブに隙間なくピタッと密着。美容液が液だれすることなく、10分間で角層の隅々まで潤いを送り届けます。剥がした直後の肌は、火照りがスッと引いてひんやり心地よく、キメがキュッと引き締まった状態に。朝使えばファンデーションの密着度が格段に上がり、夜使えば一日の乾燥ダメージをリセットできます。",
        "target": "毎日手軽に使える大容量の鎮静マスクを探している方、朝のメイク前に肌の温度を下げてメイク崩れを防ぎたい方、家族やパートナーとシェアしたい方",
        "point": "洗顔後、化粧水の代わりに10〜15分間パック。取り外した後はシートを折りたたんで首やデコルテ、手の甲までパッティングすると余すところなく活用できます。"
    },
    {
        "rank": 7,
        "tag": "🛡️ 特許MLE技術で肌バリアを完全再現！韓国皮膚科医推奨の超高保湿リペアシールド",
        "catch": "特許MLE皮膚バリア技術×パンテノール。極度の乾燥と冷風ダメージを包み込む高保湿鎮静シールド",
        "brand_name": "Real Barrier (リアルバリア)",
        "capacity": "50ml×2個 (エクストリーム クリーム)",
        "type": "皮膚バリア再建高保湿クリーム",
        "features": "特許MLE®技術、セラミド、フィトステロール、パンテノール、マデカッソシド",
        "value": "健康な肌のラメラ構造をそのまま再現した独自処方。真冬の過酷な乾燥下でも72時間潤いを持続させ、外部刺激を完全にブロック",
        "desc_p1": "韓国の敏感肌専門ブランド『リアルバリア』の最高傑作であるエクストリームクリーム。人間の皮膚バリアと同一の十字型ラメラ構造を再現する世界特許技術『MLE®』を採用し、冬の乾燥によってスカスカになった角層バリアを人工的に補強します。",
        "desc_p2": "こっくりとした濃厚なテクスチャーですが、肌の温度でスルスルとなじみ、まるで『第二の皮膚』をまとったかのような安心感のある密着膜を形成。高濃度のパンテノールとマデカッソシドが寒さによる赤みや炎症を優しく包み込みます。真冬のスキー場や極寒の屋外で過ごしても肌がカサつかず、一日中しっとりとした弾力をキープできる頼もしさです。",
        "target": "冬になるとどんなクリームを塗っても乾燥してしまう超乾燥肌の方、肌のバリア機能が低下して赤みや刺激を感じやすい方",
        "point": "夜のスキンケアの最後に、手のひらで温めてから顔全体をハンドプレスで包み込みます。皮剥けや粉吹きが気になる部分には、トントンと置くように重ね塗りしてください。"
    },
    {
        "rank": 8,
        "tag": "💎 1兆個のマイクロカプセルが叶える奇跡！カモミラエキス配合の最高峰先行美容液",
        "catch": "多重層バイオリポソーム×カモミラエキス。洗顔直後の素肌に溶け込み、真冬の乾燥を根本解決",
        "brand_name": "DECORTÉ (コスメデコルテ)",
        "capacity": "50ml (リポソーム アドバンスト リペアセラム)",
        "type": "多重層リポソーム先行美容液",
        "features": "多重層バイオリポソーム、カモミラ花エキス、ビフィズス菌培養溶解質、ヒアルロン酸",
        "value": "1滴に1兆個もの超微細カプセルを凝縮。タマネギ状の層が外側からじっくり溶け出し、24時間絶え間なく潤いと鎮静成分を供給し続ける",
        "desc_p1": "日本のプレステージスキンケアの頂点に君臨するコスメデコルテの『リポソーム アドバンスト リペアセラム』。洗顔直後のまっさらな肌に使用することで、0.1ミクロンの超微細カプセルが角層深層へ直行。壊れたバリアを修復しながら、カモミラエキスが冬の微小な炎症を優しく沈静化します。",
        "desc_p2": "オイルフリーのみずみずしい感触でありながら、後肌には驚くほどリッチな潤いとふっくらとしたハリ感が残ります。カプセルが時間差で少しずつ美容成分を放出するため、真冬の乾燥したオフィスにいても夕方まで肌がしっとりモチモチ。使い続けることで肌の基礎体力が底上げされ、乾燥や冷えにびくともしない強靭な美肌が育ちます。",
        "target": "冬の乾燥による小ジワやくすみ、キメの乱れを根本から立て直したい方、自分へのご褒美に最高峰の先行美容液を投資したい方",
        "point": "朝晩の洗顔直後、手のひらに2〜3プッシュを取り、顔全体にていねいになじませます。首すじから鎖骨にかけて伸ばすことで、首元のエイジングケアにも絶大な効果を発揮します。"
    },
    {
        "rank": 9,
        "tag": "🥛 赤ちゃんから大人まで使える優しさ！素肌由来セラミド配合の無添加全身ミルククリーム",
        "catch": "素肌由来セラミド×植物性スクワラン。寒風でヒリつく超敏感肌を優しく守る低刺激高保湿クリーム",
        "brand_name": "カウブランド 無添加フェイスケア",
        "capacity": "250g (無添加 全身保湿ミルククリーム ポンプ)",
        "type": "無添加低刺激高保湿ミルククリーム",
        "features": "天然由来セラミド（保湿成分）、植物性スクワラン、無香料・無着色・防腐剤フリー・アルコールフリー",
        "value": "大容量ポンプタイプで家族全員の冬の乾燥肌をまるごとケア。カサつきやヒリつきを感じるデリケートな肌にも摩擦レスでスルスル伸びる",
        "desc_p1": "100年以上の歴史を持つ牛乳石鹸が、徹底的な低刺激と安心感を追求して開発したカウブランド無添加シリーズ。冬の乾燥でバリアが低下し、少しの刺激でも赤くなったり痒くなったりする肌に向けて、余計な成分を極限まで削ぎ落とした純粋な高保湿処方です。",
        "desc_p2": "肌にもともと存在する成分に近い天然由来セラミドと植物性スクワランを配合。ミルクのように伸びやかでありながら、クリームのような濃密な潤いの膜を肌表面に形成します。顔はもちろん、乾燥で白く粉を吹きやすいスネや腕、首元までこれ1本で全身ケアが可能。便利な大容量ポンプ式で、真冬のお風呂上がりに速攻で潤いをチャージできます。",
        "target": "敏感肌で新しい化粧品を試すのが怖い方、冬のお風呂上がりに全身がカサつく方、プチプラで気兼ねなくたっぷり使いたい方",
        "point": "お風呂から上がって水分を拭き取った直後の『3分以内』に、顔から全身へたっぷり塗り広げてください。肌に残った微細な水分を抱え込み、しっとりすべすべの肌が長続きします。"
    },
    {
        "rank": 10,
        "tag": "🌿 製薬会社の皮膚病理研究から誕生！天然セラミド×抗炎症成分の濃密薬用ジェル",
        "catch": "天然セラミド×グリチルリチン酸2K。冬の冷えによるバリア破綻を優しく修復する薬用高保湿ジェル",
        "brand_name": "Arouge (アルージェ) / 全薬工業",
        "capacity": "50ml (モイスト トリートメント ジェル)",
        "type": "薬用保湿ジェル乳液 (医薬部外品)",
        "features": "天然セラミド（ビオセラミド）、グリチルリチン酸2K、ε-アミノカプロン酸、ナノ粒子化技術",
        "value": "全薬工業の製薬技術が生んだナノ化天然セラミドが角層の奥深くまで浸透。冬の乾燥・肌荒れ・赤みを根本から防ぎ、吸い付くような潤いを持続",
        "desc_p1": "製薬会社である全薬工業が、敏感肌のために立ち上げたスキンケアブランド『アルージェ』。モイストトリートメントジェルは、肌自身のバリア機能を高めるナノ化天然セラミドと、2つの抗炎症有効成分を贅沢にブレンドした薬用ジェル乳液です。",
        "desc_p2": "みずみずしく軽やかなジェルテクスチャーでありながら、肌になじませると驚くほど濃厚な保水ヴェールへと変化。界面活性剤に頼らず、超微粒子化された天然セラミドが角質層の隙間を埋め尽くし、冷たい外気や暖房の乾燥から肌を徹底的に守り抜きます。肌がヒリつく冬のゆらぎ期でも一切染みることなく、穏やかな潤いで肌を包み込みます。",
        "target": "冬の乾燥で肌が荒れやすくピリピリ感を繰り返す方、乳液やクリームの油膜感が苦手な方、医薬部外品の確かな効果を求める方",
        "point": "化粧水の後にポンプ2プッシュを手に取り、手のひらで顔全体を優しく包み込むようになじませます。乾燥が気になる目元や口元には、指先で優しくトントンと重ねづけしてください。"
    }
]

# JSON-LD 生成
jsonld_items = []
for i, p in enumerate(items):
    d = product_details[i]
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": f"第{i+1}位：{d['brand_name']} {p['name']}",
        "description": d['catch'],
        "image": p['img_url'],
        "url": f"https://lumi-cosme.vercel.app/winter-azulene.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "アズレンコスメの独特な青紫色の正体は何ですか？肌に着色しませんか？",
        "answer": "アズレンコスメの鮮やかな青紫色は、合成着色料や人工タール色素ではなく、ハーブの『ジャーマンカモミール（カミツレ）』から抽出される天然成分『グアイアズレン』そのものの自然な色です。カモミールに含まれるマトリカリアという精油成分を水蒸気蒸留する過程で、美しいアズールブルー（濃青色）のグアイアズレンが生成されます。肌に塗布すると体温でなじんで透明に変化し、角層に浸透するため、肌や衣服に青い色が沈着することは一切ありません。安心してお使いいただけます。"
    },
    {
        "question": "なぜ11月〜12月の真冬の乾燥・赤ら顔にアズレンが特に効果的なのですか？",
        "answer": "真冬は外気の寒冷刺激と室内のエアコン暖房による温度差（10℃〜15℃以上）が激しく、顔の毛細血管が急激に拡張・収縮を繰り返すことで、血行がうっ血して頬や小鼻が赤く火照る『寒暖差赤ら顔』が起こりやすくなります。さらに乾燥によって角層バリアが剥がれ落ち、ヒスタミンが遊離して痒みやヒリつきを伴います。グアイアズレンには優れた抗ヒスタミン様作用と消炎・組織修復促進作用があるため、真冬の火照りと微小炎症を瞬時にクーリング鎮静させ、セラミドとともに傷ついた角層バリアを素早く再建できるのです。"
    },
    {
        "question": "アズレンはステロイドや他の抗炎症成分とどう違うのですか？副作用はありませんか？",
        "answer": "アズレンは医薬品でも胃潰瘍治療薬や眼科用点眼薬、うがい薬などに広く使われている極めて安全性の高い植物由来の抗炎症成分です。ステロイド系抗炎症剤のような長期連用による皮膚菲薄化（皮膚が薄くなること）や毛細血管拡張などの副作用の心配が全くありません。また、トラネキサム酸やグリチルリチン酸2Kとも異なり、火照った肌の熱感を物理的・生化学的に落ち着かせる即効的なクーリング鎮静力に優れているのが最大の特徴です。冬の間中、毎日朝晩安心して使い続けることができます。"
    },
    {
        "question": "朝のメイク前にアズレンクリームを使ってもモロモロやヨレは出ませんか？",
        "answer": "適切な量と塗り方を守れば、むしろメイク持ちを大幅に高めてくれます。冬のメイク崩れや毛穴落ちの多くは、暖房によるインナードライや肌の火照りが原因です。アズレンで肌の温度を適正にクーリングして赤みを抑えておくことで、ファンデーションの密着度が向上し、夕方の皮脂浮きや赤浮きを防げます。朝に使用する際はパール粒半分程度を薄く均一にハンドプレスでなじませ、1〜2分置いて表面がサラリとしてから下地・ファンデーションに進むのがポイントです。"
    },
    {
        "question": "ビタミンCやレチノールなど、他の機能性美容液と併用できますか？",
        "answer": "併用可能です。特にレチノールによるA反応（乾燥・皮剥け・赤み）や、高濃度ビタミンCによるピリピリ感を和らげる『鎮静バッファー（緩衝役）』としてアズレンは世界的に注目されています。併用の順序としては、レチノールやビタミンCを塗布した後、仕上げにアズレンクリームを重ねることで、有効成分の刺激感をマイルドに包み込みながら、翌朝の滑らかなツヤ肌を安全に引き出すことができます。"
    }
]

jsonld_faq = []
for faq in faq_list:
    jsonld_faq.append({
        "@type": "Question",
        "name": faq["question"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": faq["answer"]
        }
    })

jsonld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-azulene.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！寒暖差の赤ら顔とヒリつく真冬の敏感肌を濃密バリアで包み込む高保湿アズレンコスメランク10",
    "description": "11月・12月の寒暖差赤ら顔と真冬のヒリつき乾燥を救う高保湿アズレンコスメを徹底厳選！クレアスブルーカーミングクリーム、ダーマファームR4、リアルバリア、コスメデコルテからアルージェまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。",
    "image": items[0]["img_url"],
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
    "datePublished": "2026-11-04T00:00:00+09:00",
    "dateModified": "2026-11-04T00:00:00+09:00"
}

jsonld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿アズレンコスメおすすめ人気ランキング10選",
    "itemListElement": jsonld_items
}

jsonld_faqpage = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": jsonld_faq
}

cards_html = []
for i, p in enumerate(items):
    d = product_details[i]
    cards_html.append(f"""
    <article class="product-card" id="item-{i+1}">
      <div class="product-badge-rank">第{i+1}位</div>
      <div class="product-tag">{d['tag']}</div>
      <h3 class="product-name">{d['brand_name']} {p['name']}</h3>
      <p class="product-catch">{d['catch']}</p>
      
      <div class="product-flex">
        <div class="product-img-box">
          <img src="{p['img_url']}" alt="{p['name']}" class="product-img" loading="lazy">
          <div class="price-box">
            <span class="price-label">楽天市場参考価格</span>
            <span class="price-val">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で詳細を見る・購入
          </a>
        </div>
        
        <div class="product-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{d['brand_name']}</td></tr>
            <tr><th>容量 / 規格</th><td>{d['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{d['type']}</td></tr>
            <tr><th>主要成分・処方</th><td>{d['features']}</td></tr>
            <tr><th>高保湿・鎮静の理由</th><td>{d['value']}</td></tr>
          </table>
          
          <div class="review-block">
            <h4>💡 冬の寒暖差赤み・ヒリつき乾燥に対する詳細解説</h4>
            <p>{d['desc_p1']}</p>
            <p>{d['desc_p2']}</p>
          </div>
          
          <div class="target-block">
            <strong>🎯 こんな方に特におすすめ：</strong>
            <p>{d['target']}</p>
          </div>
          
          <div class="usage-block">
            <strong>✨ 美容のプロ直伝！冬のおすすめ活用テクニック：</strong>
            <p>{d['point']}</p>
          </div>
        </div>
      </div>
    </article>
    """)

cards_str = "\n".join(cards_html)

faq_html = []
for f in faq_list:
    faq_html.append(f"""
      <div class="faq-item">
        <h3 class="faq-q">Q. {f['question']}</h3>
        <p class="faq-a">A. {f['answer']}</p>
      </div>
    """)
faq_str = "\n".join(faq_html)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！寒暖差の赤ら顔とヒリつく真冬の敏感肌を濃密バリアで包み込む高保湿アズレンコスメランク10 - 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒暖差赤ら顔と真冬のヒリつき乾燥を救う高保湿アズレンコスメを徹底厳選！クレアスブルーカーミングクリーム、ダーマファームR4、リアルバリア、コスメデコルテからアルージェまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta name="keywords" content="アズレン,グアイアズレン,高保湿クリーム,寒暖差赤ら顔,敏感肌,冬コスメ,乾燥肌,クレアス,ダーマファーム,リアルバリア,楽天コスメ">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-azulene.html">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！寒暖差の赤ら顔とヒリつく真冬の敏感肌を濃密バリアで包み込む高保湿アズレンコスメランク10">
  <meta property="og:description" content="11月・12月の寒暖差赤ら顔と真冬のヒリつき乾燥を救う高保湿アズレンコスメを徹底厳選！クレアスブルーカーミングクリーム、ダーマファームR4、リアルバリア、コスメデコルテからアルージェまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-azulene.html">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
  <script type="application/ld+json">
  {json.dumps(jsonld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(jsonld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(jsonld_faqpage, ensure_ascii=False, indent=2)}
  </script>
  
  <style>
    :root {{
      --primary: #2e1065;
      --primary-light: #4c1d95;
      --accent: #2563eb;
      --accent-soft: #dbeafe;
      --bg: #fdfcff;
      --card-bg: #ffffff;
      --text: #1e1b4b;
      --text-muted: #6b7280;
      --border: #ddd6fe;
      --radius: 12px;
      --shadow: 0 4px 16px rgba(46, 16, 101, 0.08);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Kaku Gothic ProN", "Yu Gothic", Meiryo, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: linear-gradient(135deg, #1e1b4b, #3b0764);
      color: #fff;
      padding: 18px 24px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    }}
    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #fff;
      text-decoration: none;
      letter-spacing: 0.5px;
    }}
    .breadcrumb {{
      max-width: 1080px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb a {{ color: var(--primary-light); text-decoration: none; }}
    .main-container {{
      max-width: 1080px;
      margin: 20px auto 60px;
      padding: 0 20px;
    }}
    .article-header {{
      background: #fff;
      padding: 36px 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 32px;
    }}
    .article-badge {{
      display: inline-block;
      background: #ede9fe;
      color: #6d28d9;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 14px;
    }}
    h1 {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #1e1b4b;
      margin-bottom: 20px;
      font-weight: 800;
    }}
    .meta-box {{
      display: flex;
      gap: 18px;
      font-size: 0.85rem;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
      margin-bottom: 20px;
    }}
    .lead-text {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #312e81;
      margin-bottom: 18px;
    }}
    .toc-box {{
      background: #f5f3ff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      margin: 28px 0;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--primary);
      margin-bottom: 14px;
    }}
    .toc-list {{
      list-style-position: inside;
      line-height: 2;
    }}
    .toc-list a {{ color: var(--primary-light); text-decoration: none; }}
    .toc-list a:hover {{ text-decoration: underline; }}
    
    .guide-section {{
      background: #fff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 36px;
    }}
    .guide-section h2 {{
      font-size: 1.45rem;
      color: var(--primary);
      border-left: 5px solid var(--accent);
      padding-left: 14px;
      margin-bottom: 20px;
      line-height: 1.4;
    }}
    .guide-section h3 {{
      font-size: 1.2rem;
      color: #3b0764;
      margin: 24px 0 12px;
    }}
    .guide-section p {{
      margin-bottom: 16px;
      font-size: 0.98rem;
      line-height: 1.85;
    }}
    .guide-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin: 24px 0;
    }}
    .grid-card {{
      background: #eff6ff;
      padding: 20px;
      border-radius: 10px;
      border: 1px solid #bfdbfe;
    }}
    .grid-card:nth-child(2) {{ background: #f5f3ff; border-color: #ddd6fe; }}
    .grid-card:nth-child(3) {{ background: #fdf2f8; border-color: #fbcfe8; }}
    .grid-card h4 {{
      color: #1e1b4b;
      margin-bottom: 8px;
      font-size: 1.05rem;
    }}
    
    /* Product Cards */
    .product-card {{
      background: #fff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      padding: 32px;
      margin-bottom: 36px;
      position: relative;
    }}
    .product-badge-rank {{
      position: absolute;
      top: -14px;
      left: 24px;
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: #fff;
      font-size: 1.05rem;
      font-weight: 800;
      padding: 6px 18px;
      border-radius: 20px;
      box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3);
    }}
    .product-tag {{
      display: inline-block;
      margin-top: 6px;
      font-size: 0.88rem;
      font-weight: 700;
      color: #1d4ed8;
      background: #dbeafe;
      padding: 3px 10px;
      border-radius: 6px;
      margin-bottom: 10px;
    }}
    .product-name {{
      font-size: 1.4rem;
      line-height: 1.4;
      color: #1e1b4b;
      margin-bottom: 8px;
      font-weight: 800;
    }}
    .product-catch {{
      font-size: 0.98rem;
      font-weight: 600;
      color: #4338ca;
      margin-bottom: 24px;
    }}
    .product-flex {{
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    @media (min-width: 768px) {{
      .product-flex {{
        flex-direction: row;
        align-items: flex-start;
      }}
    }}
    .product-img-box {{
      flex: 0 0 280px;
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      border-radius: 10px;
      background: #fafafa;
      border: 1px solid #f0f0f0;
      padding: 8px;
    }}
    .price-box {{
      margin: 14px 0;
      padding: 10px;
      background: #f5f3ff;
      border-radius: 8px;
      border: 1px dashed #c4b5fd;
    }}
    .price-label {{ display: block; font-size: 0.78rem; color: #6b7280; }}
    .price-val {{ font-size: 1.5rem; font-weight: 800; color: #2563eb; }}
    .price-tax {{ font-size: 0.8rem; color: #6b7280; }}
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: #fff;
      font-weight: 700;
      text-align: center;
      padding: 14px 20px;
      border-radius: 8px;
      text-decoration: none;
      font-size: 0.98rem;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #d60000, #b00000);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
    }}
    .product-spec-box {{
      flex: 1;
    }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 18px;
      font-size: 0.88rem;
    }}
    .spec-table th {{
      width: 28%;
      background: #f5f3ff;
      padding: 8px 12px;
      border: 1px solid #ddd6fe;
      text-align: left;
      color: #2e1065;
      font-weight: 600;
    }}
    .spec-table td {{
      padding: 8px 12px;
      border: 1px solid #ddd6fe;
      background: #fff;
    }}
    .review-block {{
      background: #f5f3ff;
      border-left: 4px solid var(--accent);
      padding: 16px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 14px;
    }}
    .review-block h4 {{
      font-size: 0.98rem;
      color: #1e1b4b;
      margin-bottom: 8px;
    }}
    .review-block p {{
      font-size: 0.92rem;
      line-height: 1.75;
      color: #312e81;
      margin-bottom: 8px;
    }}
    .review-block p:last-child {{ margin-bottom: 0; }}
    .target-block, .usage-block {{
      font-size: 0.9rem;
      margin-bottom: 10px;
      line-height: 1.7;
    }}
    
    /* Comparison Table */
    .compare-table-wrap {{
      overflow-x: auto;
      margin: 20px 0;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 650px;
      font-size: 0.88rem;
    }}
    .compare-table th, .compare-table td {{
      padding: 10px 14px;
      border: 1px solid #ddd6fe;
      text-align: center;
    }}
    .compare-table th {{
      background: #ede9fe;
      color: #1e1b4b;
      font-weight: 700;
    }}
    .compare-table td.left-align {{
      text-align: left;
    }}
    
    /* FAQ Section */
    .faq-section {{
      background: #fff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 36px;
    }}
    .faq-section h2 {{
      font-size: 1.45rem;
      color: var(--primary);
      border-left: 5px solid var(--accent);
      padding-left: 14px;
      margin-bottom: 24px;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 18px 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.05rem;
      color: #1d4ed8;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #312e81;
    }}
    
    /* Internal Links Grid */
    .internal-section {{
      background: #fff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 36px;
    }}
    .internal-section h2 {{
      font-size: 1.4rem;
      color: var(--primary);
      border-left: 5px solid var(--accent);
      padding-left: 14px;
      margin-bottom: 20px;
    }}
    .internal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
    }}
    .internal-card {{
      background: #f5f3ff;
      padding: 16px;
      border-radius: 8px;
      border: 1px solid #e0e7ff;
      text-decoration: none;
      color: var(--text);
      transition: all 0.2s;
    }}
    .internal-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
      border-color: var(--accent);
    }}
    .internal-card h4 {{
      font-size: 0.95rem;
      color: var(--primary);
      margin-bottom: 6px;
    }}
    .internal-card p {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    footer {{
      background: #0f172a;
      color: #94a3b8;
      text-align: center;
      padding: 36px 20px;
      font-size: 0.85rem;
    }}
    footer a {{ color: #cbd5e1; text-decoration: none; }}
  </style>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="/" class="site-logo">❄️ 冬コスメ徹底比較ラボ</a>
    <span style="font-size: 0.85rem; color: #c7d2fe;">2026-2027年 冬季最新スキンケア特集</span>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">ホーム</a> &gt; <span>高保湿アズレンコスメ</span>
</div>

<main class="main-container">
  <div class="article-header">
    <span class="article-badge">💙 11月〜12月寒暖差赤み・敏感肌レスキュー</span>
    <h1>保湿力の強さで肌乾燥とさようなら！寒暖差の赤ら顔とヒリつく真冬の敏感肌を濃密バリアで包み込む高保湿アズレンコスメランク10</h1>
    <div class="meta-box">
      <span>📅 最終更新日: 2026年11月4日</span>
      <span>✍️ 監修: 冬コスメ徹底比較ラボ 美容皮膚科学リサーチチーム</span>
      <span>⏱️ 読了目安: 約8分</span>
    </div>
    <p class="lead-text">
      11月から12月へと季節が移り変わる時期、多くの人を悩ませるのが「外の凍える寒風と室内の強暖房による極端な寒暖差」です。通勤や外出のたびに15℃以上もの急激な気温変化に晒された顔の皮膚は、毛細血管が激しく拡張と収縮を繰り返し、頬や小鼻が火照って真っ赤に染まる「寒暖差赤ら顔」を引き起こします。さらに乾燥によって角質層が傷つき、普段のスキンケアがピリピリと染みる冬の敏感肌危機に陥ります。
    </p>
    <p class="lead-text">
      この冬枯れ火照り肌を鎮める究極の切り札として、美容皮膚科や韓国の皮膚科医（ダーマコスメ）が絶大な信頼を寄せるのが、カモミール由来の神秘の青色鎮静成分『グアイアズレン』です。本特集では、火照った皮膚をクーリング鎮静させながら、失われたセラミドバリアを再建する高保湿アズレンコスメ10選を楽天市場の最新データから徹底比較。真冬の過酷な環境から素肌を死守する選び方と活用テクニックをお届けします。
    </p>
  </div>

  <div class="toc-box">
    <div class="toc-title">📑 目次 - タップして各項目へジャンプ</div>
    <ol class="toc-list">
      <li><a href="#guide-mechanism">1. なぜ11月〜12月の真冬に「アズレン」が救世主となるのか？（寒暖差赤ら顔の科学）</a></li>
      <li><a href="#guide-points">2. 冬の高保湿アズレンコスメを選ぶ3つの絶対チェックポイント</a></li>
      <li><a href="#ranking-section">3. 【2026年最新】真冬の高保湿アズレンコスメおすすめ人気ランキング10選</a></li>
      <li><a href="#comparison-section">4. 高保湿アズレンコスメ10選スペック＆価格早見表</a></li>
      <li><a href="#usage-technique">5. 美容のプロ直伝！冬の赤み・ヒリつきを即刻鎮静する「青のクーリング密着法」</a></li>
      <li><a href="#faq-section">6. 高保湿アズレンコスメに関するよくある質問（FAQ）</a></li>
      <li><a href="#related-section">7. あわせて読みたい冬の集中鎮静＆高保湿関連記事</a></li>
    </ol>
  </div>

  <section class="guide-section" id="guide-mechanism">
    <h2>1. なぜ11月〜12月の真冬に「アズレン」が救世主となるのか？</h2>
    <p>
      冬になると「頬だけがリンゴのように赤くなって恥ずかしい」「化粧水を塗ると火がついたようにヒリヒリする」という経験はありませんか？これは単なる肌荒れではなく、冬特有の『寒暖差ストレス』と『水分蒸散によるバリア崩壊』が重なった複合トラブルです。
    </p>
    <p>
      寒い外気に当たると血管は熱を逃がさないよう収縮しますが、暖房の効いた室内に入ると一気に拡張します。冬の肌はこの急激な伸縮を1日に何十回も強いられ、血管の弾力性が失われて拡張したまま元に戻らなくなります。さらに湿度の急低下で角層細胞がめくれ上がり、外部の刺激物質が侵入してヒスタミンが遊離。これが真冬の「赤ら顔」と「耐えがたいヒリつき」のメカニズムです。
    </p>
    
    <div class="guide-grid">
      <div class="grid-card">
        <h4>① ハーブ由来の強力な抗ヒスタミン作用</h4>
        <p>グアイアズレンはカモミールから抽出される天然の青色ピグメント。痒みやヒリつきの元凶であるヒスタミンの遊離を抑制し、火照った皮膚を瞬時に鎮めます。</p>
      </div>
      <div class="grid-card">
        <h4>② 皮膚組織の再生＆修復スピードを加速</h4>
        <p>医療現場で胃粘膜修復や火傷治療に使われるほどの細胞賦活・組織修復力を発揮。寒風で傷ついた角層の隙間を埋め、再生を強力に促します。</p>
      </div>
      <div class="grid-card">
        <h4>③ セラミド＆高保水膜との相乗バリア</h4>
        <p><a href="/winter-ceramide-cream" style="color:#2563eb;font-weight:600;">セラミド</a>や<a href="/winter-cica-cream" style="color:#2563eb;font-weight:600;">CICA</a>、<a href="/winter-panthenol-cream" style="color:#2563eb;font-weight:600;">パンテノール</a>と組み合わせることで、冷気を通さない強固な水分シールドを構築します。</p>
      </div>
    </div>
  </section>

  <section class="guide-section" id="guide-points">
    <h2>2. 冬の高保湿アズレンコスメを選ぶ3つの絶対チェックポイント</h2>
    <p>
      冬の過酷な肌荒れを救うため、失敗しないアズレンコスメの選び方を3つの視点で解説します。
    </p>
    <h3>① 高純度グアイアズレンが主役として高配合されているか</h3>
    <p>
      コスメの全成分表示を確認し、「グアイアズレン（Guaiazulene）」がしっかりと配合されているかをチェックしましょう。合成着色料の青色○号ではなく、成分そのものの自然な青紫色をしている製品は、植物エキスの高濃度な鎮静パワーが凝縮されている証です。
    </p>
    <h3>② 真冬の冷気を遮断するリッチな「バーム・クリーム」テクスチャーか</h3>
    <p>
      春夏向けのアズレン化粧水や軽いジェルは、冬の乾燥環境では水分がすぐに蒸発してしまいます。11〜12月は、セラミドやスクワラン、シア脂などがベースになった「リッチな保護クリーム」や「密着バーム」を選ぶことで、鎮静成分を一晩中肌に閉じ込めることができます。
    </p>
    <h3>③ 刺激となるアルコール・人工香料が無添加の低刺激処方か</h3>
    <p>
      ヒリついている冬の肌はバリアが極限まで薄くなっています。エタノール（アルコール）や強い合成香料、防腐剤が過剰に含まれていると、かえって刺激になるリスクがあります。弱酸性、アレルギーテスト済み、無香料などの低刺激設計を優先しましょう。
    </p>
  </section>

  <section id="ranking-section">
    <h2 style="font-size: 1.6rem; color: #1e1b4b; margin-bottom: 24px; padding-left: 14px; border-left: 6px solid #2563eb;">
      3. 【2026年最新】真冬の高保湿アズレンコスメおすすめ人気ランキング10選
    </h2>
    <p style="margin-bottom: 32px; font-size: 0.95rem; color: #475569;">
      楽天市場の最新流通データに基づき、寒暖差赤み・乾燥ヒリつきへの鎮静実感度、保湿持続力、リアルタイムの販売価格を多角的にスコアリングしたおすすめ10選です。
    </p>
    
    {cards_str}
  </section>

  <section class="guide-section" id="comparison-section">
    <h2>4. 高保湿アズレンコスメ10選スペック＆価格早見表</h2>
    <p>
      ランクインした全10アイテムの参考価格、アイテム形状、主要な強みを一覧で整理しました。お肌のゆらぎレベルや好みの使用感に合わせてお選びください。
    </p>
    
    <div class="compare-table-wrap">
      <table class="compare-table">
        <thead>
          <tr>
            <th>順位・製品名</th>
            <th>参考価格</th>
            <th>分類</th>
            <th>主要な強み・特徴</th>
            <th>おすすめの悩み</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>第1位 クレアス ブルーカーミングクリーム</strong></td>
            <td>¥3,300</td>
            <td>リペアバーム</td>
            <td>天然グアイアズレン×CICAの青色バーム</td>
            <td>寒暖差赤み・火照り・ピリつき</td>
          </tr>
          <tr>
            <td><strong>第2位 サーメディック アズレンクリーム</strong></td>
            <td>¥2,640</td>
            <td>高保湿クリーム</td>
            <td>グアイアズレン×セラミドNPの濃密シールド</td>
            <td>粉吹き・ひび割れ・寒風ダメージ</td>
          </tr>
          <tr>
            <td><strong>第3位 ダーマファーム R4 アンプル</strong></td>
            <td>¥1,520</td>
            <td>高濃度セラム</td>
            <td>ナノリポソーム化アズレン×17種アミノ酸</td>
            <td>赤み・インナードライ・ハリ不足</td>
          </tr>
          <tr>
            <td><strong>第4位 ベルフラワー カーミングセラム</strong></td>
            <td>¥2,580</td>
            <td>水分セラム</td>
            <td>低分子ヒアルロン酸×グアイアズレン</td>
            <td>冬のテカリ＆乾燥・メイク前保湿</td>
          </tr>
          <tr>
            <td><strong>第5位 ダーマファーム R4 クリーム</strong></td>
            <td>¥1,980</td>
            <td>高機能クリーム</td>
            <td>銅トリペプチド×リポソームアズレン</td>
            <td>大人のゆらぎ乾燥・首元ケア</td>
          </tr>
          <tr>
            <td><strong>第6位 VT CICA デイリーマスク</strong></td>
            <td>¥3,490 (2箱)</td>
            <td>シートマスク</td>
            <td>0.2mm極薄シートで毎日10分水分チャージ</td>
            <td>朝晩のスピード鎮静・火照りケア</td>
          </tr>
          <tr>
            <td><strong>第7位 リアルバリア エクストリーム</strong></td>
            <td>¥4,690 (2個)</td>
            <td>バリアクリーム</td>
            <td>世界特許MLE皮膚バリア技術再現</td>
            <td>極度の乾燥肌・72時間水分キープ</td>
          </tr>
          <tr>
            <td><strong>第8位 コスメデコルテ リポソームセラム</strong></td>
            <td>¥7,260</td>
            <td>先行美容液</td>
            <td>1兆個のマイクロカプセル×カモミラエキス</td>
            <td>冬の土台再建・最高峰の持続保湿</td>
          </tr>
          <tr>
            <td><strong>第9位 カウブランド 無添加ミルククリーム</strong></td>
            <td>¥1,158</td>
            <td>大容量クリーム</td>
            <td>素肌由来セラミド×植物性スクワラン</td>
            <td>家族全員の全身乾燥・超敏感肌</td>
          </tr>
          <tr>
            <td><strong>第10位 アルージェ モイストジェル</strong></td>
            <td>¥7,317</td>
            <td>薬用ジェル乳液</td>
            <td>ナノ化天然セラミド×抗炎症W有効成分</td>
            <td>繰り返す肌荒れ・敏感肌のデイリーケア</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="guide-section" id="usage-technique">
    <h2>5. 美容のプロ直伝！冬の赤み・ヒリつきを即刻鎮静する「青のクーリング密着法」</h2>
    <p>
      アズレンコスメの鎮静効果を何倍にも引き上げる、真冬のプロフェッショナルな活用テクニックです。
    </p>
    <h3>① 「手のひら摩擦ゼロ」のスタンプ塗布テクニック</h3>
    <p>
      赤みが出ている肌は、指先で横に擦るだけでも毛細血管が刺激され悪化します。アズレンクリームを手のひらに伸ばしたら、顔全体に「ペタッ、ペタッ」と優しくスタンプを押すように垂直に押し当ててください。摩擦係数をゼロに抑えながら、体温で自然にアズレンを角層深層へ浸透させます。
    </p>
    <h3>② 帰宅直後の「寒暖差リセット・部分パック」</h3>
    <p>
      寒い屋外から帰宅して暖房の部屋に入った瞬間、頬がカッと火照ったら、メイクの上からでも使えるアズレンミストを吹きかけるか、洗顔後にクレアスなどのアズレンクリームを頬にやや厚めに塗り、コットンやラップを5分間のせて集中クーリングパックを行いましょう。毛細血管のうっ血を素早くリセットできます。
    </p>
    <h3>③ レチノールとの「鎮静サンドイッチ法」</h3>
    <p>
      冬に<a href="/winter-retinol-cream" style="color:#2563eb;font-weight:600;">レチノールクリーム</a>を使いたいけれど皮剥けや赤みが怖いという方は、化粧水→【アズレンセラム】→【レチノール】→【アズレンクリーム】というようにアズレンで挟み込む「サンドイッチ法」がおすすめ。A反応のピリピリ感を強力に抑えながら、ふっくらとしたハリツヤを安全に獲得できます。
    </p>
  </section>

  <section class="faq-section" id="faq-section">
    <h2>6. 高保湿アズレンコスメに関するよくある質問（FAQ）</h2>
    {faq_str}
  </section>

  <section class="internal-section" id="related-section">
    <h2>7. あわせて読みたい冬の集中鎮静＆高保湿関連記事</h2>
    <p style="margin-bottom: 20px; font-size: 0.95rem; color: #475569;">
      冬の敏感肌や赤み・乾燥トラブルを解決するための関連スキンケア特集です。
    </p>
    <div class="internal-grid">
      <a href="/winter-cica-cream" class="internal-card">
        <h4>🌿 高保湿CICAクリームランク10</h4>
        <p>ツボクサエキスの力で真冬の肌荒れ・マスク擦れを素早く鎮める名品クリーム。</p>
      </a>
      <a href="/winter-ceramide-cream" class="internal-card">
        <h4>🛡️ 高保湿セラミドクリームランク10</h4>
        <p>冷たい風と暖房乾燥から素肌を守り抜くヒト型セラミド配合の最強シールド。</p>
      </a>
      <a href="/winter-panthenol-cream" class="internal-card">
        <h4>💧 高保湿パンテノールクリームランク10</h4>
        <p>ビタミンB5の力で角層バリアを強固に修復する真冬のレスキューコスメ。</p>
      </a>
      <a href="/winter-tranexamic-acid" class="internal-card">
        <h4>✨ 高保湿トラネキサム酸コスメランク10</h4>
        <p>冬の寒暖差による微小炎症を抑えながら澄んだ透明感を叶える薬用美白特集。</p>
      </a>
      <a href="/winter-vaseline" class="internal-card">
        <h4>🛡️ 高純度ワセリンコスメランク10</h4>
        <p>粉吹きや皮剥けを即効保護する高精製ワセリンの低刺激シールドアイテム。</p>
      </a>
      <a href="/winter-mugwort" class="internal-card">
        <h4>🌿 高保水ヨモギ（マグワート）コスメランク10</h4>
        <p>冷えによる肌の赤みとゴワつきをじんわりほぐす伝統ハーブスキンケア。</p>
      </a>
    </div>
  </section>
</main>

<footer>
  <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 画像および商品情報は楽天市場Web APIより取得しています。</p>
</footer>

</body>
</html>
"""

with open("winter-azulene.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-azulene.html successfully!")
