# Emily Savela; Created 13 September 2016
# Exercise 3

import numpy as np
import scipy.stats
import bootcamp_utils

# This is how we import the module of Matplotlib
import matplotlib.pyplot as plt

# Import Seaborn and settings
import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
      'axes.titlesize' : 18}
sns.set(rc=rc)


def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Computes theoretical fold change as a function of IPTG concentration;
    c is concentration of IPTG;
    RK is an array or scalar (R/K)
    KdA, KdI, and Kswitch are constants
    """
    numerator = RK * (1+(c/KdA))**2
    denominator = (1+(c/KdA))**2 + Kswitch * (1+(c/KdI))**2
    fold_change = 1/(1+(numerator/denominator))

    return fold_change


# Load data
wt_lac = np.loadtxt('data/wt_lac.csv', comments='#',
                    delimiter=',', skiprows=3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', comments='#',
                      delimiter=',', skiprows=3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', comments='#',
                      delimiter=',', skiprows=3)

# Slice raw data
wt_IPTG = wt_lac[:,0]
wt_fold = wt_lac[:,1]
q18m_IPTG = q18m_lac[:,0]
q18m_fold = q18m_lac[:,1]
q18a_IPTG = q18a_lac[:,0]
q18a_fold = q18a_lac[:,1]

# Compute theoretical concentrations
wt_IPTG_theo = np.logspace(9e-6, 25, 500)
q18m_IPTG_theo = np.logspace(9e-6, 25, 500)
q18a_IPTG_theo = np.logspace(9e-6, 25, 500)

# Compute theoretical fold Change
wt_fold_theo = fold_change(wt_IPTG_theo, 141.5)
q18m_fold_theo = fold_change(q18m_IPTG_theo, 16.56)
q18a_fold_theo = fold_change(q18a_IPTG_theo, 1332)

# Ensure no open plots
plt.close()

# Plot all experimental data
plt.semilogx(wt_IPTG, wt_fold, marker='.', linestyle='none',
         markersize=20, alpha=0.8)
plt.semilogx(q18m_IPTG, q18m_fold, marker='.', linestyle='none',
         markersize=20, alpha=0.8)
plt.semilogx(q18a_IPTG, q18a_fold, marker='.', linestyle='none',
         markersize=20, alpha=0.8)

# Plot theoretical data
plt.semilogx(wt_IPTG_theo, wt_fold_theo, color='magenta')
plt.semilogx(q18m_IPTG_theo, q18m_fold_theo, color='black')
plt.semilogx(q18a_IPTG_theo, q18a_fold_theo, color='yellow')

# Plot parameters
plt.xlabel('Concentration IPTG (mM)')
plt.ylabel('Fold Change')
plt.legend(('wt_lac', 'q18m_lac', 'q18a_lac',
            'theoretical wt_lac', 'theoretical q18m_lac',
            'theoretical q18a_lac'), loc='center right')
plt.show()
