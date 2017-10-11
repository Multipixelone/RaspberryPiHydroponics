#!/usr/bin/env python
# Made by Multipixelone
# Pump Controller
import RPi.GPIO as GPIO
# import schedule
# from time import sleep

def Flood():
    GPIO.output(18, GPIO.HIGH)
    #  Check for water level?
    GPIO.output(18, GPIO.LOW)
