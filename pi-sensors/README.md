# Hardware setup

## Pulse sensor

Base code from: https://github.com/tutRPi/Raspberry-Pi-Heartbeat-Pulse-Sensor/tree/master

First install spidev
	$ pip install spidev
	
Make sure SPI interface is enabled on raspi-config. Pulse sensor is using SPI0.

## Ultrasonic sensor

No dependencies, asides from RPi.GPIO which is installed with the pi.

## GPS Receiver

Disable serial shell login.

Run command sudo 
	$ apt-get install gpsd gpsd-
	
To show raw GPS output

	$ cat /dev/serial 0
	

