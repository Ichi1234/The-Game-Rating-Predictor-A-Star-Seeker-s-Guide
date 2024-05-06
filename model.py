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

    def game_title(self):
        return self.df["Title"].values.tolist()

    @staticmethod
    def k_destroyer(val):
        """Remove K in csv and *1000 to the value which have K"""
        val = val.replace('K', '')
        val = float(val)
        return val * 1000

    def string_to_number(self):
        """Convert K (1,000) in csv to be integer"""
        for change in self.df.columns.tolist():
            if change in ['Plays', 'Playing', 'Backlogs', 'Wishlist', 'Lists', 'Reviews']:
                self.df[change].apply(self.k_destroyer)

    def stats(self, column):
        """Send statistic datas to controller"""
        return {"mean": round(self.df[column].mean(), 3), "median": round(self.df[column].median(), 3),
                "sd": round(self.df[column].std(), 3),
                "min": self.df[column].min(), "max": self.df[column].max(), "var": round(self.df[column].var(), 3)}

    def find_game_data(self, name_of_the_game):
        """Send datas of the game to controller"""
        return self.df[self.df['Title'] == name_of_the_game].iloc[0].to_dict()

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
