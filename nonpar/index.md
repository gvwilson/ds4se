# Non-Parametric Methods and Rank-Based Tests

## Learning Goals

-   Apply [%g bootstrap_resampling "bootstrap resampling" %] to compute confidence intervals without distributional assumptions
-   Run a [%g kruskal_wallis "Kruskal-Wallis test" %] and explain why it is preferable to one-way ANOVA for SE data
-   Compute Spearman rank correlation between teacher predictions and student error data
-   Reproduce the Brown and Altadmri finding that educators' rankings correlate poorly with Blackbox data

## When to Distrust Parametric Tests

-   Parametric tests like the t-test assume the data follow a specific distribution, usually normal
    -   SE data — error counts, response times, bug counts, commit counts — is almost never normally distributed
    -   Applying a parametric test to heavily skewed count data produces p-values you cannot trust
-   Rank-based and resampling methods make no distributional assumptions
    -   They transform the data into ranks or resample it directly, then compute statistics on those
    -   The cost is slightly lower power when the normality assumption would actually hold, which in SE research is rare enough to be worth ignoring

## What Brown and Altadmri Found

-   Brown and Altadmri asked experienced programming teachers to rank the most common mistakes novice programmers make [%b Brown2017 %]
    -   They then compared those rankings to actual frequency data from Blackbox, a system that logged millions of student Java compilation attempts
    -   Teachers were wrong in systematic ways: they over-predicted mistakes they teach explicitly and under-predicted mistakes students actually make repeatedly
-   The key finding is not just that teachers were wrong, but that their errors were consistent
    -   If teachers were wrong randomly, averaging across many teachers would give you a reasonable estimate
    -   Because the errors are systematic, averaging makes the bias worse

## Spearman Rank Correlation

-   Spearman rank correlation measures whether two ranked lists agree, without assuming the distances between ranks are equal
    -   Pearson correlation assumes that the difference between ranks 1 and 2 is the same as between ranks 9 and 10
    -   Spearman makes no such assumption: it converts both variables to ranks and then computes Pearson on the ranks
-   A Spearman r of 1.0 means the two lists are in perfect agreement; -1.0 means they are perfectly reversed; 0 means no monotone relationship
    -   For the Brown and Altadmri data, r values close to zero or negative mean individual teachers are not reliably tracking what students actually struggle with
-   Use `scipy.stats.spearmanr` and read the `.statistic` attribute for the correlation value

## Kruskal-Wallis Test

-   The [%g kruskal_wallis "Kruskal-Wallis test" %] compares more than two groups without assuming normality
    -   It is the rank-based generalization of the Mann-Whitney U test
    -   The null hypothesis is that all groups are drawn from the same distribution
-   It is preferable to one-way ANOVA for SE data because ANOVA assumes that observations within each group are normally distributed with equal variance
    -   Error counts in different categories violate both assumptions routinely
    -   Kruskal-Wallis converts all observations to ranks across the combined dataset and tests whether the average ranks differ by group
-   A significant Kruskal-Wallis result tells you that at least one group differs; it does not tell you which ones
    -   Follow up with pairwise Mann-Whitney U tests and apply the Bonferroni correction

## Bootstrap Resampling

-   [%g bootstrap_resampling "Bootstrap resampling" %] estimates the sampling distribution of any statistic without assuming a distribution
    -   Draw N samples with replacement from your data (N = size of the original dataset)
    -   Compute your statistic on the resample
    -   Repeat 1,000 or more times
    -   Take the 2.5th and 97.5th percentiles of the resulting distribution as your 95% confidence interval
-   The bootstrap works for almost any statistic: means, medians, Gini coefficients, Spearman correlations, regression slopes
    -   The only requirement is that your original sample is a reasonable representation of the population
    -   It does not fix a biased sample; it only quantifies uncertainty given the sample you have
-   Use `numpy.random.default_rng` with a fixed seed for reproducibility, and `rng.choice(..., replace=True)` for the resample
    -   Never use the deprecated `numpy.random.choice`; the new generator API is safer and faster

## When to Bootstrap vs. When to Use a Parametric Test

-   Use bootstrap when: the data is non-normal, the statistic has no closed-form sampling distribution, the sample is small, or you want a check on a parametric result
-   Use parametric tests when: you have strong theoretical reasons to expect normality, you need maximum power with a large sample, or you are computing a statistic for which bootstrap is known to perform poorly (e.g., the minimum or maximum)
-   In practice, running both and checking for disagreement is a useful diagnostic
    -   If the bootstrap CI and the parametric CI are very different, the parametric assumptions are probably violated

## Code

[%inc bootstrap.py %]

## Check Understanding

<details markdown="1">
<summary markdown="1">What does Spearman rank correlation measure that Pearson correlation does not?</summary>

Spearman rank correlation measures whether the relationship between two variables is monotone — that is, whether one tends to increase as the other increases, regardless of whether that relationship is linear. Pearson correlation measures the strength of a linear relationship specifically. A dataset where one variable grows as the square of another would show a high Spearman r (because the monotone trend is strong) but possibly a lower Pearson r (because the relationship is not linear). For ranked lists like the educator and Blackbox rankings, Spearman is the natural choice because the concept of "twice as far apart in rank" is not well-defined.

</details>

<details markdown="1">
<summary markdown="1">The following bootstrap loop has a bug. What is wrong and how do you fix it?

```python
boot_medians = []
for _ in range(1000):
    sample = np.random.choice(data, size=len(data))  # no replace=True
    boot_medians.append(np.median(sample))
```
</summary>

The call to `np.random.choice` is missing `replace=True`. Without replacement, every resample is just a permutation of the original data and every median will be identical to the original median. The whole point of bootstrap resampling is to sample with replacement so that different values appear different numbers of times, which simulates the variability you would see across repeated studies. The fix:

```python
boot_medians = []
rng = np.random.default_rng(42)
for _ in range(1000):
    sample = rng.choice(data, size=len(data), replace=True)
    boot_medians.append(np.median(sample))
```

Using `np.random.default_rng` rather than `np.random.choice` is also better practice because the new generator API is reproducible with an explicit seed and avoids global state.

</details>

<details markdown="1">
<summary markdown="1">Why is Kruskal-Wallis preferable to a one-way ANOVA for comparing error counts across three or more categories of programming mistakes?</summary>

One-way ANOVA assumes that observations within each group follow a normal distribution with equal variance across groups. Error counts are non-negative integers that are often heavily right-skewed — a few error types occur very frequently while most occur rarely. That distribution is not normal, and the variance across error categories is unlikely to be equal. Kruskal-Wallis makes neither assumption. It ranks all observations together and tests whether the average rank differs by group, which is a valid procedure regardless of the underlying distribution.

</details>

<details markdown="1">
<summary markdown="1">If the bootstrap 95% CI for median Spearman r across educators is [-0.1, 0.3], what does this tell you about whether educators predict student errors reliably?</summary>

A confidence interval that spans from negative to positive includes zero, which means the data are consistent with no relationship at all between educator rankings and the Blackbox data. The upper bound of 0.3 is a weak positive correlation even in the most optimistic reading. Taken together, this interval tells you that there is no reliable evidence that educators predict student error frequencies better than chance. Any individual educator who happens to have a positive r may simply be lucky; the uncertainty in the estimate is too large to conclude otherwise.

</details>

## Exercises

<div class="exercise" markdown="1">

### Educators vs. Reality vs. Each Other

Test whether educators agree with each other more than they agree with reality. Compute the average Spearman r between all pairs of educators, and separately compute the average Spearman r between each educator and the Blackbox ranking. Report both averages. Write three sentences interpreting the comparison: what the relative magnitudes tell you about where educators' beliefs about novice mistakes come from, what this implies for the design of programming courses that aim to address the errors students most frequently make, and what additional data you would need to determine whether changing course content would actually reduce those errors.

</div>

<div class="exercise" markdown="1">

### Kruskal-Wallis on Error Categories

Run a Kruskal-Wallis test on error counts grouped by error category, using at least three distinct categories (syntax errors, type errors, and logic errors) from the educator rankings dataset. Report the test statistic and p-value. Write two sentences explaining your choice of Kruskal-Wallis over one-way ANOVA for this particular data — be specific about the properties of error count data that make the ANOVA assumptions implausible.

</div>

<div class="exercise" markdown="1">

### Bootstrap CI for the Best Educator

Identify the educator whose ranking has the highest Spearman r with the Blackbox data. Compute a bootstrap 95% confidence interval for that correlation using 1,000 bootstrap samples. Report the interval. Write one sentence interpreting whether even the best-performing educator's rankings are reliably better than chance, given the width and location of the interval.

</div>

<div class="exercise" markdown="1">

### Visualizing Bootstrap Uncertainty

Plot the distribution of the 1,000 bootstrap median Spearman r values as a histogram using Altair. Add two vertical rules marking the 2.5th and 97.5th percentiles, using a distinct color or stroke pattern for each. Write one sentence explaining what the width of the distribution tells you about uncertainty in your estimate of the median Spearman r — specifically, whether you would reach the same conclusion if you had surveyed a different set of educators.

</div>

<div class="exercise" markdown="1">

### Systematic Over-Prediction

Identify the three error types that educators most consistently over-predict relative to the Blackbox data — that is, the three types where educator rankings systematically place the error as more common than the Blackbox frequency data show. Write two sentences suggesting why educators might systematically over-estimate the frequency of those particular errors: consider what gets emphasized in introductory teaching materials, what kinds of errors instructors see and remember, and what kinds of errors students fix quickly and therefore stop making.

</div>
