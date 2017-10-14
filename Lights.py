#!/usr/bin/env python
# Made by Multipixelone
# Controller for Lights
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

def LightsOn():
    GPIO.output(2, GPIO.HIGH)
    print("Lights On")
def LightsOff():
    GPIO.output(2, GPIO.LOW)
