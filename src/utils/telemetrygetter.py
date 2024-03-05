from src.utils.base import Base
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QTimer
import sys


class TelemetryGetter(Base):
    def __init__(self):
        super().__init__()
        self._auto_state = {'gps': 0, 'imu': 0}  # состояние комбо бокса gps, imu
        self.ui.btn_gps.clicked.connect(lambda _: self.request_telemetry('gps'))
        self.ui.btn_imu.clicked.connect(lambda _: self.request_telemetry('imu'))
        self.ui.cb_auto_gps.stateChanged.connect(lambda _: self.update_auto_state('gps'))
        self.ui.cb_auto_imu.stateChanged.connect(lambda _: self.update_auto_state('imu'))
        self.auto_request_timer = QTimer()  # таймер автозапроса телеметрии
        self.auto_request_timer.timeout.connect(self.auto_request_telemetry)
        self.auto_request_timer.start(300)

    def update_auto_state(self, telemetrytype):
        if self.ui.__dict__[f'cb_auto_{telemetrytype}'].checkState() == Qt.CheckState.Unchecked:
            self._auto_state[telemetrytype] -= 1
        elif self.ui.__dict__[f'cb_auto_{telemetrytype}'].checkState() == Qt.CheckState.Checked:
            self._auto_state[telemetrytype] += 1

    def auto_request_telemetry(self):
        try:
            if self.server.conn is not None:
                for telemetrytype in ['gps', 'imu']:
                    if self._auto_state[telemetrytype] == 1:
                        self.ui.__dict__[f'btn_{telemetrytype}'].setEnabled(False)
                        self.request_telemetry(telemetrytype)
                    elif self._auto_state[telemetrytype] == 0:
                        self.ui.__dict__[f'btn_{telemetrytype}'].setEnabled(True)
        except AttributeError as _:
            pass

    def request_telemetry(self, telemetrytype):
        self.server.signals.__dict__[f'get_{telemetrytype}'].emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelemetryGetter()
    window.show()
    app.exec()
