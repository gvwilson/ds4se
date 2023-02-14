---
permalink: "/programmer-survey/"
---

-   How are programmers' salaries related to their genders?
-   Redo [this analysis][silge-survey-analysis] by [Julia Silge][silge-julia]

## What's in the data? {#s:programmer-survey:clean-explore}

-   Get the data from [the Stack Overflow survey site][stack-overflow-survey-data]
-   Unzip, and then re-zip the responses so that GitHub will accept the file
    -   Pandas can read a zipped file directly (though it takes longer because it has to uncompress)
-   Sample to create a subset of data that's quick to load for testing during development
    -   Turns out that none of the sample includes non-binary people (fix in the exercises)
-   Follow Silge's analysis
    -   Use explicit enumeration of values when doing conversion
    -   Print messages if asked to (`--verbose`) to check totals

## Interpreting results

The reason I built that first linear regression as `ConvertedComp ~ 0 + DevType + .`
is that I wanted no global intercept but instead an intercept for each developer type,
including the one that would have been assigned as the reference level for dummy coding.
In this particular case, we are (well, at least, I am) not very interested in the developer-role-to-role variations
and whether those are significantly different from each other (different from reference level);
I just want the regular linear regression to be allowed to fit a different intercept for each of those kinds of roles,
while using the same model parameters for the other predictors (like education level, gender, etc).
Notice that when fitting as `ConvertedComp ~ 0 + .` there is still no global intercept (because of the `0 +`)
but now it is the education level that gets fit to a different intercept for each level, because it's the first column.
It's possible that this could be a reasonable choice for certain questions,
but I was more interested in treating developer role as an intercept/random effect
and education level as an explanatory variable to be compared to other explanatory variables like experience and gender.
(You can tell I was setting up in the blog post to move to the fancier modeling approaches.)

Dan is of course right that these different choices change the model matrix,
but this is on purpose because of the modeling question I was asking.
The linear mixed effects modeling (and definitely the Bayesian approach) are better ways to implement this from a stats perspective,
but starting off with fitting an intercept for each is not a bad way to get going.

The reason that the R results don't report "Less than bachelor's" and "Back-end" in a table of coefficients
is that they are the reference level in a factor for modeling purposes (dummy coding).
The other results in those factors are reported relative to them.
For example,
"Bachelor's degree" and "Graduate degree" are reported relative to "Less than bachelor's";
the estimates are how much salary increases relative to the lowest factor level.
Notice that when we specify `0 + DevType + .` that we do see "Back-end" because we're essentially saying to R:
"fit an intercept to each developer type".

Let me know if any of that doesn't make sense!
I haven't used Pandas enough to know how to fit, say,
a model that forces the intercepts to be a certain variable instead of a global variable.

Thanks,
Julia

## Exercises {#s:programmer-survey:ex}

FIXME: exercises

1.  Modify `Makefile` to unzip the compressed survey results file
    and `.gitignore` to ignore the unzipped file.

1.  Modify `bin/create-test-subset.py` to create a subset that always includes
    a representative portion of all three gender categories.

1.  Refactor `bin/analyze-survey.py` to do analyses for sets of countries
    and then see how Western Europe and CANZ (Canada, Australia, and New Zealand)
    compare to the United States.

{% include links.md %}
