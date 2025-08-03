- path: js-func-count.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Number of lines and functions in JavaScript files"
  where: "Taken from a Node project on author's computer"
  when: 2020-01-17
  how: "Use Unix shell find and bin/js-func-count.js"
  fields:
  - name: Path
    type: text
    content: path to file
  - name: Lines
    type: integer
    content: number of lines in file
  - name: Functions
    type: integer
    content: number of function definitions found in file

- path: py-func-count.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Number of lines and functions in Python files"
  where: "Taken from Python installation on author's computer"
  when: 2020-01-17
  how: "Use Unix shell find and bin/py-func-count.py"
  fields:
  - name: Path
    type: text
    content: path to file
  - name: Lines
    type: integer
    content: number of lines in file
  - name: Functions
    type: integer
    content: number of function definitions found in file

- path: py-func-name-len.csv.gz
  format: CSV+gzip
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Lengths of functions in Python files"
  where: "Taken from Python installation on author's computer"
  when: 2020-01-17
  how: "Use Unix shell find and bin/py-func-name-len.py"
  fields:
  - name: Path
    type: text
    content: path to file
  - name: Name
    type: text
    content: function name
  - name: Lines
    type: integer
    content: number of lines in file

- path: git-novice.csv
  what: "File-level change statistics for gh-pages branch of Software Carpentry lesson on Git"
  where: "https://github.com/swcarpentry/git-novice/"
  how: "bin/get-file-stats.py --repo $REPO --branch gh-pages"
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-08
  fields:
  - name: branch
    type: text
    content: branch commit taken from
  - name: hash
    type: text
    content: unique hash of commit
  - name: email
    type: text
    content: email address of commit author
  - name: timestamp
    type: datetime
    content: timestamp of commit
  - name: path
    type: text
    content: path of modified file
  - name: insertions
    type: number
    content: insertions
  - name: deletions
    type: number
    content: deletions
  - name: lines
    type: number
    content: lines

- path: python-novice-gapminder.csv
  what: "File-level change statistics for gh-pages branch of Software Carpentry lesson on Pyth    Format: CSV"
  where: "https://github.com/swcarpentry/python-novice-gapminder/"
  how: "bin/get-file-stats.py --repo $REPO --branch gh-pages"
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-08
  fields:
  - name: branch
    type: text
    content: branch commit taken from
  - name: hash
    type: text
    content: unique hash of commit
  - name: email
    type: text
    content: email address of commit author
  - name: timestamp
    type: datetime
    content: timestamp of commit
  - name: path
    type: text
    content: path of modified file
  - name: insertions
    type: number
    content: insertions
  - name: deletions
    type: number
    content: deletions
  - name: lines
    type: number
    content: lines

- path: r-novice-gapminder.csv
  what: "File-level change statistics for master branch of Software Carpentry lesson on R"
  where: "https://github.com/swcarpentry/r-novice-gapminder/"
  how: "bin/get-file-stats.py --repo $REPO --branch master"
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-08
  fields:
  - name: branch
    type: text
    content: branch commit taken from
  - name: hash
    type: text
    content: unique hash of commit
  - name: email
    type: text
    content: email address of commit author
  - name: timestamp
    type: datetime
    content: timestamp of commit
  - name: path
    type: text
    content: path of modified file
  - name: insertions
    type: number
    content: insertions
  - name: deletions
    type: number
    content: deletions
  - name: lines
    type: number
    content: lines

- path: shell-novice.csv
  what: "File-level change statistics for gh-pages branch of Software Carpentry lesson on Unix shell"
  where: "https://github.com/swcarpentry/shell-novice/"
  how: "bin/get-file-stats.py --repo $REPO --branch gh-pages"
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-08
  fields:
  - name: branch
    type: text
    content: branch commit taken from
  - name: hash
    type: text
    content: unique hash of commit
  - name: email
    type: text
    content: email address of commit author
  - name: timestamp
    type: datetime
    content: timestamp of commit
  - name: path
    type: text
    content: path of modified file
  - name: insertions
    type: number
    content: insertions
  - name: deletions
    type: number
    content: deletions
  - name: lines
    type: number
    content: lines

- path: sql-novice-survey.csv
  what: "File-level change statistics for gh-pages branch of Software Carpentry lesson on SQL"
  where: "https://github.com/swcarpentry/sql-novice-survey/"
  how: "bin/get-file-stats.py --repo $REPO --branch gh-pages"
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-08
  fields:
  - name: branch
    type: text
    content: branch commit taken from
  - name: hash
    type: text
    content: unique hash of commit
  - name: email
    type: text
    content: email address of commit author
  - name: timestamp
    type: datetime
    content: timestamp of commit
  - name: path
    type: text
    content: path of modified file
  - name: insertions
    type: number
    content: insertions
  - name: deletions
    type: number
    content: deletions
  - name: lines
    type: number
    content: lines

- path: numpy.csv
  what: "File-level change statistics for master branch of numpy repository"
  where: "https://github.com/numpy/numpy/"
  how: "bin/get-file-stats.py --repo $REPO --branch master"
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-08
  fields:
  - name: branch
    type: text
    content: branch commit taken from
  - name: hash
    type: text
    content: unique hash of commit
  - name: email
    type: text
    content: email address of commit author
  - name: timestamp
    type: datetime
    content: timestamp of commit
  - name: path
    type: text
    content: path of modified file
  - name: insertions
    type: number
    content: insertions
  - name: deletions
    type: number
    content: deletions
  - name: lines
    type: number
    content: lines

- path: pandas.csv
  what: "File-level change statistics for master branch of pandas repository"
  where: "https://github.com/pandas-dev/pandas/"
  how: "bin/get-file-stats.py --repo $REPO --branch master"
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-08
  fields:
  - name: branch
    type: text
    content: branch commit taken from
  - name: hash
    type: text
    content: unique hash of commit
  - name: email
    type: text
    content: email address of commit author
  - name: timestamp
    type: datetime
    content: timestamp of commit
  - name: path
    type: text
    content: path of modified file
  - name: insertions
    type: number
    content: insertions
  - name: deletions
    type: number
    content: deletions
  - name: lines
    type: number
    content: lines

- path: scikit-image.csv
  what: "File-level change statistics for master branch of scikit-image repository"
  where: "https://github.com/scikit-image/scikit-image/"
  how: "bin/get-file-stats.py --repo $REPO --branch master"
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-08
  fields:
  - name: branch
    type: text
    content: branch commit taken from
  - name: hash
    type: text
    content: unique hash of commit
  - name: email
    type: text
    content: email address of commit author
  - name: timestamp
    type: datetime
    content: timestamp of commit
  - name: path
    type: text
    content: path of modified file
  - name: insertions
    type: number
    content: insertions
  - name: deletions
    type: number
    content: deletions
  - name: lines
    type: number
    content: lines

- path: scikit-learn.csv
  what: "File-level change statistics for master branch of scikit-learn repository"
  where: "https://github.com/scikit-learn/scikit-learn/"
  how: "bin/get-file-stats.py --repo $REPO --branch master"
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-08
  fields:
  - name: branch
    type: text
    content: branch commit taken from
  - name: hash
    type: text
    content: unique hash of commit
  - name: email
    type: text
    content: email address of commit author
  - name: timestamp
    type: datetime
    content: timestamp of commit
  - name: path
    type: text
    content: path of modified file
  - name: insertions
    type: number
    content: insertions
  - name: deletions
    type: number
    content: deletions
  - name: lines
    type: number
    content: lines

- path: scipy.csv
  what: "File-level change statistics for master branch of scipy repository"
  where: "https://github.com/scipy/scipy/"
  how: "bin/get-file-stats.py --repo $REPO --branch master"
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  when: 2019-12-08
  fields:
  - name: branch
    type: text
    content: branch commit taken from
  - name: hash
    type: text
    content: unique hash of commit
  - name: email
    type: text
    content: email address of commit author
  - name: timestamp
    type: datetime
    content: timestamp of commit
  - name: path
    type: text
    content: path of modified file
  - name: insertions
    type: number
    content: insertions
  - name: deletions
    type: number
    content: deletions
  - name: lines
    type: number
    content: lines
