from view import View
from model import Model
from controller import Controller


if __name__ == "__main__":
    modeler = Model()
    viewer = View()
    controller = Controller(modeler, viewer)
    controller.start_program()
