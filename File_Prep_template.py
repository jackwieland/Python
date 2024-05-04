#!/usr/local/bin/python3

import pandas as pd 

# Data reading
set1_columns = ['col0', 'col1', 'col2', 'col3']
set2_columns = ['col0', 'col1', 'col2', 'col3']

# Column extraction and excludes col0 from calculation
set1_df = df[set1_columns].copy()
set1_df['Mean_Col_Name'] = set_df.iloc[:, 1:].mean(axis=1)

set2_df = df[set2_columns].copy()
set2_df['Mean_Col_Name'] = set_df.iloc[:, 1:].mean(axis=1)

# Output saving for validation
set1_df.to_csv('File_Path_to_Save/file1.csv', index=False)
set2_df.to_csv('File_Path_to_Save/file2.csv', index=False)

# Output saving for validation for the mean
set1_df.to_csv('File_Path_to_Save/file1.csv', columns=['col0', 'col1'] index=False)
set2_df.to_csv('File_Path_to_Save/file2.csv', columns=['col0', 'col1'] index=False)

# Uses CSV from lines 21 and 22
set_1df = ('File_Path_to_file/file1.csv')
set_2df = ('File_Path_to_file/file1.csv')

# Column 0 dropped from set_2df
set_2df_stripped = set_2df.drop(set_2df.columns[0], axis=1)

# merges set_1df and set_2df, using code from CSV_Merger.py
merged_df = pd.concat([set_1df, set_2df_stripped], axis=1)

# merged output save
merged_df.to_csv('File_Path_to_save_for_t_test/file.csv', index=False)