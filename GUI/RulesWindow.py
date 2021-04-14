from PyQt5.QtWidgets import QMainWindow

from InitWindows import MainWindow
from InitWindows.RulesWindowUI import Ui_RulesWindow


class RulesWindow(QMainWindow, Ui_RulesWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(MainWindow.go_to_menu)
