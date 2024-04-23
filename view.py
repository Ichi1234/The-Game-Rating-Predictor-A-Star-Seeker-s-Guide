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
    """This is view"""

    def __init__(self):
        self.app = App()
        self.menu = {"login": Login, "game": GameData, "stat": StatisticData,
                     "forum": Forum, "credit": Credit}
        self.current_menu = Login(self.app)
        self.current_menu.grid(row=0, column=0, sticky="nsew")

    def switch_menu(self, menu_name):
        """This method use for switching menu"""
        pass

    def loop(self):
        self.app.mainloop()


class Login(tk.CTkFrame):
    """class for sign in/sign up menu"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=2)
        anoucement = tk.CTkScrollableFrame(master=self)
        anoucement.grid(row=0, column=0, sticky="news", padx=50, pady=50, rowspan=4)

    def init_components(self) -> None:
        pass


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
    app =View()
    app.loop()