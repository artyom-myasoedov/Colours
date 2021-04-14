from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox, QTableWidget, QLabel

from InitWindows import MainWindow
from Logic import Variables
from Colours import Colours
from Logic.Game import Game
from InitWindows.GameWindowUI import Ui_GameWindow


class GameWindow(QMainWindow, Ui_GameWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.menu_button.clicked.connect(MainWindow.go_to_menu)
        self.game = Game(Variables.field_size, Variables.number_of_colours)
        self.colour_buttons = []
        self.restart_button.clicked.connect(self.restart)
        self.__init_buttons()
        self.__init_field()
        self.optimal_label = QLabel(self)
        self.optimal_label.setGeometry(20, 180, 200, 80)
        self.optimal_label.setText('Оптимальное кол-\nво ходов = ' + str(self.game.optimal_turns_number))
        self.optimal_label.setFont(QFont("Times", 12))
        self.optimal_label.show()

    def __init_buttons(self):
        for i in range(0, Variables.number_of_colours):
            self.colour_buttons.append(self.__create_colour_button(i))

    def __init_field(self):
        cell_size = float(800 / self.game.field_size)
        self.field = QTableWidget(self.field_widget)
        self.field.setGeometry(0, 0, 800, 800)
        self.field.verticalHeader().setVisible(False)
        self.field.horizontalHeader().setVisible(False)
        self.field.setColumnCount(self.game.field_size)
        self.field.setRowCount(self.game.field_size)
        self.field.horizontalHeader().setDefaultSectionSize(cell_size)
        self.field.verticalHeader().setDefaultSectionSize(cell_size)
        for x in range(0, self.game.field_size):
            for y in range(0, self.game.field_size):
                self.field.setCellWidget(x, y, self.__create_label())
        self.field.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.start_draw()
        self.redraw()

    def __create_colour_button(self, n: int) -> QPushButton:
        btn = QPushButton(self.colours_widget)
        btn.setGeometry(25 + 100 * n, 25, 50, 50)
        btn.setStyleSheet("background: rgb(" + Variables.colours[Colours(n + 1)] + ");")
        btn.clicked.connect(self.__change_colour)
        return btn

    def __create_label(self):
        cell = QLabel(self.field)
        cell.setAlignment(Qt.AlignCenter)
        cell.setFont(QFont("Times", 50 / self.game.field_size, QFont.Bold))
        return cell

    def __change_colour(self):
        index = self.colour_buttons.index(self.sender())
        if self.game.make_turn(Colours(index + 1)):
            self.turns_label.setText(str(self.game.number_of_turns))
            self.redraw()
        if self.game.is_win:
            if self.game.optimal_turns_number < self.game.number_of_turns:
                s = "Вы выиграли!\n Не уложились в оптимальное количество ходов :("
            else:
                s = "Вы выиграли!\n Уложились в оптимальное количество ходов :)"
            QMessageBox.about(self, "Победа", s)
            MainWindow.go_to_menu()

    def restart(self):
        self.game = Game(Variables.field_size, Variables.number_of_colours)
        for x in range(self.game.field_size):
            for y in range(self.game.field_size):
                self.field.cellWidget(x, y).setText('')
        self.start_draw()
        self.redraw()

    def start_draw(self):
        for x in range(self.game.field_size):
            for y in range(self.game.field_size):
                node = self.game.field[x][y]
                self.field.cellWidget(node.x, node.y).setStyleSheet(
                    "background: rgb(" + Variables.colours[node.colour] + ");")

    def redraw(self):
        for node in self.game.active_nodes:
            self.field.cellWidget(node.x, node.y).setStyleSheet(
                "background: rgb(" + Variables.colours[node.colour] + ");")
            self.field.cellWidget(node.x, node.y).setText('<h1 style="color: rgb(255, 255, 255);">o</h1>')
