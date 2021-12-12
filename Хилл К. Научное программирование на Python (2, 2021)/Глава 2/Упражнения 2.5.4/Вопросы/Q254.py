# Неразветвлённые алканы
stoich = 'c1h1M'
ch2 = '-CH2'

stoich = stoich.upper()
iC = stoich.index('C')
if iC == 0:
    iH = stoich.index('H')
    nC = int(stoich[iC + 1:iH]) # также необходимо провести проверку на возможность такого преобразования

    if nC == 0:
        print('нет углерода')
    else:
        rest = stoich[iH+1:]
        if rest.isdigit():
            nH = int(rest)
            if nH == 0:
                print('углерод-', nC, sep='')
            elif nC == 1 and nH == 1:
                print('=CH-')
            elif nC == 1 and nH == 2:
                print('-CH2-')
            elif nC == 1 and nH == 3:
                print('CH3-')
            else:
                if nH == 2*nC + 2:
                    print(f'{stoich} - алкан')
                    if nC == 1:
                        print('CH4')
                    else:
                        metilen = ch2 * (nC - 2)
                        print(f'H3C{metilen}-CH3')
                elif nH == 2*nC:
                    print(f'{stoich} - циклоалкан или алкен')
                elif nH == 2*nC -2:
                    print(f'{stoich} - алкин')
                elif nH == nC:
                    print(f'{stoich} - арен')
                else:
                    print(stoich)
        print(stoich)
else:
    print(stoich)



