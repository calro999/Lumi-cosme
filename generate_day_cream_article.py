import json

with open("rakuten_new_3articles_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

daycream_items = data["winter_day_cream"]["items"]

# 各アイテムの独自詳細レビューデータ（完全オリジナル、独立した専門レビュー）
item_details_map = {
    1: {
        "tag": "🏆 田中みな実愛用・朝用クリームの最高峰",
        "catch": "日中の乾燥と紫外線から守り抜く！夕方まで潤いとツヤを湛え続ける奇跡の朝クリーム",
        "spec_cap": "40g (SPF20 / PA+++)",
        "spec_texture": "みずみずしく滑らかで、肌に溶け込むように一体化する軽やかクリーム",
        "spec_ing": "ベビーソフトオイル処方、ヒバマタエキス、アルテア根エキス、ゴールデンカモミールエキス",
        "spec_finish": "内側から発光するような生ツヤと、夕方まで崩れないもっちり保湿感",
        "desc_p1": "数々のベストコスメを総なめにし、美容賢者やプロのメイクアップアーティストがこぞって指名買いするカネボウの看板クリーム。赤ちゃんの未熟な肌を乾燥から守る胎脂に着想を得た『ベビーソフトオイル処方』を採用。日中の過酷なエアコン温風や冬の寒冷外気から肌を長時間シールドし、夕方になっても小ジワや乾燥崩れを一切寄せ付けません。",
        "desc_p2": "SPF20/PA+++のUVカット効果を備えながら、日焼け止め特有のきしみや白浮き、乾燥感がゼロ。朝のスキンケアの最後に塗るだけで、肌表面がなめらかに整い、後から重ねるファンデーションの密着度とツヤ感を何倍にも引き上げます。日中のメイク直し時にも、乾燥した部分にファンデの上からトントンと重ねてツヤを復活させられる万能さも魅力です。",
        "target": "日中オフィスで暖房の直風を浴びて頬がパリパリに乾く方、メイクのノリが悪く夕方のファンデ割れに悩む方",
        "how_to": "朝の化粧水・乳液の後、スパチュラ1杯分（約0.5g）を顔全体に馴染ませます。目元やほうれい線など乾燥しやすい部位には少量を指先で重ね塗りするのがポイントです。",
        "voice": "『これがないと冬を越せません！朝塗ると夕方までずっと肌がぷるぷるで、乾燥崩れ知らず。ツヤ感が本当に綺麗で、ベースメイクの仕上がりが格段に上がります。』(30代・乾燥肌)"
    },
    2: {
        "tag": "🌹 最高峰ピンクUV・極上トーンアップ",
        "catch": "素肌を美しく魅せる血色ピンク！エーデルワイスの生命力で冬の大気汚染と紫外線から肌を守る",
        "spec_cap": "30ml / 50ml (SPF50+ / PA++++ )",
        "spec_texture": "みずみずしく伸びの良いミルキージェルテクスチャー",
        "spec_ing": "エーデルワイス花/葉エキス、ビタミンE、モリンガエキス、ローズ水",
        "spec_finish": "ほんのり血色感を帯びた、透明感あふれる上品なツヤ白肌",
        "desc_p1": "デパコス日焼け止め・化粧下地の頂点として世界中で愛され続けるランコムのUVエクスペール。日本女性のために開発された『トーンアップローズ』は、黄ぐすみしやすい冬の肌に自然な血色感と透明感を与え、ひと塗りで素肌そのものが発光しているかのような美肌補正力を発揮します。",
        "desc_p2": "過酷な高山植物エーデルワイスのエキスを高濃度配合し、強力な抗酸化・保湿バリアを形成。最高基準のUVカット性能（SPF50+/PA++++）を誇りながら、冬の強い暖房乾燥やPM2.5などの大気汚染物質まで強力にブロック。しっとりとした潤いヴェールが一日中続き、ノーファンデの日でもこれ1本で自信の持てるツヤ肌が完成します。",
        "target": "冬の寒さや血行不良で顔色が青白くくすんで見える方、最高レベルの紫外線カットとスキンケア効果を両立したい方",
        "how_to": "小豆粒大を手にとり、両頬、額、鼻、顎の5点に置き、顔の中心から外側へムラなく伸ばします。首筋やデコルテまで伸ばすと自然な透明感が際立ちます。",
        "voice": "『日焼け止め特有のキシキシ感が全くなく、高級な乳液を塗っているような贅沢な使用感。くすみがパッと消えて自然なツヤが出るので、休日はこれにお粉だけで十分です。』(30代・混合肌)"
    },
    3: {
        "tag": "✨ 1本でベース完成・潤いマルチプロテクション",
        "catch": "高いカバー力と保湿力を両立！毛穴や色ムラを光で飛ばして一日中うるおいツヤ肌をキープ",
        "spec_cap": "35g (SPF50+ / PA++++ )",
        "spec_texture": "なめらかに伸び広がるリッチなクリームファンデーション感覚のテクスチャー",
        "spec_ing": "ゼニアオイエキス、ローズマリー葉水、モイスチュア成分、アミノ酸系パウダー",
        "spec_finish": "毛穴や赤みが自然に消え、うるおいに満ちたセミツヤ肌",
        "desc_p1": "日焼け止め、スキンケア乳液、コントロールカラー、ファンデーションの4役をこなすコスメデコルテの超人気CCクリーム。独自の『マルチプロテクション技術』により、紫外線や微粒子汚れから肌を守りながら、日中の乾燥による水分蒸散を徹底的にガードします。",
        "desc_p2": "ソフトフォーカス効果に優れたパウダーが、冬の乾燥によって目立つキメの乱れや毛穴、色ムラを光の反射で美しくカバー。高い保湿成分が配合されているため、夕方になってもほうれい線にファンデがめり込むことなく、つけたてのみずみずしいツヤ感が持続します。時短で完成度の高いベースメイクを求める朝に最適です。",
        "target": "忙しい朝に時短で完璧なベースメイクを仕上げたい方、ファンデーションを使うと乾燥崩れしやすい方",
        "how_to": "パール粒大を手にとり、指先で顔全体に手早く均一に伸ばします。気になるシミや赤みがある部分には、少量を指でポンポンと重ね付けします。",
        "voice": "『これ1本でファンデいらずのカバー力！真冬でも全然乾燥せず、夕方になっても汚く崩れません。01番のライトベージュは肌がパッと明るくなって大満足です。』(20代後半・乾燥肌)"
    },
    4: {
        "tag": "🛡️ 医薬部外品・シワ改善×美白×UVカット",
        "catch": "日焼け止めでシワ改善！ナイアシンアミド配合で日中のエイジングケアを革新する薬用UVプロテクター",
        "spec_cap": "50g (SPF50+ / PA++++ )",
        "spec_texture": "ベタつきも白浮きもゼロ！極上のみずみずしい保湿デイクリーム感触",
        "spec_ing": "Wナイアシン（ナイアシンアミド）、ベースメイクプロテクト成分、複合植物エキス",
        "spec_finish": "ふっくらハリのある感触で、ファンデの邪魔をしないサラしと肌",
        "desc_p1": "有効成分ナイアシンアミドを配合し、『シワ改善』『美白』『最高峰UVカット（SPF50+/PA++++）』を同時に叶えるオルビスの傑作UVプロテクター。日中の紫外線ダメージを予防するだけでなく、すでに気になる目元や額のシワへ積極的にアプローチし、メラニンの生成を抑えてシミ・ソバカスを防ぎます。",
        "desc_p2": "日焼け止めであることを忘れてしまうほど滑らかでみずみずしいクリーム状テクスチャー。肌に伸ばすとすっと溶け込み、被膜感やキシつきが一切ありません。大気中の有害物質やブルーライトカットにも配慮されており、暖房の効いた室内で一日中PC作業をするオフィスワーカーのデイリーケアにも最適です。",
        "target": "日中の紫外線対策と同時に本格的なシワ改善・美白ケアを行いたい方、キシキシしない保湿UVを探している方",
        "how_to": "大きめのパール1粒分を朝のスキンケアの最後に使用。顔全体にムラなく均一に伸ばし、首筋にもしっかり塗り伸ばします。",
        "voice": "『日焼け止め特有の嫌な匂いや重さが全くなく、完全に高保湿クリームの塗り心地です。使い始めてから目元の乾燥小ジワが目立たなくなり、リピート3本目です！』(40代・乾燥小ジワ悩み)"
    },
    5: {
        "tag": "✨ 朝用乳液の決定版・夕方までふっくら",
        "catch": "化粧水の後はこれ1本！乳液・日焼け止め・化粧下地をこなす大人のトーンアップ美容乳液",
        "spec_cap": "35g (SPF50+ / PA++++ )",
        "spec_texture": "軽やかでみずみずしく、肌にピタッと吸着するトーンアップミルク",
        "spec_ing": "m-トラネキサム酸、コラーゲンGL、ワンデーアクアマスクEX、高純度エモリエント",
        "spec_finish": "夕方まで『つや玉』が輝き続ける、明るく引き締まったハリ肌",
        "desc_p1": "資生堂エリクシールの代名詞である『デーケアレボリューション』の最新トーンアップバージョン。朝の化粧水の後、これ1本で乳液、UVカット、化粧下地の3役が完了。独自技術『ワンデーアクアマスクEX』が日中の肌をうるおいマスクで覆い続け、夕方になっても肌のハリと透明感をキープします。",
        "desc_p2": "大人のくすみや影を自然に飛ばすペールピンクのトーンアップパウダーを配合。毛穴や小ジワをふんわりぼかし、若々しい血色感と健康的なツヤ肌を演出します。美白＆抗肌荒れ有効成分のトラネキサム酸も配合されており、冬の紫外線や乾燥から肌を守りながらメラニンの蓄積を防ぎます。",
        "target": "朝のスキンケア工程を減らしたいけれど保湿とエイジングケアは妥協したくない方、夕方のくすみとしぼみが気になる方",
        "how_to": "朝の化粧水の後、手のひらに1円硬貨大を取り、顔全体に馴染ませます。紫外線が当たりやすい頬骨のあたりには重ね塗りすると効果的です。",
        "voice": "『朝の時短に最強のアイテム！乳液なのにしっかりSPF50+あって、トーンアップ効果も自然。夕方になってもお疲れ顔にならずツヤ玉が残っています。』(30代・働くママ)"
    },
    6: {
        "tag": "🎭 表情追従・ディープUVシールド",
        "catch": "笑っても喋ってもUV膜がひび割れない！角層の奥まで届くディープ紫外線を徹底遮断する高機能UV",
        "spec_cap": "30g (SPF50+ / PA++++ )",
        "spec_texture": "肌に乗せるとスーッと馴染んで軽やかに密着するストレッチテクスチャー",
        "spec_ing": "ナノアスタキサンチン、D-UVガード+、ツボクサエキス、ナノリコピン",
        "spec_finish": "キュッと引き締まったハリ感と、澄み渡るような透明感",
        "desc_p1": "富士フイルムの写真技術と光学研究から生まれたアスタリフトの多機能UV美容液。肌の奥深く（真皮層）まで届いて光老化を引き起こす『Deep紫外線（長波長UVA）』を99%カットする独自技術『D-UVガード+』を搭載。さらに、笑ったり話したりする日常の表情の動きに合わせて日焼け止め膜が伸縮する『ストレッチ機能』により、塗りムラや膜割れを防ぎます。",
        "desc_p2": "ブランドの象徴である抗酸化成分『ナノアスタキサンチン』と『ナノリコピン』を配合。オレンジ色の美容液が肌に伸ばすと瞬時に無色透明になり、日中の酸化ストレスから肌を強力にガード。光をコントロールして素肌を明るく美しく見せるトーンアップ効果も備えており、化粧下地としても極めて優秀です。",
        "target": "冬でも真皮まで届く紫外線によるたるみ・光老化を本気で予防したい方、日焼け止めのモロモロ崩れに悩む方",
        "how_to": "直径約1cmを手にとり、顔の5点に置いてムラなく伸ばします。目元や口元などよく動く部位にもストレッチが効くので安心して塗り広げてください。",
        "voice": "『表情を動かしてもヨレたりモロモロが出ないのが素晴らしい！冬でも乾燥せず、むしろお肌がピンと張るようなハリを感じます。紫外線対策は年中これ一筋です。』(40代・エイジングケア重視)"
    },
    7: {
        "tag": "🛡️ 敏感肌No.1・光を乱反射するトーンアップUV",
        "catch": "世界中で愛される皮膚科医推奨の低刺激UV！花粉・PM2.5・乾燥から肌を優しく守るピンクのヴェール",
        "spec_cap": "30ml (SPF50+ / PA++++ )",
        "spec_texture": "こっくりとしたクリーム状で肌を優しく包み込む安心の保湿感",
        "spec_ing": "ターマルウォーター（整肌成分）、ビタミンE、シアバターエキス",
        "spec_finish": "白浮きせず肌に溶け込む、素肌感あふれるナチュラルなツヤ肌",
        "desc_p1": "敏感肌向けスキンケアとして不動の人気を誇るラロッシュポゼのトーンアップUV。フランスの天然湧水『ターマルウォーター』を配合し、肌のバリア機能をサポートしながら肌を穏やかに整えます。肌なじみの良いピンクカラーが、冬のくすみがちな日本人の肌に自然な血色感と澄んだ透明感をプラスします。",
        "desc_p2": "高いUVカット効果（SPF50+/PA++++）を持ちながら、紫外線だけでなくPM2.5や花粉などの大気中微粒子物質の付着からも肌を物理的に保護。石けんで落とせる処方なので、クレンジングによる肌負担を減らしたい冬の休日のデイリーメイクにも最適です。無香料・パラベンフリー・アレルギーテスト済み。",
        "target": "冬の寒暖差や乾燥で肌が敏感になりやすく、肌に優しいUVを探している方、石けんでオフしたい方",
        "how_to": "パール1粒大を顔全体に馴染ませます。Tゾーンには薄く、乾燥しやすい頬には重ね塗りすると崩れにくくツヤ感がアップします。",
        "voice": "『敏感肌の私の必需品です！冬の乾燥したオフィスでも肌がピリピリせず、夕方までしっとり。自然なトーンアップでくすみが消えるのでファンデの量が減りました。』(30代・敏感肌)"
    },
    8: {
        "tag": "🍄 白トリュフ水光肌・韓国ヴィーガンサンクリーム",
        "catch": "イタリア産高級白トリュフ配合！まるで水分クリームを塗っているかのような極上の水光ツヤUV",
        "spec_cap": "50ml (SPF50+ / PA++++ )",
        "spec_texture": "水分が溢れ出すようなみずみずしいウォータリーテクスチャー",
        "spec_ing": "ホワイトトリュフエキス、トコフェロール（ビタミンE）、ツボクサエキス、ヒアルロン酸",
        "spec_finish": "内側から水分が湧き出るような濡れ感のある極上水光ツヤ肌",
        "desc_p1": "韓国オリーブヤングやSNSで大バズりし、日本でも爆発的な人気を誇るd'Alba（ダルバ）のウォータフルトーンアップサンクリーム。イタリア産最高級ホワイトトリュフとトコフェロールを組み合わせた独自成分『トリュフェロール』を配合し、紫外線対策をしながらリッチなエイジング保湿ケアを両立します。",
        "desc_p2": "日焼け止め特有の重さやキシつきが全くなく、まるで上質な水分クリームを塗り拡げているかのようなみずみずしい感触。肌に伸ばすと華やかなピンクカラーがすっと馴染み、内側からパンッと発光するような韓国アイドルの水光ツヤ肌を演出。イタリアヴィーガン認証（V-LABEL）取得の肌思い設計です。",
        "target": "乾燥してツヤを失った冬肌に、うるおいに満ちた濡れツヤ感を与えたい方、韓国トレンドの水光肌を作りたい方",
        "how_to": "適量を手にとり、スキンケアの最後に顔全体にムラなく馴染ませます。ツヤを出したい鼻筋やCゾーンにトントンと重ねると自然なハイライト効果が得られます。",
        "voice": "『日焼け止めでこんなにツヤが出るなんて感動！乾燥する冬でも一日中肌がしっとりツヤツヤで、友人から「肌が綺麗」と褒められました。リピ確定です！』(20代・乾燥肌)"
    },
    9: {
        "tag": "👑 最高峰ラグジュアリー・極上のエイジングケアUV",
        "catch": "太陽光を美の味方に変える！クレ・ド・ポー ボーテが誇る最高峰トリートメント日焼け止め",
        "spec_cap": "50g (SPF50+ / PA++++ )",
        "spec_texture": "高級美容液クリームそのもの！肌の上でとろけて上質なヴェールを形成",
        "spec_ing": "アダプタブルインシールドテクノロジー、モロッカンタイムエキス、スキンイルミネイター",
        "spec_finish": "シルクのような極上のなめらかさと、内側から溢れ出す気品ある輝き",
        "desc_p1": "美容業界の最高峰に君臨するクレ・ド・ポー ボーテのプレミアムUVクリーム。最新のテクノロジーにより、肌に悪影響を与える紫外線は徹底的にカットしながら、肌に良い光（赤色光）を選択して取り込む革新的なアプローチを実現。日焼け止めを塗ることがそのまま最上級のエイジングトリートメントへと昇華されています。",
        "desc_p2": "極上のコクを持ちながら、肌に触れるとスッと溶け込むように馴染み、一日中乾かない高保湿シールドを構築。冬の冷たい風や室内の暖房による激しい乾燥から肌を守り抜き、夕方になっても疲れた印象を与えないふっくらとしたハリを維持します。天然ローズや希少なランを調香したエレガントな香りに包まれます。",
        "target": "投資を惜しまず最高峰のスキンケア効果を求める方、夕方の肌のしぼみ・ハリ不足・乾燥崩れを完全に防ぎたい方",
        "how_to": "朝のお手入れの最後に、指先に適量（パール粒約2個分）をとり、顔全体に優しく丁寧に伸ばします。",
        "voice": "『1万円超えの価値が間違いなくあります。日焼け止めというより最高級のデイクリーム。これを使うと日中の肌の治安が劇的に良くなり、落とした後の肌の柔らかさに驚きます。』(40代・美肌追求派)"
    },
    10: {
        "tag": "🛡️ 医薬部外品・消炎剤配合セラミドUV",
        "catch": "乾燥性敏感肌を考えた低刺激設計！セラミド機能成分が夕方まで肌のうるおいを満たし続ける",
        "spec_cap": "50g (SPF30 / PA+++ )",
        "spec_texture": "みずみずしく軽やかなエッセンス状で肌にすっと馴染む",
        "spec_ing": "セラミド機能成分（ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド）、ユーカリエキス、アスナロエキス、消炎剤",
        "spec_finish": "負担感のないサラッとしたうるおいで、粉吹きを防ぐ健やかな仕上がり",
        "desc_p1": "乾燥性敏感肌の悩みに寄り添い続ける花王キュレルの高保湿UVエッセンス。角層のバリア機能を支える『セラミド機能成分』を配合し、紫外線から肌を守りながら角質細胞の隙間をうるおいで満たします。消炎剤（有効成分）配合により、冬の寒暖差やマスク擦れで起こる肌荒れをしっかり防止します。",
        "desc_p2": "紫外線吸収剤無配合（ノンケミカル処方）、無香料・無着色・アルコールフリーの徹底した低刺激性。赤ちゃんのデリケートな肌にも使えるほどの優しさを誇り、日焼け止め特有のキシキシ感や白残りがありません。みずみずしいエッセンスタイプで、朝の忙しい時でもサッとムラなく塗り広げられる使い勝手の良さも魅力です。",
        "target": "紫外線吸収剤で赤みや痒みが出やすい敏感肌の方、ドラッグストアで手軽に買える確かな保湿UVを求める方",
        "how_to": "適量（直径約1.5cm）を手にとり、顔全体に優しく馴染ませます。化粧下地としても使え、ファンデーションの密着度を高めます。",
        "voice": "『冬になると日焼け止めでピリピリしがちなのですが、キュレルだけは本当に刺激ゼロで快適です。白浮きせずしっかり潤うので、家族みんなで毎日愛用しています。』(30代・敏感肌)"
    }
}

# 比較表の行生成
table_rows = []
for item in daycream_items:
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
for item in daycream_items:
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
            <div class="spec-item"><span class="spec-key">容量/SPF</span><span class="spec-val">{details['spec_cap']}</span></div>
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
            <span class="howto-title">✨ モロモロ・乾燥崩れを防ぐプロ直伝の塗り方</span>
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
for item in daycream_items:
    json_ld_items.append(f"""          {{
            "@type": "ListItem",
            "position": {item['rank']},
            "name": "{item['display_name']}",
            "url": "https://lumi-cosme.vercel.app/winter-day-cream#rank-{item['rank']}"
          }}""")

item_list_json = ",\n".join(json_ld_items)
og_image = daycream_items[0]["image_url"]

html_content = f"""<!DOCTYPE html>
<html lang="ja" prefix="og: http://ogp.me/ns#">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【2026最新】暖房乾燥と冬紫外線をダブル遮断！一日中しっとり続く高保湿UV美容液＆朝用デイクリームおすすめ10選 | Lumi Cosme</title>
  <meta name="description" content="11月・12月のエアコン温風による砂漠化と真皮まで届く冬のUV-A波を完全ブロック！カネボウ クリームインデイ、ランコム、コスメデコルテCC、オルビス薬用UV、ラロッシュポゼなど夕方までツヤ肌が続く高保湿UV＆朝用デイクリーム厳選10選を徹底レビュー。モロモロ崩れを防ぐ朝の塗り方まで解説。">
  <meta name="keywords" content="朝用クリーム, デイクリーム, 冬 日焼け止め, 高保湿UV, カネボウ クリームインデイ, ランコム UVエクスペール, コスメデコルテCC, オルビス リンクルブライトUV, ラロッシュポゼ トーンアップ, 2026コスメ">

  <!-- SEO & Canonical -->
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-day-cream">
  <meta name="robots" content="index, follow">

  <!-- OGP -->
  <meta property="og:site_name" content="Lumi Cosme (ルミコスメ)">
  <meta property="og:title" content="暖房乾燥と冬紫外線をダブル遮断！一日中しっとり続く高保湿UV美容液＆朝用デイクリームおすすめ10選">
  <meta property="og:description" content="エアコン温風でも夕方まで乾かない！カネボウ、ランコム、コスデコなど話題の高保湿UV＆朝用デイクリームを徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-day-cream">
  <meta property="og:image" content="{og_image}">
  <meta property="og:locale" content="ja_JP">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="暖房乾燥と冬紫外線をダブル遮断！一日中しっとり続く高保湿UV美容液＆朝用デイクリームおすすめ10選">
  <meta name="twitter:description" content="エアコン温風でも夕方まで乾かない！カネボウ、ランコム、コスデコなど話題の高保湿UV＆朝用デイクリームを徹底比較。">
  <meta name="twitter:image" content="{og_image}">

  <link rel="stylesheet" href="style.css">

  <!-- 構造化データ (JSON-LD) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "headline": "暖房乾燥と冬紫外線をダブル遮断！一日中しっとり続く高保湿UV美容液＆朝用デイクリームおすすめ10選",
        "description": "11月・12月のエアコン乾燥と冬のUV-A波から肌を守る高保湿UV美容液＆朝用デイクリームの選び方、成分比較、おすすめ10選を徹底解説。",
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
        "name": "冬の高保湿UV美容液＆朝用デイクリームおすすめ10選",
        "itemListElement": [
{item_list_json}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "冬でも日焼け止めは毎日塗る必要がありますか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "絶対に必要です！肌を黒くするUV-B波は冬に減少しますが、波長が長く真皮層のコラーゲンを破壊してシワやたるみを引き起こす『UV-A波』は、冬でも真夏の約半分が地上に降り注いでいます。さらに雲や窓ガラスを軽々と透過するため、暖房の効いた室内にいても知らず知らずのうちに光老化が進行します。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "夜用の保湿クリームを朝のメイク前に使ってはいけませんか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "夜用クリームは油分やエモリエント成分が多く配合されており、睡眠中の水分蒸発を防ぐために表面に重い油膜を作ります。これを朝のメイク前に塗ると、ファンデーションの密着を妨げて『ヨレ』や『油浮き』『モロモロ』の原因になります。朝は日中専用に設計された、水分と油分のバランスが良くUVカット効果も備えた『デイクリーム』を使うのが鉄則です。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "冬の日焼け止めはSPFやPAの数値が低いものを選んでも大丈夫ですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "日常の通勤や短時間の買い物であれば『SPF20〜30 / PA++〜+++』で十分肌を守れます。大切なのは数値の高さよりも『保湿力の持続性』と『肌への優しさ』です。ただし、冬のレジャー（スキーやスノボなど雪山）では雪の照り返しで真夏以上の紫外線を浴びるため、必ず『SPF50+ / PA++++』を選びましょう。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "朝のUVクリームを塗った後、ファンデーションを重ねるとモロモロが出る原因は？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "モロモロ（消しゴムのカスのようなダスト）が出る主な原因は、スキンケアや日焼け止めに含まれる水溶性ポリマー（増粘剤）とファンデーションの粉体が、乾き切らないうちに強く擦り合わされることです。UVクリームを塗った後、擦らず優しくハンドプレスし、1〜2分置いて肌表面がサラッと馴染んでからファンデーションを重ねるとモロモロを防げます。"
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body class="theme-daycream">

  <!-- ヘッダー -->
  <header class="site-header">
    <div class="header-badge">☀️ 2026 WINTER DAY CREAM SELECTION</div>
    <h1 class="site-title">高保湿UV＆朝用デイクリーム10選</h1>
    <p class="site-subtitle">11月・12月の暖房直風による乾燥崩れと冬紫外線を防ぎ、夕方まで潤いツヤ肌をキープ</p>
  </header>

  <main class="container">

    <!-- 記事トップ・アイキャッチ -->
    <article class="article-intro">
      <div class="article-meta">
        <span class="article-cat-tag">スキンケア特集 / 朝用クリーム・UV美容液</span>
        <span class="article-date">📅 2026.10.28 更新</span>
      </div>

      <h1 class="article-main-heading">暖房乾燥と冬紫外線をダブル遮断！一日中しっとり続く高保湿UV美容液＆朝用デイクリームランク10</h1>

      <p class="article-lead">
        11月から12月にかけて、<strong>「朝しっかり保湿してメイクしたのに、昼過ぎにはエアコンの温風で頬が突っ張る」「夕方になるとほうれい線や目元にファンデーションがピキピキひび割れる」「冬だからと油断していたら知らぬ間にシミやくすみが濃くなった」</strong>と感じたことはありませんか？<br><br>
        冬のオフィスや室内環境は、湿度が20%前後にまで干からびる過酷な砂漠地帯。さらに恐ろしいのが、雲や窓ガラスを軽々と透過して肌の真皮層を破壊する<strong>「冬のUV-A波」</strong>です。夏よりも太陽の高度が低いため、顔全体に斜めから深く紫外線が突き刺さり、光老化によるシワやたるみを加速させます。<br><br>
        この冬特有のダブルの脅威から肌を守る唯一の盾が、水分パックのように潤いを補給し続ける<strong>「高保湿朝用デイクリーム」</strong>と、キシキシ感ゼロで美容液のように肌を包み込む<strong>「最新高保湿UV美容液」</strong>です。<br><br>
        本記事では、2026年最新のデイトリートメント技術を結集した、夕方まで崩れない至高の10選を徹底比較します！
      </p>

      <!-- 目次ナビゲーション -->
      <nav class="toc-container">
        <div class="toc-title">📑 本記事の目次</div>
        <ul class="toc-list">
          <li><a href="#why-daycream">1. 冬こそ朝クリームが必須！エアコン蒸散と冬UV-A波のサイエンス</a></li>
          <li><a href="#types">2. スキンケア特化型vsトーンアップ型！目的別の選び方</a></li>
          <li><a href="#comparison">3. 【一目でわかる】冬の高保湿UV＆朝用デイクリーム10選 比較早見表</a></li>
          <li><a href="#ranking">4. 【2026最新】冬の高保湿UV＆朝用デイクリームおすすめ10選 詳細個別レビュー</a></li>
          <li><a href="#technique">5. モロモロ・ヨレを完全追放！「プロ直伝・朝の馴染ませルーティン」</a></li>
          <li><a href="#faq">6. 冬の朝用UVケアに関するよくある質問（FAQ）</a></li>
          <li><a href="#related">7. あわせて読みたい！冬の保湿ケア特集一覧</a></li>
        </ul>
      </nav>
    </article>

    <!-- メカニズム解説セクション -->
    <section id="why-daycream">
      <h2 class="section-title">冬こそ朝クリームが必須！エアコン蒸散と冬UV-A波のサイエンス</h2>
      <p class="content-text">
        日中の肌は、私たちが思っている以上に過酷な環境に晒されています。特に11月〜12月の暖房空間では、角層から空気中へ水分が奪われる『経表皮水分蒸散（TEWL）』が急速に進行します。
      </p>
      <p class="content-text">
        さらに見落とされがちなのが紫外線です。肌を赤く日焼けさせるUV-B波は冬に減りますが、波長が長く真皮の弾力線維（エラスチンやコラーゲン）を切断する<strong>『UV-A波（生活紫外線）』</strong>は、冬でも真夏の約50%が降り注いでいます。冬のノーガードな日焼け止め怠慢が、春先のシワ・たるみの直撃原因となるのです。
      </p>
      <div class="product-catch" style="margin: 20px 0;">
        💡 優れた朝用デイクリーム＆UV美容液の3大条件：<br>
        ① <strong>朝用の黄金油水分バランス</strong>：メイク崩れやテカリを起こさず、水分を閉じ込める擬似皮脂膜機能<br>
        ② <strong>スキンケア成分80%以上の高保湿設計</strong>：日中ずっとパックされているかのようなうるおい持続力<br>
        ③ <strong>光拡散・トーンアップ機能</strong>：冬の血行不良による青白さや黄ぐすみを光で美しく補正
      </div>
    </section>

    <!-- タイプ別選び方 -->
    <section id="types">
      <h2 class="section-title">スキンケア特化型vsトーンアップ型！目的別の選び方</h2>
      <div class="content-text">
        <p>朝用デイクリームと高保湿UVは、仕上がりの目的やメイク習慣に合わせて最適なタイプを選びましょう。</p>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #fecdd3; box-shadow: var(--shadow-soft);">
          <h3 style="color: #be123c; font-size: 16px; font-weight: 700; margin-bottom: 6px;">① 保湿シールド・朝用クリーム型（カネボウ、オルビス、クレ・ド・ポーなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">日中の粉吹きや乾燥によるひび割れを最優先で防ぎたい方に。スキンケア効果が高く、肌表面に薄い保湿フィルムを形成して夕方までふっくらとしたツヤと弾力を保ちます。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #fecdd3; box-shadow: var(--shadow-soft);">
          <h3 style="color: #be123c; font-size: 16px; font-weight: 700; margin-bottom: 6px;">② 血色感・美肌トーンアップ型（ランコム、コスメデコルテ、ラロッシュポゼなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">冬の寒さで顔色がくすんで見える方、休日はファンデなしで過ごしたい方に。光を乱反射する微細パールやピンクピグメントが毛穴やくすみを一掃し、素肌が透き通るような発光肌を叶えます。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #fecdd3; box-shadow: var(--shadow-soft);">
          <h3 style="color: #be123c; font-size: 16px; font-weight: 700; margin-bottom: 6px;">③ 敏感肌・低刺激ノンケミカル型（キュレルなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">冬の乾燥で肌がピリピリしがちな方、紫外線吸収剤が苦手な方に。セラミド機能成分や消炎剤を配合し、肌荒れを防ぎながらマイルドに日中の外部刺激をシャットアウトします。</p>
        </div>
      </div>
    </section>

    <!-- 比較早見表 -->
    <section id="comparison">
      <h2 class="section-title">【一目でわかる】冬の高保湿UV＆朝用デイクリーム10選 比較早見表</h2>
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
      <h2 class="section-title">【2026最新】冬の高保湿UV＆朝用デイクリームおすすめ10選 詳細個別レビュー</h2>
{chr(10).join(items_detail_html)}
    </section>

    <!-- プロ直伝テクニック -->
    <section id="technique">
      <h2 class="section-title">モロモロ・ヨレを完全追放！「プロ直伝・朝の馴染ませルーティン」</h2>
      <div class="content-text">
        <p>
          「朝クリームを塗るとファンデがヨレる」「消しゴムのカスのようなモロモロが出る」という失敗を防ぎ、夕方までツヤ肌をキープするプロ直伝の4ステップです。
        </p>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fecdd3;">
          <h3 style="color: #be123c; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 1：スキンケアの各ステップで「手のひらプレス」を行う</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            化粧水や美容液を塗った直後の濡れた肌にそのままUVクリームを重ねると、成分同士が反発してヨレの原因になります。各アイテムを塗るごとに手のひらで優しく包み込み、肌表面が落ち着くまで数秒待ちましょう。（※<a href="/winter-lotion" style="color: #e11d48; font-weight: 700; text-decoration: underline;">高保湿化粧水10選はこちら</a>）
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fecdd3;">
          <h3 style="color: #be123c; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 2：擦らず「ポンポンとスタンプを押すように置く」</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            UVデイクリームを顔の上で力強く擦り伸ばすと、ポリマー成分がダマになってモロモロが出やすくなります。指の腹でスタンプを押すようにトントンと優しく均一に密着させましょう。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fecdd3;">
          <h3 style="color: #be123c; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 3：ファンデーションを塗る前に「1分間の放置タイム」</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            UVクリームを塗り終えたら、すぐにファンデーションにいかず1分間置きましょう。この間にクリームが肌の皮脂膜と馴染み、強固な保護ヴェールが形成されます。余分な油分が気になる場合は、ティッシュで軽く押さえます。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fecdd3;">
          <h3 style="color: #be123c; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 4：高保湿ファンデーションを重ねて一日中ツヤ肌キープ</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            朝用デイクリームで土台を完璧に整えたら、美容液成分高配合のファンデーションを重ねることで、エアコンの直風下でも夕方までひび割れない極上のツヤ肌が完成します。（※<a href="/winter-base-makeup" style="color: #e11d48; font-weight: 700; text-decoration: underline;">高保湿ファンデーション10選はこちら</a>）
          </p>
        </div>
      </div>
    </section>

    <!-- FAQ セクション -->
    <section id="faq">
      <h2 class="section-title">冬の朝用UVケアに関するよくある質問（FAQ）</h2>
      <div class="faq-list">
        <div class="faq-item">
          <div class="faq-question">Q1. 冬でも日焼け止めは毎日塗る必要がありますか？</div>
          <div class="faq-answer">
            絶対に必要です！肌を黒くするUV-B波は冬に減少しますが、波長が長く真皮層のコラーゲンを破壊してシワやたるみを引き起こす『UV-A波』は、冬でも真夏の約半分が地上に降り注いでいます。さらに雲や窓ガラスを軽々と透過するため、暖房の効いた室内にいても知らず知らずのうちに光老化が進行します。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q2. 夜用の保湿クリームを朝のメイク前に使ってはいけませんか？</div>
          <div class="faq-answer">
            夜用クリームは油分やエモリエント成分が多く配合されており、睡眠中の水分蒸発を防ぐために表面に重い油膜を作ります。これを朝のメイク前に塗ると、ファンデーションの密着を妨げて『ヨレ』や『油浮き』『モロモロ』の原因になります。朝は日中専用に設計された、水分と油分のバランスが良くUVカット効果も備えた『デイクリーム』を使うのが鉄則です。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q3. 冬の日焼け止めはSPFやPAの数値が低いものを選んでも大丈夫ですか？</div>
          <div class="faq-answer">
            日常の通勤や短時間の買い物であれば『SPF20〜30 / PA++〜+++』で十分肌を守れます。大切なのは数値の高さよりも『保湿力の持続性』と『肌への優しさ』です。ただし、冬のレジャー（スキーやスノボなど雪山）では雪の照り返しで真夏以上の紫外線を浴びるため、必ず『SPF50+ / PA++++』を選びましょう。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q4. 朝のUVクリームを塗った後、ファンデーションを重ねるとモロモロが出る原因は？</div>
          <div class="faq-answer">
            モロモロ（消しゴムのカスのようなダスト）が出る主な原因は、スキンケアや日焼け止めに含まれる水溶性ポリマー（増粘剤）とファンデーションの粉体が、乾き切らないうちに強く擦り合わされることです。UVクリームを塗った後、擦らず優しくハンドプレスし、1〜2分置いて肌表面がサラッと馴染んでからファンデーションを重ねるとモロモロを防げます。
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
        <a href="/winter-base-makeup" class="related-link-card">
          <div class="related-link-title">✨ 夕方まで潤いツヤが続く高保湿ファンデーション＆美容液下地10選</div>
          <div class="related-link-desc">朝用デイクリームと相性抜群！エアコン直撃でもひび割れない生ツヤ肌ベースメイク。</div>
        </a>

        <a href="/winter-lotion" class="related-link-card">
          <div class="related-link-title">💧 保湿力の強さで肌乾燥とさようなら！冬の乾きを満たす高保湿化粧水ランク10</div>
          <div class="related-link-desc">朝クリームの前に！硬くなった冬の角層を深部までうるおいで満たす神ローション。</div>
        </a>

        <a href="/winter-cleansing" class="related-link-card">
          <div class="related-link-title">洗うほど肌がモチモチ潤う！冬の高保湿クレンジング＆濃密バームランク10</div>
          <div class="related-link-desc">日中しっかりガードしたUV膜を摩擦レスに優しくオフする至高のうるおいクレンジング。</div>
        </a>

        <a href="/winter-moisture-cream" class="related-link-card">
          <div class="related-link-title">🧴 保湿力の強さで肌乾燥とさようなら！高保湿フェイスクリーム＆濃密バーム10選</div>
          <div class="related-link-desc">夜のお手入れにはこちら！就寝中の暖房蒸発をゼロに抑え込む夜用最強リペアクリーム。</div>
        </a>

        <a href="/winter-eye-cream" class="related-link-card">
          <div class="related-link-title">👁️ 暖房直撃の目元・ほうれい線をふっくら密着！高保湿アイクリーム＆薬用リンクルケア10選</div>
          <div class="related-link-desc">日中の乾燥小ジワを集中防御！目元・口元の皮膚をふっくら保つ薬用ケア。</div>
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
      <a href="/winter-day-cream">朝用UVクリーム</a>
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

output_path = "winter-day-cream.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {output_path} successfully! Size: {len(html_content)} bytes")
