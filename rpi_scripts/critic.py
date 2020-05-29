import RPi.GPIO as GPIO, time

pin = 4
pin2 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)


GPIO.cleanup(pin)
GPIO.cleanup(pin2)