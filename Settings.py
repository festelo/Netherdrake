from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon


RUCAPTCHA_KEY = 'TEST'


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
        self.labelAntigate = QLabel('Ключ от RuCaptcha')
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

    def closeEvent(self, QCloseEvent):
        global RUCAPTCHA_KEY
        RUCAPTCHA_KEY = self.textEditAntigate.toPlainText()
