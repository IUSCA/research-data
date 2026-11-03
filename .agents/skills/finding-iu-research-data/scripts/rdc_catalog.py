#!/usr/bin/env python3
"""Read IU Research Data Catalog entries from a terminal.

Usage:
    rdc_catalog.py list                 # entries recorded in references/catalog.md
    rdc_catalog.py show <id|words>      # one live entry, all fields
    rdc_catalog.py check                # live updated_at versus the recorded date
    rdc_catalog.py new                  # listed entries not in references/catalog.md

The catalog's /catalog search pages and feeds sit behind a Cloudflare human
check. Each entry's JSON is open, so `show` and `check` read entries by id.
The home page listing, newest first, loads from a script (Observed
2026-11-03), so `new` reads entry ids from it.

`check` pauses between requests and retries timeouts. It exits 1 when any
entry changed, disappeared, or could not be read. `new` reads robots.txt and
waits its crawl delay before the listing. It exits 1 when any listed entry is
new, and 2 when the listing returns the human check or changes shape.
Standard library only.
"""

import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request
import urllib.robotparser

SITE = "https://researchdatacatalog.iu.edu"
BASE = SITE + "/concern/data_sets/"
LISTING = SITE + "/?sort=system_modified_dtsi+desc&per_page=100"
USER_AGENT = "research-data-skills/1.0 (+https://github.com/IUSCA/research-data)"
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
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
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


# One listed entry: its <li id="document_<id>"> and the title link inside it.
LISTED_RE = re.compile(
    r'id="document_(?P<id>[0-9a-f-]{36})".*?class="search-result-title">\s*<a [^>]*>(?P<title>[^<]*)</a>',
    re.S,
)
TOTAL_RE = re.compile(r'class="page-entries">.*?of\s*<strong>(?P<total>[\d,]+)</strong>', re.S)
HUMAN_CHECK = ("Verifying you are human", "cf-turnstile", "challenge-platform")


def listing_problem(message):
    print(f"ERROR    catalog listing: {message}  {LISTING}")
    return 2


def cmd_new():
    robots = urllib.robotparser.RobotFileParser(SITE + "/robots.txt")
    try:
        req = urllib.request.Request(robots.url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            robots.parse(resp.read().decode("utf-8", "replace").splitlines())
    except (urllib.error.URLError, TimeoutError) as e:
        return listing_problem(f"could not read robots.txt ({e})")
    if not robots.can_fetch(USER_AGENT, LISTING):
        return listing_problem("robots.txt now disallows the listing for this script")
    time.sleep(robots.crawl_delay(USER_AGENT) or 10)
    try:
        req = urllib.request.Request(LISTING, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=60) as resp:
            page = resp.read().decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError) as e:
        return listing_problem(f"no reply ({e})")
    if any(mark in page for mark in HUMAN_CHECK):
        return listing_problem("the page returned the human check; a person must browse it")
    listed = {m["id"]: html.unescape(m["title"]).strip() for m in LISTED_RE.finditer(page)}
    total = TOTAL_RE.search(page)
    if not listed or not total:
        return listing_problem("no entries or no entry count found; the page changed shape")
    total = int(total["total"].replace(",", ""))
    if total != len(listed):
        return listing_problem(f"the catalog has {total} entries but the page lists {len(listed)}; raise per_page or read more pages")
    known = {entry_id for entry_id, _, _ in recorded()}
    new = [(i, t) for i, t in listed.items() if i not in known]
    for entry_id, title in new:
        print(f"NEW      {title}  {BASE}{entry_id}")
    print(f"{len(new)} of {len(listed)} listed entries are not in references/catalog.md.")
    return 1 if new else 0


def main(argv):
    if len(argv) >= 2 and argv[1] == "list":
        return cmd_list()
    if len(argv) >= 3 and argv[1] == "show":
        return cmd_show(" ".join(argv[2:]))
    if len(argv) == 2 and argv[1] == "check":
        return cmd_check()
    if len(argv) == 2 and argv[1] == "new":
        return cmd_new()
    print(__doc__.strip())
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
