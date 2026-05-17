# Mixed Methods

## Learning Goals

-   Describe the three [%g mixed_methods "mixed-methods" %] designs (sequential QUAN→qual, sequential QUAL→quan, concurrent)
-   Explain when [%g triangulation "triangulation" %] strengthens a finding and when conflicting results require investigation
-   Apply the DeSouza Santos et al. example to explain what interviews added that a survey alone could not
-   Evaluate a study's claim to be "mixed methods" using appropriate criteria

---

-   [%g mixed_methods "Mixed methods" %]: combining quantitative and qualitative data in a single study
    -   The quantitative part answers "how much" and "how often"
    -   The qualitative part answers "why" and "in what context"
    -   Neither is subordinate; each compensates for the other's weaknesses
    -   Combining two quantitative instruments does not make a study mixed methods

-   Sequential designs:
    -   Quantitative then qualitative (QUAN → qual): mine repositories to identify anomalies, then interview developers at those projects to explain them
    -   Qualitative then quantitative (QUAL → quan): interview developers to identify hypotheses, then test those hypotheses on a large dataset
    -   The order reflects which question comes first: discovery or confirmation

-   Concurrent (convergent) design: collect both types of data at the same time and compare results
    -   Use when you want [%g triangulation "triangulation" %]: if the numbers and the interviews point in the same direction, confidence in the finding increases
    -   If quantitative and qualitative results conflict, that conflict is itself a finding — investigate rather than discard one result
    -   Concurrent designs require more coordination but avoid the problem of one phase contaminating the other

-   DeSouza Santos et al. [%b DeSouzaSantos2022 %] studied coordination in remote-first and hybrid software teams
    -   Survey data (quantitative) identified broad patterns in how teams communicated and coordinated
    -   Interviews (qualitative) explained why those patterns emerged and what mechanisms produced them
    -   Neither component alone would have established both the pattern and the explanation for it

-   Furia et al. [%b Furia2023 %] argue that observational SE data supports only predictive claims, not causal ones
    -   Mixed methods can help bridge that gap: the qualitative component can reveal plausible causal mechanisms that the quantitative data identifies but cannot explain
    -   This is not the same as proof of causation, and researchers should say so

-   Common pitfall: running the qualitative part as an afterthought to explain away inconvenient quantitative results
    -   If the qualitative component is designed after you see the numbers, it will confirm your preferred interpretation rather than test it
    -   Design both components together, before either is collected

## Check Understanding

<details markdown="1">
<summary markdown="1">What is the difference between a sequential QUAN→qual design and a sequential QUAL→quan design? Give a research question that each is appropriate for.</summary>

In a QUAN→qual design, the quantitative phase runs first and identifies patterns that the qualitative phase then explains. For example: "Repository mining shows that projects with more than ten contributors have fewer bugs per commit — we then interview contributors at high- and low-contributor projects to understand why." In a QUAL→quan design, interviews or observations run first to generate hypotheses, which are then tested on a larger dataset. For example: "Interviews with senior developers suggest that code review depth predicts post-release defects — we then mine 500 repositories to test whether that relationship holds at scale."

</details>

<details markdown="1">
<summary markdown="1">A paper describes its research as "mixed methods" and reports that it collected both server log data and a Likert-scale survey. What is missing and why does it matter?</summary>

Both server logs and Likert-scale surveys are quantitative instruments. Mixed methods requires at least one qualitative component — text, interviews, observations, or open-ended responses — alongside the quantitative data. Without a qualitative component, the paper has two quantitative data sources, which is useful but not what "mixed methods" means. The label matters because mixed methods carries an implicit claim about the kind of questions the study can answer: specifically, that it can explain why patterns occur, not just that patterns exist.

</details>

<details markdown="1">
<summary markdown="1">What does triangulation mean in a mixed-methods study, and what should a researcher do if the quantitative and qualitative results point in opposite directions?</summary>

Triangulation means using multiple data sources or methods to cross-check a finding. When the numbers and the interviews agree, you have more grounds for confidence than either source alone provides. When they conflict, the conflict itself needs investigation. The researcher should not simply defer to whichever result fits their prior expectation. Instead, they should ask whether the two instruments are measuring the same thing, whether one population answered the survey and a different population was interviewed, or whether the conflict reveals a real tension in the phenomenon being studied. Reporting the conflict and investigating it honestly is more informative than smoothing it over.

</details>

<details markdown="1">
<summary markdown="1">Why does DeSouza Santos et al.'s finding about coordination in remote teams require both a survey and interviews to establish? What does each component contribute?</summary>

A survey can show that many teams report certain coordination patterns — it can establish frequency and distribution across a sample. But a survey cannot show why those patterns emerged or what mechanisms produce them, because that requires participants to explain their experience in their own words. Interviews provide the mechanism. Without the survey, you would not know how widespread the patterns are; without the interviews, you would not know why they occur. Each component answers a question the other cannot.

</details>

## Exercises

<div class="exercise" markdown="1">
### Designing a follow-up interview study

The motivating question for this lesson is: a repository mining study finds that projects with more contributors have fewer bugs per commit. Propose a follow-up interview study to investigate why. Specify who you would recruit and why they have relevant experience, write three questions you would ask them, and describe one specific finding from the interviews that would lead you to revise your interpretation of the quantitative result — that is, what would you need to hear to conclude that the correlation is explained by something other than the obvious interpretation?
</div>

<div class="exercise" markdown="1">
### What the survey alone could not have produced

DeSouza Santos et al. [%b DeSouzaSantos2022 %] used survey data followed by interviews to study coordination in remote and hybrid teams. Describe one finding from a study of this type that a survey alone could not have produced — not just a finding the survey did not happen to produce, but one that is structurally impossible to obtain from closed-ended survey items. Explain in two sentences why the interview component was necessary to produce it, referring to what interviews can capture that surveys cannot.
</div>

<div class="exercise" markdown="1">
### Designing a concurrent study

Design a concurrent mixed-methods study to answer this single question: "Do developers read the documentation before filing a bug report?" Describe your quantitative data source and how you would collect it, describe your qualitative data source and how you would collect it, and explain in two sentences how you would handle a case where the two sources give contradictory answers. Name the contradiction explicitly rather than assuming the sources will agree.
</div>

<div class="exercise" markdown="1">
### Evaluating a mixed-methods claim

A paper combines server log data (quantitative) with a structured satisfaction survey (also quantitative) and describes the result as "mixed methods research." Write two sentences explaining why this label is inaccurate, referring to what is missing and what question the missing component would answer. Then write one sentence about the practical consequence: what kind of claim does the paper make that it is not entitled to make?
</div>

<div class="exercise" markdown="1">
### From correlation to causal mechanism

Furia et al. [%b Furia2023 %] argue that observational SE data supports correlation claims, not causal claims. Pick one finding from Day 2 of this tutorial — any correlation or group comparison result — and describe a qualitative follow-up study that would provide evidence (though not proof) for a causal interpretation of that finding. Specify who you would interview, what you would ask, and what answer would be consistent with a causal interpretation. Then write a prompt you could give an LLM to help you design a mixed-methods study for any research question:

> [your prompt here]
</div>
