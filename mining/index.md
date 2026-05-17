# Mining Software Repositories

## Learning Goals

-   Extract contribution data from git commit histories using GitPython
-   Compute [%g gini_coefficient "Gini coefficients" %] and plot [%g lorenz_curve "Lorenz curves" %]
-   Identify [%g hero_developer "hero developer" %] patterns in open-source projects
-   Recognize ethical and data-quality issues in MSR work

## Git Objects and History

-   Git stores four kinds of objects: blobs (file contents), trees (directory snapshots), commits (pointers to trees with metadata), and tags
    -   Every commit records a tree, a parent commit, an author, a committer, a timestamp, and a message
    -   The author and committer can differ: a patch author and the person who merged it are both recorded
-   GitPython gives you Python-level access to a local repository without shelling out to `git`
    -   `repo.iter_commits()` walks the commit graph from HEAD backward
    -   `commit.author.name` and `commit.author.email` identify the person who wrote the change
    -   `commit.stats.total` summarizes lines added and deleted across all files in that commit

## Measuring Contribution

-   Three common metrics: number of commits, lines added, and lines deleted
    -   These correlate strongly but not perfectly
    -   A contributor who adds 10,000 lines in one commit and one who makes 100 small fixes look very different by commit count but possibly similar by lines added
-   Commit count is the most common metric in MSR studies because it is cheap to compute and robust to whitespace-only changes
    -   Lines-added counts are inflated by code generation, vendored libraries, and bulk reformatting
    -   Deleting code also contributes; weighting insertions and deletions equally is a defensible choice that you should state explicitly

## Gini Coefficient and Lorenz Curve

-   The [%g gini_coefficient "Gini coefficient" %] is a single number measuring inequality in a distribution
    -   0 means perfect equality (every contributor has the same share)
    -   1 means one person does everything and everyone else does nothing
    -   For commit counts, values above 0.7 are common in open-source projects
-   The formula sorts values from smallest to largest and computes a weighted average of ranks
    -   It is equivalent to the area between the [%g lorenz_curve "Lorenz curve" %] and the line of perfect equality, doubled
    -   The Lorenz curve plots cumulative share of contributors on the x-axis against cumulative share of commits on the y-axis
-   Giger et al. used Gini to predict bug-prone files in Eclipse [%b Giger2011 %]
    -   Files where a single developer owned nearly all changes were more likely to contain bugs
    -   Ownership concentration is a measurable proxy for knowledge silos

## Hero Developers

-   Most open-source projects have one person — a [%g hero_developer "hero developer" %] — doing the majority of the work [%b Majumder2019 %]
    -   Typically more than 80% of commits come from roughly 20% of contributors
    -   The pattern holds across projects of very different sizes and ages
-   Hero developers create risk: if they stop contributing, the project loses most of its institutional knowledge
    -   They also create measurement problems: their commit style dominates any aggregate statistic you compute
-   Whether hero developers are a problem or just an efficient structure is a values question, not a statistical one
    -   Majumder et al. found that hero projects were not inherently lower quality, but they were more fragile

## Data Quality and Sampling

-   He et al. found that GitHub star counts are routinely inflated by bots and purchased services [%b He2024 %]
    -   A sample of "popular" projects selected by star count is not representative of real adoption
    -   Clean your sampling frame before you start mining: check for bot accounts, mirrored repos, and star-farming patterns
-   Merging contributor identities is harder than it looks
    -   The same developer may appear under different names, email addresses, or usernames across commits
    -   Name disambiguation is an active research problem; ignoring it inflates your contributor count

## Dirty Data in Version Control

-   Flint et al. found that at least 35% of MSR papers use time-based data without cleaning it [%b Flint2021 %]
    -   Git timestamps are set by the committing machine's clock, which may be wrong
    -   Commits can be back-dated, cherry-picked across branches with old timestamps, or imported from another VCS
    -   A commit dated before the repository was created is a strong signal of dirty data
-   Gold and Krinke argue that treating public Git data as ethically unconstrained is a mistake [%b Gold2020 %]
    -   Developers push code publicly to share software, not to participate in research
    -   Commit histories contain personal information: work hours, productivity patterns, professional relationships
    -   Mining that information without consent raises the same ethical questions as any other human subjects research

## Code

[%inc gini.py %]

## Check Understanding

<details markdown="1">
<summary markdown="1">What does a Gini coefficient of 0.85 mean for the distribution of commits in a project?</summary>

A Gini coefficient of 0.85 means the distribution of commits is highly unequal. In practice, a value that high usually means a very small fraction of contributors — perhaps one or two people — account for most of the commits, while many contributors have made only one or two. It does not tell you who those people are or whether the concentration is a good or bad thing, only that it exists. Compare it with a value near 0, where every contributor has committed roughly the same number of times.

</details>

<details markdown="1">
<summary markdown="1">The following function has a bug. What is wrong and how do you fix it?

```python
def gini(values):
    arr = np.sort(values)  # values is a Polars Series
    n = len(arr)
    index = np.arange(1, n + 1)
    return (2 * (index * arr).sum() / (n * arr.sum())) - (n + 1) / n
```
</summary>

`np.sort` works on NumPy arrays, but `values` here is a Polars Series. Passing a Polars Series to `np.sort` without converting it first may silently produce wrong results or raise a type error depending on the version. The fix is to convert explicitly before sorting:

```python
def gini(values):
    arr = np.sort(np.array(values, dtype=float))
    n = len(arr)
    index = np.arange(1, n + 1)
    return (2 * (index * arr).sum() / (n * arr.sum())) - (n + 1) / n
```

Adding `dtype=float` also guards against integer overflow when the values are large.

</details>

<details markdown="1">
<summary markdown="1">Flint et al. found that 35% of MSR papers use time-based data without cleaning it. What is one type of data-quality problem specific to Git timestamps?</summary>

Git timestamps are recorded by the committing machine's clock, which may be wrong. A developer who commits on a laptop with an incorrect system clock will produce commits timestamped in the past or future. Commits imported from another version control system (SVN, Mercurial) often carry the original repository's timestamps, which predate the Git repository's creation. Either problem breaks any analysis that uses commit order or time between commits as a variable.

</details>

<details markdown="1">
<summary markdown="1">Why does Gold and Krinke argue that public Git commit data does not automatically mean developers consented to being studied?</summary>

Developers make code public so that others can read and use it, not to participate in research. Consent to one use does not imply consent to all uses. Commit histories contain information that developers may not have intended to share as research data: work schedules, productivity patterns on specific days, and professional relationships between collaborators. Using that information in a study about individual behavior goes beyond what a typical developer would expect when pushing to a public repository, which is why Gold and Krinke argue for applying the same ethical standards used in human subjects research.

</details>

## Exercises

<div class="exercise" markdown="1">

### Hero Developer Fraction

Compute the top-contributor share (commits by the most active contributor divided by total commits) for each of the three projects in the pre-collected dataset. Report which project is most concentrated. Then write two sentences about what a software team relying on that project should consider before assuming continued maintenance: one sentence about the practical risk and one sentence about what evidence would increase or decrease your concern.

</div>

<div class="exercise" markdown="1">

### Lines Added vs. Commit Count

Compute the Gini coefficient for lines added rather than commit count for each of the three projects. Report whether the ranking of projects by inequality changes when you switch metrics. Write two sentences explaining why commit count and lines added might give different pictures of contribution concentration — consider what kinds of contributions each metric captures and what each one is blind to.

</div>

<div class="exercise" markdown="1">

### Sampling Without Star Counts

He et al. showed that GitHub star counts can be artificially inflated by bots and purchased services, which means star count is a poor primary filter for selecting representative open-source projects. Design a two-step sampling procedure that avoids relying on star count as the main selection criterion. Write four sentences describing your procedure: what proxy you would use instead of stars, how you would define your initial population, what a second filter would eliminate, and what residual bias your procedure still cannot remove.

</div>

<div class="exercise" markdown="1">

### Ethical Limits of Commit Mining

Gold and Krinke argue that mining commit histories raises ethical questions even when the data is publicly accessible. Identify two specific pieces of information that appear in a typical commit history that a developer might not expect to be used in research. For each piece of information, write one sentence describing a potential harm that could result from including it in a published study without consent.

</div>

<div class="exercise" markdown="1">

### Timestamp Cleaning

Flint et al. found that 35% of MSR papers use time-based data without cleaning it. In the pre-collected commit dataset, check for commits with timestamps before the project's first known public release (use 2006-01-01 for NumPy, 2007-06-01 for scikit-learn, and 2014-01-01 for shell-novice as approximate lower bounds) and for commits with timestamps after today's date. Report how many such commits you find in each project. Then write one sentence explaining one plausible mechanism that could produce a commit with a timestamp in the future.

</div>
