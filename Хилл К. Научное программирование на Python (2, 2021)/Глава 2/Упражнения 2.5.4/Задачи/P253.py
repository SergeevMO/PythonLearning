# алгоритм Луна
card = '4799 2739 8713 6272'

card = card.replace(' ', '')[::-1]
n_max = len(card)
num_list = []

for i in range(n_max):
    if i % 2 == 1:
        t_num2 = 2 * int(card[i])
        if t_num2 > 9:
            t_num2 -= 9
        num_list.append(t_num2)
    else:
        num_list.append(int(card[i]))

sum_card =sum(num_list)

if not sum_card % 10:
    print('Номер карты действителен.')
else:
    print('Номер карты не действителен.')



print('\n')

# второй вариант
ccno = '4556737586899855'
ccl = []
for n in ccno:
    if n == ' ':
        continue
    ccl.append(int(n))

for i in range(0,16,2):
    ccl[i] *= 2
    if ccl[i] > 9:
        ccl[i] = 1 + (ccl[i] - 10)
checksum = sum(ccl) % 10
if checksum:
    print(ccno, 'is not a valid credit card number')
else:
    print(ccno, 'is a valid credit card number')