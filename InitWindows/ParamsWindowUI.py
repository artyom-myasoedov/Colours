# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParamsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Logic import Variables
from Colours import Colours
from Logic.Node import Node


class Ui_ParamsWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 460, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.slider_number_colours = QtWidgets.QSlider(self.centralwidget)
        self.slider_number_colours.setGeometry(QtCore.QRect(260, 190, 160, 22))
        self.slider_number_colours.setMinimum(2)
        self.slider_number_colours.setMaximum(9)
        self.slider_number_colours.setPageStep(1)
        self.slider_number_colours.setOrientation(QtCore.Qt.Horizontal)
        self.slider_number_colours.setObjectName("slider_number_colours")
        self.slider_size_field = QtWidgets.QSlider(self.centralwidget)
        self.slider_size_field.setGeometry(QtCore.QRect(260, 260, 160, 22))
        self.slider_size_field.setMinimum(2)
        self.slider_size_field.setMaximum(18)
        self.slider_size_field.setPageStep(1)
        self.slider_size_field.setOrientation(QtCore.Qt.Horizontal)
        self.slider_size_field.setObjectName("slider_size_field")
        self.label_number_colours = QtWidgets.QLabel(self.centralwidget)
        self.label_number_colours.setGeometry(QtCore.QRect(490, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_number_colours.setFont(font)
        self.label_number_colours.setObjectName("label_number_colours")
        self.label_field_size = QtWidgets.QLabel(self.centralwidget)
        self.label_field_size.setGeometry(QtCore.QRect(490, 260, 63, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_field_size.setFont(font)
        self.label_field_size.setObjectName("label_field_size")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????????????"))
        self.label.setText(_translate("MainWindow", "??????????????????"))
        self.pushButton.setText(_translate("MainWindow", "????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????????? ????????????:"))
        self.label_3.setText(_translate("MainWindow", "???????????? ????????:"))
        self.label_number_colours.setText(_translate("MainWindow", "2"))
        self.label_field_size.setText(_translate("MainWindow", "2x2"))


if __name__ == "__main__":
    # game = Logic(2, 2)
    # game.test_field()
    # print(game.field)
    # print(game.active_nodes)
    # game.make_turn(Colours(1))
    # print(game.field)
    # print(game.active_nodes)
    # print(str(game.is_win))
    node = Node(Colours.red, 0, 0)
    print(Variables.colours[node.colour])
