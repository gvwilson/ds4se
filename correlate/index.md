# Correlation and Prediction

## Learning Goals

-   Compute and interpret Pearson and Spearman rank correlations
-   Fit and interpret a simple linear regression model
-   Evaluate model fit using R² and residual plots
-   Explain when Spearman correlation is more appropriate than Pearson

---

-   The [%g pearson_correlation "Pearson correlation coefficient" %] r measures the strength of a linear relationship
    between two numerical variables
    -   r always falls between -1 (perfect negative) and 1 (perfect positive); r = 0 means no linear relationship
    -   For Python files, lines vs. functions gives r ≈ 0.806; for JavaScript, r ≈ 0.728
    -   A high r does not imply causation — something else could be driving both variables
    -   r can be misleading when the relationship is non-linear or when a handful of outliers dominate

-   Always plot before computing
    -   Draw a scatter plot of the two variables; add a trend line
    -   Anscombe's quartet showed that four very different datasets can produce the same r
    -   If your scatter plot shows a curve or a cluster of extreme points pulling the line, r is the wrong summary

-   [%g spearman_correlation "Spearman rank correlation" %] replaces raw values with their ranks before computing r
    -   Use Spearman when data is ordinal, heavily skewed, or contains outliers that you cannot remove
    -   Spearman measures monotonic relationships; Pearson measures only linear ones
    -   If a scatter plot shows a consistent upward trend but not a straight line, Spearman is more reliable

-   Simple [%g linear_regression "linear regression" %] fits the equation y = a + bx to minimize the sum of squared errors
    -   The slope b tells you how much y changes for each unit increase in x
    -   The intercept a is the predicted value of y when x = 0 — interpret carefully, since x = 0 may not be realistic
    -   `scipy.stats.linregress` returns slope, intercept, r, p-value, and standard error of the slope

-   The [%g r_squared "coefficient of determination (R²)" %] is the fraction of variance in y explained by x
    -   R² = r² for simple linear regression with one predictor
    -   R² = 0.65 means the model accounts for 65% of the variation; 35% is unexplained
    -   A high R² does not mean the model is well-specified; it only measures linear fit

-   [%g residual "Residuals" %] are the differences between observed values and model predictions
    -   Plot residuals on the y-axis against predicted values on the x-axis
    -   If the plot shows a random scatter with no pattern, the linear model is plausible
    -   A fan shape (wider spread for larger predictions) indicates that prediction error grows with the outcome
    -   A curve indicates the relationship is non-linear and a straight line is the wrong model

-   The code below loads Python and JavaScript function-count data, computes Pearson r,
    fits a linear model to the Python data, and reports residual statistics

[%inc correlation.py %]

-   The regression output shows the slope (roughly how many functions per additional line),
    the intercept, R², and the spread of residuals
    -   A residual standard deviation larger than the mean of y should make you cautious about predictions
    -   The p-value on the slope tests whether the slope is distinguishable from zero; here it is not in doubt

## Check Understanding

<details markdown="1">
<summary markdown="1">If Pearson r = 0.8 between lines-per-file and functions-per-file, can you conclude that longer files cause more functions to be defined?</summary>

No. Correlation does not imply causation. Both variables could be driven by a third factor,
such as the age of the codebase or the programming style of a particular team. Longer files
might accumulate more functions simply because the same developer who writes long files also
writes many functions; the file length itself might not cause anything. To make a causal
claim you would need to control for confounds or run an experiment.

</details>

<details markdown="1">
<summary markdown="1">The following code computes R² incorrectly. What is the bug and how do you fix it?

```python
slope, intercept, r, p, se = stats.linregress(x, y)
print(f"R² = {r:.3f}")
```
</summary>

`stats.linregress` returns the Pearson correlation coefficient r, not R². To get R² you
must square it:

```python
slope, intercept, r, p, se = stats.linregress(x, y)
print(f"R² = {r**2:.3f}")
```

Printing r directly gives a value between -1 and 1 that looks plausible but is wrong. For
r = 0.806, the code prints 0.806 instead of the correct R² ≈ 0.650.

</details>

<details markdown="1">
<summary markdown="1">A residual plot shows a fan shape: residuals are small for files with few predicted functions and large for files with many predicted functions. What does this indicate about the model?</summary>

The fan shape indicates heteroscedasticity: the variance of the prediction error is not
constant but grows with the predicted value. A plain linear regression assumes constant
variance, so its confidence intervals and standard errors for large files will be too
narrow. One common remedy is to log-transform the outcome variable, which often stabilizes
variance when the data spans several orders of magnitude.

</details>

<details markdown="1">
<summary markdown="1">You are comparing lines-per-file to functions-per-file in a dataset where 90% of files have fewer than 100 lines but a handful have more than 10,000 lines. When would Spearman rank correlation give a more reliable answer than Pearson r?</summary>

Pearson r is sensitive to outliers because it is calculated from the raw values. A handful
of extremely long files will pull the regression line toward them and inflate r, giving the
impression of a stronger or weaker linear relationship than exists for the majority of
files. Spearman r replaces raw values with ranks, so those giant files simply become "the
largest" rather than values 100 times bigger than everything else. Spearman is more
reliable here because it describes the relationship across the full distribution rather
than being dominated by the extreme tail.

</details>

## Exercises

<div class="exercise" markdown="1">
### Spearman vs. Pearson

Compute the Spearman rank correlation between lines-per-file and functions-per-file for
both the Python and JavaScript datasets using `scipy.stats.spearmanr`. Compare each
Spearman value to the corresponding Pearson r. For which language does the gap between
the two measures suggest the relationship is driven by outliers? Describe the
characteristics of a file for which Spearman would be substantially more reliable than
Pearson, and explain why in terms of what each measure actually computes.
</div>

<div class="exercise" markdown="1">
### Regression interpretation

Fit a linear regression of functions-per-file on lines-per-file for the Python dataset
using `scipy.stats.linregress`. Report the slope, intercept, and R². Use the model to
predict the number of functions in a 500-line file. Then explain in two sentences whether
you trust that prediction, considering both the R² value and the range of file sizes in
the training data.
</div>

<div class="exercise" markdown="1">
### In-sample vs. out-of-sample R²

Split the Python dataset in half randomly (use a fixed random seed so your results are
reproducible). Fit the linear regression on the first half and compute R² for both halves:
once on the data you trained on (in-sample) and once on the data you held out
(out-of-sample). Report both values. Explain in two sentences what the difference between
them reveals about whether the model is overfitting to the training data.
</div>

<div class="exercise" markdown="1">
### Large-file sensitivity

Compute Pearson r between lines-per-file and functions-per-file for the Python dataset.
Then remove all files with more than 1,000 lines and compute it again on the remaining
data. Report both values. Write two sentences explaining whether the correlation is driven
by large files and what this implies about using a single r to summarize the relationship
across the full dataset.
</div>

<div class="exercise" markdown="1">
### Heteroscedasticity and transformation

After fitting the linear regression on the Python data, plot the residuals against the
predicted values using Altair. Describe in one sentence whether the plot shows a fan
shape. If it does, re-fit the model after applying a log transformation to both variables
(use `pl.col("lines").log()` and `pl.col("functions").log()`) and compare the residual
plots before and after. Explain in one sentence why log-transforming both variables can
reduce heteroscedasticity in file-size data.
</div>
