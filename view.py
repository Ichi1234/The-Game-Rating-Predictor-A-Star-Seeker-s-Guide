from PIL import Image
from controller import Controller
import customtkinter as tk

FONT = ("Arial", 16)
FRAME_COLOR = "#202020"


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
        self.controller = None
        self.menu = {"login": Login, "game": GameData, "stat": StatisticData,
                     "forum": Forum, "credit": Credit, "menu": MenuBar}

        self.current_menu = None
        self.menu_open = None
        self.title_label = None

        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1, minsize=70)

    def switch_menu(self, menu_name, controller=None):
        """This method use for switching menu"""

        if menu_name not in ["login"] and not self.menu_open:
            self.menu_title_creation()

        elif menu_name == "menu" and not self.controller:
            self.controller = controller

        self.current_menu = self.menu[menu_name](self.app, controller)

        # if it login menu it will grid at the top elif it will grid at 1 because of menu_bar
        if isinstance(self.current_menu, Login):
            self.current_menu.grid(row=0, sticky="news", rowspan=2)
        else:
            self.app.rowconfigure(1, weight=2, minsize=500)
            self.current_menu.grid(row=1, sticky="news", rowspan=2)
            self.title_label.configure(text=self.current_menu.title)

    def menu_title_creation(self):
        # TODO try to acess menu_open from Frame (menu_label
        menu_label = tk.CTkFrame(master=self.app, fg_color="dark blue")
        menu_label.grid(row=0, sticky="news")

        self.menu_open = tk.CTkButton(menu_label, text="Menu", fg_color="dark blue", font=("Arial", 16))
        self.menu_open.pack(side="left", expand=True)

        self.title_label = tk.CTkLabel(menu_label, text="Game Data", fg_color="dark blue", font=("Arial", 16))
        self.title_label.pack(side="left", padx=220, pady=3, expand=True)

        checkbox = tk.CTkSwitch(master=menu_label, text="Light Mode", font=("Arial", 16))
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
        self.configure(fg_color=FRAME_COLOR)  # TODO light mode - dark mode
        self.title = "Game Data"

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

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Statistic Data"
        self.configure(fg_color=FRAME_COLOR)
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        for i in range(5):
            self.rowconfigure(i, weight=1)
        for i in range(2):
            self.columnconfigure(i, weight=1)

        # Logo
        distribute_image = tk.CTkImage(light_image=Image.open("img/dis.png"), size=(200, 200))
        storytelling_image = tk.CTkImage(light_image=Image.open("img/scat.png"), size=(200, 200))

        story_button = tk.CTkButton(self, text="", image=storytelling_image, fg_color="transparent")
        story_button.grid(row=2, column=0)

        left_label = tk.CTkLabel(self, text="Game Rating Prediction", font=('Arial', 18, 'bold'))
        left_label.grid(row=3, column=0, sticky="n")

        distribution_button = tk.CTkButton(self, text="", image=distribute_image, fg_color="transparent")
        distribution_button.grid(row=2, column=1)

        right_label = tk.CTkLabel(self, text="Distribution", font=('Arial', 18, 'bold'))
        right_label.grid(row=3, column=1, sticky="n")


class StoryTelling(tk.CTkFrame):
    """This class is use for Data story telling"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Game Rating Prediction"
        self.configure(fg_color=FRAME_COLOR)
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        select_graph = tk.CTkComboBox(self)
        graph = tk.CTkLabel(self, text="this is graph")
        back_button = tk.CTkButton(self, text="Back")

        select_graph.pack(pady=50, expand=True)
        graph.pack(pady=50, expand=True)
        back_button.pack(pady=55, expand=True)


class Forum(tk.CTkFrame):
    """class for Forum menu"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Forum"
        self.configure(fg_color=FRAME_COLOR)
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        pass


class Credit(tk.CTkFrame):
    """class for About us menu"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(fg_color=FRAME_COLOR)
        self.title = "About us"
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        pass


class MenuBar(tk.CTkFrame):
    """this class is for menu select screen"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Menu"
        self.configure(fg_color=FRAME_COLOR)
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        self.columnconfigure((0, 1, 2, 3), weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1)

        haha = tk.CTkLabel(self, text="This button screen is for testing I will make real button screen after finished "
                                      "everything", font=FONT)
        haha.grid(column=2, row=0)
        game_button = tk.CTkButton(self, text="Game Data")
        game_button.grid(column=1, row=1)

        stat_button = tk.CTkButton(self, text="Statistic Data")
        stat_button.grid(column=2, row=2)

        forum_button = tk.CTkButton(self, text="Forum")
        forum_button.grid(column=1, row=2)

        credit_button = tk.CTkButton(self, text="About Us")
        credit_button.grid(column=2, row=1)

        # Bind Button
        game_button.bind("<Button-1>", lambda event: self.controller.menu_button("game", event))
        stat_button.bind("<Button-1>", lambda event: self.controller.menu_button("stat", event))
        forum_button.bind("<Button-1>", lambda event: self.controller.menu_button("forum", event))
        credit_button.bind("<Button-1>", lambda event: self.controller.menu_button("credit", event))


if __name__ == "__main__":
    app = View("a")
    app.switch_menu("menu")
    app.main_loop()
