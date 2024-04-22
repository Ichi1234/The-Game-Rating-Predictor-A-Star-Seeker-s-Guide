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
        self.menu = {"game": GameData, "stat": StatisticData,
                     "forum": Forum, "credit": Credit}

    def switch_menu(self, menu_name):
        """This method use for switching menu"""
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
