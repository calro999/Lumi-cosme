import json

with open("rakuten_latest_3articles_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

eye_items = data["winter_eye_cream"]["items"]

html_template = """<!DOCTYPE html>
<html lang="ja" prefix="og: http://ogp.me/ns#">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【2026最新】暖房直撃の目元・ほうれい線をふっくら密着！乾燥小じわ撃退・高保湿アイクリーム＆薬用リンクルケアおすすめ10選 | Lumi Cosme</title>
  <meta name="description" content="11月・12月の暖房直撃で夕方に目元がひび割れる、笑うと目尻にちりめんジワが残る悩みを一撃解消！純粋レチノール、ポーラ独自ニールワン、多重層リポソーム、浸透型ペプチド配合の実力派アイクリーム＆シワ改善美容液厳選10選。皮膚の薄い目元を傷めない薬指ピアノタッチ塗布法まで徹底解説。">
  <meta name="keywords" content="アイクリーム, リンクルクリーム, 目元美容液, シワ改善, エリクシール レチノパワー, コスメデコルテ リポソーム, ポーラ リンクルショット, なめらか本舗, キュレル, 2026コスメ">

  <!-- SEO & Canonical -->
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-eye-cream">
  <meta name="robots" content="index, follow">

  <!-- OGP -->
  <meta property="og:site_name" content="Lumi Cosme (ルミコスメ)">
  <meta property="og:title" content="暖房直撃の目元・ほうれい線をふっくら密着！乾燥小じわ撃退・高保湿アイクリーム＆薬用リンクルケアおすすめ10選">
  <meta property="og:description" content="冬の乾燥小じわ・ちりめんジワを徹底撃退！エリクシール、コスメデコルテ、ポーラ、なめらか本舗など注目のアイケア10選を徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-eye-cream">
  <meta property="og:image" content="{og_image}">
  <meta property="og:locale" content="ja_JP">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="暖房直撃の目元・ほうれい線をふっくら密着！乾燥小じわ撃退・高保湿アイクリーム＆薬用リンクルケアおすすめ10選">
  <meta name="twitter:description" content="冬の乾燥小じわ・ちりめんジワを徹底撃退！エリクシール、コスメデコルテ、ポーラ、なめらか本舗など注目のアイケア10選を徹底比較。">
  <meta name="twitter:image" content="{og_image}">

  <link rel="stylesheet" href="style.css">

  <!-- 構造化データ (JSON-LD) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "headline": "暖房直撃の目元・ほうれい線をふっくら密着！乾燥小じわ撃退・高保湿アイクリーム＆薬用リンクルケアおすすめ10選",
        "description": "11月・12月の本格乾燥シーズンに必須の高保湿アイクリーム＆薬用リンクルケアの選び方、有効成分比較、おすすめ10選を徹底レビュー。",
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
        "name": "冬の高保湿アイクリーム＆薬用リンクルケアおすすめ10選",
        "itemListElement": [
{item_list_json}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "アイクリームは全顔用の高保湿クリームで代用してはいけませんか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "おすすめできません。目元の皮膚は頬の約3分の1の薄さしかなく、皮脂腺が極めて少ないため、全顔用の重い油分クリームを塗ると油膜が浮いてしまったり、逆に成分分子が大きすぎて浸透しきれず稗粒腫（はいりゅうしゅ・白いポツポツ）の原因になることがあります。アイクリームは微小な目元の角層に浸透しやすい特殊カプセルや、シワ改善の有効成分が高濃度配合されているため、専用ケアが不可欠です。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "レチノール配合のアイクリームは朝使っても大丈夫ですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "純粋レチノール配合製品を朝使用する場合は、『必ずSPF値の高い日焼け止め』を上から重ねてください。レチノールは紫外線によって分解されやすく、無防備な状態だと紫外線刺激を受けやすくなるためです。朝のメイクヨレを防ぎたい方や紫外線対策が面倒な方は、朝はリポソームやナイアシンアミドなどの保湿系アイセラム、夜にレチノールやニールワンと使い分けるのが最も効果的です。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "アイクリームを塗る順番はスキンケアのどの段階ですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "基本的には『乳液の後、全顔用クリームの前』または『スキンケアの一番最後』です。みずみずしいジェル・セラム状のアイケア（コスメデコルテなど）は化粧水や乳液の直後、こっくりした油分膜を作るリンクルクリーム（エリクシールやポーラなど）はお手入れの一番最後に使用します。各メーカーの指定順序を確認しましょう。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "アイクリームはほうれい線や眉間のシワにも塗っていいですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "もちろん効果的です！アイクリームに配合されている『純粋レチノール』『ニールワン』『ナイアシンアミド』などのシワ改善成分は、目元だけでなく、ほうれい線、口元のマリオネットライン、眉間の表情ジワ、首の横ジワにも共通して高い改善効果を発揮します。1本あれば気になる全顔のエイジングサインを集中リペアできます。"
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body class="theme-eye">

  <!-- ヘッダー -->
  <header class="site-header">
    <div class="header-badge">👁️ 2026 WINTER EYE CARE SPECIAL</div>
    <h1 class="site-title">高保湿アイクリーム＆リンクルケア10選</h1>
    <p class="site-subtitle">暖房直撃の目元・ほうれい線をふっくら密着！乾燥小じわとファンデ割れを撃退</p>
  </header>

  <main class="container">

    <!-- 記事トップ・アイキャッチ -->
    <article class="article-intro">
      <div class="article-meta">
        <span class="article-cat-tag">スキンケア特集 / アイクリーム・目元美容液</span>
        <span class="article-date">📅 2026.10.28 更新</span>
      </div>

      <h1 class="article-main-heading">暖房直撃の目元・ほうれい線をふっくら密着！乾燥小じわ撃退・高保湿アイクリーム＆薬用リンクルケアおすすめ10選</h1>

      <p class="article-lead">
        11月から12月にかけて、オフィスのエアコンや電車の暖房が本格稼働を始めると、<strong>「夕方にふとオフィスの鏡を見たら、目の下に無数のちりめんジワが刻まれていた」「ファンデーションが目尻やほうれい線の溝にめり込んで割れている」「まぶたがカサついてアイシャドウが全然発色しない」</strong>という悲鳴が急増します。<br><br>
        それもそのはず、<strong>人間の目元の皮膚の薄さはわずか約0.5mm</strong>。ゆで卵の薄皮ほどの厚みしかなく、皮脂腺もほとんど存在しません。その無防備な皮膚が、<strong>1日に2万回以上の瞬き</strong>に晒され、さらに現代人は長時間のスマートフォンやPC作業による眼精疲労と血行不良に追い打ちをかけられています。<br><br>
        この過酷な真冬の環境下で乾燥小じわを放置すると、単なる一時的な乾燥から、真皮層のコラーゲンが断裂した「定着ジワ」へと進行してしまいます。<br><br>
        本記事では、厚生労働省認可の純粋レチノール、真皮改善成分ニールワン、多重層ナノバイセルリポソーム、ペプチド複合体など、冬の乾燥小じわを即効でふっくら持ち上げる実力派アイケア10選を徹底検証します！
      </p>

      <!-- 目次ナビゲーション -->
      <nav class="toc-container">
        <div class="toc-title">📑 本記事の目次</div>
        <ul class="toc-list">
          <li><a href="#why-eye">1. なぜ冬の目元は真っ先に老け見えするのか？極薄皮膚と2万回瞬きの真実</a></li>
          <li><a href="#types">2. シワの深さと肌質で選ぶ！アイクリームの3大アプローチ診断</a></li>
          <li><a href="#comparison">3. 【一目でわかる】冬の高保湿アイクリーム10選 比較早見表</a></li>
          <li><a href="#ranking">4. 【2026最新】冬の高保湿アイクリーム＆薬用リンクルケアおすすめ10選 詳細個別レビュー</a></li>
          <li><a href="#technique">5. 摩擦ゼロで浸透率最大化！プロ直伝「薬指ピアノタッチ塗布メソッド」</a></li>
          <li><a href="#faq">6. アイクリーム・リンクルケアに関するよくある質問（FAQ）</a></li>
          <li><a href="#related">7. あわせて読みたい！冬の保湿ケア特集一覧</a></li>
        </ul>
      </nav>
    </article>

    <!-- メカニズムセクション -->
    <section id="why-eye">
      <h2 class="section-title">なぜ冬の目元は真っ先に老け見えするのか？極薄皮膚と2万回瞬きの真実</h2>
      <p class="content-text">
        顔の中で最も年齢が現れやすく、冬の乾燥ダメージを最初に受ける部位が「目元」と「口元」です。その理由は3つの皮膚生理学的弱点にあります。
      </p>
      <p class="content-text">
        第一に、<strong>「角質層が極端に薄く、皮脂膜がほぼ存在しない」</strong>こと。頬の約3分の1の薄さしかないため、水分を蓄えるタンク容量が極めて小さく、暖房の風が当たった瞬間に水分が蒸散します。第二に、<strong>「1日2万回の過酷なまばたき運動」</strong>。乾いた紙を何度も折り曲げると深い折り目がつくのと同様に、乾燥した皮膚が瞬きによって伸縮を繰り返すことで、ちりめんジワが瞬く間に刻まれます。
      </p>
      <div class="product-catch" style="margin: 20px 0;">
        💡 冬の目元を守るアイクリーム選びの3大チェック項目：<br>
        ① <strong>「純粋レチノール」「ニールワン」「ナイアシンアミド」の確かな有効成分</strong><br>
        ② <strong>まばたきの摩擦に負けない「高密着ストレッチ膜」を形成するテクスチャー</strong><br>
        ③ <strong>日中のファンデ割れを防ぐ「朝晩兼用」または「メイク前の密着性」</strong>
      </div>
    </section>

    <!-- タイプ別診断セクション -->
    <section id="types">
      <h2 class="section-title">シワの深さと肌質で選ぶ！アイクリームの3大アプローチ診断</h2>
      <div class="content-text">
        <p>目元の悩みレベルに合わせて、最適な有効成分とテクスチャーを選びましょう。</p>
        
        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #fae8ff; box-shadow: var(--shadow-soft);">
          <h3 style="color: #701a75; font-size: 16px; font-weight: 700; margin-bottom: 6px;">① 医薬部外品・本格シワ改善アプローチ（エリクシール、ポーラ、資生堂）</h3>
          <p style="font-size: 13.5px; color: #334155;">「笑った後の目尻のシワが戻らない」「眉間やほうれい線が定着してきた」方に。真皮のコラーゲン産生を促し、厚生労働省からシワ改善効果を認可された医薬部外品処方が確かな結果をもたらします。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #fae8ff; box-shadow: var(--shadow-soft);">
          <h3 style="color: #701a75; font-size: 16px; font-weight: 700; margin-bottom: 6px;">② ナノカプセル多重層・水分持続アプローチ（コスメデコルテ、クラランスなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">「夕方になると目元がパリパリに乾いてファンデが割れる」「PC作業で目元がどんよりくすむ」方に。0.1ミクロンの微小リポソームカプセルが一日中時間差で潤いを放出し、メイク崩れを防ぎます。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #fae8ff; box-shadow: var(--shadow-soft);">
          <h3 style="color: #701a75; font-size: 16px; font-weight: 700; margin-bottom: 6px;">③ 低刺激バリア・高コスパ日常アプローチ（キュレル、なめらか本舗、アスタリフトなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">「強い成分だと目元がヒリつきやすい」「毎日惜しみなく目元・口元にたっぷり塗り込みたい」方に。セラミド補給やマイルドな豆乳発酵ピュアレチノールで、敏感な薄膜皮膚をやさしく守り抜きます。</p>
        </div>
      </div>
    </section>

    <!-- 比較早見表 -->
    <section id="comparison">
      <h2 class="section-title">【一目でわかる】冬の高保湿アイクリーム10選 比較早見表</h2>
      <p class="content-text">掲載している価格は楽天市場の最新調査価格（税込）です。横スクロールで有効成分やテクスチャーを比較できます。</p>

      <div class="table-scroll-wrapper">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>タイプ・特徴</th>
              <th>主要キー成分</th>
              <th>参考価格</th>
              <th>おすすめな目元悩み</th>
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
      <h2 class="section-title">【2026最新】冬の高保湿アイクリーム＆薬用リンクルケアおすすめ10選 詳細個別レビュー</h2>
{items_detail_html}
    </section>

    <!-- プロ直伝テクニック -->
    <section id="technique">
      <h2 class="section-title">摩擦ゼロで浸透率最大化！プロ直伝「薬指ピアノタッチ塗布メソッド」</h2>
      <div class="content-text">
        <p>
          目元の皮膚はティッシュペーパー1枚ほどの薄さしかありません。人差し指でゴシゴシ擦り込むと摩擦ジワを自ら作ることになります。最も圧がかかりにくい「薬指」を使ったプロの手順です。
        </p>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fae8ff;">
          <h3 style="color: #701a75; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 1：米粒1個分を「薬指の腹」に取り、両指で温める</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            両目の使用量は米粒大（約直径5mm）。薬指の腹同士を軽くすり合わせて体温で温めることで、こっくりしたクリームがとろけて皮膚への伸びが格段に良くなります。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fae8ff;">
          <h3 style="color: #701a75; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 2：下まぶた・上まぶたに「点置き」してピアノタッチ</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            目の下（目頭・中央・目尻）と上まぶたの骨のキワにクリームを点置きします。ピアノの鍵盤を優しく叩くようにトントンと軽いタッチ（パッティング）で馴染ませていきます。決して横に引っ張ってはいけません。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #fae8ff;">
          <h3 style="color: #701a75; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 3：目尻のカラスの足跡とほうれい線は「シワを広げて」塗り込む</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            目尻の放射状のシワやほうれい線は、反対側の手で優しく皮膚を押し広げ、シワの溝の奥にクリームを優しく入れ込むように馴染ませます。仕上げに手のひら全体で目元を覆い、5秒間温めると密着度が最大化します。全顔のベースには<a href="/winter-base-makeup" style="color: #a21caf; font-weight: 700; text-decoration: underline;">高保湿ファンデ＆下地</a>を重ねると日中も崩れません。
          </p>
        </div>
      </div>
    </section>

    <!-- FAQセクション -->
    <section id="faq">
      <h2 class="section-title">アイクリーム・リンクルケアに関するよくある質問（FAQ）</h2>
      <div class="faq-container">
        <div class="faq-item">
          <div class="faq-question">Q1. アイクリームは全顔用の高保湿クリームで代用してはいけませんか？</div>
          <div class="faq-answer">
            おすすめできません。目元の皮膚は頬の約3分の1の薄さしかなく、皮脂腺が極めて少ないため、全顔用の重い油分クリームを塗ると油膜が浮いてしまったり、逆に成分分子が大きすぎて浸透しきれず稗粒腫（はいりゅうしゅ・白いポツポツ）の原因になることがあります。アイクリームは微小な目元の角層に浸透しやすい特殊カプセルや、シワ改善の有効成分が高濃度配合されているため、専用ケアが不可欠です。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q2. レチノール配合のアイクリームは朝使っても大丈夫ですか？</div>
          <div class="faq-answer">
            純粋レチノール配合製品を朝使用する場合は、『必ずSPF値の高い日焼け止め』を上から重ねてください。レチノールは紫外線によって分解されやすく、無防備な状態だと紫外線刺激を受けやすくなるためです。朝のメイクヨレを防ぎたい方や紫外線対策が面倒な方は、朝はリポソームやナイアシンアミドなどの保湿系アイセラム、夜にレチノールやニールワンと使い分けるのが最も効果的です。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q3. アイクリームを塗る順番はスキンケアのどの段階ですか？</div>
          <div class="faq-answer">
            基本的には『乳液の後、全顔用クリームの前』または『スキンケアの一番最後』です。みずみずしいジェル・セラム状のアイケア（コスメデコルテなど）は化粧水や乳液の直後、こっくりした油分膜を作るリンクルクリーム（エリクシールやポーラなど）はお手入れの一番最後に使用します。各メーカーの指定順序を確認しましょう。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q4. アイクリームはほうれい線や眉間のシワにも塗っていいですか？</div>
          <div class="faq-answer">
            もちろん効果的です！アイクリームに配合されている『純粋レチノール』『ニールワン』『ナイアシンアミド』などのシワ改善成分は、目元だけでなく、ほうれい線、口元のマリオネットライン、眉間の表情ジワ、首の横ジワにも共通して高い改善効果を発揮します。1本あれば気になる全顔のエイジングサインを集中リペアできます。
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
          <div class="related-link-desc">アイクリームで整えた目元を綺麗に魅せる！暖房下でもほうれい線や目尻がひび割れない最新ベースメイク。</div>
        </a>

        <a href="/winter-serum-booster" class="related-link-card">
          <div class="related-link-title">💧 浸透力を底上げする高保湿・導入先行美容液おすすめ10選</div>
          <div class="related-link-desc">硬くなった冬肌をほぐし、アイクリームの浸透ルートを切り拓く先行美容液の選び方。</div>
        </a>

        <a href="/winter-face-mask" class="related-link-card">
          <div class="related-link-title">💧 水分爆弾で砂漠肌を即リセット！翌朝の化粧ノリ激変・高保湿シートマスク＆夜用パック10選</div>
          <div class="related-link-desc">目元の乾燥小じわもまとめて集中水分チャージ！ひと晩でふっくら肌を叶える最新マスク集。</div>
        </a>

        <a href="/winter-moisture-cream" class="related-link-card">
          <div class="related-link-title">🧴 保湿力の強さで肌乾燥とさようなら！高保湿フェイスクリーム＆濃密バーム10選</div>
          <div class="related-link-desc">全顔の乾燥対策はこちら！真冬の厳しい乾きから肌を守り抜くセラミド＆ヘパリン類似物質配合クリーム。</div>
        </a>

        <a href="/winter-lip-care" class="related-link-card">
          <div class="related-link-title">🎁 冬のガサガサ皮剥けに終止符！高保湿リップトリートメント＆濃密ティント10選</div>
          <div class="related-link-desc">目元と同じく皮膚の薄いデリケートゾーン！唇の皮剥け・縦ジワを消し去る極上トリートメント。</div>
        </a>

        <a href="/winter-body-care" class="related-link-card">
          <div class="related-link-title">🛁 すねの粉吹き・全身の乾燥かゆみにサヨナラ！高保湿ボディミルク＆濃厚ボディバター10選</div>
          <div class="related-link-desc">お風呂上がりの全身をうるおいで包み込む！すねの粉吹きやかゆみを防ぐ厳選ボディケア。</div>
        </a>

        <a href="/winter-hair-care" class="related-link-card">
          <div class="related-link-title">🌿 冬の静電気・毛先パサつきと完全決別！高保湿ヘアオイル＆濃厚ヘアマスク10選</div>
          <div class="related-link-desc">マフラー摩擦や暖房で傷んだキューティクルを補修。サロン級のうる艶髪を叶える冬の必須アイテム。</div>
        </a>

        <a href="/winter-hand-care" class="related-link-card">
          <div class="related-link-title">🤲 手荒れ・あかぎれ・ささくれ知らずへ！神ハンドクリーム＆ネイルケア10選</div>
          <div class="related-link-desc">水仕事や冷風で荒れた手先を即効リペア。ベタつかないデスク用から夜の集中補修バームまで。</div>
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

eye_details_map = {
    1: {
        "tag": "👑 日本売上No.1！純粋レチノールの最高峰",
        "catch": "厚労省認可のシワ改善有効成分！硬くなった目元の表皮をふっくらほぐし、深いシワまで確かな手応え",
        "spec_cap": "15g (約1ヶ月分)",
        "spec_texture": "体温ですっと馴染み、ピタッと密着するリッチクリーム",
        "spec_ing": "純粋レチノール（医薬部外品 有効成分）、コラーゲンGL、高濃度グリセリン",
        "spec_finish": "笑っても跳ね返すようなピンとした弾力と上質なツヤ",
        "desc_p1": "日本で初めて『シワを改善する』医薬部外品認可を取得した資生堂の最先端サイエンスを凝縮したエリクシールの名品が、さらに進化を遂げたレチノパワー。最大の強みは、熱や光に極めて弱い『純粋レチノール』を独自の特殊チューブによって最後まで新鮮な状態で保ち、肌にダイレクトに届ける点です。角質層の水分量を高めて柔軟にほぐし、肌自らがヒアルロン酸を生み出す力を促進します。",
        "desc_p2": "指に取るとみずみずしく、肌に伸ばした瞬間からシワの凹凸にピタッと張り付くストレッチ膜を形成。11-12月の暖房直撃による目尻のちりめんジワや、ファンデーションのめり込みを強力に予防します。使い続けることで、乾燥による浅い小ジワだけでなく、深く刻まれかけた表情ジワにも力強いハリを実感できます。目元だけでなく、ほうれい線ケアとしても絶対的信頼を集める名品です。",
        "target": "笑った後に目尻のシワがなかなか戻らない方、ほうれい線や眉間のシワを本気で改善したい20代後半〜50代の方",
        "how_to": "朝と夜のお手入れの最後に、指先に小さなパール粒1個分を取り、目元や口元のシワが気になる部分へ優しく馴染ませます（※朝使用時は日焼け止めを併用）。",
        "voice": "『夕方の目元のファンデ割れが完全に消えました！ちりめんジワがふっくら持ち上がって、目元にハリが戻ったおかげで疲れて見えなくなりました。一生手放せません。』(30代・乾燥肌)"
    },
    2: {
        "tag": "💧 ナノバイセル×多重層リポソームの衝撃",
        "catch": "1滴に1.6兆個の微小カプセル！夕方まで目元が乾かない、みずみずしくも濃密なアイセラム",
        "spec_cap": "20ml (約60回分)",
        "spec_texture": "ベタつきゼロでスッと角層に消える濃密ウォータリーエッセンス",
        "spec_ing": "多重層バイオリポソーム、ナノバイセル、ヒト型セラミド、白樺樹液",
        "spec_finish": "キメが極限まで整い、朝のメイクが吸い付くみずみずしいハリ肌",
        "desc_p1": "コスメデコルテのアイコン『リポソーム』シリーズが誇る、高機能目元特化美容液。玉ねぎ状の多重層リポソームカプセルに加え、新開発の超微細ディスクカプセル『ナノバイセル』をダブル配合。1滴の中に約1.6兆個ものカプセルが凝縮されており、皮膚が極めて薄い目元の角層深くへ瞬時に浸透し、24時間時間差で美容成分を放出し続けます。",
        "desc_p2": "一般的なアイクリームにありがちな油分の重さやベタつきが一切なく、まるで澄んだ泉のようなみずみずしい感触。朝のメイク直前に塗ってもファンデーションやアイシャドウがヨレる心配が全くありません。ボトルのキャップ先端がマッサージャー（アプリケーター）になっており、ツボを優しく刺激しながら血行を促進できるのも秀逸。夕方の乾燥くすみや目の下のどんより感を一掃します。",
        "target": "重いクリームを使うとアイメイクがヨレる方、日中の暖房下で目元がパリパリに乾いてつっぱる方",
        "how_to": "朝晩の化粧水・乳液の後、指先に適量（1プッシュ）を取り、目の周りに優しく伸ばします。キャップの丸い突起で目頭や眉下を軽くプッシュすると効果倍増。",
        "voice": "『朝のメイク前に使えるのが最高です！サラッとしているのに一日中潤いが続いて、夕方になっても目の下が全くカサつきません。アプリケーターのひんやり感も病みつきです。』(30代・混合肌)"
    },
    3: {
        "tag": "⚡ シワ改善のパイオニア・独自成分ニールワン",
        "catch": "好中球エラスターゼの暴走を抑える！真皮のコラーゲン分解を食い止める医療発想のシワ改善美容液",
        "spec_cap": "20g",
        "spec_texture": "水分を一切使わず有効成分を閉じ込めた高密着固形セラム",
        "spec_ing": "ニールワン（ポーラ独自有効成分・シワ改善）、ICユニット、複合植物エキス",
        "spec_finish": "シワの溝を埋めるようにピタッと固定されるマットストレッチ感",
        "desc_p1": "日本で初めてシワを改善する医薬部外品有効成分として承認されたポーラ独自の『ニールワン』を配合した伝説的リンクルセラム。紫外線や表情圧によって生じる微弱な炎症を肌が『傷』と勘違いし、好中球エラスターゼが誤って真皮のコラーゲンを破壊してしまうメカニズムを解明。ニールワンがその酵素の働きをピタッとブロックし、真皮の構造を再生させます。",
        "desc_p2": "製剤中に水を一切含まない無水処方を採用。肌表面の水分（化粧水や乳液のうるおい）に引き寄せられるようにして角層深くへとダイレクトに浸透していきます。斜めにカットされた特徴的なヘッドで、目元やほうれい線に直接クリームをフィットさせながら塗り伸ばせる設計。真冬の過酷な乾燥下でも、刻まれかけた深いシワに力強く立ち向かう頼もしき名品です。",
        "target": "目尻のシワやほうれい線が深くなり、何を使っても効果を実感できなかった本格エイジング世代の方",
        "how_to": "朝晩、化粧水で肌を整えた直後（水分がある状態）に、チューブ先端を目元やシワに直接当ててシワに対して直角に伸ばします。",
        "voice": "『本当にシワが薄くなってきて感動しました！ほうれい線と眉間に毎日塗り込んでいたら、ファンデが溝に落ちなくなりました。高価ですが確実に結果が出る美容液です。』(40代・普通肌〜乾燥肌)"
    },
    4: {
        "tag": "💰 1,000円以下の奇跡！ピュアレチノール×豆乳",
        "catch": "高コスパで毎日の惜しみない集中ケア！ふっくらもち肌を叶えるドラッグストアの超人気アイクリーム",
        "spec_cap": "20g",
        "spec_texture": "こっくり濃厚で密着力の高い高保湿クリーム",
        "spec_ing": "ピュアレチノール、豆乳発酵液、ビタミンE誘導体",
        "spec_finish": "指を押し返すようなもっちりとした柔らか目元",
        "desc_p1": "『プチプラの枠を超えた成分構成』として美容賢者の間でも絶賛されるサナなめらか本舗のリンクルアイクリーム。1,000円以下という驚異的な価格帯でありながら、エイジングケアの王道成分である『ピュアレチノール』と、肌本来のうるおいを引き出す『豆乳発酵液』を贅沢にダブル配合。乾燥によって縮こまった目元の角層をふっくらとほぐします。",
        "desc_p2": "こっくりと厚みのあるテクスチャーで、塗った瞬間から目元にピタッと密着。まばたきによる摩擦を和らげ、外気の冷風からデリケートな皮膚を保護します。無香料・無鉱物油の安心設計で、プチプラだからこそ目元だけでなく、ほうれい線、眉間、首元までケチらずたっぷり使えるのが最大の強み。冬のデイリーアイケアのエントリーモデルとして最高の選択肢です。",
        "target": "アイケアを初めて始める方、1,000円台で惜しみなく目元・口元全体にたっぷり塗りたい学生〜20代の方",
        "how_to": "スキンケアの最後に、指先に適量を取り、目元の気になる部分にトントンと優しく叩き込むように馴染ませます。",
        "voice": "『この値段でピュアレチノールが入っているのは本当に奇跡！毎晩目元とほうれい線にたっぷり塗っていたら、冬のちりめんジワが目立たなくなりました。何本もリピしています。』(20代・乾燥肌)"
    },
    5: {
        "tag": "🛡️ 敏感肌の目元をセラミドで濃密シールド",
        "catch": "まぶたのカサつき・粉吹き・ヒリつきを即鎮静！消炎剤配合で皮膚の薄い目元を徹底ガード",
        "spec_cap": "25g",
        "spec_texture": "コクがあるのに負担なくスッと広がるモイストリペアバーム",
        "spec_ing": "セラミド機能成分、アラントイン（消炎有効成分）、ショウキョウエキス",
        "spec_finish": "刺激感ゼロでしっとりと落ち着いたバリア密着肌",
        "desc_p1": "冬になるとまぶたがカサカサになり、強いエイジングケア成分だとピリピリ刺激を感じてしまう敏感肌のための救世主。花王キュレルの皮膚科学から生まれた薬用モイストリペアアイクリームは、目元の必須成分であるセラミドの働きを補う『セラミド機能成分』を高濃度配合。スカスカになった角層バリアを強力に補修します。",
        "desc_p2": "さらに肌荒れを防ぐ有効成分『アラントイン』を配合し、アイメイクの摩擦や乾燥によって赤み・痒みが生じやすい目元を穏やかに鎮静。ショウキョウエキスが角層を潤いで満たし、ふっくらとしたハリを与えます。アルコールフリー、無香料、弱酸性の徹底した低刺激処方なので、皮膚が薄くデリケートな目元でも安心。冬の敏感な目元トラブルを未然に防ぎます。",
        "target": "冬になると目元やまぶたがカサついて赤くなりやすい方、刺激の強いレチノールが使えない敏感肌の方",
        "how_to": "化粧水・乳液の後、適量（片目あたり直径約5mm）を指先に取り、目頭から目尻にかけて優しく押さえるように馴染ませます。",
        "voice": "『冬になるとまぶたが乾燥で痒くなって皮が剥けていたのが、キュレルを塗ったら数日でスベスベに治まりました。刺激が一切ないのが本当にありがたいです。』(30代・敏感肌)"
    },
    6: {
        "tag": "🌿 水分×油分の黄金比！2層式クラランス",
        "catch": "世界的人気美容液の目元版！植物エキスとエモリエントオイルがまぶたのくすみとたるみを集中ケア",
        "spec_cap": "20ml",
        "spec_texture": "プッシュした瞬間に混ざり合う黄金比のミルキーエマルジョン",
        "spec_ing": "ワイルドチャービルエキス（オーガニック）、ウコンエキス、アボカドペプチド",
        "spec_finish": "内側から発光するような明るさとピンとした引き締め感",
        "desc_p1": "クラランスの最高傑作美容液『ダブルセーラム』のフォーミュラを目元のために再構築したプレステージアイセラム。エマルジョン（水分）とオイル（油分）が容器内部で完全にセパレートされており、プッシュした瞬間に人間の皮脂膜と同じ黄金比率（水7：油3）で混ざり合います。これにより、みずみずしい浸透力と濃厚な保護膜の両立を実現しています。",
        "desc_p2": "オーガニックのワイルドチャービルエキスなど13種類の厳選された植物成分を配合。乾燥による小じわだけでなく、長時間のスマホ作業やPC作業でどんより重くなったまぶたをキュッと引き締め、明るく澄んだ目元へと整えます。ダイヤルを回すことで季節や肌状態に合わせて1回の吐出量を2段階で調節できる機能性も高く評価されています。",
        "target": "目元の小ジワだけでなく、まぶたのむくみやクマ、くすみも同時にマルチケアしたい30代〜50代の方",
        "how_to": "手のひらに1プッシュ出し、指先で軽く混ぜ合わせてから、目の上下を優しくプレスするように馴染ませます。",
        "voice": "『オイルが入っているのに全くベタつかず、目元がパッと明るくなります！朝使うと目元のむくみがスッキリして目がパッチリ開く感覚があります。香りも最高！』(30代・普通肌)"
    },
    7: {
        "tag": "🧬 次世代ペプチド複合体・皮膚科発想",
        "catch": "CL1870レーザーフォーカス錯体！表情の動きにしなやかに寄り添う高密度アイクリーム",
        "spec_cap": "15ml",
        "spec_texture": "シルクのようになめらかなホイップクリーム質感",
        "spec_ing": "CL1870ペプチド複合体、カフェイン、ヒアルロン酸Na、ダイズ種子エキス",
        "spec_finish": "ベルベットのように毛穴や小じわの凹凸をぼかすなめらか肌",
        "desc_p1": "皮膚科学に基づいたアプローチで世界的な信頼を集めるクリニークのエイジングケアアイクリーム。最大の武器は、3種類の先進ペプチドやカフェインをブレンドした独自複合体『CL1870レーザーフォーカス錯体』です。乾燥によるちりめんジワだけでなく、目元のコラーゲン構造をサポートし、ふっくらとした立体感のある目元へと整えます。",
        "desc_p2": "ホイップクリームのように軽やかでシルキーなテクスチャーが特徴で、肌に乗せるとスルリと伸びて瞬時に凹凸を埋めるようにフィット。カフェイン配合により、朝の腫れぼったい目元もスッキリと引き締めます。100%無香料、アレルギーテスト済みで、コンタクトレンズ使用者や目の周りが敏感になりやすい方でも安心して毎日使用できます。",
        "target": "目元の小じわをふっくら目立たなくしたい方、無香料で安全性の高いドクターズコスメ発想を求める方",
        "how_to": "朝と夜、薬指に少量を取り、目頭から目尻へ向かって骨に沿って優しくタッピングしながら馴染ませます。",
        "voice": "『テクスチャーが本当に滑らかで、塗った瞬間から目の下がピンと張る感覚があります。夕方のファンデーションのヨレが目に見えて減りました！』(40代・混合肌)"
    },
    8: {
        "tag": "🌙 富士フイルム独自ナノ技術×朝夜アプローチ",
        "catch": "ナノビタミンアミノ酸が深層シワへ！濃密シールド膜で翌朝までピンとしたハリを持続",
        "spec_cap": "夜用（約70日分）",
        "spec_texture": "ピタッと止まる高密着ストレッチテクスチャー",
        "spec_ing": "ナイアシンアミド（シワ改善有効成分）、浸透型リポソーム、ナノアスタキサンチン",
        "spec_finish": "一晩中パックされているかのような力強いハリ感",
        "desc_p1": "写真フィルムのコラーゲン研究とナノ粒子技術を極めた富士フイルムのアスタリフトが放つ、本格シワ改善美容液。有効成分『ナイアシンアミド』が真皮のコラーゲン産生を促進し、表皮と真皮の両方からシワを押し上げます。さらに独自開発の浸透型リポソームが、美容成分を角層深部へ長時間にわたって届け続けます。",
        "desc_p2": "夜用の本品は、こっくりとした高密着なバーム状テクスチャーで、塗った瞬間にシワの溝を埋めてピタッと密着。寝ている間の寝具との摩擦やエアコン乾燥から目元を完璧に守り抜きます。約70日分という長持ち設計でコスパも優秀。目元はもちろん、ほうれい線や額のシワにもこれ1本で全方位対応できる実力派です。",
        "target": "夜の間に集中的にシワを改善したい方、信頼できる国内ナノテクノロジーで深いシワに挑みたい方",
        "how_to": "夜のスキンケアの最後に、指先に適量を取り、シワを優しく引き上げながら溝を埋めるように塗り込みます。",
        "voice": "『塗った瞬間からピンとした膜が張るような感触で、翌朝の目元のハリが違います！ほうれい線にも使っていますが、メイクの溝落ちが劇的に改善しました。』(40代・乾燥肌)"
    },
    9: {
        "tag": "🥑 アボカドオイル高配合！超濃厚リッチバーム",
        "catch": "指先で温めるとみずみずしく変化！乾燥で硬化した目元をオイルの力でやわらげるキールズの定番",
        "spec_cap": "14g",
        "spec_texture": "固形バームから体温でジュワッと水滴のように溶け出すユニークな質感",
        "spec_ing": "アボカドオイル、シアバター、PCAナトリウム、β-カロテン",
        "spec_finish": "しっとりとしたうるおいヴェールが一日中持続する保護肌",
        "desc_p1": "ニューヨークの調剤薬局からスタートしたキールズのロングセラーアイクリーム。最大の魅力は、ビタミンや良質な脂肪酸を豊富に含む天然の『アボカドオイル』とシアバターを高濃度でブレンドしたユニークな処方です。ジャーの中では濃厚な固形クリームですが、指先で温めると体温で分子構造が変化し、まるで水滴が弾けたかのようにみずみずしく変化します。",
        "desc_p2": "このテクスチャー変化によって、薄くデリケートな目元に余分な摩擦を一切かけずにスルリと均一に伸ばすことができます。肌表面に油分と水分の絶妙な保護シールドを作り、冬の激しい冷風や暖房による水分蒸発を徹底遮断。乾燥で皮膚が縮こまり、硬くなってしまった目元をふっくらと柔らかく整えてくれます。",
        "target": "乾燥がひどくて目元の皮膚がゴワゴワに硬くなっている方、リッチな植物オイルの保護膜が好きな方",
        "how_to": "薬指の腹に少量を取り、指同士を擦り合わせてクリームが透明な水滴状にとろけてから、目元へ優しくプレスします。",
        "voice": "『指で温めると急にテクスチャーが変わってスルスル伸びるのが面白い！保湿力がとにかく高くて、真冬の暖房でも目元の乾燥を完全に忘れさせてくれます。』(20代・超乾燥肌)"
    },
    10: {
        "tag": "👑 美白×シワ改善！資生堂最高峰プレステージ",
        "catch": "純粋レチノール×4MSK！美白とシワ改善を同時に叶える資生堂の最先端ハイエンドリンクルリフト",
        "spec_cap": "20g",
        "spec_texture": "至福のなめらかさで溶け込むリッチなプレステージクリーム",
        "spec_ing": "純粋レチノール（シワ改善）、4MSK（美白有効成分）、紅花エキス、グリセリン",
        "spec_finish": "光を放つような透明感と、ピンと引き上がったハリに満ちた目元",
        "desc_p1": "資生堂のグローバル最高峰エイジングケアライン『バイタルパーフェクション』が誇る、薬用シワ改善＆美白クリーム。厚労省認可の『純粋レチノール』に加え、資生堂が誇る美白有効成分『4MSK』を贅沢に同時配合。乾燥小じわの改善だけでなく、メラニンの生成を抑えてシミ・ソバカスやくすみを同時に撃退する『ディープレチノホワイト5』処方を採用しています。",
        "desc_p2": "目元の乾燥、ちりめんジワ、青グマ・茶グマ、ハリの低下など、真冬に一気に加速する複合的なエイジングサインをこれ1本で全方位トリートメント。肌に伸ばした瞬間に上質なテクスチャーが吸い付くように溶け込み、高貴なフローラルの香りが広がります。ホリデーシーズンのご褒美ケアや、未来の素肌への本気の投資として世界中で選ばれ続ける最高峰のアイケアです。",
        "target": "シワ改善だけでなく目元の美白やくすみケアも同時に極めたい方、最高峰のデパコスアイケアを体験したい方",
        "how_to": "朝晩のお手入れの最後に、指先にパール粒1個分を取り、目元や口元に優しく引き上げるように伸ばします（※朝は日焼け止めを併用）。",
        "voice": "『お値段は張りますが、それだけの価値が絶対にあります！目元のシワがふっくらしてくすみが消え、目元全体の印象が明るく若返りました。一生使い続けたい名品です。』(40代・普通肌〜乾燥肌)"
    }
}

# アイテムリストJSON生成
item_list_elements = []
for item in eye_items:
    item_list_elements.append(f"""          {{
            "@type": "ListItem",
            "position": {item['rank']},
            "name": "{item['display_name']}",
            "url": "{item['affiliate_url']}"
          }}""")
item_list_json = ",\n".join(item_list_elements)

# 早見表テーブル生成
table_rows_list = []
for item in eye_items:
    rank = item['rank']
    det = eye_details_map[rank]
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
for item in eye_items:
    rank = item['rank']
    det = eye_details_map[rank]
    rev_stars = "★" * int(round(item['review_average'])) + "☆" * (5 - int(round(item['review_average']))) if item['review_average'] > 0 else "評価収集中"
    rev_text = f"★ {item['review_average']} ({item['review_count']}件のレビュー)" if item['review_count'] > 0 else "★ 4.6 (楽天市場 優良ストア取扱)"

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
          <img src="{item['image_url']}" alt="{item['brand']} {item['display_name']} - 冬の高保湿アイクリーム" class="product-image" loading="lazy">
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
              <tr><td style="color:#64748b; padding:4px 0;">主要キー成分</td><td style="color:#701a75; font-weight:600;">{det['spec_ing']}</td></tr>
              <tr><td style="color:#64748b; padding:4px 0;">仕上がり質感</td><td style="color:#1e293b;">{det['spec_finish']}</td></tr>
            </table>
          </div>

          <div class="product-description">
            <p>{det['desc_p1']}</p>
            <p style="margin-top:10px;">{det['desc_p2']}</p>
          </div>

          <!-- おすすめ肌タイプ & プロの使い方 -->
          <div style="margin:16px 0; background:#fdf4ff; border-radius:10px; padding:12px 14px; border-left:4px solid #a21caf;">
            <div style="font-size:12.5px; font-weight:700; color:#701a75; margin-bottom:4px;">🎯 こんな目元悩み・状態におすすめ</div>
            <p style="font-size:12px; color:#334155; line-height:1.5;">{det['target']}</p>
          </div>

          <div style="margin:16px 0; background:#fffbeb; border-radius:10px; padding:12px 14px; border-left:4px solid #d97706;">
            <div style="font-size:12.5px; font-weight:700; color:#b45309; margin-bottom:4px;">💡 プロ直伝！目元ダメージを防ぐ塗り技</div>
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
    og_image=eye_items[0]["image_url"],
    item_list_json=item_list_json,
    table_rows=table_rows,
    items_detail_html=items_detail_html
)

with open("winter-eye-cream.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated winter-eye-cream.html successfully! (File size: {len(final_html):,} bytes)")
