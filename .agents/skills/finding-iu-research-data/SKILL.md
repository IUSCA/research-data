---
name: finding-iu-research-data
description: Find research data that Indiana University already has or can get, using the IU Research Data Commons (RDC) Research Data Catalog as the source of truth. Covers matching a research question to datasets such as INPC, HCUP, MarketScan, All of Us, Human Connectome Project, OSoMe social media archives, WRDS, CoreLogic, Web of Science, and library-licensed data, and checking eligibility and campus. Use when someone asks what data IU has on a topic, whether IU already licenses a dataset, or where to start getting data for a project.
---

# Finding IU research data

Verified 2026-10-04 against the IU Research Data Commons (RDC) site and the
Research Data Catalog. Sources are listed at the end.

Start with the Research Data Catalog, then confirm the entry live before
advising anyone. Access terms, eligibility, and contacts change. A copy in
this skill is a lead, not an answer.

## Where IU lists its data

- **Research Data Catalog**, https://researchdatacatalog.iu.edu, lists
  datasets "available to researchers at Indiana University, including
  licensed data sets and, in some cases, publicly-available data." It is
  curated by the RDC Data Cataloging Working Group. It held 35 entries when
  Observed 2026-10-04.
- **RDC Resource Catalog**, https://researchdata.iu.edu/resource-catalog/,
  lists services, units, and policies rather than datasets. Use it to find
  RADaRS, the Federal Statistical Research Data Center, ICPSR, and support
  offices.
- **RDC Featured Data Program** offers self-paced Canvas modules for
  CoreLogic, INPC, HCUP, environmental data, All of Us, Web of Science, and
  the Human Connectome Project.

The RDC itself says no complete list exists: "There is not a current,
comprehensive catalog of data assets owned by Indiana University." A dataset
missing from the catalog may still be licensed somewhere at IU. See "When the
catalog has nothing" below.

## Find candidates

1. Read [references/catalog.md](references/catalog.md). It groups the 35
   entries by domain, with host, eligibility, campus, and access route.
2. Match on the research question, not only the keyword. For example,
   hospital utilization questions fit HCUP, MarketScan, or INPC. They differ
   in population, identifiability, and access burden.
3. Check eligibility and campus first. Many licensed sets are IU Bloomington
   only. Some exclude undergraduates or need a faculty sponsor.
4. Read the live entry before giving access steps:

```bash
s=.agents/skills/finding-iu-research-data/scripts
$s/rdc_catalog.py show hcup national inpatient   # title words or an id
$s/rdc_catalog.py list                           # every recorded entry
```

The script reads each entry's JSON. The catalog's search pages and feeds sit
behind a Cloudflare human check. A person must browse the catalog to see
entries added after the snapshot.

## Compare candidates

Give the person a short comparison, not a list. For each dataset, say:

| Question | Where to find it |
| --- | --- |
| Does it answer the research question? | Description, Timeframe, Spatial subject |
| Can this person use it? | Access eligibility, Campus |
| What does access take? | Access instructions: forms, training, IRB, DUA, fees |
| Where must the analysis run? | Data location, for example "RADaRS" or "UITS RT HPC" |
| Whom to ask | Public contact |

Then hand off:

- Clinical, claims, or biospecimen data: `accessing-health-and-clinical-data`.
- Licensed, social media, or federal restricted data:
  `using-licensed-and-public-data`.
- Storage and handling once access is granted: `classifying-research-data`.

**Recommended.** Name the access burden plainly. IRB approval, a DUA, and a
secure enclave can add weeks. Say so before someone builds a project plan on
a dataset.

## When the catalog has nothing

The RDC's guidance for checking whether IU already owns data:

1. Search the Research Data Catalog.
2. Search the supplier in BUY.IU. Students cannot.
3. Search IUCAT or the IU Libraries A–Z database list.
4. Ask a subject librarian, or Research Data Services at resdata@iu.edu.

If IU does not have it, `using-licensed-and-public-data` covers buying data.
**Recommended.** Before buying, email iurdc@iu.edu. The RDC catalog exists
partly "to reduce redundancies in data acquisition."

## Suggest an addition

Anyone can propose a dataset for the catalog by emailing iurdc@iu.edu, per
the catalog's About page.

**Recommended.** When a lab holds licensed or shareable data that others at
IU could use, list it in the catalog. A listing prevents duplicate purchases.
It also means the data keeps a contact after the person who acquired it
leaves.

## Keep this file current

- Run `scripts/rdc_catalog.py check`. It reports entries whose `updated_at`
  changed, and entries that no longer exist. Update the row in
  `references/catalog.md`, including its date.
- Browse https://researchdatacatalog.iu.edu sorted by date modified. Add any
  entry not in `references/catalog.md`.
- **Open item.** Both `researchdata.iu.edu` and `rdc.iu.edu` serve the RDC
  site, with no redirect. This skill uses `researchdata.iu.edu`, which the
  catalog links back to. Ask iurdc@iu.edu which host is canonical.
- **Open item.** Catalog entries carry no data classification. Ask the RDC
  whether one will be added.

## Sources

Checked 2026-10-04.

- Research Data Catalog and About page: https://researchdatacatalog.iu.edu,
  https://researchdatacatalog.iu.edu/about
- Data Cataloging Working Group:
  https://researchdata.iu.edu/about/working-groups/data-cataloging/
- RDC Resource Catalog: https://researchdata.iu.edu/resource-catalog/
- Featured Data Program:
  https://researchdata.iu.edu/resources/featured-data-program/
- RDC FAQ, "Determine whether IU already owns it":
  https://researchdata.iu.edu/faqs/acquiring-data/determine-whether-iu-already-owns-it/
- All 35 catalog entry pages and their JSON, listed in
  `references/catalog.md`.
