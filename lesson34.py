# Emily Savela; Created 15 September 2016
# Lesson 34, Seaborn and Data Display

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')
df = df.rename(columns={'impact force (mN)' : 'impf'})

# Instructions to reate groupby object
gb_frog = df.groupby('ID')
mean_impf = gb_frog['impf'].mean()
sem_impf = gb_frog['impf'].sem()

# Bar graph (in Seaborn); Groupby object is not necessary
# sns.barplot(data=df, x='ID', y='impf')
# plt.clf()

plt.close()
# Prepare plot
sns.boxplot(data=df, x='ID', y='impf')
sns.swarmplot(data=df, x='ID', y='impf', hue='date')
# removes the legend
plt.gca().legend_.remove
plt.show()
