#!/usr/bin/env python
# Made by Multipixelone
# Pump Controller
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)


def PumpOn():
    GPIO.output(22, 1)
    print("Pump On")


def PumpOff():
    GPIO.output(22, 0)
    print("Pump Off")


def Flood():
    PumpOn()
    sleep(4)  # Stopwatch the tray, set the correct time to flood ;)
    PumpOff()
