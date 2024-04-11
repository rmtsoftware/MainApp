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
        self.telemetry_flag = 0

    def update_auto_state(self, telemetrytype):
        if self.ui.__dict__[f'cb_auto_{telemetrytype}'].checkState() == Qt.CheckState.Unchecked:
            self._auto_state[telemetrytype] -= 1
        elif self.ui.__dict__[f'cb_auto_{telemetrytype}'].checkState() == Qt.CheckState.Checked:
            self._auto_state[telemetrytype] += 1

    def auto_request_telemetry(self):
        try:

            if self.server.conn is not None:

                if self._auto_state["gps"] == 1:
                    self.ui.btn_gps.setEnabled(False)
                else:
                    self.ui.btn_gps.setEnabled(True)

                if self._auto_state["imu"] == 1:
                    self.ui.btn_imu.setEnabled(False)
                else:
                    self.ui.btn_imu.setEnabled(True)

                if self.telemetry_flag == 0 and self._auto_state['gps'] and self._auto_state['imu']:
                    self.server.signals.get_gps.emit()
                    self.telemetry_flag += 1
                    return
                
                if self.telemetry_flag == 1 and self._auto_state['imu'] and self._auto_state['gps']:
                    self.server.signals.get_imu.emit()
                    self.telemetry_flag -= 1
                    return
                
                if self._auto_state['imu'] and not self._auto_state['gps']:
                    self.server.signals.get_imu.emit()
                    return
                
                if self._auto_state['gps'] and not self._auto_state['imu']:
                    self.server.signals.get_gps.emit()
                    return

        except AttributeError as _:
            pass

    def request_telemetry(self, telemetrytype):
        self.server.signals.__dict__[f'get_{telemetrytype}'].emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelemetryGetter()
    window.show()
    app.exec()
