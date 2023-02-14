DATA=$(wildcard data/*-counts.csv)
FIGURES=\
  $(patsubst data/%-counts.csv,%-counts-all.svg,${DATA}) \
  $(patsubst data/%-counts.csv,%-counts-trimmed.svg,${DATA})

#  js-trimmed js-trimmed-low

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## figures : re-make all figures
figures : ${FIGURES}

%-counts-all.svg : data/%-counts.csv
	@mkdir -p figures
	python bin/length-frequency-plot.py --data $< --fig $@ --logx

%-counts-trimmed.svg : data/%-counts.csv
	@mkdir -p figures
	python bin/length-frequency-plot.py --data $< --fig $@ --low 2 --high 200

## clean : clean up editor backup files etc.
clean :
	find . -name '*~' -exec rm {} \;
	find . -name '*.bak' -exec rm {} \;

## settings : show variable values.
settings :
	@echo DATA ${DATA}
	@echo FIGURES ${FIGURES}
