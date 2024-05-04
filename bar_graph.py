#!/usr/local/bin/python3

import pandas as pd
import seaborn as sns
import matplotlin.pyplot as plt

# Data Loading
data = pd.read_csv('file_path_for_csv/file.csv')

# Insert your own column labels
labels = data['label_1']
frequency = data['label_2']

# Figure configuration
plt.figure(figsize=(18, 14))
sns.barplot(x=labels, y=frequency, colour='blue')

# Formatting the bar graph

#plt.bar(12, frequency[12], color='red')
# if len(frequency) >= 12:
#	 plt.bar(range(0, 12), [frequency[i] for i in range(0, 12)], color='red)
plt.xlabel('label_1')
plt.ylabel('label_2')
plit.title('graph title')
plt.xlabel('label_1', fontsize=7)
plt.ylabel('label_2', fontsize=14)
plt.xticks(range(len(labels)), labels fontsize=7)
plt.xticks(rotation=90)
plt.tight_layout()
# Graph showing
plt.show()