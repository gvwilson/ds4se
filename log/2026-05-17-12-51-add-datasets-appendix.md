# Add Datasets Appendix

## Prompt

Add an appendix 'datasets' with a complete list of the datasets required by all tutorials,
including dataset name, URL if available, list of slugs of lessons where it's used, and
brief description.

## Actions

1. Ran `brief .` for project overview.
2. Used Explore agent to scan all lesson Python files and index.md files for dataset references.
3. Verified dataset list by grepping `*/*.py` for `read_csv` calls.
4. Checked `_extras/links.md` for existing URLs.
5. Created `datasets/index.md` with 16 dataset entries (14 files, with 3 separate commit files listed individually).
6. Added three new link keys to `_extras/links.md` (numpy-github, sklearn-github, shell-novice-github).
7. Added `[Datasets](@/datasets/)` to the appendices list in `README.md`.

## Datasets Catalogued

- `copilot_snippets.csv` — aitools
- `educator_rankings.csv` — nonpar
- `fucci_replication.csv` — design
- `fucci_tdd.csv` — effectsize, tddlab
- `github_repos.csv` — threats
- `jccpprtTR.csv` — intro, visualize
- `js_func_counts.csv` — grouping, correlate
- `js_line_lengths.csv` — hypotest
- `line_lengths.csv` — tidy, pep8lab
- `numpy_commits.csv` — mining
- `programmer_hours.csv` — compare
- `py_func_counts.csv` — grouping, visualize, correlate
- `py_line_lengths.csv` — hypotest
- `pypi_releases.csv` — describe
- `scikit-learn_commits.csv` — mining
- `shell-novice_commits.csv` — mining
