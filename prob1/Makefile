nwf = prob1.nw
hfile = $(nwf:.nw=.html)

all: $(hfile) ddist.py 

$(hfile): $(nwf) Makefile
	noweave -n -filter l2h -html $(nwf)  > help.html 
	sed '19r help.txt' help.html > $(hfile) 


ddist.py: $(nwf) Makefile
	notangle -R$@ $(nwf) > $@


clean:
	rm $(hfile) *.py
