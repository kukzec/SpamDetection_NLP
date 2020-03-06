
import numpy as np
import pandas as pd

import csv




df = pd.read_csv("spam.csv", encoding = "latin-1")
df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis = 1)
df = df.replace(["ham", "spam"], [0,1])
print(df.shape)
print(df.head(1))









