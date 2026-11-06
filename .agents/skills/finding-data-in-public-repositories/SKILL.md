---
name: finding-data-in-public-repositories
description: Find existing research data in public and controlled-access repositories outside any one university, and get access to it. Covers NIH and NCBI repositories (dbGaP, SRA, GEO, GDC, AnVIL, NIMH Data Archive, BioLINCC, NIDDK Central Repository), All of Us, UK Biobank, Vivli, NHANES, CDC WONDER, the Protein Data Bank, ICPSR, IPUMS, Pew, the Roper Center, Census data and the Federal Statistical Research Data Centers, Data.gov, NOAA NCEI, NASA Earthdata, USGS EarthExplorer, and generalist repositories (Zenodo, Dryad, Figshare, Harvard Dataverse, OSF). Explains open, registered, membership, and controlled access, and what a controlled-access request needs. Use when someone wants public or national datasets, asks where to find data beyond their own institution, needs genomic or cohort data from NIH, or wants to know what a repository holds and how hard access is.
---

# Finding data in public repositories

Verified 2026-11-05 against each repository's own pages, listed in the
reference files and in Sources.

Most research questions can start from data someone has already shared.
Repositories differ less in what they hold than in what access takes. Name
the access level first, because it sets the timeline.

This skill is written for any institution. Only the last section is specific
to Indiana University. It lives in research-data for now. It moves to a
repository of its own only if it grows beyond research-data's scope.

## When to ask a person

| Situation | Ask | Send |
| --- | --- | --- |
| A controlled-access request needs an institutional signature or security attestation | Your institution's signing official, usually its research administration office | The repository, the data use certification or agreement, and your project |
| Restricted or human-subjects data, or a repository asks for IRB documentation | Your institution's IRB | The repository's terms and your study plan |
| A repository's terms on use, sharing, or publishing derived data | The repository's help desk | The dataset and the planned use |
| Whether your institution already licenses or holds the data | Your institution's library or research data office | The dataset and the planned use |

**Recommended.** Say plainly when a question needs one of these people. Do
not guess at an institution's obligations. Only the signer can bind the
institution.

## Access levels

| Level | Meaning | Typical time to data |
| --- | --- | --- |
| **Open** | Download without an account | Minutes |
| **Registered** | A free account, often with click-through terms | Same day |
| **Membership** | Your institution must subscribe or be a member | Same day if it is; otherwise a purchase |
| **Controlled** | An application reviewed by a committee or data access committee, and an agreement signed by your institution | Weeks to months |

The time column is **Recommended** planning guidance, not a repository
statement. Census says its own review takes up to 12 weeks, before Special
Sworn Status (Observed 2026-11-05).

## Choose a repository

| Need | Start with | Access |
| --- | --- | --- |
| Human genotype and phenotype data from NIH studies | dbGaP; cancer genomics in the GDC; NHGRI data in AnVIL | Controlled; summary data open |
| Gene expression or sequencing reads | GEO; SRA | Open; human data in dbGaP is controlled |
| A large cohort with EHR, surveys, and genomes | All of Us; UK Biobank | Registered and controlled |
| Clinical trial participant data | Vivli; BioLINCC (NHLBI); NIDDK Central Repository | Controlled |
| Mental health research data | NIMH Data Archive (NDA) | Controlled |
| National health and nutrition statistics | NHANES; CDC WONDER | Open; restricted NHANES files controlled |
| Protein and nucleic acid structures | Protein Data Bank | Open |
| Social science surveys and studies | ICPSR; Pew; Roper Center | Open, registered, membership, or controlled |
| Census microdata, harmonized | IPUMS; NHGIS | Registered |
| Federal restricted microdata | Federal Statistical Research Data Centers, through the Standard Application Process | Controlled |
| Climate, ocean, and atmosphere | NOAA NCEI | Open |
| Satellite and Earth observation | NASA Earthdata; USGS EarthExplorer | Registered |
| Any field, small datasets | Zenodo, Dryad, Figshare, Harvard Dataverse, OSF | Mostly open |
| Not sure where it would be | re3data.org; Google Dataset Search; Data.gov | Finding aids |

Details, quotes, and links are in two reference files:

- [references/biomedical.md](references/biomedical.md): genomic, cohort,
  clinical trial, population health, and structure repositories.
- [references/general-and-social.md](references/general-and-social.md):
  finding aids, generalist repositories, social science, federal statistics,
  and Earth science.

## Requesting controlled-access data

Controlled access runs in the same steps at most repositories. Read the
repository's own instructions for the exact form.

1. **Check eligibility.** **External.** dbGaP requires the requester to be
   "a permanent employee of their institution." Graduate students and
   postdocs join a project an eligible user oversees (NIH dbGaP page).
2. **Get the accounts.** dbGaP and the GDC need an eRA Commons account.
   All of Us needs your institution to have signed its Data Use and
   Registration Agreement. BioLINCC uses Login.gov.
3. **Write the research use statement.** Data access committees review the
   proposed use against the data's consent.
4. **Get IRB documentation** where the repository asks. Some dbGaP studies,
   NDA permission groups, and BioLINCC require it.
5. **Have your institution sign.** dbGaP routes requests to the
   institution's Signing Official. NDA needs "an Authorized Institutional
   Business Official." Vivli, BioLINCC, and NIDDK-CR send an agreement for
   an institutional signature.
6. **Plan for renewal.** dbGaP and NDA grant access for one year, with
   renewal or a close-out report before it ends.

**Required.** Since January 25, 2025, approved users of NIH controlled-access
data attest that their institution complies with NIST SP 800-171, per
NOT-OD-24-157. The NIH Security Best Practices for Users of Controlled-Access
Data describe the attestation. Choose where the data will be stored and
analyzed before you apply.

**Required.** Data use certifications and agreements bind the user. Common
terms are no attempt to identify or contact participants, no redistribution,
and deletion at the end of the project (dbGaP DUC, NDA DUC, BioLINCC RMDA).

**Recommended.** Start a controlled-access request as soon as a project
depends on it. Institutional signature and committee review are the slow
steps, and neither can be rushed by the researcher.

## Using open and registered data well

- **Required.** Registered data comes with terms you accept on sign-up. For
  example, IPUMS's terms bar redistribution without permission and any
  attempt to identify individuals. CDC WONDER's terms bar publishing NCHS
  statistics on nine or fewer births or deaths.
- **Recommended.** Cite the dataset by its persistent identifier and
  version, and record the date you downloaded it. Repositories update data
  in place.
- **Recommended.** Read the license before combining datasets. CC0 data,
  such as the PDB archive and NASA mission data, may be combined freely.
  Data under use terms may not.

## Depositing data

Zenodo, Dryad, Figshare, Harvard Dataverse, OSF, and NOAA NCEI take
deposits. Their limits are in `references/general-and-social.md`. Dryad
refuses personally identifiable data. Prefer a domain repository where one
exists, as NIH advises.

## At Indiana University

This section is the only IU-specific part of the skill.

- Check whether IU already holds or licenses the data first.
  `finding-iu-research-data` searches the Research Data Catalog and the IU
  inventory.
- IU holds an institutional All of Us agreement, ICPSR membership for IU
  Bloomington and IU Indianapolis, and Roper Center membership for IU
  Bloomington. The IU inventory in `finding-iu-research-data` lists the
  last two. `using-licensed-and-public-data` and
  `accessing-health-and-clinical-data` cover both.
- For NIH controlled-access data rules at IU, see
  `navigating-research-data-policy`. For storage of the data,
  `classifying-research-data`.

## Keep this file current

- Re-read each repository's access page every quarter. Update the
  Observed date in the reference file.
- Check the NIH Guide for notices replacing NOT-OD-24-157 or the Genomic
  Data Sharing policy.
- **Open item.** ICPSR, UK Biobank, Harvard Dataverse's support site, and
  researchdatagov.org returned HTTP 403 to scripts on 2026-11-05. GEO and
  NDA returned a browser check or an empty script shell. Read them in a
  browser and fill in the reference files.
- **Open item.** Search results, not UK Biobank's own pages, said UK
  Biobank had paused applications. Confirm before advising anyone.
- This skill stays in research-data for now. If it grows beyond the
  repository's scope and moves to one that is not IU-specific, drop the "At
  Indiana University" section and the IU pointers in the reference files.

## Sources

Checked 2026-11-05.

- The repository pages listed in `references/biomedical.md` and
  `references/general-and-social.md`.
- External: NOT-OD-24-157, Implementation Update for Data Management and
  Access Practices Under the Genomic Data Sharing Policy,
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-157.html
- External: NIH Security Best Practices for Users of Controlled-Access Data,
  https://grants.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf
- External: dbGaP Data Use Certification,
  https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/accessing-data/certification-agreement
- External: NIH generalist repositories,
  https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/accessing-data/scientific
