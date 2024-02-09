# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 599)
        MainWindow.setStyleSheet(u"color: black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 100, 141, 130))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_connection_2 = QLabel(self.layoutWidget)
        self.lb_connection_2.setObjectName(u"lb_connection_2")

        self.verticalLayout.addWidget(self.lb_connection_2)

        self.btn_gps = QPushButton(self.layoutWidget)
        self.btn_gps.setObjectName(u"btn_gps")

        self.verticalLayout.addWidget(self.btn_gps)

        self.btn_imu = QPushButton(self.layoutWidget)
        self.btn_imu.setObjectName(u"btn_imu")

        self.verticalLayout.addWidget(self.btn_imu)

        self.cb_auto_gps = QCheckBox(self.layoutWidget)
        self.cb_auto_gps.setObjectName(u"cb_auto_gps")

        self.verticalLayout.addWidget(self.cb_auto_gps)

        self.cb_auto_imu = QCheckBox(self.layoutWidget)
        self.cb_auto_imu.setObjectName(u"cb_auto_imu")

        self.verticalLayout.addWidget(self.cb_auto_imu)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 10, 141, 78))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_connection = QLabel(self.layoutWidget1)
        self.lb_connection.setObjectName(u"lb_connection")

        self.verticalLayout_2.addWidget(self.lb_connection)

        self.btn_server_start = QPushButton(self.layoutWidget1)
        self.btn_server_start.setObjectName(u"btn_server_start")

        self.verticalLayout_2.addWidget(self.btn_server_start)

        self.btn_server_stop = QPushButton(self.layoutWidget1)
        self.btn_server_stop.setObjectName(u"btn_server_stop")

        self.verticalLayout_2.addWidget(self.btn_server_stop)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(170, 100, 141, 111))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.btn_mnl_mode = QPushButton(self.layoutWidget2)
        self.btn_mnl_mode.setObjectName(u"btn_mnl_mode")
        self.btn_mnl_mode.setMinimumSize(QSize(0, 25))
        self.btn_mnl_mode.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_mnl_mode)

        self.btn_rmt_mode = QPushButton(self.layoutWidget2)
        self.btn_rmt_mode.setObjectName(u"btn_rmt_mode")
        self.btn_rmt_mode.setMinimumSize(QSize(0, 25))
        self.btn_rmt_mode.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_rmt_mode)

        self.btn_auto_mode = QPushButton(self.layoutWidget2)
        self.btn_auto_mode.setObjectName(u"btn_auto_mode")
        self.btn_auto_mode.setMinimumSize(QSize(0, 25))
        self.btn_auto_mode.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_auto_mode)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 240, 141, 80))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_mtr_ctrl = QLabel(self.layoutWidget3)
        self.lb_mtr_ctrl.setObjectName(u"lb_mtr_ctrl")

        self.verticalLayout_4.addWidget(self.lb_mtr_ctrl)

        self.btn_motor_start = QPushButton(self.layoutWidget3)
        self.btn_motor_start.setObjectName(u"btn_motor_start")
        self.btn_motor_start.setMinimumSize(QSize(0, 25))
        self.btn_motor_start.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_motor_start)

        self.btn_motor_stop = QPushButton(self.layoutWidget3)
        self.btn_motor_stop.setObjectName(u"btn_motor_stop")
        self.btn_motor_stop.setMinimumSize(QSize(0, 25))
        self.btn_motor_stop.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_motor_stop)

        self.layoutWidget4 = QWidget(self.centralwidget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(170, 220, 141, 49))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_set_power = QLabel(self.layoutWidget4)
        self.lb_set_power.setObjectName(u"lb_set_power")

        self.verticalLayout_5.addWidget(self.lb_set_power)

        self.le_pwr_mnl = QLineEdit(self.layoutWidget4)
        self.le_pwr_mnl.setObjectName(u"le_pwr_mnl")
        self.le_pwr_mnl.setMinimumSize(QSize(0, 25))
        self.le_pwr_mnl.setMaximumSize(QSize(16777215, 16777215))
        self.le_pwr_mnl.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.le_pwr_mnl)

        self.layoutWidget5 = QWidget(self.centralwidget)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(170, 10, 141, 81))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lb_info = QLabel(self.layoutWidget5)
        self.lb_info.setObjectName(u"lb_info")

        self.verticalLayout_6.addWidget(self.lb_info)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_status = QLabel(self.layoutWidget5)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lb_status)

        self.lb_status_val = QLabel(self.layoutWidget5)
        self.lb_status_val.setObjectName(u"lb_status_val")
        self.lb_status_val.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lb_status_val)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_rmode = QLabel(self.layoutWidget5)
        self.lb_rmode.setObjectName(u"lb_rmode")
        self.lb_rmode.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.lb_rmode)

        self.lb_rmode_val = QLabel(self.layoutWidget5)
        self.lb_rmode_val.setObjectName(u"lb_rmode_val")
        self.lb_rmode_val.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.lb_rmode_val)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.layoutWidget6 = QWidget(self.centralwidget)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(20, 330, 141, 80))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_man_cmd = QLabel(self.layoutWidget6)
        self.lb_man_cmd.setObjectName(u"lb_man_cmd")

        self.verticalLayout_7.addWidget(self.lb_man_cmd)

        self.le_mnl_cmd = QLineEdit(self.layoutWidget6)
        self.le_mnl_cmd.setObjectName(u"le_mnl_cmd")
        self.le_mnl_cmd.setMinimumSize(QSize(0, 25))
        self.le_mnl_cmd.setMaximumSize(QSize(16777215, 16777215))
        self.le_mnl_cmd.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.le_mnl_cmd)

        self.btn_mnl_cmd = QPushButton(self.layoutWidget6)
        self.btn_mnl_cmd.setObjectName(u"btn_mnl_cmd")
        self.btn_mnl_cmd.setMinimumSize(QSize(0, 25))
        self.btn_mnl_cmd.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_mnl_cmd)

        self.layoutWidget7 = QWidget(self.centralwidget)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(320, 10, 461, 261))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget7)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.terminal_window = QTextBrowser(self.layoutWidget7)
        self.terminal_window.setObjectName(u"terminal_window")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.terminal_window.setFont(font)
        self.terminal_window.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.terminal_window)

        self.btn_clean_textBrw = QPushButton(self.layoutWidget7)
        self.btn_clean_textBrw.setObjectName(u"btn_clean_textBrw")
        self.btn_clean_textBrw.setMinimumSize(QSize(0, 25))
        self.btn_clean_textBrw.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.btn_clean_textBrw)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(800, 10, 126, 140))
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_latitude = QLabel(self.widget)
        self.lb_latitude.setObjectName(u"lb_latitude")
        self.lb_latitude.setMinimumSize(QSize(58, 0))
        self.lb_latitude.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_3.addWidget(self.lb_latitude)

        self.lb_latitude_val = QLabel(self.widget)
        self.lb_latitude_val.setObjectName(u"lb_latitude_val")

        self.horizontalLayout_3.addWidget(self.lb_latitude_val)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_NS = QLabel(self.widget)
        self.lb_NS.setObjectName(u"lb_NS")
        self.lb_NS.setMinimumSize(QSize(58, 0))
        self.lb_NS.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_4.addWidget(self.lb_NS)

        self.lb_NS_val = QLabel(self.widget)
        self.lb_NS_val.setObjectName(u"lb_NS_val")

        self.horizontalLayout_4.addWidget(self.lb_NS_val)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_longitude = QLabel(self.widget)
        self.lb_longitude.setObjectName(u"lb_longitude")
        self.lb_longitude.setMinimumSize(QSize(58, 0))
        self.lb_longitude.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_5.addWidget(self.lb_longitude)

        self.lb_longitude_val = QLabel(self.widget)
        self.lb_longitude_val.setObjectName(u"lb_longitude_val")

        self.horizontalLayout_5.addWidget(self.lb_longitude_val)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_EW = QLabel(self.widget)
        self.lb_EW.setObjectName(u"lb_EW")
        self.lb_EW.setMinimumSize(QSize(58, 0))
        self.lb_EW.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_6.addWidget(self.lb_EW)

        self.lb_EW_val = QLabel(self.widget)
        self.lb_EW_val.setObjectName(u"lb_EW_val")

        self.horizontalLayout_6.addWidget(self.lb_EW_val)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_altitude = QLabel(self.widget)
        self.lb_altitude.setObjectName(u"lb_altitude")
        self.lb_altitude.setMinimumSize(QSize(58, 0))
        self.lb_altitude.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_7.addWidget(self.lb_altitude)

        self.lb_altitude_val = QLabel(self.widget)
        self.lb_altitude_val.setObjectName(u"lb_altitude_val")

        self.horizontalLayout_7.addWidget(self.lb_altitude_val)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_grndspeed = QLabel(self.widget)
        self.lb_grndspeed.setObjectName(u"lb_grndspeed")
        self.lb_grndspeed.setMinimumSize(QSize(58, 0))
        self.lb_grndspeed.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_8.addWidget(self.lb_grndspeed)

        self.lb_grndspeed_val = QLabel(self.widget)
        self.lb_grndspeed_val.setObjectName(u"lb_grndspeed_val")

        self.horizontalLayout_8.addWidget(self.lb_grndspeed_val)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(800, 160, 131, 236))
        self.verticalLayout_10 = QVBoxLayout(self.widget1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_axl_x = QLabel(self.widget1)
        self.lb_axl_x.setObjectName(u"lb_axl_x")
        self.lb_axl_x.setMinimumSize(QSize(58, 0))
        self.lb_axl_x.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_9.addWidget(self.lb_axl_x)

        self.lb_axl_x_val = QLabel(self.widget1)
        self.lb_axl_x_val.setObjectName(u"lb_axl_x_val")
        self.lb_axl_x_val.setMinimumSize(QSize(0, 0))
        self.lb_axl_x_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.lb_axl_x_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_axl_y = QLabel(self.widget1)
        self.lb_axl_y.setObjectName(u"lb_axl_y")
        self.lb_axl_y.setMinimumSize(QSize(58, 0))
        self.lb_axl_y.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_10.addWidget(self.lb_axl_y)

        self.lb_axl_y_val = QLabel(self.widget1)
        self.lb_axl_y_val.setObjectName(u"lb_axl_y_val")
        self.lb_axl_y_val.setMinimumSize(QSize(0, 0))
        self.lb_axl_y_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.lb_axl_y_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_axl_z = QLabel(self.widget1)
        self.lb_axl_z.setObjectName(u"lb_axl_z")
        self.lb_axl_z.setMinimumSize(QSize(58, 0))
        self.lb_axl_z.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_11.addWidget(self.lb_axl_z)

        self.lb_axl_z_val = QLabel(self.widget1)
        self.lb_axl_z_val.setObjectName(u"lb_axl_z_val")
        self.lb_axl_z_val.setMinimumSize(QSize(0, 0))
        self.lb_axl_z_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_11.addWidget(self.lb_axl_z_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_mag_x = QLabel(self.widget1)
        self.lb_mag_x.setObjectName(u"lb_mag_x")
        self.lb_mag_x.setMinimumSize(QSize(58, 0))
        self.lb_mag_x.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_12.addWidget(self.lb_mag_x)

        self.lb_mag_x_val = QLabel(self.widget1)
        self.lb_mag_x_val.setObjectName(u"lb_mag_x_val")
        self.lb_mag_x_val.setMinimumSize(QSize(0, 0))
        self.lb_mag_x_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_12.addWidget(self.lb_mag_x_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lb_mag_y = QLabel(self.widget1)
        self.lb_mag_y.setObjectName(u"lb_mag_y")
        self.lb_mag_y.setMinimumSize(QSize(58, 0))
        self.lb_mag_y.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_13.addWidget(self.lb_mag_y)

        self.lb_mag_y_val = QLabel(self.widget1)
        self.lb_mag_y_val.setObjectName(u"lb_mag_y_val")
        self.lb_mag_y_val.setMinimumSize(QSize(0, 0))
        self.lb_mag_y_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_13.addWidget(self.lb_mag_y_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_mag_z = QLabel(self.widget1)
        self.lb_mag_z.setObjectName(u"lb_mag_z")
        self.lb_mag_z.setMinimumSize(QSize(58, 0))
        self.lb_mag_z.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_14.addWidget(self.lb_mag_z)

        self.lb_mag_z_val = QLabel(self.widget1)
        self.lb_mag_z_val.setObjectName(u"lb_mag_z_val")
        self.lb_mag_z_val.setMinimumSize(QSize(0, 0))
        self.lb_mag_z_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_14.addWidget(self.lb_mag_z_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lb_gyro_x = QLabel(self.widget1)
        self.lb_gyro_x.setObjectName(u"lb_gyro_x")
        self.lb_gyro_x.setMinimumSize(QSize(58, 0))
        self.lb_gyro_x.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_15.addWidget(self.lb_gyro_x)

        self.lb_gyro_x_val = QLabel(self.widget1)
        self.lb_gyro_x_val.setObjectName(u"lb_gyro_x_val")
        self.lb_gyro_x_val.setMinimumSize(QSize(0, 0))
        self.lb_gyro_x_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_15.addWidget(self.lb_gyro_x_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lb_gyro_y = QLabel(self.widget1)
        self.lb_gyro_y.setObjectName(u"lb_gyro_y")
        self.lb_gyro_y.setMinimumSize(QSize(58, 0))
        self.lb_gyro_y.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_16.addWidget(self.lb_gyro_y)

        self.lb_gyro_y_val = QLabel(self.widget1)
        self.lb_gyro_y_val.setObjectName(u"lb_gyro_y_val")
        self.lb_gyro_y_val.setMinimumSize(QSize(0, 0))
        self.lb_gyro_y_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_16.addWidget(self.lb_gyro_y_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lb_gyro_z = QLabel(self.widget1)
        self.lb_gyro_z.setObjectName(u"lb_gyro_z")
        self.lb_gyro_z.setMinimumSize(QSize(58, 0))
        self.lb_gyro_z.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_17.addWidget(self.lb_gyro_z)

        self.lb_gyro_z_val = QLabel(self.widget1)
        self.lb_gyro_z_val.setObjectName(u"lb_gyro_z_val")
        self.lb_gyro_z_val.setMinimumSize(QSize(0, 0))
        self.lb_gyro_z_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_17.addWidget(self.lb_gyro_z_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lb_grn_head = QLabel(self.widget1)
        self.lb_grn_head.setObjectName(u"lb_grn_head")
        self.lb_grn_head.setMinimumSize(QSize(58, 0))
        self.lb_grn_head.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_18.addWidget(self.lb_grn_head)

        self.lb_grn_head_val = QLabel(self.widget1)
        self.lb_grn_head_val.setObjectName(u"lb_grn_head_val")
        self.lb_grn_head_val.setMinimumSize(QSize(0, 0))
        self.lb_grn_head_val.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_18.addWidget(self.lb_grn_head_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_18)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 994, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_connection_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441 \u0442\u0435\u043b\u0435\u043c\u0435\u0442\u0440\u0438\u0438", None))
        self.btn_gps.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.btn_imu.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.cb_auto_gps.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e \u0437\u0430\u043f\u0440\u043e\u0441 GPS", None))
        self.cb_auto_imu.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e \u0437\u0430\u043f\u0440\u043e\u0441 IMU", None))
        self.lb_connection.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.btn_server_start.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b", None))
        self.btn_server_stop.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c\u0430", None))
        self.btn_mnl_mode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u043e\u0439", None))
        self.btn_rmt_mode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u044b\u0439", None))
        self.btn_auto_mode.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439", None))
        self.lb_mtr_ctrl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u0435\u043c", None))
        self.btn_motor_start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.btn_motor_stop.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.lb_set_power.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438", None))
        self.le_pwr_mnl.setText("")
        self.lb_info.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e", None))
        self.lb_status.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.lb_status_val.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d", None))
        self.lb_rmode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c", None))
        self.lb_rmode_val.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e", None))
        self.lb_man_cmd.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u0432\u0440\u0443\u0447\u043d\u0443\u044e", None))
        self.le_mnl_cmd.setText("")
        self.btn_mnl_cmd.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u0430", None))
        self.btn_clean_textBrw.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.lb_latitude.setText(QCoreApplication.translate("MainWindow", u"Latitide", None))
        self.lb_latitude_val.setText(QCoreApplication.translate("MainWindow", u"Latitide", None))
        self.lb_NS.setText(QCoreApplication.translate("MainWindow", u"NS", None))
        self.lb_NS_val.setText(QCoreApplication.translate("MainWindow", u"NS", None))
        self.lb_longitude.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lb_longitude_val.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lb_EW.setText(QCoreApplication.translate("MainWindow", u"EW", None))
        self.lb_EW_val.setText(QCoreApplication.translate("MainWindow", u"EW", None))
        self.lb_altitude.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.lb_altitude_val.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.lb_grndspeed.setText(QCoreApplication.translate("MainWindow", u"GrndSpeed", None))
        self.lb_grndspeed_val.setText(QCoreApplication.translate("MainWindow", u"GrndSpeed", None))
        self.lb_axl_x.setText(QCoreApplication.translate("MainWindow", u"AXL_x", None))
        self.lb_axl_x_val.setText(QCoreApplication.translate("MainWindow", u"AXL_x", None))
        self.lb_axl_y.setText(QCoreApplication.translate("MainWindow", u"AXL_y", None))
        self.lb_axl_y_val.setText(QCoreApplication.translate("MainWindow", u"AXL_y", None))
        self.lb_axl_z.setText(QCoreApplication.translate("MainWindow", u"AXL_z", None))
        self.lb_axl_z_val.setText(QCoreApplication.translate("MainWindow", u"AXL_z", None))
        self.lb_mag_x.setText(QCoreApplication.translate("MainWindow", u"MAG_x", None))
        self.lb_mag_x_val.setText(QCoreApplication.translate("MainWindow", u"MAG_x", None))
        self.lb_mag_y.setText(QCoreApplication.translate("MainWindow", u"MAG_y", None))
        self.lb_mag_y_val.setText(QCoreApplication.translate("MainWindow", u"MAG_y", None))
        self.lb_mag_z.setText(QCoreApplication.translate("MainWindow", u"MAG_z", None))
        self.lb_mag_z_val.setText(QCoreApplication.translate("MainWindow", u"MAG_z", None))
        self.lb_gyro_x.setText(QCoreApplication.translate("MainWindow", u"GYRO_x", None))
        self.lb_gyro_x_val.setText(QCoreApplication.translate("MainWindow", u"GYRO_x", None))
        self.lb_gyro_y.setText(QCoreApplication.translate("MainWindow", u"GYRO_y", None))
        self.lb_gyro_y_val.setText(QCoreApplication.translate("MainWindow", u"GYRO_y", None))
        self.lb_gyro_z.setText(QCoreApplication.translate("MainWindow", u"GYRO_z", None))
        self.lb_gyro_z_val.setText(QCoreApplication.translate("MainWindow", u"GYRO_z", None))
        self.lb_grn_head.setText(QCoreApplication.translate("MainWindow", u"GndHead", None))
        self.lb_grn_head_val.setText(QCoreApplication.translate("MainWindow", u"GndHead", None))
    # retranslateUi

