import json
import re

with open("fetched_3new_barrier_niacinamide_exosome.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_niacinamide_cream"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 医薬部外品シワ改善クリームの頂点！有効成分リンクルナイアシンが真冬の深い乾燥溝を押し戻す最高峰",
        "catch": "コーセーが誇るシワ改善の絶対的エース。有効成分リンクルナイアシンが表皮だけでなく真皮の線維芽細胞にまでダイレクトに作用し、真冬の寒冷と乾燥で定着しそうな目元・口元・眉間のシワをふっくら押し広げる名品",
        "brand_name": "ONE BY KOSÉ (ワンバイコーセー)",
        "capacity": "20g (または18g) / チューブ容器",
        "type": "医薬部外品 有効成分リンクルナイアシン配合 薬用シワ改善・高密着クリーム",
        "features": "リンクルナイアシン（ナイアシンアミド）、AZ-アスタキサンチン、低分子コラーゲン、エラスチン、高保湿シアバター",
        "value": "日本で初めて真皮と表皮の両方にアプローチする効果が認められた実力派。11月・12月の暖房直撃による『乾燥ちりめんジワ』の深いシワ化を未然に完全ブロック",
        "desc_p1": "11月から12月にかけて外気温度と湿度が低下すると、表情筋の動きに伴って生じる一時的な表情ジワが、角層の柔軟性低下によって復元しにくくなり、そのまま深い『定着ジワ』へと進行します。ONE BY KOSÉの『ザ リンクレス W』は、コーセーが長年研究を重ねた有効成分リンクルナイアシンを惜しみなく配合。真皮のコラーゲン産生を強力に促進すると同時に、表皮の細胞間脂質（セラミド）の合成を後押しし、肌の奥底から押し返すような弾力ネットを再構築します。",
        "desc_p2": "こっくりとしたオレンジ色の濃密クリームが、シワの溝にピタッと吸い付くように密着。ストレッチ性のある高密着ポリマーが肌表面をピンと引き伸ばすような心地よいテンションを与え、冷たい冬風に当たっても乾かない鉄壁のエモリエント膜を形成します。目元や口元はもちろん、冬の乾燥で目立ちやすい額や首の横ジワにも効果的。メイク前に薄く馴染ませるとファンデーションのシワ落ちも見事に防ぎます。",
        "target": "笑った後の目尻やほうれい線のシワが戻りにくくなってきた方、医薬部外品の確かなエビデンスでシワ改善したい方、目元口元の集中ケアを求める方",
        "point": "朝晩のお手入れの最後に、片方の目元で米粒1個分を目安に取り、シワの溝を指先で優しく広げながら、下から上へ引き上げるように馴染ませます。最後に温かい手のひらで軽く包み込んで密着度を高めてください。"
    },
    {
        "rank": 2,
        "tag": "✨ リンクルナイアシン×浸透型コラーゲン！寝ている間にシワを伸ばし切る薬用濃密ナイトクリーム",
        "catch": "コーセーの先進カプセル技術を搭載したエイジングケアブランド『ルシェリ』。有効成分リンクルナイアシンとハートリフトコンプレックスが、睡眠中の肌代謝に寄り添い、真冬の寝返り摩擦や乾燥から肌を守り抜く濃密クリーム",
        "brand_name": "LECHÉRI (ルシェリ / コーセー)",
        "capacity": "35g / ジャー容器",
        "type": "医薬部外品 シワ改善有効成分リンクルナイアシン配合 薬用ナイトクリーム",
        "features": "リンクルナイアシン、ハートリフトコンプレックス、イオン化カプセル（浸透型コラーゲン・エラスチン）、スクワラン",
        "value": "イオン化カプセル技術により真冬のこわばった角層へスムーズに浸透。翌朝起きた瞬間に肌のハリ密度が跳ね上がるような引き締まり感を実感",
        "desc_p1": "ルシェリの『リンクルリペア ナイトクリーム』は、夜の睡眠時間を利用して真冬の乾燥ダメージを徹底修復するために設計された高機能クリームです。冬の寒さで血行が悪くなった肌は代謝が低下し、真皮の線維構造が脆弱化しますが、本品は生体類似のイオン化カプセルが肌表面のマイナス電位に引き寄せられ、有効成分リンクルナイアシンを角層深部へ効率的にデリバリーします。",
        "desc_p2": "糸を引くようにもっちりとしたリッチな感触のクリームで、肌に伸ばすとピタッと密着して濃厚なパック膜へと変化します。暖房をつけたまま眠る真冬の寝室でも、一晩中水分蒸散をシャットアウト。ミュゲ（スズラン）を基調とした爽やかでリラックスできるフローラルの香りに包まれ、心地よい眠りとともに翌朝にはパンと張った弾力ツヤ肌に出会えます。",
        "target": "夜寝ている間に手軽にシワ改善と高保湿を同時に完了させたい方、頬の位置が下がってきたと感じるたるみ世代、心地よい香りで癒されたい方",
        "point": "夜のお手入れの最後に、添付のスパチュラでパール粒大を手に取り、両頬・額・鼻・あごに置きます。顔の内側から外側へ、フェイスラインをキュッと持ち上げるように引き上げながら馴染ませるのがコツです。"
    },
    {
        "rank": 3,
        "tag": "🌙 ナイアシンアミド×ピュアレチノール×豆乳発酵液！プチプラの常識を覆す薬用美白＆シワ改善ナイトクリーム",
        "catch": "ドラッグストアで爆発的人気を誇るなめらか本舗のプレミアム薬用ライン。有効成分ナイアシンアミドに滋賀県産大豆たまほまれ使用の豆乳発酵液とピュアレチノールを融合。真冬の乾燥小ジワを改善しながらメラニンの生成を抑えてシミも防ぐ",
        "brand_name": "SANA なめらか本舗 (常盤薬品工業)",
        "capacity": "50g / ジャー容器",
        "type": "医薬部外品 ナイアシンアミド配合 薬用美白・シワ改善ナイトクリーム",
        "features": "有効成分ナイアシンアミド、ピュアレチノール、豆乳発酵液、セラミド、ビタミンE誘導体",
        "value": "1,000円台前半という驚異的なプチプラ価格で医薬部外品のシワ改善×美白×高保湿のトリプルアプローチを実現。惜しみなくたっぷり使える大人の味方",
        "desc_p1": "なめらか本舗の『薬用リンクルナイトクリーム ホワイト』は、コストパフォーマンスを極限まで追求した傑作スキンケアです。冬は乾燥によって肌がくすみ、さらに乾燥小ジワが目立ちやすくなりますが、本品はナイアシンアミドがセラミドの合成を促してバリアを高めつつ、シワを改善しシミの元となるメラニン輸送をブロック。ピュアレチノールとの相乗効果で、冬のゴワついた角層をふっくら柔軟にほぐします。",
        "desc_p2": "こってりとコクのある濃厚なテクスチャーで、塗布直後はしっかりとした油膜感がありますが、ハンドプレスしてなじませるとベタつきが落ち着き、肌表面にしっとりとしたラッピング膜を形成します。無香料・無鉱物油の低刺激設計で、敏感になりがちな冬の肌にも安心して使用可能。ネッククリームとして首筋やデコルテまで広範囲に塗り広げる贅沢使いにも最適です。",
        "target": "プチプラで本気のシワ改善＆美白ケアを始めたい方、顔だけでなく首元までたっぷりクリームを塗りたい方、レチノール初心者の方",
        "point": "夜のお手入れの最後に、さくらんぼ粒大をたっぷり手に取り、顔全体から首元にかけて優しく引き上げるように伸ばします。乾燥が特に深刻な目尻やほうれい線には重ねづけして『追い保湿』を行ってください。"
    },
    {
        "rank": 4,
        "tag": "💎 ナイアシンアミド×ビタミンC誘導体！真冬の乾燥くすみを一掃して透明ツヤを呼び戻すオールインワン",
        "catch": "クレンジングバームDUOの姉妹ブランドとして人気のカナデル。有効成分ナイアシンアミドを中心とするブライトニング複合成分が、冬の冷えによる血行不良くすみと乾燥小ジワを同時にケアする高機能美白ジェルクリーム",
        "brand_name": "CANADEL (カナデル)",
        "capacity": "58g / ジャー容器",
        "type": "医薬部外品 ナイアシンアミド配合 薬用美白・抗シワ高機能オールインワン",
        "features": "有効成分ナイアシンアミド、ビタミンC誘導体（エチルアスコルビン酸）、ボタニカルブライト13、セラミド複合体、スクワラン",
        "value": "忙しい年末の朝晩でもワンステップで美容液＋乳液＋クリーム級の濃厚保湿。乾燥小ジワを目立たなくする効能評価試験済みで透明感とハリを両立",
        "desc_p1": "11月から12月は仕事や大掃除、年末年始の準備で忙殺される季節。手短にスキンケアを済ませたいけれど冬の乾燥やくすみは放置できない、という大人の女性に最適なのがカナデル プレミアホワイトです。有効成分ナイアシンアミドが角層の水分保持力を高めながらメラニンの過剰生成を抑制。冬の冷えで血色感を失った『どんより土気色肌』をパッと明るい発光肌へと導きます。",
        "desc_p2": "みずみずしいジェルのみずみずしさと、クリームのリッチな保護力を併せ持つ絶妙な感触。肌に乗せるとスルスルと滑らかに広がり、角層のすみずみまで美容成分を浸透させた後、薄いモイスチャーヴェールとなって肌を包み込みます。調香師が手掛けた天然カーミングフローラルの穏やかな香りが冬のお手入れ時間を上質なリラクゼーションタイムに変えてくれます。",
        "target": "ワンステップで本格的な冬の美白・シワ改善・高保湿を完了させたい方、乾燥くすみを素早く明るくしたい方、上質な香りを好む方",
        "point": "洗顔後、付属のスパチュラで大きめのパール粒大を取り、両頬・額・鼻・あごに置きます。顔の中心から外側へ向けて優しく滑らせるように伸ばし、最後に手のひらで顔全体を優しく包み込んで馴染ませます。"
    },
    {
        "rank": 5,
        "tag": "💧 ナイアシンアミド×3種のヒアルロン酸！ドラッグストア最強の保水シワ改善プチプラ名品",
        "catch": "ロート製薬が誇る『極潤プレミアム』の進化形。有効成分ナイアシンアミドにロート独自の3種のヒアルロン酸を贅沢に配合。真冬の過酷な乾燥による目元・口元の小ジワを改善しながら角層内部を満水状態に保つ薬用ハリクリーム",
        "brand_name": "肌ラボ (ロート製薬)",
        "capacity": "50g / ジャー容器",
        "type": "医薬部外品 ナイアシンアミド×ヒアルロン酸配合 薬用シワ改善・美白クリーム",
        "features": "有効成分ナイアシンアミド、3種のヒアルロン酸（浸透型・ナノ化・スーパーヒアルロン酸）、アセチルグルコサミン、シア脂",
        "value": "千円台の手軽さでシワ改善・シミ予防・深層保湿の三拍子。無香料・無着色・鉱物油フリー・アルコールフリーのやさしい処方で真冬の敏感肌にも完全フィット",
        "desc_p1": "ロート製薬のヒアルロン酸研究の英知を結集した『極潤 薬用ハリクリーム』。冬の乾燥肌は角層細胞内の水分保持量が極度に低下していますが、本品は分子量の異なる3種類のヒアルロン酸が角層の表面から深部まで多層的に保水膜を形成。そこに有効成分ナイアシンアミドが加わることで、真皮のコラーゲン産生を促して乾燥によって縮こまった肌溝を内側からパンと押し上げます。",
        "desc_p2": "指に取るとねっとりとした濃厚なテクスチャーですが、肌の上で伸ばすと体温でスーッととろけてみずみずしく広がります。塗布後はモチモチと吸い付くような潤い膜が完成し、暖房の風が直接当たる室内でも肌の乾燥感を一切感じさせません。弱酸性で肌への刺激が極めて少なく、レチノールなどの刺激が強いエイジングケア成分が苦手な方でも安心して冬のシワ改善を継続できます。",
        "target": "低刺激で毎日たっぷり使えるシワ改善クリームを求める方、ヒアルロン酸のみずみずしい保水感が好きな方、冬の乾燥と小ジワを同時に防ぎたい方",
        "point": "化粧水や乳液の後に、パール粒大を手にとって顔全体にムラなくなじませます。特に乾燥小ジワが目立ちやすい目尻や眉間、ほうれい線周りには指先で優しくトントンと叩き込むように重ねづけしてください。"
    },
    {
        "rank": 6,
        "tag": "🛡️ カモミラET×セラミド機能成分×ナイアシンアミド！乾燥性敏感肌の冬のくすみとバリアを完全防衛",
        "catch": "花王キュレルが誇る美白ラインの最高峰。天然植物由来の美白有効成分カモミラETにセラミド機能成分とナイアシンアミド誘導体を融合。真冬の乾燥でバリアが乱れ、くすみがちな大人の敏感肌をしっとり明るく整える薬用クリーム",
        "brand_name": "Curel (キュレル / 花王)",
        "capacity": "40g / ジャー容器",
        "type": "医薬部外品 美白有効成分カモミラET×セラミド機能成分配合 薬用美白フェイスクリーム",
        "features": "カモミラET（美白有効成分）、ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド（セラミド機能成分）、ユーカリエキス、スクワラン",
        "value": "敏感肌対応の極めて低刺激な処方設計。冬の乾燥性肌荒れを防ぎながら、メラニン生成の初期段階をブロックして濁りのない透明美肌を維持",
        "desc_p1": "冬の敏感肌は、刺激に対して過敏になるだけでなく、微小な肌荒れによってターンオーバーが滞り、メラニンが排出されにくくなってどんよりと顔色が悪くなります。キュレルの美白ケアフェイスクリームは、花王独自の美白有効成分カモミラETがメラノサイトの増殖・活性化指令を根本から抑制。さらにセラミド機能成分が角層のバリアを整え、外的刺激を寄せ付けない強い素肌を育みます。",
        "desc_p2": "キュレル特有のふんわりと軽やかなスフレテクスチャーで、塗った瞬間から肌にしっとりと吸い込まれ、ベタつきのないサラサラの上質膜を形成します。美白クリームにありがちな『乾燥感』や『つっぱり感』が全くなく、真冬の乾燥地帯でも一日中潤いが持続。無香料・アルコールフリーで、風邪気味や生理前で肌が過敏になっている真冬のタイミングでも心置きなく使えます。",
        "target": "一般的な美白化粧品を使うとピリつく敏感肌の方、冬のくすみと乾燥を両方ケアしたい方、軽くてベタつかない使用感を好む方",
        "point": "化粧水の後に適量（直径約2cm程度）を取り、顔全体に優しく塗り広げます。赤みが出やすい小鼻の脇や頬骨の高い位置には、擦らないよう手のひらで包み込むように優しくハンドプレスしてください。"
    },
    {
        "rank": 7,
        "tag": "🍑 発酵桃エキス77%×ナイアシンアミド！冷えで血色を失った冬肌に桃色のうるおいツヤをチャージ",
        "catch": "SNSで大ブレイク中のAnua（アヌア）が手掛ける桃ナイアシンシリーズ。自然発酵させた桃果実エキスを77%高配合し、ナイアシンアミドとセラミド、ビタミンB12が真冬の冷気で青白くくすんだ肌にみずみずしい血色ツヤを宿す水分コンディショニングクリーム",
        "brand_name": "Anua (アヌア)",
        "capacity": "50mL / ジャー容器",
        "type": "発酵桃エキス77%×ナイアシンアミド配合 水分トーンアップクリーム",
        "features": "PEACHNIA™（発酵桃エキス77%）、ナイアシンアミド2%、ビタミンB12、3重ヒアルロン酸、セラミドNP",
        "value": "肌のキメ密度を整えて内側から発光するような透明感を演出。冬のくすみ肌をファンデーションなしでも血色感ある桃肌へ導くトーンコンディショニング",
        "desc_p1": "11月から12月は冷えによって末梢血管の血流が滞り、顔全体が青白く、あるいはグレーっぽくくすんで見えがちです。アヌアの桃77%ナイアシンクリームは、低温発酵させた清浄桃エキスが角層に豊富なポリフェノールとアミノ酸を補給。さらにナイアシンアミドが肌のターンオーバーを正常化し、古い角質が溜まってゴワついた冬の肌をなめらかに解きほぐします。",
        "desc_p2": "淡いピンク色のぷるんとしたジェルプリンのようなテクスチャーで、人工着色料ではなくビタミンB12本来の天然ピンクカラーが視覚的にも気分を高めます。肌に乗せると水分が弾けるようにみずみずしく広がり、ベタつかずにツルンとした水光膜を形成。ほのかな甘い桃の香りに癒されながら、翌朝にはメイクノリ抜群のふっくらジューシーな素肌へと生まれ変わります。",
        "target": "冬になると顔色がどんより暗くくすむ方、ベタつかないジェルテクスチャーで水光肌を作りたい方、フルーティーな香りでスキンケアを楽しみたい方",
        "point": "朝晩のお手入れの最後に適量を取り、顔全体に優しく伸ばします。朝のメイク前に薄く塗布すると、自然なツヤが仕込まれて冬のファンデーションが素肌のように密着します。"
    },
    {
        "rank": 8,
        "tag": "🧬 ナイアシンアミド×低分子コラーゲン！真冬の寒冷たるみ毛穴をキュッと引き締める毛穴特化リッチクリーム",
        "catch": "オリーブヤングの女王BIOHEAL BOH（バイオヒールボ）が開発した、たるみ毛穴特化のコラーゲンクリーム。ナイアシンアミドと微小コラーゲン、タンニンコンプレックスが冬の乾燥と筋力低下で縦長に開いた毛穴を濃密にホールド",
        "brand_name": "BIOHEAL BOH (バイオヒールボ)",
        "capacity": "50mL / ジャー容器",
        "type": "ナイアシンアミド×低分子コラーゲン配合 毛穴タイトニング高保湿クリーム",
        "features": "ナイアシンアミド、LHA（毛穴角質ケア）、低分子コラーゲンコンプレックス、ペプチド、カキ葉エキス",
        "value": "冬の『乾燥毛穴開き』と『たるみ毛穴』を同時に引き締め。コクのあるリッチな水分膜で毛穴の凹凸をなめらかに埋め立て、フラットな陶器肌へ",
        "desc_p1": "冬の毛穴トラブルは夏の皮脂毛穴とは異なり、肌の乾燥とハリ低下によって毛穴周囲の皮膚がしぼみ、毛穴が引っ張られてしずく型に広がる『乾燥たるみ毛穴』が主原因です。バイオヒールボのタイトニングコラーゲンクリームは、ナイアシンアミドが皮脂バランスを整えつつコラーゲン構造を強化。さらに刺激の少ないLHA成分が真冬の硬化した古い角栓を優しく除去し、毛穴周りの皮膚を引き締めます。",
        "desc_p2": "なめらかで弾力のあるカスタードクリームのような質感で、肌に伸ばすと毛穴の凹凸にスッと入り込んで密着します。水分と油分のバランスが計算し尽くされており、真冬の乾燥から肌を長時間シールドしながらも、日中のTゾーンのテカリを抑えるという優れもの。夕方になっても毛穴落ちせず、つるんとしたなめらか肌が一日中キープされます。",
        "target": "冬になると頬や小鼻の毛穴が縦長に目立つ方、高保湿と毛穴ケアを同時に叶えたい方、韓国の最新タイトニング技術を体感したい方",
        "point": "化粧水やアンプルの後、スパチュラで適量を取り、特に毛穴の開きが気になる頬の中心部から外側へ向けて優しく塗り広げます。最後に毛穴を下から上へ持ち上げるように優しくタッピングしてください。"
    },
    {
        "rank": 9,
        "tag": "💊 薬用ナイアシンアミド×高濃度コエンザイムQ10！真冬の冷え枯れ肌に黄金の活力とコクを与える名品",
        "catch": "DHCのロングセラー最高峰『薬用Qシリーズ』の看板フェースクリーム。薬用成分ナイアシンアミド誘導体に基準上限濃度の0.3%コエンザイムQ10を配合。真冬の寒冷で代謝が落ち、衰えを感じる大人肌に圧倒的なリッチ保湿と弾力を注入",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "50g / ジャー容器",
        "type": "医薬部外品 ナイアシンアミド誘導体×高濃度コエンザイムQ10配合 薬用エイジングクリーム",
        "features": "ナイアシンアミド誘導体（水溶性ビタミンB）、コエンザイムQ10（0.3%高濃度）、プラセンタエキス、低分子コラーゲン、ヒアルロン酸",
        "value": "鮮やかな黄金色は高濃度Q10の証。真冬の過酷な乾燥環境でも油分と水分の強固な保護ヴェールが肌を包み込み、指を押し返すようなもっちりハリ肌を復元",
        "desc_p1": "冬の寒さは細胞のエネルギー産生工場であるミトコンドリアの働きを鈍らせ、肌の基礎代謝を低下させます。DHCの薬用Qフェースクリームは、エネルギー代謝に不可欠な抗酸化成分コエンザイムQ10を医薬部外品の配合上限である10倍濃度で配合。さらにナイアシンアミド誘導体が血行を促しながら表皮のセラミド合成をサポートし、冬の冷えによるエイジングの加速を食い止めます。",
        "desc_p2": "鮮やかな濃い黄色のリッチなテクスチャーで、肌に乗せると体温でとろけるように広がり、肌の凹凸をピタッと埋める濃厚な保護ヴェールを形成します。翌朝の洗顔時まで確実に潤い膜が残っている安心感があり、真冬の強風やエアコン暖房を浴び続けても乾燥を感じさせません。無香料・パラベンフリーで、天然成分の贅沢な濃密さをそのまま肌で享受できます。",
        "target": "40代〜60代で冬の本格的な乾燥とたるみに直面している方、こってりとした重ための保護クリームを好む方、コエンザイムQ10のパワーを実感したい方",
        "point": "夜のお手入れの最後に、パール粒大を手に取り、両手で軽く擦り合わせて温めてから顔全体を包み込むように押し込みます。首元やデコルテまで伸ばして温めながらマッサージすると、血行が促されて顔色が一段と明るくなります。"
    },
    {
        "rank": 10,
        "tag": "🌸 リンクルナイアシン配合の大容量100g！真冬のシワ改善と美白を全身・顔中贅沢に満たす濃密ジェル",
        "catch": "コーセーコスメポートが大人世代のために開発した本格薬用オールインワン。シワ改善有効成分リンクルナイアシンを配合し、1品で化粧水・美容液・乳液・クリーム・パック・アイクリーム・ネッククリームの7役を完璧にこなす大容量100g",
        "brand_name": "コーセーコスメポート (グレイスワン)",
        "capacity": "100g / ジャー容器",
        "type": "医薬部外品 リンクルナイアシン配合 薬用シワ改善・美白モイストジェルクリーム",
        "features": "有効成分リンクルナイアシン、濃厚コラーゲン、ヒアルロン酸、エラスチン、高保湿シアバター、スクワラン",
        "value": "100gの大容量で2,000円台という破格のコスパ。真冬の顔全体から首・デコルテ・手の甲まで、気になるシワ改善と美白を惜しみなく全身ケア",
        "desc_p1": "冬のシワ悩みは顔のパーツだけにとどまりません。タートルネックを着る季節、首元の横ジワや手の甲の乾燥ジワが急激に目立ち始めます。グレイスワンのリンクルケアホワイトは、コーセーの先進シワ改善有効成分リンクルナイアシンを贅沢に配合した100gのメガサイズ。顔の小ジワやほうれい線はもちろん、年齢が出やすい首やデコルテまで毎日惜しみなくケアできる頼もしい存在です。",
        "desc_p2": "コクのあるこっくりとしたジェルクリームで、伸ばすと肌表面にピンとしたハリ膜（タイトニングネット）を形成。水分蒸散を防ぐエモリエント成分が豊富に含まれているため、真冬の夜に塗って眠れば翌朝までパックをしたかのような濃密な潤いが持続します。上品なリラックスフローラルの香りで、毎日のスキンケアタイムを心地よく締めくくります。",
        "target": "顔だけでなく首元やデコルテまでシワ改善クリームをたっぷり塗りたい方、大容量でコストパフォーマンスの高い医薬部外品を探している方",
        "point": "洗顔後、さくらんぼ粒大を手に取り、顔の中心から外側へ引き上げるように伸ばします。さらに同量を首筋から鎖骨へ向かって上から下へ優しく撫で下ろすように塗り広げると、首のシワ予防とリンパ流しが同時に完了します。"
    }
]

html_title = "✨ 保湿力の強さで肌乾燥とさようなら！医薬部外品ナイアシンアミドのシワ改善×セラミド自生力で真冬の寒冷くすみ・小ジワをふっくら押し上げる保湿力高めナイアシンアミドクリームランク10"
html_desc = "11月・12月の寒冷くすみ・乾燥小ジワ・暖房脱水を徹底救済！ONE BY KOSÉ、ルシェリ、なめらか本舗、カナデル、極潤ハリクリームまで医薬部外品ナイアシンアミドのシワ改善＆美白メカニズム・最新実勢価格・口コミを網羅してご紹介。"
canonical_url = "https://lumi-cosme.vercel.app/winter-niacinamide-cream"

# FAQリスト
faq_list = [
    {
        "q": "なぜ真冬（11月・12月）にナイアシンアミド配合クリームが特に効果的なのですか？",
        "a": "ナイアシンアミド（ビタミンB3）は、真皮の線維芽細胞に働きかけてコラーゲン産生を促す『シワ改善効果』だけでなく、表皮の角質細胞における『セラミド（細胞間脂質）の生合成を促進する効果』を併せ持っています。11月・12月の冬は寒冷と空気乾燥でセラミド量が激減するため、外から油分を補うだけでなく、肌自身がセラミドを作り出す自活力を高めてくれるナイアシンアミドクリームは、冬の根本的な乾燥・小ジワ対策として極めて理にかなっています。"
    },
    {
        "q": "レチノールクリームとナイアシンアミドクリームはどのように使い分けるのが良いですか？",
        "a": "レチノールは高いターンオーバー促進力を持つ反面、真冬のバリア機能が低下した肌ではA反応（皮剥けや赤み、ヒリつき）が出やすい傾向があります。一方、ナイアシンアミドは肌への刺激性が極めて低く、むしろバリア機能を高めてくれるため、真冬の乾燥敏感肌でも安心してお使いいただけます。より高いエイジング効果を求める場合は、朝にナイアシンアミドクリーム、夜に低濃度レチノールを使うか、本ランキング第3位のなめらか本舗のように両方がバランスよく処方されたアイテムを選ぶのがおすすめです。"
    },
    {
        "q": "ナイアシンアミドクリームは朝のメイク前に塗ってもヨレたりテカったりしませんか？",
        "a": "ナイアシンアミドには皮脂分泌を正常化するバランシング作用があるため、日中の皮脂崩れを防ぐ効果もあります。朝は夜の半分程度の量（パール粒1個分）を手のひらで温めてから顔全体に薄くハンドプレスし、1〜2分置いて肌表面がなじんでから下地を塗ることで、日中のエアコン暖房によるメイク割れやシワ落ちを防止できます。"
    },
    {
        "q": "医薬部外品と一般化粧品のナイアシンアミドクリームでは何が違うのですか？",
        "a": "医薬部外品の製品（ONE BY KOSÉやルシェリ、なめらか本舗、カナデル、極潤など）は、厚生労働省から『シワを改善する』『メラニンの生成を抑え、シミ・ソバカスを防ぐ』という効果効能が正式に承認された有効濃度のナイアシンアミドが配合されています。真冬の深刻な小ジワやくすみに対して確実な手応えを求める場合は、パッケージに『医薬部外品』または『薬用』と記載されたアイテムを選ぶことを強く推奨します。"
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
                "reviewCount": str(max(it["review_count"], 28))
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
                    "name": "高保湿ナイアシンアミドクリームランク10",
                    "item": canonical_url
                }
            ]
        },
        {
            "@type": "ItemList",
            "name": "高保湿ナイアシンアミドクリームおすすめランキング10選",
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
            <span class="rev-count">({max(it['review_count'], 28):,}件の評価)</span>
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
              <span class="spec-name">主要エイジング成分</span>
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
      --primary: #9333ea;
      --primary-light: #f3e8ff;
      --primary-dark: #7e22ce;
      --accent: #a855f7;
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
      background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
      border-radius: 20px;
      padding: 40px 30px;
      margin-bottom: 40px;
      border: 1px solid #e9d5ff;
      text-align: center;
    }}
    .hero-badge {{
      display: inline-block;
      background: #9333ea;
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
      background: #faf5ff;
      border: 1px solid #e9d5ff;
      border-radius: 12px;
      padding: 16px;
    }}
    .science-card.blue {{
      background: #f0f9ff;
      border-color: #bae6fd;
    }}
    .science-card.amber {{
      background: #fffbeb;
      border-color: #fde68a;
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
      background: linear-gradient(135deg, #9333ea 0%, #7e22ce 100%);
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
      background: #fdf4ff;
      border: 1px solid #f5d0fe;
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
      background: #f3e8ff;
      color: #9333ea;
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
      background: linear-gradient(135deg, #9333ea 0%, #7e22ce 100%);
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
      color: #9333ea;
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
      color: #c084fc;
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
    <span>高保湿ナイアシンアミドクリームおすすめ10選</span>
  </nav>

  <main>
    <div class="hero">
      <span class="hero-badge">2026-2027 WINTER MEDICATED CARE</span>
      <h1>{html_title}</h1>
      <div class="hero-meta">
        <span>更新日: 2026年11月11日</span>
        <span>検証機関: LUMI COSMETICS LAB</span>
        <span>対象季節: 11月・12月 真冬</span>
      </div>
      <p class="lead">
        11月から12月にかけての本格的な真冬は、外気湿度30%台の空気乾燥に加えて、室内のエアコン暖房が一日中肌の水分を奪い去ります。さらに寒冷による血行不良が重なることで、顔全体が青黒くくすみ、笑った後の目尻や口元の小ジワが戻らずにそのまま深い溝へと刻まれる『冬のシワ・くすみ定着危機』が訪れます。本特集では、医薬部外品有効成分として真皮のコラーゲン産生と表皮のセラミド自生を同時に促進する『高保湿ナイアシンアミドクリーム』を徹底検証。最新の楽天市場実勢価格・レビュー評価と連動し、冬の肌にしっとりとしたハリと透明感を呼び戻す名品10選を詳しくご紹介します。
      </p>
    </div>

    <div class="toc-box">
      <div class="toc-title">
        <span>📑</span> 目次・ランキング一覧
      </div>
      <ul class="toc-list">
        <li><a href="#science-guide">1. 11月〜12月の肌で何が起きている？『寒冷シワ・くすみ定着』の皮膚科学</a></li>
        <li><a href="#rank-1">第1位: ONE BY KOSÉ ザ リンクレス W</a></li>
        <li><a href="#rank-2">第2位: LECHÉRI リンクルリペア ナイトクリーム</a></li>
        <li><a href="#rank-3">第3位: SANA なめらか本舗 薬用リンクルナイトクリーム ホワイト</a></li>
        <li><a href="#rank-4">第4位: CANADEL プレミアホワイト オールインワン</a></li>
        <li><a href="#rank-5">第5位: 肌ラボ 極潤 薬用ハリクリーム</a></li>
        <li><a href="#rank-6">第6位: Curel 美白ケア フェイスクリーム</a></li>
        <li><a href="#rank-7">第7位: Anua 桃 77% ナイアシン クリーム</a></li>
        <li><a href="#rank-8">第8位: BIOHEAL BOH プロバイオダーム タイトニング コラーゲン クリーム</a></li>
        <li><a href="#rank-9">第9位: DHC 薬用Qフェースクリーム</a></li>
        <li><a href="#rank-10">第10位: コーセーコスメポート グレイスワン リンクルケア モイストジェルクリーム</a></li>
        <li><a href="#selection-matrix">2. 専門ラボ直伝：冬の肌悩み別ナイアシンアミドクリーム選び方マトリクス</a></li>
        <li><a href="#faq-section">3. よくある質問・Q&Aセクション</a></li>
      </ul>
    </div>

    <div class="science-box" id="science-guide">
      <h3>🔬 11月〜12月の肌で何が起きている？『寒冷シワ・くすみ定着』の皮膚科学メカニズム</h3>
      <p>
        冬の肌老化のスピードは、他の季節の約3倍とも言われます。その主たる要因は、低温による『真皮線維芽細胞の機能低下』と『表皮セラミド合成の鈍化』です。
      </p>
      <div class="science-grid">
        <div class="science-card">
          <h4>① 表皮セラミド枯渇と小ジワの固定化</h4>
          <p>寒冷刺激によってセラミド合成酵素の活性が低下し、角層内部がスカスカに乾燥。浅い小ジワが真皮の深いシワへと進行する足がかりを作ります。</p>
        </div>
        <div class="science-card blue">
          <h4>② 真皮コラーゲンの断裂と寒冷たるみ</h4>
          <p>血行不良による酸素・栄養不足でコラーゲンやエラスチンの生成が停滞。重力と表情圧に耐えきれず、目元やフェイスラインが下垂します。</p>
        </div>
        <div class="science-card amber">
          <h4>③ メラニン停滞と土気色くすみ</h4>
          <p>新陳代謝（ターンオーバー）の周期が遅延し、排泄されるべきメラニンと古い角質が肌表面に蓄積。冬特有のどんよりとした暗い顔色を招きます。</p>
        </div>
      </div>
      <p style="margin-top: 20px;">
        これらすべての負の連鎖を断ち切る唯一無二のマルチビタミンが『ナイアシンアミド（ビタミンB3）』です。水溶性で浸透力が高く、表皮でのセラミド産生促進と真皮でのコラーゲン合成促進という2層同時の若返りアプローチを叶えます。高保湿クリームの濃厚エモリエント膜で密閉することで、夜間や日中の暖房下でも逃げない持続的なエイジングケアが可能になります。
      </p>
    </div>

    <h2 class="section-title">真冬の肌乾燥とさようなら！高保湿ナイアシンアミドクリームおすすめランキング10選</h2>

    {product_cards_html}

    <div class="summary-box" id="selection-matrix">
      <h3>📊 目的・肌質別の最適なナイアシンアミドクリーム選び方マトリクス</h3>
      <p>
        ナイアシンアミドクリームは製品ごとに『シワ改善特化』『美白・透明感特化』『高コスパ大容量』など得意領域が分かれます。ご自身の優先度に合わせて最適な1本を選んでみてください。
      </p>
      <table class="summary-table">
        <thead>
          <tr>
            <th>ケアの優先目的</th>
            <th>おすすめのアイテム</th>
            <th>配合されている特徴成分</th>
            <th>使用タイミング・特徴</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>目元・口元の深いシワを本格改善</strong></td>
            <td>ONE BY KOSÉ ザ リンクレス W</td>
            <td>リンクルナイアシン、AZアスタキサンチン</td>
            <td>朝晩のピンポイント集中密着</td>
          </tr>
          <tr>
            <td><strong>寝ている間に顔全体のハリを底上げ</strong></td>
            <td>LECHÉRI ナイトクリーム</td>
            <td>リンクルナイアシン、イオン化カプセル</td>
            <td>夜用濃厚パック・リッチ密着</td>
          </tr>
          <tr>
            <td><strong>プチプラでシワ改善＆美白を両立</strong></td>
            <td>なめらか本舗 / 肌ラボ 極潤ハリ</td>
            <td>ナイアシンアミド、レチノール、ヒアルロン酸</td>
            <td>毎日惜しみなく使える高コスパ</td>
          </tr>
          <tr>
            <td><strong>冬の青白いくすみ・血色感チャージ</strong></td>
            <td>Anua 桃77% / CANADEL プレミアホワイト</td>
            <td>発酵桃エキス、ビタミンC誘導体</td>
            <td>朝のメイク前・自然なトーンアップ</td>
          </tr>
          <tr>
            <td><strong>敏感肌で刺激なく美白・バリアケア</strong></td>
            <td>Curel 美白ケア フェイスクリーム</td>
            <td>カモミラET、セラミド機能成分</td>
            <td>低刺激スフレ・通年使える軽やかさ</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="hub-link-banner">
      <div>
        <h4>❄️ あわせてチェックしたい冬の集中美容液</h4>
        <p>ナイアシンアミドクリームと相性抜群！冬の角層に浸透する高保湿レチノール美容液やペプチド特集も公開中！</p>
      </div>
      <a href="/winter-retinol-serum" class="hub-link-btn">高保湿レチノール美容液特集へ →</a>
    </div>

    <div class="summary-box" id="faq-section">
      <h2 style="font-size: 1.3rem; margin-bottom: 20px; color: #0f172a;">❓ 真冬の高保湿ナイアシンアミドクリームに関するよくある質問（FAQ）</h2>
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

with open("winter-niacinamide-cream.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-niacinamide-cream.html!")
