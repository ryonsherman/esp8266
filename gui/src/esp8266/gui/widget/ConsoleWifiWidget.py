#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

from esp8266.gui import util
from esp8266.gui.ui.ConsoleWifiWidget import Ui_ConsoleWifiWidget

# define NodeMCU constants
MODE_STATION = 0
MODE_SOFTAP = 1
MODE_STATIONAP = 2


class ConsoleWifiWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # set app instance
        self.app = self.window().app

        # initialize user interface
        self.ui = Ui_ConsoleWifiWidget()
        self.ui.setupUi(self)
        self.ui.ap_input.hide()

        # connect to widget events
        self.ui.mode_select.currentIndexChanged.connect(self.onSelectModeChanged)
        self.ui.button_set_ap.clicked.connect(self.onButtonSetAPClicked)
        self.ui.button_connect.clicked.connect(self.onConnectClicked)
        self.ui.button_survey.clicked.connect(self.onButtonSurveyClicked)
        self.ui.button_get_ip.clicked.connect(self.onButtonGetIPClicked)

    def onSelectModeChanged(self, mode):
        # toggle display of additional input
        if mode == MODE_STATIONAP:
            self.ui.ap_input.show()
        else:
            self.ui.ap_input.hide()

    def onButtonSetAPClicked(self):        
        # get essid from input
        essid = self.ui.essid_input.text()
        # require essid
        if not essid: return # TODO: error message
        # get password from input
        password = self.ui.password_input.text()
        
        # get mode selection
        mode = self.ui.mode_select.currentIndex()
        # set station mode
        if mode == MODE_STATION:
            # write command to serial
            self.app.serial.write("""
                wifi.setmode(wifi.STATION)
                wifi.sta.config(\"%s\",\"%s\")
            """ % (essid, password))
        # set ap mode
        elif mode == MODE_SOFTAP:
            # write command to serial
            self.app.serial.write("""
                wifi.setmode(wifi.SOFTAP)
                wifi.ap.config({ssid="%s", pwd="%s"})
            """ % (essid, password, ap_essid, ap_password))
        # set station/ap mode
        elif mode == MODE_STATIONAP:
            # get ap essid from input
            ap_essid = self.ui.ap_essid_input.text()
            # require ap essid
            if not ap_essid: return # TODO: error message
            # get ap password from input
            ap_password = self.ui.ap_password_input.text()
            # write command to serial
            self.app.serial.write("""
                wifi.setmode(wifi.STATIONAP)
                wifi.sta.config(\"%s\",\"%s\")
                wifi.ap.config({ssid="%s", pwd="%s"})
            """ % (essid, password, ap_essid, ap_password))

    def onConnectClicked(self):
        # write command to serial
        self.app.serial.write("wifi.sta.connect()")

    def onButtonSurveyClicked(self):
        # write command to serial
        self.app.serial.write("""
            function listap(t)
              for ssid,v in pairs(t) do
                authmode, rssi, bssid, channel = string.match(v, 
                    "(%d),(-?%d+),(%x%x:%x%x:%x%x:%x%x:%x%x:%x%x),(%d+)")
                print(ssid,authmode,rssi,bssid,channel)
              end
            end
            wifi.sta.getap(listap)
        """)

    def onButtonGetIPClicked(self):
        # get mode from selection
        mode = self.ui.mode_select.currentIndex()
        # write command to serial
        if mode in (MODE_STATION, MODE_STATIONAP):
            self.app.serial.write("print(wifi.sta.getip())")
        if mode in (MODE_SOFTAP, MODE_STATIONAP):
            self.app.serial.write("print(wifi.ap.getip())")
