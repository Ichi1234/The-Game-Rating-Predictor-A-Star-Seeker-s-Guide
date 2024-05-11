"""MVC model class"""
import pandas as pd
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image


class Model:
    """This class use for store database and calculation"""

    def __init__(self):
        self.df = pd.read_csv('backloggd_games.csv')
        self.password = pd.read_csv('user_password.csv')
        self.forum_data = pd.read_csv('forum.csv')

        self.credit = ("Hello! My name is Kasidet Uthaiwiwatkul. \n"
                       "I am the developer of this program. \nIf you have any "
                       "questions or would like to hire me, \n"
                       "please feel free to contact me using any of the following"
                       " methods. \n \nMy contact information:"
                       "\nFacebook: Kasidet Uthaiwiwatkul\nEmail: "
                       "ichigamer111th@gmail.com"
                       "\nInstragram : iiiiiiiiiiiiiichiiiiiiiiiiiiii"
                       "\nYoutube: "
                       "@Chosen_Banana\nDiscord: what_is_my_username")

        self.user = ""
        # drop none and unused column
        self.df.dropna(subset=self.df.columns.tolist(), how='any', inplace=True)
        self.string_to_number()

    def game_title(self):
        """send all the game title to GameData class"""
        return self.df["Title"].values.tolist()

    def new_post(self, title: str):
        """Append new post to csv"""
        new_post = {'Title': title, 'Name': self.user}

        try:
            self.forum_data = pd.read_csv('forum.csv')
            # handle row error by input waiting-for-user-to-comment
            if len(new_post) != len(self.forum_data.columns):
                for i in range(int(self.forum_data.columns[-1][-1]) + 1):
                    new_post.update({f"com_{i}": "waiting-for-user-to-comment"})
                    new_post.update({f"user_{i}": "waiting-for-user-to-comment"})
            self.forum_data._append(new_post, ignore_index=True).to_csv('forum.csv', index=False)

            self.forum_data = pd.read_csv('forum.csv')
            return True

        except PermissionError:
            return False

    def show_post(self):
        """Show all the available code to user"""
        self.forum_data = pd.read_csv('forum.csv')
        return [{k: v[i] for k, v in self.forum_data.items()} for i in range(len(self.forum_data))]

    def check_password(self, user, password):
        """Is the password correct?"""
        self.user = user
        try:
            who = self.password[self.password['Username'] == user]
            if who.empty:
                return False
            return password in str(who['Password'].iloc[0])

        except ValueError:
            return False

    def update_csv(self, csv_name: str, value: dict, value2=None):
        """Update target csv file"""
        if csv_name == "pass":
            try:
                if self.password[self.password["Username"] == value["Username"]].empty:
                    (self.password._append(value, ignore_index=True)
                     .to_csv('user_password.csv', index=False))

                    self.password = pd.read_csv('user_password.csv')
                    return True
                return "exist"

            except PermissionError:
                return False
        elif csv_name == "forum":
            try:
                self.forum_data = pd.read_csv('forum.csv')
                if len(value) != len(self.forum_data.columns):
                    handle_error_list = ["waiting-for-user-to-comment"
                                         for _ in range(len(self.forum_data))]
                    if self.forum_data.columns[-1] == "Name":
                        self.forum_data["com_0"] = handle_error_list
                        self.forum_data["user_0"] = handle_error_list

                    else:
                        self.forum_data[value2[0]] = handle_error_list
                        self.forum_data[value2[1]] = handle_error_list
                self.forum_data.loc[self.forum_data["Title"] == value["Title"],
                                    value2[0]] = value2[2][0]
                self.forum_data.loc[self.forum_data["Title"] == value["Title"],
                                    value2[1]] = value2[2][1]

                self.forum_data.to_csv('forum.csv', index=False)
                self.forum_data = pd.read_csv('forum.csv')
                return True
            except PermissionError:
                return False

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
        return {"mean": round(self.df[column].mean(), 3),
                "median": round(self.df[column].median(), 3),
                "sd": round(self.df[column].std(), 3),
                "type": self.df[column].dtypes,
                "min": self.df[column].min(),
                "max": self.df[column].max(),
                "var": round(self.df[column].var(), 3)}

    def find_game_data(self, name_of_the_game):
        """Send datas of the game to controller"""
        return self.df[self.df['Title'] == name_of_the_game].iloc[0].to_dict()

    @staticmethod
    def pull_image(img_name):
        """sent image to controller"""
        img = Image.open(f"img/{img_name}.png")
        return img

    def create_figure(self, master, x, y) -> FigureCanvasTkAgg:
        """Create a graph from x and y that user select for UserGraph class"""
        # plot the data
        figure = Figure(figsize=(4, 4))
        ax = figure.add_subplot(111)

        if x == "empty_x" and y == "empty_y":
            empty_df = pd.DataFrame()
            empty_df[x], empty_df[y] = [], []
            sns.scatterplot(x=x, y=y, data=empty_df, ax=ax)
        else:
            sns.scatterplot(x=x, y=y, data=self.df, ax=ax)

        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"Relationship between {x} and {y}")

        canvas = FigureCanvasTkAgg(figure, master=master)
        return canvas
