import json
from update_all_internal_links import ALL_ARTICLES

HOST = "lumi-cosme.vercel.app"

# sitemap.xml の作成
sitemap_urls = [
    '  <url>\n    <loc>https://lumi-cosme.vercel.app/</loc>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>\n  </url>'
]
for a in ALL_ARTICLES:
    sitemap_urls.append(f"""  <url>
    <loc>https://{HOST}{a['url']}</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>""")

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>
"""

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)
print("Updated sitemap.xml successfully!")

# submit_indexnow.py の更新
url_list = [f"https://{HOST}/"] + [f"https://{HOST}{a['url']}" for a in ALL_ARTICLES]

indexnow_code = f"""import json
import urllib.request
import urllib.parse
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open("indexnow_key.txt", "r", encoding="utf-8") as f:
    KEY = f.read().strip()

HOST = "{HOST}"
URL_LIST = {json.dumps(url_list, indent=4, ensure_ascii=False)}

payload = {{
    "host": HOST,
    "key": KEY,
    "keyLocation": f"https://{{HOST}}/{{KEY}}.txt",
    "urlList": URL_LIST
}}

data_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")

ENDPOINTS = [
    "api.indexnow.org",
    "www.bing.com",
    "yandex.com",
    "search.seznam.cz"
]

print(f"=== Submitting {{len(URL_LIST)}} URLs to IndexNow (Host: {{HOST}}) ===")
print(f"Key: {{KEY}}")

for endpoint in ENDPOINTS:
    url = f"https://{{endpoint}}/indexnow"
    req = urllib.request.Request(
        url,
        data=data_bytes,
        headers={{
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Mozilla/5.0 (compatible; IndexNowSubmittingBot/1.0)"
        }},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            code = res.getcode()
            body = res.read().decode("utf-8", errors="ignore")
            print(f"✓ {{endpoint}}: HTTP {{code}} {{body if body else '(OK)'}}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        print(f"✓ {{endpoint}}: HTTP {{e.code}} (Response: {{body}})")
    except Exception as e:
        print(f"✗ {{endpoint}}: Error {{e}}")
    time.sleep(0.5)

print("\\n=== Pinging Sitemaps to Search Engines ===")
sitemap_url = f"https://{{HOST}}/sitemap.xml"
ping_targets = [
    f"https://www.bing.com/ping?sitemap={{urllib.parse.quote(sitemap_url)}}",
    f"https://www.google.com/ping?sitemap={{urllib.parse.quote(sitemap_url)}}"
]

for p_url in ping_targets:
    try:
        req = urllib.request.Request(p_url, headers={{"User-Agent": "Mozilla/5.0"}})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
            print(f"✓ Ping {{p_url.split('?')[0]}}: HTTP {{res.getcode()}}")
    except Exception as e:
        print(f"✗ Ping {{p_url.split('?')[0]}}: {{e}}")

print("\\n=== IndexNow Submission Completed Successfully ===")
"""

with open("submit_indexnow.py", "w", encoding="utf-8") as f:
    f.write(indexnow_code)
print("Updated submit_indexnow.py successfully!")
