from src.utils.terminalwindow import TerminalWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot
import sys


class DataShower(TerminalWindow):
    def __init__(self):
        super().__init__()
        self.telemetry_to_operator.connect(self.parse)

    @Slot(object)
    def parse(self, raw_data: str):
        
        print(raw_data)

        splitted = raw_data.split(',')
        data = splitted[4:-1]

        if raw_data.startswith("D,s,1,1"):
            self.parse_msg_gps(data)

        # 'D,s,1,3,-0.134,0.248,176.790*88\r\n'
        if raw_data.startswith("D,s,1,3"):
            self.parse_msg_imu(data)

        if raw_data.startswith("D,s,5"):
            self.parse_remote(data)


        #raw_crc = splitted[-1:]
        #crc = int(raw_crc[0].split("*")[1])
        ## TODO: добавить вызов эстимейтора

    def parse_msg_gps(self, data):
        # "D,s,1,1,5520.0459,N,2047.5840,E,15.2,123752,38.000,48.000,*73"
        Latitude = float(data[0])
        NS: str = data[1]
        Longitude = float(data[2])
        EW = data[3]
        Altitude = float(data[4])
        _ = int(data[5])  # TODO: получить акту
        _ = float(data[6])
        GrndSpeed = float(data[7])

        self.ui.lb_latitude_val.setText(str(Latitude))
        self.ui.lb_NS_val.setText(str(NS))
        self.ui.lb_longitude_val.setText(str(Longitude))
        self.ui.lb_EW_val.setText(str(EW))
        self.ui.lb_altitude_val.setText(str(Altitude))
        self.ui.lb_grndspeed_val.setText(str(GrndSpeed))

    def parse_msg_imu(self, data): ...
        # 'D,s,1,3,-0.134,0.248,176.790*88\r\n'
        #AXL_x = data[0]
        #AXL_y = data[1]
        #AXL_z = data[2]
        #self.ui.lb_axl_x_val.setText(str(AXL_x))
        #self.ui.lb_axl_y_val.setText(str(AXL_y))
        #self.ui.lb_axl_z_val.setText(str(AXL_z))

    def parse_remote(self, data):
        print(data)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataShower()
    window.show()
    app.exec()
