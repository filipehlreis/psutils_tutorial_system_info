# #############################################
# SPINN Design Code
# #############################################

# Imports
import sys
import os
from turtle import width
from PySide2 import *
# Import QT Material
from qt_material import *
# import PSUtil
import psutil
# Import PYSIDE2EXTN
import PySide2extn


# Import GUI File
from ui_tutorial_system_info import *


# Main Window Class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load Style sheet, this will override and fonts selected in qt
        # designer
        apply_stylesheet(app, theme="dark_cyan.xml")

        # Remove window tittle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        # Apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Set window icon
        # This icon and title will not appear on our app main window because
        # we removed the title bar
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/feather/airplay.svg"))
        # Set window title
        self.setWindowTitle("UTIL Manager")

        # Window Size grip to resize window
        QSizeGrip(self.ui.size_grip)

        # # Navigation Window Bar
        # Minimize window
        self.ui.minimize_window_button.clicked.connect(
            lambda: self.showMinimized())

        # Close window
        self.ui.close_window_button.clicked.connect(
            lambda: self.close())

        # Restore/Maximize Window
        self.ui.restore_window_button.clicked.connect(
            lambda: self.restore_or_maximize_window())

        # STACKED PAGES NAVIGATION /////////////////////////
        # Using side menu buttons

        # navigate to CPU page
        self.ui.cpu_page_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.cpu_and_memory))

        # navigate to Battery page
        self.ui.battery_page_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.battery))

        # navigate to system info page
        self.ui.system_inf_page_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.system_information))

        # navigate to activity page
        self.ui.activity_page_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.activities))

        # navigate to storage page
        self.ui.storage_page_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.storage))

        # navigate to sensors page
        self.ui.sensors_page_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.sensors))

        # navigate to networks page
        self.ui.networks_page_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.networks))

        # Function to move window on mouse drag event on the title bar
        def moveWindow(e):
            # detect if the window is normal size
            if self.isMaximized() == False:  # not maximize
                # move window only when window is normal size
                #####
                # if left mouse button is clicked (only accept left mouse
                # button clicks)
                if e.buttons() == Qt.LeftButton:
                    # move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        # add click event/mouse move event/drag event to the top header to
        # move the window
        self.ui.header_frame.mouseMoveEvent = moveWindow

        # left menu toggle button (show hide menu labels)
        self.ui.open_close_side_bar_button.clicked.connect(
            lambda: self.slideLeftMenu())

        # Style clicked menu button
        for w in self.ui.menu_frame.findChildren(QPushButton):
            # Add click event listener
            w.clicked.connect(self.applyButtonStyle)

        self.show()

        self.battery()

    # A function to convert seconds to hours

    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)

    # Get system battery information

    def battery(self):
        batt = psutil.sensors_battery()
        self.ui.battery_usage.show()

        if not hasattr(psutil, "sensors_battery"):
            self.ui.battery_status.setText("Platform not supported")

        if batt is None:
            self.ui.battery_status.setText("No battery installed")

        if hasattr(batt, "power_plugged"):
            if batt.power_plugged:
                self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
                self.ui.battery_time_left.setText("N/A")

                if batt.percent < 100:
                    self.ui.battery_status.setText("Charging")
                else:
                    self.ui.battery_status.setText("Fully Charged")

                self.ui.battery_plugged.setText("Yes")

            else:
                self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
                self.ui.battery_time_left.setText(
                    self.secs2hours(batt.secsleft))

                if batt.percent < 100:
                    self.ui.battery_status.setText("Discharging")
                else:
                    self.ui.battery_status.setText("Fully Charged")

                self.ui.battery_plugged.setText("No")

        if hasattr(batt, "percent"):
            # Battery Power Indicator using round progress bar
            # SET progress bar value
            self.ui.battery_usage.rpb_setMaximum(100)
            # SET Progress values
            self.ui.battery_usage.rpb_setValue(batt.percent)
            # SET progress bar style
            self.ui.battery_usage.rpb_setBarStyle("Hybrid2")
            # SET progress bar line color
            self.ui.battery_usage.rpb_setLineColor((255, 30, 90))
            # SET progress bar line color
            # self.ui.battery_usage.rpb_setCircleColor((45, 74, 83))
            # SET progress bar line color
            self.ui.battery_usage.rpb_setPieColor((45, 74, 83))
            # CHANGING the path color
            # self.ui.battery_usage.rpb_setPathColor((45, 74, 83))
            # SET progress bar TEXT COLOR
            self.ui.battery_usage.rpb_setTextColor((255, 255, 255))
            # SET Progress bar starting position
            # North, East, West, South
            self.ui.battery_usage.rpb_setInitialPos("West")
            # SET progress bar text type: VALUE or PERCENTAGE
            # Value, Percentage
            self.ui.battery_usage.rpb_setTextFormat("Percentage")
            # SET progress bar font
            # set progress bar line width
            self.ui.battery_usage.rpb_setLineWidth(15)
            # Path width
            self.ui.battery_usage.rpb_setPathWidth(15)
            # set progress bar line cap
            # RoundCap, SquareCap
            self.ui.battery_usage.rpb_setLineCap("RoundCap")
            # Line Style
            # DotLine, DashLine
            # self.ui.battery_usage.rpb_setLineStyle("DotLine")
        else:
            self.ui.battery_usage.hide()

    # Side Menu buttons styling function

    def applyButtonStyle(self):
        # Reset style for other buttons
        for w in self.ui.menu_frame.findChildren(QPushButton):
            # If the button name is not equal to clicked button name
            if w.objectName() != self.sender().objectName():
                # Create defaul style by removing the left border
                # Lets remove the bottom border style

                # Lets also remove the left border style

                # Apply the default style
                w.setStyleSheet("border-bottom: none;")

        # Apply new style to clicked button
        # Sender = clicked button
        # Get the clicked button stylesheet then add new left-border style to it
        # Lets add the bottom border style
        # Apply the new style
        self.sender().setStyleSheet("border-bottom: 2px solid;")
        #
        return

    # slide left menu function

    def slideLeftMenu(self):
        # get current left menu width
        width = self.ui.left_menu_cont_frame.width()

        # if minimized
        if width == 40:
            # Expand menu
            newWidth = 200
        # if maximized
        else:
            # retore menu
            newWidth = 40

        # animate the transition
        self.animation = QPropertyAnimation(
            self.ui.left_menu_cont_frame, b"minimumWidth")  # animate
        self.animation.setDuration(250)
        # start value is the current menu width
        self.animation.setStartValue(width)
        # end value is the new menu width
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

        # add mouse events to the window
    def mousePressEvent(self, event):
        # get the current position of the mouse
        self.clickPosition = event.globalPos()
        # we will use this value to move the window

    # update restore button icon on maximizing or minimizing window
    def restore_or_maximize_window(self):
        # IF window is maximized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.restore_window_button.setIcon(
                QtGui.QIcon(u":/icons/icons/cil/cil-window-restore.png"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.restore_window_button.setIcon(
                QtGui.QIcon(u":/icons/icons/cil/cil-window-maximize.png"))


# Execute App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
