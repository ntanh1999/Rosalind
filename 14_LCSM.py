from Bio import SeqIO
import sys

f = sys.argv[1]
seq_list = []
min_length = 10000
min_seq = None
for seq_record in SeqIO.parse(open(f, 'r'), 'fasta'):
    seq = str(seq_record.seq)
    seq_length = len(seq)
    if seq_length < min_length:
        min_length = seq_length
        min_seq = seq
    seq_list.append(seq)

num_of_seq = len(seq_list)

for k in reversed(range(1,min_length)):
    k_mer_dict = {}
    found = False
    for seq_id, seq in enumerate(seq_list):
        for i in range(0,len(seq)-k):
            k_mer = seq[i:i+k]
            if k_mer in k_mer_dict:
                k_mer_dict[k_mer].add(seq_id)
            else:
                k_mer_dict[k_mer] = set()
                k_mer_dict[k_mer].add(seq_id)

    for k_mer in k_mer_dict:
        if len(k_mer_dict[k_mer]) == num_of_seq:
            print(k_mer)
            found = True
            break
    if found == True:
        break




