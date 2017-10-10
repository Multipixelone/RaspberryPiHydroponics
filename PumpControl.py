#!/usr/bin/env python
# Made by Multipixelone
# Pump Controller
import RPi.GPIO as GPIO
# import schedule
from time import sleep

def valveOn():
    GPIO.output(18, GPIO.HIGH)
    print("Valve On")
def valveOff():
    GPIO.output(18, GPIO.LOW)
    print("Valve Off")
def Cycle():
    while True:
        valveOn()
        sleep(5)  # Some Check of Water...?
        valveOff()
