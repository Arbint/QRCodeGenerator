from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox
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

        versionLayout = QHBoxLayout()
        self.masterLayout.addLayout(versionLayout)
        versionLayout.addWidget(QLabel("Version (1=smallest, 40=largest):"))
        self.versionSpinBox = QSpinBox()
        self.versionSpinBox.setRange(1, 40)
        self.versionSpinBox.setValue(1)
        self.versionSpinBox.setToolTip("Controls QR code density. Version 1 = auto (smallest that fits). Higher versions add more modules.")
        versionLayout.addWidget(self.versionSpinBox)
        versionLayout.addStretch()

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
        GenerateQrCode(destination[0], url, self.iconPath, version=self.versionSpinBox.value())


def RunGUI():
    app = QApplication()
    widget = QRCodeWidget()
    widget.show()
    app.exec()