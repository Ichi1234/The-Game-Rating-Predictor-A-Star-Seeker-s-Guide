import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

df = pd.read_csv('backloggd_games.csv')

# drop none and unused column
df = df.iloc[:, 1:]
df.dropna(subset=df.columns.tolist(), how='any', inplace=True)

seaborn.scatterplot(x="timepoint",
                    y="signal",
                    data=fmri)
class Model:
    def __init__(self):
        pass

    @staticmethod
    def create_figure(master, x, y) -> FigureCanvasTkAgg:
        # plot the data
        figure = Figure(figsize=(4, 4))
        ax = figure.subplots()
        sns.barplot(x=x, y=y, data=df, errorbar=None, ax=ax)
        plt.xticks(rotation=45)

        if x == "Rating":
            ax.set_xlim(1, 5)
        else:
            ax.set_xlim(1, 10)

        if y == "Rating":
            ax.set_ylim(1, 5)
        else:
            ax.set_ylim(1, 25)

        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"Relationship between {x} and {y}")

        canvas = FigureCanvasTkAgg(figure, master=master)
        return canvas
