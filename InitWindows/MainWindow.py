from PyQt5.QtWidgets import QMainWindow

from Logic import Variables
from GUI.GameWindow import GameWindow
from InitWindows.MainWindowUI import Ui_MainWindow
from GUI.ParamsWindow import ParamsWindow
from GUI.RulesWindow import RulesWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.rulesButton.clicked.connect(self.__go_to_rules)
        self.parametersButton.clicked.connect(self.__go_to_params)
        self.playButton.clicked.connect(self.__go_to_game)

    def __go_to_rules(self):
        del Variables.mw
        Variables.mw = RulesWindow()
        Variables.mw.show()

    def __go_to_params(self):
        del Variables.mw
        Variables.mw = ParamsWindow()
        Variables.mw.show()

    def __go_to_game(self):
        del Variables.mw
        Variables.mw = GameWindow()
        Variables.mw.show()


def go_to_menu():
    del Variables.mw
    Variables.mw = MainWindow()
    Variables.mw.show()
