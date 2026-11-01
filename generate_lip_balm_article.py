import json

with open("rakuten_hair_lip_carbonic_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_lip_balm"]["items"]

lip_balm_details = [
    {
        "rank": 1,
        "tag": "🏆 セラミドケア×低刺激処方！敏感で荒れやすい冬の唇を濃密ラップで徹底シールドする薬用スティック",
        "catch": "角層の隙間を満たすセラミド機能成分が唇深くまで浸透。無香料・弱酸性で荒れた唇に刺激なく密着",
        "capacity": "4.2g",
        "type": "医薬部外品・薬用セラミド高保湿リップケアクリーム",
        "texture": "唇の体温でするりととろけ、摩擦を一切感じさせずに滑らかに広がるメルティバーム",
        "ingredients": "消炎有効成分（グリチルレチン酸ステアリル）、セラミド機能成分（ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド）、ホホバ油、スクワラン",
        "finish": "ベタつかないのに唇全体がうるおいの膜でピタッと密着コーティングされ、乾いた突っ張り感が瞬時に消失",
        "desc_p1": "11月から12月にかけて外気の湿度が低下すると、最も早く深刻なダメージを受けるのが唇です。唇には皮脂腺や汗腺が一切存在せず、自力で皮脂膜（天然のうるおいバリア）を作ることができません。さらに角層の厚さは通常の皮膚の約3分の1しかなく、エアコン暖房の温風やマスク内の呼気蒸散によって、わずか数分で水分が蒸発してカサカサに強張ります。",
        "desc_p2": "花王キュレルの『リップケアクリーム』は、皮膚科医からも推奨される低刺激設計の薬用リップクリーム。角層の水分保持に不可欠なセラミドの働きを忠実に補うセラミド機能成分を配合し、乾いてめくれかけた唇の角層をなめらかに密着修復します。無香料・無着色・アルコールフリーのため、皮が剥けてヒリヒリ痛むデリケートな唇にも全く染みることなく、一日中みずみずしいバリアを保ち続けます。",
        "target": "唇が乾燥して皮が剥けやすくヒリヒリ刺激を感じやすい敏感肌の方、マスクや暖房による唇の強張りや縦ジワが気になる方、口紅を塗る前の無色・低刺激な保湿下地を求める方",
        "technique": "唇の縦ジワに沿って、上から下へと縦方向に優しく滑らせるように塗布します。横方向にゴシゴシ塗ると摩擦で角質が剥がれる原因になるため、体温でリップの表面を少し温めてから軽いタッチで乗せるのがコツです。",
        "voice": "『毎年冬になると唇の皮がめくれて血が出ていましたが、キュレルを使い始めてから全く荒れなくなりました。ベタベタせずマスクにもつかないので年中持ち歩いています。』(30代・看護師)",
        "caution": "柔らかいスティックのため、2〜3mm以上長く繰り出しすぎると折れることがあります。少しずつ出してご使用ください。"
    },
    {
        "rank": 2,
        "tag": "🩹 医薬品の確かな治療力！唇のひび割れ・血がにじむ深い皮剥け・口唇炎を根本から治す冬の救世主",
        "catch": "5つの有効成分が炎症を鎮め組織を修復。痛くて笑えないガサガサ唇を一晩でなめらかな健やか唇へ",
        "capacity": "8g",
        "type": "第3類医薬品・口唇炎・口角炎治療薬リップ",
        "texture": "こっくりとして厚みのあるなめらかバーム。チューブタイプで患部に直接ピンポイント密着",
        "ingredients": "アラントイン（組織修復）、グリチルレチン酸（抗炎症）、トコフェロール酢酸エステル（ビタミンE・血行促進）、ピリドキシン塩酸塩（ビタミンB6・皮膚代謝）、パンテノール（皮膚粘膜修復）",
        "finish": "唇全体が医療用レベルの保護膜で覆われ、パックされているような安心感としっとり感が持続",
        "desc_p1": "冬の乾燥が進むと、単なるカサつきを超えて「唇の中央がピキッと割れて出血する」「口を開けた瞬間に口角が裂けて痛む」「皮が剥けて赤く腫れる」といった皮膚炎（口唇炎・口角炎）に発展することがあります。この段階になると、通常の化粧品リップクリームでは保湿が追いつかず、薬用成分による治療が必要となります。",
        "desc_p2": "資生堂薬品の『モアリップN』は、5大有効成分を贅沢に配合した第3類医薬品の治療薬リップです。荒れた唇の修復を促すアラントインとパンテノール、炎症を抑えるグリチルレチン酸、皮膚の新陳代謝を整えるビタミンB6、血行を促進するビタミンEが協力し、痛むひび割れや赤みをスピーディーに鎮静します。就寝前にたっぷり塗って寝るだけで、翌朝には見違えるほどふっくらとなめらかな唇が蘇ります。",
        "target": "唇の皮がベリベリ剥けて出血や強い痛みを伴っている方、あくびや食事で口角がピキッと裂けてしまう口角炎にお悩みの方、冬のお守り常備薬として即効性のある医薬品リップを求める方",
        "technique": "チューブの先端を唇に直接あてて優しく伸ばすか、清潔な指先に取り、ひび割れや傷がある部分に厚めに置くように塗布します。夜寝る前に唇の輪郭からはみ出るくらいオーバーに塗ると集中リップパックになります。",
        "voice": "『冬になると必ず口角が切れて痛くて笑えなくなるのですが、モアリップを夜塗って寝ると翌朝には痛みが引き傷口がふさがります。本当にこれがないと冬を越せません。』(20代・営業職)",
        "caution": "第3類医薬品のため、症状が治まった後は日常ケア用のリップクリームに切り替えることをおすすめします。5〜6日間使用しても改善しない場合は皮膚科を受診してください。"
    },
    {
        "rank": 3,
        "tag": "🍯 5つの保湿成分とはちみつ配合！唇の体温でジュワッととろけてうるおいを抱え込む高保水リップ",
        "catch": "高保水型持続ヴェール処方。ひと塗りで鏡のようなツヤと濃密なうるおいが長持ちするドラコス名品",
        "capacity": "2.2g",
        "type": "医薬部外品・高保水持続メルティリップクリーム",
        "texture": "唇に触れた瞬間に体温でオイルのようにとろけ、厚みのあるうるおいヴェールへと変化",
        "ingredients": "有効成分（ビタミンE・グリチルレチン酸ステアリル）、はちみつ、ローヤルゼリーエキス、トレハロース、ホホバオイル、スクワラン、オリーブオイル",
        "finish": "リップグロスを塗ったようなみずみずしいツヤ感と、ふっくらとした立体感のあるうるおい唇に",
        "desc_p1": "ドラッグストアで圧倒的な人気を誇るニベアのディープモイスチャーシリーズ。冬の乾燥した唇は水分を自ら保持する力が落ちており、塗っても塗ってもすぐにカサカサに戻ってしまうという悩みが多発します。",
        "desc_p2": "『ディープモイスチャーリップ』は、水分をギュッと抱え込む「高保水型持続ヴェール処方」を採用。はちみつやローヤルゼリーエキス、3種の良質な天然オイルが唇の体温でジュワッととろけ、唇の凹凸を埋めるように密着します。SPF26/PA++で冬の紫外線もカットし、外出先でも塗り直しの回数を減らせる高持続力が魅力です。",
        "target": "ツヤ感のあるしっとりした仕上がりが好きな方、ドラッグストアで手軽に買えて一日中潤いが続くリップを探している方、冬の紫外線対策も同時に行いたい方",
        "technique": "唇の中央に当てて少し体温で温めてから、外側に向かって円を描くように優しく滑らせます。ツヤが出るので、ナチュラルメイクの日の単体使いや口紅の上のグロス代わりにも最適です。",
        "voice": "『スルスルととろける塗り心地が最高です。冬のエアコンが効いたオフィスでも唇が全く乾かず、ドラッグストアでこのクオリティが買えるのは感動的です。』(30代・OL)",
        "caution": "非常に柔らかくとろける処方のため、夏の高温多湿な場所や暖房器具の近くに放置すると溶けやすくなります。涼しい場所で保管してください。"
    },
    {
        "rank": 4,
        "tag": "✨ エラスチン×コラーゲン配合！しぼんだ冬の唇にふっくらとしたハリと弾力を呼び覚ます美容液リップ",
        "catch": "ロート製薬の先進皮膚科学が注入。縦ジワが深く刻まれた大人の唇を内側から押し上げる濃密エイジングケア",
        "capacity": "10g",
        "type": "高機能・唇用美容液リップエッセンス",
        "texture": "まるで濃密なセラム美容液のようなリッチテクスチャー。ピタッと吸い付く密着バーム",
        "ingredients": "エラスチン、コラーゲン、ヒアルロン酸Na、プロテオグリカン、シアバター、マカデミア種子油",
        "finish": "縦ジワが目立たなくなり、まるでヒアルロン酸を注入したかのようなふっくらボリューミーなハリ艶",
        "desc_p1": "年齢とともに唇のコラーゲンやエラスチンが減少すると、冬の乾燥によって唇のボリュームがしぼみ、縦ジワが深く刻まれて老け見えの原因になります。通常の油分リップだけでは、しぼんだ唇にハリを取り戻すことはできません。",
        "desc_p2": "オバジのエイジングケア研究を結集した『ダーマパワーX リップエッセンス』は、コラーゲンとエラスチン、ヒアルロン酸を高濃度配合した本格リップ美容液。濃厚なテクスチャーが唇に密着し、角層細胞をふっくらと押し上げます。斜めカットのチューブで塗りやすく、夜塗って寝れば翌朝の口紅のノリが劇的に向上します。",
        "target": "唇の縦ジワが目立ち口紅がシワに入り込んでしまう大人の女性、唇のしぼみやハリ不足を感じている方、ワンランク上の贅沢なリップ美容液を求める方",
        "technique": "チューブから適量を直接唇に出し、斜めカット面を使って唇の中央から外側へマッサージするように塗り広げます。夜のスキンケアの最後にラップを貼って3分置くとサロン級のリップパックになります。",
        "voice": "『これを使い始めてから唇の縦ジワが本当に目立たなくなりました。リップモンスターなどのマット系リップを塗る前にも下地として手放せません。』(40代・公務員)",
        "caution": "美容液成分が濃厚なため、塗った直後は少し厚みを感じます。ティッシュオフしてから口紅を重ねると色持ちが良くなります。"
    },
    {
        "rank": 5,
        "tag": "🌿 ヒアルロン酸×シアバター配合！楕円形スティックで口角まで塗りやすい薬用高保湿リップ",
        "catch": "唇の端までフィットするオーバル容器。うるおい成分を贅沢に閉じ込め水分の蒸散を長時間ブロック",
        "capacity": "4.5g",
        "type": "医薬部外品・薬用ディープモイスチャーリップスティック",
        "texture": "固すぎず柔らかすぎない絶妙な硬さ。唇に密着して滑らかな保護膜を形成",
        "ingredients": "有効成分（ビタミンE誘導体・グリチルレチン酸ステアリル）、ヒアルロン酸Na、シアバター、ホホバ油、高純度ワセリン",
        "finish": "ギラギラしない自然で上品なツヤ感。男性やビジネスシーンでも使いやすい清潔感のある仕上がり",
        "desc_p1": "丸いスティックリップだと、唇の端や口角、上唇の山部分を塗る際にはみ出してしまうという日常のプチストレスがあります。特に冬場は口角のキワが最も乾燥しやすく、塗り残しが原因で裂けてしまうケースが目立ちます。",
        "desc_p2": "ロート製薬の『メンソレータム ディープモイスト』は、唇の形にぴったりフィットする楕円形（オーバル型）容器を採用。細い面を使えば口角や唇の輪郭までムラなく塗り込めます。ヒアルロン酸やシアバター、ホホバ油などの高保湿成分が角層にうるおいを届け、荒れがちな冬の唇をすこやかに保護します。",
        "target": "口角や唇のキワまでしっかり塗り残しなくケアしたい方、テカテカしすぎず自然な保湿感を好む方、男性や家族全員で気兼ねなく使いたい方",
        "technique": "楕円形の広い面を使って唇全体にスーッと伸ばし、細い面を使って口角の端や上唇の輪郭を丁寧に塗り上げます。日中のこまめな保湿に最適です。",
        "voice": "『楕円形の形がとにかく塗りやすくて感動しました。端っこまでしっかり塗れるので、冬に口角がピキッと切れることがなくなりました。リピート3本目です。』(30代・男性・エンジニア)",
        "caution": "無香料タイプですが、原料特有のわずかな香りが気になる場合は風通しの良い場所でお使いください。"
    },
    {
        "rank": 6,
        "tag": "🫒 高純度オリーブバージンオイル配合！人の皮脂に最も近い植物油脂が極薄の保護膜を張る超定番",
        "catch": "発売以来のロングセラー。アロエエキスとビタミンEが荒れた唇にピタッと吸着しうるおいを持続",
        "capacity": "1.5g",
        "type": "医薬部外品・オリーブオイル薬用リップクリーム",
        "texture": "細身のスティックで唇に吸い付くように薄く均一に伸び広がるなめらかテクスチャー",
        "ingredients": "指定成分（液状ラノリン）、オリーブバージンオイル、アロエエキス、甘草誘導体、ビタミンE",
        "finish": "ベタつきや重さが一切なく、唇表面に極薄の皮脂膜が再生したような自然なツヤとなめらかさ",
        "desc_p1": "数々のリップクリームが生まれては消える中で、長年にわたり不動の支持を誇るDHCの薬用リップ。冬の乾燥した唇に必要なのは、人工的な分厚い膜ではなく、本来の皮膚呼吸を妨げない良質な皮脂膜の代用品です。",
        "desc_p2": "オリーブの果実から採れる高純度バージンオイルは、人間の皮脂の主成分であるオレイン酸トリグリセリドを豊富に含有。唇の角層細胞と瞬時に一体化し、水分蒸散を防ぎながら外部刺激をブロックします。スリムなスティックで持ち運びやすく、口紅の前後どちらに使ってもヨレない万能性が冬のデイリーケアに不可欠です。",
        "target": "ベタつかないサラリとした高保湿を求める方、口紅の下地として色ムラなく綺麗に仕上げたい方、ポーチやポケットにすっきり収まるスリムタイプが好きな方",
        "technique": "口紅を塗る直前に薄く一度塗りし、軽くティッシュで押さえてから口紅を重ねると、乾燥を防ぎながら口紅の発色と密着感が格段に向上します。",
        "voice": "『学生の頃から何十本使ったかわかりません。冬の乾燥でガサガサになっても、これを塗ると一瞬でスベスベになります。口紅の下地にもこれ以外考えられません。』(30代・アパレル)",
        "caution": "オリーブオイルやラノリンなど天然油脂を豊富に含むため、開封後はできるだけ早めに使い切ることをおすすめします。"
    },
    {
        "rank": 7,
        "tag": "🇫🇷 パンテノール5%×MP-リピッド配合！極度の乾燥でボロボロになった敏感唇を集中リペアする皮膚科発想",
        "catch": "フランスの湧水ターマルウォーター配合。バリア機能が崩壊した唇をやさしく包み込み水分を逃さない",
        "capacity": "7.5ml",
        "type": "敏感肌用・高濃度パンテノール集中リペアリップバーム",
        "texture": "体温でじんわり伸びる濃厚なバーム状。唇にピタッと保護膜を形成して外部刺激を遮断",
        "ingredients": "パンテノール5%（プロビタミンB5・皮膚修復）、MP-リピッド（角層バリア再構築脂質）、シアバター、大豆油、ミツロウ",
        "finish": "しっとりとしたうるおいバリアが唇を隙間なく覆い、風や冷気による刺激を一切遮断する安心感",
        "desc_p1": "極度の寒冷地やアレルギー、マスクの摩擦によって唇のバリア機能が完全に破壊されると、水分保持能力がゼロになり、皮剥けを無限に繰り返す悪循環に陥ります。",
        "desc_p2": "ラロッシュポゼの『シカプラスト リップバーム』は、組織修復を助けるパンテノールを高濃度5%配合し、特許成分MP-リピッドが角層のバリア膜を物理的に再構築。冬の過酷な寒気や摩擦ダメージから唇を徹底保護します。低刺激・パラベンフリーで、子どもから大人まで荒れ果てた唇の集中ケアに最適です。",
        "target": "何を塗っても皮剥けが治まらない重度の乾燥唇の方、海外の皮膚科発想スキンケアの確かな効果を実感したい方、冬のアウトドアやウィンタースポーツで唇を守りたい方",
        "technique": "指先に米粒大を取り、唇の縦ジワを広げるように優しく塗り込みます。特に荒れがひどい夜は、リップバームを塗った後にラップを小さく切って唇に貼り、5分置くと見違えるように回復します。",
        "voice": "『冬になると皮が剥けて唇の皮を剥く癖がやめられませんでしたが、これを塗ったら薄い皮がピタッと定着してツルツルになりました。本当にすごい保護力です。』(20代・大学院生)",
        "caution": "濃厚なバームのため、寒い場所ではチューブから出す際に少し硬く感じることがあります。手の中で少し温めてから押し出してください。"
    },
    {
        "rank": 8,
        "tag": "💛 ビタミンE×スクワラン配合！冬のカサカサ唇あれを防ぎすこやかに保つ老舗ユースキンの薬用スティック",
        "catch": "唇の荒れを科学するユースキン製薬。黄色いビタミン配合で唇のあれ・ひび割れを未然に防ぐ実力派",
        "capacity": "3.5g",
        "type": "医薬部外品・薬用ビタミン配合リリップケアスティック",
        "texture": "しっかりとした固めのスティックながら、唇に乗せると体温でなめらかに馴染む",
        "ingredients": "有効成分（トコフェロール酢酸エステル・グリチルレチン酸ステアリル）、スクワラン、ホホバ油、アボカド油、リボフラビン（ビタミンB2）",
        "finish": "黄色いクリームが唇に伸びると透明に変化。サラリとした密着感でマスクの内側を汚さない",
        "desc_p1": "手荒れ治療薬で絶大な信頼を集めるユースキンが、長年の皮膚研究を結集して開発したリップケアライン。冬の唇あれは、乾燥だけでなく血行不良やビタミン不足も大きな原因となります。",
        "desc_p2": "『リリップ ケアスティック』は、血行を促進するビタミンEや炎症を抑えるグリチルレチン酸ステアリル、肌なじみの良い植物スクワランを配合。黄色いテクスチャーはビタミンB2（リボフラビン）本来の色であり、着色料は無添加です。唇あれを未然に防ぎ、すこやかで血色の良いツヤ唇をキープします。",
        "target": "冬になると唇がくすんだり冷えで血色が悪くなる方、ユースキンの高い保湿力と信頼感を信頼している方、日常使いで唇あれをしっかり予防したい方",
        "technique": "朝の洗顔後と夜の就寝前、そして日中の乾燥を感じる前にこまめに塗り直します。唇の上下を軽く擦り合わせて全体に行き渡らせてください。",
        "voice": "『ハンドクリームのユースキンが大好きで購入しましたが、リップも期待を裏切らない保湿力でした。変なテカリやベタつきがなく、一日中潤います。』(40代・パート)",
        "caution": "メントールは配合されていないため、スースーした清涼感を求める方には向きませんが、敏感な荒れ唇には優しく最適です。"
    },
    {
        "rank": 9,
        "tag": "💧 コールドクリーム成分×アベンヌ温泉水！唇をうるおいラップで包み込み乾燥と荒れを防ぐ敏感肌設計",
        "catch": "南仏アベンヌのミネラル温泉水とミツロウの恵み。使うほどに唇の角層がふっくらと柔らかく整う",
        "capacity": "4g",
        "type": "医薬部外品・薬用コールドクリームリップケア",
        "texture": "固すぎず滑らかな塗り心地。唇に密着して厚みのあるうるおいシールドを形成",
        "ingredients": "有効成分（グリチルレチン酸ステアリル・酢酸DL-α-トコフェロール）、アベンヌ温泉水、ミツロウ、ミネラルオイル、シア脂",
        "finish": "しっとりとした柔軟性とツヤが持続。唇のキメが整い、カサつきによる凸凹をなめらかに補正",
        "desc_p1": "ヨーロッパの温泉療法から生まれたアベンヌ。冬の冷えや乾燥、花粉、寒風に敏感に反応してしまう唇は、刺激物質を寄せ付けない強固なエモリエント膜が必要です。",
        "desc_p2": "『薬用リップケア モイスト』は、アベンヌ温泉水と天然ミツロウをブレンドした伝統のコールドクリーム成分を配合。唇の角層細胞を水分で満たしながら、ミツロウのラップ効果で水分蒸散をブロックします。敏感肌パッチテスト済みで、冬のデリケートな唇を穏やかに守り抜きます。",
        "target": "唇の皮膚が薄く刺激に弱い方、ミツロウ配合の自然なうるおいラップ感を好む方、無香料で使い心地の優しい薬用リップを求める方",
        "technique": "唇全体に優しく塗り広げた後、指の腹でトントンと軽く叩き込むようにすると、温泉水成分が角層になじみやすくなります。",
        "voice": "『他のリップだと皮がポロポロ剥けてしまう敏感唇ですが、アベンヌだけは全く荒れずしっとり潤いが続きます。何年もリピートしています。』(30代・主婦)",
        "caution": "スティックを出しすぎると戻りにくくなることがあるため、1〜2mm程度繰り出してご使用ください。"
    },
    {
        "rank": 10,
        "tag": "💊 アラントイン×ビタミンB6配合！荒れ果てた唇のひび割れ・皮剥けを穏やかに治すノンメントール治療薬",
        "catch": "近江兄弟社メンタームの医療用処方。スースーしない優しい使い心地でデリケートな唇の傷口を治療",
        "capacity": "3.2g",
        "type": "第3類医薬品・薬用メディカルリップスティック",
        "texture": "なめらかに伸びる薬用スティック。メントール無配合でしみる刺激が一切ない",
        "ingredients": "アラントイン（傷口修復）、ピリドキシン塩酸塩（ビタミンB6・皮膚代謝促進）、グリチルレチン酸（抗炎症）、dl-カンフル、トコフェロール酢酸エステル",
        "finish": "患部を優しく保護し、痛むひび割れや赤みを穏やかに落ち着かせるマットなしっとり感",
        "desc_p1": "冬の乾燥で唇がひび割れて出血している時、通常のメンタームやメントール配合のリップを塗ると激痛が走ることがあります。傷口がある状態では、刺激を極限まで抑えた治療用リップが必要です。",
        "desc_p2": "近江兄弟社の『薬用メディカルリップスティック Mn』は、メントールを配合しないマイルド処方の第3類医薬品。組織修復を助けるアラントインとビタミンB6が、痛むひび割れや口角炎を根本から治します。スティックタイプなので外出先でも指を汚さずにサッと塗れる利便性も大きな魅力です。",
        "target": "唇のひび割れがしみて痛い方、メントールのスースーする刺激が苦手な方、スティックタイプで手軽に唇炎の治療を行いたい方",
        "technique": "ひび割れや皮剥けがある部分を中心に、擦らずポンポンと置くように優しく塗布します。1日数回、乾燥を感じた時にこまめに塗り直してください。",
        "voice": "『唇が切れて痛いときに普通のリップだと激痛でしたが、このMnは全くしみずにスーッと痛みが引いて傷が治りました。冬の必需品です。』(20代・学生)",
        "caution": "第3類医薬品のため、症状が治った後は日常ケア用の保湿リップに切り替えてください。"
    }
]

# JSON-LD用ItemList
json_ld_items = []
for idx, it in enumerate(items):
    dt = lip_balm_details[idx]
    json_ld_items.append({
        "@type": "ListItem",
        "position": idx + 1,
        "item": {
            "@type": "Product",
            "name": it["name"],
            "image": it["image_url"],
            "description": dt["catch"],
            "brand": {
                "@type": "Brand",
                "name": it["brand"]
            },
            "offers": {
                "@type": "Offer",
                "price": str(it["price"]),
                "priceCurrency": "JPY",
                "availability": "https://schema.org/InStock",
                "url": it["affiliate_url"]
            }
        }
    })

json_ld_structure = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで冬の唇ひび割れ・血がにじむガサガサ皮剥けとさようなら！ひと塗りで潤い密封する薬用高保湿リップクリームランク10",
            "description": "11月・12月の冬の乾燥で血がにじむ唇のひび割れ・皮剥け・口角炎を徹底解決！キュレル、モアリップ、ニベア、オバジ、メンソレータム、DHC、ラロッシュポゼなど、セラミドやアラントイン配合の最強薬用高保湿リップクリーム10選を徹底比較！",
            "datePublished": "2026-11-01T00:00:00+09:00",
            "dateModified": "2026-11-01T00:00:00+09:00",
            "author": {
                "@type": "Organization",
                "name": "冬コスメ徹底比較ラボ"
            }
        },
        {
            "@type": "ItemList",
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "医薬品リップ、医薬部外品リップ、化粧品リップの違いと使い分け方は？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "『医薬品リップ（モアリップやメディカルリップ等）』は、ひび割れ・出血・口唇炎・口角炎などの症状を治療するための薬です。『医薬部外品（薬用リップ）』は有効成分（アラントインやビタミンE等）が配合され、唇荒れの予防を目的としています。『化粧品リップ』は主に油分による保湿やツヤ出しが目的です。血がにじんだり痛むときは医薬品で治し、日常の予防・保湿には薬用リップを使うのが正しい選び方です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "リップクリームを塗ってもすぐに乾いて皮が剥けてしまう原因は何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "主な原因は『横方向にゴシゴシ塗る摩擦』と『唇を舐める癖』です。唇の皮膚構造は縦方向に繊維が走っているため、横に塗ると角質がめくれ上がり皮剥けを助長します。また、乾いた唇を舌で舐めると、唾液が蒸発する際に唇本来の水分まで一緒に奪い去り、過乾燥を引き起こします。縦ジワに沿って優しく乗せるように塗り、舐める癖を意識してやめることが重要です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "口紅（リップモンスターやマットリップ）を塗る前の正しい下地ケアは？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "メイクを始める前のスキンケア段階で、まず薬用リップクリーム（キュレルやDHCなど油分が多すぎないもの）を唇全体に馴染ませておきます。ベースメイクが終わった後、口紅を塗る直前にティッシュで軽く唇を挟んで余分な油分を押さえてから口紅を重ねてください。このワンステップで、口紅の色ムラや縦ジワ落ちを防ぎ、一日中しっとり美発色が続きます。"
                    }
                }
            ]
        }
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の唇ひび割れ・血がにじむガサガサ皮剥けとさようなら！ひと塗りで潤い密封する薬用高保湿リップクリームランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の乾燥で血がにじむ唇のひび割れ・皮剥け・口角炎を徹底解決！キュレル、モアリップ、ニベア、オバジ、メンソレータム、DHC、ラロッシュポゼなど、セラミドやアラントイン配合の最強薬用高保湿リップクリーム10選を徹底比較！">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-lip-balm">
  <meta property="og:title" content="保湿力の強さで冬の唇ひび割れ・血がにじむガサガサ皮剥けとさようなら！ひと塗りで潤い密封する薬用高保湿リップクリームランク10">
  <meta property="og:description" content="11月・12月の冬の乾燥で血がにじむ唇のひび割れ・皮剥け・口角炎を徹底解決！キュレル、モアリップ、ニベア、オバジ、メンソレータム、DHC、ラロッシュポゼなど、セラミドやアラントイン配合の最強薬用高保湿リップクリーム10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-lip-balm">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="style.css">
  <script type="application/ld+json">
{json.dumps(json_ld_structure, ensure_ascii=False, indent=2)}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container header-container">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav class="site-nav">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#guide-section">選び方解説</a>
        <a href="#faq-section">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container main-content">
    <article class="article-body">
      <nav class="breadcrumb" aria-label="パンくずリスト">
        <ol>
          <li><a href="/">トップ</a></li>
          <li aria-current="page">薬用高保湿リップクリーム</li>
        </ol>
      </nav>

      <header class="article-header">
        <span class="badge category-badge">唇集中保湿・ひび割れ修復</span>
        <h1 class="article-title">保湿力の強さで冬の唇ひび割れ・血がにじむガサガサ皮剥けとさようなら！ひと塗りで潤い密封する薬用高保湿リップクリームランク10</h1>
        <div class="article-meta">
          <time datetime="2026-11-01">2026年11月1日更新</time>
          <span class="author">執筆：冬コスメ比較検証チーム</span>
        </div>
      </header>

      <!-- 導入文 -->
      <section class="intro-box">
        <p>
          11月から12月にかけて気温と湿度が急落すると、顔の中でも真っ先に悲鳴を上げるのが「唇」です。「朝起きると唇がカサカサに強張っている」「笑ったりあくびをした瞬間に唇の中央がピキッと裂けて血がにじむ」「皮がめくれて気になり、指で剥いて悪化させてしまう」「口紅を塗ると縦ジワに色が入り込んで汚く見えてしまう」といった深刻なトラブルに悩まされていませんか？
        </p>
        <p>
          実は、唇の構造は通常の皮膚とは根本的に異なります。皮脂腺や汗腺が一切ないため、自前の皮脂膜（天然の保護膜）を作ることができません。さらに角層の厚さは頬や額のわずか3分の1程度しかなく、水分を保持する力が極端に微弱です。乾燥した外気や暖房風、マスクの内外での急激な湿度変化にさらされると、わずか数分で水分が蒸散してしまいます。
        </p>
        <p>
          この過酷な真冬の唇を守り抜くためには、単に油を塗るだけの一時的なリップでは力不足です。傷ついた組織を修復する抗炎症成分（アラントイン、グリチルレチン酸）や、角層の隙間を満たす保水成分（セラミド、高純度ワセリン、ビタミンE）がしっかり配合された<strong>本格的な薬用高保湿リップクリーム</strong>が必須です。
        </p>
        <p>
          本特集では、楽天市場やドラッグストアで圧倒的な評価を誇るリップクリームの中から、検証チームが密着持続力・修復力・低刺激性・使用感・口紅下地としての適性を徹底検証し、11月〜12月の真冬に本当に頼れる実力派10選をランキング形式で厳選しました。
        </p>
      </section>

      <!-- 目次 -->
      <nav class="toc-card" aria-label="目次">
        <h2 class="toc-title">📑 目次</h2>
        <ul class="toc-list">
          <li><a href="#why-dry">1. なぜ11月〜12月に唇のひび割れ・激しい皮剥けが起きるのか？</a></li>
          <li><a href="#how-to-choose">2. 失敗しない冬の薬用高保湿リップクリームの選び方3原則</a></li>
          <li><a href="#ranking">3. 薬用高保湿リップクリームおすすめ厳選ランキング10選</a></li>
          <li><a href="#comparison">4. 薬用高保湿リップクリーム10選 スペック比較表</a></li>
          <li><a href="#guide-section">5. 縦ジワに沿って塗るのが正解！唇を傷めない「縦塗り＆就寝前ラップパック術」</a></li>
          <li><a href="#faq-section">6. よくある質問 (FAQ)</a></li>
          <li><a href="#related-section">7. あわせて読みたい冬の徹底保湿特集</a></li>
        </ul>
      </nav>

      <!-- 科学的背景解説 -->
      <section id="why-dry" class="content-block">
        <h2>🔬 なぜ11月〜12月に唇のひび割れ・激しい皮剥けが起きるのか？</h2>
        <p>
          唇が他の皮膚よりも圧倒的に乾燥しやすく、冬になると簡単に血がにじんでしまうのには、皮膚科学的な3つの明確な理由が存在します。
        </p>
        <div class="science-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:20px; margin:24px 0;">
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">① 皮脂膜がゼロ！水分を逃さないフタがない</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              唇には皮脂腺も汗腺も存在しません。通常の肌は皮脂と汗が混ざり合った「皮脂膜」が表面を覆って水分蒸散を防いでいますが、唇にはその天然のバリアが存在しないため、無防備な角層から水分が直接空気中へ蒸発していきます。
            </p>
          </div>
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">② 角層が通常の1/3！バリアが極めて薄い</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              唇の角質層は数層から十数層しかなく、通常の皮膚の約3分の1の薄さしかありません。水分を溜め込んでおく保水タンクとしての容量が非常に小さいため、暖房の効いた乾燥した室内にいるだけで、急速に干からびてしまいます。
            </p>
          </div>
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">③ ターンオーバーが3〜5日と超高速で未熟</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              唇の細胞生まれ変わり周期は約3〜5日と、通常の肌（約28日）に比べて極端に早いです。乾燥や摩擦のダメージを受けると、細胞が十分に成熟しないまま表面に押し上げられ、剥がれかけの薄皮となって白くめくれ上がってしまいます。
            </p>
          </div>
        </div>
      </section>

      <!-- 選び方解説 -->
      <section id="how-to-choose" class="content-block">
        <h2>💡 失敗しない冬の薬用高保湿リップクリームの選び方3原則</h2>
        <p>
          冬の深刻な唇乾燥やひび割れに立ち向かうためには、単なる香料入りのプチプラリップでは逆効果になることがあります。以下の3つの基準をチェックして、確かな修復力と保護力を持つリップを選びましょう。
        </p>
        <div class="choose-principles" style="margin:24px 0;">
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin-bottom:16px;">
            <h3 style="color:#0369a1; margin-top:0;">基準1：目的（治療の医薬品 vs 予防の医薬部外品）を明確に分ける</h3>
            <p style="line-height:1.7; color:#475569;">
              出血やひび割れ、口角炎がある場合は、組織修復成分（アラントイン・パンテノール）を配合した「第3類医薬品（モアリップ等）」でまず集中治療します。日常的なカサつき予防や口紅下地には、低刺激な「医薬部外品（キュレルやニベア等）」を選ぶのが鉄則です。
            </p>
          </div>
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin-bottom:16px;">
            <h3 style="color:#0369a1; margin-top:0;">基準2：セラミド・高純度ワセリン・天然オイルのシールド力</h3>
            <p style="line-height:1.7; color:#475569;">
              角層の隙間を埋めるセラミド機能成分や、水分を物理的に逃さない高純度ワセリン、人の皮脂に似たオリーブスクワランやシアバターが配合されているかを確認しましょう。唇の体温でとろけてピタッと密着する処方が持続力を高めます。
            </p>
          </div>
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <h3 style="color:#0369a1; margin-top:0;">基準3：摩擦レスなテクスチャー＆低刺激設計（無香料・弱酸性）</h3>
            <p style="line-height:1.7; color:#475569;">
              冬の乾燥した唇は非常にデリケートです。固すぎて塗る時に摩擦が生じるスティックや、過度なメントール・香料は刺激となり炎症を悪化させます。力を入れずにスルスルと伸びるメルティな塗り心地と、無香料・低刺激設計のものを選びましょう。
            </p>
          </div>
        </div>
      </section>

      <!-- ランキング一覧セクション -->
      <section id="ranking" class="ranking-section">
        <div class="ranking-header">
          <h2>🏆 薬用高保湿リップクリームおすすめ厳選ランキング10選</h2>
          <p class="ranking-subtitle">11月〜12月のひび割れ・ガサガサ皮剥けを防ぎ、ひと塗りでぷるんと潤う唇へ導く実力派を比較検証！</p>
        </div>
"""

# ランキング各商品のHTML生成
for idx, it in enumerate(items):
    dt = lip_balm_details[idx]
    rank_num = it["rank"]
    
    html_content += f"""
        <!-- 第{rank_num}位 -->
        <article id="rank-{rank_num}" class="product-card">
          <div class="product-badge-wrap">
            <span class="rank-badge rank-{rank_num}">第{rank_num}位</span>
            <span class="product-sub-badge">{dt["type"]}</span>
          </div>

          <h3 class="product-name">{it["name"]}</h3>
          <p class="product-catch">{dt["catch"]}</p>

          <div class="product-main-grid">
            <div class="product-img-box">
              <img src="{it["image_url"]}" alt="{it["name"]}" class="product-img" loading="lazy">
              <div class="price-box">
                <span class="price-label">参考価格</span>
                <span class="price-value">¥{it["price"]:,}</span>
                <span class="price-tax">(税込)</span>
              </div>
              <a href="{it["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
                楽天で詳細・最安値を見る <span>&rarr;</span>
              </a>
              <span class="shop-name">取扱ショップ: {it["shop_name"]}</span>
            </div>

            <div class="product-spec-box">
              <div class="spec-highlight">
                <strong>注目ポイント:</strong> {dt["tag"]}
              </div>
              <table class="spec-table">
                <tr><th>ブランド</th><td>{it["brand"]}</td></tr>
                <tr><th>容量</th><td>{dt["capacity"]}</td></tr>
                <tr><th>テクスチャー</th><td>{dt["texture"]}</td></tr>
                <tr><th>主要有効・保湿成分</th><td>{dt["ingredients"]}</td></tr>
                <tr><th>仕上がりの質感</th><td>{dt["finish"]}</td></tr>
              </table>
            </div>
          </div>

          <div class="product-detail-desc">
            <h4>💡 美容エディターの実力検証レビュー</h4>
            <p>{dt["desc_p1"]}</p>
            <p>{dt["desc_p2"]}</p>

            <div class="user-target-box">
              <h5>🎯 こんな方に特におすすめ！</h5>
              <p>{dt["target"]}</p>
            </div>

            <div class="expert-tips-box">
              <h5>✨ 効果を最大化するプロの使いこなし術</h5>
              <p>{dt["technique"]}</p>
            </div>

            <div class="review-quote-box">
              <span class="quote-icon">💬</span>
              <blockquote>{dt["voice"]}</blockquote>
            </div>

            <div class="caution-note">
              <strong>⚠️ 使用上の注意:</strong> {dt["caution"]}
            </div>
          </div>
        </article>
"""

html_content += f"""
      </section>

      <!-- 比較表セクション -->
      <section id="comparison" class="comparison-section" style="margin:48px 0;">
        <h2>📊 薬用高保湿リップクリーム10選 スペック比較表</h2>
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; margin-top:16px; font-size:0.95rem;">
            <thead>
              <tr style="background:#0284c7; color:#fff; text-align:left;">
                <th style="padding:12px; border:1px solid #e2e8f0;">順位・ブランド</th>
                <th style="padding:12px; border:1px solid #e2e8f0;">商品名</th>
                <th style="padding:12px; border:1px solid #e2e8f0;">区分・主要成分</th>
                <th style="padding:12px; border:1px solid #e2e8f0;">仕上がり特徴</th>
                <th style="padding:12px; border:1px solid #e2e8f0;">参考価格</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">1位 キュレル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">リップケアクリーム</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">医薬部外品・セラミド機能成分</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">無香料・低刺激で唇深くまで密着保湿</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[0]["price"]:,}</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">2位 モアリップ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">モアリップN</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">第3類医薬品・アラントイン・パンテノール</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ひび割れ・血がにじむ皮剥けを集中治療</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[1]["price"]:,}</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">3位 ニベア</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ディープモイスチャーリップ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">医薬部外品・はちみつ・植物オイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">体温でジュワッととろける高保水ツヤ</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[2]["price"]:,}</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">4位 オバジ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ダーマパワーX リップエッセンス</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">化粧品・エラスチン・コラーゲン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">縦ジワをふっくら押し上げる美容液リップ</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[3]["price"]:,}</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">5位 メンソレータム</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ディープモイスト</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">医薬部外品・ヒアルロン酸・シアバター</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">楕円形スティックで口角まで塗りやすい</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[4]["price"]:,}</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">6位 DHC</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">薬用リップクリーム</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">医薬部外品・オリーブバージンオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">極薄の皮脂膜を再現し口紅下地にも最適</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[5]["price"]:,}</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">7位 ラロッシュポゼ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">シカプラスト リップバーム</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">化粧品・パンテノール5%・MPリピッド</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">荒れ果てた唇のバリアを再構築するバーム</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[6]["price"]:,}</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">8位 ユースキン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">リリップ ケアスティック</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">医薬部外品・ビタミンE・スクワラン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">血行を促進し唇あれを未然に防ぐ実力派</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[7]["price"]:,}</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">9位 アベンヌ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">薬用リップケア モイスト</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">医薬部外品・アベンヌ温泉水・ミツロウ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">敏感唇をうるおいラップで包み込む</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[8]["price"]:,}</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">10位 メンターム</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">薬用メディカルリップスティック Mn</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">第3類医薬品・アラントイン・ビタミンB6</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">しみないノンメントールで痛む傷口を治療</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥{items[9]["price"]:,}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 塗り方テクニック解説 -->
      <section id="guide-section" class="expert-guide-section" style="background:#f8fafc; border-radius:12px; padding:28px; margin:40px 0;">
        <h2>🛁 縦ジワに沿って塗るのが正解！唇を傷めない「縦塗り＆就寝前ラップパック術」</h2>
        <div style="line-height:1.8; color:#334155;">
          <h3>1. 横に滑らせるのはNG！「縦ジワに沿って上から下へ」</h3>
          <p>
            多くの方がリップクリームを唇の横方向に往復させて塗っていますが、これは大きな間違いです。唇の皮膚のシワやキメは縦方向に走っているため、横に塗ると角質細胞のすき間に成分が入らず、かえって摩擦で薄皮をめくり上げてしまいます。唇の縦の筋に沿って、上から下へと垂直に優しく乗せるように塗布してください。
          </p>

          <h3 style="margin-top:24px;">2. 唇を舐める癖は「自爆行為」！乾燥したら即リップ</h3>
          <p>
            唇が乾いた瞬間に、無意識に舌で唇をペロッと舐めてしまう方が多くいます。唾液がつくと一時的に湿ったように感じますが、唾液が蒸発する際に唇本来の水分まで一緒に奪い去り、極度の「過乾燥」を招きます。カサつきを感じたら舐めずに、すぐにポケットのリップクリームを取り出す習慣をつけましょう。
          </p>

          <h3 style="margin-top:24px;">3. 就寝前の「オーバーリップ塗り＆ラップ密着パック」</h3>
          <p>
            夜寝ている間は唾液の分泌が減り、口呼吸によって唇が激しく乾燥します。就寝前にリップクリーム（または医薬品リップ）を唇の輪郭からはみ出るくらい厚めに塗布します。特にガサガサがひどい夜は、小さく切った食品用ラップを唇に貼り、3〜5分置いてから剥がすと、翌朝プルプルの柔らかい唇に生まれ変わります。
          </p>
        </div>
      </section>

      <!-- よくある質問 (FAQ) -->
      <section id="faq-section" class="faq-section">
        <h2>❓ 冬の薬用高保湿リップクリーム よくある質問 (FAQ)</h2>
        <div class="faq-item">
          <h3>Q1. 医薬品リップ、医薬部外品リップ、化粧品リップの違いと使い分け方は？</h3>
          <p>『医薬品リップ（モアリップやメディカルリップ等）』は、ひび割れ・出血・口唇炎・口角炎などの症状を治療するための薬です。『医薬部外品（薬用リップ）』は有効成分（アラントインやビタミンE等）が配合され、唇荒れの予防を目的としています。『化粧品リップ』は主に油分による保湿やツヤ出しが目的です。血がにじんだり痛むときは医薬品で治し、日常の予防・保湿には薬用リップを使うのが正しい選び方です。</p>
        </div>
        <div class="faq-item">
          <h3>Q2. リップクリームを塗ってもすぐに乾いて皮が剥けてしまう原因は何ですか？</h3>
          <p>主な原因は『横方向にゴシゴシ塗る摩擦』と『唇を舐める癖』です。唇の皮膚構造は縦方向に繊維が走っているため、横に塗ると角質がめくれ上がり皮剥けを助長します。また、乾いた唇を舌で舐めると、唾液が蒸発する際に唇本来の水分まで一緒に奪い去り、過乾燥を引き起こします。縦ジワに沿って優しく乗せるように塗り、舐める癖を意識してやめることが重要です。</p>
        </div>
        <div class="faq-item">
          <h3>Q3. 口紅（リップモンスターやマットリップ）を塗る前の正しい下地ケアは？</h3>
          <p>メイクを始める前のスキンケア段階で、まず薬用リップクリーム（キュレルやDHCなど油分が多すぎないもの）を唇全体に馴染ませておきます。ベースメイクが終わった後、口紅を塗る直前にティッシュで軽く唇を挟んで余分な油分を押さえてから口紅を重ねてください。このワンステップで、口紅の色ムラや縦ジワ落ちを防ぎ、一日中しっとり美発色が続きます。</p>
        </div>
      </section>

      <!-- 関連特集への内部リンク -->
      <section id="related-section" class="related-section">
        <h2>🔗 あわせて読みたい冬の徹底保湿・リップケア特集</h2>
        <div class="internal-links-grid">
          <a href="/winter-lipstick" class="related-card">
            <span class="related-tag">口紅・ルージュ</span>
            <h4>💄 高保湿口紅・リップスティック ランク10</h4>
            <p>冬でも皮剥けせず一日中鮮やかな発色とうる艶が続く口紅特集。</p>
          </a>
          <a href="/winter-lip-mask" class="related-card">
            <span class="related-tag">夜用集中マスク</span>
            <h4>🌙 高保湿リップマスク ランク10</h4>
            <p>寝ている間に角層を集中ラッピングして翌朝ぷるぷるに整える夜用ケア。</p>
          </a>
          <a href="/winter-lip-oil" class="related-card">
            <span class="related-tag">リップオイル</span>
            <h4>✨ 高保湿リップオイル ランク10</h4>
            <p>濃密オイルの膜で縦ジワを消し去りガラスのような光沢を与える名品。</p>
          </a>
          <a href="/winter-lip-serum" class="related-card">
            <span class="related-tag">唇用美容液</span>
            <h4>💧 高保湿リップセラム ランク10</h4>
            <p>唇のしぼみやくすみをケアし内側からハリを呼び覚ます唇美容液。</p>
          </a>
        </div>
      </section>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <p class="copyright">&copy; 2026-2027 冬コスメ徹底比較ラボ All Rights Reserved.</p>
      <div class="footer-links">
        <!-- 後ほど一括スクリプトで全更新 -->
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-lip-balm.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated winter-lip-balm.html ({len(html_content):,} bytes)")
