import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/home/pl2/Downloads/iris.csv')
df.columns = df.columns.str.strip()  # Clean column names
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# Separating out the features
x = df.loc[:, features].values

# Standardizing the features
x = StandardScaler().fit_transform(x)

# PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)

# Create a DataFrame with the principal components
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])

# Concatenate with the target variable
finalDf = pd.concat([principalDf, df[['species']]], axis=1)

# Print debug information
print(finalDf.head())
print(finalDf['species'].unique())

# Visualization
# Visualization
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 Component PCA', fontsize=20)

# Define targets and colors (remove "Iris-" prefix)
targets = ['setosa', 'versicolor', 'virginica']  # Update to match the DataFrame
colors = ['r', 'g', 'b']

# Plot each target
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['species'] == target
    print(f"Plotting {target}: {indicesToKeep.sum()} points")  # Count of points being plotted
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
               finalDf.loc[indicesToKeep, 'principal component 2'],
               c=color, s=50, label=target)

ax.legend()
ax.grid()
plt.show()  # Display the plot

