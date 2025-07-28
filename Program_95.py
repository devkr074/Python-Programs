# Seaborn Module in Python

import matplotlib.pyplot as plt
import seaborn as sns
print(f"\nPlotting a Displot\n")
sns.displot([0,1,2,3,4,5])
plt.show()
print(f"\nPlotting a Displot Without the Histogram\n")
sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
plt.show()