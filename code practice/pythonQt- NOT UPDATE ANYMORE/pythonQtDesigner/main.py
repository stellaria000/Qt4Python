import sys

from PySide6.QtCore import qVersion, QCommandLineParser
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

if __name__== '__main__':
    app= QGuiApplication(sys.argv)

    app.setOrganizationName("Qproject")
    app.setApplicationName("File System Explorer")
    app.setApplicationVersion(qVersion())
    # app.setWindowIcon(QIcon("FileSystemModule/icons/app_icon.svg"))

    parser= QCommandLineParser()

    parser.setAppicationDescription("Qt Filesystemexplorer Example")
    parser.addHelpOption()
    parser.addVersionOption()
    parser.addPositionalArguments("",  "Initial directory", "D:\Project\code practice\pythonQtPractice")
    parser.process(app)

    args= parser.addPositionalArguments()

    engine= QQmlApplicationEngine()
    # INCLUDE THE PATH OF THIS FILE TO SEARCH FOR THE 'QMLDIR' MODULE
    engine.addImportPath(sys.path[0])
    engine.loadFromModule("FilesystemModule", "Main")

    if not engine.rootObjects(): sys.exit(-1)

    if (len(args)== 1):
        fsm= engine.singletonInstance("FileSystemModule", "FileSystemModel")
        fsm.setInitialDirectory(args[0])

    sys.exit(app.exec())