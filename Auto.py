#!/usr/bin/env python
# Made by Multipixelone
# Automatic Plant Control, With Defaults set from the Install script!
import Pump
import Lights
import schedule

# Schedule
schedule.every().day.at("10:30").do(Pump.Flood)
schedule.every().day.at("7:00").do(Lights.LightsOn)
schedule.every().day.at("13:00").do(Lights.LightsOff)
