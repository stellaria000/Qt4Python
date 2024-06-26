# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TxtEdt_uiTOtDNt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(702, 276)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 60, 16))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(400, 50, 271, 207))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_printTextEdit = QPushButton(self.layoutWidget)
        self.btn_printTextEdit.setObjectName(u"btn_printTextEdit")

        self.verticalLayout.addWidget(self.btn_printTextEdit)

        self.btn_clearTextEdit = QPushButton(self.layoutWidget)
        self.btn_clearTextEdit.setObjectName(u"btn_clearTextEdit")

        self.verticalLayout.addWidget(self.btn_clearTextEdit)

        self.btn_setFont = QPushButton(self.layoutWidget)
        self.btn_setFont.setObjectName(u"btn_setFont")

        self.verticalLayout.addWidget(self.btn_setFont)

        self.btn_setFontItalic = QPushButton(self.layoutWidget)
        self.btn_setFontItalic.setObjectName(u"btn_setFontItalic")

        self.verticalLayout.addWidget(self.btn_setFontItalic)

        self.btn_setFontColor = QPushButton(self.layoutWidget)
        self.btn_setFontColor.setObjectName(u"btn_setFontColor")

        self.verticalLayout.addWidget(self.btn_setFontColor)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_fontSizeUp = QPushButton(self.layoutWidget)
        self.btn_fontSizeUp.setObjectName(u"btn_fontSizeUp")

        self.horizontalLayout_2.addWidget(self.btn_fontSizeUp)

        self.btn_fontSizeDown = QPushButton(self.layoutWidget)
        self.btn_fontSizeDown.setObjectName(u"btn_fontSizeDown")

        self.horizontalLayout_2.addWidget(self.btn_fontSizeDown)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textedit_Test = QTextEdit(Dialog)
        self.textedit_Test.setObjectName(u"TxtEdt")
        self.textedit_Test.setGeometry(QRect(20, 50, 369, 211))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.TxtEdt(QCoreApplication.translate("Dialog", u"Text Edit", None))
        self.printTextEdit.setText(QCoreApplication.translate("Dialog", u"Print Text Edit", None))
        self.clearTextEdit.setText(QCoreApplication.translate("Dialog", u"Clear Text Edit", None))
        self.setFont.setText(QCoreApplication.translate("Dialog", u"Set Font", None))
        self.setFontItalic.setText(QCoreApplication.translate("Dialog", u"Set Font Italic", None))
        self.setFontColor.setText(QCoreApplication.translate("Dialog", u"Set Font Color Red", None))
        self.fontSizeUp.setText(QCoreApplication.translate("Dialog", u"Font Size Up", None))
        self.fontSizeDown.setText(QCoreApplication.translate("Dialog", u"Font Size Down", None))
        self.TxtEdt.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:600; color:#feaba5;\">This is Text Edit</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.SF NS Text'; font-size:13pt; color:#baa4ff;\">This widget support </span><span"
                        " style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:600; font-style:italic; text-decoration: underline; color:#baa4ff;\">Rich Text</span></p></body></html>", None))
    # retranslateUi

