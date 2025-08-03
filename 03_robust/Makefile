## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## results : re-make all results
results : results/releases.csv results/name-component-count.csv

## data/all-versions.csv.gz : fetch all information (may take several hours).
data/all-versions.csv.gz : bin/get-all-versions.py
	python bin/get-all-versions.py > data/all-versions.csv
	gzip data/all-versions.csv

## results/releases.csv : regenerate list of releases per package.
results/releases.csv : data/all-versions.csv.gz bin/count-releases.py
	mkdir -p results
	python bin/count-releases.py data/all-versions.csv.gz > results/releases.csv

## results/name-component-count.csv : regenerate count of '.'-separated name components.
results/name-component-count.csv : data/all-versions.csv.gz bin/components.py
	mkdir -p results
	python bin/components.py data/all-versions.csv.gz > results/name-component-count.csv

## count-redundant-releases : report how many packages have releases things in multiple formats.
count-redundant-releases : data/all-versions.csv.gz
	python bin/remove-duplicates.py data/all-versions.csv.gz

## clean : clean up editor backup files etc.
clean :
	find . -name '*~' -exec rm {} \;
	find . -name '*.bak' -exec rm {} \;
