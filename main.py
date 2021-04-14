import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMessageBox

from Logic import Variables
from InitWindows.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    Variables.mw = MainWindow()
    Variables.mw.show()

    def exception_hook(type_, value, tb):
        msg = '\n'.join(traceback.format_exception(type_, value, tb))
        print(msg)
        QMessageBox.critical(Variables.mw, 'Unhandled top level exception', msg)

    sys.excepthook = exception_hook

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
