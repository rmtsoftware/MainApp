from terminalwindow import TerminalWindow
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QTimer, Slot
import sys

 
class DataShower(TerminalWindow):
    def __init__(self):
        super().__init__()
        self.telemetry_to_operator.connect(self.parse)

    @Slot(object)  
    def parse(self, raw_data: str):

        splitted = raw_data.split(',')
        data = splitted[4:-1]

        if raw_data[0:7] == "D,s,1,1":  
            # "D,s,1,1,5520.0459,N,2047.5840,E,15.2,123752,38.000,48.000,*73"
            Latitude = float(data[0])
            NS: str = data[1]
            Longitude = float(data[2])
            EW = data[3]
            Altitude = float(data[4])
            _ = int(data[5]) # TODO: получить акту
            _ = float(data[6])
            GrndSpeed = float(data[7])


        if raw_data[0:7] == "D,s,1,2":
            # "D,s,1,2,546,21068,15139,11540,4355,8600,28862,20656,15206,168.000,*65\r\n"
            AXL_x = int(data[0])
            AXL_y =  int(data[1])
            AXL_z = int(data[2])
            MAG_x = int(data[3])
            MAG_y = int(data[4])
            MAG_z = int(data[5])
            GYRO_x = int(data[6])
            GYRO_y = int(data[7])
            GYRO_z = int(data[8])
            Gnd_Heading = float(data[9])
        
        raw_crc = splitted[-1:]
        crc = int(raw_crc[0].split("*")[1]) 

        #TODO: добавить вызов эстимейтора
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataShower()
    window.show()
    app.exec()
