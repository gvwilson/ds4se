# Reading and Critiquing the Literature

## Learning Goals

-   Find SE research papers in [IEEE Xplore][ieee-xplore], [ACM Digital Library][acm-dl], and [arXiv][arXiv]
-   Apply a structured reading order: abstract, conclusion, figures, then methods
-   Identify statistical red flags in published papers
-   Reproduce one specific statistic from a paper using only its reported numbers

## Finding Papers

-   The main venues for software engineering research are conferences and journals
    -   Key conferences: ICSE (International Conference on Software Engineering), FSE (Foundations of Software Engineering), MSR (Mining Software Repositories), ESEM (Empirical Software Engineering and Measurement)
    -   Key journals: TSE (IEEE Transactions on Software Engineering), EMSE (Empirical Software Engineering), IST (Information and Software Technology)
    -   [IEEE Xplore][ieee-xplore] indexes IEEE conferences and journals; [ACM Digital Library][acm-dl] indexes ACM venues; many papers appear in both
-   [arXiv][arXiv] hosts preprints: drafts that have not yet been peer-reviewed
    -   A preprint may be a submitted version of a paper that later appeared in a venue, or it may never have been reviewed at all
    -   Be appropriately skeptical: peer review is imperfect, but it does catch some errors that preprints carry permanently
-   Google Scholar indexes all of these and is often the fastest starting point
    -   It also tracks citations, which lets you find newer papers that built on an older one
    -   Citation counts are not a measure of correctness

## Reading Order

-   Reading a paper from abstract to conclusion in sequence is rarely the most efficient strategy
    -   The abstract tells you what the authors claim; read it first to decide whether to continue
    -   The conclusion is where authors summarize findings and acknowledge limitations; read it second
    -   Figures and tables carry most of the empirical weight; read them third, before the methods
    -   The methods section tells you how to evaluate whether the figures are trustworthy; read it last
-   Most papers bury the most important caveats in the threats-to-validity section
    -   Authors are required by many venues to include this section, but there is no incentive to make it prominent
    -   A threats section that says "we acknowledge that our sample size is small" in the second-to-last paragraph is not an endorsement of the result
-   Reading the conclusion before the methods helps you decide which methodological details matter
    -   If the conclusion depends on a particular statistical test, you know to look at that test carefully
    -   If the conclusion makes a causal claim but the methods are observational, you have found the gap worth scrutinizing

## Identifying Statistical Red Flags

-   A p-value reported without an effect size tells you nothing about practical importance
    -   With a large enough sample, any difference becomes statistically significant
    -   An effect size (Cohen's d, Cliff's delta, or similar) is needed to know whether the difference is meaningful
-   No confidence intervals means you cannot assess the precision of the estimate
    -   A mean of 15.2 is not useful without knowing whether the plausible range is 14–16 or 10–20
-   N < 30 with parametric tests and no normality check is a common problem in older SE papers
    -   Parametric tests assume normal distributions; with small samples, that assumption is untestable without explicit checking
    -   The appropriate response is either to report a normality test or to use a non-parametric alternative
-   Comparison groups that differ on more than one variable make causal interpretation impossible
    -   If teams using Copilot are also more experienced than teams not using it, you cannot separate the tool's effect from the experience effect
-   Self-selected samples presented as representative are a widespread problem
    -   Developers who volunteer for a study, or projects that opt into a tool's beta program, are not random draws from the population of developers or projects
    -   Results from self-selected samples can only be generalized with caution and explicit justification

## The Gap Between Research and Practice

-   Lo et al. surveyed practitioners at Microsoft on which software engineering research topics they find relevant [%b Lo2015 %]
    -   Most practitioners ranked topics related to their daily work — debugging, testing, code review — as highly relevant
    -   Many practitioners reported that they never read research papers, citing inaccessibility and lack of time
-   This is a two-way problem: researchers write for other researchers, and practitioners do not read the results
    -   Plain-language summaries, practitioner-targeted venues, and embedded researchers (industrial doctorates, research teams inside companies) are partial responses
    -   The gap means that practice often lags behind evidence by years, and that evidence is sometimes disconnected from what practice actually needs

## Check Understanding

<details markdown="1">
<summary markdown="1">What is wrong with a paper that reports N < 30 with a parametric test but no normality check? What should the authors have done instead?</summary>

Parametric tests like t-tests and ANOVA assume that the data come from a normally distributed population. With small samples, you cannot reliably verify this assumption from the data itself. Running the test anyway produces p-values and confidence intervals that may be badly wrong if the distribution is skewed or has heavy tails. The authors should either have reported a normality test (Shapiro-Wilk is standard for small samples) and justified using the parametric test if the result was non-significant, or used a non-parametric alternative such as the Mann-Whitney U test that does not require the normality assumption.

</details>

<details markdown="1">
<summary markdown="1">A paper reports mean = 15.2, standard deviation = 4.3, N = 50, and a 95% confidence interval of [14.0, 16.4]. Is this confidence interval correct? If not, what is the correct value?</summary>

The reported interval is wrong. The standard formula for a 95% confidence interval is approximately mean ± 1.96 × (standard deviation / sqrt(N)). Plugging in the numbers: 1.96 × (4.3 / sqrt(50)) = 1.96 × (4.3 / 7.07) = 1.96 × 0.608 = 1.19. The correct interval is approximately [15.2 − 1.19, 15.2 + 1.19] = [14.01, 16.39], which rounds to [14.0, 16.4]. In this case the reported interval happens to be correct, and this question is checking whether you can reproduce it. If a paper reported [14.5, 15.9] instead, that would be inconsistent with the stated standard deviation and sample size, and worth flagging.

</details>

<details markdown="1">
<summary markdown="1">What does it mean for a sample to be "self-selected"? Give an example from SE research where self-selection would distort results.</summary>

A self-selected sample is one where the people or projects in the study chose to participate rather than being randomly assigned or randomly drawn from a population. In SE research, a common example is a study of open-source project quality that uses only projects that opted into a code quality tool's analysis service. Projects that choose to use a quality tool are probably already more quality-conscious than projects that do not; the study therefore overestimates quality in the population of open-source projects as a whole. Any result from that study — "median technical debt is X" — does not generalize to projects that ignored the tool.

</details>

<details markdown="1">
<summary markdown="1">Why should you read a paper's conclusion before its methods section?</summary>

The conclusion tells you what the authors claim their study shows. Knowing the claim in advance lets you read the methods with a specific question in mind: does this method actually support that conclusion? If the conclusion makes a causal claim ("adopting linters reduces bugs"), you know to look for whether the methods involved randomization or only observation. If you read methods first, you absorb a lot of detail without knowing which parts are load-bearing for the final argument.

</details>

<details markdown="1">
<summary markdown="1">Lo et al. found that many practitioners do not read SE research. What would need to change for research to be more accessible and relevant to practitioners?</summary>

At minimum, venues would need to require plain-language summaries written for a non-specialist audience, and researchers would need incentives to produce them. The research questions themselves would need to connect more directly to decisions practitioners actually face, rather than being driven primarily by what is tractable with available data. Practitioners would need channels through which to communicate what they find confusing or irrelevant. None of this is technically difficult; it is a coordination and incentive problem. The most promising existing interventions are embedded researchers in industry and practitioner-facing publication tracks at major conferences.

</details>

## Exercises

<div class="exercise" markdown="1">

### Paired Paper Review

In pairs, each pair receives a different short SE paper. Identify the research question, the independent variable, the dependent variable, the sample size, and the statistical method used. Find one thing the authors did well methodologically. Find one validity threat the authors did not discuss in their threats-to-validity section. Pick one reported statistic — a percentage, a mean, a Cohen's d — and check whether it is consistent with other numbers in the same paper. Present your findings in two minutes, ending with the sentence: "We reproduced / could not reproduce the claim that ___."

</div>

<div class="exercise" markdown="1">

### Threats Not Acknowledged

Pick any paper discussed in this tutorial that you did not use for the paired review exercise. Read its threats-to-validity section carefully. List every threat the authors acknowledge. Then list at least one threat they do not acknowledge. Write two sentences explaining why the unacknowledged threat matters for interpreting the paper's conclusions, and rate how serious you think it is on a scale from minor to fatal.

</div>

<div class="exercise" markdown="1">

### Plain-Language Summary

Write a one-paragraph plain-language summary of any one study from this tutorial, aimed at a software developer who has never read an academic paper. Your summary must state the main finding in one sentence that avoids statistical jargon, give the sample size in plain terms ("the researchers studied forty developers over six months"), and include one sentence explaining a reason to be cautious about generalizing the result to other contexts.

</div>

<div class="exercise" markdown="1">

### Verifying a Table Entry

Take any table of results from a paper covered in this tutorial. Identify one number in the table that you can compute from other numbers in the same paper — for example, a percentage derived from a count and a total, or a Cohen's d derived from two group means and standard deviations. Compute it yourself using the reported values. Report whether your computed value matches the published value. Write one sentence explaining what a mismatch would imply about the paper's reliability.

</div>

<div class="exercise" markdown="1">

### Evaluating a Preprint Claim

A preprint on arXiv claims that a new code review tool reduces review time by 40% based on a study of eight developers over two weeks. List four specific red flags in that claim. For each one, write one sentence explaining what additional information would let you decide whether the flag represents a serious problem or a minor limitation of an otherwise sound study.

</div>
