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
        """Initialize for LoginController"""
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

    def get_game_title(self):
        """Get game title from model then send it to view"""
        return self.model.game_title

    def get_data_of_the_game(self, game_name):
        """Get data of the game from model"""
        data = self.model.find_game_data(game_name)


class StatController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def story_telling(self, event):
        """This method use for story button in Statistic class"""
        self.view.switch_menu("story", StatController(self.view, self.model))

    def change_statistic_menu(self, statistic_menu: str):
        """This method use for change statistic menu"""
        self.view.switch_menu(statistic_menu, StatController(self.view, self.model))

    def user_select_graph(self, master, x, y):
        user_graph = self.model.create_figure(master, x, y)
        user_graph.get_tk_widget().grid(row=4, column=3, sticky="e", columnspan=1)

    def story_graph(self, which):
        img = tk.CTkImage(light_image=self.model.pull_image(which), size=(300, 300))
        self.view.current_menu.graph.configure(image=img)

    def get_statistic(self, column: str):
        """Get statistic dict from model"""
        data = self.model.stats(column)
        self.view.current_menu.database.configure(text=f"Mean = {data['mean']}\nMedian = {data['median']}"
                                                       f"\nS.D. = {data['sd']}\nMin = {data['min']}"
                                                       f"\nMax = {data['max']}\nVariance = {data['var']}")


class ForumController:
    def __init__(self, view, model):
        self.view = view
        self.model = model


class CreditController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
