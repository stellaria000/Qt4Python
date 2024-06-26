from argparse import ArgumentParser, RawTextHelpFormatter
import sys

from PySide6.QtCore import (QByteArray, QFile, QFileInfo, QSaveFile, QSettings,
                            QTextStream, Qt, Slot)
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QTextEdit)

import application_rc  # noqa: F401

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._cur_file= ''
        self._text_edit= QTextEdit()
        self.setCentralWidget(self._text_edit)

        self.create_actions()
        self.create_menus()
        self.create_tool_bars()
        self.create_status_bar()
        self.read_settings()

        self._text_edit.document().contentsChanged.connect(self.document_was_modified)

        self.set_current_file('')
        self.setUnifiedTitleAndToolBarOnMac(True)

    def closeEvent(self, event):
        if self.maybe_save():
            self.write_settings()
            event.accept()
        else: event.ignore()

    @Slot()
    def new_file(self):
        if self.maybe_save():
            self._text_edit.clear()
            self.set_current_file('')

    @Slot()
    def open(self):
        if self.maybe_save():
            fileName, filtr= QFileDialog.getOpenFileName(self)
            if fileName: self.load_file(fileName)

    @Slot()
    def save(self):
        if self._cur_file: return self.save_file(self._cur_file)
        return self.save_as()

    @Slot()
    def save_as(self):
        fileName, filtr= QFileDialog.getOpenFileName(self)
        if fileName: return self.save_file(fileName)

        return False

    @Slot()
    def about(self):
        QMessageBox.about(self, "About Application",
                          "The <b>Application</b> example demonstrates how to write modern GUI applications "
                          "using Qt, with a menu bar, toolbars, and a status bar.")
    @Slot()
    def document_was_modified(self): self.setWindowModified(self._text_edit.document().isModified())

    def create_actions(self):
        icon= QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew, QIcon(':/images/new.png'))
        self._new_act= QAction(icon, "&New", self, shortcut= QKeySequence.New,
                               statusTip= "Create a new file", triggered= self.new_file)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew, QIcon(':/images/open.png'))
        self._open_act= QAction(icon, "&Open... ", self, shortcut= QKeySequence.Open, statusTip= "Open an existing file",
                                triggered= self.open)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew, QIcon(':/images/save.png'))
        self._save_act = QAction(icon, "&Save", self, shortcut=QKeySequence.Save, statusTip="Save the doocument to disk",
                                 triggered=self.save)

        self._save_as_act = QAction(icon, "Save &As... ", self, shortcut=QKeySequence.SaveAs, statusTip="Save the doocument under a new name",
                                    triggered=self.save_as)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit)
        self._exit_act = QAction(icon, "E&xit", self, shortcut="Ctrl+Q", statusTip="Exit the application",
                                 triggered=self.close)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.EditCut, QIcon(':/images/cut.png'))
        self._cut_act = QAction(icon, "Cu&t", self, shortcut=QKeySequence.Save,
                                statusTip="Cut the current selection's contents to the clipboard", triggered=self._text_edit.cut)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.EditCut, QIcon(':/images/copy.png'))
        self._copy_act = QAction(icon, "Cu&t", self, shortcut=QKeySequence.Copy,
                                statusTip="Copy the current selection's contents to the clipboard", triggered=self._text_edit.copy)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.EditCut, QIcon(':/images/paste.png'))
        self._paste_act = QAction(icon, "&Paste", self, shortcut=QKeySequence.Paste, statusTip="Paste teh clipboard's contents into the currnet selection",
                                  triggered=self._text_edit.paste)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout)
        self._about_act = QAction(icon, "&About", self, statusTip="Show the Qt library's About box", triggered=self.about)

        self._about_qt_act= QAction("About &Qt", self, statusTip= "Show the applpication's About box", triggered= qApp.aboutQt)

        self._cut_act.setEnabled(False)
        self._copy_act.setEnabled(False)
        self._text_edit.copyAvailable.connect(self._cut_act.setEnabled)
        self._text_edit.copyAvailable.connect(self._copy_act.setEnabled)

    def create_menus(self):
        self._file_menu= self.menuBar().addMenu("&File")
        self._file_menu.addAction(self._new_act)
        self._file_menu.addAction(self._open_act)
        self._file_menu.addAction(self._save_act)
        self._file_menu.addAction(self._save_as_act)
        self._file_menu.addSeparator()
        self._file_menu.addAction(self._exit_act)

        self._edit_menu= self.menuBar().addMenu("&Edit")
        self._edit_menu.addAction(self._cut_act)
        self._edit_menu.addAction(self._copy_act)
        self._edit_menu.addAction(self._paste_act)

        self.menuBar().addSeparator()

        self._help_menu= self.menuBar().addMenu("&Help")
        self._help_menu.addAction(self._about_act)
        self._help_menu.addAction(self._about_qt_act)

    def create_tool_bars(self):
        self._file_tool_bar= self.addToolBar("File")
        self._file_tool_bar.addAction(self._new_act)
        self._file_tool_bar.addAction(self._open_act)
        self._file_tool_bar.addAction(self._save_act)

        self._edit_tool_bar= self.addToolBar("Edit")
        self._edit_tool_bar.addAction(self._cut_act)
        self._edit_tool_bar.addAction(self._copy_act)
        self._edit_tool_bar.addAction(self._paste_act)
    def create_status_bar(self): self.statusBar().showMessage("Ready")

    def read_settings(self):
        settings= QSettings('QtProject', 'Application Example')
        geometry= settings.value('geometry', QByteArray())
        if geometry.size(): self.restoreGeometry(geometry)

    def write_settings(self):
        settings= QSettings('QtProject', 'Application Example')
        settings.setValue('geometry', self.saveGeometry())

    def maybe_save(self):
        if self._text_edit.document().isModified():
            ret= QMessageBox.warning(self, "Application", "The document has been modified. \n "
                                                          "Do you want to save your changes?", QMessageBox.Save| QMessageBox.Discard| QMessageBox.Cancel)

            if ret== QMessageBox.Save: return self.save
            elif ret== QMessageBox.Canel: return False
            return True

    def load_file(self, fileName):
        file= QFile(fileName)

        if not file.open(QFile.ReadOnly| QFile.Text):
            reason= file.errorString()
            QMessageBox.warning(self, "Application", f"Cannot read file {fileName}: \n {reason}.")
            return

        inf= QTextStream(file)
        with QApplication.setOverrideCursor(Qt.WaitCursor): self._text_edit.setPlainText(inf.readAll())

        self.set_current_file(fileName)
        self.statusBar().showMessage("File loaded", 2000)

    def save_file(self, fileName):
        error= None

        with QApplication.setOverrideCursor(Qt.WaitCursor):
            file= QSaveFile(fileName)
            if file.open(QFile.WriteOnly| QFile.Text):
                outf= QTextStream(file)
                outf<< self._text_edit.toPlainText()
                if not file.commit():
                    reason= file.errorString()
                    error= f"Cannot write file {fileName}: \n{reason}."
            else:
                reason= file.errorString()
                error= f"Cannot write file {fileName}: \n{reason}."

        if error:
            QMessageBox.warning(self, "Application", error)
            return False

        self.set_current_file(fileName)
        self.statusBar().showMessage("File saved", 2000)
        return True

    def set_current_file(self, fileName):
        self._cur_file= fileName
        self._text_edit.document().setModified(False)
        self.setWindowModified(False)

        if self._cur_file: shown_name= self.stripped_name(self._cur_file)
        else: shown_name= 'untitled.txt'

        self.setWindowTitle(f"{shown_name}[*]- Application")

    def strippewd_name(self, fullFileName): return QFileInfo(fullFileName).fileName()

if __name__== '__main__':
    argument_parser= ArgumentParser(description='Application Example', formatter_class=RawTextHelpFormatter)
    argument_parser.add_argument("file", help="File", nargs= '?', type= str)
    options= argument_parser.parse_args()

    app= QApplication(sys.argv)
    main_win = MainWindow()
    if options.file: main_win.load_file(options.file)

    main_win.show()
    sys.exit(app.exec())






