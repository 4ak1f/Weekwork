import pandas as pd

df = pd.read_csv("data.csv")

df = df.fillna(df.mean(numeric_only=True))
df = df.fillna(df.median(numeric_only=True))

print(df)