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

import datetime

def daterange(date1, date2):
    date_list = []
    for n in range(int((date2-date1).days)+1):
         date_list.append(date1 + datetime.timedelta(n))
    return date_list

start = datetime.date(1901,1,1)
end = datetime.date(2000,12,31)
dates = daterange(start,end)
ans = 0
for dt in dates:
    if dt.day == 1 and dt.weekday() == 6:
        print(dt.strftime('%Y-%m-%d'))
        ans += 1
print(ans)
