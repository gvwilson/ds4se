# Grounded Theory: A Practical Introduction

## Learning Goals

-   Distinguish [%g grounded_theory "grounded theory" %] from thematic analysis in terms of starting point, output, and use case
-   Apply the three coding stages (open, axial, selective) to a small dataset
-   Explain why iterative data collection is a defining feature of grounded theory
-   Recognize when a paper claims GT but actually did thematic analysis

---

-   [%g grounded_theory "Grounded theory" %] builds theory from data rather than testing a pre-specified hypothesis
    -   Appropriate when the phenomenon is not well understood and no existing theory fits
    -   Produces a conceptual model, not a p-value
    -   The name comes from the idea that the theory is grounded in the data itself, not imposed from outside

-   The three coding stages (Strauss & Corbin):
    -   Open coding: read the data and label concepts freely, without constraint
    -   Axial coding: connect concepts by identifying causes, conditions, and consequences
    -   Selective coding: identify the core category that integrates everything else

-   [%g constant_comparison "Constant comparison" %]: as you code new data, compare it to everything coded so far
    -   This comparison drives changes to your codes and categories while data collection is still ongoing
    -   This is what makes GT iterative, not just a fancy name for thematic analysis
    -   If you finish collecting data before you start comparing, you have not done constant comparison

-   [%g theoretical_saturation "Theoretical saturation" %]: stop collecting data when new interviews stop producing new concepts
    -   Saturation is a judgment call, not a formula — report the evidence for it
    -   Evidence might include: the last three interviews added zero new open codes; no new categories emerged after interview eight
    -   Claiming saturation without evidence is one of the most common weaknesses reviewers flag

-   Zieris & Prechelt [%b Zieris2021 %] used GT to study pair programming skill
    -   They interviewed and observed professional developers and derived a model of what distinguishes productive from unproductive pairing
    -   Crucially, they did not start from an existing taxonomy of pair programming behaviors
    -   Each session of observation informed who to recruit and what to look for next

-   Barke & Prechelt [%b Barke2019 %] used GT to study role conflict in self-organizing agile teams
    -   Interviews revealed that role ambiguity was both a source of conflict and, paradoxically, a source of flexibility
    -   That finding would be hard to design into a survey instrument, because you would not know to ask about flexibility until you had seen it emerge in the data

-   GT is frequently misused in SE research
    -   Claiming GT when you actually did thematic analysis is common in published papers
    -   The distinguishing mark is iterative data collection driven by emerging theory, not sequential collection followed by coding
    -   If a paper describes collecting all participants before analysis began, it is not grounded theory regardless of what the authors call it

## Check Understanding

<details markdown="1">
<summary markdown="1">What is the difference between open coding and axial coding in grounded theory?</summary>

Open coding is the initial pass through the data where you attach labels to segments of text without worrying about how those labels relate to each other. Axial coding comes after you have a set of open codes and involves connecting them: asking what causes this concept, what are the conditions under which it appears, and what consequences it has. Open coding produces a vocabulary; axial coding produces structure.

</details>

<details markdown="1">
<summary markdown="1">A research report states: "We used grounded theory. We first collected all 30 interviews and transcribed them, then coded the transcripts over two weeks." What is wrong with this and what should the researchers have done instead?</summary>

Grounded theory requires that data collection and analysis happen in parallel. Constant comparison means coding each interview and revising your categories before recruiting or interviewing the next participant. By collecting all 30 interviews before any analysis, the researchers eliminated the mechanism that makes GT iterative: the ability for emerging theory to guide who you talk to next and what you ask. What they describe is thematic analysis on a fixed dataset, not grounded theory. They should have begun coding after the first two or three interviews, revised their sampling and interview guide as new concepts emerged, and stopped collecting data when new interviews added no new open codes.

</details>

<details markdown="1">
<summary markdown="1">What does "theoretical saturation" mean, and how would you report evidence for it in a paper?</summary>

Theoretical saturation is the point at which new data stops producing new concepts. It means the emerging theory is sufficiently developed that additional interviews are unlikely to change it. To report evidence for it, you might record how many new open codes appeared in each interview and show that the count dropped to zero by interview N. A table with interview number and new-codes-added is more convincing than the phrase "we reached saturation" on its own.

</details>

<details markdown="1">
<summary markdown="1">How do you tell whether a paper that claims to use grounded theory actually used grounded theory?</summary>

Look for three things. First, check whether data collection and analysis overlapped: GT requires coding to begin before all data is collected. If the methods section describes sequential phases ("we collected, then we coded"), that is a red flag. Second, look for evidence that early findings changed the sampling strategy or interview guide, which is how emerging theory is supposed to drive data collection. Third, look for a description of theoretical saturation with some evidence — not just the claim. Papers that pass all three checks are rare.

</details>

## Exercises

<div class="exercise" markdown="1">
### Core category in Zieris & Prechelt

Read the abstract of Zieris & Prechelt [%b Zieris2021 %]. Identify the core category they report — the concept that integrates the rest of their model — and write one sentence explaining how that core category connects to at least two other concepts they identify. Then write one sentence about whether the core category could have been specified in advance as a survey question.
</div>

<div class="exercise" markdown="1">
### Proposing axial codes

You interview five developers about how they decide which bugs to fix first. Your open codes include "customer pressure," "ease of fix," "affects many users," "personal interest," and "manager says so." Propose two axial codes that group these into broader categories. Write one sentence for each axial code explaining which open codes fall under it and why the grouping makes sense conceptually. Then write one sentence identifying which open code is hardest to place and why.
</div>

<div class="exercise" markdown="1">
### Diagnosing a GT violation

A paper claims to use grounded theory but collected all data before any coding began. Explain in two sentences why this violates a core GT principle. Then explain in one sentence what consequence that violation has for the resulting theory: specifically, what kind of claim is the paper not entitled to make?
</div>

<div class="exercise" markdown="1">
### Designing a saturation check

Theoretical saturation is often invoked without evidence. Design a simple record-keeping procedure that a researcher could follow during data collection that would let a reader judge whether saturation was actually reached. Your procedure should specify what you record after each interview, how you would display the evidence in a published paper, and what pattern in the data would convince you that collection should stop.
</div>

<div class="exercise" markdown="1">
### Comparing methods

Compare thematic analysis (Lesson 20) and grounded theory (this lesson) on three dimensions: starting point, output, and appropriate use case. Write one sentence per dimension per method, for six sentences total. Then write a prompt you could give to an LLM to help you choose between the two methods for a specific research question:

> [your prompt here]
</div>
