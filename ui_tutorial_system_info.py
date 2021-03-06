# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tutorial_system_infosilIil.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(699, 600)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background: #171C29;\n"
"}\n"
"QProgressBar{\n"
"background-color:rgb(20,30,43);\n"
"border-style: none;\n"
"border-radius: 10px;\n"
"text-align:center;\n"
"color:rgb(255,0,0)\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color:qlineargradient(spread:pad,x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,136,255,255), stop:1 rgba(255,255,255,255));\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(29, 47, 65);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_button = QPushButton(self.header_left_frame)
        self.open_close_side_bar_button.setObjectName(u"open_close_side_bar_button")
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.open_close_side_bar_button.setFont(font)
        self.open_close_side_bar_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/feather/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_button.setIcon(icon)
        self.open_close_side_bar_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_button, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setPixmap(QPixmap(u":/icons/icons/feather/airplay.svg"))

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setEnabled(True)
        self.header_right_frame.setMinimumSize(QSize(100, 0))
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil/cil-window-restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        self.left_menu_cont_frame.setMinimumSize(QSize(40, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_cont_frame.setStyleSheet(u"background-color: #1D2F41")
        self.left_menu_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(100, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.cpu_page_btn = QPushButton(self.menu_frame)
        self.cpu_page_btn.setObjectName(u"cpu_page_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/feather/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_page_btn.setIcon(icon4)
        self.cpu_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.cpu_page_btn, 0, 0, 1, 1, Qt.AlignLeft)

        self.activity_page_btn = QPushButton(self.menu_frame)
        self.activity_page_btn.setObjectName(u"activity_page_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/feather/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_page_btn.setIcon(icon5)
        self.activity_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.activity_page_btn, 3, 0, 1, 1, Qt.AlignLeft)

        self.sensors_page_btn = QPushButton(self.menu_frame)
        self.sensors_page_btn.setObjectName(u"sensors_page_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/feather/thermometer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sensors_page_btn.setIcon(icon6)
        self.sensors_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.sensors_page_btn, 5, 0, 1, 1, Qt.AlignLeft)

        self.battery_page_btn = QPushButton(self.menu_frame)
        self.battery_page_btn.setObjectName(u"battery_page_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/feather/battery-charging.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_page_btn.setIcon(icon7)
        self.battery_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.battery_page_btn, 1, 0, 1, 1, Qt.AlignLeft)

        self.system_inf_page_btn = QPushButton(self.menu_frame)
        self.system_inf_page_btn.setObjectName(u"system_inf_page_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/feather/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.system_inf_page_btn.setIcon(icon8)
        self.system_inf_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.system_inf_page_btn, 2, 0, 1, 1, Qt.AlignLeft)

        self.networks_page_btn = QPushButton(self.menu_frame)
        self.networks_page_btn.setObjectName(u"networks_page_btn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/feather/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.networks_page_btn.setIcon(icon9)
        self.networks_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.networks_page_btn, 6, 0, 1, 1, Qt.AlignLeft)

        self.storage_page_btn = QPushButton(self.menu_frame)
        self.storage_page_btn.setObjectName(u"storage_page_btn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/feather/disc.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_page_btn.setIcon(icon10)
        self.storage_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.storage_page_btn, 4, 0, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setMargin(5)

        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)

        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setMargin(5)

        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)

        self.label_10 = QLabel(self.menu_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setMargin(5)

        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_cont_frame)

        self.main_body_contents = QFrame(self.main_body_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_4 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cpu_info_frame = QFrame(self.cpu_and_memory)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_16 = QLabel(self.cpu_info_frame)
        self.label_16.setObjectName(u"label_16")
        font3 = QFont()
        font3.setFamily(u"Noto Sans")
        font3.setPointSize(10)
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.label_19 = QLabel(self.cpu_info_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_12 = QLabel(self.cpu_info_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)

        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")
        self.cpu_count.setFont(font3)
        self.cpu_count.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.cpu_count, 0, 1, 1, 1)

        self.cpu_per = QLabel(self.cpu_info_frame)
        self.cpu_per.setObjectName(u"cpu_per")
        self.cpu_per.setFont(font3)
        self.cpu_per.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.cpu_per, 1, 1, 1, 1)

        self.cpu_main_core = QLabel(self.cpu_info_frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")
        self.cpu_main_core.setFont(font3)
        self.cpu_main_core.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.cpu_main_core, 2, 1, 1, 1)

        self.cpu_percentage = roundProgressBar(self.cpu_info_frame)
        self.cpu_percentage.setObjectName(u"cpu_percentage")
        self.cpu_percentage.setMinimumSize(QSize(150, 150))
        self.cpu_percentage.setMaximumSize(QSize(150, 150))

        self.gridLayout_3.addWidget(self.cpu_percentage, 0, 3, 3, 1)


        self.verticalLayout_4.addWidget(self.cpu_info_frame)

        self.ram_info_frame = QFrame(self.cpu_and_memory)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.ram_info_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.free_used = QLabel(self.ram_info_frame)
        self.free_used.setObjectName(u"free_used")
        self.free_used.setFont(font3)
        self.free_used.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.free_used, 3, 1, 1, 1)

        self.label_21 = QLabel(self.ram_info_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_21, 0, 0, 1, 1)

        self.used_ram = QLabel(self.ram_info_frame)
        self.used_ram.setObjectName(u"used_ram")
        self.used_ram.setFont(font3)
        self.used_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.used_ram, 2, 1, 1, 1)

        self.label_25 = QLabel(self.ram_info_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_26 = QLabel(self.ram_info_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_26, 3, 0, 1, 1)

        self.label_27 = QLabel(self.ram_info_frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_27, 4, 0, 1, 1)

        self.total_ram = QLabel(self.ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")
        self.total_ram.setFont(font3)
        self.total_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_22 = QLabel(self.ram_info_frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_22, 1, 0, 1, 1)

        self.ram_usage = QLabel(self.ram_info_frame)
        self.ram_usage.setObjectName(u"ram_usage")
        self.ram_usage.setFont(font3)
        self.ram_usage.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ram_usage, 4, 1, 1, 1)

        self.available_ram = QLabel(self.ram_info_frame)
        self.available_ram.setObjectName(u"available_ram")
        self.available_ram.setFont(font3)
        self.available_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.available_ram, 1, 1, 1, 1)

        self.ram_percentage = spiralProgressBar(self.ram_info_frame)
        self.ram_percentage.setObjectName(u"ram_percentage")
        self.ram_percentage.setMinimumSize(QSize(150, 150))
        self.ram_percentage.setMaximumSize(QSize(150, 150))

        self.gridLayout_4.addWidget(self.ram_percentage, 0, 2, 5, 1)


        self.verticalLayout_4.addWidget(self.ram_info_frame)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.verticalLayout_5 = QVBoxLayout(self.battery)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.battery)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_31, 0, Qt.AlignBottom)

        self.frame_3 = QFrame(self.battery)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.label_35, 4, 0, 1, 1)

        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.label_32, 0, 0, 1, 1)

        self.battery_usage = roundProgressBar(self.frame_3)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMinimumSize(QSize(150, 150))
        self.battery_usage.setMaximumSize(QSize(150, 150))

        self.gridLayout_5.addWidget(self.battery_usage, 0, 2, 5, 1)

        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.label_33, 1, 0, 2, 1)

        self.battery_time_left = QLabel(self.frame_3)
        self.battery_time_left.setObjectName(u"battery_time_left")
        self.battery_time_left.setFont(font3)
        self.battery_time_left.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.battery_time_left, 2, 1, 2, 1)

        self.battery_charge = QLabel(self.frame_3)
        self.battery_charge.setObjectName(u"battery_charge")
        self.battery_charge.setFont(font3)
        self.battery_charge.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.battery_charge, 1, 1, 1, 1)

        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.label_34, 3, 0, 1, 1)

        self.battery_plugged = QLabel(self.frame_3)
        self.battery_plugged.setObjectName(u"battery_plugged")
        self.battery_plugged.setFont(font3)
        self.battery_plugged.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.battery_plugged, 4, 1, 1, 1)

        self.battery_status = QLabel(self.frame_3)
        self.battery_status.setObjectName(u"battery_status")
        self.battery_status.setFont(font3)
        self.battery_status.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.battery_status, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.battery)
        self.system_information = QWidget()
        self.system_information.setObjectName(u"system_information")
        self.verticalLayout_6 = QVBoxLayout(self.system_information)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.system_information)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.system_version = QLabel(self.frame_4)
        self.system_version.setObjectName(u"system_version")
        self.system_version.setFont(font3)
        self.system_version.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.system_version, 4, 1, 1, 1)

        self.label_48 = QLabel(self.frame_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_48, 2, 2, 1, 1)

        self.system_system = QLabel(self.frame_4)
        self.system_system.setObjectName(u"system_system")
        self.system_system.setFont(font)
        self.system_system.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.system_system, 1, 0, 1, 2)

        self.label_43 = QLabel(self.frame_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_43, 4, 0, 1, 1)

        self.label_44 = QLabel(self.frame_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)
        self.label_44.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_44, 7, 0, 1, 1)

        self.system_date = QLabel(self.frame_4)
        self.system_date.setObjectName(u"system_date")
        self.system_date.setFont(font3)
        self.system_date.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.system_date, 7, 1, 1, 1)

        self.system_processor = QLabel(self.frame_4)
        self.system_processor.setObjectName(u"system_processor")
        self.system_processor.setFont(font3)
        self.system_processor.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.system_processor, 2, 3, 1, 1)

        self.system_time = QLabel(self.frame_4)
        self.system_time.setObjectName(u"system_time")
        self.system_time.setFont(font3)
        self.system_time.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.system_time, 7, 3, 1, 1)

        self.label_42 = QLabel(self.frame_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font)
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_42, 2, 0, 1, 1)

        self.label_40 = QLabel(self.frame_4)
        self.label_40.setObjectName(u"label_40")
        font4 = QFont()
        font4.setFamily(u"Noto Sans")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_40.setFont(font4)
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_40, 0, 0, 1, 2)

        self.system_platform = QLabel(self.frame_4)
        self.system_platform.setObjectName(u"system_platform")
        self.system_platform.setFont(font3)
        self.system_platform.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.system_platform, 2, 1, 1, 1)

        self.label_50 = QLabel(self.frame_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)
        self.label_50.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_50, 7, 2, 1, 1)

        self.label_49 = QLabel(self.frame_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_49, 4, 2, 1, 1)

        self.system_machine = QLabel(self.frame_4)
        self.system_machine.setObjectName(u"system_machine")
        self.system_machine.setFont(font3)
        self.system_machine.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.system_machine, 4, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.system_information)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_7 = QVBoxLayout(self.activities)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.activities)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_54 = QLabel(self.frame_5)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)
        self.label_54.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.label_54)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.activity_search = QLineEdit(self.frame_8)
        self.activity_search.setObjectName(u"activity_search")
        self.activity_search.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.activity_search)

        self.pushButton_3 = QPushButton(self.frame_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/feather/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon11)

        self.horizontalLayout_12.addWidget(self.pushButton_3)


        self.horizontalLayout_11.addWidget(self.frame_8, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.activities)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        font5 = QFont()
        font5.setFamily(u"Noto Sans")
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        font6 = QFont()
        font6.setFamily(u"Noto Sans")
        font6.setPointSize(9)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_8.addWidget(self.tableWidget)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.activities)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font7 = QFont()
        font7.setFamily(u"Noto Sans")
        font7.setPointSize(12)
        self.pushButton_4.setFont(font7)
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font7)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font7)
        self.pushButton_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font7)
        self.pushButton_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.pushButton_7)


        self.verticalLayout_7.addWidget(self.frame_7, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activities)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_9 = QVBoxLayout(self.storage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_55 = QLabel(self.storage)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font4)
        self.label_55.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_55)

        self.storageTable = QTableWidget(self.storage)
        if (self.storageTable.columnCount() < 10):
            self.storageTable.setColumnCount(10)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font5);
        self.storageTable.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font5);
        self.storageTable.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.storageTable.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.storageTable.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.storageTable.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font5);
        self.storageTable.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.storageTable.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.storageTable.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.storageTable.setHorizontalHeaderItem(9, __qtablewidgetitem17)
        self.storageTable.setObjectName(u"storageTable")

        self.verticalLayout_9.addWidget(self.storageTable)

        self.stackedWidget.addWidget(self.storage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.verticalLayout_10 = QVBoxLayout(self.sensors)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_56 = QLabel(self.sensors)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font4)
        self.label_56.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_56)

        self.sensorTable = QTableWidget(self.sensors)
        if (self.sensorTable.columnCount() < 6):
            self.sensorTable.setColumnCount(6)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font5);
        self.sensorTable.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font5);
        self.sensorTable.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font5);
        self.sensorTable.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font5);
        self.sensorTable.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font5);
        self.sensorTable.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font5);
        self.sensorTable.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        self.sensorTable.setObjectName(u"sensorTable")

        self.verticalLayout_10.addWidget(self.sensorTable)

        self.stackedWidget.addWidget(self.sensors)
        self.networks = QWidget()
        self.networks.setObjectName(u"networks")
        self.verticalLayout_11 = QVBoxLayout(self.networks)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea = QScrollArea(self.networks)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 420, 784))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_57 = QLabel(self.frame_9)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font4)
        self.label_57.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.label_57)

        self.net_stats_table = QTableWidget(self.frame_9)
        if (self.net_stats_table.columnCount() < 5):
            self.net_stats_table.setColumnCount(5)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        self.net_stats_table.setObjectName(u"net_stats_table")
        self.net_stats_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_13.addWidget(self.net_stats_table)


        self.verticalLayout_12.addWidget(self.frame_9)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_59 = QLabel(self.frame_12)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font4)
        self.label_59.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_59)

        self.net_io_table = QTableWidget(self.frame_12)
        if (self.net_io_table.columnCount() < 9):
            self.net_io_table.setColumnCount(9)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(8, __qtablewidgetitem37)
        self.net_io_table.setObjectName(u"net_io_table")
        self.net_io_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_14.addWidget(self.net_io_table)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_60 = QLabel(self.frame_11)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font4)
        self.label_60.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.label_60)

        self.net_address_table = QTableWidget(self.frame_11)
        if (self.net_address_table.columnCount() < 6):
            self.net_address_table.setColumnCount(6)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(5, __qtablewidgetitem43)
        self.net_address_table.setObjectName(u"net_address_table")
        self.net_address_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_15.addWidget(self.net_address_table)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_61 = QLabel(self.frame_10)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font4)
        self.label_61.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_61)

        self.net_connections_table = QTableWidget(self.frame_10)
        if (self.net_connections_table.columnCount() < 7):
            self.net_connections_table.setColumnCount(7)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(6, __qtablewidgetitem50)
        self.net_connections_table.setObjectName(u"net_connections_table")
        self.net_connections_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_16.addWidget(self.net_connections_table)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.networks)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_body_contents)

        self.right_frame = QFrame(self.main_body_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMaximumSize(QSize(300, 16777215))
        self.right_frame.setStyleSheet(u"background-color: rgb(29, 47, 65);")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.right_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_2 = QFrame(self.right_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(200, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setMaximumSize(QSize(301, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        font8 = QFont()
        font8.setFamily(u"Noto Sans")
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setUnderline(True)
        font8.setWeight(75)
        self.label_14.setFont(font8)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_14, 4, 1, 1, 1, Qt.AlignLeft)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_15, 9, 1, 1, 1, Qt.AlignLeft)

        self.pushButton_12 = QPushButton(self.frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        font9 = QFont()
        font9.setBold(True)
        font9.setWeight(75)
        self.pushButton_12.setFont(font9)
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/feather/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon12)
        self.pushButton_12.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.pushButton_12, 9, 0, 1, 1, Qt.AlignLeft)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font8)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_13, 3, 1, 1, 1, Qt.AlignLeft)

        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font9)
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/feather/coffee.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon13)
        self.pushButton_11.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.pushButton_11, 4, 0, 1, 1, Qt.AlignLeft)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font9)
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/feather/youtube.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon14)
        self.pushButton_10.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1, Qt.AlignLeft)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 2, Qt.AlignLeft)

        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy2)
        self.textBrowser.setMinimumSize(QSize(20, 0))
        self.textBrowser.setMaximumSize(QSize(300, 301))
        self.textBrowser.setFont(font4)
        self.textBrowser.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)

        self.gridLayout_2.addWidget(self.textBrowser, 2, 0, 1, 2, Qt.AlignLeft)


        self.horizontalLayout_10.addWidget(self.frame, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.footer_left_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(229, 229, 229);")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color: rgb(229, 229, 229);")

        self.horizontalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PSUTIL MANAGER", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_page_btn.setText("")
        self.activity_page_btn.setText("")
        self.sensors_page_btn.setText("")
        self.battery_page_btn.setText("")
        self.system_inf_page_btn.setText("")
        self.networks_page_btn.setText("")
        self.storage_page_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sysem Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.free_used.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Total RAM", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Used RAM", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Available RAM", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.system_system.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.system_platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.pushButton_3.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"PROCESS ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PROCESS NAME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PROCESS STATUS", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"SUSPEND", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"STARTED", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"RESUME", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TERMINATE", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"KILL", None));
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Disk Partitions", None))
        ___qtablewidgetitem8 = self.storageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"DEVICE", None));
        ___qtablewidgetitem9 = self.storageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"MOUNT POINT", None));
        ___qtablewidgetitem10 = self.storageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem11 = self.storageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"MAX", None));
        ___qtablewidgetitem12 = self.storageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"MAX FILE", None));
        ___qtablewidgetitem13 = self.storageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"MAX PATH", None));
        ___qtablewidgetitem14 = self.storageTable.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TOTAL STORAGE", None));
        ___qtablewidgetitem15 = self.storageTable.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"FREE STORAGE", None));
        ___qtablewidgetitem16 = self.storageTable.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"USED STORAGE", None));
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem17 = self.sensorTable.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"SENSOR", None));
        ___qtablewidgetitem18 = self.sensorTable.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"LABEL", None));
        ___qtablewidgetitem19 = self.sensorTable.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"CURRENT", None));
        ___qtablewidgetitem20 = self.sensorTable.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"HIGH", None));
        ___qtablewidgetitem21 = self.sensorTable.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"CRITICAL", None));
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem22 = self.net_stats_table.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem23 = self.net_stats_table.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"DUPLEX", None));
        ___qtablewidgetitem24 = self.net_stats_table.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"SPEED", None));
        ___qtablewidgetitem25 = self.net_stats_table.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Network IO Counters", None))
        ___qtablewidgetitem26 = self.net_io_table.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"IO", None));
        ___qtablewidgetitem27 = self.net_io_table.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"BYTES SENT", None));
        ___qtablewidgetitem28 = self.net_io_table.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"BYTES RECEIVED", None));
        ___qtablewidgetitem29 = self.net_io_table.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"PACKETS SENT", None));
        ___qtablewidgetitem30 = self.net_io_table.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"PACKETS RECEIVED", None));
        ___qtablewidgetitem31 = self.net_io_table.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ERR In", None));
        ___qtablewidgetitem32 = self.net_io_table.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ERR Out", None));
        ___qtablewidgetitem33 = self.net_io_table.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"DROP IN", None));
        ___qtablewidgetitem34 = self.net_io_table.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"DROP OUT", None));
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Network Addresses", None))
        ___qtablewidgetitem35 = self.net_address_table.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem36 = self.net_address_table.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"ADDRESS", None));
        ___qtablewidgetitem37 = self.net_address_table.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"NETMASK", None));
        ___qtablewidgetitem38 = self.net_address_table.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"BROADCAST", None));
        ___qtablewidgetitem39 = self.net_address_table.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Network Connections", None))
        ___qtablewidgetitem40 = self.net_connections_table.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem41 = self.net_connections_table.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem42 = self.net_connections_table.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem43 = self.net_connections_table.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"LADDR", None));
        ___qtablewidgetitem44 = self.net_connections_table.horizontalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem45 = self.net_connections_table.horizontalHeaderItem(5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem46 = self.net_connections_table.horizontalHeaderItem(6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Patreon/", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PayPal", None))
        self.pushButton_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Youtube/", None))
        self.pushButton_11.setText("")
        self.pushButton_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400;\">App Designed And Developed By Khamisi Kibet.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright Spinn Co.", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

