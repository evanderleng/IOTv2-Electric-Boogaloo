import serial
import time
import keyboard  # using module keyboard

port ="/dev/ttyUSB0"

s1 = serial.Serial(port,9600)
s1.flushInput()
try:
	while True:  # making a loop
		if keyboard.is_pressed('w'):  # if key 'q' is pressed 
	            s1.write('3\r')
	        else:
	            pass
		if keyboard.is_pressed('s'):  # if key 's' is pressed 
	            s1.write('4\r')
	        else:
	            pass
	
		if keyboard.is_pressed('a'):  # if key 'q' is pressed 
	            s1.write('1\r')
	        else:
	            pass
		if keyboard.is_pressed('d'):  # if key 's' is pressed 
	            s1.write('2\r')
	        else:
	            pass
except:
		print("test")