#Emily Savela; Created 14 September 2016
#Lesson 27 Hacker Statistics Lesson

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils
sns.set()

# Load data from finch beaks
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

# Generate bootstrap replicates
n_reps = 100000
bs_replicates_1975 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates_1975[i] = np.mean(bs_sample)

conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])

n_reps = 100000
bs_replicates_2012 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_replicates_2012[i] = np.mean(bs_sample)

conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])

# Compute EDCF of raw data
# x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)
# x_2012, y_2012 = bootcamp_utils.ecdf(bd_2012)
# x_1975_bs, y_1975_bs = bootcamp_utils.ecdf(bs_sample)
#
# # Plot data
# plt.close()
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none')
# plt.xlabel('beak depth (mm)')
# plt.ylabel('EDCF')
# plt.legend(('1975 data', 'bootstrap'), loc='lower right')
# plt.show()
