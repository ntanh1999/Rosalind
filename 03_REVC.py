def revc(string):
    dictionary = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    result = []
    for c in reversed(string):
        result.append(dictionary[c])

    print(''.join(result))


# revc('AAAACCCGGT')

revc('CCCCGGGAGACTGAGCGAAACAGACGTGGCCAACCGCGCTGGACTCATCTCGCCTCTGGGTAATTCCCAAAGGAGACCCCGTTCTCTACTTTACCGATGTATGAGTCTACCTTCAACTGCTACCTAACCCTCAACTAGAGGGTTTCCTAAAGCATTCAGTCCCGAGACCACAGGGCCGTCCGCTAGCGCTTCTATCACATACACACTGAACGTGGCGTTGGGCTACCGCGCCGAGACATTCTACCCCTGGGTGCTCGACGCTCACCATGGTTCTTTAGTGGGACAGAGTGATTTCGAGGCACCAAGAAGACAGCCTTCCGGGGAGAGTGAGCTTGCTATCCGCCACGTTTTGGGAGGGGGCTCTTTATTCATATACATCCCGGACAGAAATAAAGCAGATGACTACGGGGTGATGGTGGAAGGTTCACAGGGTGGATTGCCACTTGACAAGCACGCTAATGGTTACAAGGACCCACCGCATTGGCTGAGAACTGCGGCGACTCGGCAAAGAATACGAGCTGAAATTCTACACAACGCCTCTTTTGATGACGCTAACTTAAGAATAAATTCATAGAGCAAATAGTAGGATTACACGTTTCTTCCAGGTTTTCCTAGTACTTCCTCGGGGTCGACTATCCGTCCTAATGGTTGTGTAACTGATTAATCAACACATGTCGCTGGCCAGTAGGGTTCATTATAACACCACGTCAGATAGTTCGCTCTGAGCTACGACTCTATCGTGCATACATGGTCGTACATCGCGTTCGAAAACCTTACCTATAGCGAAGCCGAATTTGCACCACTCATACATCATCAGTGATGCGGAGTAAAGCAGTCTTCCTTCAGCTACGGCAAAT')