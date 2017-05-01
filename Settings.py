import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon


class SettingsForAccountGrid(QGridLayout):

    def __init__(self):
        super().__init__()
        self.initGrid()

    def initGrid(self):
        pass


class SettingsForAccount(QWidget):

    def __init__(self, user):
        super().__init__()
        self.user = user
        self.layout = SettingsForAccountGrid()

        self.addWidgets()
        self.initUI()

    def addWidgets(self):
        groupLabel = QLabel('Группа')
        groupTextEdit = QTextEdit()
        groupTextEdit.setMaximumSize(250, 25)
        self.layout.addWidget(groupLabel, 0, 0)
        self.layout.addWidget(groupTextEdit, 0, 1)

        postLabel = QLabel('Пост')
        postTextEdit = QTextEdit()
        postTextEdit.setMaximumSize(250, 25)
        self.layout.addWidget(postLabel, 1, 0)
        self.layout.addWidget(postTextEdit, 1, 1)

        commentaryLabel = QLabel('Комментарий')
        commentaryTextEdit = QTextEdit()
        self.layout.addWidget(commentaryLabel, 2, 0)
        self.layout.addWidget(commentaryTextEdit, 2, 1, 50, 50)

    def initUI(self):
        self.setWindowIcon(QIcon('resources/icon.jpg'))
        self.setLayout(self.layout)
        self.setWindowTitle('NetherDrake')
        self.resize(658, 324)
        self.show()
