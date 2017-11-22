#!/usr/bin/env python
# Made by Multipixelone
# Controller for Lights
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


def LightsOn():
    GPIO.output(17, 1)
    print("Lights On")


def LightsOff():
    GPIO.output(17, 0)
