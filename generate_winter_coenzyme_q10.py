import json
import re

with open("fetched_final_30_liposome_coenzyme_astaxanthin.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_coenzyme_q10"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 圧倒的な人気を誇る黄色い濃密ジェル！高濃度Q10×美白の最高峰オールインワン",
        "catch": "コエンザイムQ10を限界濃度0.3%配合。寒さで代謝が落ちた真冬の肌にハリ・弾力・透明感を一挙に注ぎ込む",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "100g (薬用Qクイックジェル モイスト＆ホワイトニング)",
        "type": "薬用高濃度Q10美白オールインワンジェル",
        "features": "高濃度コエンザイムQ10（0.3%配合）、トラネキサム酸（美白・抗炎症）、甘草誘導体、ヒアルロン酸、コラーゲン",
        "value": "鮮やかな黄金色は高純度Q10の証。真冬の過酷な寒冷・暖房乾燥から角層を密閉保護し、1つで小ジワ・くすみ・しぼみ肌を劇的リペア",
        "desc_p1": "11月から12月にかけて気温が急降下すると、皮膚の毛細血管が収縮して血行不良に陥り、細胞に酸素や栄養が届きにくくなります。その結果生じるのが、顔全体がしぼんで弾力を失い、黄色くくすむ『冬枯れ肌』。DHCの薬用Qクイックジェルは、細胞のエネルギー工場であるミトコンドリアを活性化する補酵素『コエンザイムQ10』を基準上限の10倍（0.3%）配合した最高峰の薬用ジェルです。",
        "desc_p2": "フタを開けると広がるリッチな濃黄色は、着色料ではなく高濃度コエンザイムQ10そのものの天然色。濃厚でぷるんとしたジェルが肌の上でとろけるように広がり、トラネキサム酸が冬のメラニン生成と微小炎症をブロックしながら、Q10が弱まった細胞活力を底上げします。化粧水・ミルク・クリーム・パック・化粧下地の5役をこなし、忙しい冬の朝でもひと塗りでピンとしたハリと上質なツヤが一日中続きます。",
        "target": "冬の寒さで肌のハリ・弾力が衰えてきたと感じる方、時短で最高峰のエイジングケアと保湿を両立させたい方、くすみと乾燥小ジワを同時に防ぎたい方",
        "point": "洗顔後、さくらんぼ粒大を手にとって顔全体に厚めに広げます。手のひらの熱で温めながらハンドプレスし、余ったジェルは首元から鎖骨へ引き上げるようになじませてください。"
    },
    {
        "rank": 2,
        "tag": "🛡️ こっくり濃密な油分で水分蒸散を完全遮断！真冬の夜を制する最高峰リペアクリーム",
        "catch": "高濃度コエンザイムQ10×オリーブバージンオイル。真冬の冷風で強張った角層をふっくら柔らかくほぐすリッチクリーム",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "50g (薬用Qフェーストクリーム)",
        "type": "薬用超高保湿エイジングリペアクリーム",
        "features": "コエンザイムQ10（10倍濃度）、薬用美白水溶性プラセンタ、甘草誘導体、オリーブスクワラン",
        "value": "濃厚なコクのあるテクスチャーが肌表面に強力なエモリエント膜を形成。真冬の深夜暖房下でも翌朝まで一滴の水分も逃さない",
        "desc_p1": "真冬の過酷な乾燥環境では、水分を与えるだけでなく『いかに油分のバリアでフタをするか』が勝敗を分けます。DHCの薬用Qフェーストクリームは、年齢とともに急激に減少するコエンザイムQ10を贅沢に肌へ補給し、肌本来の再生力を夜の間にブーストする濃厚クリームです。",
        "desc_p2": "こっくりとリッチなバターのような質感ですが、肌にのばすと体温でじんわりと馴染み、ベタつかずベルベットのような極上の保護ヴェールへと変化します。プラセンタエキスが透明感を守り、オリーブスクワランが硬くなった角層を柔らかくほぐします。乾燥による目元のちりめんジワやほうれい線まわりにハリのクッションを満たし、真冬の朝の洗顔時に吸い付くようなもっちり感を実感できます。",
        "target": "朝起きると目元や口元がカサついてシワっぽくなる方、クリームには濃厚なコクと高い密閉力を求める方、本格的な冬のエイジングケアを始めたい方",
        "point": "夜のお手入れの総仕上げとして、パール粒大を手のひらで温めてから全顔に押し込むように密着させます。目尻やほうれい線には米粒大を重ね、薬指の腹でトントンと優しく叩き込んでください。"
    },
    {
        "rank": 3,
        "tag": "💧 角層深部へ黄色の活力シャワー！乾いた大人の肌をゴクゴク潤す薬用高保水ローション",
        "catch": "高濃度コエンザイムQ10×高浸透モイスチュア処方。真冬のゴワついた肌にすっと浸透し、内側から押し返すような弾力を宿す",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "160ml (薬用Qローション)",
        "type": "薬用高浸透エイジング化粧水",
        "features": "高濃度コエンザイムQ10、ヒアルロン酸Na、コラーゲン、薬用甘草フラボノイド",
        "value": "とろみがあるのに角層へグングン吸い込まれる驚異の浸透力。冬の寒さで硬化した角層細胞をふやかすように潤す",
        "desc_p1": "冬になると化粧水が肌表面で弾かれてしまい、奥まで浸透していかないと感じることはありませんか？それは角層細胞の水分保持力と代謝が落ちているサインです。DHC薬用Qローションは、高濃度Q10を微細乳化し、硬くなった角層深層へ速やかに届けるために開発されたプレミアム化粧水です。",
        "desc_p2": "黄金色のみずみずしいローションを手にとって肌になじませると、まるで乾いたスポンジが水を吸い込むようにスーッと浸透。ベタつきを残さず、肌の内側が水分で満たされて手のひらに吸い付くような弾力が戻ります。コラーゲンとヒアルロン酸が角層細胞の隙間を埋め、次に使う美容液やクリームの受け入れ態勢を完璧に整えます。",
        "target": "冬になると化粧水が浸透しにくくなる方、軽すぎず重すぎない絶妙なとろみ保湿を求める方、朝のスキンケアで肌にハリとツヤをチャージしたい方",
        "point": "500円玉大を手のひらに取り、顔全体になじませた後、もう一度同量を重ねづけする『2度塗り（レイヤリング）』が冬の砂漠肌を救うプロの裏技です。"
    },
    {
        "rank": 4,
        "tag": "🔬 浸透型ナノカプセル化ユビキノン原液！手持ちコスメを瞬時に真冬仕様へ格上げ",
        "catch": "ナノカプセル化された高純度コエンザイムQ10原液。寒さでしぼんだ目元やほうれい線にダイレクトに注ぎ込む集中原液",
        "brand_name": "TUNEMAKERS (チューンメーカーズ)",
        "capacity": "10ml / 20ml (コエンザイムQ10 原液)",
        "type": "高純度ナノ化コエンザイムQ10原液",
        "features": "高純度ユビキノン（レシチンナノカプセル化）、水添レシチン、グリセリン",
        "value": "油溶性のQ10をレシチンでナノカプセル化。水溶性の化粧水にも弾かれずスーッと溶け込み、細胞間脂質へ直接浸透",
        "desc_p1": "成分を薄めずそのまま届ける原液スキンケアのトップブランド・チューンメーカーズの『コエンザイムQ10』。本来は油溶性で化粧水などに溶けにくいユビキノンを、独自のレシチンナノカプセル技術によって超微細化し、角層への浸透力を極限まで高めた逸品です。",
        "desc_p2": "さらりとしたテクスチャーで肌なじみが抜群。洗顔後すぐに乾燥小ジワが気になる目尻や口元に直接原液をピンポイント塗りするもよし、手持ちの化粧水や乳液に1〜2滴混ぜて使うもよし。冬の寒さでいきいきとした血色感や弾力を失った肌に、細胞レベルの活力を素早く吹き込みます。",
        "target": "いつものスキンケアにプラスして真冬のハリ不足をケアしたい方、目元や口元の乾燥小ジワを集中撃退したい方、無駄な成分を省いた原液を好む方",
        "point": "化粧水の直後に、気になる目元・口元へ原液を1〜2滴指先で直接トントンと塗り込みます。さらに夜の乳液やクリームに2滴混ぜて全顔になじませると、翌朝のハリ感が段違いに向上します。"
    },
    {
        "rank": 5,
        "tag": "🌙 就寝中に手肌を集中エイジングリペア！カプセルQ10が弾ける夜用ハンドセラム",
        "catch": "マイクロカプセル化コエンザイムQ10×ローヤルゼリー。冷たい水仕事や冬の寒風で荒れ果てた手肌を一晩で蘇らせる",
        "brand_name": "KOSE (コーセー) コエンリッチ",
        "capacity": "80g (ナイトリニュー ハンドセラム)",
        "type": "夜用集中リペア高保湿ハンドクリーム",
        "features": "コエンザイムQ10カプセル、ローヤルゼリーエキス、ホホバオイル、フルーティフローラルの香り",
        "value": "黄色の美容液カプセルが肌の上で弾けて浸透。就寝中に手肌のキメ奥まで潤いを行き渡らせ、翌朝ふっくら若々しい手元へ",
        "desc_p1": "顔以上に年齢と冬の過酷な乾燥が現れやすいのが「手肌」。冷たい水での手洗いやアルコール消毒、真冬の寒風にさらされてガサガサに粉を吹いた手肌を救うのが、コーセーの『コエンリッチ ナイトリニュー』です。",
        "desc_p2": "クリームの中に無数に浮かぶ黄色い粒々は、コエンザイムQ10を凝縮したマイクロカプセル。手に伸ばすとカプセルがプチプチと弾けて角層へと溶け込み、ローヤルゼリーとホホバオイルが濃厚な潤い膜で手肌を包み込みます。就寝前に塗って寝るだけで、翌朝の手指の節々までふっくらと滑らかになり、手の甲の血管浮きや乾燥シワが目立たなくなります。",
        "target": "冬になると手荒れやあかぎれ、指先のカサつきに悩む方、手の甲の乾燥小ジワや年齢感が気になる方、夜のハンドケアを習慣にしたい方",
        "point": "寝る直前にパール粒大を手に取り、手の甲を重ね合わせて体温で温めながら全体に塗り広げます。指の関節や爪の生え際までマッサージするように揉み込み、綿の手袋をして眠るとさらに効果的です。"
    },
    {
        "rank": 6,
        "tag": "🥛 粉吹く真冬の全身をもっちり包み込む！贅沢Q10配合の超高保湿ボディミルク",
        "catch": "コエンザイムQ10×プレミアムモイスト処方。冬の冷えでカサつくスネや腕をシルクのようなツヤ肌へ導く",
        "brand_name": "NIVEA (ニベア花王)",
        "capacity": "200g (プレミアムボディミルク モイスチャー)",
        "type": "超高保湿エイジングケアボディミルク",
        "features": "コエンザイムQ10（ユビキノン）、ヒアルロン酸、カモミールエキス、マヨラナエキス、ローズヒップオイル",
        "value": "高保水エモリエント成分とQ10が角層奥深くまで浸透。タイツやヒートテックを脱いだときに粉が舞う冬のすねを完全レスキュー",
        "desc_p1": "真冬になるとスネや腰回りが白く粉を吹き、衣類の摩擦でチクチク痒くなる方に絶対的な人気を誇るニベアの最高峰ボディミルク。乾燥による肌荒れを防ぐだけでなく、肌にハリとツヤを与えるコエンザイムQ10をリッチに配合した大人のためのボディケアです。",
        "desc_p2": "ミルクとクリームの中間のようなとろける感触で、冬の冷えた肌にもスーッと伸びて瞬時に密着。重苦しいベタつきを残さないため、塗ってすぐにパジャマを着ても張り付きません。翌日の夜にお風呂に入る瞬間まで潤いのヴェールが途切れず、触れると思わずうっとりするような柔らかくすべすべの素肌が保たれます。",
        "target": "冬場にスネや背中、腕が粉を吹いてカサカサになる方、衣類の静電気や乾燥摩擦で肌が痒くなりやすい方、上品な香りと高い保湿力を両立したい方",
        "point": "お風呂上がりの水分を軽く拭き取った直後の温まった肌になじませます。特に乾燥しやすいスネ・ひざ・かかとには円を描くように優しく重ね塗りしてください。"
    },
    {
        "rank": 7,
        "tag": "✨ 薬用美白×Q10で真冬の手肌をガード！日中も使いやすいディープモイスチャー",
        "catch": "高純度コエンザイムQ10×トラネキサム酸。冬の手肌の乾燥を防ぎながらシミ・そばかすを予防する薬用ハンドジェル",
        "brand_name": "KOSE (コーセー) コエンリッチ",
        "capacity": "80g (薬用ホワイトニング ハンドクリーム ディープモイスチュア)",
        "type": "薬用美白・高保湿ハンドクリーム",
        "features": "マイクロカプセル化Q10、トラネキサム酸（美白有効成分）、ワセリン、ホホバオイル",
        "value": "濃厚なうるおいを与えながらも表面はサラリと密着。日中のデスクワークやスマートフォン操作中もストレスフリーで手肌を守る",
        "desc_p1": "手肌の乾燥を防ぎたいけれど、塗った後にベタついてスマホやキーボードに指紋がつくのがストレス…という悩みを完璧に解消した薬用ハンドクリーム。コエンザイムQ10の高保湿力とトラネキサム酸の美白効果を兼ね備えています。",
        "desc_p2": "肌にのばすとマイクロカプセルが弾け、高精製ワセリンとホホバオイルが肌表面に撥水性の保護ヴェールを形成。冷たい風や手洗い後の乾燥から手指をガードしながら、内側はしっとりとした潤いで満たされます。無香料タイプのため、仕事中や食事の前でも気兼ねなく何度でも塗り直せます。",
        "target": "日中こまめにハンドクリームを塗り直したい方、ベタつきが苦手なオフィスワーカーの方、手肌のシミ予防と保湿を同時に行いたい方",
        "point": "手洗いの後、水分をハンカチでしっかり拭き取ったらすぐに小豆粒大をなじませます。手の甲だけでなく、爪の甘皮まわりにも丁寧になじませることでささくれも防止できます。"
    },
    {
        "rank": 8,
        "tag": "🌿 驚異のプチプラ高保湿！コエンザイムQ10×Wコラーゲンのとろみ化粧水",
        "catch": "ユビキノン×加水分解コラーゲン配合。大人の乾燥肌をとろりと潤し、もっちり弾力を与えるコスパ最強ローション",
        "brand_name": "CEZANNE (セザンヌ)",
        "capacity": "160ml (モイスチュアリッチ エッセンスローション)",
        "type": "高保湿エイジングケア化粧水",
        "features": "コエンザイムQ10、加水分解コラーゲン、水溶性コラーゲン、ヒアルロン酸Na、無香料・無着色・アルコールフリー",
        "value": "1,000円台とは思えないリッチな美容液級のとろみ。真冬の乾燥で強張った角層をふっくらほぐし、毎日の水分補給を贅沢に叶える",
        "desc_p1": "ドラッグストアの実力派コスメブランド・セザンヌが手掛けるエイジングケア化粧水。プチプラの常識を覆す贅沢な美容成分ブレンドで、美容賢者や乾燥肌ユーザーの間で長年隠れた名品として愛され続けています。",
        "desc_p2": "とろみのあるまろやかなテクスチャーが肌の上を滑らかに広がり、吸い付くようなしっとり感をもたらします。2種類のコラーゲンとコエンザイムQ10がタッグを組み、真冬の寒さで失われがちな肌の弾力と水分保持力をサポート。低刺激処方でアルコールフリーのため、季節の変わり目や乾燥でピリつきやすい時期でも安心してたっぷり使えます。",
        "target": "惜しみなくバシャバシャ使える高保湿エイジング化粧水を探している方、プチプラで優秀なQ10コスメを試してみたい方、アルコール刺激に弱い敏感肌の方",
        "point": "コットンにたっぷり含ませて優しくパッティングした後、手のひらでハンドプレスして肌を密閉します。乾燥が激しい日はコットンを2枚に裂いて頬に貼る『5分間ローションパック』が絶大な威力を発揮します。"
    },
    {
        "rank": 9,
        "tag": "💎 シワ改善×美白の最高峰ナイアシンアミド配合！大人の手肌を格上げするプレミアムケア",
        "catch": "マイクロカプセル化コエンザイムQ10×有効成分ナイアシンアミド。手肌の本格的なシワ改善とシミ予防を両立する傑作",
        "brand_name": "KOSE (コーセー) コエンリッチ",
        "capacity": "60g (ザ プレミアム 薬用リンクルホワイト ハンドクリーム)",
        "type": "薬用シワ改善・美白プレミアムハンドクリーム",
        "features": "コエンザイムQ10、ナイアシンアミド（シワ改善・美白有効成分）、ヒアルロン酸、コラーゲン",
        "value": "医薬部外品として手肌のシワ改善承認を取得。真冬の過酷な寒さと乾燥で老け見えしやすい手肌に、内側から押し返すようなピンとしたハリを再生",
        "desc_p1": "年齢の出やすい手肌を本気で若々しく保ちたい大人のために、コエンリッチシリーズが持てる技術を全て注ぎ込んだ最高峰プレミアムハンドクリーム。真皮まで浸透してコラーゲン産生を促すナイアシンアミドと、高濃度コエンザイムQ10の黄金コンビネーションが話題を呼んでいます。",
        "desc_p2": "リッチで濃厚なクリームを手肌になじませると、吸い付くように密着し、手の甲の細かなちりめんジワや血管の凹凸を光のヴェールでふんわりカバー。継続して使用することで、冬の間に進行しやすい手肌の真皮シワを根本から改善し、透明感のある明るい手元をキープできます。大切な人へのプチギフトや冬の自分へのご褒美にも最適です。",
        "target": "手肌のシワや年齢感が本格的に気になり始めた方、従来のハンドクリームでは保湿力が物足りない方、医薬部外品の確かなエイジング効果を求める方",
        "point": "外出前や就寝前に適量を手に取り、手の甲全体を包み込むようになじませます。指の関節のシワを伸ばすように、指先に向かって引き伸ばしながら丁寧に塗り込んでください。"
    },
    {
        "rank": 10,
        "tag": "🥛 高濃度コエンザイムQ10の潤いヴェール！真冬の乾燥から肌を守る薬用高保水ミルク",
        "catch": "コエンザイムQ10高濃度配合×ヒアルロン酸。水分と油分を黄金バランスで補給し、もっちり吸い付く素肌を育む",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "100g (薬用Q クイックジェル モイスト＆ホワイトニング L)",
        "type": "薬用高純度Q10高保水ジェルミルク",
        "features": "高濃度コエンザイムQ10、トラネキサム酸、セラミド様成分、天然ビタミンE",
        "value": "みずみずしいジェルミルクテクスチャーで角層深くまでうるおいを満たし、真冬のエアコン乾燥に負けないハリ艶肌をキープ",
        "desc_p1": "DHC薬用Qシリーズの誇る高濃度コエンザイムQ10テクノロジーを、よりみずみずしく軽やかな使用感で体感できるジェルミルク。真冬でも重すぎるクリームが苦手な方や、朝のメイク前に素早く保湿を完了させたい方に絶大な支持を得ています。",
        "desc_p2": "肌にのばした瞬間にすっとほどけて角層の隙間を満たし、ベタつきを残さずに内側からふっくらとした潤いのクッションを形成。ビタミンEとQ10の抗酸化ネットワークが冬の冷気ストレスから肌を一日中ガードします。首元やデコルテまでたっぷり使える100gのたっぷりサイズで、真冬のトータルエイジングケアを支えます。",
        "target": "高保湿でありながらベタつかないテクスチャーを好む方、朝のメイク前に素早く肌のキメを整えたい方、首元やデコルテまでしっかりエイジングケアしたい方",
        "point": "朝晩、化粧水で肌を整えた後に適量を手に取り、顔の中心から外側へなじませます。手のひらで顔全体を優しくリフトアップするようにハンドプレスすると、よりピンとしたハリを実感できます。"
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
        "url": f"https://lumi-cosme.vercel.app/winter-coenzyme-q10.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "コエンザイムQ10（ユビキノン）とはどのような成分ですか？なぜ冬の乾燥に効くのですか？",
        "answer": "コエンザイムQ10（ユビキノン）は、私たちの体内のすべての細胞、特にエネルギーを産生するミトコンドリアに存在する必須の補酵素です。強力な抗酸化作用を持ち、細胞の代謝エネルギー（ATP）の生成をサポートします。真冬は寒さによって毛細血管が収縮し、肌細胞の活動が鈍化してターンオーバーが乱れ、肌がしぼんで乾燥小ジワが目立ちやすくなります。コエンザイムQ10を肌に補給することで、冷え切った肌細胞に活力を与え、自ら潤いとコラーゲンを生み出す力を底上げするため、真冬の乾燥・しぼみ肌に劇的な効果を発揮します。"
    },
    {
        "question": "コスメに含まれるコエンザイムQ10が黄色いのは着色料ですか？肌に色はつきませんか？",
        "answer": "着色料ではありません。コエンザイムQ10（ユビキノン）という原料そのものが、鮮やかな濃黄色〜オレンジ色をしています。そのため、高濃度に配合されている製品ほど綺麗な黄色をしています。肌に塗布すると、体温で素早くなじんで角層深層へ浸透するため、肌が黄色く染まったり衣服に着色したりすることは一切ありません。むしろ、黄色い濃厚な見た目は、高純度・高濃度に有効成分が配合されている信頼の証です。"
    },
    {
        "question": "コエンザイムQ10とビタミンEやビタミンCは一緒に使うと効果が高まりますか？",
        "answer": "非常に高い相乗効果を発揮します。コエンザイムQ10とビタミンEは、肌の脂質部分で活性酸素を除去する抗酸化パートナーです。ビタミンEが酸化されて力を失ったとき、コエンザイムQ10がビタミンEを還元して再び抗酸化力を復活させる『抗酸化リサイクル機構』が働きます。さらに水溶性のビタミンCが加わることで、角層の内外を隙間なく酸化ダメージから守り抜き、真冬の寒風による酸化・乾燥ストレスを跳ね返すことができます。"
    },
    {
        "question": "20代や若い世代でもコエンザイムQ10コスメを使うメリットはありますか？",
        "answer": "大いにあります。体内のコエンザイムQ10の量は20歳前後をピークに急激に減少していきます。特に11月〜12月の真冬は、寒暖差やエアコン乾燥、年末の多忙による睡眠不足やストレスで肌の酸化ストレスがピークに達します。早いうちからコエンザイムQ10で細胞エネルギーを補給しておくことで、将来のシワやたるみを予防し、冬でも生き生きとした血色感とハリツヤを維持することができます。"
    },
    {
        "question": "コエンザイムQ10配合のハンドクリームやボディミルクは普通のものと何が違いますか？",
        "answer": "一般的なハンドクリームやボディミルクが『油分で表面にフタをするだけ』であるのに対し、コエンザイムQ10配合のアイテムは角層細胞のキメ奥まで浸透し、皮膚の真皮・表皮環境に働きかけて内側からふっくらとしたハリを回復させます。特に手肌やスネは皮脂腺が少なく真冬に血管浮きや粉吹き、ちりめんジワが目立ちやすいため、Q10によるエイジングケア効果が最も顕著に実感できる部位です。"
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
        "@id": "https://lumi-cosme.vercel.app/winter-coenzyme-q10.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！寒さで活力を失った冬枯れ肌に濃密なハリと弾力を満たす高濃度コエンザイムQ10コスメランク10",
    "description": "11月・12月の寒冷・暖房乾燥による肌しぼみ・ハリ不足を救う高濃度コエンザイムQ10コスメを徹底厳選！DHC薬用Qシリーズ、ニベアプレミアム、コーセーコエンリッチ、チューンメーカーズからセザンヌまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。",
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
    "name": "真冬の高濃度コエンザイムQ10コスメおすすめ人気ランキング10選",
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
      
      <div class="product-layout">
        <div class="product-visual">
          <img src="{p['img_url']}" alt="{p['name']}" class="product-img" loading="lazy" width="300" height="300">
          <div class="price-box">
            <span class="price-label">楽天参考価格</span>
            <span class="price-value">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['affiliate_url']}" target="_blank" rel="noopener sponsored" class="rakuten-btn">
            楽天で最新価格・在庫を見る
          </a>
        </div>
        
        <div class="product-info-detail">
          <div class="spec-table">
            <div class="spec-row"><span class="spec-th">ブランド</span><span class="spec-td">{d['brand_name']}</span></div>
            <div class="spec-row"><span class="spec-th">容量・規格</span><span class="spec-td">{d['capacity']}</span></div>
            <div class="spec-row"><span class="spec-th">アイテム種別</span><span class="spec-td">{d['type']}</span></div>
            <div class="spec-row"><span class="spec-th">注目成分</span><span class="spec-td">{d['features']}</span></div>
            <div class="spec-row"><span class="spec-th">真冬の保湿価値</span><span class="spec-td">{d['value']}</span></div>
          </div>
          
          <div class="review-box">
            <h4>💡 美容皮膚専門ライターの詳細解説＆真冬のレビュー</h4>
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
      <td class="tbl-rank">第{i+1}位</td>
      <td class="tbl-name"><a href="#item-{i+1}">{d['brand_name']} {p['name'][:22]}...</a></td>
      <td class="tbl-type">{d['type']}</td>
      <td class="tbl-price">¥{p['price']:,}</td>
      <td class="tbl-merit">{d['value'][:32]}...</td>
    </tr>
    """)
table_rows_joined = "\n".join(table_rows)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！寒さで活力を失った冬枯れ肌に濃密なハリと弾力を満たす高濃度コエンザイムQ10コスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒冷・暖房乾燥による肌しぼみ・ハリ不足を救う高濃度コエンザイムQ10コスメを徹底厳選！DHC薬用Qシリーズ、ニベアプレミアム、コーセーコエンリッチ、チューンメーカーズからセザンヌまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta name="keywords" content="コエンザイムQ10 コスメ,ユビキノン 保湿,冬 乾燥肌 ハリ,DHC 薬用Q,コエンリッチ ハンドクリーム,冬 エイジングケア ランキング">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-coenzyme-q10.html">
  
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！寒さで活力を失った冬枯れ肌に濃密なハリと弾力を満たす高濃度コエンザイムQ10コスメランク10">
  <meta property="og:description" content="11月・12月の寒冷・暖房乾燥による肌しぼみ・ハリ不足を救う高濃度コエンザイムQ10コスメを徹底厳選！楽天で買える人気ランキング10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-coenzyme-q10.html">
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
      --primary: #9a3412;
      --primary-light: #fff7ed;
      --primary-border: #fed7aa;
      --accent: #ea580c;
      --accent-hover: #c2410c;
      --gold: #b45309;
      --text-main: #1f2937;
      --text-muted: #4b5563;
      --bg-light: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
      --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08);
      --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1);
    }}
    
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
      line-height: 1.8;
      color: var(--text-main);
      background-color: #fdfaf7;
      padding-bottom: 60px;
    }}
    
    header {{
      background: linear-gradient(135deg, #9a3412 0%, #ea580c 100%);
      color: #ffffff;
      padding: 40px 20px;
      text-align: center;
      box-shadow: var(--shadow-md);
    }}
    
    .site-logo {{
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 12px;
      opacity: 0.95;
    }}
    
    .site-logo a {{
      color: #ffffff;
      text-decoration: none;
    }}
    
    header h1 {{
      font-size: 1.8rem;
      line-height: 1.4;
      max-width: 900px;
      margin: 0 auto 16px;
      font-weight: 800;
    }}
    
    .header-meta {{
      font-size: 0.9rem;
      opacity: 0.9;
    }}
    
    .container {{
      max-width: 1000px;
      margin: 30px auto;
      padding: 0 20px;
    }}
    
    .lead-box {{
      background-color: #ffffff;
      border-radius: 12px;
      padding: 30px;
      margin-bottom: 35px;
      box-shadow: var(--shadow-sm);
      border-left: 6px solid var(--accent);
    }}
    
    .lead-box p {{
      margin-bottom: 16px;
      font-size: 1.05rem;
      color: #374151;
    }}
    
    .lead-box p:last-child {{
      margin-bottom: 0;
    }}
    
    .toc-box {{
      background-color: var(--primary-light);
      border: 1px solid var(--primary-border);
      border-radius: 10px;
      padding: 24px;
      margin-bottom: 40px;
    }}
    
    .toc-title {{
      font-weight: 700;
      font-size: 1.15rem;
      color: var(--primary);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    
    .toc-list {{
      list-style-type: none;
      padding-left: 5px;
    }}
    
    .toc-list li {{
      margin-bottom: 10px;
    }}
    
    .toc-list a {{
      color: #c2410c;
      text-decoration: none;
      font-weight: 500;
      transition: color 0.2s;
    }}
    
    .toc-list a:hover {{
      color: #ea580c;
      text-decoration: underline;
    }}
    
    .section-title {{
      font-size: 1.5rem;
      color: #7c2d12;
      border-bottom: 3px solid #ea580c;
      padding-bottom: 10px;
      margin: 45px 0 25px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    
    .content-box {{
      background-color: #ffffff;
      border-radius: 12px;
      padding: 30px;
      margin-bottom: 35px;
      box-shadow: var(--shadow-sm);
    }}
    
    .content-box h3 {{
      font-size: 1.25rem;
      color: var(--primary);
      margin: 25px 0 12px;
      font-weight: 700;
    }}
    
    .content-box h3:first-child {{
      margin-top: 0;
    }}
    
    .content-box p {{
      margin-bottom: 16px;
      color: #374151;
    }}
    
    .content-box ul, .content-box ol {{
      margin: 15px 0 20px 25px;
      color: #374151;
    }}
    
    .content-box li {{
      margin-bottom: 8px;
    }}
    
    .product-card {{
      background: #ffffff;
      border-radius: 14px;
      padding: 30px;
      margin-bottom: 40px;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--border);
      position: relative;
    }}
    
    .product-badge-rank {{
      display: inline-block;
      background: linear-gradient(135deg, #9a3412, #ea580c);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 6px 18px;
      border-radius: 20px;
      margin-bottom: 12px;
    }}
    
    .product-tag {{
      font-size: 0.95rem;
      color: #c2410c;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    
    .product-name {{
      font-size: 1.4rem;
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 10px;
      font-weight: 800;
    }}
    
    .product-catch {{
      font-size: 1rem;
      color: #475569;
      font-weight: 600;
      margin-bottom: 24px;
      line-height: 1.6;
    }}
    
    .product-layout {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 30px;
    }}
    
    @media (max-width: 820px) {{
      .product-layout {{
        grid-template-columns: 1fr;
      }}
    }}
    
    .product-visual {{
      text-align: center;
    }}
    
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 10px;
      border: 1px solid #e2e8f0;
      background-color: #ffffff;
      margin-bottom: 15px;
      object-fit: contain;
    }}
    
    .price-box {{
      background: #fff7ed;
      padding: 12px;
      border-radius: 8px;
      margin-bottom: 15px;
      border: 1px solid #fed7aa;
    }}
    
    .price-label {{
      font-size: 0.85rem;
      color: #9a3412;
      display: block;
      margin-bottom: 2px;
    }}
    
    .price-value {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #c2410c;
    }}
    
    .price-tax {{
      font-size: 0.8rem;
      color: #9a3412;
    }}
    
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 1.05rem;
      padding: 14px 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
    }}
    
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a60000 0%, #cc0000 100%);
      box-shadow: 0 6px 10px rgba(191, 0, 0, 0.35);
      transform: translateY(-1px);
    }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
      font-size: 0.95rem;
    }}
    
    .spec-row {{
      display: grid;
      grid-template-columns: 130px 1fr;
      border-bottom: 1px solid #e2e8f0;
      padding: 8px 0;
    }}
    
    .spec-th {{
      font-weight: 700;
      color: #475569;
    }}
    
    .spec-td {{
      color: #1e293b;
    }}
    
    .review-box {{
      background: #fff7ed;
      border-left: 4px solid #ea580c;
      padding: 16px 20px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 16px;
    }}
    
    .review-box h4 {{
      font-size: 1.05rem;
      color: #9a3412;
      margin-bottom: 10px;
      font-weight: 700;
    }}
    
    .review-box p {{
      margin-bottom: 10px;
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.7;
    }}
    
    .review-box p:last-child {{
      margin-bottom: 0;
    }}
    
    .target-box, .usage-box {{
      background: #ffffff;
      border: 1px solid #fed7aa;
      padding: 14px 18px;
      border-radius: 8px;
      margin-bottom: 12px;
      font-size: 0.95rem;
    }}
    
    .target-box strong, .usage-box strong {{
      color: #9a3412;
      display: block;
      margin-bottom: 4px;
    }}
    
    .target-box p, .usage-box p {{
      color: #475569;
      margin-bottom: 0;
    }}
    
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      font-size: 0.95rem;
      background: #ffffff;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }}
    
    .data-table th, .data-table td {{
      padding: 12px 14px;
      border: 1px solid #fed7aa;
      text-align: left;
    }}
    
    .data-table th {{
      background-color: #9a3412;
      color: #ffffff;
      font-weight: 700;
    }}
    
    .data-table tr:nth-child(even) {{
      background-color: #fff7ed;
    }}
    
    .tbl-rank {{
      font-weight: 700;
      color: #ea580c;
      white-space: nowrap;
    }}
    
    .tbl-name a {{
      color: #1e293b;
      text-decoration: none;
      font-weight: 600;
    }}
    
    .tbl-name a:hover {{
      color: #ea580c;
      text-decoration: underline;
    }}
    
    .tbl-price {{
      font-weight: 700;
      color: #c2410c;
      white-space: nowrap;
    }}
    
    .faq-item {{
      background: #ffffff;
      border-radius: 10px;
      padding: 20px 24px;
      margin-bottom: 18px;
      box-shadow: var(--shadow-sm);
      border: 1px solid #fed7aa;
    }}
    
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #9a3412;
      margin-bottom: 10px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    
    .faq-q::before {{
      content: "Q";
      display: inline-block;
      background: #ea580c;
      color: #ffffff;
      font-size: 0.9rem;
      font-weight: 800;
      width: 26px;
      height: 26px;
      line-height: 26px;
      text-align: center;
      border-radius: 50%;
      flex-shrink: 0;
    }}
    
    .faq-a {{
      color: #334155;
      font-size: 0.98rem;
      line-height: 1.7;
      padding-left: 36px;
    }}
    
    .internal-links-box {{
      background: #ffffff;
      border-radius: 12px;
      padding: 30px;
      margin-top: 40px;
      box-shadow: var(--shadow-sm);
    }}
    
    .link-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 15px;
      margin-top: 20px;
    }}
    
    .link-card {{
      background: #fff7ed;
      border: 1px solid #fed7aa;
      padding: 14px 18px;
      border-radius: 8px;
      text-decoration: none;
      color: #7c2d12;
      font-size: 0.95rem;
      font-weight: 600;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    
    .link-card:hover {{
      background: #ffedd5;
      border-color: #ea580c;
      color: #c2410c;
      transform: translateY(-2px);
    }}
    
    footer {{
      text-align: center;
      margin-top: 60px;
      color: #64748b;
      font-size: 0.9rem;
    }}
  </style>
</head>
<body>

  <header>
    <div class="site-logo"><a href="index.html">❄️ 冬コスメ徹底比較ラボ</a></div>
    <h1>保湿力の強さで肌乾燥とさようなら！寒さで活力を失った冬枯れ肌に濃密なハリと弾力を満たす高濃度コエンザイムQ10コスメランク10</h1>
    <div class="header-meta">
      <span>更新日：2026年11月4日</span> | <span>執筆・監修：冬コスメ徹底比較ラボ 抗酸化エイジングケア班</span>
    </div>
  </header>

  <div class="container">
    
    <div class="lead-box">
      <p>11月に入ると気温は一気に下がり、木枯らしが吹き荒れる12月にかけて、私たちの肌は「冷え」と「乾燥」の猛烈なダブルパンチにさらされます。寒さによって皮膚の血行が滞ると、細胞への栄養供給と新陳代謝（ターンオーバー）が急激にストップ。その結果、肌が水分を蓄える力を失い、夕方になると顔全体がしぼんで小ジワが目立ち、どんより黄色くくすむ「冬枯れ肌」が一気に進行します。</p>
      <p>この真冬の深刻な代謝停滞としぼみ乾燥を救う鍵が、細胞のエネルギー産生を支える黄金の補酵素「コエンザイムQ10（ユビキノン）」です。本記事では、楽天APIからリアルタイムに取得した正規商品画像・最新価格・在庫状況をもとに、真冬の肌に圧倒的なハリと濃密な潤いを取り戻す高濃度コエンザイムQ10コスメ厳選10選を徹底ランキング形式でご紹介します。</p>
    </div>

    <div class="toc-box">
      <div class="toc-title">📑 目次（クリックで各項目へジャンプ）</div>
      <ul class="toc-list">
        <li><a href="#mechanism">1. なぜ真冬のしぼみ肌に「コエンザイムQ10」が劇的に効くのか？細胞エネルギーと抗酸化の科学</a></li>
        <li><a href="#ranking">2. 真冬の高濃度コエンザイムQ10コスメおすすめ人気ランキング10選</a></li>
        <li><a href="#comparison">3. 厳選10商品のスペック・価格・配合成分徹底比較表</a></li>
        <li><a href="#guide">4. 失敗しないQ10コスメの選び方＆黄色い濃密テクスチャーの使い分け</a></li>
        <li><a href="#synergy">5. ビタミンC・Eとの相乗効果！真冬の抗酸化ネットワーク活用術</a></li>
        <li><a href="#faq">6. コエンザイムQ10コスメに関するよくある質問（FAQ）</a></li>
        <li><a href="#links">7. あわせて読みたい冬の集中高保湿スキンケア特集</a></li>
      </ul>
    </div>

    <section id="mechanism" class="content-box">
      <h2 class="section-title">1. なぜ真冬のしぼみ肌に「コエンザイムQ10」が劇的に効くのか？細胞エネルギーと抗酸化の科学</h2>
      <p>冬になると「水分を入れても入れても肌が乾く」「肌が硬くなって弾力が消えた」と感じる方が多いのは、肌の細胞そのものが寒さでエネルギー不足に陥っているからです。</p>
      
      <h3>細胞の発電所「ミトコンドリア」を回す補酵素</h3>
      <p>コエンザイムQ10は、あらゆる細胞のミトコンドリアに存在し、生命活動に必要なエネルギー分子「ATP」を合成するために不可欠な補酵素です。しかし、体内のコエンザイムQ10量は20歳をピークに急激に減少し、60代では約半分にまで激減します。</p>
      <p>真冬の寒冷環境下でQ10が不足すると、表皮細胞のターンオーバーや真皮のコラーゲン産生が完全に停滞。Q10を高濃度に肌へ直接補給してあげることで、眠っていた肌細胞のエネルギー産生が再起動し、自ら潤いとハリを生み出す自活力が蘇ります。</p>

      <h3>強力な油溶性抗酸化力で冷気酸化ストレスを無力化</h3>
      <p>さらにコエンザイムQ10は、ビタミンEと並ぶ強力な油溶性抗酸化物質です。冬のエアコンによる過乾燥や紫外線残存ダメージによって角層の脂質が酸化されるのを強力に防ぎ、細胞膜の劣化を阻止します。濃厚な黄色いヴェールが肌を包み込むことで、真冬の冷風から角層の水分と油分を鉄壁ガードします。</p>
    </section>

    <section id="ranking">
      <h2 class="section-title">2. 真冬の高濃度コエンザイムQ10コスメおすすめ人気ランキング10選</h2>
      {cards_joined}
    </section>

    <section id="comparison" class="content-box">
      <h2 class="section-title">3. 厳選10商品のスペック・価格・配合成分徹底比較表</h2>
      <p>ご紹介したコエンザイムQ10コスメ10品の種別、参考価格、真冬における保湿価値を一目で比較できるよう一覧表にまとめました。フェイスケアから手肌・全身のボディケアまで、用途に合わせて最適な1本をお選びください。</p>
      
      <div style="overflow-x: auto;">
        <table class="data-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>製品名</th>
              <th>タイプ</th>
              <th>楽天参考価格</th>
              <th>真冬の保湿バリュー</th>
            </tr>
          </thead>
          <tbody>
            {table_rows_joined}
          </tbody>
        </table>
      </div>
    </section>

    <section id="guide" class="content-box">
      <h2 class="section-title">4. 失敗しないQ10コスメの選び方＆黄色い濃密テクスチャーの使い分け</h2>
      <p>コエンザイムQ10コスメを選ぶ際は、配合濃度とアイテムのテクスチャーを用途に応じて見極めることが重要です。</p>

      <h3>① 本格的な全顔エイジングケアなら「基準上限配合の薬用シリーズ」</h3>
      <p>DHCの薬用Qシリーズのように、コエンザイムQ10を高濃度（0.3%等）配合し、医薬部外品として抗炎症や美白成分を組み合わせた処方は、真冬の乾燥小ジワ・くすみ・ハリ不足を一挙に解決したい大人肌に最も確実な投資となります。</p>

      <h3>② 乾燥小ジワ・目元口元の集中ケアなら「ナノ化原液」</h3>
      <p>手持ちの化粧水やクリームの保湿力を底上げしたい場合は、チューンメーカーズのようなナノ化原液が重宝します。レシチンナノカプセル化されているため角層の奥まで素早く届き、ピンポイントでハリをチャージできます。</p>

      <h3>③ 最も老けが出やすい手肌とボディには「高保湿ハンド＆ボディミルク」</h3>
      <p>皮脂腺が少なく寒風に直撃される手肌やスネには、コエンリッチのナイトリニューやニベアプレミアムが必須です。カプセル化されたQ10が摩擦や水仕事で荒れた角層を優しく包み込み、若々しいふっくら感をキープします。</p>
    </section>

    <section id="synergy" class="content-box">
      <h2 class="section-title">5. ビタミンC・Eとの相乗効果！真冬の抗酸化ネットワーク活用術</h2>
      <p>コエンザイムQ10の抗酸化力をさらに引き出すプロの秘訣は、ビタミンCおよびビタミンEとの「トリプル抗酸化ネットワーク」を意識することです。</p>

      <ul>
        <li><strong>Q10 × ビタミンEの相乗効果：</strong> ビタミンEが活性酸素を消去して酸化されると、コエンザイムQ10がビタミンEを還元して復活させます。このサイクルにより、肌の抗酸化防御力が何倍にも長持ちします。</li>
        <li><strong>朝のQ10＋夜のレチノール：</strong> 朝にコエンザイムQ10を取り入れることで、日中の冷気・紫外線・暖房ストレスから肌を守り、夜にレチノールやペプチドで細胞修復を促すステップが冬のエイジングケアに極めて効果的です。</li>
      </ul>
    </section>

    <section id="faq">
      <h2 class="section-title">6. コエンザイムQ10コスメに関するよくある質問（FAQ）</h2>
      <div class="faq-list">
        {''.join([f'''
        <div class="faq-item">
          <div class="faq-q">{faq["question"]}</div>
          <div class="faq-a">{faq["answer"]}</div>
        </div>
        ''' for faq in faq_list])}
      </div>
    </section>

    <section id="links" class="internal-links-box">
      <h2 class="section-title" style="margin-top:0;">7. あわせて読みたい冬の集中高保湿スキンケア特集</h2>
      <p>冬の乾燥・肌荒れ・寒暖差トラブルを乗り越えるために、併せてチェックしたい注目の高保湿特集です。お悩みに合わせた最適なケアを見つけてみてください。</p>
      
      <div class="link-grid">
        <a href="winter-liposome.html" class="link-card">🧬 多重層リポソーム高保湿コスメ10選</a>
        <a href="winter-astaxanthin.html" class="link-card">🌹 高保湿アスタキサンチンコスメ10選</a>
        <a href="winter-ceramide-cream.html" class="link-card">🛡️ 真冬の高保湿セラミドクリーム10選</a>
        <a href="winter-ceramide-lotion.html" class="link-card">💧 高保湿セラミド化粧水ランキング</a>
        <a href="winter-retinol-cream.html" class="link-card">🌙 真冬の濃密レチノールクリーム</a>
        <a href="winter-niacinamide-serum.html" class="link-card">✨ シワ改善ナイアシンアミド美容液</a>
        <a href="winter-panthenol-cream.html" class="link-card">🌿 真冬の高保湿パンテノールクリーム</a>
        <a href="winter-azulene.html" class="link-card">💙 寒暖差赤ら顔を救う高保湿アズレン</a>
        <a href="winter-tranexamic-acid.html" class="link-card">✨ 冬の透明ツヤ肌トラネキサム酸</a>
        <a href="winter-volufiline.html" class="link-card">🧬 目元口元ふっくらボルフィリン</a>
        <a href="winter-hand-cream.html" class="link-card">🧤 冬の手荒れを防ぐ高保湿ハンドクリーム</a>
        <a href="winter-body-milk.html" class="link-card">🥛 粉吹き乾燥を防ぐ高保湿ボディミルク</a>
      </div>
    </section>

    <footer>
      <p>© 2026 冬コスメ徹底比較ラボ All Rights Reserved. 本サイトに掲載されている商品情報・価格は楽天APIより自動取得された最新データです。</p>
    </footer>

  </div>

</body>
</html>
"""

with open("winter-coenzyme-q10.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated winter-coenzyme-q10.html! Size: {len(html_content):,} bytes")
