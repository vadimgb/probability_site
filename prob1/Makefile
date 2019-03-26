nwf = prob1.nw
hfile = $(nwf:.nw=.html)

all: $(hfile) ddist.py prob1.py prob.zip

$(hfile): $(nwf) Makefile help.txt
	cat  $(nwf)   > help.html 
	sed '20r help.html' help.txt > $(hfile) 


ddist.py: $(nwf) Makefile
	notangle -R$@ $(nwf) > $@

prob1.py: $(nwf) Makefile
	notangle -R$@ $(nwf) > $@

prob.zip: $(nwf) Makefile
	zip prob *.py

clean:
	rm $(hfile) *.py
