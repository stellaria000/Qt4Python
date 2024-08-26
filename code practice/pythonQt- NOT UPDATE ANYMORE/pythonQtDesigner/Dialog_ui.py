# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_uiHYBKfJ.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1108, 875)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 210, 601, 151))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(249, 469, 601, 211))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(250, 400, 601, 22))

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(Dialog.slot_1st)
        self.pushButton_2.clicked.connect(Dialog.slot_2nd)
        self.pushButton.clicked.connect(Dialog.slot_3rd)
        self.lineEdit.textChanged.connect(self.label.setText)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\uc5ec\uae30\uc5d0 \ucd9c\ub825\ub429\ub2c8\ub2e4.", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\uccab\ubc88\uc9f8 \ubc84\ud2bc", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\ub450\ubc88\uc9f8 \ubc84\ud2bc", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\uc138\ubc88\uc9f8 \ubc84\ud2bc", None))
    # retranslateUi

