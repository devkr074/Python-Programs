# ufunc Products in Python

import numpy as np
arr1=np.array([1,2,3,4])
x=np.prod(arr1)
print(x)
arr2=np.array([5,6,7,8])
x=np.prod([arr1,arr2])
print(x)
newarr=np.prod([arr1,arr2],axis=1)
print(newarr)
newarr=np.cumprod(arr1)
print(newarr)