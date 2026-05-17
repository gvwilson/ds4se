# Thematic Analysis

## Learning Goals

-   Apply the six-step Braun & Clarke process for [%g thematic_analysis "thematic analysis" %] to a small dataset
-   Distinguish [%g inductive_coding "inductive coding" %] from [%g deductive_coding "deductive coding" %] and choose appropriately
-   Explain how Aghajani et al. and Fan et al. used thematic analysis in SE research
-   Recognize what automatic sentiment analysis misses that thematic analysis captures

## Lesson

-   Thematic analysis identifies, analyzes, and reports patterns (themes) in textual data
    -   A theme is not a keyword; it is a pattern of meaning that recurs across the data
    -   Counting how often the word "frustration" appears is not thematic analysis
    -   The researcher is the instrument: two researchers reading the same data might identify
        different themes, which is why transparency about choices matters
-   Braun & Clarke describe a six-step process
    -   Step 1 — Familiarize yourself with the data: read everything before you code anything;
        take notes about what strikes you, but do not commit to categories yet
    -   Step 2 — Generate initial codes: label short segments of text with a phrase describing
        what that segment is about; aim for many codes at first, not a tidy taxonomy
    -   Step 3 — Search for themes: look across your codes and group the ones that seem to
        be about the same underlying idea into candidate themes
    -   Step 4 — Review themes: read all the data that falls under each candidate theme and
        ask whether it holds together; if a theme contains contradictory material, split it;
        if two themes are really the same idea, merge them
    -   Step 5 — Define and name themes: write a sentence or two describing what each theme
        captures and what distinguishes it from neighboring themes
    -   Step 6 — Write up: illustrate each theme with direct quotes from the data; the quotes
        do the work of convincing readers that the theme is real
-   Aghajani et al. analyzed 878 documentation artifacts from mailing lists, Stack Overflow,
    issue trackers, and pull requests [%b Aghajani2019 %]
    -   They identified themes such as "incorrect documentation," "incomplete examples," and
        "missing rationale" through open reading, not keyword search
    -   A keyword search for "incorrect" would have missed every comment that described
        inaccurate documentation without using that word
-   Fan et al. used thematic analysis on community discussions about protestware [%b Fan2024b %]
    -   Protestware is open-source software modified to protest a political or social cause
    -   Themes they identified included "normative disagreement" (is this acceptable behavior?)
        and "platform responsibility" (should npm or GitHub have intervened?)
    -   Neither theme would appear in a word-frequency list; they require reading for argument
-   Inductive coding lets themes emerge from the data without a prior framework
    -   You start with an open mind and build the category system from what you see
    -   Appropriate when a phenomenon is poorly understood or when you suspect existing frameworks
        will miss something important
-   Deductive coding applies a predefined framework or set of categories
    -   You start with a list of codes derived from theory or prior work and apply them to the data
    -   Appropriate when replicating a previous study or testing whether an established framework
        applies to a new context
-   Most SE qualitative work is inductive on first pass, then deductive on replication
    -   A first study might inductively identify five themes in how developers describe technical debt
    -   A replication study then applies those five themes deductively to a new dataset and checks
        whether they still appear

## Check Understanding

<details markdown="1">
<summary markdown="1">What is the difference between a code and a theme in thematic analysis?</summary>

A code is a label applied to a short segment of text describing what that segment is about. It is
local and specific: a code might be "developer blames tooling" or "user asks for an example." A
theme is a higher-level pattern that groups multiple codes together around a shared meaning. The
theme "frustration with the development environment" might collect codes about tooling complaints,
environment setup problems, and debugging difficulties from many different places in the data. Codes
are the raw material; themes are the result of interpreting that material.

</details>

<details markdown="1">
<summary markdown="1">A researcher codes 200 issue comments and reports "I found five themes by grouping the comments that used similar words." What is missing from this approach and which step of the Braun & Clarke process did they skip?</summary>

Grouping by similar words is keyword clustering, not thematic analysis. The researcher skipped
step 4 (reviewing themes) and arguably never completed step 2 correctly, since codes should
capture meaning rather than vocabulary. Two comments can use the same word with opposite meanings,
and two comments can describe the same idea with completely different words. The result of grouping
by words is a vocabulary taxonomy, not a meaning taxonomy. What is missing is any evidence that the
researcher read the data for meaning, checked that each candidate theme held together, and revised
themes that were internally inconsistent.

</details>

<details markdown="1">
<summary markdown="1">Why is automatic sentiment analysis (positive, neutral, negative) not a substitute for thematic analysis?</summary>

Sentiment classifiers answer one narrow question: is this text expressing a positive or negative
attitude? Thematic analysis answers a much richer set of questions: what are people actually
saying, what arguments are they making, what concerns recur, and how do different kinds of
responses relate to each other? A comment classified as "negative" by a sentiment model might be
a technical objection, a personal complaint, a normative disagreement, or a request for
clarification. Sentiment analysis collapses all of those into a single label and loses everything
that would let you understand what is actually happening.

</details>

<details markdown="1">
<summary markdown="1">Aghajani et al. read 878 artifacts rather than using keyword search. What would keyword search have missed?</summary>

Keyword search finds text that contains a specific word or phrase. It would have missed every case
where a developer described a documentation problem using non-standard vocabulary, hedged language,
or indirect phrasing. It also cannot identify the absence of information: "incomplete examples" is
a theme about what documentation fails to include, and no keyword signals that absence. More
broadly, keyword search cannot group things by meaning — it groups things by surface form, which
often produces the wrong groupings and misses real ones.

</details>

## Exercises

<div class="exercise" markdown="1">
### Coding Stack Overflow comments

Read ten Stack Overflow comments on any Python or JavaScript question. Generate at least five
initial codes describing what the comments are doing, for example: "corrects an error in the
accepted answer," "asks for clarification," "provides an alternative solution," "warns about a
version-specific behavior." Group your codes into two or three candidate themes, and write one
sentence describing each theme. For at least one theme, identify a comment that almost fits but
that you decided to exclude, and explain why.
</div>

<div class="exercise" markdown="1">
### Finding examples of a documentation theme

Aghajani et al. identified a taxonomy of documentation issues that includes categories such as
"incorrect documentation," "incomplete examples," and "missing rationale." Pick one category from
their taxonomy, then find three real examples of it in the documentation of any open-source library
you have used. For each example, write one sentence explaining why it fits the category you chose,
and one sentence describing how a reader encountering that documentation problem would be affected.
</div>

<div class="exercise" markdown="1">
### When sentiment scoring goes wrong

A study classifies GitHub issue comments as "positive," "neutral," or "negative" using an
off-the-shelf sentiment analysis library. Identify two types of comments where automatic sentiment
scoring would assign the wrong label, and write one sentence for each explaining why the classifier
fails. For each case, describe what a human coder would need to know to assign the correct label
that the classifier cannot know from the text alone.
</div>

<div class="exercise" markdown="1">
### Documenting an interpretive choice

Thematic analysis requires the researcher to make choices that another researcher might make
differently. Return to the ten Stack Overflow comments you coded in the first exercise and identify
one decision you made about where to draw a boundary between two codes or two themes. Describe the
decision in one sentence, explain in one sentence why a different researcher might have drawn that
boundary differently, and write two sentences describing how you would document that choice in a
published paper so that a reader could evaluate your reasoning.
</div>

<div class="exercise" markdown="1">
### Evaluating threats to validity in a qualitative paper

Find the threats-to-validity section of any qualitative SE paper. Identify the threat the author
discusses most prominently and write one sentence summarizing it. Write two more sentences
evaluating whether the proposed mitigation is convincing: what does it address, and what does it
leave unresolved? Then write a prompt you could give to an LLM to help you identify threats to
validity in a qualitative methods section:

> [your prompt here]
</div>
