all: html/prob.html html/prob1.html html/src.zip
html/prob.html: prob.nw test.tex 
	latexml test.tex | latexmlpost - --format=html4 --destination=html/probH.html 
	sed '10r help1.txt' html/probH.html > html/probH.txt
	sed '16r help2.txt' html/probH.txt > html/prob.html
#	pdflatex test.tex
#	pdflatex test.tex
#--splitat=section --splitnaming=label 

html/src.zip: prob.py ddist.py test.py	
	zip html/src *.py	

prob.py:  prob.nw
	notangle -Rprob.py prob.nw > prob.py

html/prob1.html: prob1.nw test1.tex  help1.txt
	latexml test1.tex | latexmlpost - --format=html5 --destination=html/probH.html
	sed '10r help1.txt' html/probH.html > html/probH.txt
	sed '16r help2.txt' html/probH.txt > html/prob1.html

ddist.py: prob1.nw
	notangle -Rddist.py prob1.nw > ddist.py
test.py: prob1.nw
	notangle -Rtest.py prob1.nw > test.py
clean:
	rm ddist.py html/prob.html html/prob1.html test.py  
