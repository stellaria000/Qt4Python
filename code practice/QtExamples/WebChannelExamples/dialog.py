from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QDialog
from dialog import *


class Dialog(QDialog):
    send_text = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.send.clicked.connect(self.clicked)
        self.ui.input.returnPressed.connect(self._ui.send.animateClick)

    @Slot(str)
    def display_message(self, message):
        self.ui.output.appendPlainText(message)

    @Slot()
    def clicked(self):
        text = self.ui.input.text()
        if not text:
            return
        self.send_text.emit(text)
        self.display_message(f"Sent message: {text}")
        self.ui.input.clear()