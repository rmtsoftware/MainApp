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
        MainWindow.resize(800, 461)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 100, 141, 130))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_connection_2 = QLabel(self.widget)
        self.lb_connection_2.setObjectName(u"lb_connection_2")

        self.verticalLayout.addWidget(self.lb_connection_2)

        self.btn_gps = QPushButton(self.widget)
        self.btn_gps.setObjectName(u"btn_gps")

        self.verticalLayout.addWidget(self.btn_gps)

        self.btn_imu = QPushButton(self.widget)
        self.btn_imu.setObjectName(u"btn_imu")

        self.verticalLayout.addWidget(self.btn_imu)

        self.cb_auto_gps = QCheckBox(self.widget)
        self.cb_auto_gps.setObjectName(u"cb_auto_gps")

        self.verticalLayout.addWidget(self.cb_auto_gps)

        self.cb_auto_imu = QCheckBox(self.widget)
        self.cb_auto_imu.setObjectName(u"cb_auto_imu")

        self.verticalLayout.addWidget(self.cb_auto_imu)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 10, 141, 78))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_connection = QLabel(self.widget1)
        self.lb_connection.setObjectName(u"lb_connection")

        self.verticalLayout_2.addWidget(self.lb_connection)

        self.btn_server_start = QPushButton(self.widget1)
        self.btn_server_start.setObjectName(u"btn_server_start")

        self.verticalLayout_2.addWidget(self.btn_server_start)

        self.btn_server_stop = QPushButton(self.widget1)
        self.btn_server_stop.setObjectName(u"btn_server_stop")

        self.verticalLayout_2.addWidget(self.btn_server_stop)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(170, 100, 141, 111))
        self.verticalLayout_3 = QVBoxLayout(self.widget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.btn_mnl_mode = QPushButton(self.widget2)
        self.btn_mnl_mode.setObjectName(u"btn_mnl_mode")
        self.btn_mnl_mode.setMinimumSize(QSize(0, 25))
        self.btn_mnl_mode.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_mnl_mode)

        self.btn_rmt_mode = QPushButton(self.widget2)
        self.btn_rmt_mode.setObjectName(u"btn_rmt_mode")
        self.btn_rmt_mode.setMinimumSize(QSize(0, 25))
        self.btn_rmt_mode.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_rmt_mode)

        self.btn_auto_mode = QPushButton(self.widget2)
        self.btn_auto_mode.setObjectName(u"btn_auto_mode")
        self.btn_auto_mode.setMinimumSize(QSize(0, 25))
        self.btn_auto_mode.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_auto_mode)

        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(20, 240, 141, 80))
        self.verticalLayout_4 = QVBoxLayout(self.widget3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_mtr_ctrl = QLabel(self.widget3)
        self.lb_mtr_ctrl.setObjectName(u"lb_mtr_ctrl")

        self.verticalLayout_4.addWidget(self.lb_mtr_ctrl)

        self.btn_motor_start = QPushButton(self.widget3)
        self.btn_motor_start.setObjectName(u"btn_motor_start")
        self.btn_motor_start.setMinimumSize(QSize(0, 25))
        self.btn_motor_start.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_motor_start)

        self.btn_motor_stop = QPushButton(self.widget3)
        self.btn_motor_stop.setObjectName(u"btn_motor_stop")
        self.btn_motor_stop.setMinimumSize(QSize(0, 25))
        self.btn_motor_stop.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_motor_stop)

        self.widget4 = QWidget(self.centralwidget)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(170, 220, 141, 49))
        self.verticalLayout_5 = QVBoxLayout(self.widget4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_set_power = QLabel(self.widget4)
        self.lb_set_power.setObjectName(u"lb_set_power")

        self.verticalLayout_5.addWidget(self.lb_set_power)

        self.le_pwr_mnl = QLineEdit(self.widget4)
        self.le_pwr_mnl.setObjectName(u"le_pwr_mnl")
        self.le_pwr_mnl.setMinimumSize(QSize(0, 25))
        self.le_pwr_mnl.setMaximumSize(QSize(16777215, 16777215))
        self.le_pwr_mnl.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.le_pwr_mnl)

        self.widget5 = QWidget(self.centralwidget)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(170, 10, 141, 81))
        self.verticalLayout_6 = QVBoxLayout(self.widget5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lb_info = QLabel(self.widget5)
        self.lb_info.setObjectName(u"lb_info")

        self.verticalLayout_6.addWidget(self.lb_info)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_status = QLabel(self.widget5)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lb_status)

        self.lb_status_val = QLabel(self.widget5)
        self.lb_status_val.setObjectName(u"lb_status_val")
        self.lb_status_val.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lb_status_val)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_rmode = QLabel(self.widget5)
        self.lb_rmode.setObjectName(u"lb_rmode")
        self.lb_rmode.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.lb_rmode)

        self.lb_rmode_val = QLabel(self.widget5)
        self.lb_rmode_val.setObjectName(u"lb_rmode_val")
        self.lb_rmode_val.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.lb_rmode_val)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.widget6 = QWidget(self.centralwidget)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(20, 330, 141, 80))
        self.verticalLayout_7 = QVBoxLayout(self.widget6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_man_cmd = QLabel(self.widget6)
        self.lb_man_cmd.setObjectName(u"lb_man_cmd")

        self.verticalLayout_7.addWidget(self.lb_man_cmd)

        self.le_mnl_cmd = QLineEdit(self.widget6)
        self.le_mnl_cmd.setObjectName(u"le_mnl_cmd")
        self.le_mnl_cmd.setMinimumSize(QSize(0, 25))
        self.le_mnl_cmd.setMaximumSize(QSize(16777215, 16777215))
        self.le_mnl_cmd.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.le_mnl_cmd)

        self.btn_mnl_cmd = QPushButton(self.widget6)
        self.btn_mnl_cmd.setObjectName(u"btn_mnl_cmd")
        self.btn_mnl_cmd.setMinimumSize(QSize(0, 25))
        self.btn_mnl_cmd.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_mnl_cmd)

        self.widget7 = QWidget(self.centralwidget)
        self.widget7.setObjectName(u"widget7")
        self.widget7.setGeometry(QRect(320, 10, 461, 261))
        self.verticalLayout_8 = QVBoxLayout(self.widget7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget7)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.terminal_window = QTextBrowser(self.widget7)
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

        self.btn_clean_textBrw = QPushButton(self.widget7)
        self.btn_clean_textBrw.setObjectName(u"btn_clean_textBrw")
        self.btn_clean_textBrw.setMinimumSize(QSize(0, 25))
        self.btn_clean_textBrw.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.btn_clean_textBrw)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
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
    # retranslateUi

