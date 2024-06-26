from PySide6.QtCore import (Qt, Signal)
from PySide6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout)

from adddialogwidget import AddDialogWidget

class NewAddressTab(QWidget):
    '''
        AN EXTRA TAB THAT PROMPTS THE USER TO ADD NEW CONTACTS.
        TO BE DISPLAYES ONLY WHEN THERE ARE NO CONTACTS IN THE MODEL.
    '''
    send_details= Signal(str, str)

    def __init__(self, parent= None):
        super().__init__(parent)

        description_label= QLabel("THERE ARE NO CONTACTS IN YOUR ADDRESS BOOK."
                                  "\n CLICK ADD TO ADD NEW CONTACTS.")
        add_button= QPushButton("Add")

        layout= QVBoxLayout()
        layout.addWidget(description_label)
        layout.addWidget(add_button, 0, Qt.AlignCenter)

        self.setLayout(layout)
        add_button.clicked.connect(self.add_entry)

    def add_entry(self):
        add_dialog= AddDialogWidget()

        if add_dialog.exec():
            name= add_dialog.name
            address= add_dialog.address
            self.send_details.emit(name, address)

if __name__== "__main__":
    def print_address(name, address):
        print(f"Name: {name}")
        print(f"Address: {address}")

    import sys
    from PySide6.QtWidgets import QApplication

    app= QApplication(sys.argv)
    new_address_tab= NewAddressTab()
    new_address_tab.send_details.connect(print_address)
    new_address_tab.show()

    sys.exit(app.exec())
