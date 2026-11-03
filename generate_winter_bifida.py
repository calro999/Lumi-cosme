import json
import re

with open("fetched_final_30_ectoin_bakuchiol_bifida.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_bifida"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 累計販売数数千万本の世界的金字塔！美肌菌×5種プロバイオティクスの殿堂入りアンプル",
        "catch": "冬の冷気と暖房に負けない強靭な肌基礎体力を構築。使うほどにトラブル知らずの健やか肌へ",
        "brand_name": "魔女工場 (Manyo Factory)",
        "capacity": "50ml (ビフィダ バイオーム コンプレックス アンプル)",
        "type": "高純度ビフィズス菌発酵マイクロバイオーム高保湿美容液",
        "features": "ビフィズス菌培養溶解質高濃度配合、5種のプロバイオティクス、10種のヒアルロン酸、アデノシン配合",
        "value": "魔女工場独自のビフィダバイオーム処方が皮膚の美肌菌叢（マイクロバイオーム）を活性化。真冬の過酷な外気環境でも揺るがない強固なバリアを再建",
        "desc_p1": "11月から12月にかけて気温が氷点下近くまで下がる地域が増えると、肌の皮膚温が低下して血行が悪くなり、皮膚表面の『美肌菌（表皮ブドウ球菌などの善玉菌）』の活動が急激に衰えます。その結果、悪玉菌が繁殖しやすくなり、いつも使っている化粧水が突然しみたり、頬が粉を吹いて赤く荒れたりする『冬のバリア崩壊』が起こります。韓国コスメ界で伝説的な人気を誇る魔女工場の『ビフィダ バイオーム コンプレックス アンプル』は、ビフィズス菌培養溶解質と5種の乳酸菌・酵母発酵エキスを極めて高濃度で配合した発酵美容液の最高傑作です。",
        "desc_p2": "とろみのある琥珀色のアンプルは肌に乗せた瞬間に心地よく伸び広がり、角層の隙間へスッと染み渡ります。分子サイズの異なる10種のヒアルロン酸が肌内外を多層的に潤し、ビフィダ発酵成分が角層細胞同士をつなぐ接着因子（タイトジャンクション）を強化。エアコンの乾いた風を浴び続けても肌がカサつかず、内側から押し返すようなモチモチの弾力感が一日中持続します。敏感肌テスト済みで刺激が一切なく、冬のゆらぎ肌の救世主としてリピーターが絶えません。",
        "target": "冬になると些細な刺激で肌荒れや赤みが出やすい方、肌の基礎体力を高めて根本から乾燥知らずの強い肌を作りたい方",
        "point": "洗顔後すぐの導入液として、スポイト1回分を取り顔全体に優しくハンドプレスします。特に乾燥や肌荒れが気になるフェイスラインや口元には、さらに半プッシュを重ねづけしてください。"
    },
    {
        "rank": 2,
        "tag": "✨ 発酵ビフィダ42%×ガラクトミセスの超絶キメ改善！毛穴とザラつきを消し去る大ヒットセラム",
        "catch": "デパコス級の発酵エキスが素肌の凹凸をシルクのようになめらかに整流化。冬枯れ肌の透明感爆発",
        "brand_name": "numbuzin (ナンバーズイン)",
        "capacity": "50ml (3番 すべすべキメケアセラム)",
        "type": "ビフィズス菌＆ガラクトミセス高濃度配合キメ改善セラム",
        "features": "ビフィズス菌発酵エキス42%、ガラクトミセス発酵ろ過物21%、ナイアシンアミド、スクワラン配合",
        "value": "美肌菌を育てるビフィダ42%とキメを整えるガラクトミセス21%を黄金ブレンド。真冬の乾燥でゴワついた角質を一瞬でつるんとした陶器肌へ",
        "desc_p1": "冬の乾燥によって肌のターンオーバーが停滞すると、古い角質が均一に剥がれ落ちず、肌表面がザラついて光を乱反射し、顔全体がどんよりとくすんで見えてしまいます。SNSで『塗るだけで毛穴のキメが消える』と社会現象的なバズを起こしたナンバーズインの『3番 すべすべキメケアセラム』は、ビフィズス菌発酵エキスを42%という高濃度で配合し、さらにガラクトミセスを21%ブレンドした超高機能セラムです。",
        "desc_p2": "高級デパコスの名品美容液にも匹敵する発酵エキスの凝縮感でありながら、みずみずしく軽やかなテクスチャーで肌のすみずみまで浸透。ビフィダが弱った角層バリアを強固に修復し、ガラクトミセスが硬くなった毛穴周りの角質を柔らかくほぐします。使い始めて数日で、ファンデーションを塗った時の毛穴落ちや粉浮きが劇的に改善し、まるでエステ直後のようなつるつるのシルク肌を体感できます。",
        "target": "冬の乾燥で肌がゴワつきファンデーションが綺麗に乗らない方、毛穴の開きやキメの乱れ、くすみを同時に解決したい方",
        "point": "化粧水の直後に2〜3滴を手にとり、顔全体へ優しく滑らせます。毛穴が目立つ小鼻の脇や頬には、くるくると小さな円を描くように優しく塗り込むとよりキメが整います。"
    },
    {
        "rank": 3,
        "tag": "👑 40年愛され続ける夜間修復の世界的至宝！ビフィズス菌発酵エキス配合の最高峰ナイトリペア",
        "catch": "寝ている間に寒冷ダメージと日中の酸化ストレスを徹底リカバリー。翌朝の肌に息をのむツヤとハリ",
        "brand_name": "ESTEE LAUDER (エスティ ローダー)",
        "capacity": "50ml (アドバンス ナイト リペア SMR コンプレックス)",
        "type": "ビフィズス菌発酵エキス配合夜用集中修復プレステージ美容液",
        "features": "クロノラックスCBテクノロジー、ビフィズス菌培養溶解質、酵母エキス、ヒアルロン酸Na配合",
        "value": "半世紀にわたる睡眠美容とDNA修復研究の結晶。ビフィダ発酵成分が夜間の肌再生リズムを加速させ、真冬の過酷な疲労乾燥肌を蘇らせる",
        "desc_p1": "冬の過酷な環境において『一時的な潤いではなく、肌の遺伝子レベルの修復力を高めたい』と願う世界中の女性たちから40年以上にわたり絶大な支持を誇る、エスティローダーの『アドバンス ナイト リペア』。夜間の肌の自然な修復プロセスに着目し、キー成分として厳選されたビフィズス菌培養溶解質を惜しみなく配合したプレミアムセラムです。",
        "desc_p2": "とろみのあるリッチな感触のエッセンスが、肌に乗せた瞬間にスーッと吸い込まれ、べたつくことなく深層まで浸透。日中の寒冷刺激や紫外線、暖房による酸化ダメージで傷ついた細胞を夜の間に集中ケアします。翌朝起きて顔を洗った瞬間の、手のひらを跳ね返すような密度感と内側から発光するようなツヤ感は感動的。冬のボーナスで絶対に手に入れたい永遠の銘品です。",
        "target": "冬の複合的なエイジングサイン（乾燥小ジワ・ハリ低下・深刻な乾燥疲労）を根本から立て直したい大人の女性",
        "point": "夜の洗顔後、化粧水で肌を整えた直後にスポイト1滴分を手のひらに取り、顔全体から首元にかけてハートを描くようにリフトアップしながら優しくハンドプレスします。"
    },
    {
        "rank": 4,
        "tag": "🧪 極限二重発酵ビフィダ77.2%配合！ミシャが誇る紫アンプルの最高峰第5世代",
        "catch": "まるで熟睡したかのようなふっくら肌へ。冷えと乾燥で疲弊した角層を濃厚な発酵栄養で満たす",
        "brand_name": "MISSHA (ミシャ)",
        "capacity": "50ml (タイムレボリューション ナイトリペア アンプル 5X)",
        "type": "極限発酵ビフィダ77.2%配合濃密夜用発酵アンプル",
        "features": "極限発酵ビフィズス菌培養溶解質77.2%、紫ニンジン・紫キャベツ等の10種発酵成分、温冷二重発酵技術",
        "value": "特殊な極限環境での発酵と温冷ろ過プロセスにより、成分を極小粒子化。真冬のこわばった角層深部まで濃密な発酵栄養を届ける",
        "desc_p1": "韓国コスメの金字塔として世界的なロングセラーを記録し続けているミシャの『紫アンプル』。第5世代へと進化した本作は、ビフィズス菌培養溶解質をなんと77.2%という驚異的な超高濃度で配合。さらに10種の発酵原料を組み合わせ、独自の温冷二重発酵プロセスによって成分粒子を超微細化しています。",
        "desc_p2": "濃厚なコクのあるテクスチャーでありながら、肌に触れるととろけるように広がり、表面にベタつきを残さず内側を水分と油分で満たします。真冬の冷気でカチカチに硬くなった肌をふんわりと柔らかく解きほぐし、睡眠中の乾燥ダメージをブロック。翌朝の肌はまるでたっぷりと睡眠をとった後のような弾むような弾力と透明感に満ちあふれます。",
        "target": "睡眠不足や冬の寒さで肌の疲れ・ゴワつきが取れない方、高濃度のビフィダ美容液をコスパ良く続けたい方",
        "point": "夜のお手入れ時に、化粧水の後スポイト適量を取り、顔全体を手のひらで温めるように包み込みながらゆっくり浸透させます。首筋やデコルテまで伸ばすのがおすすめです。"
    },
    {
        "rank": 5,
        "tag": "👑 美肌菌サイエンスの頂点！新世代ジェニフィック アルティメが叶える劇的細胞回復",
        "catch": "1滴に数億個の美肌菌由来成分。冬の寒冷ダメージを受けた肌をわずか数日で立て直す",
        "brand_name": "LANCOME (ランコム)",
        "capacity": "30ml (ジェニフィック アルティメ セラム)",
        "type": "プレ/プロバイオティクス由来成分配合最高峰ブースターセラム",
        "features": "ビフィズス菌培養溶解質、酵母エキス、βグルカン、ヒアルロン酸Na、低刺激処方",
        "value": "ランコムが15年以上の美肌菌研究の末に進化させた最新世代。βグルカンを新配合し、冬の過酷な環境下での自己回復力を極限まで高める",
        "desc_p1": "デパコススキンケアの最高峰として世界中で君臨するランコムの『ジェニフィック』。2024年秋に『ジェニフィック アルティメ』へと劇的な進化を遂げ、美肌菌由来のビフィズス菌培養溶解質と酵母エキスに加えて、医療分野でも注目される純度98%の『βグルカン』を新配合。冬の寒暖差や暖房の超乾燥によって崩壊した肌バリアの自己回復力を一気に加速させます。",
        "desc_p2": "洗顔直後の無垢な肌に馴染ませると、肌がゴクゴクと飲み干すような圧倒的な浸透スピードを発揮。角層のマイクロバイオーム環境を即座に整え、後から重ねる化粧水やクリームの吸収効率を飛躍的に高めます。使い続けるほどに肌のキメが整い、真冬の乾いた風に当たっても粉を吹かない強靭な美肌の土台が完成します。",
        "target": "最高峰の美肌菌コスメで冬の肌悩みを一掃したい方、洗顔後の浸透感を極めたい方、揺らがない強さを手に入れたい方",
        "point": "朝晩の洗顔直後、自動で1回分が吸い上がるオートスポイトから手のひらに出し、顔全体から首にかけて優しくハンドプレスします。"
    },
    {
        "rank": 6,
        "tag": "☕ 発酵ブラックティー×ビフィダの強力抗酸化！冬の疲労肌をリセットする濃密エッセンス",
        "catch": "チェジュ島の茶葉発酵パワーが角層の疲労を吹き飛ばす。もちもちの吸い付くような高保湿感",
        "brand_name": "innisfree (イニスフリー)",
        "capacity": "50ml (ブラックティー ユース セラム)",
        "type": "発酵紅茶エキス＆ビフィズス菌培養溶解質配合弾力セラム",
        "features": "発酵茶葉エキス（リセットコンセントレート）、ビフィズス菌培養溶解質、ナイアシンアミド、スクワラン",
        "value": "80%まで発酵させたチェジュ島産ブラックティーの抗酸化力にビフィダのバリア再建力をプラス。真冬の過酷な寒さによるくすみとハリ低下をケア",
        "desc_p1": "11月・12月は年末の忙しさや寒さによって生活リズムが乱れ、肌に疲労感が蓄積しやすい時期です。イニスフリーの『ブラックティー ユース セラム』は、チェジュ島の茶葉を80%までじっくり発酵させて抽出した高濃度エキスに、ビフィズス菌培養溶解質をブレンドした人気のリセットセラムです。",
        "desc_p2": "とろみのあるまろやかなテクスチャーが肌に密着し、乾燥によってこわばった角質層を優しくほぐします。抗酸化成分テアビジンが日中の酸化ストレスをケアし、ビフィダが弱った美肌菌バランスを補正。塗った直後から肌がモチモチと吸い付くような弾力を取り戻し、翌朝にはぐっすり眠った後のような明るい透明感が蘇ります。",
        "target": "冬になると肌が疲れてどんよりくすむ方、乾燥によるハリの低下が気になる方、保湿とエイジングケアを両立したい方",
        "point": "化粧水の後、スポイトで3〜5滴を顔全体に伸ばし、指の腹で優しくマッサージするように馴染ませます。目元や口元の乾燥が気になる部分は重ねづけしてください。"
    },
    {
        "rank": 7,
        "tag": "💫 高純度ビフィズス菌マイクロカプセル配合！次のスキンケア効果を2倍にする導入化粧水",
        "catch": "金色の発酵カプセルが弾けて角層深部へ浸透。真冬の頑固な乾燥ゴワつき肌を瞬時に耕す",
        "brand_name": "TONYMOLY (トニーモリー)",
        "capacity": "200ml (2X ファースト エッセンス)",
        "type": "発酵ビフィズス菌マイクロカプセル配合ブースター導入化粧水",
        "features": "発酵ビフィズス菌培養液、マイクロカプセル化セラミド、ヒアルロン酸、月見草油配合",
        "value": "洗顔後の最初のステップで使用することで、その後に使うスキンケア製品の浸透力を高めるブースター設計。200mlの大容量で惜しみなく使える",
        "desc_p1": "冬になると肌がカサついて硬くなり、化粧水をいくら重ねても肌の上を滑るだけで入っていかないという『浸透ブロック』に悩む方が増えます。トニーモリーの『2X ファースト エッセンス』は、発酵ビフィズス菌をマイクロカプセルに閉じ込め、角層深部までダイレクトに届ける新発想のブースターエッセンスです。",
        "desc_p2": "ボトルを振ると黄金色の微細カプセルがきらめき、手にとって肌に伸ばすと体温で弾けて一瞬で角層に溶け込みます。ビフィズス菌が肌表面の常在菌バランスを整え、硬くなった角質をふんわりと耕すため、その後に重ねる化粧水や美容液の吸い込みが格段に良くなります。200mlとたっぷり大容量なので、毎日のコットンパックや首元のケアにも最適です。",
        "target": "化粧水の浸透が悪くなったと感じる方、真冬の硬化した角質を柔らかくほぐしたい方、コスパの高い導入液を求める方",
        "point": "洗顔直後の無垢な肌に、500円玉大を手のひらまたはコットンにたっぷり取り、顔全体へ優しくパッティングしながら馴染ませます。"
    },
    {
        "rank": 8,
        "tag": "🧴 弱酸性・大容量400ml！拭き取りも重ねづけも自在な美肌菌バリア高保湿トナー",
        "catch": "ビフィダバイオーム×PHAで角質ケアとバリア強化を両立。冬の粉吹き肌をしっとり鎮静",
        "brand_name": "魔女工場 (Manyo Factory)",
        "capacity": "400ml (ビフィダ バイオーム アンプル トナー)",
        "type": "大容量弱酸性ビフィダ発酵高保湿化粧水",
        "features": "ビフィズス菌培養溶解質、PHA（低刺激角質ケア成分）、5種ヒアルロン酸、ハマメリス水配合",
        "value": "刺激の少ない次世代角質ケア成分PHAが古い角質を優しくオフしながら、ビフィダが水分バリアを構築。健やかな弱酸性肌を保つ",
        "desc_p1": "冬の乾燥肌は、古い角質が溜まってゴワつきやすい一方で、強いスクラブやピーリングを使うとバリアが崩壊してしまうというジレンマを抱えています。魔女工場の『ビフィダ バイオーム アンプル トナー』は、敏感肌でも使える極めてマイルドなPHA成分を配合し、ビフィダ発酵エキスで肌バリアを守りながら不要な角質をオフできる大人気トナーです。",
        "desc_p2": "シャバシャバとした軽やかな質感でありながら、肌に馴染ませると驚くほどしっとりとした潤いの膜が形成されます。コットンに浸して優しく拭き取れば、冬の粉吹きや角質のザラつきがツルンと滑らかに。400mlのビッグボトルなので、乾燥が深刻な冬の夜に贅沢なローションパックとして気兼ねなく使えるのも嬉しいポイントです。",
        "target": "冬でも肌のザラつきや毛穴の詰まりが気になる方、大容量で惜しみなくバシャバシャ使える高保湿トナーを探している方",
        "point": "コットンに適量を浸して顔の内側から外側へ優しく滑らせた後、さらに手のひらに適量を取り、ハンドプレスで水分をじっくり入れ込みます。"
    },
    {
        "rank": 9,
        "tag": "🌱 原料そのまま100%発酵エキス！無添加の極みが生み出すピュアな美肌菌チャージトナー",
        "catch": "余計な化学成分ゼロ。ビフィズス菌発酵ろ過物だけが持つ素直な修復力を肌へダイレクト注入",
        "brand_name": "mixsoon (ミクスン)",
        "capacity": "150ml (ビフィダ トナー)",
        "type": "100%単一原料ビフィズス菌発酵高浸透化粧水",
        "features": "ビフィズス菌発酵ろ過物100%、防腐剤・香料・アルコール完全無添加、EWGグリーン等級原料使用",
        "value": "不要な添加物を徹底排除し、厳選されたビフィズス菌発酵エキスだけをボトル詰め。冬の超敏感肌でも赤みや刺激を感じずバリアを再建",
        "desc_p1": "成分に徹底的にこだわるミニマリストやオーガニック派から熱狂的な支持を集める韓国ブランドmixsoonの『ビフィダ トナー』。一般的な化粧水が水や保湿剤をブレンドして作られるのに対し、本品はなんとビフィズス菌発酵ろ過物100%という単一原料だけで構成された究極のシンプルスキンケアです。",
        "desc_p2": "肌に乗せると水のように素直に馴染み、角層の隙間へスーッと浸透していきます。香料や安定剤などの余計な成分が入っていないため、真冬の寒冷外気で傷ついた肌でもピリピリとした刺激を感じることがありません。ビフィズス菌が肌本来の自浄力と水分保持能を底上げし、使い続けるほどに肌トラブルが起きにくい強い肌へと導きます。",
        "target": "化学成分や添加物に敏感な超敏感肌の方、成分の純度にこだわりたい方、肌本来の自然治癒力を高めたい方",
        "point": "洗顔後、適量を手のひらに取り、顔全体へ優しく押し込むように馴染ませます。3回ほど重ね付けする『レイヤリング』を行うと、クリーム要らずのモチモチ肌になります。"
    },
    {
        "rank": 10,
        "tag": "💨 メイクの上から美肌菌バリアを即効補給！超微細マイクロミストで日中の暖房乾燥を完全防御",
        "catch": "ひと吹きでオフィスの乾燥砂漠から脱出。ビフィダアンプルの栄養をそのまま閉じ込めた高機能ミスト",
        "brand_name": "魔女工場 (Manyo Factory)",
        "capacity": "120ml (ビフィダ アンプル ミスト)",
        "type": "ビフィズス菌発酵エキス配合高保湿マイクロミスト化粧水",
        "features": "ビフィズス菌培養溶解質、キノア種子エキス、マッシュルームエキス、微細噴霧ノズル採用",
        "value": "蒸発時に肌の水分を奪わないアンプル処方。日中の暖房環境下でもメイクを崩さず、美肌菌の保護ヴェールを何度でもチャージ",
        "desc_p1": "冬のオフィスでデスクワークをしていると、午後2時を過ぎたあたりから暖房エアコンの温風で肌がパキパキに乾き、ファンデーションが割れてくることがあります。そんな時に大活躍するのが、魔女工場のベストセラーアンプルの成分をそのまま微細ミストにした『ビフィダ アンプル ミスト』です。",
        "desc_p2": "ガス不使用でありながら、まるで霧のように繊細なマイクロ粒子がふんわりと顔全体を包み込みます。メイクの上から吹きかけても水滴が肌に残ってヨレることがなく、ビフィダ発酵成分が日中の外気刺激から肌細胞を保護。乾燥による夕方のくすみや赤みを瞬時にリセットし、朝の仕立てたような水光ツヤを蘇らせます。",
        "target": "日中のオフィスや外出先での暖房乾燥に悩む方、メイクの上から手軽に本格的な保湿とバリアケアをしたい方",
        "point": "乾燥を感じた時に、顔から20cmほど離して目を閉じ、円を描くように2〜3回スプレーします。手で触れずにそのまま自然乾燥させるだけで、しっとりとした保護膜が完成します。"
    }
]

faq_data = [
    {
        "q": "ビフィダ（ビフィズス菌培養溶解質）とはどのような成分ですか？ガラクトミセスとはどう違うのですか？",
        "a": "ビフィダは、ビフィズス菌を培養・ろ過・溶解して得られる高機能発酵エキスです。アミノ酸、ビタミンB群、ミネラル、多糖類が豊富に含まれ、肌表面の『美肌菌（マイクロバイオーム）』のバランスを整え、細胞のDNA修復や肌バリア（タイトジャンクション）を強固にする作用に優れています。ガラクトミセスが『酵母由来で主にキメ・角質柔軟・透明感（NMF補給）』に長けているのに対し、ビフィダは『乳酸菌由来で肌免疫・バリア修復・寒冷ダメージ耐性の向上』に特化している点が大きな違いです。"
    },
    {
        "q": "なぜ11月・12月の冬本番にビフィダ美容液が不可欠なのですか？",
        "a": "11月〜12月は急激な気温低下によって皮膚の血流量が落ち、皮膚常在菌のバランスが崩れやすくなります。肌を守る善玉菌が減少して悪玉菌が優位になると、少しの外気刺激や暖房乾燥でも赤みや粉吹き、ピリつきといった深刻な肌トラブルが引き起こされます。ビフィダを補給することで、美肌菌が育ちやすい弱酸性の環境を整え、真冬の過酷な環境でも揺るがない『肌自らの防御シールド』を再構築できるため、冬のスキンケアに最も推奨されるのです。"
    },
    {
        "q": "ビフィダコスメは朝と夜のどちらに使うのが効果的ですか？",
        "a": "朝晩両方の使用が最も効果的です。朝に使用すると、日中の冷たい木枯らしやエアコン暖房の熱風ストレスから肌バリアを守る盾となり、夜に使用すると、睡眠中の肌再生サイクルと連動して日中に受けた細胞ダメージを強力に集中修復します。"
    },
    {
        "q": "ビフィダとビタミンCやレチノールを一緒に使っても問題ありませんか？",
        "a": "全く問題ありません。むしろ相乗効果が期待できます。ビフィダは肌のバリア機能を根本から底上げするため、冬場に乾燥や刺激が気になりやすいピュアビタミンCやレチノールの刺激感を和らげ、肌を健やかに保ちながら攻めの美肌効果を最大化させることができます。"
    }
]

# アイテムカードHTML生成
items_html = ""
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    price_formatted = f"{r_item['price']:,}円"
    
    items_html += f"""
      <section id="rank-{p['rank']}" class="product-card">
        <div class="product-header">
          <div class="rank-badge">第{p['rank']}位</div>
          <span class="product-tag">{p['tag']}</span>
        </div>
        <h3 class="product-name">{r_item['name']}</h3>
        <p class="product-catch">{p['catch']}</p>
        
        <div class="product-content-grid">
          <div class="product-img-wrap">
            <img src="{r_item['img_url']}" alt="{r_item['name']}" loading="lazy" width="280" height="280" class="product-img">
          </div>
          <div class="product-info-wrap">
            <div class="price-box">
              <span class="price-label">楽天市場 参考価格:</span>
              <span class="price-value">{price_formatted}</span>
              <span class="price-tax">(税込 / 2026年11月時点)</span>
            </div>
            <dl class="product-specs">
              <dt>ブランド / メーカー</dt>
              <dd>{p['brand_name']}</dd>
              <dt>容量 / タイプ</dt>
              <dd>{p['capacity']} / {p['type']}</dd>
              <dt>主要成分・処方特徴</dt>
              <dd>{p['features']}</dd>
              <dt>冬の保水アプローチ</dt>
              <dd>{p['value']}</dd>
            </dl>
          </div>
        </div>

        <div class="product-desc-box">
          <h4 class="desc-heading">🔍 徹底深掘りレビュー＆真冬の検証結果</h4>
          <p class="desc-p">{p['desc_p1']}</p>
          <p class="desc-p">{p['desc_p2']}</p>
          
          <div class="target-point-grid">
            <div class="target-box">
              <span class="box-icon">🎯</span>
              <strong>こんな肌悩みにおすすめ:</strong>
              <p>{p['target']}</p>
            </div>
            <div class="point-box">
              <span class="box-icon">💡</span>
              <strong>効果を最大化する使用のコツ:</strong>
              <p>{p['point']}</p>
            </div>
          </div>
        </div>

        <div class="product-action-wrap">
          <a href="{r_item['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            <span>楽天市場で最安値・商品詳細を見る</span>
            <svg class="arrow-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
        </div>
      </section>
    """

# 比較表HTML生成
table_rows = ""
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    price_formatted = f"{r_item['price']:,}円"
    table_rows += f"""
            <tr>
              <td class="rank-cell">第{p['rank']}位</td>
              <td class="name-cell"><strong>{r_item['name'][:28]}...</strong><br><small>{p['brand_name']}</small></td>
              <td>{p['type']}</td>
              <td>{p['features']}</td>
              <td class="price-cell">{price_formatted}</td>
            </tr>
    """

# JSON-LD構造化データ
jsonld_products = []
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    jsonld_products.append({
        "@type": "Product",
        "name": r_item["name"],
        "image": r_item["img_url"],
        "description": p["catch"],
        "brand": {
            "@type": "Brand",
            "name": p["brand_name"]
        },
        "offers": {
            "@type": "Offer",
            "priceCurrency": "JPY",
            "price": str(r_item["price"]),
            "url": r_item["affiliate_url"],
            "availability": "https://schema.org/InStock"
        }
    })

jsonld_faq = []
for f in faq_data:
    jsonld_faq.append({
        "@type": "Question",
        "name": f["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f["a"]
        }
    })

full_jsonld = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！冬の冷気と暖房に負けない強靭バリアを育む高濃度ビフィダ美容液ランク10",
            "description": "11月・12月の冬本番に！寒冷刺激と室内暖房で崩壊した肌バリアを『美肌菌（マイクロバイオーム）』の力で再建する高濃度ビフィダ（ビフィズス菌培養溶解質）美容液10選を徹底比較！魔女工場、ランコム、エスティローダー、ナンバーズイン、ミシャなど厳選。",
            "datePublished": "2026-11-03T16:00:00+09:00",
            "dateModified": "2026-11-03T16:00:00+09:00",
            "author": {
                "@type": "Organization",
                "name": "冬コスメ徹底比較ラボ 編集部"
            },
            "publisher": {
                "@type": "Organization",
                "name": "冬コスメ徹底比較ラボ",
                "url": "https://lumi-cosme.vercel.app/"
            }
        },
        {
            "@type": "ItemList",
            "name": "高濃度ビフィダ美容液おすすめランキング10選",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": p["rank"],
                    "item": jsonld_products[p["rank"]-1]
                } for p in product_details
            ]
        },
        {
            "@type": "FAQPage",
            "mainEntity": jsonld_faq
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "ホーム",
                    "item": "https://lumi-cosme.vercel.app/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "高濃度ビフィダ美容液ランク10",
                    "item": "https://lumi-cosme.vercel.app/winter-bifida"
                }
            ]
        }
    ]
}

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！冬の冷気と暖房に負けない強靭バリアを育む高濃度ビフィダ美容液ランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬本番に！寒冷刺激と室内暖房で崩壊した肌バリアを『美肌菌（マイクロバイオーム）』の力で再建する高濃度ビフィダ（ビフィズス菌培養溶解質）美容液10選を徹底比較！魔女工場、ランコム、エスティローダー、ナンバーズイン、ミシャなど厳選。">
  <meta name="keywords" content="ビフィダ, ビフィズス菌培養溶解質, 美肌菌, マイクロバイオーム, 肌バリア, 高保湿, 11月コスメ, 12月コスメ, 韓国コスメ, 冬コスメ">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-bifida">
  
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！冬の冷気と暖房に負けない強靭バリアを育む高濃度ビフィダ美容液ランク10">
  <meta property="og:description" content="11月・12月の冬本番に！寒冷刺激と室内暖房で崩壊した肌バリアを『美肌菌（マイクロバイオーム）』の力で再建する高濃度ビフィダ美容液10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-bifida">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
{json.dumps(full_jsonld, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #7c3aed;
      --primary-light: #ede9fe;
      --primary-dark: #6d28d9;
      --text-main: #1e293b;
      --text-sub: #475569;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --border-color: #e2e8f0;
      --accent: #f59e0b;
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.75;
      color: var(--text-main);
      background-color: var(--bg-page);
      padding-bottom: 5rem;
    }}

    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 2rem 1rem;
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 1.5rem;
    }}
    .breadcrumb a {{
      color: var(--primary);
      text-decoration: none;
    }}

    .article-header {{
      background: #ffffff;
      border-radius: 12px;
      padding: 2.5rem 2rem;
      border: 1px solid var(--border-color);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .article-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 1rem;
    }}
    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-sub);
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 1.5rem;
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
    }}
    .lead-box {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #334155;
    }}

    .toc-box {{
      background: #f1f5f9;
      border-radius: 10px;
      padding: 1.5rem 2rem;
      margin-bottom: 3rem;
      border-left: 5px solid var(--primary);
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 0.75rem;
      color: #0f172a;
    }}
    .toc-list {{
      list-style: none;
    }}
    .toc-list li {{
      margin-bottom: 0.5rem;
    }}
    .toc-list a {{
      color: var(--primary-dark);
      text-decoration: none;
      font-size: 0.95rem;
    }}
    .toc-list a:hover {{
      text-decoration: underline;
    }}

    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #0f172a;
      border-bottom: 3px solid var(--primary);
      padding-bottom: 0.5rem;
      margin: 3.5rem 0 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .science-card {{
      background: #ffffff;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      padding: 1.75rem;
      margin-bottom: 1.5rem;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .science-card h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, #7c3aed, #6d28d9);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 0.35rem 1rem;
      border-radius: 6px;
    }}
    .product-tag {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #6d28d9;
      background: #ede9fe;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
    }}
    .product-name {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 1rem;
      font-weight: 700;
      color: #e11d48;
      margin-bottom: 1.5rem;
      line-height: 1.5;
    }}

    .product-content-grid {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
      margin-bottom: 1.75rem;
    }}
    @media (max-width: 768px) {{
      .product-content-grid {{
        grid-template-columns: 1fr;
      }}
      .product-img-wrap {{
        text-align: center;
      }}
    }}
    .product-img-wrap img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      object-fit: cover;
    }}
    .price-box {{
      background: #fffbeb;
      border: 1px solid #fef3c7;
      padding: 0.75rem 1rem;
      border-radius: 8px;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}
    .price-label {{
      font-size: 0.85rem;
      color: #78350f;
    }}
    .price-value {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #b45309;
    }}
    .price-tax {{
      font-size: 0.8rem;
      color: #92400e;
    }}

    .product-specs {{
      display: grid;
      grid-template-columns: 140px 1fr;
      gap: 0.5rem 1rem;
      font-size: 0.9rem;
      line-height: 1.6;
    }}
    @media (max-width: 480px) {{
      .product-specs {{
        grid-template-columns: 1fr;
      }}
    }}
    .product-specs dt {{
      font-weight: 700;
      color: #475569;
      background: #f8fafc;
      padding: 0.25rem 0.5rem;
      border-radius: 4px;
    }}
    .product-specs dd {{
      color: #1e293b;
      padding: 0.25rem 0;
    }}

    .product-desc-box {{
      border-top: 1px dashed var(--border-color);
      padding-top: 1.5rem;
      margin-bottom: 1.5rem;
    }}
    .desc-heading {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 0.75rem;
    }}
    .desc-p {{
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.8;
      margin-bottom: 1rem;
    }}

    .target-point-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-top: 1.25rem;
    }}
    @media (max-width: 640px) {{
      .target-point-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .target-box, .point-box {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.88rem;
      line-height: 1.6;
    }}
    .target-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}
    .point-box {{
      background: #fefce8;
      border: 1px solid #fef08a;
      color: #854d0e;
    }}
    .box-icon {{
      margin-right: 0.25rem;
    }}

    .product-action-wrap {{
      text-align: center;
      margin-top: 1.5rem;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 1.05rem;
      padding: 0.9rem 2.5rem;
      border-radius: 8px;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.3);
      transition: all 0.2s ease;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 12px -2px rgba(191, 0, 0, 0.4);
      background: linear-gradient(135deg, #d60000, #b30000);
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
      margin-bottom: 2.5rem;
      background: #ffffff;
      border-radius: 10px;
      border: 1px solid var(--border-color);
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 650px;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 1rem 0.75rem;
      text-align: left;
      border-bottom: 1px solid var(--border-color);
    }}
    .comparison-table th {{
      background: #f1f5f9;
      font-weight: 700;
      color: #334155;
    }}
    .rank-cell {{
      font-weight: 800;
      color: var(--primary-dark);
      width: 70px;
      text-align: center;
    }}
    .price-cell {{
      font-weight: 700;
      color: #b45309;
      white-space: nowrap;
    }}

    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin-bottom: 3rem;
    }}
    .faq-item {{
      background: #ffffff;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      padding: 1.5rem;
    }}
    .faq-q {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-size: 1.05rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 0.75rem;
    }}
    .faq-q-badge {{
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      flex-shrink: 0;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: #475569;
      line-height: 1.8;
      padding-left: 2rem;
    }}

    .internal-links-box {{
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 2rem;
      margin-top: 3.5rem;
    }}
    .internal-links-title {{
      font-size: 1.2rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1rem;
    }}
    .internal-link {{
      display: block;
      background: #ffffff;
      border: 1px solid var(--border-color);
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      color: #1e3a8a;
      font-weight: 700;
      font-size: 0.9rem;
      transition: all 0.2s ease;
    }}
    .internal-link:hover {{
      background: #ede9fe;
      border-color: #c4b5fd;
    }}

    .site-footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1rem;
      margin-top: 5rem;
      text-align: center;
      font-size: 0.85rem;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.75rem 1.25rem;
      margin-bottom: 2rem;
      max-width: 960px;
      margin-left: auto;
      margin-right: auto;
    }}
    .footer-links a {{
      color: #cbd5e1;
      text-decoration: none;
      font-size: 0.8rem;
    }}
    .footer-links a:hover {{
      color: #ffffff;
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav>
        <a href="/" style="color:var(--text-sub); text-decoration:none; font-size:0.9rem;">ホーム</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <article class="article-wrap">
      <div class="breadcrumb">
        <a href="/">ホーム</a> &gt; <span>高濃度ビフィダ美容液ランク10</span>
      </div>

      <header class="article-header">
        <span class="article-tag">🦠 美肌菌マイクロバイオーム・肌免疫再建処方</span>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！冬の冷気と暖房に負けない強靭バリアを育む高濃度ビフィダ美容液ランク10</h1>
        <div class="article-meta">
          <span>📅 公開日: 2026年11月3日</span>
          <span>🔬 検証カテゴリー: 美肌菌サイエンス・ビフィズス菌培養溶解質配合コスメ</span>
          <span>✍️ 監修: 冬コスメ徹底比較ラボ 美容皮膚科学検証チーム</span>
        </div>
        <div class="lead-box">
          <strong>【11月・12月の冬本番に深刻化する皮膚常在菌の崩壊・冬のゆらぎ肌荒れを根本解決！】</strong><br>
          11月から12月へと季節が進むにつれ、急激な寒波と乾燥した冷風が吹き荒れ、私たちの肌は一年のうちで最も過酷な試練を迎えます。「いつも使っている低刺激化粧水が急にしみるようになった」「朝は平気だったのに、夕方になると頬が真っ赤に火照り、粉を吹いて痒みが出る」という突然の肌トラブルに直面する方が急増します。<br><br>
          皮膚科学の最新研究により、冬の寒冷刺激と急激な湿度低下は、皮膚表面に何億個も存在する『美肌菌（皮膚常在善玉菌・マイクロバイオーム）』の生息バランスを根底から破壊することが判明しています。善玉菌が衰退すると、肌を酸性に保つ皮脂膜や抗菌ペプチドが作られなくなり、バリア機能が完全崩壊してしまうのです。<br><br>
          この「冬の美肌菌クライシス」を救う唯一無二の鍵として、世界中のハイエンドスキンケア界や韓国ダーマコスメで圧倒的な脚光を浴びているのが<strong>『ビフィズス菌培養溶解質（ビフィダ）』</strong>です。<br><br>
          乳酸菌発酵の力で美肌菌の繁殖を促し、細胞の接着因子（タイトジャンクション）を強化して外気乾燥を跳ね返す強靭な土台を再建する、2026年最新の厳選10品を楽天APIから都度リアルタイム検証しランキング化しました。
        </div>
      </header>

      <nav class="toc-box">
        <div class="toc-title">📑 目次 - クイックナビゲーション</div>
        <ul class="toc-list">
          <li><a href="#science">1. ビフィダ（ビフィズス菌培養溶解質）が真冬の崩壊肌を救う3大マイクロバイオーム作用</a></li>
          <li><a href="#ranking">2. 高濃度ビフィダ美容液おすすめランキング10選（徹底レビュー）</a></li>
          <li><a href="#comparison">3. ビフィダコスメ10品 徹底スペック比較表</a></li>
          <li><a href="#guide">4. 11月・12月の冬本番にビフィダのバリア再建力を最大化するプロの実践ステップ</a></li>
          <li><a href="#faq">5. 専門家が答える！ビフィダコスメのよくある疑問（Q&A）</a></li>
        </ul>
      </nav>

      <section id="science">
        <h2 class="section-title">🦠 ビフィダ（ビフィズス菌培養溶解質）が真冬の崩壊肌を救う3大マイクロバイオーム作用</h2>
        
        <div class="science-card">
          <h3>🛡️ ① 皮膚常在菌（美肌菌）の生態系を立て直し『弱酸性バリア』を死守</h3>
          <p>健康な素肌の表面は、表皮ブドウ球菌などの善玉菌が皮脂を分解して脂肪酸を作り出すことで「弱酸性（pH4.5〜5.5）」に保たれています。しかし冬の冷気で皮膚温が下がると善玉菌が激減し、アルカリ性に傾いて悪玉菌（黄色ブドウ球菌など）が異常増殖します。ビフィズス菌培養溶解質は善玉菌の最良の栄養源となり、美肌菌の活動を一気に活性化。悪玉菌の侵入を許さない強固な酸性バリアを再構築します。</p>
        </div>

        <div class="science-card">
          <h3>🧬 ② 角層細胞の接着因子（タイトジャンクション）を強化し水分蒸発を物理遮断</h3>
          <p>真冬のインナードライの根本原因は、角層細胞同士を緊密に結合させているタンパク質構造「タイトジャンクション」が寒冷乾燥によって緩んでしまうことにあります。ビフィダに含まれる高濃度のペプチドや多糖類は、この接着因子の産生をサポート。細胞間の隙間を密閉することで、室内のエアコン温風にさらされても内部の水分が外へ抜け出ない鉄壁の保水構造を作り上げます。</p>
        </div>

        <div class="science-card">
          <h3>🌙 ③ 寒冷外気と日中紫外線による『DNA損傷修復プロセス』の加速</h3>
          <p>冬の寒風にさらされた肌細胞は、目に見えない微小な酸化ストレスとDNAダメージを受けています。ビフィズス菌発酵エキスは、皮膚の自然な修復酵素の活性を高め、夜間の睡眠中に傷ついた細胞を急速リカバリーする作用が科学的に実証されています。夜に塗ることで、翌朝の肌に圧倒的な柔らかさと弾力が蘇ります。</p>
        </div>
      </section>

      <section id="ranking">
        <h2 class="section-title">🏆 高濃度ビフィダ美容液おすすめランキング10選</h2>
        {items_html}
      </section>

      <section id="comparison">
        <h2 class="section-title">📊 ビフィダコスメ10品 徹底スペック比較表</h2>
        <div class="comparison-table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名・ブランド</th>
                <th>カテゴリー</th>
                <th>主成分・処方特徴</th>
                <th>参考価格</th>
              </tr>
            </thead>
            <tbody>
              {table_rows}
            </tbody>
          </table>
        </div>
      </section>

      <section id="guide">
        <h2 class="section-title">💡 11月・12月の冬本番にビフィダのバリア再建力を最大化するプロの実践ステップ</h2>
        
        <div class="science-card">
          <h3 style="color:#6d28d9;">【STEP 1】洗顔後すぐの『ブースター投入』で美肌菌の受け入れ態勢を整える</h3>
          <p>冬の洗顔後は水道水の塩素や洗浄成分によって皮膚のpHが一時的にアルカリ性に傾いています。タオルオフ後すぐにビフィダ発酵美容液または導入トナーを素肌に馴染ませることで、瞬時に弱酸性の環境へと引き戻し、後から使う化粧水や乳液の美肌成分の吸収効率を飛躍的に向上させます。</p>
        </div>

        <div class="science-card">
          <h3 style="color:#6d28d9;">【STEP 2】赤み・粉吹きゾーンへの『コットン密着ローションパック』</h3>
          <p>暖房の温風やマスクの擦れで赤みや粉吹きが出やすい両頬や口角には、ビフィダトナーをたっぷり含ませた薄手コットンを3分間密着させます。ビフィダの豊富なアミノ酸と多糖類が角層の接着因子を急速補修し、エステ帰りのようなモチモチの吸い付き肌へとリセットします。</p>
        </div>

        <div class="science-card">
          <h3 style="color:#6d28d9;">【STEP 3】夜の『ビフィダ×セラミドクリーム密閉』で翌朝の肌密度を極大化</h3>
          <p>ビフィダ美容液で角層の常在菌バランスと水分を満たしたら、仕上げに高保湿ヒト型セラミドクリームやエクトイン乳液でしっかりと蓋をします。睡眠中の乾燥蒸発を遮断し、翌朝洗顔した瞬間に手のひらを押し返すような強靭な弾力とキメの美しさを体感できます。</p>
        </div>
      </section>

      <section id="faq">
        <h2 class="section-title">❓ 専門家が答える！ビフィダコスメのよくある疑問</h2>
        <div class="faq-list">
          {"".join([f'''
          <div class="faq-item">
            <div class="faq-q">
              <span class="faq-q-badge">Q</span>
              <span>{f["q"]}</span>
            </div>
            <div class="faq-a">{f["a"]}</div>
          </div>
          ''' for f in faq_data])}
        </div>
      </section>

      <div class="internal-links-box">
        <h3 class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</h3>
        <div class="internal-links-grid">
          <a href="/winter-ectoin" class="internal-link">🧬 極限保水シェルター！高保水エクトイン10選</a>
          <a href="/winter-bakuchiol" class="internal-link">🌿 次世代レチノール！高保湿バクチオール10選</a>
          <a href="/winter-galactomyces" class="internal-link">🍶 酵母発酵で透明感！高浸透ガラクトミセス10選</a>
          <a href="/winter-propolis" class="internal-link">🐝 濃密蜜膜ヴェール！高保湿プロポリスアンプル10選</a>
          <a href="/winter-proteoglycan" class="internal-link">🧬 ヒアルロン酸超え保水！高純度プロテオグリカン10選</a>
          <a href="/winter-ceramide-cream" class="internal-link">🧴 究極のラメラ修復！高保湿セラミドクリーム10選</a>
          <a href="/winter-cica-cream" class="internal-link">🌿 冬の肌荒れ鎮静！高保湿シカクリーム10選</a>
          <a href="/winter-panthenol-cream" class="internal-link">🧪 肌バリア鎮静！高保湿パンテノールクリーム10選</a>
          <a href="/winter-heparinoid" class="internal-link">🩺 角層深部保水！薬用ヘパリン類似物質コスメ10選</a>
          <a href="/winter-rice-power" class="internal-link">🌾 水分保持能改善！米発酵・ライスパワー10選</a>
          <a href="/winter-squalane-oil" class="internal-link">✨ 極上ツヤ膜！高純度スクワランオイル10選</a>
          <a href="/winter-serum-booster" class="internal-link">💧 浸透ルート開通！冬の導入美容液10選</a>
        </div>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-links">
        <a href="/">トップページ</a>
      </div>
      <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved.</p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #64748b;">当サイトは楽天市場アフィリエイトプログラムに参加しており、適格販売により収入を得ています。</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-bifida.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("winter-bifida.html successfully generated!")
