#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

from lua_loader.ui.ConsoleGPIOActionsWidget import Ui_ConsoleGPIOActionsWidget


class ConsoleGPIOActionsWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_ConsoleGPIOActionsWidget()
        self.ui.setupUi(self)
