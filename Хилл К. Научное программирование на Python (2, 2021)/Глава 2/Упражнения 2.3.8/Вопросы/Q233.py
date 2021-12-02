days = 'Sun Mon Tues Weds Thurs Fri Sat'

# а)
print(days[days.index('M'):])

# б)
print(days[days.index('M'):days.index('Sa')].rstrip())

# в)
print(days[6:3:-1].lower()*3)

# г)
print(days.replace('rs', '').replace('s ', ' ')[::4])

# д)
print(' -*- '.join(days.split()))
