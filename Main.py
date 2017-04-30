import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QCheckBox, QLabel, QGridLayout, QTableWidget,
                             QTableWidgetItem)
from PyQt5.QtGui import QIcon, QColor


class Account:

    def __init__(self, vk_id, login, password, status, enabled):
        self.id = vk_id
        self.login = login
        self.password = password
        self.status = status
        self.enabled = enabled


class MainGrid(QGridLayout):

    def __init__(self):
        super().__init__()
        self.initGrid()

    def initGrid(self):
        pass


class AccountsTable(QTableWidget):

    def __init__(self):
        super().__init__()
        self.initTable()

    def initTable(self):
        self.horizontalHeader().hide()
        self.verticalHeader().hide()

        self.setAcceptDrops(True)
        self.setDragEnabled(True)

        self.setRowCount(10)
        self.setColumnCount(6)
        self.setItem(0, 0, QTableWidgetItem("Номер"))
        self.setItem(0, 1, QTableWidgetItem("Логин"))
        self.setItem(0, 2, QTableWidgetItem("Пароль"))
        self.setItem(0, 3, QTableWidgetItem("Статус"))
        self.setItem(0, 4, QTableWidgetItem("Настройки"))
        self.setItem(0, 5, QTableWidgetItem("Вкл/Выкл"))

        for i in range(9):
            button = QPushButton(f'Настройки {i+1}')
            button.clicked.connect(self.pressedSettings)
            self.setCellWidget(i+1, 4, button)

        for i in range(9):
            button = QPushButton(f'Вкл/Выкл {i+1}')
            button.setCheckable(True)
            button.clicked.connect(self.pressedButtonOnOff)
            self.setCellWidget( i+1, 5, button)

    def pressedSettings(self, event):
        sender = int(self.sender().text()[-1])
        try:
            current_account_id = self.item(sender, 0).text()
            current_account_login = self.item(sender, 1).text()
            current_account_password = self.item(sender, 2).text()
            current_account_status = self.item(sender, 3).text()
            if current_account_id == '' or current_account_login == '' or current_account_password == ''\
                                                                        or current_account_status == '':
                raise Exception
            print(current_account_id, current_account_login, current_account_password, current_account_status)
            self.cellWidget(sender, 4).setStyleSheet("background-color: #E1E1E1")
        except:
            self.cellWidget(sender, 4).setStyleSheet("background-color: red")

    def pressedButtonOnOff(self, event):
        sender = self.sender().text()[-1]

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.grid = MainGrid()
        self.table = AccountsTable()
        self.addButton = QPushButton()

        self.addWidgets()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('resources/icon.jpg'))
        self.setLayout(self.grid)
        self.setWindowTitle('NetherDrake')
        self.resize(625, 325)
        self.show()

    def addWidgets(self):
        self.grid.addWidget(self.table, 0, 0, 0, 4)
        self.grid.addWidget(self.addButton, 0, 1, 0, 0)
        self.addButton.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
