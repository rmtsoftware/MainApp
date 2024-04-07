import os
from PySide6.QtCore import QRunnable, QThreadPool, Signal, QObject, Slot
import socket
import select
import json
from dotenv import load_dotenv

load_dotenv()

class ServerSignals(QObject):
    started = Signal()
    stoped = Signal()
    connection_timeout = Signal()
    data_received = Signal(dict)
    data_sent = Signal(dict)

    get_gps = Signal()  # Запрос gps
    get_imu = Signal()  # Запрос imu

    set_mode = Signal(str)  # Установка режима
    mtr_cmd = Signal(str)  # Установка режима
    man_commandline = Signal(str)  # Мануальная команда
    man_key_control = Signal(str)  # Ручное управление при помощи клавиш


class ServerThread(QRunnable):

    def __init__(self):
        super().__init__()
        self.snd_msg = {'cmd': [], 'msg_data': {}}

        self.HOST = "192.168.0.124" # home
        #self.HOST = "192.168.31.58"  # directly
        #self.HOST = "10.0.6.78"     # vpn
        self.PORT = 12345
        print(self.HOST, self.PORT)
        
        self.conn = None
        self.no_ro_resp_counts = 0

        self.signals = ServerSignals()

        self.signals.get_gps.connect(self.get_gps)
        self.signals.get_imu.connect(self.get_imu)

        self.signals.set_mode.connect(self.set_mode)

        self.signals.mtr_cmd.connect(self.mtr_cmd)

        self.signals.man_commandline.connect(self.man_commandline)

        self.signals.man_key_control.connect(self.man_key_control)

    def exception_handler(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            try:
                func(*args, **kwargs)
            except TimeoutError as e:
                print(e, end=': ')
                print('[ERROR] - Таймаут ожидания подключения клиента к серверу\n')
                self.signals.connection_timeout.emit()
            except ConnectionAbortedError as e:
                pass
            except OSError as e:
                pass
            except TypeError as e:
                print(e)
            except RuntimeError as e:
                print(e)
                print('[ERROR] - Перед закрытием приложения отключайте клиента (кнопка отключить)')
            finally:
                self.signals.stoped.emit()
            # ВОЗМОЖНОСТЬ МАСШТАБИРОВАТЬ

        return wrapper

    def get_gps(self):
        self.snd_msg["cmd"].append("GPS")

    def get_imu(self):
        self.snd_msg["cmd"].append("IMU")

    @Slot(object)
    def set_mode(self, mode):
        self.snd_msg["cmd"].append("SETMODE")
        self.snd_msg['msg_data']['SETMODE'] = mode

    @Slot(object)
    def mtr_cmd(self, cmd):
        self.snd_msg["cmd"].append("MTRCMD")
        self.snd_msg['msg_data']['MTRCMD'] = cmd

    @Slot(object)
    def man_commandline(self, cmd):
        if "MANLINECMD" not in self.snd_msg["cmd"]:
            self.snd_msg["cmd"].append("MANLINECMD")
            self.snd_msg['msg_data']['MANLINECM'] = cmd

    @Slot(object)
    def man_key_control(self, cmds):
        if "MANKEYCMD" not in self.snd_msg["cmd"]:
            self.snd_msg["cmd"].append("MANKEYCMD")
            self.snd_msg['msg_data']['MANKEYCMD'] = cmds

    @exception_handler
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.bind((self.HOST, self.PORT))
            s.listen()

            self.conn, self.addr = s.accept()

            with self.conn:
                self.signals.started.emit()

                while True:
                    raw_data = self._get_data(self.conn)
                    data = self._parse_data(raw_data)
                    self.signals.data_received.emit(data)

                    self._send_data(self.conn)
                    self.signals.data_sent.emit(self.snd_msg)
                    self.snd_msg = {'cmd': [], 'msg_data': {}}

    def _get_data(self, conn):
        """Получение данных от клиента\n_TIMEOUT - время ожидания сообщения от клиента\n
        _CTIMEOUT - количество раз ожидание сообщения"""
        _TIMEOUT = 5
        _CTIMEOUT = 3
        if conn:
            ready = select.select([conn], [], [], _TIMEOUT)
            if ready[0]:
                self.no_ro_resp_counts = 0
                raw_data = conn.recv(1024).decode()
                return raw_data

            else:
                print(f'\n\t[WARNING] - Сервер не получил ответ {self.noRespCounts} раз')
                self.no_ro_resp_counts += 1
                if self.no_ro_resp_counts >= _CTIMEOUT:
                    raise ConnectionError(
                        f" [ERROR] - Нет ответа от клиента в течение {self.noRespCounts * _TIMEOUT} секунд!\n")

    def _parse_data(self, raw_data):
        """Преобразование полученных данных"""
        """Transform received data"""
        try:
            data = json.loads(raw_data)
        except json.JSONDecodeError as e:
            print(f'[ERROR] - Unable to parse the raw data: {e}')
            data = {}
        return data

    def _send_data(self, conn):
        """Отправка данных клиенту"""
        self.data_to_resp = json.dumps(self.snd_msg).encode()
        if conn is not None:  # Check if conn is not None before calling sendall
            conn.sendall(self.data_to_resp)
