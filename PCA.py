# Import required libraries
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from your local system
# Adjust the path as per your Downloads folder
file_path = r"C:\Users\<YourUsername>\Downloads\iris.csv"
df = pd.read_csv(file_path)

# Display initial statistics
print("Initial statistics of the dataset:")
print(df.describe())

# Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Separate features and target variable
X = df.iloc[:, :-1]  # Assuming the last column is the target
y = df.iloc[:, -1]   # Adjust if the target is in a different position

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA for 2 components
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)

# Create a DataFrame for the principal components
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_df['target'] = y

# Explained variance
print("\nExplained variance by each component:", pca.explained_variance_ratio_)

# Plot the results
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PC1', y='PC2', hue='target', data=pca_df, palette='viridis', s=100)
plt.title("PCA of Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Target")
plt.show()
