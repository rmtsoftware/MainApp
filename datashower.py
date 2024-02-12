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

        if raw_data.startswith("D,s,1,1"):
            self.parse_msg_gps(data)

        elif raw_data.startswith("D,s,1,3"):
            self.parse_msg_imu(data)

        raw_crc = splitted[-1:]
        crc = int(raw_crc[0].split("*")[1])
        # TODO: добавить вызов эстимейтора

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

    def parse_msg_imu(self, data):
        # D,s,1,3,0.606,-0.128,95.909*1
        AXL_x = int(data[0])
        AXL_y = int(data[1])
        AXL_z = int(data[2])
        MAG_x = int(data[3])
        MAG_y = int(data[4])
        MAG_z = int(data[5])
        GYRO_x = int(data[6])
        GYRO_y = int(data[7])
        GYRO_z = int(data[8])
        Gnd_Heading = float(data[9])

        self.ui.lb_axl_x_val.setText(str(AXL_x))
        self.ui.lb_axl_y_val.setText(str(AXL_y))
        self.ui.lb_axl_z_val.setText(str(AXL_z))
        self.ui.lb_mag_x_val.setText(str(MAG_x))
        self.ui.lb_mag_y_val.setText(str(MAG_y))
        self.ui.lb_mag_z_val.setText(str(MAG_z))
        self.ui.lb_gyro_x_val.setText(str(GYRO_x))
        self.ui.lb_gyro_y_val.setText(str(GYRO_y))
        self.ui.lb_gyro_z_val.setText(str(GYRO_z))
        self.ui.lb_grn_head_val.setText(str(Gnd_Heading))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataShower()
    window.show()
    app.exec()
