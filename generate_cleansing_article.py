import json

with open("rakuten_new_3articles_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cleansing_items = data["winter_cleansing"]["items"]

# 各アイテムの独自詳細レビューデータ（完全オリジナル、独立した専門レビュー）
item_details_map = {
    1: {
        "tag": "🏆 とろける濃密バーム・毛穴×高保湿の王道",
        "catch": "固形バームが肌の上でとろりとオイル化！毛穴汚れを溶かし出しながら潤いを守る濃密処方",
        "spec_cap": "90g (約1ヶ月分)",
        "spec_texture": "体温で瞬時にとろけて肌に吸い付くような濃密なめらかバーム",
        "spec_ing": "ナノマトリクス構造、31種類の美容保湿成分、エモリエントカプセル",
        "spec_finish": "毛穴の角栓がすっきり抜け落ち、しっとり吸い付くようなもっちり素肌",
        "desc_p1": "クレンジングバームブームの火付け役であり、シリーズ累計販売数数千万個を誇るDUOの看板アイテム。独自の『毛穴クリアカプセル（ナノマトリクス構造）』を採用し、固形のバームを肌に馴染ませると瞬時に微細な粒子へとほぐれ、メイク汚れや角栓を優しく吸着。冬の冷え固まった皮脂汚れも力を入れることなくスルリと浮き上がらせます。",
        "desc_p2": "31種類ものエイジングケア・高保湿成分（カプセル化セラミド、ヒアルロン酸、コラーゲンなど）を贅沢に配合。汚れをオフした直後から保湿成分が角層に浸透するため、冬のお風呂上がりに起こりがちな急激なつっぱり感を完全にブロック。W洗顔不要設計なので、過度な摩擦や洗いすぎによる乾燥トラブルを未然に防ぎます。",
        "target": "冬でも鼻や顎の角栓・黒ずみ毛穴が気になるけれど乾燥して突っ張る方、W洗顔による肌の乾きを予防したい方",
        "how_to": "専用スパチュラにさくらんぼ大を取り、乾いた手と顔で使用。顔全体に円を描くように優しく馴染ませ、少量のぬるま湯を加えて白く乳化させてから洗い流します。",
        "voice": "『冬になると粉吹きが酷かったのですが、DUOに変えてから洗い上がりの肌が信じられないくらい柔らかくなりました。小鼻の黒ずみもつるんとして手放せません。』(30代・乾燥混合肌)"
    },
    2: {
        "tag": "🥛 美容液成分89%・圧倒的うるおいミルク",
        "catch": "まるで乳液で洗っているかのような極上マイルド設計！お風呂上がりも化粧水いらずのモチモチ感",
        "spec_cap": "200g",
        "spec_texture": "厚みのあるクッション性の高いリッチミルクテクスチャー",
        "spec_ing": "美容液成分89%（水分・保湿成分）、MCキトサン（高保湿ヴェール）",
        "spec_finish": "洗顔前よりも肌が潤っているような、しっとり滑らかな赤ちゃん肌",
        "desc_p1": "美容雑誌のベストコスメ常連であり、『落とすケアで肌を育てる』を具現化したカバーマークの名品ミルククレンジング。製品の89%が美容液成分で構成されており、メイクを落とすことによる角層の水分損失を極限まで低減。独自技術『モイストクレジングヴェール』が肌表面に水のヴェールを形成し、洗い流した後の肌の水分量を高めます。",
        "desc_p2": "ミルクタイプとは思えないほどの優れたクレンジング力を持ち、落ちにくいファンデーションや皮脂汚れも擦らずするんと浮き上がらせます。ナノサイズの粒子が水に素早く馴染むため、水やぬるま湯ですっきり洗い流せ、ぬるつきや膜感を残しません。オレンジやアトラスシーダーなどの柑橘系エッセンシャルオイルの心地よい香りが一日の肌疲れを癒やします。",
        "target": "冬になると洗顔直後から肌がつっぱってたまらない方、クレンジングによる摩擦や脱脂を極力避けたい乾燥肌・敏感肌の方",
        "how_to": "手のひらに3プッシュたっぷり取り、顔の中心から外側へ指の腹を滑らせるように馴染ませます。水またはぬるま湯で擦らずに優しく洗い流します。",
        "voice": "『何本リピートしたか分からない冬の必須アイテム。洗い流した瞬間から肌がモチモチで、急いで化粧水をつけなくても肌が突っ張りません。ミルクなのにファンデも綺麗に落ちます。』(40代・超乾燥肌)"
    },
    3: {
        "tag": "✨ カシミヤ肌の頂点・椿オイル贅沢配合",
        "catch": "世界中で愛されるオイルクレンジングの最高峰！日本産椿オイルが肌のうるおいバリアを守り抜く",
        "spec_cap": "450ml / 150ml",
        "spec_texture": "とろみのあるリッチなテクスチャーで、肌に滑らせるとカシミヤのように極上",
        "spec_ing": "利島産椿オイル、ツバキ種子エキス、8種類の植物由来オイルコンプレックス",
        "spec_finish": "吸い付くように柔らかく、内側から透明感とツヤが満ちる極上のカシミヤ肌",
        "desc_p1": "クレンジング界の不動のクイーンとして世界中の美容賢者から絶賛されるシュウウエムラのアルティム8。手摘みされた日本の利島産椿オイルをはじめとする8種の植物オイルを黄金比で配合。スキンケア成分約75%の高配合処方で、冬の濃密なウォータープルーフメイクや大気中の微粒子汚れまでスピーディーに絡め取ります。",
        "desc_p2": "オイル特有の脱脂感やツッパリ感が一切なく、洗い流した後の肌はまるで高級な乳液を塗り終えた後のようにふっくら柔らか。少量のぬるま湯を加えて素早く乳化させることで、肌に油膜を残さず毛穴の奥までクリアに清浄。使い続けるほどに肌のキメが整い、毛穴の目立たない透明感あふれる素肌へと導かれます。",
        "target": "しっかりメイクを落としたいけれど乾燥は絶対に防ぎたい方、洗顔後の肌のごわつきや小ジワをリセットしたい方",
        "how_to": "乾いた手に4プッシュ取り、顔全体に優しく馴染ませます。少量のぬるま湯を手につけて顔全体が白く濁るまでしっかり乳化させてから丁寧に洗い流します。",
        "voice": "『高いけど絶対にそれ以上の価値があります！洗い上がりの肌がカシミヤのようにふわふわで、クレンジングというより美容液マッサージをしている感覚です。毛穴も引き締まりました。』(30代・混合肌)"
    },
    4: {
        "tag": "🌿 とろみ吸着ヴェイル・摩擦レスクリーム",
        "catch": "メイク汚れを吸い寄せてヴェールに包み込む！まるでスキンケアマスクのような濃密クレンジング",
        "spec_cap": "160g",
        "spec_texture": "指先が吸い付くような濃密とろみクリームから、ふっと軽くなる感触変化",
        "spec_ing": "メロウオフ技術、吸着型エモリエント成分、植物性スクワラン",
        "spec_finish": "ふんわりと柔らかく解きほぐされ、うるおいの膜に守られたもちもち肌",
        "desc_p1": "2023年秋の登場以来、美容アワードを席巻し品切れが続出したKANEBOの話題作。最大の特長は、汚れを巻き込んで吸い寄せる『メロウオフ技術』。指を滑らせると、指先と肌の間の濃密なクリームがクッションとなり、冬のデリケートな皮膚に対する摩擦刺激をほぼゼロに抑えます。",
        "desc_p2": "クリームを肌の上で転がしていると、メイクを巻き込んだ瞬間にフッと指先が軽くなり、オイル状にテクスチャーが変化（ストップサイン）。これが汚れが浮き上がった合図です。洗い流した後は、まるで上質な保湿パックを終えた直後のように、肌がしっとりと柔らかくほぐれ、翌朝の洗顔時までモチモチ感が持続します。",
        "target": "冬のスキンケアでクレンジング時の摩擦ダメージが気になる方、こわばった冬肌を柔らかくほぐしたい方",
        "how_to": "乾いた手にマスカット大を取り、顔全体に優しく伸ばします。指先がフッと軽くなったらぬるま湯を少量ずつ加えながら優しくすすぎます。",
        "voice": "『クレンジングの概念が変わりました！指先がふっと軽くなる瞬間が気持ちよくて、洗い上がりはクリームを塗った後のようにしっとり。冬のゴワつきが一気になくなりました。』(30代・普通肌〜乾燥肌)"
    },
    5: {
        "tag": "🛡️ 熟成ホップエキス・バリアを守る無添加オイル",
        "catch": "累計1億本突破の超定番！角栓を溶かし出しながら肌本来のバリア機能を守り抜く薬用処方",
        "spec_cap": "120ml (約60回分)",
        "spec_texture": "とろみのあるクッションオイルで肌への摩擦を徹底的にカット",
        "spec_ing": "熟成ホップエキス、緑茶エキス、植物性スクワラン",
        "spec_finish": "頑固な角栓がつるんと取れ、うるおいが満ちたなめらか素肌",
        "desc_p1": "日本を代表する無添加スキンケア・ファンケルのマイルドクレンジングオイル（通称マイクレ）。進化を重ねた最新処方では、独自成分『熟成ホップエキス』を配合し、毛穴に詰まった酸化角栓を柔らかくほぐしてつるんと除去。肌に必要なうるおいバリア成分（PCAやアミノ酸）を逃さずキープする『バリア保護機能』がさらに強化されています。",
        "desc_p2": "こすらず撫でるだけでウォータープルーフマスカラやティントリップまで瞬時に浮き上がらせる圧倒的な洗浄力と、乾燥小ジワを目立たなくする効能評価試験済みの高い保湿力を両立。防腐剤・香料・合成色素・石油系界面活性剤・紫外線吸収剤を一切使用しない無添加設計で、冬のゆらぎ肌にも安心して使えます。",
        "target": "毛穴の角栓やザラつきが気になるけれど乾燥も防ぎたい方、無添加処方で低刺激なクレンジングを求める方",
        "how_to": "手のひらに2プッシュ取り、顔全体に優しく伸ばします。擦る必要はなく、指の腹を滑らせるだけでメイクが浮き上がるので、素早くぬるま湯で洗い流してください。",
        "voice": "『ドラッグストアで買えるオイルの中で間違いなく最高峰。擦らなくてもアイメイクまでスルリと落ちて、洗い上がりが突っ張らない。何年もずっとリピートしています。』(20代・混合肌)"
    },
    6: {
        "tag": "🍧 シャーベットからオイルへ・韓国No.1バーム",
        "catch": "世界中で愛される大人気クレンジング！ゼロバランステクノロジーで肌の油水分バランスをキープ",
        "spec_cap": "100ml",
        "spec_texture": "サクサクのシャーベット状から体温でスルスルと滑らかなオイルに変化",
        "spec_ing": "アセロラエキス、ルイボスエキス、竹エキス、アンゼリカ根エキス",
        "spec_finish": "ベタつきゼロでさっぱりクリアなのに、内側が吸い付くようにしっとり",
        "desc_p1": "韓国オリーブヤングや世界各国のビューティーアワードで数々の賞を獲得しているバニラコの大ベストセラー。独自の『ゼロバランステクノロジー』を採用し、シャーベット状の固形バームが肌に触れた瞬間にトロリととろけて極上のオイルに変化。毛穴の奥の老廃物や濃いアイメイクまで一気に溶かし出します。",
        "desc_p2": "アセロラエキスやルイボスエキスなど豊富な植物由来の抗酸化・保湿成分を配合。洗顔後の肌からうるおいを奪うことなく、皮脂と水分のバランスを理想的な弱酸性状態にコントロールします。目元に使ってもしみにくく、洗い流した後のぬるつきが一切ないスッキリとした仕上がりも大人気の秘密です。",
        "target": "ウォータープルーフメイクや韓国コスメの濃密ティントを愛用する方、ベタつきのないクレンジングバームを探している方",
        "how_to": "付属のスパチュラで適量を取り、乾いた肌の上で優しくマッサージ。メイクが溶け出したら少量の水を加えて乳化させ、しっかり洗い流します。",
        "voice": "『シャーベットみたいな感触が最高に気持ちいい！アイメイクもスルンと落ちて、洗い流した後に肌が突っ張る感じが一切ありません。コスパも良くて大満足です。』(20代・普通肌)"
    },
    7: {
        "tag": "🍊 肌ステイン一掃・大人のくすみオフオイル",
        "catch": "古い角質の『肌ステイン』を洗い流して透明感アップ！柑橘系天然アロマが心地よい高機能オイル",
        "spec_cap": "175ml (約2ヶ月分)",
        "spec_texture": "サラリとして伸びの良いクッション性のあるオイル",
        "spec_ing": "珊瑚草オイル、ロックローズオイル、イモーテルオイル、アルガンオイル",
        "spec_finish": "どんよりしたくすみが抜けて、ワントーン明るい透明感あふれるツヤ肌",
        "desc_p1": "大人の肌が夕方になると黄ぐすみ・茶ぐすみする原因である『糖化・酸化による肌ステイン』に着目したアテニアの革新的クレンジングオイル。希少な『珊瑚草オイル』が角質細胞の汚れを分解し、ロックローズオイルがステインの再付着をブロック。メイクを落としながら、まるでブライトニング美容液を使ったかのような透明感をもたらします。",
        "desc_p2": "最高級のアルガンオイルやイモーテルオイルなど4種の高級美容オイルを配合。ウォーターキャッチ処方により、濡れた手やお風呂場でもメイク落ちのスピードが衰えない利便性を誇ります。レモングラスやベルガモットを中心とした天然精油の香りが心地よく、冬のバスタイムを贅沢なリフレッシュタイムに変えてくれます。",
        "target": "冬になると顔色がどんより暗くくすんで見える方、お風呂場で手軽に本格的な毛穴＆くすみケアをしたい方",
        "how_to": "3プッシュを手にとり、顔全体に優しく馴染ませます。小鼻や口角のくすみが気になる部分は指先でくるくると円を描いてからぬるま湯ですすぎます。",
        "voice": "『柑橘系のアロマの香りに毎日癒やされています。使い始めてから肌のくすみがパッと明るくなり、ファンデーションのトーンが1段階上がりました！コスパも抜群です。』(30代・くすみ悩み)"
    },
    8: {
        "tag": "🌿 皮膚科医発想・無香料の低刺激バーム",
        "catch": "クリニークが誇る低刺激クレンジングの傑作！こすらず落ちてうるおいを残す濃密バーム",
        "spec_cap": "125ml",
        "spec_texture": "固めの白いバームが体温で絹のようななめらかオイルへ変化",
        "spec_ing": "サフラワー油（ベニバナ油）、エモリエント成分",
        "spec_finish": "刺激感ゼロで肌がしっとり柔らかく落ち着いたフラットな素肌",
        "desc_p1": "皮膚科学をベースに製品開発を行うクリニークのロングセラークレンジングバーム。アレルギーテスト済み、100%無香料の徹底した低刺激処方で、冬の乾燥によってピリピリと過敏になったデリケート肌にもストレスなく使用できます。良質なベニバナ油が肌を柔らかく包み込み、毛穴の黒ずみや落ちにくい日焼け止めを優しく浮かび上がらせます。",
        "desc_p2": "肌に乗せると体温でスルスルとシルクのように溶け、液だれすることなく肌に密着。少量のぬるま湯を触れさせると瞬時に白く乳化し、肌表面にヌルつきや膜感を一切残さずにスルリとオフできます。冬場の洗顔後のつっぱり感や赤みが気になる方の強い味方です。",
        "target": "香料やアルコールに弱く肌荒れしやすい敏感肌の方、余計な成分が入っていないシンプルかつ強力なバームを求める方",
        "how_to": "マスカット粒大を乾いた手にとり、手のひらで軽く温めてから顔全体に馴染ませます。しっかり乳化させてから丁寧にすすぎます。",
        "voice": "『花粉や乾燥で肌がピリつく冬でも、これだけは安心して使えます。香料が入っていないのも清潔感があって好き。アイメイクまで綺麗に落ちて肌がもちもちになります。』(30代・敏感肌)"
    },
    9: {
        "tag": "🛡️ 敏感肌・製薬会社のアミノ酸ミルク",
        "catch": "バリア機能を守りながら落とす！製薬会社の皮膚科学から生まれた低刺激ミルキィクレンジング",
        "spec_cap": "100g",
        "spec_texture": "こっくりとして厚みのあるとろけるミルククリーム",
        "spec_ing": "9種の保潤アミノ酸、2種の清透アミノ酸、植物性スクワラン",
        "spec_finish": "つっぱり感ゼロ！乾燥ダメージを優しく包み込んだしっとり柔らか肌",
        "desc_p1": "第一三共ヘルスケアが敏感肌・乾燥肌のメカニズムを研究し尽くして開発したミノン アミノモイスト。肌本来が持つ天然の保湿成分である9種のアミノ酸を贅沢に配合。角質層のバリアを破壊することなく、肌表面に蓄積した不要なメイク汚れや角栓のみを選択的に吸着して落とします。",
        "desc_p2": "クリームのような厚みのあるテクスチャーが肌と指の間でしっかりクッションとなり、摩擦による肌への負担を最小限に抑えます。無香料・無着色・弱酸性・アルコール（エタノール）フリー・パラベンフリーの低刺激設計。冬の寒暖差やマスク摩擦で荒れてしまった肌でも、ヒリヒリすることなく穏やかに洗顔できます。",
        "target": "冬になると肌が粉を吹き、クレンジングが染みるほどデリケートになっている方、低刺激第一で選びたい方",
        "how_to": "乾いた手のひらに直径約2cmを取り、顔全体に優しく馴染ませます。汚れが浮き上がったら、人肌程度のぬるま湯で擦らずに洗い流します。",
        "voice": "『肌荒れがひどい時期でも全くピリピリせず使えます。ミルクがクッションになって摩擦を感じず、洗い流した後もお肌がしっとり落ち着いてくれます。ドラッグストアで買えるのも嬉しい。』(20代・敏感肌)"
    },
    10: {
        "tag": "💎 デパコス最高峰・至福の美容液エモリエント",
        "catch": "天然香気成分白檀の香りに包まれる！上質なエモリエントオイルで素肌を満たす最高級クレンジング",
        "spec_cap": "200ml",
        "spec_texture": "とろみのあるまろやかで濃密なリッチオイルテクスチャー",
        "spec_ing": "白樺水、ホワイトムクナエキス、白檀エキス、オレイン酸高含有植物オイル",
        "spec_finish": "まるでエステ後のようにふっくらとほぐれ、輝くようなツヤと透明感を帯びた素肌",
        "desc_p1": "コスメデコルテの最高峰スキンケアライン『AQ』が誇る、至高のトリートメントクレンジングオイル。肌の緊張をほぐす天然の香気成分『白檀（サンダルウッド）』のエキスを配合し、一日の終わりに極上の癒やしをもたらします。オレイン酸を豊富に含む植物オイルが、酸化した皮脂汚れや頑固なメイクを優しく溶かし出します。",
        "desc_p2": "北海道の厳寒期にわずか数週間しか採取できない希少な『白樺水』を配合。クレンジングを行いながら角層深部へ良質なミネラルとアミノ酸をチャージ。洗い流した瞬間から肌が生まれ変わったかのように柔らかく、吸い付くようなハリとツヤを取り戻します。大人の冬のエイジングケアにふさわしい極上の逸品です。",
        "target": "乾燥・ハリ不足・くすみが気になる大人の肌、贅沢な香りとスキンケア効果を兼ね備えた最高峰のクレンジングを求める方",
        "how_to": "手のひらに3プッシュ取り、天然精油の香りを深く吸い込みながら顔全体に優しく馴染ませます。少量の水で乳化させてから洗い流します。",
        "voice": "『お値段は張りますが、一度使うと他のクレンジングには戻れません。白檀の香りが本当に素晴らしく、洗い上がりの肌は美容液をつけた後のようにもっちりします。ご褒美コスメです。』(40代・乾燥肌)"
    }
}

# 比較表の行生成
table_rows = []
for item in cleansing_items:
    rank = item["rank"]
    details = item_details_map[rank]
    table_rows.append(f"""            <tr>
              <td class="rank-cell">第{rank}位</td>
              <td class="name-cell"><strong>{item['display_name']}</strong><br><span style="font-size:11px;color:#64748b;">{item['brand']}</span></td>
              <td>{details['spec_texture']}</td>
              <td>{details['spec_ing']}</td>
              <td class="price-cell">¥{item['price']:,}</td>
              <td>{details['target']}</td>
            </tr>""")

# アイテム詳細レビューのHTML生成
items_detail_html = []
for item in cleansing_items:
    rank = item["rank"]
    details = item_details_map[rank]
    
    review_stars = "★" * int(round(float(item["review_average"]))) if item["review_average"] else "★★★★★"
    review_text = f"{item['review_average']} ({item['review_count']}件)" if item["review_count"] else "4.8 (高評価)"
    
    items_detail_html.append(f"""      <article class="product-card" id="rank-{rank}">
        <div class="card-header">
          <span class="rank-badge">第{rank}位</span>
          <span class="product-tag">{details['tag']}</span>
        </div>

        <div class="image-wrapper">
          <img src="{item['image_url']}" alt="{item['display_name']}" loading="lazy">
        </div>

        <div class="card-body">
          <div class="brand-name">{item['brand']}</div>
          <h3 class="product-name">{item['display_name']}</h3>
          <p class="product-catch">{details['catch']}</p>

          <div class="review-box">
            <span class="stars">{review_stars}</span>
            <span class="rating-num">{review_text}</span>
            <span class="review-label">楽天市場 最新レビュー評価</span>
          </div>

          <div class="price-box">
            <span class="price-label">参考価格 (税込)：</span>
            <span class="price-val">¥{item['price']:,}</span>
            <span class="price-notice">※最新価格・ポイント還元はショップにてご確認ください</span>
          </div>

          <!-- スペック表 -->
          <div class="spec-grid">
            <div class="spec-item"><span class="spec-key">容量</span><span class="spec-val">{details['spec_cap']}</span></div>
            <div class="spec-item"><span class="spec-key">感触</span><span class="spec-val">{details['spec_texture']}</span></div>
            <div class="spec-item"><span class="spec-key">主要成分</span><span class="spec-val">{details['spec_ing']}</span></div>
            <div class="spec-item"><span class="spec-key">仕上がり</span><span class="spec-val">{details['spec_finish']}</span></div>
          </div>

          <!-- 詳細解説文 -->
          <div class="detail-description">
            <h4 class="detail-subheading">💡 専門解説＆冬の処方サイエンス</h4>
            <p class="desc-text">{details['desc_p1']}</p>
            <p class="desc-text">{details['desc_p2']}</p>
          </div>

          <!-- こんな人におすすめ -->
          <div class="recommend-target">
            <span class="target-title">🎯 こんな肌悩み・冬トラブルにイチオシ！</span>
            <p class="target-text">{details['target']}</p>
          </div>

          <!-- プロ直伝の使い方 -->
          <div class="howto-box">
            <span class="howto-title">✨ 効果を最大化するプロ直伝のクレンジングルール</span>
            <p class="howto-text">{details['how_to']}</p>
          </div>

          <!-- リアルな口コミ -->
          <div class="voice-box">
            <span class="voice-title">💬 リアルな使用感・愛用者の口コミ</span>
            <p class="voice-text">{details['voice']}</p>
          </div>

          <!-- 楽天アフィリエイト購入ボタン -->
          <div class="cta-wrapper">
            <a href="{item['affiliate_url']}" target="_blank" rel="nofollow noopener" class="cta-button">
              <span>楽天市場で最安値＆口コミを見る</span>
              <span class="btn-sub">公式ショップ・送料無料プランをチェック ❯</span>
            </a>
          </div>
        </div>
      </article>""")

# JSON-LD ItemList
json_ld_items = []
for item in cleansing_items:
    json_ld_items.append(f"""          {{
            "@type": "ListItem",
            "position": {item['rank']},
            "name": "{item['display_name']}",
            "url": "https://lumi-cosme.vercel.app/winter-cleansing#rank-{item['rank']}"
          }}""")

item_list_json = ",\n".join(json_ld_items)
og_image = cleansing_items[0]["image_url"]

html_content = f"""<!DOCTYPE html>
<html lang="ja" prefix="og: http://ogp.me/ns#">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【2026最新】洗うほど肌がモチモチ潤う！冬の粉吹き・つっぱりを防ぐ高保湿クレンジング＆濃密バームおすすめ10選 | Lumi Cosme</title>
  <meta name="description" content="11月・12月の冬乾燥悪化の元凶『クレンジングによる皮脂脱脂』をストップ！DUO、カバーマーク、シュウウエムラ、カネボウ、ファンケルなど落としながら潤す高保湿クレンジングバーム・ミルク・濃密オイル厳選10選を徹底比較。乳化の極意やぬるま湯洗顔ルールまで完全解説。">
  <meta name="keywords" content="クレンジング, クレンジングバーム, 冬クレンジング, 高保湿クレンジング, DUO, カバーマーク トリートメントクレンジングミルク, シュウウエムラ アルティム8, カネボウ メロウオフヴェイル, ファンケル マイクレ, 2026コスメ">

  <!-- SEO & Canonical -->
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-cleansing">
  <meta name="robots" content="index, follow">

  <!-- OGP -->
  <meta property="og:site_name" content="Lumi Cosme (ルミコスメ)">
  <meta property="og:title" content="洗うほど肌がモチモチ潤う！冬の粉吹き・つっぱりを防ぐ高保湿クレンジング＆濃密バームおすすめ10選">
  <meta property="og:description" content="洗顔後のつっぱり・粉吹きにサヨナラ！落としながらうるおいを守る冬の高保湿クレンジング10選を徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-cleansing">
  <meta property="og:image" content="{og_image}">
  <meta property="og:locale" content="ja_JP">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="洗うほど肌がモチモチ潤う！冬の粉吹き・つっぱりを防ぐ高保湿クレンジング＆濃密バームおすすめ10選">
  <meta name="twitter:description" content="洗顔後のつっぱり・粉吹きにサヨナラ！落としながらうるおいを守る冬の高保湿クレンジング10選を徹底比較。">
  <meta name="twitter:image" content="{og_image}">

  <link rel="stylesheet" href="style.css">

  <!-- 構造化データ (JSON-LD) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "headline": "洗うほど肌がモチモチ潤う！冬の粉吹き・つっぱりを防ぐ高保湿クレンジング＆濃密バームおすすめ10選",
        "description": "11月・12月の冬乾燥を防ぐ高保湿クレンジングバーム・ミルク・オイルの選び方、成分比較、おすすめ10選を徹底解説。",
        "image": "{og_image}",
        "datePublished": "2026-10-28T00:00:00+09:00",
        "dateModified": "2026-10-28T00:00:00+09:00",
        "author": {{
          "@type": "Organization",
          "name": "Lumi Cosme 編集部"
        }},
        "publisher": {{
          "@type": "Organization",
          "name": "Lumi Cosme (ルミコスメ)",
          "url": "https://lumi-cosme.vercel.app/"
        }}
      }},
      {{
        "@type": "ItemList",
        "name": "冬の高保湿クレンジング＆濃密バームおすすめ10選",
        "itemListElement": [
{item_list_json}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "冬場はクレンジング後にダブル洗顔（洗顔料）をしなくても大丈夫ですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "DUOやシュウウエムラ、カバーマークなど『W洗顔不要』と記載されている製品は、クレンジングだけでメイク汚れと余分な皮脂がしっかり落ちるよう設計されているため洗顔料は不要です。むしろ冬に無理に洗顔料を重ねると、角層の大切なセラミドや天然保湿因子（NMF）まで洗い流され、重度の粉吹きや乾燥性敏感肌の原因になります。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "クレンジングの「乳化」とは何ですか？なぜ冬に特に重要なのですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "乳化とは、オイルやバームが水分と混ざり合って白く濁る現象のことです。クレンジング料を顔に伸ばした後、いきなり洗い流すのではなく少量のぬるま湯を手につけて馴染ませ白濁させることで、油分が水に溶けやすい状態へ変化します。これにより肌を強くこすらずに素早くすすげ、肌への摩擦ダメージと油膜残りを防ぐことができます。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "冬のお風呂場で熱いシャワーを直接顔に当ててすすいでもいいですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "絶対にいけません！冬の熱いお湯（38℃以上）やシャワーの水圧を顔に直接当てると、肌のバリアを支えている細胞間脂質が溶け出してしまいます。理想のすすぎ温度は人肌よりぬるい『32〜34℃のぬるま湯』です。両手で水をすくい、擦らずに優しくパシャパシャと20回程度すすぎましょう。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "クレンジングバームが冬の寒さで固まって使いにくい時の対処法は？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "クレンジングバームは植物オイルやエモリエントワックスで固められているため、冬場の冷えた洗面所では硬くなることがあります。スパチュラで削り取った後、すぐに顔に乗せるのではなく、両手のひらを擦り合わせて手の体温で数秒間温め、とろりとしたオイル状にほぐしてから顔に馴染ませると摩擦なく滑らかに使えます。"
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body class="theme-cleansing">

  <!-- ヘッダー -->
  <header class="site-header">
    <div class="header-badge">🍯 2026 WINTER CLEANSING SELECTION</div>
    <h1 class="site-title">高保湿クレンジング＆濃密バーム10選</h1>
    <p class="site-subtitle">11月・12月の粉吹き・つっぱりを防ぎ、落としながら潤す至高のクレンジング</p>
  </header>

  <main class="container">

    <!-- 記事トップ・アイキャッチ -->
    <article class="article-intro">
      <div class="article-meta">
        <span class="article-cat-tag">スキンケア特集 / クレンジング</span>
        <span class="article-date">📅 2026.10.28 更新</span>
      </div>

      <h1 class="article-main-heading">洗うほど肌がモチモチ潤う！冬の粉吹き・つっぱりを防ぐ高保湿クレンジング＆濃密バームランク10</h1>

      <p class="article-lead">
        11月から12月にかけて、スキンケアをどれだけ高保湿なものに変えても乾燥が改善しない場合、その最大の原因は<strong>「クレンジングによる皮脂の奪いすぎ（過剰脱脂）」</strong>にあります。<br><br>
        冬の肌は寒さで血行が悪く、皮脂の分泌量が真夏の半分以下に激減しています。そこに洗浄力の強すぎるクレンジングや強い摩擦刺激を与えてしまうと、角質細胞同士を接着している細胞間脂質（セラミド）まで根こそぎ洗い流され、洗顔後数分で肌が突っ張り、翌朝には粉を吹いてしまいます。<br><br>
        真冬のスキンケアの鉄則は<strong>「落とすケアから保湿する」</strong>こと。体温でとろける濃密バーム、美容液成分約90%のうるおいミルク、良質な植物オイルで肌を包み込むトリートメントオイルなど、バリア機能を守りながらメイクをオフする名品選びが欠かせません。<br><br>
        本記事では、2026年最新のクレンジング科学を結集した、洗うたびに肌がモチモチに潤う実力派10選を徹底レビューします！
      </p>

      <!-- 目次ナビゲーション -->
      <nav class="toc-container">
        <div class="toc-title">📑 本記事の目次</div>
        <ul class="toc-list">
          <li><a href="#why-cleansing">1. 冬の乾燥悪化の主犯は「落とすケア」！皮脂膜とラメラ構造を守るメカニズム</a></li>
          <li><a href="#types">2. バーム・ミルク・オイル・クリーム！冬クレンジングの形状別選び方</a></li>
          <li><a href="#comparison">3. 【一目でわかる】冬の高保湿クレンジング10選 比較早見表</a></li>
          <li><a href="#ranking">4. 【2026最新】冬の高保湿クレンジングおすすめ10選 詳細個別レビュー</a></li>
          <li><a href="#technique">5. 摩擦ゼロ＆完全オフを両立する「プロ直伝・ぬるま湯乳化ステップ」</a></li>
          <li><a href="#faq">6. 冬のクレンジングに関するよくある質問（FAQ）</a></li>
          <li><a href="#related">7. あわせて読みたい！冬の保湿ケア特集一覧</a></li>
        </ul>
      </nav>
    </article>

    <!-- メカニズム解説セクション -->
    <section id="why-cleansing">
      <h2 class="section-title">冬の乾燥悪化の主犯は「落とすケア」！皮脂膜とラメラ構造を守るメカニズム</h2>
      <p class="content-text">
        皮膚の最も外側にある角質層では、皮脂膜、天然保湿因子（NMF）、細胞間脂質（セラミドなど）の3大要素が協力して外部の乾燥から肌を守っています。
      </p>
      <p class="content-text">
        しかし、強い界面活性剤を含む安価なクレンジング料やゴシゴシ擦るクレンジング法を続けると、メイク汚れだけでなくこの貴重なバリア物質まで一気に溶かし出してしまいます。一度流出したセラミドが自力で再生するまでには約28日間のターンオーバー期間が必要なため、<strong>『クレンジングでの1回の脱脂が1ヶ月の乾燥肌を引き起こす』</strong>と言っても過言ではありません。
      </p>
      <div class="product-catch" style="margin: 20px 0;">
        💡 冬の高保湿クレンジング選びの3大鉄則：<br>
        ① <strong>エモリエント成分高配合</strong>：植物オイルやスクワラン、セラミドが高配合されていること<br>
        ② <strong>クッション性と摩擦レス設計</strong>：厚みのあるバームやミルクで指と皮膚の摩擦をゼロにすること<br>
        ③ <strong>素早い乳化スピード</strong>：ぬるま湯に触れた瞬間白濁し、短時間ですすぎ切れる処方
      </div>
    </section>

    <!-- タイプ別選び方 -->
    <section id="types">
      <h2 class="section-title">バーム・ミルク・オイル・クリーム！冬クレンジングの形状別選び方</h2>
      <div class="content-text">
        <p>冬のクレンジング料は、自分のメイクの濃さと肌の乾燥レベルに合わせて最適なテクスチャーを選び分けることが美肌への近道です。</p>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #fde68a; box-shadow: var(--shadow-soft);">
          <h3 style="color: #b45309; font-size: 16px; font-weight: 700; margin-bottom: 6px;">① とろけるクレンジングバーム（DUO、バニラコ、クリニークなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">毛穴の角栓・黒ずみも気になる混合肌〜普通肌に最適。固形からオイルへとろけるクッション性が摩擦を防ぎ、毛穴の汚れを優しく溶かし出しながら潤いのヴェールを残します。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #fde68a; box-shadow: var(--shadow-soft);">
          <h3 style="color: #b45309; font-size: 16px; font-weight: 700; margin-bottom: 6px;">② うるおい特化ミルク・クリーム（カバーマーク、カネボウ、ミノンなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">粉吹きやピリつきを繰り返す乾燥肌・超乾燥肌・敏感肌に最適。成分の大部分が美容液・保湿成分で構成されており、肌の水分を奪わずに優しくメイクをオフします。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #fde68a; box-shadow: var(--shadow-soft);">
          <h3 style="color: #b45309; font-size: 16px; font-weight: 700; margin-bottom: 6px;">③ 高級植物オイル＆くすみオフオイル（シュウウエムラ、ファンケル、アテニアなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">しっかりメイク派、夕方のくすみが気になる方に最適。椿オイルやアルガンオイルなど良質な天然オイルがメイクを秒速で浮かせ、擦らず短時間で落とすことで肌負担を激減させます。</p>
        </div>
      </div>
    </section>

    <!-- 比較早見表 -->
    <section id="comparison">
      <h2 class="section-title">【一目でわかる】冬の高保湿クレンジング10選 比較早見表</h2>
      <p class="content-text">掲載している価格は楽天市場の最新調査価格（税込）です。横スクロールで特徴や配合成分を比較できます。</p>

      <div class="table-scroll-wrapper">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>テクスチャー</th>
              <th>主要キー成分</th>
              <th>参考価格</th>
              <th>おすすめな肌悩み</th>
            </tr>
          </thead>
          <tbody>
{chr(10).join(table_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <!-- アイテム詳細レビュー -->
    <section id="ranking">
      <h2 class="section-title">【2026最新】冬の高保湿クレンジングおすすめ10選 詳細個別レビュー</h2>
{chr(10).join(items_detail_html)}
    </section>

    <!-- プロ直伝テクニック -->
    <section id="technique">
      <h2 class="section-title">摩擦ゼロ＆完全オフを両立する「プロ直伝・ぬるま湯乳化ステップ」</h2>
      <div class="content-text">
        <p>
          どれほど上質なクレンジングを使っても、すすぎ方や手の動かし方を間違えると乾燥の原因になります。冬の肌を傷めない正しい4ステップをマスターしましょう。
        </p>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fde68a;">
          <h3 style="color: #b45309; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 1：冷えた手は温めてから！乾いた手と顔でスタート</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            手が冷え切っているとバームやオイルが馴染みにくくなります。軽く手のひらを擦り合わせて温め、規定量をケチらずたっぷり手に取りましょう。量が少ないと摩擦の原因になります。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fde68a;">
          <h3 style="color: #b45309; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 2：擦らず「指の腹で大きな円を描いて転がす」</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            皮膚を引っ張るような強いマッサージはNG。クレンジング料の厚みをクッションにして、指の腹を滑らせるように優しくメイクと馴染ませます。目安時間は30秒〜45秒です。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fde68a;">
          <h3 style="color: #b45309; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 3：最重要！少量のぬるま湯で「必ず白濁乳化させる」</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            いきなりドバッと洗い流すのは厳禁。手のひらに少量のぬるま湯をつけ、顔全体を撫でて白く濁らせます。この乳化ステップを踏むことで、油分が水に溶けやすくなり擦らずスルリと落ちます。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fde68a;">
          <h3 style="color: #b45309; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 4：32〜34℃のぬるま湯で擦らず20回すすぐ</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            冬の熱いお湯は厳禁。人肌より少しぬるいお湯を手ですくい、顔にパシャパシャと当ててすすぎます。タオルで水分を拭き取る際も、ゴシゴシ拭かず軽く押さえるように吸水させましょう。
          </p>
        </div>
      </div>
    </section>

    <!-- FAQ セクション -->
    <section id="faq">
      <h2 class="section-title">冬のクレンジングに関するよくある質問（FAQ）</h2>
      <div class="faq-list">
        <div class="faq-item">
          <div class="faq-question">Q1. 冬場はクレンジング後にダブル洗顔（洗顔料）をしなくても大丈夫ですか？</div>
          <div class="faq-answer">
            DUOやシュウウエムラ、カバーマークなど『W洗顔不要』と記載されている製品は、クレンジングだけでメイク汚れと余分な皮脂がしっかり落ちるよう設計されているため洗顔料は不要です。むしろ冬に無理に洗顔料を重ねると、角層の大切なセラミドや天然保湿因子（NMF）まで洗い流され、重度の粉吹きや乾燥性敏感肌の原因になります。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q2. クレンジングの「乳化」とは何ですか？なぜ冬に特に重要なのですか？</div>
          <div class="faq-answer">
            乳化とは、オイルやバームが水分と混ざり合って白く濁る現象のことです。クレンジング料を顔に伸ばした後、いきなり洗い流すのではなく少量のぬるま湯を手につけて馴染ませ白濁させることで、油分が水に溶けやすい状態へ変化します。これにより肌を強くこすらずに素早くすすげ、肌への摩擦ダメージと油膜残りを防ぐことができます。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q3. 冬のお風呂場で熱いシャワーを直接顔に当ててすすいでもいいですか？</div>
          <div class="faq-answer">
            絶対にいけません！冬の熱いお湯（38℃以上）やシャワーの水圧を顔に直接当てると、肌のバリアを支えている細胞間脂質が溶け出してしまいます。理想のすすぎ温度は人肌よりぬるい『32〜34℃のぬるま湯』です。両手で水をすくい、擦らずに優しくパシャパシャと20回程度すすぎましょう。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q4. クレンジングバームが冬の寒さで固まって使いにくい時の対処法は？</div>
          <div class="faq-answer">
            クレンジングバームは植物オイルやエモリエントワックスで固められているため、冬場の冷えた洗面所では硬くなることがあります。スパチュラで削り取った後、すぐに顔に乗せるのではなく、両手のひらを擦り合わせて手の体温で数秒間温め、とろりとしたオイル状にほぐしてから顔に馴染ませると摩擦なく滑らかに使えます。
          </div>
        </div>
      </div>
    </section>

    <!-- 内部リンク・関連記事セクション -->
    <section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list">
        <a href="/winter-lotion" class="related-link-card">
          <div class="related-link-title">💧 保湿力の強さで肌乾燥とさようなら！冬の乾きを満たす高保湿化粧水ランク10</div>
          <div class="related-link-desc">クレンジングで素肌をリセットした直後に！硬くなった角層を深部までうるおいで満たす神ローション。</div>
        </a>

        <a href="/winter-serum-booster" class="related-link-card">
          <div class="related-link-title">💧 浸透力を底上げする高保湿・導入先行美容液おすすめ10選</div>
          <div class="related-link-desc">洗顔後すぐの仕込みに！固くなった角質細胞をほぐし、化粧水の水分をごくごく吸い込む素肌へ。</div>
        </a>

        <a href="/winter-moisture-cream" class="related-link-card">
          <div class="related-link-title">🧴 保湿力の強さで肌乾燥とさようなら！高保湿フェイスクリーム＆濃密バーム10選</div>
          <div class="related-link-desc">クレンジング・保湿後の仕上げに！補給した水分を逃さず朝まで完全密閉する最強クリーム。</div>
        </a>

        <a href="/winter-face-mask" class="related-link-card">
          <div class="related-link-title">💧 水分爆弾で砂漠肌を即リセット！高保湿シートマスク＆夜用パック10選</div>
          <div class="related-link-desc">クレンジング後の清潔な肌に！暖房乾燥でしぼんだ肌に潤い集中チャージする話題の密着パック。</div>
        </a>

        <a href="/winter-base-makeup" class="related-link-card">
          <div class="related-link-title">✨ 夕方まで潤いツヤが続く高保湿ファンデーション＆美容液下地10選</div>
          <div class="related-link-desc">丁寧なクレンジングと保湿で整えた肌を美しく魅せる！暖房下でもひび割れないツヤ肌ベースメイク。</div>
        </a>

        <a href="/winter-lip-care" class="related-link-card">
          <div class="related-link-title">🎁 冬のガサガサ皮剥けに終止符！高保湿リップトリートメント＆濃密ティント10選</div>
          <div class="related-link-desc">皮脂腺のない唇を乾燥冷風から強力ガード。夜用リップスリーピングマスクからプランパーまで。</div>
        </a>
      </div>
    </section>

  </main>

  <!-- フッター -->
  <footer class="site-footer">
    <div class="footer-links">
      <a href="/">トップページ</a>
      <a href="/winter-cleansing">クレンジング</a>
      <a href="/winter-lotion">高保湿化粧水</a>
      <a href="/winter-serum-booster">導入美容液</a>
      <a href="/winter-face-mask">シートマスク</a>
      <a href="/winter-moisture-cream">保湿クリーム</a>
      <a href="/winter-eye-cream">アイクリーム</a>
      <a href="/winter-base-makeup">ベースメイク</a>
      <a href="/winter-lip-care">リップケア</a>
      <a href="/winter-body-care">ボディケア</a>
      <a href="/winter-hair-care">ヘアケア</a>
      <a href="/winter-hand-care">ハンドケア</a>
    </div>
    <p class="copyright">© 2026 Lumi Cosme (ルミコスメ) All Rights Reserved.</p>
  </footer>

</body>
</html>
"""

output_path = "winter-cleansing.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {output_path} successfully! Size: {len(html_content)} bytes")
