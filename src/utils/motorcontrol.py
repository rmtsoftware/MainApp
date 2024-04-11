from src.utils.modecontrol import ModeController
from PySide6.QtWidgets import QApplication
import sys


class MotorController(ModeController):
    def __init__(self):
        super().__init__()
        #self.set_button_states(True, False)
        self.ui.btn_motor_start.clicked.connect(self.mtr_start_action)
        self.ui.btn_motor_stop.clicked.connect(self.mtr_stop_action)

    def mtr_start_action(self):
        if self.is_server_connected():
            self.server.signals.mtr_cmd.emit('START')
            #self.set_button_states(False, True)

    def mtr_stop_action(self):
        if self.is_server_connected():
            self.server.signals.mtr_cmd.emit('STOP')
            #self.set_button_states(True, False)

    def is_server_connected(self):
        try:
            return self.server.conn is not None
        except AttributeError:
            return False

    def set_button_states(self, start, stop):
        self.ui.btn_motor_start.setEnabled(start)
        self.ui.btn_motor_stop.setEnabled(stop)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MotorController()
    window.show()
    app.exec()
