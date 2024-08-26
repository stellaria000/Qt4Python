#coding: utf-8
# Signal Slot에서 Lambda 함수 이용하기
import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QBoxLayout, QSlider, QLabel, QWidget

'''
class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.lb= QLabel()
        self.sd= QSlider(Qt.Horizontal)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Signal Slot")

        form_lbx= QBoxLayout(QBoxLayout.TopToBottom, parent= self)
        self.setLayout(form_lbx)

        # 시그널 슬롯 연결
        # QLabel.setText는 문자엶만 받으므로 정수형을 주는 QSlider.valueCHange를 바로 사용할 수 없다.
        # 이를 해결하기 위해서는 따로 처리해 주는 함수를 만들어 줘야 하는데
        # Lambda를 이용하여 값을 넘기는 방법을 사용하면 간편하게 해결할 수 있다.
        self.sd.valueChanged.connect(lambda v: self.lb.setText(str(v)))

        form_lbx.addWidget(self.lb)
        form_lbx.addWidget(self.sd)

if __name__== "__main__":
    app= QApplication(sys.argv)
    form= Form()
    form.show()

    exit(app.exec_())
'''