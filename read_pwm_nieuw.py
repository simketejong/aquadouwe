
#PWM PiFace Motor Speed Controller
import os
import pifacedigitalio as p
from datetime import datetime

p.init()
t1=datetime.now()
previous=0
teller=0

while True:
	if (p.digital_read(0) == 1) and (previous == 0):
   		teller=teller+1
	previous=p.digital_read(0)
	if teller > 50:
		t2=datetime.now()    
		delta=t2-t1
		delen=delta.total_seconds()
		verhouding=60/delen
		rpm=teller*verhouding
		#print"rpm = %f verhouding = %f "%(rpm,verhouding)
		teller=0
		fh = open("/tmp/rpm0.log", "a")
		fh.write("%f\n" %rpm )
		fh.close
		os.system('./size.sh')
		t1=datetime.now()
