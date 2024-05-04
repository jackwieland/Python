#!/usr/local/bin/python3

import subprocess

def run_script1():
	subpocess.run(["Python3", 'File_Path/Backend_Multi_Python_Reader.py'])

def run_script2():
	subpocess.run(["Python3", 'File_Path/Backend_Multi_Python_Reader.py'])
	
def run_script3():
	subpocess.run(["Python3", 'File_Path/Backend_Multi_Python_Reader.py'])
	
def run_script4():
	subpocess.run(["Python3", 'File_Path/Backend_Multi_Python_Reader.py'])
	
def run_script5():
	subpocess.run(["Python3", 'File_Path/Backend_Multi_Python_Reader.py'])
	
def run_script6():
	subpocess.run(["Python3", 'File_Path/Backend_Multi_Python_Reader.py'])

def switch_case(option):
	cases = {
	1: run_script1,
	2: run_script2,
	3: run_script3,
	4: run_script4,
	5: run_script5,
	6: run_script6,
	
	# Function calling
	function = cases.get(option)
	if function:
		function()
	else:
		print('Invalid option')

# Prompt for user input

print('Select an option:')
print('1. Run Script 1')
print('2. Run Script 2')
print('3. Run Script 3')
print('4. Run Script 4')
print('5. Run Script 5')
print('6. Run Script 6')