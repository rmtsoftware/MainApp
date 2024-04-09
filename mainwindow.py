# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1140, 600)
        MainWindow.setStyleSheet(u"color: white;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0.193, y2:0.170727, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(44, 67, 150, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(490, 4, 141, 142))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"	background-color: None;\n"
"}\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.btn_gps = QPushButton(self.layoutWidget)
        self.btn_gps.setObjectName(u"btn_gps")
        self.btn_gps.setMaximumSize(QSize(16777215, 44))
        self.btn_gps.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_gps)

        self.btn_imu = QPushButton(self.layoutWidget)
        self.btn_imu.setObjectName(u"btn_imu")
        self.btn_imu.setMaximumSize(QSize(16777215, 44))
        self.btn_imu.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_imu)

        self.cb_auto_gps = QCheckBox(self.layoutWidget)
        self.cb_auto_gps.setObjectName(u"cb_auto_gps")
        self.cb_auto_gps.setMinimumSize(QSize(0, 0))
        self.cb_auto_gps.setStyleSheet(u"\n"
"    font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"	background-color: None;\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.cb_auto_gps)

        self.cb_auto_imu = QCheckBox(self.layoutWidget)
        self.cb_auto_imu.setObjectName(u"cb_auto_imu")
        self.cb_auto_imu.setStyleSheet(u"\n"
"    font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"	background-color: None;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.cb_auto_imu)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 4, 167, 92))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_status = QLabel(self.layoutWidget1)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMaximumSize(QSize(50, 16777215))
        self.lb_status.setStyleSheet(u"QLabel {\n"
"    font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"	background-color: None;\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.lb_status)

        self.lb_status_val = QLabel(self.layoutWidget1)
        self.lb_status_val.setObjectName(u"lb_status_val")
        self.lb_status_val.setStyleSheet(u"QLabel {\n"
"    font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"	background-color: None;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.lb_status_val)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.btn_server_start = QPushButton(self.layoutWidget1)
        self.btn_server_start.setObjectName(u"btn_server_start")
        self.btn_server_start.setMaximumSize(QSize(16777215, 44))
        self.btn_server_start.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_server_start)

        self.btn_server_stop = QPushButton(self.layoutWidget1)
        self.btn_server_stop.setObjectName(u"btn_server_stop")
        self.btn_server_stop.setMaximumSize(QSize(16777215, 44))
        self.btn_server_stop.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_server_stop)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(190, 4, 141, 91))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_rmode_val = QLabel(self.layoutWidget2)
        self.lb_rmode_val.setObjectName(u"lb_rmode_val")
        self.lb_rmode_val.setStyleSheet(u"QLabel {\n"
"    font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"	background-color: None;\n"
"}\n"
"\n"
"")
        self.lb_rmode_val.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_rmode_val)

        self.btn_mnl_mode = QPushButton(self.layoutWidget2)
        self.btn_mnl_mode.setObjectName(u"btn_mnl_mode")
        self.btn_mnl_mode.setMinimumSize(QSize(104, 25))
        self.btn_mnl_mode.setMaximumSize(QSize(16777215, 44))
        self.btn_mnl_mode.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_mnl_mode)

        self.btn_rmt_mode = QPushButton(self.layoutWidget2)
        self.btn_rmt_mode.setObjectName(u"btn_rmt_mode")
        self.btn_rmt_mode.setMinimumSize(QSize(104, 25))
        self.btn_rmt_mode.setMaximumSize(QSize(16777215, 44))
        self.btn_rmt_mode.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_rmt_mode)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(340, 4, 141, 91))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_mtr_ctrl = QLabel(self.layoutWidget3)
        self.lb_mtr_ctrl.setObjectName(u"lb_mtr_ctrl")
        self.lb_mtr_ctrl.setStyleSheet(u"QLabel {\n"
"    font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"	background-color: None;\n"
"}\n"
"")
        self.lb_mtr_ctrl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_mtr_ctrl)

        self.btn_motor_start = QPushButton(self.layoutWidget3)
        self.btn_motor_start.setObjectName(u"btn_motor_start")
        self.btn_motor_start.setMinimumSize(QSize(104, 25))
        self.btn_motor_start.setMaximumSize(QSize(16777215, 44))
        self.btn_motor_start.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_motor_start)

        self.btn_motor_stop = QPushButton(self.layoutWidget3)
        self.btn_motor_stop.setObjectName(u"btn_motor_stop")
        self.btn_motor_stop.setMinimumSize(QSize(104, 25))
        self.btn_motor_stop.setMaximumSize(QSize(16777215, 44))
        self.btn_motor_stop.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_motor_stop)

        self.hs_pwr_mtr = QSlider(self.centralwidget)
        self.hs_pwr_mtr.setObjectName(u"hs_pwr_mtr")
        self.hs_pwr_mtr.setGeometry(QRect(10, 110, 271, 20))
        self.hs_pwr_mtr.setStyleSheet(u"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    height: 8px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0442\u0440\u0435\u043a\u0430 */\n"
"    background: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0442\u0440\u0435\u043a\u0430 */\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: white; /* \u0411\u0435\u043b\u0430\u044f \u0440\u0443\u0447\u043a\u0430 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0440\u0443\u0447\u043a\u0438 */\n"
"    width: 20px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u0440\u0443\u0447\u043a\u0438 */\n"
"    margin: -10px 0; /* \u0412\u044b\u0441\u0442\u0443\u043f\u0430\u0435\u0442 \u0437\u0430 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0442\u0440\u0435\u043a\u0430 */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b"
                        "\u0435 \u0443\u0433\u043b\u044b */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #BDBDBD; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0440\u0443\u0447\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: #757575; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0440\u0443\u0447\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0430\u0432\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430 (\u0438\u043b\u0438 \u043b\u0435\u0432\u043e\u0439 \u0434\u043b\u044f RTL) */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444"
                        "\u043e\u043d \u043b\u0435\u0432\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430 (\u0438\u043b\u0438 \u043f\u0440\u0430\u0432\u043e\u0439 \u0434\u043b\u044f RTL) */\n"
"}\n"
"\n"
"QSlider:disabled {\n"
"    background: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"}\n"
"")
        self.hs_pwr_mtr.setMaximum(100)
        self.hs_pwr_mtr.setOrientation(Qt.Horizontal)
        self.hs_pwr_mtr.setTickPosition(QSlider.NoTicks)
        self.lb_pwr_mtr = QLabel(self.centralwidget)
        self.lb_pwr_mtr.setObjectName(u"lb_pwr_mtr")
        self.lb_pwr_mtr.setGeometry(QRect(290, 104, 41, 31))
        self.lb_pwr_mtr.setMinimumSize(QSize(0, 0))
        self.lb_pwr_mtr.setMaximumSize(QSize(16777215, 31))
        self.lb_pwr_mtr.setStyleSheet(u"QLabel {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    font-weight: bold; /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    text-align: center; /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u043e \u0446\u0435\u043d\u0442\u0440\u0443 */\n"
"}\n"
"")
        self.lb_pwr_mtr.setAlignment(Qt.AlignCenter)
        self.btn_pwr_reset = QPushButton(self.centralwidget)
        self.btn_pwr_reset.setObjectName(u"btn_pwr_reset")
        self.btn_pwr_reset.setGeometry(QRect(340, 104, 141, 31))
        self.btn_pwr_reset.setMinimumSize(QSize(104, 25))
        self.btn_pwr_reset.setMaximumSize(QSize(16777215, 44))
        self.btn_pwr_reset.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")
        self.telemetry_widget = QWidget(self.centralwidget)
        self.telemetry_widget.setObjectName(u"telemetry_widget")
        self.telemetry_widget.setGeometry(QRect(640, 28, 491, 121))
        self.telemetry_widget.setStyleSheet(u"QWidget {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442, \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u0438\u043c\u0435\u043d\u044f\u0442\u044c\u0441\u044f \u043a \u0432\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u043c \u0432\u0438\u0434\u0436\u0435\u0442\u0430\u043c, \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u044e\u0449\u0438\u043c \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u043e color */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"	font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.telemetry_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.telemetry_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel {\n"
"    font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"	color: black;\n"
"}\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_9)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_latitude = QLabel(self.telemetry_widget)
        self.lb_latitude.setObjectName(u"lb_latitude")
        self.lb_latitude.setMinimumSize(QSize(58, 0))
        self.lb_latitude.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.lb_latitude)

        self.lb_latitude_val = QLabel(self.telemetry_widget)
        self.lb_latitude_val.setObjectName(u"lb_latitude_val")
        self.lb_latitude_val.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.lb_latitude_val)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_longitude = QLabel(self.telemetry_widget)
        self.lb_longitude.setObjectName(u"lb_longitude")
        self.lb_longitude.setMinimumSize(QSize(58, 0))
        self.lb_longitude.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_5.addWidget(self.lb_longitude)

        self.lb_longitude_val = QLabel(self.telemetry_widget)
        self.lb_longitude_val.setObjectName(u"lb_longitude_val")
        self.lb_longitude_val.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.lb_longitude_val)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_axl_x = QLabel(self.telemetry_widget)
        self.lb_axl_x.setObjectName(u"lb_axl_x")
        self.lb_axl_x.setMinimumSize(QSize(58, 0))
        self.lb_axl_x.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_9.addWidget(self.lb_axl_x)

        self.lb_axl_x_val = QLabel(self.telemetry_widget)
        self.lb_axl_x_val.setObjectName(u"lb_axl_x_val")
        self.lb_axl_x_val.setMinimumSize(QSize(0, 0))
        self.lb_axl_x_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.lb_axl_x_val)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_NS = QLabel(self.telemetry_widget)
        self.lb_NS.setObjectName(u"lb_NS")
        self.lb_NS.setMinimumSize(QSize(58, 0))
        self.lb_NS.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_4.addWidget(self.lb_NS)

        self.lb_NS_val = QLabel(self.telemetry_widget)
        self.lb_NS_val.setObjectName(u"lb_NS_val")
        self.lb_NS_val.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.lb_NS_val)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_EW = QLabel(self.telemetry_widget)
        self.lb_EW.setObjectName(u"lb_EW")
        self.lb_EW.setMinimumSize(QSize(58, 0))
        self.lb_EW.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_2.addWidget(self.lb_EW)

        self.lb_EW_val = QLabel(self.telemetry_widget)
        self.lb_EW_val.setObjectName(u"lb_EW_val")
        self.lb_EW_val.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.lb_EW_val)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_axl_y = QLabel(self.telemetry_widget)
        self.lb_axl_y.setObjectName(u"lb_axl_y")
        self.lb_axl_y.setMinimumSize(QSize(58, 0))
        self.lb_axl_y.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_10.addWidget(self.lb_axl_y)

        self.lb_axl_y_val = QLabel(self.telemetry_widget)
        self.lb_axl_y_val.setObjectName(u"lb_axl_y_val")
        self.lb_axl_y_val.setMinimumSize(QSize(0, 0))
        self.lb_axl_y_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.lb_axl_y_val)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_altitude = QLabel(self.telemetry_widget)
        self.lb_altitude.setObjectName(u"lb_altitude")
        self.lb_altitude.setMinimumSize(QSize(58, 0))
        self.lb_altitude.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_7.addWidget(self.lb_altitude)

        self.lb_altitude_val = QLabel(self.telemetry_widget)
        self.lb_altitude_val.setObjectName(u"lb_altitude_val")
        self.lb_altitude_val.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_7.addWidget(self.lb_altitude_val)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_grndspeed = QLabel(self.telemetry_widget)
        self.lb_grndspeed.setObjectName(u"lb_grndspeed")
        self.lb_grndspeed.setMinimumSize(QSize(58, 0))
        self.lb_grndspeed.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_8.addWidget(self.lb_grndspeed)

        self.lb_grndspeed_val = QLabel(self.telemetry_widget)
        self.lb_grndspeed_val.setObjectName(u"lb_grndspeed_val")
        self.lb_grndspeed_val.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_8.addWidget(self.lb_grndspeed_val)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_axl_z = QLabel(self.telemetry_widget)
        self.lb_axl_z.setObjectName(u"lb_axl_z")
        self.lb_axl_z.setMinimumSize(QSize(58, 0))
        self.lb_axl_z.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_11.addWidget(self.lb_axl_z)

        self.lb_axl_z_val = QLabel(self.telemetry_widget)
        self.lb_axl_z_val.setObjectName(u"lb_axl_z_val")
        self.lb_axl_z_val.setMinimumSize(QSize(0, 0))
        self.lb_axl_z_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_11.addWidget(self.lb_axl_z_val)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_11)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.lb_name_camera_2 = QLabel(self.centralwidget)
        self.lb_name_camera_2.setObjectName(u"lb_name_camera_2")
        self.lb_name_camera_2.setGeometry(QRect(491, 158, 129, 16))
        self.lb_name_camera_2.setMaximumSize(QSize(150, 16))
        self.lb_name_camera_2.setStyleSheet(u"QLabel {\n"
"    font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"	background-color: None;\n"
"}\n"
"\n"
"border: None;")
        self.lb_camera = QLabel(self.centralwidget)
        self.lb_camera.setObjectName(u"lb_camera")
        self.lb_camera.setGeometry(QRect(491, 175, 640, 360))
        self.lb_camera.setMinimumSize(QSize(640, 360))
        self.lb_camera.setMaximumSize(QSize(640, 360))
        self.lb_camera.setStyleSheet(u"background-color: grey;\n"
"border: None;\n"
"")
        self.terminal_window = QTextBrowser(self.centralwidget)
        self.terminal_window.setObjectName(u"terminal_window")
        self.terminal_window.setGeometry(QRect(11, 175, 471, 360))
        self.terminal_window.setMinimumSize(QSize(0, 0))
        self.terminal_window.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.terminal_window.setFont(font)
        self.terminal_window.setStyleSheet(u"border: None;\n"
"background-color: white;\n"
"color: black;")
        self.btn_clean_textBrw = QPushButton(self.centralwidget)
        self.btn_clean_textBrw.setObjectName(u"btn_clean_textBrw")
        self.btn_clean_textBrw.setGeometry(QRect(10, 540, 471, 30))
        self.btn_clean_textBrw.setMinimumSize(QSize(104, 25))
        self.btn_clean_textBrw.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 158, 58, 16))
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font-weight: bold; /* \u0414\u0435\u043b\u0430\u0435\u0442 \u0442\u0435\u043a\u0441\u0442 \u0436\u0438\u0440\u043d\u044b\u043c */\n"
"	background-color: None;\n"
"}\n"
"")
        self.btn_start_camera = QPushButton(self.centralwidget)
        self.btn_start_camera.setObjectName(u"btn_start_camera")
        self.btn_start_camera.setGeometry(QRect(491, 541, 316, 30))
        self.btn_start_camera.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")
        self.btn_stop_camera = QPushButton(self.centralwidget)
        self.btn_stop_camera.setObjectName(u"btn_stop_camera")
        self.btn_stop_camera.setGeometry(QRect(815, 540, 316, 30))
        self.btn_stop_camera.setStyleSheet(u"QPushButton {\n"
"    background-color: #9E9E9E; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #9E9E9E; /* \u0421\u0435\u0440\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    padding: 5px 10px; /* \u0423\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0434\u043b\u044f \u0441\u043d\u0438\u0436\u0435\u043d\u0438\u044f \u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    min-width: 80px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    max-height: 30px; /* \u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u043d\u043e\u043f\u043a"
                        "\u0438 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 2px solid #E0E0E0;\n"
"    color: #BDBDBD; /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #BDBDBD; /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u043e\u0442\u0442\u0435\u043d\u043e\u043a \u0441\u0435\u0440\u043e\u0433\u043e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #757575; /* \u0422\u0435"
                        "\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset; /* \u0421\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u0435\u043b\u0430\u0435\u0442 \u0435\u0435 \u043f\u043e\u0445\u043e\u0436\u0435\u0439 \u043d\u0430 \u0432\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u0443\u044e */\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1140, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441 \u0442\u0435\u043b\u0435\u043c\u0435\u0442\u0440\u0438\u0438", None))
        self.btn_gps.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.btn_imu.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.cb_auto_gps.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e \u0437\u0430\u043f\u0440\u043e\u0441 GPS", None))
        self.cb_auto_imu.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e \u0437\u0430\u043f\u0440\u043e\u0441 IMU", None))
        self.lb_status.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.lb_status_val.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d", None))
        self.btn_server_start.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.btn_server_stop.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.lb_rmode_val.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c\u0430", None))
        self.btn_mnl_mode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u043e\u0439", None))
        self.btn_rmt_mode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u044b\u0439", None))
        self.lb_mtr_ctrl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0414\u0412\u0421", None))
        self.btn_motor_start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.btn_motor_stop.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.lb_pwr_mtr.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_pwr_reset.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u043c\u0435\u0442\u0440\u0438\u044f", None))
        self.lb_latitude.setText(QCoreApplication.translate("MainWindow", u"Latitide", None))
        self.lb_latitude_val.setText(QCoreApplication.translate("MainWindow", u"Latitide", None))
        self.lb_longitude.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.lb_longitude_val.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lb_axl_x.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.lb_axl_x_val.setText(QCoreApplication.translate("MainWindow", u"AXL_x", None))
        self.lb_NS.setText(QCoreApplication.translate("MainWindow", u"NS", None))
        self.lb_NS_val.setText(QCoreApplication.translate("MainWindow", u"NS", None))
        self.lb_EW.setText(QCoreApplication.translate("MainWindow", u"EW", None))
        self.lb_EW_val.setText(QCoreApplication.translate("MainWindow", u"EW", None))
        self.lb_axl_y.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.lb_axl_y_val.setText(QCoreApplication.translate("MainWindow", u"AXL_y", None))
        self.lb_altitude.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.lb_altitude_val.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.lb_grndspeed.setText(QCoreApplication.translate("MainWindow", u"GSpeed", None))
        self.lb_grndspeed_val.setText(QCoreApplication.translate("MainWindow", u"GrndSpeed", None))
        self.lb_axl_z.setText(QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.lb_axl_z_val.setText(QCoreApplication.translate("MainWindow", u"AXL_z", None))
        self.lb_name_camera_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0435\u043e\u043f\u043e\u0442\u043e\u043a \u0441 \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.lb_camera.setText("")
        self.btn_clean_textBrw.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0440\u043c\u0438\u043d\u0430\u043b", None))
        self.btn_start_camera.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.btn_stop_camera.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

