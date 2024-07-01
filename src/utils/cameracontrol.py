from src.utils.webengine import WebEngineMap
from src.video.videothread import VideoThread
from PySide6.QtCore import Slot, Qt
from PySide6 import QtWidgets, QtGui
import numpy as np
import cv2
import sys


class CameraControl(WebEngineMap):
    
    def __init__(self):
        super(CameraControl, self).__init__()
        

    def _start_camera(self):
        """Старт RTSP потока"""
        self.vthread = VideoThread()
        self.vthread.start() # запуск python потока (threading)
        self.vthread.change_pixmap_signal.connect(self.update_image) # сигнал по получению opencv фрейма
        self.ui.btn_start_camera.setEnabled(False)
        self.ui.btn_stop_camera.setEnabled(True)


    def _stop_camera(self):
        """Стоп RTSP потока"""
        self.vthread.stop()
        self.ui.btn_start_camera.setEnabled(True)
        self.ui.btn_stop_camera.setEnabled(False)
        
    
    @Slot(np.ndarray)
    def update_image(self, cv_img):
        """Обновление lb_camera с полочением opencv фрейма"""
        qt_img = self.convert_cv_qt(cv_img)
        self.ui.lb_camera.setPixmap(qt_img)
    
    
    def convert_cv_qt(self, cv_img):
        """Преобразовать opencv фрейм в QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 360, Qt.KeepAspectRatio)
        return QtGui.QPixmap.fromImage(p)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # sys.excepthook = except_hook
    window = CameraControl()
    window.show()
    sys.exit(app.exec())
