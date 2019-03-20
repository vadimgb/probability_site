nwf = lecture10.nw
hfile = $(nwf:.nw=.html)

all: $(hfile) lecture.py 

$(hfile): $(nwf) Makefile
	cp lecture.html $(hfile) 
	noweave -n -filter l2h -html $(nwf)  >> $(hfile) 
	echo "</BODY></HTML>" >> $(hfile) 


lecture.py: $(nwf) Makefile
	notangle -R$@ $(nwf) > $@


clean:
	rm $(hfile) *.py
