from telemetrygetter import TelemetryGetter
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QTimer
import sys

class ModeController(TelemetryGetter):
    def __init__(self):
        super().__init__()
        
        self.mode_timer = QTimer()
        self.mode_timer.timeout.connect(self._rmode)
        self.mode_timer.start(500)
        
        # вспомогательные флаги выбора режима
        self._flag_man_mode = -1  # ручной
        self._flag_rmt_mode = -1 # дистанционный
        self._flag_auto_mode = -1 # автономный
        
        # Кнопкка выбора ручного режима
        self.ui.btn_mnl_mode.clicked.connect(self._manual_mode)
        # Кнопка выбора автономного режима управления
        self.ui.btn_auto_mode.clicked.connect(self._auto_mode)
        # Кнопка выбора дистанционного режима управления
        self.ui.btn_rmt_mode.clicked.connect(self._remote_mode)
       
       
    def _rmode(self):
        
        try:
            if self.server.conn == None:
                self.ui.lb_status_val.setText('Не подключен')
            else:
                self.ui.lb_status_val.setText(str(self.server.addr[0]))
        except AttributeError as _:
            self.ui.lb_status_val.setText('Не подключен')
        
        
        if self._flag_man_mode == -1:
            self.ui.lb_rmode_val.setText('Не выбрано') 
        if self._flag_man_mode == 1:
            self.ui.lb_rmode_val.setText('Ручной')
        if self._flag_rmt_mode == 1:
            self.ui.lb_rmode_val.setText('Дистанционный')    
        if self._flag_auto_mode == 1:
            self.ui.lb_rmode_val.setText('Автономный')
        
        try:   
            if (self._flag_man_mode == -1 
                and self._flag_man_mode == -1 
                and self._flag_auto_mode == -1):
                self.server.signals.set_mode.emit('NAN')
        except AttributeError as _:
            pass
            
        
    def _manual_mode(self) -> None:
        """Ручной режим управления аппаратом (с ПО)""" 
        self._flag_rmt_mode = -1
        self._flag_auto_mode = -1
        self._flag_man_mode *= -1
        
        self.server.signals.set_mode.emit('MAN')

        #if self._fMan_mode == -1:
        #    logging.info(f'[{self._cur_time()}] - Manual mode off.')
        #if self._fMan_mode == 1:
        #    logging.info(f'[{self._cur_time()}] - Manual mode on.')
        
        
    def _remote_mode(self) -> None:
        """Удаленый режим управления аппаратом (с пульта)"""
        self._flag_man_mode = -1
        self._flag_auto_mode = -1
        self._flag_rmt_mode *= -1
        
        self.server.signals.set_mode.emit('RMT')
        
        #if self._fRmt_mode == -1:
        #    logging.info(f'[{self._cur_time()}] - Remote mode off.')
        #if self._fRmt_mode == 1:
        #    logging.info(f'[{self._cur_time()}] - Remote mode on.')
        

    def _auto_mode(self) -> None:
        """Автоматический режим управления аппаратом"""
        self._flag_man_mode = -1
        self._flag_rmt_mode = -1
        self._flag_auto_mode *= -1
        
        #self.server.signals.set_mode('AUT')
        
        QMessageBox.warning(None,
                                "Упсссс....", 
                                "Этот режим ещё не готов. Принесите программисту сгущёнки",
                                QMessageBox.StandardButton.Ok)
        
        self._manual_mode()
        
        #if self._fAut_mode == -1:
        #    logging.info(f'[{self._cur_time()}] - Auto mode off.')
        #if self._fAut_mode == 1:
        #    logging.info(f'[{self._cur_time()}] - Auto mode on.')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeController()
    window.show()
    app.exec()