# Emily Savela; Created 13 September 2016
# Exercise 3.3 Data Collapse (a-f)

import numpy as np
import scipy.stats
import bootcamp_utils

# This is how we import the module of Matplotlib
import matplotlib.pyplot as plt

# Import Seaborn and settings
import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
      'axes.titlesize' : 28}
sns.set(rc=rc)


def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Computes theoretical fold change as a function of IPTG concentration;
    c is concentration of IPTG;
    RK is an array or scalar (R/K)
    KdA, KdI, and Kswitch are constants
    """
    numerator = RK * (1 + (c/KdA))**2
    denominator = (1 + (c/KdA))**2 + Kswitch * (1 + (c/KdI))**2
    fold_change = 1/(1 + (numerator/denominator))

    return fold_change


def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Computes the Bohr parameter to simplify fold change calculation
    """
    num = (1 + c/KdA)**2
    den = (1 + c/KdA)**2 + Kswitch * (1 + c/KdI)**2
    bohr_par = -np.log(RK) - np.log(num/den)

    return bohr_par


def fold_change_bohr(bohr_parameter):
    """
    Computes the fold change with given bohr parameter
    """
    fc = 1 / (1 + np.exp(-bohr_parameter))

    return fc

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

# Convert raw ITPG concentration to Bohr parameter
wt_IPTG_bohr = bohr_parameter(wt_IPTG, 141.5)
q18m_IPTG_bohr = bohr_parameter(q18m_IPTG, 1332)
q18a_IPTG_bohr = bohr_parameter(q18a_IPTG, 16.56)

# Compute theoretical values
IPTG_theo = np.logspace(9e-6, 25, 500)
bohr_theo = np.linspace(-6, 6, 500)
fold_theo = fold_change_bohr(bohr_theo)

# Ensure no open plots
plt.close()

# Plot all experimental and theoretical data
plt.plot(wt_IPTG_bohr, wt_fold, marker='.', linestyle='none',
         markersize=20, alpha=0.8)
plt.plot(q18m_IPTG_bohr, q18m_fold, marker='.', linestyle='none',
         markersize=20, alpha=0.8)
plt.plot(q18a_IPTG_bohr, q18a_fold, marker='.', linestyle='none',
         markersize=20, alpha=0.8)
plt.plot(bohr_theo, fold_theo, color='gray')
plt.xlim(-6,6)
plt.xlabel('Bohr Parameter')
plt.ylabel('Fold Change')
plt.title('Data Collapse!')
plt.legend(('wt_lac', 'q18m_lac', 'q18a_lac',
            'theoretical'), loc='lower right')
plt.show()
