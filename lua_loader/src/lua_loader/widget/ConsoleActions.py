#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

from lua_loader.ui.ConsoleActionsWidget import Ui_ConsoleActionsWidget


class ConsoleActionsWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_ConsoleActionsWidget()
        self.ui.setupUi(self)

        # connect 'connect' button
        self.ui.button_connect.clicked.connect(self.onConnectClicked)
        # connect 'restart' button
        self.ui.button_restart.clicked.connect(self.onRestartClicked)
        # connect 'info' button
        self.ui.button_info.clicked.connect(self.onInfoClicked)
        # connect 'heap' button
        self.ui.button_heap.clicked.connect(self.onHeapClicked)

        # connect to app connected signal
        self.parent().window().app.serial.signals.connected.connect(self.onConnect)

    def onConnect(self, connected):
        # set 'connect' button text
        self.ui.button_connect.setText('Disconnect' if connected else 'Connect')

    def onConnectClicked(self):
        # perform app serial connect
        getattr(self.window().app, str('serial' + self.ui.button_connect.text()))()

    def onRestartClicked(self):
        # write restart command to serial
        self.window().app.serialWrite("node.restart()")

    def onInfoClicked(self):
        # write info command to serial
        self.window().app.serialWrite("print(node.chipid())")

    def onHeapClicked(self):
        # write heap command to serial
        self.window().app.serialWrite("print(node.heap())")
