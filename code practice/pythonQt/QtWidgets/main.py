import sys

from PySide6.QtWidgets import QApplication
from widgetgallery import WidgetGallery

if __name__== '__main__':
    app= QApplication()
    gallery= WidgetGallery()
    
    gallery.show()
    sys.exit(app.exec())