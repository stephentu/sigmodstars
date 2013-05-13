-include config.mk
PYTHON ?= python2

all: pres/p-crop.pdf

pres/p-crop.pdf:
	$(PYTHON) gen.py data.py > pres/data.tex
	make -C pres

.PHONY: clean
clean:
	make -C pres clean
