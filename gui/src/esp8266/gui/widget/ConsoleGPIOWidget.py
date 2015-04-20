#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

from esp8266.gui.ui.ConsoleGPIOWidget import Ui_ConsoleGPIOWidget

# define NodeMCU constants
MODE_OUTPUT = 0
MODE_INPUT = 1
MODE_INT = 2

PU_FLOAT = 0
PU_PULLUP = 1


class ConsoleGPIOWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # set app instance
        self.app = self.window().app

        # initialize user interface
        self.ui = Ui_ConsoleGPIOWidget()
        self.ui.setupUi(self)

        # connect to widget events
        self.ui.button_set.clicked.connect(self.onButtonSetClicked)
        self.ui.button_read.clicked.connect(self.onButtonReadClicked)
        self.ui.button_low.clicked.connect(self.onButtonLowClicked)
        self.ui.button_high.clicked.connect(self.onButtonHighClicked)

    def onButtonSetClicked(self):
        # get gpio pin selection
        pin = self.ui.gpio_select.currentIndex()
        # get gpio mode selection
        mode = self.ui.mode_select.currentIndex()
        # determine gpio mode
        if mode == MODE_OUTPUT:
            mode = "gpio.OUTPUT"
        elif mode == MODE_INPUT:
            mode = "gpio.INPUT"
        elif mode == MODE_INT:
            mode = "gpio.INT"
        # get gpio pullup mode selection
        pu_mode = self.ui.pu_mode_select.currentIndex()
        # determine gpio pullup mode
        if pu_mode == PU_PULLUP:
            pu_mode = "gpio.PULLUP"
        elif pu_mode == PU_FLOAT:
            pu_mode = "gpio.FLOAT"
        # write command to serial
        self.app.serial.write("gpio.mode(%s, %s, %s)" % (pin, mode, pu_mode))

    def onButtonReadClicked(self):
        # get gpio pin selection
        pin = self.ui.gpio_select.currentIndex()
        # write command to serial
        self.app.serial.write("print(gpio.read(%s))" % pin)

    def onButtonLowClicked(self):
        # get gpio pin selection
        pin = self.ui.gpio_select.currentIndex()
        # write command to serial
        self.app.serial.write("gpio.write(%s, gpio.LOW)" % pin)

    def onButtonHighClicked(self):
        # get gpio pin selection
        pin = self.ui.gpio_select.currentIndex()
        # write command to serial
        self.app.serial.write("gpio.write(%s, gpio.HIGH)" % pin)
