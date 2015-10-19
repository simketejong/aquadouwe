import pifacedigitalio as p
from time import sleep
fh = open("/tmp/pwm0.duty", "w")
fh.write("100")
fh.close
p.init()
duty=100.0
teller=0
while True:
	p.digital_write(6,1) #uit
	sleep((1.0-duty/100.0)/10)
	p.digital_write(6,0) #aan
	sleep((duty/100.0)/10)
	if teller > 1000:
		fh = open("/tmp/pwm0.duty", "r")
		duty=int(fh.readline())
		print("duty=%d"%duty)
		fh.close
		teller=0
	teller=teller+1
	
