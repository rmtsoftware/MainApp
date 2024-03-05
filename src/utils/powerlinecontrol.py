from src.utils.motorcontrol import MotorController
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QTimer
import sys


class PowerLineController(MotorController):
    def __init__(self):
        super().__init__()
        self.pwr_mnl: int = 0
        self.reset_input_to_zero()
        self.ui.le_pwr_mnl.editingFinished.connect(self._handle_line_edit)

    def _handle_line_edit(self):
        """ Действия по окончанию изменения значения в lineEdit 'Задание мощности' """

        # Получение текста из области
        user_input = self.ui.le_pwr_mnl.text()

        if self._is_input_empty(user_input):
            self.reset_input_to_zero()
            return

        try:
            self.pwr_mnl = self._check_valid_range(int(user_input))
        except ValueError as _:
            self.reset_input_to_zero()
            return

        self.ui.le_pwr_mnl.setText(str(self.pwr_mnl))

    @staticmethod
    def _is_input_empty(user_input):
        return user_input == ''

    def reset_input_to_zero(self):
        self.pwr_mnl = 0
        self.ui.le_pwr_mnl.setText(str(self.pwr_mnl))

    @staticmethod
    def _check_valid_range(value):
        if value > 100 or value < 0:
            # Reset out of bound values to maximum or minimum limit respectively.
            return 100 if value > 100 else 0
        return value


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PowerLineController()
    window.show()
    app.exec()
