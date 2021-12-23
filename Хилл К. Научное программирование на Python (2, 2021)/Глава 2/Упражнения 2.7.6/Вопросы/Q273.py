# Число харшад (число Нивена) – это целое число, которое делится нацело на сумму своих цифр

def digit_sum(n):
    """ Вычисление суммы цифр целого числа n. """
    s_digits = str(n)
    dsum = 0
    for s_digit in s_digits:
        dsum += int(s_digit)
    return dsum

def is_harshad(n):
    return  not n % digit_sum(n)

print(is_harshad(21))