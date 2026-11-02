import json
with open("fetched_3new_nov_dec_ceramide_lotion_lip_squalane_data.json") as f:
    d = json.load(f)

for cat, val in d.items():
    items = val["items"]
    print(f"=== {cat}: {len(items)} items ===")
    for it in items:
        r = it["rank"]
        nm = it["name"]
        rn = it["rakuten_name"][:45]
        pr = it["price"]
        img = "OK" if it["image"].startswith("http") else "NO_IMG"
        aff = "OK" if it["affiliateUrl"].startswith("http") else "NO_AFF"
        print(f"  Rank {r:2d}: {nm[:30]:30s} | ¥{pr:5d} | Img: {img} | Aff: {aff} | {rn}")
