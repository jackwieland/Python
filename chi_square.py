#!/usr/local/bin/python3

import os
import pandas as pd
from scipy.stats import chi2

# direcotry input path
directory ='file_path_for_csv_folder/folder'

# Looping through all CSVs in directory path
for filename in os.listdir(directory):
	if filename.endswith('.csv'):
		print(f"Calculating Chi-square for file {filename}")
		
		# CSV data loading
		data = pd.read_csv(os.path.join(directory, filename))
		
		# Observed frequency defining 
		observed_frequencies = data['column_1'].values
		
		# Expected value defining
		expected_frequencies = data['column_2'].values
		
		# Defining the alpha level
		alpha = 0.05
		
		# degree of freedom calculation
		degree_of_freedom = len(observed_frequencies) - 1
		
		# Chi-square calculation
		chi2_statistic = sum((observed_frequencies - expected_frequencies) ** 2 / expected_frequencies)
		
		# P-value calculation
		p_value = 1 - chi2.cdf(chi2_statistic, degree_of_freedom)
		
	# P-value comparisons to determine signficance is present
	if p_value < alpha:
		print ('There is a significant association/goodness of fit')
	else:
		print('There is no association/goodness of fit')
	
	print(f"Chi-square statistic: {chi2_statistic}")
	print(f"Degree of freedom: {degree_of_freedom}")
	print(f"P-value: {p_value}")
	print('\n')