"""
Bootcamp utils: A collection of statistical functions
Proved useful to 55 students
"""

import numpy as np

def ecdf(data):
    """
    Compute x, y values for an emperical distribution function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y


def draw_bs_reps(data, func, size=1):
    """
    Generate an array of bootstrap replicates;
    data: array of data
    func: numpy function to asses (np.mean, np.std, np.median, etc)
    size: the number of replicates
    """
    n = len(data)
    n_reps = size
    bs_replicates = np.empty(size)

    for i in range(n_reps):
        bs_sample = np.random.choice(data, replace=True, size=n)
        bs_replicates[i] = func(bs_sample)

    return bs_replicates
