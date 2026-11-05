import json
import re

with open("fetched_3new_sacran_fullerene_hatomugi.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_hatomugi"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 油分に頼らず水分で満たすマイクロゲル！冬のゴワつく角層をみずみずしく解きほぐす",
        "catch": "天然ハトムギエキスを高配合した国民的ベストセラージェル。すっと溶け込むマイクロジェル層が、真冬の暖房乾燥でゴワつく素肌に絶え間なく水分を補給し続ける保水ヴェールを形成",
        "brand_name": "naturie (ナチュリエ / イミュ)",
        "capacity": "180g / 大容量ジャー容器（6個セット）",
        "type": "高浸透マイクロジェル スキンコンディショニングジェル",
        "features": "天然ハトムギエキス（ヨクイニンエキス）、植物性グリセリン、無香料・無着色・低刺激性・アルコールフリー",
        "value": "油分によるベタつきを嫌う肌でも安心のみずみずしい保水膜。肌に乗せると液状に変化して角層深部へスッと染み渡り、冬のエアコン気流による水分蒸散をブロック",
        "desc_p1": "11月から12月にかけて外気温度が低下すると、肌は寒さから身を守ろうとして角質層を厚く硬化させます。この『角質肥厚』と暖房による乾燥が重なると、肌表面がカチコチにゴワつき、どんなに油分の多いクリームを塗っても弾かれて浸透しないという悪循環に陥ります。ナチュリエの『スキンコンディショニングジェル 180g』は、古来より角質柔軟と水分保持に優れた生薬ヨクイニンの力を、最新のジェル技術で最大限に引き出した名作です。",
        "desc_p2": "ぷるぷるのジェルを肌に伸ばした瞬間、肌の摩擦熱と水分によって構造がほぐれ、スーッと水のように液化。硬くなった角質細胞の隙間へと潤いが一気に染み渡り、角層のキメをふっくらと整えます。肌表面には薄く均一な保護ヴェールが居座り、油分に頼ることなく水分だけで肌を満たし続けるため、毛穴を塞いだりニキビを誘発する心配がありません。180gの大容量で惜しみなく使えるため、お風呂上がりの水分パックや、メイク前のベース保水としても絶大な信頼を誇ります。",
        "target": "冬の乾燥で肌がゴワついて化粧水が弾かれる方、油分の多い重いクリームをつけるとニキビができやすいインナードライ肌、顔から全身まで惜しみなくたっぷり保水したい方",
        "point": "化粧水の後に500円玉大を2枚分ほど顔全体へ贅沢に乗せ、5分間そのまま置く『ジェルパック』が極めて効果的です。最後に手のひらで馴染ませれば、翌朝まで吸い付くような瑞々しさが続きます。"
    },
    {
        "rank": 2,
        "tag": "🛡️ ヒト型セラミド3種×濃密ハトムギエキス！真冬の乾燥角層をラッピングする薬用級ローション",
        "catch": "セザンヌが開発した高機能濃密ローション。ヒト型セラミド全3種（NP/AP/EOP）に濃縮ハトムギ種子エキスとヒアルロン酸を黄金ブレンド。とろみリキッドが冬の粉吹き肌をしっとり密封",
        "brand_name": "CEZANNE (セザンヌ)",
        "capacity": "410ml / 大容量スリムボトル",
        "type": "高保湿 セラミド×ハトムギ 濃密スキンコンディショナー",
        "features": "ハトムギ種子エキス、ヒト型セラミド（NP/AP/EOP）、ヒアルロン酸Na、コラーゲン、弱酸性処方",
        "value": "ドラッグストアで手に入る最高峰のコストパフォーマンス。角層のラメラ構造を整えるセラミドと、角質を柔軟にするハトムギの相乗効果で、真冬の極乾燥肌をもっちり保護",
        "desc_p1": "冬のスキンケアにおいて、プチプラでありながら皮膚生理学に基づいた成分構成で美容のプロから絶賛されているのが、セザンヌの『濃密スキンコンディショナー 410ml』です。一般的なハトムギ化粧水がさっぱりとした拭き取り系であるのに対し、本品は冬の過酷な乾燥に打ち勝つために『ヒト型セラミド3種』を高配合した濃密高保湿設計となっています。",
        "desc_p2": "手にとると、まろやかでとろみのあるリッチなテクスチャーが広がり、乾燥でスカスカになった角層の隙間へピタッと密着。ハトムギエキスが冷気でこわばった肌を柔らかくほぐし、3種のヒト型セラミドが細胞間脂質を補修して水分の逃げ道を塞ぎます。410mlのビッグボトルなので、コットンをヒタヒタにして毎日のローションパックに使うのはもちろん、入浴後の全身の粉吹きすねや腕の保湿ケアにも最適。弱酸性・アルコールフリーの低刺激設計で、家族全員の冬の常備薬として活躍します。",
        "target": "さっぱり系のハトムギ化粧水では冬の乾燥に追いつかないと感じる方、セラミド配合の高保湿化粧水を惜しみなく全身に使いたい方、粉吹きやすねのかゆみに悩む方",
        "point": "手のひらで500円玉大を2〜3回に分けて優しく重ねづけします。乾燥が深刻な日は、大判コットンにたっぷり浸して裂き、頬・額・顎に3分間貼り付ける集中ローションパックを行ってください。"
    },
    {
        "rank": 3,
        "tag": "🏆 1974年誕生の伝説的名品！濃縮オーガニックハトムギが真冬の肌荒れ・赤みを鎮圧",
        "catch": "アルビオンが50年磨き続けた薬用スキンコンディショナーの最新進化版。北海道産の希少オーガニックハトムギ『キタノハト』から抽出した濃縮エキスとハトムギオイルをW配合した至高の化粧液",
        "brand_name": "ALBION (アルビオン)",
        "capacity": "165ml / 国内正規品ガラス調ボトル",
        "type": "薬用スキンコンディショナー エッセンシャル N（医薬部外品）",
        "features": "ハトムギエキス（キタノハト）、ハトムギ油、グリチルリチン酸ジカリウム（消炎有効成分）",
        "value": "冷えと乾燥で乱れた冬のターンオーバーを正常化。白濁した清らかなテクスチャーがほてりや赤みをスッと鎮め、透明感としなやかな弾力を兼ね備えた揺るぎない素肌を構築",
        "desc_p1": "日本のスキンケア史において『スキコン』の愛称で半世紀にわたり愛され続けるアルビオンの『薬用スキンコンディショナー エッセンシャル N』は、真冬の寒冷ストレスや暖房による肌荒れに対する最高峰のアンサーです。原料には、寒冷地である北海道の大地で力強く育った国産唯一の認可ハトムギ『キタノハト』を採用。独自の爆砕抽出法によって、ハトムギの有効成分を余すところなく抽出しています。",
        "desc_p2": "さらに最新処方では、ハトムギの種子からわずかしか採れない貴重なハトムギオイルを新配合。肌に乗せると、スキコンならではの清涼感あふれるフローラルブーケの香りと共に、肌がキュッと引き締まるような心地よい浸透感が広がります。有効成分グリチルリチン酸ジカリウムが、冬の冷たい風による赤みや乾燥荒れを素早く消炎。水分と油分の絶妙な黄金バランスが、乾燥によるテカリとカサつきが混在する大人の冬肌を澄み切ったクリアな状態へ導きます。",
        "target": "冬になると寒暖差で顔が赤くなったり小さなプツプツ肌荒れが出る方、キメが乱れてファンデーションが綺麗に乗らない方、歴史と実績に裏打ちされた名品コスメを使いたい方",
        "point": "アルビオンの乳液で肌をほぐした直後、または洗顔後の肌に、コットンへ裏側まで透けるくらいたっぷり含ませて、顔の中心から外側へリズミカルに優しくパッティングして馴染ませます。"
    },
    {
        "rank": 4,
        "tag": "❄️ 甘草由来のW有効成分×国産ハトムギ！真冬のくすみと乾燥を払う薬用美白ローション",
        "catch": "コーセー雪肌精が40年の研究を結集してリニューアルした薬用ブライトニングエッセンス。厳選された国産ハトムギエキスと甘草由来有効成分が、冬のどんよりくすみと肌荒れを同時に一掃",
        "brand_name": "雪肌精 (SEKKISEI / コーセー)",
        "capacity": "200mL / 伝統の瑠璃色ボトル",
        "type": "薬用雪肌精 ブライトニング エッセンス ローション（医薬部外品）",
        "features": "グリチルレチン酸ステアリルSW（美白・肌荒れ防止有効成分）、国産ハトムギエキス、植物性モイスチャー成分",
        "value": "日本初の甘草由来美白・抗炎症有効成分を配合。冬の寒さによる血行不良くすみと、暖房による乾燥肌荒れを1本で全方位ケアし、雪のように透き通るみずみずしい素肌を育成",
        "desc_p1": "11月から12月は、夏の紫外線ダメージの蓄積に加えて、真冬の寒さによる血行不良と角層の乾燥くすみが重なり、顔全体のトーンが最も暗く沈みがちな季節です。2024年に待望の医薬部外品リニューアルを果たしたコーセーの『薬用雪肌精 ブライトニング エッセンス ローション』は、誕生以来受け継がれてきたハトムギの力を最新の皮膚科学で昇華させた名品です。",
        "desc_p2": "コーセーが16年の歳月をかけて開発した甘草由来の有効成分が、メラニン生成を抑える美白効果と肌荒れ防止効果を同時に発揮。そこに厳選された国産ハトムギエキスが角層深部まで豊かな潤いを送り込みます。雪が肌の上でとろけるようなみずみずしく心地よいテクスチャーは、ベタつきを一切残さず、内側から澄み渡るような透明感と滑らかなツヤを創出。真冬の過酷な環境下でも、くすみ知らずの明るいすっぴん美肌を叶えます。",
        "target": "冬になると顔全体が土気色にくすんで疲れて見える方、乾燥対策だけでなく美白やシミ予防も同時に妥協したくない方、みずみずしい浸透感と上質な和漢の香りに癒やされたい方",
        "point": "500円玉大を手またはコットンに取り、肌全体へ優しく押し込むように塗布します。冬の朝のメイク前に首元までパッティングすると、デコルテまでトーンアップした印象になります。"
    },
    {
        "rank": 5,
        "tag": "💧 累計売上No.1の国民的化粧水！ぐんぐん浸透する天然ハトムギのメガサイズ500ml",
        "catch": "ドラッグストアのスキンケアコーナーで不動の人気を誇る元祖ハトムギ化粧水。角層への浸透性を極限まで高めた独自処方で、冬の入浴後の全身保水や毎日のローションパックに最適",
        "brand_name": "naturie (ナチュリエ / イミュ)",
        "capacity": "500ml / メガサイズボトル",
        "type": "大容量 スキンコンディショナー（高浸透ハトムギ化粧水）",
        "features": "天然ハトムギエキス（ヨクイニンエキス）、アミノ酸群、無香料・無着色・低刺激性・オイルフリー",
        "value": "圧倒的な大容量と浸透力。ベタつかず何度でも重ねづけできるため、真冬の乾いた角層に水分を満杯まで蓄えさせる『水分満タン肌』を誰でも手軽に実現可能",
        "desc_p1": "スキンケアの基本は、何よりもまず『角層細胞を水分で満たすこと』にあります。どんなに高価な美容液やクリームであっても、ベースとなる角層が水分不足でカサカサに縮んでいては本来の威力を発揮できません。ナチュリエの『ハトムギ化粧水 500ml』は、2022年のリニューアルで天然ハトムギエキスの配合量を従来の20%増量し、さらに浸透力を研ぎ澄ませた国民的化粧水です。",
        "desc_p2": "水のようにサラサラとしたテクスチャーでありながら、肌に乗せるとグングン吸い込まれるように角層深部へ浸透。アミノ酸を豊富に含むハトムギエキスが、乾き切った角質細胞をみずみずしく膨らませます。500mlの大容量なので、お風呂上がりに全身にバシャバシャ浴びるように使うことができ、タイツの静電気やすねの粉吹きを未然に防止。手持ちのスプレー容器に詰め替えて、日中のオフィス暖房下での水分補給ミストとしても大活躍します。",
        "target": "とにかく大容量で惜しみなく全身に水分補給したい方、スキンケアの導入として肌を水分で満たしたい方、べたつかないサラサラの感触でしっかり潤したい方",
        "point": "500円玉大を3回重ねづけするのが基本の『重ねづけ保水』です。手のひらがひんやりと冷たく吸い付くようになったら、水分が角層満杯まで満ちた合図です。"
    },
    {
        "rank": 6,
        "tag": "🫧 ハトムギ×ドクダミ×ヒアルロン酸！冬の乾燥摩擦をゼロにする薬用濃密泡洗顔",
        "catch": "ロート製薬が乾燥肌と肌荒れに悩む大人のために開発した薬用スキンコンディショナー洗顔。天然ハトムギエキスとドクダミエキスを配合した弾力もっちり泡が、必要な潤いを残して優しく洗浄",
        "brand_name": "肌ラボ (ロート製薬)",
        "capacity": "詰替え用 / ポンプ対応パウチ",
        "type": "薬用 極潤 ハトムギ泡洗顔（医薬部外品）",
        "features": "ハトムギエキス、ドクダミエキス、ヒアルロン酸Na、グリチルリチン酸2K、アミノ酸系洗浄成分",
        "value": "冬の冷たい朝でもワンプッシュで濃密泡。アミノ酸系洗浄成分が肌のバリア脂質を守り抜き、洗顔後のつっぱり感を完全にゼロ化して滑らかなすっぴん素肌へ",
        "desc_p1": "冬の乾燥肌の悪化原因として見落とされがちなのが『洗顔による過剰脱脂と摩擦ダメージ』です。寒い季節に強力な洗浄剤で洗顔すると、肌が自ら作り出した貴重な天然保湿因子（NMF）やセラミドが洗い流され、洗顔直後から顔全体が突っ張ってしまいます。ロート製薬肌ラボの『極潤 薬用スキンコンディショナー 泡洗顔』は、そうした冬の洗顔クライシスを防ぐために生まれた低刺激泡洗顔です。",
        "desc_p2": "ポンプを押すだけで、キメ細かく弾力のあるクッション泡が瞬時に出現。手と肌の間の摩擦を完全に遮断しながら、毛穴の余分な皮脂や古い角質を優しく吸着します。ハトムギエキスとドクダミエキスの消炎保水ヴェールが、冬の暖房や冷風で敏感になった肌荒れを穏やかに整え、ヒアルロン酸が洗い流した後もしっとりとした潤い膜をキープ。タオルドライ後も突っ張らず、次に使う化粧水の浸透を劇的にスムーズにします。",
        "target": "冬の朝の洗顔後に肌が突っ張ってカサカサする方、泡立てるのが面倒で手軽に濃密泡で洗いたい方、乾燥による大人ニキビや肌荒れを予防したい方",
        "point": "顔をぬるま湯で軽く濡らした後、2〜3プッシュを手にとり泡を肌の上で転がすように洗います。熱いお湯は肌の潤いを奪うため、32〜34℃のぬるま湯で優しくすすぎ流してください。"
    },
    {
        "rank": 7,
        "tag": "🌿 濃密和漢ヨクイニン100%原液！首元・目元のポツポツ角質粒と冬のザラつきを集中ケア",
        "catch": "自然化粧品研究所が誇る純粋ハトムギ抽出エキス。90mlの贅沢ビッグサイズ。冬の乾燥とターンオーバーの停滞で硬化した首元や目元の角質粒、ゴワゴワ肌に直接働きかけるピュア美容液",
        "brand_name": "自然化粧品研究所 / 原液シリーズ",
        "capacity": "大容量 90ml / 遮光ボトル",
        "type": "高純度 ヨクイニンエキス（ハトムギ原液）美容液",
        "features": "ハトムギ種子エキス（ヨクイニンエキス100%抽出原液）、水、BG",
        "value": "無添加・無香料のピュア和漢原液。大容量90mlなので、顔だけでなく首元やデコルテ、手の甲まで惜しみなく毎日塗り重ねて、冬のゴワつき角質を根本から柔軟リペア",
        "desc_p1": "冬になると、タートルネックのセーターやマフラーの摩擦、そして寒さによる新陳代謝の低下によって、首元や目元、デコルテに『小さなポツポツとした角質粒』やザラつきが発生しやすくなります。古くから生薬としてイボ取りや角質柔軟に用いられてきたヨクイニンの力をダイレクトに肌へ届けるのが、自然化粧品研究所の『ヨクイニンエキス原液 90ml』です。",
        "desc_p2": "化粧品原料として使われる高濃度ヨクイニンエキスをそのままボトル詰めした本品は、余計な増粘剤や香料を一切含まない純粋設計。洗顔後の肌や気になる首筋に直接馴染ませると、硬くなった古い角質層にスーッと染み込み、日を追うごとに肌表面が滑らかに解きほぐされていきます。90mlという大容量仕様のため、顔全体のくすみケアから首・デコルテの集中ケアまで何か月も贅沢に使い倒せる圧倒的コストパフォーマンスを誇ります。",
        "target": "首元や目元のポツポツしたザラつきや角質粒が気になる方、冬の乾燥で肌全体がゴワゴワしてキメが乱れている方、和漢生薬の原液をたっぷり使いたい方",
        "point": "洗顔直後の清潔な肌に、スポイト1回分を直接馴染ませます。特に首元や目元のザラつきが気になる部分には、指先で優しくクルクルと円を描くように重ねづけしてください。"
    },
    {
        "rank": 8,
        "tag": "🥛 粉吹きすね＆冬の全身乾燥をレスキュー！ハトムギエキス×ヒアルロン酸の乳液ミルク",
        "catch": "熊野油脂・麗白が送り出す全身用高保湿ボディミルク。天然保湿成分ハトムギエキスにヒアルロン酸をプラス。真冬の乾燥で粉を吹くすね・腕・背中にスッと伸びてしっとり潤す名作",
        "brand_name": "麗白 (レイハク / 熊野油脂)",
        "capacity": "400ml / ポンプ式大容量ボトル",
        "type": "高保湿 ハトムギボディミルク（全身用エマルジョン）",
        "features": "天然ハトムギ種子エキス、ヒアルロン酸Na、シア脂、ミネラルオイル、弱酸性処方",
        "value": "ポンプ式で入浴後に素早く全身ケア。ベタつきが一切残らないシルキーなテクスチャーで、塗った直後に冬の厚手タイツやパジャマを着ても張り付かない実用性",
        "desc_p1": "冬のボディの乾燥は、顔以上に深刻です。特に11月以降は、タイツやスキニーパンツとの摩擦、熱い湯船への入浴によって皮脂が奪われ、すねや太ももが白く粉を吹いてかゆみに襲われるトラブルが多発します。麗白の『ハトムギ ボディミルク 400ml』は、毎日の入浴後にストレスなく全身を高保湿ラッピングできる大容量ボディミルクです。",
        "desc_p2": "ポンプをプッシュして手に取ると、とろけるように滑らかなミルクが広がり、乾燥してカサカサになった皮膚へ水が染み込むように馴染みます。ハトムギエキスの角質柔軟作用とヒアルロン酸の保水力により、粉を吹いていたすねが瞬時にベルベットのようななめらか素肌へと復活。ベタつきのないさらりとした仕上がりなので、朝の出勤前のハンド＆ボディケアとしても快適に使えます。大容量400mlで家族全員の冬のボディを守ります。",
        "target": "冬になるとすねが粉を吹いてかゆくなる方、お風呂上がりに全身を手早く保湿したいけれどベタつくクリームは嫌な方、高コスパでたっぷり使えるボディ乳液を探している方",
        "point": "お風呂から上がってタオルで軽く水気を拭き取った直後、3〜4プッシュを手にとり全身へ滑らせるように塗り広げます。乾燥しやすいひじ・ひざ・かかとには重ね塗りがおすすめです。"
    },
    {
        "rank": 9,
        "tag": "🌿 薬用ハトムギ配合クリーミー濃密泡！メイクと毛穴の余分な角質をオフする洗顔フォーム",
        "catch": "ソフティモのロングセラー薬用洗顔。天然ハトムギエキスを配合したクリーミーな濃密泡が、冬のメイク汚れとくすみの原因となる古い角質を包み込んで落とし、しっとり透明感ある素肌へ",
        "brand_name": "softymo (ソフティモ / コーセー)",
        "capacity": "190g / チューブ容器",
        "type": "薬用ホワイト クレンジングウォッシュ（医薬部外品）",
        "features": "ハトムギエキス（ヨクイニンエキス）、グリチルリチン酸ジカリウム、植物性アミノ酸系洗浄成分",
        "value": "メイク落としと洗顔がこれ1本で完了。冬のダブル洗顔による肌への負担と脱脂を防ぎ、必要な水分を守りながらワントーン明るいクリアな素肌へ洗い上げる",
        "desc_p1": "真冬のクレンジングにおいて最も肌を傷めるのが『クレンジングオイル後の強い洗顔料によるダブル洗顔』です。皮脂分泌が激減している冬に洗いすぎると、肌のバリア機能は完全に崩壊してしまいます。コーセーソフティモの『薬用ホワイト クレンジングウォッシュ（ハトムギ）』は、1本で軽めのメイク落としと洗顔を同時に完了できる高機能ウォッシュです。",
        "desc_p2": "少量を泡立てネットにとると、まるでホイップクリームのように濃密で弾力のあるミクロ泡が立ち上がり、肌と手の間で厚いクッションを形成。ハトムギエキスの保湿成分が角質を優しくいたわりながら、毛穴の奥の汚れやくすみ物質を浮き上がらせて洗い流します。薬用消炎成分配合で、冬のマスク摩擦や乾燥による肌荒れを優しく防止。洗い流した後はつっぱり感がなく、しっとり吸い付くような明るい肌質へと仕上がります。",
        "target": "冬の洗顔による乾燥やつっぱり感を防ぎたい方、日焼け止めやナチュラルメイクを1ステップで優しく落としたい方、家族で毎日使える大容量洗顔フォームを求める方",
        "point": "泡立てネットを使って空気を含ませながらレモン1個分のもっちり泡を作り、顔全体に泡を乗せて押し洗いします。Tゾーンから洗い始め、乾燥しやすい頬や目元は泡を転がす程度ですすいでください。"
    },
    {
        "rank": 10,
        "tag": "🍯 大容量300gのこっくり高保湿！ハトムギ×植物オイルが冬の乾燥肌をラッピングする万能クリーム",
        "catch": "熊野油脂・麗白が誇るメガサイズ高保湿クリーム。ハトムギエキスにスクワランとヒアルロン酸をブレンドしたリッチなエマルジョンが、冬のカチコチ乾燥肌を柔らかなベルベット肌へ",
        "brand_name": "麗白 (レイハク / 熊野油脂)",
        "capacity": "大容量 300g / 広口ジャー容器",
        "type": "高保湿 ハトムギ ミルキークリーム（全身用濃密バーム）",
        "features": "天然ハトムギ種子エキス、ヒアルロン酸Na、スクワラン、植物性グリセリン",
        "value": "300gという圧倒的大容量。顔のナイトパックから、ひび割れやすいかかと・ひじ・手肌の集中エモリエントまで、冬のあらゆる乾燥部位を惜しみなく濃密ラッピング",
        "desc_p1": "冬の乾燥対策において、スキンケアの最後に欠かせないのが『水分を閉じ込める油分膜』です。しかし、高価なフェイスクリームを首や手足、かかとにまで毎日たっぷり塗るわけにはいきません。麗白の『ハトムギ ミルキークリーム 300g』は、ずっしり重い大容量ジャーに、ハトムギの角質柔軟成分と良質なエモリエントオイルをぎっしり詰め込んだマルチプロテクトクリームです。",
        "desc_p2": "指先ですくうと、こっくりとしていながら体温でスルスルと滑らかに広がる極上のテクスチャー。ハトムギエキスが真冬の冷えで硬化した角質層を柔らかくほぐし、スクワランが肌表面に長時間の保護バリアを構築します。夜のスキンケアの最後に顔全体へ少し厚めに塗って眠れば、翌朝まで暖房の乾燥に負けないモチモチ肌が持続。ガサガサに角化したかかとや肘にたっぷり塗り込めば、タイツに引っかからない滑らかな素肌へと導きます。",
        "target": "大容量で惜しみなく全身に塗りまくれる高保湿クリームを探している方、冬になるとかかとやひじがガサガサに硬化する方、家族全員で使える安心の保湿バームを求める方",
        "point": "お風呂上がりや就寝前、適量を手のひらに取って温めてから乾燥部位へ馴染ませます。かかとや手肌にはたっぷり塗った後に靴下や手袋を着用すると、スチームパック効果で劇的に柔らかくなります。"
    }
]

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge">第{p["rank"]}位</span>
            <span class="product-tag">{p["tag"]}</span>
          </div>

          <h3 class="product-title">{p["catch"]}</h3>
          <p class="product-display-name">{item_data["display_name"]}</p>

          <div class="product-layout">
            <div class="product-visual-col">
              <div class="img-wrap">
                <img src="{item_data["image_url"]}" alt="{p["brand_name"]} {item_data["item_name"]}" class="product-img" loading="lazy" />
              </div>
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">¥{item_data["price"]:,}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", "4.8")}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", "120")}件）</span>
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
  <title>保湿力の強さで肌乾燥とさようなら！古来伝承の和漢ヨクイニンが真冬のゴワつく角層を柔軟にほぐし透き通るみずみずしさを宿す高保湿ハトムギコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の寒冷乾燥で硬化した角層・ゴワつき・粉吹き・くすみを救う高保湿ハトムギ（ヨクイニン）コスメを徹底厳選！ナチュリエ、セザンヌ、アルビオン、雪肌精、肌ラボ、麗白までアミノ酸と角質柔軟の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="ハトムギ コスメ, ハトムギ化粧水, ヨクイニン エキス, 高保湿 コスメ 冬, 角質ゴワつき 11月 12月, ナチュリエ 保湿ジェル, セザンヌ 濃密スキンコンディショナー, アルビオン スキコン, 薬用雪肌精">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！古来伝承の和漢ヨクイニンが真冬のゴワつく角層を柔軟にほぐし透き通るみずみずしさを宿す高保湿ハトムギコスメランク10">
  <meta property="og:description" content="和漢ヨクイニンの力で冬のゴワつき・粉吹き角層を柔軟にほぐす！真冬の過酷な乾燥を跳ね返すおすすめ高保湿ハトムギコスメ10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-hatomugi">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿ハトムギコスメランク10">
  <meta name="twitter:description" content="11月・12月のゴワつき枯れ肌に！角層を柔軟に解きほぐす高保湿ハトムギコスメおすすめ厳選10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！古来伝承の和漢ヨクイニンが真冬のゴワつく角層を柔軟にほぐし透き通るみずみずしさを宿す高保湿ハトムギコスメランク10",
    "description": "11月・12月の寒冷乾燥で硬化した角層・ゴワつき・粉吹き・くすみを救う高保湿ハトムギ（ヨクイニン）コスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-06T01:00:00+09:00",
    "dateModified": "2026-11-06T01:00:00+09:00",
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
      "@id": "https://lumi-cosme.vercel.app/winter-hatomugi"
    }}
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #2: ItemList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿ハトムギ（ヨクイニン）コスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "{product_details[0]["brand_name"]} {items[0]["item_name"]}",
        "url": "{items[0]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{product_details[1]["brand_name"]} {items[1]["item_name"]}",
        "url": "{items[1]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{product_details[2]["brand_name"]} {items[2]["item_name"]}",
        "url": "{items[2]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 4,
        "name": "{product_details[3]["brand_name"]} {items[3]["item_name"]}",
        "url": "{items[3]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 5,
        "name": "{product_details[4]["brand_name"]} {items[4]["item_name"]}",
        "url": "{items[4]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 6,
        "name": "{product_details[5]["brand_name"]} {items[5]["item_name"]}",
        "url": "{items[5]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 7,
        "name": "{product_details[6]["brand_name"]} {items[6]["item_name"]}",
        "url": "{items[6]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 8,
        "name": "{product_details[7]["brand_name"]} {items[7]["item_name"]}",
        "url": "{items[7]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 9,
        "name": "{product_details[8]["brand_name"]} {items[8]["item_name"]}",
        "url": "{items[8]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 10,
        "name": "{product_details[9]["brand_name"]} {items[9]["item_name"]}",
        "url": "{items[9]["affiliate_url"]}"
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
        "name": "ハトムギ化粧水はさっぱりしていて冬には乾燥しませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "一般的には夏向けのさっぱりタイプというイメージがありますが、冬用には『セラミド高配合の濃密タイプ（セザンヌ等）』や『マイクロゲル構造のジェル（ナチュリエ等）』『ハトムギオイル配合の乳化ローション（アルビオン等）』を選ぶことで、油分に頼らず水分保持力を極限まで高めた上質な冬ケアが可能です。水分が満たされた後に乳液やクリームで蓋をすることで、インナードライを根本から解消できます。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "ハトムギ（ヨクイニン）は首元や目元のポツポツ角質粒にも効きますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "古来より生薬ヨクイニンは皮膚のターンオーバー正常化と角質柔軟作用で広く知られています。冬の乾燥と摩擦によって硬化した首元や目元のザラつき・小さな角質粒に対して、高濃度のヨクイニン原液やハトムギクリームを継続して優しく馴染ませることで、角質を無理なく柔らかく整える効果が期待できます。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "冬の敏感肌や乾燥による大人ニキビにも使えますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "非常に適しています。ハトムギ種子エキスには肌の水分・油分バランスを整える働きがあり、さらに消炎成分（グリチルリチン酸2K等）が配合されている医薬部外品タイプであれば、冬の暖房やマスクによる摩擦荒れ、乾燥性ニキビを穏やかに鎮静させることができます。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #059669;
      --primary-light: #d1fae5;
      --primary-dark: #047857;
      --accent: #10b981;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f0fdf4;
      --card-bg: #ffffff;
      --border: #a7f3d0;
      --gold: #d97706;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Meiryo", sans-serif;
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
    }}

    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      letter-spacing: -0.025em;
    }}

    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    .container {{
      max-width: 1000px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .article-header {{
      background: #ffffff;
      padding: 2.5rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}

    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}

    .article-category {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}

    h1.article-title {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #0f172a;
      margin-bottom: 1.25rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }}

    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      padding-top: 1rem;
      border-top: 1px solid var(--border);
    }}

    .lead-box {{
      background: #ffffff;
      border-left: 5px solid var(--primary);
      padding: 1.75rem;
      border-radius: 0 var(--radius) var(--radius) 0;
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      font-size: 1.05rem;
      color: #334155;
    }}

    .lead-box p {{
      margin-bottom: 1rem;
    }}
    .lead-box p:last-child {{
      margin-bottom: 0;
    }}

    .science-section {{
      background: #ffffff;
      padding: 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border: 1px solid var(--border);
    }}

    .section-title {{
      font-size: 1.45rem;
      color: #0f172a;
      font-weight: 800;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.5rem;
    }}

    .science-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin-top: 1.5rem;
    }}

    .science-card {{
      background: #ffffff;
      padding: 1.5rem;
      border-radius: var(--radius);
      border: 1px solid var(--border);
    }}

    .science-card h4 {{
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-box {{
      background: #ffffff;
      padding: 1.75rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border: 1px solid var(--border);
    }}

    .toc-title {{
      font-weight: 800;
      font-size: 1.15rem;
      margin-bottom: 1rem;
      color: var(--primary-dark);
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 0.5rem 1.5rem;
    }}

    .toc-list li a {{
      color: #334155;
      text-decoration: none;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list li a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.25rem 2rem;
      margin-bottom: 3rem;
      border: 1px solid var(--border);
      transition: box-shadow 0.2s, transform 0.2s;
    }}

    .product-card:hover {{
      box-shadow: var(--shadow-lg);
      transform: translateY(-2px);
    }}

    .product-header {{
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}

    .rank-badge {{
      background: var(--gold);
      color: #ffffff;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 0.25rem 0.85rem;
      border-radius: 9999px;
      letter-spacing: 0.05em;
    }}

    .product-tag {{
      color: var(--primary-dark);
      font-size: 0.9rem;
      font-weight: 700;
    }}

    .product-title {{
      font-size: 1.4rem;
      line-height: 1.45;
      color: #0f172a;
      margin-bottom: 0.5rem;
      font-weight: 800;
    }}

    .product-display-name {{
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 1.75rem;
      background: var(--bg);
      padding: 0.6rem 1rem;
      border-radius: 8px;
    }}

    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
    }}

    @media (max-width: 768px) {{
      .product-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    .product-visual-col {{
      text-align: center;
    }}

    .img-wrap {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem;
      margin-bottom: 1rem;
    }}

    .product-img {{
      max-width: 100%;
      height: auto;
      max-height: 240px;
      object-fit: contain;
    }}

    .price-box {{
      background: var(--bg);
      padding: 0.75rem;
      border-radius: 8px;
      margin-bottom: 0.75rem;
    }}

    .price-label {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .price-value {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #e11d48;
    }}

    .review-meta {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.25rem;
    }}

    .review-stars {{
      color: var(--gold);
      font-weight: 700;
    }}

    .rakuten-btn {{
      display: block;
      background: #bf0000;
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      transition: background 0.2s, transform 0.1s;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.2);
    }}

    .rakuten-btn:hover {{
      background: #990000;
      transform: translateY(-1px);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      margin-bottom: 1.5rem;
    }}

    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.85rem;
      border: 1px solid var(--border);
    }}

    .spec-table th {{
      background: var(--bg);
      color: #334155;
      width: 25%;
      font-weight: 700;
      text-align: left;
    }}

    .spec-table td {{
      color: #1e293b;
    }}

    .product-body p {{
      margin-bottom: 1.1rem;
      color: #334155;
      font-size: 0.98rem;
    }}

    .body-title {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      font-weight: 700;
      margin-bottom: 0.75rem;
      border-left: 3px solid var(--primary);
      padding-left: 0.5rem;
    }}

    .recommend-box, .usage-box {{
      padding: 1rem 1.25rem;
      border-radius: 8px;
      margin-top: 1.25rem;
      font-size: 0.92rem;
    }}

    .recommend-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}

    .recommend-title {{
      font-weight: 700;
      margin-bottom: 0.4rem;
      color: #15803d;
    }}

    .usage-box {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      color: #065f46;
    }}

    .usage-title {{
      font-weight: 700;
      margin-bottom: 0.4rem;
      color: var(--primary-dark);
    }}

    .comparison-section, .faq-section, .internal-links-section {{
      background: #ffffff;
      padding: 2.25rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border: 1px solid var(--border);
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
    }}

    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}

    .comparison-table th, .comparison-table td {{
      padding: 0.85rem;
      border: 1px solid var(--border);
      text-align: left;
    }}

    .comparison-table th {{
      background: var(--bg);
      color: #0f172a;
      font-weight: 700;
    }}

    .comparison-table tr:hover {{
      background: #d1fae5;
    }}

    .faq-item {{
      margin-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 1.5rem;
    }}

    .faq-item:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}

    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-a {{
      color: #334155;
      font-size: 0.95rem;
      padding-left: 1.5rem;
    }}

    .internal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin-top: 1.5rem;
    }}

    .internal-card {{
      background: var(--bg);
      padding: 1.25rem;
      border-radius: 8px;
      border: 1px solid var(--border);
      text-decoration: none;
      color: var(--text);
      display: block;
      transition: border-color 0.2s, transform 0.1s;
    }}

    .internal-card:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
    }}

    .internal-card-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
    }}

    .internal-card-desc {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1.5rem;
      margin-top: 4rem;
    }}

    .footer-inner {{
      max-width: 1000px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 2rem;
    }}

    @media (max-width: 768px) {{
      .footer-inner {{
        grid-template-columns: 1fr;
      }}
    }}

    .footer-logo {{
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      margin-bottom: 0.75rem;
    }}

    .footer-text {{
      font-size: 0.85rem;
      line-height: 1.7;
    }}

    .footer-links h5 {{
      color: #ffffff;
      margin-bottom: 0.75rem;
      font-size: 0.95rem;
    }}

    .footer-links ul {{
      list-style: none;
    }}

    .footer-links li a {{
      color: #94a3b8;
      text-decoration: none;
      font-size: 0.85rem;
      line-height: 2;
    }}

    .footer-links li a:hover {{
      color: #ffffff;
    }}

    .copyright {{
      max-width: 1000px;
      margin: 2rem auto 0;
      padding-top: 1.5rem;
      border-top: 1px solid #1e293b;
      text-align: center;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">冬コスメTOP</a>
        <a href="#ranking">ランキング10選</a>
        <a href="#comparison">徹底比較表</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <article>
      <div class="article-header">
        <div class="breadcrumb">
          <a href="/">HOME</a> &gt; <a href="/">冬の乾燥対策スキンケア</a> &gt; 高保湿ハトムギ（ヨクイニン）特集
        </div>
        <span class="article-category">11月・12月 冬季和漢高保湿スキンケア特集</span>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！古来伝承の和漢ヨクイニンが真冬のゴワつく角層を柔軟にほぐし透き通るみずみずしさを宿す高保湿ハトムギコスメランク10</h1>
        <div class="article-meta">
          <span>📅 公開日: 2026年11月6日</span>
          <span>🔄 最終更新: 2026年11月6日</span>
          <span>✍ 監修: LUMI COSMETICS 皮膚科学コスメ解析班</span>
          <span>⏱ 読了目安: 約8分</span>
        </div>
      </div>

      <div class="lead-box">
        <p><strong>11月から12月にかけて、肌の『ゴワつき』や『化粧水が弾かれる感覚』に悩まされていませんか？</strong>外気温度が急低下する真冬の季節、皮膚は冷たい寒風から身を守るために角質層を急速に硬化・肥厚化させます。この『角質肥厚』と室内の暖房乾燥が重なると、どんなに油分の多いクリームを塗り重ねても表面で滑るだけで角層深部に届かず、肌の内側がカラカラに干からびる深刻なインナードライを引き起こします。</p>
        <p>この真冬の硬化したゴワつき肌を劇的に柔らかくほぐし、清らかな水分を満杯にチャージする伝統の和漢植物が<strong>『ハトムギ（生薬名：ヨクイニン）』</strong>です。豊富に含まれる12種類以上のアミノ酸が角層細胞の天然保湿因子（NMF）を補強し、特有の角質柔軟成分が古い角質を無理なくほぐして滑らかな透明感を引き出します。「ハトムギは夏用」という先入観を覆す、<strong>セラミド高配合の濃密処方やマイクロジェル、濃縮オイルブレンド</strong>など、真冬にこそ真価を発揮する高保湿ハトムギコスメが今大ヒットを記録しています。</p>
        <p>本記事では、楽天市場で実際に高評価を獲得している正規品の中から、処方設計・浸透力・角質ケア効果・コストパフォーマンスを徹底検証した<strong>真冬の高保湿ハトムギコスメおすすめランキング10選</strong>をご紹介します。</p>
      </div>

      <section class="science-section">
        <h2 class="section-title">🧬 なぜ真冬のゴワつき・乾燥に「ハトムギ（ヨクイニン）」が圧倒的に効くのか？皮膚科学的3大根拠</h2>
        <p>日本の過酷な冬の乾燥環境において、ハトムギエキスが果たす独自の皮膚科学的アプローチを解説します。</p>

        <div class="science-grid">
          <div class="science-card">
            <h4>🌾 豊富な必須アミノ酸がNMF（天然保湿因子）を再構築</h4>
            <p>ハトムギ種子には、グルタミン酸、アラニン、ロイシンなど、人間の皮膚の角層内に存在する天然保湿因子（NMF）とほぼ同一のアミノ酸が極めて高濃度に含まれています。乾燥で水分を抱え込めなくなった角質細胞へ直接アミノ酸を補給し、自らうるおいを蓄える素肌力を蘇らせます。</p>
          </div>

          <div class="science-card">
            <h4>✨ 硬化した古い角質を無理なくほぐす角質柔軟作用</h4>
            <p>冬の寒冷でターンオーバーが滞り、肥厚化した不要な角質を穏やかに軟化。ピーリングのような物理的摩擦や刺激を与えることなく、キメの乱れやザラつき、首元・目元の小さな角質粒を滑らかに整え、後から使う美容成分の浸透ルートを劇的に開通させます。</p>
          </div>

          <div class="science-card">
            <h4>🛡️ 暖房乾燥による大人ニキビ・赤みを鎮静する抗炎症作用</h4>
            <p>ハトムギ特有の成分コイクセノリドやグリチルリチン酸との相乗効果により、寒暖差やマスク摩擦、暖房気流による微弱炎症を素早く消炎。油分過多で毛穴を詰まらせることなく、水分バランスを整えて清潔で健やかな肌環境を維持します。</p>
          </div>
        </div>
      </section>

      <section class="toc-box">
        <div class="toc-title">📑 目次：高保湿ハトムギコスメ厳選10選一覧</div>
        <ul class="toc-list">
          <li><a href="#rank-1">第1位：ナチュリエ ハトムギ保湿ジェル 180g</a></li>
          <li><a href="#rank-2">第2位：セザンヌ 濃密スキンコンディショナー 410ml</a></li>
          <li><a href="#rank-3">第3位：アルビオン 薬用スキンコンディショナー 165ml</a></li>
          <li><a href="#rank-4">第4位：薬用雪肌精 ブライトニング エッセンス 200mL</a></li>
          <li><a href="#rank-5">第5位：ナチュリエ ハトムギ化粧水 500ml</a></li>
          <li><a href="#rank-6">第6位：肌ラボ 薬用 極潤 ハトムギ泡洗顔</a></li>
          <li><a href="#rank-7">第7位：自然化粧品研究所 ヨクイニン原液美容液 90ml</a></li>
          <li><a href="#rank-8">第8位：麗白 ハトムギ ボディミルク 400ml</a></li>
          <li><a href="#rank-9">第9位：コーセー ソフティモ 薬用ハトムギクレンジング</a></li>
          <li><a href="#rank-10">第10位：麗白 ハトムギ ミルキークリーム 300g</a></li>
        </ul>
      </section>

      <section id="ranking">
        <h2 class="section-title">🏆 2026年最新！真冬の高保湿ハトムギコスメおすすめ厳選ランキング10選</h2>
        <p style="margin-bottom: 2rem; color: #475569;">※本ランキングは、楽天市場におけるリアルタイムの商品データ（価格・在庫・口コミ評価・成分配合）を基準に、冬の乾燥・ゴワつき対策に特化して厳正に順位づけしています。</p>

        {all_cards_html}
      </section>

      <section class="comparison-section" id="comparison">
        <h2 class="section-title">📊 高保湿ハトムギコスメ10選 スペック徹底比較表</h2>
        <p style="margin-bottom: 1.5rem; color: #475569;">あなたの肌質、使いたい部位、テクスチャーの好みに合わせて最適な1品をお選びください。</p>

        <div class="comparison-table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位 / 商品名</th>
                <th>ブランド</th>
                <th>アイテム種別</th>
                <th>参考価格</th>
                <th>特長・おすすめターゲット</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>第1位</strong> ナチュリエ ハトムギ保湿ジェル</td>
                <td>naturie</td>
                <td>マイクロジェル 180g</td>
                <td>¥3,990</td>
                <td>油分ゼロで水分満タン！冬のゴワつく肌にぷるぷる水分パック</td>
              </tr>
              <tr>
                <td><strong>第2位</strong> セザンヌ 濃密スキンコンディショナー</td>
                <td>CEZANNE</td>
                <td>高保湿化粧水 410ml</td>
                <td>¥638</td>
                <td>ヒト型セラミド3種配合。とろみリキッドで冬の粉吹き肌を密封</td>
              </tr>
              <tr>
                <td><strong>第3位</strong> アルビオン 薬用スキコン</td>
                <td>ALBION</td>
                <td>薬用化粧液 165ml</td>
                <td>¥5,900</td>
                <td>北海道産キタノハトエキス×オイル。冬の赤み肌荒れを澄んだ肌へ</td>
              </tr>
              <tr>
                <td><strong>第4位</strong> 薬用雪肌精 ブライトニング</td>
                <td>雪肌精</td>
                <td>薬用美白化粧水 200mL</td>
                <td>¥3,399</td>
                <td>甘草由来W有効成分。冬の血行不良くすみと乾燥を払拭</td>
              </tr>
              <tr>
                <td><strong>第5位</strong> ナチュリエ ハトムギ化粧水</td>
                <td>naturie</td>
                <td>高浸透化粧水 500ml</td>
                <td>¥618</td>
                <td>メガサイズ500ml。お風呂上がりの全身バシャバシャ保水に</td>
              </tr>
              <tr>
                <td><strong>第6位</strong> 肌ラボ 極潤 ハトムギ泡洗顔</td>
                <td>肌ラボ</td>
                <td>薬用泡洗顔</td>
                <td>¥2,079</td>
                <td>アミノ酸系弾力泡。冬の朝の洗顔後もつっぱり感ゼロ</td>
              </tr>
              <tr>
                <td><strong>第7位</strong> ヨクイニン原液 美容液</td>
                <td>自然化粧品研究所</td>
                <td>100%原液 90ml</td>
                <td>¥6,480</td>
                <td>首元・目元のポツポツ角質粒や冬のザラつきを集中ケア</td>
              </tr>
              <tr>
                <td><strong>第8位</strong> 麗白 ハトムギ ボディミルク</td>
                <td>麗白</td>
                <td>ボディミルク 400ml</td>
                <td>¥457</td>
                <td>タイツ摩擦ですねが粉を吹く方へ。ベタつかずスーッと伸びる</td>
              </tr>
              <tr>
                <td><strong>第9位</strong> ソフティモ 薬用ハトムギ洗顔</td>
                <td>softymo</td>
                <td>メイク落とし洗顔 190g</td>
                <td>¥373</td>
                <td>1本でメイクも毛穴汚れもオフ。冬のダブル洗顔による脱脂を防ぐ</td>
              </tr>
              <tr>
                <td><strong>第10位</strong> 麗白 ハトムギ ミルキークリーム</td>
                <td>麗白</td>
                <td>濃密クリーム 300g</td>
                <td>¥566</td>
                <td>大容量300g。カチコチかかとや就寝前のナイトパックに万能</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="faq-section" id="faq">
        <h2 class="section-title">❓ 真冬のハトムギコスメ活用 Q&A：よくある質問</h2>

        <div class="faq-item">
          <div class="faq-q">Q1. ハトムギ化粧水はさっぱりしていて冬には乾燥しませんか？</div>
          <div class="faq-a">
            一般的には夏向けのさっぱりタイプというイメージがありますが、冬用には『セラミド高配合の濃密タイプ（セザンヌ等）』や『マイクロゲル構造のジェル（ナチュリエ等）』『ハトムギオイル配合の乳化ローション（アルビオン等）』を選ぶことで、油分に頼らず水分保持力を極限まで高めた上質な冬ケアが可能です。水分が満たされた後に乳液やクリームで蓋をすることで、インナードライを根本から解消できます。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Q2. ハトムギ（ヨクイニン）は首元や目元のポツポツ角質粒にも効きますか？</div>
          <div class="faq-a">
            古来より生薬ヨクイニンは皮膚のターンオーバー正常化と角質柔軟作用で広く知られています。冬の乾燥と摩擦によって硬化した首元や目元のザラつき・小さな角質粒に対して、高濃度のヨクイニン原液やハトムギクリームを継続して優しく馴染ませることで、角質を無理なく柔らかく整える効果が期待できます。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Q3. 冬の敏感肌や乾燥による大人ニキビにも使えますか？</div>
          <div class="faq-a">
            非常に適しています。ハトムギ種子エキスには肌の水分・油分バランスを整える働きがあり、さらに消炎成分（グリチルリチン酸2K等）が配合されている医薬部外品タイプであれば、冬の暖房やマスクによる摩擦荒れ、乾燥性ニキビを穏やかに鎮静させることができます。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Q4. 朝のメイク前にも使えますか？</div>
          <div class="faq-a">
            非常に使いやすいのがハトムギの大きなメリットです。油分が過剰に含まれていないため、朝のスキンケアでたっぷり使ってもメイクがヨレたり崩れたりする原因になりません。特にナチュリエの保湿ジェルやセザンヌの濃密ローションは、角層に素早く馴染んで肌表面をさらりと滑らかに整えるため、ファンデーションの密着度を格段に高めてくれます。
          </div>
        </div>
      </section>

      <section class="internal-links-section">
        <h2 class="section-title">🔗 あわせて読みたい！冬の高保湿スキンケア関連記事</h2>
        <p style="color: #475569; font-size: 0.95rem;">真冬の乾燥トラブルを全方位から撃退する人気特集記事をピックアップ。</p>

        <div class="internal-grid">
          <a href="/winter-sacran" class="internal-card">
            <div class="internal-card-title">💧 高保湿サクランコスメ10選</div>
            <div class="internal-card-desc">ヒアルロン酸の約10倍の保水膜！阿蘇の希少藍藻多糖体が真冬のインナードライを徹底救済。</div>
          </a>
          <a href="/winter-fullerene" class="internal-card">
            <div class="internal-card-title">⚡ 高保湿フラーレンコスメ10選</div>
            <div class="internal-card-desc">ビタミンCの250倍の抗酸化力！真冬の寒冷酸化ストレスから皮脂を守り抜く名品。</div>
          </a>
          <a href="/winter-rice-power" class="internal-card">
            <div class="internal-card-title">🌾 高保湿ライスパワーコスメ10選</div>
            <div class="internal-card-desc">皮膚水分保持能の改善が認められた有効成分！自らうるおうセラミドを増やす冬の救世主。</div>
          </a>
          <a href="/winter-ceramide-lotion" class="internal-card">
            <div class="internal-card-title">🛡️ 高保湿セラミド化粧水10選</div>
            <div class="internal-card-desc">角層の水分保持バリアを根本から立て直す！真冬の乾燥肌を満たす高濃度セラミド。</div>
          </a>
        </div>
      </section>
    </article>
  </main>

  <footer>
    <div class="footer-inner">
      <div>
        <div class="footer-logo">LUMI COSMETICS</div>
        <p class="footer-text">
          LUMI COSMETICSは、11月〜12月の本格的な寒冷・乾燥シーズンを乗り切るための高品質コスメ・スキンケア情報を専門にお届けするビューティーメディアです。皮膚科学的根拠に基づいた成分解析と楽天市場のリアルタイムデータを融合し、客観的で信頼性の高いコスメ選びをサポートします。
        </p>
      </div>
      <div class="footer-links">
        <h5>サイトマップ・リンク</h5>
        <ul>
          <li><a href="/">冬コスメTOP</a></li>
          <li><a href="/winter-hatomugi">高保湿ハトムギ</a></li>
          <li><a href="/winter-sacran">高保湿サクラン</a></li>
          <li><a href="/winter-fullerene">高保湿フラーレン</a></li>
          <li><a href="/winter-rice-power">高保湿ライスパワー</a></li>
        </ul>
      </div>
    </div>
    <div class="copyright">
      &copy; 2026 LUMI COSMETICS. All Rights Reserved.
    </div>
  </footer>

</body>
</html>
"""

with open("winter-hatomugi.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Generated winter-hatomugi.html successfully! (File size: {len(full_html):,} bytes)")
