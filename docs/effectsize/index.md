# Effect Size and Practical Significance

## Learning Goals

-   Distinguish statistical significance from practical significance
-   Compute [%g cohens_d "Cohen's d" %], [%g cles "common-language effect size" %], and [%g cliffs_delta "Cliff's delta" %] and interpret each
-   Explain why DeOliveiraNeto et al. found most SE papers fail to report [%g effect_size "effect sizes" %]
-   Use effect size to evaluate TDD outcomes from Fucci et al.

---

-   A p-value tells you whether an effect exists; an [%g effect_size "effect size" %] tells you whether it matters
    -   With N = 100,000, even a difference of 0.001 lines of code per hour can produce p < 0.05
    -   With N = 10, even a genuinely large difference may not reach significance
    -   Statistical significance and practical importance are separate questions that require separate answers

-   [%g cohens_d "Cohen's d" %] measures the standardized difference between two group means
    -   d = (mean of group A − mean of group B) / pooled standard deviation
    -   The pooled standard deviation puts both groups on the same scale
    -   Rough guidelines: d ≈ 0.2 is small, d ≈ 0.5 is medium, d ≈ 0.8 is large
    -   These guidelines come from Cohen's 1977 textbook and are heuristics, not laws

-   [%g cles "Common-language effect size" %] (CLES) is the probability that a randomly chosen value
    from group A is larger than a randomly chosen value from group B
    -   A CLES of 0.5 means the groups are indistinguishable; 0.7 means group A is larger 70% of the time
    -   Much easier to explain to a non-statistician than Cohen's d
    -   Compute it as the Mann-Whitney U statistic divided by n1 × n2

-   [%g cliffs_delta "Cliff's delta" %] is a non-parametric effect size for ordinal data
    -   It measures the probability that a value from group A exceeds a value from group B,
        minus the probability that a value from group B exceeds a value from group A
    -   Ranges from -1 to 1; values near 0 indicate no difference; values near ±1 indicate near-total separation
    -   Prefer Cliff's delta over Cohen's d when data is ordinal or when distributions are heavily skewed

-   DeOliveiraNeto et al. reviewed more than 5,000 SE papers and found that very few report effect sizes [%b DeOliveiraNeto2019 %]
    -   Papers report p-values but rarely say how large the effect is
    -   This makes it impossible to tell whether a significant result is important or trivial
    -   A paper that says "TDD reduced defects significantly (p = 0.03)" but gives no effect size
        has told you almost nothing useful for deciding whether to adopt TDD

-   Furia et al. make a related point: conflicting conclusions in SE often arise from ignoring confounds,
    not from genuine disagreement about the data [%b Furia2022 %]
    -   Effect sizes help because they are more stable across analysis choices than p-values
    -   Reporting both p-values and effect sizes gives readers more to work with

-   The code below loads the Fucci TDD dataset and computes Cohen's d and Cliff's delta
    for three outcome variables

[%inc cohens_d.py %]

-   The paper describes a "small" effect for PROD; verify whether your computed d is consistent with that claim
    -   Small means d ≈ 0.2 by Cohen's guidelines
    -   Cliff's delta near 0 means the groups overlap substantially
    -   A "statistically significant small effect" in a software engineering study should change practice only
        if the practical context makes even a small improvement worthwhile

## Check Understanding

<details markdown="1">
<summary markdown="1">A study finds p = 0.0001 with N = 500,000. Does this mean the effect is large? Explain.</summary>

No. With half a million observations, a t-test will detect effects so small they are
meaningless in practice. A difference of 0.1 lines of code per function, or 0.002
extra defects per month, can produce p = 0.0001 at that sample size. The p-value
tells you that the observed difference is unlikely to be due to chance, not that the
difference is large enough to care about. You need an effect size (Cohen's d, Cliff's
delta, or a confidence interval for the difference) to judge practical significance.

</details>

<details markdown="1">
<summary markdown="1">The following function computes something, but it is not Cohen's d. What is wrong and how do you fix it?

```python
def cohens_d(group_a, group_b):
    return (group_a.mean() - group_b.mean()) / group_a.std()
```
</summary>

The function divides by the standard deviation of group A alone, rather than the pooled
standard deviation of both groups. If group A has a much smaller spread than group B,
this inflates d; if it has a larger spread, it deflates d. The pooled standard deviation
accounts for variability in both groups symmetrically, so the result does not change
depending on which group you label A. The fix is:

```python
def cohens_d(group_a, group_b):
    pooled_std = np.sqrt((group_a.std()**2 + group_b.std()**2) / 2)
    return (group_a.mean() - group_b.mean()) / pooled_std
```

</details>

<details markdown="1">
<summary markdown="1">What does a CLES of 0.55 mean in plain language?</summary>

If you picked one person at random from group A and one person at random from group B,
the person from group A would have the higher value 55% of the time. That is only
slightly better than a coin flip. While the difference between the groups may be
statistically significant, a CLES of 0.55 means the groups overlap so much that knowing
which group someone is in barely helps you predict their outcome. A CLES near 0.5 is
one good way to communicate a small practical effect to a non-technical audience.

</details>

<details markdown="1">
<summary markdown="1">Why is Cliff's delta preferable to Cohen's d for ordinal outcome variables?</summary>

Cohen's d is computed from means and standard deviations, which assume the data is at
least interval-level (i.e., that equal differences in the scale represent equal real-world
differences). Ordinal data does not satisfy this assumption: the difference between
"strongly agree" and "agree" is not necessarily the same as the difference between "agree"
and "neutral." Cliff's delta works on ranks, so it only requires that you can order the
values, not that the distances between them are meaningful. It is also more robust to
skewed distributions and outliers, which are common in SE survey data.

</details>

## Exercises

<div class="exercise" markdown="1">
### Cohen's d for Working Hours

Using the weekday and weekend programmer-hours data from the previous lesson, compute
Cohen's d for the difference in hours worked. The t-test found p ≈ 10⁻³¹, which is about
as small as p-values get. What is d? Based on Cohen's rough guidelines, how would you
characterize the effect? Write two sentences directed at a manager considering a policy
of discouraging weekend work: one based on the p-value and one based on Cohen's d, and
explain which sentence is more useful for making that decision.
</div>

<div class="exercise" markdown="1">
### CLES for Working Hours

Compute the CLES for the weekday versus weekend programmer-hours comparison. Write exactly
one sentence interpreting the result in plain English, using language that a project
manager who has never taken a statistics course would understand. Then write one sentence
explaining why CLES is easier to communicate to that audience than Cohen's d.
</div>

<div class="exercise" markdown="1">
### Small Effect, No Significance

Construct a synthetic dataset in Python where Cohen's d is approximately 0.8 (a large
effect by Cohen's guidelines) but the t-test produces p > 0.05. Report the sample size
you needed to make this happen. Explain in one sentence what this demonstrates about the
relationship between effect size and statistical significance.
</div>

<div class="exercise" markdown="1">
### Effect Size for Prechelt Data

From the Prechelt data analyzed in the first lesson, pick one statistically significant
p-value you found earlier (e.g., a comparison between two languages on work hours).
Compute Cohen's d for that comparison. Write one sentence describing whether the effect
size strengthens or weakens the claim that the difference is practically important for a
team deciding which language to use.
</div>

<div class="exercise" markdown="1">
### Cliff's Delta Table for TDD Outcomes

Using the Fucci TDD dataset, compute Cliff's delta for all three outcome variables (TESTS,
QLTY, and PROD). Present the results as a Polars dataframe with columns `outcome`,
`cliffs_delta`, and `label`, where `label` is one of "negligible" (|delta| < 0.147),
"small" (< 0.33), "medium" (< 0.474), or "large" (≥ 0.474). Write one sentence summarizing
what the table implies for a development team considering whether to adopt TDD.
</div>
