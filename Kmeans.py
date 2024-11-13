# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = "C:/Users/YourUsername/Downloads/sales_data_sample.csv"  # Update with your local path
data = pd.read_csv(file_path)

# Preview the dataset
print("Dataset preview:")
print(data.head())

# Select features for clustering (example: choosing numerical columns)
# Adjust feature selection based on available columns in your dataset
features = data[['SALES', 'QUANTITYORDERED']]  # Replace with relevant columns

# Standardize the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Use the Elbow Method to find the optimal number of clusters
inertia = []
cluster_range = range(1, 11)

for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the Elbow graph
plt.figure(figsize=(8, 5))
plt.plot(cluster_range, inertia, marker='o')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Based on the Elbow plot, select the optimal number of clusters
optimal_k = 3  # Adjust based on the elbow point in your plot
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

# Add cluster labels to the original dataset
data['Cluster'] = clusters
print("\nDataset with cluster labels:")
print(data.head())

# Plot clusters
plt.figure(figsize=(8, 5))
plt.scatter(scaled_features[:, 0], scaled_features[:, 1], c=clusters, cmap='viridis', marker='o')
plt.title('K-Means Clustering')
plt.xlabel('SALES (scaled)')
plt.ylabel('QUANTITYORDERED (scaled)')
plt.show()
