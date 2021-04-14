from PyQt5.QtWidgets import QMainWindow

from InitWindows import MainWindow
from Logic import Variables
from InitWindows.ParamsWindowUI import Ui_ParamsWindow


class ParamsWindow(QMainWindow, Ui_ParamsWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.label_number_colours.setText(str(Variables.number_of_colours))
        self.label_field_size.setText(str(Variables.field_size) + "x" + str(Variables.field_size))
        self.slider_size_field.setValue(Variables.field_size)
        self.slider_number_colours.setValue(Variables.number_of_colours)
        self.pushButton.clicked.connect(MainWindow.go_to_menu)
        self.slider_size_field.valueChanged.connect(self.change_field_size)
        self.slider_number_colours.valueChanged.connect(self.change_number_of_colours)

    def change_field_size(self):
        self.label_field_size.setText(str(self.slider_size_field.value()) + "x" + str(self.slider_size_field.value()))
        Variables.field_size = int(self.slider_size_field.value())

    def change_number_of_colours(self):
        self.label_number_colours.setText(str(self.slider_number_colours.value()))
        Variables.number_of_colours = int(self.slider_number_colours.value())
