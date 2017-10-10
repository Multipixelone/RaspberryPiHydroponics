#!/usr/bin/env python
# Made by Multipixelone
# Manual Control
from Pump import Cycle
print "Welcome to RaspberryPiHydroponics by Multipixelone"
print "For help, type help"

while True:
    query = raw_input("> ")
    if query == "help":
        print "HELP IS HERE"
        query = ""
    if query == "exit" or query == "quit":
        break
        query == ""
    if query == "auto":
        Cycle()
        query == ""
    else:
        print "Unrecognized statement"
        query = ""
