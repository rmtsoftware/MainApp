from src.utils.motorcontrol import MotorController
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QTimer
import sys


class PowerLineController(MotorController):
    def __init__(self):
        super().__init__()
        self.pwr_mnl: int = 0
        self.reset_input_to_zero()
        self.ui.hs_pwr_mtr.valueChanged.connect(self.on_value_changed)
        self.ui.btn_pwr_reset.clicked.connect(self.reset_input_to_zero)

    def on_value_changed(self, value: int):
        self.pwr_mnl = value
        self.ui.lb_pwr_mtr.setText(str(value))

    def reset_input_to_zero(self):
        self.ui.hs_pwr_mtr.setValue(0)
        self.ui.lb_pwr_mtr.setText('0')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PowerLineController()
    window.show()
    app.exec()
