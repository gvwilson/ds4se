# Tidy Data and Polars Basics

## Learning Goals

-   Explain the three rules of tidy data
-   Load, inspect, filter, and select data with Polars
-   Handle missing values appropriately
-   Write cleaned data back to CSV

## Lesson

-   Most data you find in the wild is not structured for analysis; cleaning it takes time
    -   [%g tidy_data "Tidy data" %] has a simple definition from Wickham [%b Wickham2014 %]:
        each column is one variable, each row is one observation, and one table holds one
        set of related observations
    -   Violating any of these rules makes even simple analyses harder than they need to be
    -   Examples of untidy data: a column called `jan_sales` alongside `feb_sales`
        (the month is a variable, not a column name); a row that mixes individual and
        aggregate data; two different kinds of observation packed into the same table
-   Load a CSV with `pl.read_csv`
    -   Polars infers column types from the first batch of rows; check that inference is correct
    -   Common surprises: dates read as strings, integers read as floats because one cell is empty,
        numeric columns that contain notes like "n/a" read as strings
-   Inspect a dataframe before doing anything else
    -   `df.shape` returns `(rows, columns)` as a tuple
    -   `df.columns` lists column names; `df.dtypes` lists the inferred type of each column
    -   `df.head()` shows the first five rows; `df.describe()` gives count, mean, std, min, and
        percentiles for every numeric column
-   Select columns with `select` and filter rows with `filter`
    -   `df.select(["col_a", "col_b"])` keeps only those two columns
    -   `df.filter(pl.col("value") > 0)` keeps only rows where the condition is true
    -   Polars expressions are lazy by default when using the lazy API; `select` and `filter`
        on a plain dataframe execute immediately
-   [%g null_value "Null values" %] in Polars represent missing or unknown data
    -   A null is not the same as zero; treating it as zero changes the meaning of the data
    -   A null is not the same as an empty string; an empty string is present but blank
    -   `df.drop_nulls("column_name")` removes every row where that column is null
    -   `df.fill_null(value)` replaces every null with the given value; use this only when
        you have a defensible reason for the replacement
-   Write a cleaned dataframe back to CSV with `df.write_csv("output.csv")`
    -   Always write to a new file name rather than overwriting the original data
    -   If you overwrite the original, you cannot tell whether a problem appeared before or
        after the cleaning step

-   Data availability has its own biases [%b Acciai2023 %]
    -   Acciai et al. sent data requests to corresponding authors of published papers and
        found that requesters with Chinese-sounding names received significantly fewer
        responses than those with Anglo-Saxon-sounding names
    -   This means any study that relies on author cooperation to obtain data may have
        systematically incomplete coverage of researchers from certain regions
    -   You cannot fix this bias after the fact; you have to design around it

[%inc line_lengths.py %]

## Check Understanding

<details markdown="1">
<summary markdown="1">What are the three rules of tidy data? Give a concrete example of real data that violates each rule.</summary>

The three rules are: (1) each column is one variable, (2) each row is one observation,
(3) one table per set of related observations. A spreadsheet that stores monthly sales
figures in columns named `jan`, `feb`, `mar` violates rule 1 because the month is a
variable that belongs in its own column. A CSV where some rows hold individual transaction
data and other rows hold subtotals for a category violates rule 2 because a subtotal row
is not an observation of the same kind as a transaction row. A single table that combines
customer information (name, address) with order information (item, quantity, price)
violates rule 3 because those are two different sets of observations that should be
normalized into separate tables joined by a customer identifier.

</details>

<details markdown="1">
<summary markdown="1">The following code is supposed to double all positive values in a column, but it will raise an error in Polars. What is wrong and how do you fix it?

```python
df = pl.read_csv("data.csv")
result = df.filter(pl.col("value") > 0)
result["value"] = result["value"] * 2  # this line
```
</summary>

Polars dataframes are immutable: you cannot modify a column in place using index
assignment the way you can with a Pandas dataframe. The line `result["value"] = ...`
will raise a `TypeError`. The fix is to use `with_columns` to create a new dataframe
with the modified column:

```python
df = pl.read_csv("data.csv")
result = (df
          .filter(pl.col("value") > 0)
          .with_columns((pl.col("value") * 2).alias("value")))
```

</details>

<details markdown="1">
<summary markdown="1">Why is it wrong to fill null line lengths with 0 when computing PEP 8 compliance?</summary>

A null line length means the length of that line is unknown, not that the line has zero
characters. Replacing null with 0 would classify every unknown-length line as compliant
with PEP 8 (which requires lines to be 79 characters or shorter), because 0 is less than
79. This artificially inflates the compliance rate. The correct approach is to drop rows
with null line lengths so they do not contribute to either the numerator or denominator
of the compliance fraction, and then note in any report that some lines had missing
length data.

</details>

<details markdown="1">
<summary markdown="1">What does the Acciai et al. finding imply for a study that relies on requesting data from paper authors?</summary>

It implies that the resulting dataset will not be a random sample of all relevant
research. Researchers with names associated with certain ethnic backgrounds are less
likely to respond to data requests, so the study will systematically underrepresent work
from those groups. Any analysis built on that data will generalize only to the subset of
research that was willing to share, which may differ from the full population in ways
that matter for the conclusions. This is a form of selection bias that the study design
itself introduced, not something in the underlying research being studied.

</details>

## Exercises

<div class="exercise" markdown="1">
### Compliance by Directory

The line-length dataset includes a column indicating which part of the Python installation
each file came from (for example, `site-packages` versus `bin`). Filter the cleaned data
to each directory category separately and compute the fraction of lines exceeding 79
characters for each one. Present the results as a Polars dataframe with one row per
directory. Write one sentence interpreting any difference you find: does it make sense
that one category would have different style compliance than another?
</div>

<div class="exercise" markdown="1">
### Two Ways to Handle Nulls

Compute the fraction of lines exceeding 79 characters in two ways: first by dropping all
rows where `line_length` is null before computing the fraction, and second by filling
null line lengths with 0 before computing the fraction. Report both fractions. Explain
in two or three sentences which approach is more defensible for a study about PEP 8
compliance, and under what circumstances (if any) filling with 0 would be the correct
choice.
</div>

<div class="exercise" markdown="1">
### File-Level Versus Line-Level Compliance

The dataset allows you to compute compliance in two ways. The line-level rate is the
fraction of individual lines that are 79 characters or shorter. The file-level rate is
the fraction of files where every line is 79 characters or shorter. Compute both rates
using the cleaned data and report which is larger. Write two or three sentences explaining
which rate is more useful for a team that wants to enforce a style guide, and which is
more useful for a researcher comparing style conventions across programming communities.
</div>

<div class="exercise" markdown="1">
### Alternative Data Sources

You are replicating a study that originally required data from paper authors, but you
suspect that bias in data-sharing responses (as documented by Acciai et al. [%b Acciai2023 %])
may have skewed the original dataset. Propose two alternative data sources you could use
instead of contacting authors directly. For each source, describe what data it provides,
what bias it might introduce, and how you would check whether the alternative source gives
similar results to the original data where overlap exists.
</div>

<div class="exercise" markdown="1">
### Making and Repairing Untidy Data

Take the cleaned line-length data and deliberately restructure it in two different ways
that violate the tidy data rules: once by creating a version that violates rule 1 (one
variable per column) and once by creating a version that violates rule 2 (one observation
per row). Write the untidy versions to CSV files. Then write Polars code that reads each
untidy file and transforms it back into a tidy dataframe equivalent to the original.
Include a comment in each transformation explaining which tidy rule was violated and what
operation restores it.
</div>
