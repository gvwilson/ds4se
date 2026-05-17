# Lab: Does Test-Driven Development Work?

## Learning Goals

-   Reproduce Mann-Whitney U tests and Cliff's delta values from Fucci et al. [%b Fucci2016 %]
-   Evaluate how exclusion criteria affect statistical results
-   Explain why TDD and TLD produce similar outcomes in controlled experiments
-   Interpret null results in terms of statistical power

---

-   Test-driven development (TDD) is one of the most debated practices in software engineering
    -   The premise: write a failing test before writing the code that makes it pass
    -   Many developers swear by it; many others ignore it; few have looked at the evidence carefully
    -   Today you will look at the evidence yourself and decide what to believe

-   Fucci et al. ran a multi-site blind analysis with five academic sites [%b Fucci2016 %]
    -   Participants were professional developers, not students, across multiple countries
    -   Each participant implemented a feature either test-first (TDD) or test-last (TLD)
    -   Outcomes measured: number of passing tests (TESTS), external quality (QLTY), productivity (PROD)
    -   "Blind analysis" means the researchers committed to their analysis plan before seeing the results

-   The lab workflow follows the steps of a real replication study
    -   Load the Fucci dataset and inspect its structure
    -   Apply the same exclusion criteria the original authors used
    -   Run Mann-Whitney U tests on all three outcome variables
    -   Compute Cliff's delta for each outcome
    -   Compare your numbers to Table 3 of the paper
    -   If your numbers differ by more than rounding, diagnose the discrepancy before moving on

-   The target values from Fucci et al. Table 3 are:
    -   TESTS: p = 0.052, Cliff's delta = 0.19
    -   QLTY: p = 0.38, Cliff's delta = 0.12
    -   PROD: p = 0.89, Cliff's delta = 0.02

-   The code below loads the dataset, runs the tests, and prints a comparison table

[%inc replicate_fucci.py %]

-   If your p-values match the published ones to within rounding, the replication succeeded
    -   Small discrepancies often trace to differences in how null values are handled or how the
        exclusion criteria are applied — track these down before calling it a match
    -   Large discrepancies suggest a substantive difference in the dataset or the test setup

-   Fucci et al. [%b Fucci2017 %] followed up with a deeper analysis of the same data
    -   TDD and TLD produce similar outcomes in terms of quality and productivity
    -   What matters more is the rhythm of test-code interleaving: developers who switched
        frequently between writing tests and writing code performed better regardless of which came first
    -   The test-first vs. test-last distinction turns out to be less important than how granular
        the development cycle is

-   What does this mean for your team?
    -   Nagappan et al. found TDD reduced defects by 40-90% in industrial case studies [%b Nagappan2008a %]
    -   Fucci et al. found little effect in controlled experiments
    -   Both findings can be correct: controlled experiments isolate a single variable;
        industrial case studies capture the full complexity of real teams and real incentives
    -   The safest conclusion is that TDD is not magic, and TDD that is done badly is not better
        than thoughtful test-last development

-   Wrap-up: the distinction between belief and evidence matters
    -   "We believe TDD works" is not evidence
    -   "We measured TDD and found these results" is the beginning of evidence
    -   Even measured results need replication, and even replication needs interpretation

## Check Understanding

<details markdown="1">
<summary markdown="1">Fucci et al. found no significant difference in QLTY or PROD between TDD and TLD. What are two possible explanations for this null result?</summary>

One explanation is that TDD and TLD genuinely produce equivalent outcomes for quality and
productivity, at least in short controlled experiments with professional developers, and
the null result reflects the true state of affairs. A second explanation is that the study
was underpowered: with the number of participants in the study, the statistical tests could
not reliably detect a small-to-medium effect even if one existed. Dyba et al. showed that
most SE experiments lack sufficient power to detect realistic effects [%b Dyba2006 %], so a
null result often means "we could not see it" rather than "it is not there."

</details>

<details markdown="1">
<summary markdown="1">The following code produces an error when run on the Fucci data. What is the bug and how do you fix it?

```python
tdd = df.filter(pl.col("approach") == "TDD")
tld = df.filter(pl.col("approach") == "TLD")
u, p = stats.mannwhitneyu(tdd["PROD"], tld["PROD"])
```
</summary>

`stats.mannwhitneyu` requires NumPy arrays or Python lists, not Polars Series. Passing a
Polars Series directly will raise a TypeError. The fix is to call `.to_numpy()` and drop
null values before passing the data to the test:

```python
a = tdd["PROD"].drop_nulls().to_numpy()
b = tld["PROD"].drop_nulls().to_numpy()
u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
```

The `alternative="two-sided"` argument is also important: the default in older versions of
scipy is `"two-sided"`, but specifying it explicitly matches the analysis in the paper and
avoids confusion about which alternative hypothesis is being tested.

</details>

<details markdown="1">
<summary markdown="1">What does it mean for a study to be underpowered, and why might an underpowered study produce a null result even when a real effect exists?</summary>

Statistical power is the probability that a test will correctly reject the null hypothesis
when a real effect exists. A study is underpowered when its sample size is too small to
give the test a reasonable chance of detecting an effect of the expected size. If power is
0.30 for a medium effect, the test will fail to detect that effect 70% of the time purely
due to sampling noise. An underpowered study that finds p > 0.05 cannot conclude there is
no effect; it can only conclude that its sample was not large enough to see one if it is there.

</details>

<details markdown="1">
<summary markdown="1">Nagappan et al. found TDD reduced defects by 40-90% in industrial case studies, while Fucci et al. found little effect in a controlled experiment. How can both findings be correct?</summary>

The two studies measured different things in different contexts. Nagappan et al. studied
real teams on real projects over extended periods, where TDD adoption likely came bundled
with other practices: more careful design, better discipline, and organizational support
for quality. Fucci et al. isolated the test-first vs. test-last distinction in a short
controlled task, removing most of the surrounding context. It is plausible that TDD's
benefits in industry come from the culture and habits it encourages rather than from the
mechanical act of writing tests before code. The external validity of a controlled
experiment is always limited, and the internal validity of an industrial case study is
always limited. Together they are more informative than either alone.

</details>

## Exercises

<div class="exercise" markdown="1">
### Reproduce Table 3

Run `replicate_fucci.py` and compare your output to the published values for all three
outcomes. Report your reproduced p-values and Cliff's delta values alongside the published
values in a table. For any discrepancy larger than 0.01 in either p or delta, write one
sentence hypothesizing what might cause the discrepancy, considering differences in
exclusion criteria, null value handling, or test parameterization.
</div>

<div class="exercise" markdown="1">
### Effect of exclusion criteria

Rerun the Mann-Whitney U tests for all three outcomes without applying any exclusion
criteria used in the original analysis (include all rows in the dataset). Report how the
p-values change compared to the analysis with exclusions. Write two sentences explaining
whether the exclusion decisions strengthen or weaken the main finding, and whether you
think the original authors were justified in applying them.
</div>

<div class="exercise" markdown="1">
### Operationalizing rhythm

Fucci et al. [%b Fucci2017 %] found that the rhythm of test-code interleaving matters more
than whether tests are written first or last. Write one sentence defining an
operationalization of "rhythm" that could be measured from a version control history (for
example, using commit timestamps and commit messages or file names to identify test commits
vs. implementation commits). Write a second sentence describing the dataset you would need
to measure this operationalization across a sample of open-source projects.
</div>

<div class="exercise" markdown="1">
### Power analysis

Using `scipy.stats` or a power analysis library such as `statsmodels.stats.power`, compute
the statistical power of a Mann-Whitney U test with the actual sample sizes in the Fucci
dataset to detect a medium effect (Cliff's delta ≈ 0.3). Report the power value. Write
two sentences explaining what this power level implies for how much confidence you should
place in the null results for QLTY and PROD, given that both outcomes showed p > 0.05.
</div>

<div class="exercise" markdown="1">
### Reconciling contradictory findings

Nagappan et al. found TDD reduced defects by 40-90% in industrial case studies [%b Nagappan2008a %],
while Fucci et al. found little effect in a controlled experiment. Write three sentences
reconciling these findings, using the concepts of external validity, confounds, and effect
size. Your answer should explain how both studies can be correct without either being
dishonest or incompetent.
</div>
