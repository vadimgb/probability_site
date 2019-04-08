html/prob.html: prob.nw test.tex ddist.py
	latexml test.tex | latexmlpost - --format=html5 --destination=html/prob.html 
#	pdflatex test.tex
#	pdflatex test.tex
#--splitat=section --splitnaming=label 
	
ddist.py:  prob.nw
	notangle -Rprob.py prob.nw > ddist.py
clean:
	rm ddist.py html/prob.html
