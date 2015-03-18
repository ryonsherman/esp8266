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

from node_gui import util
from node_gui.log import log
from node_gui.window import MainWindow
from node_gui.settings import QSettings

EXIT_CODE_SUCCESS = 0
EXIT_CODE_FAILURE = 1
EXIT_CODE_UNSUPPORTED_PLATFORM = 128


class Serial(object):
    def __init__(self, *args, **kwargs):
        # define signals
        class QSignals(QtCore.QObject):
            connected = QtCore.pyqtSignal(bool)
        # initialize signals
        self.signals = QSignals()

    def write(self, data):
        print 'TODO: serial write: %s' % data


class MainApplication(QtGui.QApplication):
    def __init__(self, *args, **kwargs):
        # initialize application
        QtGui.QApplication.__init__(self, *args, **kwargs)
        # set application version
        self.version = __version__

        # handle unsupported platforms
        if not util.platformSupported():
            util.dialog.critical(self, self.tr("Unsupported platform!"))
            self.exit(EXIT_CODE_UNSUPPORTED_PLATFORM)

        # set application debug
        self.debug = self.settings.value('Debug').toBool()
        # set console log output if debugging
        if self.debug:
            log.setConsoleLogHandler()
            log.info(self.tr("Debug mode activated"))
        # set log file output
        log.setFileLogHandler(self.log_file)
        # set qt log output
        log.setQLogHandler()

        # connect last window close event to app exit
        self.lastWindowClosed.connect(self.exit)

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

    @property
    def log_file(self):
        # attempt to get stored object
        log_file = getattr(self, '_log_file', None)
        # initialize log file
        if log_file is None:
            # format log file name
            log_file = 'NodeGUI_%s-log.txt' % time.strftime('%Y%m%d')
            # determine temp directory path
            log_file = os.path.join(tempfile.gettempdir(), log_file)
            # set log file object
            self._log_file = log_file
        # return object
        return log_file

    @property
    def settings(self):
        # attempt to get stored object
        settings = getattr(self, '_settings', None)
        # initialize settings
        if not settings:
            # determine settings path
            if sys.platform.startswith('win'):
                settings = 'HKEY_CURRENT_USER\\Software\\NodeGUI\\NodeGUI.ini'
            elif sys.platform.startswith('darwin'):
                settings = os.path.expanduser('~/.NodeGUI.plist')
            else:
                settings = os.path.expanduser('~/.NodeGUI.conf')
            # initialize settings object
            settings = QSettings(settings, QtCore.QSettings.NativeFormat)
            # store settings object
            self._settings = settings
        # return object
        return settings

    def openLocalFile(self, path):
        # normalize path
        path = str(path)
        # call external process
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', path))
        elif os.name == 'nt':
            os.startfile(path)
        elif os.name == 'posix':
            subprocess.call(('xdg-open', path))

    def editLocalFile(self, path):
        print "MainApplication::editLocalFile(%s)" % path

    def deleteLocalFile(self, path):
        # normalize path
        path = str(path)
        print "MainApplication::deleteLocalFile(%s)" % path

    def openRemoteFile(self, path):
        print "MainApplication::openRemoteFile(%s)" % path

    def editRemoteFile(self, path):
        print "MainApplication::editRemoteFile(%s)" % path

    def deleteRemoteFile(self, path):
        print "MainApplication::deleteRemoteFile(%s)" % path

    def exit(self, retCode=0):
        # exit with return code if no log handlers
        if not log.handlers: sys.exit(retCode)

        # if cleanly shutdown
        if retCode == EXIT_CODE_SUCCESS:
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
