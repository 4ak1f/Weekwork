import pandas as pd

df = pd.read_csv("data.csv")

df = df.dropna()
df = df[df.iloc[:,0] > 50]

print(df)