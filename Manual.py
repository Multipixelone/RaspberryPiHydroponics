#!/usr/bin/env python
# Made by Multipixelone
# Manual Control, for when you need control
# Pretty badly coded, but I wanted a way to do it manualy
import Pump
from Lights import LightsOff, LightsOn
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

print "Welcome to RaspberryPiHydroponics by Multipixelone"
print "For help, type help"

while True:
    query = raw_input("> ")
    if query == "help":
        print "Type pumpon to turn pump on"
        print "Type pumpoff to turn pump off"
        print "Type lightson to turn lights on"
        print "Type lightsoff to turn lights off"
        print "Type flood to flood the grow tray"
        query = ""
    if query == "exit" or query == "quit":
        GPIO.cleanup()
        break
        query == ""
    if query == "flood":
        print "Flooding grow tray..."
        Pump.Flood()
        query == ""
    if query == "lightson":
        print "Turning Lights On..."
        LightsOn
        query = ""
    if query == "lightsoff":
        print "Turning Lights Off..."
        LightsOff
        query = ""
    if query == "pumpon":
        print "Turning Pump On..."
        Pump.PumpOn
        query = ""
    if query == "pumpoff":
        print "Turning Pump Off..."
        Pump.PumpOff
        query = ""
