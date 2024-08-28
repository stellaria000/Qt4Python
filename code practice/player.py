# MEDIA PLAYER DEMONSTRATES A SIMPLE MULTIMEDIA PLAYER THAT CAN PLAY AUDIO AND OR VIDEO FILES USING VARIOUS CODECS
# https://doc.qt.io/qtforpython-6/examples/example_multimedia_player.html

import sys
from PySide6.QtCore import QStandardPaths, Qt, Slot
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog,
                               QMainWindow, QSlider, QStyle, QToolBar)
from PySide6.QtMultimedia import (QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget

AVI= "" # AVI
MP4= '' 

def get_supported_mime_types():
    result= []

    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type= QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    
    return result

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.playlist= []
        self.playlist_index= -1
        self.audio_output= QAudioOutput()
        self.player= QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)
        self.player.errorOccurred.connect(self.player_error)

        tool_bar= QToolBar()
        self.addToolBar(tool_bar)

        file_menu= self.menuBar().addMenu("&File")
        icon= QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen)
        open_action= QAction(icon, "&Open...", self, shortcut= QKeySequence.Open, triggered= self.open)
        file_menu.addAction(open_action)
        tool_bar.addAction(open_action)

        icon= QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit)
        exit_action= QAction(icon, "E&xit", self, shortcut= "Ctrl+Q", triggered= self.close)
        file_menu.addAction(exit_action)

        play_menu= self.menuBar().addMenu("&Play")
        style= self.style()
        icon= QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart, style.standardIcon(QStyle.SP_MediaPlay))
        self.play_action= tool_bar.addAction(icon, "Play")
        self.play_action.triggered.connect(self.player.play)
        play_menu.addAction(self.play_action)

        icon= QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipBackward, style.standardIcon(QStyle.SP_MediaSkipBackward))
        self.previous_action= tool_bar.addAction(icon, "Previous")
        self.previous_action.triggered.connect(self.previous_clicked)   
        play_menu.addAction(self.previous_action)   

        icon= QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause, style.standardIcon(QStyle.SP_MediaPause))
        self.pause_action= tool_bar.addAction(icon, "Pause")
        self.pause_action.triggered.connect(self.player.pause)   
        play_menu.addAction(self.pause_action)

        icon= QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward, style.standardIcon(QStyle.SP_MediaSkipForward))
        self.next_action= tool_bar.addAction(icon, "Next")
        self.next_action.triggered.connect(self.next_clicked)   
        play_menu.addAction(self.next_action)

        icon= QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop, style.standardIcon(QStyle.SP_MediaStop))
        self.stop_action= tool_bar.addAction(icon, "Stop")
        self.stop_action.triggered.connect(self.ensure_stopped)   
        play_menu.addAction(self.stop_action)

        self.volume_slider= QSlider()
        self.volume_slider.setOrientation(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        available_width= self.screen().availableGeometry().width()
        self.volume_slider.setFixedWidth(available_width/ 10)
        self.volume_slider.setValue(self.audio_output.volume())
        self.volume_slider.setTickInterval(10)
        self.volume_slider.setTickPosition(QSlider.TicksBelow)
        self.volume_slider.setToolTip("Volume")
        self.volume_slider.valueChanged.connect(self.audio_output.setVolume)
        tool_bar.addWidget(self.volume_slider)

        icon= QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout)
        about_menu= self.menuBar().addMenu("&About")
        about_qt_act= QAction(icon, "About &Qt", self, triggered= qApp.aboutQt)
        about_menu.addAction(about_qt_act)

        self.video_widget= QVideoWidget()
        self.setCentralWidget(self.video_widget)
        self.player.playbackStateChanged.connect(self.update_buttons)
        self.player.setVideoOutput(self.video_widget)

        self.update_buttons(self.player.playbackState())
        self.mime_types= []

    def closeEvent(self, event):
        self.ensure_stopped()
        event.accept()
    
    @Slot()
    def open(self):
        self.ensure_stopped()
        file_dialog= QFileDialog(self)

        is_windows= sys.platform== 'win32'  
        if not self.mime_types:
            self.mime_types= get_supported_mime_types()
            if (is_windows and AVI not in self.mime_types):
                self.mime_types.append(AVI)
            elif MP4 not in self.mime_types: self.mime_types.append(MP4)
        
        file_dialog.setMimeTypeFilters(self.mime_types)
        default_mimetype= AVI if is_windows else MP4
        if default_mimetype in self.mime_types: file_dialog.selectedMimeTypeFilter(default_mimetype)

        movies_location= QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_location)
        if file_dialog.exec()== QDialog.Accepted:
            url= file_dialog.selectedUrls()[0]
            self.playlist.append(url)
            self.playlist_index= len(self.playlist)- 1
            self.player.setSource(url)
            self.player.play()
    
    @Slot()
    def ensure_stopped(self):
        if self.player.playbackState()!= QMediaPlayer.StoppedState:  self.player.stop()

    @Slot()
    def previous_clicked(self):
        # GO TO PREVIOUS TRACK IF WE ARE WITHIN THE FIRST 5 SECONDS OF PLAYBACK
        # OTHERWISE, SEEK TO THE BEGINNING
        if self.player.position()<= 5000 and self.playlist_index> 0:
            self.playlist_index-= 1
            self.playlist.previous()
            self.player.setSource(self.playlist[self.playlist_index])
        else: self.player.setPosition(0)
    
    @Slot()
    def next_clicked(self):
        if self.playlist_index< len(self.playlist)- 1:
            self.playlist_index+= 1
            self.player.setSource(self.playlist[self.playlist_index])
    
    @Slot("QMediaPlayer:: PlaybackState")
    def update_buttons(self, state):
        media_count= len(self.playlist)
        self.play_action.setEnabled(media_count> 0 and state!= QMediaPlayer.PlayingState)
        self.pause_action.setEnabled(state== QMediaPlayer.PlayingState)
        self.stop_action.setEnabled(state!= QMediaPlayer.StoppedState)
        self.previous_action.setEnabled(self.player.position()> 0)
        self.next_action.setEnabled(media_count> 1)
    
    def show_status_message(self, message): self.statusBar().showMessage(messge, 5000)

    @Slot()
    def player_error(self, error, error_string):
        print(error_string, file= sys.stderr)
        self.show_status_message(error_string)


if __name__== "__main__":
    app= QApplication(sys.argv)
    mainWindow= MainWindow()
    available_geometry= mainWindow.screen().availableGeometry()
    mainWindow.resize(available_geometry.width()/ 3, available_geometry.height()/ 2)

    mainWindow.show()
    sys.exit(app.exec())


