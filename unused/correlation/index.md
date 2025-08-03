---
draft: true
---

-   FIXME: introduction.

## How can we extract features from software?

-   Lines per file is interesting, but we probably care more about the content of those files
-   Can't use regular expressions for feature extraction
    -   Keywords like `for` and `while` can appear in strings
    -   And programs are inherently nested structures, which regexp can't handle
-   Parse the software and then extract features from the <span g="ast">abstract syntax tree</span> (AST)
-   Find a parser rather than writing one
    -   [`ast`][ast-py] is part of the standard Python library
    -   [`acorn`][acorn] is widely used for JavaScript, but using it requires us to write a little JavaScript
-   Analyze the same files as above
-   Look at the Python first
    -   Read a file as a whole (because that's what the parser wants)
    -   Split on newlines to count lines
        -   Strip off any trailing newlines, but don't strip leading blank lines
        -   Another arbitrary decision that needs to be documented to make work reproducible
    -   Use `ast.parse` to create a parse tree
    -   Then create a sub-class of `ast.NodeVisitor` to do something for each node in that tree
        -   Uses the the <span g="visitor_pattern">Visitor pattern</span>
        -   `NodeVisitor` has empty methods corresponding to each type of node
        -   We override the ones we care about to define actions at those nodes
        -   In this case, count how many are function definitions

```py
def handle(path, verbose):
    '''
    Analyze a single file.
    '''
    if verbose:
        print(path, file=sys.stderr)
    with open(path, 'r') as reader:
        try:
            data = reader.read()
            lines = len(data.rstrip().split('\n'))
            tree = ast.parse(data)
            analyzer = Analyzer()
            analyzer.visit(tree)
            result = (path, lines, analyzer.num_functions)
        except UnicodeDecodeError as e:
            result = (path, None, None)
        except SyntaxError as e:
            result = (path, lines, None)
        return result


class Analyzer(ast.NodeVisitor):
    '''
    Count the number of function nodes in a parse tree.
    '''

    def __init__(self):
        self.num_functions = 0


    def visit_FunctionDef(self, node):
        self.num_functions += 1
        self.generic_visit(node)
```
{: title="bin/py-func-count.py"}

-   Testing this on itself shows that method definitions also count as functions
    -   Yet another decision
-   Run it on the local Python installation to collect data

```sh
find /anaconda3/ -name '*.py' | bin/py-func-count.py --list > data/py-func-count.csv
```
{: display="none"}

-   What about JavaScript?
    -   `acorn`'s AST isn't as well documented as Python's
    -   But a helper library called `acorn-walk` works like Python's `NodeVisitor`

```js
  const data = fs.readFileSync(path, 'utf-8')
  const lines = data.trimEnd().split('\n').length

  const ast = acorn.parse(data, {
    ecmaVersion: 8
  })

  const state = {functions: 0}
  walk.simple(ast, {
    FunctionDeclaration: (node, state) => {
      state.functions += 1
    }
  }, null, state)
    
  return {
    path: path,
    lines: lines,
    functions: state.functions
  }
```
{: title="bin/js-func-count.js"}

-   Several things go wrong
    -   Have to add the `ecmaVersion` option to get anything to work
    -   Some of the things ending in `.js` in `node_modules` are directories, not files
    -   Some are modules (`acorn`'s error message helpfully tells us what to add to our parser options)
-   Most importantly, this code doesn't find any functions when we run it on some test files
-   So we experiment by parsing some files and printing the parse tree
    -   Empirical software engineers spend a lot of time reverse engineering data structures and data formats

```js
const fs = require('fs')
const acorn = require('acorn')

const data = fs.readFileSync(process.argv[2], 'utf-8')
const ast = acorn.parse(data, {
  locations: true,
  onComment: [],
  ecmaVersion: 8
})
console.log(JSON.stringify(ast, null, 2))
```
{: title="bin/js-test-parser.js"}

-   The input is a script from this website
    -   Uses modern <span g="fat_arrow_function">fat arrow</span> notation for defining functions

```js
const createToc = () => {
  const div = document.querySelector('div#toc')
  const nodes = Array.from(document.querySelectorAll('h2'))
        .filter(node => !node.classList.contains('lede'))
  if (! nodes.length) {
    div.classList.remove('dropdown-content')
    div.parentNode.classList.add('disabled')
  }
  else {
    const text = nodes
          .map(node => `<a href="#${node.id}"><span class="nowrap">${node.textContent}</span></a>`)
          .join('<br/>')
    div.innerHTML = text
  }
}
```
{: title="test/test.js"}

-   Output contains entries like this:

```js
"init": {
  "type": "ArrowFunctionExpression",
  "start": 47,
  "end": 526,
  ...
}
```
{: title="test/test.json"}

-   So we modify our data collection program to:
    1.  Count `FunctionExpression` and `ArrowFunctionExpression` as well as classical `FunctionDeclaration`
    2.  Check that things are actually files before opening them
        -   Report no lines or functions
    3.  Handle parse errors
        -   Report lines but no functions

```js
const countFile = (path) => {
  if (! fs.lstatSync(path).isFile()) {
    return {path: path, lines: null, functions: null}
  }

  const data = fs.readFileSync(path, 'utf-8')
  const lines = data.trimEnd().split('\n').length

  try {
    const ast = acorn.parse(data, {
      ecmaVersion: 8,
      sourceType: 'module'
    })

    const state = {functions: 0}
    walk.simple(ast, {
      FunctionDeclaration: (node, state) => {
        state.functions += 1
      },
      ArrowFunctionExpression: (node, state) => {
        state.functions += 1
      }
    }, null, state)
    
    return {
      path: path,
      lines: lines,
      functions: state.functions
    }
  } catch (err) {
    return {
      path: path,
      lines: lines,
      functions: null
    }
  }
}
```
{: title="bin/js-func-count.js"}

-   Run this on a local JavaScript project with:

```sh
find ~/blocks/node_modules/ -name '*.js' | node bin/js-func-count.js > data/js-func-count.csv
```

-   Now we have two CSV files with the same column headers
    -   So we can process them with the same scripts
-   Python has a reasonable distribution <span f="lines-per-func-python-all"></span>
    -   A lot of very short functions and a small number of very long ones (remember, Y axis has logarithmic scale)

{% include figure
   id="lines-per-func-python-all"
   cap="Lines per Function (Python)"
   alt="FIXME"
   title="Histogram with spike over Y equals 10,000 at X equals 0 and a smooth (possibly exponential) decline up to Y equals 10 at X in the low hundreds, after which there are jagged spikes at or below Y equals 5 up to X in the low thousands."
   fixme=true %}

-   JavaScript has a notch at x=0 <span f="lines-per-func-javascript-all"></span>

{% include figure
   id="lines-per-func-javascript-all"
   cap="Lines per Function (JavaScript / All)"
   alt="FIXME"
   title="Histogram with Y near 100 at X equals 0, immediately rising to Y around 2000 and then smooth (possibly exponential) decline to Y in the 20s at X above 100 with a low notch exactly at X equals 100."
   fixme=true %}

-   Take a closer look at the low end of the data
    -   A significant number of one-line functions

{% include figure
   id="lines-per-func-javascript-low"
   cap="Lines per Function (JavaScript / Low End)"
   alt="FIXME"
   title="Histogram with a spike of Y around 80 at X equals 0, dropping immediately to Y around 20 at X equals 1, climbing to Y around 1000 at X near 10, then declining jaggedly with occasional spikes."
   fixme=true %}

## How can we use one value to predict another?

-   Counting the number of lines in a file is easier than counting the number of functions
-   Can we use the number of lines to predict the number of functions?
    -   Better question: how well does the number of lines let us predict the number of functions?
-   This is a central issue in statistics: we can measure X, but what we really want to know is Y
-   <span g="covariance">Covariance</span> $$\sigma_{XY}$$ of $$X$$ and $$Y$$ is $$E((X - \mu_{X})(Y - \mu_{Y}))$$
    -   If $$X$$ and $$Y$$ are both above or below their means at the same time, $$\sigma_{XY}$$ will be positive
    -   If $$X$$ is above when $$Y$$ is below and vice versa, $$\sigma_{XY}$$ will be negative
    -   If there is no relation, $$\sigma_{XY}$$ will be zero
-   <span g="pearson_correlation_coefficient">Pearson's correlation coefficient</span> $$r_{XY}$$
    is covariance normalized by standard deviations
    -   $$r_{XY} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y}$$
    -   Always lies in $$[-1 \ldots 1]$$
-   What's the difference?
    -   Covariance tells us about the sign of the relationship between $$X$$ and $$Y$$,
        but its magnitude depends on the magnitude of the two variables
    -   Correlation coefficient is standardized
        so we can compare strength of relationship between different scenarios

```py
    # calculate covariance matrix for selected columns
    data = pd.read_csv(args.input)
    data = data[args.columns]
    corr = data.corr()
    print(args.title)
    print(corr)
```
{: title="bin/correlation.py"}
```sh
python bin/correlation.py --title "Python" --input data/py-func-count.csv Lines Functions
```
```txt
Python
             Lines  Functions
Lines      1.00000    0.80566
Functions  0.80566    1.00000
```
```sh
python bin/correlation.py --title "JavaScript" --input data/js-func-count.csv Lines Functions
```
```txt
JavaScript
              Lines  Functions
Lines      1.000000   0.727698
Functions  0.727698   1.000000
```

-   Conclusions:
    1.  Number of lines "explains" about 80% of the number of functions in Python.
    2.  Less strong a predictor for JavaScript, but 72% is still pretty good
-   Always check correlations with scatterplots

{% include figure
   id="py-lines-funcs"
   cap="Correlation Between Lines and Functions per File (Python)"
   alt="FIXME"
   title="A log-log plot with an empty upper triangle (showing that almost all cases have more lines than functions), some horizontal stripes showing files with many lines and only a small number of functions, and the rest of the data tightly bunched."
   fixme=true %}

{% include figure
   id="js-lines-funcs"
   cap="Correlation Between Lines and Functions per File (JavaScript)"
   alt="FIXME"
   title="A log-log plot with some points in the upper triangle (showing cases with one line and many functions, which is probably a result of minimization), some horizontal stripes showing files with many lines and only a small number of functions, and the rest of the data tightly bunched, but not as tightly as the Python case."
   fixme=true %}

-   By comparison, look at the lengths of functions and the lengths of their names
    -   "Do programmers give longer functions more meaningful names?"
-   Getting the lengths of functions from the Python AST involves a bit of work
-   Correlation between function name length and function length in lines is just above 0.01

```py
class Analyzer(ast.NodeVisitor):
    '''
    Count the number of function nodes in a parse tree.
    '''

    def __init__(self):
        self.functions = {}


    def visit_FunctionDef(self, node):
        last = max([self.line(x) for x in ast.walk(node)])
        num_lines = 1 + last - node.lineno
        self.functions[node.name] = num_lines
        self.generic_visit(node)


    def line(self, node):
        try:
            return node.lineno
        except AttributeError:
            return 0
```
{: title="bin/py-func-name-len.py"}
```txt
            Len     Lines
Len    1.000000  0.013593
Lines  0.013593  1.000000
```

{% include figure
   id="py-func-name-len"
   cap="Correlation Between Function Length and Function Name Length in Python"
   alt="FIXME"
   title="Log-log plot with essentially no relationship between X and Y axes."
   fixme=true %}

-   Harder to do this analysis for JavaScript
    -   Functions are often "declared" by assigning a function to a variable,
        which makes them more difficult to find in the AST
    -   Many anonymous callback functions,
        which makes the results less meaningful

## How strongly correlated are different measures of contribution?

-   Problem: how much do different people contribute to software projects?
-   Get data from Git repositories
-   Check analysis from <cite>Elbaum1998</cite> (cited in <cite>Bird2011</cite>)
    that number of changes and number of lines changed are strongly correlated

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
    -   Should be cited in any published work

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

-   This gives us:

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
    -   Took over 16 hours to get the histories of 5 scientific Python repositories
        on a 2.2GHz MacBook with 8Gbyte of RAM
-   Can we measure contributions in a faster way and get a good enough answer?
-   Try using `git blame`
    -   Labels each line with the identity of the last person to touch it
    -   Extract these with a regular expression for all the interesting files in a repository

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

-   Output looks like this:

```txt
email,lines
swast@google.com,317
jeff@reback.net,59544
emailformattr@gmail.com,8794
sinhrks@gmail.com,12876
josh@lambdafoundry.com,16
wesmckinn@gmail.com,16161
...
```

-   Try matching by email address

```py
def main():
    '''
    Main driver.
    '''
    left_pattern = sys.argv[1]
    right_pattern = sys.argv[2]
    print(f'stem,{left_pattern},both,{right_pattern}')
    for stem in sys.argv[3:]:
        left_file = left_pattern.replace('%', stem)
        right_file = right_pattern.replace('%', stem)

        left_data = pd.read_csv(left_file)
        left_addr = set(left_data.email)

        right_data = pd.read_csv(right_file)
        right_addr = set(right_data.email)

        left_only = left_addr - right_addr
        right_only = right_addr - left_addr
        both = left_addr & right_addr
        print(f'{stem},{len(left_only)},{len(both)},{len(right_only)}')
```
{: title="bin/match-addresses.py"}

| stem                    | blame | both | history |
| :---------------------- | ----: | ---: | ------: |
| git-novice              | 43    | 36   | 251     |
| python-novice-gapminder | 0     | 131  | 54      |
| r-novice-gapminder      | 2     | 169  | 51      |
| shell-novice            | 1     | 192  | 135     |
| sql-novice-survey       | 1     | 78   | 48      |
| numpy                   | 15    | 829  | 254     |
| pandas                  | 0     | 1622 | 387     |
| scikit-image            | 1     | 381  | 84      |
| scikit-learn            | 6     | 1478 | 343     |
| scipy                   | 5     | 845  | 199     |

-   Lots of contributors don't show up in the final list of lines
    -   I.e., they added something at some point, but it hasn't survived
-   There's another problem
    -   Use a small program to add insertions minus deletions

```py
def main():
    '''
    Main driver.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=str,
                        help='output file (default stdout)')
    parser.add_argument('files', type=str, nargs='*')
    args = parser.parse_args()

    writer = open(args.output, 'w') if args.output else sys.stdout
    writer = csv.writer(writer, lineterminator='\n')
    writer.writerow(['filename', 'total'])

    for filename in args.files:
        df = pd.read_csv(filename)
        total = df.insertions.sum() - df.deletions.sum()
        writer.writerow([filename, total])
```
{: title="bin/insert-minus-delete.py"}

| filename                                       | total   |
| :--------------------------------------------- | ------: |
| data/commits-lines-git-novice.csv              | 54680   |
| data/commits-lines-python-novice-gapminder.csv | 96446   |
| data/commits-lines-r-novice-gapminder.csv      | 109252  |
| data/commits-lines-shell-novice.csv            | 206774  |
| data/commits-lines-sql-novice-survey.csv       | 63844   |
| data/commits-lines-numpy.csv                   | 771834  |
| data/commits-lines-pandas.csv                  | 1032206 |
| data/commits-lines-scikit-image.csv            | 399427  |
| data/commits-lines-scikit-learn.csv            | 1808751 |
| data/commits-lines-scipy.csv                   | -328141 |

-   Bears little relation to the total number of lines in the repository
    -   Leave it as an exercise to measure *how* little
-   Our simple counting method doesn't track renames or file splits/merges
-   Doing that is hard (FIXME: pointers)
