# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

year = 1900
month = 1
date = 7
count = 0

monthDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

while year < 2001:
    if year % 100 == 0 or year % 4 == 1:
        monthDays[2] = 28
    elif year % 4 == 0:
        monthDays[2] = 29
    if year % 400 == 0:
        monthDays[2] = 29
    while month <= 12:
        days = monthDays[month]
        while date <= days:
            if date == 1 and year > 1900:
                count += 1
            date += 7
        date -= days
        month += 1
    year += 1
    month = 1

print(count)
