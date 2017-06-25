#_*_ conding: utf-8 _*_
"""
Stopwatch to use from the GUI
"""

import sys
from datetime import datetime
import time
from PyQt5.QtWidgets import (QWidget, QPushButton, QGridLayout, QVBoxLayout,
                             QLCDNumber, QApplication, QMainWindow, QTextEdit)
from PyQt5.QtCore import QTimer

class ButtonBoxWidget(QWidget):
    """
    Create button GUI
    """

    def __init__(self, parent=None):

        QWidget.__init__(self, parent=parent)
        # necessary to access time from function
        self.time1 = None

        self.initUi_1()


    def initUi_1(self):
        """
        Place buttons
        """

        self.start_button = QPushButton('Start', self)
        self.stop_button = QPushButton('Stop', self)
        self.reset_button = QPushButton('Reset', self)
        self.rap_button = QPushButton('Rap', self)
        self.csv_button = QPushButton('CSV', self)
        self.quit_button = QPushButton('Quit', self)

        layout = QGridLayout()
        layout.addWidget(self.start_button, 0, 0)
        layout.addWidget(self.stop_button, 0, 1)
        layout.addWidget(self.reset_button, 1, 0)
        layout.addWidget(self.rap_button, 1, 1)
        layout.addWidget(self.csv_button, 2, 0)
        layout.addWidget(self.quit_button, 2, 1)

        self.setLayout(layout)


class CountUpWidget(QWidget):
    """
    Timer and time hadling
    """

    def __init__(self, parent=None):

        QWidget.__init__(self, parent=parent)
        self.interval = 10

        self.time1 = None
        self.time2 = None
        self.log = None

        self.initUi_2()


    def initUi_2(self):
        """
        Place timer and EditText
        """

        self.timer = QTimer(self)
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.do_countup)

        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)

        self.editor = QTextEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(self.lcd, 3)
        layout.addWidget(self.editor, 2)
        self.setLayout(layout)

        self.reset_count()


    def update_display(self):
        """
        Update the timer display
        """

        self.lcd.display("%6.2f" % (self.count / 100))
        self.lcd.update()


    def do_countup(self):
        """
        Count the time
        """

        self.count += 1
        self.update_display()
        if self.count >= 10000000:
            self.stop_countup()


    def start_countup(self):
        """
        Start timer
        """

        self.timer.start()
        # changed because the decimal point number was not displayed
        self.time1 = time.time()

        return self.time1


    def stop_countup(self):
        """
        Stop timer
        """

        self.timer.stop()


    def reset_count(self):
        """
        Reset timer
        """

        self.count = 000000
        self.update_display()


    def rap_count(self):
        """
        Measure the lap and output the log
        """

        now = datetime.now()
        days = now.strftime("%Y/%m/%d")
        seconds = now.strftime("%H:%M:%S")
        if self.time1 != None:
        # changed because the decimal point number was not displayed
            self.time2 = time.time()
            # output up to 2 decimal places
            self.log = str(days) + ',' + str(seconds) + ',' \
                    + str("%.2f" % (self.time2 - self.time1))
            print(self.log)
            self.editor.append(self.log)
            self.time1 = time.time()

        return self.log


    def log_output(self):
        """
        Output the log to EditText
        """

        print(rap)

        w = self.editor.append(rap)
        print(w)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    panel = QWidget()

    countup_widget = CountUpWidget(parent=panel)
    button_box_widget = ButtonBoxWidget(parent=panel)

    panel_layout = QVBoxLayout()
    panel_layout.addWidget(countup_widget)
    panel_layout.addWidget(button_box_widget)
    panel.setLayout(panel_layout)
    panel.setFixedSize(400, 400)

    main_window = QMainWindow()
    main_window.setWindowTitle('StopWatch')
    main_window.setCentralWidget(panel)

    main_window.show()


    button_box_widget.start_button.clicked.connect(
        countup_widget.start_countup)

    button_box_widget.stop_button.clicked.connect(
        countup_widget.stop_countup)

    button_box_widget.reset_button.clicked.connect(
        countup_widget.reset_count)

    button_box_widget.rap_button.clicked.connect(
        countup_widget.rap_count)

    button_box_widget.quit_button.clicked.connect(
        app.quit)


    sys.exit(app.exec_())
