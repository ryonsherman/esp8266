#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import os
import shutil

from PyQt4 import QtCore, QtGui

from esp8266.gui.widget.ConsoleActionsWidget import ConsoleActionsWidget
from esp8266.gui.widget.ConsoleGPIOWidget import ConsoleGPIOWidget
from esp8266.gui.widget.ConsoleWifiWidget import ConsoleWifiWidget

from esp8266.gui.ui.ConsoleWidget import Ui_ConsoleWidget
from esp8266.gui.ui.ConsolePanelWidget import Ui_ConsolePanelWidget


class ConsolePanelWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_ConsolePanelWidget()
        self.ui.setupUi(self)

        # initialize and insert console actions widget
        self.ui.console_actions = ConsoleActionsWidget(self)
        self.layout().insertWidget(0, self.ui.console_actions)

        # initialize and insert gpio widget
        self.ui.gpio_actions = ConsoleGPIOWidget(self)
        self.layout().insertWidget(1, self.ui.gpio_actions)

        # initialize and insert wifi widget
        self.ui.wifi_actions = ConsoleWifiWidget(self)
        self.layout().insertWidget(2, self.ui.wifi_actions)

    def show(self):
        # show widget
        QtGui.QWidget.show(self)
        # get window
        window = self.window()
        # set tab view index to console tab since it contans the panel
        window.ui.tabs.setCurrentIndex(0)
        # check 'View -> Actions' menu option
        window.ui.menu_view_actions.setChecked(True)

    def hide(self):
        # show widget
        QtGui.QWidget.hide(self)
        # check 'View -> Actions' menu option
        self.window().ui.menu_view_actions.setChecked(False)

    def toggle(self, display):
        # show or hide panel
        self.show() if display else self.hide()


class ConsoleWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize input buffer
        self.buffer = []
        self.buffer_pos = 0

        # initialize user interface
        self.ui = Ui_ConsoleWidget()
        self.ui.setupUi(self)

        # initialize panel widget
        self.ui.panel = ConsolePanelWidget(self)
        self.ui.view.addWidget(self.ui.panel)

        # initialize output widget
        self.ui.output.keyPressEvent = self.onOutputKeyPressed

        # initialize input widget
        self.ui.input.keyPressEvent = self.onInputKeyPressed
        self.ui.input.returnPressed.connect(self.ui.button_send.animateClick)

        # connect to send input button click
        self.ui.button_send.clicked.connect(self.onSendButtonClicked)
        # connect to clear output button click
        self.ui.button_clear.clicked.connect(self.ui.output.clear)

        # connect pref dialog accept to dialog show
        self.window().ui.prefs.accepted.connect(self.onConsoleColorChanged)

        # set console colors
        self.onConsoleColorChanged()

    def onConsoleColorChanged(self):
        # retrieve console colors from settings
        settings = self.window().app.settings
        self.bg_color = settings.getValue('Interface/ConsoleBGColor').toString()
        self.fg_color = settings.getValue('Interface/ConsoleFGColor').toString()

        # set console style
        style = 'color: %s; background-color: %s' % (self.fg_color, self.bg_color)
        self.ui.output.setStyleSheet(style)

    def onOutputKeyPressed(self, event):
        # send event to output if modified (cut/copy)
        if event.modifiers():
            return QtGui.QPlainTextEdit.keyPressEvent(self.ui.output, event)
        # set focus to input and select all for overwrite
        self.ui.input.setFocus(True)
        self.ui.input.selectAll()
        # send event to input
        self.ui.input.keyPressEvent(event)

    def onInputKeyPressed(self, event):
        # increase buffer position
        if event.key() == QtCore.Qt.Key_Up:
            self.buffer_pos -= 2 if self.buffer_pos == len(self.buffer) else 1
            if self.buffer_pos < 0:
                self.buffer_pos = 0
        # decrease buffer position
        elif event.key() == QtCore.Qt.Key_Down:
            self.buffer_pos += 1
            if self.buffer_pos > len(self.buffer):
                self.buffer_pos = len(self.buffer)
        else:
            # perform default keypress event
            return QtGui.QLineEdit.keyPressEvent(self.ui.input, event)
        try:
            # attempt to set input text to buffer position
            self.ui.input.setText(self.buffer[self.buffer_pos])
        except Exception, e:
            pass

    def onSendButtonClicked(self):
        # get data from input
        data = str(self.ui.input.text())
        # write data to serial
        self.window().app.serial.write(data)

        if not self.buffer or data != self.buffer[-1]:
            # only keep last 500 items
            if len(self.buffer) > 500:
                self.buffer.pop(0)
            # append current text to input buffer
            self.buffer.append(data)
        # reset buffer position
        self.buffer_pos = len(self.buffer)

        # select current input to allow for overwrite
        self.ui.input.selectAll()
