import os
from time import sleep

Difference=1
SetPoint=35.0
pid=100.0
while True:
	f = os.popen('/bin/cat /sys/class/thermal/thermal_zone0/temp')
	measurement_value=int(f.read())
	measurement_value=measurement_value/1000
	Difference=abs(SetPoint-measurement_value)
	if measurement_value > SetPoint:
		pid=pid+1*Difference
#		print ("+pid=%d"%pid)
	else:
		pid=pid-1*Difference
#		print ("-pid=%d"%pid)
	if pid > 100:
		pid = 100
	if pid < 15:
		pid = 15
	fh = open("/tmp/pwm0.duty", "w")
	fh.write("%d" %pid)
#	print ("pid=%f verstuur=%d")%(pid,pid)
	fh.close
	try:
  		with open("/tmp/temperatuur", "r") as fh:
	   		SetPoint=int(fh.readline())
#			print("SetPoint=%f"%SetPoint)
			fh.close
			teller=0
	except:
  		SetPoint=35.0
	sleep(5)
