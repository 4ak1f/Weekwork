import pandas as pd

df = pd.read_csv("data.csv")

print(df.isnull().sum())
print(df[df.isnull().any(axis=1)])