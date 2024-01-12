from modecontrol import ModeController
from PySide6.QtWidgets import QApplication
import sys

class MotorController(ModeController):
    def __init__(self):
        super().__init__()
        
        self.ui.btn_motor_start.setEnabled(True)
        self.ui.btn_motor_stop.setEnabled(False) 
        
        self.ui.btn_motor_start.clicked.connect(self.mtr_start_action)
        self.ui.btn_motor_stop.clicked.connect(self.mtr_stop_action)
        
    def mtr_start_action(self):
        try:
            if self.server.conn is not None:
                self.server.signals.mtr_cmd.emit('START')
                self.ui.btn_motor_start.setEnabled(False)
                self.ui.btn_motor_stop.setEnabled(True)
            else:
                pass
        except AttributeError as _:
            pass
    
    def mtr_stop_action(self):
        try:
            if self.server.conn is not None:
                self.server.signals.mtr_cmd.emit('STOP')
                self.ui.btn_motor_start.setEnabled(True)
                self.ui.btn_motor_stop.setEnabled(False)
            else:
                pass
        except AttributeError as _:
            pass
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MotorController()
    window.show()
    app.exec()
    