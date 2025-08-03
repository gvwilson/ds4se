## How can we measure fairness of contributions? {#s:gini}

-   Use the [Gini coefficient][gini-coefficient]
    -   Ratio of the difference between the area under the actual [Lorenz curve][lorenz-curve] and equality
    -   Perfect equality is a coefficient of 0
    -   One person has everything is a coefficient of 1
-   Internet search turns up [this code][guest-gini]
    -   Which should be credited in every publication that uses it
    -   And should have the magic number 0.000001 adjusted

```python
# Taken from <https://github.com/oliviaguest/gini>

def gini(array):
    """
    Calculate the Gini coefficient of a numpy array.
    """
    # based on bottom eq: http://www.statsdirect.com/help/content/image/stat0206_wmf.gif
    # from: http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    if np.amin(array) < 0:
        array -= np.amin(array) # values cannot be negative
    array += 0.0000001 # values cannot be 0
    array = np.sort(array) # values must be sorted
    index = np.arange(1, array.shape[0] + 1) # index per array element
    n = array.shape[0] # number of array elements
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array))) # Gini coefficient
```
{: title="bin/util.py"}

-   Add code to calculate:
    -   Number of commits per email
    -   Insertions minus deletions per email (i.e., lines added)

```python
    writer.writerow(['filename', 'gini_commits', 'gini_lines'])
    for filename in args.files:
        data = pd.read_csv(filename)
        data['lines'] = data['insertions'] - data['deletions']
        commits = data[['hash', 'email']]\
            .drop_duplicates()\
            .groupby('email')\
            .email.count()
        lines = data.groupby('email')\
                    .lines.sum()
        writer.writerow([filename, gini(commits), gini(lines)])
```
{: title="bin/commits-lines.py"}

| filename | gini_commits | gini_lines |
| :------- | -----------: | ---------: |
| data/commits-lines-git-novice.csv | 0.7866 | 0.0306 |
| data/commits-lines-python-novice-gapminder.csv | 0.8249 | 0.0981 |
| data/commits-lines-r-novice-gapminder.csv | 0.7898 | 0.0298 |
| data/commits-lines-shell-novice.csv | 0.7955 | 0.0362 |
| data/commits-lines-sql-novice-survey.csv | 0.8100 | 0.0462 |
| data/commits-lines-numpy.csv | 0.9097 | 0.0104 |
| data/commits-lines-pandas.csv | 0.8742 | 0.0306 |
| data/commits-lines-scikit-image.csv | 0.8547 | 0.2495 |
| data/commits-lines-scikit-learn.csv | 0.8836 | 0.0049 |
| data/commits-lines-scipy.csv | 0.8821 | 0.0047 |

-   Numbers are unexpectedly consistent within each measure
-   But the differences between the measures are also unexpected
-   Try measuring in a different way: `git blame`

```python
EMAIL_PAT = re.compile(r'^.*?<(.+?)>')
EXCLUDE_DIR = '.git .jekyll-cache .jekyll-metadata'.split()
EXCLUDE_SUFFIX = '.eps .ico .jpg .pdf .png .xlsx'.split()


def main():
    # …parse arguments…

    count = Counter()
    for root, dirs, files in os.walk(args.repo):
        for path in [os.path.join(root, f) for f in files]:
            if not include(path):
                continue
            if args.verbose:
                print(path, file=sys.stderr)
            try:
                cmd = f'git -C {args.repo} blame -e {path}'
                lines = os.popen(cmd).readlines()
                emails = [EMAIL_PAT.search(x).group(1) for x in lines]
                for e in emails:
                    count[e] += 1
            except Exception as e:
                if args.verbose:
                    print(f'error in {path}: {e}', file=sys.stderr)

    # …write counts as CSV…
```
{: title="bin/get-blame.py"}

| filename | gini_blame |
| :------- | -----------: |
| data/blame-git-novice.csv | 0.9157 |
| data/blame-python-novice-gapminder.csv | 0.9272 |
| data/blame-r-novice-gapminder.csv | 0.9321 |
| data/blame-shell-novice.csv | 0.9655 |
| data/blame-sql-novice-survey.csv | 0.9157 |
| data/blame-numpy.csv | 0.9624 |
| data/blame-pandas.csv | 0.9443 |
| data/blame-scikit-image.csv | 0.8673 |
| data/blame-scikit-learn.csv | 0.9162 |
| data/blame-scipy.csv | 0.9464 |

-   Much closer to Gini coefficient of commits
-   Very different from coefficient obtained from counting insertions - deletions
-   The latter measure is even more suspicious when we do a spot check:

```python
import pandas as pd
df = pd.read_csv('data/commits-lines-scipy.csv')
df.insertions.sum()
```
```text
5733276
```
```python
df.deletions.sum()
```
```text
6061417
```

-   It's unlikely that the developers have deleted more than 32,000 lines more than they've written…
-   Use a small program to check the others

| filename | total |
| :------- | ----: |
| data/commits-lines-git-novice.csv | 54680 |
| data/commits-lines-python-novice-gapminder.csv | 96446 |
| data/commits-lines-r-novice-gapminder.csv | 109252 |
| data/commits-lines-shell-novice.csv | 206774 |
| data/commits-lines-sql-novice-survey.csv | 63844 |
| data/commits-lines-numpy.csv | 771834 |
| data/commits-lines-pandas.csv | 1032206 |
| data/commits-lines-scikit-image.csv | 399427 |
| data/commits-lines-scikit-learn.csv | 1808751 |
| data/commits-lines-scipy.csv | -328141 |

-   Problem is that our simple counting method doesn't track renames or file splits/merges
-   Doing that is hard, so for the moment we will look at how well line-by-line credit and number of commits match up
-   Use [Pearson correlation coefficient][pearson-correlation-coefficient] $r$
    and [Spearman's rank correlation][spearmans-rank-correlation] $\rho$

| stem | pearson | spearman |
| :--- | ------: | -------: |
| git-novice | 0.3572 | -0.2618 |
| python-novice-gapminder | 0.2018 | 0.2569 |
| r-novice-gapminder | 0.5725 | 0.5342 |
| shell-novice | 0.4187 | 0.3468 |
| sql-novice-survey | 0.2921 | 0.2248 |
| numpy | 0.6003 | 0.4140 |
| pandas | 0.5810 | 0.4752 |
| scikit-image | 0.6206 | 0.5822 |
| scikit-learn | 0.5853 | 0.3980 |
| scipy | 0.6565 | 0.4850 |

{% include figure.html
   key="correlation"
   caption="Pearson and Spearman Correlations for Commits and Final Lines"
   explain="Scatter plot showing weak to moderate positive correlation for the two correlation coefficients for everything except the git-novice lesson, which has a moderate positive Pearson correlation and a moderate negative Spearman correlation." %}

## Exercises {#s:ex}

FIXME: exercises

1.  Modify Gini coefficient calculation to replace the magic number 0.000001 with something adaptive.
