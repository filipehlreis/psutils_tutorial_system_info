# #############################################
# SPINN Design Code
# #############################################

# Imports
from datetime import datetime
import platform
import shutil
import sys
import os
from turtle import width
from PySide2 import *
from multiprocessing import cpu_count
# Import QT Material
from qt_material import *
# import PSUtil
import psutil
# Import PYSIDE2EXTN
import PySide2extn

from time import sleep

# Import GUI File
from ui_tutorial_system_info import *


# Global
platforms = {
    "linux": "Linux",
    "linux1": "Linux",
    "linux2": "Linux",
    "darwin": "OS X",
    "win32": "Windows",
    "win64": "Windows",
}


class WorkerSignals(QObject):
    """
    Defines the signals abailable from a running worker thread

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    """

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


# Worker Class
class Worker(QRunnable):
    """
    Work thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up

    :param callback: The function callback to run on this worker thread
    Supplied args and kwargs will be passed through to the runner.

    :type callback: Function
    :param args: Arguments to pass to the callback function    

    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        """
        Initialise the runner function with passed args, kwargs.
        """

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            # Return the result of the processing
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()  # Done


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

        # Start THREAD
        self.threadpool = QThreadPool()

        self.show()

        # self.battery()
        # self.cpu_ram()
        self.system_info()
        self.processes()
        self.storage()
        self.sensors()
        self.networks()
        self.psutil_thread()

    # ######################################################
    # CREATE PSUTIL THREAD FUNCTION
    # ######################################################

    def psutil_thread(self):
        # Live CPU Info
        cpu_worker = Worker(self.cpu_ram)

        # Start worker
        cpu_worker.signals.result.connect(self.print_output)
        cpu_worker.signals.finished.connect(self.thread_complete)
        cpu_worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(cpu_worker)

        # Live Battery Info
        battery_worker = Worker(self.battery)

        # Start worker
        battery_worker.signals.result.connect(self.print_output)
        battery_worker.signals.finished.connect(self.thread_complete)
        battery_worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(battery_worker)

        # # Live CPU Info
        # worker = Worker(self.cpu_ram)

        # # Start worker
        # worker.signals.result.connect(self.print_output)
        # worker.signals.finished.connect(self.thread_complete)
        # worker.signals.progress.connect(self.progress_fn)

        # # Execute
        # self.threadpool.start(worker)

    # ######################################################
    # WORKER PRINT OUT
    # ######################################################

    def print_output(self, s):
        print(s)

    # ######################################################
    # WORKER THREAD COMPLETE FUNCTION
    # ######################################################

    def thread_complete(self):
        print("THREAD COMPLETE!")

    # ######################################################
    # WORKER PRINT OUT
    # ######################################################

    def progress_fn(self, n):
        # n = progress value
        print("%dd%% done" % n)

    # ######################################################
    # NETWORKS FUNCTIONS
    # ######################################################

    def networks(self):
        # NET STATS
        for x in psutil.net_if_stats():
            z = psutil.net_if_stats()
            # Create new Row
            rowPosition = self.ui.net_stats_table.rowCount()
            self.ui.net_stats_table.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "net_stats_table")
            self.create_table_widget(
                rowPosition, 1, str(z[x].isup), "net_stats_table")
            self.create_table_widget(rowPosition, 2, str(
                z[x].duplex), "net_stats_table")
            self.create_table_widget(
                rowPosition, 3, str(z[x].speed), "net_stats_table")
            self.create_table_widget(
                rowPosition, 4, str(z[x].mtu), "net_stats_table")

        # NET IO COUNTERS
        for x in psutil.net_io_counters(pernic=True):
            z = psutil.net_io_counters(pernic=True)
            # Create new Row
            rowPosition = self.ui.net_io_table.rowCount()
            self.ui.net_io_table.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "net_io_table")
            self.create_table_widget(rowPosition, 1, str(
                z[x].bytes_sent), "net_io_table")
            self.create_table_widget(rowPosition, 2, str(
                z[x].bytes_recv), "net_io_table")
            self.create_table_widget(rowPosition, 3, str(
                z[x].packets_sent), "net_io_table")
            self.create_table_widget(rowPosition, 4, str(
                z[x].packets_recv), "net_io_table")
            self.create_table_widget(
                rowPosition, 5, str(z[x].errin), "net_io_table")
            self.create_table_widget(
                rowPosition, 6, str(z[x].errout), "net_io_table")
            self.create_table_widget(
                rowPosition, 7, str(z[x].dropin), "net_io_table")
            self.create_table_widget(
                rowPosition, 8, str(z[x].dropout), "net_io_table")

        # NET ADDRESS
        for x in psutil.net_if_addrs():
            z = psutil.net_if_addrs()
            # print(z)
            for y in z[x]:
                # Create new Row
                rowPosition = self.ui.net_address_table.rowCount()
                self.ui.net_address_table.insertRow(rowPosition)

                self.create_table_widget(
                    rowPosition, 0, str(x), "net_address_table")
                self.create_table_widget(
                    rowPosition, 1, str(y.family), "net_address_table")
                self.create_table_widget(rowPosition, 2, str(
                    y.address), "net_address_table")
                self.create_table_widget(rowPosition, 3, str(
                    y.netmask), "net_address_table")
                self.create_table_widget(rowPosition, 4, str(
                    y.broadcast), "net_address_table")
                self.create_table_widget(
                    rowPosition, 5, str(y.ptp), "net_address_table")

        # NET CONNECTIONS
        for x in psutil.net_connections():
            z = psutil.net_connections()
            # Create new Row
            rowPosition = self.ui.net_connections_table.rowCount()
            self.ui.net_connections_table.insertRow(rowPosition)

            self.create_table_widget(
                rowPosition, 0, str(x.fd), "net_connections_table")
            self.create_table_widget(rowPosition, 1, str(
                x.family), "net_connections_table")
            self.create_table_widget(rowPosition, 2, str(
                x.type), "net_connections_table")
            self.create_table_widget(rowPosition, 3, str(
                x.laddr), "net_connections_table")
            self.create_table_widget(rowPosition, 4, str(
                x.raddr), "net_connections_table")
            self.create_table_widget(rowPosition, 5, str(
                x.status), "net_connections_table")
            self.create_table_widget(rowPosition, 6, str(
                x.pid), "net_connections_table")

    # ######################################################
    # SENSORS INFORMATION
    # ######################################################

    def sensors(self):
        # PSUTIL Sensors currently works on linux platform
        if sys.platform == "linux" or sys.platform == "linux1" or sys.platform == "linux2":

            for x in psutil.sensors_temperature():
                for y in psutil.sensors_temperature()[x]:
                    # Create new row
                    rowPosition = self.ui.sensorTable.rowCount()
                    self.ui.sensorTable.insertRow(rowPosition)

                    self.create_table_widget(rowPosition, 0, x, "sensorTable")
                    self.create_table_widget(
                        rowPosition, 1, y.label, "sensorTable")
                    self.create_table_widget(
                        rowPosition, 2, str(y.current), "sensorTable")
                    self.create_table_widget(
                        rowPosition, 3, str(y.high), "sensorTable")
                    self.create_table_widget(
                        rowPosition, 4, str(y.critical), "sensorTable")

                    temp_per = (y.current / y.high) * 100

                    progressBar = QProgressBar(self.ui.sensorTable)
                    progressBar.setObjectName(u"progressBar")
                    progressBar.setValue(temp_per)
                    self.ui.sensorTable.setCellWidget(
                        rowPosition, 5, progressBar)

        else:
            global platforms
            # Create new Row
            rowPosition = self.ui.sensorTable.rowCount()
            self.ui.sensorTable.insertRow(rowPosition)

            self.create_table_widget(
                rowPosition, 0, "Function not supported on " + platforms[sys.platform], "sensorTable")
            self.create_table_widget(rowPosition, 1, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 2, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 3, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 4, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 5, "N/A", "sensorTable")

    # ######################################################
    # STORAGE PARTITIONS
    # ######################################################

    def storage(self):
        global platforms
        storage_device = psutil.disk_partitions(all=False)
        z = 0
        for x in storage_device:
            # print(x)
            # Create new Row
            rowPosition = self.ui.storageTable.rowCount()
            self.ui.storageTable.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x.device, "storageTable")
            self.create_table_widget(
                rowPosition, 1, x.mountpoint, "storageTable")
            self.create_table_widget(rowPosition, 2, x.fstype, "storageTable")
            self.create_table_widget(rowPosition, 3, x.opts, "storageTable")

            # check platform
            if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':
                self.create_table_widget(
                    rowPosition, 4, str(x.maxfile), "storageTable")
                self.create_table_widget(
                    rowPosition, 5, str(x.maxpath), "storageTable")
            else:
                self.create_table_widget(
                    rowPosition, 4, "Function not available on " + platforms[sys.platform], "storageTable")
                self.create_table_widget(
                    rowPosition, 5, "Function not available on " + platforms[sys.platform], "storageTable")

            # print(psutil.disk_usage(x.device))
            disk_usage = shutil.disk_usage(x.mountpoint)
            # print(disk_usage.total)
            disk_usage_total_formated = round(
                (disk_usage.total / (1024 * 1024 * 1024)), 4)
            disk_usage_free_formated = round(
                (disk_usage.free / (1024 * 1024 * 1024)), 4)
            disk_usage_used_formated = round(
                (disk_usage.used / (1024 * 1024 * 1024)), 4)

            self.create_table_widget(rowPosition, 6, str("{:.3f}".format(
                disk_usage_total_formated)) + " GB", "storageTable")
            self.create_table_widget(rowPosition, 7, str(
                "{:.3f}".format(disk_usage_free_formated)) + " GB", "storageTable")
            self.create_table_widget(rowPosition, 8, str(
                "{:.3f}".format(disk_usage_used_formated)) + " GB", "storageTable")
            # print(shutil.disk_usage(x.mountpoint))

            full_disk = (disk_usage.used / disk_usage.total) * 100
            progressBar = QProgressBar(self.ui.storageTable)
            progressBar.setObjectName(u"progressBar")
            progressBar.setValue(full_disk)
            self.ui.storageTable.setCellWidget(rowPosition, 9, progressBar)

    # ######################################################
    # A FUNCTION THAT CREATES TABLE WIDGETS
    # ######################################################

    def create_table_widget(self, rowPosition, columnPosition, text, tableName):
        qtablewidgetitem = QTableWidgetItem()

        # USER getattr() METHOD
        getattr(self.ui, tableName).setItem(
            rowPosition, columnPosition, qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui, tableName).item(
            rowPosition, columnPosition)

        qtablewidgetitem.setText(text)
    # ######################################################

    # ######################################################
    # GET RUNNING PROCESSES
    # ######################################################

    def processes(self):
        for x in psutil.pids():
            # Create new row
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)

            try:
                process = psutil.Process(x)
                # # Create widget
                # print(process)
                # rowPosition = row number
                # # x = column number

                self.create_table_widget(
                    rowPosition, 0, str(process.pid), "tableWidget")
                self.create_table_widget(
                    rowPosition, 1, process.name(), "tableWidget")
                self.create_table_widget(
                    rowPosition, 2, process.status(), "tableWidget")
                self.create_table_widget(rowPosition, 3, str(datetime.utcfromtimestamp(
                    process.create_time()).strftime("%Y-%m-%d %H:%M:%S")), "tableWidget")

                # create cell widget
                suspend_btn = QPushButton(self.ui.tableWidget)
                suspend_btn.setText("Suspend")
                suspend_btn.setStyleSheet("color: brown")
                self.ui.tableWidget.setCellWidget(rowPosition, 4, suspend_btn)

                # create cell widget
                resume_btn = QPushButton(self.ui.tableWidget)
                resume_btn.setText("Resume")
                resume_btn.setStyleSheet("color: green")
                self.ui.tableWidget.setCellWidget(rowPosition, 5, resume_btn)

                # create cell widget
                terminate_btn = QPushButton(self.ui.tableWidget)
                terminate_btn.setText("Terminate")
                terminate_btn.setStyleSheet("color: orange")
                self.ui.tableWidget.setCellWidget(
                    rowPosition, 6, terminate_btn)

                # create cell widget
                kill_btn = QPushButton(self.ui.tableWidget)
                kill_btn.setText("Kill")
                kill_btn.setStyleSheet("color: red")
                self.ui.tableWidget.setCellWidget(rowPosition, 7, kill_btn)

            except Exception as e:
                # Handle exceptions when a process ID is not found(x)
                print(e)

        # print(self.ui.tableWidget.findItems("sleeping", QtCore.Qt.MatchFlag.MatchRecursive|QtCore.Qt.MatchFlag.MatchExactly))
        self.ui.activity_search.textChanged.connect(self.findName)

    # ######################################################
    # SEARCH ACTIVITY TABLE
    # ######################################################
    def findName(self):
        name = self.ui.activity_search.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 1)
            # if the search is *not* in the item's text *do not hide* the row
            self.ui.tableWidget.setRowHidden(
                row, name not in item.text().lower())
    # ######################################################

    # ######################################################
    # GET SYSTEM INFORMATION
    # ######################################################
    def system_info(self):
        time = datetime.now().strftime("%I:%M:%S %p")
        date = datetime.now().strftime("%Y-%m-%d")
        self.ui.system_date.setText(str(date))
        self.ui.system_time.setText(str(time))

        self.ui.system_machine.setText(platform.machine())
        self.ui.system_version.setText(platform.version())
        self.ui.system_platform.setText(platform.platform())
        self.ui.system_system.setText(platform.system())
        self.ui.system_processor.setText(platform.processor())
    # ######################################################

    # ######################################################
    # System CPU and RAM Information
    # ######################################################
    def cpu_ram(self, progress_callback):
        while True:
            totalRam = 1.0
            totalRam = psutil.virtual_memory()[0] * totalRam
            totalRam = totalRam / (1024 * 1024 * 1024)
            self.ui.total_ram.setText(str("{:.2f}".format(totalRam) + " GB"))

            availRam = 1.0
            availRam = psutil.virtual_memory()[1] * availRam
            availRam = availRam / (1024 * 1024 * 1024)
            self.ui.available_ram.setText(
                str("{:.2f}".format(availRam) + " GB"))

            ramUsed = 1.0
            ramUsed = psutil.virtual_memory()[3] * ramUsed
            ramUsed = ramUsed / (1024 * 1024 * 1024)
            self.ui.used_ram.setText(str("{:.2f}".format(ramUsed) + " GB"))

            ramFree = 1.0
            ramFree = psutil.virtual_memory()[4] * ramFree
            ramFree = ramFree / (1024 * 1024 * 1024)
            self.ui.free_used.setText(str("{:.2f}".format(ramFree) + " GB"))

            ramUsages = str(psutil.virtual_memory()[2]) + "%"
            self.ui.ram_usage.setText(str("{:.2f}".format(totalRam) + " GB"))

            core = cpu_count()
            self.ui.cpu_count.setText(str(core))

            cpuPer = psutil.cpu_percent()
            self.ui.cpu_per.setText(str(cpuPer) + " %")

            cpuMainCore = psutil.cpu_count(logical=False)
            self.ui.cpu_main_core.setText(str(cpuMainCore))

            # CPU Percentage Indicator
            # SET Progress Bar Value
            self.ui.cpu_percentage.rpb_setMaximum(100)
            # SET Progress Values
            self.ui.cpu_percentage.rpb_setValue(cpuPer)
            # SET Progress Bar Style
            self.ui.cpu_percentage.rpb_setBarStyle("Hybrid2")
            # SET Progress Bar Line Color
            self.ui.cpu_percentage.rpb_setLineColor((255, 30, 99))
            # SET Progress Bar Line Color
            # self.ui.cpu_percentage.rpb_setCircleColor((45,74,83))
            # SET Progress bar line color
            self.ui.cpu_percentage.rpb_setPieColor((45, 74, 83))
            # CHanging the path color
            # self.ui.cpu_percentage.rpb_setPathColor((45, 74, 83))
            # SET Progress va text color
            self.ui.cpu_percentage.rpb_setTextColor((255, 255, 255))
            # SET Progress bar starting position
            # North, East, West, South
            self.ui.cpu_percentage.rpb_setInitialPos("West")
            # sET  Progress bar text type : Value or Percentage
            self.ui.cpu_percentage.rpb_setTextFormat('Percentage')
            # SET progress bar font
            self.ui.cpu_percentage.rpb_setTextFont("Arial")
            # set text hidden
            # self.ui.cpu_percentage.rpb_enableText(False)
            # set progress bar line width
            self.ui.cpu_percentage.rpb_setLineWidth(15)
            # path width
            self.ui.cpu_percentage.rpb_setPathWidth(15)
            # set progress bar line cap
            # RoundCap, SquareCap
            self.ui.cpu_percentage.rpb_setLineCap("RoundCap")
            # line style
            # DotLine, DashLine
            # self.ui.cpu_percentage.rpb_setLineStyle('SolidLine')

            # #################################################
            # RAM USAGE INDICATOR USING SPIRAL PROGRESS BAR
            # ######################################################
            # SETTING THE MINIMUM VALUE
            self.ui.ram_percentage.spb_setMinimum((0, 0, 0))
            # SETTING THE MAXIMUM VALUE
            self.ui.ram_percentage.spb_setMaximum(
                (totalRam, totalRam, totalRam))
            # set progress value
            self.ui.ram_percentage.spb_setValue((availRam, ramUsed, ramFree))
            # set progress color (R,G,B)
            self.ui.ram_percentage.spb_lineColor(
                ((6, 233, 38), (6, 201, 233), (233, 6, 201)))
            # setting the initial position of the progress bar: from outer -> inwards
            self.ui.ram_percentage.spb_setInitialPos(("West", "West", "West"))
            # setting the direction of progress of the progress bar: from outer-inwards
            # self.ui.percentage.spb_setDirection(
            #     ('Clockwise', 'Clockwise', 'Clockwise'))
            # set line width: 5px
            self.ui.ram_percentage.spb_lineWidth(15)
            # Set gap width
            self.ui.ram_percentage.spb_setGap(15)
            # set line style
            self.ui.ram_percentage.spb_lineStyle(
                ("SolidLine", "SolidLine", "SolidLine"))
            # Set line cap
            self.ui.ram_percentage.spb_lineCap(
                ("RoundCap", "RoundCap", "RoundCap"))
            # hide the path
            self.ui.ram_percentage.spb_setPathHidden(True)

            # sleep 1 second
            sleep(1)
        # ######################################################

    # ######################################################
    # A function to convert seconds to hours
    # ######################################################

    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)

    # Get system battery information

    def battery(self, progress_callback):
        while True:
            batt = psutil.sensors_battery()
            self.ui.battery_usage.show()

            if not hasattr(psutil, "sensors_battery"):
                self.ui.battery_status.setText("Platform not supported")

            if batt is None:
                self.ui.battery_status.setText("No battery installed")

            if hasattr(batt, "power_plugged"):
                if batt.power_plugged:
                    self.ui.battery_charge.setText(
                        str(round(batt.percent, 2))+"%")
                    self.ui.battery_time_left.setText("N/A")

                    if batt.percent < 100:
                        self.ui.battery_status.setText("Charging")
                    else:
                        self.ui.battery_status.setText("Fully Charged")

                    self.ui.battery_plugged.setText("Yes")

                else:
                    self.ui.battery_charge.setText(
                        str(round(batt.percent, 2))+"%")
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

            # sleep 1 second
            sleep(1)

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
