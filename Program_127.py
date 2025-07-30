# Pandas Cleaning Data of Wrong Format in Python

import pandas as pd

df = pd.read_csv("data.csv")
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
print(df.to_string())
df.dropna(subset=["Date"], inplace=True)