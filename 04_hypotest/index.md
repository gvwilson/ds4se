# Hypothesis Testing

-   Problem: how to estimate development effort or likely fault rates
    -   Intuitively seems like this should depend on some measurable properties of the software
    -   Lines of code (LoC) is easy to count but seems like a pretty coarse measure
    -   How can we count other things?
    -   How can we tell whether a hypothesis is true or not?
-   Steps are:
    -   Collect data
    -   Formulate testable hypotheses
    -   Calculate likelihood of getting the answer we observe
    -   Decide whether that answer is so unlikely that we probably didn't get it by chance

## How can we get data on file sizes?

-   Start by asking whether Python and JavaScript files are different,
    i.e., how our measurements depend on source language
-   Parsing arguments and writing CSV is normal by now
-   Use `os.walk` to recurse through directories
-   After the first failure because of bad <span g="character_encoding">character encoding</span>, add error handling
-   Then capture `stderr` to a log file for later inspection
-   Then realize that storing (filename, length, count):
    1.  Is too big for GitHub unless we compress it
    2.  Contains a lot of redundancy
-   Instead of compressing the file, create two files:
    -   One stores (filename, unique ID)
    -   The other stores (unique ID, length, count)
    -   So the largest field (filename) only appears once
    -   And gives us a natural way to record files we couldn't read because of character encoding issues (`NA` for file ID)
-   This technique is also useful when storing <span g="pid">personal identifying information</span> (PID)
    -   Shareable data is keyed
    -   Personal data is not shared
    -   Beware of <span g="de_anonymization">de-anonymization</span>

-   Main driver is straightforward

```py
def main():
    '''
    Main driver.
    '''
    args = parse_args()
    counts = lengths(args)
    report_filenames(args.output, counts)
    report_counts(args.output, counts)
```
{: title="bin/file-size.py"}

-   Parse arguments
    -   Root directory
    -   Filename extension
    -   Stem of output files (because there are two)
    -   E.g., processing `data/python` will produce `data/python-filenames.csv` and `data/python-counts.csv`

```py
def parse_args():
    '''
    Handle command-line arguments.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=str, help='root directory')
    parser.add_argument('--ext', type=str, help='extension')
    parser.add_argument('--output', type=str, help='stem of output files')
    return parser.parse_args()
```
{: title="bin/file-size.py"}

-   Find files and record lengths
    -   A dictionary mapping filenames to `Counter` objects
    -   Or to `None` if the file couldn't be read

```py
def lengths(args):
    '''
    Find files and count line lengths.
    '''
    counts = {}
    for (curr_dir, sub_dirs, files) in os.walk(args.root):
        for filename in [x for x in files if x.endswith(args.ext)]:
            path = os.path.join(curr_dir, filename)
            with open(path, 'r') as reader:
                try:
                    counts[path] = Counter()
                    for x in reader.readlines():
                        counts[path][len(x)] += 1
                except Exception as e:
                     print(f'Failed to read {path}: {e}',
                           file=sys.stderr)
                     counts[path] = None
    return counts
```
{: title="bin/file-size.py"}

-   Write the filenames or `NA`
    -   Uses `X if test else Y`, which is frequently confusing

```py
def report_filenames(output_stem, counts):
    '''
    Report filename-to-ID as CSV with 'NA' for errored files.
    '''
    with open(f'{output_stem}-filenames.csv', 'w') as writer:
        writer = csv.writer(writer, lineterminator='\n')
        writer.writerow(['Filename', 'FileID'])
        for (file_id, filename) in enumerate(sorted(counts.keys())):
            writer.writerow([filename, file_id if counts[filename] else 'NA'])
```
{: title="bin/file-size.py"}

-   And the counts where available

```py
def report_counts(output_stem, counts):
    '''
    Report file ID-to-count as CSV for non-errored files.
    '''
    with open(f'{output_stem}-counts.csv', 'w') as writer:
        writer = csv.writer(writer, lineterminator='\n')
        writer.writerow(['FileID', 'Length', 'Count'])
        for (file_id, filename) in enumerate(sorted(counts.keys())):
            if counts[filename]:
                for (length, freq) in counts[filename].most_common():
                    writer.writerow([file_id, length, freq])
```
{: title="bin/file-size.py"}

-   `python bin/file-size.py --root /anaconda3 --ext .py --output data/python`
-   Get some errors
    -   Store in `log/file-size-python-errors.txt` for later reference

```txt
Failed to read /anaconda3/pkgs/xlwt-1.3.0-py37_0/lib/python3.7/site-packages/xlwt/BIFFRecords.py: 'utf-8' codec can't decode byte 0x93 in position 68384: invalid start byte
Failed to read /anaconda3/pkgs/xlwt-1.3.0-py37_0/lib/python3.7/site-packages/xlwt/UnicodeUtils.py: 'utf-8' codec can't decode byte 0xb7 in position 1950: invalid start byte
Failed to read /anaconda3/pkgs/pylint-2.3.1-py37_0/lib/python3.7/site-packages/pylint/test/functional/implicit_str_concat_in_sequence_latin1.py: 'utf-8' codec can't decode byte 0xe9 in position 96: invalid continuation byte
Failed to read /anaconda3/pkgs/joblib-0.13.2-py37_0/lib/python3.7/site-packages/joblib/test/test_func_inspect_special_encoding.py: 'utf-8' codec can't decode byte 0xa4 in position 64: invalid start byte
...
```
{: title="log/file-size-python-errors.txt"}

-   Also run `python bin/file-sizes.py ~/blocks/node_modules`
    -   `blocks` is a JavaScript project we just have to have lying around
    -   `node_modules` is where the project's JavaScript packages are stored
-   Create scatter plots of to show frequency of line lengths
-   Add a <span g="pattern_rule">pattern rule</span> to `Snakefile`
    -   Assign the languages and kinds of figures to variables
    -   Fill in all combinations of those variables with `expand`
    -   Create a target called `all` that depends on the expanded list of files

```python
LANGS = ['javascript', 'python']
KINDS = ['all', 'trimmed']

rule all:
    input:
        expand('figures/{lang}-counts-{kind}.svg', lang=LANGS, kind=KINDS)

rule count_all:
    input:
        'data/{lang}-counts.csv'
    output:
        'figures/{lang}-counts-all.svg'
    shell:
        'python bin/length-frequency-plot.py --data {input} --fig {output} --logx'

rule count_trimmed:
    input:
        'data/{lang}-counts.csv'
    output:
        'figures/{lang}-counts-trimmed.svg'
    shell:
        'python bin/length-frequency-plot.py --data {input} --fig {output} --low 2 --high 200'
```
{: title="Snakefile"}

-   Create log-log histograms for frequency of line lengths
    in JavaScript <span f="javascript-counts-all"/>
    and Python <span f="python-counts-all"/>

{% include figure
   id="javascript-counts-all"
   img="figures/javascript-counts-all.svg"
   cap="Frequency of Line Lengths (JavaScript, All)"
   alt="FIXME"
   title="Log-log scatter plot with a point at Y equals 200,000 and X equals 1 and then a noticeable decline for X above 80." %}

{% include figure
   id="python-counts-all"
   img="figures/python-counts-all.svg"
   cap="Frequency of Line Lengths (Python, All)"
   alt="FIXME"
   title="Log-log scatter plot with a point at Y equals 2,000,000 at X equals 1 and then a sharp decline for X above 80." %}

-   Exclude lines of length 1
    -   These only contain the newline character, i.e., they're empty
-   Exclude lines longer than 200 characters
    -   Possibly a character encoding issue
    -   Or <span g="minification">minification</span> of JavaScript

{% include figure
   id="javascript-counts-trimmed"
   img="figures/javascript-counts-trimmed.svg"
   cap="Frequency of Line Lengths (JavaScript, Trimmed)"
   alt="FIXME"
   title="Log-linear plot showing Y approximately 20,000 for X up to 50 and steady decline thereafter." %}

{% include figure
   id="python-counts-trimmed"
   img="figures/python-counts-trimmed.svg"
   cap="Frequency of Line Lengths (Python, Trimmed)"
   alt="FIXME"
   title="Log-linear plot showing Y approximately 20,000 for X below 10, Y between 100,000 and 200,000 for X up to 80, and a very sharp decline thereafter." %}

-   These curves look different, but are they?

## How can we tell if two populations are different?

-   <span g="null_hypothesis">Null hypothesis</span>: there is no significant difference between these curves
-   <span g="alternative_hypothesis">Alternative hypothesis</span>: there is a significant difference between these curves
-   Reject the null hypothesis if the probability of getting this data *if the null hypothesis is true*
    is less than a chosen probability called a <span g="p_value">\\(p\\) value</span>
    -   Typically use \\(p = 0.05\\), i.e., less than 1 chance in 20 of getting the data if there isn't actually a difference
    -   The lower the \\(p\\) value, the higher our confidence

<div class="callout" markdown="1">

### Kick the ball then move goal

\\(p\\) values can be mis-used in several ways.
The most obvious is to choose a \\(p\\) value after the fact in order to get a significant result:
if you ever see reports that mix several different \\(p\\) values or use odd numbers like 0.073,
this is probably what's going on.

The second form of abuse, called <span g="p_hacking">*p* hacking</span>,
is to re-analyze the data over and over until a "significant" result emerges.
Consider: if the odds of getting a false positive for one analysis are 0.05,
then the odds of getting a true negative are 0.95.
The odds of getting two true negatives in a row are therefore \\(0.95^2\\),
which is 0.9025.
If we keep going, the odds of none of our analyses meeting this threshold are 50/50
when we do 14 analyses.
One sign that people are *p* hacking is that they find niche results like,
"This treatment was effective for left-handed non-smokers between the ages of 45 and 55."
The best way to safeguard against *p* hacking is to <span g="pre_registration">pre-register</span> studies,
i.e.,
to declare before collecting data what analyses are going to be done and how.

</div>

-   But how do we measure the likelihood?
-   One approach is to use simulation
    -   Combine data sets
    -   Split into two pieces at random (where each piece is the same size as one of the originals)
    -   See how far apart the means are
    -   Repeat a few thousand times
    -   See how often we get the difference we actually see
    -   Decide if we believe the difference is likely

```py
#!/usr/bin/env python

import sys
import argparse
import numpy as np
import pandas as pd


def main():
    '''
    Sample two datasets to calculate odds of means being distant.
    '''
    # ...parse arguments...
    # ...read data and calculate actual means and difference...
    # ...repeatedly sample and calculate difference...
    # ...report...
```
{: title="bin/simulate.py"}

-   Arguments are pretty simple
    -   Two files
    -   Cut the low and high values as we did for plotting
    -   Number of trials
    -   <span g="rng_seed">Seed</span> for <span g="rng">random number generator</span> so we can reproduce results

```py
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--left', type=str, help='first dataset')
    parser.add_argument('--right', type=str, help='second dataset')
    parser.add_argument('--low', type=int, help='lower limit')
    parser.add_argument('--high', type=int, help='upper limit')
    parser.add_argument('--trials', type=int, help='number of trials (>0)')
    parser.add_argument('--seed', type=int, help='RNG seed')
    args = parser.parse_args()
    np.random.seed(args.seed)
```
{: title="bin/simulate.py"}

-   Read the data and calculate actual statistics

```py
    # read data and calculate actual means and difference
    data_left = read_data(args.left, args.low, args.high)
    data_right = read_data(args.right, args.low, args.high)
    mean_left = data_left.mean()
    mean_right = data_right.mean()
    actual_diff = mean_left - mean_right
```
{: title="bin/simulate.py"}

-   And:

```py
def read_data(filename, low, high):
    '''
    Read data and remove lines of length 1 and very long lines.
    '''
    data = pd.read_csv(filename)
    if (high != None):
        data = data[data.Length <= high]
    if (low != None):
        data = data[data.Length >= low]
    return data.Length.repeat(repeats=data.Count)
```
{: title="bin/simulate.py"}

-   For each simulation:
    -   Shuffle the index
    -   Cut the data in two
    -   Calculate means for the sections
    -   Record difference in the means
-   Afterward:
    -   Calculate the fraction of differences that are less than or equal to the actual difference
    -   For comparison, also report the average difference in the means

```py
    # repeatedly sample and calculate difference
    combined = data_left.append(data_right).reset_index(drop=True)
    split = len(data_left)
    sample_diffs = []
    for t in range(args.trials):
        shuffle = np.random.permutation(len(combined))
        sample_left = combined[shuffle[:split]]
        sample_right = combined[shuffle[split:]]
        sample_diffs.append(sample_left.mean() - sample_right.mean())

    sample_diff_mean = sum(sample_diffs) / args.trials
    success_frac = sum([x <= actual_diff for x in sample_diffs]) / args.trials
```
{: title="bin/simulate.py"}

-   Write results as <span g="yaml">YAML</span>
    -   A long two-column CSV with (title, value) pairs would work
    -   As would a wide CSV with one row of titles and one row of values
    -   Either way, must write parameter values to ensure reproducibility

```py
    # report
    print(f'parameters:')
    print(f'- left: "{args.left}"')
    print(f'- right: "{args.right}"')
    print(f'- low: {"null" if (args.low is None) else args.low}')
    print(f'- high: {"null" if (args.high is None) else args.high}')
    print(f'- trials: {args.trials}')
    print(f'- seed: {args.seed}')
    print(f'results:')
    print(f'- mean_left: {mean_left}')
    print(f'- mean_right: {mean_right}')
    print(f'- actual_diff: {actual_diff}')
    print(f'- sample_diff: {sample_diff_mean}')
    print(f'- successes: {success_frac}')
```
{: title="bin/simulate.py"}

## How can we test our approach?

-   We're showing completed working code, but we didn't get it right the first time
-   Create two "populations" and see if we get a plausible answer
    -   `[1, 1]` vs. `[10, 10]`

```sh
python bin/simulate.py --left test/test-a.csv --right test/test-b.csv --trials 10000 --seed 1234567
```
```txt
parameters:
- left: "test/test-a.csv"
- right: "test/test-b.csv"
- low: null
- high: null
- trials: 10000
- seed: 1234567
results:
- mean_left: 1.0
- mean_right: 10.0
- actual_diff: -9.0
- sample_diff: -0.0126
- successes: 0.1661
```

-   Is that right?
    -   8/24 permutations of the four values are a "perfect split"
    -   But only half of those have the low values in the lower half
    -   So we expect 4/24 successes, which is 0.1666... and we actually got 0.1661
    -   Our simulation reports that the expected difference is 0.0 and the simulated difference is -0.0126
    -   Seems to be doing what we want
-   We should test with unequal counts and numbers of samples
    -   Left as an exercise
-   And note that this doesn't test if the means are *different*, only if the first is less than the second
    -   A <span g="one_sided_test">one-sided test</span>
    -   If this says "yes" and we reverse the order of the datasets, the answer will be "no"
    -   Convert this into a <span g="two_sided_test">two-sided test</span> in the exercises

```sh
python bin/simulate.py --left data/javascript-counts.csv --right data/python-counts.csv --trials 5000 --seed 57622
```
```txt
parameters:
- left: "data/javascript-counts.csv"
- right: "data/python-counts.csv"
- low: null
- high: null
- trials: 5000
- seed: 57622
results:
- mean_left: 38.168300030969725
- mean_right: 36.41329390723824
- actual_diff: 1.7550061237314836
- sample_diff: 0.00398256511711528
- successes: 1.0
```

-   None of the 5000 random trials had a difference as big as what we actually see
-   So it seems pretty certain that the difference is more than just chance
-   But it takes about two hours to run 5000 simulations on our real data
    -   We should add a `--verbose` flag to report progress
    -   Or print the stats every N iterations so we can check <span g="convergence">convergence</span> interactively
        and decide when to cut things off
-   And we should find a better way to answer the question
    -   Take less time
    -   Tell us how confident we can be in the answer
    -   Because right now 5000 is a <span g="magic_number">magic number</span>
