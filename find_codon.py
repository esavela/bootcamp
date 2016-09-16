# Emily Savela; Created 15 September 2016
# Lesson 36, Practice Test-Driven Development (problem 1)

# seq = """ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAACGAGAACAACAATGCAGCCCAGAAGA
# AGCTGCAGCAGACCCAAGCCAAGGTGGACGAGGTGGTCGGGATTATGCGTGTGAACGTGGAGAAGGTCCT
# GGAGCGGGACCAGAAGCTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAGCATCCCAGTTC
# GAGCAGCAGGCCGGCAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGATCATTCTGGGCG
# TGATAGCCGTTGTGCTGCTCATCATCGTTCTGGTGTCGCTTTTCAATTG"""
# codon = "ATG"

import bioinfo_dicts

def find_codon(codon, seq):
    """Find a specified codon with a given sequence."""

    i = 0
    start_codon = 'ATG'
    # Scan sequence until we hit the start codon,
    # Then determine if the codon is in range of a start codon
    while seq[i:i+3] != start_codon and i < len(seq):
        if codon == start_codon:
            i += 1
        elif codon in bioinfo_dicts.codon_list:
            while seq[i:i+3] 


    if i == len(seq):
        return -1
    else:
        return i

    return i
