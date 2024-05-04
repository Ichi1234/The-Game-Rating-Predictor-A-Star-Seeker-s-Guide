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

    def menu_title_button(self):
        """method for bind menu button"""
        self.view.switch_menu("menu", self)


class LoginController(Controller):  # TODO if not use inherit delete it
    """Controller class for login class"""

    def __init__(self, view):
        super().__init__()
        self.view = view

    def signin(self, event):
        """This method use for login button in Login class"""
        self.view.switch_menu("game", GameController(self.view))
        self.view.menu_open.configure(command=self.menu_title_button)

    def signup(self, event):
        """This method use for signup button in Login class"""
        print("UwU")


class GameController:
    """Controller class for game data class"""

    def __init__(self, view):
        self.view = view


class StatController:
    def __init__(self, view):
        self.view = view

    def story_telling(self, event):
        """This method use for login button in Login class"""
        self.view.switch_menu("story", StatController(self.view))

    def distribution(self, event):
        """This method use for login button in Login class"""
        self.view.switch_menu("distribute", StatController(self.view))

    def back_button(self, event):
        """This method use in StoryTelling and UserGraph class
           The function of this method is return to Statistic menu
           to chose which statistic menu user want to go again
        """
        self.view.switch_menu("stat", StatController(self.view))


class ForumController:
    def __init__(self, view):
        self.view = view


class CreditController:
    def __init__(self, view):
        self.view = view
