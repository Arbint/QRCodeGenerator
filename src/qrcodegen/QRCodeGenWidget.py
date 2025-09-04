from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel
from qrcodegen.QRCodeUtils import GenerateQrCode

class QRCodeWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.masterLayout = QVBoxLayout() 
        self.setLayout(self.masterLayout)

        self.masterLayout.addWidget(QLabel("URL: "))
        self.URLLineEdit = QLineEdit() 
        self.masterLayout.addWidget(self.URLLineEdit)

        createButton = QPushButton("Create")
        createButton.clicked.connect(self.CreateButtonClicked)
        self.masterLayout.addWidget(createButton)

    def CreateButtonClicked(self):
        url:str = self.URLLineEdit.text()
        destination = QFileDialog.getSaveFileName(self, "Save File")
        GenerateQrCode(destination[0], url)

def RunGUI():
    app = QApplication()
    widget = QRCodeWidget()
    widget.show()
    app.exec()