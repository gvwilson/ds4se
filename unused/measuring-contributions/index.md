---
draft: true
---

-   Problem: how much do different people contribute to software projects?
-   <cite>Majumder2019</cite> reports that most projects have <span g="hero_developer">hero developers</span>
    and that these developers create fewer bugs than other contributors
-   Get data from Git repositories
-   Check analysis from <cite>Elbaum1998</cite> cited in <cite>Bird2011</cite>
    that number of changes and number of lines changed are strongly correlated

## Where can we get data?

-   Use [GitPython][gitpython]
-   Need to know a bit about Git's storage format
    -   Every unique piece of content is stored in a <span g="blob">blob</span>
    -   A tree can contain blobs or trees
    -   A commit refers to a set of trees

```py
#!/usr/bin/env python

import sys
import time
from collections import Counter
from git import Repo


REMOTE = '''\
  - name: "{remote}"
    url: "{remote.url}"\
'''

BRANCH = '''\
  - name: "{branch}"
    hash: "{branch.commit}"
    author: "{branch.commit.author}"
    committer: "{branch.commit.committer}"
    committed: "{branch.commit.committed_datetime}"\
'''

COMMIT='''\
  - hash: "{hash}"
    author: "{author}"
    committed: {time}"
    blob: {blob}
    tree: {tree}\
'''

TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'


def main():
    '''
    Show a few things about a repository.
    '''
    repo = Repo(sys.argv[1])

    print('- remotes:')
    for remote in repo.remotes:
        print(REMOTE.format(remote=remote))

    print('- branches:')
    for branch in repo.heads:
        print(BRANCH.format(branch=branch))

    print('- master_commits:')
    for commit in repo.iter_commits('master'):
        info = commit_info(commit)
        print(COMMIT.format(hash=str(commit),
                            author=commit.author.name,
                            time=fmt_time(commit.committed_date),
                            blob=info['blob'],
                            tree=info['tree']))


def fmt_time(t):
    return time.strftime(TIME_FORMAT, time.gmtime(t))


def commit_info(commit):
    c = Counter()
    for item in commit.tree.traverse():
        c[item.type] += 1
    return c


if __name__ == '__main__':
    main()
```
{: title="bin/inspect-repo.py"}
```sh
python bin/inspect-repo.py ~/js4ds
```
```txt
- remotes:
  - name: "origin"
    url: "git@github.com:software-tools-in-javascript/js4ds.git"
- branches:
  - name: "109-minimal"
    hash: "d3bf9a70fe7ff1a73829ad4f5f95d751559f658c"
    author: "Greg Wilson"
    committer: "Greg Wilson"
    committed: "2019-11-10 19:22:02-05:00"
  - name: "images"
    hash: "42a0543544bbe6b56503dd45d7d87a5c765d3cb4"
    author: "Greg Wilson"
    committer: "Greg Wilson"
    committed: "2019-09-26 09:41:50-04:00"
  - name: "master"
    hash: "74498d9eda25e97aa6e2d691c7f8e2d3b4cd5885"
    author: "Greg Wilson"
    committer: "Greg Wilson"
    committed: "2019-11-15 10:04:50-05:00"
- master_commits:
  - hash: "74498d9eda25e97aa6e2d691c7f8e2d3b4cd5885"
    author: "Greg Wilson"
    committed: 2019-11-15T15:04:50"
    blob: 572
    tree: 46
  ...
  - hash: "2f3476b3eba26a86cb19378bf7f99e015fdbbd71"
    author: "Toby Hodges"
    committed: 2019-11-10T19:43:59"
    blob: 536
    tree: 45
  ...
  - hash: "030cdb7efb24a2fdf2dbb1f603ba2178ba6918a8"
    author: "Maya Gans"
    committed: 2019-11-09T17:29:45"
    blob: 536
    tree: 45
  ...
```

-   The GitPython tutorial is a bit overwhelming
    -   But [this code][harrer-gitpython] is a big help
    -   And again, should be cited or credited in any work

```py
TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
DETAILS = 'insertions deletions lines'.split()
TITLES = 'branch email timestamp path'.split() + DETAILS


def main():
    # ...parse arguments...
    # ...write CSV header...

    repo = Repo(args.repo)
    for commit in repo.iter_commits(args.branch):
        for path in commit.stats.files:
            info = [args.branch, commit.author.email, fmt_time(commit.authored_date), path]
            details = [commit.stats.files[path][k] for k in DETAILS]
            writer.writerow(info + details)
```
{: title="bin/get-file-stats.py"}

-   Works:

```txt
branch,hash,email,timestamp,path,insertions,deletions,lines
master,08eb19...,juan.nunez-iglesias@monash.edu,2019-12-21T01:50:22,skimage/transform/hough_transform.py,84,8,92
master,08eb19...,juan.nunez-iglesias@monash.edu,2019-12-21T01:50:22,skimage/transform/tests/test_hough_transform.py,85,2,87
master,54ea55...,xwu@enthought.com,2019-12-20T16:04:12,skimage/transform/hough_transform.py,1,1,2
master,827ade...,juan.nunez-iglesias@monash.edu,2019-12-19T21:00:19,doc/source/themes/scikit-image/search.html,3,1,4
master,141801...,xwu@enthought.com,2019-12-19T16:24:27,skimage/transform/hough_transform.py,7,5,12
master,141801...,xwu@enthought.com,2019-12-19T16:24:27,skimage/transform/tests/test_hough_transform.py,16,4,20
master,b686bc...,olebole@debian.org,2019-12-19T10:11:14,doc/source/themes/scikit-image/search.html,3,1,4
master,1b6b2f...,xwu@enthought.com,2019-12-19T06:40:00,skimage/transform/hough_transform.py,3,0,3
...
```

-   But it's very slow
    -   Took over 16 hours to get the histories of 5 scientific Python repositories on a 2.2GHz MacBook with 8Gbyte of RAM

## How can we measure fairness of contributions?

-   Use the <span g="gini_coefficient">Gini coefficient</span>
    -   Ratio of the difference between the area under the actual <span g="lorenz_curve">Lorenz curve</span> and equality
    -   Perfect equality is a coefficient of 0
    -   One person has everything is a coefficient of 1
-   Internet search turns up [this code][guest-gini]
    -   Which should be credited in every publication that uses it
    -   And should have the magic number 0.000001 adjusted

```py
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

```py
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

```py
EMAIL_PAT = re.compile(r'^.*?<(.+?)>')
EXCLUDE_DIR = '.git .jekyll-cache .jekyll-metadata'.split()
EXCLUDE_SUFFIX = '.eps .ico .jpg .pdf .png .xlsx'.split()


def main():
    # ...parse arguments...

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

    # ...write counts as CSV...
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

```py
import pandas as pd
df = pd.read_csv('data/commits-lines-scipy.csv')
df.insertions.sum()
```
```txt
5733276
```
```py
df.deletions.sum()
```
```txt
6061417
```

-   It's unlikely that the developers have deleted more than 32,000 lines more than they've written...
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
-   Use <span g="pearson_correlation_coefficient">Pearson correlation coefficient</span> $$r$$
    and <span g="spearmans_rank_correlation">Spearman's rank correlation</span> $$\rho$$

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

{% include figure
   id="correlation"
   cap="Pearson and Spearman Correlations for Commits and Final Lines"
   alt="FIXME"
   title="Scatter plot showing weak to moderate positive correlation for the two correlation coefficients for everything except the git-novice lesson, which has a moderate positive Pearson correlation and a moderate negative Spearman correlation."
   fixme=true %}
