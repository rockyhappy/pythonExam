import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arr = [1,2,7,4,5,6]
index=['a', 'b', 'c', 'd', 'e', 'f']
# to create a pandas series use the pd.Series method from a list 
sr = pd.Series(arr, index=index)
# to access elements of a pandas series use the natural index of the element 
print(sr.iloc[2])
# to access elements of a pandas series use the given index of the element
print(sr.loc['c'])
print(sr['c'])

# to create a pandas series use the pd.Series method from a dictionary
data = {'a': 65, 'b': 66, 'c': 67}
sr = pd.Series(data)
# to access elements of a pandas series use the natural index of the element 
print(sr.iloc[1])
# to access elements of a pandas series use the given index of the element
print(sr.loc['b'])
print(sr['b'])
print(sr)


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df=pd.DataFrame(data,index=["day1","day2","day3"])
print(df.loc["day1"])   

df=pd.read_csv("python\data.csv")
print(df.to_string())
