import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon

import vk

from SettingsForAccount import SettingsForAccount
from Settings import SettingsWindow


ID_APP = '5892536'

# глобальные переменные - это зло
users = []


class Account:

    def __init__(self, number, login, password, status, enabled, group, post, commentary):
        self.number = number
        self.login = login
        self.password = password
        self.status = status
        self.enabled = enabled
        self.group = group
        self.post = post
        self.commentary = commentary


class MainGrid(QGridLayout):

    def __init__(self):
        super().__init__()
        self.initGrid()

    def initGrid(self):
        pass


class AccountsTable(QTableWidget):

    def __init__(self):
        super().__init__()
        self.size = 10
        self.initTable()

    def initTable(self):
        self.horizontalHeader().hide()
        self.verticalHeader().hide()

        self.setAcceptDrops(True)
        self.setDragEnabled(True)

        self.setRowCount(self.size)
        self.setColumnCount(6)
        self.setItem(0, 0, QTableWidgetItem("Имя"))
        self.setItem(0, 1, QTableWidgetItem("Логин"))
        self.setItem(0, 2, QTableWidgetItem("Пароль"))
        self.setItem(0, 3, QTableWidgetItem("Статус"))
        self.setItem(0, 4, QTableWidgetItem("Настройки"))
        self.setItem(0, 5, QTableWidgetItem("Вкл/Выкл"))

        for i in range(9):
            self.setItem(i+1, 0, QTableWidgetItem(str(i+1)))

        for i in range(9):
            self.setItem(i+1, 3, QTableWidgetItem('Не работает'))

        for i in range(9):
            button = QPushButton(f'Настройки {i+1}')
            button.setStyleSheet("background-color: #E1E1E1")
            button.clicked.connect(self.pressedSettings)
            self.setCellWidget(i+1, 4, button)

        for i in range(9):
            button = QPushButton(f'Вкл/Выкл {i+1}')
            button.setStyleSheet("background-color: #E1E1E1")
            button.setCheckable(True)
            button.clicked.connect(self.pressedButtonOnOff)
            self.setCellWidget(i+1, 5, button)

    def addRow(self):
        self.size += 1
        self.setRowCount(self.size)

        self.setItem(self.size-1, 0, QTableWidgetItem(str(self.size-1)))
        self.setItem(self.size-1, 3, QTableWidgetItem('Не работает'))

        button = QPushButton(f'Настроки {self.size-1}')
        button.setStyleSheet("background-color: #E1E1E1")
        button.clicked.connect(self.pressedSettings)
        self.setCellWidget(self.size-1, 4, button)

        button = QPushButton(f'Вкл/Выкл {self.size-1}')
        button.setStyleSheet("background-color: #E1E1E1")
        button.setCheckable(True)
        button.clicked.connect(self.pressedButtonOnOff)
        self.setCellWidget(self.size-1, 5, button)

    def getRowInformation(self, sender) -> tuple:
        current_account_id = self.item(sender, 0).text()
        current_account_login = self.item(sender, 1).text()
        current_account_password = self.item(sender, 2).text()
        current_account_status = self.item(sender, 3).text()
        if current_account_id == '' or current_account_login == '' or current_account_password == '' \
                or current_account_status == '':
            raise Exception
        return current_account_id, current_account_login, current_account_password, current_account_status

    def pressedSettings(self, event):
        sender = int(self.sender().text().split(' ')[-1])
        try:
            current_account_id, current_account_login, current_account_password, current_account_status = \
                self.getRowInformation(sender)
            self.cellWidget(sender, 4).setStyleSheet("background-color: #E1E1E1")
            user = Account(current_account_id, current_account_login, current_account_password, current_account_status,
                           True, 0, 0, 0)
            users.append(user)
            self.createSettingsForAccountWindow(user)
        except:
            self.cellWidget(sender, 4).setStyleSheet("background-color: red")

    @staticmethod
    def createSettingsForAccountWindow(user):
        global settingsForAccountWindow
        settingsForAccountWindow = SettingsForAccount(user)

    def pressedButtonOnOff(self, event):
        if event:
            try:
                sender = int(self.sender().text().split(' ')[-1])
                for user in users:
                    if int(user.number) == int(sender):
                        try:
                            self.doCommentaries(user)
                        except:
                            break
            except:
                self.cellWidget(sender, 4).setStyleSheet("background-color: red")
        else:
            pass

    def doCommentaries(self, user):
        number = str(user.number)
        login = str(user.login)
        password = str(user.password)
        status = str(user.status)
        enabled = str(user.enabled)
        group = str(user.group)
        post = str(user.post)
        commentary = str(user.commentary)

        # This one is for test
        # number = '242757858'
        # login = '79048284618'
        # password = 'SJtVePtF'
        # post = '182'
        # commentary = 'ТЕСТИРУЕМ'

        while True:
            print(login, password, group, post, commentary)
            session = vk.AuthSession(ID_APP, login, password, scope='groups, wall')
            vkAPI = vk.API(session)
            comments = vkAPI.wall.createComment(owner_id=group, post_id=post, message=commentary)
            print(comments)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.grid = MainGrid()
        self.table = AccountsTable()
        self.addButton = QPushButton()
        self.deleteButton = QPushButton()
        self.settingsButton = QPushButton()

        self.initButtons()
        self.addWidgets()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('resources/icon.jpg'))
        self.setLayout(self.grid)
        self.setWindowTitle('VKcomments')
        self.resize(675, 325)
        self.setMinimumSize(675, 325)
        self.show()

    def initButtons(self):
        self.addButton.setIcon(QIcon('resources/plus.png'))
        self.addButton.clicked.connect(self.pressedAddButton)

        self.deleteButton.setIcon(QIcon('resources/minus.png'))
        self.deleteButton.clicked.connect(self.pressedDeleteButton)

        self.settingsButton.setIcon(QIcon('resources/six.png'))
        self.settingsButton.clicked.connect(self.pressedSettingsButton)

    def addWidgets(self):
        self.grid.addWidget(self.table, 0, 0, 4, 1)
        self.grid.addWidget(self.addButton, 0, 1)
        self.grid.addWidget(self.deleteButton, 1, 1)
        self.grid.addWidget(self.settingsButton, 2, 1)

    def pressedAddButton(self):
        self.table.addRow()

    def pressedDeleteButton(self):
        if self.table.size != 1:
            self.table.size -= 1
            self.table.removeRow(self.table.size)

    @staticmethod
    def pressedSettingsButton(self):
        global settingsWindow
        settingsWindow = SettingsWindow()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
