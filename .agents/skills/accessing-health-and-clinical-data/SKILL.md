---
name: accessing-health-and-clinical-data
description: Request and use health and clinical research data at Indiana University, including the Indiana Network for Patient Care (INPC), IU Health and Eskenazi records through Regenstrief Data Services, HCUP, MarketScan claims, All of Us, the Human Connectome Project, and biospecimen data from BC2 and the Komen Tissue Bank. Covers feasibility counts, honest-broker extraction, IRB and HIPAA requirements, data use agreements, and where the data must be analyzed. Use when someone needs EHR, claims, hospital discharge, or patient-level data for research at IU.
---

# Accessing health and clinical data

Verified 2026-10-08 (the MarketScan catalog entry only) against the
Research Data Catalog. Other sources were verified 2026-10-04 against
Regenstrief Data Services, Indiana CTSI, IU Research, IU Data Management,
and Research Data Catalog pages. Sources are listed at the end.

Patient-level data is the most tightly controlled data at IU. Settle three
things before anything else: IRB status, who holds the identifiers, and where
the analysis may run.

## Choose the source

| Need | Source | Identifiable? | Typical burden |
| --- | --- | --- | --- |
| Indiana patients' EHR across health systems | INPC through Regenstrief Data Services (RDS) | RDS extracts and de-identifies; identified data needs extra approval | IRB, data agreement, analyst cost |
| IU Health or Eskenazi records | RDS, under its business agreements with both systems | As above | As above |
| National hospital inpatient, ED, or ambulatory surgery stays | HCUP NIS, NEDS, NASS | De-identified | Canvas course, HCUP training and DUA |
| Indiana hospital stays | HCUP IN SID | De-identified | Ask the catalog contact; no access steps posted |
| Commercial, Medicare, and Medicaid claims | MarketScan | De-identified | RDC request, NDA for documentation, RT HPC only |
| Diverse national cohort with EHR, surveys, and genomics | All of Us | Tiered | Registration and training; IU holds an institutional DURA |
| Neuroimaging | Human Connectome Project | De-identified | RDC form plus HCP terms |
| Tissue and biospecimens | BC² and Komen Tissue Bank | Sample-linked | Committee proposal |

Read the live catalog entry before giving steps. `finding-iu-research-data`
explains how.

## INPC, IU Health, and Eskenazi: Regenstrief Data Services

**External.** RDS calls itself "the central point of access to data from the
Indiana Network for Patient Care, as well as the electronic medical record
data warehouses for IUHealth and Eskenazi." Regenstrief is "the Honest Data
Broker" for the INPC and two hospital systems.

- **Required.** Under the INPC terms, "only they are allowed direct access to
  the identifiable patient data." Researchers receive extracts, not access to
  the source (RDS data page).
- The INPC research database is managed by the Indiana Health Information
  Exchange (IHIE). Researchers do not request data from IHIE directly.

The request path, per RDS:

1. **Feasibility.** Aggregate counts are "provided at no cost to Regenstrief
   and Indiana CTSI member investigators."
2. **Extraction.** **Required** by RDS terms: IRB approval "from either IU, Purdue, or
   Notre Dame or an approved reliance request," and an award. RDS "doesn't
   sell the data but we do require the cost of the analyst's time be
   covered."
3. **De-identification.** "RDS uses HIPAA Safe Harbor standards to
   de-identify all datasets."

The INPC catalog entry adds: research purpose only, IU IRB approval, current
HIPAA training, a signed data agreement, and INPC institutional approval for
identified data. Contact askrds@regenstrief.org.

Tools RDS offers include ATLAS (OHDSI) and nDepth for clinical text. RDS also
takes part in N3C, PCORnet, OHDSI, and the ACT network.

**Recommended.** Ask RDS for feasibility counts before writing the IRB
protocol. Counts show whether the cohort is large enough, at no cost.

**Recommended.** Use the acknowledgment RDS asks for: "Regenstrief
Institute, Inc.'s participation in this project is acknowledged for access to
and expertise in data management."

## HCUP

The RDC and the Social Science Research Commons (SSRC) host the national
HCUP databases. For NIS, NEDS, and NASS, the entries say:

- IU faculty and graduate students may use them. Undergraduates need a
  faculty sponsor.
- **Required.** Complete the HCUP training and the HCUP data use agreement.
  Keep CITI and HIPAA certification current. These are the data provider's
  terms.
- Enroll in the Canvas course named on the entry to request access.
- The data lives on RADaRS and Slate Project.

## MarketScan

Per the catalog entry, observed 2026-10-08 (entry updated 2026-10-05):

- Commercial, Medicare, Medicaid, Dental, and National Weights products for
  2016 to 2024, with partial 2025 data.
- IU faculty, research staff, and PhD students on existing faculty projects.
- **Required.** "All analysis of the MarketScan data must be performed on
  UITS Research Technologies High Performance Computing Systems." This is
  the license term.
- Free for existing and internally funded projects. Grant-funded use
  "requires a fee to be written into the proposal budget before the grant
  is submitted."
- Documentation requires an NDA.
- Access runs in steps: the documentation form and NDA, a short Canvas
  course on the vendor's terms, a meeting with the Technical Data Custodian,
  then a 45-day trial on a large sample. Full data follows a summary of the
  proposed research and a workflow review. Plan for these steps before a
  project depends on the data.
- Data stays on UITS Research Technologies systems: Research Desktop,
  Quartz, Slate, and Slate Scratch.

The RDC posted a MarketScan Research Acceleration RFP on 2026-08-20. RDC staff
draft an initial analysis for accepted proposals. Proposals were accepted on
a rolling basis until November 1. Check the RDC news page for current status.

## All of Us

The catalog entry says "Indiana University has an institutional Data Use and
Registration Agreement (DURA)." The public tier is open. Registered and
controlled tiers need registration and the program's training.

## Handling the data once you have it

- **Required.** PHI and data with research-participant identifiers are
  **Critical** under DM-01, per the IU Data Classification Matrix. A dataset
  with any Critical element is handled entirely as Critical.
- **Required.** Data received under a DUA is at least **Restricted**, per the
  matrix. Its agreement may add terms.
- **Required.** Approval for PHI on a system does not meet your HIPAA duties.
  Add your own administrative, physical, and technical safeguards (KB0023515).
- Where PHI may be stored and computed on is covered by the
  [`iu-research-computing-map`](https://github.com/IUSCA/research-technologies/tree/main/.agents/skills/iu-research-computing-map) skill in the research-technologies repository.
  `classifying-research-data` covers the classification itself.
- **Required.** The human subjects data rules in the HRPP Research Data
  Management policy apply: retention of at least three years, and longer for
  HIPAA authorizations. See `navigating-research-data-policy`.

**Recommended.** Keep extracts inside the environment the data came to. Do
not copy subsets to laptops or personal cloud storage, even de-identified
ones, unless the data agreement and classification allow it.

## Keep this file current

- Re-read the RDS pages when a researcher reports a changed process.
- **Open item.** RDS links two REDCap request forms. Which is feasibility and
  which is extraction is inferred from page order. Confirm with
  askrds@regenstrief.org.
- **Open item.** No public IU Health research data request path outside RDS
  was found.
- **Open item.** No IU or Indiana CTSI page offering TriNetX was found. RDS
  names the ACT network for CTSA feasibility.
- **Open item.** The INPC size differs by source. The RDS data page says "10
  billion clinical observations." The CTSI service core page says "13 billion
  data elements."

## Sources

Checked 2026-10-04.

- External: Regenstrief Data Services, https://www.regenstrief.org/rds/,
  /rds/data/, /rds/services/, /rds/networks/, and /rds/faq/
- External: Indiana CTSI RDS service core,
  https://indianactsi.org/servicecores/core/75/
- External: IHIE, https://www.ihie.org/about-us/
- Research Data Catalog entries for INPC, HCUP NIS, NEDS, NASS, and IN SID,
  MarketScan, All of Us, HCP, BC², and KTB; links in the
  `finding-iu-research-data` catalog snapshot.
- RDC MarketScan RFP:
  https://researchdata.iu.edu/news-events/posts/2026-08-20-marketscan-research-acceleration-rfp/
- IU Data Classification Matrix: https://datamanagement.iu.edu/tools/matrix.html
- DM-01: https://policies.iu.edu/policies/dm-01-management-institutional-data/index.html
- HRPP Research Data Management policy:
  https://research.iu.edu/policies/human-subjects-irb/research-data-management.html
- [KB0023515](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0023515),
  RT systems for data containing HIPAA-regulated PHI
