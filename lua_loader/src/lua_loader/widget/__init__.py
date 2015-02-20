#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import os
import time

from PyQt4 import QtCore, QtGui

from lua_loader.util import overrideEvent, QSyntaxHighlighter

from lua_loader.ui.LogWidget import Ui_LogWidget
from lua_loader.ui.FileWidget import Ui_FileWidget
from lua_loader.ui.ConsoleWidget import Ui_ConsoleWidget
from lua_loader.ui.FileTreeWidget import Ui_FileTreeWidget

from lua_loader.ui.ConsoleActionsWidget import Ui_ConsoleActionsWidget
from lua_loader.ui.ConsoleGPIOActionsWidget import Ui_ConsoleGPIOActionsWidget
from lua_loader.ui.ConsoleWirelessActionsWidget import Ui_ConsoleWirelessActionsWidget


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
        self.parent().window().app.signals.connected.connect(self.onConnect)

    def onConnect(self, connected):
        self.ui.button_connect.setText('Disconnect' if connected else 'Connect')

    def onConnectClicked(self):
        # move this
        window = self.window()
        if self.ui.button_connect.text() == 'Connect':
            window.ui.console_tab.writeToConsole("Connecting to %s at %s baud..." %
                (window.app.port, window.app.baud))
            window.app.serialConnect()
        else:
            window.app.serialDisconnect()

    def onRestartClicked(self):
        # write restart command to serial
        self.window().app.serialWrite("node.restart()")

    def onInfoClicked(self):
        # write info command to serial
        self.window().app.serialWrite("print(node.chipid())")

    def onHeapClicked(self):
        # write heap command to serial
        self.window().app.serialWrite("print(node.heap())")






class ConsoleGPIOActionsWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_ConsoleGPIOActionsWidget()
        self.ui.setupUi(self)







class ConsoleWirelessActionsWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_ConsoleWirelessActionsWidget()
        self.ui.setupUi(self)

        # connect 'survey' button
        self.ui.button_survey.clicked.connect(self.onSurveyClicked)
        # connect 'get ip' button
        self.ui.button_get_ip.clicked.connect(self.onGetIPClicked)

    def onSurveyClicked(self):
        # write wireless survey command to serial
        self.window().app.serialWrite("""wifi.sta.getap(function(t) for k,v in pairs(t) do print(k.." "..v) end end) print("Please wait...")""")

    def onGetIPClicked(self):
        # write get wireless ip command to serial
        self.window().app.serialWrite("print(wifi.ap.getip())")








class ConsoleWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_ConsoleWidget()
        self.ui.setupUi(self)

        # initialize console actions widget
        self.ui.console_actions = ConsoleActionsWidget(self)
        self.ui.action_view.layout().insertWidget(0, self.ui.console_actions)
        # initialize gpio actions widget
        self.ui.gpio_actions = ConsoleGPIOActionsWidget(self)
        self.ui.action_view.layout().insertWidget(1, self.ui.gpio_actions)
        # initialize wireless actions widget
        self.ui.wireless_actions = ConsoleWirelessActionsWidget(self)
        self.ui.action_view.layout().insertWidget(2, self.ui.wireless_actions)

        # save and override output keypress event
        self.ui.output._keyPressEvent = self.ui.output.keyPressEvent
        self.ui.output.keyPressEvent = self.redirectInput

        # connect input return to 'send' button click
        self.ui.input.returnPressed.connect(self.ui.button_send.animateClick)
        # connect 'send' button to write to serial
        self.ui.button_send.clicked.connect(self.writeToSerial)
        # connect 'clear' button to clear console output
        self.ui.button_clear.clicked.connect(self.ui.output.clear)

        # add tab to window tab view
        self.window().ui.tab_view.addTab(self, 'Console')

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

    def redirectInput(self, event):
        # send event to output if modified
        if event.modifiers():
            return self.ui.output._keyPressEvent(event)
        # set focus to input and select all for overwrite
        self.ui.input.setFocus(True)
        self.ui.input.selectAll()
        # send event to input
        self.ui.input.keyPressEvent(event)

    def writeToConsole(self, data):
        # get output widget
        output = self.ui.output
        # append text to console output
        output.appendPlainText(data)
        # TODO: if 'scroll on output' preference
        # get console cursor
        cursor = output.textCursor()
        # move cursor to end position
        cursor.movePosition(QtGui.QTextCursor.End)
        # set console cursor
        output.setTextCursor(cursor)
        # ensure console cursor is visible
        output.ensureCursorVisible()

    def writeToSerial(self):
        # write console input to serial
        self.window().app.serialWrite(self.ui.input.text())
        # select current input to allow for overwrite
        self.ui.input.selectAll()









class LogWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_LogWidget()
        self.ui.setupUi(self)

        # connect 'close' button to close log tab
        self.ui.button_close.clicked.connect(self.hide)
        # connect 'save' button to log save dialog
        self.ui.button_save.clicked.connect(self.showSaveDialog)

        # add log tab to window tab view
        self.window().ui.tab_view.addTab(self, 'Log')

    def show(self):
        # insert log tab into tab view at index 1 (after console)
        self.window().ui.tab_view.insertTab(1, self, 'Log')
        # set tab view index to newly inserted log tab
        self.window().ui.tab_view.setCurrentIndex(1)

    def hide(self):
        # remove log tab at index 1 (after console)
        self.window().ui.tab_view.removeTab(1)
        # set tab view to console index since log tab is gone
        self.window().ui.tab_view.setCurrentIndex(0)

    def showSaveDialog(self):
        path = os.path.expanduser('~')
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save Log File', path, '.txt')
        if not path: return
        with open(path, 'wb') as f:
            f.write('TODO: log data')








class FileWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_FileWidget()
        self.ui.setupUi(self)

        # set syntax highlighter
        self.highlighter = QSyntaxHighlighter(self.ui.input.document())

        self.ui.input._keyPressEvent = self.ui.input.keyPressEvent
        self.ui.input.keyPressEvent = self.inputKeyPressEvent

        # connect 'close' button to file close
        self.ui.button_close.clicked.connect(self.closeFile)
        # connect 'save' button to file save dialog
        self.ui.button_save.clicked.connect(self.showSaveDialog)

    def inputKeyPressEvent(self, event):
        self.ui.input._keyPressEvent(event)

        # ignore modifiers
        if event.modifiers(): return

        # file created
        if not self.ui.button_close.isEnabled():
            self.ui.button_close.setEnabled(True)
            self.ui.button_save.setEnabled(True)
            self.window().ui.file_tree.createFile()
            return

        # file changed
        tabs = self.window().ui.tab_view
        index = tabs.indexOf(self)
        if not str(tabs.tabText(index)).startswith('*'):
            tabs.setTabText(index, '*' + tabs.tabText(index))
        self.ui.button_save.setEnabled(True)

    def closeFile(self):
        tabs = self.window().ui.tab_view
        index = tabs.indexOf(self)

        if not self.ui.button_save.isEnabled():
            tabs.removeTab(index)
            return

        file_name = tabs.tabText(index)[1:]
        confirm = QtGui.QMessageBox().question(self, 'Save Changes', "Save changes to %s before closing?" % file_name,
            QtGui.QMessageBox.Discard, QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Save)

        if confirm == QtGui.QMessageBox.Discard:
            tabs.removeTab(index)
        elif confirm == QtGui.QMessageBox.Save:
            self.showSaveDialog()

    def showSaveDialog(self):
        path = os.path.expanduser('~')
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', path, '.lua')

        if not path: return

        with open(path, 'wb') as f:
            f.write(str(self.ui.input.toPlainText()).strip() + '\r\n')

        file_name = os.path.basename(str(path))
        tabs = self.window().ui.tab_view
        tabs.setTabText(tabs.indexOf(self), file_name)
        self.ui.button_save.setEnabled(False)











class FileTreeWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_FileTreeWidget()
        self.ui.setupUi(self)

        # add widget to window file tree view
        self.window().ui.file_tree_view.addWidget(self)

    def show(self):
        # show widget view
        QtGui.QWidget.show(self)
        # defer list files call until after view has been displayed
        QtCore.QTimer.singleShot(1, self.listFiles)

    def toggleView(self, display):
        # show or hide widget view
        self.show() if display else self.hide()

    def listFiles(self):
        self.window().app.serialWrite("""print("FILES:") for k, v in pairs(file.list()) do print("name:"..k..", size:"..v) end""")

    def createFile(self):
        # TODO: move this
        # add new file widget to tab view
        self.window().ui.tab_view.addTab(FileWidget(self.window().ui.tab_view), 'New File')
