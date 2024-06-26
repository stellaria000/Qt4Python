import os
from pathlib import Path
import sys

from PySide6.QtCore import Property, Signal, QUrl
from PySide6.QtGui import QGuiApplication, QPen, QPainter, QColor
from PySide6.QtQml import QmlElement
from PySide6.QtQuick import QQuickPaintedItem, QQuickView

# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "Charts"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class PieChart(QQuickPaintedItem):
    nameChanged= Signal()

    def __init__(self, parent= None):
        QQuickPaintedItem.__init__(self, parent)
        self._name= u''
        self._color= QColor()
    
    def paint(self, painter):
        pen= QPen(self.color, 2)
        painter.setPen(pen)
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.drawPie(self.boundingRect().adjusted(1, 1, -1, -1), 90* 16, 290* 16)

    @Property(QColor, final= True)
    def color(self): return self._color

    @color.setter
    def color(self, value): self._color= value

    @Property(str, notify= nameChanged, final= True)
    def name(self): return self._name

    @name.setter
    def name(self, value): self._name= value

if __name__== '__main__':
    app= QGuiApplication(sys.argv)

    view= QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)

    qml_file= os.fspath(Path(__file__).resolve().parent/ 'app.qml')

    view.setSource(QUrl.fromLocalFile(qml_file))
    if view.status()== QQuickView.Error: sys.exit(-1)
    view.show()

    res= app.exec()

    '''
    DELETING THE VIEW BEFORE IT GOES OUT OF SCOPE IS REQUIRED TO MAKE SURE
    ALL CHILE QML INSTANCES ARE DESTORYED IN THE CORRECT ORDER.
    '''

    del view
    sys.exit(res)