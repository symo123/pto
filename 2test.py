#!/usr/bin/env python3

#how much pto can you take and never run out?

testDays = 365

while testDays > 0:
  start = 31.5
  while start > 0:
    hoursOff = (start*8) + (6.47*26) - (testDays*8)
    hoursStart = start*8
    if hoursOff >= hoursStart:
      print(str(testDays)+" days off if you start with "+str(start)+" days accrued")
    start -= 1
  if hoursOff >= hoursStart:
    break
  testDays -= 1
