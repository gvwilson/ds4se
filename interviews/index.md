# Interviews and Survey Open-Ends

## Learning Goals

-   Design a semi-structured interview guide using appropriate question types
-   Distinguish leading, binary, and double-barreled questions from useful interview questions
-   Choose between purposive sampling and snowball sampling and explain the trade-offs
-   Apply ethical principles from [%b Gold2020 %] to interview research design

---

-   Semi-structured interviews: a prepared list of topics, but the interviewer follows the conversation rather than reading a script
    -   The most common qualitative method in SE research
    -   Preparation matters: pilot your questions with someone not in your sample before you interview anyone who counts
    -   Record and transcribe with consent; field notes are a poor substitute for verbatim transcripts

-   Question types to use:
    -   Grand tour: "Walk me through the last time you reviewed someone's code" — opens a complete episode without specifying what you expect to hear
    -   Experience: "Tell me about a time a tool surprised you" — anchors the conversation in a specific memory rather than a general opinion
    -   Probing: "Can you say more about that?" and "What happened next?" — lets the participant lead while keeping the conversation moving

-   Question types to avoid:
    -   Leading: "Don't you think pull requests improve quality?" — the answer is already embedded in the question
    -   Binary: "Do you use code reviews? Yes or no" — a yes/no answer tells you nothing about how, when, or why
    -   Double-barreled: "How do you feel about pair programming and mob programming?" — you cannot tell which practice the participant is commenting on

-   Ameller et al. [%b Ameller2012 %] interviewed 18 developers at different companies about how they handle non-functional requirements in practice
    -   The findings contradicted several textbook recommendations about how NFRs should be documented and tracked
    -   Semi-structured interviews were necessary because textbook prescriptions had not predicted what developers actually did

-   Survey open-ends: shorter responses, larger N, but less depth than interviews
    -   Useful for validating or extending qualitative findings at scale once you know what categories exist
    -   Begel & Zimmermann [%b Begel2014 %] combined structured ratings with open-ended responses to understand what questions practitioners most wanted researchers to answer
    -   The open-ended responses revealed priorities that a fixed-response survey would not have captured

-   Sampling in qualitative work:
    -   [%g purposive_sampling "Purposive sampling" %]: select participants who have relevant experience — you want developers who have actually done code review, not random employees
    -   [%g snowball_sampling "Snowball sampling" %]: ask participants to refer others with relevant experience, used when the target population is hard to identify directly
    -   Random sampling is rarely used and rarely appropriate in qualitative work, because randomness makes no sense when you are looking for people with specific knowledge

-   Ethical considerations: consent, anonymization, right to withdraw, data retention
    -   Participants must know what the data will be used for before they agree to be recorded
    -   Gold & Krinke [%b Gold2020 %] extend these concerns to mined data where participants never consented to being studied: public does not mean consented to research use

## Check Understanding

<details markdown="1">
<summary markdown="1">What makes a question "leading"? Rewrite this question to make it non-leading: "Don't you find that test-driven development improves code quality?"</summary>

A leading question signals the answer the interviewer expects, making it socially awkward for the participant to disagree. "Don't you find that..." presupposes the answer is yes. A non-leading version removes the presupposition: "How has writing tests before code affected the quality of your work, if at all?" or more simply, "Walk me through your experience with test-driven development."

</details>

<details markdown="1">
<summary markdown="1">A researcher interviews developers about their debugging practices; all participants are the researcher's current colleagues. What is wrong with this sampling strategy and what should the researcher do instead?</summary>

The researcher's colleagues share a workplace, a codebase, a toolchain, and possibly a team culture. Any finding will reflect that specific environment, not debugging practice in general. This is also a convenience sample rather than a purposive one: the participants were chosen because they were available, not because they represent the range of debugging experience relevant to the research question. The researcher should define the target population more precisely (e.g., developers with at least three years of experience debugging production systems in a compiled language) and recruit participants who fit that definition from outside their immediate workplace, using purposive or snowball sampling.

</details>

<details markdown="1">
<summary markdown="1">What is the difference between purposive sampling and snowball sampling? When would you use each?</summary>

Purposive sampling means selecting participants because they have specific characteristics relevant to your research question. You define the criteria in advance and recruit accordingly. Snowball sampling means asking participants to refer others who might qualify. Purposive sampling is appropriate when you can identify potential participants directly — for example, by searching LinkedIn for developers who have contributed to a specific type of project. Snowball sampling is appropriate when the target population is hard to identify from the outside — for example, developers who have experienced burnout, who are unlikely to self-identify publicly.

</details>

<details markdown="1">
<summary markdown="1">Why do Ameller et al.'s findings about non-functional requirements matter for how SE courses teach requirements engineering?</summary>

If courses teach that non-functional requirements should be documented in a structured format and tracked through a requirements management tool, but practitioners systematically handle them differently, students are learning a process they will never use. Ameller et al.'s interviews revealed that the actual practice diverges from the prescribed process in specific, describable ways. That gap is exactly the kind of finding that should feed back into curricula — and it required interviews to discover, because no survey instrument would have known to ask the right questions about informal practices.

</details>

## Exercises

<div class="exercise" markdown="1">
### Writing an interview guide

Write five interview questions for a study about how developers choose between writing tests before or after writing code. At least two questions must be grand-tour or experience questions. None may be leading, binary, or double-barreled. For each question, write one sentence explaining what type of information it is designed to surface and why that information is relevant to your research question.
</div>

<div class="exercise" markdown="1">
### Converting a question to a survey item

Take one of the questions you wrote in Exercise 1 and rewrite it as a Likert-scale survey item (1 = strongly disagree, 5 = strongly agree). Write one sentence explaining what information the quantitative version captures that the interview question does not, and one sentence explaining what information the interview question captures that the Likert scale cannot. Then write one sentence about when you would use each format.
</div>

<div class="exercise" markdown="1">
### Probing non-functional requirements

Ameller et al. found that developers handle non-functional requirements in ways that differ from textbook prescriptions. Pick one non-functional requirement type — performance, security, or usability — and write two interview questions that would reveal how a developer actually handles it day-to-day, without assuming they follow any particular documented process. For each question, write one sentence explaining why it avoids the leading/binary/double-barreled pitfalls.
</div>

<div class="exercise" markdown="1">
### Evaluating a sampling strategy

A study recruits interview participants by posting on Reddit and Twitter. Identify two specific ways this sampling strategy might bias the findings — think about who uses those platforms, who responds to research recruitment posts, and what that implies about whose experience is captured. For each bias, propose one mitigation and write one sentence explaining what the mitigation costs in time, money, or access.
</div>

<div class="exercise" markdown="1">
### Explaining saturation to a skeptical supervisor

You conduct 12 interviews and your supervisor asks how you know you have enough. Write a three-sentence response that explains theoretical saturation in plain language and describes one specific piece of evidence from your interviews that would support the claim that saturation has been reached — not just the assertion that you reached it. Then write a prompt you could give an LLM to help you evaluate whether your interview data shows signs of saturation:

> [your prompt here]
</div>
