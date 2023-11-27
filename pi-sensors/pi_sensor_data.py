import requests
from datetime import datetime
import sys

import RPi.GPIO as GPIO
import time
from pulsesensor import Pulsesensor

GPIO.setmode(GPIO.BCM)

# Ultrasonic Sensor
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


# Pulse Sensor Object Creation
p = Pulsesensor()
p.startAsyncBPM()


# Rumble Motor
GPIO_RUMBLE = 25
GPIO.setup(GPIO_RUMBLE, GPIO.OUT)


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

def postSensorData():
	bpm = p.BPM
	distance = get_ultrasonic_distance()
	print('Heartrate: '+str(bpm))
	print('Distance: ' + str(distance))
	formatJson = {
		"type":"bpm",
		"heartrate": bpm,
		"ultrasonic": distance
	}
	request = requests.post("http://100.72.37.45:5000/data", json=formatJson)
	if (dict(request.json()).get("rumble")):
		rumble_on()
	else:
		rumble_off()
	print(dict(request.json()).get("rumble"))
	
if __name__ == '__main__':
	try:
		while True:
			postSensorData()
			time.sleep(2)

	except KeyboardInterrupt:
		print("Program stopped by User")
		GPIO.cleanup()
