## How is the popularity of programming languages changing?

-   How is the popularity of [Stack Overflow][stack-overflow] query tags changing over time?
    -   Which may not be the same thing
-   Based on [this analysis](stack-overflow.Rmd).
-   Use [Stack Exchange API][stack-exchange-api] to get tags of top queries by month from [Stack Overflow][stack-overflow]
-   All seem to follow the same [sigmoidal curve][sigmoidal-curve] except `Python`
    -   Compare to `PHP`
-   FIXME: do analysis

> Spare Me the Math
>
> The [Wikipedia page on the Kolmogorov-Smirnov test][kolmogorov-smirnov] says,
> "…a very simple expedient of replacing $x$ by $x + {\frac {1}{6{\sqrt {n}}}} + {\frac {x-1}{4n}}$
> in the argument of the Jacobi theta function reduces these errors…"
> While we feel it is important to understand some of the mathematics behind statistical tests,
> we are willing to take matters such as this on trust.
{: class="aside"}
