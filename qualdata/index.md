# What Qualitative Data Looks Like in SE Research

## Learning Goals

-   Distinguish [%g qualitative_data "qualitative data" %] from quantitative data and explain when each is appropriate
-   Identify types of qualitative data that appear in SE research
-   Explain how Ait et al. used quantitative data to raise a question that qualitative methods then began to answer
-   Read Silva et al.'s refactoring study as an example of qualitative coding applied to a quantitative data source

## Lesson

-   Quantitative data is counts and measurements: number of commits, lines of code, defect rate, star count
    -   Qualitative data is language: interview transcripts, open survey responses, code review comments,
        issue tracker text, commit messages, Stack Overflow posts
    -   The goal of quantitative analysis is to measure frequency and magnitude
    -   The goal of qualitative analysis is to understand meaning, context, and motivation
-   SE research produces qualitative data in many forms
    -   Interview transcripts: asking developers why they made a decision or stopped contributing
    -   Open survey responses: free-text answers to questions like "what slows you down most?"
    -   Code review comments: reviewers explaining what they want changed and why
    -   Issue tracker text: bug reports describing what happened and what was expected
    -   Commit messages: developers describing what they changed and, occasionally, why
    -   Stack Overflow posts: questions and answers about programming problems
-   Hoda [%b Hoda2024 %] provides a practitioner-focused introduction to qualitative methods in SE
    -   Qualitative work is not easier than quantitative work
    -   It is harder to do rigorously and harder to convince readers to trust
    -   The difficulty is not in collecting the data but in interpreting it consistently
-   Qualitative methods are the right choice in three situations
    -   You do not yet know what the important variables are
    -   The phenomenon involves judgment, motivation, or social context that numbers cannot capture
    -   Numbers exist but do not explain the pattern you found
-   Ait et al. studied survival rates of GitHub projects [%b Ait2022 %]
    -   Their quantitative finding: most GitHub projects go inactive within a few years of creation
    -   Survival curves tell you when projects die; they do not explain why
    -   Interviews with maintainers reveal the reasons: burnout, loss of interest, employer pressure,
        feeling underappreciated by users
    -   The quantitative result raises the question; the qualitative result begins to answer it
-   Silva et al. studied why developers refactor [%b Silva2016 %]
    -   They read 548 commit messages from GitHub and classified each one into a motivational theme
    -   The data source is quantitative (GitHub commits); the analysis is qualitative (reading and
        interpreting text)
    -   This combination appears often in SE research: mine a repository for text, then code the text
    -   The themes they identified included "fixing a bug," "improving design," and "enabling a new feature"
    -   None of those themes could be identified by counting keywords; you have to read for meaning

## Check Understanding

<details markdown="1">
<summary markdown="1">What distinguishes qualitative data from quantitative data? Give one example of each from the same GitHub repository.</summary>

Quantitative data consists of counts or measurements that can be compared numerically: for example,
the number of open issues in a repository. Qualitative data consists of text or other non-numerical
content that has to be interpreted for meaning: for example, the text of those issue descriptions,
which might reveal whether developers are frustrated, confused, or requesting enhancements. Both
come from the same repository, but they answer different questions.

</details>

<details markdown="1">
<summary markdown="1">A researcher wants to study developer frustration during code review. Their approach is to count the number of words in each review comment and use that count as a measure of frustration. What is wrong with this approach and what should they do instead?</summary>

Word count is a proxy for frustration, and a bad one. A long comment might be a patient explanation
of a complex issue, not a frustrated rant. A short comment might be curt and hostile. Word count
measures length, not sentiment or emotion. The researcher is substituting something easy to measure
for something meaningful but hard to measure. A better approach would be to read a sample of comments
and code them for frustration directly, using a defined scheme, then measure agreement between two
coders. Alternatively, they could recruit developers to rate comments on a frustration scale, which
at least grounds the measure in human judgment.

</details>

<details markdown="1">
<summary markdown="1">When is qualitative research the right choice? Give two criteria and one example from SE research.</summary>

Qualitative research is appropriate when you do not yet know what the important variables are,
so you cannot write a survey with fixed-response options. It is also appropriate when the phenomenon
involves social or motivational factors that numbers cannot capture. The Ait et al. study illustrates
both: before interviewing maintainers about why projects go inactive, researchers did not know
whether the cause was technical (no one could merge contributions), social (maintainers burned out),
or economic (employers withdrew support). A survey with fixed options would have assumed answers to
a question that was still open.

</details>

<details markdown="1">
<summary markdown="1">Hoda [%b Hoda2024 %] argues qualitative work is harder to do rigorously than quantitative work. What makes it harder?</summary>

In quantitative work, the analysis pipeline is mostly fixed once the data is collected: apply a
statistical test, report a p-value and effect size. In qualitative work, the researcher is the
instrument. Two people reading the same interview can reach different conclusions depending on
their background, assumptions, and what they noticed first. Making the analysis rigorous requires
documenting every interpretive choice, having multiple coders work independently and measuring
their agreement, and being transparent about how themes were constructed. There is no statistical
test that can substitute for that kind of disciplined attention to the text.

</details>

## Exercises

<div class="exercise" markdown="1">
### Reading commit messages for motivation

Find five recent commit messages in any open-source repository on GitHub. For each one, write one
sentence describing the developer's apparent motivation. Compare your interpretations with a partner:
where did you agree, where did you disagree, and what does each disagreement reveal about the
difficulty of reading intent from a short text?
</div>

<div class="exercise" markdown="1">
### Writing open-ended interview questions

The Ait et al. study counts inactive projects but cannot explain why they went inactive from
survival data alone. Write three interview questions you would ask a former maintainer to understand
why they stopped contributing. Each question must be open-ended (cannot be answered with yes or no)
and non-leading (does not hint at the answer you expect). For each question, write one sentence
explaining what kind of information it is designed to surface.
</div>

<div class="exercise" markdown="1">
### Critiquing a proxy measure

A colleague proposes to measure "developer satisfaction" by running a sentiment classifier over
commit messages and computing the fraction of positive-sentiment commits per developer per month.
Identify two specific ways this approach might mislead you that a survey with open-ended questions
would not. For each problem, write one sentence describing what the open-ended question would
reveal that the automated measure would miss.
</div>

<div class="exercise" markdown="1">
### Sorting phenomena by method

List three SE phenomena that you think quantitative methods handle well and three that you think
require qualitative investigation. For each of your three qualitative examples, write one sentence
stating the specific question you would be trying to answer and one sentence explaining why a count
or measurement would not be sufficient to answer it.
</div>

<div class="exercise" markdown="1">
### Diagnosing a common mistake

Read the abstract of Hoda [%b Hoda2024 %] and identify what the author describes as the most
common mistake researchers make when analyzing qualitative data. Write one sentence summarizing
the mistake and one sentence explaining how you would avoid it in your own work. Then write a
prompt you could give to an LLM to help you detect that mistake when reviewing a qualitative
methods section:

> [your prompt here]
</div>
