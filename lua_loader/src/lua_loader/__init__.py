#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"
__version__   = "1.0" # app version

import re
import os
import sys
import time
import json
import serial

from PyQt4 import QtCore, QtGui

from lua_loader.window import MainWindow


class Serial(object):
    def __init__(self, *args, **kwargs):
        # initialize serial
        self.baud = 9600
        self.port = '/dev/ttyUSB0'
        self.serial = serial.Serial()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read)

    @property
    def signals(self):
        # attempt to get stored object
        signals = getattr(self, '_signals', None)
        # initialize signals
        if not signals:
            # define signals object
            class QSignals(QtCore.QObject):
                connected = QtCore.pyqtSignal(bool)
                privateTextChanged = QtCore.pyqtSignal(object)
                publicTextChanged = QtCore.pyqtSignal(str)
            # initialize signals object
            signals = QSignals()
            # store object
            self._signals = signals
        # return object
        return signals

    def connect(self):
        # initialize serial
        self.serial = serial.Serial(self.port, self.baud, timeout=0.1)
        # start read timer
        self.timer.start(100)
        # emit connected signal
        self.signals.connected.emit(True)

    def disconnect(self):
        # stop read timer
        self.timer.stop()
        # close serial
        self.serial.close()
        # emit disconnected signal
        self.signals.connected.emit(False)

    def write(self, data):
        # write data to serial
        self.serial.write(str(data).strip() + '\r\n')
        # time delay
        time.sleep(0.3)

    def read(self):
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

        # find all data tags in buffer
        for match in re.findall('<!--(.*?)-->', buff, re.DOTALL):
            # strip data tags
            data = match.lstrip('<!--').rstrip('-->')
            try:
                # attemp to parse data
                data = json.loads(data)
                # emit signal with data
                self.signals.privateTextChanged.emit(data)
                # return instead of buffer output
                return
            except: pass

        # emit signal with buffer
        self.signals.publicTextChanged.emit(buff)


class MainApplication(QtGui.QApplication):
    def __init__(self, *args, **kwargs):
        # initialize application
        QtGui.QApplication.__init__(self, *args, **kwargs)
        # set application version
        self.version = __version__
        # initialize debugging
        self.debug = self.settings.value('Debug').toBool()

        # TODO: handle unsupported platform

        # initialize serial
        self.serial = Serial()

        # initialize and show main window
        self.window = MainWindow(self)
        self.window.show()

    @property
    def settings(self):
        # attempt to get stored object
        settings = getattr(self, '_settings', None)
        # initialize settings
        if not settings:
            # determine settings path
            if sys.platform.startswith('win'):
                settings = 'HKEY_CURRENT_USER\\Software\\LuaLoader\\LuaLoader.ini'
            else:
                settings = os.path.expanduser('~/.LuaLoader.conf')
            # initialize settings object
            settings = QtCore.QSettings(settings, QtCore.QSettings.NativeFormat)
            # set defaults
            def set_default(key, value):
                if settings.contains(key): return
                settings.setValue(key, value)
            for key, value in {
                'Debug': False,
                'Interface/ScrollOnOutput': True
            }.iteritems(): set_default(key, value)
            # store object
            self._settings = settings
        # return object
        return settings

    def serialConnect(self):
        # attempt serial connection
        try:
            self.serial.connect()
        except Exception, e:
            self.window.ui.statusbar.showMessage(str(e), 3000)

    def serialDisconnect(self):
        # disconnect serial
        self.serial.disconnect()

    def serialWrite(self, data):
        # attempt serial write
        try:
            self.serial.write(data)
        except Exception, e:
            self.window.ui.statusbar.showMessage(str(e), 3000)


def main():
    MainApplication(sys.argv).exec_()

if __name__ == '__main__':
    main()
