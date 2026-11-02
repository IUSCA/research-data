# Group feedback, November 2026

Feedback and questions from the group review of the research-data skills, with a proposed answer or action for each. Several items apply to the whole family (research-technologies, research-data, research-funding, research-cores), and are marked **Family**.

Status: draft for discussion, 2026-11-02.

## 1. How to send feedback

> Feedback or changes can be sent to Charles directly; can also clone and/or submit PRs.

research-technologies already has a `reporting-a-skill-problem` skill and a "Skill feedback" issue form. research-data has neither, and its README has no feedback section.

Proposed:

- Add a short "Feedback" section to the README: open an issue or send a pull request.
- Copy the "Skill feedback" issue form from research-technologies.
- **Family.** Generalize `reporting-a-skill-problem` so each repository carries it with its own repository name, rather than only research-technologies.

Decided, 2026-11-02: GitHub issues and pull requests are the primary route for feedback and changes. The README and CONTRIBUTING.md list no personal contact, because maintenance will pass to others and requests should not depend on one person. The "Skill feedback" issue form is adapted to this repository's skills. Its config sends questions about data itself to the Research Data Commons contact page, so the issue tracker is not taken for a help desk.

## 2. How many skills is the right number?

There is no fixed number. Two costs set the limit:

- Every installed skill's `description` sits in the agent's context in every session. The body loads only when used. Eight descriptions here are about 1,000 tokens; all four repositories (42 skills) are about 7,000.
- Skills with overlapping descriptions get confused for each other. That risk grows with the count, especially across repositories. For example, `classifying-research-data` (here) and `storing-and-moving-research-data` (research-technologies) both answer "can I put this data on X?"

Rule of thumb: one skill per distinct question a researcher brings, and split a skill only when its body passes about 500 lines or its description stops fitting one job. Measure instead of guessing: `tests/trigger-prompts.md` already checks routing within this repository.

Proposed:

- **Family.** Run the trigger prompts of all four repositories with all four plugins installed together, and fix any prompt that loads the wrong repository's skill.
- Add trigger prompts phrased the way a researcher new to IU would ask, without IU names ("where can I get patient data", "is there a place to keep sensitive interview files").

## 3. How many levels of agents makes sense?

One. The researcher's own agent reads the descriptions, loads the skill that fits, and follows hand-offs by skill name (for example, `finding-iu-research-data` hands off to `accessing-health-and-clinical-data`). No skill starts a subagent.

A second level adds a hand-off where context and source citations get lost, and it costs tokens. It earns its place only for wide, mechanical work that a person is not watching, such as a maintainer checking every catalog entry during a review. That is maintenance, not researcher use, and the scripts already do most of it without an agent.

## 4. Making skills findable and complete enough to be found

Findability depends almost entirely on the `description`. The current descriptions name datasets, offices, and policies, which helps when a researcher uses those names. They help less when a researcher describes a need in plain words.

Proposed:

- Review each description against plain-language trigger prompts (item 2), and add the words researchers use, not only IU's names.
- **Family.** Keep each repository's README skills table as the one human-readable index, and link the four tables to each other.

## 5. Data Storage Finder as a skill

> Instead of clicking check boxes, point the agent at the solicitation; the researcher provides full context, which gives more flexibility.

This is feasible without copying the tool's data. **Observed 2026-11-02:** the Data Storage Finder's question logic is a small public file, https://datastoragefinder.iu.edu/dsf/config.js (3.6 KB). It lists its six questions (HPC use, outside collaborators, classification, usage pattern, size, largest file) and which of 13 storage services each answer allows. A script can fetch it live, the same way `rdc_catalog.py` reads the catalog.

The agent would read the solicitation, the DMS plan, or the data use agreement, derive the six answers, show the researcher how it derived each one, and list the allowed services with links to their KB pages.

Two cautions:

- The classification answer must come from `classifying-research-data`, not be guessed from the solicitation.
- The tool's Critical row allows storage that the KB allows only up to Restricted (open item 9 in [open-items.md](open-items.md), still open). The script must flag that conflict, not repeat it.

Proposed home: storage belongs to research-technologies, whose `storing-and-moving-research-data` skill already cites the tool. Add the script there, and have `classifying-research-data` and `planning-data-management-and-sharing` here hand off to it. Ask the tool's maintainers (UITS Research Technologies) whether `config.js` is stable enough to script against.

## 6. How much is stored in the repo versus pointed to?

Current rule (README, "What the skills trust"; CONTRIBUTING): the canonical source decides, and the repository keeps only enough to route a question.

| Kind | Kept in the repo | Fetched live |
| --- | --- | --- |
| Datasets | A one-row summary per catalog entry (`references/catalog.md`, about 1,250 words for 35 entries), with its `updated_at` date | Access terms, eligibility, and contacts, via `rdc_catalog.py show` |
| KB articles | Article number, version, date, and a hash of the text (`tools/kb-snapshot.json`); a short paraphrase where a skill relies on it | The full text, when a claim needs checking |
| Policies | The policy number and what it requires, in one or two sentences | The policy text |
| Office contacts | Role addresses, in `getting-help-with-research-data` | Nothing; checked at each review |

In all, the eight skills and their references are about 11,000 words.

## 7. More context in the skill versus keeping one source of truth

> Want more context in the agent so it doesn't call out to the source and spend tokens, but don't want the skill files to become the canonical source, or to maintain data in multiple places.

The way through is to copy for *choosing* and fetch for *acting*:

- Copy what an agent needs to pick an answer: which dataset, which office, which policy. Copies are short, so their token cost is low.
- Fetch what a person will act on: access steps, eligibility, fees, deadlines. Those change, and a stale copy does harm.
- Give every copied fact its source and date. Detect drift by machine rather than by maintaining it by hand. The monthly `freshness` workflow already does this for KB articles (hash), the catalog (`updated_at`), and links. A changed source opens an issue; nobody edits the same fact in two places.

Where a copy proves too thin and agents keep fetching the same page, that is a signal to add one more line to the copy, with its date, rather than to copy the page.

## 8. Make clear when to reach out, and to whom

The contacts exist but are spread out. `getting-help-with-research-data` is the directory, and other skills name offices in passing. Nothing tells the agent when to stop and send the researcher to a person.

Proposed, in every skill:

- A short "When to ask a person" section near the top: the situations this skill cannot settle (signing an agreement, an unclear classification, Restricted or Critical data, an open item, a deadline), each with the office, its address, and what to send.
- An instruction that the agent says so plainly, for example, "This needs a decision from ORA. Send them X, Y, and Z," rather than giving its best guess.
- `getting-help-with-research-data` stays the full directory. Each skill names only its two or three offices, and the checker's `allowed_emails` list keeps the addresses consistent.

## Proposed order of work

1. Feedback route (item 1): README section and issue form. Small.
2. "When to ask a person" in each skill (item 8). One commit per skill.
3. Plain-language trigger prompts and description fixes (items 2 and 4).
4. **Family.** Cross-repository trigger test with all four plugins installed (item 2).
5. Data Storage Finder script in research-technologies (item 5), after asking its maintainers.
