import customtkinter as tk


class Controller:
    """MVC Controller"""

    def __init__(self, model=None, view=None):
        self.model = model
        self.view = view
        self.menu = {"login": LoginController, "game": GameController, "stat": StatController,
                     "forum": ForumController, "credit": CreditController}

    def start_program(self):
        """Start the Program"""
        self.view.switch_menu("login", LoginController(self.view, self.model))
        self.view.main_loop()

    def menu_button(self, menu_name, event):
        """method for bind menu button"""
        self.view.switch_menu(menu_name, self.menu[menu_name](self.view, self.model))

    def menu_title_button(self):
        """method for bind menu button"""
        self.view.switch_menu("menu", self)


class LoginController(Controller):
    """Controller class for login class"""

    def __init__(self, view, model):
        super().__init__()
        self.view = view
        self.model = model

    def signin(self, event):
        """This method use for login button in Login class"""
        self.view.switch_menu("game", GameController(self.view, self.model))
        self.view.menu_open.configure(command=self.menu_title_button)

    def signup(self, event):
        """This method use for signup button in Login class"""
        print("UwU")


class GameController:
    """Controller class for game data class"""

    def __init__(self, view, model):
        self.view = view
        self.model = model


class StatController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def story_telling(self, event):
        """This method use for login button in Login class"""
        self.view.switch_menu("story", StatController(self.view, self.model))

    def distribution(self, event):
        """This method use for login button in Login class"""
        self.view.switch_menu("distribute", StatController(self.view, self.model))

    def back_button(self, event):
        """This method use in StoryTelling and UserGraph class
           The function of this method is return to Statistic menu
           to chose which statistic menu user want to go again
        """
        self.view.switch_menu("stat", StatController(self.view, self.model))

    def user_select_graph(self, master, x, y):
        user_graph = self.model.create_figure(master, x, y)
        user_graph.get_tk_widget().grid(row=4, column=3, sticky="e", columnspan=1)

    def story_graph(self, which):
        img = tk.CTkImage(light_image=self.model.pull_image(which), size=(300, 300))
        self.view.current_menu.graph.configure(image=img)


class ForumController:
    def __init__(self, view, model):
        self.view = view
        self.model = model


class CreditController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
