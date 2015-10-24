#!/usr/bin/python
import commands
import os
from time import sleep
from subprocess import PIPE, Popen

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

test=commands.getstatusoutput('/bin/ps -ef | /bin/grep pwm0.py | /usr/bin/wc -l ')
print test[1]
if test[1] == "2":
	os.system('/usr/bin/python /home/pi/ACD/ABElectronics_Python_Libraries/ADCPi/PWM0/pwm0.py &') 

test=commands.getstatusoutput('/bin/ps -ef | /bin/grep read_pwm0.py | /usr/bin/wc -l')
print test[1]
if test[1] == "2":
	os.system('/usr/bin/python /home/pi/ACD/ABElectronics_Python_Libraries/ADCPi/PWM0/read_pwm0.py &') 

test=commands.getstatusoutput('/bin/ps -ef | /bin/grep PID_pwm0.py | /usr/bin/wc -l')
print test[1]
if test[1] == "2":
	os.system('/usr/bin/python /home/pi/ACD/ABElectronics_Python_Libraries/ADCPi/PWM0/PID_pwm0.py &') 

test=commands.getstatusoutput('/bin/ps -ef | /bin/grep Run_PWM_0.py | /usr/bin/wc -l')
print test[1]
if test[1] == "2":
	os.system('/usr/bin/python /home/pi/ACD/ABElectronics_Python_Libraries/ADCPi/PWM0/PID_pwm0.py &') 
		while True:
			laatste=cmdline('/usr/bin/tail -n 1 /tmp/rpm0.log')
			sleep(5)
			aller_laatste=cmdline('/usr/bin/tail -n 1 /tmp/rpm0.log')
			if laatste == aller_laatste:
				if laatste != "0":
					fh = open("/tmp/rpm0.log", "a")
					for x in range (0,20):
						fh.write("0\n")
					fh.close
		#print("laatste=%s aller_laatste=%s"%(laatste,aller_laatste))
					os.system('./size.sh')
			sleep(5)


