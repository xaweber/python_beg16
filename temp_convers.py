#!/usr/bin/env python
import sys

def celsius_to_fahr(temp_c):
	temp_f=temp_c* (9/5)+32
	return temp_f

try:
	celsius = float(sys.argv[1])
	print('Temperature of ', celsius, ' degrees celcius can be converted to ',celsius_to_fahr(celsius), ' degrees fahrenheit')
except:
	print("Incorrect input provided, please try again")
