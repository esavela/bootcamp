#Emily Savela; 11 September 2016

def ratio(x,y):
    """the ratio of 'x' to 'y'.""" #doc string of the function
    return x / y


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
    for base in reversed(seq):
        rev_comp += complement_base(base, material=material)

    return(rev_comp)


def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    """Simpler program that Deep Thought's, I bet."""
    return 42


def think_too_much():
    """Express Ceasar's skepticism about Cassius."""
    print("""Yond Cassius has a lean and hungry look,
    He thinks too much; such men are dangerous.""")
