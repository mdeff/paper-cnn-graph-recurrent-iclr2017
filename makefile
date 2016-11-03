TEX = $(wildcard *.tex)
PDF = $(TEX:.tex=.pdf)
BIB = $(wildcard *.bib)

all: $(PDF)

figures:
	$(MAKE) -C figures

%.pdf: %.tex $(BIB) figures
	latexmk -pdf $<

clean:
	$(MAKE) clean -C figures
	rm -f *.{aux,bbl,blg,fdb_latexmk,fls,log,out,lof,dvi}
	rm -f *.{bcf,run.xml}
	rm -f *.{toc,snm,nav}
	rm -f *.gz*
	rm -f arxiv.zip

cleanall: clean
	rm -f $(PDF)

arxiv: all
	apack arxiv.zip figures/*.pdf $(TEX:.tex=).{tex,sty,bbl}

.PHONY: all figures clean cleanall arxiv
