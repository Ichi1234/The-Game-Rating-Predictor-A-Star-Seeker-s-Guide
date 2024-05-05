import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image


class Model:
    def __init__(self):
        self.df = pd.read_csv('backloggd_games.csv')
        # drop none and unused column
        self.df.dropna(subset=self.df.columns.tolist(), how='any', inplace=True)
        self.string_to_number()

    def string_to_number(self):
        """Convert K (1,000) in csv to be integer"""
        for change in self.df.columns.tolist():
            if change in ['Plays', 'Playing', 'Backlogs', 'Wishlist', 'Lists', 'Reviews']:
                self.df[change] = pd.to_numeric(self.df[change], errors='coerce')

    def stats(self, column):
        return {"mean": round(self.df[column].mean(), 3), "median": round(self.df[column].median(), 3),
                "sd": round(self.df[column].std(), 3),
                "min": self.df[column].min(), "max": self.df[column].max(), "var": round(self.df[column].var(), 3)}

    @staticmethod
    def pull_image(img_name):
        """sent image to controller"""
        img = Image.open(f"img/{img_name}.png")
        return img

    def create_figure(self, master, x, y) -> FigureCanvasTkAgg:
        # plot the data
        figure = Figure(figsize=(4, 4))
        ax = figure.subplots()
        sns.barplot(x=x, y=y, data=self.df, errorbar=None, ax=ax)
        plt.xticks(rotation=45)

        if x == "Rating":
            ax.set_xlim(1, 5)
        else:
            ax.set_xlim(1, 10)

        if y == "Rating":
            ax.set_ylim(1, 5)
        else:
            ax.set_ylim(1, 10)

        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"Relationship between {x} and {y}")

        canvas = FigureCanvasTkAgg(figure, master=master)
        return canvas
