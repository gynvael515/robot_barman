import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

pins = [4, 13, 21]

for pin in pins:
	GPIO.setup(pin, GPIO.OUT)

for pin in pins:
	GPIO.cleanup(pin)
