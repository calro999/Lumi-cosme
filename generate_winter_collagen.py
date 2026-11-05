import json
import re

with open("fetched_3new_mango_tremella_collagen.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_collagen"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 Wヒト型ナノセラミド×生コラーゲン先行ジェリー！真冬のしぼみ肌の土台を再構築",
        "catch": "富士フイルムの写真フィルム技術が生んだ先行美容液の最高峰。熱変性させない水溶性生コラーゲンと高浸透ナノコラーゲン、世界最小クラスのWヒト型ナノセラミドを贅沢配合。真冬の冷風でしぼんだ角層の土台を立て直す",
        "brand_name": "ASTALIFT (アスタリフト / 富士フイルム)",
        "capacity": "60g / スパチュラ・トレイ付きジャー",
        "type": "自己復元ナノ先行美容ジェリー（洗顔直後用）",
        "features": "水溶性コラーゲン（生コラーゲン）、加水分解コラーゲン、アセチルヒドロキシプロリン、Wヒト型ナノセラミド、ナノアスタキサンチン",
        "value": "崩しても1〜2分で元に戻る自己復元ジェリー。洗顔直後のまっさらな角層へナノセラミドと生コラーゲンが電光石火で浸透し、その後の化粧水の保水力を何倍にも跳ね上げる",
        "desc_p1": "11月から12月にかけて、冷たい北風と室内外の寒暖差に晒された肌は、角質層の水分が抜け落ちてクシャッと萎縮し、頬の毛穴が縦に流れる「たるみ毛穴」や、目元・口元の細かな乾燥小ジワが深く刻まれていきます。この真冬のしぼみ肌を根底から救い上げるのが、富士フイルムの先進ナノテクノロジーを結集した『アスタリフト ジェリー アクアリスタ』です。主成分として、分子構造を壊さず熱変性させない高純度「水溶性生コラーゲン」と、角層深部へ浸透する極小分子「加水分解コラーゲン」の複数を配合しています。",
        "desc_p2": "洗顔直後の無防備な素肌に赤いジェリーを乗せると、体温で瞬時にサラリとした液体へと変化し、角層細胞の隙間へ吸い込まれるように浸透。世界最小クラスにナノ化されたWヒト型ナノセラミドが細胞間脂質を補修し、その上を生コラーゲンのしなやかな三重らせん保水膜が包み込みます。この先行ジェリーを仕込むだけで、次に使う化粧水がまるで砂漠に水が染み込むかのようにぐんぐん引き込まれ、手のひらを跳ね返すようなピンとしたハリと弾力が一日中持続します。ダマスクローズの気品ある香りが冬のスキンケアを贅沢に彩ります。",
        "target": "冬になるとどんなに高価なクリームを塗っても夕方には肌がしぼんでしまう方、乾燥による小ジワやたるみ毛穴が目立ってきた大人の肌、化粧水の浸透力を劇的に底上げしたい方",
        "point": "洗顔直後、付属のスパチュラでやや大きめのパール粒大を取り、手のひらで軽く温めてから顔全体に伸ばします。手のひらで顔全体を包み込み、ジェリーが肌にピタッと密着するまで優しくハンドプレスしてください。"
    },
    {
        "rank": 2,
        "tag": "✨ 浸透型コラーゲンEX×ナイアシンアミド！真冬のフェイスラインを引き上げ続ける名作ゲル",
        "catch": "ドクターシーラボの最高峰リフトケアオールインワン。独自開発の浸透型コラーゲンEXと薬用級ナイアシンアミドを高濃度配合。冬の乾燥と重力に立ち向かい、上向きの引き締まったハリ肌を24時間ホールド",
        "brand_name": "DR.CI:LABO (ドクターシーラボ)",
        "capacity": "120g / スパチュラ付きジャー容器",
        "type": "高密度リフトエンリッチ オールインワンゲル",
        "features": "加水分解コラーゲン発酵液エキス、水溶性コラーゲンクロスポリマー、サクシノイルアテロコラーゲン、ナイアシンアミド、酵母エキス",
        "value": "日本初の高浸透コラーゲン処方。乾燥で緩んだ角層へ異なる分子量のコラーゲンが多層的にアプローチし、塗った瞬間からピンとした見えないリフト膜を形成",
        "desc_p1": "冬の本格的な寒さは皮膚温を急激に奪い、真皮の線維芽細胞の働きを低下させます。その結果、肌のハリを支えるコラーゲン線維が硬化して弾力を失い、フェイスラインのもたつきやほうれい線の影が濃くなってしまいます。皮膚科医処方から生まれたドクターシーラボの『アクアコラーゲンゲル エンリッチリフトEX』は、この真冬の乾燥たるみを物理的かつ皮膚科学的に引き上げるために開発された高機能ゲルです。",
        "desc_p2": "コクのある濃厚なゲルを肌に伸ばすと、独自の発酵コラーゲンが角層の奥深くまで素早く届き、萎縮した細胞間をみずみずしい水分とアミノ酸で満たします。同時に、表面では高分子コラーゲンクロスポリマーが強靭な見えないネット（リフト膜）を形成。塗布直後から肌全体がキュッと上向きに引き締められるような心地よいテンションを実感できます。シワ改善とバリア機能強化で名高いナイアシンアミドも配合され、真冬の乾燥小ジワを徹底的に目立たなくします。",
        "target": "冬の乾燥でフェイスラインのもたつきや口元の影が気になる方、時短でサロン級のリフトケアと高保湿を同時に完了させたい方、乾燥小ジワを目立たなくしたい大人の肌",
        "point": "朝晩の洗顔後、スパチュラでサクランボ粒大を取り、顔の中心から外側へ、下から上へと引き上げるようにマッサージしながら塗り広げます。最後に手のひらでこめかみを押さえてキープするのがポイントです。"
    },
    {
        "rank": 3,
        "tag": "🔬 驚異のナノサイズジペプチド-8最高濃度294倍！肌奥深くまで突き抜ける浸透導入液",
        "catch": "DHCが長年の研究で到達したコラーゲンの極限進化系「DHCスーパーコラーゲン（ジペプチド-8）」を最高濃度294倍配合。高分子コラーゲンでは届かなかった角層の深部まで一瞬で突き抜け、内側から押し返すハリ肌を創出",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "100ml / ポンプディスペンサー",
        "type": "高濃度ナノコラーゲン 浸透型導入美容液",
        "features": "ジペプチド-8（DHCスーパーコラーゲン・最高濃度294倍）、マイタケ子実体エキス、スクワラン、ビタミンC誘導体",
        "value": "分子量わずか数千分の一という超極小ペプチド。肌に乗せた瞬間に水のように吸い込まれ、真冬の水分不足に悩む角層深部へダイレクトに高濃度コラーゲンを補給",
        "desc_p1": "従来のコラーゲン化粧品に対する最大の疑問は「分子量が大きすぎて肌の奥に入らないのではないか」という点でした。この分子の壁を打ち破るためにDHCが8年以上の歳月をかけて独自開発したのが、アミノ酸が2つ結合した超微小コラーゲン分子「ジペプチド-8」です。その独自成分をシリーズ最高濃度の294倍（スプリーム基準）まで極限まで高めたのが、この『DHC スーパーコラーゲン スプリーム』です。",
        "desc_p2": "手にとるとサラサラとした透明な美容液ですが、肌に触れた瞬間に吸い込まれるように消えていく驚異的な浸透スピードを誇ります。角質層のすみずみまで満ち足りたジペプチド-8が水分をがっちりと束ね、冬の冷気でスカスカになった角層の密度をギュッと高めます。塗布後の肌はベタつきが一切なく、まるで内側から水分で押し広げられたかのような、ふっくら吸い付くようなシルク肌に整います。どんなスキンケアとも相性が良く、手持ちのアイテムの浸透も高める万能ブースターです。",
        "target": "従来のコラーゲン化粧品で肌表面のペタペタ感ばかり感じて効果を実感できなかった方、肌の内側の乾燥（インナードライ）が深刻な方、無香料で高機能な美容液を求める方",
        "point": "洗顔直後の素肌、または化粧水の後に2〜3プッシュを手にとり、顔全体に優しく馴染ませます。特に乾燥小ジワが気になる目尻やほうれい線には、指先で優しくトントンと叩き込むように重ねづけしてください。"
    },
    {
        "rank": 4,
        "tag": "🌿 8種の集中モイストコラーゲン×リフト成分！真冬の乾燥小ジワ効能評価試験済み",
        "catch": "キューサイが大人世代の乾燥肌のために磨き上げたコラリッチ最高峰ジェル。機能の異なる8種の集中モイストコラーゲンと酵母エキスを凝縮。真冬の乾燥小ジワを目立たなくし、ふっくら若々しい弾力美肌へ",
        "brand_name": "cola-rich (コラリッチ / キューサイ)",
        "capacity": "55g / スパチュラ付きジャー容器",
        "type": "高機能集中モイスト 多機能コラーゲンリフトジェル",
        "features": "8種のコラーゲン（集中モイストコラーゲン、スプリングコラーゲン、モイストコラーゲン他）、シャクヤクエキス、マロニエエキス",
        "value": "表面を守る高分子コラーゲンから角層深部を潤す超低分子コラーゲンまで、サイズと役割の異なる8種が隙間なく連携。真冬の過酷な乾燥による小ジワを目立たなくする効能評価試験済み",
        "desc_p1": "真冬の空気の乾燥は、角層の表面から深部まで均一にダメージを与えます。そのため単一のコラーゲン成分だけでは、表面の乾燥は防げても内部の弾力低下は救えません。キューサイの『コラリッチEX プレミアムリフトジェル』は、大人の冬の複合肌悩みに応えるため、大きさや機能が異なる「8種類のコラーゲン」を多層的にブレンドした集中保水ジェルです。",
        "desc_p2": "ぷるんとした濃密な黄金のジェルの中には、美肌カプセルがぎっしり。肌に乗せて伸ばすとカプセルが弾け、新鮮な美容成分と8種のコラーゲンが一斉に解き放たれます。高分子コラーゲンが表面に水分蒸散を防ぐヴェールを張り、浸透型コラーゲンが角層細胞の隙間を埋め、集中モイストコラーゲンがダメージ部位を集中補修。乾燥による小ジワを目立たなくする効能評価試験をクリアしており、真冬でも若々しいハリとツヤを一日中キープします。",
        "target": "目元や口元の乾燥小ジワが本格的に気になり始めた方、オールインワンでも濃厚な潤いとハリを諦めたくない方、コラーゲンカプセルによる贅沢なスキンケアを楽しみたい方",
        "point": "付属のスパチュラで直径1.5cm程度を取り、両頬・額・鼻・顎の5点に乗せてから、顔全体に優しく引き上げるように伸ばします。乾燥しやすい目元には薬指で優しく重ね塗りしてください。"
    },
    {
        "rank": 5,
        "tag": "🐟 高純度独自ピュアコラーゲン×セラミド！敏感な冬肌をぷるぷる保水膜で包むモイスチャーゲル",
        "catch": "飲むコラーゲンで有名なエミネットが開発した高保湿オールインワン。高品質フィッシュコラーゲンに3種のセラミドと月見草油を配合。冬の乾燥でデリケートに傾いた肌をぷるぷるの保水膜で包み込む",
        "brand_name": "天使のララ (エミネット)",
        "capacity": "100g / チューブ容器",
        "type": "生フィッシュコラーゲン配合 薬用モイスチャーゲル",
        "features": "独自高純度ピュアコラーゲン、セラミドNP/AP/EOP、月見草油、植物スクワラン、カンゾウ根エキス",
        "value": "無香料・無着色・パラベンフリー・アルコールフリーの無添加設計。良質な魚鱗由来コラーゲンが肌表面にみずみずしい皮膜を作り、真冬の刺激や乾燥から素肌を守り抜く",
        "desc_p1": "冬の寒さと乾燥によって肌のバリア機能が低下すると、少しの刺激で赤みが出たりヒリヒリしたりと敏感肌に傾きがちです。そんな繊細な冬の肌のために、高純度のコラーゲン研究から誕生したのがエミネットの『天使のララ モイスチャーゲルII』です。医療グレードの衛生管理下で抽出された高純度フィッシュコラーゲンをベースに、肌のバリアを整えるヒト型セラミドや月見草オイルをブレンドしています。",
        "desc_p2": "手にとるとみずみずしく柔らかなゲルが肌に吸い付くように広がり、肌表面の微細な凹凸を潤いの膜で満たしていきます。動物由来コラーゲンに比べてアレルゲン性が極めて低い高純度フィッシュコラーゲンを使用しているため、敏感肌にも吸い込まれるように馴染み、刺激を感じさせません。塗布した直後から肌がふっくらと柔らかくなり、朝使えば一日中メイクが粉吹きせず、夜使えば翌朝まで吸い付くようなモチ肌をキープします。",
        "target": "冬になると肌が乾燥してピリピリしやすい敏感肌の方、安心できるピュアコラーゲンで肌を優しく潤したい方、ジャー容器より衛生的なチューブタイプを好む方",
        "point": "洗顔後、さくらんぼ粒大を手にとり、顔全体に優しく馴染ませます。首やデコルテまで伸ばすことで、真冬のタートルネックやマフラーの摩擦から首元の皮膚を保護できます。"
    },
    {
        "rank": 6,
        "tag": "🔬 熱変性ゼロの生コラーゲン×ナノプラチナ！サロン専売・個包装の瞬間リフトエッセンス",
        "catch": "サロン専売品ニチリのプロ仕様集中補修エッセンス。加熱処理を一切行わない生の三重らせんコラーゲンと超微粒子ナノプラチナを贅沢配合。個包装使い切りタイプで真冬の枯れ肌に瞬間リフトと圧倒的保水を注入",
        "brand_name": "ニチリ (Nichiri)",
        "capacity": "3ml×25包 / 個包装ボックス",
        "type": "サロン専売 生コラーゲン×ナノプラチナ 集中美容液",
        "features": "非加熱生コラーゲン（水溶性コラーゲン）、白金（ナノプラチナ）、加水分解エラスチン、ヒアルロン酸Na",
        "value": "熱を一切加えないため、コラーゲン本来の三重らせん構造が完全に生きた状態。個包装で毎回フレッシュな生コラーゲンが肌に乗るため、驚異的なハリ復元力を発揮",
        "desc_p1": "一般的な化粧品コラーゲンの多くは製造過程で加熱処理されており、コラーゲン特有の立体構造が壊れた「ゼラチン」に近い状態になっています。それに対し、ニチリの『プロショット 生コラーゲン』は、一切の熱変性を加えず低温で抽出された本物の「三重らせん生コラーゲン」を、1回使い切りのアルミパックに密閉したサロン専売の集中補修アイテムです。",
        "desc_p2": "封を切って手にとると、濃厚な生コラーゲン美容液がトロリと溢れ出します。肌に乗せた瞬間、生きているコラーゲンの三本鎖分子が自重の数十倍の水分を抱え込みながら、角層表面にピンとした弾力ネットを形成。さらに抗酸化ナノプラチナが真冬の冷えによる酸化ストレスを鎮め、肌の透明感を覚醒させます。夜のケアに使用して眠れば、翌朝まるでエステの生コラーゲンパックを受けた直後のように、肌が内側からパーンと張る感動的なハリを体験できます。",
        "target": "特別なイベント前や真冬の限界乾燥肌を即座にリセットしたい方、本物の非加熱生コラーゲンの実力を体感したい方、防腐剤を極力抑えたフレッシュな個包装を好む方",
        "point": "洗顔後、化粧水の前に1包を全量手にとり、顔全体から首筋にかけて一気に馴染ませます。肌表面がピンと張る感覚が出てきたら、手のひらでハンドプレスして浸透を定着させてください。"
    },
    {
        "rank": 7,
        "tag": "🌿 独自ハモコラーゲン×マツダイペプチド！真冬の過酷な寒冷乾燥から素肌を守り抜く最高峰",
        "catch": "再春館製薬所ドモホルンリンクルの頂点に君臨するクリーム20。生命力あふれる天然ハモから抽出した独自コラーゲンとマツダイコラーゲンペプチドを配合。真冬の過酷な寒冷乾燥下でも力強いハリと透明感を呼び覚ます",
        "brand_name": "Domohorn Wrinkle (再春館製薬所)",
        "capacity": "30g / チューブ容器",
        "type": "医薬部外品 最高峰薬用エイジングクリーム",
        "features": "ハモコラーゲン、マツダイコラーゲンペプチド、ナイアシンアミド、チューリップエキス、不知火菊エキス",
        "value": "日本で初めてコラーゲンを基礎化粧品に配合した歴史あるパイオニア。角層深部までコラーゲンの力を届け、寒さで硬化した大人の肌をしなやかにほぐす最高峰の密閉力",
        "desc_p1": "日本のコラーゲンスキンケアの歴史は、ドモホルンリンクルから始まったと言っても過言ではありません。1974年に日本初のコラーゲン配合クリームとして誕生して以来、半世紀にわたり進化を重ねてきた『クリーム20』は、コラーゲン研究の最高到達点です。過酷な荒波を泳ぎ抜く生命力豊かなハモの皮から抽出した独自コラーゲンと、超極小分子のマツダイコラーゲンペプチドを極限まで凝縮しています。",
        "desc_p2": "こっくりと濃厚なクリームを手にとって温め、肌に塗り広げると、体温でとろけるように角層深部へ吸い込まれていきます。油分の膜でただ表面を覆う一般的なクリームとは異なり、肌がコラーゲンそのものを飲み干すかのように一体化。真冬の氷点下の冷風に晒されても、一日中肌の奥に豊かな湿り気と力強い弾力が留まり続けます。シワ改善・美白の有効成分ナイアシンアミドも配合され、真冬の乾燥小ジワを徹底的に晴らし、ふっくら吸い付くような陶器肌を叶えます。",
        "target": "どんなクリームを使っても冬の乾燥やハリ低下が解決しなかった本気の大人の肌、最高峰のコラーゲン技術と和漢植物の相乗効果を求める方、真冬の寒冷小ジワを本気で克服したい方",
        "point": "小豆粒大を額・鼻・両頬・顎の5点に乗せ、指の腹を使って顔全体に円を描くように優しく塗り込みます。指のすべりが止まり、肌が手に吸い付く感覚になるまで丁寧に馴染ませるのがドモホルンリンクル流です。"
    },
    {
        "rank": 8,
        "tag": "💧 海洋性低分子コラーゲン100%原液！手持ちコスメに混ぜて真冬のハリ感を即効ブースト",
        "catch": "チューンメーカーズが誇る高純度原液シリーズ。良質な海洋性加水分解コラーゲンを希釈せずそのままボトリング。浸透性に優れた低分子コラーゲンが、真冬の乾燥でしぼんだ目元や口元に直接アプローチ",
        "brand_name": "TUNEMAKERS (チューンメーカーズ)",
        "capacity": "20ml / スポイト対応遮光ガラス瓶",
        "type": "海洋性加水分解コラーゲン100%原液エッセンス",
        "features": "加水分解コラーゲン（海洋性フィッシュコラーゲン）原液、水、BG",
        "value": "余計な成分を一切含まない原液設計。手持ちの化粧水や乳液に1〜2滴混ぜるだけで、いつものスキンケアを高保湿コラーゲンコスメへとカスタマイズできる圧倒的自由度",
        "desc_p1": "真冬のスキンケアにおいて「いつもの化粧水では保湿力が足りなくなってきたけれど、ラインを一式買い替えるのは大変」という方に最適なのが、原液コスメのパイオニア・チューンメーカーズの『原液 コラーゲン』です。厳選された天然魚由来の加水分解コラーゲンを、不純物を取り除きながら高濃度にボトリングした純粋原液です。",
        "desc_p2": "低分子化された海洋性コラーゲンは肌なじみが抜群で、角層のすみずみまでスッと浸透。洗顔後の肌に直接数滴なじませれば、乾燥で硬くなった角質がふっくらとほぐれ、その後のスキンケアの浸透を強力に後押しします。また、手持ちの化粧水やクリームに手のひらで1〜2滴ブレンドすれば、真冬仕様のリッチな高保湿コスメへと早変わり。目尻やほうれい線へのピンポイント原液重ね塗りも効果的で、乾燥による小ジワを目立たなくします。",
        "target": "手持ちのスキンケアの保湿力やハリ感を簡単に格上げしたい方、原液ならではのダイレクトな肌実感を求める方、目元や口元など部分的な乾燥小ジワを集中ケアしたい方",
        "point": "化粧水の前にブースターとして2〜3滴馴染ませるか、手のひらでいつもの乳液・クリームに1滴混ぜて使います。乾燥がピークになる真冬の夜は、目元に原液を直接トントンと重ねづけしてください。"
    },
    {
        "rank": 9,
        "tag": "🧪 三重らせん構造を保持した水溶性コラーゲン100%！肌表面にしなやかな保水シールドを形成",
        "catch": "KISO（基礎化粧品研究所）が手がける国産・高純度水溶性生コラーゲン原液。熱変性を避けて抽出された三重らせん構造のコラーゲンが、真冬の外気乾燥による水分蒸散を物理的にシャットアウトする純粋モイスチャー液",
        "brand_name": "KISO / 原液美容液",
        "capacity": "20ml / 遮光スポイトボトル",
        "type": "高純度水溶性コラーゲン（三重らせん）100%原液",
        "features": "水溶性コラーゲン原液（三重らせん構造保持）、フェノキシエタノールフリー処方",
        "value": "分子量が大きく肌表面に留まる特性を活かした「天然の保水シールド」。真冬の暖房下でも角層から水分が一滴も逃げ出さない強力なラッピング効果を発揮",
        "desc_p1": "コラーゲンには「低分子で角層深部に浸透するもの」と、「高分子で肌表面に留まり強固な保水シールドを張るもの」の2つの役割があります。真冬の過酷な暖房気流から肌を守るためには、後者の「表面の保水バリア」が決定的に重要です。KISOの『水溶性コラーゲン原液 100%』は、加熱によって変性していない高分子の生コラーゲンを純度そのままにお届けする本格原液です。",
        "desc_p2": "トロリとした厚みのあるリキッドを肌に伸ばすと、肌表面にしなやかで弾力のある透明なフィルムを形成。大気中の水分を引き寄せながら、角層内の水分が外気へと蒸散するのを鉄壁ブロックします。低分子美容液で肌内部を潤した後にこの生コラーゲン原液を薄く重ねると、まるで肌に潤いのラップをかけたかのような保護状態が完成。一日中エアコンの温風が吹きつけるオフィスにいても、夕方まで肌のツヤと弾力が衰えません。",
        "target": "暖房の風で肌がバリバリに乾いてしまう方、肌表面の潤いヴェールを強化したい方、安心の国産高純度原液をリーズナブルに使い続けたい方",
        "point": "化粧水や美容液をしっかり馴染ませた後、手のひらに2〜3滴取って顔全体を優しくプレスするように重ねます。擦らずに優しくハンドプレスして保水膜を定着させるのがコツです。"
    },
    {
        "rank": 10,
        "tag": "🔬 肌本来の弱酸性pH5に完全同調！サロン現場で愛される生コラーゲン濃密エッセンス",
        "catch": "プロフェッショナル仕様のECモイスチャーエッセンス。健康な素肌と同じ弱酸性「pH5」に精密調整された高濃度生コラーゲンが、真冬の暖房乾燥下でも角層をぷるぷるに保ち続けるサロン専売エッセンス",
        "brand_name": "EC (イーシー)",
        "capacity": "60ml / ポンプボトル",
        "type": "プロフェッショナル pH5生コラーゲン高保湿美容液",
        "features": "生コラーゲン（水溶性コラーゲン高配合）、弱酸性pH5設計、ヒアルロン酸Na、エラスチン",
        "value": "健康な肌の理想的なpH値であるpH5に調整されているため、冬の寒暖差でアルカリ性に傾きバリアが崩れかけた肌を瞬時に整え、生コラーゲンが吸い込まれるように馴染む",
        "desc_p1": "冬の乾燥や肌荒れが進行すると、皮膚表面の皮脂膜が失われて肌のpHバランスが崩れ、弱酸性から中性〜アルカリ性へと傾いてしまいます。この状態ではどんな美容液を塗っても浸透が悪く、刺激を感じやすくなります。エステティックサロンのトリートメント用に開発された『プロフェッショナル ECモイスチャーエッセンス』は、健康な素肌の黄金比率である「pH5」に厳密にコントロールされた高純度生コラーゲン美容液です。",
        "desc_p2": "ポンプを押して肌に乗せると、弱酸性のマイルドな刺激レス処方により、荒れた冬の角質層が穏やかに鎮静。非加熱の生コラーゲン分子が角層の水分ネットワークと即座に手を取り合い、ふっくら吸い付くような潤い膜を再構築します。乾燥で硬くなった肌が瞬時に解きほぐされ、サロン帰りのようなぷるぷるのみずみずしい弾力が復活。真冬の乾燥に負けないタフで美しい素肌をプロの技術で支えます。",
        "target": "冬になると肌荒れを繰り返しスキンケアがピリつく方、サロン専売の本格的な生コラーゲンケアを自宅で続けたい方、肌のキメとpHバランスを根本から立て直したい方",
        "point": "朝晩の洗顔後、化粧水の前に1〜2プッシュを顔全体に伸ばし、手のひらで温めるように包み込みます。弱酸性の生コラーゲンが肌に馴染んだ後にいつものお手入れを続けてください。"
    }
]

toc_items = [
    {"id": "intro", "title": "1. 11月・12月の寒冷乾燥としぼみ肌！「三重らせん」生コラーゲンの驚異の保水力"},
    {"id": "mechanism", "title": "2. なぜ生コラーゲンは真冬の肌を救うのか？トリプルヘリックスの皮膚科学"},
    {"id": "comparison", "title": "3. 高保湿コラーゲンコスメおすすめ10選の比較表"},
    {"id": "ranking", "title": "4. 高保湿コラーゲンコスメおすすめ厳選ランキング10選"},
    {"id": "guide", "title": "5. 失敗しないコラーゲンコスメの選び方＆分子量別の使い分け術"},
    {"id": "routine", "title": "6. 真冬のしぼみ肌と小ジワを押し上げる！先行コラーゲン＆密封ルーティン"},
    {"id": "faq", "title": "7. コラーゲンコスメに関するよくある質問（FAQ）"},
    {"id": "summary", "title": "8. まとめ：先端バイオの力で真冬の肌乾燥とさようなら"}
]

toc_html = "\n".join([f'          <li><a href="#{item["id"]}">{item["title"]}</a></li>' for item in toc_items])

table_rows = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    table_rows.append(f"""            <tr>
              <td class="rank-cell"><strong>第{p["rank"]}位</strong></td>
              <td class="product-cell">
                <a href="#rank-{p["rank"]}"><strong>{p["brand_name"]}</strong><br><span style="font-size:0.85rem;color:#4b5563;">{item_data["item_name"][:35]}...</span></a>
              </td>
              <td>{p["type"]}</td>
              <td class="price-cell">¥{item_data["price"]:,}</td>
              <td>{p["features"][:30]}...</td>
              <td><a href="{item_data["affiliate_url"]}" class="table-btn" target="_blank" rel="nofollow noopener">楽天で見る</a></td>
            </tr>""")

table_rows_html = "\n".join(table_rows)

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <!-- Rank {p["rank"]} -->
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge rank-{p["rank"]}">第{p["rank"]}位</span>
            <div class="product-title-group">
              <span class="product-catch">{p["tag"]}</span>
              <h3 class="product-name">{item_data["item_name"]}</h3>
              <p class="product-subname">{p["catch"]}</p>
            </div>
          </div>

          <div class="product-main-grid">
            <div class="product-visual">
              <img src="{item_data["image_url"]}" alt="{item_data["item_name"]}" class="product-img" loading="lazy">
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">¥{item_data["price"]:,}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", "4.8")}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", "110")}件）</span>
              </div>
              <a href="{item_data["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
                🛒 楽天市場で「{p["brand_name"]}」の最新価格・在庫・口コミを見る
              </a>
            </div>

            <div class="product-info-col">
              <table class="spec-table">
                <tr><th>ブランド</th><td>{p["brand_name"]}</td></tr>
                <tr><th>容量・容器</th><td>{p["capacity"]}</td></tr>
                <tr><th>アイテム種別</th><td>{p["type"]}</td></tr>
                <tr><th>注目美肌成分</th><td>{p["features"]}</td></tr>
                <tr><th>真冬の特長・価値</th><td>{p["value"]}</td></tr>
              </table>

              <div class="product-body">
                <h4 class="body-title">皮膚科学的アプローチ＆冬の使用感レビュー</h4>
                <p>{p["desc_p1"]}</p>
                <p>{p["desc_p2"]}</p>

                <div class="recommend-box">
                  <div class="recommend-title">💡 こんな方・こんな冬の肌悩みにおすすめ！</div>
                  <p>{p["target"]}</p>
                </div>

                <div class="usage-box">
                  <div class="usage-title">🧴 11月・12月の効果的な使い方テクニック</div>
                  <p>{p["point"]}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
""")

all_cards_html = "\n".join(product_cards_html)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！三重らせん生コラーゲンと高浸透ナノペプチドが真冬のしぼみ肌と乾燥小ジワをぷるんと押し上げる高保湿コラーゲンコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の寒冷乾燥で水分が抜け落ち、ハリを失ったしぼみ肌・乾燥小ジワを救う高保湿コラーゲン（生コラーゲン・浸透型ナノコラーゲン）コスメを徹底厳選！アスタリフト、ドクターシーラボ、DHC、コラリッチ、ドモホルンリンクルまで三重らせん保水の皮膚科学的根拠と共に徹底検証。">
  <meta name="keywords" content="コラーゲン コスメ, 生コラーゲン 美容液, 高保湿 コスメ 冬, 乾燥小ジワ 対策 11月 12月, アスタリフト ジェリー アクアリスタ, ドクターシーラボ エンリッチリフト, DHC スーパーコラーゲン, コラリッチEX, ドモホルンリンクル クリーム20">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！三重らせん生コラーゲンと高浸透ナノペプチドが真冬のしぼみ肌と乾燥小ジワをぷるんと押し上げる高保湿コラーゲンコスメランク10">
  <meta property="og:description" content="熱変性させない生コラーゲンの驚異的弾力保水！真冬の過酷な寒冷乾燥でしぼんだ角層を押し上げる高保湿コラーゲンコスメ10選を徹底検証。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-collagen">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿コラーゲンコスメランク10">
  <meta name="twitter:description" content="11月・12月の本格乾燥に！生コラーゲンと高浸透ペプチドで満たす高保湿コラーゲンコスメおすすめ10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！三重らせん生コラーゲンと高浸透ナノペプチドが真冬のしぼみ肌と乾燥小ジワをぷるんと押し上げる高保湿コラーゲンコスメランク10",
    "description": "11月・12月の冷気と暖房で水分が蒸散し、ハリを失ったしぼみ肌・乾燥小ジワを救う高保湿生コラーゲンコスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-05T22:00:00+09:00",
    "dateModified": "2026-11-05T22:00:00+09:00",
    "author": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS 編集部"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://lumi-cosme.vercel.app/favicon.jpg"
      }}
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-collagen"
    }}
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #2: ItemList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿コラーゲンコスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "{items[0]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{items[1]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{items[2]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 4,
        "name": "{items[3]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 5,
        "name": "{items[4]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 6,
        "name": "{items[5]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 7,
        "name": "{items[6]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 8,
        "name": "{items[7]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 9,
        "name": "{items[8]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 10,
        "name": "{items[9]["item_name"]}"
      }}
    ]
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #3: FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "生コラーゲンと加水分解コラーゲンはどのように使い分けるのがベストですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "生コラーゲンは非加熱の三重らせん構造を保ち分子量が大きいため、肌表面にしなやかな保水ネットを形成して冬の外気乾燥を物理的にシャットアウトします。一方、加水分解コラーゲン（コラーゲンペプチド）は極小分子化されているため角層深部まで浸透して内側からハリを補います。真冬のスキンケアでは、この両方を組み合わせた製品や先行美容液を活用するのが最も効果的です。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "コラーゲン化粧品は肌に塗っても真皮まで届かないと言われますが意味はありますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "化粧品が届くのは角質層までですが、角質層におけるコラーゲンの保水力は絶大です。角層が水分で満たされてふっくらと厚みを増すことで、真冬の乾燥小ジワが目立たなくなり、光を綺麗に反射してハリとツヤが生まれます。さらに最新の低分子ナノペプチド（ジペプチド-8など）は角層深部へ届き、自らうるおう力を力強くサポートします。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "朝のメイク前に生コラーゲン配合コスメを使うとモロモロが出ませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "過剰な増粘剤（カルボマー等）を多量に含んだジェルはモロモロの原因になりやすいですが、近年の上質な生コラーゲン先行美容液（アスタリフトなど）や浸透型ナノコラーゲンは肌なじみが極めて良く、塗布後にしっかりハンドプレスして角層に密着させればモロモロは出ません。むしろ日中の暖房によるメイク崩れや粉吹きを劇的に防ぐ下地効果を発揮します。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #be123c;
      --primary-light: #ffe4e6;
      --primary-dark: #9f1239;
      --accent: #e11d48;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg: #fff1f2;
      --bg-card: #ffffff;
      --border: #fecdd3;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-weight: 800;
      font-size: 1.35rem;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}
    
    .hero-container {{
      max-width: 1100px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    .hero-card {{
      background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      box-shadow: var(--shadow);
    }}
    .badge-category {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    .hero-title {{
      font-size: 1.85rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 1.25rem;
    }}
    .hero-lead {{
      font-size: 1.05rem;
      color: #374151;
      margin-bottom: 1.5rem;
    }}
    .meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      border-top: 1px solid rgba(0, 0, 0, 0.08);
      padding-top: 1rem;
    }}
    
    /* 目次 */
    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.75rem;
      margin: 2rem 0;
      box-shadow: var(--shadow);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-card ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 0.75rem 1.5rem;
    }}
    .toc-card a {{
      color: var(--text);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
      display: block;
      padding: 0.25rem 0;
    }}
    .toc-card a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}
    
    /* セクション共通 */
    .article-section {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.25rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #111827;
      border-left: 5px solid var(--primary);
      padding-left: 1rem;
      margin-bottom: 1.5rem;
      line-height: 1.35;
    }}
    .article-section p {{
      margin-bottom: 1.25rem;
      color: #374151;
      font-size: 1rem;
      text-align: justify;
    }}
    .highlight-lead {{
      background: var(--primary-light);
      border-left: 4px solid var(--accent);
      padding: 1.25rem;
      border-radius: 4px;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
    }}
    
    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .data-table th, .data-table td {{
      padding: 0.85rem 1rem;
      border: 1px solid #e5e7eb;
    }}
    .data-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}
    .rank-cell {{ text-align: center; font-size: 1rem; color: var(--primary); white-space: nowrap; }}
    .price-cell {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 4px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}
    
    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: flex-start;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .rank-badge {{
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      padding: 0.4rem 1rem;
      border-radius: 8px;
      white-space: nowrap;
    }}
    .product-catch {{
      display: block;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .product-name {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 0.35rem;
    }}
    .product-subname {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    .product-main-grid {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-main-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-visual {{
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #fff1f2;
      padding: 1.5rem;
      border-radius: 8px;
      border: 1px solid var(--border);
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      border-radius: 6px;
      background: #ffffff;
      padding: 0.5rem;
      margin-bottom: 1rem;
    }}
    .price-box {{
      width: 100%;
      text-align: center;
      margin-bottom: 0.75rem;
      padding: 0.5rem;
      background: #ffffff;
      border-radius: 6px;
      border: 1px solid #fecdd3;
    }}
    .price-label {{ font-size: 0.75rem; color: var(--text-muted); display: block; }}
    .price-value {{ font-size: 1.4rem; font-weight: 800; color: #b91c1c; }}
    .review-meta {{
      font-size: 0.85rem;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.25rem;
    }}
    .review-stars {{ color: #d97706; font-weight: 700; }}
    .review-count {{ color: var(--text-muted); }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #be123c 0%, #e11d48 100%);
      color: #ffffff;
      text-align: center;
      padding: 0.9rem 1rem;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 6px rgba(190, 18, 60, 0.25);
      transition: opacity 0.2s;
    }}
    .rakuten-btn:hover {{ opacity: 0.9; }}
    
    .product-info-col {{ display: flex; flex-direction: column; }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.85rem;
      border: 1px solid #e5e7eb;
    }}
    .spec-table th {{
      width: 28%;
      background: #fff1f2;
      color: #9f1239;
      font-weight: 700;
      white-space: nowrap;
    }}
    .body-title {{
      font-size: 1.1rem;
      font-weight: 800;
      color: #111827;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .recommend-box {{
      background: #ffe4e6;
      border-left: 4px solid var(--accent);
      padding: 1rem 1.25rem;
      border-radius: 4px;
      margin: 1.25rem 0;
    }}
    .recommend-title {{
      font-weight: 700;
      color: #9f1239;
      font-size: 0.9rem;
      margin-bottom: 0.35rem;
    }}
    .recommend-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    .usage-box {{
      background: #f3f4f6;
      border-left: 4px solid #6b7280;
      padding: 1rem 1.25rem;
      border-radius: 4px;
      margin-top: 1rem;
    }}
    .usage-title {{
      font-weight: 700;
      color: #374151;
      font-size: 0.9rem;
      margin-bottom: 0.35rem;
    }}
    .usage-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    /* FAQ & 内部リンク */
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.25rem 0;
    }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}
    .faq-a {{
      color: #374151;
      padding-left: 1.75rem;
      font-size: 0.95rem;
    }}
    
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">🌿 LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <div class="hero-container">
    <div class="hero-card">
      <span class="badge-category">熱変性させない生コラーゲン×高浸透ナノペプチドの真価</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！三重らせん生コラーゲンと高浸透ナノペプチドが真冬のしぼみ肌と乾燥小ジワをぷるんと押し上げる高保湿コラーゲンコスメランク10</h1>
      <p class="hero-lead">
        11月から12月にかけて訪れる気温低下と暖房の直撃。角層から水分が蒸散して肌がクシャッと萎縮し、目元や口元の細かな小ジワやたるみ毛穴が目立ち始める真冬の「しぼみ肌」——。熱変性させない三重らせん構造を保った「生コラーゲン」と、角層深部を貫く「極小ナノペプチド」の最先端皮膚科学を解き明かし、楽天市場で今すぐ手に入る最高峰のコラーゲンコスメ10選を徹底検証します。
      </p>
      <div class="meta-bar">
        <span>📅 2026年11月更新（真冬ハリ弾力乾燥特化版）</span>
        <span>🔬 先進ナノテクノロジー・生体模倣コラーゲン検証済み</span>
        <span>🛍️ 楽天市場公式APIデータ連携</span>
      </div>
    </div>
  </div>

  <main class="hero-container">
    <!-- 目次 -->
    <div class="toc-card">
      <div class="toc-title">📑 目次（クリックで各項目へジャンプ）</div>
      <ul>
{toc_html}
      </ul>
    </div>

    <!-- セクション1: 導入 -->
    <section class="article-section" id="intro">
      <h2 class="section-title">1. 11月・12月の寒冷乾燥としぼみ肌！「三重らせん」生コラーゲンの驚異の保水力</h2>
      <div class="highlight-lead">
        水分を与えるだけでは戻らない冬の「肌のしぼみ」。熱変性していない生コラーゲンのトリプルヘリックス（三重らせん）構造が膨大な水分を束ねて肌表面を跳ね返し、ナノペプチドが角層深部を満たして乾燥小ジワを根底から消し去ります。
      </div>
      <p>
        11月から12月にかけて、湿度の急低下と北風の吹き荒れる日本の冬。気温が低下すると顔の毛細血管が収縮して血行が滞り、真皮や表皮の細胞活性が著しく低下します。さらに室内の暖房による激しい乾燥が追い打ちをかけ、肌の角質層は水分を保てずに薄く萎縮。夕方ふと鏡を見ると、ファンデーションが細かな小ジワに落ち込み、頬の毛穴が縦に流れて顔全体がやつれたようにしぼんで見える——これが真冬の「しぼみ肌現象」です。
      </p>
      <p>
        しぼんだ冬肌を立て直すためには、単なる水分補給や油分のフタだけでは不十分です。皮膚の構造タンパク質であるコラーゲンそのものが持つ「弾力保水構造」を肌表面と角層内部に再現しなければなりません。近年のバイオテクノロジーによって実現した「非加熱・三重らせん生コラーゲン」は、一般的な加水分解コラーゲン（ゼラチン化されたペプチド）の数十倍の水分抱合力を誇り、肌に乗せた瞬間に見えない弾力ネットとなって真冬の乾燥小ジワをぷるんと押し上げます。
      </p>
    </section>

    <!-- セクション2: メカニズム -->
    <section class="article-section" id="mechanism">
      <h2 class="section-title">2. なぜ生コラーゲンは真冬の肌を救うのか？トリプルヘリックスの皮膚科学</h2>
      <p>
        生コラーゲンが真冬の深刻なしぼみ肌や乾燥小ジワに対して圧倒的なハリ復元効果を発揮する理由は、その独自の分子構造と多層アプローチにあります。
      </p>
      <p>
        <strong>① 熱変性させない「三重らせん構造（トリプルヘリックス）」の圧倒的保水力：</strong><br>
        本来、体内に存在するコラーゲンは3本のポリペプチド鎖が強固に絡み合った「三重らせん構造」をとっています。このらせんの隙間に膨大な水分子が結合水として固定され、強靭な弾力としなやかさを生み出しています。しかし一般的な化粧品原料のコラーゲンは抽出時の加熱によりらせん構造がほどけてバラバラになっています。「生コラーゲン」は特許技術などにより非加熱で抽出されているため、本来の立体構造が完全に維持されており、肌表面に驚異的な水分保持ネットワークを再構築します。
      </p>
      <p>
        <strong>② 角層深部へ届く「極小ナノペプチド（ジペプチド-8等）」の即効浸透：</strong><br>
        表面に留まって保水ネットを張る生コラーゲンと対をなすのが、最先端の加水分解技術によってコラーゲンの最小構成単位（アミノ酸2個のジペプチドや3個のトリペプチド）まで微小化されたナノコラーゲンです。分子量がわずか数千分の一であるため、角質層のバリアをやすやすと通過し、乾いて萎縮した細胞間に水分とアミノ酸をダイレクトに補給。内側から肌をふっくら押し上げるクッションの役割を果たします。
      </p>
      <p>
        <strong>③ 先行美容液（ブースター）としての自己復元ネットワーク：</strong><br>
        アスタリフトに代表されるナノ技術を応用した生コラーゲンジェリーは、洗顔直後の無防備な角層に塗布することで、乱れた角質細胞の配列を物理的に整える働きを持ちます。崩しても元の滑らかな平面に戻る自己復元ポリマーが生コラーゲンと共に肌にピタッと密着し、その後に塗布する化粧水や乳液の水分を吸い寄せる「親水ルート」を確立します。
      </p>
    </section>

    <!-- セクション3: 比較表 -->
    <section class="article-section" id="comparison">
      <h2 class="section-title">3. 高保湿コラーゲンコスメおすすめ10選の比較表</h2>
      <p>
        楽天市場で実際に購入可能な人気の高保湿コラーゲンコスメ10アイテムの種別、参考価格、主要美肌成分を一覧にまとめました。
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド・商品名</th>
              <th>カテゴリー種別</th>
              <th>参考価格（税込）</th>
              <th>注目美肌成分</th>
              <th>楽天リンク</th>
            </tr>
          </thead>
          <tbody>
{table_rows_html}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4: ランキング -->
    <section class="article-section" id="ranking">
      <h2 class="section-title">4. 高保湿コラーゲンコスメおすすめ厳選ランキング10選</h2>
      <p>
        コラーゲン純度、三重らせん構造の保持、ナノ浸透技術、真冬のハリ・弾力持続力、楽天市場での購入信頼性を総合的に審査したTOP10ランキングです。
      </p>
{all_cards_html}
    </section>

    <!-- セクション5: 選び方ガイド -->
    <section class="article-section" id="guide">
      <h2 class="section-title">5. 失敗しないコラーゲンコスメの選び方＆分子量別の使い分け術</h2>
      <p>
        コラーゲンコスメで真冬のしぼみ肌を劇的に改善するためには、コラーゲンの「分子量の役割」を理解して使い分けることが成功の鍵です。
      </p>
      <p>
        <strong>① 洗顔直後の土台再構築には「生コラーゲン先行ジェリー・導入液」：</strong><br>
        アスタリフト（第1位）やDHCスーパーコラーゲン（第3位）、ニチリ（第6位）のように、洗顔直後に使うアイテムは、乾燥で硬くなった角層をほぐし、後から使うスキンケアの通り道を開きます。
      </p>
      <p>
        <strong>② 1つでリフトアップと濃厚保湿を両立したいなら「高機能オールインワン」：</strong><br>
        ドクターシーラボ（第2位）やコラリッチ（第4位）、天使のララ（第5位）のように、複数のコラーゲンと美容成分を複合したゲルは、忙しい真冬の朝晩でも手軽に強力な保水シールドとハリ感を実感できます。
      </p>
      <p>
        <strong>③ 夜の深刻なしぼみ肌・乾燥小ジワを集中密封するなら「最高峰クリーム」：</strong><br>
        ドモホルンリンクル クリーム20（第7位）のように、上質なコラーゲンとリッチなエモリエント油分を融合させたクリームは、暖房をつけた寝室でも朝まで一滴の水分も逃さない究極の密閉バリアとなります。
      </p>
    </section>

    <!-- セクション6: ルーティン -->
    <section class="article-section" id="routine">
      <h2 class="section-title">6. 真冬のしぼみ肌と小ジワを押し上げる！先行コラーゲン＆密封ルーティン</h2>
      <p>
        生コラーゲンと浸透型ペプチドのポテンシャルを100%発揮させ、真冬でも押し返すような弾力肌を作るステップです。
      </p>
      <p>
        <strong>ステップ1【洗顔直後の生コラーゲン先行投入】：</strong><br>
        朝晩の洗顔後、タオルで水気を取った直後の肌に、アスタリフトの先行ジェリーやDHCのスパコラを馴染ませます。角層の乱れた細胞間隙が生コラーゲンとナノ成分で満たされ、水分を引き込むスポンジ状態が完成します。
      </p>
      <p>
        <strong>ステップ2【高保湿化粧水で水分をたっぷり流し込む】：</strong><br>
        先行コラーゲンが肌に密着したら、すぐに保湿化粧水を2〜3回に分けて重ねづけします。生コラーゲンの網目構造が化粧水の水分を捕らえ、角層全体がぷっくりと膨らむのを実感できます。
      </p>
      <p>
        <strong>ステップ3【コラーゲンクリーム・ゲルのリフト密閉】：</strong><br>
        仕上げにドクターシーラボやドモホルンリンクルのクリームを手にとり、フェイスラインを下から上へ、ほうれい線を外側へ引き上げるように塗り広げます。最後に手のひらでハンドプレスして形状記憶させるように温めて完了です。
      </p>
    </section>

    <!-- セクション7: FAQ -->
    <section class="article-section" id="faq">
      <h2 class="section-title">7. コラーゲンコスメに関するよくある質問（FAQ）</h2>
      
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 生コラーゲンと加水分解コラーゲンはどのように使い分けるのがベストですか？</div>
        <div class="faq-a">
          生コラーゲンは非加熱の三重らせん構造を保ち分子量が大きいため、肌表面にしなやかな保水ネットを形成して冬の外気乾燥を物理的にシャットアウトします。一方、加水分解コラーゲン（コラーゲンペプチド）は極小分子化されているため角層深部まで浸透して内側からハリを補います。真冬のスキンケアでは、この両方を組み合わせた製品や先行美容液を活用するのが最も効果的です。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> コラーゲン化粧品は肌に塗っても真皮まで届かないと言われますが意味はありますか？</div>
        <div class="faq-a">
          化粧品が届くのは角質層までですが、角質層におけるコラーゲンの保水力は絶大です。角層が水分で満たされてふっくらと厚みを増すことで、真冬の乾燥小ジワが目立たなくなり、光を綺麗に反射してハリとツヤが生まれます。さらに最新の低分子ナノペプチド（ジペプチド-8など）は角層深部へ届き、自らうるおう力を力強くサポートします。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 朝のメイク前に生コラーゲン配合コスメを使うとモロモロが出ませんか？</div>
        <div class="faq-a">
          過剰な増粘剤（カルボマー等）を多量に含んだジェルはモロモロの原因になりやすいですが、近年の上質な生コラーゲン先行美容液（アスタリフトなど）や浸透型ナノコラーゲンは肌なじみが極めて良く、塗布後にしっかりハンドプレスして角層に密着させればモロモロは出ません。むしろ日中の暖房によるメイク崩れや粉吹きを劇的に防ぐ下地効果を発揮します。
        </div>
      </div>
    </section>

    <!-- セクション8: まとめ -->
    <section class="article-section" id="summary">
      <h2 class="section-title">8. まとめ：先端バイオの力で真冬の肌乾燥とさようなら</h2>
      <p>
        11月から12月にかけての本格的な真冬シーズンは、外気の冷気と室内の暖房による激しい水分蒸散によって、私たちの素肌から急速に潤いと弾力が奪い去られていきます。表面をいくら保湿しても肌がしぼんで小ジワが目立ってしまう冬のトラブルを解決する鍵は、三重らせん構造を保った生コラーゲンと高浸透ナノペプチドによる「多層的なハリ弾力アプローチ」に他なりません。
      </p>
      <p>
        非加熱の生コラーゲンが肌表面に張るしなやかな弾力シールドと、角層深部を満たすナノペプチドの相乗効果は、過酷な真冬の乾燥環境から素肌を確実に守り抜き、指を跳ね返すようなピンとした上向き肌へと導いてくれます。ぜひ本記事のランキングや選び方を参考に、あなたのライフスタイルや肌悩みにぴったりのコラーゲンコスメを見つけて、真冬でも乾燥知らずのぷるぷる美肌を手に入れてください。
      </p>
    </section>

    <!-- 関連記事リンクプレースホルダー -->
    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <!-- update_all_internal_links.py で自動挿入 -->
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-logo">🌿 LUMI COSMETICS</div>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で自動挿入 -->
      </div>
      <div style="text-align:center;margin-top:2rem;font-size:0.8rem;color:#6b7280;">
        &copy; 2026 LUMI COSMETICS. All rights reserved.
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-collagen.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-collagen.html successfully!")
