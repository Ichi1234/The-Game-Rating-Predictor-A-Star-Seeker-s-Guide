from PIL import Image
import customtkinter as tk

FONT = ("Arial", 16)


class App(tk.CTk):
    """This class use for initialize the program"""

    def __init__(self):
        super().__init__()
        self.title("The Game Rating Predictor: A Star Seeker's Guide")
        self.geometry("800x500")
        tk.set_appearance_mode("dark")


class View:
    """This class is responsible for presenting the data to the user."""
    def __init__(self):
        self.app = App()
        # self.controller = controller
        self.menu = {"login": Login, "game": GameData, "stat": StatisticData,
                     "forum": Forum, "credit": Credit, "menu": MenuBar}

        self.current_menu = None
        self.menu_label = None
        self.menu_bar = None
        self.title_label = None

        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1)

    def switch_menu(self, menu_name, controller):
        """This method use for switching menu"""

        if menu_name not in ["login"] and not self.menu_label:
            self.menu_title_creation()

        self.current_menu = self.menu[menu_name](self.app, controller)

        # if it login menu it will grid at the top elif it will grid at 1 because of menu_bar
        if isinstance(self.current_menu, Login):
            self.current_menu.grid(row=0, sticky="news", rowspan=2)
        else:
            self.app.rowconfigure(1, weight=2, minsize=500)
            self.current_menu.grid(row=1, sticky="news", rowspan=2)

    def menu_title_creation(self):
        self.menu_label = tk.CTkFrame(master=self.app, fg_color="dark blue")
        self.menu_label.grid(row=0, sticky="news")

        menu_open = tk.CTkButton(self.menu_label, text="Menu", fg_color="dark blue", font=("Arial", 16))
        menu_open.pack(side="left", expand=True)

        self.title_label = tk.CTkLabel(self.menu_label, text="Game Data", fg_color="dark blue", font=("Arial", 16))
        self.title_label.pack(side="left", padx=220, pady=3, expand=True)

        checkbox = tk.CTkSwitch(master=self.menu_label, text="Light Mode", font=("Arial", 16))
        checkbox.pack(side="left", expand=True)

    def main_loop(self):
        """Loop"""
        self.app.mainloop()


class Login(tk.CTkFrame):
    """class for sign in/sign up menu"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.controller = controller

        self.__left_frame = tk.CTkFrame(master=self, fg_color="dark blue")
        self.__announce = tk.CTkScrollableFrame(master=self.__left_frame)
        self.__data_frame = tk.CTkFrame(master=self, fg_color="#808080")

        self.init_components()
        self.announcement_text()

    def init_components(self) -> None:
        """Create components and layout the UI."""

        # Logo
        logo = tk.CTkImage(light_image=Image.open("img/logo.png"), size=(150, 150))
        logo_label = tk.CTkLabel(self.__data_frame, image=logo, text="")
        logo_label.grid(row=0, column=0, sticky="nwe", columnspan=3)

        # Username Label and Entry
        user_label = tk.CTkLabel(self.__data_frame, text="Username", font=FONT)
        user_label.grid(row=0, column=0, sticky="sw", padx=15)
        user_entry = tk.CTkEntry(self.__data_frame, placeholder_text="Type your username....", font=FONT,
                                 width=200)
        user_entry.grid(row=1, column=0, sticky="new", padx=15, columnspan=3)

        # Password Label and Entry
        pass_label = tk.CTkLabel(self.__data_frame, text="Password", font=FONT)
        pass_label.grid(row=1, column=0, sticky="sw", padx=15)
        pass_entry = tk.CTkEntry(self.__data_frame, placeholder_text="Type your password....", font=FONT,
                                 width=200)
        pass_entry.grid(row=2, column=0, sticky="new", padx=15, columnspan=3)

        # Signup and Sign in Button
        signup_button = tk.CTkButton(self.__data_frame, text="Sign Up", height=30)
        login_button = tk.CTkButton(self.__data_frame, text="Sign In", height=30)
        signup_button.grid(row=3, column=0, sticky="n")
        login_button.grid(row=3, column=1, sticky="n")

        # Bind Button
        signup_button.bind("<Button-1>", self.controller.signup)
        login_button.bind("<Button-1>", self.controller.signin)
        # Left Frame grid and configure
        self.__left_frame.grid(row=0, column=0, sticky="news")
        self.__left_frame.columnconfigure(0, weight=1)
        self.__left_frame.rowconfigure(0, weight=1)

        # Announcement grid
        self.__announce.grid(row=0, column=0, sticky="news", padx=50, pady=50, rowspan=4)

        # Data Frame grid and configure
        self.__data_frame.grid(row=0, column=1, sticky="news", columnspan=2, rowspan=4)

        for col_index in range(2):
            self.__data_frame.columnconfigure(col_index, weight=1)

        for row_index in range(4):
            self.__data_frame.rowconfigure(row_index, weight=1)
        self.__data_frame.rowconfigure(4, weight=2)

    def announcement_text(self) -> None:
        """This method use for insert text to announce"""
        title = tk.CTkLabel(self.__announce, text="Announcement", font=("Arial", 20))
        title.grid(row=0, column=0)


class GameData(tk.CTkFrame):
    """class for Game Data menu"""
    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(fg_color="#202020")  # TODO light mode - dark mode

        # String variable for display value
        self.game_title = "Dark Souls"
        self.summary_text = "WOAHHHH THIS GAME IS SO GOOOOOD"
        self.rating = ""
        self.genre = ""
        self.platform = ""

        self.columnconfigure(0, weight=2, minsize=20)
        for i in range(4):
            self.columnconfigure(i + 1, weight=1)
        self.columnconfigure(5, weight=2, minsize=20)

        for i in range(4):
            self.rowconfigure(i, weight=1)

        self.rowconfigure(4, weight=2, minsize=40)

        self.data_frame = tk.CTkFrame(master=self, fg_color="#2d2d2d")

        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        search_label = tk.CTkLabel(self, text="Find Game by Title", font=("Arial", 22))
        search_label.grid(row=0, column=1, sticky="ws", pady=20)

        # The title of summary part.
        summary_label = tk.CTkLabel(self, text="Description of The game", font=("Arial", 22))
        summary_label.grid(row=2, column=1, sticky="nw")

        # The summary of gameplay or story
        summary = tk.CTkLabel(self, text="Description of The game", font=FONT)
        summary.grid(row=2, column=1, sticky="w")

        # Use for search the game
        search_box = tk.CTkComboBox(self)
        search_box.grid(row=1, column=1, sticky="new")

        # Title of the current game
        game_title = tk.CTkLabel(self, text=f"{self.game_title}: Datas", font=("Arial", 22))
        game_title.grid(row=0, column=3, sticky="wes", columnspan=3, pady=20)

        # Dataframe for shows values of that game
        self.data_frame.grid(row=1, column=3, sticky="news", rowspan=3, columnspan=3, padx=50)
        for i in range(5):
            self.data_frame.rowconfigure(i, weight=1)

        # Data in dataframe
        option = {"sticky": "nw", "padx": 10, "pady": 10}
        player = tk.CTkLabel(self.data_frame, text=f"Totals Players: {self.rating}", font=FONT)
        player.grid(row=0, column=0, **option)

        rating = tk.CTkLabel(self.data_frame, text=f"Rating: {self.rating}", font=FONT)
        rating.grid(row=1, column=0, **option)

        genres = tk.CTkLabel(self.data_frame, text=f"Genres: {self.genre}", font=FONT)
        genres.grid(row=2, column=0, **option)

        platform = tk.CTkLabel(self.data_frame, text=f"Platforms: {self.platform}", font=FONT)
        platform.grid(row=3, column=0, **option)


class StatisticData(tk.CTkFrame):
    """class for Statistic Data menu"""
    pass


class Forum(tk.CTkFrame):
    """class for Forum menu"""
    pass


class Credit(tk.CTkFrame):
    """class for About us menu"""
    pass


class MenuBar(tk.CTkFrame):
    """this class is for menu select screen"""
    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        self.columnconfigure((0,1,2,3), weight=1)
        self.rowconfigure((0,1,2,3), weight=1)

        game_button = tk.CTkButton(self, text="Game Data")
        game_button.grid(column=1, row=1)

        stat_button = tk.CTkButton(self, text="Statistic Data")
        stat_button.grid(column=2, row=2)

        forum_button = tk.CTkButton(self, text="Forum")
        forum_button.grid(column=1, row=2)

        credit_button = tk.CTkButton(self, text="About Us")
        credit_button.grid(column=2, row=1)



if __name__ == "__main__":
    app = View("a")
    app.switch_menu("menu")
    app.main_loop()
