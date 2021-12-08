# а)
tuple_list = [(3, 1), (1, 4), (3, 0), (2, 2), (1, -1)]

print(sorted(tuple_list))


# б)
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sunshine_hours = [44.7, 65.4, 101.7, 148.3, 170.9, 171.4, 176.7, 186.1, 133.9, 105.4, 59.6, 45.8] # hrs

z = sorted(zip(sunshine_hours, month), reverse=True)
SH, M = zip(*z)
print(M, '\n', SH, sep='')