# NumPy Logs in Python

from math import log
import numpy as np
arr=np.arange(1,10)
print(np.log2(arr))
arr=np.arange(1,10)
print(np.log10(arr))
arr=np.arange(1,10)
print(np.log(arr))
nplog=np.frompyfunc(log,2,1)
print(nplog(100,15))