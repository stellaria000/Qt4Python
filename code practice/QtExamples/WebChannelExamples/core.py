from PySide6.QtCore import QObject, Signal, Slot

class Core(QObject):
    # AND INSTANCE OF THIS CLASS GETS PUBLISHED OVER THE WEBCHANNEL AND IS THEN ACCESSIBLE TO HTML CLIENTS
    sendText= Signal(str)

    def __init__(self, dialog, parent= None):
        super().__init__(parent)
        self.dialog= dialog
        self.dialog.send_text.connect(self.emit_send_text)

    @Slot(str)
    def emit_send_text(self, text): self.sendText.emit(text)

    @Slot(str)
    def receiveText(self, text): self.dialog.display_message(f"Received message: {text}")
