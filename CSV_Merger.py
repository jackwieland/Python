#!/usr/local/bin/python3

import pandas as pd

df1 = pd.read_csv('Path_to_file/file.csv')
df2 = pd.read_csv('Path_to_file/file.csv')
df3 = pd.read_csv('Path_to_file/file.csv')

# Dropping index column from the first data frame
df1_stripped = df1.drop(df1.columns[0], axis=1)

# dropping index column and chromosome band column
df2_stripped = df2.drop(df2.columns[[0, 1]], axis=1)
df3_stripped = df3.drop(df3.columns[[0, 1]], axis=1)

merged_output = pd.concat([df1_stripped, df2_stripped, df3_stripped], axis=1)

merged_output.to_csv('Savedfile.csv', index=False)