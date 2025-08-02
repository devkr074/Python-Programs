# SciPy Matlab Arrays in Python

from scipy import io
import numpy as np

arr = np.arange(10)
io.savemat("arr.mat", {"vec": arr})
arr = np.array(
    [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]
)
io.savemat("arr.mat", {"vec": arr})
mydata = io.loadmat("arr.mat")
print(mydata)
print(mydata["vec"])
mydata = io.loadmat("arr.mat", squeeze_me=True)
print(mydata["vec"])