import pifacedigitalio as p
from time import sleep
import os

fh = open("/tmp/pwm0.duty", "w")
fh.write("100")
fh.close
p.init()
duty=100.0
teller=0
while True:
	p.digital_write(6,1) #uit
	sleep((1.0-duty/100.0)/50)
	p.digital_write(6,0) #aan
	sleep((duty/100.0)/50)
	if teller > 100:
		duty_old=duty
		try:
  			with open("/tmp/pwm0.duty", "r") as fh:
		   		duty=int(fh.readline())
#				print("duty=%d"%duty)
				fh.close
				teller=0
		except:
  			print("oops")
  		if duty_old == duty:
  			while duty == 15:
  				try:
  					with open("/tmp/pwm0.duty", "r") as fh:
		   				duty=int(fh.readline())
#						print("duty=%d"%duty)
						fh.close
						teller=0
						p.digital_write(6,1) #uit
				except:
 					#print("oops")
 					sleep(0.1)
		teller=0
	teller=teller+1
	
