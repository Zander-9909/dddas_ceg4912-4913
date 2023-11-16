import requests
from datetime import datetime
import sys

import RPi.GPIO as GPIO
import time
from pulsesensor import Pulsesensor

def postSensorData():
	formatJson = {
		"BPM": 100,
		"DIST": 1.05,
		"POS": "idk"
	}
	
	request = requests.post("https://127.0.0.1:5000/data", json=formatJson)
	
if __name__ == '__main__':
	i = 0
	try:
		while True:
			postSensor()
			print(f"Test {i}")
			time.sleep(2)
			i+=1
			
	except KeyboardInterrupt:
		print("Program stopped by User")
