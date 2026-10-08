# Research Data Catalog snapshot

**Observed 2026-10-04** from each entry page and its JSON at
`https://researchdatacatalog.iu.edu/concern/data_sets/<id>.json`. The
catalog then held 35 entries.

This is a snapshot for matching questions to datasets. The live entry is the
source of truth for access terms, contacts, and eligibility. Read it before
telling anyone how to get access:

```bash
scripts/rdc_catalog.py show <id or title words>
```

`Updated` is the entry's `updated_at` date. `scripts/rdc_catalog.py check`
compares it with the live entry and reports changes. "Who" abbreviates the
catalog's Access Eligibility field: F faculty, S staff, G graduate student,
U undergraduate, P public.

No entry states an IU data classification. See `classifying-research-data`
before you store or share any of this data.

## Health, clinical, and biospecimen data

| Dataset | Entry | Host | Who | Campus | Access route | Data location | Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Indiana Network for Patient Care (INPC) | [9f2b91f4](https://researchdatacatalog.iu.edu/concern/data_sets/9f2b91f4-1a80-48e8-81be-225a98d4bdf2) | Not stated (Regenstrief Data Services) | F S G U | All | IU IRB approval, HIPAA training, signed data agreement; request through Regenstrief | Regenstrief | 2025-08-22 |
| HCUP National Inpatient Sample (NIS) | [be7ec5af](https://researchdatacatalog.iu.edu/concern/data_sets/be7ec5af-f832-495b-8d9f-f4d12410c4ae) | RDC; SSRC | F G U* | All | Canvas course; HCUP training and DUA; CITI and HIPAA current | RADaRS; Slate Project | 2025-09-04 |
| HCUP Nationwide Emergency Department Sample (NEDS) | [b8f68b31](https://researchdatacatalog.iu.edu/concern/data_sets/b8f68b31-e263-4460-87fc-3f63ff911726) | RDC; SSRC | F G U* | All | Same as NIS | RADaRS; Slate Project | 2025-09-04 |
| HCUP Nationwide Ambulatory Surgery Sample (NASS) | [5988c2d3](https://researchdatacatalog.iu.edu/concern/data_sets/5988c2d3-7dde-45f5-a76a-f0306bc90339) | RDC; SSRC | F G U* | All | Same as NIS | RADaRS; Slate Project | 2025-09-05 |
| HCUP Indiana State Inpatient Database (IN SID) | [adf29078](https://researchdatacatalog.iu.edu/concern/data_sets/adf29078-743f-4e2a-a1d3-fcdc9e8bb2fb) | SSRC | F S G U | All | Not stated on the entry; ask the public contact | Not stated | 2025-06-26 |
| MarketScan (Merative) | [dc3c0bf0](https://researchdatacatalog.iu.edu/concern/data_sets/dc3c0bf0-f704-4ef8-9924-2442e33e50c2) | RDC | F S G† | All | Request through RDC; documentation needs an NDA; grant-funded use carries a fee; 45-day trial first | UITS RT HPC only | 2026-10-05 |
| All of Us | [4c807d32](https://researchdatacatalog.iu.edu/concern/data_sets/4c807d32-8f68-4e5d-bc22-e609c361ebde) | Not stated | F S G U P | All | Public tier open; registered and controlled tiers under IU's institutional DURA, with training | All of Us Researcher Workbench | 2025-02-08 |
| Human Connectome Project (HCP) | [dbf207bb](https://researchdatacatalog.iu.edu/concern/data_sets/dbf207bb-4c15-4003-87c7-77e6a173a53a) | RDC | F S G U* | IUB | RDC access form plus the HCP data use terms | Slate Project | 2026-04-14 |
| Biospecimen Collection and Banking Core (BC²) | [96a10a83](https://researchdatacatalog.iu.edu/concern/data_sets/96a10a83-a68a-4a48-aaf6-0103bc809a65) | BC² | Not stated | Not stated | Proposal reviewed by a Sample Access Committee | BC² | 2025-02-08 |
| Komen Tissue Bank (KTB) | [2a3a2553](https://researchdatacatalog.iu.edu/concern/data_sets/2a3a2553-e982-4f70-ae7f-7f4027092c16) | Komen Tissue Bank | F S G U P | All | Breast cancer research only; request through KTB | KTB | 2025-02-20 |

\* Undergraduates need a faculty sponsor.
† Graduate students must be PhD students on an existing faculty project.

## Social media and information operations (OSoMe)

The Observatory on Social Media hosts these. Most requests go through the
OSoMe data request form named on each entry.

| Dataset | Entry | Who | Access route | Updated |
| --- | --- | --- | --- | --- |
| BlueSky Archive | [1b894441](https://researchdatacatalog.iu.edu/concern/data_sets/1b894441-3bff-4077-bd3d-4c03eb86676c) | F S G U P | OSoMe request form | 2026-04-29 |
| BlueSky Day 1 Archive | [14db5333](https://researchdatacatalog.iu.edu/concern/data_sets/14db5333-acb7-4497-a252-69ab2da6cc42) | F S G U P | OSoMe request form; not anonymized, so seek IRB review | 2026-07-09 |
| Mastodon Archive | [99c2892f](https://researchdatacatalog.iu.edu/concern/data_sets/99c2892f-8638-48e5-9587-cd174f51580a) | F S G U P | OSoMe request form | 2026-07-13 |
| 2022 Midterm Election Raw Data | [23fd423b](https://researchdatacatalog.iu.edu/concern/data_sets/23fd423b-fe7b-4c67-bfc8-812e09d6896d) | F S G U | OSoMe request form | 2025-06-26 |
| CoVaxxy Raw Data | [b6f4ff2f](https://researchdatacatalog.iu.edu/concern/data_sets/b6f4ff2f-a0bb-4c79-9de8-4ae41dc6831b) | F S G U | OSoMe request form | 2026-04-09 |
| OSoMe: Trains Raw Data | [8c299de5](https://researchdatacatalog.iu.edu/concern/data_sets/8c299de5-0ad5-40af-8975-8dd5396f8b59) | F S G U | OSoMe request form | 2025-09-04 |
| Vendor Purchased Bot Raw Data | [08fa6b51](https://researchdatacatalog.iu.edu/concern/data_sets/08fa6b51-86a4-4b67-af8f-2a8446cd5b9a) | F S G U P | OSoMe request form for a sample | 2026-04-14 |
| Media Bias Fact Check list | [93d3fb50](https://researchdatacatalog.iu.edu/concern/data_sets/93d3fb50-8083-4642-a8af-5b2a9e3178e5) | F S G U P | OSoMe request form | 2026-04-14 |
| IO Datasets | [d11b79ea](https://researchdatacatalog.iu.edu/concern/data_sets/d11b79ea-3cd2-4169-821a-5e67cb76fec2) | F S G U P | Request on Zenodo | 2026-04-14 |
| OSoMe Publication Data | [3eebfe98](https://researchdatacatalog.iu.edu/concern/data_sets/3eebfe98-018a-442b-bce5-b75de344747e) | F S G U P | Public on Zenodo | 2026-04-14 |
| Botometer Pro API | [c82f2fec](https://researchdatacatalog.iu.edu/concern/data_sets/c82f2fec-1306-4b7b-a989-a2b58930fdc5) | F S G U P | Public API on RapidAPI | 2026-04-14 |

## Business, economics, and real estate (Kelley School of Business)

All are IU Bloomington only.

| Dataset | Entry | Who | Access route | Updated |
| --- | --- | --- | --- | --- |
| Wharton Research Data Services (WRDS) | [4c7c896f](https://researchdatacatalog.iu.edu/concern/data_sets/4c7c896f-08be-431c-9afb-f7370e9b1b18) | F S G U | Request a WRDS account | 2025-02-20 |
| NielsenIQ | [02a69c23](https://researchdatacatalog.iu.edu/concern/data_sets/02a69c23-2ed9-4515-82e7-51ce240467b4) | F G‡ | Account through the Kilts Center | 2026-05-22 |
| CoreLogic Loan-Level Market Analytics | [7dc5cf82](https://researchdatacatalog.iu.edu/concern/data_sets/7dc5cf82-26df-4e89-83b4-4c5e1c2e04de) | F S G U P | End User License Agreement | 2025-02-08 |
| CoreLogic Non-Agency RMBS | [8d303d3e](https://researchdatacatalog.iu.edu/concern/data_sets/8d303d3e-d576-43be-ba2f-67f25de9b4b3) | F S G U P | End User License Agreement | 2025-05-02 |
| CoreLogic Tax and Deed Data | [29c46949](https://researchdatacatalog.iu.edu/concern/data_sets/29c46949-48e2-45b7-b2ed-11334622ed78) | F S G U P | End User License Agreement | 2025-02-08 |

‡ Tenured and tenure-track faculty, PhD students, and postdocs.

## Library-licensed and scholarly data

| Dataset | Entry | Host | Who | Campus | Access route | Updated |
| --- | --- | --- | --- | --- | --- | --- |
| Web of Science XML dataset | [1b9e9a7d](https://researchdatacatalog.iu.edu/concern/data_sets/1b9e9a7d-00ad-46a4-a962-1f400d8d43e1) | RDC | F S G U* | IUB | RDC request form; data on Slate Project | 2026-04-14 |
| HathiTrust Research Center (HTRC) | [56b6a45e](https://researchdatacatalog.iu.edu/concern/data_sets/56b6a45e-d084-4adc-8ca3-3b5d730e7054) | HathiTrust | F S G U | All | Sign in at HTRC Analytics with IU | 2025-02-08 |
| Linguistic Data Consortium (LDC) | [60d55dea](https://researchdatacatalog.iu.edu/concern/data_sets/60d55dea-9bf1-4a9a-96e8-c46c57cc2d0b) | IU Libraries | F S G U | IUB | IU login; ask the Libraries to buy a dataset not held | 2025-02-20 |
| Cross-National Time Series (CNTS) | [337e8ff7](https://researchdatacatalog.iu.edu/concern/data_sets/337e8ff7-c888-4391-bbd8-37382d904ace) | IU Libraries | F S G U | IUB | IU login | 2025-02-08 |
| Gallup Analytics | [a631b2d8](https://researchdatacatalog.iu.edu/concern/data_sets/a631b2d8-5e9b-4208-9ac9-32685d82c7aa) | IU Libraries | F S G U P | IUB | IU login | 2025-02-08 |
| ProQuest Statistical Insight | [aaef4998](https://researchdatacatalog.iu.edu/concern/data_sets/aaef4998-28cc-4db4-82c7-f2e0bcebb98b) | IU Libraries | F S G U | IUB | IU login | 2025-05-01 |
| Sage Data | [04f03cb7](https://researchdatacatalog.iu.edu/concern/data_sets/04f03cb7-885b-4275-88de-0e0872db9488) | IU Libraries | F S G U | IUB | IU login | 2025-02-24 |
| Big Ten Academic Alliance Geoportal | [051aa0d6](https://researchdatacatalog.iu.edu/concern/data_sets/051aa0d6-bfa5-41a0-b92a-2e7c7c3c70c4) | IU Libraries | F S G U P | All | Open | 2025-02-08 |
| SAVI Community Information System | [48635252](https://researchdatacatalog.iu.edu/concern/data_sets/48635252-0d84-47b5-8856-953aa66cfaac) | The Polis Center | F S G U P | All | SAVI website | 2025-02-20 |

## Known catalog problems

- **Open item.** The Web of Science entry gives coverage as "1990 -2023" in
  Timeframe and "1900 through 2023" in its description. Observed 2026-10-04.
- **Open item.** HCUP IN SID has no Access Instructions. Observed 2026-10-04.
- The older catalog paths under `researchdata.iu.edu/data-catalog/` returned
  HTTP 404 on 2026-10-04. Link to `researchdatacatalog.iu.edu` instead.
