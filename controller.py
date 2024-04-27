from view import View, Login, GameData, StatisticData, Forum, Credit
from model import Model


class Controller:
    def __init__(self, model: Model):
        self.model = model
        self.view = View(self)

    def start_program(self):
        self.view.switch_menu("login")
        self.view.main_loop()

    def signin(self, event):
        """This method use for login button in Login class"""
        self.view.switch_menu("game")

    def signup(self, event):
        """This method use for signup button in Login class"""
        print("UwU")


if __name__ == "__main__":
    model = Model()
    controller = Controller(model)
    controller.start_program()
