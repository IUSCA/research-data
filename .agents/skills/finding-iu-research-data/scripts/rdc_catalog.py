#!/usr/bin/env python3
"""Read IU Research Data Catalog entries from a terminal.

Usage:
    rdc_catalog.py list                 # entries recorded in references/catalog.md
    rdc_catalog.py show <id|words>      # one live entry, all fields
    rdc_catalog.py check                # live updated_at versus the recorded date

The catalog's search pages and feeds sit behind a Cloudflare human check, so
this script cannot list new entries. Each entry's JSON is open, so it reads
entries by id. Find new entries by browsing https://researchdatacatalog.iu.edu
sorted by date modified, then add them to references/catalog.md.

`check` pauses between requests and retries timeouts. It exits 1 when any
entry changed, disappeared, or could not be read. Standard library only.
"""

import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

BASE = "https://researchdatacatalog.iu.edu/concern/data_sets/"
CATALOG_MD = pathlib.Path(__file__).resolve().parent.parent / "references" / "catalog.md"
ROW_RE = re.compile(
    r"^\|\s*(?P<title>[^|]+?)\s*\|.*?concern/data_sets/(?P<id>[0-9a-f-]{36}).*\|\s*(?P<updated>\d{4}-\d{2}-\d{2})\s*\|\s*$"
)

# Display label for each JSON field, in the order the entry page shows them.
FIELDS = [
    ("description", "Description"),
    ("related_url", "Documentation"),
    ("references", "RDC learning module"),
    ("rights_notes", "Access instructions"),
    ("rights_statement", "Access eligibility"),
    ("campus", "Campus"),
    ("holding_location", "Hosting unit"),
    ("location_physical", "Data location"),
    ("time_period", "Timeframe"),
    ("subject", "Keywords"),
    ("geographic_location", "Spatial subject"),
    ("domain_subject", "Domain"),
    ("digital_specifications", "File formats"),
    ("bibliographic_citation", "Citation"),
    ("expert", "Public contact"),
    ("updated_at", "Updated"),
]


def recorded():
    rows = []
    for line in CATALOG_MD.read_text().splitlines():
        m = ROW_RE.match(line)
        if m:
            rows.append((m["id"], m["title"].strip(), m["updated"]))
    return rows


class Unreachable(Exception):
    pass


def fetch(entry_id, tries=4):
    req = urllib.request.Request(
        BASE + entry_id + ".json",
        headers={"User-Agent": "research-data-skills/1.0", "Accept": "application/json"},
    )
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code not in (429, 502, 503, 504):
                raise Unreachable(f"HTTP {e.code}")
        except json.JSONDecodeError:
            raise Unreachable("non-JSON reply, probably the human check; open the entry in a browser")
        except (urllib.error.URLError, TimeoutError) as e:
            pass
        time.sleep(5 * 2 ** attempt)
    raise Unreachable(f"no reply after {tries} tries")


def resolve(arg):
    rows = recorded()
    if re.fullmatch(r"[0-9a-f-]{8,36}", arg):
        hits = [r for r in rows if r[0].startswith(arg)]
        if not hits and len(arg) == 36:
            return arg
    else:
        words = arg.lower().split()
        hits = [r for r in rows if all(w in r[1].lower() for w in words)]
    if len(hits) == 1:
        return hits[0][0]
    if not hits:
        sys.exit(f"No recorded entry matches {arg!r}. Try 'list', or pass a full id.")
    sys.exit("Several entries match:\n" + "\n".join(f"  {i}  {t}" for i, t, _ in hits))


def text(value):
    if isinstance(value, list):
        value = "\n".join(str(v).strip() for v in value if str(v).strip())
    return str(value).strip().replace("\r", "").replace("\n", "\n    ")


def cmd_list():
    for entry_id, title, updated in recorded():
        print(f"{entry_id}  {updated}  {title}")


def cmd_show(arg):
    entry_id = resolve(arg)
    try:
        data = fetch(entry_id)
    except Unreachable as e:
        sys.exit(f"{BASE}{entry_id}: {e}")
    if data is None:
        sys.exit(f"{BASE}{entry_id} returned 404. The entry may have been removed.")
    print(text(data.get("title", "")))
    print(BASE + entry_id)
    for key, label in FIELDS:
        value = data.get(key)
        if value:
            print(f"{label}:\n    {text(value)}")


def cmd_check():
    changed = failed = 0
    for entry_id, title, updated in recorded():
        time.sleep(1)
        try:
            data = fetch(entry_id)
        except Unreachable as e:
            print(f"ERROR    {title}  {e}  {BASE}{entry_id}")
            failed += 1
            continue
        if data is None:
            print(f"GONE     {title}  {BASE}{entry_id}")
            changed += 1
            continue
        live = str(data.get("updated_at", ""))[:10]
        if live != updated:
            print(f"CHANGED  {title}  recorded {updated}, live {live}  {BASE}{entry_id}")
            changed += 1
    print(f"{changed} of {len(recorded())} recorded entries changed or gone; {failed} unreachable.")
    return 1 if changed or failed else 0


def main(argv):
    if len(argv) >= 2 and argv[1] == "list":
        return cmd_list()
    if len(argv) >= 3 and argv[1] == "show":
        return cmd_show(" ".join(argv[2:]))
    if len(argv) == 2 and argv[1] == "check":
        return cmd_check()
    print(__doc__.strip())
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
