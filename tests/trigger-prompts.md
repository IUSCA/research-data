# Trigger prompts

Use these in a fresh session to check that each skill loads when it should.
Each prompt names the skill that should load first. Others may load too.
Step 6 of `MAINTAINING.md` explains the test.

| Prompt | Expected skill |
| --- | --- |
| What data does IU have on hospital inpatient stays? | `finding-iu-research-data` |
| Does IU already license CoreLogic, or do I need to buy it? | `finding-iu-research-data` |
| I need EHR data on diabetes patients in Indiana for a retrospective study. | `accessing-health-and-clinical-data` |
| How do I get access to MarketScan at IU, and where can I run the analysis? | `accessing-health-and-clinical-data` |
| Can an undergraduate in my lab use HCUP data? | `accessing-health-and-clinical-data` |
| I want Bluesky posts from 2024 for a misinformation study. | `using-licensed-and-public-data` |
| How do I buy a commercial dataset with grant funds? | `using-licensed-and-public-data` |
| Is interview audio from my study Restricted or Critical? | `classifying-research-data` |
| Can I paste my survey data into ChatGPT Edu? | `classifying-research-data` |
| Help me write the data management and sharing plan for an NIH R01. | `planning-data-management-and-sharing` |
| How long do I have to keep data after my NSF grant ends? | `planning-data-management-and-sharing` |
| A collaborator at Purdue wants a copy of our de-identified dataset. | `sharing-research-data` |
| Can I sign this data use agreement myself? | `sharing-research-data` |
| My postdoc is leaving for another university. Can they take the data? | `sharing-research-data` |
| Who owns the data my lab collects? | `navigating-research-data-policy` |
| Is it required or just recommended to have a data management plan for unfunded work? | `navigating-research-data-policy` |
| What do I need to do to use dbGaP data at IU? | `navigating-research-data-policy` |
| Whom do I ask about sharing data with a company? | `getting-help-with-research-data` |

## Plain-language prompts

A researcher new to IU may not know the names of IU datasets, offices, or
policies. These prompts use none of them. Each should still load the
expected skill first.

| Prompt | Expected skill |
| --- | --- |
| I just started at the university. Where do I look for existing data on teen mental health before collecting my own? | `finding-iu-research-data` |
| Before I pay for a dataset, how do I check whether the university already has it? | `finding-iu-research-data` |
| Where can I get patient records for a study? | `accessing-health-and-clinical-data` |
| I want insurance claims for people with asthma to study the cost of care. How do I get them? | `accessing-health-and-clinical-data` |
| I want a large collection of social media posts for a study. Can the university help? | `using-licensed-and-public-data` |
| Am I allowed to use a database from the library to train a machine learning model? | `using-licensed-and-public-data` |
| My survey asks about drug use and collects names. How careful do I have to be with it? | `classifying-research-data` |
| Can I upload my participants' answers to an AI chatbot to help analyze them? | `classifying-research-data` |
| My funder says I have to share my data. What do I do? | `planning-data-management-and-sharing` |
| My grant application asks for a document about how I will handle my data. How do I write it? | `planning-data-management-and-sharing` |
| A researcher at another university wants a copy of my data. What do I need to do first? | `sharing-research-data` |
| I'm moving to a job at another school. Can I bring my research files with me? | `sharing-research-data` |
| Does my data belong to me or to the university? | `navigating-research-data-policy` |
| Is there an actual rule about what I must do with my research data, or is it all advice? | `navigating-research-data-policy` |
| I have a question about my study's data and I don't know who to ask. | `getting-help-with-research-data` |
| Who at the university can help me figure out what to do with my research data? | `getting-help-with-research-data` |
| Is there somewhere safe to keep interview recordings? | `classifying-research-data` |
| I need to send a few terabytes of data to a collaborator at another university. What's the best way to transfer it? | `storing-and-moving-research-data` in research-technologies |
| I can't get into the server where my project's data is stored. Who do I contact? | `getting-help-from-research-technologies` in research-technologies |

The last three prompts sit on the boundary with research-technologies. Test
them with both repositories loaded, for example with `claude --add-dir`.

- **Interview recordings.** `classifying-research-data` should win. The
  recordings' classification decides which systems may hold them, so it
  comes first. `storing-and-moving-research-data` may load second to pick
  the system.
- **Sending terabytes to a collaborator.** `storing-and-moving-research-data`
  should win. The question is how to move the files, which is a transfer
  tool question. `sharing-research-data` may load second for the agreement
  and approval steps.
- **Can't get into the server.** `getting-help-from-research-technologies`
  should win. Access to a storage or computing system is a Research
  Technologies support question, not a research data one.
