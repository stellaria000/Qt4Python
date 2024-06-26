from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QMainWindow, QFileDialog, QApplication)

from addresswidget import AddressWidget

class MainWindow(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)

        self._address_widget= AddressWidget()
        self.setCentralWidget(self._address_widget)
        self.create_menus()
        self.setWindowTitle("Address Book")

    def create_menus(self):
    # CREATE THE MAIN MENUBAR MENU ITEMS
        file_menu= self.menuBar().addMenu("&File")
        tool_menu= self.menuBar().addMenu("&Tools")

    # POPULATE THE FILE MENU
        self.open_action= self.create_action("&Open...", file_menu, self.open_file)
        self.save_action= self.create_actopm("&Save As...", file_menu, self.save_file)

        file_menu.addSeparator()
        self.exit_action= self.create_action("E&xit", file_menu, self.close)

    # POPULATE THE TOOLS MENU
        self.add_action= self.create_action("&Add Entry...", tool_menu, self._address_widget.add_entry)
        self._edit_action = self.create_action("&Edit Entry...", tool_menu, self._address_widget.edit_entry)
        self._remove_action = self.create_action("&Remove Entry...", tool_menu, self._address_widget.remove_entry)

    # DISABLE THE EDIT AND REMOVE MENU ITEMS INITIALLY, AS THERE ARE NO ITEMS YET.
        self._edit_action.setEnabled(False)
        self._remove_action.setEnabled(False)

    # WIRE UP THE UPDATEACTIONS SLOT
        self._address_widget.selection_changed.connect(self.update_actions)

    def create_action(self, text, menu, slot):
    # HELPER FUNCTION TO SAVE TYPING WHEN POPULATION MENUS WITH ACTION
        action= QAction(text, self)
        menu.addMenu(action)
        action.triggered.connect(slot)

        return action

    '''
        QUICK GOTCHA:
        QFiledialog.getOpenFilename AND QFileDialog.get.SaveFileName DON'T BEHAVE  IN PYSIDE6
        AS THEY DO IN QT, WHERE THEY RETURN A QString CONTAINING THE FILENAME.
        IN PYSIDE6, THESE FUNCTIONS RETURN A TUPLE: (FILENAME, FILTER)
    '''

    @Slot()
    def open_file(self):
        filename, _= QFileDialog.getOpenFileName(self)
        if filename: self._address_widget.read_from_file(filename)

    @Slot()
    def save_file(self):
        filename, _= QFileDialog.getSaveFileName(self)
        if filename: self._address_widget.write_to_file(filename)

    def update_actions(self, selection):
    # ONLY ALLOW THE USER TO REMOVE OR EDIT AN ITEM IF AN ITEM IS ACTUALLY SELECTED.
        indexes= selection.indexes()

        if len(indexes)> 0:
            self._remove_action.setEnabled(True)
            self._edit_action.setEnabled(True)
        else:
            self._remove_action.setEnabled(False)
            self._edit_action.setEnabled(False)

if __name__== "__main__":   #RUN THE APPLICATION
    import sys

    app= QApplication(sys.argv)
    mw= MainWindow()
    mw.show()

    sys.exit(app.exec())

