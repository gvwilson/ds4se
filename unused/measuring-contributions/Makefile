LESSONS=git-novice python-novice-gapminder r-novice-gapminder shell-novice sql-novice-survey
LIBRARIES=numpy pandas scikit-image scikit-learn scipy

HISTORY_ALL=$(patsubst %,data/history-%.csv,${LESSONS}) $(patsubst %,data/history-%.csv,${LIBRARIES})

BLAME_ALL=$(patsubst %,data/blame-%.csv,${LESSONS}) $(patsubst %,data/blame-%.csv,${LIBRARIES})

COMMITS_ALL=$(patsubst %,results/commits-%.csv,${LESSONS}) $(patsubst %,results/commits-%.csv,${LIBRARIES})

RESULTS=\
  results/gini-history.csv\
  results/gini-blame.csv\
  results/insert-minus-delete.csv\
  ${COMMITS_ALL}\
  results/correlation.csv\
  correlation.svg

all : ${RESULTS}

results/gini-history.csv : ${HISTORY_ALL}
	python bin/history.py --output $@ $^

results/gini-blame.csv : ${BLAME_ALL}
	python bin/blame.py --output $@ $^

results/insert-minus-delete.csv : ${HISTORY_ALL}
	python bin/insert-minus-delete.py --output $@ $^

results/commits-%.csv : data/history-%.csv
	python bin/count-commits.py --input $< --output $@

results/correlation.csv correlation.svg : ${COMMITS_ALL} ${BLAME_ALL} bin/correlation.py
	python bin/correlation.py --commits results/commits --blame data/blame --output results/correlation.csv --figdir figures ${LESSONS} ${LIBRARIES}

settings :
	@echo HISTORY_LESSONS: ${HISTORY_LESSONS}
	@echo BLAME_LESSONS: ${BLAME_LESSONS}
	@echo HISTORY_LIBRARIES: ${HISTORY_LIBRARIES}
	@echo BLAME_LIBRARIES: ${BLAME_LIBRARIES}
	@echo COMMITS: ${COMMITS}
	@echo RESULTS: ${RESULTS}

