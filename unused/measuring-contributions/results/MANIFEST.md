- path: gini-blame.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Gini coefficients for repositories measured with line-by-line blame in final state of repository"
  where: "From data/history-*.csv"
  when: 2019-12-15
  how: "Using bin/blame.py"
  fields:
  - name: filename
    type: text
    content: name of source file
  - name: gini_blame
    type: number
    content: Gini coefficient measuring number of lines per person in final state of repository

- path: gini-history.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Gini coefficients for repositories measured by commits and lines"
  where: "From data/history-*.csv"
  when: 2019-12-15
  how: "Using bin/history.py"
  fields:
  - name: filename
    type: text
    content: name of source file
  - name: gini_commits
    type: number
    content: Gini coefficient measuring number of commits per person
  - name: gini_lines
    type: number
    content: Gini coefficient measuring number of lines committed per person

- path: correlation.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Correlation coefficients between number of commits and final number of lines"
  where: "From data/history-*.csv"
  when: 2019-12-15
  how: "Using bin/correlation.py"
  fields:
  - name: stem
    type: text
    content: repository identifier
  - name: pearson
    type: number
    content: Pearson correlation coefficient
  - name: spearman
    type: number
    content: Spearman correlation coefficient

- path: insert-minus-delete.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Sum of lines inserted and deleted over time in repository"
  where: "From data/history-*.csv"
  when: 2019-12-15
  how: "Using bin/insert-plus-minus.py"
  fields:
  - name: filename
    type: text
    content: "path to file file containing insertions and deletions per commit"
  - name: total
    type: number
    content: "sum of insertions and deletions"

- path: commits-git-novice.csv
  what: "Count of commits made to Software Carpentry git novice lesson by person"
  where: data/history-git-novice.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-19
  how: bin/count-commits.py
  fields:
  - name: email
    type: text
    content: email address of committer
  - name: commits
    type: integer
    content: number of commits made by that person

- path: commits-numpy.csv
  what: "Count of commits made to NumPy by person"
  where: data/history-numpy.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-19
  how: bin/count-commits.py
  fields:
  - name: email
    type: text
    content: email address of committer
  - name: commits
    type: integer
    content: number of commits made by that person

- path: commits-pandas.csv
  what: "Count of commits made to Pandas by person"
  where: data/history-pandas.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-19
  how: bin/count-commits.py
  fields:
  - name: email
    type: text
    content: email address of committer
  - name: commits
    type: integer
    content: number of commits made by that person

- path: commits-python-novice-gapminder.csv
  what: "Count of commits made to Software Carpentry novice Python lesson by person"
  where: data/history-python-novice-gapminder.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-19
  how: bin/count-commits.py
  fields:
  - name: email
    type: text
    content: email address of committer
  - name: commits
    type: integer
    content: number of commits made by that person

- path: commits-r-novice-gapminder.csv
  what: "Count of commits made to Software Carpentry novice R lesson by person"
  where: data/history-r-novice-gapminder.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-19
  how: bin/count-commits.py
  fields:
  - name: email
    type: text
    content: email address of committer
  - name: commits
    type: integer
    content: number of commits made by that person

- path: commits-scikit-image.csv
  what: "Count of commits made to Scikit image processing library by person"
  where: data/history-scikit-image.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-19
  how: bin/count-commits.py
  fields:
  - name: email
    type: text
    content: email address of committer
  - name: commits
    type: integer
    content: number of commits made by that person

- path: commits-scikit-learn.csv
  what: "Count of commits made to Scikit learn library by person"
  where: data/history-scikit-learn.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-19
  how: bin/count-commits.py
  fields:
  - name: email
    type: text
    content: email address of committer
  - name: commits
    type: integer
    content: number of commits made by that person

- path: commits-scipy.csv
  what: "Count of commits made to SciPy library by person"
  where: data/history-scipy.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-19
  how: bin/count-commits.py
  fields:
  - name: email
    type: text
    content: email address of committer
  - name: commits
    type: integer
    content: number of commits made by that person

- path: commits-shell-novice.csv
  what: "Count of commits made to Software Carpentry novice shell lesson by person"
  where: data/history-shell-novice.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-19
  how: bin/count-commits.py
  fields:
  - name: email
    type: text
    content: email address of committer
  - name: commits
    type: integer
    content: number of commits made by that person

- path: commits-sql-novice-survey.csv
  what: "Count of commits made to Software Carpentry novice SQL lesson by person"
  where: data/history-sql-novice-survey.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-19
  how: bin/count-commits.py
  fields:
  - name: email
    type: text
    content: email address of committer
  - name: commits
    type: integer
    content: number of commits made by that person
