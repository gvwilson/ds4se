- path: simple-index.html
  format: HTML
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Main Python package index page"
  where: "https://pypi.org/simple/"
  when: 2019-11-18
  how: "Downloaded"

- path: 0805nexter-index.html
  format: HTML
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Sample package description page"
  where: "https://pypi.org/simple/0805nexter/"
  when: 2019-11-18
  how: "Downloaded"

- path: release-count-timings.txt
  format: transcript
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Elapsed time to download Python package information"
  where: "https://pypi.org/"
  when: 2019-11-18
  how: "Verbose output from bin/get-index-page.py"

- path: data/all-versions.csv.gz
  format: CSV+gzip
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "All releases of all Python packages on PyPI"
  where: "https://pypi.org/"
  when: 2019-11-18
  how: "Scraped using bin/get-all-versions-.py"
  fields:
  - name: Package
    type: text
    content: package name
  - name: Releases
    type: text
    content: release filename

- path: results/name-component-count.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Count of types of release files"
  where: "data/all-versions.csv.gz"
  when: 2019-11-18
  how: bin/components.py
  fields:
  - name: Component
    type: text
    content: type of component in filename
  - name: Count
    type: integer
    content: number of occurences

- path: results/releases.csv
  format: HTML
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Number of releases for each Python package"
  where: "https://pypi.org/"
  when: 2019-11-18
  how: "Scraped using bin/get-index-page.py"
  fields:
  - name: Package
    type: text
    content: package name
  - name: Releases
    type: integer
    content: number of releases
