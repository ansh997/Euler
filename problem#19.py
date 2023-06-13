"""
1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.
"""
# # Counting Sundays on First Month of Twentieth Century

# Weekcode = 1 # Weekcode of 1st Jan 1900 is i.e. Monday

# months = [31,28,31,30,31,30,31,31,30,31,30,31]
# # no. of days in each month ordered as they occurence in a year.

# sunday_count = 0
# # This is the sundays counter

# for cur_year in range(1900,2000+1) :
#     # for loop from 1900 to 2000

#     # updating day count of Feb month according to the year
#     if (cur_year%4==0 and cur_year%100!=0) or (cur_year%400==0):
#         months[1] = 29
#     else:
#         months[1] = 28

#     for y in months:
#         Weekcode = (Weekcode + y)%7

#         if Weekcode==0 and cur_year>1900:
#             sunday_count+=1

# print(sunday_count)

from datetime import datetime

sunday_count = 0
for j in range(1901, 2001):  #  year
  for k in range(1, 13):  # Month
    y = datetime(j, k, 1)  # Date
    if y.strftime("%a") == 'Sun':  # Check for Sunday
      sunday_count += 1
print(sunday_count)
