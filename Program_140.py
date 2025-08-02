# SciPy Statistical Significance Tests in Python

import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import kstest
from scipy.stats import describe
from scipy.stats import skew, kurtosis
from scipy.stats import normaltest

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
print(res)
res = ttest_ind(v1, v2).pvalue
print(res)
v = np.random.normal(size=100)
res = kstest(v, "norm")
print(res)
v = np.random.normal(size=100)
res = describe(v)
print(res)
v = np.random.normal(size=100)
print(skew(v))
print(kurtosis(v))
v = np.random.normal(size=100)
print(normaltest(v))