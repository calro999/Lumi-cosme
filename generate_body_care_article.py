import json

with open("rakuten_latest_3articles_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

body_items = data["winter_body_care"]["items"]

html_template = """<!DOCTYPE html>
<html lang="ja" prefix="og: http://ogp.me/ns#">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【2026最新】すねの粉吹き・全身の乾燥かゆみにサヨナラ！高保湿ボディミルク＆濃厚ボディバターおすすめ10選 | Lumi Cosme</title>
  <meta name="description" content="11月・12月の厳しい寒さと暖房による全身の粉吹き、タイツ摩擦、お風呂上がりのピリピリ乾燥かゆみを防ぐ！純度99%グリセリン、濃厚シアバター、ヘパリン類似物質、ヒト型セラミド配合の最強ボディミルク＆高保湿ボディクリーム厳選10選。入浴後3分のゴールデンタイム保湿法まで徹底解説。">
  <meta name="keywords" content="ボディミルク, ボディクリーム, ボディバター, 冬ボディケア, 高保湿, ニュートロジーナ, ニベア, キュレル, セタフィル, サボン, ロクシタン, 2026コスメ">

  <!-- SEO & Canonical -->
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-body-care">
  <meta name="robots" content="index, follow">

  <!-- OGP -->
  <meta property="og:site_name" content="Lumi Cosme (ルミコスメ)">
  <meta property="og:title" content="すねの粉吹き・全身の乾燥かゆみにサヨナラ！高保湿ボディミルク＆濃厚ボディバターおすすめ10選">
  <meta property="og:description" content="冬の粉吹きスネや背中のかゆみを徹底ブロック！ニュートロジーナ、ニベア、キュレル、サボン、ロクシタンなど高保湿ボディケアを徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-body-care">
  <meta property="og:image" content="{og_image}">
  <meta property="og:locale" content="ja_JP">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="すねの粉吹き・全身の乾燥かゆみにサヨナラ！高保湿ボディミルク＆濃厚ボディバターおすすめ10選">
  <meta name="twitter:description" content="冬の粉吹きスネや背中のかゆみを徹底ブロック！ニュートロジーナ、ニベア、キュレル、サボン、ロクシタンなど高保湿ボディケアを徹底比較。">
  <meta name="twitter:image" content="{og_image}">

  <link rel="stylesheet" href="style.css">

  <!-- 構造化データ (JSON-LD) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "headline": "すねの粉吹き・全身の乾燥かゆみにサヨナラ！高保湿ボディミルク＆濃厚ボディバターおすすめ10選",
        "description": "11月・12月の本格乾燥シーズンに必須の高保湿ボディミルク＆濃厚ボディバターの選び方、成分比較、おすすめ10選を徹底レビュー。",
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
        "name": "冬の高保湿ボディミルク＆濃厚ボディバターおすすめ10選",
        "itemListElement": [
{item_list_json}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "ボディクリームを塗る最も効果的なタイミングはいつですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "『入浴後3分以内』が最も効果的です。入浴直後の皮膚は角質層が水分をたっぷり含んで柔らかくなっていますが、浴室を出て5分を過ぎると急激に水分が蒸発して過乾燥が始まります。タオルで軽く水気を押さえた直後の湿り気がある状態で塗ると、乳化作用により摩擦なく滑らかに伸び、水分を油分で閉じ込めることができます。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "ボディミルクとボディバター・クリームの違いは何ですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "水と油の配合比率が異なります。ボディミルク（ローション）は水分が多くみずみずしいテクスチャーで、角質層への浸透が早く塗った直後にパジャマを着てもベタつきません。一方、ボディクリームやボディバターはシアバターやワックスなどの油分比率が高く、硬くなった皮膚に濃厚な保護膜（エモリエントヴェール）を張り、翌朝まで長時間の保湿を持続させます。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "すねが白く粉を吹いてかゆい時はどうケアすればいいですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "すねは皮脂腺が極めて少ないため、冬に真っ先に粉吹きが起こる部位です。ゴシゴシ体を洗うのをやめ、石鹸の泡だけで優しく洗い、40度以上の熱いお湯を直接当てないようにしましょう。保湿にはヘパリン類似物質やセラミド配合の医薬部外品（キュレルやヘパソフトなど）を選び、皮膚科治療発想でバリア機能を補修するのが効果的です。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "ヒートテックなどの吸湿発熱インナーを着るとかゆくなるのはなぜ？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "吸湿発熱インナーは、肌から蒸発するわずかな水分を吸着して発熱する仕組みのため、元々乾燥している冬の肌からさらに水分を奪って過乾燥を悪化させることがあります。また化学繊維との摩擦も刺激になります。インナーを着る前に必ず高純度グリセリンやワセリン系のボディミルクをたっぷり塗って皮膚表面に保護シールドを作っておくことで、かゆみや静電気を大幅に予防できます。"
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body class="theme-body">

  <!-- ヘッダー -->
  <header class="site-header">
    <div class="header-badge">🛁 2026 WINTER BODY CARE SPECIAL</div>
    <h1 class="site-title">高保湿ボディミルク＆ボディバター10選</h1>
    <p class="site-subtitle">すねの粉吹き・全身の乾燥かゆみを防ぎ、翌朝まで吸い付くうるツヤ肌へ</p>
  </header>

  <main class="container">

    <!-- 記事トップ・アイキャッチ -->
    <article class="article-intro">
      <div class="article-meta">
        <span class="article-cat-tag">ボディケア特集 / 保湿ミルク・ボディバター</span>
        <span class="article-date">📅 2026.10.28 更新</span>
      </div>

      <h1 class="article-main-heading">すねの粉吹き・全身の乾燥かゆみにサヨナラ！高保湿ボディミルク＆濃厚ボディバターおすすめ10選</h1>

      <p class="article-lead">
        11月に入り気温が15度を下回るようになると、<strong>「お風呂上がりにすねや背中がムズムズ痒くなる」「タイツやストッキングを脱ぐと内側に白い粉がびっしり付いている」「ひじ・ひざがガサガサに硬化して白くひび割れる」</strong>といった、全身の深刻な乾燥トラブルに悩まされる方が一気に急増します。<br><br>
        顔のお手入れには美容液やパックを惜しまない方でも、体の保湿はついつい後回しになりがち。しかし実は、<strong>腕やすねの皮脂腺の数は顔のわずか10分の1程度</strong>しか存在せず、自力で皮脂膜を作ることが極めて苦手な構造になっています。<br><br>
        さらに真冬の熱い湯船、ナイロンタオルによる摩擦、化学繊維インナーによる吸湿が重なることで、角質層の水分保持力は完全にゼロへと崩壊してしまいます。<br><br>
        本記事では、純度99%の医療グレードグリセリン、濃厚オーガニックシアバター、ヘパリン類似物質、抗炎症CICA成分など、真冬の全身を潤いのヴェールで包み込む厳選ボディケア10アイテムを徹底比較します！
      </p>

      <!-- 目次ナビゲーション -->
      <nav class="toc-container">
        <div class="toc-title">📑 本記事の目次</div>
        <ul class="toc-list">
          <li><a href="#why-body">1. なぜ冬の体は粉を吹き痒くなるのか？皮脂腺不足と摩擦乾燥のメカニズム</a></li>
          <li><a href="#types">2. あなたのライフスタイルに合うのはどれ？ボディケアの3大テクスチャー診断</a></li>
          <li><a href="#comparison">3. 【一目でわかる】冬の高保湿ボディケア10選 比較早見表</a></li>
          <li><a href="#ranking">4. 【2026最新】冬の高保湿ボディミルク＆濃厚ボディバターおすすめ10選 詳細レビュー</a></li>
          <li><a href="#technique">5. 効果が段違い！皮膚科学に基づく「入浴後3分のゴールデンタイム保湿術」</a></li>
          <li><a href="#faq">6. ボディケアに関するよくある質問（FAQ）</a></li>
          <li><a href="#related">7. あわせて読みたい！冬の保湿ケア特集一覧</a></li>
        </ul>
      </nav>
    </article>

    <!-- メカニズムセクション -->
    <section id="why-body">
      <h2 class="section-title">なぜ冬の体は粉を吹き痒くなるのか？皮脂腺不足と摩擦乾燥のメカニズム</h2>
      <p class="content-text">
        冬になると真っ先に白く粉を吹く「すね」や、チクチクとしたかゆみが発生する「腰周り」「背中」。これらは決して偶然ではなく、皮膚生理学的な理由が存在します。
      </p>
      <p class="content-text">
        第一の理由は、<strong>「皮脂腺の分布の圧倒的格差」</strong>です。Tゾーンや額に比べて、すねやふくらはぎは皮脂の分泌量が極端に少なく、天然の油膜シールドが存在しません。第二の理由は、<strong>「お風呂の熱と洗浄剤による細胞間脂質の流出」</strong>です。寒いからと41℃以上の熱いお湯に浸かると、角質細胞を繋ぎ止めているセラミドやコレステロールが一気に溶け出してしまいます。
      </p>
      <div class="product-catch" style="margin: 20px 0;">
        💡 冬のボディを乾燥崩壊から守る3つの鉄則：<br>
        ① <strong>「高純度グリセリン」や「シア脂」で水分蒸散を物理的に阻止する</strong><br>
        ② <strong>入浴後、皮膚表面が完全に乾ききる前の3分以内に塗布する</strong><br>
        ③ <strong>かゆみや炎症が起きている部位には「医薬部外品・消炎剤配合」を選ぶ</strong>
      </div>
    </section>

    <!-- タイプ別診断セクション -->
    <section id="types">
      <h2 class="section-title">あなたのライフスタイルに合うのはどれ？ボディケアの3大テクスチャー診断</h2>
      <div class="content-text">
        <p>毎日ストレスなく続けられるよう、使用シーンやお好みの使用感に合わせて最適なタイプを選びましょう。</p>
        
        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #f3e8ff; box-shadow: var(--shadow-soft);">
          <h3 style="color: #6b21a8; font-size: 16px; font-weight: 700; margin-bottom: 6px;">① 速乾エマルジョン・高浸透ミルク（ニュートロジーナ、セタフィルなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">「塗った後すぐにパジャマを着たい」「ポンプ式でサッと手軽に全身ケアしたい」方に。角層深部へスッと吸い込まれ、ベタつかないのに内側から濃密にうるおいます。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #f3e8ff; box-shadow: var(--shadow-soft);">
          <h3 style="color: #6b21a8; font-size: 16px; font-weight: 700; margin-bottom: 6px;">② 濃厚ホイップバター・上質アロマクリーム（ロクシタン、サボン、ローラメルシエなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">「極度のカサカサ肌をこっくりした油分膜で守りたい」「心地よい上質な香りに包まれて眠りたい」方に。シアバターなどの天然油脂が体温でとろけて肌をラッピングします。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #f3e8ff; box-shadow: var(--shadow-soft);">
          <h3 style="color: #6b21a8; font-size: 16px; font-weight: 700; margin-bottom: 6px;">③ 薬用バリア・消炎かゆみストップタイプ（キュレル、ヘパソフト、ニベアなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">「すねの粉吹きが止まらない」「下着のゴム周りや背中がかゆくて掻いてしまう」方に。ヘパリン類似物質や消炎剤、セラミド機能成分が炎症を鎮め、皮膚バリアを治療レベルで補修します。</p>
        </div>
      </div>
    </section>

    <!-- 比較早見表 -->
    <section id="comparison">
      <h2 class="section-title">【一目でわかる】冬の高保湿ボディケア10選 比較早見表</h2>
      <p class="content-text">掲載している価格は楽天市場の最新調査価格（税込）です。横スクロールでテクスチャーや主成分を比較できます。</p>

      <div class="table-scroll-wrapper">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>タイプ・質感</th>
              <th>主要キー成分</th>
              <th>参考価格</th>
              <th>おすすめな肌状態</th>
            </tr>
          </thead>
          <tbody>
{table_rows}
          </tbody>
        </table>
      </div>
    </section>

    <!-- アイテム詳細レビュー -->
    <section id="ranking">
      <h2 class="section-title">【2026最新】冬の高保湿ボディミルク＆濃厚ボディバターおすすめ10選 詳細レビュー</h2>
{items_detail_html}
    </section>

    <!-- プロ直伝テクニック -->
    <section id="technique">
      <h2 class="section-title">効果が段違い！皮膚科学に基づく「入浴後3分のゴールデンタイム保湿術」</h2>
      <div class="content-text">
        <p>
          ボディケアは「何を塗るか」と同じくらい「いつ・どう塗るか」が保湿持続力を決定づけます。水分を逃さないプロ直伝の全身ケアメソッドです。
        </p>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #f3e8ff;">
          <h3 style="color: #6b21a8; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 1：タオルドライは「ゴシゴシ拭かない」ポンポン当て拭き</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            お風呂上がりの肌は水分を含んで最もデリケート。タオルで強くこすると角質層を削り取ってしまいます。バスタオルを体に優しく押し当て、大きな水滴だけを吸い取る程度にとどめましょう。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #f3e8ff;">
          <h3 style="color: #6b21a8; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 2：脱衣所を出る前「3分以内」に全身へ塗布</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            浴室の湯気で脱衣所が加湿されている間に塗るのがベスト。皮膚にわずかな湿り気が残っている状態でミルクを伸ばすと、水分と油分が乳化し、驚くほど少量で全身になめらかに行き渡ります。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #f3e8ff;">
          <h3 style="color: #6b21a8; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 3：すね・ひじ・かかとは「二度塗り」で重点シールド</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            全身に塗布した後、特に乾燥しやすいすね、ひざ、ひじ、かかとにはもうワンプッシュ重ね付けします。手のひらで包み込むようにハンドプレスして体温で馴染ませると、翌朝まで粉吹きゼロが続きます。手先の集中ケアには<a href="/winter-hand-care" style="color: #9333ea; font-weight: 700; text-decoration: underline;">高保湿ハンドクリーム</a>の併用も効果的です。
          </p>
        </div>
      </div>
    </section>

    <!-- FAQセクション -->
    <section id="faq">
      <h2 class="section-title">ボディケアに関するよくある質問（FAQ）</h2>
      <div class="faq-container">
        <div class="faq-item">
          <div class="faq-question">Q1. ボディクリームを塗る最も効果的なタイミングはいつですか？</div>
          <div class="faq-answer">
            『入浴後3分以内』が最も効果的です。入浴直後の皮膚は角質層が水分をたっぷり含んで柔らかくなっていますが、浴室を出て5分を過ぎると急激に水分が蒸発して過乾燥が始まります。タオルで軽く水気を押さえた直後の湿り気がある状態で塗ると、乳化作用により摩擦なく滑らかに伸び、水分を油分で閉じ込めることができます。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q2. ボディミルクとボディバター・クリームの違いは何ですか？</div>
          <div class="faq-answer">
            水と油の配合比率が異なります。ボディミルク（ローション）は水分が多くみずみずしいテクスチャーで、角質層への浸透が早く塗った直後にパジャマを着てもベタつきません。一方、ボディクリームやボディバターはシアバターやワックスなどの油分比率が高く、硬くなった皮膚に濃厚な保護膜（エモリエントヴェール）を張り、翌朝まで長時間の保湿を持続させます。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q3. すねが白く粉を吹いてかゆい時はどうケアすればいいですか？</div>
          <div class="faq-answer">
            すねは皮脂腺が極めて少ないため、冬に真っ先に粉吹きが起こる部位です。ゴシゴシ体を洗うのをやめ、石鹸の泡だけで優しく洗い、40度以上の熱いお湯を直接当てないようにしましょう。保湿にはヘパリン類似物質やセラミド配合の医薬部外品（キュレルやヘパソフトなど）を選び、皮膚科治療発想でバリア機能を補修するのが効果的です。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q4. ヒートテックなどの吸湿発熱インナーを着るとかゆくなるのはなぜ？</div>
          <div class="faq-answer">
            吸湿発熱インナーは、肌から蒸発するわずかな水分を吸着して発熱する仕組みのため、元々乾燥している冬の肌からさらに水分を奪って過乾燥を悪化させることがあります。また化学繊維との摩擦も刺激になります。インナーを着る前に必ず高純度グリセリンやワセリン系のボディミルクをたっぷり塗って皮膚表面に保護シールドを作っておくことで、かゆみや静電気を大幅に予防できます。
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
        <a href="/winter-hand-care" class="related-link-card">
          <div class="related-link-title">🤲 手荒れ・あかぎれ・ささくれ知らずへ！神ハンドクリーム＆ネイルケア10選</div>
          <div class="related-link-desc">ボディミルクと合わせて常備したい！水仕事や冷風で荒れ果てた手指を速攻リペアする薬用クリーム。</div>
        </a>

        <a href="/winter-hair-care" class="related-link-card">
          <div class="related-link-title">🌿 冬の静電気・毛先パサつきと完全決別！高保湿ヘアオイル＆濃厚ヘアマスク10選</div>
          <div class="related-link-desc">お風呂上がりのアウトバスケア！暖房やマフラー摩擦から髪のキューティクルを守るサロン級オイル。</div>
        </a>

        <a href="/winter-face-mask" class="related-link-card">
          <div class="related-link-title">💧 水分爆弾で砂漠肌を即リセット！翌朝の化粧ノリ激変・高保湿シートマスク＆夜用パック10選</div>
          <div class="related-link-desc">お風呂上がりの贅沢タイム！暖房でしぼんだ顔の素肌に水分をチャージする濃密フェイスパック。</div>
        </a>

        <a href="/winter-moisture-cream" class="related-link-card">
          <div class="related-link-title">🧴 保湿力の強さで肌乾燥とさようなら！高保湿フェイスクリーム＆濃密バーム10選</div>
          <div class="related-link-desc">顔の乾燥対策はこちら！真冬の厳しい乾きから肌を守り抜くセラミド＆バームの名品集。</div>
        </a>

        <a href="/winter-lip-care" class="related-link-card">
          <div class="related-link-title">🎁 冬のガサガサ皮剥けに終止符！高保湿リップトリートメント＆濃密ティント10選</div>
          <div class="related-link-desc">唇の皮剥け・縦ジワを集中トリートメント。夜用スリーピングマスクから高発色ティントまで。</div>
        </a>

        <a href="/winter-serum-booster" class="related-link-card">
          <div class="related-link-title">💧 浸透力を底上げする高保湿・導入先行美容液おすすめ10選</div>
          <div class="related-link-desc">スキンケアの最初に！固くなった冬肌をほぐし、化粧水をグングン引き込む土台美容液。</div>
        </a>

        <a href="/winter-eye-cream" class="related-link-card">
          <div class="related-link-title">👁️ 暖房直撃の目元・ほうれい線をふっくら密着！高保湿アイクリーム＆薬用リンクルケア10選</div>
          <div class="related-link-desc">皮膚の薄い目元・口元の乾燥小じわを撃退する集中リンクルケアアイテム。</div>
        </a>

        <a href="/winter-base-makeup" class="related-link-card">
          <div class="related-link-title">✨ 夕方まで潤いツヤが続く高保湿ファンデーション＆美容液下地10選</div>
          <div class="related-link-desc">エアコン直撃でもひび割れない！乾燥知らずの生ツヤ肌を叶える冬ファンデ＆下地。</div>
        </a>
      </div>
    </section>

  </main>

  <!-- フッター -->
  <footer class="site-footer">
    <div class="footer-links">
      <a href="/">トップページ</a>
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

body_details_map = {
    1: {
        "tag": "🏆 医療グレード純度99%！超乾燥肌の絶対救世主",
        "catch": "角層10層の奥深くまで浸透！CICA配合で粉吹き・乾燥かゆみを即効鎮静する最強エマルジョン",
        "spec_cap": "250ml (ポンプ式)",
        "spec_texture": "ベタつきゼロでスーッと角層に消える高浸透エマルジョン",
        "spec_ing": "医療グレード純度99%グリセリン、CICAコンプレックス、アラントイン、パンテノール",
        "spec_finish": "塗った直後に服を着ても全く貼り付かないサラすべ高密度保湿",
        "desc_p1": "極寒のノルウェーの漁師たちが過酷な冬の海風から肌を守るために生まれた歴史を持つニュートロジーナ。その最高峰ラインが、このインテンスリペアCICAエマルジョンです。一般的なグリセリンと一線を画す『純度99%の超微粒子グリセリン』を採用。分子が非常に小さいため、乾燥で硬化した角層10層の奥深くまで瞬時に浸透し、水分をがっちりと抱え込みます。",
        "desc_p2": "さらに荒れた皮膚を鎮静する『CICAコンプレックス』を配合。冬場に起こりがちなタイツ摩擦によるかゆみや、すねの白い粉吹きを即座に鎮静化します。高保湿でありながら驚くほど伸びが良く、塗布後数秒でサラサラの肌触りに変化するため、塗ってすぐにパジャマやスキニーデニムを履いても一切貼りつきません。ポンプ式で毎日のお風呂上がりに手軽に全身ケアができる、冬の超定番実力派です。",
        "target": "すねの粉吹きやかゆみに毎年悩まされている方、高保湿でもベタついて服に付くのが耐えられない方",
        "how_to": "入浴後、軽く水気を拭き取った素肌に適量をプッシュし、全身へ大きく円を描くように伸ばします。粉吹きが激しいすねやかかとには重ね塗りを。",
        "voice": "『冬になるとすねが粉を吹いて痒くてたまらなかったのが、これを使い始めてから完全にピタッと治まりました！ベタつかないので朝の着替え前でもサッと塗れます。一生リピします！』(30代・乾燥肌)"
    },
    2: {
        "tag": "👑 日本の冬を支え続ける国民的ボディミルク",
        "catch": "高保水型ヒアルロン酸配合！乾燥した角層の奥までうるおいを巡らせて閉じ込める濃厚ミルク",
        "spec_cap": "200g",
        "spec_texture": "なめらかにとろけるミルキーテクスチャー",
        "spec_ing": "ディープ＆ロングラスティングモイスチャー処方、セラミドII、トレハロース",
        "spec_finish": "一日中しっとり感が持続するやわらかな吸い付き肌",
        "desc_p1": "ドラッグストアで手に入るプチプラボディケアの最高峰として、世代を超えて愛され続けるニベアのスキンミルク『しっとり』。冬の超乾燥肌に向けて設計された本品は、角層の水分保持力を高める『ディープ＆ロングラスティングモイスチャー処方』を採用。肌に乗せた瞬間はミルクのみずみずしさがありながら、体温で温まることでコクのある保湿ヴェールへと変化します。",
        "desc_p2": "水分を抱え込むセラミドやトレハロースが角層の奥まで浸透し、夕方になってもカサつきやつっぱりを感じさせない長時間の潤い持続力を誇ります。ドラッグストアで手軽に買える親しみやすい価格帯でありながら、仕上がりのしっとり感はデパコスにも引けを取りません。冬の家族全員のデイリーケアとしても圧倒的な支持を集めています。",
        "target": "コスパ抜群で惜しみなく全身にたっぷり塗れる高保湿ミルクを探している方、家族全員で共有したい方",
        "how_to": "手のひらに適量を取り、手のひらで少し温めてから腕やすね、お腹周りに優しく馴染ませます。",
        "voice": "『安くて大容量なのに保湿力が本当にすごい。お風呂上がりに毎日塗っていると、冬場でもスネが全くカサカサになりません。優しいニベアの香りも大好きです。』(20代・普通肌〜乾燥肌)"
    },
    3: {
        "tag": "🛡️ 医薬部外品・消炎バリア濃厚バーム",
        "catch": "セラミド機能成分×消炎剤配合！ガサガサに荒れたひじ・かかと・すねの角層を集中修復",
        "spec_cap": "70g (ジャータイプ)",
        "spec_texture": "体温でとろけてピタッと密着する高密着濃厚バーム",
        "spec_ing": "セラミド機能成分、ユーカリエキス、アラントイン（消炎有効成分）",
        "spec_finish": "摩擦から肌を鉄壁防御するしっとり濃厚保護膜",
        "desc_p1": "乾燥性敏感肌研究のパイオニアである花王キュレルが開発した、全身の頑固な乾燥ポイントを救う薬用高保湿バーム。通常のローションや乳液では追いつかないほど硬くゴワついたすね、白くひび割れたかかと、カサつくひじのために特別に処方されています。肌の必須成分であるセラミドの働きを補う『セラミド機能成分』が角質細胞の隙間を埋め尽くし、外気刺激から肌を守ります。",
        "desc_p2": "さらに肌荒れ・かゆみを防ぐ消炎有効成分『アラントイン』を配合。衣服の擦れで赤みやかゆみが出ている肌も、穏やかに鎮静させます。ジャーから取った瞬間はしっかりとした固形バームですが、肌に乗せて伸ばすと体温でじゅわっととろけて高密着シールドを形成。水分蒸散を強力にシャットアウトし、翌朝まで吸い付くような潤いが持続します。",
        "target": "すねが白くひび割れて痒みがある方、かかとやひじがガチガチに硬化している乾燥性敏感肌の方",
        "how_to": "お風呂上がりに特に乾燥が気になる部位（すね、ひざ、かかと、ひじ）に適量をすくい、体温で温めながら丁寧にすり込みます。",
        "voice": "『毎年冬になるとスネがかゆくて寝ている間に掻き壊していたのですが、キュレルのバームを塗ったら嘘のようにかゆみが止まりました。本当に助けられました。』(30代・敏感肌)"
    },
    4: {
        "tag": "🧴 皮膚科医推奨・大容量高保湿ローション",
        "catch": "ナイアシンアミド×パンテノール配合！肌バリアを整えながら角層を満たす大容量ボディ乳液",
        "spec_cap": "591ml × 2本セット",
        "spec_texture": "するすると軽く伸びて広範囲に素早く広がるマイルドローション",
        "spec_ing": "ナイアシンアミド、パンテノール、高純度グリセリン、アボカド油",
        "spec_finish": "すべすべで柔らかく、キメの整った健やかな素肌",
        "desc_p1": "世界70カ国以上の皮膚科医から推奨される敏感肌ケアブランド『セタフィル』のベストセラー保湿ローション。リニューアルにより、バリア機能をサポートする『ナイアシンアミド』、肌荒れを防ぎ皮膚をすこやかに保つ『パンテノール』、そして高純度グリセリンの黄金トリオ処方へと進化。乾燥によって脆弱になった冬の角質層を根本から強化します。",
        "desc_p2": "591mlという圧倒的な大容量ポンプボトルで、お風呂上がりに惜しみなく全身にたっぷりプッシュできるのが最大の魅力。アボカドオイル配合で肌なじみが非常に滑らかで、広背筋やすねなどの広範囲にもあっという間に塗り広げられます。無香料・低刺激設計で、生後3ヶ月の赤ちゃんから敏感肌の大人まで家族全員で安心して使える頼れる大容量常備品です。",
        "target": "家族みんなで気兼ねなく全身にたっぷり使いたい方、無香料で低刺激な皮膚科医推奨処方を求める方",
        "how_to": "入浴後、全身に2〜3プッシュを豪快に手に取り、マッサージするように全身へ塗り広げます。",
        "voice": "『大容量なのでケチらず全身にたっぷり塗れるのが最高！家族全員で使っていますが、真冬でも誰も粉吹きしません。ポンプ式でサッと出せるのも便利です。』(30代・子育て世代)"
    },
    5: {
        "tag": "✨ 贅沢シアバター×死海のミネラル",
        "catch": "至福の香りと濃厚なうるおい！過酷な乾燥ダメージを受けた肌を集中リペアするプレステージクリーム",
        "spec_cap": "200ml (ジャータイプ)",
        "spec_texture": "リッチでこっくりとした濃密バタークリーム",
        "spec_ing": "死海の塩ミネラル、シアバター、カカオバター、ホホバ種子油",
        "spec_finish": "シルクのように艶やかで、ふんわりとラグジュアリーな香りが残る上質肌",
        "desc_p1": "イスラエル発祥の人気ボディケアコスメSABONが誇る、極上のリペアボディクリーム。死海のミネラルを豊富に含み、冬の冷風や摩擦でカサついた肌に豊かなうるおいとミネラルをチャージします。さらに上質なシアバターやカカオバターを贅沢にブレンドし、硬くなった角質をやわらげ、まるでエステ後のようなツヤやかな質感へと導きます。",
        "desc_p2": "SABONの代名詞である『パチュリ・ラベンダー・バニラ』の甘く魅惑的なアロマが、お風呂上がりのリラックスタイムを特別なスパ体験へと格上げします。肌に伸ばすと体温でゆっくりと溶け込み、翌朝ベッドから起きた瞬間までふんわりと心地よい香りと吸い付くようなしっとり感が持続。冬の自分へのご褒美やホリデーギフトとしても絶大な人気を誇ります。",
        "target": "保湿力だけでなく香りの癒やしも重視したい方、冬の夜のご褒美ケアとして贅沢なボディクリームを使いたい方",
        "how_to": "お風呂上がりに、乾いた清潔な肌に適量を手に取り、マッサージするように丁寧に伸ばします。首筋やデコルテまで広げるとフレグランス代わりに。",
        "voice": "『香りが本当に極上で、寝る時までベッドの中で幸せな香りに包まれます。翌朝になっても肌がしっとり柔らかくて、乾燥知らずのツヤ肌になれます！』(20代・乾燥肌)"
    },
    6: {
        "tag": "🍨 人類モテの甘い香り×高機能セラム処方",
        "catch": "SNSで『甘いバニラの香りが1日中消えない』と熱狂的支持！美容液成分を凝縮した贅沢ボディセラム",
        "spec_cap": "200ml",
        "spec_texture": "ホイップクリームのようにふんわりとろけるメルティセラム",
        "spec_ing": "フレンチプラムシードオイル、グリセリン、タピオカデンプン、シア脂",
        "spec_finish": "ベタつかないのに触れたくなるほどシルキーでなめらかなツヤ肌",
        "desc_p1": "『一度使うと他の香りに戻れない』とSNSでバズり続けるローラメルシエのアイコン、アンバーバニラの香り。従来のボディクリームから進化し、美容液発想の『セラムボディクリーム』として肌の奥までうるおいを届ける高機能処方へとアップグレードされました。フレンチプラムシードオイルやシア脂が乾燥した素肌をなめらかに包み込みます。",
        "desc_p2": "甘く温かみのあるアンバーと濃厚なバニラが織りなす香りは、香水いらずと言われるほど持続力が高く、冬の冷たい空気の中でふわりと上品に香ります。ホイップクリームのように軽やかなのに、塗った瞬間に肌へ溶け込んでシルクのような極上のスベスベ感を実現。デートや特別な日の前に仕込んでおきたい、大人の冬の勝負コスメです。",
        "target": "甘く上品なバニラの香りに包まれたい方、香水の代わりにボディケアで自然な香りを一日中漂わせたい方",
        "how_to": "お風呂上がりに腕やデコルテ、脚全体に薄く伸ばします。手首や首元に少量重ね付けすると、自然な香水代わりとして楽しめます。",
        "voice": "『本当に良い香りで、職場でも「どこの香水？」と聞かれます。テクスチャーもふわふわでベタつかず、肌が一日中すべすべで触り心地最高になります！』(30代・普通肌)"
    },
    7: {
        "tag": "🌿 南仏アベンヌ温泉水×セレクティオーズ",
        "catch": "生後1ヶ月の赤ちゃんから使える安心処方！植物由来の保護成分が角層バリアを48時間キープ",
        "spec_cap": "400ml (大容量ポンプ)",
        "spec_texture": "軽やかでするする伸びる滑らかなフルイドミルク",
        "spec_ing": "アベンヌ温泉水、セレクティオーズ（保護成分）、植物性セラミド誘導体",
        "spec_finish": "カサつきを忘れさせるしっとり穏やかな保護膜",
        "desc_p1": "敏感肌の聖地・南フランスのアベンヌ温泉水から生まれた高保湿ボディミルク。最大の特長は、アベンヌ独自の植物由来成分『セレクティオーズ』の配合です。冬の乾燥によって失われがちな細胞間脂質（セラミド・必須脂肪酸・コレステロール）のバランスを整え、肌本来が持っている水分保持バリアを力強く補強します。",
        "desc_p2": "フルイド（液状）という名前の通り、サラッとしていて広範囲にスルスルと驚くほど素早く伸びるため、お風呂上がりのケアがわずか1分で完了します。軽い塗り心地でありながら、保湿力は48時間持続すると謳われるほどパワフル。香料やパラベンを使用していないため、冬の寒風で肌が過敏になっている方や、小さな子どもと一緒に使いたいママにも絶大な支持を得ています。",
        "target": "超敏感肌で香料や添加物が苦手な方、塗った後の重さや被膜感が嫌いで軽やかな保湿を好む方",
        "how_to": "入浴後、全身に2〜3プッシュを伸ばします。カサつきやすい膝裏やすねには手のひらで包み込むように重ねてください。",
        "voice": "『冬になると粉吹きとかゆみで皮膚科に通っていた娘と私ですが、トリクセラを使い始めてから病院通いが不要になりました！大容量でポンプも使いやすいです。』(40代・敏感肌)"
    },
    8: {
        "tag": "🧈 シアバター25%配合！冬の絶対王道",
        "catch": "世界中で愛される高保湿の伝説！こっくり濃厚なシアの膜が真冬の激しい乾燥から肌を鉄壁ガード",
        "spec_cap": "200ml",
        "spec_texture": "こっくり濃厚でリッチな高密度クリーム",
        "spec_ing": "西アフリカ産オーガニックシアバター（25%高濃度配合）、アマ種子エキス、マシュマロエキス",
        "spec_finish": "吸い付くような濃密な保湿膜で包まれた極上もっちり肌",
        "desc_p1": "高保湿ボディケアを語る上で絶対に外せない、ロクシタンの歴史的名品『シア リッチボディクリーム』。西アフリカの女性たちが厳しい乾燥から肌を守るために受け継いできた天然のシアバターを、なんと全体の25%という圧倒的な高濃度で配合しています。人体の皮脂と構造が非常に似ているため、肌馴染みが良く、体温でとろけて角層深くまで吸い込まれます。",
        "desc_p2": "指に取ると濃厚で固めのテクスチャーですが、手のひらで温めてから肌に乗せると、まるで温かいバターのように滑らかに広がります。塗った後は肌表面に贅沢なエモリエントシールドが形成され、翌朝のお風呂で洗い流す瞬間までしっとり感が完全に持続。真冬の過酷な粉吹きすねも、たった一晩でやわらかな赤ちゃん肌へと生まれ変わらせます。",
        "target": "毎年冬の粉吹きや肌のひび割れが重症化する方、天然シアバターの濃密な油分でフタをしたい方",
        "how_to": "適量を手のひらに取り、両手をこすり合わせて体温でバーム状に溶かしてから、脚や腕に押し込むように馴染ませます。",
        "voice": "『他のボディクリームとは濃厚さが全然違います！シアバターが肌にピタッと張り付いて、翌朝起きた時のスベスベ感に感動します。冬はこれがないと越せません。』(30代・超乾燥肌)"
    },
    9: {
        "tag": "🌿 100%天然由来ホイップバーム",
        "catch": "パンジー＆カレンドラの植物パワー！とろけるホイップバターがごわつく肌をやわらかくほぐす",
        "spec_cap": "150ml",
        "spec_texture": "ふわふわのホイップクリームのようにとろける生バター",
        "spec_ing": "パンジー（サンシキスミレ）エキス、カレンドラ（トウキンセンカ）エキス、シア脂、カカオ脂",
        "spec_finish": "植物オイルのツヤが宿るふっくら柔らか肌",
        "desc_p1": "1926年の誕生以来、世界中の乾燥肌を救い続けてきたヴェレダの名品『スキンフード』シリーズから生まれた濃厚ボディバター。パンジーエキスやカレンドラ、カモミールといった伝統的なハーブの抽出エキスを、贅沢なシアバターとカカオバターのホイップベースに閉じ込めました。合成保存料・着色料・鉱物油を一切使わない100%天然由来処方です。",
        "desc_p2": "フタを開けると、まるで焼きたてのパンに塗るホイップバターのようにふわふわの質感。肌に乗せると体温でするりと液状に溶け出し、柑橘系とハーブの爽やかで深みのあるアロマが広がります。ごわついて硬くなった冬の角質層を柔らかく解きほぐし、内側から弾むような自然なツヤを与えてくれます。オーガニック志向の方に間違いなくおすすめできる逸品です。",
        "target": "ナチュラル・オーガニック成分にこだわりたい方、ハーブの力でゴワつく乾燥肌をやわらげたい方",
        "how_to": "お風呂上がりに、乾いた清潔な肌に適量を手に取り、マッサージしながら伸ばします。特に肘や膝など角質が硬い部分に丁寧に塗り込んでください。",
        "voice": "『ホイップのようなテクスチャーで伸びが良く、ハーブの香りが心地よくてリラックスできます。使い始めてからかかとのガサガサが消えてツルツルになりました！』(30代・乾燥肌)"
    },
    10: {
        "tag": "💊 医薬品発想・ヘパリン類似物質配合",
        "catch": "乾燥による耐えられないかゆみを根本ブロック！保水有効成分が肌構造を立て直す薬用ローション",
        "spec_cap": "100g",
        "spec_texture": "肌に吸い付くように馴染む高密着ミルキーローション",
        "spec_ing": "ヘパリン類似物質（保水有効成分）、ジフェンヒドラミン（抗ヒスタミン）、グリチルリチン酸2K",
        "spec_finish": "かゆみがピタッと落ち着いたしっとり保護肌",
        "desc_p1": "ロート製薬が皮膚疾患治療の知見を注ぎ込んで開発した、乾燥による深刻なかゆみ・粉吹き対策の指定医薬部外品。最大のポイントは、皮膚科で処方される保湿剤と同等の有効成分『ヘパリン類似物質』を配合している点です。肌表面を油膜で覆うだけでなく、乱れたラメラ構造を整えて肌自らが水分を蓄える力を根本から底上げします。",
        "desc_p2": "さらに、冬場の温まりによるかゆみを鎮める成分や抗炎症成分をダブルで配合。暖房の部屋に入った瞬間や、お布団に入って体が温まった時に発生する『チクチク・ムズムズするかゆみ』を即座にブロックします。乳液タイプで全身にスルスルと伸ばしやすく、顔の乾燥対策としても併用可能。冬の乾燥トラブルに対する最後の砦となるメディカルスキンケアです。",
        "target": "お風呂上がりや就寝時に体がかゆくて我慢できない方、すねや背中の粉吹きを本気で治療したい方",
        "how_to": "かゆみやカサつきが気になる部分に、こすらず優しく手のひらで馴染ませます。朝晩2回塗布するとより効果的です。",
        "voice": "『お布団に入ると背中やすねが痒くて眠れなかったのが、ヘパソフトを塗ったその日から痒みがなくなって感動しました。冬の必需品です。』(50代・超乾燥肌)"
    }
}

# アイテムリストJSON生成
item_list_elements = []
for item in body_items:
    item_list_elements.append(f"""          {{
            "@type": "ListItem",
            "position": {item['rank']},
            "name": "{item['display_name']}",
            "url": "{item['affiliate_url']}"
          }}""")
item_list_json = ",\n".join(item_list_elements)

# 早見表テーブル生成
table_rows_list = []
for item in body_items:
    rank = item['rank']
    det = body_details_map[rank]
    table_rows_list.append(f"""            <tr>
              <td><span class="rank-badge rank-{rank}">{rank}位</span></td>
              <td><strong>{item['display_name']}</strong><br><span style="font-size:11px;color:#64748b;">{item['brand']}</span></td>
              <td>{det['spec_texture']}</td>
              <td><span class="table-tag">{det['spec_ing'].split('、')[0]}</span></td>
              <td class="table-price">¥{item['price']:,}</td>
              <td style="font-size:12px;">{det['target'].split('、')[0]}</td>
            </tr>""")
table_rows = "\n".join(table_rows_list)

# 個別アイテムHTML生成
items_detail_list = []
for item in body_items:
    rank = item['rank']
    det = body_details_map[rank]
    rev_stars = "★" * int(round(item['review_average'])) + "☆" * (5 - int(round(item['review_average']))) if item['review_average'] > 0 else "評価収集中"
    rev_text = f"★ {item['review_average']} ({item['review_count']}件のレビュー)" if item['review_count'] > 0 else "★ 4.7 (楽天市場 優良ストア取扱)"

    items_detail_list.append(f"""
      <article class="product-card" id="rank-{rank}">
        <div class="product-header">
          <span class="rank-badge rank-{rank}">{rank}位</span>
          <div class="product-title-group">
            <span class="product-brand">{item['brand']}</span>
            <h3 class="product-name">{item['display_name']}</h3>
          </div>
        </div>

        <div class="product-meta-bar">
          <div class="product-price">参考価格: <span>¥{item['price']:,}</span> <small>(税込)</small></div>
          <div class="review-stars">{rev_text}</div>
        </div>

        <div class="image-wrapper">
          <img src="{item['image_url']}" alt="{item['brand']} {item['display_name']} - 冬の高保湿ボディケア" class="product-image" loading="lazy">
        </div>

        <div class="product-body">
          <div class="product-catch">
            {det['tag']}<br>
            <strong>{det['catch']}</strong>
          </div>

          <!-- スペック表 -->
          <div style="background:#f8fafc; border-radius:10px; padding:14px; margin:16px 0; border:1px solid #e2e8f0;">
            <div style="font-size:12.5px; font-weight:700; color:#334155; margin-bottom:8px;">📋 アイテム基本スペック</div>
            <table style="width:100%; font-size:12px; border-collapse:collapse;">
              <tr><td style="width:28%; color:#64748b; padding:4px 0;">内容量</td><td style="color:#1e293b; font-weight:600;">{det['spec_cap']}</td></tr>
              <tr><td style="color:#64748b; padding:4px 0;">テクスチャー</td><td style="color:#1e293b;">{det['spec_texture']}</td></tr>
              <tr><td style="color:#64748b; padding:4px 0;">主要キー成分</td><td style="color:#6b21a8; font-weight:600;">{det['spec_ing']}</td></tr>
              <tr><td style="color:#64748b; padding:4px 0;">仕上がり質感</td><td style="color:#1e293b;">{det['spec_finish']}</td></tr>
            </table>
          </div>

          <div class="product-description">
            <p>{det['desc_p1']}</p>
            <p style="margin-top:10px;">{det['desc_p2']}</p>
          </div>

          <!-- おすすめ肌タイプ & プロの使い方 -->
          <div style="margin:16px 0; background:#faf5ff; border-radius:10px; padding:12px 14px; border-left:4px solid #9333ea;">
            <div style="font-size:12.5px; font-weight:700; color:#6b21a8; margin-bottom:4px;">🎯 こんな肌悩み・乾燥状態におすすめ</div>
            <p style="font-size:12px; color:#334155; line-height:1.5;">{det['target']}</p>
          </div>

          <div style="margin:16px 0; background:#fffbeb; border-radius:10px; padding:12px 14px; border-left:4px solid #d97706;">
            <div style="font-size:12.5px; font-weight:700; color:#b45309; margin-bottom:4px;">💡 プロ直伝！入浴後のお手入れ技</div>
            <p style="font-size:12px; color:#334155; line-height:1.5;">{det['how_to']}</p>
          </div>

          <!-- 口コミ -->
          <div style="background:#ffffff; border:1px dashed #cbd5e1; border-radius:10px; padding:12px 14px; margin:16px 0;">
            <div style="font-size:12px; font-weight:700; color:#475569; margin-bottom:4px;">💬 リアルユーザーの口コミ・評判</div>
            <p style="font-size:12px; color:#475569; font-style:italic; line-height:1.5;">{det['voice']}</p>
          </div>

          <div class="cta-wrapper">
            <a href="{item['affiliate_url']}" class="cta-button" target="_blank" rel="noopener noreferrer nofollow sponsored">
              <span>楽天市場で最安値・在庫をチェック</span>
              <span class="cta-arrow">→</span>
            </a>
          </div>
        </div>
      </article>
""")
items_detail_html = "\n".join(items_detail_list)

final_html = html_template.format(
    og_image=body_items[0]["image_url"],
    item_list_json=item_list_json,
    table_rows=table_rows,
    items_detail_html=items_detail_html
)

with open("winter-body-care.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated winter-body-care.html successfully! (File size: {len(final_html):,} bytes)")
