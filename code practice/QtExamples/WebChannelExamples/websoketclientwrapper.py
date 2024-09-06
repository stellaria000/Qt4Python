from PySide6.QtCore import QObject, Signal, Slot
from websockettransport import WebSocketTransport

class WebSocketClientWrapper(QObject):
    '''
        WRAPS CONNECTED Q WEB SOCKETS CLIENTS IN WEBSOCKET TRANSPORT OBJECTS.
        
        THIS CODE IS ALL THAT IS REQUIRED TO CONNECT INCOMING WEBSOCKETS TO THE WEBCHANNEL.
        ANY KIND OF REMOTE JAVASCRIPT CLIENT THAT SUPPORTS WEBSOCKETS CAN THUS RECEIBE MESSAGES AND 
        ACCESS THE PUBLISHED OBJECTS.
    '''

    client_connected= Signal(WebSocketTransport)

    def __init__(self, server, parent= None):
        '''
            CONSTRUCT THE CLIENT WRAPPER WITH THE GIVEN PARENT. ALL CLIENTS CONNECTING TO THE
            QWEBSOCKET SERVER WILL BE AUTOMATICALLY WRAPPED IN WEBSOCKET TRANSPORT OBJECTS
        '''

        super().__init__(parent)
        
        self.server= server
        server.server.newConnection.connect(self.handle_new_connection)
        self.transports= []

    @Slot()
    def handle_new_connection(self):
        # WRAP AN INCOMING WEBSOCKET CONNECTION IN A WEBSOCKET TRANSPORT OBJECT
        socket= self.server.nextPendingConnection()
        transport= WebSocketTransport(socket)
        self.transports.append(transport)
        self.client_connected.emit(transport)