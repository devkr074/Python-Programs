# Pandas Removing Duplicates in Python

import pandas as pd

df = pd.read_csv("data.csv")
print(df.duplicated())
df.drop_duplicates(inplace=True)