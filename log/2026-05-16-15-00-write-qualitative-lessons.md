# Write Qualitative Methods Lessons (19-21)

## Prompt

Write three lesson files for a data science for software engineers tutorial:
- Lesson 19: qualdata/index.md — What Qualitative Data Looks Like in SE Research
- Lesson 20: themes/index.md — Thematic Analysis
- Lesson 21: reliability/index.md — Coding Schemes and Inter-Rater Reliability
- Python code file: reliability/kappa.py

Detailed content outlines, glossary terms, bibliography keys, and style rules provided.

## Actions Taken

1. Read threats/index.md and an existing lesson for style reference
2. Read glossary/index.md to confirm glossary keys for the three new terms (qualitative_data,
   thematic_analysis, inductive_coding, deductive_coding, inter_rater_reliability, cohens_kappa,
   codebook)
3. Checked bibliography/index.md for citation keys: Ait2022, Silva2016, Hoda2024, Aghajani2019,
   Fan2024b, Wang2020a — all present
4. Created qualdata/index.md with 4 learning goals, 5 content bullets, 4 Check Understanding
   questions (including one bug question), and 5 exercises
5. Created themes/index.md with 4 learning goals, 7 content bullets, 4 Check Understanding
   questions (including one bug question), and 5 exercises
6. Created reliability/index.md with 4 learning goals, 8 content bullets, 4 Check Understanding
   questions (including one bug question), and 5 exercises; includes [%inc kappa.py %]
7. Created reliability/kappa.py — computes percent agreement and Cohen's kappa

## Key Decisions

- Used `[%g qualitative_data "qualitative data" %]` only in Lesson 19 (first introduction);
  subsequent lessons reference it in prose without re-linking
- Inductive and deductive coding glossary terms introduced in Lesson 20 only
- Inter-rater reliability, Cohen's kappa, codebook glossary terms introduced in Lesson 21 only
- Bug questions use prose description of the bug (Lessons 19 and 21) or code snippet (Lesson 21)
  as appropriate to the lesson content
- kappa.py reformatted slightly from spec: multiline ternary for label to avoid line length issues
