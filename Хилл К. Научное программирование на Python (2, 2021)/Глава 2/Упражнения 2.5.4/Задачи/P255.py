today = '31/01/1960'
us_date_style = False

year = int(today[-4:])

if not year % 400:
    is_leap_year = True
elif not year % 100:
    is_leap_year = False
elif not year % 4:
    is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    day_in_months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    day_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if us_date_style:
    m = int(today[:2])
    d = int(today.split('/')[1])
else:
    m = int(today.split('/')[1])
    d = int(today[:2])

d += 1

if d > day_in_months[m]:
    d = 1
    m += 1
    if m > 12:
        m = 1
        year += 1

if us_date_style:
    print(f'Завтра: {m:02d}/{d:02d}/{year:4d}')
else:
    print(f'Завтра: {d:02d}/{m:02d}/{year:4d}')

if not year % 400:
    is_leap_year = True
elif not year % 100:
    is_leap_year = False
elif not year % 4:
    is_leap_year = True
else:
    is_leap_year = False

s_ly = '' if is_leap_year else 'не '
print('{:4d} {:s}високосный год'.format(year, s_ly))





print('\n')
# Второй вариант
# Set us_date_style to True for dates written M/D/Y, otherwise assume D/M/Y
us_date_style = False
# Number of days per month indexed from zero (Jan=0, Feb=1, ..., Dec=11)
days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# Consider the given date as "today"
today = '4/3/2013'

# Get day, month and year from the today string as integers
day, month, year = today.split('/')
if us_date_style:
    day, month = month, day
day, month, year = int(day), int(month), int(year)

# establish if today's year is a leap year
if not year % 400:
    is_leap_year = True
elif not year % 100:
    is_leap_year = False
elif not year % 4:
    is_leap_year = True
else:
    is_leap_year = False

# Form tomorrow's date by adding one to today's day...
tday, tmonth, tyear = day + 1, month, year
# ... but check if we've fallen off the end of the month
if tday > days_per_month[month-1]:
    if month == 2 and is_leap_year and tday == 29:
        # corner case of today being 28th of February of a leap year
        pass
    else:
        tday, tmonth = 1, month + 1
# Have we fallen off the end of the year?
if tmonth == 13:
    # Yup: it must be 1 January of the next year
    tday, tmonth, tyear = 1, 1, year+1

date_tuple = (tmonth, tday, tyear) if us_date_style else (tday, tmonth, tyear)
tomorrow = '{:d}/{:d}/{:d}'.format(*date_tuple)
print('The day after {:s} is {:s}'.format(today, tomorrow))