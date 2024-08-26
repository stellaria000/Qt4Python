import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication

form_class= uic.loadUiType("QLineEdit_ui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def lineEditTxtFnc(self):
        self.Ledt.setText(self.ledt.text())

    def printTxtFnc(self):
        # self. line edit name. text()
        # Line edit에 있는 글자를 가져오는 메소드
        print(self.ledt.text())

    def changeTxtFnc(self):
        # self. line edit name. setText()
        # Line Edit의 글자를 바꾸는 메소드
        self.ledt.setText("CHANGE TEXT")

if __name__== "__main__":
    app= QApplication(sys.argv)
    myWindow= WindowClass()
    myWindow.show()
    app.exec_()
