from PIL import Image
import customtkinter as tk


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
        self.menu = {"login": Login, "game": GameData, "stat": StatisticData,
                     "forum": Forum, "credit": Credit}
        self.current_menu = Login(self.app)
        self.current_menu.grid(sticky="nsew")
        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1)

    def switch_menu(self, menu_name):
        """This method use for switching menu"""
        pass

    def main_loop(self):
        self.app.mainloop()


class Login(tk.CTkFrame):
    """class for sign in/sign up menu"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.font = ("Arial", 16)

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
        user_label = tk.CTkLabel(self.__data_frame, text="Username", font=self.font)
        user_label.grid(row=0, column=0, sticky="sw", padx=15)
        user_entry = tk.CTkEntry(self.__data_frame, placeholder_text="Type your username....", font=self.font,
                                 width=200)
        user_entry.grid(row=1, column=0, sticky="new", padx=15, columnspan=3)

        # Password Label and Entry
        pass_label = tk.CTkLabel(self.__data_frame, text="Password", font=self.font)
        pass_label.grid(row=1, column=0, sticky="sw", padx=15)
        pass_entry = tk.CTkEntry(self.__data_frame, placeholder_text="Type your password....", font=self.font,
                                 width=200)
        pass_entry.grid(row=2, column=0, sticky="new", padx=15, columnspan=3)

        # Signup and Sign in Button
        signup_button = tk.CTkButton(self.__data_frame, text="Sign Up", height=30)
        signup_button.grid(row=3, column=0, sticky="n")
        login_button = tk.CTkButton(self.__data_frame, text="Sign In", height=30)
        login_button.grid(row=3, column=1, sticky="n")

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
    pass


class StatisticData(tk.CTkFrame):
    """class for Statistic Data menu"""
    pass


class Forum(tk.CTkFrame):
    """class for Forum menu"""
    pass


class Credit(tk.CTkFrame):
    """class for About us menu"""
    pass


if __name__ == "__main__":
    app = View()
    app.main_loop()
