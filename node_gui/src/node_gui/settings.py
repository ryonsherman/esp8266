#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtCore

from collections import OrderedDict

DEFAULTS = OrderedDict({
    'Interface/ConsoleBGColor': '#48483E',
    'Interface/ConsoleFGColor': '#CFD0C2',
})


class QSettings(QtCore.QSettings):
    def __init__(self, *args, **kwargs):
        # initialize settings
        QtCore.QSettings.__init__(self, *args, **kwargs)

    def getValue(self, key):
        # return value or default
        return self.value(key, QtCore.QVariant(DEFAULTS.get(key, None)))
