# Rewrite Tutorial to Match plan.txt

**Date**: 2026-05-17 01:13 UTC
**Prompt**: Completely rewrite this tutorial to match plan.txt. Use terse point-form outlines of lesson content but full descriptions for exercises. Rename lesson slugs as appropriate. Include H2 "Learning Goals" at top of each lesson. Exercises section must have H2 "Exercises" and each exercise must be wrapped in an 'exercise' div and have its own H3. Make sure bibliographic references resolve. Make sure each glossary term is defined exactly once, the first time it is used. Move any unused material to 'unused'. Take material already in 'unused' to insert in lessons if useful. Get bibliographic information from $HOME/bibliography/bib/*.bib as needed. If you include sample code, put that code in .py, .sql, or .sh files in the lesson's subdirectory and transclude it using %inc. Use blockquotes starting with '>' for LLM prompts.

## Actions taken

- Created 24 lesson directories (3 days + optional Day 4 qualitative)
- Renamed slugs: intro, tidy, grouping, visualize, describe, pep8lab, hypotest, compare, effectsize, correlate, threats, tddlab, mining, nonpar, design, aitools, reading, capstone, qualdata, themes, reliability, grounded, interviews, mixed
- Moved dataframes/, size/, finale/ to unused/
- Rewrote bibliography/index.md with all references from plan.txt (plus 3 entries written from plan.txt descriptions: Devanbu2016, Dyba2006, Flint2021)
- Rewrote glossary/index.md with all terms, each defined once
- Updated README.md with new lesson order
- Updated _extras/links.md with needed external links
- Wrote sample .py files in each lesson dir; transcluded with %inc
- FIXME note in plan.txt (Lesson 6 reuses Prechelt): changed Lesson 6 lab to replicate Bafatakis et al. PEP 8 compliance study instead
