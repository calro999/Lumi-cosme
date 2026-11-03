import glob
import os
import datetime

HOST = "https://lumi-cosme.vercel.app"
today = datetime.date.today().isoformat()

# トップページ
urls = [
    {
        "loc": f"{HOST}/",
        "lastmod": today,
        "priority": "1.0",
        "changefreq": "daily"
    }
]

# 全html記事
html_files = sorted([f for f in glob.glob("*.html") if f != "index.html"])

# 優先度の高い新記事
newest_slugs = [
    "winter-marula-oil", "winter-birch-juice", "winter-azelaic-acid",
    "winter-ectoin", "winter-bakuchiol", "winter-bifida", "winter-proteoglycan", "winter-propolis", "winter-galactomyces",
    "winter-heparinoid", "winter-vaseline", "winter-placenta",
    "winter-rice-power", "winter-camellia-oil", "winter-amino-acid",
    "winter-argan-oil", "winter-horse-oil", "winter-panthenol-cream",
    "winter-shea-butter", "winter-jojoba-oil", "winter-urea-cream",
    "winter-ceramide-lotion", "winter-medicinal-lip", "winter-squalane-oil",
    "winter-ceramide-cream", "winter-peptide-serum", "winter-hair-serum",
    "winter-exosome-serum", "winter-bath-milk", "winter-glutathione-serum",
    "winter-pdrn-serum", "winter-collagen-mask", "winter-carbonic-shampoo"
]

for f in html_files:
    slug = f.replace(".html", "")
    prio = "0.9" if slug in newest_slugs else "0.8"
    urls.append({
        "loc": f"{HOST}/{slug}",
        "lastmod": today,
        "priority": prio,
        "changefreq": "weekly"
    })

xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for u in urls:
    xml_content += f"""  <url>
    <loc>{u['loc']}</loc>
    <lastmod>{u['lastmod']}</lastmod>
    <changefreq>{u['changefreq']}</changefreq>
    <priority>{u['priority']}</priority>
  </url>\n"""

xml_content += '</urlset>\n'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)

print(f"Updated sitemap.xml successfully with {len(urls)} URLs!")
