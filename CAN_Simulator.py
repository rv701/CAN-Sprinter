#!/usr/bin/python3

import time
import re
import serial
import sys
import os

    
#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
    
if len(sys.argv) == 3:
	#print ("Arg0" , str(sys.argv[0]))
	#print ("Arg1" , str(sys.argv[1]))
	#print ("Arg2" , str(sys.argv[2]))

	if os.path.isfile(sys.argv[1]):
		s = serial.Serial(port=sys.argv[2],baudrate=115200)
		s.close()
		s.open()

		print ("Writing sys.argv[1] data to " + sys.argv[2] + " at 115200 Baud.")

		can_lines = [line.rstrip('\n').rstrip('\r') for line in open(sys.argv[1])]

		for index in range(0, len(can_lines)):
			if index > 0:
				s.write(str.encode(can_lines[index] + "\r\n"))
			time.sleep(.01)
	else :
		print (sys.argv[1] + " is not a valid logfile.")


else:
	print ("Format issue: CAN_Simulator.py <logfile> <Serial Port>")

	



