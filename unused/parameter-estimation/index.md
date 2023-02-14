---
permalink: "/parameter-estimation/"
---

-   Problems:
    -   How to fit a theoretical model to actual data?
    -   How to evaluate how well the model fits?
-   Steps are:
    -   Choose a model
    -   Fit the data
    -   Evaluate goodness of fit

## What model can we use for package data? {#s:parameter-estimation:model}

-   [Zipf's Law][zipfs-law]

## How can we fit data to a model? {#s:parameter-estimation:fit}

-   [Linear regression][linear-regression]
-   But since the model assumes exponential decay, use logarithm of [explanatory variable][explanatory-variable]

## Material from Jake Vanderplas {#s:parameter-estimation:source}

-   <https://jakevdp.github.io/blog/2017/11/09/exploring-line-lengths-in-python-packages/>
-   `pep-8-line-lengths.ipynb`

## How can we evaluate how well our model fits our data? {#s:parameter-estimation:evaluate}

-   FIXME: goodness of fit

## How can this approach be misleading? {#s:parameter-estimation:caveats}

-   FIXME: overfitting

{% include links.md %}
