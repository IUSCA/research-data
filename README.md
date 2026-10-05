# research-data

Agent skills for research data at Indiana University. They help a researcher
or a coding agent find data IU already has and get access to it. They also
cover classifying, planning, and sharing data, and staying within IU policy
and sponsor rules.

## Companion repositories

Four repositories cover research at IU. Skills name a companion's skill by
its repository and skill name, as in "`sharing-research-data` in
research-data," and link the first mention to the skill on GitHub.

- [research-technologies](https://github.com/IUSCA/research-technologies) covers clusters, storage, data transfer, and
  allocations.
- **research-data** (this repository) covers finding, classifying, managing, and sharing research
  data.
- [research-funding](https://github.com/IUSCA/research-funding) covers planning and preparing grant proposals.
- [research-cores](https://github.com/IUSCA/research-cores) covers core facilities, their instruments, and the data
  they deliver.

This repository covers the data itself. research-technologies covers where
it is computed on and stored.

## Quickstart

1. Clone this repository.
2. Start your agent in the clone. Claude Code, Codex, OpenCode, and pi all
   find the skills there with no install step.
3. Ask: "What data does IU have on hospital inpatient stays, and how do I get
   it?"

## Guidance, not new rules

IU has no single research data policy. Rules about research data are spread
across data management policies, intellectual property policies, human
subjects policy, and sponsor terms. Many questions fall between them.

These skills do two things:

- They state what is **required**, and cite the policy, law, or sponsor term
  that requires it.
- Where nothing requires a practice, they recommend one, and label it
  **Recommended**. A recommendation is advice. It is never presented as a
  rule.

When a recommendation and a binding source disagree, the binding source wins.
When a binding source is unclear or silent, the skill says so as an **open
item**. It does not guess.

## What the skills trust

Every claim carries one of these markers, or cites its source inline:

| Marker | Meaning | Must cite |
| --- | --- | --- |
| **Required** | A binding rule: an IU policy, a federal law or regulation, or a sponsor term | The policy number, regulation, or notice |
| **Recommended** | A practice this repository advises where no rule applies | The reason, and any peer policy or IU guidance it follows |
| **Observed** | Read from a live system, such as a Research Data Catalog entry | The date and the URL or command |
| **External** | From a non-IU source, such as an NIH page | The source |
| **Practice** | A lesson from experience that no source states | How to check it, where possible |
| **Open item** | No source answers it, or sources conflict | The sources that disagree |

Sources rank this way:

1. **IU policy** (`policies.iu.edu`) and **sponsor or federal rules** bind.
2. **IU guidance**, including the Data Management site, the IU Knowledge
   Base, IU Research pages, and Research Data Commons guides, explains how to
   follow them.
3. **The Research Data Catalog** (`researchdatacatalog.iu.edu`) is the source
   of truth for which datasets exist and how to request them. Each skill
   links to catalog entries instead of copying their access terms.

## A note for agents and the people using them

A coding agent is an AI tool. IU does not permit research data classified
Restricted or Critical with third-party AI tools (KB0026817). Most research
data is Restricted by default. So an agent using these skills should ask for
a dataset's classification before opening its files. With Restricted or
Critical data, it should work from schemas, codebooks, and synthetic samples
unless it runs on an IU-approved service. `classifying-research-data` has
the details.

## Skills

| Skill | Use it when |
| --- | --- |
| [finding-iu-research-data](.agents/skills/finding-iu-research-data/SKILL.md) | Looking for data for a research question, or checking whether IU already has a dataset. Start here. |
| [accessing-health-and-clinical-data](.agents/skills/accessing-health-and-clinical-data/SKILL.md) | Requesting INPC, IU Health, or Eskenazi records, or using HCUP, MarketScan, All of Us, or biospecimen data. |
| [using-licensed-and-public-data](.agents/skills/using-licensed-and-public-data/SKILL.md) | Using library-licensed, Kelley-licensed, ICPSR, OSoMe, or restricted federal data, or buying a dataset. |
| [classifying-research-data](.agents/skills/classifying-research-data/SKILL.md) | Deciding whether data is Public, University-internal, Restricted, or Critical, and what that allows. |
| [planning-data-management-and-sharing](.agents/skills/planning-data-management-and-sharing/SKILL.md) | Writing an NIH or NSF data management and sharing plan, or planning retention. |
| [sharing-research-data](.agents/skills/sharing-research-data/SKILL.md) | Sharing data with a collaborator, a repository, or the public, or moving data when someone leaves IU. |
| [navigating-research-data-policy](.agents/skills/navigating-research-data-policy/SKILL.md) | Asking who owns data, how long to keep it, what a PI is responsible for, or what NIH controlled-access rules need. |
| [getting-help-with-research-data](.agents/skills/getting-help-with-research-data/SKILL.md) | Deciding which IU office to ask, and what to send. |

## Use the skills

Each skill is a directory in the open
[Agent Skills](https://agentskills.io/specification) format. Scripts use only
Python's standard library, so any harness that can run a shell can use them.

The skills live in `.agents/skills/`. Codex, pi, and OpenCode read that
directory. Claude Code reads only `.claude/skills/`, so `.claude/skills` is a
committed symbolic link to it.

To use the skills in another project, copy the skill directories you need
into that project's `.agents/skills/`. Or use the
[`skills` CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add <this repository> --list
npx skills add <this repository> --skill finding-iu-research-data --copy
```

Claude Code users can also run `claude --add-dir ~/repos/research-data` for
one session.

## Maintaining

- [CONTRIBUTING.md](CONTRIBUTING.md) explains how to verify and write a
  single claim.
- [MAINTAINING.md](MAINTAINING.md) is the runbook for reviewing the whole
  set.
- [docs/open-items.md](docs/open-items.md) collects every open question, by
  the office that can answer it.
- `tools/check-skills.py` runs the offline checks: format, markers, sources,
  age, and what stays out. `--kb` and `--links` add the network checks, and
  `--freshness` runs every check this repository's weekly workflow runs.
  `tools/check-skills.toml` holds this repository's settings.
- The catalog helper,
  `.agents/skills/finding-iu-research-data/scripts/rdc_catalog.py check`,
  reports catalog entries that changed since they were recorded.
  `--freshness` runs it too.
- [tests/trigger-prompts.md](tests/trigger-prompts.md) checks that agents
  load the right skill.

## License

Code, meaning scripts and tools, is under the Educational Community License,
Version 2.0; see [LICENSE](LICENSE). Written content, including every
`SKILL.md` and reference file, is under CC BY 4.0; see
[LICENSE-docs](LICENSE-docs). Copyright the Trustees of Indiana University.
