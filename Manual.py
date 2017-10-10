#!/usr/bin/env python
# Made by Multipixelone
# Manual Control
print "Welcome to RaspberryPiHydroponics"
print "For help, type help"

while True:
    query = raw_input("> ")
    if query == "help":
        print "HELP IS HERE"
        query = ""
    if query == "exit" or query == "quit":
        break
        query == ""
    else:
        print "Unrecognized statement"
        query = ""
