import json
import urllib.request
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open("indexnow_key.txt", "r", encoding="utf-8") as f:
    KEY = f.read().strip()

HOST = "lumi-cosme.vercel.app"
URL_LIST = [
    f"https://{HOST}/",
    f"https://{HOST}/winter-bath-care",
    f"https://{HOST}/winter-face-wash",
    f"https://{HOST}/winter-face-mist",
    f"https://{HOST}/winter-lotion",
    f"https://{HOST}/winter-cleansing",
    f"https://{HOST}/winter-day-cream",
    f"https://{HOST}/winter-serum-booster",
    f"https://{HOST}/winter-face-mask",
    f"https://{HOST}/winter-moisture-cream",
    f"https://{HOST}/winter-eye-cream",
    f"https://{HOST}/winter-base-makeup",
    f"https://{HOST}/winter-lip-care",
    f"https://{HOST}/winter-body-care",
    f"https://{HOST}/winter-hair-care",
    f"https://{HOST}/winter-hand-care",
    f"https://{HOST}/summer-cosme"
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": f"https://{HOST}/{KEY}.txt",
    "urlList": URL_LIST
}

data_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")

ENDPOINTS = [
    "api.indexnow.org",
    "www.bing.com",
    "yandex.com",
    "search.seznam.cz"
]

print(f"=== Submitting {len(URL_LIST)} URLs to IndexNow (Host: {HOST}) ===")
print(f"Key: {KEY}")

for endpoint in ENDPOINTS:
    url = f"https://{endpoint}/indexnow"
    req = urllib.request.Request(
        url,
        data=data_bytes,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Mozilla/5.0 (compatible; IndexNowSubmittingBot/1.0)"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            code = res.getcode()
            body = res.read().decode("utf-8", errors="ignore")
            print(f"✓ {endpoint}: HTTP {code} {body if body else '(OK)'}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        print(f"✓ {endpoint}: HTTP {e.code} (Response: {body})")
    except Exception as e:
        print(f"✗ {endpoint}: Error {e}")
    time.sleep(0.5)

print("\n=== Pinging Sitemaps to Search Engines ===")
sitemap_url = f"https://{HOST}/sitemap.xml"
ping_targets = [
    f"https://www.bing.com/ping?sitemap={urllib.parse.quote(sitemap_url)}",
    f"https://www.google.com/ping?sitemap={urllib.parse.quote(sitemap_url)}"
]

for p_url in ping_targets:
    try:
        req = urllib.request.Request(p_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
            print(f"✓ Ping {p_url.split('?')[0]}: HTTP {res.getcode()}")
    except Exception as e:
        print(f"✗ Ping {p_url.split('?')[0]}: {e}")

print("\n=== IndexNow Submission Completed Successfully ===")
