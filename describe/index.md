# Descriptive Statistics

## Learning Goals

-   Compute and interpret mean, median, standard deviation, and percentiles
-   Explain when mean and median diverge and what that divergence implies
-   Recognize right-skewed distributions and choose appropriate summary statistics
-   Use PyPI release-count data to reproduce published descriptive statistics

## Mean vs. Median

-   The [%g mean "mean" %] is the sum of all values divided by the count; it is sensitive to extreme values
    -   One package on PyPI (`ccxt`) had nearly 11,000 releases at the time of the study
    -   That single package pulls the mean release count up to about 11, even though most packages have far fewer
-   The median is the middle value in a sorted list; it is not affected by extremes
    -   The median PyPI release count is 4
    -   A mean of 11 and a median of 4 together tell a story: most packages are small, but a handful of extremely prolific packages distort the average
-   When mean and median diverge substantially, report both and explain the gap
    -   Reporting only the mean is technically accurate and practically misleading

## Variance and Standard Deviation

-   [%g variance "Variance" %] is the average of the squared differences from the mean
    -   Squaring the differences makes variance sensitive to outliers: one extreme value inflates it dramatically
    -   Variance has units of (original units)², which makes it hard to interpret directly
-   [%g standard_deviation "Standard deviation" %] is the square root of the variance
    -   It has the same units as the original data, which makes it interpretable
    -   For the PyPI data, the standard deviation is much larger than the mean, which is a sign that the distribution is heavily skewed
-   Neither statistic is a good summary for heavily skewed data; use percentiles instead

## Percentiles

-   The Nth percentile is the value below which N percent of observations fall
    -   The 25th percentile (Q1) and 75th percentile (Q3) bound the middle half of the data
    -   The 10th and 90th percentiles give a view of the tails without being as extreme as the minimum and maximum
-   Percentiles are more informative than min/max for skewed data
    -   The maximum PyPI release count is nearly 11,000; the 90th percentile is much lower
    -   Min and max are the two values most likely to be unusual, so they tell you the least about the typical case
-   The [%g interquartile_range "interquartile range" %] (IQR) is Q3 minus Q1
    -   It measures the spread of the middle half of the data and is not affected by extreme values
    -   The box in a box-and-whisker plot spans the IQR

## Skewness

-   [%g skewness "Skewness" %] measures the asymmetry of a distribution
    -   Positive skew (right skew): the tail extends to the right; most values are small, a few are very large
    -   Negative skew (left skew): the tail extends to the left; most values are large, a few are very small
-   Most software engineering data is positively skewed
    -   File sizes, function lengths, bug counts, release counts, response times: all tend to have many small values and a few enormous ones
    -   This is not a coincidence; it reflects the fact that these quantities cannot go below zero and have no fixed upper bound
-   A right-skewed distribution is one where mean > median
    -   The PyPI release count has mean ≈ 11 and median = 4, confirming positive skew

## When to Use a Log Scale

-   Log scales compress large values and spread small ones, which is exactly what right-skewed data needs
    -   Plot the PyPI release counts on a linear scale and you see a spike near zero with a barely-visible tail
    -   Plot on a log scale and the shape of the distribution becomes clear
-   Any quantity with a long right tail is a candidate for a log scale: file sizes, response times, bug counts, commit counts
-   Log-transforming data before computing the mean is common in practice
    -   Compute the mean of log(x), then exponentiate: this is the geometric mean
    -   For skewed data, the geometric mean is often a better summary than the arithmetic mean

## Replication Target

-   Load the PyPI release-count dataset and reproduce these published values: mean ≈ 11, median = 4, max ≈ 10,797
-   If your numbers differ, check whether the dataset has been filtered or whether packages with zero releases were excluded

[%inc pypi_stats.py %]

## Check Understanding

<details markdown="1">
<summary markdown="1">Why is the mean number of PyPI releases so much higher than the median?</summary>

The distribution of release counts is heavily right-skewed: most packages have a small number of releases, but a handful of packages have thousands. The mean is pulled upward by those extreme values, while the median reports the experience of the typical package. When one data point can be nearly 11,000 times larger than the median, the mean stops being a useful description of the center of the distribution.

</details>

<details markdown="1">
<summary markdown="1">The code below tries to report the spread of release counts in the original units. What is wrong with it, and how do you fix it?

```python
df = pl.read_csv("data/pypi_releases.csv")
spread = df["releases"].variance()
print(f"Spread in releases: {spread:.1f} releases")
```
</summary>

Variance is measured in squared units, not in the original units. Writing "releases" after the variance value is wrong: the number is in "releases²", which has no intuitive meaning. To report spread in the original units, use standard deviation instead:

```python
spread = df["releases"].std()
print(f"Spread in releases: {spread:.1f} releases")
```

If the goal is to emphasize spread without being misled by outliers, the interquartile range is an even better choice for this skewed dataset.

</details>

<details markdown="1">
<summary markdown="1">When would a researcher reporting only the mean of a right-skewed distribution mislead readers?</summary>

Any time the distribution is heavily skewed, the mean describes a value that most observations are far below. If you report that the average PyPI package has 11 releases, a reader naturally imagines a typical package — but the typical package has only 4. The mean is dominated by the small number of packages with thousands of releases. A reader who acts on the mean (say, by setting an update-frequency benchmark) will set a standard that the vast majority of active packages cannot meet.

</details>

<details markdown="1">
<summary markdown="1">What does skewness measure, and why is most software engineering data positively skewed?</summary>

Skewness measures the asymmetry of a distribution: positive skew means the tail extends to the right, so a few very large values are far above the bulk of the data. SE data is positively skewed because most SE quantities — file sizes, function lengths, bug counts, release counts — are bounded below by zero and have no natural upper limit. The result is a pattern where most items are small, a few are medium-sized, and a small number are extremely large. This pattern appears in so many SE contexts that assuming a roughly normal distribution is almost always wrong.

</details>

## Exercises

<div class="exercise" markdown="1">

### Zero-Release Packages

The PyPI dataset contains packages with zero releases. Decide whether to keep or drop them, then compute the mean and median both ways and report all four numbers. Write one sentence explaining which treatment is more appropriate for answering the question "how often do active packages get updated?" and one sentence explaining why the choice of inclusion criteria belongs in the methods section of any paper that uses this data.

</div>

<div class="exercise" markdown="1">

### Skewness Before and After Log Transform

Compute the skewness of the raw release-count distribution using `scipy.stats.skew`. Then add 1 to each release count (to handle zeros), take the natural logarithm, and compute the skewness of the transformed values. Report both skewness values. Write one sentence interpreting what the reduction in skewness tells you about which scale — raw or log — is more appropriate for summarizing this data, and one sentence explaining why you add 1 before taking the log.

</div>

<div class="exercise" markdown="1">

### Effect of Trimming the Top 1%

Identify the threshold for the top 1% of packages by release count and remove all packages above that threshold. Recompute the mean and median on the trimmed dataset. Report the original values, the trimmed values, and the percentage change for each statistic. Write two sentences explaining which statistic changed more and what that implies for how sensitive the mean is to extreme values compared to the median.

</div>

<div class="exercise" markdown="1">

### Limits of PyPI as a Sample

The lesson uses PyPI data to describe "software projects," but PyPI is not representative of all software. Identify one specific way in which PyPI packages are not representative — for example, in terms of project age, project size, programming language, or type of software. Write one sentence stating the limitation clearly, and one sentence proposing an alternative dataset or sampling strategy that would reduce it.

</div>

<div class="exercise" markdown="1">

### Visualizing Mean vs. Median

Plot the PyPI release-count distribution on a log scale using Altair. Add two vertical rules: one at the mean and one at the median. Use different colors or stroke patterns to distinguish them, and add a legend. Write two sentences explaining what a reader should take away from the gap between the two lines — specifically, what it implies about which statistic to report when summarizing this distribution for a general audience.

</div>
