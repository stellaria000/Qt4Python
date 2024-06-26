import sys

from PyQt6.QtWidgets import QBoxLayout, QPushButton, QLabel
from PySide6.QtWidgets import QApplication, QWidget


class Form(QWidget):
    def __init__(self):
        QWidget.__init(self)

        self.cnt= 0
        self.lb= QLabel(str(self.cnt))
        self.pb= QPushButton("COUNT")
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Custom Signal")
        form_lbx= QBoxLayout(QBoxLayout.TopToBottom, parent= self)
        self.setLayout(form_lbx)

        #Connecting signal slots
        self.pb.clicked.connect(self.count)

        form_lbx.addWidget(self.lb)
        form_lbx.addWidget(self.pb)

    def count(self):
        #pyqtSlot Decorator>> 메소드를 Qt Slot으로 명시해야 한다.
        self.cnt+= 1
        self.lb.setText(str(self.cnt))

if __name__== "__main__":
    app= QApplication(sys.argv)
    form= Form()
    form.show()
    exit(app.exec_())