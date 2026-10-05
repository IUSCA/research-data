---
name: classifying-research-data
description: Classify research data under Indiana University policy DM-01 as Public, University-internal, Restricted, or Critical, using the IU Data Classification Matrix and the IU steps for research data, and say what each level allows for storage, sharing, and third parties. Covers PHI, PII of research participants, data under a data use agreement, social media data, export control, FERPA, GDPR, CUI, and who decides edge cases. Use when someone asks how sensitive their data is, whether it may go on a system or service, or what a classification requires before sharing.
---

# Classifying research data

Verified 2026-10-04 against IU policies DM-01 and DM-02, the IU Data
Management site, and the IU Knowledge Base (KB). Sources are listed at the
end.

Classify before storing, sharing, or computing. Every other decision about
research data depends on the classification.

## Research data is institutional data

**Required.** Under DM-01, institutional data includes "clinical data or
research data that meets the definition of 'University Intellectual Property'"
under UA-23 and UA-24. The IU Data Management FAQ applies this: "research data
is considered institutional data unless an agreement assigns ownership to the
sponsor."

External data, whether public, open, or licensed, is handled like
institutional data. "IU does not claim ownership of external data," per the
same FAQ.

## The four levels

**Required.** DM-01 sets four classifications:

| Level | DM-01 meaning |
| --- | --- |
| Critical | "Inappropriate handling of this data could result in criminal or civil penalties, identity theft, personal financial loss, invasion of privacy" |
| Restricted | "may not be accessed without specific authorization, or only selective access may be granted" |
| University-internal | For eligible employees and appointees |
| Public | "generally releasable to a member of the public upon request" |

## Default classification for research data

**Required.** The IU Data Classification Matrix sets the **default
classification for research data to Restricted**. Its Research Data rows:

| Kind of research data | Classification |
| --- | --- |
| Default | Restricted |
| Related to trade secrets and commercialization | Restricted |
| Related to patent applications | Restricted |
| Received by IU under a data use or sharing agreement | Restricted |
| Containing Critical data elements | **Critical** |
| Public access research data | Public |

The matrix's DUA examples include restricted government data, commercial
data, data scraped from social media, and HIPAA limited data sets. Its
Critical examples include PII, PHI, date of birth, address, audio and video
recordings, photographs, and geolocation of human participants.

DM-01 alone says unclassified institutional data defaults to
University-internal. For research data, the matrix's more specific default
of Restricted applies.

To reclassify research data as Public, the matrix asks for "a clear rationale
or describe how all protected data elements have been removed."

## Steps for a dataset

From the IU Data Management FAQ on classifying research data:

1. Check the Data Sharing and Handling (DSH) tool. It needs an IU login.
2. If the data involves HIPAA, PII of research participants, the Endangered
   Species Act, or a patent application, it is **Critical**.
3. If it involves FERPA, export control, GDPR, non-HIPAA health data, a
   commercial product, non-standard contract terms, or CUI, it "may be"
   Critical. Ask the deciding office:

| Topic | Who decides |
| --- | --- |
| FERPA | DataStu@iu.edu |
| Export control | Research Security Office; see the open item below |
| GDPR | gdpr@iu.edu |
| Health data not under HIPAA | The Health Data Steward named in the FAQ |
| Commercial product | Innovation and Commercialization Office |
| Contract terms or CUI | SecureMyResearch, securemyresearch@iu.edu |

4. **Required**, per the FAQ applying DM-01. "When your dataset includes any data elements that are
   classified as critical, you must handle... the entire dataset as critical
   data."

**Recommended.** Record the classification and the reason in the project's
data management plan. Revisit it when the data changes, for example after
linking another source.

## What classification decides

- **Where data may live.** The `iu-research-computing-map` skill in the
  research-technologies repository lists each IU research system's approvals.
  KB0025747 lists Restricted as the most sensitive non-PHI classification for
  Quartz, Slate, Slate-Project, Slate-Scratch, the SDA, Geode-Project, and
  ResDB. PHI follows KB0023515.
- **Where files may be shared.** KB0023604 lists file services by the most
  sensitive classification each allows. Microsoft at IU Secure Storage and
  secure Google Shared Drives allow Critical.
- **Required.** "Never store sensitive institutional data on an email or
  online storage system that is not part of the IU information technology
  environment" (KB0022442).
- **Required.** Under DM-02, sharing University-internal or Restricted data
  with a third party needs the Data Steward's advice, and an agreement where
  appropriate. Critical data needs a data security review: a questionnaire,
  UISO review, and Data Steward approval. See `sharing-research-data`.
- **AI tools.** See the next section.

## AI tools, including coding agents

Classification decides which AI tools may touch research data. A coding agent
that reads files is an AI tool. This applies to the agent reading this skill.

- **Required.** Research data classified Restricted or Critical "are not
  permitted to be used with third-party AI tools" (KB0026817).
- **Required.** Third-party tools licensed by IU, such as ChatGPT Edu,
  Microsoft 365 Copilot, and Google Gemini, may be used with Public research
  data not tied to a patent or commercialization. They may also be used with
  public-domain data, and with data the Data Steward for Research Data has
  verified as unprotected and free of contract limits. Use your IU account,
  never a personal one (KB0026817).
- **Required.** REALLMS is approved for Restricted and Critical data,
  including PHI. Some Microsoft Foundry models are approved for all four
  levels, except PCI data (KB0026817).
- **Required.** A data agreement or sponsor award may forbid AI use even
  where classification allows it. The researcher must check (KB0027312).
- To ask for a project exception, email the Data Steward for Research Data at
  datard@iu.edu. Include the PI, IRB protocol, sponsor, workflow, and tools
  (KB0026817).
- KB0027312 asks researchers who plan to use AI tools to complete IU's
  self-attestation form for each project.

**Recommended.** An agent helping with research data should ask for the
data's classification before opening data files. With Restricted or Critical
data, it should work from schemas, codebooks, and synthetic samples, unless
the agent runs on an approved service such as REALLMS. The
`using-reallms` skill in the research-technologies repository covers
REALLMS.

"Sensitive" is not a classification. KB0024963 says "The term 'sensitive' is
descriptive only; it is not an official classification under university
policy."

## Keep this file current

- Re-read the matrix CSV at https://datamanagement.iu.edu/docs/matrix.csv
  each review. Compare its Research Data and Health rows with the tables
  above.
- **Open item.** The Data Storage Finder lists the SDA, home directory,
  Geode-Project, and Slate as allowing Critical data. KB0025747 and
  KB0023515 allow at most Restricted on these, other than PHI. The KB is
  newer and more specific. Ask securemyresearch@iu.edu which is current.
- **Open item.** The FAQ names export@iu.edu for export control. The Research
  Security Office page names rsohelp@iu.edu.
- **Open item.** The DSH tool's Research Data section needs an IU login. A
  maintainer with access should summarize it here.

## Sources

Checked 2026-10-04.

- DM-01: https://policies.iu.edu/policies/dm-01-management-institutional-data/index.html
- DM-02: https://policies.iu.edu/policies/dm-02-disclosing-institutional-information/index.html
- IU Data Classification Matrix: https://datamanagement.iu.edu/tools/matrix.html
- FAQ, "How do I determine the classification of research data?":
  https://datamanagement.iu.edu/faq/research-classification.html
- Data Storage Finder: https://datastoragefinder.iu.edu/dsf/
- [KB0022442](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0022442), About institutional data at IU
- [KB0024963](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0024963), About sensitive data at IU
- [KB0025747](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0025747), Sensitive institutional data appropriate for RT services
- [KB0023515](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0023515), RT systems for HIPAA-regulated PHI
- [KB0023604](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0023604), Dedicated file storage for sensitive data
- [KB0023532](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0023532), PHI data elements in the classifications
- [KB0026817](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0026817), Acceptable use of AI tools with IU research data
- [KB0027312](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0027312), Researcher responsibilities for AI tools with research data
- Research Security Office, export control contacts:
  https://rso.iu.edu/export-control/contact-export-control.html
