from PySide6.QtCore import Signal, QThread
import numpy as np
import cv2
from dotenv import load_dotenv
import os

load_dotenv()

class VideoThread(QThread):
    
    change_pixmap_signal = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam+
        rtsp = os.getenv("RTSP_local")
        cap = cv2.VideoCapture(rtsp)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()


    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()