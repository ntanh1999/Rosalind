
def count_dna(string):
    count_dict = {'A':0, 'T':0, 'G':0, 'C':0}

    for c in string:
        if c in count_dict:
            count_dict[c] += 1
    
    print("{} {} {} {}".format(count_dict['A'], count_dict['C'], count_dict['G'], count_dict['T']) )

# count_dna('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')

count_dna('TCCATCGGATTATACAGCGATCTCCTATTATGGAGAAGACGGATTCCTCTAGGTACCAAGTCGAGCATCAAACTGCAGCACTCTCGTTGTCGAACCGTCTGTCCAAGAGCCCGAACATGGACCAAAGCACTGCTCCTGCGCGATCGGAAGCTGAGCTAGCGCGGCCCGGGCAGCTCGTCACACCAGGGTAGGATAACTGCCTGCATCCCCAACCTGGCCCACCCTGGTGCCCTCAACTTATGCACCTCGTGGGGGTGTATAGCTCTGACAGGACTATCCTGGTTACGGTACGCGAAGTAGAGAGGGGCTCTAAGTTGATTCTTCTTTATACATCATACAGGGAGTCAGGACGGGCCCCTTAGTCCGATAACAATTGTCGTCACTATACATTAATTAGAGTGCTATACCTCGCTACCTTGTTCGTCGGAGCTACGTCCCTATCGTCTATCCTGGGCCCCTTCTGTCATGGCCACTGGCCGCACAGTATTTCTCGAAAACAAGAGTCCGCATGCCTCACCTGGTGGTTCGTATTGATGGGTACCTCCGGAAGTATAAGCTGCTAGGATTGTATCTTCGGACAAAATATTGGCGTATCTGATTACTGTCCTAGTAAACCTTCGGAGCTAGGTCCACAGGAGCGCAGCACGTCCTTCGTGTCGCTGCAACTGAATCGTTCAGGGCTTTGGGGGTACCGGCAATTGTCATTTTACCTTCACTGTGCCGCACTGCACAGTCTACGGAACTGTTCAGATCTCACCAATGCTTCACACACACGCAAGATAGACTGCATTTAATGTAAGACGATAGTATGTGCAACGGTCGCAGCAATACGTTAGAAATTCGCGGCTTGTCCGCATGTGGAAACAATC')