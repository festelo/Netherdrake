from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTextEdit
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

        self.groupLabel = QLabel('Группа')
        self.groupTextEdit = QTextEdit()
        self.groupTextEdit.setText(str(user.group))

        self.postLabel = QLabel('Пост')
        self.postTextEdit = QTextEdit()
        self.postTextEdit.setText(str(user.post))

        self.commentaryLabel = QLabel('Комментарий')
        self.commentaryTextEdit = QTextEdit()
        self.commentaryTextEdit.setText(str(user.commentary))

        self.intervalLabel = QLabel('Интервал (в секундах)')
        self.intervalTextEdit = QTextEdit()
        self.intervalTextEdit.setText(str(user.interval))

        self.layout = SettingsForAccountGrid()

        self.addWidgets()
        self.initUI()

    def addWidgets(self):
        self.groupTextEdit.setMaximumSize(250, 25)
        self.layout.addWidget(self.groupLabel, 0, 0, 1, 1)
        self.layout.addWidget(self.groupTextEdit, 0, 1)

        self.postTextEdit.setMaximumSize(250, 25)
        self.layout.addWidget(self.postLabel, 1, 0)
        self.layout.addWidget(self.postTextEdit, 1, 1)

        self.layout.addWidget(self.commentaryLabel, 2, 0)
        self.layout.addWidget(self.commentaryTextEdit, 2, 1, 50, 50)

        self.intervalTextEdit.setMaximumSize(50, 25)
        self.layout.addWidget(self.intervalLabel, 53, 0)
        self.layout.addWidget(self.intervalTextEdit, 53, 1)

    def initUI(self):
        self.setWindowIcon(QIcon('resources/icon.jpg'))
        self.setLayout(self.layout)
        self.setWindowTitle('VKcomments')
        self.resize(658, 324)
        self.show()

    def closeEvent(self, QCloseEvent):
        self.user.group = self.groupTextEdit.toPlainText()
        self.user.post = self.postTextEdit.toPlainText()
        self.user.commentary = self.commentaryTextEdit.toPlainText()
        self.user.interval = self.intervalTextEdit.toPlainText()
