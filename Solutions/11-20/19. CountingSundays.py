#Project Euler No19 - Counting Sundays

#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

sunday_count = 0 
day_state = 2
date = 1
mon_state = 1
year = 1901

def month(mon_state,year):
  if mon_state in [9, 4, 6, 11]:
    day_cap = 30
  elif mon_state == 2:
    day_cap = 28
    if is_leap(year):
      day_cap = 29
  else:
    day_cap = 31

  return day_cap


def is_leap(year):
  if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
      return True
  else: 
    return False


loop = True
while loop:

  day_state += 1
  if day_state == 7 and date == 1:
    sunday_count += 1
    day_state = 0
  elif day_state == 7:
    day_state = 0

  date += 1
  if date > month(mon_state, year):
    if mon_state == 12:
      year += 1
      mon_state = 0

    date = 1
    mon_state += 1

  if year == 2001:
    loop = False

print("ANS:",sunday_count)

      
  
    
  
      


    
