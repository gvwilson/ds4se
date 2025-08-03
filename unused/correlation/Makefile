BINS=200
LESSONS=git-novice python-novice-gapminder r-novice-gapminder shell-novice sql-novice-survey
LIBRARIES=numpy pandas scikit-image scikit-learn scipy
TARGETS=\
  $(patsubst %,lines-per-func-%.svg,python-all javascript-all javascript-low) \
  py-lines-funcs.svg js-lines-funcs.svg py-func-name-len.svg

all : ${TARGETS}

lines-per-func-python-all.svg : data/py-func-count.csv
	bin/plot-lines-per-func.py --bins ${BINS} --output $@ --input $< --subtitle 'Python / All'

lines-per-func-javascript-all.svg : data/js-func-count.csv
	bin/plot-lines-per-func.py --bins ${BINS} --output $@ --input $< --subtitle 'JavaScript / All'

lines-per-func-javascript-low.svg : data/js-func-count.csv
	bin/plot-lines-per-func.py --bins ${BINS} --max 120 --output $@ --input $< --subtitle 'JavaScript / Low End'

correlation :
	bin/correlation.py --title "Python" --input data/py-func-count.csv Lines Functions
	bin/correlation.py --title "JavaScript" --input data/js-func-count.csv Lines Functions

py-lines-funcs.svg : data/py-func-count.csv
	bin/scatter.py --input $< --output $@ --x Lines --y Functions

js-lines-funcs.svg : data/js-func-count.csv
	bin/scatter.py --input $< --output $@ --x Lines --y Functions

data/py-func-count.csv :
	find /anaconda3/ -name '*.py' | bin/py-func-count.py --list > data/py-func-count.csv

data/js-func-count.csv :
	find ~/blocks/node_modules/ -name '*.js' | node bin/js-func-count.js > data/js-func-count.csv

data/py-func-name-len.csv.gz : bin/py-func-name-len.py
	find /anaconda3/ -name '*.py' | bin/py-func-name-len.py --list --verbose | gzip -c > $@

py-func-name-len.svg : data/py-func-name-len.csv.gz data/py-func-name-len.csv.gz
	bin/scatter-len.py --input $< --output $@

match-addresses :
	bin/match-addresses.py data/blame-%.csv data/history-%.csv ${LESSONS} ${LIBRARIES}

settings :
	@echo TARGETS: ${TARGETS}
