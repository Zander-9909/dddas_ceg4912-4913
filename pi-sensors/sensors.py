import RPi.GPIO as GPIO
import time
from pulsesensor import Pulsesensor

GPIO.setmode(GPIO.BCM)

# Ultrasonic Sensor
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Rumble Motor
GPIO_RUMBLE = 25
GPIO.setup(GPIO_RUMBLE, GPIO.OUT)

# Pulse Sensor Object Creation
p = Pulsesensor()
p.startAsyncBPM()


def get_ultrasonic_distance():
	GPIO.output(GPIO_TRIGGER, True)
	
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	
	StartTime = time.time()
	StopTime = time.time()
	
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
		
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
		
	TimeElapsed = StopTime - StartTime
	
	distance = (TimeElapsed * 34300) / 2
	
	return distance
	

def rumble_on():
	GPIO.output(GPIO_RUMBLE, True)

def rumble_off():
	GPIO.output(GPIO_RUMBLE, False)
	
if __name__ == '__main__':
	try:
		while True:
			distance = get_ultrasonic_distance()
			print(f"Measured distance: {distance} cm")
			bpm = p.BPM
			
			if bpm > 0:
				print("BPM: %d" % bpm)
			else:
				print("No heartbeat detected.")
			time.sleep(1)
			
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()



