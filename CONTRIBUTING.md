# Verifying and updating a skill

A skill is only as good as its last check. Update a skill whenever an agent
or a person finds a claim that no longer matches its source.
[MAINTAINING.md](MAINTAINING.md) is the runbook for reviewing the whole set.

## The rule this repository exists for

IU has no single research data policy. These skills must never make a
recommendation look like a rule, or a rule look optional.

- Mark a statement **Required** only when a binding source requires it. Name
  that source in the same paragraph, list item, or table row. Binding sources
  are IU policies (`policies.iu.edu`), federal law and regulation, sponsor
  notices and terms, and the data's own agreements, licenses, and consent.
- Mark a practice **Recommended** when nothing requires it. Give the reason.
  Name any IU guidance or peer policy it follows.
- IU guidance pages and KB articles explain policy. Quote them as guidance,
  unless they state a requirement that comes from a policy. Then cite both.
- When guidance and policy disagree, or two sources conflict, write an
  **Open item**. Name both sources and quote what differs. Do not pick one.

`tools/check-skills.py` fails when a **Required** statement names no
binding source.

## Other markers

| Marker | Use it for |
| --- | --- |
| **Observed** | A fact read from a live system, such as a catalog entry, with the date and the URL or command |
| **External** | A claim from a non-IU source, which must be named |
| **Practice** | A lesson from experience that no source states; give a check where one exists |
| **Open item** | A question no source answers, or sources that conflict |

## The Research Data Catalog is the source for datasets

Do not copy access terms into a skill as if they were stable. Link to the
catalog entry, and summarize only enough to match a question to a dataset.
Check an entry live before relying on it:

```bash
s=.agents/skills/finding-iu-research-data/scripts/rdc_catalog.py
$s show <id or title words>
$s check
```

The catalog's search pages and feeds are behind a Cloudflare human check.
Find new entries by browsing https://researchdatacatalog.iu.edu by date
modified.

## Reading IU sources

- **IU policies** at `policies.iu.edu` show an effective date and a last
  review date. Record both when a policy changes.
- **IU Knowledge Base** articles live at `servicenow.iu.edu/kb`. A plain
  fetch returns an empty page. Use the `searching-the-iu-knowledge-base` skill
  in the research-technologies repository to read them.
- **Login-only pages**, such as the Data Sharing and Handling tool, cannot
  be checked by script. Note who read them, and when.
- **Internal drafts**, such as committee working documents, are not sources.
  They may guide what to look for. Cite only what is public.

## Write a Recommended practice

A recommendation should help someone who has no rule to follow.

- State the practice and why it matters.
- Prefer practice that IU guidance, the RDC, or a peer university policy
  already supports, and name it.
- Leave out people, projects, and incidents.
- Use the smallest practice that solves the problem. These skills guide.
  They are not a shadow policy.

## Update the verified date

Each skill carries a `Verified <date>` line near the top. Change it only
after re-reading every source in the skill's Sources list. After a partial
check, name what was re-read, as in `Verified 2026-11-02 (DM-02 and the RDC
sharing guide only). Other sources were verified 2026-10-04.`

## Format and style

- Follow the [Agent Skills specification](https://agentskills.io/specification).
  Keep `name` equal to the directory name, in kebab-case. Keep `description`
  under 1024 characters. Say what the skill does and when to use it.
- Keep `SKILL.md` under 500 lines. Move detail to `references/`.
- Put runnable helpers in `scripts/`. Use the Python standard library.
- Keep skills harness-neutral. Do not name a harness's tools.
- Refer to another skill by its name in backticks. Do not link across skill
  directories, because a skill may be installed alone.
- One idea per sentence, under 25 words, with the serial comma.
- End every skill with a "Keep this file current" section, then Sources.
- Prefer office addresses, such as iurdc@iu.edu, to named people. A catalog
  entry's Public Contact is the source for a dataset's contact. Add a new
  office address to `allowed_emails` in `tools/check-skills.toml`. The
  checker fails any other address, and any internal hostname.
- Date every **Observed** statement. The checker fails one without a date.

Run `tools/check-skills.py` before committing. It must exit cleanly.

`tools/check-skills.py` is the same file in every repository of this
family. Do not edit it here. Change this repository's settings in
`tools/check-skills.toml`: allowed emails, the Required-source pattern,
the STALE age, link skip lists, and the weekly checks. The first line it
prints carries its version and hash, so copies can be compared.

## Commits

Make one focused commit per skill change. Say in the message which sources
were re-read.
