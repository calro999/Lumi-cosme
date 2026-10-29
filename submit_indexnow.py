import json
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
    "https://lumi-cosme.vercel.app/",
    "https://lumi-cosme.vercel.app/winter-sleeping-mask",
    "https://lumi-cosme.vercel.app/winter-nail-oil",
    "https://lumi-cosme.vercel.app/winter-foot-cream",
    "https://lumi-cosme.vercel.app/winter-emulsion",
    "https://lumi-cosme.vercel.app/winter-face-oil",
    "https://lumi-cosme.vercel.app/winter-repair-balm",
    "https://lumi-cosme.vercel.app/winter-bath-care",
    "https://lumi-cosme.vercel.app/winter-face-wash",
    "https://lumi-cosme.vercel.app/winter-face-mist",
    "https://lumi-cosme.vercel.app/winter-lotion",
    "https://lumi-cosme.vercel.app/winter-cleansing",
    "https://lumi-cosme.vercel.app/winter-day-cream",
    "https://lumi-cosme.vercel.app/winter-serum-booster",
    "https://lumi-cosme.vercel.app/winter-face-mask",
    "https://lumi-cosme.vercel.app/winter-moisture-cream",
    "https://lumi-cosme.vercel.app/winter-eye-cream",
    "https://lumi-cosme.vercel.app/winter-base-makeup",
    "https://lumi-cosme.vercel.app/winter-lip-care",
    "https://lumi-cosme.vercel.app/winter-body-care",
    "https://lumi-cosme.vercel.app/winter-hair-care",
    "https://lumi-cosme.vercel.app/winter-hand-care",
    "https://lumi-cosme.vercel.app/summer-cosme"
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
