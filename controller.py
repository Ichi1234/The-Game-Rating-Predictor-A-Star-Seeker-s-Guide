from view import View, Login, GameData, StatisticData, Forum, Credit
from model import Model


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def start_program(self):
        self.view.switch_menu("login")
        self.view.main_loop()


def signin():
    pass


def signup():
    print("UwU")


if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start_program()
