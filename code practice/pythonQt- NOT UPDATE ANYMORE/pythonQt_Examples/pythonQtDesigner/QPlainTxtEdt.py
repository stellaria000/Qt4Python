import sys

from PyQt6 import uic
from PySide6.QtWidgets import QMainWindow, QApplication

form_class = uic.loadUiType("PlainTxtEdt.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #PlainTextEdit과 관련된 버튼에 기능 연결
        self.btn_printPlainTextEdit.clicked.connect(self.Tlbl)
        self.btn_clearPlainTextEdit.clicked.connect(self.Ledt)
        self.btn_appendPlainText.clicked.connect(self.pbtn)

    #PlainTextEdit과 관련된 함수
    def printPlainTextEdit(self) :
        print(self.plaintextedit_Test.toPlainText())

    def clearPlainTextEdit(self) :
        self.plaintextedit_Test.clear()

    def appendPlainText(self) :
        self.plaintextedit_Test.appendPlainText("Append Plain Text")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()