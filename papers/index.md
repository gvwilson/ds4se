---
draft: true
---

These short reviews appeared on [It Will Never Work in Theory][nwit] between
2011 and 2017.  We hope to include re-analyses of these results in our lessons.

## Analyze This!

<cite>Begel2014</cite>

Analyzes a survey to determine the questions developers most want researchers to answer.

-   Uses <span g="kano_scale">Kano scale</span> for responses

## Test-Driven Development

<cite>Fucci2016,Fucci2017</cite>

> Context: Test-driven development (TDD) is an agile practice claimed to improve
> the quality of a software product, as well as the productivity of its
> developers. A previous study (i.e., baseline experiment) at the University of
> Oulu (Finland) compared TDD to a test-last development (TLD) approach through
> a randomized controlled trial. The results failed to support the claims. Goal:
> We want to validate the original study results by replicating it at the
> University of Basilicata (Italy), using a different design. Method: We
> replicated the baseline experiment, using a crossover design, with 21 graduate
> students. We kept the settings and context as close as possible to the
> baseline experiment. In order to limit researchers bias, we involved two other
> sites (UPM, Spain, and Brunel, UK) to conduct blind analysis of the
> data. Results: The Kruskal-Wallis tests did not show any significant
> difference between TDD and TLD in terms of testing effort (p-value = .27),
> external code quality (p-value = .82), and developers' productivity (p-value =
> .83). Nevertheless, our data revealed a difference based on the order in which
> TDD and TLD were applied, though no carry over effect. Conclusions: We verify
> the baseline study results, yet our results raises concerns regarding the
> selection of experimental objects, particularly with respect to their
> interaction with the order in which of treatments are applied.

This painstaking study is the latest in a long line to find that test-driven
development (TDD) has little or no impact on development time or code
quality. Here, the authors repeated an earlier study with a couple of new
wrinkles, and then blinded their data before giving it to someone else to
analyze to remove any possibility of bias. The result: no significant difference
between TDD and iterative test-last (ITL) development.

...which still surprises me seven years after Turhan et al's meta-analysis in
*Making Software*.  reported the same result. I don't program very much any
more, but when I do, I feel that writing tests up front makes me more
productive. I'd like to be able to say that these researchers and others must be
measuring the wrong things, or measuring things the wrong way, but after so many
years and so many different studies, those of us who believe might just have to
accept that our self-assessment is wrong.

-   Treats <span g="pair_programming">pair programming</span> as a <span g="nuisance_factor">nuisance factor</span>
-   Uses <span g="mann_whitney_u">Mann-Whitney *U* test</span>
-   Uses <span g="cliffs_delta">Cliff's $$\delta$$</span> to report effect size
-   Uses <span g="kruskal_wallis">Kruskal-Wallis test</span>

## Frequency Distribution of Error Message

<cite>Pritchard2015</cite>

> Which programming error messages are the most common? We investigate this
> question, motivated by writing error explanations for novices. We consider
> large data sets in Python and Java that include both syntax and run-time
> errors. In both data sets, after grouping essentially identical messages, the
> error message frequencies empirically resemble Zipf-Mandelbrot
> distributions. We use a maximum-likelihood approach to fit the distribution
> parameters. This gives one possible way to contrast languages or compilers
> quantitatively.

Based on a large corpus of error messages, the 5 most common errors in Python
programs are:

| Frequency | Message |
| --------- | ------- |
| 179624 | SyntaxError: invalid syntax |
| 97186 | NameError: name 'NAME' is not defined |
| 76026 | EOFError: EOF when reading a line |
| 26097 | SyntaxError: unexpected EOF while parsing |
| 20758 | IndentationError: unindent does not match any outer indentation level |

and the 5 most common in Java are:

| Frequency | Message |
| --------- | ------- |
| 702102 | cannot find symbol - variable NAME |
| 407776 | ';' expected |
| 280874 | cannot find symbol - method NAME |
| 197213 | cannot find symbol - class NAME |
| 183908 | incompatible types |

What's more, their frequency has a power law (or "long tail") distribution,
which suggests that improving reporting for just a handful of errors would have
a disproportionate effect on usability. But my favorite part of this paper comes
toward the end of Section 3.2:

> Can this [relationship] be plausible: is the total number of possible errors
> infinite? We will accept this as a reasonable hypothesis...

to which I can only say, "Amen."

-   Uses <span g="power_law_distribution">power law distribution</span>
-   Uses <span g="zipf_mandelbrot_distribution">Zipf-Mandelbrot distribution</span>
-   Uses Gamma function and Beta function
-   Uses Evert distribution
-   May be too obscure: find something else on frequency of error messages?

## Novice Programming Mistakes

<cite>Altadmri2015</cite>

> Educators often form opinions on which programming mistakes novices make most
> often—for example, in Java: "they always confuse equality with assignment", or
> "they always call methods with the wrong types". These opinions are generally
> based solely on personal experience. We report a study to determine if
> programming educators form a consensus about which Java programming mistakes
> are the most common. We used the Blackbox data set to check whether the
> educators' opinions matched data from over 100,000 students—and checked
> whether this agreement was mediated by educators' experience. We found that
> educators formed only a weak consensus about which mistakes are most frequent,
> that their rankings bore only a moderate correspondence to the students in the
> Blackbox data, and that educators' experience had no effect on this level of
> agreement. These results raise questions about claims educators make regarding
> which errors students are most likely to commit.

So, what's the most common kind of error novice Java programmers make?  Turns
out it isn't confusing assignment "=" with equality "==", but rather mis-matched
or unbalanced parentheses. Invoking methods with the wrong argument (e.g.,
`list.get("abc")`) is the second most common, and control flow being able to
reach the end of a non-void method without returning a value is third. And which
errors take the most time to fix?  The answer to that turns out to be:

-   Confusing short-circuit logical operators like `&&` and `||` with
    their non-short-circuiting bitwise equivalents `&` and `|`.

-   Using `==` instead of `.equals` to compare strings.

-   Ignoring the return value from a non-void method.

As if this data wasn't enough, the authors also compared this data to a survey
of what teachers believe about student errors (see Brown and Altadmri,
"Investigating Novice Programming Mistakes: Educator Beliefs vs Student Data",
ICER'14, <http://dx.doi.org/10.1145/2632320.2632343>). Their main finding:
"...educators formed only a weak consensus about which mistakes are most
frequent, that their rankings bore only a moderate correspondence to the
students in the Blackbox data, and that educators' experience had no effect on
this level of agreement." It may be years before textbooks begin to reflect
these insights, and decades before they start to influence language design, but
at least we now know that better is possible.

## Paradise Unplugged

<cite>Ford2016</cite>

> It is no secret that females engage less in programming fields than
> males. However, in online communities, such as Stack Overflow, this gender gap
> is even more extreme: only 5.8% of contributors are female.  In this paper, we
> use a mixed-methods approach to identify contribution barriers females face in
> online communities. Through 22 semi-structured interviews with a spectrum of
> female users ranging from non-contributors to a top 100 ranked user of all
> time, we identified 14 barriers preventing them from contributing to Stack
> Overflow. We then conducted a survey with 1470 female and male developers to
> confirm which barriers are gender related or general problems for
> everyone. Females ranked five barriers significantly higher than males. A few
> of these include doubts in the level of expertise needed to contribute,
> feeling overwhelmed when competing with a large number of users, and limited
> awareness of site features.  Still, there were other barriers that equally
> impacted all Stack Overflow users or affected particular groups, such as
> industry programmers. Finally, we describe several implications that may
> encourage increased participation in the Stack Overflow community across
> genders and other demographics.

Computing as a whole has a diversity problem, but its online communities are
even worse. This careful study explores why by looking at Stack Overflow, and
finds five barriers to contribution that are seen as significantly more
problematic by women than by men:

1.  lack of awareness of site features

2.  feeling unqualified to answer questions

3.  intimidating community size

4.  discomfort interacting with or relying on strangers

5.  perception that they shouldn't be "slacking"

Surprisingly, "fear of negative feedback" didn't quite make this list, but would
have been the next one added if the authors weren't quite so strict about their
statistical cutoffs. The authors are careful to say, "...we are not suggesting
that only females are affected by these barriers, or that these barriers are
primarily due to gender, but rather that five barriers were seen as
significantly more problematic by females than by males."

In a better world than ours, this list would lead to a series of papers and
tools that directly and explicitly tackled these challenges and measured their
success not by ad revenue but by how well they addressed the systemic failures
of our profession. In this world, I'm less hopeful, but would be very happy to
be proved wrong.

-   Uses <span g="wilcoxon_rank_sum">Wilcoxon rank-sum test</span> to compare male and female responses to survey questions
-   Use  Wilcoxon rank-sum test with <span g_"bonferroni-correction">Bonferroni correction</span>

## Too Many Knobs

<cite>Xu2015</cite>

> This paper makes a first step in understanding a fundamental question of
> configuration design: "do users really need so many knobs?" To provide the
> quantitatively answer, we study the configuration settings of real-world
> users, including thousands of customers of a commercial storage system
> (Storage-A), and hundreds of users of two widely-used open-source system
> software projects. Our study reveals a series of interesting findings to
> motivate software architects and developers to be more cautious and
> disciplined in configuration design. Motivated by these findings, we providea
> few concrete, practical guidelines which can significantly reduce the
> configuration space. Take Storage-A as an example, the guidelines can remove
> 51.9% of its parameters and simplify 19.7% of the remaining ones with little
> impact on existing users. Also, we study the existing configuration navigation
> methods in the context of "too many knobs" to understand their effectiveness
> in dealing with the over-designed configuration, and to provide practices for
> building navigation support in system software.

I can't write a better summary of the paper than the authors have themselves:

-   Only a small percentage (6.1%-16.7%) of configuration parameters are set by
    the majority of users; a significant percentage (up to 54.1%) of parameters
    are rarely set by any user.

-   A small percentage (1.8%-7.8%) of parameters are configured by more than 90%
    of the users.

-   Software developers often choose more "flexible" data types for configuration
    parameters to give users more flexibility of settings (e.g., using numeric
    types instead of the simple Boolean or enumerative ones). However, users
    seem not to take full advantage of such flexibility. A significant
    percentage (up to 47.4%) of numeric parameters have no more than five
    distinct settings among all the users' settings.

-   Similarly, for enumerative parameters with many options, typically only two to
    three of the options are actually used by the users, indicating once again
    the over-designed flexibility.

-   Too many knobs do come with a cost: users encounter tremendous difficulties in
    knowing which parameters should be set among the large configuration
    space. This is reflected by the following two facts: (1) a significant
    percentage (up to 48.5%) of configuration issues are about users'
    difficulties in finding or setting the parameters to obtain the intended
    system behavior; (2) a significant percentage (up to 53.3%) of configuration
    errors are introduced due to users' staying with default values incorrectly.

-   Configuration parameters with explicit semantics, visible external impact are
    set by more users, in comparison to parameters that are specific to internal
    system implementation.

-   The configuration of the studied software can be significantly simplified by
    reducing the configuration space both vertically and horizontally. For
    Storage-A, 51.9% of the original parameters can be hidden or removed, and
    19.7% of the remaining ones can be further converted into simpler types,
    with the impact on fewer than 1% of the users. The similar reduction rates
    are also observed in the other two open-source software.

-   Searching user manuals by keywords is not efficient to help users identify the
    target parameter(s).

-   Google search can provide useful information for 46.1%-80.0% of the historical
    configuration navigation issues. However, it is less efficient in navigation
    parameters of less popular software or new issues. The majority of resources
    on the Web that host useful information for navigation are the contents
    contributed by users, such as Q&A forums and blog articles.

-   Well-engineered NLP-based navigation can return the target configuration
    parameter for more than 60% of the historical navigation issues. Boosting
    the results with the statistics of users' configuration settings in the
    field can significantly improve the performance of NLP-based navigation.

There's lots more in here: discussion of the experimental method used, a table
of recommendations for simplifying configuration whose points are all grounded
in findings, and pointers to related work (much of which I hadn't seen
before). What's more, the configuration data is available in a GitHub repository
for those who wish to examine it themselves.

-   Uses web crawling to find configuration files

## Java Exception Handling

<cite>Nakshatri2016</cite>

> Exception handling is a powerful tool provided by many programming languages
> to help developers deal with unforeseen conditions. Java is one of the few
> programming languages to enforce an additional compilation check on certain
> subclasses of the Exception class through checked exceptions. As part of this
> study, empirical data was extracted from software projects developed in
> Java. The intent is to explore how developers respond to checked exceptions
> and identify common patterns used by them to deal with exceptions, checked or
> otherwise. Bloch's book "Effective Java" was used as reference for best
> practices in exception handling - these recommendations were compared against
> results from the empirical data. Results of this study indicate that most
> programmers ignore checked exceptions and leave them unnoticed. Additionally,
> it is observed that classes higher in the exception class hierarchy are more
> frequently used as compared to specific exception subclasses.

This paper's abstract underplays the bleakness of its findings. Rather than
being used to make software more robust, exceptions are either ignored or used
as a debugging aid. For example, the most common `catch` block is one that logs
the error rather than trying to recover from it; the next most common are to do
nothing at all (20% of cases), or to convert the checked exception into an
unchecked exception so that it can be ignored. Similarly, most programmers
ignore Java's carefully thought out exception hierarchy and simply catch
`Exception` (78%) or `Throwable` (84%) rather than any of their subclasses.

The only conclusion I can draw from this is that exception-based error handling
has failed to achieve what its creators intended. That's slightly different from
being a complete failure: based on Nakshatri et al's findings, it appears that
exception *are* useful as a debugging aid during development. And it's possible
that the real failure is educational: despite the ubiquity of distributed
systems, most undergraduate programs still spend approximately zero time on
error handling and recovery. Either way, I think language developers have their
work cut out for them.

## Variability and Reproducibility in Software Engineering

<cite>Anda2009</cite>

> The scientific study of a phenomenon requires it to be reproducible.  Mature
> engineering industries are recognized by projects and products that are, to
> some extent, reproducible. Yet, reproducibility in software engineering (SE)
> has not been investigated thoroughly, despite the fact that lack of
> reproducibility has both practical and scientific consequences. We report a
> longitudinal multiple-case study of variations and reproducibility in software
> development, from bidding to deployment, on the basis of the same requirement
> specification. In a call for tender to 81 companies, 35 responded.  Four of
> them developed the system independently. The firm price, planned schedule, and
> planned development process, had, respectively, "low", "low", and "medium"
> reproducibilities. The contractor's costs, actual lead time, and schedule
> overrun of the projects had, respectively, "medium", "high", and "low"
> reproducibilities. The quality dimensions of the delivered products,
> reliability, usability, and maintainability had, respectively, "low", "high",
> and "low" reproducibilities.  Moreover, variability for predictable reasons is
> also included in the notion of reproducibility. We found that the observed
> outcome of the four development projects matched our expectations, which were
> formulated partially on the basis of SE folklore. Nevertheless, achieving more
> reproducibility in SE remains a great challenge for SE research, education,
> and industry.

Albert Einstein once defined insanity as, "Doing the same thing over and over
again and expecting different results." That's also a good definition of
science: we repeat our experiments so that we can gather statistics about their
outcomes, which in turn give us deeper insight into what the universe is
doing. This can be an expensive process—just look at the LHC, or at the cost of
putting a probe into space, or the salaries of professional programmers. As much
as they'd like to, most researchers simply can't afford to have several teams
develop the same software independently, just so that the differences in what
they do can be studied.

That's what makes this paper so valuable. As their abstract says, Anda, Sjøberg,
and Mockus had four teams build the same software independently and in parallel
so that they could look at how much variation there was in what happened. Their
results are worth re-summarizing:

-   High reproducibility: actual lead time, usability

-   Medium reproducibility: planned development process, cost

-   Low reproducibility: firm price, planned schedule, schedule overrun,
    reliability, maintainability

Note that putting something in the "low" category doesn't mean that it was
uniformly poor. Instead, it means that there was wide variation, i.e., that
results were unpredictable. As they say, their results match software
engineering folklore, and are a solid guide to what research should focus on
improving.

-   Uses inverse of <span g="effect_size">effect size</span> as a measure of reproducibility

## Effects of Personality on Pair Programming

<cite>Hannay2010</cite>

> Personality tests in various guises are commonly used in recruitment and
> career counseling industries. Such tests have also been considered as
> instruments for predicting the job performance of software professionals both
> individually and in teams. However, research suggests that other human-related
> factors such as motivation, general mental ability, expertise, and task
> complexity also affect the performance in general. This paper reports on a
> study of the impact of the Big Five personality traits on the performance of
> pair programmers together with the impact of expertise and task
> complexity. The study involved 196 software professionals in three countries
> forming 98 pairs. The analysis consisted of a confirmatory part and an
> exploratory part. The results show that: 1) Our data do not confirm a
> meta-analysis-based model of the impact of certain personality traits on
> performance and 2) personality traits, in general, have modest predictive
> value on pair programming performance compared with expertise, task
> complexity, and country. We conclude that more effort should be spent on
> investigating other performance-related predictors such as expertise, and task
> complexity, as well as other promising predictors, such as programming skill
> and learning. We also conclude that effort should be spent on elaborating on
> the effects of personality on various measures of collaboration, which, in
> turn, may be used to predict and influence performance. Insights into such
> malleable, rather than static, factors may then be used to improve pair
> programming performance.

The topic of personality often comes up in discussions of pair programming
efficiency: whether you need to do an extravert to reap its benefits, whether
the contrast in personality with your peer is important, and so on. Many
research studies have addressed these questions; Hannay & Co's is a good place
to start reading about them.  They report: "we found no strong indications that
personality affects pair programming performance or pair gain in a consistent
manner", and suggest that industry and research should "focus on other
predictors of performance, including expertise and task complexity" instead, as
these factors overshadow any personality effects.

-   Uses <span g="pca">principal component analysis</span>

## Don't Touch My Code!

<cite>Bird2011</cite>

> Ownership is a key aspect of large-scale software development. We examine the
> relationship between different ownership measures and software failures in two
> large software projects: Windows Vista and Windows 7. We find that in all
> cases, measures of ownership such as the number of low-expertise developers,
> and the proportion of ownership for the top owner have a relationship with
> both pre-release faults and post-release failures. We also empirically
> identify reasons that low-expertise developers make changes to components and
> show that the removal of low-expertise contributions dramatically decreases
> the performance of contribution based defect prediction. Finally we provide
> recommendations for source code change policies and utilization of resources
> such as code inspections based on our results.

I used to tell my students that a paper's abstract should be a summary, not a
movie trailer. When I read, "We find that... measures of ownership... have a
relationship with both pre-release faults and post-release failures," my
reaction is, "What kind of relationship?"  And when a paper's authors say,
"We... identify reasons that low-expertise developers make changes to
components," I want to grab my red pen and scribble, "Summarize them here!"

Fortunately, this paper's abstract is the only thing about it that I don't
like. Over the course of its 11 pages, its authors explore three related
questions:

1.  Are higher levels of ownership associated with less defects?

2.  Is there a negative effect when a software entity is developed by
    many people with low ownership?

3.  Are these effects related to the development process used?

They start by defining their units of measurement (a compiled binary such as a
.dll or .exe), what they mean by major and minor contributors, and how they
measure ownership. After grinding their data (they have *lots* of data), they
come up with Table 1.  There's a lot of information in that table, and I won't
try to squeeze it all into this blog post, but as a taste, it allows them to
conclude that:

> The results indicated that pre- and post-release defects in had strong
> relationships with Minor, Total, and Ownership. In fact, Minor had a higher
> correlation with both pre- and post-release defects in Vista and pre-release
> defects in Windows 7 than any other metric that Microsoft
> collects!. Post-release failures for Windows 7 present a difficulty for
> analysis as at the time of this analysis many binaries had no post-release
> failures reported. Thus the correlation values between metrics and and
> post-release failures are noticeably lower than the other failure
> categories...

Later, after teasing apart the contributions of major and minor contributors,
and the effects of dependencies between components, they conclude that:

> ...the minor contribution edges [in the contributions graph] provide the
> "signal" used by defect predictors that are based on the contribution
> network. Without them, the ability to predict failure prone components is
> greatly diminished, further supporting our hypothesis that they are strongly
> related to software quality.

and:

> After controlling for known software quality factors, binaries with more minor
> contributors had more pre- and post-release failures in both versions of
> Windows.

They then recommend that:

1.  Changes made by minor contributors should be reviewed with more
    scrutiny.

2.  Potential minor contributors should communicate desired changes to
    developers experienced with the respective binary.

3.  Components with low ownership should be given priority by QA
    resources.

Even if you can't apply their results directly to your own projects, they show
that it is possible to analyze the impact of different software manufacturing
practices methodically and quantitatively. The next time someone suggests that
your team start doing X, Y, or Z, ask them if they have this kind of data to
back up their recommendation. If they don't, you might consider giving them a
copy of this paper...

-   Uses <span g="gqm">goal-question-metric</span> approach
-   "A developer who has made a small proportion of the commits to a binary likely has less expertise and is more likely to make an error."
    -   Very questionable assumption:
        can equally well argue that someone who only commits a small number of times
        is an outside expert brought in to help with something really hard
-   Mapping faults directly to source code wasn't possible
-   Uses <span g="multiple_linear_regression">multiple linear regression</span>
-   Uses a goodness-of-fit <span g="f_test">F-test</span>
-   Mentions work by <cite>Pinzger2008</cite> on social networks to find fault-prone binaries

## Is Transactional Programming Actually Easier?

<cite>Rossbach2010</cite>

> In this paper, we describe a user-study in which 147 undergraduate students in
> an operating systems course implemented the same programs using coarse and
> fine-grain locks, monitors, and transactions. We surveyed the students after
> the assignment, and examined their code to determine the types and frequency
> of programming errors for each synchronization technique. Inexperienced
> programmers found baroque syntax a barrier to entry for transactional
> programming. On average, subjective evaluation showed that students found
> transactions harder to use than coarse-grain locks, but slightly easier to use
> than fine-grained locks. Detailed examination of synchronization errors in the
> students' code tells a rather different story. Overwhelmingly, the number and
> types of programming errors the students made was much lower for transactions
> than for locks. On a similar programming problem, over 70% of students made
> errors with fine-grained locking, while less than 10% made errors with
> transactions.

Software Transactional Memory (STM) has been receiving a lot of press lately as
people try to find ways of making parallelism safe for human consumption. The
results presented in this paper are a very hopeful sign: students who used it
did better on simple problems than students using more traditional
mechanisms. What's equally interested is that they *thought* they had done
worse, possibly because of the "baroque syntax" the authors mention. And once
again, this paper highlights the fact that the usability of software engineering
tools, including programming languages, can and should be studied empirically.

-   Uses Wilcoxon signed rank test

## Does Adding Manpower Also Affect Quality?

<cite>Meneely2011</cite>

> With each new developer to a software development team comes a greater
> challenge to manage the communication, coordination, and knowledge transfer
> amongst teammates. Fred Brooks discusses this challenge in The Mythical
> Man-Month by arguing that rapid team expansion can lead to a complex team
> organization structure. While Brooks focuses on productivity loss as the
> negative outcome, poor product quality is also a substantial concern. But if
> team expansion is unavoidable, can any quality impacts be mitigated? Our
> objective is to guide software engineering managers by empirically analyzing
> the effects of team size, expansion, and structure on product quality. We
> performed an empirical, longitudinal case study of a large Cisco networking
> product over a five year history. Over that time, the team underwent periods
> of no expansion, steady expansion, and accelerated expansion. Using team-level
> metrics, we quantified characteristics of team expansion, including team size,
> expansion rate, expansion acceleration, and modularity with respect to
> department designations.  We examined statistical correlations between our
> monthly team-level metrics and monthly product-level metrics. Our results
> indicate that *increased team size and linear growth are correlated with later
> periods of better product quality*. However, *periods of accelerated team
> expansion are correlated with later periods of reduced software
> quality*. Furthermore, our linear regression prediction model based on team
> metrics was able to predict the product's post-release failure rate within a
> 95% prediction interval for 38 out of 40 months.  Our analysis provides
> insight for project managers into how the expansion of development teams can
> impact product quality.

If there's one "law" of software development that practitioners across the board
have heard of, it has to be Brooks' Law: "adding manpower to a late project
makes it later." This paper by Meneely & Co.  provides a good complement to
Brooks' discussions. It does not concern itself with meeting deadlines, as
Brooks did, but it explores the correlation between adding people to a team and
the posterior quality of the software the team works on.

The paper reports that adding people is correlated with a later increase in
software quality, but adding them too quickly (that is, at a faster pace than in
previous months) is correlated with a *decrease* in quality. A greater
organizational modularity is also associated with decreased quality.

I confess that I have trouble wrapping my head around the first of these
findings. Theoretically, adding people to a project increases its coordination
costs, which in turn should impact all metrics of team success negatively,
including quality. And yet we have not only Meneely & Co's findings, but also
last year's Mockus' report on organizational volatility making the case that
more newcomers are not correlated with more defects, which provides support to
this finding. One possibility, discussed by Mockus, is that newcomers are
assigned easy tasks, and so they can't really break things too dramatically or
in a way that won't get caught internally in time. Another possibility,
particularly plausible in the Cisco data set, is that the product has matured
over time—that software quality would go up no matter the team size simply
because there's less new functionality added as time goes on.

In any case, while we get better answers for the underlying mechanisms in the
correlation between increasing team sizes and software quality, the best advice
seems to be: it's OK to bring new people to a team (with respect to quality),
just don't do it too quickly.

-   Uses graph theory to measure modularity of contributor teams
-   Uses <span g="linear_regression">linear regression</span>

## An Empirical Study of Build Maintenance Effort

<cite>McIntosh2011</cite>

> The build system of a software project is responsible for transforming source
> code and other development artifacts into executable programs and
> deliverables. Similar to source code, build system specifications require
> maintenance to cope with newly implemented features, changes to imported
> Application Program Interfaces (APIs), and source code restructuring. In this
> paper, we mine the version histories of one proprietary and nine open source
> projects of different sizes and domain to analyze the overhead that build
> maintenance imposes on developers. We split our analysis into two dimensions:
> (1) Build Coupling, i.e., how frequently source code changes require build
> changes, and (2) Build Ownership, i.e., the proportion of developers
> responsible for build maintenance. Our results indicate that, despite the
> difference in scale, the build system churn rate is comparable to that of the
> source code, and build changes induce more relative churn on the build system
> than source code changes induce on the source code. Furthermore, build
> maintenance yields up to a 27% overhead on source code development and a 44%
> overhead on test development. Up to 79% of source code developers and 89% of
> test code developers are significantly impacted by build maintenance, yet
> investment in build experts can reduce the proportion of impacted developers
> to 22% of source code developers and 24% of test code developers.

One of the many reasons software projects fail is poor estimation, and one of
the reasons people estimate badly is that they don't keep track of what's
happened before. This paper provides a baseline for both how much effort is
required to keep the build system in working order, and how much those figures
can be improved.

-   Uses <span g="chi_square">chi-square test</span>

## Failure is a Four-Letter Word

<cite>Zeller2011</cite>

If you keep track of recent developments in empirical software engineering, you
may have already heard of the fantastic IROP study. I was too busy writing a
paper to blog about it when Andreas Zeller presented it at PROMISE 2011, but
here I go, in case you haven't read it.

Basically, Zeller, Thomas Zimmermann, and Christian Bird did what I'm afraid
some researchers in our field do on a regular basis: take some mining tools and
some data, and then go nuts with them—abuse of them in the most absurd ways
imaginable. Luckily, Zeller, Zimmermann, and Bird did it *on purpose* and as *a
parody*.

Here's what they did: take Eclipse data on code and errors, and correlate the
two to find good predictors of bugs. Sounds sensible. But they did the
correlation at the ASCII character level. So it turns out, for Eclipse 3.0, the
characters that are most highly correlated with errors are the letters 'i', 'r',
'o', and 'p'. What is a sensible researcher to do facing these findings? Well
take those letters out of the keyboard, of course! Problem solved:

They then go over a supposed half-baked validation study with three interns, who
reported great success in adapting to a life without 'i', 'r', 'o', and 'p' in
their keyboards. Trial feedback:

> We can shun these set majuscules, and the text stays just as swell as
> antecedently. Let us just ban them!

Near the end, the authors go over everything that's wrong with their approach
(lack of theoretical grounding, dishonest use of statistics, and a long *et
cetera*). It's a fun read, and instructive.

-   Uses logistic regression (discusses precision and recall)
-   Uses Spearman rank correlation (because distribution is visibly non-normal)
    -   Uses <span g="benjamini_hochberg">Benjamini-Hochberg p-value correction</span>

## The Impact of Irrelevant and Misleading Information

<cite>Jorgensen2011</cite>

> Studies in laboratory settings report that software development effort
> estimates can be strongly affected by effort-irrelevant and misleading
> information. To increase our knowledge about the importance of these effects
> in field settings, we paid 46 outsourcing companies from various countries to
> estimate the required effort of the same five software development
> projects. The companies were allocated randomly to either the original
> requirement specification or a manipulated version of the original requirement
> specification. The manipulations were as follows: 1) reduced length of
> requirement specification with no change of content, 2) information about the
> low effort spent on the development of the old system to be replaced, 3)
> information about the client's unrealistic expectations about low cost, and 4)
> a restriction of a short development period with start up a few months
> ahead. We found that the effect sizes in the field settings were much smaller
> than those found for similar manipulations in laboratory settings. Our
> findings suggest that we should be careful about generalizing to field
> settings the effect sizes found in laboratory settings. While laboratory
> settings can be useful to demonstrate the existence of an effect and better
> understand it, field studies may be needed to study the size and importance of
> these effects.

The researchers from the SIMULA Lab in Norway do something pretty unique in our
domain: use their research funds to pay lots of software professionals to do
their thing in a setting as natural as possible, under conditions as controlled
as possible. As a result you avoid running toy experiments with half a dozen
students and get instead, for instance, that paper on variability in software
projects, where several companies were paid to develop the exact same
software. Or this other paper. In it, the researchers contact people in 46
companies and ask them to estimate the likely effort required to develop some
software projects. However, they send slightly different descriptions of the
projects to these companies, modifying them in "irrelevant and misleading" ways
to see if that biases their estimates.

Several previous studies have tweaked project descriptions to see if the
resulting estimates varied, and the overwhelming response is that yes, they do
vary—estimators are subject to cognitive biases, like everyone else. What's
interesting is that the authors here found that most of the effects were
considerably *weaker* in their setting than those effects observed in previous
studies "in the lab" (including, by the way, my own). In most cases the effects
appear to be there, but they're often not strong enough to achieve statistical
significance.  They conclude:

> While a meaningful role of laboratory experiments is to demonstrate the
> existence of an effect and understand its nature, we should be careful to base
> statements about the size, i.e., the importance of an effect on laboratory
> studies alone. For the purpose of establishing knowledge about the importance
> of an effect, we need field studies.

-   Uses <span g="anova">ANOVA</span>
-   Uses <span g="cohens_d">Cohen's *d*</span>

## Abbreviated vs. Full-Word Identifier Names

<cite>Scanniello2017</cite>

> We carried out a family of controlled experiments to investigate whether the
> use of abbreviated identifier names, with respect to full-word identifier
> names, affects fault fixing in C and Java source code. This family consists of
> an original (or baseline) controlled experiment and three replications. We
> involved 100 participants with different backgrounds and experiences in
> total. Overall results suggested that there is no difference in terms of
> effort, effectiveness, and efficiency to fix faults, when source code contains
> either only abbreviated or only full-word identifier names. We also conducted
> a qualitative study to understand the values, beliefs, and assumptions that
> inform and shape fault fixing when identifier names are either abbreviated or
> full-word. We involved in this qualitative study six professional developers
> with 1–3 years of work experience.  A number of insights emerged from this
> qualitative study and can be considered a useful complement to the
> quantitative results from our family of experiments. One of the most
> interesting insights is that developers, when working on source code with
> abbreviated identifier names, adopt a more methodical approach to identify and
> fix faults by extending their focus point and only in a few cases do they
> expand abbreviated identifiers.

-   Uses Kim's mutation operators for changing programs
-   Uses <span g="f_measure">F-measure</span>
-   Uses multivariate linear mixed model
-   Uses <span g="shapiro_wilk">Shapiro-Wilk test</span> for normality

## An Experiment About Static and Dynamic Type Systems

<cite>Hanenberg2010</cite>

> Although static type systems are an essential part in teaching and research in
> software engineering and computer science, there is hardly any knowledge about
> what the impact of static type systems on the development time or the
> resulting quality for a piece of software is.  On the one hand there are
> authors that state that static type systems decrease an application's
> complexity and hence its development time (which means that the quality must
> be improved since developers have more time left in their projects). On the
> other hand there are authors that argue that static type systems increase
> development time (and hence decrease the code quality) since they restrict
> developers to express themselves in a desired way. This paper presents an
> empirical study with 49 subjects that studies the impact of a static type
> system for the development of a parser over 27 hours working time. In the
> experiments the existence of the static type system has neither a positive nor
> a negative impact on an application's development time (under the conditions
> of the experiment).

How many experiments in software engineering research are you aware of where the
researcher developed a new programming language and corresponding IDE just for
the experiment? Well, Stefan Hanenberg did exactly that, and the results are
remarkable. The goal of his experiment was to measure the impact of static
vs. dynamic type systems on development time and software quality. While there
is a lot of conventional wisdom around the use of static or dynamic type systems
(e.g., static type systems capture many recurring programming errors and make
systems easier to maintain, dynamic type systems make life easier by not posing
unnecessary restrictions), there is hardly any hard evidence to support these
claims, and for a practitioner, it is unclear which arguments can be trusted.

Unlike what has been done in previous work, Hanenberg decided not to use
existing programming languages and IDEs in his experiment because he worried
that subjects' familiarity with the tooling would influence the results, in
particular if his subjects knew only the dynamic or only the static version used
in the study. Therefore, he developed a new object-oriented programming language
"Purity" (with some similarities to Smalltalk, Ruby and Java) and a
corresponding IDE (class browser, test browser and console). Actually, he
developed two versions of Purity: one with static types, the other one with a
dynamic type system.  The two versions were identical in all other aspects.

His experimental setup followed a between-subject design (i.e., each subject was
only used once). He recruited 49 students, divided them into two groups, and
taught each group one of the Purity versions (the dynamic type version was
taught for 16 hours and the static type version was taught for 18 hours). All
subjects were then given exactly 27 hours to implement a scanner and a parser
for a given grammar. Hanenberg measured two outcomes: development time and
quality. Development time was measured based on log entries and test cases in
order to determine the exact point in time when subjects fulfilled all the test
cases for a minimal scanner, and the quality of the parser was measured through
400 test cases that represented valid and invalids words in the grammar.

The main result from Hanenberg's study is that–under the conditions of his
experiment–the existence of a static type system did not have a positive impact
on development time or quality. In fact, the subjects who used the dynamic type
version of Purity were significantly faster in developing a scanner, but there
was no statistically significant difference with respect to quality of the final
product.

In addition to conducting and describing a well-planned and well-executed
experiment, Hanenberg does a thorough job explaining and justifying his choice
of methods, both for data collection and data analysis. But he also discusses
the limitations of his work in great depth–in particular that it is impossible
to draw general conclusions from one experiment. However, what a single
experiment such as Hanenberg's can do is cast doubts on the role of static type
systems in software engineering, and his work opens up lots of venues for future
work on which programming languages work better than others, and why.

-   Uses Mann-Whitney *U* test
-   Uses Shapiro-Wilk test

## Do Faster Releases Improve Software Quality?

<cite>Khomh2012</cite>

> Nowadays, many software companies are shifting from the traditional 18-month
> release cycle to shorter release cycles. For example, Google Chrome and
> Mozilla Firefox release new versions every 6 weeks. These shorter release
> cycles reduce the users' waiting time for a new release and offer better
> marketing opportunities to companies, but it is unclear if the quality of the
> software product improves as well, since shorter release cycles result in
> shorter testing periods. In this paper, we empirically study the development
> process of Mozilla Firefox in 2010 and 2011, a period during which the project
> transitioned to a shorter release cycle. We compare crash rates, median
> uptime, and the proportion of post-release bugs of the versions that had a
> shorter release cycle with those having a traditional release cycle, to assess
> the relation between release cycle length and the software quality observed by
> the end user. We found that (1) with shorter release cycles, users do not
> experience significantly more post-release bugs and (2) bugs are fixed faster,
> yet (3) users experience these bugs earlier during software execution (the
> program crashes earlier).

Designing and building software is not like assembly-line manufacturing, but
some aspects of it *can* be studied and improved like other industrial
processes. In this upcoming paper, Khomh et al. examine the effects of Mozilla's
switch from a yearly (or longer) release cycle to a much more frequent
cycle. Their raw material is bug and crash data; their conclusions are:

1.  Users experience crashes earlier during the execution of versions
    developed following a rapid release model.

2.  The Firefox rapid release model fixes bugs faster than using the
    traditional model, but fixes proportionally less bugs.

3.  With a rapid release model, users adopt new versions faster compared
    to the traditional release model.

#3 is good news; #2 is (mostly) good, but #1 is a puzzle for which the authors
don't have an explanation—at least, not yet. We'd welcome suggestions about why
it might be.

-   Herraiz reports that increasing the number of deployments increases the number of reported bugs
-   Uses Wilcoxon rank-sum test

## The Effects of Stand-Up and Sit-Down Meeting Formats on Meeting Outcomes

<cite>Bluedorn1999</cite>

> The effects of meeting format (standing or sitting) on meeting length and the
> quality of group decision making were investigated by comparing meeting
> outcomes for 56 five-member groups that conducted meetings in a standing
> format with 55 five-member groups that conducted meetings in a seated
> format. Sit-down meetings were 34% longer than stand-up meetings, but they
> produced no better decisions than stand-up meetings. Significant differences
> were also obtained for satisfaction with the meeting and task information use
> during the meeting but not for synergy or commitment to the group's decision.
> The findings were generally congruent with meeting-management recommendations
> in the time-management literature, although the lack of a significant
> difference for decision quality was contrary to theoretical expectations. This
> contrary finding may have been due to differences between the temporal context
> in which this study was conducted and those in which other time constraint
> research has been conducted, thereby revealing a potentially important
> contingency—temporal context.

If there's one practice that caught on with every software team that calls
itself Agile, it's got to be daily stand-up meetings. If you hold your meetings
standing up, the argument goes, they will go briskly, which is great because
nobody likes meetings that drag on and on, especially if you hold them
daily. This paper provides valuable evidence with respect to the efficacy of
stand-up meetings: they are significantly shorter than sit-down meetings, and
the decisions taken in them are just as good. Their only downside in the
experiment is that participants were less satisfied with the meeting than those
in sit-down meetings.

These were all 5-person meetings lasting 10-20 minutes and concerning a
well-defined problem. The authors warn: "...additional research is needed to
determine whether the stand-up meeting can be used for longer meetings dealing
with problems that vary in their structure."

-   Uses ANOVA
-   Participants were overwhelmingly white (91%) and mostly men (56%)

## Got Issues? Do New Features and Code Improvements Affect Defects?

<cite>Posnett2011</cite>

> There is a perception that when new features are added to a system that those
> added and modified parts of the source-code are more fault prone. Many have
> argued that new code and new features are defect prone due to immaturity, lack
> of testing, as well unstable requirements. Unfortunately most previous work
> does not investigate the link between a concrete requirement or new feature
> and the defects it causes, in particular the feature, the changed code and the
> subsequent defects are rarely investigated. In this paper we investigate the
> relationship between improvements, new features and defects recorded within an
> issue tracker. A manual case study is performed to validate the accuracy of
> these issue types. We combine defect issues and new feature issues with the
> code from version-control systems that introduces these features; we then
> explore the relationship of new features with the fault-proneness of their
> implementations. We describe properties and produce models of the relationship
> between new features and fault proneness, based on the analysis of issue
> trackers and version-control systems. We find, surprisingly, that neither
> improvements nor new features have any significant effect on later defect
> counts, when controlling for size and total number of changes.

One piece of common wisdom in the software industry is that new code tends to be
buggier than old code, because it is immature and more poorly tested. But in
this short paper, Posnett, Hindle, and Devanbu present an interesting twist on
this. In the open source projects they studied, they found that although code
changes in general are associated with future defect fixing activity, as we
might expect, those changes that correspond to new feature development and to
code improvements are *not*. That's interesting and counter-intuitive—one would
expect new feature code commits to be among the buggiest. The authors offer a
possible explanation: well-established open source projects tend to be quite
conservative, and new feature code is heavily scrutinized, so that most defects
are found and sorted out before the code is integrated.  Which means that
projects that are not so careful might experience much more new feature pain.

-   Uses <span g="negative_binomial_regression">negative binomial regression</span>
    -   It can handle <span g="overdispersion">overdispersion</span> which is "almost always the case with software defect data"
-   Uses log of transformed lines of code and square root of number of commits because this gives a better fit
    -   But no underlying justification to explain the better fit is given
-   This one may be too clever for this course

## Software Developers' Perceptions of Productivity

<cite>Meyer2014</cite>

> The better the software development community becomes at creating software,
> the more software the world seems to demand. Although there is a large body of
> research about measuring and investigating productivity from an organizational
> point of view, there is a paucity of research about how software developers,
> those at the front-line of software construction, think about, assess and try
> to improve their productivity. To investigate software developers' perceptions
> of software development productivity, we conducted two studies: a survey with
> 379 professional software developers to help elicit themes and an
> observational study with 11 professional software developers to investigate
> emergent themes in more detail. In both studies, we found that developers
> perceive their days as productive when they complete many or big tasks without
> significant interruptions or context switches. Yet, the observational data we
> collected shows our participants performed significant task and activity
> switching while still feeling productive. We analyze such apparent
> contradictions in our findings and use the analysis to propose ways to better
> support software developers in a retrospection and improvement of their
> productivity through the development of new tools and the sharing of best
> practices.

One of the goals of software engineering researchers is to improve the
productivity of software developers. To show an improvement in productivity, you
need to be able to measure it, and that turns out to be a tricky thing to
do. Researchers have tried metrics such as lines of code per day, function
points per day and story points per iteration, but these are all ultimately
unsatisfying. Martin Fowler has gone so far as to assert that we cannot measure
productivity.

Yet, I suspect that every programmer has thought at one time or another "I
really got nothing today". Similarly, I'd wager that every programmer has had
days when they simply felt that they were more...well, productive. Like Justice
Potter Stewart said of pornography, when it comes to productivity, we know it
when we see it.

And so, it's a shock to discover that this is the first published research on
software developers' subjective sense of productivity. The authors conducted a
survey and an observational study to understand how productive programmers feel
when engaged in different tasks, as well as the impact of other factors such as
having clear goals or switching contexts.

The survey revealed that completing tasks and having few interruptions were the
top two reasons for a productive workday. The surveyed developers selected
coding as the most productive activity. Developers reported meeting as both the
most unproductive activity and the second most productive activity, a result
that manages to be both counter-intuitive and completely unsurprising (in
retrospect).

I personally find observational studies more interesting than surveys, and this
paper is no exception. For example, I would not have guessed that developers
spend only 3.9% of their time debugging compared to 32.3% of their time
coding. I was also surprised by the high rate of activity switching the authors
observed: 47 times per hour(!).

The challenge in this kind of observational research is applying the
results. The authors do make some suggestions about ways this information could
be used to improve productivity (e.g., monitoring tools, reducing context
switching, setting goals), but these aren't nearly as interesting as the results
themselves.

Still, even if we don't quite know what to do with this information yet, the
results are still important to help us to better understand how software
developers perceive their own productivity.

-   Calculates the mean of a <span g="likert_scale">Likert scale</span> (but isn't this a statistical sin?)
-   Contains data about frequency of task switching
-   Uses <span g="n_gram_analysis">n-gram analysis</span>

## Simple Testing Can Prevent Most Critical Failures

<cite>Yuan2014</cite>

> Large, production quality distributed systems still fail periodically, and do
> so sometimes catastrophically, where most or all users experience an outage or
> data loss. We present the result of a comprehensive study investigating 198
> randomly selected, user-reported failures that occurred on Cassandra, HBase,
> Hadoop Distributed File System (HDFS), Hadoop MapReduce, and Redis, with the
> goal of understanding how one or multiple faults eventually evolve into a
> user-visible failure. We found that from a testing point of view, almost all
> failures require only 3 or fewer nodes to reproduce, which is good news
> considering that these services typically run on a very large number of
> nodes. However, multiple inputs are needed to trigger the failures with the
> order between them being important. Finally, we found the error logs of these
> systems typically contain sufficient data on both the errors and the input
> events that triggered the failure, enabling the diagnose and the reproduction
> of the production failures. We found the majority of catastrophic failures
> could easily have been prevented by performing simple testing on error
> handling code—the last line of defense—even without an understanding of the
> software design. We extracted three simple rules from the bugs that have lead
> to some of the catastrophic failures, and developed a static checker,
> Aspirator, capable of locating these bugs. Over 30% of the catastrophic
> failures would have been prevented had Aspirator been used and the identified
> bugs fixed. Running Aspirator on the code of 9 distributed systems located 143
> bugs and bad practices that have been fixed or confirmed by the developers.

This is a wonderful study that explores the reasons why distributed systems fail
in production by analyzing the root causes of around 200 confirmed system
failures. The failures were reported against open-source projects that are used
to implement distributed systems, including Hadoop and Redis.

The trends in failure modes among these systems are fascinating and
actionable. The authors report many findings, but here are some key takeaways
for practitioners:

> [A]lmost all (92%) of the catastrophic system failures are the result
> of incorrect handling of non-fatal errors explicitly signaled in
> software.
> 
> [I]n 58% of the catastrophic failures, the underlying faults could
> easily have been detected through simple testing of error handling
> code.
> 
> A majority (77%) of the failures require more than one input event to
> manifest, but most of the failures (90%) require no more than 3.
> 
> For a majority (84%) of the failures, all of their triggering events
> are logged.

The lessons for software engineers are clear: put more effort into writing and
validating your error handling code, run your integration tests with a small
number of nodes (but greater than one), and examine your application logs to
diagnose failures.

This study also provides evidence for what Daniel Jackson calls the "small-scope
hypothesis": you can identify most defects through tests with a small number of
entities.

The authors developed a tool called Aspirator to help identify inadequate
error-handling in Java applications. But even if you don't write software in
Java, if you build distributed systems, you should read this paper.

## An Empirical Investigation into Programming Language Syntax

<cite>Stefik2013</cite>

> Recent studies in the literature have shown that syntax remains a significant
> barrier to novice computer science students in the field.  While this syntax
> barrier is known to exist, whether and how it varies across programming
> languages has not been carefully investigated. For this article, we conducted
> four empirical studies on programming language syntax as part of a larger
> analysis into the, so called, programming language wars. We first present two
> surveys conducted with students on the intuitiveness of syntax, which we used
> to garner formative clues on what words and symbols might be easy for novices
> to understand. We followed up with two studies on the accuracy rates of
> novices using a total of six programming languages: Ruby, Java, Perl, Python,
> Randomo, and Quorum. Randomo was designed by randomly choosing some keywords
> from the ASCII table (a metaphorical placebo). To our surprise, we found that
> languages using a more traditional C-style syntax (both Perl and Java) did not
> afford accuracy rates significantly higher than a language with randomly
> generated keywords, but that languages which deviate (Quorum, Python, and
> Ruby) did. These results, including the specifics of syntax that are
> particularly problematic for novices, may help teachers of introductory
> programming courses in choosing appropriate first languages and in helping
> students to overcome the challenges they face with syntax.

This paper is a follow-on to one we wrote about a couple of years ago that
generated a lot of comments, many of them unpleasant. Stefik responded then, and
he and Siebert have now followed up with several more studies that show:

1.  Programming language designers needlessly make programming languages
    harder to learn by not doing basic usability testing. For example,
    "...the three most common words for looping in computer science,
    for, while, and foreach, were rated as the three most unintuitive
    choices by non-programmers."

2.  C-style syntax, as used in Java and Perl, is just as hard for
    novices to learn as a randomly-designed syntax. Again, this pain is
    needless, because the syntax of other languages (such as Python and
    Ruby) is significantly easier.

They have also developed a technique called Token Accuracy Maps to make detailed
studies of language syntax more methodical, and are using this to improve the
design of a new language called Quorum that, wonder of wonders, incorporates
feedback from studies of novice programmers to eliminate stumbling blocks.

I would like to see every proposed change to widely-used languages go through
similar testing before being incorporated into standards. More than that, I
would like to see programmers demand this kind of evidence from language
designers (and each other). I suspect that would have a lot more impact than yet
another type system or any number of sermons on the beauty of functional
programming.

-   Uses QQ plots and histograms to verify distributions are normal enough
-   Uses a two-factor ANOVA with partial-eta values as a variance accounted for measure and Tukey HSD post-hoc tests.
-   Uses <span g="cohens_kappa">Cohen's kappa</span> for inter-rater reliability
-   Uses a repeated-measures ANOVA test
-   Uses <span g="mauchly_sphericity">Mauchly's test for sphericity</span>
    and the <span g="greenhouse_geisser_correction">Greenhouse-Geisser correction</span> where necessary

## Happy Software Developers Solve Problems Better

<cite>Graziotin2014</cite>

> For more than thirty years, it has been claimed that a way to improve software
> developers' productivity and software quality is to focus on people and to
> provide incentives to make developers satisfied and happy. This claim has
> rarely been verified in software engineering research, which faces an
> additional challenge in comparison to more traditional engineering fields:
> software development is an intellectual activity and is dominated by
> often-neglected human factors (called human aspects in software engineering
> research). Among the many skills required for software development, developers
> must possess high analytical problem-solving skills and creativity for the
> software construction process. According to psychology research, affective
> states-emotions and moods-deeply influence the cognitive processing abilities
> and performance of workers, including creativity and analytical problem
> solving. Nonetheless, little research has investigated the correlation between
> the affective states, creativity, and analytical problem-solving performance
> of programmers. This article echoes the call to employ psychological
> measurements in software engineering research. We report a study with 42
> participants to investigate the relationship between the affective states,
> creativity, and analytical problem-solving skills of software developers. The
> results offer support for the claim that happy developers are indeed better
> problem solvers in terms of their analytical abilities. The following
> contributions are made by this study: (1) providing a better understanding of
> the impact of affective states on the creativity and analytical
> problem-solving capacities of developers, (2) introducing and validating
> psychological measurements, theories, and concepts of affective states,
> creativity, and analytical-problem-solving skills in empirical software
> engineering, and (3) raising the need for studying the human factors of
> software engineering by employing a multidisciplinary viewpoint.

I've long harbored a suspicion that most of the technologies that we argue
about, (static/dynamic types, TDD, etc.), have little impact on the success of
software projects. Their effects, while potentially measurable in controlled
experiments, are swamped by the noise of the environments where software is
implemented. And so, if it doesn't really matter which technologies developers
use, why not just let them choose the ones that make them happiest? But this
approaches raises the question: do we actually get better outcomes with happier
developers?  That's the research question that Graziotin, Wang, and Abrahamsson
address in this paper.

Unfortunately, researchers haven't yet discovered how to induce happiness, so a
randomized controlled trial isn't an option. Instead, the authors measured
*affective states* (the term psychology researchers use to describe emotional
state) using a questionnaire developed by psychology researchers called the
SPANE.  They divided up the study participants into two equal groups based on
their questionnaire responses: a happier group which they called the positive
group (POS) and a less happy group which they called the non-positive group
(N-POS). The authors looked at how the two groups performed an analytical task
and a creative task.

For the analytical task, the authors used the Tower of London test, which is
similar to the Towers of Hanoi. They scored performance as a function of how
many trials the participant passed and how long it took to solve each trial. For
this problem, the POS group did much better, and the results were statistically
significant at p<.05. For the creative task, they showed the participants
images, and the participants had to invent captions for these images. Neither
quantity nor quality measures for this task showed statistically significant
differences between the two groups at p=.05, in contradiction with the results
of previous studies done by other authors.

Ultimately, what we want to know is *how much* developer happiness impacts
outcomes. The authors do report *d* values, which I assume is Cohen's d, an
effect size measure. Alas, I couldn't find the meaning of *d* explained in the
paper, so I can't be certain. For the analytic task, the authors report a
d=0.91. That sounds like an impressive result, given that Cohen considered a
d=0.8 to be a "large" effect in psychology research.  Unfortunately, we haven't
yet come up with conventions in software engineering research to characterize
small, medium and large effects.  The main takeaway from this study is: *happier
developers perform much better on analytic tasks*.

The authors report d=0.07 and d=0.10 for the creative quality measures, favoring
the N-POS group. They report d=0.41 for the creative quantity measure favoring
the POS group, which is somewhere between "small' and "medium" according to
Cohen's guidelines. Even though the authors didn't get statistically significant
results, a positive result would be consistent with one of the other studies
cited by the authors (Sowden & Dawson, 2011).

It seemed a bit odd that the tasks were not explicitly software related, making
the paper feel like a more traditional psychology study with a software
engineering spin. The creativity task did not use images that were related to
software development at all. The analytic task was more software-related, but
the participants had to solve the problem themselves rather than implement a
program to solve the problem. Still, it seems reasonable that these more generic
measures of creativity and analytic problem solving would be correlated with
performance on software engineering tasks.

-   Uses <span g="t_test">t-test</span>
-   Uses Cohen's *d*
-   Uses Mann-Whitney *U* test
-   Uses Shapiro-Wilk test

## Halving Fail Rates Using Peer Instruction

<cite>Porter2013</cite>

Peer Instruction (PI) is a teaching method that supports student-centric
classrooms, where students construct their own understanding through a
structured approach featuring questions with peer discussions. PI has been shown
to increase learning in STEM disciplines such as physics and biology. In this
report we look at another indicator of student success—the rate at which
students pass the course or, conversely, the rate at which they fail. Evaluating
10 years of instruction of 4 different courses spanning 16 PI course instances,
we find that adoption of the PI methodology in the classroom reduces fail rates
by a per-course average of 61% (20% reduced to 7%) compared to Standard
Instruction (SI). Moreover, we also find statistically significant improvements
within-instructor. For the same instructor teaching the same course, we find PI
decreases the fail rate, on average, by 67% (from 23% to 8%) compared to SI. As
an in-situ study, we discuss the various threats to the validity of this work
and consider implications of wide-spread adoption of PI in computing programs.

-   Uses <span g="z_test">z-test</span>

## How, and Why, Process Metrics are Better

<cite>Rahman2013</cite>

> Defect prediction techniques could potentially help us to focus
> quality-assurance efforts on the most defect-prone files. Modern statistical
> tools make it very easy to quickly build and deploy prediction
> models. Software metrics are at the heart of prediction models; understanding
> how and especially why different types of metrics are effective is very
> important for successful model deployment. In this paper we analyze the
> applicability and efficacy of process and code metrics from several different
> perspectives. We build many prediction models across 85 releases of 12 large
> open source projects to address the performance, stability, portability and
> stasis of different sets of metrics. Our results suggest that code metrics,
> despite widespread use in the defect prediction literature, are generally less
> useful than process metrics for prediction. Second, we find that code metrics
> have high stasis; they don't change very much from release to release. This
> leads to stagnation in the prediction models, leading to the same files being
> repeatedly predicted as defective; unfortunately, these recurringly defective
> files turn out to be comparatively less defect-dense.

Software engineering practices are often based on the 'guruisms' or pure
myth. However, in resent years researchers have empirically prove or disprove
some of these myths. One example is code cloning being considered as bad
practice. But why? A past review of Kapser and Godfrey's work stated that many
code clones are actually OK. Kapser and Godfrey found that as many as 71% of the
clones they studied could be considered to have a positive impact on the
maintainability of the software system. This isn't the only clones result that
denounces the "bad practice" premise: Rahman et al.'s "Clones: What is that
Smell?" found no evidence that cloning makes code more defect prone.

Here, Rahman et al. are exploring the question of "how" and "why" process
metrics are better than code metrics. In this "don't take my word for it" study,
the authors answer seven research questions comparing the performance,
stability, portability and stasis of these metrics. To answer the "how" they
found the following:

1.  Process metrics create significantly better defect predictors than
    code metrics across multiple learners.

2.  By using older project releases to predict for newer ones, they
    found no significant difference in the stability of process metrics
    and code metrics.

3.  Process metrics are more portable than code metrics, in other words,
    using data from one project to predict for another works better with
    process metrics.

4.  Process metrics are less static than code metrics: They change more
    than code metrics over releases.

To answer the "why" they found that code metrics have what the authors call
"high stasis": they don't change much over releases. This led them to conclude
that "...the stasis of code metrics leads to stagnant prediction models, that
predict the same files as defective over and over again".

Is this a bad thing? Their results show that not only do code metrics predict
for "recurringly" defective files, these files tend to be larger and less defect
dense, thus making code metric based predictors less cost effective. Considering
that the use of software metrics for defect prediction helps to prioritize
quality assurance activities, this paper definitely helps in the decision
process of which metrics to collect for software projects and why.

-   Uses a variety of sophisticated machine learning models
-   And then F-measure
