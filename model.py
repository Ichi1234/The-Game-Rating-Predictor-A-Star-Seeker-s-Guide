import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image


def k_destroyer(val):
    """Remove K in csv and *1000 to the value which have K"""
    val = val.replace('K', '')
    val = float(val)
    return val * 1000


df = pd.read_csv('backloggd_games.csv')
df.dropna(subset=df.columns.tolist(), how='any', inplace=True)
df['Plays'] = df['Plays'].apply(k_destroyer)
df['Plays'] = df['Plays'] = pd.to_numeric(df['Plays'], errors='coerce')
df['Release_Date'] = pd.to_datetime(df['Release_Date'], format='%d-%b-%y', errors='coerce')
df.set_index('Release_Date', inplace=True)
annual_df = df['Rating'].resample('YE').mean()

plt.plot(annual_df.index, annual_df, 'r-')
plt.title('Average Games Rating Per Decade')

# Set the labels for the x-axis and y-axis
plt.xlabel('Years')
plt.ylabel('Rating')
plt.show()

#
# what = "Genres"
# # all_value = []
# all_value = ['Adventure', 'RPG', 'Puzzle', 'Brawler', 'Indie', 'Platform', 'Turn Based Strategy', 'Simulator',
#              'Shooter', 'Strategy', 'Music', 'Arcade', 'Fighting', 'Visual Novel', 'Tactical', 'Card & Board Game',
#              'Sport', 'Racing', 'MOBA', 'Point-and-Click', 'Real Time Strategy', 'Quiz/Trivia', 'Pinball', 'Action']
#
# dict_of_all_value = {}
# # for i in df[what]:
# #     for j in eval(i):
# #         if j not in all_value:
# #             all_value.append(j)
# # print(all_value)
#
# # dict_with_values = {value: [0, 0, 0] for value in all_value}
# # print(dict_with_values)
# #
# # for i in df.values:
# #     for j in all_value:
# #         if j in eval(i[6]):
# #             dict_with_values[j][0] += i[7]
# #             dict_with_values[j][1] += 1
# #             dict_with_values[j][2] += i[8]
# #
# # print(dict_with_values)
#
# # result = {}
# result = {'Adventure': [29780.999999999873, 9610, 1072251400.0], 'RPG': [15136.799999999961, 4703, 560864600.0],
#           'Puzzle': [11168.500000000018, 3637, 373024300.0], 'Brawler': [3893.5, 1277, 170112800.0],
#           'Indie': [19447.39999999985, 6546, 561394500.0], 'Platform': [11021.000000000022, 3655, 423257000.0],
#           'Turn Based Strategy': [2498.800000000002, 768, 91863200.0],
#           'Simulator': [10274.699999999959, 3419, 344753200.0], 'Shooter': [12564.500000000022, 4128, 479559700.0],
#           'Strategy': [10403.100000000008, 3372, 362756500.0], 'Music': [2101.499999999999, 653, 68887800.0],
#           'Arcade': [7785.400000000013, 2697, 267541200.0], 'Fighting': [4725.2999999999965, 1608, 215555800.0],
#           'Visual Novel': [3814.900000000003, 1145, 91276900.0], 'Tactical': [1926.5999999999972, 599, 78844800.0],
#           'Card & Board Game': [1065.0000000000005, 361, 34389600.0], 'Sport': [5029.300000000007, 1729, 177894000.0],
#           'Racing': [3861.1000000000013, 1321, 142048000.0], 'MOBA': [70.79999999999998, 26, 2190200.0],
#           'Point-and-Click': [2828.200000000005, 857, 94277800.0],
#           'Real Time Strategy': [1709.6000000000004, 534, 61766400.0],
#           'Quiz/Trivia': [597.2000000000005, 207, 15144200.0], 'Pinball': [215.3000000000001, 79, 6347100.0],
#           'Action': [2.6, 1, 12000.0]}
#
# for key, var in result.items():
#     result[key] = [var[0] / var[1], var[2]]
#
# print(result)
# sorted_result = dict(sorted(result.items(), key=lambda x: x[1][1] / x[1][0], reverse=True))
# print(sorted_result)
#
# for key, var in sorted_result.items():
#     sorted_result[key] = var[0]
#
# print(sorted_result)
#
# data = pd.DataFrame({what: list(sorted_result.keys()), 'Rating': list(sorted_result.values())})
#
# plt.figure(figsize=(10, 6))
# s = sns.histplot(x='Rating', y=what, data=data)
# s.set_xticklabels(s.get_xticklabels(), rotation=50, horizontalalignment="right")
# # s.set_xlim(right=20)  # Set the x-axis limit
# plt.xlabel(what)
# plt.ylabel('Rating')
# plt.title('Relationship between Rating and Genres')
# plt.show()


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
                self.df[change] = self.df[change].apply(self.k_destroyer)
                self.df[change] = pd.to_numeric(self.df[change], errors='coerce')

    def stats(self, column):
        """Send statistic datas to controller"""
        return {"mean": round(self.df[column].mean(), 3), "median": round(self.df[column].median(), 3),
                "sd": round(self.df[column].std(), 3), "type": self.df[column].dtypes,
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

        if x == "empty_x" and y == "empty_y":
            empty_df = pd.DataFrame()
            empty_df[x], empty_df[y] = [], []
            s = sns.barplot(x=x, y=y, data=empty_df, errorbar=None, ax=ax)
        else:
            s = sns.barplot(x=x, y=y, data=self.df, errorbar=None, ax=ax)

        s.set_xticklabels([])
        s.set_yticklabels([])

        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"Relationship between {x} and {y}")

        canvas = FigureCanvasTkAgg(figure, master=master)
        return canvas
