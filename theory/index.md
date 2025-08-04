# Theory

A little theory can go a long way.

## Basic probability

-   Assume a set of <span g="event">events</span> \\(E\\) and a probability function \\(P\\) with \\(0 \leq P(x) \leq 1\\)
-   If \\(A\\) and \\(B\\) are disjoint sets of events from \\(E\\) then:
    -   \\(P(E) = 1\\) (i.e., something must happen)
    -   \\(P(A \cup B) = P(A) + P(B)\\) (i.e., probability of the union of disjoint sets is the sum of their probabilities)
-   A few consequences:
    -   If \\(A\\) and \\(B\\) are not disjoint, then \\(P(A \cup B) = P(A) + P(B) - P(A \cap B)\\)
    -   \\(P(\neg A) = 1 - P(A)\\)
    -   If \\(A\\) and \\(B\\) are disjoint, \\(P(A \cup B) = P(A)P(B)\\)
    -   The probability of \\(n\\) equally likely disjoint events \\(x_i\\) is \\(nP(x_i)\\)

## Combinatorics

-   There are \\(n^{k}\\) ways to sample \\(k\\) distinguishable items from \\(n\\) *with* replacement
-   There are \\(P(n, k) = \frac{n!}{(n - k)!}\\) ways to sample \\(k\\) distinguishable items from \\(n\\) *without* replacement
-   If the items are indistinguishable, the number of selections is
    \\(C(c, k) = \binom{c}{k} = \frac{P(n, k)}{k!} = \frac{n!}{k!(n - k)!}\\)
    -   Divide by \\(k!\\) because the indistinguishable items can be rearranged that many ways

## Conditional probability

-   The <span g="conditional_probability">conditional probability</span> \\(P(A \mid B)\\) of \\(A\\) given \\(B\\) is
    the probability of \\(A\\) occurring given that \\(B\\) is known to occur
-   \\(P(A \mid B) = \frac{P(A \cap B)}{P(B)}\\)

## Bayes Rule

-   Since \\(P(A \mid B) = P(B \mid A)\\), we have <span g="bayes_rule">Bayes' Rule</span>
    \\(P(B \mid A) = \frac{P(A \mid B)P(B)}{P(A)}\\)
-   Special case: since \\(P(A) = P(A \mid B) + P(A \mid \neg B)\\),
    \\(P(B \mid A) = \frac{P(A \mid B)P(B)}{P(A \mid B)P(B) + P(A \mid \neg B)P(\neg B)}\\)

## Mean and variance

-   The <span g="mean">mean</span> \\(\mu\\) or <span g="expected_value">expected value</span> \\(E(X)\\) is the weighted sum of possible outcomes
    \\(\sum_{x} xP(x)\\)
-   Implies \\(E(aX + bY + c) = aE(X) + bE(Y) + c\\)
-   The <span g="variance">variance</span> \\(\sigma^2\\) is the expected value of the square of the difference between values and the mean
    \\(\sum_{x} (x - \mu)^2P(x)\\)
    -   Squaring guarantees that values are positive
    -   And gives extra weight to outliers
    -   But the units are weird: "bugs squared"
-   \\(\sigma^{2}_{A + B} = \sigma^2_A + \sigma^2_B\\) if \\(A\\) and \\(B\\) are independent
-   The <span g="standard_deviation">standard deviation</span> \\(\sigma\\) is the square root of the variance
    -   Same units as original variable

## Covariance and correlation

-   <span g="covariance">Covariance</span> \\(\sigma_{XY}\\) of \\(X\\) and \\(Y\\) is \\(E((X - \mu_{X})(Y - \mu_{Y}))\\)
    -   If \\(X\\) and \\(Y\\) are both above or below their means at the same time, \\(\sigma_{XY}\\) will be positive
    -   If \\(X\\) is above when \\(Y\\) is below and vice versa, \\(\sigma_{XY}\\) will be negative
    -   If there is no relation, \\(\sigma_{XY}\\) will be zero
-   <span g="pearson_correlation_coefficient">Pearson's correlation coefficient</span> \\(r_{XY}\\) is covariance normalized by standard deviations
    -   \\(r_{XY} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y}\\)
    -   Always lies in \\([-1 \ldots 1]\\)
-   <span g="chebyshev_inequality">Chebyshev's Inequality</span>: \\(P(\mid X - \mu \mid \gt \epsilon) \leq (\frac{\sigma}{\epsilon})^2\\)
    -   I.e., the probability of a value being more than \\(\epsilon\\) away from the mean is bounded by
        the square of the ratio between the standard deviation and \\(\epsilon\\)
    -   See [proof](#chebyshev)

## Bernoulli distribution

-   A <span g="bernoulli_distribution">Bernoulli distribution</span> is
    a random variable with just two values 1 and 0 (sometimes called success and failure)
    -   Named after the mathematician who first described it
-   Probability of success is \\(p\\)
-   \\(\mu = 0(1 - p) + 1(p) = p\\)
-   \\(\sigma^2 = \sum (x - p)^2 P(x) = (0 - p)^2 (1 - p) + (1 - p)^2 p = p(1 - p)\\)

## Binomial distribution

-   A <span g="binomial_distribution">binomial distribution</span> is
    the number of successes in \\(n\\) trials of a Bernoulli variable with probability \\(p\\)
    -   Name means "two numbers" (referring to \\(n\\) and \\(k\\))
-   Probability of exactly \\(x\\) successes in \\(n\\) trials is \\(\binom{n}{x} p^x (1-p)^{n-x}\\)
    -   Number of different arrangements of that many successes and that many failures
-   \\(\mu = np\\) (because trials are independent)
-   \\(\sigma^2 = np(1-p)\\) (because \\(\sigma^{2}_{A + B} = \sigma^2_A + \sigma^2_B\\) if \\(A\\) and \\(B\\) are independent)
-   Probability of up to \\(x\\) successes is complicated to calculate, but we can use approximations (FIXME)

## Geometric distribution

-   A <span g="geometric_distribution">geometric distribution</span> is
    the number of Bernoulli trials needed to get the first success
    -   Potentially 
-   \\(P(x) = (1 - p)^{x - 1}p\\) (i.e., \\(x-1\\) failures followed by 1 success)
-   To find the mean, use the fact that \\(\sum_{i=0}^{\infty} x^i = \frac{1}{1 - x}\\) for \\(0 \lt x \lt 1\\)
    -   A geometric series, which gives the distribution its name
-   \\(\mu = 1/p\\)
-   The variance takes a little more work, but is \\(\sigma^2\\) is \\(\frac{1-p}{p^2}\\)

## Negative binomial distribution

-   The binomial distribution describes the numbr of successes in a fixed number of trials
-   The <span g="negative_binomial_distribution">negative binomial distribution</span> is
    the number of trials required to achieve a certain number of successes
    -  "Negative" in the sense of opposite: there is nothing negative in the values
-   \\(P(x) = \binom{x - 1}{k - 1} (1 - p)^{x - k} p^k\\)
    -   Reading right to left, this is \\(k\\) successes, \\(x-k\\) failures,
        and the number of possible rearrangements with the last being a success (which is why the -1)
-   \\(\mu = \frac{k}{p}\\)
-   \\(\sigma^2 = \frac{k(1-p)}{p^2}\\)
-   With \\(k=1\\), the negative binomial is just the geometric distribution (number of trials to first success)

## Poisson distribution

-   Number of events occurring within a fixed period has a <span g="poisson_distribution">Poisson distribution</span>
    -   Assuming events never occur simultaneously
-   \\(P(x) = e^{- \lambda}\frac{\lambda^x}{x!}\\)
-   \\(\mu = \lambda\\)
-   \\(\sigma^2 = \lambda\\)
-   Poisson is a special case of binomial where the number of trials is very large
    and the probability of success in any trial is small
    -   See [proof](#binomial-poisson)
-   For \\(n \geq 30\\) and \\(p \leq 0.05\\), Poisson is a good approximation of binomial

## Probability density and cumulative distribution

-   Function describing probabilities of discrete events is called the <span g="pmf">probability mass function</span>
-   When describing continuous events, use:
    -   <span g="cdf">Cumulative distribution function</span> \\(F(x) = P(X \leq x)\\)
    -   <span g="pdf">Probability density function</span> \\(f(x) = dF/dx\\)
-   So \\(P(a \lt X \lt B) = \int_{a}^{b} f(x) dx\\)
-   Require \\(\int_{-\infty}^{\infty} f(x) dx = 1\\)
    -   And notice \\(P(x) = P(x \leq X \leq x) = \int_{x}^{x} f(x) dx = 0\\)
    -   I.e., probability of any specific exact value is 0
-   \\(\mu = \int_{-\infty}^{\infty} x f(x) dx\\)
-   \\(\sigma^2 = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) dx =  \int_{-\infty}^{\infty} x^2 f(x) dx - \mu^2\\)

## Uniform distribution

-   <span g="uniform_distribution">Uniform distribution</span> has equal probability over a finite range \\([a \ldots b]\\)
-   \\(f(x) = \frac{1}{b - a}\\)
-   \\(P(a \leq t \leq X \leq t+h \leq b) = \frac{h}{b - a}\\)
    -   I.e., probability is proportional to fraction of range
-   <span g="standard_uniform">Standard uniform distribution</span> has range \\([0 \ldots 1]\\)
    -   \\(\mu = \frac{1}{2}\\)
    -   \\(\sigma^2 = \int_{0}^1 x^2 dx - (\frac{1}{2})^2 = \frac{1}{12}\\)

## Exponential distribution

-   Assume the waiting time for the next rare event is independent of the time waited so far
    -   I.e., \\(P(X \geq b+a \mid X \geq a) = P(X \geq b)\\)
-   Can show that \\(f(x) = \lambda e^{- \lambda x}\\) is the unique solution, so \\(F(x) = 1 - e^{- \lambda x}\\)
-   \\(\mu = \frac{1}{\lambda}\\)
-   \\(\sigma^2 = \frac{1}{\lambda^2}\\)
-   The parameter \\(\lambda\\) is the frequency
    -   If \\(\lambda = 2\\) then we expect 2 events per unit time and \\(\mu = \frac{1}{\lambda} = 0.5\\) units of time between events
-   The Poisson distribution with parameter \\(\lambda\\) is the number of events in time \\(t\\) (discrete)
    -   See [proof](#exponential-poisson)

## Gamma distribution

-   If there are \\(\alpha\\) independent sequential steps,
    each taking an exponentially-distributed time with rate \\(\lambda\\),
    then the total time has a <span g="gamma_distribution">Gamma distribution</span> Gamma(\\(\alpha\\), \\(\lambda\\))
    -   Name comes from the gamma function, which extends factorial to complex numbers
-   \\(f(x) = \frac{\lambda^\alpha}{\Gamma (\alpha)} x^{\alpha - 1} e^{- \lambda x}\\)
    -   \\(\alpha\\) is sometimes called the shape parameter
    -   Gamma(1, \\(\lambda\\)) is an exponential distribution with rate \\(\lambda\\)
-   \\(\mu = \frac{\alpha}{\lambda}\\)
-   \\(\sigma^2 = \frac{\alpha}{\lambda^2}\\)
-   For specific values, use library or lookup tables
-   FIXME: relationship between Gamma and Poisson

## Normal distribution

-   In its full glory, <span g="normal_distribution">normal distribution</span>
    has \\(f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{- \frac{(x - \mu)^2}{2 \sigma^2}}\\)
    -   There is no closed form for the integral \\(F(x)\\)
-   But as the notation suggests, means is \\(\mu\\) and variance is \\(\sigma^2\\)
-   The <span g="standard_normal">standard normal distribution</span> \\(Z\\) has mean \\(\mu = 0\\) and standard deviation \\(\sigma = 1\\)
    -   Reconstruct arbitrary distribution \\(X = \mu + \sigma Z\\)

## Central Limit Theorem

-   Let \\(S_n = X_1 + X_2 + \ldots + X_n\\) be the sum of \\(n\\) independent random variables,
    all with mean \\(\mu\\) and standard deviation \\(\sigma\\)
-   As \\(n \rightarrow \infty\\), \\(\frac{S_n - n\mu}{\sigma \sqrt{n}}\\) converges on a standard normal random variable
    -   Rate of convergence is \\(\frac{1}{\sqrt{n}}\\)
-   Heuristic: for \\(n \gt 30\\), a normal distribution is an accurate approximation to \\(S_n\\)
-   In particular, binomial(\\(n\\), \\(p\\)) \\(\approx\\) normal(\\(\mu = np\\), \\(\sigma = \sqrt{n p (1 - p)}\\) )
    -   But use a <span g="continuity_correction">continuity correction</span>:
        adjust interval by 0.5 units to allow for difference between discrete and continuous
    -   E.g., \\(P(X = x) = P(x - 0.5 \lt X \lt x + 0.5)\\) (because the probability of a point in a continuous distribution is zero)

## Sampling

-   A <span g="population">population</span> has a parameter; a <span g="sample">sample</span> has a <span g="statistic">statistic</span>
-   Sample mean \\(\bar{X}\\) estimates the population mean \\(\mu = E(X)\\)
-   Variance of \\(\bar{X}\\) is \\(\frac{\sigma^2}{n}\\)
-   Distribution of sample means is normal, i.e. \\(\frac{\bar{X} - \mu}{\sigma \sqrt{n}}\\) is standard normal as \\(n \rightarrow \infty\\)
    -   Regardless of the underlying distribution of \\(X\\)
-   The <span g="median">median</span> is the central value such that \\(P(X \lt M) \leq 0.5\\) and \\(P(X \gt M) \leq 0.5\\)
    -   If the distribution is skewed to the right, \\(M \lt \mu\\)
    -   If the distribution is skewed to the left, \\(M \gt \mu\\)
-   A <span g="quartile">quartile</span> is a value that divides the sample into quarters
    -   E.g., first quartile \\(Q_1\\) splits values 25%/75%, third quartile \\(Q_3\\) splits values 75%/25%
    -   Second quartile is the same as the median
    -   The <span g="iqr">interquartile range</span> IQR is \\(Q_3 - Q_1\\)
    -   Anything more than 1.5 IQR below \\(Q_1\\) or above \\(Q_3\\) is considered an outlier
    -   Because if the data is normal, only 0.7% of it should lie outside these bounds
-   The <span g="sample_variance">sample variance</span> is:

\\(
\begin{align*}
s^2 & = & \frac{1}{n-1} \sum_{i=1}^{n}(X_i - \bar{X})^2 \\
    & = & \frac{\sum X_i^2 - n\bar{X}^2}{n - 1}
\end{align*}
\\)

-   Using \\(n-1\\) instead of \\(n\\) ensures that \\(s^2\\) is unbiased (the <span g="bessel_correction">Bessel correction</span>)
    -   See [proof](#bessel-correction)

## Parameter estimation

-   The \\(k^{th}\\) <span g="population_moment">population moment</span> is \\(E(X^k)\\)
-   The \\(k^{th}\\) <span g="sample_moment">sample moment</span> is \\(\frac{1}{n}\sum_{i=1}^{n} X_i^k\\)
    -   The first sample moment is the sample mean
-   The population and sample <span g="central_moment">central moments</span> are \\(E(X - \mu)^k\\) and \\(\frac{1}{n}\sum(X_i - \bar{X})^k\\) respectively
    -   I.e., the moments after shifting the data to a mean of zero
-   Parameter estimation via the <span g="method_of_moments">method of moments</span>:
    find parameter values to match sample moments
-   Parameter estimation via <span g="maximum_likelihood_estimation">maximum likelihood</span>:
    choose parameter values to maximize the likelihood of the observed sample
-   Example: estimation \\(\lambda\\) for Poisson distribution
    -   PMF is \\(P(x) = e^{- \lambda} \frac{\lambda^x}{x!}\\)
    -   Taking logarithms, \\(\ln{P(x)} = -\lambda + x \ln{\lambda} - \ln{x!}\\)
    -   So we need to maximize \\(\ln{P(x)} = \sum{(\lambda + X_i \ln{\lambda})} + C = -n \lambda + \ln{\lambda}\sum{X_i} + C\\)
        where \\(C = -\sum{\ln{x!}}\\) is a constant that does not depend on \\(\lambda\\)
    -   Differentiating with respect to \\(\lambda\\) and setting equal to zero gives
        \\(\frac{\partial}{\partial{\lambda}}\ln{P(X)} = -n + \frac{1}{\lambda}\sum{X_i} = 0\\)
    -   Only solution is \\(\lambda = \frac{1}{n}\sum{X_i} = \bar{X}\\)

## Student's *t*-distribution

-   <span g="t_distribution">Student's *t*-distribution</span> is used to estimate the mean of a normally distributed population
    when the sample size is small (e.g., less 30) and the variance is unknown
    -   Named comes from a pseudonym used by the mathematician who first used it this way
-   If \\(X\\) is normally distributed with mean \\(\mu\\) and variance \\(\sigma^2\\),
    then \\(\bar{X} = \frac{1}{n}\sum{X_i}\\) is the sample mean
    and \\(s^2 = \frac{1}{n-1}\sum{(X_i - X)^2}\\) is the Bessel-corrected sample variance
-   The variable \\(\frac{\bar{X} - \mu}{\sigma / \sqrt{n}}\\) has a standard normal distribution
-   However, the variable \\(\frac{\bar{X} - \mu}{s / \sqrt{n}}\\) has a *t*-distribution
    with \\(n-1\\) <span g="degrees_of_freedom">degrees of freedom</span>
    -   \\(n-1\\) because there's a step in the calculation that normalizes the \\(n\\) values to unit length
    -   Once \\(n-1\\) are known, the value of the \\(n^{th}\\) is fixed
-   The exact formula for the *t*-distribution is [a little bit scary](#student-t).
    -   The PDF's shape resembles that of a normal distribution with mean 0 and variance 1,
        but is slightly lower and wider.
    -   The two become closer as the degrees of freedom \\(\nu\\) gets larger.

## Confidence intervals

-   A <span g="confidence_interval">confidence interval</span> is an interval \\([a \ldots b]\\)
    that has some probability \\(p\\) of containing the actual value of a statistic
    -   E.g., "There is a 90% probability that the actual mean of this population lies between 2.5 and 3.5"
    -   Larger intervals have a higher probability but are less precise
-   If there are more than 30 samples or the standard deviation \\(\sigma\\) is known, use a <span g="z_test">z-test</span>:
    1.  Choose a confidence level \\(C\\) (typically 95%)
    2.  Find the value \\(z^{\star}\\) such that \\(P(x \leq z^{\star}) \leq \frac{1 - C}{2}\\)
        in a standard normal distribution
        -   Divide by 2 because the normal curve has two symmetric tails
    3.  Calculate the sample mean \\(\bar{X}\\)
    4.  Interval is \\(\bar{X} \pm z^{\star}\frac{\sigma}{\sqrt{n}}\\)
-   If there are fewer than 30 samples or the standard deviation isn't known, use a <span g="t_test">t-test</span>:
    1.  Choose a confidence level \\(C\\)
    2.  Find a value \\(t^{\star}\\) such that \\(P(x \leq t^{\star}) \leq \frac{1 - C}{2}\\)
        in a Student's *t*-distribution with \\(n-1\\) degrees of freedom
    3.  Estimate the standard deviation \\(s\\)
    4.  Interval is \\(\bar{X} \pm t^{\star}\frac{s}{\sqrt{n}}\\)

## Hypothesis testing

-   What is the probability of seeing this difference between two datasets?
    -   The <span g="null_hypothesis">null hypothesis</span> \\(H_0\\) is that the samples come from a single population
        and the observed difference is purely due to chance
    -   The <span g="alternative_hypothesis">alternative hypothesis</span> \\(H_A\\) is that
        the samples come from two difference populations
    -   <span g="false_positive">False positive</span>: decide that the difference is not purely random when it is
    -   <span g="false_negative">False negative</span>: decide the difference is purely random when it isn't
-   Example: if a coin comes up heads 9 times out of 10, what are the odds it is actually fair?
    -   Probability if the coin is fair is \\(\binom{10}{9} \cdot 0.5^9 \cdot (1-0.5)^1 = 10 \cdot 0.00195 \cdot 0.5 = 0.00976\\)
    -   I.e., less than 1% chance of seeing this result if the coin is far

## Prediction

-   <span g="accuracy">Accuracy</span> is the fraction of correct predictions (true positive + true negative)
    -   Not useful if there are only a few defective items, since "all good" will have high accuracy
-   <span g="precision">Precision</span> is the fraction of positives that are actually positive,
    i.e. true positive / (true positive + false positive)
-   <span g="recall">Recall</span> is the fraction of positives the method can actually identify,
    i.e., true positive / (true positive + false negative)
-   Perfect precision and perfect recall mean all items are classified correctly
    -   But increasing precision often reduces recall and vice versa
-   The <span g="f_measure">F-measure</span> is the <span g="harmonic_mean">harmonic mean</span> of precision and recall

## Spearman's rank correlation

-   <span g="spearmans_rank_correlation">Spearman's rank correlation</span> measures the <span g="rank_correlation">rank correlation</span> between two variables
    -   Rather than the values, measure how well the sorted order of items matches
-   Given two random variables \\(X_i\\) and \\(Y_i\\), sort items and assign ranks \\(r_{X_i}\\) and \\(r_{Y_i}\\)
    and calculate the correlation coefficient of the ranks
-   If ranks are distinct integers, can use the simplified formula \\(\rho = 1 - \frac{6 \sum{d_i^2}}{n (n^2 - 1)}\\)
    where \\(d_i = r_{X_i} - r_{Y_i}\\) is the difference between the ranks of observation \\(i\\)
-   Standard error is \\(\sigma = \frac{0.6325}{\sqrt{n - 1}}\\)

## Proofs

These proofs are included primarily to help readers understand and remember
a few key relationships.

### Chebyshev's Inequality

\\(P(\mid X - \mu \mid \gt \epsilon) \leq (\frac{\sigma}{\epsilon})^2\\)

\\(
\begin{align*}
\sigma^2 & =    & \sum_x (x - \mu)^2 P(X) \\
         & \geq & \sum_{x : \mid x - \mu \mid \gt \epsilon} (x - \mu)^2 P(X) \\
         & \geq & \sum_{x : \mid x - \mu \mid \gt \epsilon} \epsilon^2 P(X) \\
         & =    & \epsilon^2 \sum_{x : \mid x - \mu \mid \gt \epsilon} P(X) \\
         & =    & \epsilon^2 P(\mid X - \mu \mid \gt \epsilon)
\end{align*}
\\)

### Poisson as the limit to the binomial distribution

-   For binomial:

\\(
\begin{align*}
P(X = k) & = & \binom{n}{k} p^k (1 - p)^{n - k}
\end{align*}
\\)

-   Let \\(\lambda = np\\) be the success rate (number of trials times probability per trial)
-   Then \\(p = \frac{\lambda}{n}\\) and:

\\(
\begin{align*}
P(X = k) & = & \frac{n!}{k!(n - k)!} (\frac{\lambda}{n})^k (1 - \frac{\lambda}{n})^{n - k} \\
         & = & (\frac{\lambda^k}{k!}) \frac{n!}{(n - k)!} \frac{1}{n^k} (1 - \frac{\lambda}{n})^n (1 - \frac{\lambda}{n})^{- k}
\end{align*}
\\)

-   But:

\\(
\begin{align*}
\lim_{n \rightarrow \infty} \frac{n!}{(n - k)!} \frac{1}{n^k} & = & \lim_{n \rightarrow \infty} \frac{n(n - 1)(n - 2)\ldots(n - k + 1)}{n^k} \\
                                                              & = & \lim_{n \rightarrow \infty} \frac{n}{n} \frac{n - 1}{n} \ldots \frac{n - k + 1}{n} \\
                                                              & = & 1
\end{align*}
\\)

-   And since \\(e = \lim_{x \rightarrow \infty} (1 + \frac{1}{x})^x\\), if \\(\theta = -\frac{n}{\lambda}\\) then:

\\(
\begin{align*}
\lim_{n \rightarrow \infty} (1 - \frac{\lambda}{n})^n & = & \lim_{n \rightarrow \infty} (1 + \frac{1}{\theta})^{-\lambda\theta} \\
                                                      & = & e^{- \lambda} \\
\end{align*}
\\)

-   Finally:

\\(
\begin{align*}
\lim_{n \rightarrow \infty} (1 - \frac{\lambda}{n})^{-k} & = & 1
\end{align*}
\\)

-   Multiplying these all together gives the formula for the Poisson distribution

### Relationship between Poisson and exponential distributions

-   Let \\(N_t\\) be the number of events in time \\(t\\)
-   And \\(X_t\\) be the time for one *additional* event if there was an event at time \\(t\\)
-   If \\(X_t \gt x\\) then \\(N_t = N_{t+x}\\)
-   Since total probability is always 1, \\(P(X_t \leq x) = 1 - P(X_t \gt x)\\)
-   So \\(P(X_t \leq x) = 1 - P(N_{t+x} - N_t = 0) = P(N_x = 0)\\) (because the process is memoryless)
-   But \\(P(N_x = 0) = \frac{(\lambda x)^0}{0!}e^{- \lambda x} = e^{- \lambda x}\\)
-   So \\(P(X_t \leq x) = 1 - e^{- \lambda x}\\)

### Bessel correction

-   For a sample \\(a\\), \\(X\\) deviates from sample mean \\(\bar{X}\\) with variance \\(\sigma_{a}^2\\)
-   But the sample mean \\(\bar{X}\\) deviates from the population mean \\(\mu\\) with variance \\(\sigma^2 / n\\)
-   So the population variance \\(\sigma^2 = \sigma_{a}^2 + \sigma^2 / n\\)
-   Rearranging gives \\(\sigma^2 = \frac{n}{n-1} \sigma_{a}^2\\)
-   But \\(\sigma_{a}^2 = \frac{\sum (X_i - \bar{X})^2}{n}\\), so \\(\sigma^2 = \frac{\sum (X_i - \bar{X})^2}{n-1}\\)

### Student's t distribution

The PDF of Student's *t*-distribution with \\(\nu\\) degrees of freedom is:

\\(
\begin{align*}
f(t)
& =
& \frac{\Gamma(\frac{\nu+1}{2})}{\sqrt{\nu\pi} \Gamma(\frac{\nu}{2})} (1+\frac{t^2}{\nu})^{-\frac{\nu+1}{2}}
\end{align*}
\\)

where \\(\Gamma\\) is the <span g="gamma_function">gamma function</span>.
For positive even integer values of \\(\nu\\),
the first term is:

\\(
\begin{align*}
\frac{\Gamma(\frac{\nu+1}{2})} {\sqrt{\nu\pi}\,\Gamma(\frac{\nu}{2})}
& =
& \frac{(\nu -1)(\nu -3)\cdots 5 \cdot 3}{2 \sqrt{\nu}(\nu -2)(\nu -4)\cdots 4 \cdot 2}
\end{align*}
\\)

For positive odd integer values of \\(\nu\\),
the first term is:

\\(
\begin{align*}
\frac{\Gamma(\frac{\nu+1}{2})} {\sqrt{\nu\pi}\,\Gamma(\frac{\nu}{2})}
& =
& \frac{(\nu -1)(\nu -3)\cdots 4 \cdot 2}{\pi \sqrt{\nu}(\nu -2)(\nu -4)\cdots 5 \cdot 3}
\end{align*}
\\)
