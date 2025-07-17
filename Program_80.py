# NumPy Array Indexing in Python

import numpy as np
arr=np.array([1,2,3,4])
print(arr[0])
print(arr[1])
print(arr[2]+arr[3])
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2nd Element in 1st Row:",arr[0,1])
print("5th Element in 2nd Row:",arr[1,4])
print("Last Element from 2nd Dimension:",arr[1,-1])
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,2])