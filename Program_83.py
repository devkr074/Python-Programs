# NumPy Array Copy vs View in Python

import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=42
print(arr)
print(x)
x=arr.view()
arr[0]=42
print(arr)
print(x)
x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)