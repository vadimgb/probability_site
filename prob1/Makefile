nwf = prob1.nw
hfile = $(nwf:.nw=.html)

all: $(hfile) ddist.py 

$(hfile): $(nwf) Makefile help.txt
	cat  $(nwf)   > help.html 
	sed '20r help.html' help.txt > $(hfile) 


ddist.py: $(nwf) Makefile
	notangle -R$@ $(nwf) > $@


clean:
	rm $(hfile) *.py
