#!/usr/bin/env python
# Test Selector
# By Multipixelone

print "Welcome to RaspberryPiHydroponics"
print "For help, type help"

while True:
    query = raw_input("> ")
    if query == "help":
        print "HELP IS HERE"
        query = ""
    if query == "exit":
        break
    else:
        print "Unrecognized statement"
        query = ""
