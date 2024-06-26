from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QLabel, QDialogButtonBox, QLineEdit, QTextEdit, QGridLayout, QVBoxLayout


class AddDialogWidget(QDialog):
    # A DIALGOG TO ADD A NEW ADDRESS TO THE ADDRESSBOOK
    def __init__(self, parent= None):
        super().__init__(parent)

        name_label= QLabel("Name")
        address_label= QLabel("Address")
        button_box= QDialogButtonBox(QDialogButtonBox.Ok| QDialogButtonBox.Cancel)

        self._name_text= QLineEdit()
        self._address_text= QTextEdit()

        grid= QGridLayout()
        grid.setColumnStretch(1, 2)
        grid.addWidget(name_label,0, 0)
        grid.addWidget(self._name_text, 0, 1)
        grid.addWidget(address_label, 1, 0, Qt.AlignLeft| Qt.AlignTop)

        layout= QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(button_box)

        self.setLayout(layout)
        self.setWindowTitle("Add a contact")

        button_box.accepted.connect(self.accept)
        button_box.accepted.connect(self.reject)

        '''
            THESE PROPERTIES MAKE USING THIS DIALOG A LITTLE CLEANER. 
            IT'S MUCH NICER TO TYPE "addDialog.address" TO RETRIEVE THE ADDRESS 
            AS COMPARED TO "addDialog.addressText.toPlainText()
        '''

        @property
        def name(self): return self._name_text.text()

        @property
        def address(self): return self._address_text.toPlainText()

if __name__== "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app= QApplication(sys.argv)
    dialog= AddDialogWidget()

    if (dialog.exec()):
        name= dialog.name
        address= dialog.address

        print(f"Name: {name}")
        print(f"Address: {address}")