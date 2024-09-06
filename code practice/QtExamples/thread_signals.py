import sys
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class MainForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Form")
        self.resize(200, 150)
        self.layout= QVBoxLayout()
        self.button= QPushButton("Click me!")
        self.button.clicked.connect(self.start_thread)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def start_thread(self):
        instanced_thread= WorkerThread(self)
        instanced_thread.start()
    
    @Slot(str)
    def update_str_field(self, message): print(message)

    @Slot(int)
    def update_int_field(self, value): print(value)

class MySignals(QObject):
    signal_str= Signal(str)
    signal_int= Signal(int)

class WorkerThread(QThread):
    def __init__(self, parent= None):
        QThread.__init__(self, parent)

        self.signals= MySignals()
        self.signals.signal_str.connect(parent.update_str_field)
        self.signals.signal_int.connect(parent.update_int_field)

    def run(self):
        a= 1+ 1

        self.signals.signal_int.emit(a)
        self.signals.signal_str.emit("THIS TEXT COMES TO MAIN THREAD FROM OUR WORKER THREAD")

if __name__== "__main__":
    app= QApplication(sys.argv)
    window= MainForm()
    window.show()

    sys.exit(app.exec())