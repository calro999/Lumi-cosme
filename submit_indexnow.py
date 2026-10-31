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
    "https://lumi-cosme.vercel.app/winter-cleansing-gel",
    "https://lumi-cosme.vercel.app/winter-peel-serum",
    "https://lumi-cosme.vercel.app/winter-lip-serum",
    "https://lumi-cosme.vercel.app/winter-cleansing-oil",
    "https://lumi-cosme.vercel.app/winter-body-milk",
    "https://lumi-cosme.vercel.app/winter-toner-pad",
    "https://lumi-cosme.vercel.app/winter-night-cream",
    "https://lumi-cosme.vercel.app/winter-cleansing-milk",
    "https://lumi-cosme.vercel.app/winter-hair-mist",
    "https://lumi-cosme.vercel.app/winter-cleansing-balm",
    "https://lumi-cosme.vercel.app/winter-scalp-shampoo",
    "https://lumi-cosme.vercel.app/winter-cica-cream",
    "https://lumi-cosme.vercel.app/winter-holiday-coffret",
    "https://lumi-cosme.vercel.app/winter-enzyme-wash",
    "https://lumi-cosme.vercel.app/winter-tinted-lip-balm",
    "https://lumi-cosme.vercel.app/winter-eyelash-serum",
    "https://lumi-cosme.vercel.app/winter-point-makeup-remover",
    "https://lumi-cosme.vercel.app/winter-massage-cream",
    "https://lumi-cosme.vercel.app/winter-hand-serum",
    "https://lumi-cosme.vercel.app/winter-bath-oil",
    "https://lumi-cosme.vercel.app/winter-body-butter",
    "https://lumi-cosme.vercel.app/winter-hair-balm",
    "https://lumi-cosme.vercel.app/winter-hot-cleansing",
    "https://lumi-cosme.vercel.app/winter-neck-cream",
    "https://lumi-cosme.vercel.app/winter-lip-scrub",
    "https://lumi-cosme.vercel.app/winter-bb-cream",
    "https://lumi-cosme.vercel.app/winter-carbonic-pack",
    "https://lumi-cosme.vercel.app/winter-uv-cream",
    "https://lumi-cosme.vercel.app/winter-wrinkle-cream",
    "https://lumi-cosme.vercel.app/winter-body-wash",
    "https://lumi-cosme.vercel.app/winter-make-keep-mist",
    "https://lumi-cosme.vercel.app/winter-lip-oil",
    "https://lumi-cosme.vercel.app/winter-body-oil",
    "https://lumi-cosme.vercel.app/winter-liquid-foundation",
    "https://lumi-cosme.vercel.app/winter-cream-cheek",
    "https://lumi-cosme.vercel.app/winter-cream-eyeshadow",
    "https://lumi-cosme.vercel.app/winter-highlighter",
    "https://lumi-cosme.vercel.app/winter-hair-oil",
    "https://lumi-cosme.vercel.app/winter-lip-mask",
    "https://lumi-cosme.vercel.app/winter-hair-milk",
    "https://lumi-cosme.vercel.app/winter-cushion-foundation",
    "https://lumi-cosme.vercel.app/winter-body-scrub",
    "https://lumi-cosme.vercel.app/winter-hydrating-serum",
    "https://lumi-cosme.vercel.app/winter-concealer",
    "https://lumi-cosme.vercel.app/winter-lip-tint",
    "https://lumi-cosme.vercel.app/winter-powder",
    "https://lumi-cosme.vercel.app/winter-lip-plumper",
    "https://lumi-cosme.vercel.app/winter-hair-mask",
    "https://lumi-cosme.vercel.app/winter-stick-serum",
    "https://lumi-cosme.vercel.app/winter-scalp-serum",
    "https://lumi-cosme.vercel.app/winter-toneup-base",
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
    "https://lumi-cosme.vercel.app/winter-moisture-cream",
    "https://lumi-cosme.vercel.app/winter-serum-booster",
    "https://lumi-cosme.vercel.app/winter-face-mask",
    "https://lumi-cosme.vercel.app/winter-eye-cream",
    "https://lumi-cosme.vercel.app/winter-base-makeup",
    "https://lumi-cosme.vercel.app/winter-lip-care",
    "https://lumi-cosme.vercel.app/winter-body-care",
    "https://lumi-cosme.vercel.app/winter-hair-care",
    "https://lumi-cosme.vercel.app/winter-hand-care",
    "https://lumi-cosme.vercel.app/summer-cosme"
]

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow"
]

def submit():
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": f"https://{HOST}/{KEY}.txt",
        "urlList": URL_LIST
    }
    
    data_bytes = json.dumps(payload).encode("utf-8")
    
    print(f"=== Submitting {len(URL_LIST)} URLs to IndexNow ===")
    print(f"Key: {KEY}")
    print(f"KeyLocation: https://{HOST}/{KEY}.txt")
    print(f"First 3 URLs:")
    for u in URL_LIST[:3]:
        print(f"  - {u}")
    print(f"...")

    success = False
    for ep in ENDPOINTS:
        print(f"\nSubmitting to: {ep} ...")
        try:
            req = urllib.request.Request(
                ep,
                data=data_bytes,
                headers={
                    "Content-Type": "application/json; charset=utf-8",
                    "User-Agent": "LumiCosmeIndexNowBot/2.0"
                },
                method="POST"
            )
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                code = res.getcode()
                body = res.read().decode("utf-8")
                print(f"  Response: HTTP {code} ({res.reason})")
                if code in (200, 202):
                    print(f"  ✓ Success! URLs accepted by {ep}")
                    success = True
                else:
                    print(f"  Response body: {body}")
        except urllib.error.HTTPError as e:
            print(f"  HTTP Error {e.code}: {e.reason}")
            try:
                err_body = e.read().decode("utf-8")
                print(f"  Details: {err_body}")
            except:
                pass
            if e.code in (200, 202):
                success = True
        except Exception as e:
            print(f"  Error: {e}")
            
    return success

if __name__ == "__main__":
    submit()
