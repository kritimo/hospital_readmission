import IPython
import pandas as pd
import numpy as np
from statistics import mode
import matplotlib.pyplot as plt  
from sklearn.preprocessing import MinMaxScaler

df_original = pd.read_csv("diabetic_data.csv")
print(df_original.shape)