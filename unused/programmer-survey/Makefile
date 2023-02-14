all : salary_by_devtype.svg salary_by_gender.svg

salary_by_devtype.svg salary_by_gender.svg : data/survey_results_public.csv.zip bin/analyze-survey.py
	python bin/analyze-survey.py --input $< --save figures

test : test/test_data.csv bin/analyze-survey.py
	python bin/analyze-survey.py --input $< --verbose

test/test_data.csv : data/survey_results_public.csv.zip bin/create-test-subset.py
	python bin/create-test-subset.py --input $< --output $@ --seed 172634 --number 1000
