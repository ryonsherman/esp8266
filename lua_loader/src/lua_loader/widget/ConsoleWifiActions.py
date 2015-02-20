#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

from lua_loader.ui.ConsoleWifiActionsWidget import Ui_ConsoleWifiActionsWidget


class ConsoleWifiActionsWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_ConsoleWifiActionsWidget()
        self.ui.setupUi(self)

        # connect 'survey' button
        self.ui.button_survey.clicked.connect(self.onSurveyClicked)
        # connect 'get ip' button
        self.ui.button_get_ip.clicked.connect(self.onGetIPClicked)

    def onSurveyClicked(self):
        # write wireless survey command to serial
        self.window().app.serialWrite(
            """wifi.sta.getap(function(t) for k,v in pairs(t) do print(k.." "..v) end end)""" \
            """print("Please wait...")""")

    def onGetIPClicked(self):
        # write get wireless ip command to serial
        self.window().app.serialWrite("print(wifi.ap.getip())")
