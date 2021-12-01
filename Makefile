SHELL := /bin/bash

GIT_TAG = $(shell git describe --tags)

ifeq ($(uname_S), Windows)
    venv\Scripts\activate.bat
endif

ifeq ($(uname_S), Linux)
    . venv/bin/activate
endif

test:
	python -m unittest discover tests
.PHONY: test

lint:
	pylint *.py --ignore-patterns=test_.*?py,__init*
.PHONY: lint

pip-upgrade:
	pip install --upgrade --force-reinstall -r requirements.txt
.PHONY: pip-upgrade

ui:
	pyuic5 ui/UIMainWindowForm.ui -o UIMainWindowForm.py


#	pyrcc5 resources.qrc -o resources_rc.py
.PHONY: ui

run:
	python3 main.py
.PHONY: run

build:
	rm -rf ./build ./dist
	pyinstaller main.py -n PulseAudioVolume --windowed
	cd dist; \
	tar zcvf ../dist-out/PulseAudioVolume-"${GIT_TAG}".linux.tgz PulseAudioVolume/; \
	cd ..
	@echo "TAG: ${GIT_TAG}"
.PHONY: build