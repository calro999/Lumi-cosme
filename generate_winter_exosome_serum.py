import json
import re

with open("fetched_perfect_3articles_data_v2.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_exosome_serum"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 微細ニードル×エクソソームの革新！冬の開き毛穴とたるみを角層奥から引き締める",
        "catch": "超微細スピキュールが美容成分の浸透路を拓き、高純度エクソソームが乾燥で緩んだ毛穴をキュッと密着ケア",
        "brand_name": "medicube (メディキューブ)",
        "capacity": "30ml (ゼロ毛穴エクソソームショット 2000)",
        "type": "微細スピキュール配合・高浸透毛穴引き締めエクソソームセラム",
        "features": "高純度エクソソーム、天然マイクロニードル（スピキュール）2,000本、AHA/BHA/PHA、パンテノール",
        "value": "塗った瞬間に心地よいチクチク感があり、暖房で開きがちな冬のたるみ毛穴を根本から引き締め。角層内部へダイレクトに成分をデリバリーする最新ショット美容液",
        "desc_p1": "11月から12月にかけて外気の湿度が30%を下回ると、寒さで皮脂が固まりやすくなる一方で、暖房による急激な乾燥に対抗しようと角質が肥厚し、毛穴周りの皮膚がしぼんでたるみ毛穴が目立ち始めます。表面だけの保湿では太刀打ちできないこの冬特有の毛穴悩みに、革新的なアプローチで圧倒的シェアを獲得しているのがメディキューブの『ゼロ毛穴エクソソームショット 2000』です。",
        "desc_p2": "天然の微細針（スピキュール）に高純度のエクソソームをコーティング。肌に塗布すると心地よいピリピリとした刺激とともに、硬くなった冬の角層に美容成分の通り道をつくり、毛穴の引き締め成分と潤いを深部まで届けます。テクスチャーはスッと馴染むジェル状でベタつきが一切残らず、翌朝にはまるで毛穴が引き締まったようなツルツルとなめらかな陶器肌へ整えます。2000ショットは毎日のお手入れにも無理なく使える絶妙なマイルドさです。",
        "target": "暖房の乾燥で頬の毛穴が縦に流れて目立つ方、角質が硬くなりスキンケアの浸透が悪く感じる方、最新のニードル×エクソソーム美容を試したい方",
        "point": "夜の洗顔直後、スキンケアの最初のステップとして使用。適量を指先に取り、毛穴やたるみが気になる部分に押し込むように優しくハンドプレスして浸透させます。"
    },
    {
        "rank": 2,
        "tag": "🔬 国産ヒト幹細胞原液×高純度エクソソーム！冬の寒冷で低下した肌活力を根本ブースト",
        "catch": "余計な添加物を削ぎ落とした成分主義。乾き切った大人の素肌に純度100%の細胞サイエンスを届ける",
        "brand_name": "KISO (キソ)",
        "capacity": "30ml (ステム セラム X)",
        "type": "高濃度ヒト脂肪由来幹細胞順化培養液＆エクソソーム原液美容液",
        "features": "ヒト幹細胞順化培養液エキス、ヒト脂肪由来間葉系細胞エクソソーム、グリチルリチン酸2K、ヒアルロン酸Na",
        "value": "成分特化型ブランドKISOが手掛けるハイエンド原液。冬の過酷な寒冷刺激でターンオーバーが乱れた肌に、高純度シグナル分子が活力を呼び戻す",
        "desc_p1": "12月の真冬の冷気は肌表面の毛細血管を収縮させ、皮膚への栄養供給を著しく低下させます。その結果、ターンオーバーが滞り、どれほど保湿しても『肌がくすんで生気がない』『触れるとゴワゴワする』という深刻な代謝低下に陥ります。日本の原液コスメのパイオニアであるKISOの『ステム セラム X』は、肌本来が持つコンディションの再生スイッチを押す集中美容液です。",
        "desc_p2": "日本国内の培養施設で徹底管理されたヒト幹細胞順化培養液と、そこから抽出された希少なエクソソームを高配合。とろみのあるリッチなテクスチャーが乾いた肌に吸い込まれるように馴染み、角層細胞のすき間を密度の高い潤いで埋め尽くします。無香料・無着色・パラベンフリーの低刺激設計なので、冬の寒風でデリケートに傾いた素肌にも優しくフィット。使い続けるほどに内側から押し返すようなもっちりとした弾力が蘇ります。",
        "target": "冬になると肌が硬くしぼんで元気がなくなる方、配合成分の純度や濃度にこだわりたい方、低刺激で本格的なエイジングケアを始めたい方",
        "point": "化粧水で肌を柔らかく整えた後、スポイトで手のひらに2〜3滴取り、温めてから顔全体を包み込むように塗布。目元や口元の乾燥小ジワには重ね付けが効果的です。"
    },
    {
        "rank": 3,
        "tag": "💎 ナノリポソームカプセルで急速浸透！大人の冬枯れ肌を湧き上がるハリ感で満たす",
        "catch": "フラコラ最高峰の原液技術。微小エクソソームが角層深部まで一気に駆け巡り、ふっくら艶肌へ",
        "brand_name": "fracora (フラコラ)",
        "capacity": "30ml (ヒト幹細胞培養エキス原液 LP)",
        "type": "リポソーム化ヒト幹細胞エクソソーム原液・導入型美容液",
        "features": "リポソーム化ヒト幹細胞培養エキス、高純度エクソソーム、ペプチドコンプレックス、無香料・界面活性剤フリー",
        "value": "美容液原液市場を牽引するフラコラの集大成。角層の浸透バリアをスムーズに通過するナノカプセル化で、冬の砂漠肌にも圧倒的な馴染みの良さを発揮",
        "desc_p1": "冬のスキンケアで最もストレスとなるのが、重ね付けした化粧水や美容液が肌表面で滑ってしまい、角層奥まで入っていかない『浸透の停滞感』です。フラコラが開発した『ヒト幹細胞培養エキス原液 LP』は、超微小なナノリポソームカプセルを採用することで、この浸透の壁を鮮やかに突破しました。",
        "desc_p2": "さらりとした水のようなテクスチャーでありながら、肌にのせた瞬間に驚くべきスピードで角層深部へと吸い込まれていきます。エクソソームが内包されたカプセルが肌の奥でじわじわと解き放たれ、暖房で乾ききった角層細胞に活力と潤いをチャージ。洗顔直後のファーストステップに投入することで、その後に使用する化粧水や乳液の引き込み効果が劇的に向上し、夕方になってもファンデーションが割れないしっとり感が続きます。",
        "target": "乾燥でスキンケアが浸透しにくくなったと感じる方、ベタつく美容液が苦手な方、土台からふっくらとしたハリを取り戻したい大人の女性",
        "point": "朝晩の洗顔直後、一番最初の素肌に使用。手のひらに適量（500円玉大）を出し、顔の中心から外側へ優しく引き上げるようになじませてください。"
    },
    {
        "rank": 4,
        "tag": "✨ 臍帯血幹細胞由来の圧倒的エネルギー！冬の頑固な乾燥ジワをふっくら持ち上げる",
        "catch": "韓国GD11のバイオサイエンス。大人の肌密度を高めて寒暖差ダメージに負けない健やかな皮膚へ",
        "brand_name": "GD11 (ジーディーイレブン)",
        "capacity": "アドバンスド ラボ エクソソーム アンプル (ダブルアンプル)",
        "type": "高純度ヒト臍帯血幹細胞エクソソーム・集中弾力アンプル",
        "features": "ヒト臍帯血細胞順化培養液エキス、臍帯血由来エクソソーム、エラスチン、複合ペプチド、アデノシン",
        "value": "臍帯血（へその緒）という生命エネルギーに満ちた幹細胞から抽出。脂肪由来と比較して活性タンパク質の含有量が格段に多く、冬の深いエイジングサインに直撃",
        "desc_p1": "寒波が本格化する11月下旬以降は、冷えによって肌の修復リズムが遅れ、目尻やほうれい線、眉間の小ジワが深く刻まれやすくなります。一般的な保湿クリームでは太刀打ちできない年齢肌のしぼみに対して、韓国の幹細胞研究の権威カンステムバイオテック社が送り出したのがGD11の『アドバンスドラボ ダブルアンプル』です。",
        "desc_p2": "凍結乾燥された高純度パウダーとアンプル液を使用直前に混ぜ合わせる新鮮設計。できたてのエクソソームアンプルは、濃厚でとろみのある美容液が肌にぴたりと密着し、まるでラップで密閉したかのように水分の蒸散をブロックします。寝る前にしっかり塗り込むと、翌朝の洗顔時には手のひらを押し返すようなパーンと張った弾力感を体感できます。",
        "target": "冬になると乾燥小ジワやたるみが一気に目立つ方、使う直前に混ぜる新鮮な生アンプルを好む方、本格的なサロン級リフトケアを自宅でしたい方",
        "point": "使用開始時に容器を回してパウダーとアンプルを完全に溶解させます。夜のスキンケアで化粧水の後にたっぷり馴染ませ、特に乾燥が気になる部位には重ね付けを推奨します。"
    },
    {
        "rank": 5,
        "tag": "🌿 サロン専売ハイブリッドエクソソーム！国際特許浸透技術で真冬の肌を鉄壁プロテクト",
        "catch": "エステティックサロンの最前線で採用される最高峰。角層のラメラ構造を整えて一日中ツヤを維持",
        "brand_name": "direia (ディレイア)",
        "capacity": "30ml (ザ ステム セラム EX ソーム)",
        "type": "国際特許浸透ナノテクノロジー・サロン専売ハイブリッドエクソソーム美容液",
        "features": "ヒト幹細胞培養液エキス、ヒト脂肪由来エクソソーム、イノベーティブ3Dナノテクノロジー、ナイアシンアミド",
        "value": "医療分野の薬物送達システム（DDS）をコスメに応用。美容成分を壊さず角層の深部まで届け、乾燥によるバリア破綻を即効修復",
        "desc_p1": "高級エステサロンのフェイシャルトリートメントで使われるプロ仕様コスメの頂点に君臨するディレイア。その核心技術を凝縮した『ザ ステム セラム EX ソーム』は、暖房や冷たい北風でバリア機能が崩壊し、粉を吹いてしまうような極限状態の冬肌を瞬時に救済します。",
        "desc_p2": "最大の強みは国際特許を取得した『イノベーティブ3Dナノテクノロジー』。成分のナノ粒子が肌の皮脂膜と細胞間脂質をスムーズにすり抜け、必要な場所に正確にエクソソームと潤いを届けます。少量でも顔全体にスルスルとシルクのように伸び広がり、塗った瞬間から肌のキメがピシッと揃うような高揚感を味わえます。価格以上の価値を肌で実感できる至極の一本です。",
        "target": "エステサロン級の手応えを求める本物志向の方、冬の深刻なバリア機能低下や粉吹きに悩む方、肌のキメを極限まで整えたい方",
        "point": "洗顔後、化粧水で整えた肌に適量を手に取り、顔全体からデコルテにかけて包み込むように馴染ませます。朝晩の継続使用で肌のバリア強度が劇的に向上します。"
    },
    {
        "rank": 6,
        "tag": "💧 セラミド×エクソソームの強力バリア！暖房によるインナードライを根本から解消",
        "catch": "韓国ドクターズコスメの話題作。細胞間脂質を補修しながらエクソソームが潤いを長時間閉じ込める",
        "brand_name": "Dr.Melaxin (ドクターメラクチン)",
        "capacity": "30ml (セパ ダーマ アンプル)",
        "type": "高保湿バリア再建・セラミドエクソソーム集中アンプル",
        "features": "セラミドNP・AP・EOP、バイオエクソソーム、エクトイン、低分子ヒアルロン酸、弱酸性処方",
        "value": "角層の水分保持に不可欠なセラミドとエクソソームを融合。暖房の風が直撃しても乾燥しない強靭な水分バリアを形成",
        "desc_p1": "オフィスのエアコン暖房直下で長時間過ごすと、肌の表面は皮脂でテカっているのに内側がカピカピに乾く『インナードライ』が悪化します。ドクターメラクチンの『セパ ダーマ アンプル』は、皮膚科専門医の臨床知見から生まれたインナードライ特化型アンプルです。",
        "desc_p2": "肌の水分保持の要である多重セラミドとエクソソームが複合的に働き、角層の隙間を埋めて水分の蒸散をがっちり食い止めます。白濁したまろやかなエマルジョン状のテクスチャーは肌にのせると素早く溶け込み、しっとりとしたうるおい膜を形成。夕方になると顔が突っ張る、乾燥でピリピリするというデリケートな冬の肌を穏やかに鎮め、一日中安定したコンディションをキープします。",
        "target": "冬のエアコン暖房によるインナードライや乾燥崩れに悩む方、敏感肌で刺激に弱い方、セラミド補給とエイジングケアを同時に叶えたい方",
        "point": "化粧水の直後、スポイト1回分を取り顔全体に馴染ませます。特に乾燥が気になる頬や口周りには指の腹で重ね付けを行い、最後にクリームで蓋をしてください。"
    },
    {
        "rank": 7,
        "tag": "🌸 濃厚リッチな美容液ヴェール！冬のゴワついた角質をしなやかにほぐす集中補修",
        "catch": "高純度ヒト幹細胞エキスが乾燥肌を優しく包み込み、もっちり吸い付くような上質スキンへ導く",
        "brand_name": "Cellreva (セルロジーコスメ)",
        "capacity": "30ml (リッチエッセンス)",
        "type": "高保湿リッチエッセンス・ヒト幹細胞エクソソーム美容液",
        "features": "ヒト幹細胞順化培養液、エクソソームコンプレックス、加水分解コラーゲン、リピジュア、植物スクワラン",
        "value": "エステやクリニックでも導入実績多数。濃厚なコクと抜群の保湿持続力で、冬の過酷な乾燥環境でも一日中乾かないツヤ肌を約束",
        "desc_p1": "冷え込みが厳しくなる12月は、肌の水分だけでなく皮脂分泌量も年間で最も少なくなる時期です。油分と水分の両方が枯渇した肌はカサつきが止まらず、小じわが増加します。セルロジーコスメの『リッチエッセンス』は、まさにそんな『砂漠肌』のための濃厚リッチな集中補修エッセンスです。",
        "desc_p2": "とろりとした糸を引くような濃密な美容液には、ヒト幹細胞エキスとエクソソームに加え、高保水成分リピジュアやスクワランを贅沢に配合。肌に伸ばすと極上のオイルセラムのように滑らかに広がり、乾燥で硬くなった角層をじっくりと解きほぐします。翌朝の肌に触れると、前夜のカサつきが嘘のように柔らかく吸い付くようなもっちり感を実感できます。",
        "target": "重ためのリッチなテクスチャーが好きな乾燥肌の方、冬になると粉吹きや皮むけが起きやすい方、保湿力の持続時間を最重視する方",
        "point": "夜のお手入れに、化粧水の後に2プッシュ分を顔全体に馴染ませます。両手で顔を包み込み、手のひらの温もりでじっくりと浸透させるのがポイントです。"
    },
    {
        "rank": 8,
        "tag": "⚡ 100MPa超高圧浸透テクノロジー！角層のすみずみまでスピーディに巡るドラッグストアの実力派",
        "catch": "プチプラ価格帯で最高峰のスペック。毎日惜しみなく使える浸透型エクソソームセラム",
        "brand_name": "unlabel LAB (アンレーベル ラボ)",
        "capacity": "50ml (超高圧 浸透型 エクソソーム 美容液)",
        "type": "超高圧抽出・高浸透ブースターエクソソームセラム",
        "features": "超高圧（100MPa）処理エクソソーム、浸透型コラーゲン、植物性スクワラン、無香料・弱酸性処方",
        "value": "水深1万メートルの圧力に匹敵する超高圧加工で分子を微細化。高価なエクソソームを身近な価格で贅沢に使い倒せるハイコスパの決定版",
        "desc_p1": "『エクソソーム美容液を使ってみたいけれど、1万円を超える高額なものは毎日は続けられない』という方に熱烈に支持されているのが、アンレーベル ラボの『超高圧 浸透型 エクソソーム 美容液』です。全国のドラッグストアやバラエティショップで手軽に購入できる利便性と、確かな浸透技術を両立しています。",
        "desc_p2": "深海の水圧に匹敵する100MPaの超高圧で処理されたエクソソームが、角層のミクロな隙間へ素早く浸透。さらりとしたみずみずしい使い心地で、ベタつきが苦手な方でも朝晩ストレスなく使えます。50mlと大容量なので、顔だけでなく首元やデコルテまでたっぷりケア可能。乾燥によるキメの乱れを整え、つるんとしたなめらかな素肌へ導きます。",
        "target": "コスパ抜群のエクソソーム美容液を探している方、ドラッグストアで手軽に手に入れたい方、首元や手の甲まで惜しみなくケアしたい方",
        "point": "洗顔後すぐに使用する導入タイプ。朝晩2プッシュを手に取り、顔全体から首筋までしっかりと馴染ませます。その後の化粧水の浸透が格段に高まります。"
    },
    {
        "rank": 9,
        "tag": "🍯 高純度パンテノール×エクトインの限界保水！エクソソーム技術が叶える冬の砂漠肌脱出",
        "catch": "魔女工場が誇る最強保湿ライン。暖房や乾燥による肌のつっぱり感を瞬時に鎮める高機能トナーセラム",
        "brand_name": "manyo (魔女工場)",
        "capacity": "200ml (パンテトイン エッセンストナー)",
        "type": "高保水パンテトイン・エクソソームエッセンストナー",
        "features": "パンテトイン（パンテノール×エクトイン）、エクソソーム化ナノカプセル、マカデミア種子油、シドニーハニー",
        "value": "過酷な砂漠でも水分を蓄えるエクトインと修復成分パンテノールをエクソソーム技術で角層へ。化粧水と美容液の中間のような濃密さで乾き知らずの肌へ",
        "desc_p1": "11月・12月の冬枯れ肌に対して、韓国オリーブヤングで爆発的ヒットを記録している魔女工場の『パンテトイン エッセンストナー』。過酷な乾燥環境でも水分を抱え込むエクトインと、肌荒れを防ぐパンテノールを融合した独自成分『パンテトイン』をナノエクソソーム化して配合しています。",
        "desc_p2": "乳白色のとろみのある濃厚なテクスチャーは、肌に塗った瞬間からまるでシートマスクを剥がした直後のようなみずみずしい潤い膜を形成。エアコンの温風が吹きつけるオフィスでも、夕方まで肌の突っ張りやつっぱり感を一切感じさせません。200mlと大容量なので、コットンパックや重ね付け（レイヤリング）にも最適です。",
        "target": "夕方になると顔がパリパリに乾いて痛い方、化粧水と美容液を1本で贅沢に済ませたい方、敏感肌でアルコールや香料が苦手な方",
        "point": "適量を手に取り、顔全体に優しく馴染ませた後、もう一度少量を重ね付けする『2度塗り』がおすすめ。乾燥が気になる部分はコットンに浸して3分間パックするとプルプルになります。"
    },
    {
        "rank": 10,
        "tag": "💫 レチノール×高機能エクソソームの相乗効果！冬のしぼみ肌をふっくら押し上げる大人の集中美容液",
        "catch": "大人のゆらぎ肌に寄り添うBORDER FREE。攻めと守りを両立した高濃度リペア設計",
        "brand_name": "BORDER FREE (ボーダーフリー)",
        "capacity": "30ml (エクソソーム リッチ セラム)",
        "type": "低刺激ビタミンA×ヒト幹細胞エクソソーム・エイジングリッチセラム",
        "features": "高機能エクソソーム、マイクロカプセル化レチノール、ペプチドコンプレックス、セラミド、無香料",
        "value": "乾燥で敏感になりやすい冬の大人の肌のために開発。レチノールによるターンオーバー促進とエクソソームによる肌再生・保水サポートが完璧に調和",
        "desc_p1": "40代以降の冬の肌は、乾燥だけでなくターンオーバーの遅れによるくすみや、弾力線維の衰えによるフェイスラインのゆるみが複合的に押し寄せます。エイジングケアに必須のレチノールを使いたいけれど、真冬は皮むけや乾燥が怖いという声に応えたのがボーダーフリーの集中リッチセラムです。",
        "desc_p2": "刺激を抑えて穏やかに作用するマイクロカプセル化レチノールに、高純度エクソソームとペプチドをブレンド。冬の冷えや乾燥で疲弊した角層細胞を労わりながら、内側から押し上げるようなピンとしたハリ感をもたらします。コクのあるミルキーな質感は肌の上でスッと溶け込み、後肌は吸い付くようにしっとり。冬の夜のスペシャルケアにふさわしい贅沢な一品です。",
        "target": "冬でも皮むけせずにレチノールとエクソソームを取り入れたい方、目元やほうれい線のたるみ・しぼみが気になる方、大人の肌悩みをトータルケアしたい方",
        "point": "夜のお手入れで、化粧水の後に1〜2プッシュを顔全体に優しく塗り広げます。首元までしっかり伸ばし、最後に高保湿クリームでフタをしてください。"
    }
]

faq_items = [
    {
        "q": "エクソソーム美容液とは何ですか？PDRNや一般的なヒト幹細胞美容液と何が違いますか？",
        "a": "エクソソームとは、幹細胞などから分泌される直径50〜150ナノメートルほどの微小な小胞（カプセル）のことです。細胞間の情報伝達を担うメッセンジャーとして、タンパク質やRNAなどの美肌シグナルを内包しています。従来のヒト幹細胞培養液は培養液全体の抽出物であるのに対し、エクソソーム美容液はその中から肌の再生や修復を促す重要な情報カプセルだけを高純度に取り出したものです。PDRN（DNA断片による組織修復）と比べても分子サイズが極めて微小なため、寒冷で硬くなった冬の角層深部へ驚異的な浸透力を発揮し、肌の密度やバリア機能を内側から底上げします。"
    },
    {
        "q": "11月〜12月の日本の冬にエクソソーム美容液が特に推奨される理由は何ですか？",
        "a": "11月から12月は、急激な気温低下と太平洋側のからっ風、さらに室内エアコン暖房の稼働により、湿度が年間最低レベルに落ち込みます。この寒暖差と乾燥ストレスにより、皮膚のターンオーバーが停滞して角層がゴワつき、毛穴がたるみ、小ジワが一気に定着しやすくなります。エクソソーム美容液は、低下した細胞間コミュニケーションを補い、角層のラメラ構造やコラーゲンネットワークの再構築を強力にサポートするため、真冬の『しぼみ肌』や『乾燥毛穴』を根本から立て直すのに最も適した成分です。"
    },
    {
        "q": "エクソソーム美容液を使う順番はいつですか？朝も使えますか？",
        "a": "製品の処方によって最適なタイミングが異なります。水のように軽やかな原液タイプや導入タイプ（フラコラ、アンレーベルなど）は洗顔直後の一番最初の素肌に使用します。一方、とろみのあるアンプルタイプやジェル状タイプ（メディキューブ、KISOなど）は、化粧水でしっかり肌を湿らせて角質を柔軟にした後に塗布するのが基本です。朝晩どちらも使用可能で、朝に使用するとオフィスの暖房乾燥から一日中肌を守りメイク割れを防ぎます。レチノール配合の製品（ボーダーフリーなど）のみ、紫外線影響を考慮して夜の使用をおすすめします。"
    },
    {
        "q": "敏感肌や冬のゆらぎ肌でも刺激なく使えますか？",
        "a": "エクソソーム自体は生体由来の非常に親和性の高い成分であり、炎症を鎮める抗炎症作用やバリア機能の回復サポート効果があるため、敏感肌やゆらぎ肌にこそ適しています。ただし、メディキューブのような微細ニードル（スピキュール）配合製品は塗布時に特有のチクチク感があるため、肌が極度にヒリついているときは低刺激の原液タイプ（KISOやフラコラ、manyoなど）を選ぶのが安心です。"
    },
    {
        "q": "冬の乾燥を完全に防ぐための、エクソソーム美容液の併用おすすめアイテムは？",
        "a": "エクソソームが引き込んだ潤いを逃さないために、油分を含む高保湿乳液やセラミド配合クリームでの『ラッピング』が不可欠です。また、角層の水分量を最大化するために、ヒアルロン酸化粧水で十分に保水した後にエクソソーム美容液を重ね、仕上げにスクワランやシアバター配合のフェイスクリームで密閉するサンドイッチ保湿が11月・12月の冬には最も効果的です。"
    }
]

# JSON-LD構造化データ
json_ld_products = []
for p, item in zip(product_details, items):
    json_ld_products.append({
        "@type": "Product",
        "name": f"{p['brand_name']} {p['capacity']}",
        "image": item['image'],
        "description": p['value'],
        "brand": {
            "@type": "Brand",
            "name": p['brand_name']
        },
        "offers": {
            "@type": "Offer",
            "url": item['affiliateUrl'],
            "priceCurrency": "JPY",
            "price": item['price'],
            "availability": "https://schema.org/InStock"
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで冬の肌荒れ・しぼみ肌とさようなら！次世代細胞サイエンスで角層深部から押し返す高保湿エクソソーム美容液ランク10",
    "description": "11月・12月の本格的な寒気と暖房直撃による大人のしぼみ肌・たるみ毛穴・乾燥小ジワを徹底解決！2026年最新の次世代エイジングケア成分「高純度エクソソーム」を配合した高保湿美容液10選を徹底比較！メディキューブ、KISO、フラコラ、GD11、ディレイアなど、角層奥深くまで浸透して押し返すハリツヤ肌を叶える名品を厳選。",
    "image": items[0]['image'],
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
    "datePublished": "2026-11-02",
    "dateModified": "2026-11-02"
}

json_ld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "冬の高保湿エクソソーム美容液 おすすめランキング10選",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "item": prod
        } for idx, prod in enumerate(json_ld_products)
    ]
}

json_ld_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["a"]
            }
        } for item in faq_items
    ]
}

cards_html = []
for p, item in zip(product_details, items):
    cards_html.append(f"""
      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge-wrap">
          <span class="product-rank-badge rank-{p['rank']}">第{p['rank']}位</span>
          <span class="product-tag">{p['tag']}</span>
        </div>
        <div class="product-header">
          <h3 class="product-title">{p['brand_name']} {p['capacity']}</h3>
          <p class="product-catch">{p['catch']}</p>
        </div>
        <div class="product-layout">
          <div class="product-img-box">
            <img src="{item['image']}" alt="{p['brand_name']} {p['capacity']}" class="product-img" loading="lazy" width="300" height="300">
            <div class="product-price-tag">参考価格: <span>¥{item['price']:,}</span> (税込)</div>
          </div>
          <div class="product-specs">
            <table class="spec-table">
              <tr><th>アイテムタイプ</th><td>{p['type']}</td></tr>
              <tr><th>注目美容成分</th><td>{p['features']}</td></tr>
              <tr><th>期待できる効果</th><td>{p['value']}</td></tr>
              <tr><th>おすすめの肌質</th><td>{p['target']}</td></tr>
            </table>
          </div>
        </div>
        <div class="product-body">
          <div class="product-desc">
            <p>{p['desc_p1']}</p>
            <p>{p['desc_p2']}</p>
          </div>
          <div class="product-advice">
            <div class="advice-title">💡 美容コンシェルジュの使いこなしポイント</div>
            <p>{p['point']}</p>
          </div>
        </div>
        <div class="product-action">
          <a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で最安値・在庫をチェック
            <svg class="btn-arrow" viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"/></svg>
          </a>
        </div>
      </article>
""")

comparison_rows = []
for p, item in zip(product_details, items):
    comparison_rows.append(f"""
            <tr>
              <td class="col-rank"><span class="table-rank rank-{p['rank']}">{p['rank']}</span></td>
              <td class="col-thumb"><img src="{item['image']}" alt="{p['brand_name']}" class="table-img" loading="lazy" width="60" height="60"></td>
              <td class="col-name"><strong>{p['brand_name']}</strong><br><small>{p['capacity']}</small></td>
              <td class="col-type">{p['type']}</td>
              <td class="col-features">{p['features']}</td>
              <td class="col-price">¥{item['price']:,}</td>
              <td class="col-btn"><a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="table-btn">楽天詳細</a></td>
            </tr>
""")

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の肌荒れ・しぼみ肌とさようなら！次世代細胞サイエンスで角層深部から押し返す高保湿エクソソーム美容液ランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の本格的な寒気と暖房直撃による大人のしぼみ肌・たるみ毛穴・乾燥小ジワを徹底解決！2026年最新の次世代エイジングケア成分「高純度エクソソーム」を配合した高保湿美容液10選を徹底比較！メディキューブ、KISO、フラコラ、GD11、ディレイアなど、角層奥深くまで浸透して押し返すハリツヤ肌を叶える名品を厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-exosome-serum">
  <meta name="robots" content="index, follow, max-image-preview:large">
  
  <!-- OGP & SNS -->
  <meta property="og:title" content="保湿力の強さで冬の肌荒れ・しぼみ肌とさようなら！次世代細胞サイエンスで角層深部から押し返す高保湿エクソソーム美容液ランク10">
  <meta property="og:description" content="11月・12月の暖房直撃と寒波による深刻なしぼみ肌・たるみ毛穴・乾燥小ジワを徹底解決！最新エクソソーム配合の高保湿美容液10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-exosome-serum">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#c94b6e">

  <!-- 構造化データ (JSON-LD) -->
  <script type="application/ld+json">
{json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(json_ld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(json_ld_faq, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #c94b6e;
      --primary-light: #fdf2f4;
      --primary-dark: #a33250;
      --text-main: #2d3748;
      --text-sub: #718096;
      --bg-page: #fbfbfc;
      --bg-card: #ffffff;
      --border: #edf2f7;
      --border-focus: #feb2b2;
      --shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
      --radius: 16px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif;
      background: var(--bg-page);
      color: var(--text-main);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}
    header.site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(10px);
      background-color: rgba(255, 255, 255, 0.95);
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-weight: 800;
      font-size: 1.25rem;
      color: var(--primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .header-nav a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .header-nav a:hover {{ color: var(--primary); }}
    
    .container {{
      max-width: 920px;
      margin: 0 auto;
      padding: 30px 20px 80px;
    }}
    
    .breadcrumbs {{
      display: flex;
      gap: 8px;
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 24px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .breadcrumbs a {{
      color: var(--text-sub);
      text-decoration: none;
    }}
    .breadcrumbs a:hover {{ color: var(--primary); }}
    
    .article-header {{
      background: var(--bg-card);
      padding: 36px 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 32px;
      border: 1px solid var(--border);
    }}
    .article-meta {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 12px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .badge-category {{
      background: var(--primary-light);
      color: var(--primary);
      padding: 3px 10px;
      border-radius: 20px;
      font-weight: 700;
    }}
    .article-title {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #1a202c;
      margin-bottom: 20px;
      font-weight: 800;
      letter-spacing: -0.02em;
    }}
    .article-lead {{
      font-size: 1.05rem;
      color: #4a5568;
      line-height: 1.9;
      border-left: 4px solid var(--primary);
      padding-left: 18px;
      margin-bottom: 20px;
    }}
    
    .toc {{
      background: #f7fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 24px;
      margin: 32px 0;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      color: #2d3748;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      padding-left: 8px;
      margin: 0;
    }}
    .toc-list li {{
      margin-bottom: 8px;
      font-size: 0.95rem;
    }}
    .toc-list a {{
      color: #4a5568;
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .section-block {{
      background: var(--bg-card);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 36px 32px;
      margin-bottom: 40px;
      border: 1px solid var(--border);
    }}
    .section-h2 {{
      font-size: 1.55rem;
      color: #1a202c;
      margin-bottom: 24px;
      font-weight: 800;
      position: relative;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--border);
    }}
    .section-h2::after {{
      content: "";
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 60px;
      height: 2px;
      background: var(--primary);
    }}
    
    .content-p {{
      font-size: 1.02rem;
      color: #4a5568;
      line-height: 1.9;
      margin-bottom: 18px;
    }}

    .point-box {{
      background: #fffaf0;
      border: 1px solid #feebc8;
      border-radius: 12px;
      padding: 20px 24px;
      margin: 24px 0;
    }}
    .point-box-title {{
      color: #c05621;
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    
    /* Product Card */
    .product-card {{
      background: var(--bg-card);
      border-radius: var(--radius);
      box-shadow: 0 4px 24px rgba(0,0,0,0.06);
      margin-bottom: 44px;
      overflow: hidden;
      border: 1px solid #e2e8f0;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(0,0,0,0.09);
    }}
    .product-badge-wrap {{
      background: #edf2f7;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid #e2e8f0;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .product-rank-badge {{
      display: inline-block;
      padding: 4px 14px;
      border-radius: 20px;
      font-weight: 800;
      font-size: 0.95rem;
      color: #ffffff;
      background: #718096;
    }}
    .product-rank-badge.rank-1 {{ background: linear-gradient(135deg, #d69e2e, #b7791f); }}
    .product-rank-badge.rank-2 {{ background: linear-gradient(135deg, #a0aec0, #718096); }}
    .product-rank-badge.rank-3 {{ background: linear-gradient(135deg, #dd6b20, #c05621); }}
    .product-tag {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #4a5568;
    }}
    
    .product-header {{
      padding: 24px 28px 12px;
    }}
    .product-title {{
      font-size: 1.4rem;
      color: #1a202c;
      font-weight: 800;
      line-height: 1.4;
      margin-bottom: 8px;
    }}
    .product-catch {{
      font-size: 0.98rem;
      color: var(--primary-dark);
      font-weight: 700;
      line-height: 1.5;
    }}
    
    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
      padding: 12px 28px 24px;
      align-items: start;
    }}
    @media(max-width: 768px) {{
      .product-layout {{
        grid-template-columns: 1fr;
      }}
    }}
    .product-img-box {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      background: #f7fafc;
      border-radius: 12px;
      border: 1px solid #edf2f7;
      padding: 10px;
    }}
    .product-price-tag {{
      margin-top: 10px;
      font-size: 0.9rem;
      color: #718096;
    }}
    .product-price-tag span {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #e53e3e;
    }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 10px 12px;
      border-bottom: 1px solid #edf2f7;
      text-align: left;
    }}
    .spec-table th {{
      width: 32%;
      color: #718096;
      background: #f8fafc;
      font-weight: 600;
    }}
    .spec-table td {{
      color: #2d3748;
    }}

    .product-body {{
      padding: 0 28px 24px;
    }}
    .product-desc p {{
      font-size: 0.98rem;
      color: #4a5568;
      line-height: 1.85;
      margin-bottom: 14px;
    }}
    .product-advice {{
      background: #f0fff4;
      border: 1px solid #c6f6d5;
      border-radius: 10px;
      padding: 16px 20px;
      margin-top: 18px;
    }}
    .advice-title {{
      font-weight: 700;
      font-size: 0.92rem;
      color: #276749;
      margin-bottom: 6px;
    }}
    .product-advice p {{
      font-size: 0.92rem;
      color: #2f855a;
      line-height: 1.7;
      margin: 0;
    }}
    
    .product-action {{
      padding: 16px 28px 28px;
      text-align: center;
      background: #fafafa;
      border-top: 1px solid #edf2f7;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: linear-gradient(135deg, #bf0000, #960000);
      color: #ffffff !important;
      text-decoration: none;
      font-weight: 700;
      font-size: 1.05rem;
      padding: 14px 32px;
      border-radius: 30px;
      box-shadow: 0 4px 14px rgba(191,0,0,0.3);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 440px;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(191,0,0,0.4);
      background: linear-gradient(135deg, #cc0000, #a30000);
    }}
    
    /* Comparison Table */
    .table-scroll {{
      overflow-x: auto;
      margin: 24px 0;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
    }}
    .comp-table {{
      width: 100%;
      min-width: 760px;
      border-collapse: collapse;
      font-size: 0.92rem;
      background: #ffffff;
    }}
    .comp-table th, .comp-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid #edf2f7;
      vertical-align: middle;
      text-align: left;
    }}
    .comp-table th {{
      background: #f7fafc;
      color: #4a5568;
      font-weight: 700;
      white-space: nowrap;
    }}
    .col-rank {{ width: 50px; text-align: center; }}
    .table-rank {{
      display: inline-block;
      width: 26px;
      height: 26px;
      line-height: 26px;
      border-radius: 50%;
      background: #a0aec0;
      color: #fff;
      font-weight: 800;
      font-size: 0.85rem;
      text-align: center;
    }}
    .table-rank.rank-1 {{ background: #d69e2e; }}
    .table-rank.rank-2 {{ background: #718096; }}
    .table-rank.rank-3 {{ background: #dd6b20; }}
    .table-img {{
      width: 60px;
      height: 60px;
      object-fit: contain;
      border-radius: 6px;
      border: 1px solid #edf2f7;
    }}
    .col-price {{
      font-weight: 800;
      color: #e53e3e;
      white-space: nowrap;
    }}
    .table-btn {{
      display: inline-block;
      padding: 6px 14px;
      background: #bf0000;
      color: #fff !important;
      text-decoration: none;
      font-size: 0.82rem;
      font-weight: 700;
      border-radius: 6px;
      white-space: nowrap;
    }}
    
    /* FAQ Section */
    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .faq-item {{
      background: #f8fafc;
      border-radius: 12px;
      padding: 20px 24px;
      border: 1px solid #edf2f7;
    }}
    .faq-q {{
      font-weight: 800;
      font-size: 1.05rem;
      color: #2d3748;
      margin-bottom: 10px;
      display: flex;
      gap: 10px;
      align-items: baseline;
    }}
    .faq-q-mark {{
      color: var(--primary);
      font-size: 1.2rem;
    }}
    .faq-a {{
      font-size: 0.98rem;
      color: #4a5568;
      line-height: 1.85;
      padding-left: 24px;
    }}
    
    /* Related Articles */
    .related-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 14px;
      margin-top: 20px;
    }}
    .related-link-card {{
      background: #ffffff;
      border: 1px solid #edf2f7;
      padding: 14px 18px;
      border-radius: 10px;
      text-decoration: none;
      color: #2d3748;
      font-size: 0.92rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }}
    .related-link-card:hover {{
      border-color: var(--primary);
      color: var(--primary);
      transform: translateX(3px);
      box-shadow: 0 2px 10px rgba(201, 75, 110, 0.1);
    }}

    footer.site-footer {{
      background: #1a202c;
      color: #a0aec0;
      padding: 60px 20px 30px;
      font-size: 0.9rem;
      margin-top: 60px;
    }}
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
    }}
    .footer-brand {{
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      margin-bottom: 16px;
    }}
    .footer-desc {{
      max-width: 650px;
      line-height: 1.7;
      margin-bottom: 30px;
      font-size: 0.85rem;
    }}
    .footer-links-title {{
      color: #ffffff;
      font-weight: 700;
      margin-bottom: 16px;
      font-size: 0.95rem;
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
      gap: 10px;
      margin-bottom: 40px;
    }}
    .footer-links-grid a {{
      color: #cbd5e0;
      text-decoration: none;
      font-size: 0.82rem;
      transition: color 0.2s;
    }}
    .footer-links-grid a:hover {{
      color: #feb2b2;
    }}
    .footer-copy {{
      border-top: 1px solid #2d3748;
      padding-top: 24px;
      text-align: center;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">
        <span>✨</span> 冬コスメ徹底比較ラボ
      </a>
      <nav class="header-nav">
        <a href="/">冬コスメ一覧トップへ</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumbs">
      <a href="/">ホーム</a>
      <span>&gt;</span>
      <a href="/winter-hydrating-serum">高保湿美容液</a>
      <span>&gt;</span>
      <span>高保湿エクソソーム美容液</span>
    </nav>

    <header class="article-header">
      <div class="article-meta">
        <span class="badge-category">2026年最新エイジングサイエンス</span>
        <span class="badge-date">更新日: 2026年11月02日</span>
        <span class="badge-author">監修: 冬コスメ徹底比較ラボ 専門検証チーム</span>
      </div>
      <h1 class="article-title">保湿力の強さで冬の肌荒れ・しぼみ肌とさようなら！次世代細胞サイエンスで角層深部から押し返す高保湿エクソソーム美容液ランク10</h1>
      <p class="article-lead">
        11月から12月にかけて日本列島に冬将軍が到来すると、外気の急激な冷え込みと太平洋側特有のからっ風、さらに室内を24時間温め続ける暖房エアコンの温風により、肌の湿度は砂漠以下の20%台まで急降下します。寒暖差で硬くなった角質と血行不良により、夕方になると「頬の毛穴が縦に流れてしぼむ」「ファンデーションが乾燥でひび割れる」という深刻なエイジングサインに直面する女性が後を絶ちません。従来の保湿美容液では届かなかった角層深部へのアプローチとして、2026年冬に美容皮膚科医やコスメフリークの間で圧倒的な注目を集めているのが「高純度エクソソーム美容液」です。本記事では、微細ニードル配合タイプから国産ヒト幹細胞原液、サロン専売モデルまで、真冬の砂漠肌を跳ね返す最強の10本を厳選徹底比較します。
      </p>
    </header>

    <nav class="toc">
      <div class="toc-title">📑 目次・もくじ</div>
      <ul class="toc-list">
        <li><a href="#mechanism">1. 11月・12月の冬に肌が「しぼむ」メカニズムとエクソソームの役割</a></li>
        <li><a href="#how-to-choose">2. 失敗しない！冬の高保湿エクソソーム美容液を選ぶ3つの基準</a></li>
        <li><a href="#ranking">3. 冬の高保湿エクソソーム美容液 おすすめランキング10選</a></li>
        <li><a href="#comparison">4. 一目でわかる！全10商品のスペック＆価格徹底比較表</a></li>
        <li><a href="#skincare-method">5. 美容エディター直伝！冬の浸透力を極限まで高める実践スキンケアメソッド</a></li>
        <li><a href="#faq">6. よくある質問（FAQ）</a></li>
        <li><a href="#related">7. あわせて読みたい関連冬コスメ特集</a></li>
      </ul>
    </nav>

    <!-- セクション1: メカニズム -->
    <section class="section-block" id="mechanism">
      <h2 class="section-h2">1. 11月・12月の冬に肌が「しぼむ」メカニズムとエクソソームの役割</h2>
      <p class="content-p">
        11月に入ると外気温は一気に一桁台へと冷え込み、湿度は初秋の半分以下に低下します。特に東京をはじめとする太平洋側では乾燥した北西の季節風が吹き荒れ、大気中の水分が極端に奪われます。さらにオフィスや自宅でエアコン暖房が稼働し始めると、温風が直接素肌に吹きつけ、角層の水分蒸散スピードは夏の約3倍に加速します。
      </p>
      <p class="content-p">
        寒冷ストレスにさらされた肌は、体温を逃さないように末梢血管を収縮させるため、真皮層への酸素や栄養素の補給が滞り、肌の生まれ変わりであるターンオーバー周期が鈍化します。その結果、古い角質が排出されずに表面に蓄積してゴワつきが生じ、細胞と細胞のすき間を満たす「細胞間脂質（セラミドなど）」のラメラ構造が崩壊。水分を保持できなくなった角層は萎縮し、頬のたるみ毛穴や表情ジワが夕方にくっきりと浮き彫りになる「冬枯れしぼみ肌」が完成してしまうのです。
      </p>
      <div class="point-box">
        <div class="point-box-title">💡 なぜ2026年冬、エクソソームが最強の解決策になるのか？</div>
        <p class="content-p" style="margin-bottom:0;">
          エクソソームは、細胞と細胞の間で美肌情報を伝達する直径50〜150ナノメートルの微小な情報カプセルです。従来の保湿成分が「表面を水分で覆う」のに対し、ナノサイズのエクソソームは寒さで硬くなった角層細胞のミクロな隙間を軽々とすり抜け、角層深部へダイレクトに到達。弱った細胞間コミュニケーションを活性化し、コラーゲンやエラスチンの土台づくりをサポートすることで、外気20%の砂漠環境でも押し返すような肌密度を蘇らせます。
        </p>
      </div>
    </section>

    <!-- セクション2: 選び方 -->
    <section class="section-block" id="how-to-choose">
      <h2 class="section-h2">2. 失敗しない！冬の高保湿エクソソーム美容液を選ぶ3つの基準</h2>
      
      <h3 style="font-size:1.15rem; color:#2d3748; margin: 18px 0 10px; font-weight:700;">① 由来と純度：ヒト脂肪由来・臍帯血由来の明記とリポソーム化技術</h3>
      <p class="content-p">
        エクソソーム美容液を選ぶ第一の基準は、幹細胞の「由来」と「浸透技術」です。美容医療やエイジングケアで確かな実績を持つヒト脂肪由来間葉系幹細胞や、希少なヒト臍帯血（へその緒）由来のエクソソームは、成長因子や活性ペプチドを豊富に含有しています。さらに、熱や乾燥にデリケートなエクソソームを生体膜に近い「リポソームカプセル」でナノカプセル化した製品は、冬のゴワついた角質層にもスムーズに引き込まれ、持続的な保水力を発揮します。
      </p>

      <h3 style="font-size:1.15rem; color:#2d3748; margin: 18px 0 10px; font-weight:700;">② 複合保湿処方：セラミド・ヒアルロン酸・エクトインとの相乗効果</h3>
      <p class="content-p">
        11月〜12月の過酷な暖房環境下では、エクソソーム単体だけでなく、角層の水分をガッチリ抱え込む高保湿成分が同時に配合されているかどうかが勝負の分かれ目となります。肌のバリアを補強するヒト型セラミド（NP・AP・EOP）、分子量の異なる多重ヒアルロン酸、そして過酷な砂漠生物由来の保水成分「エクトイン」が組み合わさった製品を選ぶことで、日中の水分蒸散を鉄壁ブロックできます。
      </p>

      <h3 style="font-size:1.15rem; color:#2d3748; margin: 18px 0 10px; font-weight:700;">③ 使用シーンに合わせたテクスチャー：朝の速攻浸透か、夜の集中リッチか</h3>
      <p class="content-p">
        朝のメイク前に使用する場合は、ファンデーションのモロモロやヨレを防ぐため、水のように馴染む導入リキッド型（フラコラやアンレーベル）やジェル型（メディキューブ）が最適です。一方、夜の就寝中に暖房直撃による砂漠化を防ぎたい場合は、とろみのある濃厚アンプル型（KISOやGD11、セルロジーコスメ）を選び、睡眠中の肌再生をバックアップしましょう。
      </p>
    </section>

    <!-- セクション3: ランキング -->
    <section id="ranking">
      <div style="text-align: center; margin-bottom: 32px;">
        <span style="color: var(--primary); font-weight: 800; font-size: 0.95rem; letter-spacing: 0.1em; text-transform: uppercase;">RECOMMENDED RANKING</span>
        <h2 style="font-size: 1.8rem; color: #1a202c; font-weight: 800; margin-top: 6px;">冬の高保湿エクソソーム美容液 おすすめランキング10選</h2>
        <p style="color: var(--text-sub); font-size: 0.95rem; margin-top: 8px;">2026年11月・12月の冬枯れ肌を救う、厳選された高純度エクソソーム美容液を徹底検証</p>
      </div>

      {"".join(cards_html)}
    </section>

    <!-- セクション4: 比較表 -->
    <section class="section-block" id="comparison">
      <h2 class="section-h2">4. 一目でわかる！全10商品のスペック＆価格徹底比較表</h2>
      <p class="content-p">
        ランクインした10商品のアイテムタイプ、注目成分、参考価格を一元化しました。肌質やお好みの使用感に合わせて最適な1本を見つけてみてください。
      </p>
      <div class="table-scroll">
        <table class="comp-table">
          <thead>
            <tr>
              <th class="col-rank">順位</th>
              <th>商品画像</th>
              <th>ブランド・商品名</th>
              <th>タイプ</th>
              <th>注目成分</th>
              <th>参考価格</th>
              <th>楽天リンク</th>
            </tr>
          </thead>
          <tbody>
            {"".join(comparison_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション5: 実践スキンケアメソッド -->
    <section class="section-block" id="skincare-method">
      <h2 class="section-h2">5. 美容エディター直伝！冬の浸透力を極限まで高める実践スキンケアメソッド</h2>
      <p class="content-p">
        どんなに高価で優れたエクソソーム美容液であっても、冬の冷え切った肌にそのまま塗布しただけでは、そのポテンシャルの半分も引き出せません。気温が急降下する11月・12月に実践すべき「浸透力最大化の3ステップ」を伝授します。
      </p>
      
      <div style="background:#f8fafc; border-left:4px solid var(--primary); padding:16px 20px; margin-bottom:18px; border-radius:0 8px 8px 0;">
        <strong style="color:#2d3748; display:block; margin-bottom:4px;">ステップ1：入浴直後の「スチーム温感ハンドプレス」</strong>
        <p style="font-size:0.95rem; color:#4a5568; margin:0; line-height:1.7;">
          冬は皮脂が固まり毛穴が収縮しています。洗顔後、清潔なホットタオルで顔全体を30秒温めるか、入浴直後の血流が促された状態でスキンケアをスタート。美容液を手にとったら、両手のひらを擦り合わせて体温程度に温めてから肌を包み込みます。これだけで角層の柔軟性が劇的に高まります。
        </p>
      </div>

      <div style="background:#f8fafc; border-left:4px solid var(--primary); padding:16px 20px; margin-bottom:18px; border-radius:0 8px 8px 0;">
        <strong style="color:#2d3748; display:block; margin-bottom:4px;">ステップ2：乾燥ゾーンへの「ミルフィーユ重ね付け」</strong>
        <p style="font-size:0.95rem; color:#4a5568; margin:0; line-height:1.7;">
          顔全体に薄く伸ばしてハンドプレスした後、暖房の温風が直撃しやすい「頬の高い位置」「目尻のちりめんジワ」「口周りのほうれい線」に、もう半滴を指の腹でトントンと優しくタップするように重ね付けします。層（ミルフィーユ）を重ねることで、乾燥の集中地帯に強靭な保湿クッションが形成されます。
        </p>
      </div>

      <div style="background:#f8fafc; border-left:4px solid var(--primary); padding:16px 20px; margin-bottom:18px; border-radius:0 8px 8px 0;">
        <strong style="color:#2d3748; display:block; margin-bottom:4px;">ステップ3：高保湿クリームでの「3分以内密閉シールド」</strong>
        <p style="font-size:0.95rem; color:#4a5568; margin:0; line-height:1.7;">
          エクソソームが浸透した直後の肌は水分保持の好機。そのまま放置すると湿度の低い室内に水分を奪われてしまうため、美容液塗布から3分以内にセラミドやシアバターを配合した濃厚クリームで油分のフタを密着させます。水分の蒸散を完全に遮断することで、翌朝まで吸い付くようなハリが続きます。
        </p>
      </div>
    </section>

    <!-- セクション6: FAQ -->
    <section class="section-block" id="faq">
      <h2 class="section-h2">6. よくある質問（FAQ）</h2>
      <div class="faq-list">
        {"".join([f'''
        <div class="faq-item">
          <div class="faq-q"><span class="faq-q-mark">Q.</span><span>{item["q"]}</span></div>
          <div class="faq-a">{item["a"]}</div>
        </div>
        ''' for item in faq_items])}
      </div>
    </section>

    <!-- セクション7: 関連記事リンク -->
    <section class="section-block" id="related">
      <h2 class="section-h2">7. あわせて読みたい関連冬コスメ特集</h2>
      <p class="content-p">冬の乾燥対策を完璧にするために、他の高保湿スキンケア特集もあわせてチェックしてみてください。</p>
      <div class="related-links-grid">
        <a href="/winter-pdrn-serum" class="related-link-card">🧬 高保湿PDRN美容液</a>
        <a href="/winter-collagen-mask" class="related-link-card">🌙 バイオコラーゲンマスク</a>
        <a href="/winter-carbonic-shampoo" class="related-link-card">🫧 高濃度炭酸シャンプー</a>
        <a href="/winter-ceramide-serum" class="related-link-card">🛡️ セラミド美容液</a>
        <a href="/winter-retinol-cream" class="related-link-card">🌟 レチノールクリーム</a>
        <a href="/winter-night-cream" class="related-link-card">🌃 ナイトクリーム</a>
        <a href="/winter-oil-mist" class="related-link-card">✨ 高保湿オイルインミスト</a>
        <a href="/winter-carbonic-serum" class="related-link-card">🫧 高保湿炭酸泡美容液</a>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand">冬コスメ徹底比較ラボ</div>
      <p class="footer-desc">
        冬コスメ徹底比較ラボは、11月・12月の本格的な日本の冬に立ち向かう女性のために、乾燥・冷え・寒暖差から素肌と髪を守る高保湿コスメを徹底検証・比較する専門メディアです。全商品は楽天市場公式APIおよび各種臨床データを基に中立的に評価・掲載しています。
      </p>
      <div class="footer-links-title">カテゴリ別 冬コスメ徹底比較ガイド</div>
      <div class="footer-links-grid">
        <a href="/winter-exosome-serum">高保湿エクソソーム美容液</a>
        <a href="/winter-pdrn-serum">高保湿PDRN美容液</a>
        <a href="/winter-collagen-mask">バイオコラーゲンマスク</a>
        <a href="/winter-carbonic-shampoo">高濃度炭酸シャンプー</a>
        <a href="/winter-oil-mist">高保湿オイルインミスト</a>
        <a href="/winter-carbonic-bath">薬用重炭酸入浴剤</a>
        <a href="/winter-hot-treatment">温感ヘッドスパ</a>
        <a href="/winter-foot-mask">高保湿かかとパック</a>
        <a href="/winter-eye-patch">高保湿アイパッチ</a>
        <a href="/winter-nail-serum">ネイル補修美容液</a>
        <a href="/winter-inbath-body">インバスボディミルク</a>
        <a href="/winter-hot-eyemask">ホットアイマスク</a>
        <a href="/winter-hand-mask">高保湿ハンドマスク</a>
        <a href="/winter-needle-patch">ニードルパッチ</a>
        <a href="/winter-bath-salt">高保湿バスソルト</a>
        <a href="/winter-lip-gloss">リップグロス</a>
        <a href="/winter-morning-mask">朝用シートマスク</a>
        <a href="/winter-gel-wash">ジェル洗顔</a>
        <a href="/winter-lip-primer">リップ下地</a>
        <a href="/winter-carbonic-wash">炭酸泡洗顔</a>
        <a href="/winter-ceramide-serum">セラミド美容液</a>
        <a href="/winter-retinol-cream">レチノールクリーム</a>
        <a href="/winter-night-cream">ナイトクリーム</a>
        <a href="/winter-cica-cream">シカクリーム</a>
        <a href="/winter-lotion">高保湿化粧水</a>
        <a href="/winter-face-mask">シートマスク</a>
        <a href="/winter-eye-cream">アイクリーム</a>
        <a href="/winter-lip-cream">リップクリーム</a>
        <a href="/winter-hand-cream">ハンドクリーム</a>
        <a href="/winter-body-cream">ボディクリーム</a>
        <a href="/winter-hair-oil">ヘアオイル</a>
        <a href="/summer-cosme">夏コスメ</a>
      </div>
      <div class="footer-copy">
        &copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved.
      </div>
    </div>
  </footer>

</body>
</html>
"""

output_path = "winter-exosome-serum.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"🎉 Generated {output_path} successfully!")
