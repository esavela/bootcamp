#Emily Savela; Created 12 September 2016
#Exercise 2.3 Pathogenicity Islands

def seq_blocks(seq, block_size):
    """Divides sequence into blocks"""
    seq_list = []
    for i in range(0, len(seq), block_size):
        if (block_size + i) <= len(seq):
            seq_list.append(seq[i:i+block_size])

    return seq_list


def gc_blocks(seq, block_size):
    """Finds GC content of blocks of a sequence"""

    #Divide sequence into blocks
    seq_list = seq_blocks(seq, block_size)

    #Calculate the frequency of gc in each block
    gc_list = []
    for j in range(0, len(seq_list)):
        gc_list.append(seq_list[j].count('C')+seq_list[j].count('G'))

    #Calculate gc content of each block
    gc_content = []
    for k in range(0, len(gc_list)):
        gc_content.append(gc_list[k] / block_size)

    return gc_content


def gc_map(seq, block_size, gc_thresh):
    """Sequences above gc_thresh capitalized; below gc_thresh lowercase"""

    #Call functions to divide into blocks; calc gc content of blocks
    seq_list = seq_blocks(seq, block_size)
    gc_content = gc_blocks(seq, block_size)

    #check value of gc_thresh
    if gc_thresh > 1:
        print('Invalid GC threshold. Please enter value <= 1')

    seq_thresh = []
    for i in range(0, len(gc_content)):
        if gc_content[i] > gc_thresh:
            seq_thresh.append(seq_list[i].upper())
        elif gc_content[i] <= gc_thresh:
            seq_thresh.append(seq_list[i].lower())

    seq_map = ''.join(seq_thresh)

    return seq_map
