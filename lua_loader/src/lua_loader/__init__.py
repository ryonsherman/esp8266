#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"
__version__   = "1.0" # app version

import sys
import time
import serial

from PyQt4 import QtCore, QtGui

from lua_loader.window import MainWindow


class MainApplication(QtGui.QApplication):
    def __init__(self, *args, **kwargs):
        QtGui.QApplication.__init__(self, *args, **kwargs)

        class QSignals(QtCore.QObject):
            connected = QtCore.pyqtSignal(bool)
        self.signals = QSignals()

        self.baud = 9600
        self.port = '/dev/ttyUSB0'

        # initialize serial
        self.serial = serial.Serial()
        self.serial_timer = QtCore.QTimer()
        self.serial_timer.timeout.connect(self.serialRead)

        # initialize and show main window
        self.window = MainWindow(self)
        self.window.show()

    def serialConnect(self):
        self.serial = serial.Serial(self.port, self.baud, timeout=0.1)
        self.serial_timer.start(100)
        self.signals.connected.emit(True)

    def serialDisconnect(self):
        self.serial_timer.stop()
        self.serial.close()
        self.signals.connected.emit(False)

    def serialWrite(self, data):
        try:
            #self.serial.flushInput()
            self.serial.write(str(data) + '\r\n')
            time.sleep(0.3)
        except Exception, e:
            self.window.ui.statusbar.showMessage(str(e), 3000)

    def serialRead(self):
        # return if serial has no data
        if not self.serial.inWaiting(): return
        # initialize buffer
        buff = ""
        # read line from serial
        line = self.serial.readline()
        # append line to buffer until EOL
        while line:
            buff += line
            line = self.serial.readline()
        # append buffer to console output
        self.window.ui.console_tab.writeToConsole(buff)

def main():
    MainApplication(sys.argv).exec_()

if __name__ == '__main__':
    main()
