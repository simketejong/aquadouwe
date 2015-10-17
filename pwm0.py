import pifacedigitalio as p
from time import sleep

p.init()

while True:
	p.digital_write(0,1)
	sleep(5)
	p.digital_write(0,0)
	sleep(2)