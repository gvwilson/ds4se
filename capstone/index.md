# Capstone: Design Your Own Study

## Learning Goals

-   Identify an existing published result to replicate as a baseline
-   Write a complete one-page study design with research question, data, variables, analysis, and threats
-   Give and receive structured methodological critique using the framework from the previous lesson

## Part 1: Choose a Replication Baseline (10 minutes, individual)

-   Before designing a new study, identify an existing result you intend to replicate
    -   A replication baseline is not just background reading; it is a specific claim you will try to reproduce with your own data before you extend it
    -   You cannot evaluate whether your new result is different from prior work unless you first verify that you can reproduce prior work at all
-   Pick one published result from the studies covered in this tutorial
    -   State the claim in one sentence ("Fucci et al. found no significant difference in external quality between TDD and TLD in a multi-site study")
    -   Identify the key number (effect size, p-value, or percentage)
    -   Identify the dataset or data type the original authors used
-   At this stage, just confirm that the baseline claim is specific enough to check
    -   Vague baselines ("studies show TDD is good") cannot be replicated
    -   A good baseline has a number, a sample, and a method

## Part 2: Design Your Study (20 minutes, individual)

-   Pick one research question from the list below, or propose your own with instructor approval
    -   Does code review comment length predict whether the comment is accepted?
    -   Do projects that adopt linters have fewer bugs in later commits?
    -   Is there a relationship between number of dependencies and how long a package stays active?
    -   Does time between bug report and fix vary by programming language?
    -   Do commit messages written at night differ in quality from those written during the day?
-   Write a one-page study design covering each of the following components
    -   Research question: one sentence
    -   Connection to your replication baseline: how does your new question extend or challenge the prior result?
    -   Data source: where will you get data and how will you access it?
    -   Variables: what exactly will you measure, how will you operationalize each variable, and how will you handle missing data?
    -   Analysis: which statistical methods from this tutorial apply, and why are they appropriate for your data type and research question?
    -   Threats: at least three specific threats to validity, each with a proposed mitigation
    -   Interpretation: what would a positive result look like, and what would a null result mean?

## Part 3: Group Critique (30 minutes, groups of three)

-   Share your designs within your group; each person has about eight minutes total
    -   The designer presents for two to three minutes
    -   The other two give specific feedback for five to six minutes
-   Use the red-flag framework from the previous lesson to structure your feedback
    -   Identify the single biggest methodological risk in each design
    -   Comment on whether the variables are operationalized specifically enough to measure
    -   Check whether the proposed analysis matches the data type (categorical, continuous, ordinal)
-   For each design, answer this question as a group: can the replication baseline actually be reproduced with the proposed data?
    -   If not, what would need to change in the data source or the design?
    -   This is not a failure; it is useful information before anyone spends time collecting data

## Check Understanding

<details markdown="1">
<summary markdown="1">What is the difference between a replication baseline and your new research question?</summary>

A replication baseline is a specific published claim you are trying to reproduce — same question, same method, same kind of data, checking whether you get the same number. A new research question is something you want to investigate that goes beyond the original study: a different context, a different variable, a different population. The baseline matters because it lets you calibrate your methods before you trust your new results. If you cannot reproduce the original finding, you should understand why before you try to extend it.

</details>

<details markdown="1">
<summary markdown="1">What is wrong with this study design? "We will collect tweets mentioning our product and count positive vs. negative words to measure user satisfaction with our new feature." List two specific problems.</summary>

The first problem is that tweets about a product are a self-selected sample: only users who felt strongly enough to post something publicly are included, which excludes the silent majority. Satisfaction measured from tweets is not representative of satisfaction in the user base as a whole. The second problem is that counting positive vs. negative words (a simple lexicon-based sentiment analysis) conflates many things: sarcasm, complaints about unrelated issues, and neutral technical questions will all be misclassified. The operationalization of "user satisfaction" as word polarity is too coarse to be meaningful.

</details>

<details markdown="1">
<summary markdown="1">Why does Part 3 of the capstone require you to check whether your replication baseline can actually be reproduced with your proposed data?</summary>

A study design can be logically coherent and still be impossible to execute if the data it requires does not exist or cannot be accessed. Checking whether your proposed data can reproduce the baseline forces you to confront this early, when you can still adjust the design. If the baseline requires a dataset you cannot access, or variables that your data source does not record, you need to know that before collecting data rather than after analyzing it.

</details>

<details markdown="1">
<summary markdown="1">What makes a study "pre-registered" rather than just "planned in advance"?</summary>

Pre-registration means submitting your research question, hypotheses, data collection procedure, and analysis plan to a public registry before you collect or see any data. The timestamp proves that you decided what to test before you saw the results. Planning in advance without pre-registration can still involve unconscious adjustment of the analysis after seeing the data — choosing which test to report, which outliers to exclude, or which subgroup to highlight based on what the data show. Pre-registration does not prevent errors, but it prevents the specific error of treating exploratory findings as confirmatory ones.

</details>

## Exercises

<div class="exercise" markdown="1">

### Looking Back

Looking back across all 18 sessions, identify the single concept that most changed how you think about software engineering claims you encounter in blog posts, conference talks, or vendor marketing. Write three sentences: state the concept in one sentence using plain language, describe a specific claim you have seen in the wild that this concept helps you evaluate, and explain what question you would now ask before accepting that claim.

</div>

<div class="exercise" markdown="1">

### Replication Divergence

You have replicated results from at least five published studies in this tutorial. Identify the replication in which your numbers diverged most from the published values. Write two sentences: describe the divergence (what the paper reported versus what you computed) and give your best explanation for it. Then write one sentence about what that experience implies for how much weight you should give to a single published result when making a decision.

</div>

<div class="exercise" markdown="1">

### Study Type

This tutorial covered controlled experiments, observational studies, and mining studies. For the study you designed in Part 2 of this capstone, identify which type you ended up with. Write two sentences explaining one specific change to your design that would move it one step closer to a controlled experiment, and then write one sentence assessing whether that change is feasible given realistic constraints of time, access, and ethics.

</div>

<div class="exercise" markdown="1">

### Measuring Productivity

Noda et al. argue that developer productivity is multidimensional [%b Noda2023 %]. If your employer asked you to evaluate whether a new tool increases team productivity, write three sentences describing the measurement approach you would use: one sentence naming at least two dimensions of productivity you would measure and how you would operationalize them, one sentence identifying which statistical method from this tutorial you would apply and why, and one sentence identifying the single biggest threat to validity in your proposed approach and how you would mitigate it.

</div>
