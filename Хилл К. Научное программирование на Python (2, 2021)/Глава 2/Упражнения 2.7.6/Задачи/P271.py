# Игра Эрудит
word_list = ['тайга', 'никотинамиддинуклеотидфосфат', 'автомобиль']
position_list = ['A7', 'F10', 'D5']
vector = ['H', 'V']
"""
def Scrabble(s, pos):
    l_d = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7),
           ('H', 8), ('I', 9), ('J', 10), ('K', 11), ('L', 12), ('M', 13), ('N', 14), ('O', 15)]
    length_word = len(s)
    letter = pos[0]
    for i in l_d:
        if i[0] == letter:
            dig = i[1]
            break
    rest_position = 225 - 15 * dig + pos[1]
"""

def Scrabble(s, pos, v):
    l_d = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7),
           ('H', 8), ('I', 9), ('J', 10), ('K', 11), ('L', 12), ('M', 13), ('N', 14), ('O', 15)]
    length_word = len(s)

    if v == 'H':
        if length_word > (15 - int(pos[1:])):
            print(f'Слово {s} на позиции {pos} в направлении {v} не умещается.')
        else:
            print(f'Слово {s} на позиции {pos} в направлении {v} умещается.')
    else:
        letter = pos[0]
        for i in l_d:
            if i[0] == letter:
                dig = int(i[1])
                break
        if length_word > (15 - dig):
            print(f'Слово {s} на позиции {pos} в направлении {v} не умещается.')
        else:
            print(f'Слово {s} на позиции {pos} в направлении {v} умещается.')

for w in word_list:
    for p in position_list:
        for v in vector:
            Scrabble(w, p, v)


# Второй пример
def word_fits(word, position, across):
    """ Determine if a given word fits in a scrabble grid.

    Given a word and starting position, determine whether the word fits
    within the standard Scrabble grid. The position is specified as a string
    giving the grid reference as a row letter (A-O) followed by a column
    number (1-15); across is True if the word is to be placed along a row and
    False if it is to be placed down a column from the starting position.

    """

    if across:
        # Get the starting column position (starting at 1)
        i = int(position[1:])
    else:
        # Get the starting row position (starting at 'A'=1)
        i = ord(position[0]) - 64   # NB ord('A') is 65 ... ord('O') is 79

    return len(word) <= 16 - i

def report(word, position, across):
    across_down = 'across' if across else 'down'
    mod = 'not' if not word_fits(word, position, across) else ''
    return '"{}" {} at {} does {} fit'.format(word, across_down, position, mod)


print(report('HELLO', 'I2', across=False))
print(report('HELLO', 'J2', across=False))
print(report('HELLO', 'K2', across=False))
print(report('HELLO', 'L2', across=False))
print(report('HELLO', 'M2', across=False))
print(report('HELLO', 'N2', across=False))
print(report('HELLO', 'O2', across=False))
print(report('LO', 'A12', across=True))
print(report('LO', 'A13', across=True))
print(report('LO', 'A14', across=True))
print(report('LO', 'A15', across=True))