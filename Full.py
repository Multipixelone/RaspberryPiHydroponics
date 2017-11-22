#!/usr/bin/env python
# Made by Multipixelone
# Automatic Ebb and Flow Hydroponics control
from time import sleep
import RPi.GPIO as GPIO
import schedule
import atexit
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(17, 0)
GPIO.output(22, 0)
print("Welcome to RaspberryPiHydroponics By Multipixelone.")
print("Starting schedule...")


def OnExit():
    GPIO.cleanup()


def LightsOn():
    GPIO.output(17, 1)
    print("Lights On")


def LightsOff():
    GPIO.output(17, 0)


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


atexit.register(OnExit)  # Added GPIO Cleanup to Script Exit
# Schedule
schedule.every().day.at("10:30").do(Flood)
schedule.every().day.at("7:00").do(LightsOn)
schedule.every().day.at("13:30").do(LightsOff)

while True:
    schedule.run_pending()
    sleep(1)
