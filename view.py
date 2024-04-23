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

        left_frame = tk.CTkFrame(master=self, fg_color="dark blue")
        left_frame.grid(row=0, column=0, sticky="news")
        left_frame.columnconfigure(0, weight=1)

        anoucement = tk.CTkScrollableFrame(master=left_frame)
        anoucement.grid(row=0, column=0, sticky="news", padx=50, pady=50, rowspan=4)

        label2 = tk.CTkLabel(anoucement, text="Announcement", font=("Arial", 16))
        label2.grid(row=0, column=0)

        data_frame = tk.CTkFrame(master=self, fg_color="#808080")
        data_frame.grid(row=0, column=1, sticky="news", columnspan=2, rowspan=4)
        data_frame.columnconfigure((0, 1), weight=1)
        data_frame.rowconfigure((0, 1, 2), weight=2)
        data_frame.rowconfigure(3, weight=1)
        data_frame.rowconfigure(4, weight=4)



        logo = tk.CTkImage(light_image=Image.open("img/logo.png"), size=(150, 150))
        logo_label = tk.CTkLabel(data_frame, image=logo, text="")
        logo_label.grid(row=0, column=0, sticky="nwe", columnspan=3)

        user_label = tk.CTkLabel(data_frame, text="Username", font=("Arial", 16))
        user_label.grid(row=0, column=0, sticky="sw", padx=15)

        user_entry = tk.CTkEntry(data_frame, placeholder_text="Type your username....", font=("Arial", 16), width=200)
        user_entry.grid(row=1, column=0, sticky="new", padx=15, columnspan=3)

        pass_label = tk.CTkLabel(data_frame, text="Password", font=("Arial", 16))
        pass_label.grid(row=1, column=0, sticky="sw", padx=15)

        pass_entry = tk.CTkEntry(data_frame, placeholder_text="Type your password....", font=("Arial", 16), width=200)
        pass_entry.grid(row=2, column=0, sticky="new", padx=15, columnspan=3)

        signup_button = tk.CTkButton(data_frame, text="Sign Up", height=30)
        signup_button.grid(row=3, column=0, sticky="n")

        login_button = tk.CTkButton(data_frame, text="Sign In", height=30)
        login_button.grid(row=3, column=1, sticky="n")
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
    app.main_loop()