#!/usr/local/bin/python3

import os
import pandas as pd
from scipy import stats

# Defining a function
def run_t_test(data):
	t_stat, p_val = stats,ttest_rel(data['Column_1'], data['Column_2'])
	
	print('Paired t-statistic:', t_stat)
	print('Two-tailed p-value', p_val)
	return p_val

# directory input
directory = 'file_path_to_input/file.csv'

# list generation
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# t-test significance determination
alpha = 0.05

# t-test output
for file in csv_files:
	print('Analysing:', file)
	data = pd.read_csv(os.path.join(directory, file))
	p_val = run_t_test(data)
	if p_val < alpha:
		if Column_1 > Column_2
			print('There is statical significance for Column_1')
			print('There is Significance)
		else:
			print('There is statical significance for Column_2')
			print('There is Significance)
	else:
		print('There is no statisitcal significance between Column_1 and Column_2')
	print('\n')