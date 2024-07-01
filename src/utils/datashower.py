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
        
        splitted = raw_data.split('*')
        print(splitted)

        if splitted[0].startswith("D,s,1,1"):
            self.parse_msg_gps(splitted[0])

        if splitted[0].startswith("D,s,1,3"):
            self.parse_msg_imu(splitted[0])

        if splitted[0].startswith("D,s,5"):
            self.parse_remote()

    def parse_msg_gps(self, data):
        try:
            data = data[8:-1].split(',')

            Latitude = data[0]
            NS = data[1]
            Longitude = data[2]
            EW = data[3]
            Altitude = data[4]
            GrndSpeed = data[7]

            self.ui.lb_latitude_val.setText(Latitude)
            self.ui.lb_NS_val.setText(NS)
            self.ui.lb_longitude_val.setText(Longitude)
            self.ui.lb_EW_val.setText(EW)
            self.ui.lb_altitude_val.setText(Altitude)
            self.ui.lb_grndspeed_val.setText(GrndSpeed)

            with open("./gps_data.txt", "a") as file:
                file.write(f"{self.get_current_time()}, {' '.join(data)}\n")

        except Exception as e:
            print(f"[ERROR]: DataShower.parse_msg_gps : {e}")


    def parse_msg_imu(self, data):
        try:
            data = data[8:-1].split(',')
    
            # 0 AXL_x -0.134
            # 1 AXL_y 0.248
            # 2 AXL_z 176.790

            AXL_x = data[0]
            AXL_y = data[1]
            AXL_z = data[2]

            print(self.get_current_time(), ": IMU")
            print(f'AXL_x:\t{AXL_x}')
            print(f'AXL_y:\t{AXL_y}')
            print(f'AXL_z:\t{AXL_z}')

            self.ui.lb_axl_x_val.setText(AXL_x)
            self.ui.lb_axl_y_val.setText(AXL_y)
            self.ui.lb_axl_z_val.setText(AXL_z)

            with open("./imu_data.txt", "a") as file:
                file.write(f"{self.get_current_time()}, {' '.join(data)}\n")

        except Exception as e:
            print(f"[ERROR]: DataShower.parse_msg_imu : {e}")

    def parse_remote(self):
        print(self.get_current_time(), ": REMOTE")


    def get_current_time(self):
        import datetime
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataShower()
    window.show()
    app.exec()
