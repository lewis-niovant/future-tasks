#!/usr/bin/env python3
"""Analyze Open Brewery DB data around World Cup 2026 stadiums (Scotland matches)."""
import json
import math
import os
from collections import Counter

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

STADIUMS = {
    "boston": {"name": "Gillette Stadium", "lat": 42.0909, "lon": -71.2643, "raw": "raw_ma.json"},
    "miami": {"name": "Hard Rock Stadium", "lat": 25.9580, "lon": -80.2389, "raw": "raw_fl.json"},
}


def haversine_miles(lat1, lon1, lat2, lon2):
    r = 3958.7613  # Earth mean radius in miles
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlam / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def load_breweries(path):
    with open(path) as f:
        raw = json.load(f)
    seen = set()
    breweries = []
    for b in raw:
        if b.get("latitude") in (None, "") or b.get("longitude") in (None, ""):
            continue
        try:
            lat, lon = float(b["latitude"]), float(b["longitude"])
        except (TypeError, ValueError):
            continue
        key = b.get("id") or (b.get("name"), b.get("city"))
        if key in seen:
            continue
        seen.add(key)
        breweries.append({
            "name": b.get("name"),
            "city": b.get("city"),
            "type": b.get("brewery_type"),
            "website": b.get("website_url"),
            "lat": lat,
            "lon": lon,
        })
    return breweries, len(raw)


def analyze(key):
    s = STADIUMS[key]
    breweries, total_raw = load_breweries(os.path.join(DATA_DIR, s["raw"]))
    for b in breweries:
        b["miles"] = haversine_miles(s["lat"], s["lon"], b["lat"], b["lon"])
    breweries.sort(key=lambda b: b["miles"])

    within_25 = [b for b in breweries if b["miles"] <= 25]
    closest = [
        {"name": b["name"], "city": b["city"], "type": b["type"],
         "miles": round(b["miles"], 1), "website": b["website"]}
        for b in breweries[:12]
    ]
    top_city = Counter(b["city"] for b in within_25).most_common(1)
    type_counts = Counter(b["type"] for b in breweries)

    result = {
        "stadium": s["name"],
        "total_in_state": total_raw,
        "with_coordinates": len(breweries),
        "within_10mi": sum(1 for b in breweries if b["miles"] <= 10),
        "within_25mi": len(within_25),
        "by_type": dict(type_counts),
        "closest": closest,
        "fun_stats": {
            "top_city_within_25mi": {"city": top_city[0][0], "count": top_city[0][1]} if top_city else None,
            "micro_vs_brewpub_vs_large": {
                "micro": type_counts.get("micro", 0),
                "brewpub": type_counts.get("brewpub", 0),
                "large": type_counts.get("large", 0),
            },
        },
    }
    return result


def main():
    out = {key: analyze(key) for key in STADIUMS}
    out_path = os.path.join(DATA_DIR, "breweries.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    for key, r in out.items():
        print(f"{key}: {r['stadium']} | state total={r['total_in_state']} "
              f"(geocoded={r['with_coordinates']}) | <=10mi={r['within_10mi']} | <=25mi={r['within_25mi']}")
        print(f"  top city: {r['fun_stats']['top_city_within_25mi']}")
        print(f"  types: {r['by_type']}")
        print(f"  closest: {r['closest'][0]['name']} ({r['closest'][0]['miles']} mi, {r['closest'][0]['city']})")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
