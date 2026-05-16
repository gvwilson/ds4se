# Claude

This project is an introduction to data science for undergraduates in
software engineering. The aim is to teach them enough statistics and
data analysis for them to understand, evaluate, and participate in
empirical studies of the impact of AI on software engineering.

## Audience

Learners have completed the first two years of an undergraduate degree
in Computer Science. They are comfortable writing Python and Java
programs that are hundreds of lines long, with using Git for version
control, and with writing unit tests. They learned a little bit of
statistics in high school, but haven't used it since. They are new to
Polars and Altair.  They frequently use LLM tools like Claude to
assist with homework assignments

## Content

-   Each lesson should take one hour to complete, including exercises.
    When in doubt, go slowly.

-   Each lesson is built around a separate small example, each drawn
    from an actual empirical study in software engineering.

-   Lesson content in each section is written as point-form lists
    using four-space indentation. *NEVER* put tab characters in files.
    Point-form lists may include sub-lists, but only one level deep.

-   Code is put in files in the lesson directory. These files are
    transcluded in the lesson using mccole's `%inc` tag. The shell
    command to run the code (if needed) is put in a `.sh` file in the
    lesson directory, which is also transcluded in the lesson.

-   The penultimate section of each lesson is an H2 titled `Check
    Understanding`. The content underneath this is a series of 3-5
    questions for learners to answer *without* using an LLM. At least
    one question must ask the learner to diagnose and fix a bug rather
    than simply recall or distinguish concepts. Each question is
    written as `<details markdown="1">`, followed by `<summary
    markdown="1">text of question</summary>` on a line of its own,
    followed by a blank line, followed by a paragraph answer and/or
    snippets of code, followed by a blank line, followed by
    `</details>`.

-   The final section of each lesson is an H2 titled `Exercises`. It
    is followed by 5-8 exercises, each of which has a brief H3 title
    followed by a paragraph describing the goal of the exercise.

## Stack

-   [bash](https://www.gnu.org/software/bash/): Unix shell
-   [git](https://git-scm.com/): version control
-   [uv](https://docs.astral.sh/uv/): package and environment management
-   [polars](https://pola.rs/): dataframes
-   [Vega-Altair](https://altair-viz.github.io/): charts
-   [SQLite](https://sqlite.org/): database
-   [ruff](https://astral.sh/ruff): linting
-   [taskipy](https://github.com/taskipy/taskipy): task runner

@~/.claude/mccole.md
