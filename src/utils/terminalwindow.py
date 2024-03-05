from src.utils.manualkeyscontrol import ManualKeysControl
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QTimer, Slot
import sys
import datetime


class TerminalWindow(ManualKeysControl):
    def __init__(self):
        super().__init__()
        self.current_text: str = ""
        self.msg_to_terminal.connect(self.show_msg)

        self.terminal_cleaner = QTimer()  # таймер очистки содержимого терминала
        self.terminal_cleaner.timeout.connect(self._clean_by_timer)
        self.terminal_cleaner.start(300)

        self.ui.btn_clean_textBrw.clicked.connect(self._clean_by_button)

    def _clean_by_timer(self):
        if len(self.current_text) > 2000:
            self.current_text = ''

    def _clean_by_button(self):
        self.current_text = ''

    def _add_to_terminal(self, message):
        self.current_text = f'{message}' + self.current_text
        self.ui.terminal_window.setText(self.current_text)

    @Slot(object)
    def show_msg(self, data, msg_type):

        try:
            if data['msg_data'] == {} and data['cmd'] == []:
                return
        except KeyError:
            return

        if list(data['msg_data'].keys()) == ['INFO']:
            return

        message = self._create_message(data, msg_type)
        self._add_to_terminal(message)

    def _create_message(self, data, msg_type):
        message = self._current_time() + f' - {msg_type}' + '\n'
        try:
            if len(data['cmd']) != 0:
                message += 'CMD: '
                for command in data['cmd']:
                    message += f'{command} '
                message += '\n'
        except Exception as _:
            pass

        for key in data['msg_data']:
            value_string = f'{str(data["msg_data"][key])[:-4]}\n'
            if key in ['INFO', 'SETMODE', 'MANKEYCMD', 'MANLINECM']:
                value_string = f'{str(data["msg_data"][key])}\n'
            message += f'{key}: {value_string}'

        return message + '\n'

    @staticmethod
    def _current_time():
        return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TerminalWindow()
    window.show()
    app.exec()
