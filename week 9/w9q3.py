import pandas as pd

df = pd.read_csv('data.csv')

# Keep only numeric columns
df_num = df.select_dtypes(include=['number'])

Q1 = df_num.quantile(0.25)
Q3 = df_num.quantile(0.75)
IQR = Q3 - Q1

df_clean = df_num[~((df_num < (Q1 - 1.5*IQR)) | (df_num > (Q3 + 1.5*IQR))).any(axis=1)]

print(df_clean.head())