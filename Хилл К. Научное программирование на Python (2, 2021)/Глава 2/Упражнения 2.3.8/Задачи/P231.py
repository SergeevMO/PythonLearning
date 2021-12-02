s = 'ACCAGTTTACGATGCAAATCCAATAGGGTTGCGCTGCTGCCGAT'
len_s = len(s)

# а)
A = s.count('A')
T = s.count('T')
G = s.count('G')
C = s.count('C')

print(f'Доля A: {A / len_s:.2%}\n'
      f'Доля T: {T / len_s:.2%}\n'
      f'Доля G: {G / len_s:.2%}\n'
      f'Доля C: {C / len_s:.2%}')

print(f'{(A + T) / len_s:0.2%}')
print(f'{(C + G) / len_s:0.2%}')


# б)
s1 = 'TGGATCCA'

s2 = s1[::-1]
s1_2 = s1.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()
print(f'Является ли последовательность {s1} палиндромом? : {s1_2 == s2}')

s1 = s

s2 = s1[::-1]
s1_2 = s1.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()
print(f'Является ли последовательность {s1} палиндромом? : {s1_2 == s2}')