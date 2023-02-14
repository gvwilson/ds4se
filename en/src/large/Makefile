DATA=$(wildcard data/*-counts.csv)
FIGURES=\
  $(patsubst data/%-counts.csv,%-counts-all.svg,${DATA}) \
  $(patsubst data/%-counts.csv,%-counts-trimmed.svg,${DATA})

#  js-trimmed js-trimmed-low

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## t-test-counts : re-run t-test on count data from previous chapter
t-test-counts :
	python bin/t-test.py --left ../hypothesis-testing/data/javascript-counts.csv --right ../hypothesis-testing/data/python-counts.csv --low 1 --high 200

## violin : re-make violin plots
violin :
	python bin/plot-actual.py --data data/programmer-hours.csv --save programmer-hours.svg

## programmer-hours : re-run t-test on weekday vs. weekend programmer hours
programmer-hours :
	python bin/weekends.py --data data/programmer-hours.csv

## clean : clean up editor backup files etc.
clean :
	find . -name '*~' -exec rm {} \;
	find . -name '*.bak' -exec rm {} \;

## settings : show variable values.
settings :
	@echo DATA ${DATA}
	@echo FIGURES ${FIGURES}
