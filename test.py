#!/usr/bin/env python3

#how much pto can you expend yearly and never run out?
start = int(input("Want to know how many PTO days you can take each year and never run out?  How many days do you already have accrued? "))
#start = 31.5

#yearlyAccrual - daysOff = startPoint, aka how much you accru each year minus the amount you take off gets you back to start
#daysOff = yearlyAccrual - startPoint
#we know startPoint but the problem is that yearlyAccrual and daysOff are both unknowns
# so we iterate with one number and then change it to a differnet one?

daysOff = 20 
z = 0

while daysOff > z:
    y = start
    while y > 0:
        hoursAcc = (y*8) - (daysOff*8)
        x = 0
        while x <= 26:
            hoursAcc += 6.47
            x += 1
        daysAcc = hoursAcc/8
        if daysAcc >= y:
            print("If you start with "+str(y)+" days accrued you can take "+str(daysOff)+" days of pto without running out.")
            break
#        print(str(daysAcc))
        y -= 1
    z += 1
#print("You can take up to " +days+ " of PTO each year and never run out!")


