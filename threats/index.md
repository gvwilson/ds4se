# Confounds, Bias, and Threats to Validity

## Learning Goals

-   Identify and name specific threats to validity in published SE studies
-   Distinguish confounds, selection bias, and survivorship bias
-   Explain why GitHub data over-represents certain types of projects
-   Apply the Kalliamvakou criteria to classify repositories as real projects or not

## Lesson

-   Bird et al. studied file ownership and defect rates in Windows Vista and Windows 7 [%b Bird2011 %]
    -   Files with low ownership (many contributors, none dominant) had significantly higher post-release defect rates
    -   But larger files also have more defects, and larger files tend to attract more contributors
    -   File size is a [%g confound "confound" %]: a third variable that affects both the apparent cause
        (ownership) and the apparent effect (defect rate), making it hard to isolate the real relationship
    -   Bird et al. controlled for file size; if you do not, you cannot tell whether ownership matters or
        whether you are just rediscovering that big files are complicated
-   [%g selection_bias "Selection bias" %] occurs when the sample you study is not representative of the
    population you care about
    -   GitHub hosts millions of repositories, which sounds like a comprehensive sample of software
    -   Kalliamvakou et al. examined 3,000 GitHub projects and found that the majority were personal
        experiments, mirrors of other repositories, or clearly abandoned [%b Kalliamvakou2014 %]
    -   Fewer than 8% had an active pull-request workflow; most repositories had a single contributor
    -   Studying "GitHub projects" and calling the results representative of software development
        is like studying Amazon reviews and calling them representative of consumer opinion
-   Kalliamvakou et al. proposed concrete criteria for identifying repositories worth studying
    -   Fewer than 5 commits: not a real project
    -   Only one contributor: not a collaborative project
    -   Last commit more than two years ago: likely abandoned
    -   Applying these filters removes most repositories from any random GitHub sample
-   [%g survivorship_bias "Survivorship bias" %] is a specific form of selection bias that targets things
    that survived a process, ignoring everything that did not
    -   Ait et al. found that a large fraction of GitHub projects go inactive within months of creation,
        and these projects are almost never studied [%b Ait2022 %]
    -   If you want to know what makes software projects succeed, studying only successful projects
        tells you what survivors look like, not what causes survival
    -   The missing projects may be the most informative data you have
-   [%g hero_developer "Hero developers" %] add a confound to ownership studies [%b Majumder2019 %]
    -   In many open-source projects, one person makes more than 80% of the commits
    -   A file that appears to have "high ownership" (one dominant contributor) may simply be
        a file the hero cares about, not a file that benefits from single ownership
    -   The hero's attention, not the ownership structure, may be what reduces defects
-   He et al. found that GitHub star counts are routinely inflated by bots and paid services [%b He2024 %]
    -   Millions of stars across tens of thousands of repositories appear to be fake
    -   Stars are used as a proxy for project quality and adoption in dozens of published studies
    -   A metric that can be purchased for a few dollars is not a reliable signal of anything
-   Acciai et al. found systematic bias in who gets access to shared research data [%b Acciai2023 %]
    -   Researchers at high-prestige institutions are more likely to receive shared datasets
    -   This means replication attempts are not evenly distributed across the research community
    -   The studies most likely to be replicated are studies by the researchers least likely to need it
-   Furia et al. argue that most observational SE studies support only correlational claims [%b Furia2023 %]
    -   Correlation describes what tends to happen together; causation describes what produces what
    -   Claiming that a correlation implies causation is one of the most common threats to validity in SE
    -   A confound, a reverse causation, or a shared underlying driver can all produce strong correlations
-   The [%g observer_effect "observer effect" %] applies when programmers know they are being studied
    -   Developers in productivity studies often produce unusually clean, well-documented code
    -   Self-reported data about hours worked and task difficulty is systematically biased toward
        what respondents think the researchers want to hear
-   [%g external_validity "External validity" %] asks whether findings generalize beyond the study context
    -   A study of undergraduate students in a two-hour lab session may not generalize to a professional
        team shipping production software over six months
    -   Open-source projects and proprietary commercial software differ in structure, incentives,
        and contributor motivation; findings in one setting may not transfer
-   The code below loads a sample of 200 GitHub repositories, applies the Kalliamvakou criteria,
    and computes Pearson r between stars and commits

[%inc classify_repos.py %]

-   The fraction that fails the Kalliamvakou criteria is typically large, often more than half
    -   The correlation between stars and commits reveals whether popularity and activity are linked
    -   A high r might suggest stars track real activity; it might also reflect that active repos
        attract both legitimate users and bots

## Check Understanding

<details markdown="1">
<summary markdown="1">What is the difference between a confound and selection bias? Give one example of each from SE research.</summary>

A confound is a variable that affects both the cause and the effect in a study, creating
a spurious relationship between them. For example, in the Bird et al. study, file size
affects both the number of contributors (big files attract more contributors) and the
defect rate (big files have more defects), so any relationship between contributors and
defects could be explained by size alone.

Selection bias occurs when the sample studied is not representative of the population of
interest because of how participants or cases were selected. For example, studying only
active GitHub repositories biases toward projects that already succeeded, omitting the
failed projects that might reveal what causes failure.

</details>

<details markdown="1">
<summary markdown="1">The following code tries to filter repositories whose last commit was more than two years ago, but it does not work correctly. What is the bug and how do you fix it?

```python
cutoff = datetime.datetime.today() - datetime.timedelta(730)
old = df.filter(pl.col("last_commit") < cutoff)
# last_commit column contains strings like "2023-04-15"
```
</summary>

There are two bugs. First, `datetime.datetime.today()` returns a datetime object, but
`last_commit` contains ISO date strings. Comparing a string to a datetime object will
either raise an error or produce incorrect results depending on the comparison method.
Second, subtracting a timedelta from a datetime gives another datetime; you need an ISO
format string to compare against the string column. The fix is:

```python
cutoff = (datetime.date.today() - datetime.timedelta(days=730)).isoformat()
old = df.filter(pl.col("last_commit") < cutoff)
```

This produces a string like `"2024-05-16"` that sorts lexicographically in the same order
as chronologically, so the string comparison is correct.

</details>

<details markdown="1">
<summary markdown="1">Why does studying only active GitHub repositories introduce survivorship bias?</summary>

Survivorship bias occurs because the repositories you can observe are the ones that
survived long enough to still exist and still be active. Projects that were abandoned
early, deleted by their owners, or never gained any traction are absent from the sample.
If you want to understand what makes projects succeed, you are missing the very data that
would contrast success with failure. The effect is that your conclusions describe what
active projects look like, not what causes a project to become active.

</details>

<details markdown="1">
<summary markdown="1">A paper finds that repositories with more GitHub stars have higher code quality as measured by static analysis. Why can't you conclude that gaining stars causes quality to improve?</summary>

Correlation between stars and quality is consistent with at least three explanations.
Stars might cause quality if developers clean up their code after it becomes popular.
Quality might cause stars if well-written code attracts users. Or a third variable, such
as the reputation and skill of the original author, might cause both high quality and high
star counts independently. Without an experiment or a careful causal design, you cannot
distinguish between these explanations. The correlation is real; the direction and
mechanism are unknown.

</details>

## Exercises

<div class="exercise" markdown="1">
### Threats to validity in a published claim

In a small group, review the following hypothetical finding: "Teams that conduct daily
standups ship features 30% faster, based on a voluntary survey of 200 developers at a
single company." Identify three specific threats to validity in this study design,
name each threat using the vocabulary from this lesson, and describe one concrete change
to the study design that would address each threat. For each change, estimate in one
sentence how difficult that change would be to implement in practice.
</div>

<div class="exercise" markdown="1">
### Stars as a quality signal

He et al. found that millions of GitHub stars appear to be fake. Using the 200-repository
sample, compute Pearson r between star counts and commit counts. Write one sentence
interpreting the correlation you find. Write a second sentence explaining why a high
correlation between stars and commits still does not make star count a reliable signal of
project quality, given what He et al. found.
</div>

<div class="exercise" markdown="1">
### Controlling for a confound

Bird et al. controlled for file size when studying the relationship between ownership and
defect rates. In the 200-repository sample, compute Pearson r between the number of
commits and the number of contributors. Write two sentences explaining why this
correlation matters when any study claims that either variable affects code quality.
Then describe in one sentence the statistical approach you would use to study the effect
of commits while controlling for contributors.
</div>

<div class="exercise" markdown="1">
### From correlation to causal claim

Furia et al. argue that observational data supports only correlational claims, not causal
ones. Pick any finding from the first week of the course (for example, Python files tend
to be longer than JavaScript files). Write one sentence stating the correlation. Write a
second sentence proposing a plausible confound that could explain the correlation without
any causal relationship between language choice and file length. Write a third sentence
describing the study design you would need to rule out that confound.
</div>

<div class="exercise" markdown="1">
### Activity and star counts

Ait et al. found that many GitHub projects go inactive shortly after creation. In the
200-repository sample, classify each repository as active (last commit within 12 months)
or inactive (last commit more than 12 months ago). Compute the mean star count for each
group. Report whether active repositories have more stars on average. Write two sentences
interpreting the result and explaining whether the difference, if any, implies that star
count is a useful predictor of project activity.
</div>
