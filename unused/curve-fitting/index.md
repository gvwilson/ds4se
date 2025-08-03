---
draft: true
---

-   FIXME: Look at mail arrival times

## How can we get data?

-   Use a script to pull `Date:` fields out of mail files on the author's Mac

```sh
python mailbox.py --root Library/Mail/ --output timestamps.csv
```
```txt
12397 bad files / 271846 files
```

-   Bad files are character encoding problems
    -   4.5% of files (!)

-   Calculate inter-message times by shifting rows one place and subtracting
    -   Of course, dates and times are never that easy

```py
    data = pd.read_csv(args.input)
    data.Timestamp = pd.to_datetime(data.Timestamp, utc=True)
    data = data.sort_values('Timestamp')
    data['Shift'] = data.Timestamp.shift(periods=1)
    data = data.dropna()
    data['Date'] = data.Timestamp.dt.date
    data['Interval'] = data.Timestamp.sub(data.Shift)
    data['Interval'] = data.Interval.dt.total_seconds().round(decimals=1)
```
{: title="bin/calculate-intervals.py"}

-   Result is dates and intervals in seconds

```txt
Date,Interval
2010-09-08,3551.0
2010-09-08,45709.0
2010-09-08,2936.0
2010-09-08,127.0
2010-09-08,943.0
...
```
{: title="results/raw-intervals.csv"}

-   Histogram of all arrival intervals <span f="raw-view-all"></span>

{% include figure
   id="raw-view-all"
   cap="Frequency of Arrival Intervals (All)"
   alt="FIXME"
   title="Histogram from X equals 0 to X equals 10 million with almost all values in a spike at X equals 0 going above Y equals 200,000."
   fixme=true %}

-   Largest value is over 90 days
    -   More likely to be a gap in record keeping than anything else
-   Use `bin/raw-view.py` to re-plot
    with intervals of a week or less <span f="raw-view-one-week"></span>
    and eight hours or less <span f="raw-view-eight-hours"></span>

{% include figure
   id="raw-view-one-week"
   cap="Frequency of Arrival Intervals (7 Days or Less)"
   alt="FIXME"
   title="Histogram from X equals 0 to X equals 600,000 (i.e., seconds per week) with almost all values in a spike at X equals 0 going above Y equals 200,000."
   fixme=true %}

{% include figure
   id="raw-view-eight-hours"
   cap="Frequency of Arrival Intervals (8 Hours or Less)"
   alt="FIXME"
   title="Histogram from X equals 0 to X equals 30,000 (i.e., seconds in 8 hours) with a spike of almost 200,000 values at X equals 0."
   fixme=true %}

## How can we see the trends in this data?

-   How can we abstract out the jitter to get a better sense of trends?
-   <span g="smoothing">Smooth</span> the data by averaging values in a <span g="sliding_window">sliding window</span>
-   Smoothing always involves <span g="weighting">weighting</span> the points in the window
    -   Simplest weighting function gives equal weight to all points
    -   Technical term is <span g="convolution">convolution</span>
-   How to handle ends (where the window overlaps missing data)?
    -   Explore strategies in the exercises
-   More importantly, how to justify window size and weighting?
    -   Magic weights are just another kind of magic number

FIXME: redo smoothing example

-   These curves have different shapes but similar characteristics
    -   Climb from near zero to a sharp peak around 20 lines per function
    -   Precipitous drop thereafter

## Does this belong here?

-   FIXME: fitting piecewise linear functions with [pwlf][pwlf]
    -   Specify number of segments
    -   Library chooses endpoints to minimize error
-   Our data seems to have three segments:
    -   Initial rise
    -   Drop
    -   Tail
    -   Could make an argument that the rise is two parts, but keep it simple for now

## What sort of curve should we fit to this data?

-   Suppose the chance of an email arriving per unit time is $$\lambda$$, where $$0 < \lambda < 1$$
    -   If a message just arrived at $$t = 0$$, the chance of the next message at $$t = 1$$ is $$\lambda$$
    -   $$t = 2$$ is $$\lambda (1 - \lambda)$$, $$t = 3$$ is $$\lambda (1 - \lambda)^2$$, etc.
    -   In general, the odds of the next message at $$t = N$$ is $$\lambda (1 - \lambda)^{N-1}$$
    -   Since $$\lambda < 1$$, this is an exponential decay curve
-   The one-week curve sort of looks like an exponential decay curve
    -   Though the Y axis is logarithmic, which ought to turn an exponential curve into a straight line
-   The eight-hour curve looks more tractable
-   Use `scipy.optimize.curve_fit` to find a best-fit curve
    -   Need X and Y values
    -   And a function that takes X and some parameters and produces Y
-   Result is a pair:
    -   Values for the parameters (in order)
    -   A <span g="covariance_matrix">covariance matrix</span> that describes the fit in more detail
-   Draw the curves for various degrees of binning to see whether they:
    -   Have the same shape as our data
    -   Converge

```py
    # read and slice
    data = pd.read_csv(args.input)
    slice = data[data.Interval <= (8 * 60 * 60)].drop(columns=['Date'])

    # fit exponential curves with binning and draw figures of low end
    curves = pd.DataFrame({'x': pd.Series(range(100))})
    for bins in range(100, 1100, 200):
        counts, edges = np.histogram(slice.Interval, bins=bins)
        params, covar = scipy.optimize.curve_fit(expo_decay, edges[:-1], counts)
        a, b, c = params
        print(f'with {bins:4} bins: y = {a:8} e**(-{b:8} x) + {c:8}')
        name = f'N{bins}'
        curves[name] = expo_decay(curves.x, a, b, c)
        fig = px.line(curves, x='x', y=name, log_y=True)
        fig.show()
        fig.write_image(f'{args.output}-{name}.svg')

# ...

def expo_decay(x, a, b, c):
    return a * np.exp(-b * x) + c
```
{: title="bin/curve-fit.py"}

{% include figure
   id="fit-all-n100"
   cap="Fitted Curve (8 Hours or Less, 100 Bins)"
   alt="FIXME"
   title="Smooth exponential decay curve from Y approximately 150,000 at X equals 0 declining quickly to Y approximately 1000 at X equals 10."
   fixme=true %}

{% include figure
   id="fit-all-n500"
   cap="Fitted Curve (8 Hours or Less, 500 Bins)"
   alt="FIXME"
   title="Smooth exponential decay curve from Y approximately 80,000 at X equals 0 declining quickly to Y approximately 350 at X equals 10."
   fixme=true %}

{% include figure
   id="fit-all-n900"
   cap="Fitted Curve (8 Hours or Less, 900 Bins)"
   alt="FIXME"
   title="Smooth exponential decay curve from Y approximately 60,000 at X equals 0 declining quickly to Y approximately 22 at X equals 10."
   fixme=true %}

-   Predictions aren't converging particularly well
-   A closer look at the values up to 100 seconds reveals the problem
    <span f="fit-all-actual-100"></span>

{% include figure
   id="fit-all-actual-100"
   cap="All Values (100 Seconds or Less)"
   alt="FIXME"
   title="Jagged curve with large spike from Y equals 30,000 at X equals 0 dropping immediately to Y equals 500 at X equals 1 then rising slightly to Y equals 1000 at X equals 20 and declining slowly after that."
   fixme=true %}

-   Well that's not good

## Are duplicate messages the problem?

-   A large number of duplicated messages would explain the exaggerated value at 0 seconds
    -   Use the `Message-Id` header to detect duplicates
    -   Takes a few tries to get the regular expression right
        -   Case-insensitive
        -   Value might be on the next line and indented
    -   And once again have file encoding problems
        -   But only a few
-   First results:

```txt
...
001a1136006e24ff75050cb42178@google.com,/Users/gvwilson/Library/Mail/V5/0E639AE7-C627-4DBE-AE02-62746E206A82/INBOX.mbox/Archives.mbox/2015.mbox/FB78EF49-899B-4D40-8560-72C141DFDEF2/Data/2/7/Messages/72172.emlx
001a1136006ee6917a050aecae68@google.com,/Users/gvwilson/Library/Mail/V5/0E639AE7-C627-4DBE-AE02-62746E206A82/INBOX.mbox/Archives.mbox/2014.mbox/FB78EF49-899B-4D40-8560-72C141DFDEF2/Data/2/1/1/Messages/112262.emlx
001a11361f7a174db60513cafc74@google.com,/Users/gvwilson/Library/Mail/V5/0E639AE7-C627-4DBE-AE02-62746E206A82/INBOX.mbox/Archives.mbox/2015.mbox/FB78EF49-899B-4D40-8560-72C141DFDEF2/Data/9/7/1/Messages/179608.emlx
001a11361f7a174db60513cafc74@google.com,/Users/gvwilson/Library/Mail/V5/0E639AE7-C627-4DBE-AE02-62746E206A82/INBOX.mbox/Archives.mbox/2015.mbox/FB78EF49-899B-4D40-8560-72C141DFDEF2/Data/0/2/1/Messages/120977.emlx
001a11361f7aa71c87050429ad5c@google.com,/Users/gvwilson/Library/Mail/V5/0E639AE7-C627-4DBE-AE02-62746E206A82/INBOX.mbox/Archives.mbox/2014.mbox/FB78EF49-899B-4D40-8560-72C141DFDEF2/Data/6/7/Messages/76436.emlx
...
```

-   This is bad
    -   The message IDs reveal information about who I have exchanged email with
    -   The file paths reveal information about my computer
-   Offer an option to obfuscate the first and remove revealing details from the second
-   Result is `bin/get-mail-data.py`
    -   Message IDs are `some-string@domain.tech`
    -   So split on `@` and use a dictionary to replace each unique `domain.tech` with the same integer
    -   Then discover that `some-string` can contain `@` so adjust the split
    -   Use another dictionary-of-integers to turn each unique `some-string` into a number to (dramatically) reduce file size
    -   The two integers are as unique as the original ID
    -   Erase the first few parts of the file path
    -   And do a little cleanup on dates (remove commas and parenthesized timezone names)
-   Since we have `args` anyway, add everything else we need as attributes of that object
    -   A rough approximation of object-oriented programming
-   First discovery is how many messages are duplicated how many times
    -   Which we can find with a shell command

```sh
cut -d , -f 1-3 data/mail-data.csv | sort | uniq -c | sort -n | cut -c 1-4 | uniq -c
```

| Frequency | Number |
| --------: | -----: |
|         1 | 200197 |
|         2 |  28236 |
|         3 |     75 |
|         4 |    535 |
|         5 |      3 |
|         6 |      4 |

-   Only about 12.6% of the messages are duplicated, which isn't enough to explain the spike at $$\delta t = 0$$
-   Manual inspection reveals other problems:
    -   4.3% of messages have 'Recovered' in the mailbox name
    -   A whopping 39.7% have 'partial' in the mailbox name
-   Write a small script `bin/mail-data-filter.py` to filter `mail-data.csv` to create `mail-data-filtered.csv`

```txt
259072 records
229049 after removing duplicates
218311 after removing "Recovered"
130996 after removing "partial"
```

-   How good are the results?

```sh
cut -d , -f 3 results/mail-data-filtered.csv | sort | uniq -c | sort -n | cut -c 1-4 | uniq -c
```

| Frequency | Number |
| --------: | -----: |
|         1 | 130864 |
|         2 |     65 |
|         3 |      1 |

-   We can re-use the scripts developed earlier to generate intervals and plot

{% include figure
   id="fit-filtered-actual-100"
   cap="Filtered Values (100 Seconds or Less)"
   alt="FIXME"
   title="Jagged curve rising steeply from Y approximately 100 at X equals 0 to Y approximately 500 near X equals 30 and then declining gradually."
   fixme=true %}

{% include figure
   id="fit-filtered-N100"
   cap="Fit on Filtered Values (100 Seconds or Less)"
   alt="FIXME"
   title="Smooth exponential decay curve from Y approximately 60,000 at X equals 0 declining quickly to Y approximately 700 at X equals 5."
   fixme=true %}

-   The exponential curve might fit for high intervals, but it clearly doesn't for short ones
