from manualcommandline import ManualCommandLine
from modecontrol import ControlMode
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
import sys


class ManualKeysControl(ManualCommandLine):
    def __init__(self):
        super().__init__()

    def emit_server_signal(self, cmds_character):
        cmds = cmds_character + str(self.pwr_mnl)
        self.server.signals.man_key_control.emit(cmds)

    def keyPressEvent(self, event):
        try:
            if self.server.conn is None:
                return
        except:
            return
        if self.mode != ControlMode.MANUAL:
            return
        key_press = event.key()
        if key_press == Qt.Key.Key_W:
            self.emit_server_signal('F')
        elif key_press == Qt.Key.Key_S:
            self.emit_server_signal('B')
        elif key_press == Qt.Key.Key_A:
            self.emit_server_signal('L')
        elif key_press == Qt.Key.Key_D:
            self.emit_server_signal('R')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManualKeysControl()
    window.show()
    app.exec()
