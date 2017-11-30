#! /usr/bin/env python
# _*_ coding: utf:8 _*_

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
print(df)
