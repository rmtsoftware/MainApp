from PySide6.QtWidgets import QApplication
from src.utils.autonmoving import AutonomMoving
import sys
from dotenv import load_dotenv

# Загрузка переменных срежы с файла .env
load_dotenv()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutonomMoving()
    window.show()
    app.exec()
    