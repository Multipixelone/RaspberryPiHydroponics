#!/usr/bin/env python
# Made by Multipixelone
# Pump Controller
import RPi.GPIO as GPIO
from time import sleep  # Import Sleep Control

def valveCycle():
    while True:
        GPIO.output(18, GPIO.HIGH)
        print("Valve On")
        sleep(10)
        GPIO.output(18, GPIO.LOW)
        print("Valve is off")
        sleep(1)
