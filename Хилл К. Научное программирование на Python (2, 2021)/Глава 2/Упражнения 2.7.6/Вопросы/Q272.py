balance = 100

def add_interest(b, rate):
   global balance
   balance += b * rate / 100
   print('Balance after year {}: ${:.2f}'.format(year + 1, balance))

for year in range(4):
    add_interest(balance, 5)


# второй вариант
balance = 100

def add_interest(balance, rate):
   balance += balance * rate / 100
   return balance


for year in range(4):
    balance = add_interest(balance, 5)
    print('Balance after year {}: ${:.2f}'.format(year + 1, balance))