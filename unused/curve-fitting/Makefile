FITTINGS=N100 N300 N500 N700 N900 actual-100
TARGETS=\
  results/raw-intervals.csv \
  $(patsubst %,raw-%.svg,view-all view-one-week view-eight-hours) \
  $(patsubst %,fit-all-%.svg,${FITTINGS}) \
  results/filtered-intervals.csv \
  $(patsubst %,fit-filtered-%.svg,${FITTINGS})

all : ${TARGETS}

results/raw-intervals.csv : data/timestamps.csv
	python bin/calculate-intervals.py --input $< --output $@

raw-view-%.svg : results/raw-intervals.csv
	python bin/raw-view.py --input $< --output raw-view

fit-all-%.svg : results/raw-intervals.csv
	python bin/curve-fit.py --input $< --output fit-all

data/mail-data.csv log/mail-data.txt :
	python bin/get-mail-data.py --root ~/Library/Mail --output data/mail-data.csv --errors log/mail-data.txt --obfuscate ${HOME}/Library/Mail --verbose

results/filtered-data.csv : data/mail-data.csv
	python bin/mail-data-filter.py --input $< --output $@ --logfile log/mail-data-filter.txt

results/filtered-intervals.csv : results/filtered-data.csv
	python bin/calculate-intervals.py --input $< --output $@

fit-filtered-%.svg : results/filtered-intervals.csv
	python bin/curve-fit.py --input $< --output fit-filtered

settings :
	@echo TARGETS: ${TARGETS}
