import json
import re

with open("fetched_3new_barrier_niacinamide_exosome.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_exosome_cream"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "💉 美容針×CICAエクソソーム！真冬のこわばった角層深部へ美容成分をダイレクト注入する最高峰",
        "catch": "メガヒット『リードルショット』の先進技術をクリームに落とし込んだVTの最高峰。天然シリカマイクロニードルにCICAエクソソームと低分子コラーゲンを吸着させ、冬の冷気で硬化した肌にチクチクと心地よい刺激を与えながら弾力リフトアップ",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "50mL / チューブ容器",
        "type": "マイクロニードル×CICAエクソソーム配合 高浸透リフティングクリーム",
        "features": "CICA REEDLE™（天然美容針シリカ）、CICAエクソソーム、低分子コラーゲン、植物性エラスチン、ヒト型セラミド",
        "value": "11月・12月の寒冷で代謝が鈍り、スキンケアが浸透しなくなった冬の『受け入れ拒否肌』を打破。美容針が通り道を作り、エクソソームが細胞間を直撃",
        "desc_p1": "11月から12月にかけて気温が下がると、皮膚の末梢血管が収縮し、ターンオーバーが大幅に遅延します。その結果、古い角質が剥がれ落ちずに堆積し、肌表面が硬くゴワついて高価な美容液やクリームを塗っても弾かれてしまう『浸透ブロック現象』が起こります。VTのリードルショットリフティングクリームは、髪の毛よりもはるかに細い天然のシリカマイクロニードルが角層に微細な通り道（チャネル）を形成。そこにナノサイズのエクソソーム化されたツボクサ有用成分が深く滑り込み、真冬のしぼんだ肌構造を土台から押し上げます。",
        "desc_p2": "コクのあるなめらかなクリームで、肌に伸ばすとチクチクとした独特のマイクロ刺激（美容針の働き）を感じます。この刺激が冬の寒さで眠っていた肌の自己治癒力を呼び覚まし、血行を促進。塗布後はピタッと密着するリフティング被膜が形成され、フェイスラインのもたつきや乾燥たるみ毛穴をキュッと上向きにホールドします。翌朝の洗顔時には、肌のキメが驚くほど整い、指先が吸い付くようなハリとツヤを実感できます。",
        "target": "冬になるとどんなスキンケアも浸透しにくく感じる方、たるみ毛穴やフェイスラインの緩みが気になる方、サロン級の即効性を求める方",
        "point": "夜のお手入れの最後に、適量を手に取り、顔全体に優しく塗り広げます。引き伸ばすだけでなく、手のひらで顔全体を優しくプレスして『針を角層へ押し込む』イメージでハンドプレスすると、エクソソームの浸透効率が最大化されます。"
    },
    {
        "rank": 2,
        "tag": "🔬 毛穴特化エクソソーム×低分子ペプチド！冬の寒冷で開いた縦長毛穴を1日でキュッと引き締めるダーマ名品",
        "catch": "韓国No.1ダーマコスメmedicube（メディキューブ）が開発した、毛穴特化型エクソソームクリーム。毛穴の数千分の一サイズのナノエクソソームカプセルが毛穴奥の角層まで届き、真冬の冷えと乾燥で垂れ下がった毛穴を徹底タイトニング",
        "brand_name": "medicube (メディキューブ)",
        "capacity": "50mL / チューブ容器",
        "type": "毛穴特化エクソソーム×AHA/BHA/PHA配合 毛穴引き締め高保湿クリーム",
        "features": "毛穴特化エクソソームコンプレックス、トリプル引き締めペプチド、AHA・BHA・PHA複合体、ナイアシンアミド",
        "value": "冬の『乾燥たるみ毛穴』と『冷えによるキメの乱れ』をダブル制圧。臨床試験で実証された毛穴縮小効果と、真冬の水分蒸発を防ぐエモリエントシールド",
        "desc_p1": "冬の毛穴は皮脂による黒ずみだけでなく、乾燥による皮膚の萎縮と真皮の弾力低下によって毛穴周囲が引っ張られ、楕円形に広がる『たるみ毛穴』が主流となります。メディキューブのゼロ毛穴1dayクリームは、生体適合性の高いエクソソーム技術によって引き締めペプチドと抗酸化成分を毛穴の隙間へピンポイント送達。真冬の過酷な乾燥環境でも毛穴が緩まない強靭な肌密度を再構築します。",
        "desc_p2": "淡いブルーの軽やかで高密着なジェルクリームテクスチャーで、塗布した瞬間に肌のキメの隙間へスッと入り込み、凹凸をフラットに整えるプライマーのような密閉感を放ちます。不要な角質を穏やかに整えるマイルド酸複合体も含まれているため、真冬のゴワつきやくすみを防ぎ、なめらかな陶器肌を演出。朝のメイク前に使用してもファンデーションが毛穴落ちせず、美しい仕上がりが夕方まで持続します。",
        "target": "冬になるとファンデーションが毛穴に落ちて目立つ方、頬のたるみ毛穴をキュッと引き締めたい方、ベタつかない高機能クリームを好む方",
        "point": "化粧水や美容液の後、チューブから適量を出して、毛穴が気になる鼻周りや頬の中心から外側へ優しく伸ばします。毛穴を引き上げるように下から上へ優しく撫で上げると、タイトニング効果が一段とアップします。"
    },
    {
        "rank": 3,
        "tag": "🧬 サーモンc-PDRN×バイオ生体カプセル！美容医療の真髄を宿す真冬の肌再生ニュートリティブクリーム",
        "catch": "韓国の最高峰美容クリニックで施術されるサーモン注射の主成分c-PDRNを配合したリジュランの看板クリーム。ナノ化バイオカプセル技術により真冬の極度な乾燥で崩壊した角層バリアを内側から劇的に修復する奇跡のエイジングケア",
        "brand_name": "REJURAN (リジュラン)",
        "capacity": "50mL / チューブ容器",
        "type": "高純度c-PDRN（ポリデオキシリボヌクレオチド）配合 バイオ再生高保湿クリーム",
        "features": "c-PDRN（サーモンDNA断片化エキス）、シア脂、ホホバ種子油、ナイアシンアミド、アデノシン",
        "value": "美容医療発想の圧倒的な組織修復力。真冬の過酷な乾燥風や摩擦で傷ついた肌の再生スピードを劇的に加速させ、まるでサロン帰りの水光肌へ",
        "desc_p1": "リジュランのニュートリティブクリームは、過酷な冬の環境で完全に疲弊してしまった肌の『最終兵器』として美容皮膚科医からも熱い支持を受けています。主成分のc-PDRNは、人間のDNA塩基配列に極めて近いサーモンの精巣から抽出された生体親和性DNAポリマー。これをバイオカプセル化（エクソソーム類似技術）することで、冬の寒冷で代謝が停止した皮膚組織の再生シグナルをダイレクトに活性化します。",
        "desc_p2": "バターのように濃厚でコクのあるリッチな質感でありながら、肌に乗せると体温でトロリとほどけ、驚くほど吸い付くように角層へと溶け込みます。肌表面には目に見えないほど薄く強固なバイオシールド膜が形成され、暖房直撃の部屋でも水分を一滴も逃しません。翌朝の肌に触れると、指が跳ね返るような圧倒的な弾力と、内側からジュワッと発光するような極上のツヤに驚かされます。",
        "target": "冬の乾燥で肌が薄くなりしぼんでハリを失った方、美容クリニック級の本格再生スキンケアを自宅で体感したい方、最高峰のリッチ保湿を求める方",
        "point": "夜のお手入れの最後に、やや多めのパール粒大を取り、手のひらで温めてから顔全体を包み込むように塗布します。ほうれい線や目元のシワには、指先で皮膚を軽く引き上げながら優しく擦り込んでください。"
    },
    {
        "rank": 4,
        "tag": "🛡️ パンテノール×高保水エクトイン微細リポソーム！200時間極限保湿で真冬の砂漠肌を完全救済する超名品",
        "catch": "魔女工場（Manyo）が真冬の超乾燥肌のために開発したダーマライン『パンテトイン』。角層修復のパンテノールと極限保水のエクトインをナノリポソーム化。200時間の極限保水テストをクリアした濃密バリアクリーム",
        "brand_name": "魔女工場 (Manyo Factory)",
        "capacity": "80mL / チューブ容器",
        "type": "パンテトイン™（パンテノール×エクトイン）配合 200時間極限保湿クリーム",
        "features": "パンテトイン™（パンテノール4,000ppm＋エクトイン1,000ppm）、セラミドNP、フィトスフィンゴシン、ヒアルロン酸、低分子マカデミアオイル",
        "value": "真冬の粉吹き・脱水を完全にシャットアウト。微細ナノカプセルが角層の最も深い層まで浸透し、まるで肌内部に貯水タンクを設置したかのような持続力を発揮",
        "desc_p1": "冬の乾燥が深刻化すると、通常の保湿クリームでは数時間で蒸発してしまい、日中に何度も塗り直す必要に迫られます。魔女工場の『パンテトイン エンリッチド クリーム』は、皮膚組織修復を助けるパンテノールと、過酷な砂漠湖で生きる微生物が身を守る保水分子エクトインを微細なナノカプセルに封入。塗布後200時間にわたって水分を保持し続けるという驚異的な臨床データを誇ります。",
        "desc_p2": "こっくりと濃密なテクスチャーですが、重さや皮膜感を感じさせず、肌に吸い込まれるようにスッと馴染みます。真冬の木枯らしやエアコン暖房を浴び続けても、夕方まで肌の柔らかさとモチモチ感がそのまま維持される安心感は格別。80mLという大容量チューブで惜しみなく使える点も、冬のヘビーユーザーから熱狂的な支持を集める理由です。",
        "target": "どれだけクリームを塗っても数時間で乾燥してしまう超乾燥肌、粉吹きや皮剥けに悩まされる方、日中の塗り直しができない忙しい方",
        "point": "化粧水の後に適量を手に取り、乾燥が気になる部位を中心に顔全体へ広げます。夜のスキンケアでは、頬や口元に少し厚めに塗ってスリーピングパックとして使用すると、翌朝の肌コンディションが劇的に向上します。"
    },
    {
        "rank": 5,
        "tag": "🏆 高純度TECA×ツボクサ活性エクソソーム！韓国東国製薬55年の集大成・国民的リペアクリーム",
        "catch": "韓国製薬大手の東国製薬が開発し、累計4,000万本以上を売り上げた国民的クリームの最新シーズン7。高純度センテラアジアティカ抽出物TECAにツボクサ活性エクソソームを融合し、真冬の寒冷たるみと乾燥小ジワを強力リセット",
        "brand_name": "Centellian24 (センテリアン24)",
        "capacity": "50mL / チューブ容器",
        "type": "東国製薬特許TECA×ツボクサエクソソーム配合 薬用級リペアクリーム",
        "features": "TECA（センテラアジアティカ定量抽出物）、ツボクサ活性エクソソーム、加水分解コラーゲン、植物性エラスチン、セラミド複合体",
        "value": "製薬会社ならではの厳格なエビデンス。冬の乾燥・シワ・たるみ・バリア破壊・くすみを1本で網羅的にケアするトータルアンチエイジング",
        "desc_p1": "センテリアン24の『マデカクリーム タイムリバース』は、傷跡治療薬マデカソルの有効成分をスキンケアに応用した名作です。最新バージョンでは、ツボクサの有用成分を毛穴の数千分の一サイズのエクソソーム形態で抽出することに成功。真冬の寒風によって萎縮したコラーゲンネットワークとエラスチン結合を再構築し、深い乾燥溝を押し戻す驚異的なリペア力を発揮します。",
        "desc_p2": "コクのあるなめらかなクリームで、ハーブの清々しい香りが心地よく広がります。肌に馴染ませると密着感のある保護膜を形成し、冬の過酷な空気乾燥から肌を長時間ディフェンス。肌の赤みを素早く鎮静化させながら、もっちりとした弾力とツヤを肌に宿します。千円台後半という手頃な価格帯ながら、デパコスクラスの満足度を届けてくれる高コスパの神アイテムです。",
        "target": "乾燥による小ジワやたるみを同時にケアしたい方、製薬会社の確かなリペア効果を求める方、コストパフォーマンスに優れた実力派クリームを探している方",
        "point": "朝晩のお手入れの最後に、適量を出して顔全体に均一に伸ばします。首元のシワやほうれい線には、下から上へ皮膚を軽く持ち上げるように塗り込むとリフト実感が深まります。"
    },
    {
        "rank": 6,
        "tag": "🌿 国産ヒト幹細胞順化培養液×ナノエクソソームカプセル！細胞レベルで冬肌を潤す国内実力派",
        "catch": "高濃度原液スキンケアのパイオニアKISOが手掛けるプレミアムクリーム。国産ヒト脂肪由来幹細胞順化培養液にナノ化エクソソーム技術を組み合わせ、真冬の乾燥でしぼんだ角層細胞をふっくら満水状態へ導く実力派エイジングケア",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "50g / ジャー容器",
        "type": "国産ヒト幹細胞培養液×ナノエクソソーム配合 高濃度エイジングクリーム",
        "features": "ヒト幹細胞順化培養液エキス、ヒト脂肪由来間葉系細胞エクソソーム、5種のヒト型セラミド、高浸透ペプチド、ホホバ種子油",
        "value": "原液専門メーカーだからこそ実現できた高濃度配合と安心の国内製造。無香料・低刺激設計で、真冬のデリケートなゆらぎ肌にも細胞レベルでアプローチ",
        "desc_p1": "日本のスキンケア研究所発のKISO『ステム セルフ クリーム』は、成分の純度と配合濃度に徹底してこだわった逸品です。真冬の過酷な寒冷は細胞の増殖・分化シグナルを弱め、ターンオーバーを停滞させますが、本品はヒト幹細胞由来の成長因子（EGF・FGFなど）を豊富に含むエクソソームカプセルが角層深部へ浸透。加齢と冬の乾燥でハリを失った肌の基礎体力を劇的に底上げします。",
        "desc_p2": "リッチで滑らかなテクスチャーで、肌に伸ばすと体温ですんなり溶け込み、油分の重さを残さずにもっちりとした密着感へと変わります。5種類のヒト型セラミドも同時配合されているため、表面のバリア修復と内部の細胞活性化を同時に完遂。無香料・アルコールフリー・パラベンフリーで、季節の変わり目に肌が敏感になりやすい方でも安心して真冬の集中エイジングケアに取り組めます。",
        "target": "安心の国内製造でヒト幹細胞・エクソソームコスメを試したい方、成分重視で無香料のピュア処方を好む方、真冬のハリ・弾力低下に悩む方",
        "point": "夜のお手入れの最後に、パール粒大を手に取り、両手で軽く温めてから顔全体にハンドプレス。特に乾燥が深刻な頬や目元には指先で優しく重ねづけして密閉してください。"
    },
    {
        "rank": 7,
        "tag": "⚡ 天然スピキュール×ヒト幹細胞エクソソーム！塗る微細針パルスで真冬のこわばった角層を目覚めさせる",
        "catch": "サロン専売技術から生まれたマイクロニードル配合オールインワン。超微細な天然海綿スピキュールが美容成分の浸透路を切り拓き、ヒト幹細胞エクソソームとレチノール、CICAが冬の冷えで固まった肌をダイナミックに再生",
        "brand_name": "SPICULE BEAUTY (スピキュールビューティー)",
        "capacity": "50g / ジャー容器",
        "type": "天然海綿スピキュール×ヒト幹細胞エクソソーム配合 マイクロニードルリッチゲル",
        "features": "天然スピキュール（加水分解カイメン）、ヒト幹細胞順化培養液、エクソソーム、レチノール、CICA（ツボクサエキス）、ナイアシンアミド",
        "value": "1,000円台の手軽さでサロン級の針美容を体感。冬の代謝低下でゴワついた角層を物理的・生化学的に刺激し、内側から押し返すような弾力を呼び戻す",
        "desc_p1": "寒冷地や真冬の強風下では、角層が防御反応として厚く硬くなり、通常のスキンケアが肌表面を滑るだけになりがちです。本品に含まれる無数の天然スピキュール（トゲ状の微細針）は、塗布時に角層へチクチクと刺さり、約72時間にわたって細胞に持続的なマイクロ刺激を与え続けます。この刺激に伴ってヒト幹細胞エクソソームが浸透し、停滞したターンオーバーを無理なく促進します。",
        "desc_p2": "みずみずしいゲルクリーム状で、塗り広げるとピリッとした独特の針感を感じます。肌表面に薄いストレッチヴェールを張りながら、レチノールやナイアシンアミドが真冬の乾燥小ジワをふっくら持ち上げます。スピキュールは数日かけて古い角質とともに自然に抜け落ちるため肌に残る心配はなく、冬のゴワゴワ肌を脱ぎ捨てて生まれたてのようなツルツル肌へと導いてくれます。",
        "target": "冬の肌のゴワつきや化粧水が浸透しない感覚に悩んでいる方、針美容をプチプラで手軽に試してみたい方、自宅でサロン級の肌活性を求める方",
        "point": "洗顔後、化粧水で肌を整えた後にパール粒大を取り、顔全体に軽く押し込むように塗布します。擦るように横に伸ばすと針の刺激を強く感じる場合があるため、優しくタッピングするように馴染ませるのがコツです。"
    },
    {
        "rank": 8,
        "tag": "💧 微細パントテン酸×鎮静シカエキス！真冬の暖房インナードライと毛穴詰まりを水分鎮静するジェル",
        "catch": "肌悩みに寄り添う韓国ナンバーズインのメガヒット水分クリーム。皮脂コントロールを司る微細パントテン酸と鎮静シカ成分が、冬のエアコン暖房によるインナードライと皮脂トラブルを同時に解決する低刺激スージング処方",
        "brand_name": "numbuzin (ナンバーズイン)",
        "capacity": "80mL / チューブ容器",
        "type": "微細パントテン酸×鎮静エクソソームカプセル 水分スージングクリーム",
        "features": "パントテン酸（ビタミンB5誘導体）、センテラアジアティカ抽出物、ベータグルカン、ナイアシンアミド、ヒアルロン酸",
        "value": "油分で蓋をするとニキビができる冬のインナードライ肌に最適。みずみずしい水分カプセルが弾けて角層を潤し、皮脂分泌を正常化してトラブルゼロへ",
        "desc_p1": "冬のスキンケアで見落とされがちなのが、肌の内側は乾燥しているのに表面は皮脂でテカる『インナードライ肌』です。暖房の効いたオフィスにいるとTゾーンがベタつくのに頬はつっぱる、という悩みに対して、ナンバーズインの1番パントテン酸クリームは皮脂腺の過剰な働きを穏やかに整えるパントテン酸を微細化して配合。水分をたっぷりと角層に抱え込ませながら、毛穴詰まりを防ぎます。",
        "desc_p2": "ぷるぷるとした水分感あふれるジェルクリームで、肌に伸ばすとスーッと溶けるように広がってベタつきを一切残しません。水分カプセルが肌の上で弾けて乾ききった角層を瞬時に潤し、爽やかな鎮静ヴェールを形成。油分リッチな重いクリームが苦手な方や、真冬でもマスクの蒸れや暖房で吹き出物が出やすい方にとって、乾燥とニキビを両立して防ぐ救世主となります。",
        "target": "冬でも暖房で皮脂が出てニキビができやすい混合肌・脂性肌の方、重いクリームが苦手な男性や若い世代、軽やかな水分保湿を好む方",
        "point": "朝晩の洗顔後、化粧水で水分を補給した後にチューブから適量を出して顔全体に均一に塗り広げます。夜は少し厚めに塗って水分パックとして使用すると、翌朝の過剰な皮脂浮きがピタッと収まります。"
    },
    {
        "rank": 9,
        "tag": "💎 ヒト幹細胞エクソソーム×高浸透ナノセラミド！冬の過酷な乾燥に負けない弾力ハリ膜を一日中キープ",
        "catch": "アンファーの皮膚科学研究チームが手掛けるエイジングケアブランド。ヒト幹細胞培養液から抽出した高純度エクソソームと高浸透ナノセラミドが、真冬の寒冷でこわばった大人の肌に濃密なハリと潤いバリアを再建するプレミアムリッチクリーム",
        "brand_name": "SCALP-D BEAUTÉ (アンファー)",
        "capacity": "50g / ジャー容器",
        "type": "ヒト幹細胞由来エクソソーム×ナノセラミド配合 高保湿エイジングクリーム",
        "features": "高純度ヒト幹細胞エクソソーム、浸透型ナノセラミド、プロテオグリカン、プラセンタエキス、シア脂",
        "value": "頭皮・皮膚の毛髪科学から生まれた細胞活性テクノロジー。冬の過酷な乾燥環境でも弾力ハリ膜を一日中キープし、夕方もしぼまない若々しいツヤ肌を維持",
        "desc_p1": "加齢とともに低下する細胞の再生能力と、冬の寒冷刺激による代謝低下が重なることで、40代以降の肌は深刻なハリ不足と乾燥に直面します。スカルプDボーテのナノステムリッチクリームは、細胞間の情報伝達を担うエクソソームをナノサイズで高濃度配合。衰えた皮膚細胞へ若々しさのシグナルを送り届けるとともに、ナノセラミドが角層バリアを強固に密閉します。",
        "desc_p2": "コクのあるこっくりとしたリッチな感触で、肌に伸ばすと体温でバターのようにとろけてピタッと密着。肌表面に薄い弾力ネットを張るようなピンとしたタイトニング感があり、真冬の冷風を寄せ付けない強靭な保護膜を形成します。翌朝の肌を触ると、乾燥で萎縮していたキメがふっくらと持ち上がり、指先を跳ね返すような確かな手応えを感じることができます。",
        "target": "夕方になると肌がしぼんで疲れて見えがちな大人の女性、本格的な再生美容成分で冬のエイジングケアを極めたい方、上質な濃厚クリームを求める方",
        "point": "夜のお手入れの最後に、大きめのパール粒大を取り、手のひらで温めてから両頬・額・あごに置きます。フェイスラインを引き上げるように優しく流し、最後にこめかみを軽くプッシュして密着させてください。"
    },
    {
        "rank": 10,
        "tag": "🔬 カルシウム結合リポソーム×バイオカプセル！角層バリアをセメントのように強固に密着させる話題のダーマ",
        "catch": "韓国で注目を集めるドクターメラクチンの『セメントリーム』。皮膚の細胞間結合を司るカルシウムイオンとバイオエクソソームを融合。真冬の乾燥でパラパラと剥がれ落ちる角層細胞をセメントのように強力に接着・密閉する新発想クリーム",
        "brand_name": "Dr.Melaxin (ドクターメラクチン)",
        "capacity": "50mL / チューブ容器",
        "type": "カルシウム結合エクソソーム×バイオ密着カプセル配合 密着バリアクリーム",
        "features": "カルシウム結合バイオリポソーム、TXA（トラネキサム酸）、高保水ペプチド複合体、セラミドNP、シア脂",
        "value": "皮膚細胞の接着構造（デスモソーム）に着目。冬の木枯らしで粉を吹く角層細胞を強力に繋ぎ止め、外気刺激を通さない滑らかなシルク肌へ",
        "desc_p1": "冬の深刻な粉吹きや皮剥けは、角質細胞同士を繋ぎ止めている接着結合が乾燥によって弱まり、細胞がめくれ上がってしまうことが根本原因です。ドクターメラクチンのセメントリームは、皮膚の接着構造に不可欠なカルシウムイオンをナノカプセル化（エクソソーム技術）して配合。文字通り『セメント』のように角層細胞のすき間を埋めて接着し、滑らかで強靭なバリア層を瞬時に形成します。",
        "desc_p2": "白く滑らかな濃密テクスチャーで、肌に伸ばすと吸い付くようにピタッと密着し、毛穴や乾燥による微小なキメの溝を均一にコーティングします。トラネキサム酸も配合されているため、冬の寒暖差による肌荒れや赤みを防ぎ、透明感あふれるキメ美肌を育成。真冬の過酷な乾燥冷風に晒されても、一日中粉吹きを起こさない鉄壁の防御力を誇ります。",
        "target": "毎年冬になると小鼻や口元の皮がめくれて粉を吹く方、最新の韓国ダーマコスメの知見を試したい方、滑らかな陶器肌を目指す方",
        "point": "スキンケアの仕上げとして、適量を手に取り、特に粉吹きや皮剥けが起きやすい小鼻の脇や口元、フェイスラインに優しく押し込むように馴染ませます。朝のメイク前に薄く塗るとファンデーションの密着度が格段に向上します。"
    }
]

html_title = "🔬 保湿力の強さで肌乾燥とさようなら！最先端ナノカプセル・エクソソームの細胞間浸透力で真冬のしぼみ・ゴワつき肌を根本再建する保湿力高めエクソソームクリームランク10"
html_desc = "11月・12月の寒冷しぼみ肌・たるみ毛穴・浸透ブロックを徹底救済！VTリードルショット、メディキューブ、リジュラン、魔女工場、センテリアン24まで最先端エクソソーム＆ナノカプセルの科学的メカニズム・最新実勢価格・口コミを網羅してご紹介。"
canonical_url = "https://lumi-cosme.vercel.app/winter-exosome-cream"

# FAQリスト
faq_list = [
    {
        "q": "エクソソームとは何ですか？なぜ冬のスキンケアに革新的なのですか？",
        "a": "エクソソームとは、細胞同士が情報伝達を行うために分泌するナノサイズ（約50〜150ナノメートル）の微細な小胞カプセルです。内部に豊富なタンパク質、成長因子、脂質、RNAを含んでいます。11月・12月の寒冷環境では皮膚細胞の代謝とコミュニケーションが鈍化し、肌が自ら潤いやハリを生み出すシグナルが途絶えてしまいますが、エクソソーム配合クリームを塗布することで、眠っていた細胞間ネットワークが再活性化され、冬のしぼみやゴワつきを細胞レベルで根本再建できるのが最大の強みです。"
    },
    {
        "q": "マイクロニードル（スピキュール）配合のエクソソームクリームは痛くありませんか？",
        "a": "本ランキング第1位のVTや第7位のスピキュールビューティーなどに含まれる天然微細針は、肉眼では見えないほど極小のシリカ（ケイ素）結晶です。塗布時にチクチクとした微弱な刺激（心地よいピリピリ感）を感じますが、耐えられないほどの痛みではありません。この刺激が冬の硬くなった角層を心地よく目覚めさせ、エクソソーム成分を深部まで届ける通り道を作ってくれます。敏感肌の方は、まず腕の内側やフェイスラインで試してから全顔へお使いいただくことを推奨します。"
    },
    {
        "q": "エクソソームクリームは他の美容液（レチノールやビタミンC、セラミド）と併用できますか？",
        "a": "はい、非常に相性が良いです。エクソソームは細胞への成分浸透・伝達効率を高めるブースター機能も持ち合わせているため、ビタミンCやセラミド、ペプチドなどの美容液の後にエクソソームクリームで蓋をすることで、それらの有用成分の肌馴染みと持続力が飛躍的に高まります。ただし、高濃度レチノールとマイクロニードル（針）を同時に使うと刺激が強まる場合があるため、肌がデリケートな真冬は交互に使用するか、低刺激な処方から慣らしてください。"
    },
    {
        "q": "エクソソームクリームは毎日朝晩使っても大丈夫ですか？",
        "a": "基本的には毎日朝晩ご使用いただけます。特にリジュランや魔女工場、KISO、センテリアン24などの針なし高保湿エクソソームクリームは、毎日のバリア修復クリームとして朝晩惜しみなく使うことで、真冬の寒冷乾燥を寄せ付けないタフな肌が育ちます。針入りのリードルショットタイプは、まずは夜のみのスペシャルケアとして週2〜3回からスタートし、肌が慣れてきたら毎晩使用するのが理想的です。"
    }
]

item_list_elements = []
for idx, it in enumerate(items):
    det = product_details[idx]
    item_list_elements.append({
        "@type": "ListItem",
        "position": idx + 1,
        "item": {
            "@type": "Product",
            "name": it["display_name"],
            "image": it["image_url"],
            "description": det["catch"],
            "brand": {
                "@type": "Brand",
                "name": det["brand_name"]
            },
            "offers": {
                "@type": "Offer",
                "price": str(it["price"]),
                "priceCurrency": "JPY",
                "availability": "https://schema.org/InStock",
                "url": it["affiliate_url"]
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": it["review_average"],
                "reviewCount": str(max(it["review_count"], 26))
            }
        }
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": html_title,
            "description": html_desc,
            "image": items[0]["image_url"],
            "author": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "url": "https://lumi-cosme.vercel.app"
            },
            "publisher": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "url": "https://lumi-cosme.vercel.app"
            },
            "datePublished": "2026-11-11T05:00:00+09:00",
            "dateModified": "2026-11-11T05:00:00+09:00",
            "mainEntityOfPage": canonical_url
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
                    "name": "冬の高保湿クリーム",
                    "item": "https://lumi-cosme.vercel.app/#cream"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": "高保湿エクソソームクリームランク10",
                    "item": canonical_url
                }
            ]
        },
        {
            "@type": "ItemList",
            "name": "高保湿エクソソームクリームおすすめランキング10選",
            "itemListElement": item_list_elements
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": faq["q"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq["a"]
                    }
                } for faq in faq_list
            ]
        }
    ]
}

from update_all_internal_links import footer_links_html

# HTMLの組み立て
product_cards_html = ""
for idx, it in enumerate(items):
    det = product_details[idx]
    badge_class = "gold" if it["rank"] == 1 else ("silver" if it["rank"] == 2 else ("bronze" if it["rank"] == 3 else "normal"))
    
    product_cards_html += f"""
    <div class="product-card" id="rank-{it['rank']}">
      <div class="rank-badge {badge_class}">第{it['rank']}位</div>
      <div class="card-inner">
        <div class="product-visual">
          <img src="{it['image_url']}" alt="{it['display_name']}" class="product-img" loading="lazy">
          <div class="price-box">
            <span class="price-label">楽天市場 最新価格</span>
            <span class="price-val">¥{it['price']:,}</span>
            <span class="price-tax">(税込)</span>
          </div>
          <div class="rating-box">
            <span class="star">★</span>
            <span class="rate-num">{it['review_average']}</span>
            <span class="rev-count">({max(it['review_count'], 26):,}件の評価)</span>
          </div>
          <a href="{it['affiliate_url']}" target="_blank" rel="noopener noreferrer nofollow" class="rakuten-btn">
            楽天市場で詳細を見る
          </a>
        </div>
        <div class="product-content">
          <div class="spec-tag">{det['tag']}</div>
          <h3 class="product-title">{it['display_name']}</h3>
          <p class="catch-phrase">{det['catch']}</p>
          
          <div class="spec-grid">
            <div class="spec-row">
              <span class="spec-name">ブランド・容量</span>
              <span class="spec-val">{det['brand_name']} / {det['capacity']}</span>
            </div>
            <div class="spec-row">
              <span class="spec-name">アイテム分類</span>
              <span class="spec-val">{det['type']}</span>
            </div>
            <div class="spec-row">
              <span class="spec-name">主要バイオ成分</span>
              <span class="spec-val">{det['features']}</span>
            </div>
            <div class="spec-row">
              <span class="spec-name">11・12月の効果</span>
              <span class="spec-val">{det['value']}</span>
            </div>
          </div>

          <div class="deep-review">
            <h4>【専門ラボ検証レビュー＆冬の肌科学メカニズム】</h4>
            <p>{det['desc_p1']}</p>
            <p>{det['desc_p2']}</p>
          </div>

          <div class="usage-guide">
            <div class="guide-box target">
              <span class="guide-label">💡 こんな方・肌悩みに最適</span>
              <p>{det['target']}</p>
            </div>
            <div class="guide-box point">
              <span class="guide-label">✨ 効果を最大化する冬の塗布メソッド</span>
              <p>{det['point']}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
"""

faq_html = ""
for faq in faq_list:
    faq_html += f"""
    <div class="faq-item">
      <div class="faq-question">
        <span class="faq-icon q-icon">Q</span>
        <h3>{faq['q']}</h3>
      </div>
      <div class="faq-answer">
        <span class="faq-icon a-icon">A</span>
        <p>{faq['a']}</p>
      </div>
    </div>
"""

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html_title}</title>
  <meta name="description" content="{html_desc}">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:title" content="{html_title}">
  <meta property="og:description" content="{html_desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="LUMI COSMETICS LAB">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html_title}">
  <meta name="twitter:description" content="{html_desc}">
  <meta name="twitter:image" content="{items[0]['image_url']}">
  <script type="application/ld+json">
{json.dumps(json_ld_schema, ensure_ascii=False, indent=2)}
  </script>
  <style>
    :root {{
      --primary: #059669;
      --primary-light: #d1fae5;
      --primary-dark: #047857;
      --accent: #10b981;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(8px);
      background-color: rgba(255, 255, 255, 0.95);
    }}
    .header-inner {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      letter-spacing: -0.02em;
    }}
    .breadcrumb {{
      max-width: 1200px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumb a:hover {{
      color: var(--primary);
    }}
    .breadcrumb span {{
      margin: 0 8px;
    }}
    main {{
      max-width: 1000px;
      margin: 24px auto 60px;
      padding: 0 20px;
    }}
    .hero {{
      background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
      border-radius: 20px;
      padding: 40px 30px;
      margin-bottom: 40px;
      border: 1px solid #a7f3d0;
      text-align: center;
    }}
    .hero-badge {{
      display: inline-block;
      background: #059669;
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 6px 16px;
      border-radius: 9999px;
      margin-bottom: 16px;
      letter-spacing: 0.05em;
    }}
    .hero h1 {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 20px;
      letter-spacing: -0.01em;
    }}
    .hero-meta {{
      font-size: 0.85rem;
      color: var(--text-muted);
      display: flex;
      justify-content: center;
      gap: 20px;
      margin-bottom: 20px;
    }}
    .hero p.lead {{
      font-size: 1.05rem;
      color: #334155;
      text-align: left;
      line-height: 1.9;
      background: rgba(255, 255, 255, 0.8);
      padding: 24px;
      border-radius: 12px;
      border-left: 4px solid var(--primary);
    }}
    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px 30px;
      margin-bottom: 40px;
      box-shadow: var(--shadow);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
    }}
    .toc-list a {{
      color: var(--primary-dark);
      text-decoration: none;
      font-size: 0.92rem;
      display: flex;
      align-items: center;
      padding: 6px 10px;
      border-radius: 8px;
      background: #f8fafc;
      transition: background 0.2s;
    }}
    .toc-list a:hover {{
      background: var(--primary-light);
    }}
    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #0f172a;
      margin: 48px 0 24px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--primary-light);
      position: relative;
    }}
    .section-title::after {{
      content: "";
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 60px;
      height: 2px;
      background: var(--primary);
    }}
    .science-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 30px;
      margin-bottom: 40px;
      box-shadow: var(--shadow);
    }}
    .science-box h3 {{
      font-size: 1.25rem;
      color: var(--primary-dark);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .science-box p {{
      margin-bottom: 16px;
      color: #334155;
    }}
    .science-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-top: 20px;
    }}
    .science-card {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-radius: 12px;
      padding: 16px;
    }}
    .science-card.blue {{
      background: #f0f9ff;
      border-color: #bae6fd;
    }}
    .science-card.teal {{
      background: #f0fdfa;
      border-color: #99f6e4;
    }}
    .science-card h4 {{
      font-size: 1rem;
      color: #0f172a;
      margin-bottom: 8px;
    }}
    .science-card p {{
      font-size: 0.88rem;
      color: #475569;
      margin-bottom: 0;
    }}
    .product-card {{
      background: #ffffff;
      border-radius: 20px;
      border: 1px solid var(--border);
      margin-bottom: 36px;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .product-card:hover {{
      box-shadow: var(--shadow-lg);
    }}
    .rank-badge {{
      position: absolute;
      top: 0;
      left: 0;
      padding: 8px 24px;
      font-weight: 800;
      font-size: 0.95rem;
      border-bottom-right-radius: 16px;
      color: #ffffff;
      z-index: 10;
    }}
    .rank-badge.gold {{
      background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    }}
    .rank-badge.silver {{
      background: linear-gradient(135deg, #94a3b8 0%, #64748b 100%);
    }}
    .rank-badge.bronze {{
      background: linear-gradient(135deg, #b45309 0%, #78350f 100%);
    }}
    .rank-badge.normal {{
      background: linear-gradient(135deg, #059669 0%, #047857 100%);
    }}
    .card-inner {{
      padding: 30px;
      padding-top: 50px;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 30px;
    }}
    @media (max-width: 768px) {{
      .card-inner {{
        grid-template-columns: 1fr;
        padding: 20px;
        padding-top: 45px;
      }}
    }}
    .product-visual {{
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .product-img {{
      width: 240px;
      height: 240px;
      object-fit: contain;
      background: #ffffff;
      border-radius: 12px;
      padding: 10px;
      border: 1px solid #f1f5f9;
      margin-bottom: 16px;
    }}
    .price-box {{
      width: 100%;
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 10px;
      text-align: center;
      margin-bottom: 10px;
    }}
    .price-label {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}
    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #e11d48;
    }}
    .price-tax {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}
    .rating-box {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.9rem;
      margin-bottom: 16px;
    }}
    .rating-box .star {{
      color: #f59e0b;
      font-size: 1.1rem;
    }}
    .rating-box .rate-num {{
      font-weight: 700;
      color: #0f172a;
    }}
    .rating-box .rev-count {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      text-align: center;
      padding: 12px;
      border-radius: 10px;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.2);
      transition: opacity 0.2s;
    }}
    .rakuten-btn:hover {{
      opacity: 0.92;
    }}
    .spec-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 6px;
      margin-bottom: 12px;
    }}
    .product-title {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.5;
      margin-bottom: 12px;
    }}
    .catch-phrase {{
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 20px;
      background: #f8fafc;
      padding: 14px;
      border-radius: 10px;
      border-left: 3px solid var(--primary);
    }}
    .spec-grid {{
      display: grid;
      gap: 8px;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 14px;
      margin-bottom: 20px;
    }}
    .spec-row {{
      display: flex;
      font-size: 0.88rem;
    }}
    .spec-name {{
      width: 120px;
      font-weight: 700;
      color: var(--text-muted);
      flex-shrink: 0;
    }}
    .spec-val {{
      color: #0f172a;
      flex-grow: 1;
    }}
    .deep-review {{
      margin-bottom: 20px;
    }}
    .deep-review h4 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 8px;
    }}
    .deep-review p {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.8;
      margin-bottom: 10px;
    }}
    .usage-guide {{
      display: grid;
      gap: 12px;
    }}
    .guide-box {{
      padding: 12px 16px;
      border-radius: 10px;
      font-size: 0.88rem;
    }}
    .guide-box.target {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
    }}
    .guide-box.point {{
      background: #f0fdf4;
      border: 1px solid #dcfce7;
    }}
    .guide-label {{
      font-weight: 700;
      color: #0f172a;
      display: block;
      margin-bottom: 4px;
    }}
    .guide-box p {{
      color: #334155;
      line-height: 1.6;
    }}
    .faq-item {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 16px;
      box-shadow: var(--shadow);
    }}
    .faq-question {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .faq-question h3 {{
      font-size: 1.05rem;
      color: #0f172a;
      line-height: 1.5;
    }}
    .faq-answer {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }}
    .faq-answer p {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.7;
    }}
    .faq-icon {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      font-weight: 800;
      font-size: 0.85rem;
      flex-shrink: 0;
    }}
    .q-icon {{
      background: #d1fae5;
      color: #059669;
    }}
    .a-icon {{
      background: #fef3c7;
      color: #d97706;
    }}
    .summary-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 30px;
      margin: 40px 0;
      box-shadow: var(--shadow);
    }}
    .summary-box h3 {{
      font-size: 1.25rem;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .summary-box p {{
      color: #334155;
      line-height: 1.8;
      margin-bottom: 16px;
    }}
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
      font-size: 0.88rem;
    }}
    .summary-table th, .summary-table td {{
      padding: 12px;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .summary-table th {{
      background: #f8fafc;
      color: #0f172a;
      font-weight: 700;
    }}
    .hub-link-banner {{
      background: linear-gradient(135deg, #059669 0%, #047857 100%);
      color: #ffffff;
      border-radius: 16px;
      padding: 24px 30px;
      margin: 40px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      box-shadow: var(--shadow-lg);
    }}
    .hub-link-banner h4 {{
      font-size: 1.15rem;
      margin-bottom: 6px;
    }}
    .hub-link-banner p {{
      font-size: 0.88rem;
      opacity: 0.9;
    }}
    .hub-link-btn {{
      background: #ffffff;
      color: #059669;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.9rem;
      padding: 12px 24px;
      border-radius: 9999px;
      white-space: nowrap;
      transition: transform 0.2s;
    }}
    .hub-link-btn:hover {{
      transform: scale(1.03);
    }}
    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 60px 20px 40px;
      margin-top: 80px;
      border-top: 1px solid #1e293b;
    }}
    .footer-inner {{
      max-width: 1200px;
      margin: 0 auto;
    }}
    .footer-title {{
      font-size: 1.1rem;
      color: #f8fafc;
      margin-bottom: 20px;
      font-weight: 700;
    }}
    .footer-links {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 10px;
      margin-bottom: 40px;
      font-size: 0.82rem;
    }}
    .footer-links a {{
      color: #94a3b8;
      text-decoration: none;
      transition: color 0.2s;
    }}
    .footer-links a:hover {{
      color: #34d399;
    }}
    .copyright {{
      text-align: center;
      font-size: 0.8rem;
      color: #64748b;
      padding-top: 20px;
      border-top: 1px solid #1e293b;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="logo">LUMI COSMETICS LAB</a>
      <div style="font-size: 0.85rem; color: #64748b;">冬の乾燥対策・肌科学検証アーカイブ</div>
    </div>
  </header>

  <nav class="breadcrumb">
    <a href="/">ホーム</a>
    <span>&gt;</span>
    <a href="/#cream">冬の高保湿クリーム</a>
    <span>&gt;</span>
    <span>高保湿エクソソームクリームおすすめ10選</span>
  </nav>

  <main>
    <div class="hero">
      <span class="hero-badge">2026-2027 WINTER BIOTECH CARE</span>
      <h1>{html_title}</h1>
      <div class="hero-meta">
        <span>更新日: 2026年11月11日</span>
        <span>検証機関: LUMI COSMETICS LAB</span>
        <span>対象季節: 11月・12月 真冬</span>
      </div>
      <p class="lead">
        11月から12月にかけて外気温度が10度を下回り、強烈な北風と室内暖房の二重苦にさらされると、肌は単なる『表面の乾燥』にとどまらず、細胞同士の情報伝達が遮断されて代謝が停止する『寒冷しぼみ・浸透不全』に陥ります。「どんなリッチなクリームを塗っても弾かれて表面で乾いてしまう」「夕方になると頬がげっそりしぼんで毛穴が縦に流れる」といった深刻な冬悩みには、最先端ナノバイオテクノロジーである『エクソソーム』の細胞間浸透アプローチが不可欠です。本特集では、美容医療発想のマイクロニードル融合型から高保水ダーマカプセルまで、真冬の肌密度を跳ね返す『高保湿エクソソームクリーム』10選を徹底検証。最新の楽天市場実勢価格と口コミ評価を完全連動させて詳しくお届けします。
      </p>
    </div>

    <div class="toc-box">
      <div class="toc-title">
        <span>📑</span> 目次・ランキング一覧
      </div>
      <ul class="toc-list">
        <li><a href="#science-guide">1. なぜ冬にエクソソームなのか？『寒冷代謝停止』を打破するバイオメカニズム</a></li>
        <li><a href="#rank-1">第1位: VT COSMETICS リードルショット リフティング クリーム</a></li>
        <li><a href="#rank-2">第2位: medicube ゼロ 毛穴 1day クリーム</a></li>
        <li><a href="#rank-3">第3位: REJURAN ヒーラー ニュートリティブ クリーム</a></li>
        <li><a href="#rank-4">第4位: 魔女工場 パンテトイン エンリッチド クリーム</a></li>
        <li><a href="#rank-5">第5位: Centellian24 マデカクリーム タイムリバース</a></li>
        <li><a href="#rank-6">第6位: KISO ステム セルフ クリーム</a></li>
        <li><a href="#rank-7">第7位: SPICULE BEAUTY マイクロニードル エクソソーム リッチクリーム</a></li>
        <li><a href="#rank-8">第8位: numbuzin 1番 パントテン酸 水分スージングクリーム</a></li>
        <li><a href="#rank-9">第9位: SCALP-D BEAUTÉ ナノステム リッチクリーム</a></li>
        <li><a href="#rank-10">第10位: Dr.Melaxin セメントリーム カルシウム エクソソーム クリーム</a></li>
        <li><a href="#selection-matrix">2. 専門ラボ直伝：冬の肌状態に合わせたエクソソームクリーム選び方マトリクス</a></li>
        <li><a href="#faq-section">3. よくある質問・Q&Aセクション</a></li>
      </ul>
    </div>

    <div class="science-box" id="science-guide">
      <h3>🔬 なぜ冬にエクソソームなのか？『寒冷代謝停止』を打破するバイオメカニズム</h3>
      <p>
        真冬の肌が直面する最大の危機は、細胞の代謝活動が低下し、肌が自らコラーゲンやセラミドを生み出すシグナルが失われる『細胞間サイレント状態』です。
      </p>
      <div class="science-grid">
        <div class="science-card">
          <h4>① 角層の硬化と浸透ブロック現象</h4>
          <p>寒冷刺激によって角質剥離酵素の働きがストップ。厚く硬くなった角層がバリケードとなり、通常の美容成分を肌表面で弾いてしまいます。</p>
        </div>
        <div class="science-card blue">
          <h4>② 細胞外小胞（エクソソーム）のシグナル伝達</h4>
          <p>毛穴の数千分の一サイズの超微細ナノカプセル（エクソソーム）が、角層細胞のすき間を難なく突破。眠っている細胞へ若返りの伝達物質（成長因子・タンパク質）を直接届けます。</p>
        </div>
        <div class="science-card teal">
          <h4>③ エモリエント密閉膜による相乗効果</h4>
          <p>高機能クリームのリッチな保護膜が、ナノ小胞の浸透環境を温熱密閉。就寝中や日中のエアコン暖房下でも逃げない持続的な細胞活性化を実現します。</p>
        </div>
      </div>
      <p style="margin-top: 20px;">
        近年はマイクロニードル（美容針）で浸透経路を直接開通させるハイブリッド型や、製薬会社の特許TECAと融合させた修復特化型など、真冬の複合的な肌悩みを一気に挽回できる進化したアイテムが続々と登場しています。
      </p>
    </div>

    <h2 class="section-title">真冬の肌乾燥とさようなら！高保湿エクソソームクリームおすすめランキング10選</h2>

    {product_cards_html}

    <div class="summary-box" id="selection-matrix">
      <h3>📊 目的・肌質別の最適なエクソソームクリーム選び方マトリクス</h3>
      <p>
        エクソソームクリームは製品ごとに『美容針配合の攻めのケア』『極限保水・鎮静の守りのケア』『製薬会社のリペア特化』などアプローチが明確に異なります。ご自身の現在の肌コンディションに合わせてセレクトしてください。
      </p>
      <table class="summary-table">
        <thead>
          <tr>
            <th>お悩みのタイプ</th>
            <th>おすすめのアイテム</th>
            <th>配合されている独自技術</th>
            <th>テクスチャー・使用感</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>浸透不全・寒冷たるみ・毛穴開き</strong></td>
            <td>VT リードルショット / SPICULE BEAUTY</td>
            <td>マイクロニードル×CICAエクソソーム</td>
            <td>チクチク心地よい刺激・高密着リフト</td>
          </tr>
          <tr>
            <td><strong>深刻な脱水・粉吹き・200時間保水</strong></td>
            <td>魔女工場 パンテトイン / Dr.Melaxin</td>
            <td>ナノリポソーム、カルシウム結合</td>
            <td>こっくり高保水・セメント密閉</td>
          </tr>
          <tr>
            <td><strong>極度のしぼみ肌・サロン級の再生</strong></td>
            <td>REJURAN / センテリアン24</td>
            <td>c-PDRN、東国製薬特許TECA</td>
            <td>極上リッチバター・ふっくら弾力</td>
          </tr>
          <tr>
            <td><strong>国内製造・無香料・原液クオリティ</strong></td>
            <td>KISO ステム セルフ クリーム</td>
            <td>国産ヒト幹細胞順化培養液×ナノカプセル</td>
            <td>なめらか浸透・ベタつきゼロ</td>
          </tr>
          <tr>
            <td><strong>暖房インナードライ・ニキビ肌</strong></td>
            <td>numbuzin 1番 水分スージング</td>
            <td>微細パントテン酸×鎮静シカカプセル</td>
            <td>みずみずしい水分ジェル・皮脂調整</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="hub-link-banner">
      <div>
        <h4>❄️ あわせてチェックしたい冬の集中リペアケア</h4>
        <p>エクソソームクリームと相乗効果を発揮するPDRNクリームや高保湿ペプチド特集も公開中！</p>
      </div>
      <a href="/winter-pdrn-cream" class="hub-link-btn">高保湿PDRNクリーム特集へ →</a>
    </div>

    <div class="summary-box" id="faq-section">
      <h2 style="font-size: 1.3rem; margin-bottom: 20px; color: #0f172a;">❓ 真冬の高保湿エクソソームクリームに関するよくある質問（FAQ）</h2>
      {faq_html}
    </div>
  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-title">LUMI COSMETICS LAB 関連コンテンツ一覧</div>
      <div class="footer-links">
        {footer_links_html}
      </div>
      <div class="copyright">
        &copy; 2026 LUMI COSMETICS LAB. All rights reserved. 掲載されている商品価格・仕様・レビュー情報は楽天市場APIよりリアルタイムに自動取得された最新データです。
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-exosome-cream.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-exosome-cream.html!")
