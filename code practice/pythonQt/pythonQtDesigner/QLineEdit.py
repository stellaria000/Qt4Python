'''
    QLineEdit
    한 줄짜리 글자를 입력받을 수 있는 입력위젯
    LineEdit의 글자가 바뀔 때마다 기능을 수행하는 시그널+ Return키가 눌렸을 때 기능을 수행하는 시그널
'''
import sys

import uic
from PySide6.QtWidgets import QMainWindow, QApplication

from QPushButton import form_class, WindowClass


# self.LineEdit이름.textChanged.connect(함수)
# self.LineEdit이름.returnPressed.connect(함수)

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        uic.loadUi("QLineEdit.ui", self)

        # 버튼에 기능 할당
        self.lineedit_Test.textChanged.connect(self.lineeditTestFunction)
        self.lineedit_Test.returnPressed.connect(self.printTextFunction)
        self.btn_changeText.clicked.connect(self.changeTextFunction)

    def lineeditTextFunction(self):
        self.lbl_textHere.setText(self.lineedit_Test.text())

    def printTextFunction(self):
        # self.lineedit이름.text()
        # Lineedit에 있는 글자를 가져오는 메소드
        print(self.lineedit_Test.text())

    def changeTextFunction(self):
        # Lineedit의 글자를 바꾸는 메소드
        self.lineedit_Test.setText("Change Text")

if __name__== "__main__":
    app= QApplication(sys.argv)
    myWindow= WindowClass()
    myWindow.show()
    app.exec()