- path: timestamps.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Number of lines and functions in Python files"
  where: "Taken from mail folder on author's computer"
  when: 2019-12-14
  how: "Use bin/mailbox.py"
  fields:
  - name: Timestamp
    type: datetime
    content: when mail message was received

- path: mail-data.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Number of lines and functions in Python files"
  where: "Taken from mail folder on author's computer"
  when: 2019-12-14
  how: "Use bin/get-mail-data.py"
  fields:
  - name: Domain
    type: number
    content: unique identifier for mail message origin domain
  - name: MessageId
    type: number
    content: unique identifier for mail message
  - name: Timestamp
    type: datetime
    content: when mail message was received
  - name: Path
    type: text
    content: path to mailbox
