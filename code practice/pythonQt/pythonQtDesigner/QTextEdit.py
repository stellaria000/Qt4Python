'''
    RichText, PlainText
    Rich Text== 글자의 색상, 크기, 기울임, 굵기 등을 조절할 수 있는 텍스트
    Plain Text== 색상, 크기를 별도로 조절할 수 없고 시스템에서 지정된대로만 글자를 표시하는 것
'''
import uic
from PySide6.QtWidgets import QMainWindow

from QPushButton import form_class

class MyWidow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        uic.loadUi("QTextEdit.ui", self)


        self.fontSize= 10

        self.btn_printTextEdit.clikced.connect(self.printTextEdit)
        self.btn_clearTextEdit.clicked.connect(self.clearTextEdit)
        self.btn_setFont.clicked.connect(self.setFont)
        self.btn_setFontItalic.clicked.connect(self.fonrItalic)
        self.btn_setFontColor.clicked.connect(self.fonetColorRed)
        self.btn_fontSizeUP.clicked.connect(self.fontSizeUp)
        self.btn_fonrSizeDown.clicked.connect(self.fontSizeDown)

    def printTextEdit(self):
        print(self.texteidot_Test.toPlainText())


