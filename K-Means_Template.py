#!/usr/local/bin/python3

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('YOUR/FILE/PATH/FILE.CSV')

# Extract feature columns and label column
features = data[['Col_1', 'Col_2']]
labels = data['Some_column']

# Apply K-means clustering
kmeans = KMeans(n_clusters=3) # Change as appropriate
clusters = kmeans.fit_predict(features)

# Visualise the cluster graph
plt.scatter(features['Col_1'], features['Col_2'], c=clusters, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids')
plt.xlabel('Col_1')
plt.ylabel('Col_2')
plt.title('TITLE')
plt.legend()
plt.show
plt.savefig('/file_path/test.png', dpi=300)

print("Plot saved successfully as 'check.png'")
