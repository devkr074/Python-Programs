# Creating Your Own ufunc in Python

import numpy as np
def myadd(x,y):
    return x+y
myadd=np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4],[5,6,7,8]))
print(type(np.add))
print(type(np.concatenate))
if type(np.add)==np.ufunc:
    print("Add is ufunc")
else:
    print("Add is not ufunc")