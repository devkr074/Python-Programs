# Random Permutations in NumPy in Python

from numpy import random
import numpy as np
arr=np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)
print(random.permutation(arr))