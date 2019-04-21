all: html/prob.html html/prob1.html
html/prob.html: prob.nw test.tex ddist.py
	latexml test.tex | latexmlpost - --format=html5 --destination=html/prob.html 
#	pdflatex test.tex
#	pdflatex test.tex
#--splitat=section --splitnaming=label 
	
ddist.py:  prob.nw
	notangle -Rprob.py prob.nw > ddist.py

html/prob1.html: prob1.nw test1.tex prob1.py
	latexml test1.tex | latexmlpost - --format=html5 --destination=html/prob1.html

prob1.py: prob1.nw
	notangle -Rprob1.py prob1.nw > prob1.py
clean:
	rm ddist.py html/prob.html html/prob1.html prob1.py
