import pandas as pd

df = pd.read_csv("python\data.csv")
df.drop("Duration", axis=1, inplace=True)
len_df = len(df)
for i in range(10, len_df):
    df.drop(i, inplace=True)
df.index = [10,9,8,7,6,5,4,3,2,1]
print(df.to_string())
print(df.loc[1]['Pulse'])
print(df.iloc[2]['Pulse'])
df.to_csv("python\data2.csv", index=False)
