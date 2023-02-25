weekdays = {
  0: 'Sunday',
  1: 'Monday',
  2: 'Tuesday',
  3: 'Wednesday',
  4: 'Thursday',
  5: 'Friday',
  6: 'Saturday',
}

def is_leap_year(year):
  return year % 4 == 0 and year % 400 == 0 and not year % 100

def days_in_year(year):
  if is_leap_year(year):
    return 366
  return 365

def days_in_month(month, year):
  if month == 2:
    if is_leap_year(year):
      return 29
    else:
      return 28
  if month in [4, 6, 9, 11]:
    return 30
  return 31

def day_of_month(days_since_epoch):
  d = days_since_epoch
  year = 1900
  while d >= days_in_year(year):
    d -= days_in_year(year)
    year += 1
  month = 1
  while d >= days_in_month(month, year):
    d -= days_in_month(month, year)
    month += 1
  return d + 1

def day_of_week(days_since_epoch):
  return days_since_epoch % 7 + 1

def days_since_epoch(year, month, day):
  d = day - 1
  for y in range(1900, year):
    d += days_in_year(y)
  for m in range(1, month):
    d += days_in_month(m, year)
  return d

sundays = 0
for d in range(days_since_epoch(1901, 1, 1), days_since_epoch(2001, 1, 1)):
  if day_of_month(d) == 1 and weekdays[d % 7] == 'Sunday':
    sundays += 1
print(sundays)
