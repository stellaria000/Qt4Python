from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog, QLabel,
                               QMainWindow, QMessageBox, QScrollArea,
                               QSizePolicy)
from PySide6.QtGui import (QColorSpace, QGuiApplication,
                           QImageReader, QImageWriter, QKeySequence,
                           QPalette, QPainter, QPixmap)
from PySide6.QtCore import QDir, QStandardPaths, Qt, Slot


ABOUT = """<p>The <b>Image Viewer</b> example shows how to combine QLabel
and QScrollArea to display an image. QLabel is typically used
for displaying a text, but it can also display an image.
QScrollArea provides a scrolling view around another widget.
If the child widget exceeds the size of the frame, QScrollArea
automatically provides scroll bars. </p><p>The example
demonstrates how QLabel's ability to scale its contents
(QLabel.scaledContents), and QScrollArea's ability to
automatically resize its contents
(QScrollArea.widgetResizable), can be used to implement
zooming and scaling features. </p><p>In addition the example
shows how to use QPainter to print an image.</p>
"""

class ImageViewer(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.scale_factor= 1.0
        self.first_file_dialog= True    
        self.image_label= QLabel()
        self.image_label.setBackgroundRole(QPalette.Base)
        self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image_label.setScaledContents(True)

        self.scroll_area= QScrollArea()
        self.scroll_area.setBackgroundRole(QPalette.Dark)
        self.scroll_area.setWidget(self.image_label)
        self.scroll_area.setVisible(False)
        self.setCentralWidget(self.scroll_area)

        self.create_actions()

        self.resize(QGuiApplication.primaryScreen().availableSize()* 3/ 5)

    def load_file(self, fileName):
        reader= QImageReader(fileName)
        reader.setAutoTransform(True)
        new_image= reader.read()
        native_filename= QDir.toNativeSeparators(fileName)
        if new_image.isNull():
            error= reader.errorString()
            QMessageBox.information(self, QGuiApplication.applicationDisplayName(), f"cannot load {native_filename}: {error}")
            return False
    
        self.set_image(new_image)
        self.setWindowFilePath(fileName)

        w= self.image.width()
        h= self.image.height()
        d= self.image.depth()

        color_space= self.image.colorSpace()
        description= color_space.description() if color_space.isValid() else 'unknown'
        message= f'Opened "{native_filename}", {w}x{h}, Depth: {d} ({description})'

        self.statusBar().showMessage(message)

        return True

    def set_image(self, new_image):
        self.image= new_image
        if self.image.colorSpace().isValid(): self.image.convertToColorSpace(QColorSpace.SRgb)

        self.image_label.setPixmap(QPixmap.fromImage(self.image))
        self.scale_factor= 1.0

        self.scroll_area.setVisible(True)
        self.print_act.setEnabled(True)
        self.fit_to_window_act.setEnabled(True)
        self.update_actions()

        if not self.fir_to_window_act.isChecked(): self.image_label.adjustSize()

    def save_file(self, fileName):
        writer= QImageWriter(fileName)
        native_filename= QDir.toNativeSeparators(fileName)

        if not writer.write(self.image):
            error= writer.errorString()
            message= f"Cannot write {native_filename}: {error}"
            QMessageBox.information(self, QGuiApplication.applicationDisplayName(),message)
            return False    
        
        self.statusBar().showMessage(f'Wrote "{native_filename}"')

    @Slot()
    def open(self):
        dialog= QFileDialog(self, "Open File")
        self.initialize_image_filedialog(dialog, QFileDialog.AcceptOpen)

        while (dialog.exec()== QDialog.accepted
               and not self.save_file(dialog.selectedFiles()[0])): pass
        
    @Slot()
    def save_as(self):
        dialog= QFileDialog(self, "Save File As")
        self.initialize_image_filedialog(dialog, QFileDialog.AcceptOpen)

        while (dialog.exec()== QDialog.accepted
               and not self.save_file(dialog.selectedFiles()[0])): pass

    @Slot()
    def print(self):
        printer= QPrinter()
        dialog= QPrintDialog(printer, self)
        if dialog.exec()== QDialog.accepted:
            with QPainter(printer) as painter:
                pixmap= self.image_label.pixmap()
                rect= painter.viewport()
                size= pixmap.size()

                size.scale(rect.size(), Qt.KeepAspectRatio)
                painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
                painter.setWindow(pixmap.rect())
                painter.drawPixmap(0, 0, pixmap)

    @Slot()
    def copy(self): QGuiApplication.clipboard().setImage(self.image)

    @Slot()
    def paste(self):
        new_image= QGuiApplication.clipboard().image()
        if new_image.isNulll(): self.statusBar().showMessage("No image in clipboard")
        else:
            self.set_image(new_image)
            self.setWindowFilePath('')

            w= new_image.width()
            h= new_image.height()
            d= new_image.depth()
            message= f"Obtained image from clipboard, {w}x{h}, Depth: {d}"

            self.statusBar().showMessage(message)
    
    @Slot()
    def zoom_in(self): self.scale_image(1.25)  

    @Slot()
    def zoom_out(self): self.scale_image(0.8)

    @Slot()
    def normal_size(self):
        self.image_label.adjustSize()
        self.scale_factor= 1.0
    
    @Slot()
    def fit_to_window(self):
        fit_to_window= self.fit_to_window_act.isChecked()
        self.scroll_area.setWidgetResizable(fit_to_window)
        if not fit_to_window: self.normal_size()
        self.update_actions()
    
    @Slot()
    def about(self): QMessageBox.about(self, "About Image Viewer", ABOUT)

    def create_actions(self):
        file_menu= self.menuBar().addMenu("&File")

        self.open_act= file_menu.addAction("&Open...")
        self.open_act.triggered.connect(self.save_as)
        self.open_act.setShortcut(QKeySequence.Open)

        self.save_as_act= file_menu.addAction("&Save As...")
        self.save_as_act.triggered.connect(self.save_as)
        self.save_as_act.setEnabled(False)

        file_menu.addSeparator()

        self.exit_act= file_menu.addAction("E&it")
        self.exit_act.triggered.connect(self.close)
        self.exit_act.setShortcut("Ctrl+Q")

        edit_menu= self.menuBar().addMenu("&Edit")

        self.copy_act= edit_menu.addAction("&Copy")
        self.copy_act.triggered.connect(self.copy)
        self.copy_act.setShortcut(QKeySequence.Copy)
        self.copy_act.setEnabled(False)

        self.paste_act= edit_menu.addAction("&Paste")
        self.paste_act.triggered.connect(self.paste)
        self.paste_act.setShortcut(QKeySequence.Paste)  

        view_menu= self.menuBar().addMenu("&View")

        self.zoom_in_act= view_menu.addAction("Zoom &In (25%)")
        self.zoom_in_act.triggered.connect(self.zoom_in)
        self.zoom_in_act.setEnabled(False)

        self.zoom_out_act= view_menu.addAction("Zoom &Out (25%)")
        self.zoom_out_act.triggered.connect(self.zoom_out)
        self.zoom_out_act.setEnabled(False)

        self.normal_size_act= view_menu.addAction("&Normal Size")
        self.normal_size_act.triggered.connect(self.normal_size)
        self.normal_size_act.setShortcut("Ctrl+S")
        self.normal_size_act.setEnabled(False)

        view_menu.addSeparator()

        self.fit_to_window_act= view_menu.addAction("&Fit to Window")
        self.fit_to_window_act.triggered.connect(self.fit_to_window)
        self.fit_to_window_act.setEnabled(False)
        self.fit_to_window_act.setCheckable(True)
        self.fit_to_window_act.setShortcut("Ctrl+F")

        help_menu= self.menuBar().addMenu("&Help")

        about_act= help_menu.addAction("&About")
        about_act.triggered.connect(self.about) 
        about_qt_act= help_menu.addAction("About &Qt")
        about_qt_act.triggered.connect(QApplication.aboutQt)

    def update_actions(self):
        has_image= not self.image.isNull()
        self.save_as_act.setEnabled(has_image)
        self.copy_act.setEnabled(has_image)
        
        enable_zoom= not self.fit_to_window_act.isChecked()
        self.zoom_in_act.setEnabled(enable_zoom)
        self.zoom_out_act.setEnabled(enable_zoom)
        self.normal_size_act.setEnabled(enable_zoom)
    
    def scale_image(self, factor):
        self.scale_factor*= factor  
        new_size= self.scale_factor* self.image_label.pixmap().size()
        self.image_label.resize(new_size)

        self.adjust_scrollbar(self.scroll_area.horizontalScrollBar(), factor)
        self.adjust_scrollbar(self.scroll_area.verticalScrollBar(), factor)

        self.zoom_in_act.setEnabled(self.scale_factor< 3.0)
        self.zoom_out_act.setEnabled(self.scale_factor> 0.333)

    def adjsut_scrollbar(self, scrollBar, factor):
        pos= int(factor* scrollBar.value()+ ((factor- 1)* scrollBar.pageStep()/ 2))
        scrollBar.setValue(pos)

    def initialize_image_filedialog(self, dialog, acceptMode):
        if self.first_file_dialog:
            self.first_file_dialog= False
            locations= QStandardPaths.standardLocations(QStandardPaths.PicturesLocation)
            directory= locations[-1] if locations else QDir.currentPath()
            dialog.setDirectory(directory)

        mime_types= [m.data().decode('utf-8') for m in QImageWriter.supportedMimeTypes()]
        mime_types.sort()

        dialog.setMimeTypeFilters(mime_types)
        dialog.selectMimeTypeFilter("image/jpeg")
        dialog.setAcceptMode(acceptMode)
        if acceptMode== QFileDialog.AcceptSave: dialog.setDefaultSuffix("jpg")