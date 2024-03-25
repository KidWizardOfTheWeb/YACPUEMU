import os, sys
from views.CPUView import *
from models.CPU import *
from controllers.CPUController import *


def main():
    view = CPUView()
    controller = CPUController(view)
    view.setController(controller)
    controller.cycle()


if __name__ == '__main__':
    main()