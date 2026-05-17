# The Logic of Hypothesis Testing

## Learning Goals

-   State and distinguish the null hypothesis, p-value, and confidence interval
-   Explain Type I and Type II errors and why SE studies are often underpowered
-   Apply the Bonferroni correction when running multiple tests
-   Run a two-sample t-test and interpret the result

## Lesson

-   Every statistical test starts with a [%g null_hypothesis "null hypothesis" %]: the assumption that there is no effect
    and any difference you see is random noise
    -   For a line-length comparison: "Python and JavaScript files have the same median line length;
        any observed difference is due to chance"
    -   You do not try to prove your hypothesis; you try to reject the null
-   The [%g p_value "p-value" %] is the probability of seeing a difference at least as large as the one you observed,
    if the null hypothesis were true
    -   A small p-value means your data would be surprising in a world where nothing is going on
    -   It is not the probability that the null hypothesis is true
    -   It is not the probability that your result is a fluke
    -   Misreading the p-value is the single most common error in empirical SE papers
-   The conventional significance threshold is 0.05, meaning a 1-in-20 chance of a false alarm
    -   This number is arbitrary: Fisher proposed it as a rough guideline in 1925 and it stuck
    -   Some fields use 0.01; particle physicists use 0.0000003; the choice depends on how bad a false alarm is
    -   A result just below 0.05 is not meaningfully different from one just above it
-   A [%g type_i_error "Type I error" %] (false positive) occurs when you reject a null hypothesis that is actually true
    -   With a threshold of 0.05, you will make this mistake 5% of the time even when doing everything right
    -   A [%g type_ii_error "Type II error" %] (false negative) occurs when you fail to reject a null hypothesis that is false
    -   The probability of avoiding a Type II error is [%g statistical_power "statistical power" %]
-   Most SE studies are dramatically underpowered
    -   Dyba et al. reviewed 103 controlled experiments published in SE journals [%b Dyba2006 %]
    -   The majority did not have enough participants to reliably detect a realistic effect
    -   If your study cannot detect an effect of realistic size, a non-significant result tells you almost nothing
    -   "We found no significant difference" may mean there is no difference, or it may mean your study was too small to see it
-   [%g p_hacking "P-hacking" %] is what happens when researchers run many tests and report only the significant ones
    -   If you run 20 independent tests, you expect one to come up significant by chance alone
    -   The [%g bonferroni_correction "Bonferroni correction" %] controls for this: if you run K tests,
        require p < 0.05 / K for any single result to count as significant
    -   Running 20 tests and requiring p < 0.0025 keeps the family-wise error rate at 5%
    -   The correction is conservative but simple; more sophisticated alternatives exist
-   A [%g confidence_interval "confidence interval" %] gives you a range of plausible values for the true effect,
    not just a yes/no verdict
    -   A 95% confidence interval means: if you repeated this study many times,
        95% of the intervals you constructed would contain the true value
    -   A CI that includes zero is consistent with no effect; a CI far from zero is more informative
    -   Confidence intervals convey more information than bare p-values and should be reported alongside them
-   Furia et al. catalogued a long list of analytic pitfalls in SE research [%b Furia2022 %]
    -   Using the wrong test for the data type (e.g., a t-test on ordinal data)
    -   Ignoring violations of test assumptions without checking them
    -   Reporting p-values without verifying that the model fits the data
    -   These problems are common enough that reviewers should ask for them explicitly
-   The code below loads Python and JavaScript line-length data, computes median line length
    per file, and runs a two-sample t-test

[%inc ttest.py %]

-   The t-statistic of -269.67 and p-value near zero mean the difference is highly significant
    -   The sign of t tells you which group is larger; the magnitude tells you how many standard errors apart the means are
    -   When p rounds to 0.0, report it as p < 2.2 × 10⁻¹⁶ or use scientific notation; never write "p = 0"
    -   The confidence interval tells you the range of plausible values for the true difference in means

## Check Understanding

<details markdown="1">
<summary markdown="1">What two common misinterpretations of the p-value should you always avoid?</summary>

The p-value is not the probability that the null hypothesis is true, and it is not the
probability that your result is a fluke. It is the probability of observing data at least
as extreme as yours, assuming the null hypothesis were true. Confusing these leads to
conclusions like "there is only a 4% chance we are wrong," which is not what p = 0.04
means. The null hypothesis is either true or false; probability applies to your data
given the null, not to the null given your data.

</details>

<details markdown="1">
<summary markdown="1">The following code runs 20 comparisons and reports the significant ones. What is wrong and how do you fix it?

```python
results = []
for lang_pair in language_pairs:  # 20 pairs
    t, p = stats.ttest_ind(data[lang_pair[0]], data[lang_pair[1]])
    if p < 0.05:
        results.append((lang_pair, p))
print(f"Found {len(results)} significant differences!")
```
</summary>

With 20 independent tests at a threshold of 0.05, you expect one false positive by chance
alone even when no real differences exist. The code reports any result that crosses 0.05
as a finding, which inflates the false positive rate. Apply the Bonferroni correction by
dividing the threshold by the number of tests:

```python
threshold = 0.05 / len(language_pairs)
results = []
for lang_pair in language_pairs:
    t, p = stats.ttest_ind(data[lang_pair[0]], data[lang_pair[1]])
    if p < threshold:
        results.append((lang_pair, p))
print(f"Found {len(results)} significant differences (Bonferroni-corrected threshold: {threshold:.4f})")
```

</details>

<details markdown="1">
<summary markdown="1">Why does a very large sample size not automatically make a study more trustworthy?</summary>

With a large enough sample, a t-test will detect arbitrarily small differences as
statistically significant. A study comparing two million lines of code might find that
Python lines average 0.3 characters longer than JavaScript lines, with p < 0.0001, but
a 0.3-character difference has no practical consequence for anyone. Statistical
significance and practical importance are separate questions. Large samples also amplify
small biases in data collection: if the Python files were sampled from different projects
than the JavaScript files, that confound becomes a highly significant result.

</details>

<details markdown="1">
<summary markdown="1">A study finds p = 0.04 with N = 8. Should you trust this finding? What would make you more confident?</summary>

A p-value of 0.04 with only 8 observations should be treated with skepticism. With such
a small sample, statistical power is low, meaning the study would often miss real effects.
Paradoxically, the effects that do clear the significance bar in small studies tend to be
large overestimates of the true effect. You should want to see a pre-registered replication
with a larger sample (at least 30-50 per group for a medium effect), a confidence interval
for the effect size, and a plausible causal mechanism. A single small study with p just
below 0.05 is weak evidence.

</details>

## Exercises

<div class="exercise" markdown="1">
### Reproduce the t-statistic

Run the code in `ttest.py` and verify that you get t = -269.67 and p ≈ 0.0. Then
filter both datasets to keep only lines between 2 and 200 characters (excluding blank
lines and unusually long auto-generated lines) and re-run the test. Report whether the
finding is still statistically significant and whether the t-statistic changes substantially.
If you ran both the full-data test and the filtered test, should you apply a Bonferroni
correction? Explain your reasoning.
</div>

<div class="exercise" markdown="1">
### Bootstrapped t-statistics

Write a loop that draws a random sample of 500 rows from each of the Python and JavaScript
datasets, runs a two-sample t-test, and records the t-statistic. Repeat this 20 times.
Plot the distribution of the 20 t-statistics as a histogram using Altair. Describe in one
sentence whether the t-statistic is stable across subsamples and what that stability (or
instability) implies about the robustness of the original finding.
</div>

<div class="exercise" markdown="1">
### Confidence interval interpretation

Using the full Python and JavaScript datasets, compute the 95% confidence interval for
the difference in mean line lengths between the two languages. Write a two-sentence
interpretation that a software team lead (not a statistician) could act on. Then explain
in one sentence why the confidence interval conveys more information than a bare p-value
for this kind of decision.
</div>

<div class="exercise" markdown="1">
### Bonferroni in practice

A colleague tested all pairwise combinations of 6 programming languages (15 pairs total)
and found 5 results significant at p < 0.05. Apply the Bonferroni correction and report
how many of the 5 survive at the corrected threshold. Write one sentence explaining to
the colleague why applying the correction is not optional when testing multiple hypotheses
on the same dataset.
</div>

<div class="exercise" markdown="1">
### Pairwise test function

Write a function called `pairwise_ttests` that accepts a Polars dataframe with columns
`language` and `line_length` and returns a Polars dataframe with one row per pair of
languages, containing columns `lang_a`, `lang_b`, `t_statistic`, and `p_value`. Apply
it to at least three language pairs from the line-length dataset and display the result
sorted by p-value. Verify that the t-statistics match what you get when you call
`stats.ttest_ind` directly on each pair.
</div>
