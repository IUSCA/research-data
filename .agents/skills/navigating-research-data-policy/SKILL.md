---
name: navigating-research-data-policy
description: Navigate the rules for research data at Indiana University, which has no single research data policy. Separates what is required (DM-01, DM-02, UA-23, UA-24, HRPP policy, 2 CFR 200, NIH and NSF terms, NIH controlled-access security) from recommended practice, covering ownership, PI and team responsibilities, retention, disposal, departing researchers, NIH genomic and controlled-access data, and where policy is silent. Use when someone asks who owns research data, what a PI must do, how long data must be kept, whether something is required or only advised, or what to do where IU policy says nothing.
---

# Navigating research data policy

Verified 2026-10-04 against IU policies, the IU Data Management site, IU
Research, NIH, and eCFR. Sources are listed at the end.

IU has no single research data policy. Rules come from several policies,
federal regulations, and each project's agreements. This skill says which
rules bind, and recommends practice where none does.

## How to read this skill

- **Required** means a policy, law, regulation, or agreement binds the
  researcher. Each one names its source. Follow it.
- **Recommended** means no rule applies, and this repository advises the
  practice. Each one gives its reason. Adapt it to the project.
- When a sponsor's terms, an agreement, or consent is stricter than either,
  the stricter one governs.

Answer the question asked, then say which kind of answer it is. Never present
a recommendation as an IU rule.

## Status of an IU research data policy

The RDC announced in August 2025 that it had "received approval to support a
new comprehensive research data policy." Supporting that drafting was one of
its first-year priorities as a service unit. No draft or adopted policy was
public as of 2026-10-04. Until one is adopted, use the map in
[references/policy-map.md](references/policy-map.md). It shows, topic by
topic, what binds today and where the gaps are.

## Ownership

- **Required.** "At Indiana University, the Board of Trustees owns all data
  at the highest level, except for information excluded by Intellectual
  Property policies," per IU Data Management governance. The exclusions are
  set by UA-23 and UA-24.
- **Required.** Under UA-23, research data counts as university
  intellectual property "only when the data may have commercial value and/or
  be subject of sponsor or contractual obligations." Copyrightable works made
  with university funds, within the scope of employment, or with University
  Resources belong to IU. Scholarly works and some agreement terms are
  exceptions.
- **Required.** For human subjects research, the HRPP Research Data
  Management policy states: "Research data which is not generated pursuant to
  a contract or agreement that explicitly details ownership is the property
  of IU."
- **Required.** An agreement, such as a sponsor award, DUA, or collaboration
  agreement, can set ownership differently. Read it first.

In practice, treat research data done at IU, with IU resources, as IU's,
unless an agreement says otherwise. The PI is its custodian.

## Who is responsible for what

The PI is accountable for the project's data, however tasks are delegated.
Some duties are already required. Others are recommended.

| Duty | Status and source |
| --- | --- |
| Get IRB approval before human subjects research | **Required**, RP-11-004 and HRPP policy |
| Collect, manage, keep, and destroy human subjects data as custodian | **Required**, HRPP Research Data Management policy |
| Follow every agreement, license, and sponsor term on the data | **Required**, the agreements themselves |
| Classify data and use systems approved for it | **Required**, DM-01 and its standards |
| Never sign data agreements personally; go through ORA | **Required**, IU Research agreements process |
| Report suspected exposure of sensitive data | **Required**, IT-12 and the IU incident reporting process |
| Check AI tools against the data's classification | **Required**, KB0026817 |
| Keep a written data management plan for every project, including unfunded ones | **Recommended**; see `planning-data-management-and-sharing` |
| Record in that plan who handles which duties | **Recommended**; delegation is clear only if written down |
| Make sure team members finish required training before touching data | **Recommended**; the training itself is often required by the IRB or a DUA |
| Name a successor custodian for each dataset | **Recommended**; data outlives appointments |
| Consult research support offices before a project that needs special storage, agreements, or sharing | **Recommended**; capacity takes time to arrange |

**Recommended.** The rest of the team also shares responsibility. Each person
should know the data's classification, its agreements, and where it may be
stored.

## Retention and disposal

- **Required.** Federal award records must be kept "for three years from the
  date of submission of their final financial report," longer if litigation,
  claims, or audits are open (2 CFR 200.334).
- **Required.** Human subjects data must be kept at least 3 years after the
  final expenditure report or IRB closure, and 6 years for HIPAA
  authorizations (HRPP policy).
- **Required.** University records follow UA-18 and its retention schedules.
- IU's 2019 research data guidance recommends 5 years. The
  `planning-data-management-and-sharing` skill has the full table.

**Recommended.** Keep data that supports a publication for at least five
years after publication. Dispose of it only after the PI confirms no
agreement, audit, or dispute needs it. Record the disposal.

**Open item.** No IU policy sets a minimum retention period for research data
in general, or a disposal procedure. DM-01, DM-01-S, and DM-02 do not cover
retention, disposal, or archiving; see the policy map.

## NIH genomic and controlled-access data

- **Required.** Since January 25, 2025, users of human genomic data from NIH
  controlled-access data repositories must secure it per NIH's security best
  practices. These follow NIST SP 800-171 (NOT-OD-24-157).
- **Required.** From February 25, 2026, this extends to data from any NIH
  controlled-access repository, "as stipulated in new or renewed agreements,"
  per NIH's controlled-access data requirements page.
- **Required.** PIs attest to NIH that the system storing the data meets
  NIST SP 800-171. IU states that its administrators ensure "designated
  systems" meet the requirements.
- **Open item.** IU does not publicly name its designated systems. The KB
  article IU links for instructions, KB0026806, could not be found. Ask
  securemyresearch@iu.edu before requesting controlled-access data.
- NIH's draft Controlled-Access Data Policy (NOT-OD-26-023) is proposed, not
  in force. It would require controlled access for more kinds of data, such
  as precise geolocation, biometrics, and face or head imaging. Its comment
  period closed March 18, 2026.

## Where policy is silent

The questions below have no published IU answer. The repository's
`docs/open-items.md` lists each one with the office able to answer it. Do not invent an answer. Give the Recommended practice,
say it is a recommendation, and name the office to ask.

- When an affiliate account is enough for an outside collaborator, and when
  a data agreement is needed. See `sharing-research-data`.
- What a departing researcher may take, and how.
- A minimum retention period for research data in general.
- How disputes over access to data within a team are resolved.

Peer universities have adopted policies on these questions.
[references/peer-policies.md](references/peer-policies.md) summarizes them.
Use them as examples, not as IU rules.

## Keep this file current

- Watch the RDC news page for the research data policy. When IU adopts one,
  rewrite this skill around it and change each Recommended item it covers to
  Required.
- Re-read UA-23 each review. It had substantive revisions in August 2026.
- Watch NIH notices for a final controlled-access data policy.

## Sources

Checked 2026-10-04.

- IU Data Management governance: https://datamanagement.iu.edu/governance/index.html
- DM-01: https://policies.iu.edu/policies/dm-01-management-institutional-data/index.html
- DM-02: https://policies.iu.edu/policies/dm-02-disclosing-institutional-information/index.html
- UA-18: https://policies.iu.edu/policies/ua-18-university-records-retention-disposition/index.html
- UA-23: https://policies.iu.edu/policies/ua-23-intellectual-property-copyrightable-works/index.html
- UA-24: https://policies.iu.edu/policies/ua-24-intellectual-property-inventions-and-patents/index.html
- RP-11-004: https://policies.iu.edu/policies/rp-11-004-research-human-subjects/index.html
- IT-12: https://policies.iu.edu/policies/it-12-security-it-resources/index.html
- IU incident reporting: https://informationsecurity.iu.edu/report-incident/index.html
- HRPP Research Data Management policy:
  https://research.iu.edu/policies/human-subjects-irb/research-data-management.html
- IU Research, other research agreements:
  https://research.iu.edu/awards-agreements/research-agreements/other-agreements.html
- IU Guidance for the Management of Research Data:
  https://datamanagement.iu.edu/governance/policies/rdm-guidance.html
- IU NIH GDS update:
  https://datamanagement.iu.edu/governance/policies/nih-gds-policy-update.html
- RDC service unit announcement:
  https://researchdata.iu.edu/news-events/posts/2025-08-29-research-data-commons-established-as-service-center/
- KB0026806, linked from the IU NIH GDS update page; not found by KB search
  on 2026-10-04
- [KB0026817](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0026817), Acceptable use of AI tools with IU research data
- External: 2 CFR 200.334,
  https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-D/subject-group-ECFR4e2c2f81ba45d3c/section-200.334
- External: NIH controlled-access data requirements,
  https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/accessing-data/requirements
- External: NOT-OD-24-157, NIH GDS data management and access practices,
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-157.html
- External: NOT-OD-26-023,
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-023.html
