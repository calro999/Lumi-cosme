import json
import re

with open("fetched_final_30_marula_birch_azelaic.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_birch_juice"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 韓国オリーブヤング殿堂入り！江原道インジェ産白樺樹液×ヒアルロン酸の水分爆弾",
        "catch": "精製水ゼロの極上保水体験。冬の室内暖房でカラカラに干からびた角層へ清潤な水分を行き渡らせる",
        "brand_name": "ROUND LAB (ラウンドラボ)",
        "capacity": "80ml (シラカバ水分クリーム)",
        "type": "高保水白樺樹液ジェルモイストクリーム",
        "features": "韓国江原道インジェ産白樺樹液高配合、ビタヒアルロン酸カプセル、グリセリルグルコシド（アクアポリン活性化）",
        "value": "オイルでフタをする前に水分を極限まで補給。ベタつきゼロなのに48時間みずみずしさが続く驚異の水分持続力",
        "desc_p1": "11月から12月にかけて、オフィスや自宅でエアコン暖房をつけ始めると、肌表面がパサつくだけでなく、肌の深部がギシギシと引きつるような『インナードライ』に多くの人が悩まされます。油分の多いリッチなクリームを重ねても、肝心の水分が不足していると肌はしぼんだまま。韓国オリーブヤングで長年アワードを独占し続けるROUND LABの『白樺水分クリーム』は、澄んだ高原地帯で育った白樺の樹液を贅沢に配合し、肌の奥深くへ澄み切った清潤な水分を送り込む殿堂入りの水分クリームです。",
        "desc_p2": "クリームの中に目に見える微細なビタヒアルロン酸カプセルが配合されており、肌に乗せて伸ばすとプチプチと心地よく弾けて角質層へ素早く浸透します。白樺樹液特有のアミノ酸やミネラルが細胞の水分保持ゲートであるアクアポリンを力強くサポート。油膜感で誤魔化すのではなく、内側から水分で満タンに満たされたような透明感あふれる『水光肌（ムルグァンピブ）』へと導きます。メイク前に塗ってもファンデーションが一切ヨレず、暖房直風の下でも夕方までぷるぷるの柔軟性が持続します。",
        "target": "暖房の部屋にいると肌の奥がつっぱるインナードライ肌の方、ベタつく油分クリームが苦手でみずみずしい保湿を求める方、夕方の毛穴落ちを防ぎたい方",
        "point": "朝晩の洗顔・化粧水・美容液の後、付属のスパチュラで適量を取り顔全体に滑らせます。乾燥が気になる夜は、2回重ね塗りして『水分スリーピングパック』として使うと、翌朝の肌の透明感と吸い付きが別次元に変わります。"
    },
    {
        "rank": 2,
        "tag": "🌿 白樺樹液70%超高配合！アクアキシル×パンテノールで水分バリアを鉄壁密閉",
        "catch": "水分が足りずにゆらぐ冬の乾燥肌へ。角層のすみずみまで澄んだ潤いを届ける高浸透ブースティング美容液",
        "brand_name": "Anua (アヌア)",
        "capacity": "30ml (シラカバ70 水分ブースティングセラム)",
        "type": "白樺樹液70%高濃度保水セラム",
        "features": "白樺樹液70%、アクアキシル、10重ヒアルロン酸、パンテノール、弱酸性低刺激処方",
        "value": "精製水の大半をミネラル豊富な白樺樹液に置き換えた贅沢仕様。乱れた角質水分サイクルを整えてうるおい循環を正常化",
        "desc_p1": "敏感肌ケアで不動の地位を築いたAnuaが、冬の深刻な脱水肌のために開発した『シラカバ70 水分ブースティングセラム』。一般的な美容液の主原料である精製水の代わりに、北海道や北欧に匹敵する冷涼地で採取された高純度白樺樹液を実に70%も濃縮配合しています。白樺樹液は分子が極めて小さいため、ゴワついた真冬の角質層にも抵抗なくすーっと吸い込まれていきます。",
        "desc_p2": "さらに水分蒸散を防ぐ特許成分アクアキシルと、分子量の異なる10種のマルチヒアルロン酸が連携。肌表面から角層深部まで段階的に水分を留まらせ、パンテノールが真冬の冷風や摩擦で荒れたバリア機能を穏やかに保護します。とろみがあるのに肌に乗せるとサラリとした水膜に変化する絶妙なテクスチャーで、塗った瞬間から肌の赤みや火照りがスッと落ち着き、キメが整ったなめらかな肌触りを実感できます。",
        "target": "冬になると乾燥でキメが乱れて肌がザラつく方、スキンケアを重ねてもすぐに乾いてしまう方、低刺激で穏やかに潤したい敏感肌の方",
        "point": "化粧水の後、スポイトで1〜2滴を両頬と額に落とし、指先で優しくピアノを弾くようにタッピング。目元や口元の乾燥小ジワが気になる部分には重ねづけが効果的です。"
    },
    {
        "rank": 3,
        "tag": "💧 濃縮白樺エッセンスの集中点滴！真冬の乾き切った細胞を救出する水分爆弾アンプル",
        "catch": "乾く隙を与えない密着ハイドレーション。高分子と低分子の白樺ヒアルロン酸が織りなす潤いヴェール",
        "brand_name": "ROUND LAB (ラウンドラボ)",
        "capacity": "50ml (シラカバ水分アンプル美容液)",
        "type": "高純度白樺樹液集中保水アンプル",
        "features": "インジェ産濃縮白樺樹液、グリセリルグルコシド、ヒアルロン酸コンプレックス、ノンコメドジェニックテスト済み",
        "value": "化粧水とクリームの間に挟むことで保水力を最大化。エアコンのドライな空気に一日中さらされても乾かない底力を育む",
        "desc_p1": "ROUND LABのシラカバラインの中でも、特に保水密度の高さに特化して設計された集中アンプル。11月後半から12月の過酷な寒冷環境では、湿度の低さに加えて室内の暖房によって肌内部の水分が強制的に蒸散させられます。このアンプルは、白樺樹液に含まれる豊富なアミノ酸とミネラルを高濃度で凝縮し、肌が自ら水分を抱え込む力を強力にバックアップします。",
        "desc_p2": "テクスチャーは濃厚で糸を引くようなリッチ感がありながら、肌に伸ばすと不思議なほど素早く馴染んでベタつきを一切残しません。角層の奥深くに水分を蓄える『水分タンク』を築き上げるため、暖房直風を浴び続けても夕方の肌がしぼまず、ふっくらとしたハリと弾力が一日中持続。乾燥による毛穴の開きやくすみが気になる大人の冬肌にも、透明感あふれるみずみずしい生命感を与えてくれます。",
        "target": "真冬のエアコン乾燥で午後になると顔がパリパリに突っ張る方、乾燥毛穴やハリ不足が気になる方、濃密な水分セラムを求める方",
        "point": "手のひらに2〜3滴取り、両手で軽く擦り合わせて温めてから顔全体を包み込むように密着させます。頬を手のひらで押し上げるようにハンドプレスするとリフト感も高まります。"
    },
    {
        "rank": 4,
        "tag": "🛡️ 白樺樹液×パンテノールの潤いシールド！水分蒸発を許さない高保湿ジェルクリーム",
        "catch": "水分補給とバリア保護を完璧に両立。乾燥で過敏になった冬肌を優しく鎮静しながらうるおいを密閉",
        "brand_name": "Anua (アヌア)",
        "capacity": "50ml (シラカバ70 水分ブースティングクリーム)",
        "type": "白樺樹液高配合水分バリアジェルクリーム",
        "features": "白樺樹液70%、高純度パンテノール、セラミドNP、アクアキシル、弱酸性処方",
        "value": "水分リッチな白樺樹液をパンテノールとセラミドのヴェールでしっかりラッピング。外気刺激をブロックしながら水分をキープ",
        "desc_p1": "水分をいくら補給しても、外気へと逃げてしまっては意味がありません。Anuaの『シラカバ70 水分ブースティングクリーム』は、白樺樹液による潤いチャージと、肌バリア修復成分として名高いパンテノール＆セラミドNPによるフタの役割を1つで完結させるよう精密に設計されたモイスチャークリームです。",
        "desc_p2": "なめらかで伸びの良いウォータージェルテクスチャーは、肌に乗せた瞬間に心地よい清涼感を与え、暖房の熱気で赤く火照った肌を穏やかにクールダウン。肌表面に薄く軽やかな水分シールドを形成し、冬の乾いた冷風やチリ・ホコリなどの外部刺激から角層をしっかりと隔離します。重たい油分クリームを使うと吹き出物ができやすい混合肌の方でも、毛穴を塞がずに快適な高保湿をキープできます。",
        "target": "Tゾーンはテカリやすいのに頬や口元がカサつく混合肌の方、暖房による火照りや赤みに悩む方、ベタつかない保護膜が欲しい方",
        "point": "スキンケアの仕上げに適量を顔全体に優しく塗り広げます。乾燥が厳しい日は、首元までしっかり伸ばしてデコルテの水分ケアも同時に行うのが美肌を保つ秘訣です。"
    },
    {
        "rank": 5,
        "tag": "☀️ 白樺エッセンス配合で乾かない！冬の紫外線と乾燥から肌を守る水分UVサンクリーム",
        "catch": "まるで美容液を塗っているような心地よさ。SPF50+ PA++++の強力防御と高保水を同時に実現",
        "brand_name": "ROUND LAB (ラウンドラボ)",
        "capacity": "50ml (シラカバ水分日焼け止め)",
        "type": "白樺樹液エッセンス配合高保湿水分サンクリーム",
        "features": "白樺樹液高配合、ヒアルロン酸、ナイアシンアミド、アデノシン、SPF50+ PA++++、白浮きゼロ処方",
        "value": "冬の紫外線UVAと暖房乾燥のダブルパンチを鉄壁ブロック。日中の乾燥による化粧崩れや粉吹きを根本から防ぐ",
        "desc_p1": "冬は夏に比べて紫外線量が減ると思われがちですが、肌の奥まで届いて真皮を破壊する紫外線UVAは11月・12月でも依然として強く降り注いでいます。さらに冬の紫外線対策を怠ると、乾燥によるバリア破壊と相まってシミやたるみが一気に加速します。ROUND LABのシラカバ水分サンクリームは、韓国コスメ界で『水分日焼け止め』という新ジャンルを確立した伝説的ベストセラーです。",
        "desc_p2": "日焼け止め特有のキシキシ感、白浮き、乾燥によるつっぱり感が一切なく、まるで高級な水分乳液を塗っているかのようなみずみずしい塗り心地。白樺樹液とヒアルロン酸が日中も角層に潤いを供給し続けるため、ファンデーションの下地として使うと、一日中乾燥崩れや粉吹きが起きないしっとりツヤ肌が完成します。石鹸や軽い洗顔料でオフできる肌への優しさも冬のデリケート肌に最適です。",
        "target": "冬の日焼け止めを使うと肌が乾燥してつっぱる方、白浮きせず透明感のあるツヤ下地を求める方、日常使いで肌に負担をかけたくない方",
        "point": "朝のスキンケアの最後に、パール粒2個分を顔全体にムラなく馴染ませます。耳の後ろや首筋、手の甲まで伸ばすことで、冬のうっかり日焼けと乾燥をトータルで防げます。"
    },
    {
        "rank": 6,
        "tag": "🧻 朝の3分集中水分チャージ！白樺樹液ひたひたの角質ケア＆高保水トナーパッド",
        "catch": "メイク前の時短レスキュー。拭き取りで不要な角質をオフしながら、白樺の清潤水分を急速チャージ",
        "brand_name": "Anua (アヌア)",
        "capacity": "70枚入 (シラカバ水分ブースティングパッド)",
        "type": "白樺樹液含浸デュアル水分トナーパッド",
        "features": "白樺樹液高配合エッセンスひたひた含浸、アクアキシル、エンボス面＆フラット面の2WAYパッド、弱酸性",
        "value": "忙しい冬の朝に洗顔代わりやメイク前部分パックとして大活躍。ファンデーションの密着度とノリを劇的に向上させる",
        "desc_p1": "11月・12月の朝は寒さで洗顔するのが億劫になりがちですが、就寝中の皮脂やホコリを放置すると化粧ノリが極端に悪化します。また、乾燥して硬くなった角質が剥がれ落ちずに表面に残っていると、どんな保湿剤も浸透しません。Anuaの『シラカバ水分ブースティングパッド』は、70枚のパッドに白樺樹液たっぷりの美容液が容器底まで溢れるほど浸透した贅沢なトナーパッドです。",
        "desc_p2": "凸凹のあるエンボス面で小鼻や顎の角質を優しく拭き取った後、なめらかなフラット面を両頬や額に貼り付けて3分間パック。白樺の天然ミネラルと水分が乾いた角層へ一気にチャージされ、朝の肌温度を心地よくクーリングしながらキメをキュッと引き締めます。パックを剥がした後の肌はぷるんとした弾力と透明感に満ち、その後のファンデーションが吸い付くように密着します。",
        "target": "朝のメイク前に肌がカサついてファンデが浮いてしまう方、冬の角質ゴワつきを優しくオフしたい方、手軽に集中保水したい方",
        "point": "乾燥が気になる両頬に1枚ずつ貼り、ドライヤーで髪を乾かす間の3分パックとして使用するのがおすすめ。ドライヤーの温風による肌乾燥を防ぎながら、メイク準備が完了します。"
    },
    {
        "rank": 7,
        "tag": "🫧 洗い上がりがつっぱらない奇跡の洗顔！白樺樹液ベースの弱酸性モイストクレンザー",
        "catch": "汚れだけを吸着し、肌の水分は1ミリも逃さない。冬の朝洗顔を至福のうるおいタイムに変える",
        "brand_name": "ROUND LAB (ラウンドラボ)",
        "capacity": "150ml (シラカバ水分クレンザー)",
        "type": "白樺樹液配合弱酸性高保湿洗顔フォーム",
        "features": "インジェ産白樺樹液、ヒアルロン酸、ココナッツ由来アミノ酸系洗浄成分、低刺激弱酸性ジェル処方",
        "value": "冬の乾燥を悪化させる最大の要因である『脱脂力の強すぎる洗顔』を根本解決。洗う前より潤うようなしっとり感",
        "desc_p1": "冬の乾燥肌の悪化原因の実に7割は、洗浄力の強すぎる洗顔料によって皮脂やNMF（天然保湿因子）が洗い流されてしまうことにあります。特に11月以降の肌はバリア機能が低下しており、アルカリ性の強いフォームで洗うと直後から激しいツッパリ感や粉吹きが生じます。ROUND LABのシラカバ水分クレンザーは、肌のpHバランスに近い弱酸性に保たれた高保湿ジェル洗顔料です。",
        "desc_p2": "白樺樹液とヒアルロン酸をベースに配合し、肌に必要な潤いをがっちり守りながら、酸化した皮脂や毛穴汚れだけを選択的に優しくオフ。手で泡立てるとキメ細やかで柔らかな濃密クッション泡が立ち、摩擦を一切起こさずに肌を包み込みます。ぬるま湯で洗い流した瞬間、まるで化粧水を塗った後のようなしっとり・もちもちとした吸い付き感に誰もが驚かされます。",
        "target": "洗顔後すぐに肌がつっぱって慌てて化粧水を塗っている方、冬になると洗顔時にピリつきを感じる敏感肌の方、朝洗顔で乾燥したくない方",
        "point": "ぬるま湯（32〜34℃程度）で顔を濡らした後、適量をしっかり泡立てて泡を転がすように洗います。熱いお湯は皮脂膜を溶かしてしまうため絶対に避け、ぬるま湯で優しくすすぎましょう。"
    },
    {
        "rank": 8,
        "tag": "🎭 乾いた肌へ白樺の恵みを一晩中閉じ込める！濃縮水分エッセンス密着シートマスク",
        "catch": "週末の贅沢ご褒美ケア。密着ヴィーガンシートが白樺樹液の濃密ミネラルを角層の奥深くへプレス",
        "brand_name": "Anua (アヌア)",
        "capacity": "10枚入 (シラカバ モイスチャーマスクパック)",
        "type": "高保水白樺樹液密着シートマスク",
        "features": "白樺樹液濃縮エッセンス25ml贅沢含浸、生分解性ヴィーガン認証シート、10重ヒアルロン酸、弱酸性",
        "value": "1枚に美容液ほぼ丸ごと1本分の白樺樹液を濃縮。暖房直風で干からびた週末のレスキューケアに最適",
        "desc_p1": "平日の過酷なオフィス暖房や長時間の外出で限界を迎えた肌を、週末に一気にリセットするためのスペシャルケアマスク。Anuaの『シラカバ モイスチャーマスクパック』は、薄手でありながら驚異的な保水力を誇る植物由来の生分解性ヴィーガンシートを採用し、顔のあらゆる凹凸に吸い付くようにピタッと密着します。",
        "desc_p2": "シートには25mlもの白樺樹液濃縮美容液がひたひたに含まれており、貼っている間中ずっと肌細胞へミネラルと水分を点滴のように注入し続けます。15分後、マスクを剥がした瞬間に現れるのは、まるで温泉から上がったばかりのようなみずみずしい透明感とふっくらとしたハリ。乾燥による小ジワやくすみが一掃され、翌朝のメイク乗りが劇的に改善します。",
        "target": "特別な日の前夜に即効で肌コンディションを引き上げたい方、週末に集中的な水分チャージを行いたい方、密着力の高いパックを好む方",
        "point": "化粧水で肌を整えた後に密着させ、15分ほど置きます。剥がした後は肌表面に残ったエッセンスを手で優しくハンドプレスし、最後にクリームで水分を密閉するのが鉄則です。"
    },
    {
        "rank": 9,
        "tag": "🌲 白樺の恵みを原点から体感！天然白樺樹液を惜しみなく配合した極上の濃密化粧水",
        "catch": "北欧の大自然の生命力をそのまま肌へ。肌本来の保水リズムを呼び覚ます至高のミネラルトナー",
        "brand_name": "KOIVE (コイヴ)",
        "capacity": "150ml (モイスチャライジングトナー)",
        "type": "天然白樺樹液ベース高保湿化粧水",
        "features": "天然白樺樹液（バーチサップ）ベース処方、白樺樹皮エキス、スズランエキス、無香料・無着色・アルコールフリー",
        "value": "精製水で薄めず、白樺樹液そのものの高い栄養価を凝縮。肌の角質層を自然の生命力で満たすワンランク上のスキンケア",
        "desc_p1": "白樺樹液のスキンケア効果を極限まで追求する専門ブランド『KOIVE（コイヴ）』。白樺の木が春先の雪解け時期に、芽吹くためのエネルギーとして大地から吸い上げるわずか数週間しか採取できない希少な天然白樺樹液を主成分として贅沢に使用しています。",
        "desc_p2": "精製水とは明らかに異なる、まろやかでとろみのあるテクスチャーが特徴。白樺樹液に含まれる天然のフルクトースやアミノ酸、キシリトールが肌の水分を強力に引き寄せ、乾燥してスカスカになった角層のすき間を濃密に埋め戻します。肌にスッと吸い込まれた後は、表面はサラリとしているのに内側がモチモチと跳ね返すような豊かな潤い感を長時間実感できます。",
        "target": "原料そのものの質にこだわりたい本物志向の方、自然由来の成分で確かな高保湿を実感したい方、冬の乾燥くすみを根本から晴らしたい方",
        "point": "手のひらに500円玉大を取り、顔全体を包み込むようにハンドプレス。一度肌に入り切った後、もう一度少量を重ねづけする『2度塗り』を行うと、潤いの持続時間が劇的に伸びます。"
    },
    {
        "rank": 10,
        "tag": "🥛 300ml大容量で惜しみなく水分補給！白樺樹液×ヒアルロン酸のデイリー弱酸性トナー",
        "catch": "肌がごくごく飲み干す水分補給。コットンパックや全身のインナードライ対策にも最適な万能化粧水",
        "brand_name": "ROUND LAB (ラウンドラボ)",
        "capacity": "300ml (シラカバ水分トナー)",
        "type": "大容量弱酸性白樺水分トナー",
        "features": "インジェ産白樺樹液、ビタヒアルロン酸、パンテノール、弱酸性処方、300mlビッグボトル",
        "value": "300mlの大容量で毎日惜しみなく水分チャージ。何層も重ねづけすることで冬の角層水分量を極限まで引き上げる",
        "desc_p1": "冬のスキンケアで最も重要なのは『惜しみなく十分な量の水分を角層に届けること』です。高価な化粧水を少量ケチって使っていては、真冬の強烈な乾燥には太刀打ちできません。ROUND LABのシラカバ水分トナーは、300mlという大容量ボトルに白樺樹液の豊かな保水力をたっぷり詰め込んだ実力派デイリートナーです。",
        "desc_p2": "水のようにサラッとしたテクスチャーでありながら、肌に馴染ませるとグングン浸透し、重ねるごとに肌が柔らかく解きほぐされていくのを実感できます。コットンをひたひたにして乾燥が気になる部分に貼る『ローションパック』や、スプレー容器に詰め替えて日中の暖房乾燥対策ミストとして使うのにも最適。家族みんなで真冬の水分補給を徹底できる頼もしい1本です。",
        "target": "化粧水をたっぷり重ねづけして角層を満タンにしたい方、大容量でコスパの高い高保湿トナーを探している方、コットンパックを習慣にしたい方",
        "point": "手で一度全体に馴染ませた後、コットンにたっぷり含ませて優しくパッティング。乾燥しやすい目元や口元には、薄く裂いたコットンで5分間集中ローションパックを行うのが効果的です。"
    }
]

faq_data = [
    {
        "q": "白樺樹液（バーチウォーター）とはどのような成分ですか？精製水を使った化粧水と何が違うのですか？",
        "a": "白樺樹液は、北欧や北海道、韓国などの寒冷地で白樺の木が春先に芽吹くために、大地から吸い上げる天然の樹液です。採取できるのは雪解けのわずか数週間に限られる希少な素材です。一般的な化粧水の基剤である『精製水』はミネラル等の栄養素を含まない純水ですが、白樺樹液にはカルシウム・マグネシウム・カリウムなどの天然ミネラル、グルタミン酸やアミノ酸、キシリトール、果糖（フルクトース）が極めて豊富に溶け込んでいます。水分子のクラスター（集まり）が非常に細かいため、肌の細胞間脂質の隙間に驚くほどスムーズに浸透し、肌内部で水分子を強力に抱え込む力（天然の保水力）に優れています。"
    },
    {
        "q": "白樺樹液コスメは11月・12月の真冬のスキンケアでどの肌質に最も向いていますか？",
        "a": "特に『インナードライ肌（肌の内部は突っ張るのに表面は皮脂でテカる肌）』や『暖房の効いた室内で赤み・火照りが出やすい乾燥敏感肌』に最も適しています。冬場に油分の多いリッチなクリームを塗っても乾燥が改善しない場合、角層の水分そのものが圧倒的に不足しています。白樺樹液コスメは油分による重さや毛穴詰まりを起こさずに、角層深部へ澄んだ水分を大量に供給できるため、混合肌やオイリー肌の乾燥対策としても抜群の相性を誇ります。"
    },
    {
        "q": "白樺（シラカバ）花粉症のアレルギーがある人でも白樺樹液コスメは安全に使えますか？",
        "a": "一般的に化粧品に使用される白樺樹液（バーチサップ）やエキスは、花粉そのものではなく樹幹から採取した樹液を高度に濾過・精製したものです。花粉アレルゲンタンパク質とは異なるため、花粉症の方でも問題なく使用できるケースがほとんどです。ただし、重度のシラカバ花粉アレルギーや口腔アレルギー症候群（リンゴやモモなどでアレルギーが出る方）をお持ちの場合は、念のため使用前に腕の内側などで簡易的なパッチテストを行うことをおすすめします。"
    },
    {
        "q": "白樺樹液コスメとマルラオイルやセラミドクリームを一緒に使う場合の正しい順番は？",
        "a": "『水分を先に補給し、油分でフタをする』のがスキンケアの基本鉄則です。洗顔後、まず白樺樹液トナーやセラムで角層深部まで水分をしっかりと満たし（インナードライ解消）、その後にセラミドクリームやマルラオイルを薄く重ねて水分蒸発を密閉します。また、マルラオイルをブースターとして使う場合は、洗顔直後にオイルを1滴馴染ませて角質を柔らかくほぐしてから白樺樹液トナーを重ねると、水分がスポンジのように驚くほど深く引き込まれる相乗効果が得られます。"
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
            "headline": "保湿力の強さで肌乾燥とさようなら！天然ミネラルの潤い巡る白樺樹液で乾かない水光肌へ導く高保水バーチコスメランク10",
            "description": "11月・12月の冬本番に！天然ミネラルとアミノ酸に満ちた白樺樹液（バーチウォーター）でインナードライを解消する高保水コスメ10選を徹底比較！ROUND LAB、Anua、KOIVEなど厳選。",
            "datePublished": "2026-11-03T18:00:00+09:00",
            "dateModified": "2026-11-03T18:00:00+09:00",
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
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": "https://lumi-cosme.vercel.app/winter-birch-juice"
            }
        },
        {
            "@type": "ItemList",
            "name": "真冬の高保水白樺樹液コスメおすすめランキング10選",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": idx + 1,
                    "item": prod
                }
                for idx, prod in enumerate(jsonld_products)
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
                    "name": "高保水白樺樹液コスメ",
                    "item": "https://lumi-cosme.vercel.app/winter-birch-juice"
                }
            ]
        }
    ]
}

faq_html = ""
for f in faq_data:
    faq_html += f"""
      <div class="faq-item">
        <dt class="faq-question">
          <span class="faq-q-badge">Q</span>
          <span>{f['q']}</span>
        </dt>
        <dd class="faq-answer">
          <span class="faq-a-badge">A</span>
          <p>{f['a']}</p>
        </dd>
      </div>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！天然ミネラルの潤い巡る白樺樹液で乾かない水光肌へ導く高保水バーチコスメランク10</title>
  <meta name="description" content="11月・12月の冬本番に！天然ミネラルとアミノ酸に満ちた白樺樹液（バーチウォーター）でインナードライを解消する高保水コスメ10選を徹底比較！ROUND LAB、Anua、KOIVEなど厳選。">
  <meta name="keywords" content="白樺樹液, シラカバ コスメ, バーチウォーター, 水分クリーム, 冬 保湿, ROUND LAB, Anua, インナードライ">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-birch-juice">
  
  <!-- OGP -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！天然ミネラルの潤い巡る白樺樹液で乾かない水光肌へ導く高保水バーチコスメランク10">
  <meta property="og:description" content="11月・12月の冬本番に！天然ミネラルとアミノ酸に満ちた白樺樹液（バーチウォーター）でインナードライを解消する高保水コスメ10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-birch-juice">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta name="twitter:card" content="summary_large_image">
  
  <script type="application/ld+json">
{json.dumps(full_jsonld, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary-color: #0f766e;
      --primary-light: #f0fdfa;
      --accent-color: #0d9488;
      --accent-hover: #115e59;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --bg-main: #f8fafc;
      --card-bg: #ffffff;
      --border-color: #ccfbf1;
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.04);
      --shadow-md: 0 4px 12px rgba(15,118,110,0.08);
      --shadow-lg: 0 8px 24px rgba(15,118,110,0.12);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif;
      line-height: 1.8;
      color: var(--text-main);
      background-color: var(--bg-main);
    }}

    .container {{
      max-width: 920px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* ヘッダー */
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      padding: 16px 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .site-nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-color);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 20px;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--accent-color);
    }}

    /* パンくずリスト */
    .breadcrumb {{
      display: flex;
      list-style: none;
      padding: 14px 0;
      font-size: 0.85rem;
      color: var(--text-muted);
      overflow-x: auto;
      white-space: nowrap;
    }}
    .breadcrumb li+li:before {{
      content: "›";
      padding: 0 8px;
      color: #cbd5e1;
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumb a:hover {{
      color: var(--accent-color);
    }}

    /* 記事メイン */
    article {{
      background: var(--card-bg);
      border-radius: var(--radius-lg);
      padding: 40px;
      margin: 20px 0 40px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    @media (max-width: 640px) {{
      article {{ padding: 20px; }}
    }}

    .article-header {{
      margin-bottom: 36px;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 24px;
    }}
    .season-badge {{
      display: inline-block;
      background: #ccfbf1;
      color: #0f766e;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 12px;
    }}
    h1.article-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.45;
      color: #0f172a;
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }}
    @media (max-width: 640px) {{
      h1.article-title {{ font-size: 1.45rem; }}
    }}
    .meta-info {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    /* リード文 */
    .lead-box {{
      background: var(--primary-light);
      border-left: 4px solid var(--primary-color);
      padding: 24px;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      margin-bottom: 36px;
      font-size: 1.02rem;
      line-height: 1.85;
      color: #334155;
    }}
    .lead-box p+p {{ margin-top: 14px; }}

    /* 目次 */
    .toc-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-md);
      padding: 24px;
      margin-bottom: 44px;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--primary-color);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      padding-left: 0;
    }}
    .toc-list li {{
      margin-bottom: 8px;
      font-size: 0.95rem;
    }}
    .toc-list a {{
      color: #475569;
      text-decoration: none;
      display: inline-block;
      transition: color 0.15s;
    }}
    .toc-list a:hover {{
      color: var(--accent-color);
      text-decoration: underline;
    }}

    /* 見出し */
    h2.section-heading {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #0f172a;
      margin: 48px 0 24px;
      padding-left: 14px;
      border-left: 5px solid var(--accent-color);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    h3.sub-heading {{
      font-size: 1.2rem;
      font-weight: 700;
      color: #1e293b;
      margin: 28px 0 16px;
    }}

    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 28px;
      margin-bottom: 40px;
      box-shadow: var(--shadow-sm);
      transition: box-shadow 0.25s, transform 0.25s;
    }}
    .product-card:hover {{
      box-shadow: var(--shadow-md);
    }}
    .product-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, #0f766e, #0d9488);
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 4px 14px;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(15,118,110,0.3);
    }}
    #rank-1 .rank-badge {{
      background: linear-gradient(135deg, #0d9488, #14b8a6);
      font-size: 1.05rem;
      padding: 6px 18px;
    }}
    .product-tag {{
      background: #f0fdfa;
      color: #0f766e;
      border: 1px solid #99f6e4;
      font-size: 0.85rem;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 6px;
    }}
    h3.product-name {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 8px;
      line-height: 1.45;
    }}
    .product-catch {{
      color: #0f766e;
      font-weight: 600;
      font-size: 0.95rem;
      margin-bottom: 20px;
    }}

    .product-content-grid {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }}
    @media (max-width: 680px) {{
      .product-content-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-img-wrap {{
      text-align: center;
      background: #f8fafc;
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #f1f5f9;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      object-fit: contain;
      border-radius: var(--radius-sm);
    }}

    .price-box {{
      background: #f0fdfa;
      border: 1px solid #ccfbf1;
      border-radius: var(--radius-sm);
      padding: 12px 16px;
      margin-bottom: 16px;
      display: flex;
      align-items: baseline;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .price-label {{
      font-size: 0.85rem;
      color: #134e4a;
      font-weight: 600;
    }}
    .price-value {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #0f766e;
    }}
    .price-tax {{
      font-size: 0.75rem;
      color: #115e59;
    }}

    .product-specs {{
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 8px 16px;
      font-size: 0.88rem;
      background: #f8fafc;
      padding: 14px;
      border-radius: var(--radius-sm);
    }}
    .product-specs dt {{
      font-weight: 700;
      color: #64748b;
      white-space: nowrap;
    }}
    .product-specs dd {{
      color: #334155;
    }}

    .product-desc-box {{
      background: #f8fafc;
      border-radius: var(--radius-md);
      padding: 20px;
      margin-bottom: 20px;
      border: 1px solid #f1f5f9;
    }}
    .desc-heading {{
      font-size: 1rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 12px;
    }}
    .desc-p {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
      margin-bottom: 12px;
    }}
    .desc-p:last-child {{ margin-bottom: 0; }}

    .target-point-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-top: 16px;
      padding-top: 16px;
      border-top: 1px dashed #cbd5e1;
    }}
    @media (max-width: 600px) {{
      .target-point-grid {{ grid-template-columns: 1fr; }}
    }}
    .target-box, .point-box {{
      background: #ffffff;
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid #e2e8f0;
      font-size: 0.88rem;
    }}
    .target-box strong, .point-box strong {{
      display: block;
      color: #0f172a;
      margin-bottom: 4px;
      font-size: 0.88rem;
    }}
    .target-box p, .point-box p {{
      color: #475569;
      line-height: 1.6;
    }}

    .product-action-wrap {{
      text-align: center;
      margin-top: 20px;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: linear-gradient(135deg, #bf0000, #dc2626);
      color: #ffffff;
      font-size: 1.05rem;
      font-weight: 700;
      padding: 14px 28px;
      border-radius: var(--radius-md);
      text-decoration: none;
      box-shadow: 0 4px 12px rgba(191,0,0,0.25);
      transition: transform 0.15s, box-shadow 0.15s, background 0.15s;
      width: 100%;
      max-width: 440px;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000, #b91c1c);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191,0,0,0.35);
    }}

    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 30px 0 40px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      background: #ffffff;
      font-size: 0.9rem;
      text-align: left;
    }}
    .compare-table th {{
      background: var(--primary-light);
      color: var(--primary-color);
      font-weight: 700;
      padding: 14px 16px;
      border-bottom: 2px solid var(--border-color);
      white-space: nowrap;
    }}
    .compare-table td {{
      padding: 14px 16px;
      border-bottom: 1px solid #f1f5f9;
      color: #334155;
    }}
    .compare-table tr:hover {{
      background: #f8fafc;
    }}
    .compare-table .rank-cell {{
      font-weight: 700;
      color: var(--accent-color);
      white-space: nowrap;
    }}
    .compare-table .price-cell {{
      font-weight: 700;
      color: #0f766e;
      white-space: nowrap;
    }}

    /* Q&A */
    .faq-list {{
      margin: 24px 0 40px;
    }}
    .faq-item {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      margin-bottom: 16px;
      overflow: hidden;
    }}
    .faq-question {{
      background: #f8fafc;
      padding: 16px 20px;
      font-weight: 700;
      font-size: 1rem;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 1px solid #f1f5f9;
    }}
    .faq-q-badge {{
      background: var(--primary-color);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .faq-answer {{
      padding: 18px 20px;
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
      display: flex;
      gap: 12px;
    }}
    .faq-a-badge {{
      background: var(--accent-color);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
    }}

    /* 内部リンクカード */
    .related-articles {{
      margin: 40px 0 20px;
      padding: 24px;
      background: #f8fafc;
      border-radius: var(--radius-md);
      border: 1px solid #e2e8f0;
    }}
    .related-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 16px;
    }}
    .related-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-sm);
      padding: 14px;
      text-decoration: none;
      color: #1e293b;
      transition: border-color 0.2s, box-shadow 0.2s;
      display: block;
    }}
    .related-card:hover {{
      border-color: var(--accent-color);
      box-shadow: var(--shadow-sm);
    }}
    .related-card-title {{
      font-size: 0.92rem;
      font-weight: 700;
      line-height: 1.45;
      margin-bottom: 6px;
      color: #0f172a;
    }}
    .related-card-desc {{
      font-size: 0.8rem;
      color: #64748b;
      line-height: 1.5;
    }}

    /* フッター */
    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 48px 0 32px;
      margin-top: 60px;
      font-size: 0.88rem;
    }}
    .footer-content {{
      display: grid;
      grid-template-columns: 1fr 2fr;
      gap: 32px;
      margin-bottom: 32px;
    }}
    @media (max-width: 768px) {{
      .footer-content {{ grid-template-columns: 1fr; }}
    }}
    .footer-brand h4 {{
      color: #ffffff;
      font-size: 1.1rem;
      margin-bottom: 12px;
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 12px;
    }}
    .footer-links-grid a {{
      color: #cbd5e1;
      text-decoration: none;
      transition: color 0.15s;
    }}
    .footer-links-grid a:hover {{
      color: #2dd4bf;
    }}
    .copyright {{
      text-align: center;
      padding-top: 24px;
      border-top: 1px solid #1e293b;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <!-- ヘッダー -->
  <header>
    <div class="container site-nav">
      <a href="/" class="site-logo">
        <span>❄️</span>
        <span>冬コスメ徹底比較ラボ</span>
      </a>
      <nav class="nav-links">
        <a href="/">ホーム</a>
        <a href="/#ranking">最新ランキング</a>
        <a href="/#ingredients">成分別ガイド</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <!-- パンくずリスト -->
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li><a href="/">ホーム</a></li>
        <li aria-current="page">高保水白樺樹液コスメ</li>
      </ol>
    </nav>

    <article>
      <div class="article-header">
        <span class="season-badge">2026-2027 冬の厳選高保湿コスメ</span>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！天然ミネラルの潤い巡る白樺樹液で乾かない水光肌へ導く高保水バーチコスメランク10</h1>
        <div class="meta-info">
          <span>📅 公開: 2026年11月3日</span>
          <span>✍️ 監修: 冬コスメ徹底比較ラボ 美容解析チーム</span>
          <span>⏱️ 読了目安: 約8分</span>
        </div>
      </div>

      <!-- リード文 -->
      <div class="lead-box">
        <p>11月・12月の冬本番、室内で暖房エアコンが稼働し始めると急増するのが『クリームを重ね塗りしているのに肌の奥が引きつる』『表面はテカるのに内側がスカスカに乾く』という<strong>インナードライ（隠れ乾燥）</strong>の深刻な肌悩みです。角層細胞自体の水分が干からびている状態で油分ばかりを与えても、肌内部の渇きは決して癒されず、乾燥小ジワやキメの乱れ、大人ニキビが頻発してしまいます。</p>
        <p>そこでいま、韓国スキンケア界や日本の美容皮膚科領域で熱烈な支持を集めているのが、精製水の代わりに天然の<strong>『白樺樹液（バーチウォーター）』</strong>を主原料に据えた高保水コスメです。雪解けのわずか数週間、白樺が芽吹くための爆発的なエネルギーを宿した樹液には、天然ミネラル、アミノ酸、フルクトースが濃密に凝縮。水分子クラスターが極めて微細なため、砂漠化した角層深部へすーっと浸透し、肌のアクアポリン（水分チャンネル）を活性化させて内側から押し返すような水光ツヤ肌を叶えます。</p>
        <p>本稿では、楽天市場で現在入手可能な最新の白樺樹液コスメから、オリーブヤング殿堂入りの水分クリーム、白樺70%超高配合の濃縮アンプル、朝の時短を叶えるトナーパッドまでを厳選。保水持続力・角層浸透度・ベタつきのなさを徹底比較し、本当におすすめできる名品10選をランキング形式で詳しくレビューします。</p>
      </div>

      <!-- 目次 -->
      <div class="toc-box">
        <div class="toc-title">📑 目次（タップで各項目へジャンプ）</div>
        <ul class="toc-list">
          <li><a href="#why-birch">1. なぜ真冬のインナードライに「白樺樹液」がこれほど効くのか？</a></li>
          <li><a href="#compare-table">2. 高保水白樺樹液コスメおすすめ人気比較一覧表</a></li>
          <li><a href="#rank-1">3. 【第1位〜第10位】白樺樹液コスメ徹底レビュー＆真冬の検証結果</a></li>
          <li><a href="#how-to-choose">4. 失敗しない冬の白樺樹液コスメの選び方3つの鉄則</a></li>
          <li><a href="#faq-section">5. 白樺樹液コスメに関するよくある疑問とプロの回答（Q&A）</a></li>
        </ul>
      </div>

      <!-- 解説セクション1 -->
      <section id="why-birch">
        <h2 class="section-heading">なぜ真冬のインナードライに「白樺樹液」がこれほど効くのか？</h2>
        <p class="desc-p">多くの人が誤解していますが、冬の肌乾燥は『油分不足』だけでなく、それ以上に深刻な『角層の水分枯渇』によって引き起こされます。11月から12月にかけて東京や主要都市の外気湿度は30%台まで急落し、室内のエアコン暖房が肌細胞から猛烈な勢いで水分を吸い上げます。水分を失った肌は、自らを守ろうとして過剰な皮脂を分泌し、結果として『Tゾーンはテカリ、頬や口元はカピカピ』というアンバランスなインナードライ状態に陥ります。</p>
        <p class="desc_p">一般的な化粧水の主成分は、何の栄養素も持たない『精製水』が約80〜90%を占めています。しかし白樺樹液（バーチウォーター）は、カルシウム、カリウム、マグネシウムなどの生体親和性ミネラルや、グルタミン酸、アスパラギン酸などのアミノ酸、そして水分子を抱え込む天然キシリトールが自然の比率で溶け込んだ『生きた保水液』です。</p>
        <p class="desc_p">白樺樹液の水分子集団（クラスター）は一般的な純水よりも格段に小さく、角層細胞の膜をすり抜けるように深部へ浸透。さらに細胞膜に存在する水分の通り道『アクアポリン（AQP3）』の働きを刺激し、補給した潤いを肌全体へ巡らせます。表面にベタつく油膜を残すことなく、角層の隙間という隙間を純度の高い水分で満タンに満たすことこそが、白樺樹液の圧倒的な強みなのです。</p>
      </section>

      <!-- 比較表 -->
      <section id="compare-table">
        <h2 class="section-heading">高保水白樺樹液コスメおすすめ人気比較一覧表</h2>
        <p class="desc-p">楽天市場で絶大な人気を誇る実力派白樺樹液コスメ10選の価格・容量・処方特徴を一目で比較できます。</p>
        <div class="table-container">
          <table class="compare-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>タイプ / 容量</th>
                <th>主要成分・処方特徴</th>
                <th>参考価格(税込)</th>
              </tr>
            </thead>
            <tbody>
              {table_rows}
            </tbody>
          </table>
        </div>
      </section>

      <!-- ランキングメイン -->
      <section id="ranking-list">
        <h2 class="section-heading">【第1位〜第10位】高保水白樺樹液コスメ徹底レビュー＆真冬の検証結果</h2>
        <p class="desc-p">楽天市場で流通している最新ロットをもとに、真冬の保水アプローチやテクスチャー、効果的な使用法まで詳細にレビューします。</p>
        
        {items_html}
      </section>

      <!-- 選び方セクション -->
      <section id="how-to-choose">
        <h2 class="section-heading">失敗しない冬の白樺樹液コスメの選び方3つの鉄則</h2>
        <p class="desc-p">白樺樹液の恩恵を100%引き出すためには、製品の配合比率やアイテムカテゴリ（クリーム、セラム、パッド）を用途に応じて選ぶことが肝心です。</p>

        <h3 class="sub-heading">① 白樺樹液が成分表示の上位に記載されているか確認する</h3>
        <p class="desc-p">化粧品の成分表示は配合量の多い順に記載されるルールがあります。全成分の最初に『精製水』ではなく『シラカバ樹液』が記載されているもの、または『シラカバ樹液70%』など高配合が明記された製品を選ぶことで、ミネラルやアミノ酸の濃厚な保水効果をダイレクトに享受できます。</p>

        <h3 class="sub-heading">② ヒアルロン酸やパンテノールとの「シナジー配合」を狙う</h3>
        <p class="desc-p">白樺樹液単体でも優れた保水力を持ちますが、冬の厳しい乾燥環境では、分子量の異なるマルチヒアルロン酸や、バリア機能を立て直すパンテノール（プロビタミンB5）が組み合わされた処方が最強です。白樺樹液が引き込んだ水分をヒアルロン酸ががっちりホールドし、パンテノールが冷風の刺激から肌を守る盤石の体制が整います。</p>

        <h3 class="sub-heading">③ 朝のメイク前用と夜の集中ケア用でテクスチャーを使い分ける</h3>
        <p class="desc-p">朝はメイク崩れやモロモロを防ぐため、肌なじみの速いウォータージェルクリームやトナーパッドが最適です。一方、就寝中のエアコン暖房で水分が奪われやすい夜は、濃厚なアンプルセラムをたっぷり仕込んだ後に水分クリームを2度塗りする『水分パックケア』を取り入れることで、翌朝の洗顔時の肌のふっくら感が劇的に向上します。</p>
      </section>

      <!-- FAQセクション -->
      <section id="faq-section">
        <h2 class="section-heading">白樺樹液コスメに関するよくある疑問とプロの回答（Q&A）</h2>
        <div class="faq-list">
          {faq_html}
        </div>
      </section>

      <!-- 内部リンク関連記事 -->
      <section class="related-articles">
        <h3 class="related-title">❄️ あわせて読みたい！冬の高保湿スキンケア特集</h3>
        <div class="related-grid" id="related-grid-box">
          <!-- 自動更新スクリプトにより最新リンクが挿入されます -->
        </div>
      </section>
    </article>
  </main>

  <!-- フッター -->
  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-brand">
          <h4>冬コスメ徹底比較ラボ</h4>
          <p>乾燥が深刻化する11月・12月の冬期に特化し、科学的根拠に基づいた高保湿成分や楽天市場の人気コスメを徹底検証・レビューする専門メディアです。</p>
        </div>
        <div>
          <h4 style="color:#ffffff; margin-bottom:12px;">注目の高保湿テーマ</h4>
          <div class="footer-links-grid" id="footer-links-box">
            <!-- 自動更新スクリプトにより最新リンクが挿入されます -->
          </div>
        </div>
      </div>
      <div class="copyright">
        <p>&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved.</p>
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-birch-juice.html", "w", encoding="utf-8") as f:
    f.write(full_html.strip())

print("winter-birch-juice.html generated successfully!")
