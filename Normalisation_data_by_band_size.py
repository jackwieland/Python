#!/usr/local/bin/python3

import pandas as pd

# to read csv in a Pandas data frame and generates a new data frame
df = pd.read_csv('file_path_input/input.csv')

cols_to_remove = [
	'insert column names' 
]
# Reads all columns except the ones specified for division
cols_div = df.drop(columns=cols_to_remove)

# Loop is created to apply the division and multiplied by 1 million
division_results_df = cols_div.apply(lambda x: x / df['Band_Size'] * 1000000)

# Write the division results DataFrame to a new CSV file
division_results_df.to_csv('file_path_for_output/output.csv', index=False)

print('Output to csv saved')