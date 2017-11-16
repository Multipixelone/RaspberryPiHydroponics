#!/usr/bin/env python
# Made by Multipixelone
# Automatic Ebb and Flow Hydroponics control
from time import sleep
import RPi.GPIO as GPIO
import Pump
import Lights
import schedule
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
print("Welcome to RaspberryPiHydroponics By Multipixelone.")
print("Starting schedule...")

# Schedule
schedule.every().day.at("10:30").do(Pump.Flood)
schedule.every().day.at("13:00").do(Pump.Flood)
schedule.every().day.at("7:00").do(Lights.LightsOn)
schedule.every().day.at("13:30").do(Lights.LightsOff)

while True:
    schedule.run_pending()
    sleep(1)
