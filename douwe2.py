#!/usr/bin/python
# -*- coding: utf-8 -*-

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import time
import os
import math

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 18)


def NuGoed(Vin, Vout):
	R1 = 9610
	R_load = 7800

	I_Load = Vout / R_load
	V_load = 10000 * I_Load # Real Vout

	Overdracht = V_load / Vin # 
	R_themistor = ((Overdracht * R1)/(1 - Overdracht))
	return (R_themistor)

def temp_get(Vin, Vout):
	R1 = 9610 # Resistor in serie measured
	R_load = 7800 # Measured internal impedance
	I_Load = Vout / R_load # Amp 
	V_load = 10000 * I_Load # Real Vout
	Overdracht = V_load / Vin # 
	R_themistor = ((Overdracht * R1)/(1 - Overdracht))
	lnohm = math.log1p(R_themistor) #take ln(ohms)
    #a, b, & c values from http://www.thermistor.com/calculators.php
    #using curve T (-3.5%/C @ 25C) Mil Ratio L

	a = 0.001415520801807
	b = 0.000199552765877
	c = 0.000000128856702
    #Steinhart Hart Equation
    # T = 1/(a + b[ln(ohm)] + c[ln(ohm)]^3)
	t1 = (b*lnohm) # b[ln(ohm)]
	c2 = c*lnohm # c[ln(ohm)]
	t2 = math.pow(c2,3) # c[ln(ohm)]^3
	temp = 1/(a + t1 + t2) #calcualte temperature
	tempc = temp - 273.15 - 12 #K to C was 4
    # the -4 is error correction for bad python math
	return (tempc)

def polynoom(Vin, Vout):
 	R1 = 9610
	R_load = 7800

	I_Load = Vout / R_load
	V_load = 10000 * I_Load # Real Vout

	Overdracht = V_load / Vin # 
	R_themistor = ((Overdracht * R1)/(1 - Overdracht))
	a = 1.636904762e-7
	b = 6.458333333e-3
	c = 73.21428571
	tempc = a*math.pow(R_themistor,2) - b * R_themistor + c
	return (tempc)

while (True):
	os.system('clear')
	print ("Voltage on channel 2: %0.06f Volt" % adc.read_voltage(2))
#    print ("Temperature on channel 3: %0.06f°C" % calcTemperature(adc.read_voltage(2)))
	print ("Voltage on channel 3: %0.06f Volt" % (adc.read_voltage(3)))
	print ("R2 = %0.06f Ohm" % NuGoed(adc.read_voltage(3), adc.read_voltage(2)))
	print ("%0.06f °C" % temp_get(adc.read_voltage(3), adc.read_voltage(2)))
	print ("%0.06f °C" % polynoom(adc.read_voltage(3), adc.read_voltage(2)))
	# wait 0.5 seconds before reading the pins again
	fh = open("/tmp/temperature.log", "a")
	fh.write("%0.06f\n" % temp_get(adc.read_voltage(3), adc.read_voltage(2)))
	time.sleep(1)
	fh.close
	os.system('/home/pi/size.sh')

