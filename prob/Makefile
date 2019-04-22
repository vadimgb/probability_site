all: html/prob.html html/prob1.html html/src.zip
html/prob.html: prob.nw test.tex 
	latexml test.tex | latexmlpost - --format=html4 --destination=html/probH.html 
	sed '10r help1.txt' html/probH.html > html/probH.txt
	sed '16r help2.txt' html/probH.txt > html/prob.html
#	pdflatex test.tex
#	pdflatex test.tex
#--splitat=section --splitnaming=label 

html/src.zip: prob.py prob1.py	
	zip html/src *.py	

prob.py:  prob.nw
	notangle -Rprob.py prob.nw > prob.py

html/prob1.html: prob1.nw test1.tex prob1.py help1.txt
	latexml test1.tex | latexmlpost - --format=html5 --destination=html/probH.html
	sed '10r help1.txt' html/probH.html > html/probH.txt
	sed '16r help2.txt' html/probH.txt > html/prob1.html

prob1.py: prob1.nw
	notangle -Rprob1.py prob1.nw > prob1.py
clean:
	rm ddist.py html/prob.html html/prob1.html prob1.py 
