from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon


class SettingsGrid(QGridLayout):

    def __init__(self):
        super().__init__()
        self.initGrid()

    def initGrid(self):
        pass


class SettingsWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = SettingsGrid()
        self.labelAntigate = QLabel('Ключ от antigate')
        self.textEditAntigate = QTextEdit()

        self.addWidgets()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('resources/icon.jpg'))
        self.setLayout(self.layout)
        self.setWindowTitle('VKcomments')
        self.resize(658, 324)
        self.show()

    def addWidgets(self):
        self.layout.addWidget(self.labelAntigate, 0, 0)
        self.layout.addWidget(self.textEditAntigate, 0, 1)
        self.textEditAntigate.setMaximumSize(450, 25)
