import pandas as pd

df = pd.read_csv("data.csv")

df = df.rename(columns={"A":"Age","B":"Marks"})
df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(float)

print(df)
print(df.dtypes)