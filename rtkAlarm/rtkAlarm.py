#!/usr/bin/pytho
# -*- coding: utf-8 -*-

import sys
#from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import re
import time
import os

DEFAULT_NMEA_FILE = ""
DEFAULT_SOUND_FILE = ".\\knocking_an_iron_door1.mp3"

TIMER_WAIT = 100

GGA_PATTERN = r"""
    ^\$GPGGA,         # GGA id
    ([\d\.]*),        # GPS time(1)
    ([\d\.]*),        # Latitude(2)
    ([NS]?),          # North or South(3)
    ([\d\.]*),        # Longitude(4)
    ([EW]?),          # East or West(5)
    (\d?),            # GNSS Quality(Mode)(6)
    (\d*),            # the number of Sat(7)
    ([-\d\.]*),       # HDOP(8)
    ([-\d\.]*),M,     # Altitude(9)
    ([-\d\.]*),M,     # Height of geoid(10)
    ([\d\.]*),        # Data Age(11)
    (\d*)             # Base Station ID(12)
    \*([\da-zA-Z]{2}) # checksum(13)
"""

GPS_MODE = ["invalid", "stand alone", "DGPS", "None", "RTK-Fixed", "RTK-Float"]

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("RTKアラーム")
        self.resize(480, 64)

        self.initGuiItems()
        self.initTimer()

        self.pos = 0
        self.gpsMode = 0
        self.isStart = False
        self.firstCheck = True

    def initGuiItems(self):
        self.textBoxNmeaPath = QtWidgets.QLineEdit(DEFAULT_NMEA_FILE)
        self.textBoxSoundPath = QtWidgets.QLineEdit(DEFAULT_SOUND_FILE)
        self.buttonNmeaSelect = QtWidgets.QPushButton("NMEA")
        self.buttonSoundSelect = QtWidgets.QPushButton("Sound")
        self.buttonStart = QtWidgets.QPushButton("Start")
        self.gpsLabel = QtWidgets.QLabel("None")

        self.textBoxNmeaPath.setReadOnly(True)
        self.textBoxSoundPath.setReadOnly(True)
        self.buttonStart.setCheckable(True)

        self.buttonNmeaSelect.clicked.connect(self.selectNmeaFile)
        self.buttonSoundSelect.clicked.connect(self.selectSoundFile)
        self.buttonStart.clicked.connect(self.startWatchNmea)

        self.guiLayout = QtWidgets.QGridLayout()
        self.guiLayout.addWidget(self.textBoxNmeaPath, 0, 0)
        self.guiLayout.addWidget(self.textBoxSoundPath, 1 ,0)
        self.guiLayout.addWidget(self.buttonNmeaSelect, 0, 1)
        self.guiLayout.addWidget(self.buttonSoundSelect, 1, 1)
        self.guiLayout.addWidget(self.buttonStart, 2, 0)
        self.guiLayout.addWidget(self.gpsLabel, 2, 1)

        self.setLayout(self.guiLayout)

    def initTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(TIMER_WAIT)
        self.timer.timeout.connect(self.timeout)

    def selectNmeaFile(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "NMEA File")
        self.textBoxNmeaPath.setText(filename)

    def selectSoundFile(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Sound File")
        self.textBoxSoundPath.setText(filename)

    def startWatchNmea(self):
        if self.buttonStart.isChecked():
            self.buttonNmeaSelect.setEnabled(False)
            self.buttonSoundSelect.setEnabled(False)

            self.gpsMode = 0
            self.pos = 0
            nmeaFile = self.textBoxNmeaPath.text()
            self.pos = self.check_file(nmeaFile, self.pos, self.firstCheck)
            self.firstCheck = False
            self.timer.start()
            self.isStart = True
        else:
            self.timer.stop()
            self.isStart = False
            self.buttonNmeaSelect.setEnabled(True)
            self.buttonSoundSelect.setEnabled(True)


    def timeout(self):
        self.timer.stop()
        nmeaFile = self.textBoxNmeaPath.text()
        self.pos = self.check_file(nmeaFile, self.pos, self.firstCheck)
        if self.isStart:
            self.timer.start()

    def check_file(self, filename, pos, firstCheck):
        ggaPattern = re.compile(GGA_PATTERN, re.VERBOSE)
        with open(filename) as f:
            end_pos = f.seek(0, 2) # ファイル末尾へシーク
            f.seek(pos)
            while True:
                try:
                    line = f.readline()
                    pos = f.tell()
                    #print(str(pos) + "/" + str(end_pos))
                    if (line == "") or (pos == end_pos):
                        break
                    m = ggaPattern.search(line)
                    if m:
                        if m.group(6) != self.gpsMode:
                            print("mode change:" + m.group(6))
                            self.gpsMode = m.group(6)
                            self.updateGpsLabel()
                            if(not firstCheck):
                                self.playAlarm()
                except UnicodeDecodeError:
                    pass
                except UnicodeEncodeError:
                    pass

            return pos

    def playAlarm(self):
        soundFile = self.textBoxSoundPath.text()
        os.system("start " + soundFile)

    def updateGpsLabel(self):
        self.gpsLabel.setText(GPS_MODE[int(self.gpsMode)])

def main():

    app = QtWidgets.QApplication(sys.argv)
    mWindow = MainWindow()

    mWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
