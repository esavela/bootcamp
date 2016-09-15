# Emily Savela; Created 15 September 2016
# Lesson 37, Performing Regressions

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

df = pd.read_csv('data/bcd_gradient.csv', comment='#')
df = df.rename(columns={'fractional distance from anterior' : 'x',
                        '[bcd] (a.u.)' : 'I_bcd'})
plt.close()
plt.plot(df['x'], df['I_bcd'], marker='.', linestyle='none')
plt.show()

def gradient_model(x, I_0, a, lam):
    """Model for Bcd gradient: exponential decay plus background."""
    if np.any(np.array(x) <= 0):
        raise RuntimeError('x must be positive.')
    if np.any(np.array([I_0, a, lam]) < 0):
        raise RuntimeError('all params must be positive')

    return a + I_0 * np.exp(-x / lam)

# popt, _ = scipy.optimize.curve_fit(gradient_model, df['x'], df['I_bcd'], p0=p0)
# x_smooth = np.linspace(0, 1, 200)
# I_smooth = gradient_model(x_smooth, *tuple(popt))
