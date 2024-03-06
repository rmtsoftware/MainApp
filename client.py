from threading import Thread, Lock
import socket
import setting
import json
import time
import sys
import _my_test_data
import random
import serial.tools.list_ports


class TCPThread():
    def __init__(self):
        # Вспомогательный флаг
        self._run_flag = True

        # Структура сообщения
        self.snd_msg = {'status': None, 'available_ports': [], 'msg_data': {}}

    def run(self):

        global cmds
        global snd_msg

        while self._run_flag:
            try: # пробуем подключиться 
                # если все ок , то далее ... если нет то к <_икслючение № 1>
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(5)
                client.connect((setting.HOST, setting.EPORT))

                snd_msg['status'] = "CONNECTEDTOSERVER"
                #snd_msg['msg_data']["INFO"] = [socket.gethostbyname(socket.gethostname())]

                data_to_resp = json.dumps(snd_msg).encode()

                try:
                    client.sendall(data_to_resp)
                except ConnectionResetError as e:
                    print(e)
                    break

                while True:
                    try:
                        raw_data = client.recv(1024).decode()
                        try:
                            data = json.loads(raw_data)
                            print(data)
                        except json.decoder.JSONDecodeError as _:
                            break
                    # когда не получен ответ
                    except ConnectionAbortedError as e:
                        print(e)
                    except ConnectionResetError as e:
                        print(e)
                        break

                    self.procces_commands(data=data)

                    if len(data['cmd']) == 0:
                        snd_msg['status'] = "CONNECTEDTOSERVER"
                        snd_msg['msg_data']['INFO'] = socket.gethostbyname(socket.gethostname())

                    snd_msg['available_ports'] = self.avail_dev()
                    snd_msg['msg_data']["INFO"] = [socket.gethostbyname(socket.gethostname())]


                    try:
                        data_to_resp = json.dumps(snd_msg).encode()
                        client.sendall(data_to_resp)
                    except ConnectionResetError as e:
                        print(e)
                        break

                    try:
                        snd_msg = {'status': None, 'available_ports': [], 'msg_data': {}}
                    except Exception as e:
                        print("Ошибка очистки содержимого отправляемого пакета:\n", e)

                    time.sleep(0.1)

            # <_икслючение № 1>
            # когда не видит хост
            except ConnectionRefusedError as e:
                print(f"{e} - Отсутствие хоста в сети\n")
                time.sleep(0.5)

            except socket.timeout as e:
                print(e)

            finally:
                try:
                    self.stop_listen()
                except:
                    pass

    def stop(self):
        self._run_flag = False
        # TODO: переписать wait
        #self.wait()

    def procces_commands(self, data):

        global cmds

        if "GPS" in data['cmd']:    
            """ ЗАПРОС GPS"""
            cmds.append('D,s,4,GPS,*,\r\n')
            #cmds.append("D,s,1,1,5520.0459,N,2047.5840,E,15.2,123752,38.000,48.000,*73\r\n")
            #d = _my_test_data.TESTGPSDATA[random.randint(0, len(_my_test_data.TESTGPSDATA)-1)]
            #cmds.append(d)


        if "IMU" in data['cmd']:
            """ ЗАПРОС IMU """
            cmds.append('D,s,4,IMU,*,\r\n')
            #cmds.append("D,s,1,2,546,21068,15139,11540,4355,8600,28862,20656,15206,168.000,*65\r\n")
            #d = _my_test_data.TESTIMUDATA[random.randint(0, len(_my_test_data.TESTIMUDATA)-1)]
            #cmds.append(d)

        if "MTRCMD" in data['cmd']:
            """ УПРАВЛЕНИЕ МОТОРОМ ВКЛ/ВЫКЛ """

            if data['msg_data']['MTRCMD'] == 'START':
                cmds.append('D,s,ESTART,*,\r\n')

            if data['msg_data']['MTRCMD'] == 'STOP':
                cmds.append('D,s,ESTOP,*,\r\n')

        if 'SETMODE' in data['cmd']:

            if data['msg_data']['SETMODE'] == 'RMT':
                print('D,s,5,RC,*,\r\n')
                cmds.append('D,s,5,RC,*,\r\n')

            if data['msg_data']['SETMODE'] == 'MAN': ...


        if "MANKEYCMD" in data['cmd']:
            """ РУЧНОЕ УПРАВЛЕНИЕ """            
            _raw_cmd = data['msg_data']['MANKEYCMD']
            _cmd = f'D,s,3,{_raw_cmd[0]},{_raw_cmd[1:]},*,\r\n'
            cmds.append(_cmd)

        if "MANLINECMD" in data["cmd"]:
            cmds.append(data['msg_data']['MANLINECM'])


    @staticmethod
    def avail_dev():
        """
        Функция смотрит доступные последовательные порты в ОС
        """
        res = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            res.append(port.name)
        return res


class SerialThread():
    
    def __init__(self):
        #self.port = '/dev/ttyUSB0'
        self.port = '/dev/ttyACM0'
        self.ser = serial.Serial(self.port, 115200, timeout=5)
        self.rcv_data: str = ''


    def write(self):
        global cmds
        self.ser.close() 
        self.ser.open()

        while True:

            time.sleep(0.1)

            if len(cmds) != 0: 
                for idx, cmd in enumerate(cmds):
                    print(cmds)

                    _b_cmd = cmd.encode("utf-8")
                    self.ser.write(_b_cmd)

            # Сброс списка команд после чтения
            cmds = []


    def read(self):

        # Задержка 1 с, на инициализацию и запуск порта
        time.sleep(1) 

        while True: 

            if not self.ser.is_open:
                continue


            rcv_data_bytes = self.ser.readline()
            rcv_data = rcv_data_bytes.decode()


            if rcv_data[0:7] == "D,s,1,1":
                #print(">>>> Полчен ответ от на запрос GPS")
                snd_msg['status'] = "RESPONSE"
                snd_msg['msg_data']["GPSRESPONSE"] = rcv_data

            if rcv_data[0:7] == "D,s,1,3":
                #print(">>>> Полчен ответ от на запрос IMU")
                snd_msg['status'] = "RESPONSE"
                snd_msg['msg_data']["IMURESPONSE"] = rcv_data


if __name__ == "__main__":

    try:

        cmds: str = [] # список отправленных команд в последовательный порт
        rcv_data: str = [] # список полученных команд в последовательный порт
        snd_msg: dict = {'status': None, 'available_ports': [], 'msg_data': {}}

        tcp_connection = TCPThread()
        serial_connection = SerialThread()

        t1 = Thread(target=tcp_connection.run)
        t2 = Thread(target=serial_connection.write)
        t3 = Thread(target=serial_connection.read)

        t1.start()
        t2.start()
        t3.start()

    except KeyboardInterrupt as e:
        print('>> prog has been ended')
        sys.exit(0)



