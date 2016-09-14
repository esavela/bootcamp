# Emily Savela; Created 14 September 2016
# Lesson 32: Practice with Pandas; Frog adhesion data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Extract impact time of all impacts that had ad. strength > 2000 Pa
df_ad_strength = df[np.abs(df['adhesive strength (Pa)']) > (2000)]
df_time_ad_strength = df_ad_strength.loc[:, ['impact time (ms)',
                                         'adhesive strength (Pa)']]
print(df_time_ad_strength)
print('\n')

# Extract the impact force and adhesive force for all of Frog II
df_frog_ii = df.loc[df['ID'] == 'II', ['impact time (ms)', 'adhesive strength (Pa)']]
print(df_frog_ii)
print('\n')
