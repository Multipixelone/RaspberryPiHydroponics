#!/usr/bin/env python
# Made by Multipixelone
# Automatic Plant Control, With Defaults set from the Install script!
from PumpControl import Cycle
import schedule

# Schedule
schedule.every().day.at("10:30").do(Cycle)
