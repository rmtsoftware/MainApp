# Required python packages
from PySide6.QtCore import QThreadPool, Slot, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# User-defined packages
from src.server.server import ServerThread
from mainwindow import Ui_MainWindow

# System package
import sys

# Constants
ZERO = '0'
ERROR_TITLE = "Внимание"
ERROR_MESSAGE = "Сервер не запущен"
WARNING_BUTTON = QMessageBox.StandardButton.Ok


class Base(QMainWindow):  # renaming the class for more clarity
    msg_to_terminal = Signal(dict, str)
    telemetry_to_operator = Signal(str)

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setting Button Stats
        self.ui.btn_server_start.setDisabled(False)
        self.ui.btn_server_stop.setDisabled(True)

        # Signals on Button Click
        self.ui.btn_server_start.clicked.connect(self.start_server)
        self.ui.btn_server_stop.clicked.connect(self.stop_server)

        self.pool = QThreadPool.globalInstance()
        self.set_zero_values()

    def set_zero_values(self):
        zero_labels = [self.ui.lb_latitude_val, self.ui.lb_NS_val, self.ui.lb_longitude_val,
                       self.ui.lb_EW_val, self.ui.lb_altitude_val, self.ui.lb_grndspeed_val,
                       self.ui.lb_axl_x_val, self.ui.lb_axl_y_val, self.ui.lb_axl_z_val,]

        for label in zero_labels:
            label.setText(ZERO)  # Introduced Constant 'ZERO'

    # Renaming start and stop with more context
    def start_server(self):
        self.server = ServerThread()
        self.pool.start(self.server)

        # signals from the thread
        self.server.signals.started.connect(self.server_started_actions)
        self.server.signals.connection_timeout.connect(self.timeout_actions)
        self.server.signals.data_received.connect(self._process_rcv_data)
        self.server.signals.data_sent.connect(self._process_snd_data)

    def stop_server(self):
        try:
            self.server.conn.shutdown(0)
            self.set_zero_values()
            self.server.conn = None
            self.server.addr = None
            self.ui.btn_motor_start.setEnabled(True)
            self.ui.btn_motor_stop.setEnabled(False)
        except AttributeError as _:
            self.display_error()
        except OSError as e:
            self.display_error()
        finally:
            self.server_stopped_actions()

    # ... Rest of the Class ...

    def server_started_actions(self):
        self.ui.btn_server_start.setDisabled(True)
        self.ui.btn_server_stop.setDisabled(False)

    def server_stopped_actions(self):
        self.ui.btn_server_start.setDisabled(False)
        self.ui.btn_server_stop.setDisabled(True)

    @staticmethod
    def timeout_actions(self):
        QMessageBox.critical(None, "Ошибка", "Таймаут подключения",
                             QMessageBox.StandardButton.Ok)

    @staticmethod
    def display_error(self):
        print('Сервер не запущен, чтобы его останавливать')
        QMessageBox.warning(None, ERROR_TITLE, ERROR_MESSAGE, WARNING_BUTTON)

    @Slot(object)
    def _process_snd_data(self, data):
        self.msg_to_terminal.emit(data, "SEND")

    @Slot(object)
    def _process_rcv_data(self, data):
        self.msg_to_terminal.emit(data, "RCVD")
        if "status" in data and data["status"] == "RESPONSE":
            if "GPSRESPONSE" in data["msg_data"]:
                self.telemetry_to_operator.emit(data["msg_data"]["GPSRESPONSE"])
            if "IMURESPONSE" in data["msg_data"]:
                self.telemetry_to_operator.emit(data["msg_data"]["IMURESPONSE"])

    # ... Rest of the Class ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Base()  # renamed Base to MainWindowApp
    window.show()
    app.exec()
