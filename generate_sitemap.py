from update_all_internal_links import ALL_ARTICLES

sitemap_header = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://lumi-cosme.vercel.app/</loc>
    <lastmod>2026-11-02</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
"""

url_blocks = []
for idx, a in enumerate(ALL_ARTICLES):
    priority = "0.95" if idx < 3 else ("0.9" if idx < 15 else "0.8")
    url_blocks.append(f"""  <url>
    <loc>https://lumi-cosme.vercel.app{a['url']}</loc>
    <lastmod>2026-11-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_footer = "</urlset>\n"

sitemap_content = sitemap_header + "\n".join(url_blocks) + "\n" + sitemap_footer

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"Successfully generated sitemap.xml with {len(ALL_ARTICLES)+1} URLs!")
