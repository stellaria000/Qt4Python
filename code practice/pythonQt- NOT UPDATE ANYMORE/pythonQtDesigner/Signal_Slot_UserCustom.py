# coding: utf- 8
# 사용자 정의 시그널 만들어 사용하기

import sys

from PySide6.QtCore import QThread
# from PyQt6.QtWidgets import QWidget
# from PyQt6.QtWidgets import QTextEdit
# from PyQt6.QtWidgets import QApplication
# from PyQt6.QtWidgets import QBoxLayout
# from PyQt5.QtCore import Qt
# from PyQt5.QtCore import QThread
# from PyQt5.QtCore import pyqtSignal

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QBoxLayout, QSlider, QLabel, QWidget, QTextEdit
from PyQt6.QtCore import pyqtSignal
import time


class TicGenerator(QThread):
    # 5초마다 틱 신호를 전달
    tic = pyqtSignal(name="Tic")

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            t = int(time.time())

            if t % 5 != 0:
                time.sleep(0.1)  # CPU 사용을 줄이기 위해 더 긴 sleep 시간
                continue

            self.tic.emit()
            self.msleep(1000)


class Form(QWidget):
    def __init__(self):
        super().__init__()

        self.te = QTextEdit()
        self.tic_gen = TicGenerator()

        self.init_widget()
        self.tic_gen.start()

    def init_widget(self):
        self.setWindowTitle("Custom Signal")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)

        self.setLayout(form_lbx)

        # 시그널 슬롯 연결
        self.tic_gen.tic.connect(lambda: self.te.insertPlainText(time.strftime("[%H:%M:%S] Tic! \n")))
        form_lbx.addWidget(self.te)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()

    form.show()

    sys.exit(app.exec_())