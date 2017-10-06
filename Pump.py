#!/usr/bin/env python
# Made by Multipixelone
# Pump Controller
import RPi.GIPO  # Import GPIO Control
from time import sleep  # Import Sleep Control

def valve_cycle():
    while True:
        GPIO.output(18, GPIO.HIGH)
        print("Valve On")
        time.sleep(10)
        GPIO.output(18, GPIO.LOW)
        print("Valve is off")
        time.sleep(1)
