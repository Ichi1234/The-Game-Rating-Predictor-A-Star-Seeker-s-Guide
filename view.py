"""This module is MVC view class it is use for show GUI to user"""
from PIL import Image
import customtkinter as tk

FONT = ("Arial", 16)
FRAME_COLOR = ("white", "#202020")


class App(tk.CTk):
    """This class use for initialize the program"""

    def __init__(self):
        super().__init__()
        self.title("The Game Rating Predictor: A Star Seeker's Guide")
        self.geometry("800x500")
        tk.set_appearance_mode("dark")

    def closing_the_program(self):
        """When user click at X symbol on the top left destroy everything
        or click at exit button
        """
        self.tk.quit()


class View:
    """This class is responsible for presenting the data to the user."""

    def __init__(self):
        """Initialize of View class"""
        self.app = App()

        self.app.protocol("WM_DELETE_WINDOW", self.app.closing_the_program())
        self.controller = None
        self.menu = {"login": Login, "game": GameData, "stat": StatisticData,
                     "forum": Forum, "credit": Credit, "up": SignUp, "UserForum": SelectedForum,
                     "story": StoryTelling, "distribute": UserGraph, "statistic": StatisticMenu}
        self.forum_data = {}

        self.current_menu = None
        self.menu_button = None
        self.menu_window = None
        self.title_label = None
        self.dark_mode = None

        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1, minsize=70)

    def switch_menu(self, menu_name, controller=None):
        """This method use for switching menu"""

        # Fix Memory Management My code not working because I'm not delete old widget
        if self.current_menu is not None:
            self.current_menu.destroy()

        if menu_name not in ["login"] and not self.menu_button:
            self.menu_title_creation()

        # send the forum data if it SelectedForum class
        if menu_name == "UserForum":
            self.current_menu = self.menu[menu_name](self.app, controller, self.forum_data)
        else:
            self.current_menu = self.menu[menu_name](self.app, controller)

        # if it login menu it will grid at the top elif it will grid at 1 because of menu_bar
        if isinstance(self.current_menu, Login):
            self.current_menu.grid(row=0, column=0, sticky="news", rowspan=2)
        else:
            self.app.rowconfigure(1, weight=2, minsize=500)
            self.current_menu.grid(row=1, column=0, sticky="news", rowspan=2)
            self.title_label.configure(text=self.current_menu.title)
            if self.controller:
                self.dark_mode.configure(command=self.controller.dark_mode)

    def menu_title_creation(self):
        """Create menu label at the top"""
        menu_label = tk.CTkFrame(master=self.app, fg_color="dark blue")
        menu_label.grid(row=0, column=0, sticky="news", columnspan=10)

        self.menu_button = tk.CTkButton(menu_label, text="Menu", fg_color="transparent", font=FONT)
        self.menu_button.pack(side="left", expand=True)

        self.title_label = tk.CTkLabel(menu_label, text="Game Data",
                                       fg_color="transparent", font=FONT, text_color="white")
        self.title_label.pack(side="left", padx=100, pady=3, expand=True)

        self.dark_mode = tk.CTkSwitch(master=menu_label, text="Dark Mode",
                                      font=FONT, text_color="white")
        self.dark_mode.select()
        self.dark_mode.pack(side="left", expand=True)

        exit_button = tk.CTkButton(menu_label, text="Exit", font=FONT,
                                   command=self.app.closing_the_program, fg_color="transparent")
        exit_button.pack(side="left", expand=True)

    def menu_window_creation(self):
        """When user click at menu. Menu window will pop up on the left side"""
        button_option = {'font': ('Arial', 13), 'fg_color': "transparent",
                         'text_color': ("black", "white")}
        option = {'pady': 20, 'fill': "both", 'expand': True}

        self.menu_window = tk.CTkFrame(self.app, fg_color=("#e8e8e8", "#252525"))

        game_button = tk.CTkButton(self.menu_window, text="Game Data", **button_option)
        game_button.pack(**option)

        stat_button = tk.CTkButton(self.menu_window, text="Statistic Data", **button_option)
        stat_button.pack(**option)

        forum_button = tk.CTkButton(self.menu_window, text="Forum", **button_option)
        forum_button.pack(**option)

        credit_button = tk.CTkButton(self.menu_window, text="About Us", **button_option)
        credit_button.pack(**option)

        self.menu_window.grid(row=1, column=0, rowspan=10, sticky="new")
        # Bind Button
        game_button.bind("<Button-1>", lambda event: self.controller.menu_button("game"))
        stat_button.bind("<Button-1>", lambda event: self.controller.menu_button("stat"))
        forum_button.bind("<Button-1>", lambda event: self.controller.menu_button("forum",))
        credit_button.bind("<Button-1>", lambda event: self.controller.menu_button("credit"))

    def main_loop(self):
        """Loop of the program"""
        self.app.mainloop()


class Login(tk.CTkFrame):
    """class for sign in/sign up menu"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.app = master
        self.controller = controller

        self.__left_frame = tk.CTkFrame(master=self, fg_color="#031b70")
        self.announce = tk.CTkScrollableFrame(master=self.__left_frame, orientation="horizontal")
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
        user_entry = tk.CTkEntry(self.__data_frame, font=FONT, width=200
                                 , placeholder_text="Type your username....")
        user_entry.grid(row=1, column=0, sticky="new", padx=15, columnspan=3)

        # Password Label and Entry
        pass_label = tk.CTkLabel(self.__data_frame, text="Password", font=FONT)
        pass_label.grid(row=1, column=0, sticky="sw", padx=15)
        pass_entry = tk.CTkEntry(self.__data_frame, font=FONT, width=200
                                 , placeholder_text="Type your password....")
        pass_entry.grid(row=2, column=0, sticky="new", padx=15, columnspan=3)

        # Signup and Sign in Button
        signup_button = tk.CTkButton(self.__data_frame, text="Sign Up", height=30)
        login_button = tk.CTkButton(self.__data_frame, text="Sign In", height=30)
        signup_button.grid(row=3, column=0, sticky="n")
        login_button.grid(row=3, column=1, sticky="n")

        # Bind Button
        signup_button.bind("<Button-1>",
                           lambda event=None: self.controller.signup(self.app))
        login_button.bind("<Button-1>",
                          lambda event=None: self.controller.signin(user_entry.get(),
                                                                    pass_entry.get()))
        # Left Frame grid and configure
        self.__left_frame.grid(row=0, column=0, sticky="news")
        self.__left_frame.columnconfigure(0, weight=1)
        self.__left_frame.rowconfigure(0, weight=1)

        # Announcement grid
        self.announce.grid(row=0, column=0, sticky="news", padx=50, pady=50, rowspan=4)

        # Data Frame grid and configure
        self.__data_frame.grid(row=0, column=1, sticky="news", columnspan=2, rowspan=4)

        for col_index in range(2):
            self.__data_frame.columnconfigure(col_index, weight=1)

        for row_index in range(4):
            self.__data_frame.rowconfigure(row_index, weight=1)
        self.__data_frame.rowconfigure(4, weight=2)

    def announcement_text(self) -> None:
        """This method use for insert text to announce"""
        frame = tk.CTkFrame(self.announce)
        title = tk.CTkLabel(frame, text="Announcement", font=("Arial", 20))
        frame.columnconfigure(0, weight=1)
        title.grid(row=0, column=0, sticky="w")
        frame.pack()

        tk.CTkLabel(self.announce,
                    text="If you are a new user you should Sign up first.\n"
                         " But, if you don't want to Sign Up you can "
                         "use \n\nUsername: Guest \nPassword: Guest \n\n"
                         "to sign in.\n However, if you use a Guest ID "
                         "you can't"
                         "comment or create a new forum.").pack()


class SignUp(tk.CTkToplevel):
    """When user click sign up button user will lead to this class"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.app = master
        self.controller = controller
        self.title("Sign Up")
        self.geometry("600x400")
        self.attributes("-topmost", True)
        self.resizable(False, False)

        self.user_name = tk.StringVar()
        self.password = tk.StringVar()

        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        sign_up_frame = tk.CTkFrame(self, fg_color="#808080")
        sign_up_frame.pack(expand=True, fill="both")

        # Username Label and Entry
        user_label = tk.CTkLabel(sign_up_frame, text="New Username", font=FONT)
        user_label.grid(row=0, column=0, sticky="sw", padx=15)
        user_entry = tk.CTkEntry(sign_up_frame, font=FONT,
                                 width=200, textvariable=self.user_name)
        user_entry.grid(row=1, column=0, sticky="new", padx=15, columnspan=10)

        # Password Label and Entry
        pass_label = tk.CTkLabel(sign_up_frame, text="New Password", font=FONT)
        pass_label.grid(row=1, column=0, sticky="sw", padx=15)
        pass_entry = tk.CTkEntry(sign_up_frame, font=FONT,
                                 width=200, textvariable=self.password)
        pass_entry.grid(row=2, column=0, sticky="new", padx=15, columnspan=10)

        signup_button = tk.CTkButton(sign_up_frame, text="Sign Up", height=30)
        signup_button.grid(row=2, column=2, sticky="s")

        # Bind Button
        signup_button.bind("<Button-1>",
                           lambda event=None:
                           self.controller.add_new_people(user_entry.get(),
                                                          pass_entry.get()))

        for i in range(4):
            sign_up_frame.rowconfigure(i, weight=1)
            sign_up_frame.columnconfigure(i, weight=1)
        sign_up_frame.columnconfigure(5, weight=3)


class GameData(tk.CTkFrame):
    """class for Game Data menu"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(fg_color=FRAME_COLOR)
        self.title = "Game Data"
        self.controller = controller

        # Frame
        self.data_frame = tk.CTkFrame(master=self, fg_color=("#a5a5a5", "#2d2d2d"))

        # Database of the game
        self.game_title = tk.CTkLabel(self, text="Please selects the game", font=("Arial", 22))
        self.summary = tk.CTkLabel(self, text="", font=("Arial", 13))
        self.player = tk.CTkLabel(self.data_frame, text="Totals Players: None", font=FONT)
        self.rating = tk.CTkLabel(self.data_frame, text="Rating: None", font=FONT)
        self.genres = tk.CTkLabel(self.data_frame, text="Genres: None", font=FONT)
        self.platform = tk.CTkLabel(self.data_frame, text="Platforms: None", font=FONT)

        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        self.columnconfigure(0, weight=1, minsize=20)
        for i in range(4):
            self.columnconfigure(i + 1, weight=1)
        self.columnconfigure(5, weight=1, minsize=20)

        for i in range(4):
            self.rowconfigure(i, weight=1)

        self.rowconfigure(4, weight=1, minsize=40)

        search_label = tk.CTkLabel(self, text="Find Game by Title", font=("Arial", 22))
        search_label.grid(row=0, column=1, sticky="ws", pady=20)

        # The title of summary part.
        summary_label = tk.CTkLabel(self, text="Description of The game", font=("Arial", 22))
        summary_label.grid(row=2, column=1, sticky="nw")

        # Use for search the game
        search_box = tk.CTkComboBox(self, values=self.controller.get_game_title(),
                                    command=lambda event=None: self.controller
                                    .get_data_of_the_game(search_box.get()))

        search_box.grid(row=1, column=1, sticky="new")

        # grid at main
        self.game_title.grid(row=0, column=3, sticky="wes", columnspan=3, pady=20)
        self.summary.grid(row=3, column=1, sticky="news", columnspan=2)
        self.data_frame.grid(row=1, column=3, sticky="news", rowspan=3, columnspan=3, padx=50)

        for i in range(5):
            self.data_frame.rowconfigure(i, weight=1)

        # Data in dataframe
        option = {"sticky": "nw", "padx": 10, "pady": 10}
        self.player.grid(row=0, column=0, **option)

        self.rating.grid(row=1, column=0, **option)

        self.genres.grid(row=2, column=0, **option)

        self.platform.grid(row=3, column=0, **option)


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
        for i in range(3):
            self.columnconfigure(i, weight=1)

        # image to use in button
        distribute_image = tk.CTkImage(light_image=Image.open("img/dis.png"), size=(200, 200))
        storytelling_image = tk.CTkImage(light_image=Image.open("img/scat.png"), size=(200, 200))

        # data story telling graph
        story_button = tk.CTkButton(self, text="", image=storytelling_image, fg_color="transparent")
        story_button.grid(row=2, column=0)

        # label for left button
        left_label = tk.CTkLabel(self, text="Game Rating Prediction", font=('Arial', 18, 'bold'))
        left_label.grid(row=3, column=0, sticky="n")

        # statistic menu use for show mean median max
        stat_button = tk.CTkButton(self, text="", image=distribute_image, fg_color="transparent")
        stat_button.grid(row=2, column=1)

        # label for middle button
        middle_label = tk.CTkLabel(self, text="Statistic", font=('Arial', 18, 'bold'))
        middle_label.grid(row=3, column=1, sticky="n")

        # distribution graph (user can create graph in this menu)
        distribution_button = tk.CTkButton(self, text="",
                                           image=distribute_image, fg_color="transparent")
        distribution_button.grid(row=2, column=2)

        # label for left button
        right_label = tk.CTkLabel(self, text="Create Your Graph", font=('Arial', 18, 'bold'))
        right_label.grid(row=3, column=2, sticky="n")

        story_button.bind("<Button-1>",
                          lambda event=None:
                          self.controller.change_statistic_menu("story"))
        stat_button.bind("<Button-1>",
                         lambda event=None:
                         self.controller.change_statistic_menu("statistic"))
        distribution_button.bind("<Button-1>",
                                 lambda event=None:
                                 self.controller.change_statistic_menu("distribute"))


class StatisticMenu(tk.CTkFrame):
    """This class is use for show statistic"""

    def __init__(self, master, controller, *args, **kwargs):
        """initialize for Statistic class"""
        super().__init__(master, *args, **kwargs)
        self.title = "Statistic"
        self.configure(fg_color=FRAME_COLOR)
        self.controller = controller
        self.database = None
        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        self.columnconfigure(0, weight=1, minsize=200)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1, minsize=200)

        for i in range(3):
            self.rowconfigure(i, weight=1)

        select_label = tk.CTkLabel(self, text="Select Attributes =", font=FONT)
        select_label.grid(row=0, column=1, sticky="w")

        select_attribute = tk.CTkComboBox(self, values=["Rating", "Plays", "Playing",
                                                        "Backlogs", "Wishlist", "Lists", "Reviews"],
                                          command=lambda event=None:
                                          self.controller.get_statistic(select_attribute.get()))

        select_attribute.grid(row=0, column=1, padx=120)

        dataframe = tk.CTkFrame(self, fg_color=("#a5a5a5", "#2d2d2d"))
        dataframe.grid(row=1, column=1, sticky="news")

        self.database = tk.CTkLabel(dataframe,
                                    text="Mean = None\nMedian = None\nS.D. = None\nMin = None"
                                         "\nMax = None\nVariance = None\nType of Data = None",
                                    font=("Arial", 25))
        self.database.pack(pady=20)

        back_button = tk.CTkButton(self, text="Back")
        back_button.grid(row=2, column=1)

        back_button.bind("<Button-1>",
                         lambda event=None:
                         self.controller.change_statistic_menu("stat"))


class StoryTelling(tk.CTkFrame):
    """This class is use for Data story telling"""

    def __init__(self, master, controller, *args, **kwargs):
        """initialize for StoryTelling class"""
        super().__init__(master, *args, **kwargs)
        self.title = "Game Rating Prediction"
        self.configure(fg_color=FRAME_COLOR)
        self.controller = controller
        self.graph = tk.CTkLabel(self, text="", image=self.controller.pull_img_model("empty"))
        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        top_frame = tk.CTkFrame(self)
        top_frame.pack(pady=10, expand=True)

        select_graph = tk.CTkComboBox(top_frame,
                                      values=["Rating and Plays", "Rating and Genres",
                                              "Avg Rating Per Decade",
                                              "Top 20 Platforms Based on Rating and Popularity"])
        select_graph.pack(side="left", expand=True)
        self.graph.pack(pady=10, expand=True)

        create_button = tk.CTkButton(top_frame, text="Create Graph")
        create_button.pack(side="left", padx=5, expand=True)
        create_button.bind("<Button-1>",
                           lambda event=None: self.controller.story_graph(select_graph.get()))

        back_button = tk.CTkButton(self, text="Back")
        back_button.pack(pady=5, expand=True)
        back_button.bind("<Button-1>",
                         lambda event=None: self.controller.change_statistic_menu("stat"))


class UserGraph(tk.CTkFrame):
    """User can create the graph that they want"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Create Your Graph"
        self.configure(fg_color=FRAME_COLOR)
        self.controller = controller

        self.frame = tk.CTkFrame(self, fg_color="transparent")

        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        for i in range(6):
            self.columnconfigure(i, weight=1)
        for i in range(5):
            self.rowconfigure(i, weight=1)

        option = {'side': 'left', 'padx': 10, 'pady': 5, 'expand': True, 'fill': 'both'}

        attribute_frame = tk.CTkFrame(self, fg_color="transparent")

        self.controller.user_select_graph(self.frame, "empty_x", "empty_y")

        label_x = tk.CTkLabel(attribute_frame, text="x:", font=FONT)
        label_x.pack(**option)

        select_x = tk.CTkComboBox(attribute_frame,
                                  values=["Rating", "Plays", "Playing",
                                          "Backlogs", "Wishlist", "Lists", "Reviews"])
        select_x.pack(**option)

        label_y = tk.CTkLabel(attribute_frame, text="y:", font=FONT)
        label_y.pack(**option)

        select_y = tk.CTkComboBox(attribute_frame,
                                  values=["Rating", "Plays", "Playing", "Backlogs",
                                          "Wishlist", "Lists", "Reviews"])
        select_y.pack(**option)

        start_button = tk.CTkButton(attribute_frame, text="Create Graph")
        start_button.pack(**option)

        back_button = tk.CTkButton(self, text="Back")
        back_button.grid(row=4, column=3, pady=10)

        attribute_frame.grid(row=0, column=3, sticky="we")
        self.frame.grid(row=2, column=3, sticky="ns")

        back_button.bind("<Button-1>",
                         lambda event=None: self.controller.change_statistic_menu("stat"))
        start_button.bind("<Button-1>",
                          lambda event=None:
                          self.controller.user_select_graph(self.frame,
                                                            select_x.get(), select_y.get()))


class Forum(tk.CTkFrame):
    """class for Forum menu"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Forum"
        self.configure(fg_color=FRAME_COLOR)
        self.controller = controller

        self.post_frame = tk.CTkScrollableFrame(self)
        self.post = []

        self.new_post_frame = tk.CTkFrame(self, fg_color="transparent")

        self.user_entry = tk.CTkEntry(self.new_post_frame, font=FONT,
                                      width=200, placeholder_text="Insert new post title....")
        self.init_components()

        self.controller.display_all_forum(self)

    def init_components(self) -> None:
        """Create components and layout the UI."""
        for i in range(3):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

        self.new_post_frame.grid(row=0, column=0, sticky="es", pady=5, columnspan=2)

        self.user_entry.pack(side="left")

        new_post = tk.CTkButton(self.new_post_frame, text="New post", corner_radius=360, height=30)
        new_post.pack(side="left", padx=10)

        self.post_frame.grid(row=1, column=1, sticky="news")

        if self.controller.is_it_guest():
            new_post.configure(state="disabled")
            self.user_entry.configure(state="disabled")
        else:
            new_post.bind("<Button-1>",
                          lambda event=None: self.controller.create_new_post(self.user_entry.get(),
                                                                             self))


class SelectedForum(tk.CTkFrame):
    """When user selected forum program will change to this class"""

    def __init__(self, master, controller, data, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Selected Forum"
        self.configure(fg_color=FRAME_COLOR)
        self.controller = controller

        self.data = data

        self.list_data = list(self.data.values())[2:]
        self.track_comment = []

        self.new_comment_text = tk.CTkEntry(self, placeholder_text="Send a message (PRESS ENTER)")
        self.frame_for_comment = tk.CTkScrollableFrame(self)

        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5, minsize=300)
        self.rowconfigure(2, weight=1)

        self.columnconfigure(0, weight=1)

        title_frame = tk.CTkFrame(self, fg_color=("white", "#343434"))
        title_frame.grid(row=0, sticky="news", column=0, pady=2)
        title_frame.columnconfigure(0, weight=1)

        if len(self.data["Title"]) > 90:
            new_title = self.controller.fix_toolong_text(self.data["Title"], 90)
        else:
            new_title = self.data["Title"]

        title = tk.CTkLabel(title_frame, text=new_title, font=("Arial", 30))
        title.grid(column=0, columnspan=10, sticky="new", pady=20)

        writer = tk.CTkLabel(title_frame, text=f"-{self.data['Name']}-", font=("Arial", 20))
        writer.grid(column=0, columnspan=10, sticky="se", padx=10)

        self.frame_for_comment.grid(row=1, column=0, sticky="news")

        user_name = []
        user_comment = []
        for i, data in enumerate(self.list_data):
            if i % 2 == 0:
                user_comment.append(data)
            else:
                user_name.append(data)

        for comment in range(len(user_name)):
            comment_frame = tk.CTkFrame(self.frame_for_comment)
            comment_frame.columnconfigure(0, weight=1)

            title_frame.columnconfigure(0, weight=1)

            if user_comment[comment] == "waiting-for-user-to-comment":
                break

            who_comment = tk.CTkLabel(comment_frame,
                                      text=f"{user_name[comment]} :", font=("Arial", 18))
            who_comment.pack(side="left", padx=10)

            if len(user_comment[comment]) > 170:
                spaced_com = self.controller.fix_toolong_text(user_comment[comment], 170)
            else:
                spaced_com = user_comment[comment]

            add_comment = tk.CTkLabel(comment_frame, text=spaced_com, font=FONT)
            add_comment.pack(side="left", padx=10)

            self.track_comment.append((user_name[comment], user_comment[comment]))
            comment_frame.pack(side="top", expand=True, anchor="w")

        if self.controller.is_it_guest():
            self.new_comment_text.configure(state="disabled")
        self.new_comment_text.grid(row=2, sticky="news", column=0, pady=5)

        # Bind Button
        self.new_comment_text.bind("<Return>",
                                   lambda event=None: self.controller.new_comment(
                                       self.new_comment_text.get(), self.data))


class Credit(tk.CTkFrame):
    """class for About us menu"""

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(fg_color=FRAME_COLOR)
        self.title = "About us"
        self.controller = controller
        self.text = tk.CTkLabel(self, text=self.controller.display_text(), font=("Arial", 20))
        self.text.pack(side="top", expand=True, fill="both")
