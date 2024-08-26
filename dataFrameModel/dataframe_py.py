# A PYTHON APPLICATION THAT DEMONSTRATES HOW TO VISUALIZE A PANDAS DATAFRAME
import pandas as pd

from PySide6.QtWidgets import QTableView, QApplication
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
import sys

class pandasModel(QAbstractTableModel):
# A MODEL TO INTERFACE A QT VIEW WITH PANDAS DATAFRAME
    def __init__(self, dataframe: pd.DataFrame, parent= None):
        QAbstractTableModel.__init__(self, parent)
        self.dataframe= dataframe

    def rowCount(self, parent= QModelIndex())-> int:
    # OVERRIDE METHOD FROM Q ABSTRACT TABLE MODEL, RETURN ROW COUNT OF THE PANDAS DATAFRAME
        if parent== QModelIndex(): 
            return len(self.dataframe)
        return 0
    
    def columnCount(self, parent= QModelIndex())-> int:
    # OVERRIDE METHOD FROM Q ABSTRACT TABLE MODEL, RETURN COLUMN COUNT OF THE PANDAS DATAFRAME
        if parent== QModelIndex(): 
            return len(self.dataframe.columns)
        
        return 0
    
    def data(self, index: QModelIndex, role= Qt.ItemDataRole):
    # OVERRIDE METHOD FROM Q ABSTRACT TABLE MODEL, RETURN DATA CELL FROM TEH PANDAS DATAFRAME
        if not index.isValid(): return None

        if role== Qt.DisplayRole:
            return str(self.dataframe.iloc[index.row(), index.column()])
        
        return None
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole):
    # OVERRIDE METHOD FROM Q ABSTRACT TABLE MODEL, 
    # RETURN DATAFRAME INDEX AS VERTICAL HEADER DATA AND COLUMNS AS HORIZONTAL HEADER DATA
        if role== Qt.DisplayRole: 
            if orientation== Qt.Horizontal: return str(self.dataframe.columns[section])

            if orientation== Qt.Vertical: return str(self.dataframe.index[section])

        return None
    
if __name__== "__main__":
    app= QApplication(sys.argv)
    df= pd.read_csv()   # file name 
    
    view= QTableView()
    view.resize(800, 500)
    view.horizontalHeader().setStretchLastSection(True)
    view.setAlternatingRowColors(True)
    view.setSelectionBehavior(QTableView.selectRows)

    model= PandasModel(df)
    view.setModel(model)
    view.show()

    app.exec()
