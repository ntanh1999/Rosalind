from Bio import SeqIO
import numpy as np
import sys

f = sys.argv[1]

di = {'A':0, 'C':1, 'G':2, 'T':3}
ls = ['A', 'C', 'G', 'T']

reader = SeqIO.parse(open(f, 'r'), 'fasta')
for seq_record in reader:
    try:
        matrix
    except:
        seq_len = len(seq_record.seq)
        matrix = np.zeros((seq_len, 4))
    
    for row, c in enumerate(seq_record.seq):
        col = di[c]
        matrix[row, col] +=1

# print(matrix)

cons = []

for row in matrix:
    max_pos = 0
    max_val = 0
    for i, cell in enumerate(row):
        if cell > max_val:
            max_val = cell
            max_pos = i
    
    cons.append(ls[max_pos])

print(''.join(cons))

for i, row in enumerate(matrix.T):
    row_ls = []
    for cell in row:
        row_ls.append(str(int(cell)))
    print(ls[i] + ': ' + ' '.join(row_ls))


