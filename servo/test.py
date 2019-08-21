import serial
import time
import keyboard

port ="/dev/ttyUSB0"

s1 = serial.Serial(port,9600)
s1.flushInput()


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
            pass
    except:
        break 
'''
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
'''
