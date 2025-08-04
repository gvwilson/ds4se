# Non-Parametric Statistics

<span x="introduction"/> asked whether some programmers are more productive than others.
The answer was "yes",
which immediately begs the question "why?"
Is there a "geek gene",
i.e.,
are some people just naturally better at programming?
[[Patitsas2016](b:Patitsas2016)] showed that
there is little evidence for that theory in students' grades
and that confirmation bias probably explains why some instructors believe it.

Another possibility is that some programmers discovered or been taught
more productive working practices.
One practice that is frequently mentioned is <span g="tdd">test-driven development</span> (TDD):
instead of writing code and then writing tests,
programmers write tests and then write just enough code to make them pass.
The idea is that writing tests first:

1.  helps developers figure out exactly what the code is supposed to do,

2.  avoids confirmation bias, and

3.  prevents gold-plating (when the tests pass, the work is done).

TDD has many passionate advocates, but does it actually work?

-   Discussion based on [[Fucci2016](b:Fucci2016)]
    -   Use non-parametric tests when data isn't normal (and most data isn't in software engineering)
    -   Introduce <span g="mann_whitney_u">Mann-Whitney U test</span>
        (also called <span g="wilcoxon_rank_sum">Wilcoxon rank sum test</span>)
    -   Also introduce <span g="effect_size">effect size</span>
        (in particular, the common-language effect size)

<blockquote>
The research questions driving the part of the baseline study replicated in this paper were:

1. Do test-first developers write more tests than test-last developers?
2.  Do test-first developers produce solutions with higher external quality than test-last developers?
3.  Are test-first developers more productive than test-last developers?

The independent variable was...development approach (i.e., TDD or TLD), whereas the dependent variables were:
testing effort (TESTS),
software external quality (QLTY),
and developers’ productivity (PROD).
Note that,
following from the research questions,
the hypotheses were formulated as directional for consistency with [[Erdogmus2005](b:Erdogmus2005)],
but analyzed as non-directional
since the existing body of knowledge regarding the postulated impact of TDD
does not suggest a specific direction of the effect.
</blockquote>

-   FIXME: unpack this quote

---

Each row is a mistake (label in first column),
then the next two columns are the real rank in frequency (1 = most frequent) and time-to-fix (TTF) in Blackbox.
Then it's a column for each educator for their frequency rank predictions,
same again for TTF prediction.

There's also a set for "spread"
which was a question we asked about whether the mistakes were concentrated in a few users or evenly spread across them all.
We dropped that after I decided I wasn't confident how best to operationalise that in the data (variance?  entropy?).

The original analysis was done in SPSS,
so I don't have any R code for you.
But hopefully we described it well enough in the paper:
I recommend the journal version: http://twistedsquare.com/Educators-TOCE.pdf.
Section 6.1 describes comparing educators amongst themselves,
and section 7.1 describes comparing educators to Blackbox.
