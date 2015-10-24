import os
from time import sleep

SetPoint=48.0
pid=100
while True:
	f = os.popen('/bin/cat /sys/class/thermal/thermal_zone0/temp')
	measurement_value=int(f.read())
	measurement_value=measurement_value/1000
	if measurement_value > SetPoint:
		pid=pid+1
		print ("+pid=%d"%pid)
	else:
		pid=pid-1
		print ("-pid=%d"%pid)
	if pid > 100:
		pid = 100
	if pid < 15:
		pid = 15
	fh = open("/tmp/pwm0.duty", "w")
	fh.write("%d" %pid)
	print ("pid=%d"%pid)
	fh.close
	sleep(5)
