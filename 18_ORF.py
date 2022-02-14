from Bio import SeqIO
import sys

def revc(string):
    dictionary = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    result = []
    for c in reversed(string):
        result.append(dictionary[c])

    return ''.join(result)

def find_pro(string):
    codontable = {'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
            'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
            'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
            'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
            'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
            'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
            'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
            'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
            'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
            }
    result = set()
    prot = []
    start = False
    for n in range(0, len(string), 3):
        codon = string[n:n + 3]
        if codon == 'ATG':
            start = True

        if start == True and codon in ['TAA', 'TGA', 'TAG']:
            result.add(''.join(prot))
            prot = []
            start = False
        if start == True:
            if codon in codontable:
                prot.append(codontable[codon])

    inside_protein = set()
    for protein in result:
        for i,aa in enumerate(protein):
            if aa == 'M':
                inside_protein.add(protein[i:])
    

    result = set.union(result, inside_protein)

    return result


f = sys.argv[1]
for seq_record in SeqIO.parse(open(f, 'r'), 'fasta'):
    seq = str(seq_record.seq)

revc_seq = revc(seq)

final_result = set()

for string in [seq, revc_seq]:
    for i in range(0,3):
        orf = string[i:]
        result = find_pro(orf)
        final_result = set.union(final_result, result)

for i in final_result:
    print(i)