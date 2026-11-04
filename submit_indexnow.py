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
    "https://lumi-cosme.vercel.app/winter-tamanu-oil",
    "https://lumi-cosme.vercel.app/winter-baobab-oil",
    "https://lumi-cosme.vercel.app/winter-kombucha",
    "https://lumi-cosme.vercel.app/winter-manuka-honey",
    "https://lumi-cosme.vercel.app/winter-prickly-pear",
    "https://lumi-cosme.vercel.app/winter-calendula",
    "https://lumi-cosme.vercel.app/winter-resurrection-plant",
    "https://lumi-cosme.vercel.app/winter-beta-glucan",
    "https://lumi-cosme.vercel.app/winter-avocado",
    "https://lumi-cosme.vercel.app/winter-elastin",
    "https://lumi-cosme.vercel.app/winter-allantoin",
    "https://lumi-cosme.vercel.app/winter-beeswax",
    "https://lumi-cosme.vercel.app/winter-yuzu-ceramide",
    "https://lumi-cosme.vercel.app/winter-sake-kasu",
    "https://lumi-cosme.vercel.app/winter-vitamin-e",
    "https://lumi-cosme.vercel.app/winter-liposome",
    "https://lumi-cosme.vercel.app/winter-coenzyme-q10",
    "https://lumi-cosme.vercel.app/winter-astaxanthin",
    "https://lumi-cosme.vercel.app/winter-tranexamic-acid",
    "https://lumi-cosme.vercel.app/winter-azulene",
    "https://lumi-cosme.vercel.app/winter-volufiline",
    "https://lumi-cosme.vercel.app/winter-spicule",
    "https://lumi-cosme.vercel.app/winter-stem-cell",
    "https://lumi-cosme.vercel.app/winter-lipidure",
    "https://lumi-cosme.vercel.app/winter-rosehip-oil",
    "https://lumi-cosme.vercel.app/winter-honey",
    "https://lumi-cosme.vercel.app/winter-mugwort",
    "https://lumi-cosme.vercel.app/winter-marula-oil",
    "https://lumi-cosme.vercel.app/winter-birch-juice",
    "https://lumi-cosme.vercel.app/winter-azelaic-acid",
    "https://lumi-cosme.vercel.app/winter-ectoin",
    "https://lumi-cosme.vercel.app/winter-bakuchiol",
    "https://lumi-cosme.vercel.app/winter-bifida",
    "https://lumi-cosme.vercel.app/winter-proteoglycan",
    "https://lumi-cosme.vercel.app/winter-propolis",
    "https://lumi-cosme.vercel.app/winter-galactomyces",
    "https://lumi-cosme.vercel.app/winter-heparinoid",
    "https://lumi-cosme.vercel.app/winter-vaseline",
    "https://lumi-cosme.vercel.app/winter-placenta",
    "https://lumi-cosme.vercel.app/winter-rice-power",
    "https://lumi-cosme.vercel.app/winter-camellia-oil",
    "https://lumi-cosme.vercel.app/winter-amino-acid",
    "https://lumi-cosme.vercel.app/winter-argan-oil",
    "https://lumi-cosme.vercel.app/winter-horse-oil",
    "https://lumi-cosme.vercel.app/winter-panthenol-cream",
    "https://lumi-cosme.vercel.app/winter-shea-butter",
    "https://lumi-cosme.vercel.app/winter-jojoba-oil",
    "https://lumi-cosme.vercel.app/winter-urea-cream",
    "https://lumi-cosme.vercel.app/winter-ceramide-lotion",
    "https://lumi-cosme.vercel.app/winter-medicinal-lip",
    "https://lumi-cosme.vercel.app/winter-squalane-oil",
    "https://lumi-cosme.vercel.app/winter-ceramide-cream",
    "https://lumi-cosme.vercel.app/winter-peptide-serum",
    "https://lumi-cosme.vercel.app/winter-hair-serum",
    "https://lumi-cosme.vercel.app/winter-exosome-serum",
    "https://lumi-cosme.vercel.app/winter-bath-milk",
    "https://lumi-cosme.vercel.app/winter-glutathione-serum",
    "https://lumi-cosme.vercel.app/winter-pdrn-serum",
    "https://lumi-cosme.vercel.app/winter-collagen-mask",
    "https://lumi-cosme.vercel.app/winter-carbonic-shampoo"
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": f"https://{HOST}/{KEY}.txt",
    "urlList": URL_LIST
}

data_bytes = json.dumps(payload, ensure_ascii=False).encode('utf-8')

endpoints = [
    "https://api.indexnow.org/IndexNow",
    "https://www.bing.com/IndexNow",
    "https://searchadvisor.naver.com/IndexNow",
    "https://yandex.com/indexnow"
]

print(f"Submitting IndexNow for {len(URL_LIST)} URLs...")
print(f"Key: {KEY}")
print(f"Key location: https://{HOST}/{KEY}.txt")

for ep in endpoints:
    print(f"\nSubmitting to: {ep} ...")
    req = urllib.request.Request(
        ep,
        data=data_bytes,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Mozilla/5.0 (compatible; IndexNowBot/1.0)"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            status = res.status
            body = res.read().decode('utf-8')
            print(f"  -> SUCCESS! HTTP status: {status}")
            if body:
                print(f"  -> Response: {body}")
    except urllib.error.HTTPError as e:
        print(f"  -> HTTP Error: {e.code} - {e.reason}")
        try:
            err_body = e.read().decode('utf-8')
            print(f"     Body: {err_body}")
        except:
            pass
    except Exception as e:
        print(f"  -> Connection Error: {e}")
    time.sleep(1)

print("\nIndexNow submission completed!")
