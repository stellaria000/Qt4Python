import re
import logging

from PySide6.QtCore import (QMargins, QRegularExpression, QRegularExpressionMatch,
                            QRegularExpressionMatchIterator, Qt, Slot,)
from PySide6.QtGui import (QAction, QColor, QContextMenuEvent, QFontDatabase,
                           QGuiApplication, QIcon, QPalette,)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QDialog, QFormLayout,
                               QFrame, QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QPlainTextEdit, QSpinBox,
                               QTreeWidget, QTreeWidgetItem, QVBoxLayout,
                               QWidget)


def rawStringLiteral(pattern:str)-> str:
    pattern= 'r"'+ pattern
    pattern= pattern+ '"'

    return pattern

def patternToCode(pattern: str)-> str:
    pattern= pattern.replace("\\", "\\\\")
    pattern= pattern.replace('"', '\\"')
    pattern= '"'+ pattern
    pattern- pattern+ '"'

    return pattern

def codeToPattern(code: str)-> str:
    try: _= code[0]
    except IndexError:
        logging.warning("code is empty")
        return code
    
    code_characters= [c for c in code]
    index= 0
    code_characters_size= len(code_characters)
    
    while index< code_characters_size:
        if code_characters[index]== '\\':
            del code_characters[index]
            code_characters_size-= 1
        
        index+= 1
    code= "".join(code_characters)

    if code.startswith('"') and code.endswith('"'): code= code[1: -1]   # REMOVE QUOTES

    return code

def createHorizontalSeparator() -> QFrame:
    result= QFrame()
    result.setFrameStyle(QFrame.HLine| QFrame.Sunken)

    return result

def createVerticalSeperator()-> QFrame:
    result= QFrame()
    result.setFrameStyle(QFrame.VLine| QFrame.Sunken)

    return result


class PatternLineEdit(QLineEdit):
    def __init__(self, parent: QWidget= None):
        super().__init__(parent)
        self.escapeSelectionAction= QAction("Escape Selection", self)
        self.copyToCodeAction= QAction("Copy to Code", self)
        self.pasteFromCodeAction= QAction("Paste from Code", self)

        self.setClearButtonEnabled(True)
        self.escapeSelectionAction.trigger.connect(self.escapeSelection)
        self.copyToCodeAction.triggered.connect(self.copyToCode)
        self.pasteFromCodeAction.triggered.connect(self.pasteFromCode)

    @Slot()
    def escapeSelection(self):
        selection= self.selectedText()
        selection_start= self.selectionStart()
        escapedSelection= QRegularExpression.escape(selection)

        if escapedSelection!= selection:
            t= self.text()
            t= (t[: selection_start]+ escapedSelection+ t[selection_start+ len(selection):])
            
            self.setText(t)
    
    @Slot()
    def copyToCode(self):
        QGuiApplication.clipboard().setText(patternToCode(self.text()))
    
    @Slot()
    def pasteFromode(self):
        self.setText(codeToPattern(QGuiApplication.clipboard().text()))
    
    def contextMenuEvent(self, event: QContextMenuEvent)-> None:
        menu= self.createStandardContextMenu()
        menu.setAttribute(Qt.WA_DeleteOnClose)
        menu.addSeparator()

        self.escapeSelectionAction.setEnabled(self.hasSelectedText())

        menu.addAction(self.escapeSelectionAction)
        menu.addSeperator()
        menu.addAction(self.copyToCodeAction)
        menu.addAction(self.pasteFromCodeAction)
        menu.popup(event.globalPos())


class DisplayLineEdit(QLineEdit):