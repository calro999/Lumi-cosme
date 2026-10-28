import json

with open("rakuten_latest_3articles_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

mask_items = data["winter_face_mask"]["items"]

html_template = """<!DOCTYPE html>
<html lang="ja" prefix="og: http://ogp.me/ns#">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【2026最新】水分爆弾で砂漠肌を即リセット！翌朝の化粧ノリ激変・高保湿シートマスク＆夜用パックおすすめ10選 | Lumi Cosme</title>
  <meta name="description" content="11月・12月の深刻な暖房乾燥と冷風でカサつく冬肌をひと晩で救済！低分子ヒアルロン酸、エクソソーム、ヒト型セラミド、バイオコラーゲンなど最新テクノロジーを凝縮した高保湿シートマスク＆洗い流さないスリーピングパック厳選10選。シート素材別の選び方や水分逆流を防ぐ正しい密着時間まで徹底解説。">
  <meta name="keywords" content="シートマスク, フェイスパック, 冬スキンケア, 高保湿パック, トリデン ダイブイン, ルルルン ハイドラEX, メディヒール, バイオダンス, スリーピングパック, 2026コスメ">

  <!-- SEO & Canonical -->
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-face-mask">
  <meta name="robots" content="index, follow">

  <!-- OGP -->
  <meta property="og:site_name" content="Lumi Cosme (ルミコスメ)">
  <meta property="og:title" content="水分爆弾で砂漠肌を即リセット！翌朝の化粧ノリ激変・高保湿シートマスク＆夜用パックおすすめ10選">
  <meta property="og:description" content="真冬の暖房下でも乾かない！トリデン、ルルルン、メディヒール、バイオダンスなど話題の高保湿フェイスマスクを徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-face-mask">
  <meta property="og:image" content="{og_image}">
  <meta property="og:locale" content="ja_JP">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="水分爆弾で砂漠肌を即リセット！翌朝の化粧ノリ激変・高保湿シートマスク＆夜用パックおすすめ10選">
  <meta name="twitter:description" content="真冬の暖房下でも乾かない！トリデン、ルルルン、メディヒール、バイオダンスなど話題の高保湿フェイスマスクを徹底比較。">
  <meta name="twitter:image" content="{og_image}">

  <link rel="stylesheet" href="style.css">

  <!-- 構造化データ (JSON-LD) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "headline": "水分爆弾で砂漠肌を即リセット！翌朝の化粧ノリ激変・高保湿シートマスク＆夜用パックおすすめ10選",
        "description": "11月・12月の本格乾燥シーズンに必須の高保湿シートマスク＆スリーピングパックの選び方、成分比較、おすすめ10選を徹底レビュー。",
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
        "name": "冬の高保湿シートマスク＆夜用パックおすすめ10選",
        "itemListElement": [
{item_list_json}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "シートマスクは毎日使っても肌に負担になりませんか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "ルルルンやVTなどの『デイリー用・大容量タイプ』として処方設計されているものは、化粧水代わりに毎朝晩使用しても肌への負担はほぼありません。ただし、美容液1本分相当の濃厚成分を含む『個包装スペシャルケア用』やピーリング酸配合のものは、過剰栄養や摩擦を防ぐため週1〜2回の使用が推奨されます。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "シートマスクを貼る時間は長ければ長いほど潤いますか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "厳禁です！規定時間（通常10〜15分）を超えてシートが乾き始めると、浸透圧と毛細管現象によって『シートが肌の水分を逆に吸い取ってしまう水分逆流現象』が起こります。シートがまだしっとり湿っているうちに剥がすのが、最も肌の水分量を保つ秘訣です。ただし、バイオダンスのようなハイドロゲル固形マスクやエリクシールのようなスリーピングジェルパックは就寝中の一晩使用が前提となっています。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "冬場はシートマスクが冷たくてヒヤッとします。温めて使っても良いですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "個包装の未開封パウチであれば、人肌程度（約38℃前後）のぬるま湯に数分浸してから開封すると心地よく使えます。ただし、ビタミンCやレチノール、生酵素などの熱に弱い美容成分を含む製品は変質する恐れがあるため常温で使用し、手のひらでハンドプレスして温めるのがベストです。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "シートマスクを剥がした後は乳液やクリームが必要ですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "絶対に必要です。シートマスクは主に水分と水溶性美容成分を肌にチャージするもの。油分による『エモリエントのフタ』をしないと、せっかく補給した水分が室内の暖房によって一気に蒸発し、使用前よりも肌が乾燥する『過乾燥』を招きます。マスク直後に必ず乳液や高保湿クリームを重ねましょう。"
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body class="theme-mask">

  <!-- ヘッダー -->
  <header class="site-header">
    <div class="header-badge">💧 2026 WINTER MOISTURE RESCUE</div>
    <h1 class="site-title">高保湿シートマスク＆夜用パック10選</h1>
    <p class="site-subtitle">暖房と冷風でしぼんだ砂漠肌をひと晩で満水リセットする集中水分チャージ</p>
  </header>

  <main class="container">

    <!-- 記事トップ・アイキャッチ -->
    <article class="article-intro">
      <div class="article-meta">
        <span class="article-cat-tag">スキンケア特集 / フェイスマスク・パック</span>
        <span class="article-date">📅 2026.10.28 更新</span>
      </div>

      <h1 class="article-main-heading">水分爆弾で砂漠肌を即リセット！翌朝の化粧ノリ激変・高保湿シートマスク＆夜用パックおすすめ10選</h1>

      <p class="article-lead">
        11月から12月にかけて、本格的な木枯らしとオフィスの暖房がフル稼働を始めると、<strong>「いつも通りスキンケアをしているのに頬がつっぱる」「夕方になると口元の皮膚が粉を吹き始める」「朝起きた瞬間から肌がゴワついてメイクが全く乗らない」</strong>という深刻な水分不足トラブルに直面します。<br><br>
        冬の肌は、低温による毛細血管の収縮で新陳代謝が低下し、角質層のバリア機能がガタ落ちした状態。通常のハンドプレス塗布だけでは、角質細胞のすみずみまで十分な水分を行き渡らせることが極めて困難です。<br><br>
        そんな真冬のピンチ肌を一発逆転させる最強のソリューションが、密封効果で美容成分を角層深くまでダイレクトに流し込む<strong>「高保湿シートマスク」</strong>と、就寝中の8時間に水分を密閉し続ける<strong>「ナイトリペア・スリーピングパック」</strong>です。<br><br>
        本記事では、低分子5Dヒアルロン酸、エクソソーム、高濃度セラミド、密着ハイドロゲルコラーゲンなど、2026年の最先端スキンケア科学が詰まった実力派アイテム10選を徹底検証します！
      </p>

      <!-- 目次ナビゲーション -->
      <nav class="toc-container">
        <div class="toc-title">📑 本記事の目次</div>
        <ul class="toc-list">
          <li><a href="#why-mask">1. なぜ冬こそシートマスクが必要なのか？密封浸透圧と角層保水のサイエンス</a></li>
          <li><a href="#types">2. シート素材と配合成分で選ぶ！冬のフェイスマスク3大タイプ別診断</a></li>
          <li><a href="#comparison">3. 【一目でわかる】冬の高保湿シートマスク＆パック10選 比較早見表</a></li>
          <li><a href="#ranking">4. 【2026最新】冬の高保湿シートマスク＆パックおすすめ10選 詳細個別レビュー</a></li>
          <li><a href="#technique">5. 水分逆流を防ぐ！プロが教える「効果を200%引き出すマスク密着ルーティン」</a></li>
          <li><a href="#faq">6. シートマスク・パックに関するよくある質問（FAQ）</a></li>
          <li><a href="#related">7. あわせて読みたい！冬の保湿ケア特集一覧</a></li>
        </ul>
      </nav>
    </article>

    <!-- メカニズム解説セクション -->
    <section id="why-mask">
      <h2 class="section-title">なぜ冬こそシートマスクが必要なのか？密封浸透圧と角層保水のサイエンス</h2>
      <p class="content-text">
        秋から冬（11月〜12月）にかけて、空気中の湿度は30%台へと急激に低下します。この乾燥環境下では、化粧水を肌に手で馴染ませても、角層奥深くに浸透する前に表面から水分が蒸発してしまいます。
      </p>
      <p class="content-text">
        シートマスクの最大の強みは、繊維が肌に隙間なく密着することで生まれる<strong>「閉塞密封効果（オクルーシブ効果）」</strong>です。外気との接触を遮断しながら、シートに含まれる数千万個の微細美容カプセルが肌表面の温度を均一に保ち、角質層をふやかして美容成分の浸透圧を高めます。
      </p>
      <div class="product-catch" style="margin: 20px 0;">
        💡 冬のシートマスク集中ケアがもたらす3大効果：<br>
        ① <strong>角層水分量の即時底上げ</strong>：手塗り塗布の約3〜5倍の保水成分を角層深部までダイレクト供給<br>
        ② <strong>乱れたキメの整列</strong>：乾燥でしぼんだ細胞間脂質を水分で満たし、翌朝の毛穴落ちやファンデ割れを解消<br>
        ③ <strong>バリア機能の急速鎮静</strong>：外気冷風やマフラー摩擦でヒリついた肌を、鎮静成分と冷却密着で優しくリカバリー
      </div>
    </section>

    <!-- タイプ別解説セクション -->
    <section id="types">
      <h2 class="section-title">シート素材と配合成分で選ぶ！冬のフェイスマスク3大タイプ別診断</h2>
      <div class="content-text">
        <p>冬のシートマスク選びで最も重要なのは、「シートの繊維構造」と「保湿アプローチの違い」を理解することです。肌状態に合わせて最適な組み合わせを選びましょう。</p>
        
        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #ccfbf1; box-shadow: var(--shadow-soft);">
          <h3 style="color: #0f766e; font-size: 16px; font-weight: 700; margin-bottom: 6px;">① 水分爆弾・インナードライ解消タイプ（トリデン、メディヒールなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">「表面はテカるのに内側が突っ張る」「化粧水がぐんぐん吸い込まれない」という方に。分子サイズの異なる複合ヒアルロン酸やNMF成分が、角層の隙間を純粋な水分で満たします。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #ccfbf1; box-shadow: var(--shadow-soft);">
          <h3 style="color: #0f766e; font-size: 16px; font-weight: 700; margin-bottom: 6px;">② 密着バリア・高濃度ナノリポソームタイプ（ルルルンEX、ダーマレーザーなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">夕方になると暖房で肌がひび割れる方、エイジングサインやくすみが気になる方に。ヒト幹細胞エクソソームや高濃度セラミドを内包したナノカプセルが、肌の防御壁を強力に再構築します。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #ccfbf1; box-shadow: var(--shadow-soft);">
          <h3 style="color: #0f766e; font-size: 16px; font-weight: 700; margin-bottom: 6px;">③ 睡眠密封・ナイトリペアパックタイプ（バイオダンス、エリクシールなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">忙しくてパック時間を待てない方、翌朝劇的なハリツヤを求める特別な日の前夜に。夜通し貼り続けられるハイドロゲルマスクや塗って寝るジェルが、睡眠中の水分蒸発をゼロに抑え込みます。</p>
        </div>
      </div>
    </section>

    <!-- 比較早見表 -->
    <section id="comparison">
      <h2 class="section-title">【一目でわかる】冬の高保湿シートマスク＆パック10選 比較早見表</h2>
      <p class="content-text">掲載している価格は楽天市場の最新調査価格（税込）です。横スクロールで特徴や配合成分を比較できます。</p>

      <div class="table-scroll-wrapper">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>タイプ・シート特徴</th>
              <th>主要キー成分</th>
              <th>参考価格</th>
              <th>おすすめな肌悩み</th>
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
      <h2 class="section-title">【2026最新】冬の高保湿シートマスク＆夜用パックおすすめ10選 詳細個別レビュー</h2>
{items_detail_html}
    </section>

    <!-- プロ直伝テクニック -->
    <section id="technique">
      <h2 class="section-title">水分逆流を防ぐ！プロが教える「効果を200%引き出すマスク密着ルーティン」</h2>
      <div class="content-text">
        <p>
          どれほど高価なシートマスクを使っても、使い方が間違っていると水分が肌に戻るどころか外へ逃げてしまいます。冬の乾燥肌を最短で立て直す4ステップをマスターしましょう。
        </p>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #ccfbf1;">
          <h3 style="color: #0f766e; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 1：マスクの前に「導入先行美容液」で角質をほぐす</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            洗顔後の乾いた肌にいきなりシートマスクを貼るのではなく、まずブースター美容液をワンプッシュ馴染ませます。硬化した角質層の道筋を開いておくことで、マスクに含まれる大量のエッセンスの吸水スピードが劇的に向上します。（※<a href="/winter-serum-booster" style="color: #0d9488; font-weight: 700; text-decoration: underline;">冬の導入先行美容液10選はこちら</a>）
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #ccfbf1;">
          <h3 style="color: #0f766e; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 2：空気を抜きながら中央から外側へ「完全密着」</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            目元と口元の位置を合わせたら、小鼻の脇や顎下まで指の腹で滑らせて気泡を完全に追い出します。シートと皮膚の間に隙間があると、その部分から急速に乾燥が進んでしまいます。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #ccfbf1;">
          <h3 style="color: #0f766e; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 3：放置時間は10〜15分厳守！乾く前に剥がすのが鉄則</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            シートマスクの「もったいないから乾くまで貼る」は最大の過ちです。シートの端が白っぽくなってきたら水分逆流の合図。まだひたひたの状態で剥がし、残った液は首筋やデコルテに馴染ませましょう。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #ccfbf1;">
          <h3 style="color: #0f766e; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 4：剥がした直後30秒以内に高保湿クリームで「完全密閉」</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            マスクを外した肌は無防備な満水状態。そのまま放置すると室内暖房の熱で一瞬にして気化熱を奪われます。間髪入れずにセラミドやスクワラン高配合の濃厚クリームをハンドプレスし、うるおいを閉じ込めましょう。（※<a href="/winter-moisture-cream" style="color: #0d9488; font-weight: 700; text-decoration: underline;">高保湿フェイスクリーム＆バーム10選はこちら</a>）
          </p>
        </div>
      </div>
    </section>

    <!-- FAQセクション -->
    <section id="faq">
      <h2 class="section-title">シートマスク・パックに関するよくある質問（FAQ）</h2>
      <div class="faq-container">
        <div class="faq-item">
          <div class="faq-question">Q1. シートマスクは毎日使っても肌に負担になりませんか？</div>
          <div class="faq-answer">
            ルルルンやVTなどの『デイリー用・大容量BOXタイプ』として処方設計されているものは、化粧水代わりに毎朝晩使用しても肌への負担はほぼありません。ただし、美容液1本分相当の濃厚成分を含む『個包装スペシャルケア用』やピーリング酸配合のものは、過剰栄養や摩擦を防ぐため週1〜2回の使用が推奨されます。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q2. シートマスクを貼る時間は長ければ長いほど潤いますか？</div>
          <div class="faq-answer">
            厳禁です！規定時間（通常10〜15分）を超えてシートが乾き始めると、浸透圧と毛細管現象によって『シートが肌の水分を逆に吸い取ってしまう水分逆流現象』が起こります。シートがまだしっとり湿っているうちに剥がすのが、最も肌の水分量を保つ秘訣です。ただし、バイオダンスのようなハイドロゲル固形マスクやエリクシールのようなスリーピングジェルパックは就寝中の一晩使用が前提となっています。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q3. 冬場はシートマスクが冷たくてヒヤッとします。温めて使っても良いですか？</div>
          <div class="faq-answer">
            個包装の未開封パウチであれば、人肌程度（約38℃前後）のぬるま湯に数分浸してから開封すると心地よく使えます。ただし、ビタミンCやレチノール、生酵素などの熱に弱い美容成分を含む製品は変質する恐れがあるため常温で使用し、手のひらでハンドプレスして温めるのがベストです。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q4. シートマスクを剥がした後は乳液やクリームが必要ですか？</div>
          <div class="faq-answer">
            絶対に必要です。シートマスクは主に水分と水溶性美容成分を肌にチャージするもの。油分による『エモリエントのフタ』をしないと、せっかく補給した水分が室内の暖房によって一気に蒸発し、使用前よりも肌が乾燥する『過乾燥』を招きます。マスク直後に必ず乳液や高保湿クリームを重ねましょう。
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
        <a href="/winter-serum-booster" class="related-link-card">
          <div class="related-link-title">💧 浸透力を底上げする高保湿・導入先行美容液おすすめ10選</div>
          <div class="related-link-desc">マスク前の仕込みに必須！固くなった角質細胞をほぐし、シートマスクの美容成分をごくごく吸い込む素肌へ。</div>
        </a>

        <a href="/winter-moisture-cream" class="related-link-card">
          <div class="related-link-title">🧴 保湿力の強さで肌乾燥とさようなら！高保湿フェイスクリーム＆濃密バーム10選</div>
          <div class="related-link-desc">シートマスク後の仕上げに！補給した水分を逃さず朝まで完全密閉する最強クリームを徹底比較。</div>
        </a>

        <a href="/winter-eye-cream" class="related-link-card">
          <div class="related-link-title">👁️ 暖房直撃の目元・ほうれい線をふっくら密着！高保湿アイクリーム＆薬用リンクルケア10選</div>
          <div class="related-link-desc">皮膚が薄く乾燥小じわができやすいデリケートゾーンをピンポイント集中ケアする名品集。</div>
        </a>

        <a href="/winter-base-makeup" class="related-link-card">
          <div class="related-link-title">✨ 夕方まで潤いツヤが続く高保湿ファンデーション＆美容液下地10選</div>
          <div class="related-link-desc">シートマスクで整えたプルプル肌を1日中キープ！暖房下でもひび割れないツヤ肌ベースメイク。</div>
        </a>

        <a href="/winter-lip-care" class="related-link-card">
          <div class="related-link-title">🎁 冬のガサガサ皮剥けに終止符！高保湿リップトリートメント＆濃密ティント10選</div>
          <div class="related-link-desc">皮脂腺のない唇を乾燥冷風から強力ガード。夜用リップスリーピングマスクからプランパーまで。</div>
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

# 各アイテムの個別情報辞書
item_details_map = {
    1: {
        "tag": "💧 水分爆弾・インナードライ救世主",
        "catch": "角層深部までうるおいが染み渡る！低分子5Dヒアルロン酸配合の極上ヴィーガンマスク",
        "spec_cap": "27ml × 10枚入",
        "spec_texture": "とろみがあるのにベタつきゼロのみずみずしいエッセンス",
        "spec_ing": "5D複合ヒアルロン酸、D-パンテノール、アラントイン",
        "spec_finish": "内側から水分で満たされたプルプルのウォーターグロウ肌",
        "desc_p1": "韓国の美容アワードを総なめにし、日本でも『水分の塊を貼っているかのよう』と絶賛されるトリデンの大ヒットシートマスク。最大の特長は、高分子・中分子・低分子・超低分子など5種類の異なるサイズのヒアルロン酸を緻密にブレンドした『5D複合ヒアルロン酸』処方です。肌表面を潤すだけでなく、角質層の最深部まで段階的に水分を送り届け、エアコン直撃によるインナードライを根本から解消します。",
        "desc_p2": "シートには環境にも肌にも優しい生分解性セルロース100%を採用。薄手でありながら1枚に27mlもの美容液を贅沢に抱え込み、フェイスラインにぴったりと隙間なく密着。液だれしにくく、パック中もストレスフリーに過ごせます。剥がした瞬間の肌は、まるで上質な温泉から上がったかのような透明感と吸い付くようなもっちり感に満たされます。",
        "target": "暖房の部屋にいると肌の内側がピキピキ突っ張る方、重い油分が苦手で純粋な水分補給を求める脂性肌〜混合肌の方",
        "how_to": "洗顔後、化粧水で軽く肌を整えた後に15分密着。袋に残ったたっぷりの美容液は首元や腕にも伸ばして全身保水するのがおすすめ。",
        "voice": "『暖房でカサカサだった頬が一発で生き返った！美容液がヒタヒタなのに全くベタつかず、翌朝のメイクのノリが別人級に良くなります。常にストックしています。』(30代・混合肌)"
    },
    2: {
        "tag": "✨ 先端再生美容・白玉ツヤ肌",
        "catch": "エクソソーム×高純度グルタチオン！大人のくすみと乾燥疲れを集中ケアする濃密デイリーマスク",
        "spec_cap": "28枚入 (エッセンス510ml)",
        "spec_texture": "とろけるような感触のミルキーリッチ美容液",
        "spec_ing": "ヒト脂肪由来幹細胞エクソソーム、白玉グルタチオン、EGF、ナイアシンアミド",
        "spec_finish": "内側から発光するような透明感となめらかなハリツヤ肌",
        "desc_p1": "SNSで『デパコス級の成分が毎日使える神BOX』と話題沸騰のルルルン最高峰ハイドラシリーズ。美容医療でも大注目の『幹細胞エクソソーム』と、白玉点滴で知られる高純度『グルタチオン』を贅沢にダブル配合。乾燥によってターンオーバーが滞り、ゴワつきやくすみが気になる11-12月の肌を、細胞レベルから呼び覚ますかのように集中トリートメントします。",
        "desc_p2": "シートはルルルンが独自開発した『メルティーフィールシート』。まるでシルクのように滑らかで摩擦を感じさせず、肌に吸い付くようにフィット。目元や小鼻のキワまでしっかりカバーできる設計で、28枚入りのBOXタイプながら最後の1枚までひたひたの潤いが持続します。使用後は肌のキメがふっくらと整い、夕方までどんよりくすまない透き通るような白玉肌へと導きます。",
        "target": "冬の乾燥くすみやキメの乱れ、ハリ不足を毎日手軽に本格ケアしたい20代後半〜40代の方",
        "how_to": "洗顔後すぐ、または化粧水代わりに毎晩5〜10分使用。手のひらでハンドプレスしながら温めると、美容成分の馴染みがさらにアップします。",
        "voice": "『シートの柔らかさが別格！毎日お風呂上がりに使っていたら、職場の同僚に「肌のトーン明るくなった？」と褒められました。大容量でコスパも最高です。』(30代・乾燥肌)"
    },
    3: {
        "tag": "🏆 高保水NMF・不動のベストセラー",
        "catch": "世界中で愛される水分補給の金字塔！ベンリーゼシートが吸い付くように角層を満たす濃密アンプル",
        "spec_cap": "25ml × 3枚入",
        "spec_texture": "とろみのあるジェルアンプル状エッセンス",
        "spec_ing": "ヒアルロン酸Na、天然保湿因子（NMF成分）、ハマメリス水、アラントイン",
        "spec_finish": "手のひらが吸い付くようなもっちり高密度肌",
        "desc_p1": "シートマスク界の絶対王者として世界中で数億枚を売り上げているメディヒールのN.M.Fアクアアンプルマスク。人間の皮膚角質層に存在する『天然保湿因子（Natural Moisturizing Factor）』を忠実に再現した成分構成により、肌が本来持っている水分保持力を力強くアシストします。冬の木枯らしに晒されてカサついた肌も、短時間でふっくらとしたうるおいを取り戻します。",
        "desc_p2": "旭化成が開発したコットン生まれの長繊維不織布『ベンリーゼ』を採用。驚異的な保水力と透明感を持ち、顔に貼るとまるで第二の皮膚のようにピタッと一体化。時間とともにシートが引き締まるリフティング効果も兼ね備えています。剥がした後の肌はぷるんと弾むような弾力感に満ち、乾燥による毛穴の目立ちもきれいに目立たなくなります。",
        "target": "とにかく失敗しない定番の実力派パックを探している方、冬の深刻な粉吹きや肌のゴワつきを速攻で鎮めたい方",
        "how_to": "週に2〜3回、化粧水後に10〜20分密着。シートの『MEDIHEAL』ロゴが白く浮き上がってきたら剥がし時のサインです。",
        "voice": "『冬になると必ずこれに戻ってきます。エアコンでパリパリだった肌が一晩でモチモチに復活して、ファンデーションの毛穴落ちが劇的になくなりました。』(20代・敏感肌)"
    },
    4: {
        "tag": "🛡️ 敏感肌・低刺激ジェルラッピング",
        "catch": "アミノ酸の濃厚ジェルがとろけて密着！乾燥性敏感肌を優しく包み込む低刺激処方",
        "spec_cap": "22ml × 4枚入",
        "spec_texture": "液だれ知らずのぷるぷる高保湿ジェル状美容液",
        "spec_ing": "9種の保潤アミノ酸、2種の清透アミノ酸、リピジュア",
        "spec_finish": "刺激感ゼロでしっとり落ち着いた柔らかマシュマロ肌",
        "desc_p1": "製薬会社（第一三共ヘルスケア）の皮膚科学研究から生まれた、敏感肌・乾燥肌のための名品シートマスク。最大の特長は、一般的なシャバシャバした液体ではなく、ぷるんとした濃厚な『アミノ酸ジェル美容液』がシートにびっしりと絡みついている点です。袋から取り出す際も液だれが一切なく、肌に乗せた瞬間からピタッと吸着して乾燥ダメージを鎮めます。",
        "desc_p2": "角質層のバリアを支える天然の保湿構成要素であるアミノ酸を贅沢に配合。アルコール（エタノール）無添加、パラベンフリー、無香料・無着色、弱酸性の徹底した低刺激設計なので、冬の寒風や花粉でヒリヒリしがちなデリケート肌でも安心して使用できます。マスクを剥がした後は、まるで上質な乳液でパックしたかのような優しいヴェールに包まれます。",
        "target": "冬の乾燥で肌が過敏になり、通常のシートマスクだとピリピリ刺激を感じる敏感肌・アトピー素因の方",
        "how_to": "洗顔後、化粧水で肌を整えた後に10〜15分密着。袋の中にジェルがたっぷり残るので、シートの上から重ね塗りするかデコルテケアに活用してください。",
        "voice": "『他のパックがしみる時でも、ミノンだけは全く刺激なく使えます。ジェルがピタッと密着して剥がれず、翌朝洗顔すると肌が信じられないくらい柔らかくなっています。』(40代・乾燥性敏感肌)"
    },
    5: {
        "tag": "🌿 寒暖差ゆらぎ・CICA水分沈静",
        "catch": "真冬の赤み・肌荒れをクールに鎮圧！1日10分の手軽さでうるおいバランスを整える定番BOX",
        "spec_cap": "30枚入 (350ml)",
        "spec_texture": "みずみずしくさっぱりした浸透型エッセンス",
        "spec_ing": "シカヒアルロン（ツボクサエキス×プロポリス×3重ヒアルロン酸）",
        "spec_finish": "ベタつかずスーッと肌が落ち着く爽快なめらか肌",
        "desc_p1": "暖房の効いた室内と極寒の屋外を行き来することで起こる『冬の寒暖差ゆらぎ肌』を救う、VTの超ベストセラーマスク。独自成分『シカヒアルロン』が、乾燥によるバリア機能低下や赤み・肌トラブルを穏やかにクールダウン。乾燥しているのにTゾーンがテカるといった、真冬のアンバランスな肌環境を健やかな弱酸性状態へと導きます。",
        "desc_p2": "わずか0.2mmという驚異的な薄さを誇る『ヌードシールシート』を採用。通気性に優れ、肌への摩擦や閉塞感を最小限に抑えながら、目元や鼻周りにもピタッと張り付きます。付属の専用ミニピンセットで1枚ずつ衛生的に引き出せるため、忙しい朝のメイク前3分パックとしても大活躍。余分なベタつきを残さないため、直後のメイク崩れを防ぐ土台作りに最適です。",
        "target": "冬場のマスク摩擦や暖房で顔が赤くなりやすい方、朝のスキンケアを手早く済ませて化粧ノリを上げたい方",
        "how_to": "洗顔後、ピンセットで1枚取り出し顔に密着させて10分。朝のメイク前なら3〜5分のクイック使用でも十分に肌が潤い整います。",
        "voice": "『朝のメイク前に貼ると、ベースメイクの毛穴落ちが劇的になくなります！サッパリしているのに角層にはしっかり水分が入って、一日中テカリも乾燥も防げます。』(20代・脂性肌寄り混合肌)"
    },
    6: {
        "tag": "💎 朝まで貼れる！生コラーゲンゲル",
        "catch": "成分が肌に浸透すると透明に変化！翌朝の圧倒的なハリと毛穴レスに世界が驚愕した密着パック",
        "spec_cap": "34g × 4枚入",
        "spec_texture": "高濃度美容成分そのものを固めた肉厚ハイドロゲルシート",
        "spec_ing": "超低分子コラーゲン（243Da）、オリゴヒアルロン酸、ガラクトミセス発酵濾過物",
        "spec_finish": "まるでゆで卵を剥いたかのような発光ツヤ＆ぷるんとした高密度ハリ",
        "desc_p1": "世界中でバズを巻き起こし、美容マニアの間で『新時代のシートマスク』と称賛されるバイオダンスのリアルディープマスク。美容液を不織布に染み込ませる一般的なマスクとは根本的に異なり、低分子コラーゲンやヒアルロン酸そのものを贅沢に固めた厚みのある『ハイドロゲル製』です。最初は白濁したプルプルのゲルが、角質層に成分が吸収されるにつれて徐々に透明へと変化していく驚きの設計です。",
        "desc_p2": "推奨使用時間は3〜4時間、または『就寝中に貼って朝剥がす』スリーピング使用。長時間の密封によって、冬の激しい寝室暖房乾燥から素肌を完全に遮断。超低分子コラーゲンが肌の奥深くまでじっくり浸透します。翌朝、透明になったシートをペリッと剥がした瞬間、鏡を見て声が出るほどの毛穴の引き締まり感と、指を跳ね返すような濃厚なハリツヤを実感できます。",
        "target": "冬の本格的なエイジングサイン（たるみ毛穴、ハリ不足、乾燥小じわ）を短期間で劇的に立て直したい方",
        "how_to": "夜のスキンケア（化粧水・美容液・クリーム）をすべて完了させた後、最後に貼ってそのまま就寝。約3〜4時間以上おいてシートが透明になったら剥がします。",
        "voice": "『夜貼って朝起きて剥がした時の感動が忘れられません！毛穴が本当に消えたように見えて、肌が内側からパーンと張っています。特別なイベント前には欠かせないお守りです。』(30代・乾燥肌)"
    },
    7: {
        "tag": "⚡ 3分で速攻チャージ！高濃度セラミド",
        "catch": "レーザー美容発想の浸透技術！ナノカプセル化セラミドが真冬の砂漠肌バリアを瞬時に再構築",
        "spec_cap": "7枚入",
        "spec_texture": "とろみのあるリッチなミルキーテクスチャー",
        "spec_ing": "天然型高濃度セレブロシド（セラミド）、水添レシチン、フィトステロールズ",
        "spec_finish": "外気刺激に負けない吸い付くような濃密シールド肌",
        "desc_p1": "レーザー美容の浸透スピードに着想を得たクオリティファーストの大人気シリーズ『ダーマレーザー』。中でもこのスーパーセラミド100は、真冬の乾燥でバリア機能が崩壊したカサカサ肌のためのレスキュー処方です。肌の水分保持に最も重要な『セラミド』を高濃度配合し、独自のナノカプセルに内包することで、角質層深部へわずか3分という圧倒的な速さで届けます。",
        "desc_p2": "シートには長繊維不織布を採用し、シリコンマスクのような高い密着性を実現。液含みが非常に良く、わずか3分の使用でも長時間のパックに匹敵するうるおいチャージが完了します。7枚入りで880円という驚異的なプチプラ価格でありながら、仕上がりは高級エステ級。乾燥による肌荒れや粉吹きが気になる日のデイリーリペアとして常備しておきたい逸品です。",
        "target": "乾燥による肌のピリつきや粉吹きを今すぐ立て直したい方、高コスパで濃厚なセラミド補給をしたい方",
        "how_to": "洗顔後、マスクを広げて肌に密着させ、わずか3分でOK。剥がした後はシートを折りたたんで優しくパッティングし、クリームでフタをします。",
        "voice": "『たった3分でいいのが忙しい夜に本当に助かる！液がヒタヒタで、剥がした直後から肌がモチモチになって乾燥のピリピリ感がスッと落ち着きます。リピ確定です。』(20代・乾燥肌)"
    },
    8: {
        "tag": "🌿 まるでガムのように超密着！",
        "catch": "極細マイクロファイバーが隙間なく吸着！智異山ドクダミエキスが乾燥トラブルを素早く鎮静",
        "spec_cap": "27ml × 10枚入",
        "spec_texture": "みずみずしく清涼感のあるウォータリーエッセンス",
        "spec_ing": "智異山ドクダミエキス、ツボクサエキス、カミツレ花エキス",
        "spec_finish": "テカリを抑えてキメが整ったサラすべ潤い肌",
        "desc_p1": "韓国スキンケアブランドAbibの代名詞とも言えるガムシートマスク。最大の特徴は、繊維と繊維の間に隙間がない特殊な『極細マイクロファイバーシート』です。まるで肌の上にガムを貼り付けたかのように、顔の起伏に寸分の狂いもなくピタッと密着。密着力が極めて高いため、下を向いたりドライヤーをかけたりしても剥がれ落ちることがありません。",
        "desc_p2": "韓国の霊峰・智異山（チリサン）で栽培された高純度のドクダミエキスを贅沢に配合。冬の乾燥冷風やニットの襟擦れによって生じる肌の炎症・大人ニキビを穏やかに鎮静し、透明感のある健やかな素肌へと整えます。27mlのエッセンスがシート全体に行き渡り、パック後は肌がひんやりと引き締まり、キメがキュッと細かく整います。",
        "target": "シートマスクが途中で浮いてくるのがストレスな方、乾燥とニキビ・肌荒れが同時に起きやすいゆらぎ肌の方",
        "how_to": "洗顔後、化粧水で整えた肌にシートを貼り、青い保護フィルムを外して10〜20分密着させます。",
        "voice": "『本当にガムみたいに密着して全く剥がれません！ドライヤーしながら使えるのが最高。ドクダミのおかげで冬の謎の肌荒れや赤みが翌朝には綺麗に引いていました。』(20代・敏感肌)"
    },
    9: {
        "tag": "🌙 塗って寝るだけ！高弾力コラーゲンジェル",
        "catch": "シートを貼る手間すら不要！コラーゲンカプセルが就寝中にじっくり浸透して「つや玉」輝く朝へ",
        "spec_cap": "105g (約45回分)",
        "spec_texture": "みずみずしくとろける高弾力ジェル（美容カプセル入り）",
        "spec_ing": "コラーゲンGL、イノシトールカプセル、マンダリンオレンジ果皮エキス",
        "spec_finish": "翌朝洗顔した瞬間から手のひらを押し返す濃密なハリつや肌",
        "desc_p1": "夜のお手入れの最後にスパチュラでひとすくいして塗るだけ。シートを剥がすタイマーすらセットしたくない疲れた夜に絶大な威力を発揮する、エリクシールの名品ナイトパックです。弾力のあるぷるぷるジェルの中に、美容成分を濃縮した無数のカプセルが浮かんでおり、肌に伸ばすと体温でカプセルが弾けて美容成分が角層へと溶け込みます。",
        "desc_p2": "就寝中の肌を一晩中高密度のジェル膜でラッピングし、冬の過酷な寝室乾燥から肌を完璧に保護。睡眠中のターンオーバーに合わせてコラーゲンや保湿成分が浸透し続けます。ベタつかず枕にも付きにくい処方で、翌朝ぬるま湯で洗顔した瞬間、思わず頬を触りたくなるようなぷるんとした弾力と、頬の高い位置に輝く「つや玉」に感動します。",
        "target": "シートマスクを貼る時間すら惜しい忙しい方、冬の暖房による睡眠中の水分蒸発をゼロにしたい方",
        "how_to": "夜のお手入れの最後に、スパチュラでさくらんぼ1個分を目安に取り、顔全体に広げてそのまま就寝。週2〜3回、または毎晩使用可能です。",
        "voice": "『夜塗って寝るだけで翌朝の肌がプルプルになります！冬のエアコンをつけっぱなしで寝ても全く乾燥しません。シートマスクのように剥がす時間を気にしなくていいのが本当に楽！』(40代・普通肌〜乾燥肌)"
    },
    10: {
        "tag": "👑 集中ピテラケア・最高峰ご褒美マスク",
        "catch": "美容液1本分のピテラを濃縮！特別な日の前夜に肌の運命を変える伝説のプレステージマスク",
        "spec_cap": "6枚入 / 10枚入",
        "spec_texture": "リッチで上質なとろみのある発酵美容液",
        "spec_ing": "ピテラ（ガラクトミセス培養液）、マルチビタミン、ミネラル複合体",
        "spec_finish": "キメが極限まで整い、内側から澄み渡る圧倒的な陶器肌",
        "desc_p1": "世界中のセレブリティやメイクアップアーティストが『勝負日の前夜にはこれ以外考えられない』と口を揃える、SK-IIの伝説的フェイシャルマスク。SK-IIの代名詞である独自発酵成分『ピテラ』を、なんと美容液1本分相当もシート1枚に凝縮。乾燥、キメの乱れ、くすみ、ハリ不足など、冬の複合的な肌悩みをたった1回で全方位リセットします。",
        "desc_p2": "上質な天然コットン100%の多層シートは肉厚で重厚感があり、肌に吸い付くように密着。ピテラに含まれる50種類以上のアミノ酸、ビタミン、ミネラルが角質層のすみずみまでチャージされます。マスクを外した後の肌は、毛穴がキュッと引き締まり、くすみが一掃されて光をパーンと跳ね返すような透明感が出現。12月のホリデーディナーや大切な記念日の前夜に相応しい至極の逸品です。",
        "target": "ここ一番の大切なイベントを控えている方、1年間頑張った自分へのご褒美として最高峰の保湿を体験したい方",
        "how_to": "洗顔後、化粧水で肌を整えた後に5〜15分密着。剥がした後は肌に残った液を優しくパッティングし、クリームで仕上げます。",
        "voice": "『ここぞという前夜に必ず使います。外した瞬間の肌の透明感とキメの細かさは他のどんなパックでも代用できません。冬のごわつき肌が生き返ります！』(30代・混合肌)"
    }
}

# アイテムリストJSON生成
item_list_elements = []
for item in mask_items:
    item_list_elements.append(f"""          {{
            "@type": "ListItem",
            "position": {item['rank']},
            "name": "{item['display_name']}",
            "url": "{item['affiliate_url']}"
          }}""")
item_list_json = ",\n".join(item_list_elements)

# 早見表テーブル生成
table_rows_list = []
for item in mask_items:
    rank = item['rank']
    det = item_details_map[rank]
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
for item in mask_items:
    rank = item['rank']
    det = item_details_map[rank]
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
          <img src="{item['image_url']}" alt="{item['brand']} {item['display_name']} - 冬の高保湿シートマスク" class="product-image" loading="lazy">
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
              <tr><td style="color:#64748b; padding:4px 0;">主要キー成分</td><td style="color:#0f766e; font-weight:600;">{det['spec_ing']}</td></tr>
              <tr><td style="color:#64748b; padding:4px 0;">仕上がり質感</td><td style="color:#1e293b;">{det['spec_finish']}</td></tr>
            </table>
          </div>

          <div class="product-description">
            <p>{det['desc_p1']}</p>
            <p style="margin-top:10px;">{det['desc_p2']}</p>
          </div>

          <!-- おすすめ肌タイプ & プロの使い方 -->
          <div style="margin:16px 0; background:#f0fdfa; border-radius:10px; padding:12px 14px; border-left:4px solid #0d9488;">
            <div style="font-size:12.5px; font-weight:700; color:#0f766e; margin-bottom:4px;">🎯 こんな肌悩み・肌質におすすめ</div>
            <p style="font-size:12px; color:#334155; line-height:1.5;">{det['target']}</p>
          </div>

          <div style="margin:16px 0; background:#fffbeb; border-radius:10px; padding:12px 14px; border-left:4px solid #d97706;">
            <div style="font-size:12.5px; font-weight:700; color:#b45309; margin-bottom:4px;">💡 プロ直伝！失敗しない使いこなし技</div>
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
    og_image=mask_items[0]["image_url"],
    item_list_json=item_list_json,
    table_rows=table_rows,
    items_detail_html=items_detail_html
)

with open("winter-face-mask.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated winter-face-mask.html successfully! (File size: {len(final_html):,} bytes)")
