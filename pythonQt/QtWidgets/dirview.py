<<<<<<< HEAD
import sys
from argparse import ArgumentParser, RawTextHelpFormatter

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication, QFileSystemModel, QFileIconProvider, QTreeView, QScroller

if __name__== "__main__":
    app= QApplication(sys.argv)

    name= "Dir View"

    argument_parser= ArgumentParser(description= name, formatter_class= RawTextHelpFormatter)
    argument_parser.add_argument("--no custom", "-c", action="store_true",
                                 help= "set QFileSystemModel.DontUseCustuomDirectoryIcons")
    argument_parser.add_argument("--no watch", "-w", action="store_true", help="set QFileSystemModel.DontWatch")
    argument_parser.add_argument("directory", help="The directory to start in.", nargs= '?', type= str)

    options= argument_parser.parse_args()
    root_path= options.directory

    model= QFileSystemModel()
    icon_provider= QFileIconProvider()
    model.setIconProvider(icon_provider)
    model.setRootPath("")

    if options.no_custom: model.setOption(QFileSystemModel.DontUseCustomDirectoryIcons)
    if options.no_watch: model.setOption(QFileSystemModel.DontWatchForChanges)

    tree= QTreeView()
    tree.setModel(model)

    if root_path:
        root_index= model.index(QDir.cleanPath(root_path))
        if root_index.isValid(): tree.setRootIndex(root_index)

    # DEMONSTRATING LOOK AND FEEL FEATURES
    tree.setAnimated(False)
    tree.setIndentation(20)
    tree.setSortingEnabled(True)

    availableSize= tree.screen().availableGeometry().size()
    tree.resize(availableSize/ 2)
    tree.setColumnWidth(0, tree.width()/ 3)

    # MAKE IT FLICKABLE ON TOUCHSCREENS
    QScroller.grabGesture(tree, QScroller.ScrollerGestureType.TouchGesture)

    tree.setWindowTitle(name)
    tree.show()

    sys.exit(app.exec())
=======
import sys
from argparse import ArgumentParser, RawTextHelpFormatter

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication, QFileSystemModel, QFileIconProvider, QTreeView, QScroller

if __name__== "__main__":
    app= QApplication(sys.argv)

    name= "Dir View"

    argument_parser= ArgumentParser(description= name, formatter_class= RawTextHelpFormatter)
    argument_parser.add_argument("--no custom", "-c", action="store_true",
                                 help= "set QFileSystemModel.DontUseCustuomDirectoryIcons")
    argument_parser.add_argument("--no watch", "-w", action="store_true", help="set QFileSystemModel.DontWatch")
    argument_parser.add_argument("directory", help="The directory to start in.", nargs= '?', type= str)

    options= argument_parser.parse_args()
    root_path= options.directory

    model= QFileSystemModel()
    icon_provider= QFileIconProvider()
    model.setIconProvider(icon_provider)
    model.setRootPath("")

    if options.no_custom: model.setOption(QFileSystemModel.DontUseCustomDirectoryIcons)
    if options.no_watch: model.setOption(QFileSystemModel.DontWatchForChanges)

    tree= QTreeView()
    tree.setModel(model)

    if root_path:
        root_index= model.index(QDir.cleanPath(root_path))
        if root_index.isValid(): tree.setRootIndex(root_index)

    # DEMONSTRATING LOOK AND FEEL FEATURES
    tree.setAnimated(False)
    tree.setIndentation(20)
    tree.setSortingEnabled(True)

    availableSize= tree.screen().availableGeometry().size()
    tree.resize(availableSize/ 2)
    tree.setColumnWidth(0, tree.width()/ 3)

    # MAKE IT FLICKABLE ON TOUCHSCREENS
    QScroller.grabGesture(tree, QScroller.ScrollerGestureType.TouchGesture)

    tree.setWindowTitle(name)
    tree.show()

    sys.exit(app.exec())
>>>>>>> 5f9325a602879c9b5f4d4bc1a8dfbc3a1acad5c1
