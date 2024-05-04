#!/usr/local/bin/python3

import os
import pandas as pd
from scipy import stats

# Defining a function
def run_t_test(data):
	t_stat, p_val = stats,ttest_rel(data['Column_1'], data['Column_2'])
	
	print('Paired t-statistic:', t_stat)
	print('Two-tailed p-value', p_val)

# Running the t-test 	
	alpha = 0.05
	
	if p_val < alpha:
		print('There is statistical significnace between Column_1 and Column_2')
		print('There is signficiance for Column_1')
	else:
		print('There is no statistical significnace between Column_1 and Column_2')
		print('There is no signficiance for Column_1')

# file directory
directory = 'file_path_for_csvs/folder'

# list generation
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# t-test outputs
for file in csv_files:
	print('Analysing:', file)
	data = pd.read_csv(os.path.join(directory, file))
	run_t_test(data)
	print('\n')