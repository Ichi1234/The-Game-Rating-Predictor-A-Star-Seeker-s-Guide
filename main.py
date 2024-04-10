import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('backloggd_games.csv')

# drop none and unused column
df = df.iloc[:, 1:]
df.dropna(subset=df.columns.tolist(), how='any', inplace=True)
print(df)