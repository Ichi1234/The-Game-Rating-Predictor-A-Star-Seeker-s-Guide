
class Controller:
    """MVC Controller"""
    def __init__(self, model=None, view=None):
        self.model = model
        self.view = view
        self.menu = {"login": LoginController, "game": GameController, "stat": StatController,
                     "forum": ForumController, "credit": CreditController}

    def start_program(self):
        """Start the Program"""
        self.view.switch_menu("login", LoginController(self.view))
        self.view.main_loop()

    def menu_button(self, menu_name, event):
        """method for bind menu button"""
        self.view.switch_menu(menu_name, self.menu[menu_name](self.view))

    def menu_title_button(self, event):
        """method for bind menu button"""
        self.view.switch_menu("menu", self)


class LoginController(Controller):
    """Controller class for login class"""
    def __init__(self, view):
        super().__init__()
        self.view = view

    def signin(self, event):
        """This method use for login button in Login class"""
        self.view.switch_menu("game", GameController(self.view))

    def signup(self, event):
        """This method use for signup button in Login class"""
        print("UwU")


class GameController:
    """Controller class for game data class"""
    def __init__(self, view):
        self.view = view


class StatController:
    pass


class ForumController:
    pass


class CreditController:
    pass



