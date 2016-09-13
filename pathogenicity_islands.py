#Emily Savela; Created 12 September 2016
#Exercise 2.3 Pathogenicity Islands

def gc_blocks(seq, block_size):
    """Divides sequence into blocks; finds GC content of each block"""

    #Divide sequence into blocks
    seq_list = []
    for i in range(0, len(seq), block_size):
        if (block_size + i) <= len(seq):
            seq_list.append(seq[i:i+block_size])

    #Calculate the frequency of gc in each block
    gc_list = []
    for j in range(0, len(seq_list)):
        gc_list.append(seq_list[j].count('C')+seq_list[j].count('G'))

    #Calculate gc content of each block
    gc_content = []
    for k in range(0, len(gc_list)):
        gc_content.append(gc_list[k] / block_size)

    return gc_content
