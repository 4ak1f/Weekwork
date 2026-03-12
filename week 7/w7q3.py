    import pandas as pd

    df = pd.DataFrame([[10,5,2,1],[20,15,4,3],[30,25,6,5],[40,35,8,7],[50,45,10,9]])
    print (df)
    print(df.iloc[:,1].mean())
    print(df.iloc[0:5,2:4].mean())
    print(df.sum(axis=1))
    print(df.mean(axis=1).max())