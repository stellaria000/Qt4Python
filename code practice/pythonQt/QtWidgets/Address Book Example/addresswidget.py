try: import cpickle as pickle
except ImportError: import pickle

from PySide6.QtCore import (Qt, Signal, Slot, QRegularExpression, QModelIndex,
                            QItemSelection, QSortFilterProxyModel)
from PySide6.QtWidgets import QTabWidget, QMessageBox, QTableView, QAbstractItemView

from tablemodel import TableModel
from newaddresstab import NewAddressTab
from adddialogwidget import AddDialogWidget

class AddressWidget(QTabWidget):
    # THE CENTRAL WIDGET OF THE APPLICATION. MOST OF THE ADDRESSBOOK'S FUNCIONALITY IS CONNTAINED IN THIS CLASS
    selection_changed= Signal(QItemSelection)

    def __init__(self, parent= None):
        # INITIALIZE THE ADDREWSSWIDGET
        super().__init__(parent)

        self._table_model= TableModel()
        self._new_address_tab= NewAddressTab()
        self._new_address_tab.send_details.connect(self.add_entry)
        self.addTab(self._new_address_tab, "Address Book")
        self.setup_tabs()

    @Slot()
    def add_entry(self, name= None, address= None):
        # ADD ENTRY TO THE ADDRESSBOOK
        if name is None and address is None:
            add_dialog= AddDialogWidget()

            if add_dialog.exec():
                name= add_dialog.name
                address= add_dialog.address

        address= {"name": name, "address": address}
        addresses= self._table_model.addresses[:]

        '''
            THE QT DOCS FOR THIS EXAMPLE STATE THAT WHAT WE'RE DOING HERE
            IS CHECKING IF THE ENTERED NAME ALREADY EXISTS. WHAT THEY (AND WE HERE)
            ARE ACTUALLY DOING IS CHECKING IF THE WHOLE NAME/ADDRESS PAIR EXISTS ALREADY- OK FOR
            PURPOSES OF THIS EXAMPLE, BUT OBVIOUSLY NOT HOW A REAL ADDRESSBOOK APPLICATION SHOULD BEHAVE.
        '''
        try:
            addresses.remove(address)
            QMessageBox.information(self, "Duplicate Name", f'The name "{name}" already exists.')
        except ValueError:
            # THE ADDRESS DIDN'T ALREADY EXIST, SO LET'S ADD IT TO THE MODEL.
            # STEP 1. CREATE THE ROW
            self._table_model.insertRows(0)

            #STEP 2. GET THE INDEX OF THE NEWLY CREATED ROW AND USE IT.
            # TO SET THE NAME
            ix= self._table_model.index(0, 0, QModelIndex())
            self._table_model.setData(ix, address["name"], Qt.EditRole)

            #STEP 3: LATHER, RINSE, REPEAT FOR THE ADDRESS.
            ix= self._table_model.index(0, 1, QModelIndex())
            self._table_model.setData(ix, address["address"], Qt.EditRole)

            # REMOVE THE newAdressTab, AS WE NOW HAVE AT LEAST ONE ADDRESS IN THE MODEL.
            self.removeTab(self.indexOf(self._new_address_tab))

            '''
                THE SCREENSHOR FOR THE QT EXAMPLE SHOW NICELY FORMATTED MULTILINE CELLS,
                BUT THE ACTUAL APPLICATION DOESNT BEHAVE QUITE SO NICELY, AT LEAST ON UBUNTU. 
                HERE WE RESIZE THE NEWLY CREATED EOW SO THAT MULTILINE ADDRESSES LOOK REASONABLE.
            '''
            table_view= self.currentWidget()
            table_view.resizeRowToContents(ix.row())

    @Slot()
    def edit_entry(self):
        # EDIT AN ENTRY IN THE ADDRESSBOOK.
        table_view= self.currentWidget()
        proxy_model= table_view.model()
        selection_model= table_view.selectionModel()

        # GET TEH NAMEAND ADDRESS OF THE CURRENTLY SELECTED ROW.
        indexes= selection_model.selectedRows()
        if len(indexes)!= 1: return

        row= proxy_model.mapToSource(indexes[0]).row()
        ix= self._table_model.index(row, 0, QModelIndex())
        name= self._table_model.data(ix, Qt.DisplayRole)
        ix= self._table_model.index(row, 1, QModelIndex())
        address= self._table_model.data(ix, Qt.DisplayRole)

        # OPEN AN addDialogWidget, AND ONLY ALLOW THE USER TO EDIT THE ADDRESS.
        add_dialog= AddDialogWidget()
        add_dialog.setWindowTitle("Edit a Contact")
        add_dialog._name_text.setReadOnly(True)
        add_dialog._name_text.setText(name)
        add_dialog._address_text.setText(address)

        #IF THE ADDRESS IS DIFFERENT, ADD IT TO THE MODEL.
        if add_dialog.exec():
            new_address= add_dialog.address

            if new_address!= address:
                ix= self._table_model.index(row, 1, QModelIndex())
                self._table_model.setData(ix, new_address, Qt.EditRole)
    @Slot()
    def remove_entry(self):
        # REMOVE AN ENTRY FROM THE ADDRESSBOOK.
        table_view= self.currentWidget()
        proxy_model= table_view.model()
        selection_model= table_view.selectionModel()

        #JUST LIKE editEntry, BUT THIS TIME REMOVE THE SELECTED ROW.
        indexes= selection_model.selectedRows()
        for index in indexes:
            row= proxy_model.mapToSource(index).row()
            self._table_model.removeRows(row)

        #IF WE'RE REMOVED THE LAST ADDRESS IN THE MODEL, DISPLAY THE NEWADDRESSTAB
        if self._table_model.rowCount()== 0:
            self.insertTab(0, self._new_address_tab, "Address Book")

    def setup_tabs(self):
        # SETUP THE VARIOUS TABS IN THE ADDRESSWIDGET.
        groups = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VW", "XYZ"]

        for group in groups:
            proxy_model= QSortFilterProxyModel(self)
            proxy_model.setSourceModel(self._table_model)
            proxy_model.setDynamicSortFilter(True)

            table_view= QTableView()
            table_view.setModel(proxy_model)
            table_view.setSortingEnabled(True)
            table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
            table_view.horizontalHeader().setStretchLastSection(True)
            table_view.verticalHeader().hide()
            table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
            table_view.setSelectionMode(QAbstractItemView.SingleSelection)

            '''
            THIS HERE BE THE MAGIC: WE USE THE GROUP NAME TO BUILD THE REGEX FOR THE QSortFilterProxyModel 
            FOR THE GROUP'S TAB. THE REGEX WILL END UP LOOKING LIKE "^[ABC].*", ONLY ALLOWING THIS TAB
            TO DISPLAY ITEMS WEHRE THE NAME STARTS WITH "A", "B", OR "C". NOTICE THAT WE SET IT TO BE
            CASE-INTENSITIVE.
            '''
            re= QRegularExpression(f"^[{group}].*")
            assert re.isValid()
            re.setPatternOptions(QRegularExpression.CaseInsensitiveOption)

            proxy_model.setFilterRegularExpression(re)
            proxy_model.setFilterKeyColumn(0) # filter on the name column
            proxy_model.sort(0, Qt.AscendingOrder)

            # THIS PREVENTS AN APPLICATION CRASH
            self.viewselectionmodel= table_view.selectionModel()
            table_view.selectionModel().selectionChanged.connect(self.selection_changed)

            self.addTab(table_view, group)

    '''
        THE QT EXAMPLE USES A QDataStream FOR THE SAVING AND LOADING. HERE WE'RE USINGA PYTHON
        DISCTIONARY TO STORE THE ADDRESSES, WHICK CAN'T BE STREAMED USING QDataStream, 
        SO WER JUST USE CPICKLE FOR THIS EXAMPLE.
    '''
    def read_from_file(self, filename):
        # READ CONTACTS IN FROM A FILE
        try:
            f= open(filename, "rb")
            addresses= pickle.load(f)
        except IOError: QMessageBox.information(self, f"unable to open file: {filename}")
        finally: f.close()

        if len(addresses)== 0: QMessageBox.information(self, f"No contacts in file: {filename}")
        else:
            for address in addresses: self.add_entry(address["name"], address["address"])

    def write_to_file(self, filename):
        # SAVE ALL CONTACTS IN THE MODEL TO A FILE
        try:
            f= open(filename, "wb")
            pickle.dump(self._table_model.addresses, f)
        except IOError: QMessageBox.information(self, f"unable to open file: {filename}")
        finally: f.close()

if __name__== "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app= QApplication(sys.argv)
    address_widget= AddressWidget()
    address_widget.show()

    sys.exit(app.exec())