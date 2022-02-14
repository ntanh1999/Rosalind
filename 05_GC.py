from Bio import SeqIO
import sys

f = sys.argv[1]

max_id = None
max_gc = 0

for seq_record in SeqIO.parse(open(f, 'r'), 'fasta'):
    gc = 0
    seq = seq_record.seq
    total = len(seq)
    for c in seq:
        if c == 'G' or c == 'C':
            gc += 1

    gc_content = gc / total 
    if gc_content > max_gc:
        max_id = seq_record.id
        max_gc = gc_content
    
print(max_id)
print(max_gc*100)
