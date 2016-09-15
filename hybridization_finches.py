# Emily Savela; Created 14 September 2016
# Exercise 4 Long-term trends in hybridization of Darwin Finches
# Problem 4.1 (a-c)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils as bcu
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load data into panda data frames
df_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
df_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

# Change column names to be equivalent across data frames
df_1973 = df_1973.rename(columns={'beak length' : 'beak length (mm)',
                                  'beak depth' : 'beak depth (mm)',
                                  'yearband' : 'year'})
df_1975 = df_1975.rename(columns={'Beak length, mm' : 'beak length (mm)',
                                  'Beak depth, mm' : 'beak depth (mm)'})
df_1987 = df_1987.rename(columns={'Beak length, mm' : 'beak length (mm)',
                                  'Beak depth, mm' : 'beak depth (mm)'})
df_1991 = df_1991.rename(columns={'blength' : 'beak length (mm)',
                                  'bdepth' : 'beak depth (mm)'})
df_2012 = df_2012.rename(columns={'blength' : 'beak length (mm)',
                                  'bdepth' : 'beak depth (mm)'})

# Ensure all data frame have years displayed in YYYY format
df_1973 = df_1973.replace(73, 1973)
df_1975['year'] = 1975
df_1987['year'] = 1987
df_1991['year'] = 1991
df_2012['year'] = 2012

# # Checking consistency of column labels
# print(df_1973.columns)
# print(df_1975.columns)
# print(df_1987.columns)
# print(df_1991.columns)
# print(df_2012.columns)

# Concatenate all dataframes into one
df_finch = pd.concat((df_1973, df_1975, df_1987, df_1991, df_2012),
                      ignore_index=True, axis=0)

# Drop duplicate measurements of finches in the same year
df_finch = df_finch.drop_duplicates(subset=['band','year'])
df_finch.to_csv('grant_complete_finch.csv', index=False)
