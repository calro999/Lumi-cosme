import os
import re

with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

fl_match = re.search(r'<div class="footer-links">.*?</div>', idx_content, re.DOTALL)
footer_links_html = fl_match.group(0)

unified_footer = f"""  <!-- フッター -->
  <footer class="site-footer">
    {footer_links_html}
    <p class="copyright">© 2026 Lumi Cosme (ルミコスメ) All Rights Reserved.</p>
  </footer>"""

html_files = [f for f in os.listdir(".") if f.endswith(".html")]

for fn in sorted(html_files):
    if fn == "index.html":
        continue
    with open(fn, "r", encoding="utf-8") as f:
        c = f.read()

    # フッターの置換
    new_c = re.sub(r'<!-- (?:サイト共通)?フッター -->\s*<footer class="site-footer">.*?</footer>', unified_footer, c, flags=re.DOTALL)
    if new_c == c:
        # コメントなしパターン
        new_c = re.sub(r'<footer class="site-footer">.*?</footer>', unified_footer, c, flags=re.DOTALL)

    if new_c != c:
        with open(fn, "w", encoding="utf-8") as f:
            f.write(new_c)
        print(f"✓ Unified footer in {fn}")
    else:
        print(f"! Failed to replace footer in {fn}")

print("Footer unification finished.")
