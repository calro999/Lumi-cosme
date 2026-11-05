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
    "https://lumi-cosme.vercel.app/winter-lactobacillus",
    "https://lumi-cosme.vercel.app/winter-swallow-nest",
    "https://lumi-cosme.vercel.app/winter-dokudami",
    "https://lumi-cosme.vercel.app/winter-fucoidan",
    "https://lumi-cosme.vercel.app/winter-royal-jelly",
    "https://lumi-cosme.vercel.app/winter-soy-isoflavone",
    "https://lumi-cosme.vercel.app/winter-sacran",
    "https://lumi-cosme.vercel.app/winter-fullerene",
    "https://lumi-cosme.vercel.app/winter-hatomugi",
    "https://lumi-cosme.vercel.app/winter-mango-butter",
    "https://lumi-cosme.vercel.app/winter-tremella",
    "https://lumi-cosme.vercel.app/winter-collagen",
    "https://lumi-cosme.vercel.app/winter-olive-oil",
    "https://lumi-cosme.vercel.app/winter-meadowfoam-oil",
    "https://lumi-cosme.vercel.app/winter-trehalose",
    "https://lumi-cosme.vercel.app/winter-murumuru-butter",
    "https://lumi-cosme.vercel.app/winter-cranberry-oil",
    "https://lumi-cosme.vercel.app/winter-emu-oil",
    "https://lumi-cosme.vercel.app/winter-ginseng",
    "https://lumi-cosme.vercel.app/winter-cacao-butter",
    "https://lumi-cosme.vercel.app/winter-silk",
    "https://lumi-cosme.vercel.app/winter-apricot-oil",
    "https://lumi-cosme.vercel.app/winter-sweet-almond-oil",
    "https://lumi-cosme.vercel.app/winter-shikon",
    "https://lumi-cosme.vercel.app/winter-seabuckthorn-oil",
    "https://lumi-cosme.vercel.app/winter-black-seed-oil",
    "https://lumi-cosme.vercel.app/winter-hemp-seed-oil",
    "https://lumi-cosme.vercel.app/winter-macadamia-oil",
    "https://lumi-cosme.vercel.app/winter-pomegranate-oil",
    "https://lumi-cosme.vercel.app/winter-rice-bran-oil",
    "https://lumi-cosme.vercel.app/winter-damask-rose",
    "https://lumi-cosme.vercel.app/winter-evening-primrose",
    "https://lumi-cosme.vercel.app/winter-moringa-oil",
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
    "https://lumi-cosme.vercel.app/winter-carbonic-shampoo",
    "https://lumi-cosme.vercel.app/winter-oil-mist",
    "https://lumi-cosme.vercel.app/winter-carbonic-bath",
    "https://lumi-cosme.vercel.app/winter-hot-treatment",
    "https://lumi-cosme.vercel.app/winter-foot-mask",
    "https://lumi-cosme.vercel.app/winter-eye-patch",
    "https://lumi-cosme.vercel.app/winter-nail-serum",
    "https://lumi-cosme.vercel.app/winter-inbath-body",
    "https://lumi-cosme.vercel.app/winter-hot-eyemask",
    "https://lumi-cosme.vercel.app/winter-hand-mask",
    "https://lumi-cosme.vercel.app/winter-needle-patch",
    "https://lumi-cosme.vercel.app/winter-bath-salt",
    "https://lumi-cosme.vercel.app/winter-lip-gloss",
    "https://lumi-cosme.vercel.app/winter-morning-mask",
    "https://lumi-cosme.vercel.app/winter-gel-wash",
    "https://lumi-cosme.vercel.app/winter-lip-primer",
    "https://lumi-cosme.vercel.app/winter-carbonic-wash",
    "https://lumi-cosme.vercel.app/winter-control-color",
    "https://lumi-cosme.vercel.app/winter-multi-balm",
    "https://lumi-cosme.vercel.app/winter-advent-calendar",
    "https://lumi-cosme.vercel.app/winter-hyaluronic-serum",
    "https://lumi-cosme.vercel.app/winter-hand-wash",
    "https://lumi-cosme.vercel.app/winter-scalp-scrub",
    "https://lumi-cosme.vercel.app/winter-medicinal-bath",
    "https://lumi-cosme.vercel.app/winter-wipe-lotion",
    "https://lumi-cosme.vercel.app/winter-hair-treatment",
    "https://lumi-cosme.vercel.app/winter-lip-balm",
    "https://lumi-cosme.vercel.app/winter-carbonic-serum",
    "https://lumi-cosme.vercel.app/winter-body-cream",
    "https://lumi-cosme.vercel.app/winter-booster-oil",
    "https://lumi-cosme.vercel.app/winter-moisture-shampoo",
    "https://lumi-cosme.vercel.app/winter-vitamin-c-serum",
    "https://lumi-cosme.vercel.app/winter-makeup-primer",
    "https://lumi-cosme.vercel.app/winter-cream-foundation",
    "https://lumi-cosme.vercel.app/winter-cleansing-cream",
    "https://lumi-cosme.vercel.app/winter-niacinamide-serum",
    "https://lumi-cosme.vercel.app/winter-lipstick",
    "https://lumi-cosme.vercel.app/winter-hand-cream",
    "https://lumi-cosme.vercel.app/winter-retinol-cream",
    "https://lumi-cosme.vercel.app/winter-ceramide-serum",
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
