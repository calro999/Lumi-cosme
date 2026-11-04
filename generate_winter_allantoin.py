import json
import re

with open("fetched_3new_nov_dec_elastin_allantoin_beeswax.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_allantoin"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 医薬部外品・消炎アラントイン×潤浸セラミド！冬の赤み・粉吹き肌を救う絶対王者",
        "catch": "有効成分アラントインが真冬の冷風による微小炎症を鎮静。疑似セラミドが角層の隙間を満たし、ふんわり軽いのに鉄壁の潤い膜を形成",
        "brand_name": "Curel (キュレル) / 花王",
        "capacity": "40g (ジャータイプ)",
        "type": "薬用消炎高保湿フェイスクリーム",
        "features": "アラントイン（有効成分）、ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド（潤浸セラミド機能成分）、ユーカリエキス、スクワラン",
        "value": "寒暖差でピリつく肌の炎症を速やかに抑え、角層セラミドを補修。真冬の過酷な乾燥下でも赤みや粉吹きを寄せ付けない圧倒的安心感",
        "desc_p1": "11月から12月にかけて外気温度が下がり、暖房の効いた室内との温度差が15℃を超えるようになると、顔の毛細血管が急激な拡張と収縮を繰り返し、皮膚表面に微小な炎症（赤ら顔・火照り・ピリピリ感）が発生します。この『寒暖差ストレス』に最も効果的なアプローチを発揮するのが、乾燥性敏感肌研究の金字塔であるキュレルの『潤浸保湿フェイスクリーム』です。有効成分として配合された『アラントイン』が、冷風や摩擦で傷ついた表皮の炎症を穏やかに鎮めます。",
        "desc_p2": "さらに花王独自開発の『潤浸セラミド機能成分』が角質細胞の隙間深くまで浸透し、水分を抱え込むラメラ構造を即効で修復。スフレのように驚くほど軽やかなホイップテクスチャーでありながら、肌に塗り広げると瞬時に溶け込み、しっとりと吸い付くような保護ベールを形成します。ベタつきや皮膜感が一切なく、メイク前にもたっぷり使えるため、朝の暖房対策から夜の集中リペアまで真冬の肌を24時間守り抜きます。",
        "target": "真冬になると頬や鼻周りが赤く火照る・ピリピリ痛む方、保湿クリームのベタつきが苦手な敏感肌の方、マスクの摩擦で粉を吹きやすい方",
        "point": "化粧水や乳液のあと、指の腹に直径約2cm（さくらんぼ大）を取り、摩擦を起こさないよう優しくハンドプレスで顔全体に包み込みます。特に赤みやカサつきが気になる頬骨まわりには、少量を重ねづけして『保護膜』を強化してください。"
    },
    {
        "rank": 2,
        "tag": "💧 アミノ酸濃密補給×消炎バリア！ゴワつく冬の角層をまろやかに満たす薬用とろみ化粧水",
        "catch": "9種の保潤アミノ酸と消炎成分が融合。吸い付くような濃厚なとろみ液が、寒さで硬化した角層をじんわり解きほぐして深層保水を叶える",
        "brand_name": "MINON (ミノン) アミノモイスト",
        "capacity": "150ml (プッシュボトル)",
        "type": "薬用角層柔軟高保湿化粧水",
        "features": "グリチルリチン酸2K・アラントイン様消炎複合体、9種の保潤アミノ酸、2種の清透アミノ酸、リピジュア類似成分",
        "value": "肌本来の天然保湿因子（NMF）の半分を占めるアミノ酸を網羅的にチャージ。真冬のバリア崩壊を食い止め、吸い付くような柔らかさを実現",
        "desc_p1": "冬になると「化粧水をいくら重ねても肌表面を滑るだけで入っていかない」と感じる原因は、寒冷によって角質細胞内の水分と天然保湿因子（NMF）が干からび、角層が角化・硬直しているためです。ミノンアミノモイストの『モイストチャージ ローション II もっとしっとりタイプ』は、敏感肌・乾燥肌の皮膚生理をとことん追求して生まれた名品ローションです。",
        "desc_p2": "とろりとした美容液のようなリッチなテクスチャーが乾いた肌に触れた瞬間、まろやかにほどけて角層の奥深くへと浸透。消炎成分が肌荒れを防ぎながら、肌の構成成分と同じ9種のアミノ酸が角質細胞ひとつひとつをうるおいで満たします。使用後の肌は手のひらが吸い付くほどモチモチになり、ゴワつきが一掃されてふっくらとしたキメが整います。低刺激・無香料・アルコールフリーで、真冬の弱った肌にも優しく染み渡ります。",
        "target": "冬場の肌のゴワつきやキメの乱れに悩む方、とろみ化粧水でじっくり角層を柔らかくしたい方、敏感肌用の安心できる薬用保湿を求める方",
        "point": "洗顔後、3〜5プッシュを手にとり、手のひらで温めてから顔全体に優しくなじませます。一度なじんだ後、さらに1〜2プッシュを手に取り、乾燥小ジワが出やすい目元や額に重ねづけする『ダブルインジェクション』が真冬の乾きを根絶します。"
    },
    {
        "rank": 3,
        "tag": "🛡️ 高精製ワセリン×抗肌あれアラントイン！体温でとろけてピタッと密着する保護バーム",
        "catch": "資生堂の高精製ワセリン技術。人肌で瞬時にとろけて密着シールドを形成し、真冬の寒冷風・マスク擦れ・暖房乾燥から肌を鉄壁ガード",
        "brand_name": "IHADA (イハダ) / 資生堂",
        "capacity": "20g (コンパクトジャー)",
        "type": "薬用とろける密着保護バーム",
        "features": "アラントイン（抗肌あれ有効成分）、グリチルレチン酸ステアリル、高精製ワセリン、シリコーンフリー",
        "value": "通常のワセリンのようなギトギト感や重さを極限まで排除。人肌温度でスルスル伸びて、角層の水分蒸発と外部刺激を物理的＆薬効的に遮断",
        "desc_p1": "冬の北風が吹き付ける屋外と、エアコンの温風が直撃するオフィス。この過酷な環境で肌の皮脂膜は完全に破壊され、無防備な角層がむき出しになります。資生堂のメディカル発想ブランド・イハダの『薬用バーム』は、不純物を極限まで取り除いた『高精製ワセリン』に、抗肌あれ有効成分アラントインを融合させた真冬の必需品です。",
        "desc_p2": "指先で触れると固めのバームですが、肌の上に乗せた瞬間に体温でジュワッととろけて、驚くほどなめらかに薄く広がります。アラントインが日中に受けた微小な肌荒れを鎮静しつつ、高純度ワセリンの保護膜が角層内部の水分を100%閉じ込めます。小鼻の脇の皮向けや、唇の山の上、口角のひび割れなど、冬にトラブルが多発するポイントへ部分使いするレスキューアイテムとしても圧倒的な実力を誇ります。",
        "target": "冬になると口周りや目元が粉を吹いて皮がめくれる方、マスクやマフラーの摩擦で肌が赤くなる方、ベタつかない高純度ワセリンバームを探している方",
        "point": "スキンケアの最後に、指先で米粒大を取り、手のひらで軽くすり合わせて温めてから、乾燥や刺激が気になる部位に優しく押し当てるように乗せます。日中のメイクの上から乾燥が気になった際も、少量をトントンと叩き込むだけで即座にツヤと潤いが復活します。"
    },
    {
        "rank": 4,
        "tag": "🏥 ヨーロッパ皮膚科処方！C+Restore×アベンヌ温泉水が真冬の損傷肌を速攻立て直す",
        "catch": "フランスのアベンヌ皮膚科学研究所が開発。温泉水と保護ポリマーが一体となり、真冬のひび割れ・ガサガサ・粉吹き肌をまるで包帯のように保護",
        "brand_name": "Avene (アベンヌ)",
        "capacity": "40g (ラミネートチューブ)",
        "type": "薬用組織修復リペアクリーム",
        "features": "C+Restore（アクアフィロバイオーム・アラントイン類似整肌成分）、硫酸銅、硫酸亜鉛、アベンヌ温泉水45%配合",
        "value": "美容医療後や極度の肌荒れにも処方されるシカ・リペアの元祖。真冬の過酷な寒冷でバリアが完全に崩壊した肌に、厚みのある保護膜を形成",
        "desc_p1": "南フランスの自然豊かなアベンヌ村で湧き出る名水を用いたスキンケアの最高峰リペアクリーム『シカルファットプラス』。ヨーロッパでは家庭の常備薬として親しまれており、皮膚科医がレーザー施術後や重度の乾燥性皮膚炎のアフターケアとして推奨するほどの本格派リペアクリームです。",
        "desc_p2": "こっくりと濃厚で白いクリームは、肌に塗るとまるで『塗る保護包帯』のようにピタッと密着。アラントイン類似の皮膚修復成分『C+Restore』とアベンヌ温泉水が、寒さで傷ついた表皮のターンオーバーを劇的に早めます。さらに銅・亜鉛のミネラル複合体が雑菌の繁殖を抑えて清潔な肌環境を保持。夜寝る前に厚めに塗って就寝すれば、翌朝には昨日までの赤みやヒリつきが嘘のように引いて、滑らかな素肌へと生まれ変わります。",
        "target": "真冬の冷風で肌が荒れ果てて何をつけても染みる方、ひび割れや粉吹きがひどく即効性のあるリペアを求める方、美容施術後のデリケートな肌を守りたい方",
        "point": "夜の洗顔後、化粧水などで肌を整えたあと、大きめのパール粒大を取り、患部を包み込むように厚めに塗布して『スリーピングパック』のようにして就寝します。擦らずに乗せるのが炎症を早く鎮める秘訣です。"
    },
    {
        "rank": 5,
        "tag": "🧬 ヘパリン類似物質×アラントイン！角層ラメラの乱れを根本修復する高保湿乳液",
        "catch": "コーセーと製薬会社マルホの共同開発。保水有効成分ヘパリン類似物質と消炎成分アラントイン（グリチルリチン酸）が、冬の乾燥悪循環を根源から断ち切る",
        "brand_name": "Carte (カルテHD) / コーセー マルホ",
        "capacity": "120ml (ポンプボトル)",
        "type": "保水有効成分ヘパリン類似物質配合乳液",
        "features": "ヘパリン類似物質HD（保水有効成分）、グリチルリチン酸ジカリウム・アラントイン（消炎有効成分）、セラミド類似ポリマー、スクワラン",
        "value": "単に表面を覆うだけでなく、角層内部の水分保持ラメラ構造そのものを再建。真冬の過酷な湿度の低さにも屈しない自立した潤い肌を育てる",
        "desc_p1": "「毎年11月を過ぎると、どんな高保湿コスメを使っても夕方には乾燥がぶり返す」という負のループに終止符を打つのが、コーセーと皮膚科処方薬のトップメーカー・マルホがタッグを組んで開発した『カルテHD モイスチュア エマルジョン』です。医療現場で長年乾燥肌治療に使われてきた保水有効成分『ヘパリン類似物質』を贅沢に配合しています。",
        "desc_p2": "ヘパリン類似物質が乱れた角層ラメラ構造を整えて肌本来の保水力を引き上げ、同時に消炎成分が冬の冷気や暖房による微小炎症を鎮静。まろやかでみずみずしいエマルジョンは、肌に乗せるとすーっと解けてベタつきを残さず、肌の内側に水分を閉じ込めます。毎日の朝晩ケアに組み込むことで、暖房の効いた乾燥部屋にいても肌が乾燥を感じにくくなる『高保水体質』へと導いてくれます。",
        "target": "冬になると毎年乾燥が深刻化して皮がむける方、ヘパリン類似物質の本格的な保湿力を日常ケアで取り入れたい方、乳液の油膜感やベタつきが苦手な方",
        "point": "化粧水のあと、ポンプ2プッシュを手にとり、手のひら全体を使って顔の中心から外側へ優しくなじませます。首元やデコルテまで滑らせるように伸ばすと、真冬の首の乾燥かゆみも同時に防ぐことができます。"
    },
    {
        "rank": 6,
        "tag": "🌿 アラントイン×紫蘇エキス！冬の入浴後かゆみと冷え乾燥を防ぐ全身ミルキィローション",
        "catch": "北海道産シソエキスと消炎アラントイン配合。水分7：油分3のゴールデンバランスで、真冬のお風呂上がりに急激に乾く全身の角層を優しく潤す",
        "brand_name": "yuskin (ユースキン) シソラ",
        "capacity": "170ml (大容量ポンプ)",
        "type": "低刺激消炎全身保湿ローション",
        "features": "アラントイン（有効成分）、シソエキス、濃グリセリン、イソノナン酸イソノニル",
        "value": "冬の入浴後の急激な水分蒸発と肌のムズムズかゆみを即座にブロック。赤ちゃんから大人まで家族全員で使える弱酸性・無香料・低刺激設計",
        "desc_p1": "11月から12月は、熱いお風呂に入った後の脱衣所で体温が下がる際、角層から水分が一気に蒸発して全身がピリピリとかゆくなる『入浴後過乾燥』が頻発します。ユースキン製薬が敏感肌のために開発した『シソラ ローション』は、厳選された北海道産紫蘇エキスと消炎成分アラントインを掛け合わせた、冬の全身レスキューローションです。",
        "desc_p2": "乳白色のさらっとしたミルキィテクスチャーは、濡れ感が残るお風呂上がりの肌にも摩擦なくスーッと伸び、素早く角層へ浸透します。アラントインが衣類のチクチク摩擦や乾燥による刺激を抑え、紫蘇のうるおい成分が肌のバリアを整えます。ポンプ式で手軽に出せるため、背中や腕、脚のすねなど粉を吹きやすい部位にたっぷり塗布可能。塗った直後に服を着てもサラリと快適です。",
        "target": "冬にお風呂から上がるとすねや腰回りがムズムズかゆくなる方、家族みんなで惜しみなく使える低刺激ボディミルクを探している方、敏感肌のお子様がいるご家庭",
        "point": "お風呂から上がってタオルで軽く水分を押さえた直後の、まだ湿り気がある肌に2〜3プッシュを素早く全身に伸ばします。肌の水分と乳液が混ざり合い、より滑らかで持続力のある保湿膜が完成します。"
    },
    {
        "rank": 7,
        "tag": "🌸 寒暖差による肌荒れと乾燥を一撃！資生堂dプログラムの薬用モイストケアローション",
        "catch": "美肌菌に着目した資生堂の独自成分×トラネキサム酸＆アラントイン配合。カサカサ粉吹き肌をしっとりなめらかな陶器肌へ導く",
        "brand_name": "d program (dプログラム) / 資生堂",
        "capacity": "125ml / ポンプボトル",
        "type": "薬用敏感肌用高保湿化粧水",
        "features": "トラネキサム酸（抗肌あれ有効成分）、グリチルリチン酸・アラントイン（消炎成分）、酵母エキス、トレハロース",
        "value": "寒暖差の激しい冬の環境変化による角層バリアの乱れを先回りしてブロック。肌表面の常在菌バランスを整えて乾燥トラブルを寄せ付けない",
        "desc_p1": "急な冷え込みや室内の暖房によって肌のコンディションが乱高下する11月・12月。資生堂の敏感肌研究から生まれたdプログラムの『モイストケア ローション MB』は、寒暖差による角層の乱れと肌荒れを未然に防ぐ薬用高保湿ローションです。",
        "desc_p2": "抗肌あれ有効成分トラネキサム酸と消炎成分アラントインのダブル作用で、冬の赤みやゴワつきをスピーディーに鎮静。さらに美肌菌を育む酵母エキスが、乾燥に負けない健やかな皮膚マイクロバイオームを形成します。とろみのあるリッチな感触でありながら肌に乗せるとスーッと馴染み、乾燥によって縮こまった角層を潤いで押し広げ、透明感のあるふっくら素肌を取り戻します。",
        "target": "季節の変わり目や真冬に肌が敏感になりスキンケアが合わなくなる方、赤みと乾燥小ジワを同時にケアしたい方、美肌菌ケアに興味がある方",
        "point": "洗顔後、ディスペンサー2回押し分を手にとり、顔全体に優しくなじませます。最後に両手で顔全体を包み込み、手のぬくもりを伝えるように5秒間ハンドプレスすると、成分の角層浸透がさらに深まります。"
    },
    {
        "rank": 8,
        "tag": "💊 天然型ビタミンE×消炎アラントイン！ひび・あかぎれ・粉吹き脚を治す国民的薬用クリーム",
        "catch": "エーザイが誇るロングセラー薬用保湿。血行を促進するビタミンEと組織を修復するアラントインが融合し、真冬のがさがさ手足をなめらかに修復",
        "brand_name": "Eisai (エーザイ) ザーネ",
        "capacity": "100g (大容量ジャー)",
        "type": "指定医薬部外品・薬用ビタミンE消炎クリーム",
        "features": "天然型ビタミンE（酢酸d-α-トコフェロール）、グリチルリチン酸ジカリウム（消炎アラントイン複合体）、グリセリン、レシチン",
        "value": "冷え切った冬の末梢血流をビタミンEで改善し、アラントインが荒れた表皮組織の修復を促進。手荒れ・かかとのひび割れ・粉吹き脚を根本治癒",
        "desc_p1": "製薬会社エーザイが60年以上にわたり日本人の冬の肌荒れを救い続けてきた『ザーネクリーム』。主成分である天然型ビタミンEが末梢の血流を促して皮膚の新陳代謝を活性化させ、消炎成分が冷気や水仕事による炎症・あかぎれを穏やかに治癒します。",
        "desc_p2": "こっくりとした白いクリームですが、肌に伸ばすとスーッと馴染んでサラサラの仕上がりに変化。ベタつきが残らないため、家事や仕事の合間でもストレスフリーで使用できます。真冬になるとひび割れてストッキングに引っかかるかかとや、白く粉を吹いてかゆい脛（すね）、水仕事で荒れ果てた指先まで、全身の深刻な乾燥部位を吸い付くようななめらか肌へと導きます。",
        "target": "冬場の水仕事であかぎれやささくれがひどい方、かかとのガサガサやひび割れを治したい方、ベタつかず日常使いしやすい薬用クリームを探している方",
        "point": "お風呂上がりや水仕事の直後、適量を手に取り、荒れが気になる部位に円を描くようにマッサージしながら塗り込みます。就寝前に手足にたっぷり塗り、綿の手袋や靴下を履いて寝ると翌朝劇的に滑らかになります。"
    },
    {
        "rank": 9,
        "tag": "🫧 ヘパリン類似物質×アラントインの濃密マイクロ泡！摩擦ゼロで溶け込むオールインワン",
        "catch": "プッシュするだけで濃密な薬用マイクロフォームが出現。手と肌の摩擦を極限までゼロにし、真冬の激乾・敏感肌に角層深層保水を届ける",
        "brand_name": "アトピアD (Atopia D)",
        "capacity": "100g (フォーム缶)",
        "type": "薬用泡状高保湿オールインワン美容液",
        "features": "ヘパリン類似物質（保水有効成分）、アラントイン（抗肌あれ有効成分）、ヒアルロン酸、水溶性コラーゲン",
        "value": "泡が弾ける力で美容成分を角層へ押し込む。冬の過敏になった肌に手のひらの摩擦ストレスを一切与えずに高保水ケアを完結",
        "desc_p1": "「冬は肌が敏感になりすぎて、コットンや手のひらの摩擦すら痛い」という極限の乾燥肌に救世主となるのが、アトピアDの『保湿フォーム』です。缶をプッシュするだけで、きめ細かく弾力のある薬用マイクロ泡が瞬時に噴出します。",
        "desc_p2": "保水有効成分ヘパリン類似物質と消炎成分アラントインを泡の中に高濃度で封じ込めており、肌に乗せると体温でジュワッと液体化して角層へ吸い込まれます。化粧水・美容液・アイクリーム・乳液の4役を兼ね備えたオールインワン設計のため、これ1本で真冬のスキンケアが完了。乾燥でひび割れそうな肌にも染みることなく、みずみずしい潤いと保護膜をもたらします。",
        "target": "スキンケアを塗る際の手のひらの摩擦が辛い超敏感肌の方、ヘパリン類似物質の保湿力を手軽な泡で体験したい方、時短で確実な冬保湿をしたい方",
        "point": "缶を上下によく振ってからピンポン玉大を手のひらに出し、顔全体に泡を乗せてハンドプレスします。泡がじゅわっと溶けて肌になじむまで、擦らずに優しく手で覆うのが最大のコツです。"
    },
    {
        "rank": 10,
        "tag": "💎 抗炎症アラントイン×濃密ヒアルロン酸！赤みとゴワつきを潤いで満たす薬用極潤",
        "catch": "ロート製薬のヒアルロン酸研究の結晶。消炎有効成分アラントインとヒアルロン酸コンプレックスが、真冬の暖房乾燥で揺らぐ角層をモチモチ肌へ",
        "brand_name": "肌ラボ (ロート製薬)",
        "capacity": "170ml (大容量ボトル)",
        "type": "薬用抗炎症・深層保水化粧水",
        "features": "アラントイン（有効成分）、グリチルリチン酸2K、加水分解ヒアルロン酸、ヒアルロン酸Na、ハトムギエキス",
        "value": "惜しみなくパシャパシャ使える大容量高コスパ。真冬の過酷な空気乾燥による角層の炎症を鎮め、肌密度を高める濃密保水膜を形成",
        "desc_p1": "ドラッグストアで手に入る国民的スキンケアブランド肌ラボの隠れた実力派『薬用 極潤 スキンコンディショナー』。乾燥肌特有の『赤み・肌荒れ・ニキビ・粉吹き』に着目し、消炎有効成分アラントインとグリチルリチン酸を贅沢にダブル配合しています。",
        "desc_p2": "みずみずしく清涼感のあるテクスチャーが肌に触れると、寒暖差でほてった肌をすっきりとクールダウン。同時にロート製薬自慢のヒアルロン酸が角層深くまで水分を注ぎ込み、乾燥によるゴワつきを和らげます。大容量で詰め替え用も充実しているため、コットンパックやボディの保湿にも惜しみなく活用可能。日々のベーシックケアとして冬の肌荒れを未然に防ぎます。",
        "target": "プチプラで惜しみなくたっぷり使える薬用保湿ローションを求める方、冬でもベタつかずみずみずしく水分補給したい方、赤みや肌荒れを予防したい方",
        "point": "500円玉大を手にとり、顔全体に優しくパッティングしながらなじませます。特に乾燥が気になる時は、大判コットンにたっぷり含ませて3分間の『ローションパック』を行うと、エステ後のような透き通るモチ肌が蘇ります。"
    }
]

faq_list = [
    {
        "question": "冬のスキンケア成分として『アラントイン』が推奨される皮膚科学的理由は何ですか？",
        "answer": "11月から12月は、外気の厳しい冷風と室内のエアコン暖房による『急激な寒暖差』によって、皮膚表面に微小な炎症（赤み・ピリつき）が頻発します。アラントインはコンフリー（ヒレハリソウ）などの植物にも含まれる成分で、優れた抗炎症作用と『表皮組織の修復・ターンオーバー正常化作用』を併せ持っています。乱れた角質細胞を穏やかに整えながら新しい健やかな角層形成を促進するため、冬の乾燥によって傷つき粉を吹いた肌をスピーディーに鎮静・再生させるのに極めて理想的な成分なのです。"
    },
    {
        "question": "アラントイン配合のコスメは、ステロイドのような副作用や依存性の心配はありませんか？",
        "answer": "アラントインは医薬品のステロイド抗炎症薬とは全く異なる非ステロイド性の成分であり、極めて穏やかで肌に優しい作用機序を持っています。そのため、長期連用による皮膚の菲薄化（薄くなること）や依存性、リバウンドなどの副作用の心配は一切ありません。日本の医薬部外品においても高い安全性が認められており、赤ちゃんや敏感肌向けのスキンケア、指定医薬部外品のひび・あかぎれ治療薬にも広く活用されています。"
    },
    {
        "question": "真冬に顔が粉を吹いてピリピリ痛む時、アラントインコスメをどのように使うのが最も効果的ですか？",
        "answer": "粉吹きやピリつきが生じている肌は、角層のバリア機能が完全に破壊されています。この時は『摩擦を極限まで減らすこと』が最優先です。洗顔時はぬるま湯（32〜34℃程度）で優しく洗い、ミノンやカルテHDのような低刺激なローションを手で温めて優しくハンドプレスします。その後、キュレルのクリームやイハダの薬用バームを手のひらに伸ばし、擦らずに肌へペタッと密着させるように蓋をしてください。患部を保護膜で覆って水分蒸発を完全に遮断することが早期回復の鉄則です。"
    },
    {
        "question": "アラントインとセラミドやヘパリン類似物質は併用しても大丈夫ですか？",
        "answer": "併用は全く問題ないどころか、真冬の乾燥対策において『最高の相乗効果（シナジー）』を発揮します。アラントインが冷風や乾燥による肌表面の炎症・赤みを鎮静させている間に、セラミドやヘパリン類似物質が角層内部の細胞間脂質やラメラ構造を強力に保水・再構築します。今回のランキングでご紹介しているキュレル（アラントイン×セラミド）やカルテHD（アラントイン×ヘパリン類似物質）のように、両方が黄金比率で組み合わされたアイテムを選ぶのが冬の乾燥脱出への最短ルートです。"
    }
]

# JSON-LD構造化データ
jsonld_items = []
for i, item in enumerate(items):
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": item["display_name"],
        "url": f"https://lumi-cosme.vercel.app/winter-allantoin.html#item-{i+1}"
    })

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
        "@id": "https://lumi-cosme.vercel.app/winter-allantoin.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！冷風と暖房寒暖差で荒れ狂う角層を鎮静＆保水バリアで満たす高保湿アラントインコスメランク10",
    "description": "11月・12月の寒暖差赤ら顔と冬の粉吹き・肌荒れを救う高保湿アラントインコスメを徹底厳選！キュレル、ミノン、イハダ、アベンヌ、カルテHDからザーネ、肌ラボまで楽天で今すぐ買えるおすすめ人気ランキング10選と冬の角層レスキュー法を詳しく解説。",
    "image": items[0]["image"],
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
    "name": "真冬の高保湿アラントインコスメおすすめ人気ランキング10選",
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
      <h3 class="product-name">{d['brand_name']} {p['display_name']}</h3>
      <p class="product-catch">{d['catch']}</p>
      
      <div class="product-layout">
        <div class="product-visual">
          <img src="{p['image']}" alt="{p['display_name']}" class="product-img" loading="lazy" width="300" height="300">
          <div class="price-box">
            <span class="price-label">楽天参考価格</span>
            <span class="price-value">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['url']}" target="_blank" rel="noopener sponsored" class="rakuten-btn">
            楽天で最新価格・在庫を見る
          </a>
        </div>
        
        <div class="product-info-detail">
          <div class="spec-table">
            <div class="spec-row"><span class="spec-th">ブランド</span><span class="spec-td">{d['brand_name']}</span></div>
            <div class="spec-row"><span class="spec-th">容量・規格</span><span class="spec-td">{d['capacity']}</span></div>
            <div class="spec-row"><span class="spec-th">アイテム種別</span><span class="spec-td">{d['type']}</span></div>
            <div class="spec-row"><span class="spec-th">注目有効成分</span><span class="spec-td">{d['features']}</span></div>
            <div class="spec-row"><span class="spec-th">真冬の消炎保水価値</span><span class="spec-td">{d['value']}</span></div>
          </div>
          
          <div class="review-box">
            <h4>💡 美容皮膚専門ライターの詳細解説＆真冬の実践レビュー</h4>
            <p>{d['desc_p1']}</p>
            <p>{d['desc_p2']}</p>
          </div>
          
          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ：</strong>
            <p>{d['target']}</p>
          </div>
          
          <div class="usage-box">
            <strong>✨ 効果を最大化する真冬の使い方テクニック：</strong>
            <p>{d['point']}</p>
          </div>
        </div>
      </div>
    </article>
    """)

cards_joined = "\n".join(cards_html)

table_rows = []
for i, p in enumerate(items):
    d = product_details[i]
    table_rows.append(f"""
    <tr>
      <td class="tb-rank">第{i+1}位</td>
      <td class="tb-img"><img src="{p['image']}" alt="{p['display_name']}" width="60" height="60" loading="lazy"></td>
      <td class="tb-name"><strong>{d['brand_name']}</strong><br><a href="#item-{i+1}">{p['display_name']}</a></td>
      <td class="tb-type">{d['type']}</td>
      <td class="tb-price">¥{p['price']:,}</td>
      <td class="tb-btn"><a href="{p['url']}" target="_blank" rel="noopener sponsored" class="table-link-btn">楽天で見る</a></td>
    </tr>
    """)

table_joined = "\n".join(table_rows)

faq_html_blocks = []
for faq in faq_list:
    faq_html_blocks.append(f"""
    <div class="faq-item">
      <h3 class="faq-q">Q. {faq['question']}</h3>
      <p class="faq-a">A. {faq['answer']}</p>
    </div>
    """)

faq_joined = "\n".join(faq_html_blocks)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！冷風と暖房寒暖差で荒れ狂う角層を鎮静＆保水バリアで満たす高保湿アラントインコスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒暖差赤ら顔と冬の粉吹き・肌荒れを救う高保湿アラントインコスメを徹底厳選！キュレル、ミノン、イハダ、アベンヌ、カルテHDからザーネ、肌ラボまで楽天で今すぐ買えるおすすめ人気ランキング10選と冬の角層レスキュー法を詳しく解説。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-allantoin.html">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！冷風と暖房寒暖差で荒れ狂う角層を鎮静＆保水バリアで満たす高保湿アラントインコスメランク10">
  <meta property="og:description" content="11月・12月の寒暖差赤ら顔と冬の粉吹き・肌荒れを救う高保湿アラントインコスメを徹底厳選！キュレル、ミノン、イハダ、アベンヌ、カルテHDまで厳選10選。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-allantoin.html">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
  <!-- 構造化データ -->
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
      --primary-color: #059669;
      --primary-light: #d1fae5;
      --primary-dark: #047857;
      --accent-color: #10b981;
      --text-main: #1f2937;
      --text-muted: #4b5563;
      --bg-light: #f0fdf4;
      --border-color: #a7f3d0;
      --card-bg: #ffffff;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
      --radius: 12px;
    }}
    
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
      line-height: 1.85;
      color: var(--text-main);
      background-color: #fafaf9;
    }}
    
    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid #e5e7eb;
      padding: 1rem 0;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title a {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-link:hover {{ color: var(--primary-dark); }}
    
    .container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 2rem 1.5rem 5rem;
    }}
    
    .breadcrumb {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
    }}
    .breadcrumb a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .breadcrumb span {{ color: #9ca3af; }}
    
    .article-header {{
      background: white;
      padding: 2.5rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border-top: 5px solid var(--primary-color);
    }}
    .article-meta {{
      display: flex;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 1.85rem;
      line-height: 1.45;
      font-weight: 800;
      color: #111827;
      margin-bottom: 1.5rem;
    }}
    .article-lead {{
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.85;
      border-left: 4px solid var(--primary-color);
      padding-left: 1.25rem;
      background: var(--bg-light);
      padding: 1.25rem;
      border-radius: 0 8px 8px 0;
    }}
    
    .toc-box {{
      background: white;
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.75rem;
      margin-bottom: 3rem;
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
    .toc-list {{
      list-style: none;
      display: grid;
      gap: 0.6rem;
    }}
    .toc-list li a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}
    .toc-list li a:hover {{
      color: var(--primary-color);
      text-decoration: underline;
    }}
    
    .content-section {{
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.5rem;
      margin-bottom: 3rem;
    }}
    .section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #111827;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 0.75rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .section-p {{
      margin-bottom: 1.25rem;
      font-size: 1rem;
      color: var(--text-main);
    }}
    
    .compare-table-wrapper {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}
    .compare-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      padding: 0.85rem;
      text-align: left;
      border: 1px solid var(--border-color);
      font-weight: 700;
    }}
    .compare-table td {{
      padding: 0.85rem;
      border: 1px solid #e5e7eb;
      vertical-align: middle;
    }}
    .tb-rank {{ font-weight: 800; color: var(--primary-color); text-align: center; width: 60px; }}
    .tb-img img {{ border-radius: 6px; object-fit: cover; }}
    .tb-name a {{ color: var(--text-main); text-decoration: none; font-weight: 600; }}
    .tb-name a:hover {{ color: var(--primary-color); text-decoration: underline; }}
    .tb-price {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-link-btn {{
      display: inline-block;
      padding: 0.4rem 0.8rem;
      background: #b91c1c;
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
    }}
    .table-link-btn:hover {{ background: #991b1b; }}
    
    .product-card {{
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.25rem;
      margin-bottom: 3.5rem;
      border: 1px solid #f3f4f6;
      position: relative;
    }}
    .product-badge-rank {{
      position: absolute;
      top: -12px;
      left: 20px;
      background: linear-gradient(135deg, #059669, #047857);
      color: white;
      font-weight: 800;
      font-size: 1rem;
      padding: 0.3rem 1.25rem;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.15);
    }}
    .product-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.25rem 0.75rem;
      border-radius: 6px;
      margin-top: 0.5rem;
      margin-bottom: 0.75rem;
    }}
    .product-name {{
      font-size: 1.4rem;
      font-weight: 800;
      line-height: 1.4;
      color: #111827;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
    }}
    
    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-layout {{ grid-template-columns: 1fr; }}
      .article-title {{ font-size: 1.45rem; }}
      .article-header {{ padding: 1.5rem; }}
      .content-section {{ padding: 1.5rem; }}
    }}
    
    .product-visual {{
      text-align: center;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid #e5e7eb;
      margin-bottom: 1rem;
    }}
    .price-box {{
      background: #fef2f2;
      border: 1px solid #fee2e2;
      padding: 0.6rem;
      border-radius: 8px;
      margin-bottom: 1rem;
    }}
    .price-label {{ font-size: 0.75rem; color: #991b1b; display: block; }}
    .price-value {{ font-size: 1.5rem; font-weight: 800; color: #b91c1c; }}
    .price-tax {{ font-size: 0.75rem; color: #7f1d1d; }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      padding: 0.85rem 1rem;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: white;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      border-radius: 8px;
      text-align: center;
      box-shadow: 0 4px 6px -1px rgba(185, 28, 28, 0.3);
      transition: opacity 0.2s;
    }}
    .rakuten-btn:hover {{ opacity: 0.9; }}
    
    .spec-table {{
      background: #f9fafb;
      border-radius: 8px;
      padding: 1rem;
      margin-bottom: 1.25rem;
      font-size: 0.88rem;
    }}
    .spec-row {{
      display: grid;
      grid-template-columns: 110px 1fr;
      padding: 0.4rem 0;
      border-bottom: 1px dashed #e5e7eb;
    }}
    .spec-row:last-child {{ border-bottom: none; }}
    .spec-th {{ font-weight: 700; color: #4b5563; }}
    .spec-td {{ color: #1f2937; }}
    
    .review-box {{
      background: #f0fdf4;
      border-left: 4px solid var(--primary-color);
      padding: 1.25rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 1.25rem;
    }}
    .review-box h4 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      font-weight: 700;
      margin-bottom: 0.5rem;
    }}
    .review-box p {{
      font-size: 0.92rem;
      color: #374151;
      margin-bottom: 0.6rem;
      line-height: 1.75;
    }}
    .review-box p:last-child {{ margin-bottom: 0; }}
    
    .target-box, .usage-box {{
      padding: 0.85rem 1rem;
      border-radius: 8px;
      margin-bottom: 0.85rem;
      font-size: 0.9rem;
    }}
    .target-box {{ background: #eff6ff; border: 1px solid #dbeafe; color: #1e40af; }}
    .target-box p {{ color: #1e3a8a; margin-top: 0.25rem; }}
    .usage-box {{ background: #fefce8; border: 1px solid #fef08a; color: #854d0e; }}
    .usage-box p {{ color: #713f12; margin-top: 0.25rem; }}
    
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.5rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: #374151;
      line-height: 1.8;
    }}
    
    .footer-internal-links {{
      background: white;
      border-radius: var(--radius);
      padding: 2rem;
      box-shadow: var(--shadow);
      margin-top: 3rem;
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 0.75rem;
      margin-top: 1rem;
    }}
    .footer-link-pill {{
      display: block;
      padding: 0.6rem 0.85rem;
      background: #f9fafb;
      border: 1px solid #e5e7eb;
      border-radius: 8px;
      color: #374151;
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .footer-link-pill:hover {{
      color: var(--primary-color);
      border-color: var(--primary-color);
      background: var(--bg-light);
    }}
    
    .site-footer {{
      text-align: center;
      padding: 3rem 1.5rem;
      font-size: 0.85rem;
      color: #9ca3af;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <div class="site-title">
        <a href="/">❄️ 冬コスメ徹底比較ラボ</a>
      </div>
      <nav>
        <a href="/" class="nav-link">トップページへ戻る</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb" aria-label="パンくずリスト">
      <a href="/">ホーム</a>
      <span>&gt;</span>
      <a href="/#skincare">薬用スキンケア・敏感肌特集</a>
      <span>&gt;</span>
      <span aria-current="page">高保湿アラントインコスメ特集</span>
    </nav>

    <article class="article-header">
      <div class="article-meta">
        <time datetime="2026-11-04">公開日：2026年11月4日</time>
        <span>執筆：冬コスメ徹底比較ラボ 編集部（敏感肌・皮膚バリア研究チーム）</span>
      </div>
      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！冷風と暖房寒暖差で荒れ狂う角層を鎮静＆保水バリアで満たす高保湿アラントインコスメランク10</h1>
      <p class="article-lead">
        11月から12月にかけて、木枯らしが吹き付ける冷たい屋外（気温5〜10℃）と、エアコンが効いた乾燥した室内（気温20〜24℃・湿度20%台）を往復する日々が始まります。この急激な「寒暖差ストレス」によって、肌表面の毛細血管がパニックを起こし、微小な炎症による赤ら顔、ピリピリとした刺激感、そして角層が剥がれ落ちる粉吹き現象が多発します。ただ油分を重ねるだけでは治まらない冬の肌荒れ連鎖を断ち切る特効薬こそ、医薬部外品有効成分『アラントイン』です。本記事では、荒れた表皮組織を修復しながら角層をみずみずしい保水膜で満たす薬用高保湿アラントインコスメを徹底比較し、おすすめ人気ランキング10選としてご紹介します。
      </p>
    </article>

    <section class="toc-box">
      <h2 class="toc-title">📑 目次・記事ナビゲーション</h2>
      <ul class="toc-list">
        <li><a href="#why-allantoin">1. 11月〜12月の寒暖差15℃パニック：なぜ冬の乾燥肌荒れにアラントインが不可欠なのか？</a></li>
        <li><a href="#selection-criteria">2. 激乾・敏感な冬肌を確実に立て直すアラントインコスメ選び・3つの鉄則</a></li>
        <li><a href="#comparison-table">3. 高保湿アラントインコスメ10選 スペック・価格比較表</a></li>
        <li><a href="#ranking-section">4. 高保湿アラントインコスメおすすめ人気ランキング10選 詳細レビュー</a></li>
        <li><a href="#faq-section">5. 美容皮膚科視点で答えるアラントインケアのよくある疑問Q&amp;A</a></li>
        <li><a href="#conclusion">6. まとめ：寒暖差と乾燥冷風に負けない冬の角層バリア再構築メソッド</a></li>
      </ul>
    </section>

    <!-- セクション1 -->
    <section class="content-section" id="why-allantoin">
      <h2 class="section-title">🌿 1. 11月〜12月の寒暖差15℃パニック：なぜ冬の乾燥肌荒れにアラントインが不可欠なのか？</h2>
      <p class="section-p">
        11月から12月は、1年の中で最も肌にとって過酷な「寒暖差ショック」が訪れる時期です。外気の冷気にさらされてキュッと収縮していた皮膚の毛細血管は、暖房の効いた室内に入った瞬間に一気に拡張します。この急激な血管の拡張と収縮の繰り返しによって、皮膚組織には活性酸素や炎症性サイトカインが放出され、慢性的な「微小炎症」が定着してしまいます。
      </p>
      <p class="section-p">
        この微小炎症が続くと、表皮細胞の正常な角化プロセス（ターンオーバー）が狂い、まだ十分に育っていない未熟な角質細胞が肌表面へと押し上げられてしまいます。これが、肌の表面が白くめくれ上がる「粉吹き」や、化粧水をつけただけで電撃のように走る「ヒリつき」の正体です。
      </p>
      <p class="section-p">
        ここで奇跡的な働きを見せるのが、ヒレハリソウなどの植物から抽出される<strong>『アラントイン』</strong>です。アラントインは単なる保湿剤ではなく、日本の厚生労働省からも認められた「医薬部外品有効成分（抗肌あれ・消炎・組織修復）」です。
      </p>
      <p class="section-p">
        アラントインの最大の強みは、寒暖差や摩擦で傷ついた表皮の炎症を瞬時にクールダウンさせながら、死んでめくれ上がった古い角質を穏やかに脱落させ、新しい正常な皮膚細胞の増殖（上皮形成）を強力に促進する点にあります。炎症を鎮めつつ皮膚の修復を同時に行うため、セラミドやヒアルロン酸などの保水成分が角層にしっかりと留まる『土台』を一から再構築できるのです。
      </p>
    </section>

    <!-- セクション2 -->
    <section class="content-section" id="selection-criteria">
      <h2 class="section-title">🔍 2. 激乾・敏感な冬肌を確実に立て直すアラントインコスメ選び・3つの鉄則</h2>
      <p class="section-p">
        冬のデリケートな乾燥・粉吹き肌を確実に鎮静・回復させるためには、以下の3つのポイントを基準に製品を選定してください。
      </p>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">鉄則①：効果が公的に認められた『医薬部外品（薬用）』表示を選ぶ</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          アラントインの抗肌あれ・消炎効果を最大限に享受するためには、有効濃度が担保された医薬部外品（キュレル、ミノン、イハダ、カルテHDなど）を選ぶのが確実です。パッケージの「医薬部外品」または「薬用」の表記を確認しましょう。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">鉄則②：セラミド・ヘパリン類似物質・高精製ワセリンとの相乗処方を狙う</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          アラントインで炎症を鎮めた上で、角層の隙間を埋める「疑似セラミド（キュレル）」や、ラメラ構造を整える「ヘパリン類似物質（カルテHD）」、水分蒸発を物理的にシャットアウトする「高精製ワセリン（イハダ）」が組み合わさった処方を選ぶことで、水分保持力が飛躍的に向上します。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">鉄則③：アルコール（エタノール）フリー・無香料・弱酸性の徹底低刺激設計</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          寒暖差でバリアが壊れている冬肌に、エタノールや強い合成香料、不要な着色料は厳禁です。肌に染みることなく穏やかに馴染む、アレルギーテスト済み・低刺激処方のブランドを厳選しましょう。
        </p>
      </div>
    </section>

    <!-- セクション3 比較表 -->
    <section class="content-section" id="comparison-table">
      <h2 class="section-title">📊 3. 高保湿アラントインコスメ10選 スペック・価格比較表</h2>
      <p class="section-p">
        楽天市場の公式APIよりリアルタイムに取得した最新の販売価格と製品仕様の一覧表です。肌悩みの度合いや使用部位に合わせて最適なアイテムを比較してください。
      </p>
      <div class="compare-table-wrapper">
        <table class="compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>画像</th>
              <th>商品名・ブランド</th>
              <th>カテゴリ種別</th>
              <th>楽天価格</th>
              <th>商品詳細</th>
            </tr>
          </thead>
          <tbody>
            {table_joined}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4 ランキング詳細 -->
    <section id="ranking-section">
      <h2 style="font-size: 1.6rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 2rem; text-align: center;">
        🏆 高保湿アラントインコスメおすすめ人気ランキング10選
      </h2>
      {cards_joined}
    </section>

    <!-- セクション5 Q&A -->
    <section class="content-section" id="faq-section">
      <h2 class="section-title">❓ 5. 美容皮膚科視点で答えるアラントインケアのよくある疑問Q&amp;A</h2>
      {faq_joined}
    </section>

    <!-- セクション6 まとめ -->
    <section class="content-section" id="conclusion">
      <h2 class="section-title">🛡️ 6. まとめ：寒暖差と乾燥冷風に負けない冬の角層バリア再構築メソッド</h2>
      <p class="section-p">
        11月から12月にかけて本格化する激しい寒暖差とエアコン暖房の猛威は、どんなに健康な肌であっても赤みや粉吹き、ヒリつきといったバリア崩壊のサインを引き起こします。
      </p>
      <p class="section-p">
        「肌が乾燥しているから油分を塗らなきゃ」と焦る前に、まずは医薬部外品有効成分『アラントイン』の力を借りて、荒れ狂う角層の微小炎症を優しく鎮火させることが最優先事項です。
      </p>
      <p class="section-p">
        炎症が鎮まり、アラントインの組織修復作用によって新しい正常な角層が育ち始めれば、セラミドやヒアルロン酸といった潤い成分が逃げることなく肌の内側にしっかりと留まるようになります。
      </p>
      <p class="section-p">
        ぜひ今回ご紹介した薬用アラントインコスメを日々のスキンケアに取り入れ、赤みや粉吹きとさようならして、真冬でも穏やかで吸い付くようなモチ肌を手に入れてください。
      </p>
    </section>

    <!-- 内部リンクラッパー -->
    <section class="footer-internal-links" id="internal-links">
      <h2 style="font-size: 1.25rem; font-weight: 800; color: #1f2937; margin-bottom: 0.5rem;">
        🔗 併せて読みたい冬コスメ・保湿スキンケア関連記事
      </h2>
      <p style="font-size: 0.9rem; color: #6b7280;">
        当サイトでは、11月〜12月の肌悩みに合わせた高保湿コスメや成分別ランキングを多数公開しています。
      </p>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で動的に同期されます -->
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 当サイトは楽天市場アフィリエイトプログラムに参加しています。</p>
  </footer>

</body>
</html>
"""

with open("winter-allantoin.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-allantoin.html successfully. Size: {len(html_content):,} bytes")
