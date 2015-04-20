#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtCore


class Serial(object):
    # # define signals
    # class QSignals(QtCore.QObject):
    #     connected = QtCore.pyqtSignal(bool)

    # def __init__(self, *args, **kwargs):
    #     # initialize signals
    #     self.signals = self.QSignals()

    def write(self, data):
        print "Serial::write(%s)" % data # TODO
        