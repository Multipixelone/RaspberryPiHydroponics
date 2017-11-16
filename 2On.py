#!/usr/bin/env python
# Made by Multipixelone
# Controller for Lights
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, 1)
print("Lights On")
GPIO.cleanup()
