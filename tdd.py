# Emily Savela; Created 15 September 2016
# Lesson 35, Testing and Test-Driven Development

import pytest
import bioinfo_dicts

def n_neg(seq):
    """Number of negative residues in a protein sequence"""
    # Convert to capital letters
    seq = seq.upper()

    # check for validity of sequence
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + 'is not a valid amino acid.')

    # Count E's and D's and retrn count
    return seq.count('D') + seq.count('E')
