# ufunc Summations in Python

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([1,2,3])
newarr=np.add(arr1,arr2)
print(newarr)
newarr=np.sum([arr1,arr2])
print(newarr)
newarr=np.sum([arr1,arr2],axis=1)
print(newarr)
newarr=np.cumsum(arr1)
print(newarr)