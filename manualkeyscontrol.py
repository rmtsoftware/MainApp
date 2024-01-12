from manualcommandline import ManualCommandLine
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QTimer
import sys


class ManualKeysControl(ManualCommandLine):
    def __init__(self):
        super().__init__()
        
    def keyPressEvent(self, event):
        
        try:
            if self.server.conn is None:
                return
        except:
            return
        
        if self._flag_man_mode == -1:
            return 
        
        key_press = event.key()

        if key_press == Qt.Key.Key_W:
            cmds = 'F' + str(self.pwr_mnl)
            self.server.signals.man_key_control.emit(cmds)
        if key_press == Qt.Key.Key_S:
            cmds = 'B' + str(self.pwr_mnl)
            self.server.signals.man_key_control.emit(cmds)
        if key_press == Qt.Key.Key_A:
            cmds = 'L' + str(self.pwr_mnl)
            self.server.signals.man_key_control.emit(cmds)
        if key_press == Qt.Key.Key_D:
            cmds = 'R' + str(self.pwr_mnl)
            self.server.signals.man_key_control.emit(cmds)
        
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManualKeysControl()
    window.show()
    app.exec()
    