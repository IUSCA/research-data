# Biomedical and health repositories

**Observed 2026-11-05** from each repository's own pages, linked in each
entry. Access terms change. Read the repository's page before telling anyone
how to get access.

Access levels follow the key in `SKILL.md`: **open**, **registered**,
**membership**, and **controlled**.

## Genomic and phenotype data

### dbGaP (database of Genotypes and Phenotypes), NIH

- **Holds.** dbGaP was "developed to archive and distribute the data and
  results from studies" of genotype and phenotype interaction in humans. It
  has public study metadata and summary files, and controlled individual-level
  data.
- **Access.** Controlled. "Investigators not affiliated with NIH must have an
  eRA account to access dbGaP." Requests are "automatically routed to the
  investigator's institutional Signing Official (SO)." "The DACs review all
  access requests for human genomic datasets distributed through dbGaP."
- **Steps.** The PI requests data in dbGaP Authorized Access. The PI must be
  "a permanent employee of their institution"; "graduate students and
  postdoctoral fellows" are "not permitted to submit data access requests."
  If approved, "the investigator will be allowed to access the dataset for
  one year, with the option to renew." "Some datasets require local IRB approval for use, as noted on
  the dbGaP study page."
- **Required.** Approved users follow the dbGaP Data Use Certification
  agreement. Its Term 4 says users "make no attempt to identify or contact"
  participants. The Genomic Data User Code of Conduct also applies.
- Sources: https://dbgap.ncbi.nlm.nih.gov/home,
  https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/accessing-data/dbgap,
  https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/accessing-data/certification-agreement

### SRA (Sequence Read Archive), NCBI

- **Holds.** "Sequence data that are submitted directly to NIH," which are
  "subsequently made available to the public."
- **Access.** Open for most data. Human data submitted to dbGaP is
  controlled: "all user access to these data is through the dbGaP Authorized
  Access portal."
- Source: https://www.ncbi.nlm.nih.gov/sra/docs/

### GEO (Gene Expression Omnibus), NCBI

- **Holds.** GEO's FTP README describes DataSets, Series, Platforms, and
  Samples. "GEO DataSets (GDS) are curated sets of comparable GEO Sample
  (GSM) data." Files sit on a public FTP site.
- **Access.** Files download from the public FTP site with no login.
- **Open item.** GEO's web pages returned a browser check to scripts on
  2026-11-05, so its own description of access terms was not read.
- Source: https://ftp.ncbi.nlm.nih.gov/geo/README.txt

### Genomic Data Commons (GDC), NCI

- **Holds.** "A unified repository and cancer knowledge base" with
  "NCI-generated data from some of the largest and most comprehensive cancer
  genomic datasets."
- **Access.** Open and controlled. "The GDC requires authentication through
  eRA Commons and dbGaP authorization to access controlled data." The PI
  gets dbGaP approval and adds lab members as downloaders. "It may take up to
  24 hours for the GDC to sync with dbGaP."
- Sources: https://gdc.cancer.gov/about-gdc,
  https://gdc.cancer.gov/access-data/obtaining-access-controlled-data

### AnVIL, NHGRI

- **Access.** "Open access datasets are available to all users in the AnVIL
  Data Explorer." "Controlled access datasets require authorization based on
  the dataset's consent codes," through dbGaP or DUOS. "All AnVIL buckets
  have Requester Pays enabled," so downloads and compute cost money.
- Source: https://anvilproject.org/learn/accessing-data/requesting-data-access

## Cohorts and biobanks

### All of Us Research Program, NIH

- **Holds.** Three tiers. The Public Tier "contains only aggregate data with
  identifiers removed." The Registered Tier "contains individual-level data,
  available only to registered researchers," including EHR, wearables,
  surveys, and physical measurements. The Controlled Tier adds "genomic data
  in the form of short-read whole genome sequences (WGS)," long-read WGS, and
  arrays.
- **Access.** Registered and controlled. "Only researchers whose
  institutions have signed a DURA may access the Researcher Workbench." Then
  verify identity, sign the Data User Code of Conduct, and "Complete our
  Responsible Conduct of Research training." Project descriptions are made
  public. Compute runs on a billing account after initial credits.
- Sources: https://www.researchallofus.org/register/,
  https://www.researchallofus.org/data-tools/data-access/

### UK Biobank

- **Open item.** UK Biobank's site returned HTTP 403 to scripts on
  2026-11-05, so nothing here is confirmed. Search results suggested that
  applications were paused while its analysis platform changes. Read
  https://www.ukbiobank.ac.uk/ in a browser before advising anyone.

### BioLINCC, NHLBI

- **Holds.** "Web Access to NHLBI Biospecimens and Data" from NHLBI-funded
  studies, plus "Teaching Datasets - Public Use Datasets." "All BioLINCC data
  and biospecimens are de-identified."
- **Access.** Controlled for study data and specimens. Register with
  Login.gov using an institutional email. The PI submits a research plan and
  IRB documentation. After NHLBI approval, the PI and an institutional
  official sign a Research Materials Distribution Agreement.
- **Cost.** "There is no cost to access BioLINCC datasets." Specimen
  requests pay shipping.
- Sources: https://biolincc.nhlbi.nih.gov/home/,
  https://biolincc.nhlbi.nih.gov/faq/

### NIDDK Central Repository (NIDDK-CR)

- **Holds.** Data and specimens from NIDDK-funded studies, including
  "Clinical phenotype data," "Genotype/genetic data," and "Continuous glucose
  monitoring."
- **Access.** Controlled. "The DUA is legally binding and signed by the
  requesting Principal Investigator and institution official." Specimen
  retrieval carries fees; see the requestors page.
- The site notes: "This repository is under review for potential
  modification in compliance with Administration directives."
- Sources: https://repository.niddk.nih.gov/home/,
  https://repository.niddk.nih.gov/pages/for_requestors

### NIMH Data Archive (NDA)

- **Holds.** "Harmonized human subjects research data and metadata from
  multiple research Data Repositories." "Data submitted to NDA have been
  stripped of all individual identifiers."
- **Access.** Controlled, per Permission Group. Submit a Data Access Request
  with a Data Use Certification. "Institutional sponsorship requires the
  signature of an Authorized Institutional Business Official and an active
  Federal Wide Assurance (FWA) number." Access lasts "for a period of one
  year."
- **Required.** The NDA Data Use Certification bars attempts to "identify
  or contact individual participants," and requires a NIST SP 800-171 or ISO
  27001/27002 attestation.
- **Open item.** NDA's web pages did not render for scripts on 2026-11-05.
  This entry rests on its Data Use Certification PDF.
- Source: https://nda.nih.gov/ndapublicweb/Documents/NDA+Data+Access+Request+DUC+FINAL.pdf

### Vivli (clinical trial participant data)

- **Holds.** "Individual participant-level data from completed clinical
  trials."
- **Access.** Controlled. Request a data package. The contributor checks
  feasibility, and an "Independent Review Panel or Scientific Committee"
  reviews it. Vivli sends a DUA to your institution's signer. Analysis runs
  in "a cloud-based remote workspace." Fees apply after an initial period;
  see the request page.
- Sources: https://vivli.org/about/overview/,
  https://vivli.org/resources/requestdata/

## Population health surveys and statistics

### NHANES, CDC National Center for Health Statistics

- **Holds.** "A national survey that measures the health and nutrition of
  adults and children in the United States," combining interviews,
  examinations, and lab tests.
- **Access.** Open: "NHANES data files and related documentation are
  publicly available to download and analyze." Controlled: "NHANES
  restricted data files are available through the NCHS Research Data Center
  (RDC) for a fee," requested through the Standard Application Process.
- Sources: https://www.cdc.gov/nchs/nhanes/about/index.html,
  https://wwwn.cdc.gov/nchs/nhanes/default.aspx

### CDC WONDER

- **Holds.** Online query tools "for the analysis of public health data,"
  including births, deaths, cancer, vaccine adverse events, and population
  estimates.
- **Access.** Open web queries.
- **Required.** The data use terms, under 42 U.S.C. 242m(d), say: "Make no
  attempt to learn the identity of any person or establishment." For NCHS
  data, do "Not present or publish statistics representing nine or fewer
  births or deaths."
- Sources: https://wonder.cdc.gov/, https://wonder.cdc.gov/datause.html

## Structures

### Protein Data Bank (RCSB PDB and wwPDB)

- **Holds.** "3D structure data for large biological molecules (proteins,
  DNA, and RNA)."
- **Access.** Open. "Data files contained in the PDB archive are available
  under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication." Cite the
  PDB ID and its publication.
- Sources: https://www.rcsb.org/pages/about-us/index,
  https://www.wwpdb.org/about/usage-policies
