import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image
import customtkinter as tk
import matplotlib.pyplot as plt

df = pd.read_csv('backloggd_games.csv')

# drop none and unused column
df = df.iloc[:, 1:]
df.dropna(subset=df.columns.tolist(), how='any', inplace=True)


class Model:
    def __init__(self):
        pass
