from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel
from qrcodegen.QRCodeUtils import GenerateQrCode
import os

class QRCodeWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.masterLayout = QVBoxLayout() 
        self.setLayout(self.masterLayout)

        configLayout = QHBoxLayout()
        self.masterLayout.addLayout(configLayout)
        configLayout.addWidget(QLabel("URL: "))
        self.URLLineEdit = QLineEdit() 
        configLayout.addWidget(self.URLLineEdit)
        iconPickBtn = QPushButton("Pick Center Icon")
        iconPickBtn.clicked.connect(self.IconPickBtnClicked)
        configLayout.addWidget(iconPickBtn)

        createButton = QPushButton("Create")
        createButton.clicked.connect(self.CreateButtonClicked)
        self.masterLayout.addWidget(createButton)

        self.imageFileDialogFilter = "Images (*.png *.jpg *.jpeg)"
        self.iconPath = None

    def IconPickBtnClicked(self):
        iconPath = QFileDialog.getOpenFileName(self, "PickIcon", "",self.imageFileDialogFilter)
        self.iconPath = iconPath[0]
        if os.path.exists(self.iconPath):
            pass
        else:
            self.iconPath = None

    def CreateButtonClicked(self):
        url:str = self.URLLineEdit.text()
        destination = QFileDialog.getSaveFileName(self, "Save File", "", self.imageFileDialogFilter)
        GenerateQrCode(destination[0], url, self.iconPath)


def RunGUI():
    app = QApplication()
    widget = QRCodeWidget()
    widget.show()
    app.exec()