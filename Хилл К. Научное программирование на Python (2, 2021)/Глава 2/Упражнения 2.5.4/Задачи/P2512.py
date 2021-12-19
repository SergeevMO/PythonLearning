# Конфигурация электронов в атоме
# а)
element_symbols = ['', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na',
                   'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn',
                   'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr',
                   'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
                   'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
                   'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
                   'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
                   'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
                   'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
orbital_quantum_number = [(0, 's'), (1, 'p'), (2, 'd'), (3, 'f'), (4, 'g'), (5, 'h'), (6, 'x')]
list_c = []
# Составим упорядоченный список энергетических уровней по возрастанию их энергии
for n in range(1, 9):
    for la in range(0, n):
        list_c.append((n + la, n, la))
list_c.sort()

for N in range(1, 119):
    print(element_symbols[N], ': ', sep='', end='')
    i = 0
    while N != 0:
        s, n, la = list_c[i]
        e_max = 2 * (2 * la + 1)
        if N > e_max:
            e_n = e_max
        else:
            e_n = N
        N -= e_n
        print(f'{n}{orbital_quantum_number[la][1]}{e_n}', end='')
        i += 1
        if N > 0:
            print(end='.')
    print()


# второй вариант
# All element symbols up to Rf
element_symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na',
                   'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn',
                   'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr',
                   'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
                   'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
                   'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
                   'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
                   'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf']
# Letters identifying subshells
l_letter = ['s', 'p', 'd', 'f', 'g']

def get_config_str(config):
    """ Turn a list of orbital, nelec pairs into a configuration string. """
    return '.'.join(['{:2s}{:d}'.format(*e) for e in config])

# Create and order a list of tuples, (n+l, n, l), corresponding to the order
# in which the corresponding orbitals are filled using the Madelung rule.
nl_pairs = []
for n in range(1,8):
    for l in range(n):
        nl_pairs.append((n+l, n, l))
nl_pairs.sort()

# inl indexes the subshell in the nl_pairs list; nelec is the number of
# electrons currently inhabiting this subshell
inl, nelec = 0, 0
# start with the 1s orbital
n, l = 1, 0
# a list of orbitals and the electrons they contain for a configuration
config = [['1s', 0]]
for element in element_symbols:
    nelec += 1
    if nelec > 2*(2*l+1):
        # this subshell is now full: start a new subshell
        inl += 1
        _, n, l = nl_pairs[inl]
        config.append(['{}{}'.format(n, l_letter[l]), 1])
        nelec = 1
    else:
        # add an electron to the current subshell
        config[-1][1] += 1
    # Turn config into a string and output it
    s_config = get_config_str(config)
    print('{:2s}: {}'.format(element, s_config))





print('*'*74)
# б)
element_symbols = ['', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na',
                   'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn',
                   'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr',
                   'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
                   'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
                   'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
                   'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
                   'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
                   'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
orbital_quantum_number = [(0, 's'), (1, 'p'), (2, 'd'), (3, 'f'), (4, 'g'), (5, 'h'), (6, 'x')]

# Составим упорядоченный список энергетических уровней по возрастанию их энергии
list_energy_level = []
for n in range(1, 9):
    for la in range(0, n):
        list_energy_level.append((n + la, n, la))
list_energy_level.sort()

for N in range(1, 119):
    configuration = [] # список энергетических уровней текущего атома
    configuration_noble_gas = [] # список энергетических уровней благородного газа
    close_shell = str() # электронная конфигурация благородного газа
    print(f'{element_symbols[N]:>2s}: ', sep='', end='')
    i = 0
    current_atom = 0 # количество электронов текущего атома
    while N != 0:
        s, n, la = list_energy_level[i]
        e_max = 2 * (2 * la + 1)
        if N > e_max:
            e_n = e_max
        else:
            e_n = N
        N -= e_n # количество оставшихся электронов
        current_atom += e_n

        configuration.append(f'{n}{orbital_quantum_number[la][1]}{e_n}')
        if N > 0 and e_n == 6 and orbital_quantum_number[la][1] == 'p' or current_atom == 2:
            close_shell = f'[{element_symbols[current_atom]}]'
            configuration_noble_gas = configuration.copy()
        i += 1
    conf_str = '.'.join(configuration)
    conf_noble_str = '.'.join(configuration_noble_gas)
    if current_atom == 2:
        conf_current_str = conf_str # электронная конфигурация текущего атома
    else:
        conf_current_str = conf_str.replace(conf_noble_str, f'{close_shell}') # электронная конфигурация текущего атома
    print(conf_current_str)




print('*'*74)
# Второй вариант
# All element symbols up to Rf
element_symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na',
                   'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn',
                   'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr',
                   'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
                   'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
                   'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
                   'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
                   'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf']

# Letters identifying subshells
l_letter = ['s', 'p', 'd', 'f', 'g']

def get_config_str(config):
    """ Turn a list of orbital, nelec pairs into a configuration string. """
    return '.'.join(['{:2s}{:d}'.format(*e) for e in config])

# Create and order a list of tuples, (n+l, n, l), corresponding to the order
# in which the corresponding orbitals are filled using the Madelung rule.
nl_pairs = []
for n in range(1,8):
    for l in range(n):
        nl_pairs.append((n+l, n, l))
nl_pairs.sort()

# inl indexes the subshell in the nl_pairs list; nelec is the number of
# electrons currently inhabiting this subshell
inl, nelec = 0, 0
# start with the 1s orbital
n, l = 1, 0
# a list of orbitals and the electrons they contain for a configuration
config = [['1s', 0]]
# Store the most recent Noble gas configuration encountered in a tuple with the
# corresponding element symbol
noble_gas_config = ('', '')
for i, element in enumerate(element_symbols):
    nelec += 1
    if nelec > 2*(2*l+1):
        # this subshell is now full
        if l == 1:
            # The most recent configuration was for a Noble gas: store it
            noble_gas_config = (get_config_str(config),
                                '[{}]'.format(element_symbols[i-1]))
        # Start a new subshell
        inl += 1
        _, n, l = nl_pairs[inl]
        config.append(['{}{}'.format(n, l_letter[l]), 1])
        nelec = 1
    else:
        # add an electron to the current subshell
        config[-1][1] += 1
    # Turn config into a string
    s_config = get_config_str(config)
    # Replace the heaviest Noble gas configuration with its symbol
    s_config = s_config.replace(*noble_gas_config)
    print('{:2s}: {}'.format(element, s_config))