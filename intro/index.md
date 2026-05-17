# Why Should You Care What Researchers Found?

## Learning Goals

-   Load a CSV with Polars and compute basic percentiles
-   Explain why the 10X productivity claim depends on measurement choices
-   Use the Noda DevEx framework to identify dimensions of developer experience
-   Recognize how Goodhart's Law undermines productivity metrics

---

-   In 2000, Lutz Prechelt asked dozens of programmers to solve the same phone-book problem
    in the language of their choice [%b Prechelt2000 Prechelt2019 %]
    -   The data file `jccpprtTR.csv` has one row per programmer with columns like
        `person`, `lang`, `whours` (work hours), `stmtL` (statement lines), and `whours`
    -   Every participant produced a working solution; the question is how long it took

-   The famous "10X programmer" claim lives in this dataset, but the number you get depends
    entirely on what you measure
    -   Comparing the single fastest to the single slowest gives a 105X ratio
    -   Restricting to Java alone gives 17X
    -   Comparing the 90th [%g percentile "percentile" %] to the 10th gives a much smaller number
    -   Comparing the [%g median "median" %] across language groups gives a different story again

-   A [%g box_and_whisker_plot "box-and-whisker plot" %] shows these differences clearly
    -   The box spans the 25th to 75th percentile; the center line is the median
    -   Points outside the whiskers are not necessarily errors; they are just far from typical

-   Begel and Zimmermann asked hundreds of Microsoft engineers what questions they most
    wanted researchers to answer [%b Begel2014 %]
    -   Top concerns span code quality, team productivity, and tool effectiveness
    -   None of the top-ten questions ask about individual programmer speed
    -   Engineers care about systems, not about ranking colleagues

-   [%g goodharts_law "Goodhart's Law" %] explains why individual productivity metrics fail:
    once you use a measure to evaluate people, they optimize the measure instead of the
    underlying goal
    -   If you reward lines of code per day, people write more lines per day
    -   If you reward closed tickets, people close tickets without fixing the underlying problem
    -   The measure stops tracking what you actually care about

-   Devanbu, Zimmermann, and Bird surveyed developers about their beliefs regarding software
    engineering practice [%b Devanbu2016 %]
    -   Developers held strong opinions that often contradicted evidence in their own project data
    -   Experience in one context does not automatically transfer to another context
    -   Personal intuition is data, but it is one data point with a very small sample size

-   Noda et al. argue that developer experience (DevEx) has three distinct dimensions
    [%b Noda2023 %]
    -   Feedback loops: how quickly do developers get signals about whether their work is correct?
    -   Flow state: how often can developers work without interruption?
    -   Cognitive load: how much mental effort does the environment impose beyond the actual problem?
    -   Simple metrics like lines of code per day collapse all three dimensions into noise

-   Before measuring productivity, you have to decide what productivity means
    -   A developer who writes 50 lines of clean, tested, documented code may deliver more value
        than one who writes 200 lines of tangled code that breaks the next sprint
    -   This is not a philosophical point; it changes which data you collect and how you analyze it

-   This tutorial covers 18 sessions organized into four days
    -   Day 1: loading, cleaning, grouping, and visualizing real data
    -   Day 2: hypothesis testing, effect size, correlation, and threats to validity
    -   Day 3: mining repositories and understanding the impact of AI tools
    -   Day 4: analyzing qualitative data from interviews and open-ended surveys

[%inc prechelt.py %]

## Check Understanding

<details markdown="1">
<summary markdown="1">What is wrong with claiming 10X productivity by comparing the best programmer to the worst?</summary>

Comparing extremes guarantees an inflated ratio regardless of the underlying distribution.
Every dataset has a maximum and a minimum; the ratio between them tells you about the
tails, not about typical performance. Prechelt found a 105X ratio across all languages,
but the 90th/10th percentile ratio in the same data is far smaller. Picking a comparison
method after seeing the data is also a form of cherry-picking: you can get almost any
number you want by choosing the right pair of values to compare.

</details>

<details markdown="1">
<summary markdown="1">The following code is supposed to compute the 10th and 90th percentile ratio, but it contains a bug. What is wrong and how do you fix it?

```python
p10 = df["whours"].quantile(10)
p90 = df["whours"].quantile(90)
ratio = p90 / p10
```
</summary>

The `quantile` method in Polars takes a value between 0.0 and 1.0, not a percentage.
Passing `10` asks for the value at the 10th *multiple* of the distribution, which is
out of range and will either raise an error or return `None`. The fix is:

```python
p10 = df["whours"].quantile(0.10)
p90 = df["whours"].quantile(0.90)
ratio = p90 / p10
```

</details>

<details markdown="1">
<summary markdown="1">What does Goodhart's Law predict will happen if a company starts evaluating developers by lines of code written per week?</summary>

Developers will write more lines of code per week, because that is the measure they are
being evaluated on. This can happen in several ways: removing whitespace compression,
splitting statements across multiple lines, avoiding helper functions that reduce
duplication, or simply writing verbose code where concise code would do. The number goes
up; the underlying quality of the software does not necessarily follow. Eventually the
metric stops reflecting what the company actually cares about, which is working software
delivered efficiently.

</details>

<details markdown="1">
<summary markdown="1">How does the Noda DevEx framework improve on simple productivity metrics like lines-per-day or tickets-closed?</summary>

The DevEx framework identifies three distinct dimensions of developer experience: feedback
loops, flow state, and cognitive load. A single metric like lines-per-day collapses all
three into one number, which means you cannot tell whether a low score reflects slow
feedback from CI/CD pipelines, constant interruptions, or a genuinely hard problem. By
measuring each dimension separately, teams can diagnose which specific aspect of their
environment is limiting productivity and target improvements accordingly. A developer
might be highly productive despite closing few tickets because they are carrying heavy
cognitive load imposed by poorly documented legacy code.

</details>

<details markdown="1">
<summary markdown="1">Devanbu et al. found that developers held beliefs about their own projects that contradicted evidence in the project's own data. What does this suggest about relying on team leads' opinions when evaluating a new tool?</summary>

It suggests that opinion alone is unreliable evidence, even when the person has direct
experience with the project in question. A team lead's intuition is shaped by memorable
incidents, recent events, and the subset of the codebase they interact with most
frequently. Data collected systematically across the whole project often tells a different
story. This does not mean team leads are wrong about everything, but it does mean their
opinions should be treated as hypotheses to be checked against data rather than as
conclusions.

</details>

## Exercises

<div class="exercise" markdown="1">
### Reproduce Prechelt's Java Claim

Load the Prechelt data file and filter it to Java submissions only. Find the minimum and
maximum values of `whours` in that subset and compute their ratio. Then compute the same
ratio for each other language in the dataset and present all ratios in a single Polars
dataframe, sorted from largest to smallest. Write a one-sentence interpretation of what
the table tells you about language choice and development time variability.
</div>

<div class="exercise" markdown="1">
### DevEx Self-Assessment

Pick two programming tasks you completed in the past two weeks: one that felt frustrating
and one that felt productive. For each task, rate it from 1 to 5 on the three DevEx
dimensions (feedback loops, flow state, cognitive load) and write a sentence explaining
each rating. Then identify which single dimension most limited your productivity on the
frustrating task and describe one concrete change to your environment or process that
would improve that dimension.
</div>

<div class="exercise" markdown="1">
### Percentiles by Language

Using the Prechelt data, compute the 25th, 50th, and 75th percentile of `whours` for
each programming language as a single Polars dataframe with one row per language. Sort
the rows by median development time. Identify the language with the widest interquartile
range (75th minus 25th percentile) and write a sentence explaining what a wide range
implies about predictability for project managers estimating delivery time.
</div>

<div class="exercise" markdown="1">
### Gaming a Metric

Choose one of the questions from the Begel and Zimmermann top-ten list [%b Begel2014 %]
that involves a measurable outcome. Describe a specific metric that a team might use to
track progress on that question. Then describe in concrete terms how a developer or
manager could game that metric: that is, how they could improve the number without
improving the underlying outcome the metric was designed to measure. Explain which aspect
of Goodhart's Law your example illustrates.
</div>

<div class="exercise" markdown="1">
### Belief Versus Evidence

The Devanbu et al. study [%b Devanbu2016 %] found that developers' beliefs often do not
match the evidence in their own projects. Write a short paragraph proposing one hypothesis
about why this gap exists: for example, why might a developer's experience with a
particular module lead them to a false belief about the codebase as a whole? Then propose
a study design that a team could run with their own project data to test whether a
specific commonly-held belief is accurate. Specify what data you would collect, how you
would collect it, and what result would count as evidence against the belief.
</div>
