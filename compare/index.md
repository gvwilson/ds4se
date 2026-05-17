# Comparing Two Groups

## Learning Goals

-   Choose between Student's t-test and Mann-Whitney U based on distribution shape
-   Check normality using QQ plots and the Shapiro-Wilk test
-   Interpret and report both test statistics appropriately
-   Recognize when a QQ plot reveals departure from normality

---

-   The previous lesson introduced hypothesis testing; this one asks which test to use
    -   The answer depends on the shape of your data, not on what answer you want to get

-   [%g t_test "Student's t-test" %] compares the means of two groups and assumes each group is approximately normally distributed
    -   Use `scipy.stats.ttest_ind` for independent groups
    -   When p rounds to 0.0, report it in scientific notation (e.g., p = 6.9 × 10⁻³¹); never write "p = 0"
    -   The t-statistic measures how many standard errors separate the two means

-   [%g mann_whitney_u "Mann-Whitney U" %] (also called the Wilcoxon rank-sum test) compares two groups without assuming normality
    -   It tests whether values from one group tend to be larger than values from the other
    -   Use `scipy.stats.mannwhitneyu` with `alternative="two-sided"` unless you have a strong directional prediction
    -   SE data is rarely normally distributed, so Mann-Whitney is usually the safer default

-   How to choose between the two: look at your data first
    -   If the distribution is roughly bell-shaped in each group, either test works
    -   If the distribution is skewed, has heavy tails, or is bounded (like hours worked or bug counts), use Mann-Whitney
    -   Never choose the test after looking at the p-values from both

-   Checking [%g normality "normality" %] with a [%g qq_plot "QQ plot" %]
    -   A QQ plot plots each quantile of your data against the corresponding quantile of a normal distribution
    -   Points that fall on a straight diagonal line indicate the data is approximately normal
    -   Points that curve away from the diagonal in the tails indicate heavier or lighter tails than normal
    -   An S-shaped curve indicates skewness

-   The Shapiro-Wilk test is a formal normality test, but use it with caution
    -   For small samples (N < 50), it has low power and may miss non-normality
    -   For large samples (N > 5,000), it almost always rejects normality because it detects tiny departures
    -   At large N, a "failed" Shapiro-Wilk test does not mean you must use Mann-Whitney; check the QQ plot too

-   Fucci et al. ran a quasi-experiment with 45 undergraduate students [%b Fucci2018 %]
    -   23 students stayed awake all night before a programming task; 22 slept normally
    -   The sleep-deprived group produced lower-quality implementations
    -   This design controls for exactly one variable (sleep), which makes causal interpretation much more defensible
    -   Small N makes the choice of test consequential: with 22 or 23 per group, normality is hard to verify

-   The code below loads programmer-hours data, splits it by day type, and runs both tests

[%inc weekday_weekend.py %]

-   Weekday mean ≈ 6.8 hours, weekend mean ≈ 3.2 hours; t ≈ 12.8, p ≈ 6.9 × 10⁻³¹
    -   The two tests should give similar conclusions when the sample is large and the difference is real
    -   When they disagree, that disagreement is itself informative: it suggests the normality assumption matters

## Check Understanding

<details markdown="1">
<summary markdown="1">When should you use Mann-Whitney U instead of Student's t-test?</summary>

Use Mann-Whitney U when the data in one or both groups is not approximately normally
distributed. In practice, this means skewed distributions, heavy tails, ordinal data,
or any bounded measurement like hours worked or bug counts. SE data rarely follows a
normal distribution, so Mann-Whitney is a reasonable default. You should also use it
when sample sizes are small and you cannot verify normality, since the t-test is not
robust to non-normality with small N.

</details>

<details markdown="1">
<summary markdown="1">The following code is supposed to filter out weekend days, but it contains a bug. What is wrong and how do you fix it?

```python
weekday = df.filter(pl.col("day") != "Sat" and pl.col("day") != "Sun")
```
</summary>

The `and` keyword in Python evaluates two boolean objects with Python's truthiness rules,
not element-wise on Polars Series. With Polars, boolean conditions on columns must be
combined with `&` (the bitwise and operator), not `and`. Using `and` here will raise an
error or produce unexpected behavior. The fix is:

```python
weekday = df.filter((pl.col("day") != "Sat") & (pl.col("day") != "Sun"))
```

Each condition must also be wrapped in parentheses because `&` has lower precedence
than `!=`.

</details>

<details markdown="1">
<summary markdown="1">A Shapiro-Wilk test on 10,000 observations gives p = 0.001. Does this mean you must use Mann-Whitney? Explain.</summary>

Not necessarily. With 10,000 observations, the Shapiro-Wilk test is extremely sensitive
and will reject normality for departures so small that they have no practical effect on
the validity of a t-test. The t-test is robust to mild non-normality when sample sizes
are large, because the central limit theorem ensures that sample means are approximately
normally distributed regardless of the underlying distribution. The right response is to
examine a QQ plot: if the points fall close to the diagonal with only minor deviations
in the tails, the t-test is likely fine. If the QQ plot shows severe skewness or heavy
tails, switch to Mann-Whitney.

</details>

<details markdown="1">
<summary markdown="1">What does a QQ plot with points curving away from the diagonal line in the tails indicate?</summary>

It indicates that the tails of the distribution are heavier than a normal distribution
would produce. The extreme high and low values occur more frequently than normality
predicts. This is common in SE data: a few files have thousands of lines while most
have dozens. A t-test on such data puts substantial weight on those extreme values, which
can distort the result. Mann-Whitney is more appropriate because it works on ranks
rather than raw values, so it is not influenced by how extreme the extremes are.

</details>

## Exercises

<div class="exercise" markdown="1">
### Normality Check for Hours Data

Run the code in `weekday_weekend.py` to reproduce the t-statistic (t ≈ 12.8, p ≈ 6.9 × 10⁻³¹).
Then run the Shapiro-Wilk test on each group separately using `scipy.stats.shapiro`.
Report the W statistic and p-value for each group. Given those results, was the t-test
appropriate? Does switching to Mann-Whitney U change the conclusion, and if so, in which
direction?
</div>

<div class="exercise" markdown="1">
### Choosing a Test Without Peeking

Suppose you are analyzing the Fucci et al. sleep deprivation data [%b Fucci2018 %], which
has two groups of roughly 22 students each. Describe in plain language the exact sequence
of steps you would take to decide whether to use a t-test or Mann-Whitney U test, without
looking at p-values from either test first. Then write the Python code for that decision
process: load the data, plot a QQ plot for each group, run Shapiro-Wilk, and print a
recommendation.
</div>

<div class="exercise" markdown="1">
### Common-Language Effect Size

The common-language effect size (CLES) is the probability that a randomly chosen weekday
observation is larger than a randomly chosen weekend observation. Compute it as the
Mann-Whitney U statistic divided by the product of the two group sizes (n1 × n2). Write
one sentence interpreting the result in plain language that a manager who has never taken
a statistics course would understand.
</div>

<div class="exercise" markdown="1">
### QQ Plots for Both Groups

Generate QQ plots for the weekday and weekend groups using `scipy.stats.probplot` and
display them side by side. For each plot, describe in one sentence what the shape of the
points tells you about the distribution. Based on those descriptions, write a one-sentence
recommendation about which test is more appropriate for this data.
</div>

<div class="exercise" markdown="1">
### Four-Group Comparison

Split the programmer-hours data into four groups: Monday through Wednesday, Thursday
and Friday, Saturday, and Sunday. Run the Kruskal-Wallis test using `scipy.stats.kruskal`
and report the H statistic and p-value. Write one sentence explaining why you should use
Kruskal-Wallis rather than running three separate Mann-Whitney U tests between the groups,
and what mistake the separate-tests approach would make.
</div>
