#!/usr/bin/env python
# Made by Multipixelone
# Pump Controller
import RPi.GPIO as GPIO
# import schedule
# from time import sleep

<<<<<<< HEAD
def Flood():
    GPIO.output(18, GPIO.HIGH)
    #  Check for water level?
    GPIO.output(18, GPIO.LOW)
=======
def PumpOn():
    GPIO.output(18, GPIO.HIGH)
    print("Pump On")
def PumpOff():
    GPIO.output(18, GPIO.LOW)
    print("Pump Off")
def Flood():
    PumpOn()
    sleep(5)  # Some Check of Water...?
    PumpOff()
>>>>>>> f36d201ab6923077c4aa78c71011e31ee384403c
