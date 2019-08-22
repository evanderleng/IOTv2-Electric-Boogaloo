from receive import receive_messages
from publish import publish_messages
from google.oauth2 import service_account
from time import sleep
from random import randrange



while True:   
	publish_messages("gungnir-249212", "data",light_value)
	GPIO.setwarnings(False)
	if light_value > 0.9:
		print("LightOn")
		GPIO.output(18,GPIO.HIGH)
	else:
		GPIO.output(18,GPIO.LOW)
	sleep(9)

