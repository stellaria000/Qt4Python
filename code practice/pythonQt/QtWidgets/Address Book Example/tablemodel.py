from PySide6.QtCore import (QAbstractTableModel, QModelIndex, Qt)

class TableModel(QAbstractTableModel):
    def __init__(self, addresses= None, parent= None):
        super().__init__(parent)

        if addresses is None: self.addresses= []
        else: self.addresses= addresses

    def rowCount(self, index= QModelIndex()):
        # RETURNS THE NUMBER OF ROWS THE MODEL HOLDS
        return len(self.addresses)

    def columnCount(self, index= QModelIndex()):
        # RETURNS THE NUMBER OF COLUMNS THE MODEL HOLDS
        return 2

    def data(self, index, role= Qt.DisplayRole):
        '''
        DEPENDING ON THE INDEX AND ROLE GIVEN, RETURN DATA.
        IF NOT RETURNING DATA, RETURN NONE(PySide EQUIVALENT OF QT'S
        INVALID Qvariant)
        '''
        if not index.isValid(): return None
        if not 0<= index.row()< len(self.addresses): return None
        if role== Qt.DisplayRole:
            name= self.addresses[index.row()]["name"]
            address= self.addresses[index.row()]["address"]

            if index.column()== 0: return name
            elif index.column()== 1: return address

        return None

    def headerData(self, section, orientation, role = Qt.DisplayRole):
        # SET THE HEADERS TO BE DISPLAYED
        if role!= Qt.DisplayRole: return None
        if orientation== Qt.Horizontal:
            if section== 0: return "Name"
            elif section== 1: return "Address"

        return None

    def insertRows(self, position, rows= 1, index= QModelIndex()):
        # INSERT A ROW INTO THE MODEL
        self.beginInsertRows(QModelIndex(), position, position+ rows- 1)

        del self.addresses[position: position+ rows]

        self.endRemoveRows()

        return True

    def removeRows(self, position, rows= 1, index= QModelIndex()):
        # REMOVE A ROW FROM THE MODEL
        self.beginRemoveRows(QModelIndex(), position, position+ rows- 1)

        self.endRemoveRows()

        return True

    def setData(self, index, value, role = Qt.EditRole):
        # ADJUST THE DATA(SET IT TO <VALUE>) DEPENDING ON THE GIVEN INDEX AND ROLE
        if role!= Qt.EditRole: return False
        if index.isValid() and 0<= index.row()< len(self.addresses):
            address= self.addresses[index.row()]

            if index.column()== 0: address["name"]= value
            elif index.column()== 1: address["address"]= value
            else: return False

            self.dataChanged.emit(index, index, 0)

            return True
        return False

def flags(self, index):
    '''
        SET THE ITEM FLAGS AT THE GIVEN INDEX.
        SEEMS LIKE WE'RE IMPLEMENTING THIS FUNCTION JUST TO SEE HOW IT'S DONE,
        AS WE MANUALLY ADJUST EACH TABLEVIEW TO HAVE NoEditTriggers
    '''
    if not index.isValid(): return Qt.ItemIsEnabled

    return Qt.ItemFlags(QAbstractTableModel.flags(self, index)| Qt.ItemIsEnable)


