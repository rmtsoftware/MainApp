from src.utils.cameracontrol import CameraControl
from PySide6 import QtWidgets
import sys


class AutonomMoving(CameraControl):
     def __init__(self):
        super(AutonomMoving, self).__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CameraControl()
    window.show()
    app.exec()