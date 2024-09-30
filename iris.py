import pandas as pd

# Load the dataset
df = pd.read_csv('/home/pl2/Downloads/iris.csv')  # Replace 'iris.csv' if your file has a different name

# Display the first few rows of the dataframe
print(df.head(10))
print(df.tail())
#print(df.info())

#print(df.describe())

print(df.isnull().sum())
