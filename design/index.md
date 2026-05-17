# Study Design and Replication

## Learning Goals

-   Classify studies by type (controlled experiment, case study, survey, mining, systematic review)
-   Explain what [%g replication "replication" %] means and why [%g pre_registration "pre-registration" %] prevents p-hacking
-   Identify when observational studies support only correlation claims, not causal claims
-   Read a published paper critically using a structured framework

## Types of Studies in SE Research

-   A controlled experiment manipulates an independent variable and measures its effect on a dependent variable
    -   Lab experiments use student participants in artificial tasks; they are clean but may not generalize
    -   Field experiments run in real organizations with real developers; they are messy but more externally valid
-   A case study examines one project, one team, or one organization in depth
    -   The goal is understanding, not statistical generalization
    -   A case study can generate hypotheses that a controlled experiment later tests
-   A survey or questionnaire collects self-reported data from a sample of respondents
    -   Useful for opinions, practices, and demographics; limited by response bias and social desirability effects
    -   Survey data is almost always observational: you cannot randomize who holds which opinion
-   A mining study extracts data from repositories, bug trackers, or platforms like Stack Overflow
    -   The data is observational; you can observe correlations but cannot establish causation without additional evidence
    -   Selection bias in what gets committed, reported, or posted is a constant threat
-   A systematic literature review synthesizes findings across many studies on the same question
    -   It requires a reproducible search protocol and explicit inclusion and exclusion criteria
    -   Meta-analysis is the quantitative version: it pools effect sizes across studies to estimate an overall effect

## What Replication Means and Why It Matters

-   [%g replication "Replication" %] means repeating a study to check whether the finding holds under similar or different conditions
    -   A direct replication uses the same methods with a new sample
    -   A conceptual replication uses different methods to test the same underlying claim
-   Pizard et al. trained students to read and replicate empirical SE studies [%b Pizard2022 %]
    -   Students who went through the training were better at critiquing new claims and more likely to check statistical assumptions
    -   The act of trying to replicate forces you to notice what a paper does not tell you: missing details that seemed obvious to the authors
-   A single significant result is weak evidence; a replicated result is much stronger
    -   If you rely on a single study to guide a major engineering decision, you are taking a risk that should be visible in your design document

## Pre-Registration

-   [%g pre_registration "Pre-registration" %] means committing to your hypotheses, methods, and analysis plan before collecting data
    -   You submit your plan to a registry (OSF, AsPredicted, or similar) before running the study
    -   The timestamp proves you did not revise your hypotheses after seeing the results
-   Pre-registration prevents p-hacking: if you cannot move the goalposts after the fact, you cannot fish for a significant result
    -   It also prevents HARKing — Hypothesizing After Results are Known — where a researcher presents a post-hoc observation as a predicted hypothesis
    -   HARKing is not necessarily dishonest; researchers genuinely convince themselves that they predicted what they found
-   Pre-registration does not prevent all problems
    -   You can still analyze the data incorrectly, report a pre-registered finding selectively, or choose a sample that favors your hypothesis
    -   It raises the cost of certain kinds of error and makes the research process more transparent

## The Replication Crisis in Software Engineering

-   Nagappan et al. found that test-driven development reduced defects by 40-90% in industrial case studies [%b Nagappan2008a %]
    -   Fucci et al. found little to no effect in a controlled experiment [%b Fucci2016 %]
    -   Both studies are valid: the settings differed, the populations differed, and the effect likely depends on context
-   Treating a single study as definitive is the source of most "we heard X works, so we do X" cargo-cult practices in software teams
    -   The question is not "did one study find an effect?" but "does the preponderance of well-designed evidence support the claim?"
-   The replication crisis in SE is less severe than in psychology, partly because SE studies often have larger samples (repositories contain millions of data points) and partly because effect sizes in SE tend to be smaller and more context-dependent

## Observational Data and Causal Claims

-   Furia et al. argue that observational data in SE supports only correlation claims, not causal claims [%b Furia2023 %]
    -   If you observe that projects with more tests have fewer bugs, you cannot conclude that adding tests causes fewer bugs
    -   Projects that invest in testing probably invest in other quality practices too; the tests may be a proxy for overall quality culture
-   When a paper uses causal language ("X leads to," "X causes," "X improves") but the study is observational, that is a validity threat the authors should acknowledge
    -   Many papers do not acknowledge it, which means you have to notice it yourself
-   The vocabulary of causation: correlation, association, prediction, and explanation are defensible with observational data; cause, effect, and impact are not without a randomized design or a strong natural experiment

## Reading a Paper Critically

-   Start with the research question: is it specific enough to be testable?
    -   "Do code reviews improve quality?" is too vague; "Does mandatory pre-merge review reduce post-release defects in industrial Java projects?" is testable
-   Identify the independent and dependent variables
    -   Confirm that the statistical test used is appropriate for those variable types
-   Examine the sample: who or what was studied, how was it selected, and what is excluded?
    -   A sample of GitHub projects is not a sample of all software projects
-   Check the threats to validity section
    -   What did the authors acknowledge? What did they not?
    -   The most important threats are often the ones authors do not mention
-   Check one reported statistic for internal consistency
    -   If the paper reports a mean and standard deviation, check whether a normal distribution with those parameters is plausible given the sample size and range

## Code

[%inc compare_results.py %]

## Check Understanding

<details markdown="1">
<summary markdown="1">What is the difference between a case study and a controlled experiment? Give one example of a research question each is well-suited to answer.</summary>

A controlled experiment manipulates an independent variable to measure its causal effect: participants are assigned to conditions, everything else is held constant (or randomized), and the outcome is compared across conditions. A case study examines one situation in depth without manipulating anything: it observes, interviews, and documents. A controlled experiment is well-suited to a question like "does pair programming reduce defect rates in a two-hour coding task?" because you can assign developers randomly to work alone or in pairs. A case study is well-suited to "how did Mozilla's code review culture evolve over the first decade of Firefox development?" because you cannot randomize history, and the goal is understanding context rather than isolating a single variable.

</details>

<details markdown="1">
<summary markdown="1">The following scenario describes a pre-registration problem. What is wrong and how would proper pre-registration have prevented it?

```
# Pre-registration exercise: after running the analysis, the researcher writes:
"We hypothesized that TDD would produce higher-quality code,
 which is confirmed by our finding of p = 0.04."
# What is wrong with this as a pre-registration?
```
</summary>

Writing down the hypothesis after seeing the results is not pre-registration; it is HARKing — Hypothesizing After Results are Known. A finding of p = 0.04 is consistent with both a genuine effect and one false positive in twenty tests. When the hypothesis is written after the data is examined, you cannot distinguish which situation you are in. Proper pre-registration would have required the researcher to file the hypothesis, the statistical test, and the significance threshold with a public registry before data collection began. That timestamp makes it impossible to claim a post-hoc observation as a predicted result.

</details>

<details markdown="1">
<summary markdown="1">Why does Furia et al. [%b Furia2023 %] argue that observational data in SE supports only correlation claims, not causal claims?</summary>

Observational data cannot establish causation because you cannot control for all the other variables that might explain the relationship. If you observe that projects with code review policies have fewer bugs, you cannot rule out that those projects also have senior developers, better test coverage, and more time for quality work — any of which could explain the lower bug count. Without randomization, you cannot separate the effect of code review from the effect of being the kind of organization that adopts code review. Furia et al. argue that SE researchers should be precise about this limit: observational findings support prediction (knowing X helps predict Y) but not intervention (changing X will change Y).

</details>

<details markdown="1">
<summary markdown="1">What is HARKing, and why does pre-registration prevent it?</summary>

HARKing stands for Hypothesizing After Results are Known. It happens when a researcher runs an analysis, notices a significant result, and then writes the paper as if that result was the predicted outcome all along. HARKing is not always deliberate fraud; researchers often genuinely convince themselves they had predicted what they found. The problem is that a HARKed hypothesis has not been tested at all — the data were used to generate it, so they cannot independently confirm it. Pre-registration prevents HARKing by requiring the researcher to commit to hypotheses and analysis plans before seeing the data; any deviation from the plan must be disclosed as exploratory, not confirmatory.

</details>

## Exercises

<div class="exercise" markdown="1">

### Paper Critique (Pairs Exercise)

Work with a partner. Each pair receives a different short SE empirical paper. Identify the research question, the independent variable, the dependent variable, the sample size, and the statistical method used. Find one methodological strength that the authors handle well and one validity threat they do not acknowledge. Pick one reported statistic and check whether it is internally consistent — for example, whether the reported mean and standard deviation are plausible for the reported sample size. Present your findings to the class in two minutes.

</div>

<div class="exercise" markdown="1">

### Write a Pre-Registration

Write a two-paragraph pre-registration for the capstone study you will design in Lesson 18. The first paragraph must state your primary hypothesis precisely (naming independent and dependent variables), the statistical test you will use to evaluate it, and the minimum effect size you would consider practically meaningful. The second paragraph must describe your sample selection criteria, explain how you will handle missing data, and identify one analysis you will not run until after you have committed to these choices in writing.

</div>

<div class="exercise" markdown="1">

### Skills Needed to Replicate a Mining Study

Pizard et al. found that training students to replicate empirical SE studies made them better critics of new claims [%b Pizard2022 %]. Imagine you want to replicate a study that reports a Gini coefficient computed from mining software repositories. List three specific skills you would need to carry out that replication. For each skill, write one sentence explaining where in this tutorial you practiced it — cite the lesson number and the specific activity.

</div>

<div class="exercise" markdown="1">

### Causal Language in Observational Studies

Furia et al. distinguish between predictive models (X predicts Y) and causal models (X causes Y). Find one claim from a paper covered in this tutorial — or from any paper you have read — that uses causal language but is based on observational data. Quote the sentence exactly as it appears in the paper. Then rewrite the sentence to accurately reflect what the observational data actually support, using language about association or prediction rather than causation.

</div>

<div class="exercise" markdown="1">

### Pre-Registered Replication Plan for Bug-Contributor Findings

A finding discussed in the threats lesson states that files with many contributors tend to have more bugs [%b Bird2011 %]. Write a four-sentence pre-registered study plan to test whether this finding replicates in a new dataset: the first sentence states your null hypothesis precisely; the second sentence states your sample selection criteria including what counts as a "contributor" and what counts as a "bug"; the third sentence names the statistical test you will use and explains why that test is appropriate for this kind of data; the fourth sentence states the effect size threshold below which you would consider the effect too small to be practically meaningful, and explains why you chose that threshold.

</div>
