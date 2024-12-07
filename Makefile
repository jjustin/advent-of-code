.PHONY: run setup

default: setup

run:
	time python setup/run.py -y $$(date +%Y) -d $$(date +%d)

setup:
	python setup/setup.py -y $$(date +%Y) -d $$(date +%d)
