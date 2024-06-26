#coding: utf- 8
import sys

import uic
from PySide6 import QtWidgets

class Form(QtWidgets.QDialog):
    def __init__(self, parent= None):
        QtWidgets.QDialog.__init>>(self, parent)
        self.ui= uic.loadUi("form.ui")
        self.ui.show()

    if __name__== '__main__':
        app= QtWidgets.QApplication(sys.argv)
        # w= Form()
        sys.exit(app.exec())