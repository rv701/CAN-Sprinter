#!/usr/bin/python3

from tkinter import *
from datetime import datetime
import random
import time
import serial
import re
import sys

	
def get_hex_bits(number, offset, count):

	mask = 0

	for i in range(0, 64):
		if (i >= offset) and (i < (offset + count)) :
			mask = mask | 1 
		#if (i >= (offset + count)) :
		#	mask = mask | 1 
		if (i < 63) :
			mask = mask << 1
			
	number = number & mask
	number = number >> 64 - offset - count
	
	return number
		
def get_byte_bits(number, offset, count):

	mask = 0

	for i in range(0, 8):
		if (i >= offset) and (i < (offset + count)) :
			mask = mask | 1 
		#if (i >= (offset + count)) :
		#	mask = mask | 1 
		if (i < 7) :
			mask = mask << 1
			
	number = number & mask
	number = number >> 8 - offset - count
	
	return number


#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
    
if len(sys.argv) == 2:
	#print ("Arg0" , str(sys.argv[0]))
	#print ("Arg1" , str(sys.argv[1]))

	ws = Tk()
	ws.title('Sprinter CAN DATA')
	ws.geometry('1000x600')
	#ws.config(bg='#5f734c')

	# Column 1 Titles
	row1_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row2_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row3_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row4_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row5_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row6_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row7_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row8_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row9_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row10_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row11_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row12_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	row13_lbl = Label(
	    text=" ",
	    font=(22),
	    padx=10,
	    pady=5,
	    bg='#d9d8d7',
	    anchor='w'
	    )
	    
	

	# Title Row
	row1_lbl.pack(fill='both')
	row2_lbl.pack(fill='both')
	row3_lbl.pack(fill='both')
	row4_lbl.pack(fill='both')
	row5_lbl.pack(fill='both')
	row6_lbl.pack(fill='both')
	row7_lbl.pack(fill='both')
	row8_lbl.pack(fill='both')
	row9_lbl.pack(fill='both')
	row10_lbl.pack(fill='both')
	row11_lbl.pack(fill='both')
	row12_lbl.pack(fill='both')
	row13_lbl.pack(fill='both')
	

	ws.update()
	
	# Open logfile
	now = datetime.now() # current date and time
	filename = now.strftime("%m-%d-%Y_%H-%M-%S_log.txt")
	path = "./log/"

	filename = path + filename
	print("Logging CAN Bus data to " + filename)

	outfile = open(filename, "w")

	# Open serial port
	s = serial.Serial(port=str(sys.argv[1]),baudrate=115200)
	s.close()
	s.open()
	
	# 208 Var Init
	whl_id_text = "208"
	whl_detail_text = " "
	whl_hex_text = " "
	whl_time_text = " "
	whl_notes_text = " "
	whl_time = time.time()
	
	# 210 Var Init
	ecu1_id_text = "210"
	ecu1_detail_text = " "
	ecu1_hex_text = " "
	ecu1_time_text = " "
	ecu1_notes_text = " "
	ecu1_time = time.time()
	
	# 212 Var Init
	ecu2_id_text = "212"
	ecu2_detail_text = " "
	ecu2_hex_text = " "
	ecu2_time_text = " "
	ecu2_notes_text = " "
	ecu2_time = time.time()
	
	# 218 Var Init
	GS_218_id_text = "218"
	GS_218_detail_text = " "
	GS_218_hex_text = " "
	GS_218_time_text = " "
	GS_218_notes_text = " "
	GS_218_time = time.time()

	# 230 Var Init
	shift_id_text = "230"
	shift_detail_text = " "
	shift_hex_text = " "
	shift_bin_text = " "
	shift_time_text = " "
	shift_notes_text = " "
	shift_time = time.time()
	
	# 338 Var Init
	tcm2_id_text = "338"
	tcm2_detail_text = " "
	tcm2_hex_text = " "
	tcm2_time_text = " "
	tcm2_notes_text = " "
	tcm2_time = time.time()
	
	# 408 Var Init
	KOMBI_408_id_text = "408"
	KOMBI_408_detail_text = " "
	KOMBI_408_hex_text = " "
	KOMBI_408_time_text = " "
	KOMBI_408_notes_text = " "
	KOMBI_408_time = time.time()
	
	# 412 Var Init
	KOMBI_412_id_text = "412"
	KOMBI_412_detail_text = " "
	KOMBI_412_hex_text = " "
	KOMBI_412_time_text = " "
	KOMBI_412_notes_text = " "
	KOMBI_412_time = time.time()

	# 418 Var Init
	tcm_id_text = "418"
	tcm_detail_text = " "
	tcm_hex_text = " "
	tcm_bin_text = " "
	tcm_time_text = " "
	tcm_notes_text = " "
	tcm_time = time.time()
	#tcm_hex = int(0)
	
	# 608 Var Init
	MS_608_id_text = "608"
	MS_608_detail_text = " "
	MS_608_hex_text = " "
	MS_608_time_text = " "
	MS_608_notes_text = " "
	MS_608_time = time.time()
	
	id_list = []
	id_line_text = " "
	
	

	while True:
		CAN_HEX = int(0)
		CAN_tmp = " "
		CAN_LINE = s.readline() # Read line from Serial port
		CAN_LINE = CAN_LINE.decode('utf-8')
		outfile.write(CAN_LINE) # log line to logfile
		CAN_tmp = CAN_LINE.split(" ")
		if( len(CAN_tmp) >= 4 ):
		
			CAN_ID = re.sub('^\[', '', CAN_tmp[2])
			CAN_ID = re.sub('\]\(00\)$', '', CAN_ID)
			CAN_ID = re.sub('^0+', '', CAN_ID)
			if(CAN_ID not in id_list):
				try:
					CAN_ID_HEX = int(CAN_ID,16)
					if((CAN_ID_HEX > 0xFF)  and (CAN_ID_HEX < 0xFFF)) : # Check if CAN ID is between assumed range
						id_list.append(CAN_ID)
						id_list.sort()
						id_line_text = id_list
				except:
					print(CAN_tmp[0] + " - Invalid CAN ID")
				
			if( len(CAN_tmp) == 5 ): # One Byte
				try:
					CAN_HEX = int(CAN_tmp[3],16)
				except: 
					print(CAN_tmp[0] + " - Failed to process value")
			
			if( len(CAN_tmp) == 6 ): # Two Bytes			
				try:
					CAN_HEX = int(CAN_tmp[3],16) # Convert str to hex
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[4],16) # Left shift and or next byte
				except: 
					print(CAN_tmp[0] + " - Failed to process value")
			
			if( len(CAN_tmp) == 11 ): # Seven Bytes
				try:			
					CAN_HEX = int(CAN_tmp[3],16) # Convert str to hex
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[4],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[5],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[6],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[7],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[8],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[9],16) # Left shift and or next byte
				except: 
					print(CAN_tmp[0] + " - Failed to process value")
			
			if( len(CAN_tmp) == 12 ): # Eight Bytes
				try:				
					CAN_HEX = int(CAN_tmp[3],16) # Convert str to hex
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[4],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[5],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[6],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[7],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[8],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[9],16) # Left shift and or next byte
					CAN_HEX = (CAN_HEX << 8) | int(CAN_tmp[10],16) # Left shift and or next byte
				except: 
					print(CAN_tmp[0] + " - Failed to process value")
					
			### IDs found 200 208 210 212 218 230 300 308 312 328 338 408 410 412 418 580 608 670 6F4
			##########################################################################################
			# 200 - ?
			# 208 - Wheel speed
			# 210 - ECU stuff - Cruise control stuff etc
			# 212 - ECU stuff - engine idle target speed
			# 218 - ECU stuff - manual shift mode
			# 230 - Shifter Status
			# 300 - Engine torque - steering angle sensor
			# 308 - ECU Stuff - oil levels and stuff
			# 312 - Engine Torque
			# 328 - Front Wheel Speeds?
			# 338 - Transmission output speed
			# 408 - fuel tank level, milage
			# 410 - AC - Outside air temp, air compressor stuff, fan speed set
			# 412 - speed, wheel speed
			# 418 - TCM status
			# 580 - Accel and Brake data?
			# 608 - ECU stuff - coolant temp
			# 670 - MESS1 ?
			# 6F4
			
			
			# 208 - 8 Bytes - Wheel Speed 
			# ECU NAME: BS_208h, ID: 0x0208. MSG COUNT: 16
			# MSG NAME: AKT_R_ESP - ESP / ART-wish: "Active downshift", OFFSET 0, LENGTH 1
			# MSG NAME: MINMAX_ART - Should speed requirement of ART, OFFSET 1, LENGTH 1
			# MSG NAME: GMAX_ESP - Target gear, upper limit, OFFSET 2, LENGTH 3
			# MSG NAME: GMIN_ESP - Target gear, lower limit, OFFSET 5, LENGTH 3
			# MSG NAME: DDYN_UNT - Suppression dynamic Vollastrückschaltung, OFFSET 8, LENGTH 1
			# MSG NAME: SZS - system state, OFFSET 9, LENGTH 2
			# MSG NAME: TM_AUS - Cruise control operation from, OFFSET 11, LENGTH 1
			# MSG NAME: SLV_ESP - Switching line shift ESP, OFFSET 12, LENGTH 4
			# MSG NAME: BRE_AKT_ESP - ESP brake intervention active, OFFSET 16, LENGTH 1
			# MSG NAME: ANFN - Insert "N": ESP request, OFFSET 17, LENGTH 2
			# MSG NAME: BRE_AKT_ART - ART-active brake intervention, OFFSET 19, LENGTH 1
			# MSG NAME: MBRE_ESP - Adjusted brake torque (BR240 factor of 1.8 larger), OFFSET 20, LENGTH 12
			# MSG NAME: DRTGHR - Direction of rotation right rear wheel, OFFSET 32, LENGTH 2
			# MSG NAME: DHR - Rear right wheel speed, OFFSET 34, LENGTH 14
			# MSG NAME: DRTGHL - Rotation direction left rear wheel, OFFSET 48, LENGTH 2
			# MSG NAME: DHL - Rear left wheel speed, OFFSET 50, LENGTH 14
			# 
			# 208 - One Byte - SZS_NEU ?
			# ECU NAME: BS_208h, ID: 0x0208. MSG COUNT: 1
			# MSG NAME: SZS_NEU - Systemzustand, OFFSET 9, LENGTH 2
			if(CAN_ID == "208"):
				whl_hex_text = hex(CAN_HEX)
				whl_time = time.time()
				
				whl_DRTGHR = get_hex_bits(CAN_HEX,32,2) # MSG NAME: DRTGHR - Direction of rotation right rear wheel, OFFSET 32, LENGTH 2
				whl_DHR = get_hex_bits(CAN_HEX,34,14) # MSG NAME: DHR - Rear right wheel speed, OFFSET 34, LENGTH 14
				whl_DRTGHL = get_hex_bits(CAN_HEX,48,2) # MSG NAME: DRTGHL - Rotation direction left rear wheel, OFFSET 48, LENGTH 2
				whl_DHL = get_hex_bits(CAN_HEX,50,14) # MSG NAME: DHL - Rear left wheel speed, OFFSET 50, LENGTH 14
				
				whl_notes_text = "RR Wheel Dir: " + str(whl_DRTGHR)
				whl_notes_text += " - LR Wheel Dir: " + str(whl_DRTGHL)
				whl_notes_text += " - RR Wheel Speed: " + str(whl_DHR)
				whl_notes_text += " - LR Wheel Speed: " + str(whl_DHL)
				print (CAN_tmp[0] + " - " + CAN_ID + " - len:" + str(len(CAN_tmp)) + " - " + hex(CAN_HEX) + " - " + whl_notes_text)
				
				
			# 210 ECU stuff - Cruise control stuff etc
			if(CAN_ID == "210"):
				ecu1_hex_text = hex(CAN_HEX)
				ecu1_time = time.time()
			
				# ECU NAME: MS_210h, ID: 0x0210. MSG COUNT: 35
				ecu1_KOMP_NOTAUS = get_hex_bits(CAN_HEX,0,1) # MSG NAME: KOMP_NOTAUS - Air compressor Emergency Shutdown, OFFSET 0, LENGTH 1
				# MSG NAME: SLV_MS - Switching line shift MS, OFFSET 1, LENGTH 4
				# MSG NAME: KRIECH_AUS - off KSG-creep, OFFSET 6, LENGTH 1
				# MSG NAME: ANF1 - MS-wish: "Approach 1.Gang", OFFSET 7, LENGTH 1
				# MSG NAME: AKT_R_MS - MS-wish: "Active downshift", OFFSET 8, LENGTH 1
				# MSG NAME: ZH_AUS_MS - off heater, OFFSET 9, LENGTH 1
				ecu1_GMAX_MS = get_hex_bits(CAN_HEX,10,3) # MSG NAME: GMAX_MS - Target gear, upper limit, OFFSET 10, LENGTH 3
				ecu1_GMIN_MS = get_hex_bits(CAN_HEX,13,3) # MSG NAME: GMIN_MS - Target gear, lower limit, OFFSET 13, LENGTH 3
				ecu1_PW = get_hex_bits(CAN_HEX,16,8) # MSG NAME: PW - pedal, OFFSET 16, LENGTH 8
				# MSG NAME: V_DSPL_NEU - retrigger minimum display time on the display, OFFSET 24, LENGTH 1
				# MSG NAME: LL_STBL - Idle is stable, OFFSET 25, LENGTH 1
				# MSG NAME: VGL_ST - Vorglühstatus, OFFSET 26, LENGTH 1
				# MSG NAME: MSS_DEF - Engine start / stop system defective, OFFSET 27, LENGTH 1
				# MSG NAME: MSS_KL - Engine start / stop system warning, OFFSET 28, LENGTH 1
				# MSG NAME: MSS_AKT - Engine start / stop system active, OFFSET 29, LENGTH 1
				# MSG NAME: KOMP_BAUS - turn air compressor: Acceleration, OFFSET 30, LENGTH 1
				# MSG NAME: CRASH_MS - Crash signal from motor control, OFFSET 31, LENGTH 1
				# MSG NAME: PWG_ERR - Error pedal sensor, OFFSET 32, LENGTH 1
				# MSG NAME: LL - Neutral, OFFSET 33, LENGTH 1
				# MSG NAME: KUEB_S_A - Beg. "Slip" lock-up clutch, OFFSET 34, LENGTH 1
				# MSG NAME: TM_REG - cruise control regulates, OFFSET 35, LENGTH 1
				# MSG NAME: V_MAX_EIN - Speed ​​limit switched, OFFSET 36, LENGTH 1
				# MSG NAME: KD_MS - Kick Down (changeover scenario open!), OFFSET 37, LENGTH 1
				# MSG NAME: NOTL - emergency operation, OFFSET 38, LENGTH 1
				# MSG NAME: V_MAX_SUM - Warning buzzer, OFFSET 39, LENGTH 1
				# MSG NAME: FBS_SE - FBS: Start Error, OFFSET 40, LENGTH 1
				# MSG NAME: V_DSPL_PGB - Display "winter tires limit reached" on the display, OFFSET 41, LENGTH 1
				# MSG NAME: TM_EIN - Cruise control switched on, OFFSET 42, LENGTH 1
				# MSG NAME: V_MAX_REG - Speed ​​controls, OFFSET 43, LENGTH 1
				# MSG NAME: V_DSPL_LIM - Display "limit?" on display, OFFSET 44, LENGTH 1
				# MSG NAME: V_DSPL_ERR - "Error" indicator on the display, OFFSET 45, LENGTH 1
				# MSG NAME: V_DSPL_BL - display flashes, OFFSET 46, LENGTH 1
				# MSG NAME: V_DSPL_EIN - Geschw.begrenzer- / cruise control display a, OFFSET 47, LENGTH 1
				# MSG NAME: FMMOTMAX - Factor for fill value. d. Max. Mom with remo.. A.druck, OFFSET 48, LENGTH 8
				# MSG NAME: V_MAX_TM - Set maximum or cruise control speed, OFFSET 56, LENGTH 8
				
				ecu1_notes_text = "Max Traget Gear: " + str(ecu1_GMAX_MS)
				ecu1_notes_text += " - Min Target Gear: " + str(ecu1_GMIN_MS)
				ecu1_notes_text += " - Pedal: " + str(ecu1_PW)
				print (CAN_tmp[0] + " - " + CAN_ID + " - len:" + str(len(CAN_tmp)) + " - " + hex(CAN_HEX) + " - " + ecu1_notes_text)
			
			# 212 ECU stuff - engine idle target speed
			if(CAN_ID == "212"):
				ecu2_hex_text = hex(CAN_HEX)
				ecu2_time = time.time()
				
				# ECU NAME: MS_212h, ID: 0x0212. MSG COUNT: 11
				ecu2_NMOTS = get_hex_bits(CAN_HEX,0,16) # MSG NAME: NMOTS - Engine idling target speed, OFFSET 0, LENGTH 16
				# MSG NAME: TM_MS - Series Cruise control is variant encodes, OFFSET 17, LENGTH 1
				# MSG NAME: M_ART_E - Enable torque requirement ART, OFFSET 18, LENGTH 1
				# MSG NAME: M_FV - Default moment driver, OFFSET 19, LENGTH 13
				# MSG NAME: SME_E - Enable Quick torque adjustment, OFFSET 33, LENGTH 1
				# MSG NAME: M_ESP_E - Enable torque request ESP, OFFSET 34, LENGTH 1
				# MSG NAME: M_FEV - Spare default torque driver, OFFSET 35, LENGTH 13
				# MSG NAME: CALID_CVN_E - Transmission CALID / CVN enable, OFFSET 48, LENGTH 1
				# MSG NAME: M_EGS_Q - Acknowledgment torque request EGS, OFFSET 49, LENGTH 1
				# MSG NAME: M_EGS_E - Enable torque request EGS, OFFSET 50, LENGTH 1
				# MSG NAME: M_ESPV - Default moment ESP, OFFSET 51, LENGTH 13	
				
				ecu2_notes_text = "Engine Idle Target: " + str(ecu2_NMOTS)
				print (CAN_tmp[0] + " - " + CAN_ID + " - len:" + str(len(CAN_tmp)) + " - " + hex(CAN_HEX) + " - " + ecu2_notes_text)
				
				
			# 218 - ECU stuff - manual shift mode	
			if(CAN_ID == "218"):
				GS_218_hex_text = hex(CAN_HEX)
				GS_218_time = time.time()
			
				# ECU NAME: GS_218h, ID: 0x0218. MSG COUNT: 31
				# MSG NAME: MTGL_EGS - Motormomentenanf. Toggle 40ms + -10, OFFSET 0, LENGTH 1
				# MSG NAME: MMIN_EGS - Engine torque requirement Min, OFFSET 1, LENGTH 1
				# MSG NAME: MMAX_EGS - Engine torque requirement Max, OFFSET 2, LENGTH 1
				# MSG NAME: M_EGS - Geford. engine torque, OFFSET 3, LENGTH 13
				# MSG NAME: GZC - Target gear, OFFSET 16, LENGTH 4
				# MSG NAME: GIC - Actual gear, OFFSET 20, LENGTH 4
				GS_218_K_S_B = get_hex_bits(CAN_HEX,24,1) # MSG NAME: K_S_B - Best. (Wandlerüberbrück.-) clutch "slipping", OFFSET 24, LENGTH 1
				GS_218_K_O_B = get_hex_bits(CAN_HEX,25,1) # MSG NAME: K_O_B - Best. (Wandlerüberbrück.-) Clutch "open", OFFSET 25, LENGTH 1
				GS_218_K_G_B = get_hex_bits(CAN_HEX,26,1) # MSG NAME: K_G_B - Best. (Wandlerüberbrück.-) clutch "closed", OFFSET 26, LENGTH 1
				# MSG NAME: G_G - off-road gear, OFFSET 27, LENGTH 1
				# MSG NAME: GSP_OK - Basic shift program O.K., OFFSET 28, LENGTH 1
				# MSG NAME: FW_HOCH - Driving resistance is high, OFFSET 29, LENGTH 1
				# MSG NAME: SCHALT - circuit, OFFSET 30, LENGTH 1
				GS_218_HSM = get_hex_bits(CAN_HEX,31,1) # MSG NAME: HSM - Manual shift mode, OFFSET 31, LENGTH 1
				GS_218_GET_OK = get_hex_bits(CAN_HEX,32,1) # MSG NAME: GET_OK - transmission ok, OFFSET 32, LENGTH 1
				# MSG NAME: KS - start bang, OFFSET 33, LENGTH 1
				# MSG NAME: ALF - start enabling, OFFSET 34, LENGTH 1
				# MSG NAME: GS_NOTL - GS in emergency operation, OFFSET 35, LENGTH 1
				# MSG NAME: UEHITZ_GET - Overtemperature gear, OFFSET 36, LENGTH 1
				# MSG NAME: KD - Kick down, OFFSET 37, LENGTH 1
				# MSG NAME: FPC_AAD - Driving program for AAD, OFFSET 38, LENGTH 2
				# MSG NAME: MPAR_EGS - Engine torque request parity (even parity), OFFSET 40, LENGTH 1
				# MSG NAME: DYN1_EGS - Engagement mode / drive torque control, OFFSET 41, LENGTH 1
				# MSG NAME: DYN0_AMR_EGS - Engagement mode / drive torque control, OFFSET 42, LENGTH 1
				# MSG NAME: K_LSTFR - Converter lockup clutch free of load, OFFSET 45, LENGTH 1
				# MSG NAME: MOT_NAUS_CNF - MOT_NAUS-Confirmbit, OFFSET 46, LENGTH 1
				# MSG NAME: MOT_NAUS - Motor Emergency Shutdown, OFFSET 47, LENGTH 1
				# MSG NAME: MKRIECH - Creep (FFh at EGS, CVT) or CALID / CVN, OFFSET 48, LENGTH 8
				# MSG NAME: FEHLPRF_ST - Status error checking, OFFSET 56, LENGTH 2
				# MSG NAME: CALID_CVN_AKT - CALID / CVN-transmission active, OFFSET 58, LENGTH 1
				# MSG NAME: FEHLER - Error number or counter for CALID / CVN transmission, OFFSET 59, LENGTH 5
				
				GS_218_notes_text = "Manual Shift Mode: " + str(GS_218_HSM)
				GS_218_notes_text += " - Transmission OK: " + str(GS_218_GET_OK)
				GS_218_notes_text += " - Clutch Slipping: " + str(GS_218_K_S_B)
				GS_218_notes_text += " - Clutch Open: " + str(GS_218_K_O_B)
				GS_218_notes_text += " - Clutch Closed: " + str(GS_218_K_G_B)
				print (CAN_tmp[0] + " - " + CAN_ID + " - len:" + str(len(CAN_tmp)) + " - " + hex(CAN_HEX) + " - " + GS_218_notes_text)
				
				
			# 230 Shifter Status
			#
			# ECU NAME: EWM_230h, ID: 0x0230. MSG COUNT: 5
			# MSG NAME: W_S - driving program, OFFSET 0, LENGTH 1
			# MSG NAME: FPT - Driving program button is pressed, OFFSET 1, LENGTH 1
			# MSG NAME: KD - Kick down, OFFSET 2, LENGTH 1
			# MSG NAME: SPERR - Blocking coil energized, OFFSET 3, LENGTH 1
			# MSG NAME: WHC - Gear selector lever position (NOS only), OFFSET 4, LENGTH 4
			if(CAN_ID == "230"):
				#shift_id_text = CAN_ID
								
				#shift_detail_text = CAN_DETAIL
				shift_hex_text = hex(CAN_HEX)
				shift_bin_text = "0b" + format(CAN_HEX, "b")
				shift_time = time.time()
				
				shift_W_S = get_byte_bits(CAN_HEX,0,1) # MSG NAME: W_S - driving program, OFFSET 0, LENGTH 1
				shift_FPT = get_byte_bits(CAN_HEX,1,1) # MSG NAME: FPT - Driving program button is pressed, OFFSET 1, LENGTH 1
				shift_KD = get_byte_bits(CAN_HEX,2,1) # MSG NAME: KD - Kick down, OFFSET 2, LENGTH 1
				shift_SPERR = get_byte_bits(CAN_HEX,3,1) # MSG NAME: SPERR - Blocking coil energized, OFFSET 3, LENGTH 1
				shift_WHC = get_byte_bits(CAN_HEX,4,4) # MSG NAME: WHC - Gear selector lever position (NOS only), OFFSET 4, LENGTH 4
				
				if (shift_WHC == 0x5):
					shift_detail_text = "Drive"
				elif (shift_WHC == 0x6):
					shift_detail_text = "Neutral"
				elif (shift_WHC == 0x7):
					shift_detail_text = "Reverse"
				elif (shift_WHC == 0x8):
					shift_detail_text = "Park"
				elif (shift_WHC == 0x9):
					shift_detail_text = "Shift+"
				elif (shift_WHC == 0xA):
					shift_detail_text = "Shift-"
				else:
					shift_detail_text = " "
							
				shift_notes_text = "W_S: " + str(shift_W_S)
				shift_notes_text += " - FPT: " + str(shift_FPT)
				shift_notes_text += " - KD: " + str(shift_KD)
				shift_notes_text += " - SPERR: " + str(shift_SPERR)
				shift_notes_text += " - WHC: " + str(shift_WHC)
				shift_notes_text += " - " +  shift_detail_text
				print (CAN_tmp[0] + " - " + CAN_ID + " - len:" + str(len(CAN_tmp)) + " - " + hex(CAN_HEX) + " - " + shift_notes_text)
			
			
			# 338 - Transmission output speed
			if(CAN_ID == "338"):
				tcm2_hex_text = hex(CAN_HEX)
				tcm2_time = time.time()
				
				
				# ECU NAME: GS_338h, ID: 0x0338. MSG COUNT: 2
				tcm2_NAB = get_hex_bits(CAN_HEX,0,16) # MSG NAME: NAB - Transmission output speed (only 463/461, otherwise FFFFh), OFFSET 0, LENGTH 16
				tcm2_NTURBINE = get_hex_bits(CAN_HEX,48,16) # MSG NAME: NTURBINE - Turbine speed (EGS52-NAG, VGS NAG2), OFFSET 48, LENGTH 16	
				
				tcm2_notes_text = "Transmission output speed: " + str(tcm2_NAB)
				tcm2_notes_text += " - Turbine speed: " + str(tcm2_NTURBINE)
				print (CAN_tmp[0] + " - " + CAN_ID + " - len:" + str(len(CAN_tmp)) + " - " + hex(CAN_HEX) + " - " + tcm2_notes_text)
			
			# 408 - fuel tank level, milage
			if(CAN_ID == "408"):
				KOMBI_408_hex_text = hex(CAN_HEX)
				KOMBI_408_time = time.time()
				
				# ECU NAME: KOMBI_408h, ID: 0x0408. MSG COUNT: 19
				KOMBI_408_TANK_FS = get_hex_bits(CAN_HEX,0,8) # MSG NAME: TANK_FS - tank level, OFFSET 0, LENGTH 8
				# MSG NAME: TF_AUF - Driver's door, OFFSET 8, LENGTH 1
				# MSG NAME: V_DSPL_AUS - Geschw.begrenzer- / cruise control display not possible, OFFSET 9, LENGTH 1
				# MSG NAME: TACHO_SYM - Tachoeichung, OFFSET 10, LENGTH 1
				KOMBI_408_V_MPH = get_hex_bits(CAN_HEX,11,1) # MSG NAME: V_MPH - mph instead km / h (variable Geschwindigkeitsbegr.), OFFSET 11, LENGTH 1
				# MSG NAME: KLA_VH - Air conditioning available, OFFSET 12, LENGTH 1
				# MSG NAME: VGL_KL_DEF - Preglow pilot defective, OFFSET 13, LENGTH 1
				# MSG NAME: TFSM - Tank level minimum, OFFSET 14, LENGTH 1
				# MSG NAME: KL_61E - Terminal 61 decoupled, OFFSET 15, LENGTH 1
				KOMBI_408_T_AUSSEN = get_hex_bits(CAN_HEX,16,8) # MSG NAME: T_AUSSEN - Outside air temperature raw value, OFFSET 16, LENGTH 8
				# MSG NAME: KL_58D - Terminal 58 dimmed, OFFSET 24, LENGTH 8
				# MSG NAME: MAZ - Motorabstellzeit (is sent from terminal 15), OFFSET 32, LENGTH 8
				KOMBI_408_KM16 = get_hex_bits(CAN_HEX,40,16) # MSG NAME: KM16 - mileage, OFFSET 40, LENGTH 16
				# MSG NAME: WRC3 - Winter tire speed Bit 3, OFFSET 56, LENGTH 1
				# MSG NAME: V_DSPL_AKT - Geschw.begrenzer- / cruise control display active, OFFSET 57, LENGTH 1
				# MSG NAME: SGT_VH - Segment tachometer available, OFFSET 58, LENGTH 1
				# MSG NAME: ZH_FREIG - enable auxiliary heaters, OFFSET 59, LENGTH 1
				# MSG NAME: RT_EIN - Roll test mode ESP switch, OFFSET 60, LENGTH 1
				# MSG NAME: WRC - Winter tire speed with 4 bits, OFFSET 61, LENGTH 3
				
				KOMBI_408_T_AUSSEN = round(((KOMBI_408_T_AUSSEN * (9/5)) + 32),1) # Temp C to F
				
				KOMBI_408_notes_text = "Tank Level: " + str(KOMBI_408_TANK_FS)
				KOMBI_408_notes_text += " - Speed : " + str(KOMBI_408_V_MPH) + "kph"
				KOMBI_408_notes_text += " - Outside Air Temp: " + str(KOMBI_408_T_AUSSEN) + "F"
				KOMBI_408_notes_text += " - Milage " + str(KOMBI_408_KM16)
				print (CAN_tmp[0] + " - " + CAN_ID + " - len:" + str(len(CAN_tmp)) + " - " + hex(CAN_HEX) + " - " + KOMBI_408_notes_text)	
				
				
			# 412 - speed, wheel speed
			if(CAN_ID == "412"):
				KOMBI_412_hex_text = hex(CAN_HEX)
				KOMBI_412_time = time.time()
				
				# ECU NAME: KOMBI_412h, ID: 0x0412. MSG COUNT: 11
				# MSG NAME: AKU_WARN_AUS - Acoustic warning, OFFSET 0, LENGTH 1
				# MSG NAME: OPT_WARN_AUS - Optical warning, OFFSET 1, LENGTH 1
				# MSG NAME: ECO_WARN_ST - Status ECO Warning, OFFSET 4, LENGTH 1
				# MSG NAME: ABST_S - distance unit, OFFSET 8, LENGTH 1
				# MSG NAME: IST_ABST - set distance, OFFSET 9, LENGTH 3
				KOMBI_412_V_ANZ = get_hex_bits(CAN_HEX,12,12) # MSG NAME: V_ANZ - Displaying speed, OFFSET 12, LENGTH 12
				# MSG NAME: DRTGANZ - Wheel rotation to V_ANZ, OFFSET 24, LENGTH 2
				KOMBI_412_DANZ = get_hex_bits(CAN_HEX,26,14) # MSG NAME: DANZ - Wheel speed calculated from V_ANZ, OFFSET 26, LENGTH 14
				# MSG NAME: ECO_AKT - ECO activation in combination menu, OFFSET 44, LENGTH 1
				# MSG NAME: PRW_ANF - Requirement Platt Roll Warner, OFFSET 46, LENGTH 2
				# MSG NAME: MAZ_NEU - Motorabstellzeit, OFFSET 52, LENGTH 12
				
				KOMBI_412_notes_text = "Speed: " + str(KOMBI_412_V_ANZ)
				KOMBI_412_notes_text += " - Calculated Wheel Speed : " + str(KOMBI_412_DANZ)
				print (CAN_tmp[0] + " - " + CAN_ID + " - len:" + str(len(CAN_tmp)) + " - " + hex(CAN_HEX) + " - " + KOMBI_412_notes_text)	
					
			
			# 418 TCM Status
			#
			# ECU NAME: GS_418h, ID: 0x0418. MSG COUNT: 17
			# MSG NAME: FSC - driving position, OFFSET 0, LENGTH 8
			# MSG NAME: FPC - driving program, OFFSET 8, LENGTH 8
			# MSG NAME: T_GET - Transmission oil temperature, OFFSET 16, LENGTH 8
			# MSG NAME: ALLRAD - all wheel drive, OFFSET 24, LENGTH 1
			# MSG NAME: FRONT - Front-wheel drive [1], rear-wheel drive [0], OFFSET 25, LENGTH 1
			# MSG NAME: SCHALT - circuit, OFFSET 26, LENGTH 1
			# MSG NAME: CVT - Continuously variable transmission [1], step transmission [0], OFFSET 27, LENGTH 1
			# MSG NAME: MECH - Gear-mechanism variant, OFFSET 28, LENGTH 2
			# MSG NAME: ESV_BRE - Brake invest in power-, OFFSET 30, LENGTH 1
			# MSG NAME: KD - Kick down, OFFSET 31, LENGTH 1
			# MSG NAME: GZC - Target gear, OFFSET 32, LENGTH 4
			# MSG NAME: GIC - Actual gear, OFFSET 36, LENGTH 4
			# MSG NAME: M_VERL - Loss torque (FFh at KSG), OFFSET 40, LENGTH 8
			# MSG NAME: FMRADPAR - Factor wheel torque parity (even parity), OFFSET 48, LENGTH 1
			# MSG NAME: FMRADTGL - Factor wheel torque Toggle 40ms + -10, OFFSET 49, LENGTH 1
			# MSG NAME: WHST - Gear selector lever position (NAG, KSG, CVT), OFFSET 50, LENGTH 3
			# MSG NAME: FMRAD - Factor wheel torque (7FFh KSG), OFFSET 53, LENGTH 11	
			# TCM 0x418
			# 50 53 ?? ?? DD ?? ?? 00 -park
			# 52 53 ?? ?? BB ?? ?? 5B -reverse
			# 4E 53 ?? ?? 00 ?? ?? 00 -neutral
			# 44 53 ?? ?? 11 ?? ?? B4 -drive
			# 31 53 ?? ?? 11 ?? ?? B4 -max gear 1
			# 32 53 ?? ?? 11 ?? ?? B4 -max gear 2
			# 33 53 ?? ?? 11 ?? ?? B4 -max gear 3
			# 34 53 ?? ?? 11 ?? ?? B4 -max gear 4
			# 50 57 ?? ?? DD ?? ?? 00 -park with S/W
			# 52 57 ?? ?? BB ?? ?? 5B -reverse with S/W
			# 42 57 ?? ?? 00 ?? ?? 00 -neutral with S/W
			# 44 57 ?? ?? 22 ?? ?? 0B -drive with S/W 
			if(CAN_ID == "418"):
				tcm_hex_text = hex(CAN_HEX)
				tcm_time = time.time()
				#tcm_bin_text = "0b" + format(CAN_HEX, "b")
				
				tcm_oil_temp = get_hex_bits(CAN_HEX,16,8) # MSG NAME: T_GET - Transmission oil temperature, OFFSET 16, LENGTH 8
				tcm_target_gear = get_hex_bits(CAN_HEX,32,4) # MSG NAME: GZC - Target gear, OFFSET 32, LENGTH 4
				tcm_actual_gear = get_hex_bits(CAN_HEX,36,4) # MSG NAME: GIC - Actual gear, OFFSET 36, LENGTH 4
				
				tcm_FCS = get_hex_bits(CAN_HEX,0,8) # MSG NAME: FSC - driving position, OFFSET 0, LENGTH 8
				tcm_FPC = get_hex_bits(CAN_HEX,8,8) # MSG NAME: FPC - driving program, OFFSET 8, LENGTH 8
				tcm_T_GET = get_hex_bits(CAN_HEX,16,8) # MSG NAME: T_GET - Transmission oil temperature, OFFSET 16, LENGTH 8
				tcm_ALLRAD = get_hex_bits(CAN_HEX,24,1) # MSG NAME: ALLRAD - all wheel drive, OFFSET 24, LENGTH 1
				tcm_FRONT = get_hex_bits(CAN_HEX,25,1) # MSG NAME: FRONT - Front-wheel drive [1], rear-wheel drive [0], OFFSET 25, LENGTH 1
				tcm_SCHALT = get_hex_bits(CAN_HEX,26,1) # MSG NAME: SCHALT - circuit, OFFSET 26, LENGTH 1
				tcm_CVT = get_hex_bits(CAN_HEX,27,1) # MSG NAME: CVT - Continuously variable transmission [1], step transmission [0], OFFSET 27, LENGTH 1
				tcm_MECH = get_hex_bits(CAN_HEX,28,2) # MSG NAME: MECH - Gear-mechanism variant, OFFSET 28, LENGTH 2
				tcm_ESV_BRE = get_hex_bits(CAN_HEX,30,1) # MSG NAME: ESV_BRE - Brake invest in power-, OFFSET 30, LENGTH 1
				tcm_KD = get_hex_bits(CAN_HEX,31,1) # MSG NAME: KD - Kick down, OFFSET 31, LENGTH 1
				tcm_GZC = get_hex_bits(CAN_HEX,32,4) # MSG NAME: GZC - Target gear, OFFSET 32, LENGTH 4
				tcm_GIC = get_hex_bits(CAN_HEX,36,4) # MSG NAME: GIC - Actual gear, OFFSET 36, LENGTH 4
				tcm_M_VERL = get_hex_bits(CAN_HEX,40,8) # MSG NAME: M_VERL - Loss torque (FFh at KSG), OFFSET 40, LENGTH 8
				tcm_FMRADPAR = get_hex_bits(CAN_HEX,48,1) # MSG NAME: FMRADPAR - Factor wheel torque parity (even parity), OFFSET 48, LENGTH 1
				tcm_FMRADTGL = get_hex_bits(CAN_HEX,49,1) # MSG NAME: FMRADTGL - Factor wheel torque Toggle 40ms + -10, OFFSET 49, LENGTH 1
				tcm_WHST = get_hex_bits(CAN_HEX,50,3) # MSG NAME: WHST - Gear selector lever position (NAG, KSG, CVT), OFFSET 50, LENGTH 3
				tcm_FMRAD = get_hex_bits(CAN_HEX,53,11) # MSG NAME: FMRAD - Factor wheel torque (7FFh KSG), OFFSET 53, LENGTH 11
				
				tcm_oil_temp = round(((tcm_T_GET * (9/5)) + 32),1)
				
				tcm_notes_text = "Temp: " + str(tcm_oil_temp) + "F"
				tcm_notes_text += " - Target Gear: " + str(tcm_GZC)
				tcm_notes_text += " - Actual Gear: " + str(tcm_GIC)
				tcm_notes_text += " - Lever Position: " + str(tcm_WHST)
				print (CAN_tmp[0] + " - " + CAN_ID + " - len:" + str(len(CAN_tmp)) + " - " + hex(CAN_HEX) + " - " + tcm_notes_text)
			
			
			# 608 - ECU stuff - coolant temp
			if(CAN_ID == "608"):
				MS_608_hex_text = hex(CAN_HEX)
				MS_608_time = time.time()
				
				# ECU NAME: MS_608h, ID: 0x0608. MSG COUNT: 13
				MS_608_T_MOT = get_hex_bits(CAN_HEX,0,8) # MSG NAME: T_MOT - Engine coolant temperature, OFFSET 0, LENGTH 8
				# MSG NAME: T_LUFT - intake, OFFSET 8, LENGTH 8
				# MSG NAME: FCOD_KAR - Vehicle code body, OFFSET 16, LENGTH 3
				# MSG NAME: FCOD_BR - Vehicle Code series, OFFSET 19, LENGTH 5
				# MSG NAME: FCOD_MOT6 - Motor vehicle code with 7-bit, bit 6, OFFSET 24, LENGTH 1
				# MSG NAME: GS_NVH - Transmission control No, OFFSET 25, LENGTH 1
				# MSG NAME: FCOD_MOT - Fzgcod.Motor 7Bit, Bit0-5 (Bit6 -> Signal FCOD_MOT6), OFFSET 26, LENGTH 6
				# MSG NAME: V_MAX_FIX - fixed speed, OFFSET 32, LENGTH 8
				# MSG NAME: VB - consumption, OFFSET 40, LENGTH 16
				# MSG NAME: ZWP_EIN_MS - Switch on auxiliary water pump, OFFSET 56, LENGTH 1
				# MSG NAME: PFW - particulate filter warning, OFFSET 57, LENGTH 2
				# MSG NAME: ZVB_EIN_MS - Turn on additional consumer, OFFSET 59, LENGTH 1
				# MSG NAME: PFKO - Particulate filter correction offset FMMOTMAX, OFFSET 60, LENGTH 4
				
				MS_608_T_MOT = round(((MS_608_T_MOT * (9/5)) + 32),1) # Temp C to F
				
				MS_608_notes_text = "Engine Coolant Tempature: " + str(MS_608_T_MOT) + "F"
				print (CAN_tmp[0] + " - 608 - len:" + str(len(CAN_tmp)) + " - " + hex(CAN_HEX) + " - " + MS_608_notes_text)	
			
				
		
			
			
				
				

		now = time.time()
		
		
		 
		row1_text = 'CAN ID	Age	Details'
		# 208
		row2_text = whl_id_text + "\t" + format(round((now - whl_time),1)) + "\t" + whl_notes_text
		# 210
		row3_text = ecu1_id_text + "\t" + format(round((now - ecu1_time),1)) + "\t" + ecu1_notes_text
		# 212
		row4_text = ecu2_id_text + "\t" + format(round((now - ecu2_time),1)) + "\t" + ecu2_notes_text
		# 218
		row5_text = GS_218_id_text + "\t" + format(round((now - GS_218_time),1)) + "\t" + GS_218_notes_text
		# 230
		row6_text = shift_id_text + "\t" + format(round((now - shift_time),1)) + "\t" + shift_notes_text
		# 338
		row7_text = tcm2_id_text + "\t" + format(round((now - tcm2_time),1)) + "\t" + tcm2_notes_text
		# 408
		row8_text = KOMBI_408_id_text + "\t" + format(round((now - KOMBI_408_time),1)) + "\t" + KOMBI_408_notes_text
		# 412
		row9_text = KOMBI_412_id_text + "\t" + format(round((now - KOMBI_412_time),1)) + "\t" + KOMBI_412_notes_text
		# 418 TCM Status
		row10_text = tcm_id_text + "\t" + format(round((now - tcm_time),1)) + "\t" + tcm_notes_text
		# 608 - ECU stuff - coolant temp
		row11_text = MS_608_id_text + "\t" + format(round((now - MS_608_time),1)) + "\t" + MS_608_notes_text + "\n\n\n"
		
		

		
		
		# Update Shift Row 1
		#shift_id_lbl.config(text=shift_id_text)
		#shift_detail_lbl.config(text=shift_detail_text)
		#shift_hex_lbl.config(text=shift_hex_text)
		#shift_bin_lbl.config(text=shift_bin_text)
		#shift_time_lbl.config(text=format(round((now - shift_time),1)))
		
		# Update Shift Notes Row 2
		#shift_notes_lbl.config(text=shift_notes_text)
		
		# Update TCM Status Row 3 
		#tcm_id_lbl.config(text=tcm_id_text)
		#tcm_detail_lbl.config(text=tcm_detail_text)
		#tcm_hex_lbl.config(text=tcm_hex_text)
		#tcm_bin_lbl.config(text=tcm_bin_text)
		#tcm_time_lbl.config(text=format(round((now - tcm_time),1)))
		
		# Update TCM Notes Row 4
		#tcm_notes_lbl.config(text=tcm_notes_text)
		
		# Update CAN ID list line
		#id_line_lbl.config(text=id_line_text)
		
		# Update last CAN data line
		#can_line_lbl.config(text=CAN_LINE)
		
		row1_lbl.config(text=row1_text)
		row2_lbl.config(text=row2_text)
		row3_lbl.config(text=row3_text)
		row4_lbl.config(text=row4_text)
		row5_lbl.config(text=row5_text)
		row6_lbl.config(text=row6_text)
		row7_lbl.config(text=row7_text)
		row8_lbl.config(text=row8_text)
		row9_lbl.config(text=row9_text)
		row10_lbl.config(text=row10_text)
		row11_lbl.config(text=row11_text)
		row12_lbl.config(text=id_line_text)
		row13_lbl.config(text=CAN_LINE)
		
		ws.update()
	    
	ws.mainloop()
	
	
else:
	print ("Format issue: CAN_GUI.py <Serial Port>")
