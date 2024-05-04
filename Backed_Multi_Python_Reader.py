#!/usr/local/bin/python3

import os
import subprocess

def run_program(scripts):
	try :
		output = subprocess.check_output(["python3",scripts],stderr=subprocess.STDOUT,text=True)
		return output
   except subprocess.CalledProcessError as e:
        return f"Error:{e.output}"
scripts=["Filepath/Backend_SQL_Processor.py"]

for script in scripts:
    output = run_program(script)
    print(f"Output of {script}{output}\n")       