#coding: utf- 8
import sys

import uic
from PySide6 import QtWidgets


class Form(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)

        self.ui= uic.loadUi("Dialog_ui.ui", self)
        self.ui.show()

    def slot_1st(self):
        self.ui.label.setText("첫 번째 버튼")

    def slot_2nd(self):
        self.ui.label.setText("두 번째 버튼")

    def slot_3rd(self):
        self.ui.label.setText("세 번째 버튼")

if __name__== '__main__':
    app= QtWidgets.QApplication(sys.argv)
    w= Form()

    sys.exit(app.exec())


'''
    Signal과 Slot은 위젯끼리 통신을 하는 용도로 사용할 수 있습니다. 어떠한 이벤트가 일어났을 때
    그것을 다른 오브젝트에게 알려주고 값을 전달하거나 받을 수 있도록 해줍니다. 콜백 함수 등을 이용ㅎ하는
    다른 GUI 프레임웍과 비교도히는 통신 방법
    
    Qobject를 상속받은 모든 위젯은 Signal과 Slot을 가질 수 있다.
'''