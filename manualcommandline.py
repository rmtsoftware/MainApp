from powerlinecontrol import PowerLineController
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QTimer
import sys


class ManualCommandLine(PowerLineController):
    def __init__(self):
        super().__init__()

        # отправка мануальной команды по нажатию клавиши "ENTER"
        self.ui.le_mnl_cmd.returnPressed.connect(self.send_mnl_cmd)
        # кнопка отправки мануальной команды
        self.ui.btn_mnl_cmd.clicked.connect(self.send_mnl_cmd)

    def send_mnl_cmd(self):

        # Проверка установлено ли соединение с клиентом
        # если нет, то функция возвращает None
        try:
            if self.server.conn is None:
                return
        except:
            return

        msg = str(self.ui.le_mnl_cmd.text())

        # Проверка на пустую строку
        # если строка пустая, то функция возвращает None
        if msg == "":
            return

        # добавляем к строке 
        full_str = msg + '\r\n'

        self.server.signals.man_commandline.emit(full_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManualCommandLine()
    window.show()
    app.exec()
