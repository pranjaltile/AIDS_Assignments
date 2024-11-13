# Step 1: Import all the required Python libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Step 2: Locate open-source data from the web
# For simplicity, we use the built-in Iris dataset from seaborn.
# Description: The Iris dataset contains measurements for 150 iris flowers from three different species.
# URL: https://www.kaggle.com/datasets/uciml/iris

# Step 3: Load the dataset into a pandas DataFrame
df = sns.load_dataset("iris")

# Step 4: Display the initial statistics
print("Initial Statistics:")
print(df.describe(include='all'))
print("\nFirst few rows of the dataset:\n", df.head())

# Step 5: Scan all variables for missing values and inconsistencies
print("\nMissing values in each column:\n", df.isnull().sum())
# As the Iris dataset has no missing values, if there were any, we could fill them like this:
# df.fillna(df.mean(), inplace=True)  # for numeric columns

# Step 6: Scan all numeric variables for outliers
# We use boxplot to visualize potential outliers in the numeric variables
numeric_columns = df.select_dtypes(include=[np.number]).columns
for col in numeric_columns:
    plt.figure()
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")

# Remove outliers using the IQR method
for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# Step 7: Apply data transformations on at least one of the variables
# Here we normalize the 'sepal_length' column as an example
scaler = StandardScaler()
df['sepal_length_scaled'] = scaler.fit_transform(df[['sepal_length']])

# Step 8: Turn categorical variables into quantitative variables
# Convert 'species' column into numerical format using label encoding
df['species_encoded'] = df['species'].astype('category').cat.codes

print("\nData after transformations and encoding:")
print(df.head())
