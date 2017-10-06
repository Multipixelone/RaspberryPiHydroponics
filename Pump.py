#!/usr/bin/env python
# Made by Multipixelone
# Pump Controller
import RPi.GIPO
def valve_OnOff(Pin):
    while True:
        GPIO.output(18, GPIO.HIGH)
        print("GPIO HIGH (on), valve should be off")
        time.sleep(10)  # Waiting time in seconds
        GPIO.output(18, GPIO.LOW)
        print("GPIO LOW (off), valve should be on"
        time.sleep(10)
