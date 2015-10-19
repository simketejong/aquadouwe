import pifacedigitalio as p
from time import sleep

p.init()

while True:
	p.digital_write(6,1)
	sleep(0.05)
	p.digital_write(6,0)
	sleep(0.05)