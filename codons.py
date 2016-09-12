#Emily Savela; 11 September 2016

codon = input('Input your codon, please: ')
codon_list = ['UAA', 'UAG', "UGA"]
codon_tuple = tuple(codon_list)

if codon == 'AUG':
    print('This codon is the start codon.')
elif codon in codon_tuple:
## replaced line codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
    print('This is a stop codon')
else:
    print('This codon is neither a start nor stop codon.')
