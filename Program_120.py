# Pandas in Python

import pandas as pd

mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
myvar = pd.DataFrame(mydataset)
print(myvar)
print(pd.__version__)