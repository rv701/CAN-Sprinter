# CAN-Sprinter
CAN Bus debugging scripts for Sprinter TN1 model vans

CAN_GUI.py - Python3 gui application to display CAN BUS data from a 2002-2006 Sprinter TN1 van
Usage Example

Linux
./CAN_GUI.py /dev/ttyUSB0

Windows
.\CAN_GUI.py COM3

-----------

CAN_Simulator.py - Python3 script to simulate capturing live can data for testing allowing you to link two local serial ports for testing.

Usage Example
.\CAN_Simulator sprinter2.log /dev/ttyUSB1

This would assume the rx/tx pins are connected between ttyUSB0 and ttyUSB1

-------------

sprinter2.log is a sample log file from CAN BUS data capture

