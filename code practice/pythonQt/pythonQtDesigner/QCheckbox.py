import sys

from PyQt6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication
from PyQt6 import uic



class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.chk1.stateChanged.connect(self.chkFunction)
        self.chk2.stateChanged.connect(self.chkFunction)
        self.chk3.stateChanged.connect(self.chkFunction)
        self.chk4.stateChanged.connect(self.chkFunction)

        self.grpchk1.stateChanged.connect(self.groupChkFunction)
        self.grpchk2.stateChanged.connect(self.groupChkFunction)
        self.grpchk3.stateChanged.connect(self.groupChkFunction)
        self.grpchk4.stateChanged.connect(self.groupChkFunction)

    def chkFunction(self):
        if self.chk1.isChecked():
            print("CHECKBOX 1 IS CHECKED.")
        if self.chk2.isChecked():
            print("CHECKBOX 2 IS CHECKED.")
        if self.chk3.isChecked():
            print("CHECKBOX 3 IS CHECKED.")
        if self.chk4.isChecked():
            print("CHECKBOX 4 IS CHECKED.")

    def groupChkFunction(self):
        if self.grpChk1.isChecked():
            print("CHECKBOX 1 IS CHECKED.")
        if self.grpChk2.isChecked():
            print("CHECKBOX 2 IS CHECKED.")
        if self.grpChk3.isChecked():
            print("CHECKBOX 3 IS CHECKED.")
        if self.grpChk4.isChecked():
            print("CHECKBOX 4 IS CHECKED.")

if __name__== "__main__":
    app= QApplication(sys.argv)
    myWindow= WindowClass()
    myWindow.show()
    app.exec_()

