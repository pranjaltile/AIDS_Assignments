import pandas as pd

# Load the dataset
df = pd.read_csv('/home/pl2/Downloads/iris.csv')

# Function to find outliers using IQR
def find_outliers_IQR(df):
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    IQR = q3 - q1
    
    # Create a boolean mask for outliers
    outliers_mask = (df < (q1 - 1.5 * IQR)) | (df > (q3 + 1.5 * IQR))
    
    # Return DataFrame with outliers
    outliers = df[outliers_mask]
    return outliers

# Function to drop outliers using IQR
def drop_outliers_IQR(df):
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    IQR = q3 - q1
    
    # Create a mask for non-outliers
    not_outliers_mask = ~((df < (q1 - 1.5 * IQR)) | (df > (q3 + 1.5 * IQR)))
    
    # Filter the DataFrame to keep only non-outliers
    not_outliers = df[not_outliers_mask].reset_index(drop=True)
    return not_outliers

# Function to cap outliers
def cap_outliers_IQR(df):
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    IQR = q3 - q1
    
    # Define cap values
    lower_cap = q1 - 1.5 * IQR
    upper_cap = q3 + 1.5 * IQR
    
    # Cap the outliers
    df_capped = df.copy()
    df_capped[df < lower_cap] = lower_cap
    df_capped[df > upper_cap] = upper_cap
    
    return df_capped

# Check for missing values
print("Missing values in each column:\n", df.isnull().sum())

# Find outliers
outliers = find_outliers_IQR(df)
print("Number of outliers:\n", len(outliers))
print("Max outlier value:\n", outliers.max())
print("Min outlier value:\n", outliers.min())
print("Outliers:\n", outliers)

# Drop outliers
df_cleaned = drop_outliers_IQR(df)
print("DataFrame after dropping outliers:\n", df_cleaned)

# Cap outliers
df_capped = cap_outliers_IQR(df)
print("DataFrame after capping outliers:\n", df_capped)

