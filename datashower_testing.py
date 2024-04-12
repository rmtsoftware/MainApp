import random

def get_current_time():
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]


def generate_gps_messages(n=30):
    messages = []
    for _ in range(n):
        lat = round(random.uniform(5500, 5600), 4)
        lon = round(random.uniform(2040, 2050), 4)
        speed = round(random.uniform(10, 20), 1)
        time = random.randint(100000, 235959)
        alt = round(random.uniform(35.000, 45.000), 3)
        accuracy = round(random.uniform(40.000, 50.000), 3)
        checksum = random.randint(10, 99)  # Simple placeholder for checksum
        message = f"D,s,1,1,{lat},N,{lon},E,{speed},{time},{alt},{accuracy},*{checksum}"
        messages.append(message)
    return messages


def generate_imu_messages(n=30):
    messages = []
    for _ in range(n):
        ax = round(random.uniform(-1, 1), 3)
        ay = round(random.uniform(-1, 1), 3)
        az = round(random.uniform(170, 180), 3)
        checksum = random.randint(10, 99)  # Simple placeholder for checksum
        message = f"D,s,1,3,{ax},{ay},{az},*{checksum}"
        messages.append(message)
    return messages


class DataShower():

    def parse(self, raw_data: str):
        splitted = raw_data.split('*')

        print(splitted)

        # Example data:
        #   GPS:    'D,s,1,1,5520.0459,N,2047.5840,E,15.2,123752,38.000,48.000,'
        #   IMU:    'D,s,1,3,-0.134,0.248,176.790'
        #           'D,s,1,3,0.155,-0.501,-12.101*'
        #   REMOTE: 'D,s,5,RC,'

        if splitted[0].startswith("D,s,1,1"):
            self.parse_msg_gps(splitted[0])

        if splitted[0].startswith("D,s,1,3"):
            self.parse_msg_imu(splitted[0])

        if splitted[0].startswith("D,s,5"):
            self.parse_remote()
        

    def parse_msg_gps(self, data):
        try:
            data = data[8:-1].split(',')
            
            # 0 Latitude   5520.0459
            # 1 NS         N
            # 2 Longitude  2047.5840
            # 3 EW         E
            # 4 Altitude   15.2
            # 5 _          123752
            # 6 _          38.000
            # 7 GrndSpeed  48.000

            Latitude = data[0]
            NS = data[1]
            Longitude = data[2]
            EW = data[3]
            Altitude = data[4]
            GrndSpeed = data[7]
            
            print(get_current_time(), ": GPS")
            print(f'Latitude:\t{Latitude}')
            print(f'NS:\t\t{NS}')
            print(f'Longitude:\t{Longitude}')
            print(f'EW:\t\t{EW}')
            print(f'Altitude:\t{Altitude}')
            print(f'GrndSpeed:\t{GrndSpeed}')

            with open("gps_data.txt", "a") as file:
                file.write(f"{get_current_time()}, {' '.join(data)}\n")

        except Exception as e:
            print(f"[ERROR]: DataShower.parse_msg_gps : {e}")

    def parse_msg_imu(self, data: str):
        try:
            data = data[8:-1].split(',')
    
            # 0 AXL_x -0.134
            # 1 AXL_y 0.248
            # 2 AXL_z 176.790

            AXL_x = data[0]
            AXL_y = data[1]
            AXL_z = data[2]

            print(get_current_time(), ": IMU")
            print(f'AXL_x:\t{AXL_x}')
            print(f'AXL_y:\t{AXL_y}')
            print(f'AXL_z:\t{AXL_z}')

            with open("imu_data.txt", "a") as file:
                file.write(f"{get_current_time()}, {' '.join(data)}\n")

        except Exception as e:
            print(f"[ERROR]: DataShower.parse_msg_imu : {e}")

    def parse_remote(self,):
        print(get_current_time(), ": REMOTE")


Data = {'gps': ['D,s,1,1,0.0000,N,0.0000,E,0.0,075607,0.000,0.000,*121\r\n'],
        'imu': ['D,s,1,3,-0.130,-0.421,-13.144*104\r\n'],
        'rmt': ['D,s,5,RC,*,']}


if __name__ == "__main__":

    #for el in generate_gps_messages(30):
    #    Data['gps'].append(el)

    #for el in generate_imu_messages(30):
    #    Data['imu'].append(el)
    print(Data)

    data_shower = DataShower()

    for key in Data:

        for i in range(0, len(Data[key])):
            data_shower.parse(raw_data=Data[key][i])
            print('\n')

