#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import sys
import logging

from PyQt4 import QtCore
from StringIO import StringIO

# define log format
LOG_FORMAT = "[%(asctime)s] (%(levelname)s) %(message)s"

# get root logger
log = logging.getLogger()
# set default logging level
log.setLevel(logging.DEBUG)

# intitialize log formatter
formatter = logging.Formatter(LOG_FORMAT)

# define qt log buffer object
class QLogBuffer(QtCore.QObject, StringIO):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        QtCore.QObject.__init__(self)
        StringIO.__init__(self, *args, **kwargs)

    def write(self, data):
        if not data: return
        self.signal.emit(unicode(data))
        StringIO.write(self, data)
log.buffer = QLogBuffer()

# log handler helper
def setLogHandler(handler):
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    log.addHandler(handler)
log.setLogHandler = setLogHandler

# console log handler helper
def setConsoleLogHandler():
    setLogHandler(logging.StreamHandler())
log.setConsoleLogHandler = setConsoleLogHandler

# file log handler helper
def setFileLogHandler(logfile):
    setLogHandler(logging.FileHandler(logfile))
log.setFileLogHandler = setFileLogHandler

# qt log handler helper
def setQLogHandler():
    setLogHandler(logging.StreamHandler(log.buffer))
log.setQLogHandler = setQLogHandler
