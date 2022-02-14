from Bio import SeqIO
import sys

f = sys.argv[1]

dictionary = {}
for seq_record in SeqIO.parse(open(f, 'r'), 'fasta'):
    seq_id = seq_record.id
    seq = seq_record.seq

    dictionary[seq_id] = [seq[:3], seq[-3:]]

for tail in dictionary:
    for head in dictionary:
        if tail == head:
            continue
        if dictionary[tail][1] == dictionary[head][0]:
            print(tail + ' ' + head)