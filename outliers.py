import pandas as pd


df = pd.read_csv('/home/pl2/Downloads/iris.csv')  

#create a function to find outliers using IQR

def find_outliers_IQR(df):

   q1=df.quantile(0.25)

   q3=df.quantile(0.75)

   IQR=q3-q1

   outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]

   return outliers


def drop_outliers_IQR(df):

   q1=df.quantile(0.25)

   q3=df.quantile(0.75)

   IQR=q3-q1

   not_outliers = df[~((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]

   outliers_dropped = outliers.dropna().reset_index()

   return outliers_dropped
#print(df.head(10))
#print(df.tail())
#print(df.info())
#print(df.describe())

print(df.isnull().sum())

outliers = find_outliers_IQR(df)

print("number of outliers:\n",str(len(outliers)))

print("max outlier value:\n",str(outliers.max()))

print("min outlier value:\n", str(outliers.min()))

print(outliers)

drop= drop_outliers_IQR(df)
print(drop)
