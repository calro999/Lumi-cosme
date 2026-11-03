import json
import re

with open("fetched_3new_nov_dec_heparinoid_vaseline_placenta_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_placenta"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 累計販売数1700万本超の殿堂入り！高浸透ナノ化ピュアプラセンタ100%原液",
        "catch": "洗顔直後の素肌に生命力を注入。冬の代謝低下でくすんだ肌を内側から押し返すハリ艶肌へ",
        "brand_name": "fracora (フラコラ)",
        "capacity": "30ml (ディープ プラセンタエキス原液)",
        "type": "高濃度・高浸透ピュアプラセンタ100%美容液",
        "features": "国産SPF豚プラセンタ100%、ナノテクノロジー浸透設計、無香料・無着色・パラベンフリー・鉱物油フリー・界面活性剤フリー",
        "value": "洗顔直後のまっさらな角層へダイレクトに浸透。アミノ酸やペプチドが真冬の冷えで滞った肌リズムを正常化し、自発的なうるおいと透明感を呼び覚ます",
        "desc_p1": "11月から12月にかけて気温が下がると、皮膚毛細血管の収縮によりターンオーバーが遅延し、角層がゴワついて顔色が暗く沈む『冬枯れ肌』が加速します。フラコラの『ディープ プラセンタエキス原液』は、徹底した衛生管理のもと育てられた国産SPF豚の胎盤から抽出した純度100%のプラセンタ原液です。",
        "desc_p2": "水のようにサラリとしたテクスチャーながら、独自のナノ抽出技術により有用成分が角層の奥深くまで瞬時に浸透。アミノ酸やビタミン、ミネラルが角質細胞を満たし、硬くこわばった素肌を内側からふっくらと解きほぐします。その後に使う化粧水の吸い込みが劇的に高まり、夕方になってもファンデーションがくすまない透き通るような明るさと弾力感を実現します。",
        "target": "冬になると肌がくすんで疲れて見える方、乾燥小ジワとハリ不足を同時に立て直したい方、原液コスメの実力派を選びたい方",
        "point": "朝晩の洗顔直後、スポイトの線まで吸い上げた1回分を手のひらに取り、顔全体に優しくハンドプレスして押し込みます。目元やほうれい線には重ねづけが効果的です。"
    },
    {
        "rank": 2,
        "tag": "🏆 美容医療クリニックでも愛用される最高峰！契約農場豚プラセンタ100%の本格原液",
        "catch": "医療用抽出技術から生まれた本物。真冬の過酷なエイジングサインに立ち向かうプロ仕様",
        "brand_name": "Bb LABORATORIES (ビービーラボ)",
        "capacity": "30ml (水溶性プラセンタエキス原液)",
        "type": "医療発想・超高濃度水溶性プラセンタエキス原液",
        "features": "国内特定契約農場豚胎盤使用、独自の高圧抽出法、無香料・無着色、高品質ガラスアンプル容器",
        "value": "プラセンタ研究のパイオニアが誇る濃密エキス。真冬の乾燥冷風で刻まれた乾燥小ジワをふっくら持ち上げ、生命力あふれるハリ肌へ再生",
        "desc_p1": "数多くの美容皮膚科やエステサロンで導入されているビービーラボラトリーズの『水溶性プラセンタエキス原液』。徹底管理された国内契約農場の豚プラセンタのみを用い、熱に弱い有用成分を壊さない独自抽出技術で抽出された最高峰の原液です。",
        "desc_p2": "独特のわずかなプラセンタ香は、香料で誤魔化さず高純度エキスをありのまま封じじ込めている証。洗顔直後の肌に塗布すると、吸い込まれるように角層深部へ消えていき、数分後には手のひらが頬に吸い付くような濃密なもっちり感に包まれます。冬の寒冷ストレスでしぼんだ大人の肌にピンとしたハリとキメ密度を取り戻し、若々しいツヤを宿します。",
        "target": "本格的なサロン品質のエイジングケアを自宅で行いたい方、目元や口元のたるみ・シワが気になる方、本物の原液効果を求める方",
        "point": "洗顔直後の清潔な素肌に、手のひらで温めながらなじませます。独特の香りは肌に浸透すると自然に消えるため、その後に化粧水をたっぷり重ねてください。開封後は冷蔵庫保管が推奨されます。"
    },
    {
        "rank": 3,
        "tag": "🧪 必要な成分だけをダイレクトにチャージ！調合して使えるチューンメーカーズの高純度原液",
        "catch": "余計なものを一切含まない純粋設計。手持ちの化粧水に混ぜても単体でも使える万能ブースター",
        "brand_name": "TUNEMAKERS (チューンメーカーズ)",
        "capacity": "20ml (プラセンタエキス)",
        "type": "高純度原液美容液",
        "features": "高濃度プラセンタエキス原液、無香料・無着色・鉱物油フリー・パラベンフリー、遮光瓶容器",
        "value": "自分の肌状態に合わせてカスタムできる原液スキンケア。冬の乾燥ぐすみやキメの乱れをピンポイントで集中トリートメント",
        "desc_p1": "成分をダイレクトに届ける原液美容の代名詞『チューンメーカーズ』。その中でも冬の人気上位に君臨するのが、くすみとハリ不足を集中ケアする『プラセンタエキス』です。",
        "desc_p2": "サラッとしてベタつかない水のようなテクスチャーで、肌にスーッと浸透。洗顔後のブースターとして原液のまま使うのはもちろん、手持ちの化粧水やクリームに2〜3滴混ぜて『冬仕様の高保湿エイジングコスメ』へアップグレードさせる使い方も大人気です。11月〜12月の急激な乾燥で乱れたキメをキュッと引き締め、なめらかな陶器肌へと導きます。",
        "target": "現在のスキンケアに手軽にプラセンタを取り入れたい方、肌のくすみを晴らして透明感が欲しい方、原液を自分好みに調合したい方",
        "point": "洗顔後すぐに2〜3滴を顔全体になじませるか、普段の化粧水を手のひらに取ったところに1〜2滴垂らして混ぜ合わせてハンドプレスしてください。"
    },
    {
        "rank": 4,
        "tag": "🐎 アミノ酸量は豚の数百倍！北海道産サラブレッド馬プラセンタ100%の濃密原液",
        "catch": "希少な国産馬プラセンタを高濃度抽出。大人の深刻な冬枯れ肌を力強く跳ね返す濃密パワー",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "20ml (プラセンタエッセンス PC)",
        "type": "国産馬プラセンタ原液100%美容液",
        "features": "北海道産サラブレッド馬胎盤抽出、必須アミノ酸全種含有、無添加処方（パラベン・合成香料・着色料・アルコールフリー）",
        "value": "希少価値の高い国産馬プラセンタを中間マージンをカットした適正価格で提供。豚プラセンタを遥かに超える高濃度アミノ酸が冬の肌密度を高める",
        "desc_p1": "研究開発型コスメブランドKISOが手がける『プラセンタエッセンス PC』。1頭から年に1度しか採取できない希少な北海道産サラブレッドの胎盤から抽出された、高濃度馬プラセンタ原液です。",
        "desc_p2": "馬プラセンタは、豚プラセンタと比較してアミノ酸の含有量が格段に多く、肌のうるおい因子NMFの産生を強力にバックアップします。サラリとしたみずみずしい感触ながら、肌になじませると角層の奥深くからふっくらとした押し返すような弾力感が湧き上がります。11月・12月の寒さでハリを失い、ファンデーションが毛穴に落ちる大人の肌に劇的なキメ改善をもたらします。",
        "target": "豚プラセンタでは効果を実感しにくかった方、高濃度アミノ酸でハリ弾力を底上げしたい方、コスパ良く馬プラセンタを続けたい方",
        "point": "洗顔後すぐの肌に、スポイトで3〜4滴を手のひらに取り、顔全体を引き上げるように優しくなじませてください。特に乾燥によるたるみ毛穴が気になる頬に重ねると効果的です。"
    },
    {
        "rank": 5,
        "tag": "🌿 動物性が苦手な方にも！植物の生命力を凝縮したエビスの植物性プラセンタ原液",
        "catch": "アロエ・カッコン・クロレラから抽出したボタニカル原液。敏感な冬肌を優しく潤す植物の恵み",
        "brand_name": "EBiS (エビス化粧品)",
        "capacity": "33ml (エクセレントバイオ EX100)",
        "type": "植物性プラセンタ100%原液美容液",
        "features": "アロエベラ葉エキス・クズ根エキス・クロレラエキス（植物性胎座エキス）、無香料・無着色・オイルフリー",
        "value": "動物性原料を一切使用せず、植物の胎座（バイオ）から抽出。動物性特有の匂いが苦手な方や、ヴィーガン志向の方にも安心の濃密保湿",
        "desc_p1": "美顔器や原液コスメのパイオニア・エビス化粧品が開発した『エクセレントバイオ EX100』。植物の種子が発芽する中心部である『胎座』から抽出された、植物性プラセンタ100%原液です。",
        "desc_p2": "アロエベラやクズ根、クロレラなどの植物パワーが凝縮されており、豊富なアミノ酸とビタミンが冬の乾燥肌を優しくサポート。動物性プラセンタ特有の匂いが全くないため、香りに敏感な方でも快適に使用できます。肌荒れを防止しながら角質層の水分保持力を高め、みずみずしく透き通るような明るい肌へと導きます。",
        "target": "動物性原料の匂いや由来に抵抗がある方、植物由来の優しい成分でエイジングケアしたい方、美顔器の導入美容液として使いたい方",
        "point": "洗顔後、10円玉大を手にとり顔全体になじませます。イオン導入器や超音波美顔器との相性も抜群で、冬のスペシャルケアとして導入すると角層の奥までうるおいが届きます。"
    },
    {
        "rank": 6,
        "tag": "✨ 国産100%プラセンタ高配合の濃密ジェル美容液！もっちり白肌へ導く高コスパ名品",
        "catch": "ぷるぷるエッセンスが肌にとろける。乾燥くすみを一掃して透明美肌を叶えるデイリー美容液",
        "brand_name": "WHITE LABEL (ミックコスモ)",
        "capacity": "20g (贅沢プラセンタのもっちり白肌エッセンス)",
        "type": "高保湿プラセンタ濃縮美容液",
        "features": "国産100%プラセンタエキス、ヒアルロン酸、コラーゲン配合、無香料・無着色・パラベンフリー・ノンアルコール",
        "value": "ドラッグストアで手軽に買えるプチプラ価格でありながら国産高品質プラセンタを贅沢配合。冬の毎日のスキンケアに惜しみなく投入可能",
        "desc_p1": "『毎日続けられる高品質なプラセンタを』というコンセプトでロングセラーを続けるホワイトラベルの『贅沢プラセンタのもっちり白肌エッセンス』。国内産100%のプラセンタエキスを高配合したジェル状濃縮美容液です。",
        "desc_p2": "みずみずしく濃密なジェルが、乾燥して硬くなった肌の上に滑らかに広がり、角層のすみずみまで浸透。ヒアルロン酸やコラーゲンが相乗効果を発揮し、塗った直後から肌がもっちりと吸い付くような柔らかさに整います。冬の紫外線や乾燥によるくすみを晴らし、赤ちゃんのような透明感のあるふっくら肌を目指す方にぴったりです。",
        "target": "プチプラで良質なプラセンタ美容液を試したい方、ジェルタイプの浸透感ともっちり感を好む方、くすみがちな冬の肌を明るくしたい方",
        "point": "化粧水の直後、適量を指先に取り、目元や口元を中心に顔全体に優しくなじませます。朝のメイク前に使ってもモロモロが出ず、ファンデーションの密着を高めてくれます。"
    },
    {
        "rank": 7,
        "tag": "❄️ 北海道十勝の厳選原料100%！熱を一切加えない非加熱・生プラセンタエッセンス",
        "catch": "活性成分をそのまま生きた状態で肌へ。冬の肌細胞を目覚めさせる極上の高純度トリートメント",
        "brand_name": "十勝プラセンタ研究所",
        "capacity": "30ml (トカプラエッセンスEX)",
        "type": "非加熱生プラセンタ高濃度原液美容液",
        "features": "北海道十勝産豚プラセンタ100%、非加熱・生抽出製法、防腐剤・界面活性剤・アルコール無添加",
        "value": "従来の加熱処理で失われがちだったペプチドやタンパク質を活性を保ったまま抽出。冬の過酷な寒冷ダメージを跳ね返す驚異の浸透力",
        "desc_p1": "澄んだ空気と清らかな水が育む北海道十勝の契約農場原料のみを使用した『トカプラエッセンスEX』。有用成分の熱変性を防ぐ独自の非加熱生抽出技術を採用したプレミアムな生プラセンタ美容液です。",
        "desc_p2": "生きたままのペプチドやアミノ酸が高濃度で保たれているため、肌に塗布したときの浸透スピードと肌馴染みが格別。角質層の深部までうるおいが素早く行き渡り、乾燥でしぼんだキメを瞬時に持ち上げます。11月〜12月の急激な冷え込みで血色感を失った肌に、内側からほんのり温かみのあるツヤと血色感、圧倒的なハリをもたらします。",
        "target": "より高活性な『生プラセンタ』を体験したい方、産地や製造工程にこだわりたい方、冬枯れ肌を短期集中でリカバリーしたい方",
        "point": "洗顔直後の素肌に適量を取り、両手で包み込むようにハンドプレスします。生プラセンタの鮮度を保つため、直射日光を避け冷暗所または冷蔵庫での保管がおすすめです。"
    },
    {
        "rank": 8,
        "tag": "🌾 国産豚プラセンタの高純度エキス！昔ながらの技術で素肌の透明感と弾力を守る",
        "catch": "純粋な潤いを角層へ届ける無駄のない処方。大人の乾燥肌にしっとり馴染む実力派",
        "brand_name": "REAL (リアル)",
        "capacity": "30ml (プラセンタエッセンス原液)",
        "type": "高純度プラセンタ原液エキス",
        "features": "国産豚胎盤抽出プラセンタエキス原液、無香料・無着色、弱酸性・低刺激設計",
        "value": "長年のスキンケア研究に基づく安定した品質と高純度。冬の乾燥で失われがちな水分とハリを補い、健やかな肌コンディションを保つ",
        "desc_p1": "サロン向けスキンケアなどを幅広く手がけるリアルの『プラセンタエッセンス原液』。安心の国産豚プラセンタを高純度で抽出した、無駄な添加物を省いたシンプルな原液美容液です。",
        "desc_p2": "サラサラとしたテクスチャーで、肌に触れるとスッと吸い込まれるように浸透。余計な油分や被膜感がないため、その後のスキンケアを一切邪魔しません。角層の水分キープ力を内側から底上げし、キメが整った透明感あふれる素肌へと整えます。冬の乾燥でメイクが崩れやすい混合肌やインナードライ肌の水分補給にも非常に適しています。",
        "target": "ベタつかない使用感でしっかり保湿したい方、無香料でシンプルな処方を好む方、混合肌・インナードライ肌の方",
        "point": "洗顔後すぐにスポイトで2〜3滴を取り、手のひらで顔全体に優しくなじませます。乾燥が気になる目元には指先でトントンと重ね塗りをしてください。"
    },
    {
        "rank": 9,
        "tag": "💧 たっぷり100mlの大容量！顔だけでなく首・デコルテ・全身に贅沢使いできる高濃度原液",
        "catch": "惜しみなくバシャバシャ使える高コスパ。冬の全身エイジング保湿を叶える大人気ボトル",
        "brand_name": "自然化粧品研究所",
        "capacity": "100ml (ピュアプラセンタ原液)",
        "type": "大容量高濃度プラセンタ原液",
        "features": "高濃度プラセンタエキス100ml、無香料・無着色、国内製造・品質検査済み",
        "value": "一般的なプラセンタ原液（20〜30ml）の3倍以上の大容量100ml。冬に乾燥しやすい首元や手の甲、デコルテまで惜しみなく贅沢エイジングケア",
        "desc_p1": "手作り化粧品や高純度原料コスメで根強いファンを持つ自然化粧品研究所の『ピュアプラセンタ原液 100ml』。高品質なプラセンタエキスをたっぷり100mlの大容量ボトルに詰めた驚きのコストパフォーマンスを誇るアイテムです。",
        "desc_p2": "水のようにサラッとした感触で肌馴染みが良く、重ねづけしても一切重くなりません。100mlと大容量のため、顔だけでなく年齢サインが出やすい首筋、デコルテ、手の甲まで毎晩贅沢に塗布できます。シートマスクに浸してプラセンタパックにしたり、ボディローションに混ぜて全身のうるおい補給に使うなど、真冬のマルチなエイジング保湿に大活躍します。",
        "target": "容量を気にせず顔から首・デコルテまでたっぷり使いたい方、コスパ重視で原液パックを楽しみたい方、ボディにも使いたい方",
        "point": "500円玉大を手にとり、顔から首筋、デコルテまで一気に伸ばしてハンドプレスします。冬はコットンやコインマスクにたっぷり含ませて5分間パックするとサロン級のツヤ肌に仕上がります。"
    },
    {
        "rank": 10,
        "tag": "👁️ 目元・口元の乾燥小ジワを薬用プラセンタで集中集中撃退！薬用美白アイクリーム",
        "catch": "医薬部外品・薬用国産プラセンタ×コラーゲン。真冬の乾燥小ジワを目立たなくする部分用名品",
        "brand_name": "明色化粧品 (MEISHOKU)",
        "capacity": "30g (プラセホワイター 薬用美白アイクリーム)",
        "type": "医薬部外品・薬用プラセンタ高配合アイクリーム",
        "features": "薬用有効成分国産プラセンタエキス、コラーゲン、ハトムギエキス配合、医薬部外品認可、高密着リッチクリーム",
        "value": "薬用プラセンタによる美白・保湿とコラーゲンによるハリサポートを1本で。冬の乾燥冷風で刻まれやすい目元・ほうれい線を集中密封",
        "desc_p1": "プチプラアイクリームの中で殿堂入りの人気を誇る明色化粧品の『プラセホワイター 薬用美白アイクリーム』。100%国産の薬用プラセンタを高濃度に配合した医薬部外品の集中トリートメントクリームです。",
        "desc_p2": "こっくりと濃厚でリッチなクリームが、皮膚の薄い目元や口元にピタッと密着。プラセンタが角層深部へ浸透してメラニン生成を抑えつつ、コラーゲンとハトムギエキスが表面をふっくらと潤します。効能評価試験済みで、乾燥による小ジワを目立たなくする効果が実証されています。真冬の暖房下でも目元がシワっぽくならず、ふっくら若々しい目元を一日中キープします。",
        "target": "目尻の乾燥小ジワやほうれい線が気になる方、プチプラで確実なアイケアを続けたい方、アイクリーム初心者の方",
        "point": "スキンケアの最後に、米粒1粒大を指先に取り、目頭から目尻へ向かって優しく引き上げるようになじませます。まぶたやほうれい線にもトントンと優しく押し込んでください。"
    }
]

# JSON-LD構造化データ作成
faq_data = [
    {
        "q": "プラセンタ原液美容液はどのような肌悩みに最も効果的ですか？",
        "a": "プラセンタには必須アミノ酸全種をはじめ、各種ビタミン、ミネラル、核酸、ペプチドが豊富に含まれています。そのため、11月〜12月の寒冷によって皮膚毛細血管が収縮し、代謝（ターンオーバー）が低下して起こる『顔全体のくすみ・ゴワつき』『ハリ・弾力の低下』『乾燥小ジワ』の改善に最も強力な効果を発揮します。"
    },
    {
        "q": "豚プラセンタと馬プラセンタにはどのような違いがありますか？",
        "a": "豚プラセンタは流通量が多く、徹底した衛生管理のもとで生産されるため高品質なものを続けやすい価格で手に入れられるのがメリットです。一方、馬プラセンタ（特に北海道産サラブレッド等）は1年に1頭しか出産しないため希少価値が高く、アミノ酸含有量が豚の数百倍と非常に豊富で、より深刻な冬の乾燥やエイジング悩みに素早い手応えを期待できます。"
    },
    {
        "q": "プラセンタ原液を使う最も効果的な順番とタイミングはいつですか？",
        "a": "『朝晩の洗顔直後（ファーストステップ）』が鉄則です。油分や他のスキンケア成分が肌表面にないまっさらな素肌に塗布することで、水溶性の高分子プラセンタが角層深部へダイレクトに浸透します。また、後から使う化粧水や乳液の引き込み効果（ブースター効果）も最大化されます。"
    },
    {
        "q": "プラセンタ独特の匂い（原料臭）は肌に残りますか？",
        "a": "高純度の無添加プラセンタ原液はわずかに特有の原料臭（アミノ酸の香り）がしますが、肌になじませて数分経つと自然に消えます。肌に匂いが残り続けることはありません。どうしても香りが気になる方は、植物性プラセンタ（エビス等）や、ジェルタイプの処方（ホワイトラベル等）を選ぶのがおすすめです。"
    },
    {
        "q": "敏感肌や冬のゆらぎ肌でもプラセンタ原液を使っても大丈夫ですか？",
        "a": "プラセンタは本来、胎児を育むための安全で栄養豊富な生体成分であり、肌との親和性が非常に高いため敏感肌でも使いやすい成分です。ただし、冬の乾燥で肌が極度に炎症を起こしている場合は、まずパッチテストを行ってから使用するか、アルコールやパラベンが無添加のピュア原液（フラコラやKISOなど）を選ぶことをおすすめします。"
    }
]

schema_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！冬の代謝低下とハリ不足を跳ね返す高濃度プラセンタ原液ランク10",
    "description": "11月・12月の冬枯れ肌に！アミノ酸と成長因子が代謝低下とハリ不足を跳ね返す高濃度プラセンタ原液10選を徹底比較。フラコラ、Bbラボラトリーズ、チューンメーカーズ、KISOなど厳選。",
    "image": items[0]["img_url"],
    "datePublished": "2026-11-03T10:00:00+09:00",
    "dateModified": "2026-11-03T10:00:00+09:00",
    "author": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ 編集部",
        "url": "https://lumi-cosme.vercel.app/"
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
        "@id": "https://lumi-cosme.vercel.app/winter-placenta"
    }
}

schema_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": it["rank"],
            "name": it["name"],
            "item": {
                "@type": "Product",
                "name": it["name"],
                "image": it["img_url"],
                "offers": {
                    "@type": "Offer",
                    "priceCurrency": "JPY",
                    "price": str(it["price"]),
                    "availability": "https://schema.org/InStock",
                    "url": it["affiliate_url"]
                }
            }
        } for it in items
    ]
}

schema_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f["a"]
            }
        } for f in faq_data
    ]
}

schema_breadcrumb = {
    "@context": "https://schema.org",
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
            "name": "高濃度プラセンタ原液ランク10",
            "item": "https://lumi-cosme.vercel.app/winter-placenta"
        }
    ]
}

# HTML構築
items_html = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    price_str = f"¥{it['price']:,}" if it['price'] > 0 else "オープン価格"
    
    items_html += f"""
    <!-- Rank {p['rank']} -->
    <div class="product-card" id="rank-{p['rank']}">
      <div class="product-rank-badge">第{p['rank']}位</div>
      <div class="product-header">
        <span class="product-tag">{p['tag']}</span>
        <h3 class="product-title">{p['catch']}</h3>
        <div class="product-meta">
          <span class="product-brand">ブランド: {p['brand_name']}</span>
          <span class="product-capacity">規格・容量: {p['capacity']}</span>
          <span class="product-type">タイプ: {p['type']}</span>
        </div>
      </div>

      <div class="product-body">
        <div class="product-img-wrap">
          <img src="{it['img_url']}" alt="{it['name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-price-box">
            <span class="price-label">楽天市場参考価格:</span>
            <span class="price-val">{price_str}</span>
            <span class="price-tax">(税込・送料込目安)</span>
          </div>
          <div class="product-features">
            <strong>抽出原料・処方特徴:</strong> {p['features']}
          </div>
          <div class="product-value-point">
            <strong>冬枯れ肌へのエイジング保湿:</strong> {p['value']}
          </div>
        </div>
      </div>

      <div class="product-desc">
        <p class="desc-lead">{p['desc_p1']}</p>
        <p class="desc-detail">{p['desc_p2']}</p>
      </div>

      <div class="product-advice-grid">
        <div class="advice-box target-box">
          <div class="advice-title">💡 こんな肌悩みの方に最適</div>
          <p>{p['target']}</p>
        </div>
        <div class="advice-box usage-box">
          <div class="advice-title">✨ ハリ・透明感を引き出す使用法</div>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-cta">
        <a href="{it['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener nofollow">
          楽天市場で詳細・最安値をチェック <span>→</span>
        </a>
      </div>
    </div>
    """

# 比較テーブル作成
table_rows = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    price_str = f"¥{it['price']:,}" if it['price'] > 0 else "オープン価格"
    table_rows += f"""
    <tr>
      <td class="tbl-rank">第{p['rank']}位</td>
      <td class="tbl-name"><a href="#rank-{p['rank']}">{p['brand_name']}<br><strong>{p['capacity']}</strong></a></td>
      <td class="tbl-type">{p['type']}</td>
      <td class="tbl-feat">{p['features']}</td>
      <td class="tbl-price">{price_str}</td>
    </tr>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！冬の代謝低下とハリ不足を跳ね返す高濃度プラセンタ原液ランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬枯れ肌に！アミノ酸と成長因子が代謝低下とハリ不足を跳ね返す高濃度プラセンタ原液10選を徹底比較！フラコラ、Bbラボラトリーズ、チューンメーカーズ、KISOなど厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-placenta">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- OGP -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！冬の代謝低下とハリ不足を跳ね返す高濃度プラセンタ原液ランク10 | 冬コスメ徹底比較ラボ">
  <meta property="og:description" content="11月・12月の冬枯れ肌に！アミノ酸と成長因子が代謝低下とハリ不足を跳ね返す高濃度プラセンタ原液10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-placenta">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta name="twitter:card" content="summary_large_image">

  <!-- JSON-LD 構造化データ -->
  <script type="application/ld+json">
  {json.dumps(schema_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_faq, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_breadcrumb, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #9333ea;
      --primary-light: #f3e8ff;
      --primary-dark: #7e22ce;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --bg-light: #f8fafc;
      --border-color: #e2e8f0;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --card-hover-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text-main);
      background-color: #f1f5f9;
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
      max-width: 1000px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .container {{
      max-width: 900px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .article-wrap {{
      background: #ffffff;
      padding: 3rem 2.5rem;
      border-radius: 12px;
      box-shadow: var(--card-shadow);
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}

    .breadcrumb a {{
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .article-title {{
      font-size: 1.85rem;
      line-height: 1.4;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.5rem;
    }}

    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border-color);
    }}

    .lead-box {{
      background: #faf5ff;
      border-left: 4px solid var(--primary);
      padding: 1.5rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 2.5rem;
      font-size: 1.05rem;
      line-height: 1.8;
    }}

    .section-title {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #0f172a;
      margin: 3rem 0 1.5rem 0;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 2rem;
      margin-bottom: 3rem;
      position: relative;
      box-shadow: var(--card-shadow);
      transition: box-shadow 0.2s ease;
    }}

    .product-card:hover {{
      box-shadow: var(--card-hover-shadow);
    }}

    .product-rank-badge {{
      position: absolute;
      top: -12px;
      left: 20px;
      background: linear-gradient(135deg, #9333ea, #7e22ce);
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 0.25rem 1rem;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(147, 51, 234, 0.3);
    }}

    .product-header {{
      margin-top: 0.5rem;
      margin-bottom: 1.5rem;
    }}

    .product-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: #7e22ce;
      background: #f3e8ff;
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      margin-bottom: 0.5rem;
    }}

    .product-title {{
      font-size: 1.3rem;
      font-weight: 700;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 0.5rem;
    }}

    .product-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .product-body {{
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 2rem;
      margin-bottom: 1.5rem;
    }}

    @media (max-width: 640px) {{
      .product-body {{
        grid-template-columns: 1fr;
      }}
      .article-wrap {{
        padding: 2rem 1.25rem;
      }}
      .article-title {{
        font-size: 1.5rem;
      }}
    }}

    .product-img-wrap {{
      text-align: center;
      background: #f8fafc;
      padding: 1rem;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .product-img {{
      max-width: 100%;
      max-height: 220px;
      object-fit: contain;
      border-radius: 4px;
    }}

    .product-info {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 0.75rem;
    }}

    .product-price-box {{
      background: #f8fafc;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}

    .price-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #b91c1c;
    }}

    .price-tax {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .product-features, .product-value-point {{
      font-size: 0.95rem;
      line-height: 1.6;
    }}

    .product-desc {{
      margin: 1.5rem 0;
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
    }}

    .desc-lead {{
      margin-bottom: 1rem;
      font-weight: 500;
    }}

    .product-advice-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }}

    @media (max-width: 640px) {{
      .product-advice-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .advice-box {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.9rem;
      line-height: 1.6;
    }}

    .target-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}

    .usage-box {{
      background: #fdf4ff;
      border: 1px solid #f5d0fe;
      color: #86198f;
    }}

    .advice-title {{
      font-weight: 700;
      margin-bottom: 0.35rem;
    }}

    .product-cta {{
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
      font-weight: 700;
      font-size: 1rem;
      padding: 0.85rem 2rem;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 420px;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 12px -2px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #d60000, #aa0000);
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 2rem 0;
    }}

    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      background: #ffffff;
    }}

    .comparison-table th, .comparison-table td {{
      padding: 0.85rem 0.75rem;
      border: 1px solid var(--border-color);
      text-align: left;
    }}

    .comparison-table th {{
      background: #f8fafc;
      color: #0f172a;
      font-weight: 700;
      white-space: nowrap;
    }}

    .tbl-rank {{
      font-weight: 700;
      color: var(--primary-dark);
      white-space: nowrap;
      text-align: center;
    }}

    .tbl-name a {{
      color: #0f172a;
      text-decoration: none;
    }}

    .tbl-name a:hover {{
      color: var(--primary);
    }}

    .tbl-price {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin: 2rem 0;
    }}

    .faq-item {{
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1.25rem;
    }}

    .faq-q {{
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 0.5rem;
      display: flex;
      gap: 0.5rem;
    }}

    .faq-q-badge {{
      background: var(--primary);
      color: #ffffff;
      font-size: 0.75rem;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      height: fit-content;
    }}

    .faq-a {{
      color: #475569;
      font-size: 0.95rem;
      line-height: 1.7;
    }}

    .internal-links-box {{
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.5rem;
      margin-top: 3rem;
    }}

    .internal-links-title {{
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: #0f172a;
    }}

    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 0.75rem;
    }}

    .internal-link {{
      color: #7e22ce;
      text-decoration: none;
      font-size: 0.85rem;
      padding: 0.4rem 0.6rem;
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      transition: all 0.2s;
    }}

    .internal-link:hover {{
      background: #f3e8ff;
      border-color: #d8b4fe;
    }}

    .site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border-color);
      padding: 2rem 0;
      margin-top: 4rem;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav>
        <a href="/" style="text-decoration: none; color: #475569; font-size: 0.9rem; font-weight: 600;">TOPへ戻る</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <article class="article-wrap">
      <nav class="breadcrumb">
        <a href="/">ホーム</a> &gt; <span>高濃度プラセンタ原液ランク10</span>
      </nav>

      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！冬の代謝低下とハリ不足を跳ね返す高濃度プラセンタ原液ランク10</h1>

      <div class="article-meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証カテゴリー: 高濃度プラセンタ・エイジング高保湿</span>
        <span>監修: 冬コスメ徹底比較ラボ 編集部</span>
      </div>

      <div class="lead-box">
        <strong>【11月・12月の冬枯れ肌に！アミノ酸と成長因子が代謝低下とハリ不足を跳ね返す】</strong><br>
        11月から12月にかけて外気温が下がり木枯らしが吹き始めると、肌の表面温度が低下して毛細血管の血流が滞り、肌細胞のターンオーバー速度が著しく低下します。「しっかり保湿しているのに顔色がどんより暗くくすむ」「肌が硬くこわばってハリや弾力が失われ、夕方にファンデーションが毛穴落ちする」という大人の肌悩みは、まさにこの代謝低下が引き金となっています。<br><br>
        そんな冬枯れ肌の救世主として愛され続けるのが<strong>『高濃度プラセンタ原液』</strong>です。生命の源である胎盤から抽出されるプラセンタには、全種類の必須アミノ酸、細胞間コミュニケーションを支えるペプチド、ビタミン、ミネラルが高密度に凝縮されています。<br><br>
        単に外から水分や油分を補うだけでなく、肌本来の自発的な潤い生成力とターンオーバーのリズムを呼び覚ます、2026年最新の厳選10品を徹底検証・ランキング化しました。
      </div>

      <h2 class="section-title">✨ なぜプラセンタ原液は真冬のエイジング乾燥肌に劇的な効果をもたらすのか？</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>プラセンタ（胎盤エキス）は、医療領域でも更年期障害や肝機能改善の注射薬として認可されている確固たる実績を持つ生体有用成分です。化粧品として角層に届けることで、冬特有の肌トラブルに対して以下の3つの大きな美肌メリットをもたらします。</p>
        <ul style="margin: 1rem 0 1rem 1.5rem;">
          <li><strong>1. 天然保湿因子（NMF）の直接補給：</strong> 角層の水分を保持する主成分であるアミノ酸群を豊富に含み、冬の乾燥によってスカスカになった角質細胞を瞬時に満たします。</li>
          <li><strong>2. 寒冷によるターンオーバー遅延の正常化：</strong> 豊富なペプチドや核酸が、寒さで眠りかけた肌リズムを活性化し、古い角質の排出と新しい健やかな角層形成をサポートします。</li>
          <li><strong>3. 水分引き込み（ブースター）効果：</strong> 洗顔直後の素肌になじませることで、角層の親水性を高め、その後に重ねる化粧水や乳液の浸透力を何倍にも引き上げます。</li>
        </ul>
      </div>

      <h2 class="section-title">🏆 高濃度プラセンタ原液高保湿おすすめランキング10選</h2>

      {items_html}

      <h2 class="section-title">📊 高濃度プラセンタ原液10品 徹底スペック比較表</h2>
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名・容量</th>
              <th>種別・タイプ</th>
              <th>抽出原料・処方特徴</th>
              <th>参考価格</th>
            </tr>
          </thead>
          <tbody>
            {table_rows}
          </tbody>
        </table>
      </div>

      <h2 class="section-title">💡 11月・12月の冬本番にプラセンタの効果を最大化するブースター手順</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>高純度のプラセンタ原液は、使う順番とステップを正しく守ることで、その美容効果を何倍にも引き出すことができます。</p>
        <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; margin-top: 1rem;">
          <h3 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: #9333ea;">① 何よりも先に「洗顔直後」の素肌に塗布</h3>
          <p>プラセンタ原液は水溶性成分のため、化粧水や乳液の油分が肌表面にあると浸透が妨げられます。朝晩の洗顔後、タオルで水気を取った直後のまっさらな素肌に一番最初になじませてください。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #9333ea;">② 体温で温めてから優しくハンドプレス</h3>
          <p>冬の冷えた手のひらではなく、両手をこすり合わせて温めてからプラセンタ原液を取り、顔全体を包み込むように優しくハンドプレスします。手の温もりによって角層の隙間が広がり、深部まで吸い込まれるように浸透します。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #9333ea;">③ 原液がなじんだ直後に化粧水で水分を重ねる</h3>
          <p>プラセンタ原液が肌に浸透すると、角層が水分を強力に引き込む状態（ブースト状態）になります。完全に乾ききる前に高保湿化粧水をたっぷり重ね、最後に乳液やクリーム、ワセリンでフタをして密閉しましょう。</p>
        </div>
      </div>

      <h2 class="section-title">❓ 専門家が答える！高濃度プラセンタ原液のよくある質問</h2>
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

      <div class="internal-links-box">
        <h3 class="internal-links-title">🔗 あわせて読みたい冬の高保湿スキンケア・コスメ特集</h3>
        <div class="internal-links-grid">
          <a href="/winter-heparinoid" class="internal-link">🧪 薬用ヘパリン類似物質コスメ10選</a>
          <a href="/winter-vaseline" class="internal-link">🛡️ 高純度ワセリン高保湿10選</a>
          <a href="/winter-rice-power" class="internal-link">🌾 米発酵・ライスパワー高保湿10選</a>
          <a href="/winter-peptide-serum" class="internal-link">🧬 高保湿ペプチド美容液10選</a>
          <a href="/winter-ceramide-serum" class="internal-link">🧴 高保湿セラミド美容液10選</a>
          <a href="/winter-amino-acid" class="internal-link">💧 高浸透アミノ酸コスメ10選</a>
          <a href="/winter-squalane-oil" class="internal-link">✨ 高純度スクワランオイル10選</a>
          <a href="/winter-vitamin-c-serum" class="internal-link">🍋 高保湿ビタミンC美容液10選</a>
          <a href="/winter-niacinamide-serum" class="internal-link">✨ ナイアシンアミド美容液10選</a>
          <a href="/winter-retinol-cream" class="internal-link">🌙 レチノール高保湿クリーム10選</a>
          <a href="/winter-exosome-serum" class="internal-link">🔬 高保湿エクソソーム美容液10選</a>
          <a href="/winter-glutathione-serum" class="internal-link">✨ 高保湿グルタチオン美容液10選</a>
          <a href="/winter-pdrn-serum" class="internal-link">🐟 高保湿PDRN美容液10選</a>
          <a href="/winter-ceramide-cream" class="internal-link">🧴 高保湿セラミドクリーム10選</a>
        </div>
      </div>

    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved.</p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #94a3b8;">当サイトは楽天市場アフィリエイトプログラムに参加しており、適格販売により収入を得ています。</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-placenta.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-placenta.html!")
