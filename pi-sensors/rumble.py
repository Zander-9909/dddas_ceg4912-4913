import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_RUMBLE = 25

GPIO.setup(GPIO_RUMBLE, GPIO.OUT)

def rumble():
	print("Rumble")
	GPIO.output(GPIO_RUMBLE, True)
	time.sleep(1)
	GPIO.output(GPIO_RUMBLE, False)
	time.sleep(1)
	
if __name__ == '__main__':
	try:
		while True:
			rumble()	
	except KeyboardInterrupt:
		print("Rumble stopped by User")
		GPIO.cleanup()
	
