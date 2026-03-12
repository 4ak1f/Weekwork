import pandas as pd

s = pd.Series([10,20,30,40,50])
print(s)

d = {"Name":["A","B","C"],"Age":[21,22,23],"Marks":[80,85,90]}
df = pd.DataFrame(d)
print(df)