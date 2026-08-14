import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Query thesis literature catalog")
    parser.add_argument("--tags", default="", help="Comma-separated tags, e.g. CMAPSS,LSTM")
    parser.add_argument("--combo", default="", help="Exact combo label, e.g. CMAPSS+LSTM")
    parser.add_argument("--min-year", type=int, default=0)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    catalog_path = Path(__file__).resolve().parents[1] / "catalog.local.json"
    data = json.loads(catalog_path.read_text(encoding="utf-8"))

    required_tags = {t.strip() for t in args.tags.split(",") if t.strip()}
    rows = []
    for e in data:
        year = 0
        if e.get("year"):
            y = "".join(ch for ch in str(e["year"]) if ch.isdigit())
            if len(y) >= 4:
                year = int(y[:4])
        if year < args.min_year:
            continue
        if required_tags and not required_tags.issubset(set(e.get("tags", []))):
            continue
        if args.combo and args.combo not in e.get("combos", []):
            continue
        rows.append((e.get("priority_score", 0), year, e))

    rows.sort(key=lambda x: (-x[0], -x[1], x[2].get("title", "")))
    for _, _, e in rows[: args.top]:
        print(f"- {e.get('title','')}")
        print(f"  key: {e.get('key','')} | year: {e.get('year','')} | tags: {','.join(e.get('tags',[]))}")
        if e.get("doi"):
            print(f"  doi: {e['doi']}")
        elif e.get("url"):
            print(f"  url: {e['url']}")
        print()


if __name__ == "__main__":
    main()
