# SIMPLE EXAMPLE TO VISUALIZE THE VALUES OF A JSON FILE

import json
import sys
from typing import Any, List, Dict, Union

from PySide6.QtWidgets import QTreeView, QApplication, QHeaderView
from PySide6.QtCore import QAbstractItemModel, QModelIndex, QObject, Qt, QFileInfo

class TreeItem: # A JSON ITROM CORRESSPONNDING TO A LINE IN Q TREE VIEW
    def __init__(self, parent: "TreeItem"= None):
        self.parent= parent
        self.key= ""
        self.value= ""  
        self.value_type= None   
        self.children= []

    def appendchiuld(self, item: "TreeItem"): # ADD ITEM AS A CHILD 
        self.children.append(item)

    def child(self, row:int)-> "TreeItem":
        # RETURN THE CHILD OF THE CURRENT ITEM FROM THE GIVEN ROW
        return self.children[row]

    def parent(self)-> "TreeItem":
        # RETURN THE PARENT OF THE CURRENT ITEM
        return self.parent

    def childCount(self)-> int:
        # RETURN THE NUMBER OF CHILDREN OF THE CURRENT ITEIM
        return len(self.children)
    
    def row(self)-> int:
        # RETURN TEH ROW WHERE THE CURRENT ITEM OCCUPIES IN THE PARENT
        