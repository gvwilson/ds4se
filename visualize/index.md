# Visualization with Altair

## Learning Goals

-   Explain why visualization must precede calculation using Anscombe's quartet
-   Build histograms, scatter plots, and box plots in Altair
-   Choose between linear and log scales for skewed distributions
-   Use jitter, color, and faceting to reveal structure hidden in aggregates

## Why Visualize Before You Calculate?

-   [%g anscombes_quartet "Anscombe's quartet" %] is the classic demonstration that summary statistics lie by omission
    -   Four datasets, each with nearly identical means, variances, and correlations
    -   Plot them and they look completely different: one linear, one curved, one with an outlier, one nearly vertical
    -   The lesson: always look at your data before trusting any single number
-   The Prechelt data from Lesson 1 illustrates the same point
    -   The mean working hours is pulled up by a handful of very slow participants
    -   The box plot reveals the skew that the mean conceals

## Altair's Grammar

-   Altair describes charts in terms of three things: data, marks, and encodings
    -   Data: a Pandas or Polars dataframe (Altair works with Pandas internally, so call `.to_pandas()`)
    -   Mark: the geometric shape used to represent each row (`mark_bar`, `mark_point`, `mark_boxplot`, ...)
    -   Encoding: which column maps to which visual channel (`x`, `y`, `color`, `facet`, ...)
-   A minimal chart looks like this:
    -   `alt.Chart(df).mark_point().encode(x="col_a", y="col_b")`
-   Add `.properties(title="...")` to set a title; chain `.save("file.html")` to write output

## Histograms

-   A [%g histogram "histogram" %] groups numerical values into bins and counts how many observations fall in each bin
    -   Use `mark_bar` with `alt.X("col:Q", bin=True)` for automatic binning
    -   Control bin width with `alt.Bin(maxbins=30)` or `alt.Bin(step=10)`
-   Bin width matters: too few bins hides structure; too many bins adds noise
    -   Always try at least two different bin widths before settling on one
-   The `Q` type annotation tells Altair the column is quantitative; use `N` for nominal (categorical) and `O` for ordinal

## Scatter Plots

-   A [%g scatter_plot "scatter plot" %] maps one column to the x-axis and another to the y-axis, with one point per row
    -   Use `mark_point` with `x` and `y` encodings
    -   When many points overlap, the plot becomes a solid mass that reveals nothing
    -   Add `size=alt.value(20)` and `opacity=alt.value(0.3)` to make overlap visible
-   Color is a third variable for free: `.encode(color="category:N")`
    -   Use color for categorical variables; avoid it for continuous variables unless you have a good reason

## Box Plots

-   `mark_boxplot` draws the five-number summary without any manual aggregation
    -   The box spans the 25th to 75th percentile; the line inside is the median
    -   Whiskers extend to 1.5 times the interquartile range; points beyond that are shown individually
-   Combine a box plot with a strip plot to show the raw data behind the summary
    -   Layer two charts with `chart1 + chart2`

## Log Scales

-   A [%g log_scale "log scale" %] replaces equal additive steps with equal multiplicative steps
    -   On a linear axis, 10, 20, 30 are equally spaced; on a log axis, 1, 10, 100, 1000 are equally spaced
    -   Use it when values span several orders of magnitude, or when the distribution has a long right tail
-   File sizes, response times, bug counts, and release counts are all candidates for log scales
    -   If most values cluster near zero and a few are ten or a hundred times larger, a linear axis compresses everything interesting into a thin sliver
-   Set a log scale with `alt.Y("col:Q", scale=alt.Scale(type="log"))`
    -   Log scales cannot include zero; filter or add 1 before plotting if your data contains zeros

## Jitter

-   [%g jitter "Jitter" %] adds a small random displacement to points that would otherwise overlap exactly
    -   Without jitter, ten points at `x=5` look like one point
    -   With jitter, you can see the density
-   In Altair, add jitter with `transform_calculate`:
    -   `transform_calculate(jitter="random()")` and encode the result as a secondary x or y offset
-   Jitter is random, so set a random seed or document that the plot will look slightly different each run

## Faceting

-   Faceting creates one sub-plot per value of a categorical variable, all with the same axes
    -   Use `facet("language:N")` to split by language; combine with `columns=2` to set layout
    -   Shared axes make comparisons honest; independent axes make patterns within each group clearer
-   Color and faceting serve different purposes
    -   Color: easy to compare a small number of groups within a single plot
    -   Faceting: better when groups overlap badly or when you have more than four or five categories

[%inc charts.py %]

## Check Understanding

<details markdown="1">
<summary markdown="1">What does Anscombe's quartet demonstrate about the relationship between summary statistics and data distributions?</summary>

Anscombe's quartet is four datasets that share nearly identical means, variances, and correlations, yet look completely different when plotted. One is linear, one is curved, one has a single outlier that distorts the regression line, and one is nearly a vertical cluster with one distant point. The quartet demonstrates that a handful of numbers can never fully describe a distribution, and that visualization is not optional — it is the first step of any honest analysis.

</details>

<details markdown="1">
<summary markdown="1">The code below is supposed to display a log Y axis. What is wrong with it, and how do you fix it?

```python
chart = (alt.Chart(df.to_pandas())
         .mark_bar()
         .encode(x="language", y="count()"))
# the user wants a log Y axis
chart = chart.encode(y=alt.Y("count()", scale="log"))
```
</summary>

Two things are wrong. First, `scale="log"` is not a valid argument: Altair expects an `alt.Scale` object, not a bare string. Second, calling `.encode()` on an already-built chart does not modify it in place — it returns a new chart, but only overrides the channels explicitly listed, which can cause unexpected merging behavior. The correct approach is to set the encoding in one place from the start:

```python
chart = (alt.Chart(df.to_pandas())
         .mark_bar()
         .encode(x="language:N",
                 y=alt.Y("count():Q", scale=alt.Scale(type="log"))))
```

</details>

<details markdown="1">
<summary markdown="1">When should you use a log scale instead of a linear scale?</summary>

Use a log scale when the data spans several orders of magnitude or has a heavy right tail — situations where most values are small but a few are vastly larger. File sizes, response times, bug counts, and package release counts are typical candidates. A log scale compresses the long tail and spreads out the dense cluster near zero, making the shape of the distribution visible. If your data contains zero, you cannot use a log scale directly; add 1 first or filter out the zeros and explain why.

</details>

<details markdown="1">
<summary markdown="1">What is the difference between color encoding and faceting in Altair, and when would you use each?</summary>

Color encoding adds a third variable to a single plot by assigning different colors to different categories. Faceting splits the data into separate sub-plots, one per category, all sharing the same axes. Use color when you have a small number of groups (ideally no more than four or five) and the groups do not overlap too much. Use faceting when the groups overlap badly, when you have more categories than colors you can distinguish, or when you want readers to focus on the shape of each group rather than on comparisons between groups. Shared axes in a faceted plot make cross-group comparison honest; independent axes highlight within-group structure.

</details>

## Exercises

<div class="exercise" markdown="1">

### Linear vs. Log Y Axis

Make two histograms of lines-per-file from the Python function-count dataset: one with a linear Y axis and one with a log Y axis, using the same bin width for both. Write two sentences comparing what each version reveals. The linear version likely shows a large spike at very small file sizes; the log version probably makes the shape of the rest of the distribution visible. Then write a Polars filter that selects only files with fewer than five lines and inspect their contents to check whether they are empty or contain only comments or docstrings.

</div>

<div class="exercise" markdown="1">

### Scatter Plot with Size Categories

Make a scatter plot of lines-per-file (X axis) versus functions-per-file (Y axis) for the Python dataset. Add a color encoding for a size category column that you compute in Polars: "small" for files with fewer than 50 lines, "medium" for 50 to 500 lines, and "large" for more than 500 lines. Use `opacity=alt.value(0.4)` to reduce overplotting. Write one sentence describing the pattern you see in the large-file region, and one sentence explaining whether the relationship between lines and functions looks linear across all size categories.

</div>

<div class="exercise" markdown="1">

### Jittered Strip Plot

Reproduce the Prechelt box plot of working hours by language using Altair. Then layer a jittered strip plot on top of it by adding a second `mark_point` layer that uses `transform_calculate` to add a small random horizontal offset to each point. The two layers should share the same data and the same Y axis. Write one sentence about what the individual points reveal that the box plot alone does not show — for example, whether any language has a suspicious cluster of identical values or a single extreme outlier that dominates the box.

</div>

<div class="exercise" markdown="1">

### Faceted Histogram

Load both the Python and JavaScript function-count datasets, add a `language` column to each, and concatenate them into a single dataframe. Create a faceted histogram of lines-per-function using 20-line bins, with one panel per language and a shared Y axis. Write one sentence about what the shared Y axis reveals that you would miss if each panel had an independent Y axis scaled to its own data — specifically, whether the two languages have similar absolute counts in each bin or whether one language simply has far more files.

</div>

<div class="exercise" markdown="1">

### Anscombe's Fifth Example

Find or construct two numerical variables where the Pearson correlation coefficient is between 0.9 and 1.0, but the scatter plot reveals an obvious non-linearity or a single dominant outlier that is driving the correlation. You might use a quadratic relationship sampled at evenly-spaced x values, or a dataset where removing one point drops the correlation below 0.5. Write the Polars code to compute the correlation, produce the scatter plot in Altair, and write two sentences explaining why a researcher who reported only the correlation value would be misleading their readers — even though the number itself is technically correct.

</div>
