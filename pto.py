#!/usr/bin/env python3
#How how long to accrue an amount of pto that is evenly divisible by days, and how many days is it
n = 6.5

while n % 8 != 0:
    n += 6.5
min_weeks = str((n/6.5)*2)
min_days = str(n/8)
min_hours = str(n)
print("It takes " + min_weeks + " weeks to accrue " + min_hours +" hours (" + min_days + " days) of pto, the lowest evenly divisible amount")


#how long to accrue the maximum amount of allowed pto
y = 6.47
max_pto = 252
x = 0
while y < max_pto:
    y += 6.47
    x += 1
max_weeks = str(x*2)
max_days = str(max_pto/8)
max_hours = str(max_pto)
print("It takes " + max_weeks + " weeks to accrue " + max_hours +" hours (" + max_days + " days) of pto, the highest possible amount.")


#long long to reach maximum with expenditure?
days_off = int(input("Want to know how long it'll be till you hit the max?  How many days off do you plan to take in total? "))
hours_off = days_off*8
y = 6.47 - hours_off
max_pto = 252
x = 0
while y < max_pto:
    y += 6.47
    x += 1
max_weeks = str(x*2)
year = str((x*2)/52)
max_days = str(max_pto/8)
max_hours = str(max_pto)
print("It takes " + year + " years (" + max_weeks + " weeks) to accrue " + max_hours +" hours (" + max_days + " days) of pto, the highest possible amount if you plan to take off " + str(days_off) + " days of PTO during that time.")


#how long to reach the maximum amount with a set yearly expenditure?
days_off = int(input("Or how about if you take the same amount of time off each year? How many days off do you plan to take each year? "))
hours_off = days_off*8
y = 6.47 - hours_off
max_pto = 252
x = 0
while y < max_pto:
    y += 6.47
    x += 1
    if x%26 == 0: #6.47 hours every 2 weeks, 52 weeks in a year, 26 pay periods
        y = y - hours_off
max_weeks = str(x*2)
year = str((x*2)/52)
max_days = str(max_pto/8)
max_hours = str(max_pto)
print("It takes " + year + " years (" + max_weeks + " weeks) to accrue " + max_hours +" hours (" + max_days + " days) of pto, the highest possible amount if you plan to take off " + str(days_off) + " days of PTO every year.")



#how much pto can you expend yearly and never run out?
start = int(input("Want to know how many PTO days you can take each year and never run out?  How many days do you already have accrued? "))

#yearlyAccrual - daysOff = startPoint, aka how much you accru each year minus the amount you take off gets you back to start
#daysOff = yearlyAccrual - startPoint
#we know startPoint but the problem is that yearlyAccrual and daysOff are both unknowns
# so we iterate with one number and then change it to a differnet one?
days = 10
hours_off = days*8

while days > 0:
    y = 0 - hours_off + start
    x = 0
    #Iterate through each day counting down from 365, see when we hit less than start, then go one back up and return that value  
    while x <= 26:
        y += 6.47
        x += 1
    print(str(y/8))
    days -= 1
#print("You can take up to " +days+ " of PTO each year and never run out!")
