#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import time

from PyQt4 import QtGui

from lua_loader.widget.Log import LogWidget
from lua_loader.widget.File import FileWidget
from lua_loader.widget.Console import ConsoleWidget
from lua_loader.widget.FileTree import FileTreeWidget

from lua_loader.ui.MainWindow import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self, app, *args, **kwargs):
        # initialize window
        QtGui.QMainWindow.__init__(self, *args, **kwargs)

        # set app instance
        self.app = app

        # initialize user interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set app version in window title
        self.setWindowTitle(self.windowTitle() + ' ' + app.version)

        # initialize file tree widget
        self.ui.file_tree = FileTreeWidget(self)
        # initialize console tab widget
        self.ui.console_tab = ConsoleWidget(self)
        # initialize log tab widget
        self.ui.log_tab = LogWidget(self)

        # connect Menu -> View Actions to toggle action view
        self.ui.menu_view_actions.triggered.connect(self.ui.console_tab.toggleActionView)
        # connect Menu -> View Files to toggle file view
        self.ui.menu_view_files.triggered.connect(self.ui.file_tree.toggle)
        # connect Menu -> View Log to toggle log tab
        self.ui.menu_view_log.triggered.connect(self.ui.log_tab.show)

        # connect to app connected signal
        self.app.serial.signals.connected.connect(self.onConnect)

        # show new file tab by default
        self.createFile()

    def createFile(self):
        self.ui.tab_view.addTab(FileWidget(self.ui.tab_view), 'New File')

    def closeEvent(self, event):
        # iterate tabs in tab view
        tabs = self.ui.tab_view
        for index in range(tabs.count()):
            # get tab widget
            widget = tabs.widget(index)
            # continue if widget is not a file
            if not type(widget) is FileWidget: continue
            # continue if file is saved
            if not widget.ui.button_save.isEnabled(): continue
            # confirm window close
            confirm = QtGui.QMessageBox().question(self,
                'Close Files', "Close before saving file changes?",
                QtGui.QMessageBox.Discard, QtGui.QMessageBox.Cancel)
            # accept event if window close confirmed
            if confirm == QtGui.QMessageBox.Discard: event.accept()
            # ignore window close event
            else: return event.ignore()
        # accept window close event by default
        event.accept()

    def onConnect(self, connected):
        # toggle Menu -> View Files option
        self.ui.menu_view_files.setEnabled(connected)
        # write connection message to console
        self.ui.console_tab.output("%s at %s" %
            ('Connected' if connected else 'Disconnected', time.ctime()) +
            ('\n>' if connected else ''))
