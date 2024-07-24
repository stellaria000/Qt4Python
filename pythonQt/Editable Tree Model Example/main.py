# A PYTHON APPLICATION THAT DEMONSTRATES THE ANALOGOUS EXAMPLE IN C++ EDITABLE TREE MODEL EXAMPLE

import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())