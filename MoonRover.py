import sys
import requests
from PySide6 import QtWidgets,QtGui,QtCore

class Mywidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button=QtWidgets.QPushButton("Click on me to get the Image")
        self.text=QtWidgets.QLabel("Hello Scientist",alignment=QtCore.Qt.AlignCenter)
        self.setWindowTitle("NASA MoonRover")
        self.layout=QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
app= QtWidgets.QApplication([])
widget=Mywidget()
widget.resize(800,500)
widget.show()
app.exec()