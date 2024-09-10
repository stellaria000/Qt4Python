import sys

from PySide6.QtCore import (QDir, QPoint, QRect, QStandardPaths, Qt, QTimer,
                            Slot)
from PySide6.QtGui import QGuiApplication, QImageWriter
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFileDialog,
                               QGridLayout, QGroupBox, QHBoxLayout, QLabel,
                               QMessageBox, QPushButton, QSizePolicy, QSpinBox,
                               QVBoxLayout, QWidget)

class Screenshot(QWidget):
    def __init__(self):
        super().__init__()

        self.screenshot_label= QLabel(self)
        self.screenshot_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Exapanding)
        self.screenshot_label.setAlignment(Qt.AlignCenter)

        screen_geometry: QRect= self.screen().geometry()

        self.screenshot_label.setMinimumSize(screen_geometry.width()/ 8, screen_geometry.height()/ 8)

        main_layout= QVBoxLayout(self)
        main_layout.addWidget(self.screenshot_label)

        options_group_box= QGroupBox("Options", self)
        self.delay_spinbox= QSpinBox(options_group_box)
        self.delay_spinbox.setSuffix(" s")
        self.delay_spinbox.setMaximum(60)

        self.delay_spinbox.valueChanged.connect(self.update_checkbox)

        self.hide_this_window_checkbox= QCheckBox("Hide This Window", options_group_box)

        options_group_box_layout= QGridLayout(options_group_box)
        options_group_box_layout.addWidget(QLabel("Screenshot Delay:", self), 0, 0) 
        options_group_box_layout.addWidget(self.delay_spinbox, 0, 1)
        options_group_box_layout.addWidget(self.hide_this_window_checkbox, 1, 0, 1, 2)

        main_layout.addWidget(options_group_box)

        buttons_layout= QHBoxLayout()
        self.new_screenshot_btn= QPushButton("New Screenshot", self)
        self.new_screenshot_btn.clicked.connect(self.new_screenshot)
        buttons_layout.addWidget(self.new_screenshot_btn)
        save_screenshot_btn= QPushButton("Save Screenshot", self)
        save_screenshot_btn.clicked.connect(self.save_screenshot)
        buttons_layout.addWidget(save_screenshot_btn)
        quit_screenshot_btn= QPushButton("Quit", self)
        quit_screenshot_btn.setShortcut(Qt.Ctrl| Qt.Key_Q)
        quit_screenshot_btn.clicked.connect(self.close)
        buttons_layout.addWidget(quit_screenshot_btn)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        self.shoot_screen()
        self.delay_spinbox.setValue(5)

        self.setWindowTitle("Screenshot")
        self.resize(300, 200)
    
    def resizeEvent(self, event):    
        scaled_size= self.original_pixmap.size()
        scaled_size.scale(self.screenshot_label.size(), Qt.KeepAspectRatio)
        if scaled_size!= self.screenshot_label.pixmap().size():
            self.update_screenshot_label()

    @Slot()
    def new_screenshot(self):
        if self.hide_this_window_checkbox.isChecked(): self.hide()

        self.new_screenshot_btn.setDisabled(True)

        QTimer.singleShot(self.delay_spinbox.value()* 1000, self.shoot_screen)

    @Slot()
    def save_screenshot(self):
        fmt= "png"
        initial_path= QStandardPaths.writableLocation(QStandardPaths.PicturesLocation)
        if not initial_path: initial_path= QDir.currentPath()
        initial_path+= f"/untitled.{fmt}"

        fileDialog= QFileDialog(self, "Save As", initial_path)
        fileDialog.setAcceptMode(QFileDialog.AcceptSave)
        fileDialog.setFileMode(QFileDialog.AnyFile)
        fileDialog.setDirectory(initial_path)

        mime_types= []
        for bf in QImageWriter.supportedMimeTypes():
            mime_types.append(bf.data().decode("utf-8"))
        fileDialog.setMimeTypeFilters(mime_types)
        fileDialog.selectMimeTypeFilter("image/"+ fmt)
        fileDialog.setDefaultSuffix(fmt)
        if fileDialog.exec()!= QDialog.Accepted: return

        file_name= fileDialog.selectedFiles()[0]
        if not self.original_pixmap.save(file_name):
            path= QDir.toNativeSeparators(file_name)
            QMessageBox.warning(self, "Save Error", f"The image could not be saved to {path}")
    
    def shoot_schreen(self):
        screen= QGuiApplication.primaryScreen()
        window= self.windowHandle()
        if window: screen= window.screen()
        if not screen: return   

        if self.delay_spinbox.value()!= 0: QApplication.beep()

        self.original_pixmap= screen.grabWindow(0)
        self.update_screenshot_label()

        self.new_screenshot_btn.setDisabled(False)
        if self.hide_this_window_checkbox.isChecked(): self.show()
    
    @Slot()
    def update_checkbox(self):
        if self.delay_spinbox.value== 0:
            self.hide_this_window_checkbox.setDisabled(True)
            self.hide_this_window_checkbox.setChecked(False)
        else: self.hide_this_window_checkbox.setDisabled(False)

    def update_screenshot_label(self):
        self.screenshot_label.setPixmap(self.original_pixmap.scaled(self.screenshot_label.size(), 
                                                                    Qt.KeepAspectRatio, Qt.SmoothTransformation, ))
        
    
if __name__== "__main__":
    app= QGuiApplication(sys.argv)
    screenshot= Screenshot()
    screenshot.move(screenshot.screen().availableGeometry().topLeft()+ QPoint(20, 20))
    screenshot.show()

    sys.exit(app.exec())