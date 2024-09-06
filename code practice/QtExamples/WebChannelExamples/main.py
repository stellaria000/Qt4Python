import os 
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QDesktopServices
from PySide6.QtNetwork import QHostAddress, QSslSocket
from PySide6.QtCore import (QFile, QFileInfo, QUrl)
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebSockets import QWebSocketServer

from dialog import *
from core import Core
from websoketclientwrapper import WebSocketClientWrapper

if __name__== '__main__':
    app= QApplication(sys.argv)

    if not QSslSocket.supportsSsl():
        print('The example requires SSL support')
        sys.exit(-1)
    
    cur_dir= os.path.dirname(os.path.abspath(__file__))
    js_file_info= QFileInfo(f"{cur_dir}/qwebchannel.js", js_file_info.absoluteFilePath())

    # SETUP THE QWEBSOCKETSERVER
    server= QWebSocketServer("QWebChannel Standalone Example Server", QWebSocketServer.NonSecureMode)
    if not server.listen(QHostAddress.LocalHost, 12345): 
        print("Failed to open web socket server.")
        sys.exit(-1)
    
    # WRAP WEBSOCKET CLIENTS IN QWEBCHANNEL ABSTRACT TRANSPORT OBJECTS
    client_wrapper= WebSocketClientWrapper(server)

    # SETUP THE CHANNEL 
    channel= QWebChannel()
    client_wrapper.client_connected.connect(channel.connectTo)

    # SETUP THE UI
    dialog= Dialog()

    # SETUP TH ECORE AND PUBLISH IT TO THE QWEBCHANNEL  
    core= Core(dialog)
    channel.registerObject("core", core)

    # OPEN A BROWSER WINDWO WITH THE CLIENT HTML PAGE
    url= QUrl.fromLocalFile(f"{cur_dir}/index.html")
    QDesktopServices.openUrl(url)

    display_url= url.toDisplayString()
    message= f"initialization complete, opening browser at {display_url}"
    
    dialog.display_message(message)
    dialog.show()

    sys.exit(app.exec())