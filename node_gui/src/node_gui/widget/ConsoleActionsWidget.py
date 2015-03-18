#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

from node_gui.ui.widget.ConsoleActionsWidget import Ui_ConsoleActionsWidget


class ConsoleActionsWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_ConsoleActionsWidget()
        self.ui.setupUi(self)

        # connect action buttons
        serial = self.window().app.serial
        self.ui.button_restart.clicked.connect(
            lambda: serial.write("print(node.restart())"))
        self.ui.button_info.clicked.connect(
            lambda: serial.write("print(node.info())"))
        self.ui.button_heap.clicked.connect(
            lambda: serial.write("print(node.heap())"))
        # connect to serial connected signal
        serial.signals.connected.connect(self.onConnected)

    def onConnected(self, connected):
        # set '(dis)connect' button text
        self.ui.button_connect.setText(
            self.tr("Disconnect" if connected else "Connect"))
