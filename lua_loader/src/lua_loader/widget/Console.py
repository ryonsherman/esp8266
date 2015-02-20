#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

from lua_loader.ui.ConsoleWidget import Ui_ConsoleWidget
from lua_loader.widget.ConsoleActions import ConsoleActionsWidget
from lua_loader.widget.ConsoleGPIOActions import ConsoleGPIOActionsWidget
from lua_loader.widget.ConsoleWifiActions import ConsoleWifiActionsWidget


class ConsoleWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_ConsoleWidget()
        self.ui.setupUi(self)

        # add tab to window tab view
        self.window().ui.tab_view.addTab(self, 'Console')

        # initialize console actions widget
        self.ui.console_actions = ConsoleActionsWidget(self)
        self.ui.action_view.layout().insertWidget(0, self.ui.console_actions)
        # initialize gpio actions widget
        self.ui.gpio_actions = ConsoleGPIOActionsWidget(self)
        self.ui.action_view.layout().insertWidget(1, self.ui.gpio_actions)
        # initialize wireless actions widget
        self.ui.wireless_actions = ConsoleWifiActionsWidget(self)
        self.ui.action_view.layout().insertWidget(2, self.ui.wireless_actions)

        # connect input return to 'send' button click
        self.ui.input.returnPressed.connect(self.ui.button_send.animateClick)

        # connect 'send' button to console output
        self.ui.button_send.clicked.connect(self.input)
        # connect 'clear' button to clear console output
        self.ui.button_clear.clicked.connect(self.ui.output.clear)

        # connect serial text change to console output
        self.window().app.serial.signals.publicTextChanged.connect(self.output)

        # override output keypress event
        self.ui.output.keyPressEvent = self.onKeyPressed

    def input(self):
        # write console input to serial
        self.window().app.serialWrite(self.ui.input.text())
        # select current input to allow for overwrite
        self.ui.input.selectAll()

    def output(self, data):
        # get output widget
        output = self.ui.output
        # append text to console output
        output.appendPlainText(data)
        # return if setting disabled
        if not self.window().app.settings.value('Interface/ScrollOnOutput').toBool(): return
        # get console cursor
        cursor = output.textCursor()
        # move cursor to end position
        cursor.movePosition(QtGui.QTextCursor.End)
        # set console cursor
        output.setTextCursor(cursor)
        # ensure console cursor is visible
        output.ensureCursorVisible()

    def showActionView(self):
        # show action view
        self.ui.action_view.show()
        # set tab view index to console tab since it contans the action view
        self.window().ui.tab_view.setCurrentIndex(0)

    def hideActionView(self):
        # hide action view
        self.ui.action_view.hide()

    def toggleActionView(self, display):
        # show or hide action view
        self.showActionView() if display else self.hideActionView()

    def onKeyPressed(self, event):
        # send event to output if modified
        if event.modifiers():
            return QtGui.QPlainTextEdit.keyPressEvent(self.ui.output, event)
        # set focus to input and select all for overwrite
        self.ui.input.setFocus(True)
        self.ui.input.selectAll()
        # send event to input
        self.ui.input.keyPressEvent(event)
