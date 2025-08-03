- path: python-local-package-size.txt
  format: transcript
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Size in lines and characters of local Python files"
  where: "/anaconda3 installation directory on local computer"
  when: 2019-11-29
  how: "find /anaconda3 -name '*.py' -exec wc -l -c {} \\;"

- path: python-local-package-size.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Size in lines and characters of local Python files"
  where: "python-local-package-size.txt"
  when: 2019-11-29
  how: "wc2csv.py on transcript"
  fields:
  - name: Lines
    type: integer
    content: "Number of lines"
  - name: Characters
    type: integer
    content: "Number of characters"
  - name: Path
    type: text
    content: "Path to file"
