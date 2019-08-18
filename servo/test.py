import serial
import time

port ="/dev/ttyUSB0"

s1 = serial.Serial(port,9600)
s1.flushInput()

for x in range(1,90):
	s1.write('1\r')