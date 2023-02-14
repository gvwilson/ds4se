- path: python-bug-summary-2020-01-22.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Summary of Python issues"
  where: "Taken from https://bugs.python.org/ (all issues, default headings)"
  when: 2020-01-21
  how: "Do a query to download the default CSV, then edit the query URL to remove filtering that restricts the data to open issues"
  fields:
  - name: id
    type: integer
    content: unique identifier of issue
  - name: activity
    type: datetime
    content: timestamp of last activity
  - name: title
    type: text
    content: summary of issue
  - name: creator
    type: integer
    content: unique identifier of issue creator
  - name: assignee
    type: integer/null
    content: unique identifier of person responsible
  - name: status
    type: integer
    content: enum of issue status
  - name: type
    type: integer/null
    content: enum of issue type
  - name: message_count
    type: number
    content: number of messages associated with issue
