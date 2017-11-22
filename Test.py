import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 0)
print("OFF")
sleep(2)
GPIO.output(17, 1)
print("ON")
sleep(5)
GPIO.output(17, 0)
print("OFF")
sleep(5)
GPIO.cleanup()
