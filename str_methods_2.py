#Emily Savela; Created 11 September 2016; Last Modified 12 September 2016
#Exercise 1.3b Using String Methods
#Same output, no loops

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


def reverse_complement_2(seq, material='DNA'):
    """Compute the reverse complement of a nucleic acid sequence"""

    #Create a new string, which is a reverse of the "seq"
    #rev_seq = ''
    rev_seq = seq[::-1]
    #check output against input sequence
    print(rev_seq)

    #Replace each base with a lowercase letter, than a captical letter
    #Make sure to check material of DNA or RNA
    if material =='DNA':
        rev_seq = rev_seq.replace("A", "t")
    elif material == 'RNA':
        rev_seq = rev_seq.replace("A", "u")

    rev_seq = rev_seq.replace("T", "a")
    rev_seq = rev_seq.replace("G", "c")
    rev_seq = rev_seq.replace("C", "g")

    #Capitalize each character
    rev_seq = rev_seq.replace("c","C")
    rev_seq = rev_seq.replace("g","G")
    rev_seq = rev_seq.replace("a", "A")
    rev_seq = rev_seq.replace("t", "T")
    rev_seq = rev_seq.replace("u", "U")

    print(rev_seq)
