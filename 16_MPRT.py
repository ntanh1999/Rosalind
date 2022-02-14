import os
import sys
from Bio import SeqIO
import re

f = sys.argv[1]
fasta_ls = []
id_ls = []
for line in open(f):
    line = line.rstrip()
    link = f'http://www.uniprot.org/uniprot/{line}.fasta'
    protein_fasta = os.path.join('data', f'{line}.fasta')
    fasta_ls.append(protein_fasta)
    id_ls.append(line)
    cmd = f'wget {link} -O {protein_fasta}'
    if not os.path.isfile(protein_fasta):
        os.system(cmd)

for fasta, pro_id in zip(fasta_ls,id_ls):
    for seq_record in SeqIO.parse(open(fasta, 'r'), 'fasta'):
        pos_ls = []
        seq = str(seq_record.seq)
        for i in range(0, len(seq)-4):
            substring = seq[i:i+4]
            if re.match(r'N[^P][ST][^P]', substring) != None:
                pos_ls.append(str(i+1))
    if len(pos_ls) != 0:
        print(pro_id)
        print(' '.join(pos_ls))
    


