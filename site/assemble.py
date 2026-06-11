#!/usr/bin/env python3
"""Fuse the template, agent-built components, and live data into one
self-contained index.html (no external requests — works offline on mobile)."""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE, DATA, COMP = ROOT / "site", ROOT / "data", ROOT / "components"

template = (SITE / "index_template.html").read_text()

# --- live brewery data (filter junk: closed/contract/proprietor entries) ---
brew = json.loads((DATA / "breweries.json").read_text())
BAD_TYPES = {"closed", "contract", "proprietor", "planning"}
for city in ("boston", "miami"):
    c = brew[city]
    c["closest"] = [b for b in c["closest"] if b.get("type") not in BAD_TYPES][:8]
    c = {k: c[k] for k in ("stadium", "total_in_state", "within_10mi", "within_25mi", "closest")}
    brew[city] = c

# --- curated dashboard data (researched figures; see data/facts.json + sources) ---
facts = json.loads((DATA / "facts.json").read_text())

payload = {
    "stats": json.loads((SITE / "stats.json").read_text()),
    "consumption": json.loads((SITE / "consumption.json").read_text()),
    "consumption_note": (SITE / "consumption_note.txt").read_text().strip(),
    "pint_prices": json.loads((SITE / "pint_prices.json").read_text()),
    "price_note": (SITE / "price_note.txt").read_text().strip(),
    "breweries": brew,
}

html = template.replace("/*DATA_JSON*/{}", json.dumps(payload, ensure_ascii=False))

for token, fname in (("<!--MATCHER-->", "matcher.html"), ("<!--CALCULATOR-->", "calculator.html")):
    snippet = (COMP / fname).read_text()
    # strip any accidental full-document wrappers, keep the <section>...</section>
    m = re.search(r"<section[\s\S]*</section>", snippet)
    html = html.replace(token, m.group(0) if m else snippet)

out = SITE / "index.html"
out.write_text(html)
print(f"wrote {out} ({out.stat().st_size/1024:.0f} KB)")
