#!/usr/local/bin/python3

import os

import pandas as pd
from scipy.stats import zscore

# Replace "column" with column names(s)
# Add your own input and output file paths.

# Applies the Z-score statistic to Chromosome 1 to 22
def generate_z_score(input_path: str, output_path: str):
    if not os.path.isfile(input_path):
        raise ValueError(f"{input_path} does not exist, try a different file")
    df = pd.read_csv(input_path, encoding='utf-8')
    print(input_path)
    dropped = df["column"]
    del_cols = ["column"]
    for col in del_cols:
    	try:
    		df = df.drop(columns=[col])
    	except KeyError as e:
    		print(e)
    z_scores = df.apply(zscore)
    z_scores.insert(0, "column", dropped)
    file_name = input_path.split('/')[-1]
    file_name = file_name.split('.')[0] + "z_score.csv"
    z_scores.to_csv(os.path.join(output_path, file_name), index=False)

# Applies the Z-score statistic to Chromosome Y
def generate_z_score_y(input_path: str, output_path: str):
    if not os.path.isfile(input_path):
        raise ValueError(f"{input_path} does not exist, try a different file")
    df = pd.read_csv(input_path, encoding='utf-8')
    dropped = df["column"]
    df = df.drop(columns=["column"])
    z_scores = df.apply(zscore)
    z_scores.insert(0, "column", dropped)
    file_name = input_path.split('/')[-1]
    file_name = file_name.split('.')[0] + "z_score.csv"
    z_scores.to_csv(os.path.join(output_path, file_name), index=False)
    
# Loops through the csv inputs and produces outputs
if __name__ == "__main__":
	folder = "file_path_to_folder/folder" # Input file directory
	for file in os.listdir(folder):  
		if "z_score" in file or ".csv" not in file:
			continue
			
		if "Chromosome_Y" in file:
			try:
				generate_z_score_y(os.path.join(folder, file), "file_path/output.csv")  # replace with output directory
			except ValueError as e:
				print(e)
		else:
			try:
				generate_z_score(os.path.join(folder, file), "file_path/output.csv")  # replace with output directory
			except ValueError as e:
				print(e)