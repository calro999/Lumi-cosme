import os
from update_all_internal_links import ALL_ARTICLES

BASE_URL = "https://lumi-cosme.vercel.app"

# 1. sitemap.xml の生成
xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    '  <url>',
    f'    <loc>{BASE_URL}/</loc>',
    '    <changefreq>daily</changefreq>',
    '    <priority>1.0</priority>',
    '  </url>'
]

for idx, a in enumerate(ALL_ARTICLES):
    priority = "0.95" if idx < 3 else ("0.8" if a["url"] == "/summer-cosme" else "0.9")
    xml_lines.extend([
        '  <url>',
        f'    <loc>{BASE_URL}{a["url"]}</loc>',
        '    <changefreq>weekly</changefreq>',
        f'    <priority>{priority}</priority>',
        '  </url>'
    ])

xml_lines.append('</urlset>')
xml_content = "\n".join(xml_lines) + "\n"

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)
print(f"Successfully generated sitemap.xml with {len(ALL_ARTICLES) + 1} URLs!")

# 2. submit_indexnow.py の生成
url_list_str = ',\n'.join([f'    "{BASE_URL}/"'] + [f'    "{BASE_URL}{a["url"]}"' for a in ALL_ARTICLES])

indexnow_script = f'''import json
import urllib.request
import urllib.parse
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open("indexnow_key.txt", "r", encoding="utf-8") as f:
    KEY = f.read().strip()

HOST = "lumi-cosme.vercel.app"
URL_LIST = [
{url_list_str}
]

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow"
]

def submit():
    payload = {{
        "host": HOST,
        "key": KEY,
        "keyLocation": f"https://{{HOST}}/{{KEY}}.txt",
        "urlList": URL_LIST
    }}
    
    data_bytes = json.dumps(payload).encode("utf-8")
    
    print(f"=== Submitting {{len(URL_LIST)}} URLs to IndexNow ===")
    print(f"Key: {{KEY}}")
    print(f"KeyLocation: https://{{HOST}}/{{KEY}}.txt")
    print(f"First 3 URLs:")
    for u in URL_LIST[:3]:
        print(f"  - {{u}}")
    print(f"...")

    success = False
    for ep in ENDPOINTS:
        print(f"\\nSubmitting to: {{ep}} ...")
        try:
            req = urllib.request.Request(
                ep,
                data=data_bytes,
                headers={{
                    "Content-Type": "application/json; charset=utf-8",
                    "User-Agent": "LumiCosmeIndexNowBot/2.0"
                }},
                method="POST"
            )
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                code = res.getcode()
                body = res.read().decode("utf-8")
                print(f"  Response: HTTP {{code}} ({{res.reason}})")
                if code in (200, 202):
                    print(f"  ✓ Success! URLs accepted by {{ep}}")
                    success = True
                else:
                    print(f"  Response body: {{body}}")
        except urllib.error.HTTPError as e:
            print(f"  HTTP Error {{e.code}}: {{e.reason}}")
            try:
                err_body = e.read().decode("utf-8")
                print(f"  Details: {{err_body}}")
            except:
                pass
            if e.code in (200, 202):
                success = True
        except Exception as e:
            print(f"  Error: {{e}}")
            
    return success

if __name__ == "__main__":
    submit()
'''

with open("submit_indexnow.py", "w", encoding="utf-8") as f:
    f.write(indexnow_script)
print("Successfully generated submit_indexnow.py!")
