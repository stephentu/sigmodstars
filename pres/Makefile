all: p-crop.pdf

p-crop.pdf: p.pdf
	pdfcrop --margins 2 p.pdf

p.pdf: data.tex p.tex
	pdflatex p.tex

.PHONY: clean
clean:
	rm -f *.aux *.log *.pdf
