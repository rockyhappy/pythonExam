import numpy as np


# for the length of a numpy array use the __len__() method
# for the row of a numpy array use the shape method .shape[0]
# for the column of a numpy array use the shape method .shape[1]
# for accessing the element of a numpy array use the index of the row and column like arr[0][0]
# numpy array are always square and each element is a list of same size
def retSmaller(arr):
    countL=1000
    len= arr.__len__()
    for i in range(len-1):
        size=arr[i].__len__()
        if size<countL:
            countL=arr[i].__len__()
    for i in range(len-1):
        size=arr[i].__len__()
        if size==countL:
            return arr[i]
    return countL


arr = np.array([[5,6,7,8,9],[1, 2, 3, 4, 5]])

print(retSmaller(arr))

go = "i am a lucky person tokyo"

size=go.__len__()
do=""
for i in range(size):
    do=do+go[i]+","

print(do)
