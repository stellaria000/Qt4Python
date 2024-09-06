from PySide6.QtWebChannel import QWebChannelAbstractTransport
from PySide6.QtCore import QByteArray, QJsonDocument, Slot

class WebSocketTransport(QWebChannelAbstractTransport):
    '''
        QWebChannelAbstractSocket implementation using a QWebSocket internally.

        The transport delegates all messages received over the QWebSocket over
        its textMessageReceived signal. Analogously, all calls to
        sendTextMessage will be sent over the QWebSocket to the remote client
    '''

    def __del__(self):  self.socket.deleteLater()
    # DESTROYS THE WEBSOCKET TRANSPORT
    
    def disconnected(self): self.deleteLater()

    def sendMessage(self, message):
        # SERIALIZE THE JSON MESSAGE AND SEND IT AS A TEXT MESSAGE VIA THE WEBSOCKET TO THE CLIENT
        doc= QJsonDocument(message)
        json_message= str(doc.toJson(QJsonDocument.Compact), "utf-8")
        self.socket.sendTextMessage(json_message)

    @Slot(str)
    def text_message_received(self, message_data_in):
        # DESERIALIZE THE STRING FIELD JSON MESSAGE DATA AND EMIT MESSAGE RECEIVED
        message_data= QByteArray(bytes(message_data_in, encoding= 'utf-8'))
        message= QJsonDocument.fromJson(message_data)

        if message.isNull(): print("Failed to parse text message as JSON object: ", message_data)
        if not message.isObject(): 
            print("Received JSON message that is not an object: ", message_data)
            return 
        
        self.messageReceived.emit(message.object(), self)
