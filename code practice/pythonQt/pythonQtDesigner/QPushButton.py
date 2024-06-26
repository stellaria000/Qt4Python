#UI 파일 여녁ㄹ
#단 UI파일은 python 코드 파일과 같은 디렉토리에 위치해야한다.
import sys

import uic
from PySide6.QtWidgets import QApplication, QMainWindow

form_class= uic.loadUiType("QPushButton.ui")

#화면을 띄우는 데 사용되는 Class 선언
class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QPushButton.ui", self
                   )
        # self.ui= Ui_Form
        # self.setupUi(self)

        #버튼에 기능 연결
        self.btn_1.clicked.connect(self.button1Functinon)
        self.btn_2.clicked.connect(self.button2Functinon)

        #Button1이 눌리면 작동할 함수
        def button1Function(self):
            print("Button 1 clicked")

        # Button2가 눌리면 작동할 함수
        def button2Function(self):
            print("Button 2 clicked")

if __name__== "__main__":
    app= QApplication(sys.argv)
    myWindow= WindowClass()
    myWindow.show()
    app.exec_()