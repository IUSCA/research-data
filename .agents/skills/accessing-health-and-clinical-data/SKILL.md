---
name: accessing-health-and-clinical-data
description: Request and use health and clinical research data at Indiana University, including the Indiana Network for Patient Care (INPC), IU Health and Eskenazi records through Regenstrief Data Services, the Indiana Biobank (DNA, omics, and linked clinical data), HCUP, MarketScan claims, All of Us, the Human Connectome Project, Alzheimer's resources (NCRAD and the Indiana ADRC), and biospecimen data from BC2 and the Komen Tissue Bank. Covers feasibility counts, honest-broker extraction, IRB and HIPAA requirements, data use agreements, and where the data must be analyzed. Use when someone needs patient or medical records (EHR), a clinical population with certain medical histories, biobank samples or genotype data, insurance claims, hospital discharge, or other patient-level data for a study at IU.
---

# Accessing health and clinical data

Verified 2026-11-05 (the Indiana Biobank, NCRAD, Indiana ADRC, and
Indiana CTSI Data Science and Informatics pages only). Verified 2026-10-08
(the MarketScan catalog entry only) against the Research Data Catalog.
Other sources were verified 2026-10-04 against
Regenstrief Data Services, Indiana CTSI, IU Research, IU Data Management,
and Research Data Catalog pages. Sources are listed at the end.

Patient-level data is the most tightly controlled data at IU. Settle three
things before anything else: IRB status, who holds the identifiers, and where
the analysis may run.

## When to ask a person

These questions need an IU office or a data provider. Contacts are from
`getting-help-with-research-data` and the sections below.
Read the KB article cited with a contact for its current form, and cite it.
A contact marked "not the IU KB" comes from the page named with it.

| Situation | Ask | Send |
| --- | --- | --- |
| INPC, IU Health, or Eskenazi data, including which RDS form to use | Regenstrief Data Services, askrds@regenstrief.org (from the [Regenstrief Data Services page](https://www.regenstrief.org/rds/), not the IU KB) | The cohort criteria; for extraction, the IRB approval and award |
| IRB approval or a HIPAA authorization | Human Research Protection Program, irb@iu.edu ([KB0024110](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0024110)) | The IRB protocol number or draft, and the data sources |
| Whether data holds PHI, or what HIPAA requires of you | HIPAA Privacy Officer, hipaa@iu.edu ([KB0023532](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0023532)) | The data elements and where they will be stored |
| Signing a data agreement | ORA Research Contracting, Unfunded Agreement Request Form in One.IU (from [IU Research, other agreements](https://research.iu.edu/awards-agreements/research-agreements/other-agreements.html), not the IU KB) | The agreement, the data, and the IRB protocol |
| Indiana Biobank samples, omics, or linked data; quotes and letters of support | Indiana Biobank, inbiobnk@iu.edu (from the [Indiana Biobank access page](https://indianabiobank.org/access-samples), not the IU KB) | The cohort criteria, the specimen or data types, and any grant deadline |
| HCUP access | Social Science Research Commons, ssrc@iu.edu (from the [RDC RADaRS page](https://researchdata.iu.edu/resource-catalog/radars/), not the IU KB) | The database, your role and campus, and your deadline |

**Recommended.** In these cases, say plainly that the question needs a
person. Name the office and what to send. Do not offer a best guess as the
answer. Only the office can decide, and a guess can lead a researcher to
break an agreement or a rule.

For any other question, see `getting-help-with-research-data`.

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
| DNA, omics, and EHR-linked data on consented Indiana patients | Indiana Biobank | De-identified data in a secure enclave | Portal request and review; DUA and terms of access; IU collaborator for outside researchers |
| Alzheimer's and dementia biospecimens and data | NCRAD; Indiana Alzheimer's Disease Research Center | Sample-linked | Review committee; cost recovery may apply |

Read the live catalog entry before giving steps. `finding-iu-research-data`
explains how. The Indiana Biobank, NCRAD, and the Indiana ADRC are not in
the catalog (Observed 2026-11-05). Its inventory file,
`references/inventory.md` in `finding-iu-research-data`, lists them.

**Recommended.** For "a clinical population with certain medical
histories," compare three routes. INPC through RDS gives the broadest
records. The Indiana Biobank adds DNA and omics for consented patients.
All of Us gives a national cohort. Get feasibility counts from each before
choosing.

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
identified data. Contact askrds@regenstrief.org (from the [Regenstrief Data Services page](https://www.regenstrief.org/rds/), not the IU KB).

Tools RDS offers include ATLAS (OHDSI) and nDepth for clinical text. RDS also
takes part in N3C, PCORnet, OHDSI, and the ACT network.

**Recommended.** Ask RDS for feasibility counts before writing the IRB
protocol. Counts show whether the cohort is large enough, at no cost.

**Recommended.** Use the acknowledgment RDS asks for: "Regenstrief
Institute, Inc.'s participation in this project is acknowledged for access to
and expertise in data management."

## Indiana Biobank

**Observed 2026-11-05** on indianabiobank.org. The Indiana Biobank is "a
statewide initiative, co-developed by Indiana University School of Medicine
and IU Health," established in 2010.

- **What it holds.** It "collects and banks DNA specimens for broad
  sharing." It "only offers DNA specimens for broad sharing." It banks other
  specimen types, such as plasma, serum, and PBMC, for specific studies.
- **Linked data.** Specimens link to the INPC for "de-identified clinical
  data, including clinical progression and outcomes data." For certain
  cohorts, omics data include whole exome sequencing, genome-wide genotype
  (GWAS) data, RNA transcriptomics, and HLA haplotypes.
- **Consent.** "Each subject is consented to allow for broad-use of
  specimens by approved researchers."
- **Diagnoses.** A Common Diagnoses page lists about 60 diagnoses with
  subject counts. Use it for a first feasibility check:
  https://indianabiobank.org/access-samples/common-diagnoses
- **Data portal.** Its cohort browser of aggregated data is "Open to anyone."
  To get data, create an account, build a cohort, and request its
  de-identified data. Requests are reviewed against the Biobank's
  "scientific and ethical standards." Approved users analyze in "a secure
  enclave that allows analysis but limits data export."
- **Who.** "Researchers outside of IU will be required to have an IU
  collaborator involved in their project."
- **Required.** Per the Biobank's agreements page, data release needs a
  Data Use Agreement. Specimens need an Internal Transfer Agreement for IU
  researchers, or a Material Transfer Agreement for outside organizations.
  The portal page adds "a Terms of Access Agreement."
- **Quotes and letters.** Request a quote or a letter of support on its
  request-a-quote page. Contact inbiobnk@iu.edu (from the
  [request-a-quote page](https://indianabiobank.org/study-support/request-a-quote), not the IU KB).
- The Provena Consortium, linked from the Biobank site, offers "limited,
  de-identified datasets" to academic and industry partners.

**Open item.** The Biobank's pages differ on its size. The home page says
"over 80,000 patients have consented." The access page says "DNA specimens
from over 60,000 residents." Neither page states IRB requirements or fees.
Ask inbiobnk@iu.edu (from the [access page](https://indianabiobank.org/access-samples), not the IU KB).

## Alzheimer's and dementia resources

- **NCRAD**, the National Centralized Repository for Alzheimer's Disease and
  Related Dementias, is "a biorepository operated by Indiana University with
  funding from the National Institute on Aging." Register, select samples
  from its catalog, and apply. Its Biospecimen Review Committee reviews
  requests, and "The approval is valid for 12 months." Contact
  alzstudy@iu.edu, or ncradbrc@iu.edu for samples not in the catalog. Both
  are from the [NCRAD request page](https://ncrad.iu.edu/access-samples/request-samples), not the IU KB.
  Observed 2026-11-05 on ncrad.iu.edu.
- **Indiana Alzheimer's Disease Research Center (IADRC)** offers
  participants, specimens (DNA, RNA, plasma, serum, CSF, PBMC), brain tissue,
  imaging, and clinical, genetic, and neuropathological data. Submit its
  Resource Request Form. "A cost recovery fee may be charged." Contact
  iadrc@iu.edu (from the [IADRC resource request page](https://medicine.iu.edu/research-centers/alzheimers/for-researchers/resource-request), not the IU KB).
  Observed 2026-11-05.

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
  names the ACT network for CTSA feasibility. Indiana CTSI Data Science and
  Informatics names the ACT Network and OHDSI Atlas for cohort discovery
  (Observed 2026-11-05).
- **Open item.** Regenstrief now has a "Regenstrief Data Core" page, which
  calls itself "a central point of access for data from the Indiana Network
  for Patient Care." The RDS page still calls RDS "Indiana's honest data
  broker." Both were live on 2026-11-05. Ask askrds@regenstrief.org which
  name and request path is current.
- Re-read the Indiana Biobank's portal, agreements, and sample-type pages
  each review. Its enrollment is growing fast, so counts age quickly.
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
- External: Regenstrief Data Core (checked 2026-11-05),
  https://www.regenstrief.org/real-world-solutions/regenstrief-data-core/
- Indiana Biobank (checked 2026-11-05): https://indianabiobank.org/,
  /access-samples, /access-samples/biobank-data-portal,
  /access-samples/common-diagnoses, /access-samples/provena,
  /study-support/sample-types-we-bank, /study-support/mta-ita, and
  /study-support/request-a-quote
- NCRAD (checked 2026-11-05): https://ncrad.iu.edu/ and
  https://ncrad.iu.edu/access-samples/request-samples
- Indiana ADRC resource request (checked 2026-11-05):
  https://medicine.iu.edu/research-centers/alzheimers/for-researchers/resource-request
- Indiana CTSI Data Science and Informatics (checked 2026-11-05):
  https://indianactsi.org/research/data-informatics/
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
- [KB0024110](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0024110), About Terracotta at IU: irb@iu.edu for IRB approval questions, read 2026-11-05
- [KB0023532](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0023532), PHI data elements in the classifications: hipaa@iu.edu, read 2026-11-05
- IU Research, other research agreements:
  https://research.iu.edu/awards-agreements/research-agreements/other-agreements.html
- RADaRS: https://researchdata.iu.edu/resource-catalog/radars/
