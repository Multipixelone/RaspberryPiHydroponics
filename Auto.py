#!/usr/bin/env python
# Made by Multipixelone
# Automatic Ebb and Flow Hydroponics control
from time import sleep
import Pump
import Lights
import schedule
print("Welcome to RaspberryPiHydroponics By Multipixelone.")
print("Starting schedule...")

# Schedule
schedule.every().day.at("10:30").do(Pump.Flood)
schedule.every().day.at("7:00").do(Lights.LightsOn)
schedule.every().day.at("13:00").do(Lights.LightsOff)

while True:
    schedule.run_pending()
    sleep(1)
