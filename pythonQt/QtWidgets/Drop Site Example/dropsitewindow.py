import re
from PySide6.QtCore import QMimeData, Qt, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (QAbstractItemView, QPushButton,
                               QDialogButtonBox, QLabel,
                               QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)

from droparea import DropArea

DESCRIPTION= """This example accepts drags from other applications and displays the MIME types provided by the drag object."""
_WHITESPACE_PATTERN= re.compile(r"\s+")

def simplify_whitespace(s): return _WHITESPACE_PATTERN.sub(" ",s).strip()

class DropSiteWindow(QWidget):
    def __init__(self):
        super().__init__()

        drop_area= DropArea()
        abstract_label= QLabel()

        self._formats_table= QTableWidget()

        button_box= QDialogButtonBox()

        abstract_label= QLabel(DESCRIPTION)
        abstract_label.setWordWrap(True)
        abstract_label.adjustSize()

        drop_area= DropArea()
        drop_area.changed.connect(self.update_formats_table)

        self._formats_table= QTableWidget()
        self._formats_table.setColumnCount(2)
        self._formats_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._formats_table.setHorizontalHeaderLabels(["Format", "Content"])
        self._formats_table.horizontalHeader().setStretchLastSection(True)

        clear_button= QPushButton("Clear")
        self._copy_button= QPushButton("")