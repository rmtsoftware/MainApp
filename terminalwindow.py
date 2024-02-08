from manualkeyscontrol import ManualKeysControl
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QTimer, Slot
import sys
import datetime

 
class TerminalWindow(ManualKeysControl):
    def __init__(self):
        super().__init__()
        self.current_text: str = ""
        self.msg_to_terminal.connect(self.show_msg)
        
        self.terminal_cleaner = QTimer() # таймер очистки содержимого терминала
        self.terminal_cleaner.timeout.connect(self._clean_by_timer)
        self.terminal_cleaner.start(300)
        
        self.ui.btn_clean_textBrw.clicked.connect(self._clean_by_button)
     
    def _clean_by_timer(self):
        if len(self.current_text) > 2000:
            self.current_text = ''
            
    def _clean_by_button(self):
        self.current_text = ''
       
    def _cur_time(self):
        return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    

    def _add_to_textBrowser(self, msg):
        """
        Добавление записи в окно вывода текста
        """
        self.current_text = f'{msg}' + self.current_text
        self.ui.terminal_window.setText(self.current_text)

 
    @Slot(object)  
    def show_msg(self, data, type):
        
        if data['msg_data'] == {} and data['cmd'] == []:
            return
        
        if list(data['msg_data'].keys()) == ['INFO']:
            return
        
        _msg = ''
        _msg += self._cur_time() + f' - {type}'+ '\n'
        
        try:
            if len(data['cmd']) != 0:
                _msg += 'CMD: '
                for el in data['cmd']:
                    _msg += f'{el} '
            _msg += '\n'           
             
        except Exception as _:
            pass
        
        for key in data['msg_data']:
            if key in ['INFO', 'SETMODE', 'MANKEYCMD', 'MANLINECM']:
                _msg += f'{key}: {str(data['msg_data'][key])}\n'
            else:
                _msg += f'{key}: {str(data['msg_data'][key])[:-4]}\n'
        _msg += '\n'
        
        self._add_to_textBrowser(_msg)
        
           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TerminalWindow()
    window.show()
    app.exec()
    