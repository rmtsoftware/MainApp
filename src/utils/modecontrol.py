from src.utils.telemetrygetter import TelemetryGetter
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QTimer
from enum import Enum
import sys


class ControlMode(Enum):
    MANUAL = 'Manual'
    REMOTE = 'Remote'
    AUTO = 'Autonomous'
    UNDEFINED = 'Not Selected'


class ModeController(TelemetryGetter):
    def __init__(self):
        super().__init__()

        self.mode = ControlMode.UNDEFINED

        self.mode_timer = QTimer()
        self.mode_timer.timeout.connect(self._rmode)
        self.mode_timer.start(500)

        self.ui.btn_mnl_mode.clicked.connect(self.set_manual_mode)  # Кнопкка выбора ручного режима
        self.ui.btn_rmt_mode.clicked.connect(self.set_remote_mode)  # Кнопка выбора дистанционного режима управления

    def _rmode(self):

        try:
            if self.server.conn == None:
                self.ui.lb_status_val.setText('Не подключен')
            else:
                self.ui.lb_status_val.setText(str(self.server.addr[0]))
        except AttributeError as _:
            self.ui.lb_status_val.setText('Не подключен')

        self.ui.lb_rmode_val.setText(self.mode.value)

    def set_manual_mode(self) -> None:
        """Ручной режим управления аппаратом (с ПО)"""
        if self.mode == ControlMode.MANUAL:
            self.mode = ControlMode.UNDEFINED
        else:
            self.mode = ControlMode.MANUAL
            self.server.signals.set_mode.emit('MAN')

    def set_remote_mode(self) -> None:
        """Удаленый режим управления аппаратом (с пульта)"""
        if self.mode == ControlMode.REMOTE:
            self.mode = ControlMode.UNDEFINED
        else:
            self.mode = ControlMode.REMOTE
            self.server.signals.set_mode.emit('RMT')

    def set_auto_mode(self) -> None:
        """Автоматический режим управления аппаратом"""
        QMessageBox.warning(None,
                            "Упсссс....",
                            "Этот режим ещё не готов. Принесите программисту сгущёнки",
                            QMessageBox.StandardButton.Ok)
        self.mode = ControlMode.UNDEFINED


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeController()
    window.show()
    app.exec()
