#!/usr/local/bin/python3

import os
import pandas as pd

# csv Data Reading
df = pd.read_csv('file_path_input/file.csv')

# Columns to be extracted
set_cols = [
    ['col1', 'col2'],
    ['col3', 'col4']

# Define the columns to include for mean calculation (excluding the first and last column)
for cols in set_cols:
    name = cols[0][0]
    tmp_df = df[['Column_index_Name'] + cols + ['Column_Name']].copy()
    tmp_df[f'File_{name}_Average'] = tmp_df.loc[:, cols].mean(axis=1)
    tmp_df.to_csv(f'file_to_folder/File_{name}/sub/Output_{name}.csv', columns=['Column_index_Name'] + cols + [f'Column_{name}_Average', 'Column_Name'], index=False)
    tmp_df.to_csv(f'path_for_output/File_{name}_Avg.csv', columns=['Column_index_Name'] + cols + [f'Column_{name}_Average'], index=False)

# directory input and output for merging
input_directory = 'input_file_directory/file.csv'
output_directory = 'output_path/file.csv'

# creating a merged dataframe
merged_df = pd.DataFrame()

# file lopping and removes column index name after the first csv
for file_name in os.listdir(input_directory):
	if file_name.endswith('.csv'):
		file_path = os.path.join(input_directory, file_name)
		df = pd.read_csv(file_path)
		
		if file_name == 'first_file_Avg.csv'
			# Columns 1 and 2 dropped from first csv file
			df_stripped = df.drop(df.columns[[1, 2]], axis=1)
		else:
			# removing columns 0, 1, 2 from csv after first_file.Avg.csv
			df_stripped = df.drop(df.columns[[0, 1, 2]], axis=1)
		
		merged_df = pd.concat([merged_df, df_stripped], axis=1)

# Merged output saved to csv file
merged_df.to_csv(output_file, index=False)
print(merged_df)