#Emily Savela; Created 11 September 2016
#Exercise 1.3a Using String Methods

def complement_base(base, material='DNA'):
    """Return the Watson-Crick complement of a base"""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else:
            raise RuntimeError('Invalid Material')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'


def reverse_complement(seq, material='DNA'):
    """Compute the reverse complement of a nucleic acid sequence"""

    #Initialize an empty string
    rev_comp = ''

    #Loop through sequence and add reverse complement bases
    for base in seq[::-1]:
        rev_comp += complement_base(base, material=material)
    return(rev_comp)
