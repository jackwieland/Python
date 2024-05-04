#!/usr/local/bin/python3

import mysqlconnector as mycom
import pandas as pd

# Database connection
mydb=mycom.connect(host="",
				   user="",
				   password="",
				   database="")

mycursor=mydb.cursor()

df = pd.DataFrame(columns=['Column_1', 'Column_2'])

# SQL File Reading and output
query=[]
count=[]
data=[]
with open ('file_path_to_file/file.sql', 'r', encoding='utf-8') as file:
	#commands = mycursor.execute(file.read(), multi=True)
# Loops over SQL files and uses SQL comment lines as a row for Column_1 and counts the number of entries associated to SQL query
	commands=file.read().split(';')
	for comm in commands:
		if comm.strip():
			mycursor.execute(comm)
			results=mycursor.fetchall()
			#print(f"column_1{comm.strip()}"\nColumn_2:{len(results)}\n")
			query.append(comm.strip())
			for line in Column_1:
				new_list=line.split()
				#print(new_list[1])
			data.append(new_list[1])
			count.appen(len(results))
		#print(query)
		#print(count)
		
# Stores outputs to a csv
df = pd.DataFrame(columns=['Column_1', 'Column_2'])
df['Column_1'] = pd.Series(data)
df['Column_2'] = pd.Series(count)
csv_file='File_Path_to_Save/file.csv'
df.to_csv(csv_file)
print(df)

mydb.close()