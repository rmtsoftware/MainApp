from PySide6.QtWidgets import QApplication
from src.utils.cameracontrol import CameraControl
import sys
from dotenv import load_dotenv

# Загрузка переменных срежы с файла .env
load_dotenv()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CameraControl()
    window.show()
    app.exec()
    