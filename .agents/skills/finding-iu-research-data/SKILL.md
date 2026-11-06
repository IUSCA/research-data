---
name: finding-iu-research-data
description: Find research data that Indiana University already has or can get, using the IU Research Data Commons (RDC) Research Data Catalog and this repository's inventory of IU data resources the catalog does not list. Covers matching a research question to datasets such as INPC, the Indiana Biobank, NCRAD, HCUP, MarketScan, All of Us, Human Connectome Project, OSoMe social media archives, WRDS, CoreLogic, Web of Science, ICPSR, the Kinsey Institute, Indiana state data, and library-licensed data, and checking eligibility and campus. Use when someone asks what data IU has on a topic, whether IU already has or licenses a dataset before they buy or collect their own, or where to start looking for existing data for a project.
---

# Finding IU research data

Verified 2026-11-05 (the inventory and its sources only). Verified
2026-11-03 (the catalog home page listing and all 35 entries' JSON only).
Other sources were verified 2026-10-04 against the IU Research
Data Commons (RDC) site and the Research Data Catalog. Sources are listed at
the end.

Search two lists: the Research Data Catalog, and this skill's inventory of
IU data resources the catalog does not list. Then confirm the entry live,
on the catalog or the resource's own page, before advising anyone. Access terms, eligibility, and contacts change. A copy in
this skill is a lead, not an answer.

## When to ask a person

These questions need a person. Contacts are from
`getting-help-with-research-data` and the sections below.
Read the KB article cited with a contact for its current form, and cite it.
A contact marked "not the IU KB" comes from the page named with it.

| Situation | Ask | Send |
| --- | --- | --- |
| Eligibility, access steps, or timing for a catalog dataset | The entry's Public Contact | The entry, your role and campus, and your deadline |
| Whether IU already has data, before buying, or a catalog addition | Research Data Commons, iurdc@iu.edu (from the [RDC contact page](https://researchdata.iu.edu/about/contact/), not the IU KB) | The dataset or supplier, and the intended use |
| Secondary data the catalog lacks | IU Libraries Research Data Services, resdata@iu.edu (from the [IU Libraries Research Data Services page](https://libraries.indiana.edu/research-data-services), not the IU KB); at IU Indianapolis, dataserv@iu.edu (from the [RDC DMP consultation page](https://researchdata.iu.edu/resources/dmp-consultation/), not the IU KB) | The research question and where you have searched |

**Recommended.** In these cases, say plainly that the question needs a
person. Name the office and what to send. Do not offer a best guess as the
answer. Only the office can decide, and a guess can lead a researcher to
break an agreement or a rule.

For any other question, see `getting-help-with-research-data`.

## Where IU lists its data

- **Research Data Catalog**, https://researchdatacatalog.iu.edu, lists
  datasets "available to researchers at Indiana University, including
  licensed data sets and, in some cases, publicly-available data." It is
  curated by the RDC Data Cataloging Working Group. It held 35 entries when
  Observed 2026-11-03.
- **RDC Resource Catalog**, https://researchdata.iu.edu/resource-catalog/,
  lists services, units, and policies rather than datasets. Use it to find
  RADaRS, the Federal Statistical Research Data Center, ICPSR, and support
  offices.
- **RDC Featured Data Program** offers self-paced Canvas modules for
  CoreLogic, INPC, HCUP, environmental data, All of Us, Web of Science, and
  the Human Connectome Project.

- **This skill's inventory**, [references/inventory.md](references/inventory.md),
  lists IU-held and IU-licensed data resources found on public IU pages but
  not in the catalog. Examples are the Indiana Biobank, NCRAD, the Kinsey
  Institute collections, and state data partnerships. Each row is Observed,
  with its source and date.

The RDC itself says no complete list exists: "There is not a current,
comprehensive catalog of data assets owned by Indiana University." A dataset
missing from the catalog may still be licensed somewhere at IU. See "When the
catalog has nothing" below.

## Find candidates

1. Read [references/catalog.md](references/catalog.md). It groups the 35
   entries by domain, with host, eligibility, campus, and access route.
   Then read [references/inventory.md](references/inventory.md) for the
   same domain. **Recommended.** Always check both. The catalog is
   incomplete by the RDC's own account, and the inventory covers known
   gaps, such as the Indiana Biobank.
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
behind a Cloudflare human check. The home page listing does not, so
`rdc_catalog.py new` lists entries added after the snapshot (Observed
2026-11-03).

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

## When neither list has it

If IU holds nothing suitable, a public or controlled-access repository
outside IU may. `finding-data-in-public-repositories` covers dbGaP, GEO,
ICPSR, UK Biobank, Census and IPUMS, generalist repositories, and others.

The RDC's guidance for checking whether IU already owns data:

1. Search the Research Data Catalog.
2. Search the supplier in BUY.IU. Students cannot.
3. Search IUCAT or the IU Libraries A–Z database list.
4. Ask a subject librarian, or Research Data Services at resdata@iu.edu
   (from the [IU Libraries Research Data Services page](https://libraries.indiana.edu/research-data-services), not the IU KB).

If IU does not have it, `using-licensed-and-public-data` covers buying data.
**Recommended.** Before buying, email iurdc@iu.edu (from the [RDC contact page](https://researchdata.iu.edu/about/contact/), not the IU KB). The RDC catalog exists
partly "to reduce redundancies in data acquisition."

## Suggest an addition

Anyone can propose a dataset for the catalog by emailing iurdc@iu.edu, per
the catalog's About page. No IU KB article lists the address.

**Recommended.** When a lab holds licensed or shareable data that others at
IU could use, list it in the catalog. A listing prevents duplicate purchases.
It also means the data keeps a contact after the person who acquired it
leaves.

## Keep this file current

- Run `scripts/rdc_catalog.py check`. It reports entries whose `updated_at`
  changed, and entries that no longer exist. Update the row in
  `references/catalog.md`, including its date.
- Run `scripts/rdc_catalog.py new`. It reads the home page listing, newest
  first, and reports entries not in `references/catalog.md`. Run `show` on
  each, and add its row. It exits 2 if the listing returns the human check
  or changes shape. Then a person must browse the listing at
  https://researchdatacatalog.iu.edu/?sort=system_modified_dtsi+desc&per_page=100
  and compare it by hand.
- Re-read each source in `references/inventory.md` every quarter, and
  update its Observed date. `tools/check-skills.py --links` checks its URLs
  monthly. Move a row to `references/catalog.md` when the catalog adds it,
  and tell the RDC about rows it lacks.
- **Open item.** Both `researchdata.iu.edu` and `rdc.iu.edu` serve the RDC
  site, with no redirect. This skill uses `researchdata.iu.edu`, which the
  catalog links back to. Ask iurdc@iu.edu which host is canonical.
- **Open item.** Catalog entries carry no data classification. Ask the RDC
  whether one will be added.

## Sources

Checked 2026-10-04.

- Research Data Catalog and About page: https://researchdatacatalog.iu.edu,
  https://researchdatacatalog.iu.edu/about
- Catalog home page listing, newest first, read by `rdc_catalog.py new`
  (Observed 2026-11-03):
  https://researchdatacatalog.iu.edu/?sort=system_modified_dtsi+desc&per_page=100
- Data Cataloging Working Group:
  https://researchdata.iu.edu/about/working-groups/data-cataloging/
- RDC Resource Catalog: https://researchdata.iu.edu/resource-catalog/
- Featured Data Program:
  https://researchdata.iu.edu/resources/featured-data-program/
- RDC FAQ, "Determine whether IU already owns it":
  https://researchdata.iu.edu/faqs/acquiring-data/determine-whether-iu-already-owns-it/
- All 35 catalog entry pages and their JSON, listed in
  `references/catalog.md`.
- RDC contact page: https://researchdata.iu.edu/about/contact/
- IU Libraries Research Data Services:
  https://libraries.indiana.edu/research-data-services
- RDC DMP consultation: https://researchdata.iu.edu/resources/dmp-consultation/
- The IU and partner pages listed in `references/inventory.md`, each with
  its own Observed date (checked 2026-11-05).
