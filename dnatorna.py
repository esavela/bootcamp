#Emily Savela; Created 12 September 2016

"""
Convert DNA to RNA.
"""

def rna(seq):
    """
    Convert DNA sequene to RNA
    """
    #convert to capital letters
    seq = seq.upper()

    return seq.replace("T", "U")
