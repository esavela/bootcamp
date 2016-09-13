#Emily Savela; Created 11 September 2016; Modified 11 September 2016
#Exercise 1.4 Longest Common Substring

def common_substr(seq1, seq2):
    """Compares two sequences and returns the longest common,
    contiguous substring"""

    #Identify shorter sequence
    if len(seq1) <= len(seq2):
        short_s = seq1
        short_s_2 = seq1
        long_s = seq2
    else:
        short_s = seq2
        short_s_2 = seq2
        long_s = seq1

    #Compare the substring, look for short string in longer string
    for i, _ in enumerate(short_s):
        while short_s not in long_s:
            #if it's not in the longest string, trim the short string (end)
            short_s = short_s[:-1]
        else:
            common_str = short_s

    for i, _ in enumerate(short_s_2):
        while short_s_2 not in long_s:
            #if it's not in the longest string, trim the short string (front)
            short_s_2 = short_s_2[1:]
        else:
            common_str_2 = short_s_2

    #Look at the two common strings found, output the longest

    if common_str > common_str_2:
        return "The longest common string is: " + common_str
    elif common_str_2 > common_str:
        return "The longest common string is: " + common_str_2
