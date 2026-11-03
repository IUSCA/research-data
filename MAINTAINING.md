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

| Trigger | Scope | How you notice |
| --- | --- | --- |
| Monthly | The `freshness` issue, with the catalog's `CHANGED`, `GONE`, and `NEW` lines ([step 2](#2-refresh-the-catalog-snapshot)) | The `freshness` issue opened on the 1st, and the month's tracking issue on iu-research |
| Anyone finds a wrong claim | That claim, right away, in its own commit | An issue on this repository |
| Every quarter (January, April, July, October) | The full review below, after the monthly one | The calendar, and the month's tracking issue |
| IU adopts a research data policy | Every skill; start with `navigating-research-data-policy` and its policy map | IU policy changes on `policies.iu.edu`, and the RDC news page |
| An NIH or NSF data policy notice | `planning-data-management-and-sharing` and `navigating-research-data-policy` | The NIH Guide table of contents, and NSF news |

No script notices the last two. The family maintainer assigns someone to
each feed, as the family runbook's "Watching for events" says.

GitHub Actions runs `tools/check-skills.py` on every pull request and push to
`main`. On the 1st of each month, `freshness.yml` runs `tools/check-skills.py
--freshness`. Here that means the KB check, the link check, and two catalog
commands. When any finds a change, it opens an issue labeled `freshness`, or
comments on the one already open.

## Working a freshness issue

Follow the family runbook,
[monthly-review.md](https://github.com/IUSCA/iu-research/blob/main/docs/monthly-review.md).
It has the general steps: how to work each kind of line, the KB snapshot
and Verified-line rules, commits, and the pull request. This section adds
only what is specific to this repository.

- `--freshness` also runs `rdc_catalog.py check` and `rdc_catalog.py new`.
  When either exits non-zero, the report prints a `CHANGED` line for it.
  The script's own lines just above it say what changed.
- Work the catalog's `CHANGED`, `GONE`, and `NEW` lines with
  [step 2](#2-refresh-the-catalog-snapshot) of the full review.
- `new` exits 2 when the listing returns the human check or changes shape.
  Then a person must browse the listing and compare it with
  `references/catalog.md` by hand. Note it on the tracking issue.
- KB0023515 is also cited in research-technologies. Look for a note on the
  tracking issue before you re-read it.

## Full review

Work on a branch. Commit as the family runbook's "Commits" section says:
one skill per commit, with each KB snapshot in the commit it supports.

### 1. Lint and check links

```bash
tools/check-skills.py --kb --links
```

`ERROR` lines must be fixed. Work `STALE`, `INFO`, and `BROKEN` lines as
the family runbook's step 3 says. Then open each `skip_urls` entry whose
comment says "check by hand", and confirm it lands where the comment says.

### 2. Refresh the catalog snapshot

```bash
s=.agents/skills/finding-iu-research-data/scripts/rdc_catalog.py
$s check
$s new
```

For each `CHANGED` entry, run `$s show <id>`. Update its row in
`references/catalog.md`, including the date. For `GONE`, remove the row and
note it in the commit. For each `NEW` entry, run `$s show <id>`, and add a
row in the right section. `new` reads the catalog's home page listing,
which loads from a script without the human check (Observed 2026-11-03).
The `/catalog` search pages and feeds still return the check.

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
