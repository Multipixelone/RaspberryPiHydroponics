#!/usr/bin/env python
# Made by Multipixelone
# Pump Controller
import RPi.GPIO as GPIO
#import schedule
from time import sleep

def valveOn():
    while True:
        GPIO.output(18, GPIO.HIGH)
        print("Valve On")
def valveOff():
    while True:
        GPIO.output(18, GPIO.LOW)
        print("Valve Off")
def Cycle():
    valveOn()
    sleep(5)  # Some Check of Water...?
    valveOff()
