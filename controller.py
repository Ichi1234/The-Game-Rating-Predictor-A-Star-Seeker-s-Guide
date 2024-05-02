from view import View, Login, GameData, StatisticData, Forum, Credit
from model import Model


class Controller:
    def __init__(self, model: Model):
        self.model = model
        self.view = View(self)
        self.menu = {"login": Login, "game": GameData, "stat": StatisticData,
                     "forum": Forum, "credit": Credit, "menu": MenuBar}

    def start_program(self):
        self.view.switch_menu("login")
        self.view.main_loop()

    def signin(self, event):
        """This method use for login button in Login class"""
        self.view.switch_menu("game")

    def signup(self, event):
        """This method use for signup button in Login class"""
        print("UwU")

class LoginController:
    pass

class GameController:
    pass

class StatController:
    pass

class ForumController:
    pass

class CreditController:
    pass
if __name__ == "__main__":
    model = Model()
    controller = Controller(model)
    controller.start_program()
