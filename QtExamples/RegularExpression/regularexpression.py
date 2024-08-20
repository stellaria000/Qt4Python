import sys

from regularexpressiondialog import RegularExpressionDialog

from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = RegularExpressionDialog()
    dialog.show()

    sys.exit(app.exec())