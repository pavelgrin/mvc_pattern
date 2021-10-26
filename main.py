import sys

from app.model import Model
from app.controller import Controller
from app.view import View


def main():
    model = Model()
    controller = Controller(model)

    View(model, controller)


if __name__ == '__main__':
    sys.exit(main())
