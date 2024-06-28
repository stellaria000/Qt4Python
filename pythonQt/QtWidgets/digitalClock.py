import sys

from PySide6.QtCore import QTime, Slot, QTimer
from PySide6.QtWidgets import QLCDNumber, QApplication

# THE DIGITAL CLOCK EXAMPLE SHOWS HOW TO USE QLCDNumber TO DISPLAY A NUMBER WITH LCD-LIKE DIGITS.

class DigitalClock(QLCDNumber):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.setSegmentStyle(QLCDNumber.Filled)
        self.setDigitCount(8)

        self.timer= QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.show_time()

        self.setWindowTitle("Digital Clock")
        self.resize(250, 60)

    @Slot()
    def show_time(self):
        time= QTime.currentTime()
        text= time.toString("hh:mm:ss")

        # BLINKING EFFECT
        if (time.second()% 2)== 0: text= text.replace(":", " ")

        self.display(text)

if __name__== "__main__":
    app= QApplication(sys.argv)
    clock= DigitalClock()
    clock.show()
    sys.exit(app.exec())