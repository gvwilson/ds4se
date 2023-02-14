- path: raw-intervals.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Intervals between email messages"
  where: "Produced from data/timestamps.csv"
  when: 2019-12-14
  how: "Use bin/calculate-intervals.py"
  fields:
  - name: Date
    type: datetime
    content: time message received
  - name: Interval
    type: duration
    content: elapsed time since previous message

- path: filtered-data.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Intervals between email messages"
  where: "Produced from data/mail-data.csv"
  when: 2019-12-14
  how: "Use bin/mail-data-filter.py"
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

- path: filtered-intervals.csv
  format: CSV
  who: "Greg Wilson <gvwilson@third-bit.com>"
  what: "Intervals between email messages"
  where: "Produced from results/filtered-data.csv"
  when: 2019-12-14
  how: "Use bin/calculate-intervals.py"
  fields:
  - name: Date
    type: datetime
    content: time message received
  - name: Interval
    type: duration
    content: elapsed time since previous message
