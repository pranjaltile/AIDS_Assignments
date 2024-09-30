import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/home/pl2/Downloads/iris.csv')  # Ensure the filename is correct

# Ensure that 'species' is treated as a categorical variable
df['species'] = df['species'].astype('category')

# Pairplot to visualize relationships between features
sns.pairplot(df, hue='species')

# Show the plot
plt.show()

