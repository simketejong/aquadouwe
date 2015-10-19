
#PWM PiFace Motor Speed Controller

import pifacedigitalio as p
import datetime, time
from datetime import timedelta

p.init()
t1=datetime.datetime.now()
previous=0
teller=0

while True:
	if (p.digital_read(0) == 1) and (previous == 0):
   		teller=teller+1
	previous=p.digital_read(0)
	if teller == 200:
		t2=datetime.datetime.now()    
		delta=t2-t1
		verhouding=60/delta.seconds
		rpm=teller*verhouding
		print"rpm = %d\n\r"%rpm
		teller=0
		t1=datetime.datetime.now()
