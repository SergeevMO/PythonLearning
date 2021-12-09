seq = 'AGTCTTATATCT'
codon1_list = []
codon2_list = []
codon3_list = []

l_seq = len(seq)

for i in range(3):
    max_seq_frame = (l_seq - i) - (l_seq - i) % 3
    for j in range(i, max_seq_frame, 3):
        codon = seq[j:j+3]
        if i == 0:
            codon1_list.append(codon)
        elif i == 1:
            codon2_list.append(codon)
        else:
            codon3_list.append(codon)

print(codon1_list)
print(codon2_list)
print(codon3_list)



print('\n')


# Вариант № 2
seq = 'AGTCTTATATCT'
frame = 0       # or 1 or 2

seq_length = len(seq[frame:])
end = seq_length - seq_length % 3

codons = []
for i in range(frame, end, 3):
    codons.append(seq[i:i+3])
print(codons)