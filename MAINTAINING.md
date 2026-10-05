# Runbook: reviewing and updating the skill set

This runbook keeps the skills true to IU as it is now. `CONTRIBUTING.md`
covers how to write and verify a single claim.

## Who decides what is true

- **IU policy, federal rules, sponsor terms, and agreements** decide what is
  required.
- **The Research Data Catalog** decides which datasets exist and how to
  request them.
- **IU guidance**, from IU Data Management, the IU KB, IU Research, and the
  RDC, explains how to follow policy.
- **The owning office** settles what none of these answers. Record its
  answer with the date and the email or ticket it came from.

## When to review

| Trigger | Scope |
| --- | --- |
| Anyone finds a wrong claim | That claim, right away, in its own commit |
| Monthly | `rdc_catalog.py check`, and browse the catalog for new entries |
| Every quarter (January, April, July, October) | The full review below |
| IU adopts a research data policy | Every skill; start with `navigating-research-data-policy` and its policy map |
| An NIH or NSF data policy notice | `planning-data-management-and-sharing` and `navigating-research-data-policy` |
| An open issue labeled `freshness` | The entries, links, and articles it lists |

GitHub Actions runs `tools/check-skills.py` on every pull request and push to
`main`. Every Monday, `freshness.yml` runs `tools/check-skills.py
--freshness`. Here that means the KB check, the link check, and the catalog
check. When any finds a change, it opens an issue labeled `freshness`, or
comments on the one already open.

## Full review

Work on a branch. Make one commit per skill.

### 1. Lint and check links

```bash
tools/check-skills.py --kb --links
```

`ERROR` and `BROKEN` lines must be fixed. A broken IU link often means a
page moved. Search the site for its new address before removing the claim.
`STALE` lines name a skill over 120 days past its Verified date, or a KB
article published after it. Re-read those sources in steps 3 and 4.

### 2. Refresh the catalog snapshot

```bash
s=.agents/skills/finding-iu-research-data/scripts/rdc_catalog.py
$s check
```

For each `CHANGED` entry, run `$s show <id>`. Update its row in
`references/catalog.md`, including the date. For `GONE`, remove the row and
note it in the commit. Then browse https://researchdatacatalog.iu.edu sorted
by date modified, and add new entries.

### 3. Re-read the policies

Open each IU policy cited in the skills. Compare the "last reviewed" date
with the skill's Verified date. Re-read any that changed. Check
`policies.iu.edu` for new policies on research data, intellectual property,
or data management.

Check the RDC news page for the research data policy. If IU adopted one,
rework `navigating-research-data-policy` and its policy map first. Turn each
Recommended practice it covers into a Required statement that cites it.

### 4. Re-read guidance and sponsor pages

- The RDC guides and FAQs.
- The IU Data Classification Matrix CSV, at
  https://datamanagement.iu.edu/docs/matrix.csv. Compare its Research Data
  and Health rows.
- The KB articles each skill cites.
- NIH DMS, GDS, and public access pages, and NSF's PAPPG.

### 5. Work the open items

```bash
grep -rn -i "open item" .agents/skills
```

Keep [docs/open-items.md](docs/open-items.md) in step. For each item, check
whether a source now answers it. Otherwise batch the questions by office,
and send one message per office. Close an item only with its source.

### 6. Test that agents find the right skill

Start a fresh session in this repository. Try the prompts in
[tests/trigger-prompts.md](tests/trigger-prompts.md). Check that the
expected skill loads. Fix a description that fails to trigger.

### 7. Finish

Run `tools/check-skills.py`. Open a pull request listing the sources re-read,
catalog changes, and open items closed or opened.

## Adding a skill

1. Create `.agents/skills/<name>/SKILL.md`. Keep `name` equal to the
   directory name.
2. Follow `CONTRIBUTING.md` for markers, sources, and style.
3. Add a row to the skills table in `README.md`.
4. Add trigger prompts to `tests/trigger-prompts.md`. The checker fails a
   skill with no README row or trigger prompt.
5. Run `tools/check-skills.py --links`.
