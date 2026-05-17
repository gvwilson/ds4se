# AI Tools and Software Engineering

## Learning Goals

-   Summarize the empirical evidence on Copilot's productivity, correctness, and security weaknesses
-   Distinguish what the research shows from what is currently unknown
-   Classify Copilot-generated code snippets using Fu et al.'s security taxonomy
-   Design a study to measure Copilot's impact on developer productivity

## Productivity Claims

-   GitHub's own studies report 55% faster task completion when developers use Copilot
    -   The studies used isolated programming tasks, not sustained work on real codebases
    -   Control conditions varied across studies and were not always pre-specified
    -   External validity is contested: a developer writing a sorting function under observation is not doing what most developers do most of the time
-   Noda et al. argue that productivity is multidimensional and that simple metrics miss most of it [%b Noda2023 %]
    -   Developer experience (DevEx) includes flow state, cognitive load, and feedback speed, not just output
    -   A study that counts lines of code written per hour measures one thing and ignores a dozen others
    -   Any claim that a tool "increases productivity by X%" should prompt the question: productivity at what, measured how, for whom?

## Code Quality and Security

-   Fu et al. analyzed Copilot-generated code found in public GitHub repositories and identified 435 snippets with security weaknesses [%b Fu2024 %]
    -   The most common categories were memory management errors, injection vulnerabilities, and weak cryptography
    -   Copilot reproduces insecure patterns from its training data: if the internet is full of MD5 password hashing, Copilot will suggest MD5 password hashing
    -   Finding the vulnerability in generated code requires the same security knowledge you would need to write secure code yourself
-   El Haji et al. studied Copilot for test generation in Python [%b ElHaji2024 %]
    -   Generated tests were syntactically correct more than 80% of the time
    -   However, assertions were often trivially weak: checking that a function returns something rather than checking that it returns the right thing
    -   Edge cases — empty inputs, boundary values, type errors — were consistently underrepresented
-   Nguyen and Nadi evaluated Copilot on LeetCode problems across multiple programming languages [%b Nguyen2022 %]
    -   Correctness rates varied substantially by problem difficulty: high on easy problems, much lower on medium and hard ones
    -   Rates also varied by language, with Python performing better than some other languages
    -   LeetCode problems are not representative of production code, but they provide a reproducible benchmark
-   Huang et al. found that LLM-generated code can reflect social biases related to age, gender, and race [%b Huang2023b %]
    -   Prompts that mentioned different demographic groups produced code with systematically different variable names, comments, and algorithmic choices
    -   Bias in generated code matters most when that code allocates resources or makes decisions about people
-   Furia et al. showed that standard frequentist analyses of code quality data often lead to conflicting conclusions depending on how confounds are handled [%b Furia2022 %] [%b Furia2023 %]
    -   The same dataset about programming languages and code quality can support opposite conclusions depending on what is controlled for
    -   This does not mean the data are useless; it means interpretation requires care about what the model actually assumes

## What We Do Not Yet Know

-   Long-term effects on code maintainability have not been studied at scale
    -   Short-term task completion speed is easy to measure; six-month code review burden is not
-   Whether AI tools help or harm junior developers' skill development is an open question
    -   If generated code is a scaffold, it may accelerate learning; if it is a crutch, it may prevent it
    -   No longitudinal study with a proper control group has answered this
-   How productivity gains distribute across team roles is unknown
    -   Most studies recruit individual developers on isolated tasks; collaboration, code review, and architecture work are not captured
-   Cappendijk et al. point out that the electricity demands of running LLMs must be weighed against any productivity benefits [%b Cappendijk2024 %]
    -   A tool that saves a developer twenty minutes while consuming significant energy may or may not be net positive
    -   Energy cost is almost never included in productivity studies, which means reported gains are systematically overstated

## Code

[%inc classify_snippets.py %]

## Check Understanding

<details markdown="1">
<summary markdown="1">What two threats to validity apply to GitHub's own report that Copilot increases task completion speed by 55%?</summary>

The first is lack of external validity: the studies used short, isolated programming tasks that are not representative of the complex, context-dependent work most developers do day-to-day. The second is conflict of interest in the control conditions: GitHub has a financial interest in Copilot's success, and the comparison conditions were not always pre-specified or independently reviewed. A 55% improvement on a contrived task tells you something, but it is not the same as a 55% improvement in daily developer output.

</details>

<details markdown="1">
<summary markdown="1">What is wrong with this function, and how would you fix it?

```python
import hashlib
def store_password(password):
    return hashlib.md5(password.encode()).hexdigest()
```
</summary>

MD5 is a cryptographically broken hash function. It was designed for fast checksum computation, not password storage, and it is trivially attacked with rainbow tables or GPU-accelerated brute force. The fix is to use a password hashing function designed for this purpose, such as `bcrypt`, `scrypt`, or `argon2`. These are deliberately slow and include salting by default:

```python
import bcrypt
def store_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

This is exactly the kind of vulnerability Fu et al. found in Copilot-generated code: the model learned from a training corpus that contains many examples of MD5 password hashing, so it reproduces the pattern confidently.

</details>

<details markdown="1">
<summary markdown="1">Huang et al. found that LLM-generated code can reflect social biases related to age, gender, and race. Why does this matter for software that allocates resources or makes decisions about people?</summary>

If a model's code generation is sensitive to demographic cues in prompts — producing different variable names, assumptions, or algorithmic choices depending on whether a persona is described as young or old, male or female — then software written with that assistance may embed those same biases into systems that allocate jobs, loans, healthcare resources, or legal outcomes. A developer who does not check for this cannot know whether the code they shipped reflects their intent or the model's training distribution.

</details>

<details markdown="1">
<summary markdown="1">Why does Cappendijk et al. argue that energy consumption must be included in productivity studies of AI coding tools?</summary>

Running a large language model at inference requires substantial electricity. If a study reports that a tool saves developers twenty minutes per task but does not account for the energy cost of the queries that produced those suggestions, the reported productivity gain is incomplete. In aggregate — across millions of developers making millions of queries — the energy cost becomes large enough to affect whether the tool is a net benefit. Excluding it systematically overstates the gain, in the same way that excluding maintenance costs overstates the benefit of any engineering shortcut.

</details>

## Exercises

<div class="exercise" markdown="1">

### Study Design

You have been asked to run a study at your company to determine whether Copilot increases developer productivity. You have six months and can recruit twenty developers. Sketch the study design, including what you will measure, what you will control for, what your comparison condition is, and three threats to validity you are most worried about. Then identify which of Fucci's methodological choices — multi-site recruitment, blind analysis, and pre-specified outcomes — you would borrow and explain why each one you select addresses a specific threat you identified.

</div>

<div class="exercise" markdown="1">

### Testing for Demographic Bias

Huang et al. found that LLM-generated code can reflect social biases. Design a minimal experiment to test whether Copilot generates code of different quality or uses different naming conventions depending on whether the prompt uses a stereotypically male versus female name for the developer persona. Write three sentences: one stating your hypothesis, one explaining how you will operationalize "code quality," and one identifying a threat to validity in your design. Write your test prompts as blockquotes so they are clearly separated from your analysis:

> Write a function that validates an email address. The function will be written by [NAME].

</div>

<div class="exercise" markdown="1">

### Adding Energy Costs

Cappendijk et al. argue that energy consumption of LLM-generated code should be included in productivity studies. Identify one existing Copilot productivity study discussed in this lesson. Write two sentences explaining what data you would need to collect in order to add an energy cost estimate to that study's reported productivity gains, and note one reason this data would be difficult to obtain in practice.

</div>

<div class="exercise" markdown="1">

### Benchmark Design

Nguyen and Nadi found that Copilot's correctness rate varies by problem difficulty. If you were designing a benchmark to evaluate a new code-generation tool fairly, what three categories of tasks would you include and why? Write one sentence per category, explaining what that category tests that the others do not.

</div>

<div class="exercise" markdown="1">

### Test Adequacy Rubric

El Haji et al. found that Copilot-generated tests lack meaningful assertions. Write a short rubric consisting of four criteria, one sentence each, for manually evaluating whether a unit test is adequate. Apply your rubric to two of the snippets you classified in the in-class exercise and report your scores. Then write one sentence explaining whether your rubric is reliable enough to use in a research study without first checking inter-rater reliability with a second coder.

</div>
