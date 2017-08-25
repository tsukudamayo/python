# coding : utf-8

import sys
import pandas as pd
import matplotlib.pyplot as plt

# read sample data
df = pd.read_csv('./data/shutdown_test_data.csv', header=None)

## read data from command line argument
#df = pd.read_csv(sys.argv[1], header=None)

# calculate mean
result_mean = df[2].groupby([df[4], df[5]]).mean()
print(result_mean)

# plot
result = df[2].groupby([df[4], df[5]]).mean().plot(kind='bar', color=['#348ABD', '#7A68A6', '#A60628'], width=1)
plt.show()
