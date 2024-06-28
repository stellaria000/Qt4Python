"""
    THE DROP SITE EXAMPLE SHOWS HOW TO DISTINGUISH THE VARIOUS MIME FORMATS AVAILABLE IN A DRAG
    AND DROP OPERATION.
    IT ACCEPTS DROPS FROM OTHER APPLICATIONS AND DISPLAYS THE MIME FORMATS PROVIDED BY THE DRAG OBJECT.
"""
import sys

from PySide6.QtWidgets import QApplication
from dropsitewindow import DropSiteWindow

if __name__== "main":
    app= QApplication(sys.argv)
    window= DropSiteWindow()
    window.show()
    sys.exit(app.exec())