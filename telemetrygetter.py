from base import Base
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QTimer
import sys


class TelemetryGetter(Base):
    def __init__(self):
        super().__init__()
        
        self._state_cb_gps = 0 # состояние комбо бокса gps
        self._state_cb_imu = 0 # состояние комбо бокса imu
        
        self.ui.btn_gps.clicked.connect(self._get_gps) # кнопка ручного запроса gps
        self.ui.btn_imu.clicked.connect(self._get_imu) # кнопка ручного запроса imu
        
        self.ui.cb_auto_gps.stateChanged.connect(self._auto_gps_actions) # комбо бокс авто gps
        self.ui.cb_auto_imu.stateChanged.connect(self._auto_imu_actions) # комбо бокс авто imu
        
        self.auto_rqst_timer = QTimer() # таймер автозапроса телеметрии
        self.auto_rqst_timer.timeout.connect(self._auto_request)
        self.auto_rqst_timer.start(300)
     
        
    def _auto_gps_actions(self):
        if self.ui.cb_auto_gps.checkState() == Qt.CheckState.Unchecked:
            self._state_cb_gps -= 1            
        if self.ui.cb_auto_gps.checkState() == Qt.CheckState.Checked:
            self._state_cb_gps += 1 


    def _auto_imu_actions(self):
        if self.ui.cb_auto_imu.checkState() == Qt.CheckState.Unchecked:
            self._state_cb_imu -= 1    
        if self.ui.cb_auto_imu.checkState() == Qt.CheckState.Checked:
            self._state_cb_imu += 1
      
            
    def _auto_request(self):
        
        #if self.port.isOpen():
        try:
            if self.server.conn is not None:
                
                if self._state_cb_gps == 1 and self._state_cb_imu == 0:
                    self._get_gps()
                    self.ui.btn_gps.setEnabled(False)
                else:
                    self.ui.btn_gps.setEnabled(True)


                if self._state_cb_imu == 1 and self._state_cb_gps == 0:
                    self._get_imu()
                    self.ui.btn_imu.setEnabled(False)
                else:
                    self.ui.btn_imu.setEnabled(True)


                if self._state_cb_imu == 1 and self._state_cb_gps == 1:
                    self.ui.btn_imu.setEnabled(False)
                    self.ui.btn_gps.setEnabled(False)

                    self._get_gps()
                    QTimer.singleShot(200, self._get_imu)
                    
                if self._state_cb_imu == 0 and self._state_cb_gps == 0:
                    self.ui.btn_imu.setEnabled(True)
                    self.ui.btn_gps.setEnabled(True)
        except AttributeError as _:
            pass
      
        
    def _get_gps(self):
        self.server.signals.get_gps.emit()


    def _get_imu(self):
        self.server.signals.get_imu.emit()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelemetryGetter()
    window.show()
    app.exec()