# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form - untitledhNIkpA.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1108, 856)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 40, 851, 741))
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 30, 321, 691))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 50, 91, 41))
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 180, 91, 41))
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 600, 91, 41))
        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(110, 460, 91, 41))
        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(110, 320, 91, 41))
        self.webEngineView = QWebEngineView(self.widget)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(390, 80, 431, 571))
        self.webEngineView.setUrl(QUrl(u"about:blank"))
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(360, 0, 20, 741))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(Form)
        self.pushButton.pressed.connect(self.webEngineView.show)
        self.pushButton_2.pressed.connect(self.webEngineView.show)
        self.pushButton_3.pressed.connect(self.webEngineView.show)
        self.pushButton_4.pressed.connect(self.webEngineView.show)
        self.pushButton_5.pressed.connect(self.webEngineView.show)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"google", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"naver", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"daum", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"bing", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"zum", None))
    # retranslateUi

