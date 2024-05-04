import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image
import customtkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

df = pd.read_csv('backloggd_games.csv')

# drop none and unused column
df = df.iloc[:, 1:]
df.dropna(subset=df.columns.tolist(), how='any', inplace=True)


# Seaborn
# Multiple bar graph example 1


class Model:
    def __init__(self):
        pass

    def create_figure(self, root) -> FigureCanvasTkAgg:
        # plot the data
        figure = Figure(figsize=(6, 6))
        ax = figure.subplots()
        sns.barplot(x='Playing', y='Plays', data=df, errorbar=None)
        plt.xticks(rotation=45)

        ax.set_xlim(1, 20)
        ax.set_ylim(1, 45)

        ax.set_xlabel('Year')
        ax.set_ylabel('Thailand Population')
        ax.set_title('Thailand Population between 2550-2564')

        canvas = FigureCanvasTkAgg(figure, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
        return canvas


root = tk.CTk()
m = Model()
canvas = m.create_figure(root)

root.mainloop()
