# Lab: Python Coding Style at Scale

## Learning Goals

-   Apply Polars, Altair, and descriptive statistics to a single published study end-to-end
-   Reproduce three specific claims from [%b Bafatakis2019 %]
-   Document analysis decisions that affect the reported result
-   Distinguish a direct replication from an analogous analysis

## The Study

-   [%b Bafatakis2019 %] examined Python code snippets posted on Stack Overflow
    -   They measured the fraction of code that exceeds the 79-character line-length limit set by [PEP 8][pep8]
    -   They found that a large fraction of snippets are non-compliant, and that compliance varies by snippet purpose
    -   The paper is a mining study: no developers were interviewed, no experiments were run
-   Our version is an analogous analysis, not a direct replication
    -   We use line-length data collected from a local Python installation rather than from Stack Overflow
    -   The data format is the same, but the source population is different
    -   Being explicit about this distinction is not a technicality; it determines what conclusions you can draw

## Lab Workflow

-   Step 1: load the data and reproduce the overall non-compliance fraction
    -   Handle null values before computing: decide whether to drop or fill, then document the choice
    -   Compute `total lines` and `lines over 79 characters`; report the fraction
-   Step 2: reproduce the finding that compliance varies by file purpose
    -   Split the data into library code (files under `site-packages`) and scripts (everything else)
    -   Compute non-compliance for each group; check whether the gap matches the paper's direction
-   Step 3: plot the distribution of line lengths as a histogram with a vertical line at 79
    -   The visual should make the PEP 8 limit visible as a reference point
    -   Choose a bin width that shows the shape of the distribution without too much noise

## Analysis Decisions That Change the Number

-   Null handling: dropping rows with null line lengths removes data; filling with 0 adds fake short lines
    -   Neither choice is obviously right; both choices must be documented
    -   The overall fraction will differ depending on which you choose
-   Unit of analysis: line-level compliance (what fraction of all lines are ≤ 79?) vs. file-level compliance (what fraction of files have all lines ≤ 79?)
    -   Line-level and file-level rates can differ substantially if non-compliant files tend to have many non-compliant lines
    -   [%b Bafatakis2019 %] reports line-level compliance; file-level compliance is a different question
-   Subset definition: what counts as "library" code?
    -   Using `site-packages` in the filepath is a reasonable proxy, but it will misclassify some files
    -   The reported gap between library and script compliance depends on how you draw this boundary

## Wrap-Up: Every Number Is a Product of Choices

-   A replication that produces exactly the same number as the original paper is reassuring but not guaranteed
    -   Different Python installations have different files; different cutoff definitions give different counts
    -   If your number differs from the paper's, that is not necessarily a failure — it is information
-   Document every decision: null handling, subset definition, unit of analysis
    -   A reader who cannot reconstruct your choices cannot evaluate your result
    -   This is the same standard you would apply to a paper you are reviewing

[%inc replicate.py %]

## Check Understanding

<details markdown="1">
<summary markdown="1">What three claims from Bafatakis et al. are you trying to reproduce in this lab?</summary>

The three claims are: (1) a substantial fraction of Python lines exceed the 79-character PEP 8 limit; (2) compliance varies by file purpose, with library code behaving differently from script code; and (3) the distribution of line lengths has a visible shape that a histogram can reveal. The first two are quantitative claims with specific numbers in the paper; the third is a qualitative claim about visual structure. Reproducing all three requires making and documenting choices about null handling, subset definition, and unit of analysis.

</details>

<details markdown="1">
<summary markdown="1">The code below tries to compute the non-compliance fraction for library files. What is wrong with it, and how do you fix it?

```python
lib = df.filter(pl.col("filepath").contains("site-packages"))
non_compliant = lib.filter(pl.col("line_length") > 79).sum()
print(f"Non-compliant lines: {non_compliant}")
```
</summary>

Two things are wrong. First, Polars string methods live under `.str`, so the correct call is `pl.col("filepath").str.contains("site-packages")` — without the `.str` accessor, Polars will raise an error. Second, calling `.sum()` on a filtered dataframe sums every column, not just the count column. The result will be a dataframe, not a scalar. To get the total number of non-compliant lines, select the count column first:

```python
lib = df.filter(pl.col("filepath").str.contains("site-packages"))
non_compliant = lib.filter(pl.col("line_length") > 79)["count"].sum()
print(f"Non-compliant lines: {non_compliant}")
```

</details>

<details markdown="1">
<summary markdown="1">How does the unit of analysis (lines vs. files) affect the reported compliance rate?</summary>

Line-level compliance asks what fraction of all lines are 79 characters or fewer; file-level compliance asks what fraction of files have every line within the limit. The two rates can differ significantly. A file with 1,000 lines where 50 exceed 79 characters contributes 50 non-compliant lines to the line-level rate but counts as one fully non-compliant file. If long files tend to violate the limit more often than short files — which is plausible — the line-level rate will be higher than the file-level rate. Choosing one over the other without explanation is an undisclosed analysis decision.

</details>

<details markdown="1">
<summary markdown="1">Why is this an analogous analysis rather than a direct replication of Bafatakis et al.?</summary>

A direct replication would use the same data — Python snippets from Stack Overflow — processed by the same method. This lab uses line-length data from a local Python installation, which is a different population: installed libraries and local scripts rather than code written to answer specific questions in a public forum. The two populations may have very different compliance rates for reasons that have nothing to do with the PEP 8 limit. Calling this a direct replication would imply that the populations are interchangeable, which they are not.

</details>

## Exercises

<div class="exercise" markdown="1">

### Null Handling Decision

Load the line-length dataset. Write two versions of the analysis: one that drops rows where `line_length` is null, and one that fills null line lengths with 0. Compute the overall non-compliance fraction for each version and report both numbers. Write one sentence stating your exact decision about null handling and why it is more defensible for this particular question, and one sentence explaining what a reader would need to know to reproduce your result from the same raw data.

</div>

<div class="exercise" markdown="1">

### File-Level vs. Line-Level Compliance

Compute two compliance rates from the same dataset: line-level compliance (the fraction of all lines that are 79 characters or fewer) and file-level compliance (the fraction of files where every line is within the limit). Report both rates and the difference between them. Write one sentence explaining which rate [%b Bafatakis2019 %] reports, and one sentence explaining which rate a developer who wants to know "how much of my codebase would pass a PEP 8 check?" should care about.

</div>

<div class="exercise" markdown="1">

### Line Length Histogram

Plot the distribution of line lengths as a histogram with 10-character bins using Altair. Add a vertical rule at `x = 79` in a contrasting color to mark the PEP 8 limit. Write two sentences describing what the distribution tells you about how developers actually write Python: for example, whether there is a visible spike just below 79, whether the distribution cuts off sharply at the limit, or whether long lines are rare or common.

</div>

<div class="exercise" markdown="1">

### Non-Compliance by Subset

Compute the non-compliance fraction for three non-overlapping subsets of the data: files with "test" anywhere in the filepath, files under `site-packages`, and all remaining files. Present the three results as a Polars dataframe with one row per subset and columns for the subset name, total line count, non-compliant line count, and non-compliance fraction. Write one sentence identifying which subset has the highest non-compliance rate and proposing one reason why that subset might behave differently from the others.

</div>

<div class="exercise" markdown="1">

### Sensitivity to Analysis Choices

Identify three analysis decisions you made while working through this lab: for example, how you handled null values, how you defined "library" files, and whether you used line-level or file-level compliance. For each decision, compute the non-compliance fraction using the opposite choice — the one you did not make. Report the six resulting numbers (three pairs). Write one sentence summarizing which decision had the largest effect on the reported fraction, and one sentence explaining what this implies for how much you should trust a single published number without seeing the analysis code.

</div>
