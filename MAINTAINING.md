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
| An open issue labeled `freshness` | [Working a freshness issue](#working-a-freshness-issue) |

GitHub Actions runs `tools/check-skills.py` on every pull request and push to
`main`. Every Monday, `freshness.yml` runs `tools/check-skills.py
--freshness`. Here that means the KB check, the link check, and the catalog
check. When any finds a change, it opens an issue labeled `freshness`, or
comments on the one already open.

## Working a freshness issue

A person or their agent works each `freshness` issue by hand. Nothing
edits a skill on its own, because every fixed claim needs someone to read
its source. An agent can do all of this; give it this section and the
issue. A person reviews and merges the pull request.

1. Make a branch from `main`. Run `tools/check-skills.py --freshness`
   again. The issue may be days old, and some lines may have cleared.
2. Work each line by kind:
   - **STALE, KB article changed.** Read the whole article with
     `iukb.py read KB0123456` (in research-technologies'
     `searching-the-iu-knowledge-base` skill). Find every claim citing it,
     in each skill the line names and in that skill's `references/`.
     Fix what changed. Then record the reading with
     `tools/check-skills.py --kb-snapshot KB0123456`.
   - **INFO, text unchanged.** The article was touched but its text was
     not. Record it with `--kb-snapshot KB0123456`. No skill changes.
   - **STALE, not found by KB search.** The article was retired or
     renumbered. Search for its replacement. If there is none, name the
     article without a link, with the date it went missing.
   - **STALE, Verified date too old.** Re-read every source the skill
     cites, then update its Verified line.
   - **BROKEN.** Run `--links` again; a single failure is often transient.
     If it still fails, find the page's new address. If the page is gone,
     find another source or make the claim an open item.
   - **CHANGED.** Run the snapshot script named in the line. Update the
     catalog or directory file it compares against, and every skill that
     names what changed.
3. A claim the new source no longer supports is fixed, cut, or turned into
   an open item in `docs/open-items.md`. A question the source now settles
   leaves the open items.
4. Update the Verified line of each skill you edited. For an article with
   a snapshot entry, `--kb-snapshot` is the record, so the Verified line
   does not need to list it as a partial re-read.
5. Run `tools/check-skills.py --freshness` until no STALE, BROKEN, or
   CHANGED line remains. Commit one skill per commit, with the snapshot
   change in the same commit as the skill it supports.
6. Open a pull request that says `Closes #<issue>`. List each line and
   what you did with it: fixed, unchanged, or opened as an item.

## Full review

Work on a branch. Make one commit per skill.

### 1. Lint and check links

```bash
tools/check-skills.py --kb --links
```

`ERROR` and `BROKEN` lines must be fixed. A broken IU link often means a
page moved. Search the site for its new address before removing the claim.
`STALE` lines name a skill over 120 days past its Verified date, or a KB
article whose text changed since `tools/kb-snapshot.json` recorded it. Re-read those sources in steps 3 and 4.

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
