from view import View, Login, GameData, StatisticData, Forum, Credit
from model import Model


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.menu = {"login": LoginController, "game": GameController, "stat": StatController,
                     "forum": ForumController}

    def start_program(self):
        self.view.switch_menu("login", LoginController(self.view))
        self.view.main_loop()


class LoginController:
    """Controller class for login class"""
    def __init__(self, view):
        self.view = view

    def signin(self, event):
        """This method use for login button in Login class"""
        self.view.switch_menu("game", GameController(self.view))

    def signup(self, event):
        """This method use for signup button in Login class"""
        print("UwU")


class GameController:
    def __init__(self, view):
        self.view = view


class StatController:
    pass


class ForumController:
    pass


class CreditController:
    pass


if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start_program()
