# Emily Savela; Created 14 September 2016
# Exercise 4 Long-term trends in hybridization of Darwin Finches
# Problem 4.1 (d)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils as bcu
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load formatted data
dt_finch = pd.read_csv('grant_complete_finch.csv', comment='#')

# ECDF Plots
fortis_data = dt_finch.loc[(dt_finch['species']=='fortis') &
                        (dt_finch['year']==1987), 'beak depth (mm)']
scandens_data = dt_finch.loc[(dt_finch['species']=='scandens') &
                        (dt_finch['year']==1987), 'beak depth (mm)']

fortis_x, fortis_y = bcu.ecdf(fortis_data)
scandens_x, scandens_y = bcu.ecdf(scandens_data)

# Plot EDCF
plt.close()
plt.plot(fortis_x, fortis_y, marker='.', linestyle='none')
plt.plot(scandens_x, scandens_y, marker='.', linestyle='none')
plt.xlabel = 'beak depth (mm)'
plt.ylabel = 'ECDF'
plt.legend = 'Geospiza fortis, 1987', 'Geospiza scandens, 1987'
plt.show()
