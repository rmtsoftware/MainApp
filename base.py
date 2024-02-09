from PySide6.QtCore import QThreadPool, Slot, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from server import ServerThread
from mainwindow import Ui_MainWindow
import sys

class Base(QMainWindow):
    
    msg_to_terminal = Signal(dict, str) # при успешном получении или отправке сообщения выводить в терминал ui.terminal_window
    telemetry_to_operator = Signal(str) # передача полученных данных для дальнейшего парсинга и вывода оператору
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Активное / неактивное состояние кнопок
        self.ui.btn_server_start.setDisabled(False)
        self.ui.btn_server_stop.setDisabled(True)
        
        # Сигналы по нажатию кнопок
        self.ui.btn_server_start.clicked.connect(self.start)
        self.ui.btn_server_stop.clicked.connect(self.stop)
        
        
        self.pool = QThreadPool.globalInstance()
        
        self.set_zero_values()
        
    def set_zero_values(self):
        self.ui.lb_latitude_val.setText('0')
        self.ui.lb_NS_val.setText('0')
        self.ui.lb_longitude_val.setText('0')
        self.ui.lb_EW_val.setText('0')
        self.ui.lb_altitude_val.setText('0')
        self.ui.lb_grndspeed_val.setText('0')
        
        self.ui.lb_axl_x_val.setText('0')
        self.ui.lb_axl_y_val.setText('0')
        self.ui.lb_axl_z_val.setText('0')
        self.ui.lb_mag_x_val.setText('0')
        self.ui.lb_mag_y_val.setText('0')
        self.ui.lb_mag_z_val.setText('0')
        self.ui.lb_gyro_x_val.setText('0')
        self.ui.lb_gyro_y_val.setText('0')
        self.ui.lb_gyro_z_val.setText('0')
        self.ui.lb_grn_head_val.setText('0')
        
        
        
        
  
    def start(self):
        self.server = ServerThread()
        self.pool.start(self.server)
        
        # сигналы из потока
        self.server.signals.started.connect(self.started_actions)
        self.server.signals.connection_timeout.connect(self.timeout_actions)
        self.server.signals.data_received.connect(self._procces_rcv_data)
        self.server.signals.data_sent.connect(self._procces_snd_data)
          
    def stop(self):
        try:
            self.server.conn.shutdown(0)
            
            self.set_zero_values()
            
            self.server.conn = None
            self.server.addr = None
            self.ui.btn_motor_start.setEnabled(True)
            self.ui.btn_motor_stop.setEnabled(False)
            
        except AttributeError as _:
            print('Сервер не запущен, чтобы его останавливать')
            QMessageBox.warning(None,
                                "Внимание", 
                                "Сервер не запущен",
                                QMessageBox.StandardButton.Ok)
            
        except OSError as e:
            print('Сервер не запущен, чтобы его останавливать')
            QMessageBox.warning(None, 
                                "Внимание", 
                                "Сервер не запущен",
                                QMessageBox.StandardButton.Ok)
        finally:
            self.stoped_actions()
    
            
    def started_actions(self):
        self.ui.btn_server_start.setDisabled(True)
        self.ui.btn_server_stop.setDisabled(False)
    
        
    def stoped_actions(self):
        self.ui.btn_server_start.setDisabled(False)
        self.ui.btn_server_stop.setDisabled(True)
    
        
    def timeout_actions(self):
        QMessageBox.critical(None, 
                            "Ошибка", 
                            "Таймаут подключения",
                            QMessageBox.StandardButton.Ok)
    
    
    @Slot(object)
    def _procces_rcv_data(self, data):
        
        self.msg_to_terminal.emit(data, 'RCVD')

        #ip_addres = data['msg_data']['INFO']
        #print(ip_addres)
        
        if data['status'] == 'RESPONSE':
            
            if 'GPSRESPONSE' in data['msg_data']:
                self.telemetry_to_operator.emit(data['msg_data']['GPSRESPONSE'])
                #print(data['msg_data']['GPSRESPONSE'], end='')
                pass
                
            if 'IMURESPONSE' in data['msg_data']:
                self.telemetry_to_operator.emit(data['msg_data']['IMURESPONSE'])
                #print(data['msg_data']['IMURESPONSE'], end='')
                pass
    
        
    @Slot(object)
    def _procces_snd_data(self, data):
        
        self.msg_to_terminal.emit(data , 'SEND')
        #print(f'{self.i} Данные отправлены: ', end='')
        #print(data)
        #self.i -= 1
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Base()
    window.show()
    app.exec()
