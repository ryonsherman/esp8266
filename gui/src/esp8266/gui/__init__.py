#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"
__version__   = "1.0" # app version

import os
import sys
import time
import tempfile
import subprocess

from PyQt4 import QtCore, QtGui

from esp8266.gui.log import log
from esp8266.gui.serial import Serial
from esp8266.gui.window import MainWindow
from esp8266.gui.settings import QSettings


class MainApplication(QtGui.QApplication):
    @property
    def log_file(self):
        # attempt to get stored value
        log_file = getattr(self, '_log_file', None)
        # initialize log file
        if log_file is None:
            # format log file name
            log_file = 'esp8266-gui_%s-log.txt' % time.strftime('%Y%m%d')
            # determine temp directory path
            log_file = os.path.join(tempfile.gettempdir(), log_file)
            # set log file value
            self._log_file = log_file
        # return value
        return log_file

    @property
    def settings(self):
        # attempt to get stored object
        settings = getattr(self, '_settings', None)
        # initialize settings
        if not settings:
            # determine settings path
            if sys.platform.startswith('win'):
                settings = 'HKEY_CURRENT_USER\\Software\\esp8266\\gui.ini'
            elif sys.platform.startswith('darwin'):
                settings = os.path.expanduser('~/.esp8266.gui.plist')
            else:
                settings = os.path.expanduser('~/.esp8266.gui.conf')
            # initialize settings object
            settings = QSettings(settings, QtCore.QSettings.NativeFormat)
            # store settings object
            self._settings = settings
        # return object
        return settings

    def __init__(self, *args, **kwargs):
        # initialize application
        QtGui.QApplication.__init__(self, *args, **kwargs)
        # set application version
        self.version = __version__

        # set log file output
        log.setFileLogHandler(self.log_file)
        # set application debug
        self.debug = self.settings.value('Debug').toBool()
        # set console log output if debugging
        if self.debug:
            log.setConsoleLogHandler()
            log.info(self.tr("Debug mode activated"))
        # set qt log output
        log.setQLogHandler()

        # log application start
        log.info(self.tr("Application starting..."))

        # initialize serial interface
        self.serial = Serial()
        # initialize main window
        self.window = MainWindow(self)
        # show main window
        self.window.show()

        # log application started
        log.info(self.tr("Application started"))

    def exit(self, retCode=0):
        # log return if possible
        if log.handlers:
            if not retCode:
                # log application shutdown
                log.info(self.tr("Application shutdown"))
            else:
                # log application exit
                log.warning(self.tr("Application exit with code %s!" % retCode))
        # exit with return code
        sys.exit(retCode)


def main():
    # execute application
    MainApplication(sys.argv).exec_()

if __name__ == '__main__':
    main()
