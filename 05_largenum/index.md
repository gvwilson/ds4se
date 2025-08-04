# The Law of Large Numbers

-   Problem: how can we do hypothesis testing
    -   More quickly (five hours of simulation to answer one question is a lot)
    -   And more confidently (is 5000 simulations enough? Would 100 work? Do we need a million?)
-   Solution: use statistics
    -   Make some very general assumptions about our data
    -   Calculate an answer based on rules that hold for large datasets

## What is the law of large numbers?

-   Function describing probabilities of discrete events is called the <span g="pmf">probability mass function</span>
-   When describing continuous events, use:
    -   <span g="cdf">Cumulative distribution function</span> \\(F(x) = P(X \leq x)\\)
    -   <span g="pdf">Probability density function</span> \\(f(x) = dF/dx\\)
-   So \\(P(a \lt X \lt B) = \int_{a}^{b} f(x) dx\\)
-   Require \\(\int_{-\infty}^{\infty} f(x) dx = 1\\)
    -   I.e., *something* has to happen
-   And notice \\(P(x) = P(x \leq X \leq x) = \int_{x}^{x} f(x) dx = 0\\)
    -   I.e., probability of any specific exact value is 0
    -   So always talk about ranges
-   <span g="mean">Mean</span> is \\(\mu = \int_{-\infty}^{\infty} x f(x) dx\\)
-   <span g="variance">Variance</span> is \\(\sigma^2 = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) dx =  \int_{-\infty}^{\infty} x^2 f(x) dx - \mu^2\\)
-   Normally use <span g="standard_deviation">standard deviation</span> \\(\sigma\\) because it has the same units as the data
    -   Saves us from trying to figure out what a squared price is...

-   Example: <span g="uniform_distribution">uniform distribution</span> has equal probability over a finite range \\([a \ldots b]\\)
    -   \\(f(x) = \frac{1}{b - a}\\)
    -   \\(P(a \leq t \leq X \leq t+h \leq b) = \frac{h}{b - a}\\)
    -   I.e., probability is proportional to fraction of range
    -   <span g="standard_uniform">Standard uniform distribution</span> has range \\([0 \ldots 1]\\)
        -   \\(\mu = \frac{1}{2}\\)
        -   \\(\sigma^2 = \int_{0}^1 x^2 dx - (\frac{1}{2})^2 = \frac{1}{12}\\)

## What is the normal distribution and why do we care?

-   In its full glory, <span g="normal_distribution">normal distribution</span> has

\\(
\begin{align*}
f(x) & = & \frac{1}{\sigma \sqrt{2 \pi}} e^{- \frac{(x - \mu)^2}{2 \sigma^2}}
\end{align*}
\\)

-   There is no closed formula for the integral \\(F(x)\\)
    -   But as the notation suggests, mean is \\(\mu\\) and variance is \\(\sigma^2\\)
-   The <span g="standard_normal">standard normal distribution</span> \\(Z\\) has mean \\(\mu = 0\\) and standard deviation \\(\sigma = 1\\)
    -   Easy to move back and forth between this and arbitrary distribution \\(X = \mu + \sigma Z\\)

-   <span g="central_limit_theorem">Central Limit Theorem</span>
    -   Let \\(S_n = X_1 + X_2 + \ldots + X_n\\) be the sum of \\(n\\) independent random variables,
        all with mean \\(\mu\\) and standard deviation \\(\sigma\\)
    -   Can be drawn from (almost) any distribution
    -   As \\(n \rightarrow \infty\\), \\(\frac{S_n - n\mu}{\sigma \sqrt{n}}\\) converges on a standard normal random variable
        -   I.e., the distribution of our estimates of the mean is normal regardless of the underlying distribution
    -   Rate of convergence is \\(\frac{1}{\sqrt{n}}\\)
        -   I.e., to double the precision, quadruple the sample size
-   Heuristic: for \\(n \gt 30\\), \\(S_n\\) is distributed normally

-   Sample mean \\(\bar{X}\\) estimates the population mean
-   Variance of \\(\bar{X}\\) is \\(\frac{\sigma^2}{n}\\)
-   Distribution of sample means is normal, i.e. \\(\frac{\bar{X} - \mu}{\sigma / \sqrt{n}}\\) is standard normal as \\(n \rightarrow \infty\\)
    -   Regardless of the underlying distribution of \\(X\\)
-   FIXME: add program to sample various uniform distributions and see how the sampling converges on a uniform distribution

## How can we use this to quantify confidence?

-   A <span g="confidence_interval">confidence interval</span> is an interval \\([a \ldots b]\\)
    that has some probability \\(p\\) of containing the actual value of a statistic
    -   E.g., "There is a 90% probability that the actual mean of this population lies between 2.5 and 3.5"
    -   Larger intervals are less precise but have a higher probability
-   If there are more than 30 samples or the standard deviation \\(\sigma\\) is known, use a <span g="z_test">Z-test</span>:
    1.  Choose a confidence level \\(C\\) (typically 95%)
    2.  Find the value \\(z^{\star}\\) such that \\(P(x \leq z^{\star}) \leq \frac{1 - C}{2}\\)
        in a standard normal distribution
        -   Divide by 2 because the normal curve has two symmetric tails
    3.  Calculate the sample mean \\(\bar{X}\\)
    4.  Interval is \\(\bar{X} \pm z^{\star}\frac{\sigma}{\sqrt{n}}\\)

{% include figure
   id="two-tailed-test"
   cap="Two-Tailed Significance Test"
   fixme=true
   alt="FIXME"
   title="Normal curve overlaid on grid. Symmetric segments in the low and high ends of the normal curve are highlighted to show regions more than a certain distance from the cente
fixme=true ."
   width="50%"
   credit="'Boundless Statistics', Lumen Learning, https://courses.lumenlearning.com/boundless-statistics/chapter/hypothesis-testing-one-sample/" %}

-   FIXME: example

## Student's *t*-distribution

-   Usually don't know the distribution's variance
-   The <span g="sample_variance">sample variance</span> is:

\\(
\begin{align*}
s^2 & = & \frac{1}{n-1} \sum_{i=1}^{n}(X_i - \bar{X})^2 \\
    & = & \frac{\sum X_i^2 - n\bar{X}^2}{n - 1}
\end{align*}
\\)

-   Using \\(n-1\\) instead of \\(n\\) ensures that \\(s^2\\) is unbiased (the <span g="bessel_correction">Bessel correction</span>)
    -   See [proof](../theory/#bessel-correction)
-   <span g="t_distribution">Student's *t*-distribution</span> is used to estimate the mean of a normally distributed population
    when the sample size is small (e.g., less 30) and the variance is unknown
    -   Named comes from a pseudonym used by the mathematician who first used it this way
-   The variable \\(\frac{\bar{X} - \mu}{\sigma / \sqrt{n}}\\) has a standard normal distribution
-   However, the variable \\(\frac{\bar{X} - \mu}{s / \sqrt{n}}\\) has a *t*-distribution
    with \\(n-1\\) <span g="degrees_of_freedom">degrees of freedom</span>
    -   Called degrees of freedom because once \\(n-1\\) values are known, the value of the \\(n^{th}\\) is fixed
    -   \\(n-1\\) because there's a step in the calculation that normalizes the \\(n\\) values to unit length
-   The exact formula for the *t*-distribution is [a little bit scary](../theory/#student-t).
    -   The PDF's shape resembles that of a normal distribution with mean 0 and variance 1,
        but is slightly lower and wider.
    -   The two become closer as the degrees of freedom \\(\nu\\) gets larger.
-   A <span g="t_test">t-test</span> follows the same steps as a Z-test:
    1.  Choose a confidence level \\(C\\)
    2.  Find a value \\(t^{\star}\\) such that \\(P(x \leq t^{\star}) \leq \frac{1 - C}{2}\\)
        in a Student's *t*-distribution with \\(n-1\\) degrees of freedom
    3.  Estimate the standard deviation \\(s\\)
    4.  Interval is \\(\bar{X} \pm t^{\star}\frac{s}{\sqrt{n}}\\)

-   FIXME: example

## How can we compare the means of two datasets?

-   What is the probability of seeing this difference between two datasets?
    -   The <span g="null_hypothesis">null hypothesis</span> \\(H_0\\) is that the samples come from a single population
        and the observed difference is purely due to chance
    -   The <span g="alternative_hypothesis">alternative hypothesis</span> \\(H_A\\) is that
        the samples come from two difference populations
    -   <span g="false_positive">False positive</span>: decide that the difference is not purely random when it is
    -   <span g="false_negative">False negative</span>: decide the difference is purely random when it isn't
    -   Also called Type I and Type II errors (but see <https://twitter.com/neilccbrown/status/1202595479890124801>)
-   Adapt the simulation program (keep a subset of the command-line parameters)

```py
from scipy.stats import ttest_ind

def main():
    # ...parse arguments...
    
    # ...read data and calculate actual means and difference...

    # test and report
    result = ttest_ind(data_left, data_right)
```

-   Run

```sh
python bin/t-test.py --left ../hypothesis-testing/data/javascript-counts.csv --right ../hypothesis-testing/data/python-counts.csv --low 1 --high 200
```
```txt
Ttest_indResult(statistic=-269.67014904687954, pvalue=0.0)
```

-   The \\(p\\) value is so small that the computer can't distinguish it from zero
-   Which means the chances of getting this difference by randomly splitting a single population is vanishingly small

-   Look at the hours worked per day in 2019
-   Data is (date, hours) pairs taken from a spreadsheet
    -   There are a lot of spreadsheets in data science
-   Split into weekday and weekend subsets and visualize <span f="programmer-hours"/>
    -   Note that hours are never actually negative, but the curve is drawn that way

{% include figure
   id="programmer-hours"
   cap="Programmer Hours (Weekday vs. Weekend)"
   alt="FIXME"
   title="A pair of vertical violin plots. The mean for weekday equals false is near 2.1 hours per day and the mean for weekday equals true is slightly above 7 hours per day. The profile for weekday equals false does not look normal, but the profile for weekday equals true looks more normal."
   fixme=true %}

-   They certainly *seem* different
-   And a t-test confirms it
    -   The odds are large enough this time to be printable...

```sh
python bin/weekends.py --data data/programmer-hours.csv
```
```txt
weekday mean 6.804375000071998
weekend mean 3.232482993312492
Ttest_indResult(statistic=12.815512046971827, pvalue=6.936182610195961e-31)
```

<div class="callout" markdown="1">

### Higher standards

-   Recall discussion of \\(p\\) hacking from <span x="hypothesis-testing"/>
    -   If we analyze the data enough different ways, one of them will be "significant"
-   Use the <span g="bonferroni_correction">Bonferroni correction</span>
    -   The more tests we do, the more stringest our significance criteria must be

</div>
